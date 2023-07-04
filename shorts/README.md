# Shorts: Very very small functions

Here are the implementations of various algorithms using very very small
functions. The main criterion for getting a function into this section is the size of its code.
Moreover, the score goes not even on strings, but on characters.
Conditionally, you can focus on $256 = 2 ^8$ characters.
The next goal is 160 characters, i.e. the length of a standard sms.
You can go even further and try to fit the entire function into $128=2^7$ characters.
Well, especially stubborn ones will be able to cram all the functionality into 100 characters.

**Conditions:**

1. The entire length of the function is taken into account from the first character in its declaration to the last character in its return value.

2. If an import is used in the function, its length is summed with the length of the imported code. This condition makes imports very unprofitable. But all the more interesting.

3. The function must pass all available tests.

4. The readability and clarity of the code, as well as performance and security when the previous conditions are met, will of course suffer. This is the case when you can neglect to break some of the commandments formulated by Tim Peters. However, in all other cases (especially sections of this project), we strongly recommend that you still follow Zen of Python.

The programs in this section will most likely not be suitable for real use. But writing them motivates you to study the most hidden corners of documentation. Trying to reduce the length of the code by a couple of characters can significantly increase the level of skill.
