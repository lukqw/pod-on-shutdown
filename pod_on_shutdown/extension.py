import os
import uuid

from localstack.extensions.api import Extension
from localstack.sdk.pods import PodsClient

LS_ENV_VAR_AUTO_SAVE_POD = "AUTO_SAVE_POD"


class PodOnShutdown(Extension):
    name = "pod-on-shutdown"
    
    def on_platform_shutdown(self):
        fallback_random_id = f"{uuid.uuid4()}"
        pod_name = os.getenv(LS_ENV_VAR_AUTO_SAVE_POD, fallback_random_id)

        client = PodsClient()
        client.save_pod(pod_name)
