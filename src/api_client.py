import logging
import os
from typing import Any

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

ACME_API_BASE_URL = os.environ.get(
    "ACME_API_BASE_URL", "https://api.acme-internal.net"
)


class AcmeAPIClient:
    """HTTP client for the Acme internal REST API."""

    def __init__(self, timeout: int = 30):
        token = os.environ.get("ACME_API_TOKEN")
        if not token:
            raise EnvironmentError(
                "ACME_API_TOKEN environment variable is not set. "
                "See .env.example for configuration."
            )
        self.base_url = ACME_API_BASE_URL
        self.token = token
        self.timeout = timeout
        self._client = httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {self.token}"},
            timeout=self.timeout,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def get_customers(self, page: int = 1, page_size: int = 500) -> dict[str, Any]:
        response = self._client.get(
            "/v2/customers",
            params={"page": page, "page_size": page_size},
        )
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
