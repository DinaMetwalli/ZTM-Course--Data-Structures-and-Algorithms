//Find the first tweet and the Nth/last tweet..

array = [{
    tweet: 'hi',
    date: 2012
}, {
    tweet: 'my',
    date: 2014
}, {
    tweet: 'teddy',
    date: 2018
}]

// To find the first or last item, the time complexity is O(1).
// To compare each item with the date of the other the time complexity is O(n^2)
// because a nested loop is needed to iterate through all items.

// This introduces the question: how could we store this data in a better format or
// data structure to avoid a time complexity of O(n^2) when comparing items?