from quant_risk_metrics.config import load_settings
from quant_risk_metrics.logging_utils import get_logger

def main() -> None:
    cfg = load_settings()
    log = get_logger(__name__, cfg["logging"]["level"])
    log.info("Starting quant-risk-metrics")
    log.info("Done")



if __name__ == "__main__":
    main()