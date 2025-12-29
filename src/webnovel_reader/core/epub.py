from pathlib import Path
from typing import List

from ebooklib import epub

from webnovel_reader.domain.models import BookMetadata


class EpubParser:
    def parse_book(self, path: Path, book_id: str) -> BookMetadata:
        book = epub.read_epub(path)

        title = self._first_dc(book, "title")
        creators = self._all_dc(book, "creator")

        return BookMetadata(
            id=book_id,
            title=title,
            authors=creators,
            path=str(Path),
            filename=path.name,
        )

    def _first_dc(self, book: epub.EpubBook, key: str) -> str:
        values = book.get_metadata("DC", key)
        if not values:
            return ""

        value = values[0][0]
        if value is None:
            return ""

        return str(value).strip()

    def _all_dc(self, book: epub.EpubBook, key: str) -> List[str]:
        out: List[str] = []

        values = book.get_metadata("DC", key)
        for v, _attrs in values:
            if v is None:
                continue

            text = str(v).strip()
            if text:
                out.append(text)

        return out
