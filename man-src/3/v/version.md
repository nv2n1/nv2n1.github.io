---
title: "version(3)"
name: "version"
section: "3"
letter: "v"
url: "/docs/linux/man/3-version/"
---

XMLTV::Version - Adds a --version argument to XMLTV grabbers 

<h2>Description</h2>Add a --version argument to your program, eg 

 <pre> use XMLTV::Version '$Id: Version.pm,v 1.3 2010/04/24 12:28:22 crispygoth Exp $';</pre>If a --version parameter is supplied on the command-line, it will be caught already by the ``use'' statement, a message will be printed to <font SIZE="-1">STDOUT</font> and the program will exit. 

 It is best to put the use XMLTV::Version statement before other module imports, so that even if they fail --version will still work.
<h2>See Also</h2>XMLTV::Options
