from fastapi import Request


def get_api_key(request: Request) -> str:
    # intentar usar valor ya validado
    api_key = getattr(request.state, "api_client", None)

    if api_key:
        return api_key

    # fallback al header (por seguridad)
    api_key = request.headers.get("x-api-key")

    if api_key:
        return api_key

    return "anonymous"
