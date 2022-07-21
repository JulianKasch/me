TODO: Reflect on what you learned this week and what is still unclear.
just had to remember the purpose of the 'try, except' stuff for get_a_word_of_length_n.
for list_of_words_of_lengths the most important thing was assigning the value given by the get_a_word_of_length_n function that was refactored in because it doesn't seem to do much on its own.
two main issues with getting abba to work, I unexpectantly couldn't split a boring 4 letter string with .split(), and secondly it was expecting an unneeded 'guard' in apply rules so after removing/replacing these issues it worked.
Suprisingly I was too dumbfounded by the process of how the koch and square_koch function was supposed to be recursively self defining itself to notice that I was calling koch in square_koch and not square_koch.