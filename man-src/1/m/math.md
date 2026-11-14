---
title: "math(1)"
name: "math"
section: "1"
letter: "m"
url: "/docs/linux/man/1-math/"
---

<h2 class="name">NAME</h2>
 

 math - Perform mathematics calculations

<h3>Synopsis</h3>

 math EXPRESSION

<h3>Description</h3>

 math is used to perform mathematical calculations. It is only a very thin wrapper for the bc program, that makes it possible to specify an expression from the command line without using non-standard extensions or a pipeline. Simply use a command like math 1+1. 

 For a description of the syntax supported by math, see the manual for the bc program. Keep in mind that parameter expansion takes place on any expressions before they are evaluated. This can be very useful in order to perform calculations involving environment variables or the output of command substitutions, but it also means that parenthesis have to be escaped. 

<h2>Index</h2>


