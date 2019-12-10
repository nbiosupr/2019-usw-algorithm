import quick_sort
import merge_sort
import sort_tester

print("-"*10)
print("<quick sort>\n")
sort_tester.test(quick_sort.sort)

print("-"*10)
print("<merge sort>\n")
sort_tester.test(merge_sort.sort)
