# BAD PortaOne Test Task

## Task: 
There is a file containing a large set of integers (you can download the file here: https://drive.google.com/file/d/1JVk4C5jUOGTiFM5xtuNQ8qjyPOhsvaNp/view?usp=sharing).

The challenge is to find the following six values:
    1.maximum number in the file;
    2. the minimum number in the file;
    3.median (https://goo.gl/hiCwVw);
    4. arithmetic mean (https://goo.gl/XJeAjZ);
    5.the largest sequences of consecutive numbers that increase
    6.the largest sequences of consecutive numbers that decrease

NB:
- Median: If the set of numbers has an even number of elements, then the half-sum of two adjacent values ​​should be used to determine the median. Those. for example, in an already sorted set {1, 8, 14, 19}, the median will be 11 (since 0.5 * (8 + 14) = 11).
- A sequence of numbers is the order of numbers in a file following one after another. Even randomly generated datasets can have quite long sequences. For example, an ascending sequence might look like this: -4390, -503, 3, 16, 5032

You are practically unlimited in the choice of the method and method of solving the problem. This means that you can use any means, methods, approaches (except those indicated below). Those. you can, for example, write a program in any programming language you know. Or you can use existing programs / utilities. Obviously, you can use sets of statistic out-of-the-box classes / functions / libraries, but this is not the preferred option.

There are only the following restrictions that should be taken into account when choosing a method for solving the problem:

Limitation # 1:
Anyone should be able to use your method. This means, for example, that if you used your own program to solve a problem, then any other person should be able to compile / run it, etc .; if you used third-party programs / utilities, then anyone should be able to install and use them too; also, anyone can take a completely different file with a different set of integers and find all six specified values);
    
Limitation # 2:
When solving the problem, you cannot use illegal software (proprietary software that has been hacked, pirated copies of the software, etc.). Also, if you borrowed the idea of ​​a solution, software or source code (or some part of it) from a friend / colleague / on the Internet / anywhere, then mention the source.

Additional condition # 1:
The proposed solution method should find all six values ​​from a given file in no more than 90 seconds. (This condition is optional, but it will be a significant plus if your solution satisfies it).

Additional condition # 2:
The file does not have to be manually modified before use. All invalid values ​​in the file must be excluded.

## Implementation: 
The problem was solved using python without using built-in functions to find the desired values. Using flask, a simple user interface was created for finding the desired values from any file using my script, the project was deployed using the Amazon EC2 service. Additional time for solving requires uploading the file itself to the server. Project: http://ec2-54-210-173-196.compute-1.amazonaws.com/ (Not relevant anymore)

To run locally, do the usual:

#. Install dependencies::

    sudo pip install flask
    
#. Run::

    python3 ./main.py
     
