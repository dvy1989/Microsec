# Question 1

## How to use this script

It is enough to run the following script. Before running the script it should be given appropriate rights.

```bash
# Gives rights to script
chmod u+x script.sh
# Runs script
./script.sh URL WORD
```

The script takes two parameters: *URL*, which is a URL of a starting page, and *WORD*, which is a word to search. It outputs all found word occurrences.

## Assumptions, limitations and future work

The limitation of this script is that it can not read dynamically rendered pages as they are rendered by browser.
The script is based on wget and, therefore, returns only a result for the provided request (HTML page from given URL). It does not execute associated JS. So it is assumed, that the
script is used for more or less static pages.
The script still requires a major improvement. The problem is that it does not keep track of visited pages and, therefore, infinite loops are possible.
E.g., when page1 refers to page2 and page2 refers to page1.


