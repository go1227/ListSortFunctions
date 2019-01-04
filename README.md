# ListSortFunctions

Program description:
Compilation of sorting algorithms and demonstration on which one is more effective for a random list of numbers

Conclusion:
If the list of numbers is short, all sorting mechanisms provide similar execution speeds.
However, once the list of numbers starts to grow, the execution times immediately begin to differentiate drastically.
In all tests performed, the built-in function ".sort()" provided the best execution time.


Execution example:
__________________

This program will demonstrate which list sorting method is the most efficient using a random list of numbers.
Please enter the number of elements you would like to have in your list [100-50000]:
10000

InsertSort() --- Execution time: 4.573638916015625 seconds

BubbleSort() --- Execution time: 8.212809085845947 seconds

SelectionSort() --- Execution time: 3.258553981781006 seconds

ShellSort() --- Execution time: 0.05242490768432617 seconds

MergesSort() --- Execution time: 0.04680490493774414 seconds

QuickSort() --- Execution time: 0.021754980087280273 seconds

list.sort() (python built-in function) --- Execution time: 0.0010759830474853516 seconds

Process finished with exit code 0
