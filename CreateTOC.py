import os
import re
import argparse


class createTOC:
    def __init__(self, path, maxdepth, ignore=[]):
        self.markdown = ""
        self.maxdepth = maxdepth
        self.ignore = ignore
        self.dirlist = self.__walkdir(path, self.maxdepth)

    # walk directory recursively till depth and create markdown TOC
    def __walkdir(self, top, depth, ):
        dirs, nondirs = [], []
        # get folders in current directory
        for name in os.listdir(top):
            (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
            if dirs and dirs[-1] in self.ignore:
                dirs.pop()
        yield top, dirs, nondirs
        dirs.sort()
        # while depth is remaining, add info to markdown and traverse recursively
        if depth > 0:
            relative = self.getRelativeParent(top, depth)
            for name in dirs:
                spaceRemove = "".join([relative, name])
                spaceRemove = spaceRemove.replace(' ', '%20')
                join = f"{'    '*(self.maxdepth-depth)}1. [{name}]({spaceRemove})\n"
                self.markdown = "".join([self.markdown, join])
                for x in self.__walkdir(os.path.join(top, name), depth-1):
                    yield x

    # get parents string to convert to links in TOC
    def getRelativeParent(self, top, depth):
        relativeParent = []
        relativeParentStr = ""
        topSplit = top.split("/")
        for index, level in enumerate(range(depth, self.maxdepth)):
            tempIndex = -index-1
            relativeParent.append(topSplit[tempIndex])
        if relativeParent:
            relativeParent.reverse()
            relativeParentStr = "/".join(relativeParent)
            relativeParentStr += "/"
        return relativeParentStr


def main():
    # create argument parser with types (path, depth, output, ignore, verbose)
    desciption = "Create Table of Content in Markdown Format for Git Repository"
    parser = argparse.ArgumentParser(description=desciption)
    parser.add_argument("-p", "--path", help="path to git repo", required=True)
    parser.add_argument(
        "-d", "--depth", help="recursive depth from path to seek")
    parser.add_argument(
        "-o", "--output", help="path to file to which output is to be written")
    parser.add_argument(
        "-i", "--ignore", help="folder names to ignore white seeking", nargs="*")
    parser.add_argument(
        "-s", "--similar", help="output file is generated in same directory as the path", action="store_true")
    parser.add_argument(
        "-v", "--verbose", help="print additional information", action="store_true")
    args = parser.parse_args()

    # default argument values
    path = ""
    depth = 1
    output = "README.md"
    ignore = [".git"]


    # update arguments if passed
    path = args.path
    if args.depth:
        depth = int(args.depth)
    if args.output:
        output = args.output
    if args.ignore:
        ignore = args.ignore
    
    # output file is generated in same directory as the path
    if args.similar:
        if not path == "":
            seperator = "" if path[-1] == "/" else "/"
            output = seperator.join([path, output])

    # generate TOC in markdown
    toc = createTOC(path, depth, ignore=ignore)
    for x in toc.dirlist:
        pass

    if args.verbose:
        print(toc.markdown)

    # write output to file
    f = open(output, "w")
    f.write(toc.markdown)
    f.close()


if __name__ == "__main__":
    main()
