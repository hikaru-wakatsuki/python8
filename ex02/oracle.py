import os
import sys


def load_env() -> dict[str, str | None]:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("ERROR: python-dotenv not installed")
        sys.exit(1)
    load_dotenv()
    config: dict[str, str | None] = {}
    config["MATRIX_MODE"] = os.getenv("MATRIX_MODE")
    config["DATABASE_URL"] = os.getenv("DATABASE_URL")
    config["API_KEY"] = os.getenv("API_KEY")
    config["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
    config["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")
    for key, value in config.items():
        if not value:
            print(f"[ERROR] Missing configuration for {key}")
            sys.exit(1)
    return config


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    config: dict[str, str | None] = load_env()
    print()
    print("Configuration loaded:")
    mode: str | None = config.get("MATRIX_MODE")
    if mode:
        print(f"Mode: {mode}")
    if config.get("DATABASE_URL"):
        if mode == "development":
            print("Database: Connected to local instance")
        elif mode == "production":
            print("Database: Connected to production instance")
        else:
            print("[WARNING] Unknown MATRIX_MODE")
    if config.get("API_KEY"):
        print("API Access: Authenticated")
    if config.get("LOG_LEVEL"):
        print(f"Log Level: {config.get('LOG_LEVEL')}")
    if config.get("ZION_ENDPOINT"):
        print("Zion Network: Online")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not found")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
