---
title: "psub(1)"
name: "psub"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psub/"
---

<h2 class="name">NAME</h2>
 

 psub - perform process substitution

<h3>Synopsis</h3>

 COMMAND1 (COMMAND2|psub [-f])

<h3>Description</h3>

 Posix shells feature a syntax that is a mix between command substitution and piping, called process substitution. It is used to send the output of a command into the calling command, much like command substitution, but with the difference that the output is not sent through commandline arguments but through a named pipe, with the filename of the named pipe sent as an argument to the calling program. The psub shellscript function, which when combined with a regular command substitution provides the same functionality. 

 If the -f or --file switch is given to psub, psub will use a regular file instead of a named pipe to communicate with the calling process. This will cause psub to be significantly slower when large amounts of data are involved, but has the advantage that the reading process can seek in the stream.

<h3>Example</h3>

 diff (sort a.txt|psub) (sort b.txt|psub) shows the difference between the sorted versions of files a.txt and b.txt. 

<h2>Index</h2>


