# markdown-table-of-content-creator
Create table of content in markdown, for any repo provided. The TOC generated is made of links to each and every directory if the repository.

### Instructions
Clone or download file to computer. Run file from command line using python.


`python CreateTOC.py --path <PATH TO REPO>`

Following are the arguments that can be passed:

`--path` specify the path to the repository for which Table of Content is to be created.


`--depth` depth level to which program will find folders recursively.


`--output` the path and file to which all the data (TOC Markdown) is stored. By default, output is stored in current directory in `README.md` file. 


`--ignore` a list of folders to be ignored while creating TOC. By default, `.git` folder in included in ignored list.


`--similar` flag to set the directory of output file as same as that of the path provided. The output will be saved in `README.md` file. This flag Overrides `--output` argument.


For more details, run script with `-h` or `--help` flag.


`python CreateTOC.py -h`


### Example
1. [Heading 1](Heading%201)
    1. [Heading 1.1](Heading%201/Heading%201.1)
    1. [Heading 1.2](Heading%201/Heading%201.2)
1. [Heading 2](Heading%202)
    1. [Heading 2.1](Heading%202/Heading%202.1)
    1. [Heading 2.2](Heading%202/Heading%202.2)
    1. [Heading 2.3](Heading%202/Heading%202.3)
1. [Heading 3](Heading%203)
1. [Heading 4](Heading%204)
    1. [Heading 4.1](Heading%204/Heading%204.1)


Similarly another example is I have used this in [My Data-Structures Repository](https://github.com/InfiniteLoopify/data-structures) in `README.md`
