from collections import Counter
from pathlib import Path

BOOK_FOLDER = Path("books")


def main() -> None:
    for book_path in BOOK_FOLDER.glob("*.txt"):
        book_text = load_book(book_path)
        word_count = count_words(book_text)
        letters_count = count_letters(book_text)
        print_report(book_path.name, word_count, letters_count)


def load_book(file: Path) -> str:
    with file.open() as f:
        return f.read()


def count_words(text: str) -> int:
    return len(text.split())


def count_letters(text: str) -> dict[str, int]:
    return Counter(text.lower())


def print_report(
    book_name: str, word_count: int, letters_count: dict[str, int]
) -> None:
    print(f"--- Begin report of '{book_name}' ---")
    print(f"{word_count} words found in the document")
    print()

    for letter, count in sorted(
        letters_count.items(), key=lambda x: x[1], reverse=True
    ):
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")
    print()
    print()


main()
