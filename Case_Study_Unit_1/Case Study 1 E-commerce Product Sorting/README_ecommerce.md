# Case Study: E-commerce Product Sorting Using Divide and Conquer

## Aim
To sort e-commerce products by price using the **Divide and Conquer** strategy.

## Strategy Used: Merge Sort
Merge Sort divides the product list into smaller lists, sorts those lists, and merges them into one sorted list.

### Steps
1. **Divide:** Split the list into two halves.
2. **Conquer:** Recursively sort each half.
3. **Combine:** Merge the sorted halves in ascending order of price.

## Example
Input products and prices:
- Headphones — Rs. 1499
- Keyboard — Rs. 899
- Smart Watch — Rs. 2499
- USB Cable — Rs. 199
- Mouse — Rs. 599

Expected order:
1. USB Cable — Rs. 199
2. Mouse — Rs. 599
3. Keyboard — Rs. 899
4. Headphones — Rs. 1499
5. Smart Watch — Rs. 2499

## How to Run
Requires Python 3.

```bash
python ecommerce_sorting.py
```

## Time and Space Complexity
- **Time complexity:** O(n log n) in the best, average, and worst cases.
- **Auxiliary space:** O(n) for merging.
- `n` is the number of products.

## Conclusion
Merge Sort efficiently sorts a product list by price. Divide and Conquer makes the task manageable by sorting smaller parts and combining their results.
