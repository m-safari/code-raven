from langchain_openai import ChatOpenAI

from ctt.config import settings


def get_llm() -> ChatOpenAI:
    """Both Ollama and OpenRouter expose OpenAI-compatible APIs."""
    if settings.llm_provider == "openrouter":
        return ChatOpenAI(
            model=settings.llm_model,
            base_url=settings.openrouter_base_url,
            api_key=settings.openrouter_api_key,
        )
    return ChatOpenAI(
        model=settings.llm_model, base_url=settings.ollama_base_url, api_key="ollama"
    )
