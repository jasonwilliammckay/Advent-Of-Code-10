# Advent-Of-Code-10

Done in python.

No testing yet, but it's pretty short.

Parts 1 and 2 of this problem are just more iterations: the size of the data set grows exponentially (~36% larger per iteration) so starts to really slow down after 40 iterations. I use list .appends ending with a .join to minimize the number of string operations, which speeds it up some.
