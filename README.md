This code will take in a stream of key/value pairs, where the key is a number and the value is a letter,
and print the letters in order from the value with a key of 1 to the end of the stream.
The assumption is made that all intervening numbers occur and that no smaller numbers occur.

Our solution is to provide a container for key/value pairs which come too early, and then check that container each time we find the key/value pair which we are
currently looking for. So all pairs are stored until hitting the key of 1, then the container is searched for a key of 2, and, if successful, 3, 4, etc.,
until the container is found to lack the sought key. The function yields the value of the pair upon finding the sought pair, allowing it to be printed.

The code also shows unittesting at work.