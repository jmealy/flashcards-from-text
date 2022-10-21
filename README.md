# flashcards-from-text
Given a text in Spanish, generate flashcards from the most difficult words. This can be used for memorising difficult words in the episode of a TV show before watching it, or similarly for the next chapter of a book.

## Install Dependencies
`pip install -r requirements.txt`

## Usage
`python get_flashcards_from_text.py`

Change the contents of `words.txt` to any Spanish text you wand to generate flashcards from.

Change the value  of `FREQUENCY` in the script to suit your level. A higher value of `FREQUENCY` will include easier words.

Words will be saved as CSV along with their translations in `target_words.csv`
