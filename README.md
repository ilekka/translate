A small script which uses the [DeepL API](https://www.deepl.com/docs-api/) to translate text (e.g. incoming e-mails) from a foreign language to English in a tmux terminal window.

**Usage:** Place the files translate.py and translate.sh in ~/.translate, and add the following line to .tmux.conf:

```
bind-key -T copy-mode-vi 'd' run-shell "tmux send-keys -X copy-pipe-and-cancel \"xsel -ib && xsel -ob > ~/.translate/translate_in.txt\"; ~/.translate/translate.sh; less ~/.translate/translate_out.txt; true"
```

Then visually selecting a block of text and pressing 'd' translates the text to English and displays the result in the terminal window.
