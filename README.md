# To for run proyect
`$ python GrammarAnalyser.py`

# To analyze a grammar follow the following steps:


## The grammar must be free of context and is written in the following format:

```
S -> A | B
A -> to A | epsilon
B -> b B | epsilon
```

* Use '->' to indicate a production, and '|' to indicate multiple pruducciones with the same header.
* Use 'epsilon' to indicate the special terminal symbol of the graph.
* All the symbols that are the head of any production will be the Non-Terminals, the rest will be considered as Terminals. Use, if possible, only letters in the defending Non-Terminals.
* Between two contiguous symbols always leave at least one space.
* You will be notified if the grammar is not in the appropriate format.

## If you do not want to analyze any chain, continue with "Quick Analysis" (F9).
* You will see the results in the "Results" tab.

## If you want to analyze some chains as well, continue with "Analyze" (F5).
* Next you must enter the desired chains, you must leave at least one space between two contiguous tokens.
* Then you will see the results in the "Results" tab.

## At the end, you can also save the grammar in text format, for future use.
* In the same way, you can load a grammar in text format, in which case you will have to carry out the
steps from the beginning.

## THANK YOU FOR USING GRAMMAR ANALYSER!
