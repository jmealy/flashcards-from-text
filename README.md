# flashcards-from-text
Given a text in Spanish, generate flashcards from the most difficult words. This can be used for memorising difficult words in an article before reading it. It can also be used for movies (given the subtitles in the original language) or for the next chapter of a book.

## Install Dependencies
`pip install -r requirements.txt`

## Usage
`python get_flashcards_from_text.py`

Change the contents of `words.txt` to any Spanish text you wand to generate flashcards from.

Change the value  of `FREQUENCY` in the script to suit your level. A higher value of `FREQUENCY` will include easier words.

## Results
Words will be saved as CSV along with their translations in `target_words.csv`
You can then import this to a flashcard app like [anki](https://apps.ankiweb.net/)