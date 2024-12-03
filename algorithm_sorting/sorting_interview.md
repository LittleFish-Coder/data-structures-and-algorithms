# Sorting Interview

## Question1
Sort 10 schools around your house by distance:
- Answer: Insertion sort
- Explain: Fast on small data sets, space complexity is O(1)


## Question2
eBay sorts listings by the current Bid amount:
- Answer: Radix or counting sort
- Explain: Because bid amounts are typically within a fixed range, radix or counting sort can efficiently handle the sorting, outperforming O(n log n) time complexity.

## Question3
Sport scores on ESPN
- Answer: Quick sort
- Explain: Quick sort is a good choice for sorting sports scores because it is efficient on average and has a time complexity of O(n log n).

## Question4
Massive database (can't fit all into memory) needs to sort through past year's user data
- Answer: Merge sort
- Explain: Merge sort is a good choice for sorting a massive database because it is stable and has a time complexity of O(n log n).

## Question5
Almost sorted Udemy review data needs to update and add 2 new reviews
- Answer: Insertion sort
- Explain: Although this data might be huge and maybe I have a lot of reviews. I'm assuming that most of the previous data is already sorted. And all I'm doing is adding two new reviews to this data. Insertion sort for pre ordered lists is going to work better than any other type of sorting.

## Question6
Temperature Records for the past 50 years in Canada
- Answer: Radix or counting sort
- Explain: Because temperature records are typically within a fixed range, radix or counting sort can efficiently handle the sorting, outperforming O(n log n) time complexity.

## Question7
Large user name database needs to be sorted. Data is very random.
- Answer: Merge sort or quick sort

## Question8
You want to teach sorting for the first time
- Answer: Bubble sort, selection sort