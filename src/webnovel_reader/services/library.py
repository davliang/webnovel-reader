import re
from pathlib import Path
from typing import Dict, List

from webnovel_reader.core.epub import EpubParser
from webnovel_reader.domain.models import BookMetadata


class LibraryService:
    def __init__(self, novels_dir: Path):
        self.novels_dir: Path = novels_dir
        self.parser = EpubParser()
        self.books: Dict[str, BookMetadata] = {}

    def _slugify(self, text: str) -> str:
        return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

    def scan(self) -> None:
        self.novels_dir.mkdir(parents=True, exist_ok=True)

        found: Dict[str, BookMetadata] = {}
        for epub_path in self.novels_dir.glob("*.epub"):
            book_id = self._slugify(epub_path.stem)
            try:
                found[book_id] = self.parser.parse_book(epub_path, book_id)
            except Exception:
                # TODO: Log and move on.
                continue

        self.books = found

    def get_all_books(self) -> List[BookMetadata]:
        self.scan()
        return sorted(self.books.values(), key=lambda b: b.title)
