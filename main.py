import quick_sort
import merge_sort
import counting_sort
import selection_sort
import sort_tester

print("-"*10)
print("<quick sort>\n")
sort_tester.test(quick_sort.sort)
print("-"*10)
print("<merge sort>\n")
sort_tester.test(merge_sort.sort)
print("-"*10)
print("<count sort>\n")
sort_tester.test(counting_sort.sort)
print("-"*10)
print("<selection sort>\n")
sort_tester.test(selection_sort.sort)
