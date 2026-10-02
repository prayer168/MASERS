from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections.abc import Iterator
import json

@dataclass
class Response:
    text: str
    tokens_in: int
    tokens_out: int
    model: str

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, role: str, context: dict) -> Response: ...
    @abstractmethod
    def stream(self, role: str, context: dict) -> Iterator[str]: ...
    @abstractmethod
    def estimate_tokens(self, text: str) -> int: ...
    @abstractmethod
    def health_check(self) -> bool: ...

class MockProvider(LLMProvider):
    """Deterministic protocol simulation; does not claim to write or test software."""
    def generate(self, role, context):
        text = json.dumps({"summary": f"Mock {role}: {context['title']}",
                           "completed": [f"Simulated {role} output"],
                           "known_issues": ["Mock mode: no real implementation or code verification"],
                           "tests": {"mode": "simulation"}}, ensure_ascii=False)
        return Response(text, self.estimate_tokens(json.dumps(context)), self.estimate_tokens(text), "mock")

    def stream(self, role, context):
        yield self.generate(role, context).text

    def estimate_tokens(self, text):
        return max(1, len(text.encode("utf-8")))

    def health_check(self):
        return True
