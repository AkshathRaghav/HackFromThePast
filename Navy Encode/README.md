# Navy Encode 

The time was 1943. You and your friend Rukhmini are in a British Navy ship when a member of the navy approaches you with a curious looking box. She recognizes it as an enigma box, which is used by the Germans to code and encrypt messages.
This particular contraption is a simple alphabet shift encoding system where each alphabet gets promoted by a certain value. Your objective is to decode the encrypted text provided to you. Assume that all characters other than spaces are encrypted. All test cases use different keys, which involve simple alphabet promoting or demoting. Your objective is to come up with a solution to decode the encrypted message, no matter the key used.

**Note** : To limit the words which can be accessed on Hackerrank, we have compiled a list of words that are required for passing the test cases. Click [here]() to download the list. Consider this list to be your English dictionary and copy paste the same into the buffer while testing the code out!

**Input Format**

`str`, which contains the encoded string

Assume that all characters in input `str` other than spaces are encrypted. Also assume that all characters of `str` are in lowercase.

**Constraints**

0 < len(`str`) < 30

**Output Format**

At the end of the test case, your code should output the decoded string, which will be in lowercase
Returns - Decoded String

**Sample Input 0**

```
g[\f f[bh_Wag gT^X `beX g[Ta gjXagl `\ahgXf
```

**Sample Output 0**
```
this shouldnt take more than twenty minutes
```
