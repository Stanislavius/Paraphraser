Paraphraser, gets permutations for a [syntax](https://en.wikipedia.org/wiki/Parse_tree) (or concrete syntax or parse)  tree, thus creating new sentences from old ones.
For example:

![image](https://github.com/Stanislavius/Paraphraser/assets/56927835/86299cd3-1c21-46fe-b0ee-d4031fc76707)

Task is to get all paraphrases to change sentense but not change it's sense. For example in the image above we could swap Jill and Joe and meaning would not be changed.

1. Install Python 3.9
2. Install Python libraries: Flask and NLTK
3. Copy files paraphraser.py and paraphrase_api.py to scripts folder in python_path\scripts (or any folder which contains flask.exe)
4. Open command line
5. Change directory to directory which contains flask.exe, paraphraser.py and paraphrase_api.py
6. Type "flask --app paraphrase_api run"
7. There will be message like "Running on http://127.0.0.1:<port\>"
8. type "localhost:<port\>/paraphrase?tree=<tree\>&limit = <limit\> in browser

Files:
1. paraphraser.py - gets all paraphrases
2. paraphrases_api.py - creates api and send results
