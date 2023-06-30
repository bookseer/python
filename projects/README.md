# Projects

This section contains completed projects implemented in Python.

The projects collected in this section satisfy several basic principles aimed at facilitating the understanding of the source code by novice developers:

**Small size**: The source code of most of the projects presented here rarely exceeds 256 lines.
The length of most projects is much less than this indicator.
Such limitations on the size of the code will make it easier for readers to understand these programs.
There are no strict restrictions when writing each individual program, just $256 = 2^8$ is an important number for programmers.
Not by chance, [Programmer's Day] (https://en.wikipedia.org/wiki/Programmer's_Day) falls on the 256th day of the year — September 13 (September 12 in a leap year).

**Text Interface**: Most of the projects presented here implement [Text-based user interface](https://ru.wikipedia.org/wiki/Text-based_user_interface).
This approach is also deliberately chosen and allows the reader to focus on the logic of the program without being distracted by the details of the interface implementation.

**Autonomy**: Most of the projects presented here do not require installation.
All programs are enclosed in separate, self-contained Python source code files with the extension.py, for example factorial.py , which do not require any installation and configuration to run.
To get acquainted with the program, just run it, for example, like 'python factorial.py '.
Also, this approach makes it easier to easily post the source code of the program on the Internet to share it with others.
Note, however, that when developing real applications, this approach is still not recommended.
For a more convenient launch, the project description and the source code of the program are placed in the jupyter notebook.

**Minimum of third-party dependencies**: most of the projects presented here do not require the installation of third-party libraries. This principle is also intended to facilitate the launch of programs for novice developers.
Although in the real world it is better not to reinvent the wheel and use the necessary libraries so that you can focus on writing the main functionality of the application.

**Variety**: This section is constantly updated with new projects on a variety of topics.

**Testing**: Most of the projects presented here are supplemented with tests. The modules `doctest` and `pytest' are used for testing.

**Simplicity**: Most of the projects presented here were written in such a way as to be understandable even to beginners. This is probably the main principle in this section. And all the others are derived from it. However, this entails a number of limitations.
Firstly, in almost all cases, the choice between performance and code clarity was made in favor of the latter.
Secondly, many programs lack security checks and special case handling.

**English-speaking**: English is used for the design of program listings (naming variables, commenting on source code).

If any project does not meet the principles listed above, this is discussed separately.

**Attention: the programs presented in this section are of an educational, familiarization nature. It is not recommended to use them in real projects without revision. The stated bet on the simplicity of understanding the implementation, in some of the programs listed, negatively affected their performance, versatility and security.**
