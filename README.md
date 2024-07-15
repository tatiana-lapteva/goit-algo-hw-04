| Algorithm      | Complexity | Stability | Sorted Data (500), sec | Sorted Data (10 000), sec |
|----------------|------------|-----------|------------------------|---------------------------|
| merge_sort     | O(n log n) |    Yes    |   0.01168              |    0.03478                |
| insertion sort | O(n^2)     |    Yes    |   0.55224              |    2.27272                |
| sorted         | O(n log n) |    Yes    |   0.00066              |    0.00176                |
| sort           | O(n log n) |    Yes    |   0.00081              |    0.00151                |

Compared to merge sort and insertion sort, built-in functions sorted and sort (Timsort algorithm) are faster and easier to use.  

![image](https://github.com/user-attachments/assets/464a3b83-e3b9-41a9-b308-00fb11ad9f38)
