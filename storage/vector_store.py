"""Vector store wrapper for knowledge retrieval (simulation-only)."""

from utils.logger import get_logger


class VectorStore:
    """Minimal vector store wrapper.

    This is a lightweight adapter around Chroma if installed.
    """

    def __init__(self, collection_name: str = "sim-knowledge") -> None:
        self.collection_name = collection_name
        self.logger = get_logger("vector_store")
        try:
            import chromadb  # type: ignore

            self.client = chromadb.Client()
            self.collection = self.client.get_or_create_collection(collection_name)
            self.available = True
        except Exception as exc:  # pragma: no cover - optional dependency
            self.available = False
            self.logger.warning("Vector store unavailable: %s", exc)

    def add_documents(self, ids: list[str], texts: list[str]) -> None:
        """Add documents to the collection if available."""
        if not self.available:
            return
        self.collection.add(ids=ids, documents=texts)

    def query(self, query_text: str, top_k: int = 3) -> list[str]:
        """Query the collection and return matching documents."""
        if not self.available:
            return []
        results = self.collection.query(query_texts=[query_text], n_results=top_k)
        return results.get("documents", [[]])[0]
