This is a quick and dirty Python/C rolling hash implementation to generate a series of unsigned integer values given a string of text and a window size.  This conversion of strings to integer hash values allows for quick longest-common-substring identification between large sets of documents using Rabin-Karp searching.

Note that superfasthash isn't a "rollable" hash algorithm (each window is calculated independently), so there may be much more performance-appropriate algorithms for extremely long strings.

More on rolling hashes: http://en.wikipedia.org/wiki/Rolling_hash
More on Rabin Karp searching: http://en.wikipedia.org/wiki/Rabin-Karp_string_search_algorithm