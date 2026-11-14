---
title: "if(1)"
name: "if"
section: "1"
letter: "i"
url: "/docs/linux/man/1-if/"
---

<h2 class="name">NAME</h2>
 

 if - conditionally execute a command

<h3>Synopsis</h3>

 if CONDITION; COMMANDS_TRUE...; [else; COMMANDS_FALSE...;] end

<h3>Description</h3>

 if will execute the command CONDITION. If the condition's exit status is 0, the commands COMMANDS_TRUE will execute. If the exit status is not 0 and else is given, COMMANDS_FALSE will be executed. 

 In order to use the exit status of multiple commands as the condition of an if block, use begin; ...; end and the short circuit commands and and or. 

 The exit status of the last foreground command to exit can always be accessed using the $status variable.

<h3>Example</h3>

 

 <pre>
if test -f foo.txt
        echo foo.txt exists
else
        echo foo.txt does not exist
end
</pre> 

 
&nbsp;<wbr>will print foo.txt exists if the file foo.txt exists and is a regular file, otherwise it will print foo.txt does not exist.&nbsp;<wbr> 

<h2>Index</h2>


