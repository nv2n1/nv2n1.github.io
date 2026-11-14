---
title: "begin(1)"
name: "begin"
section: "1"
letter: "b"
url: "/docs/linux/man/1-begin/"
---

<h2 class="name">NAME</h2>
 

 begin - start a new block of code

<h3>Synopsis</h3>

 begin; [COMMANDS...;] end

<h3>Description</h3>

 The begin builtin is used to create a new block of code. The block is unconditionally executed. begin; ...; end is equivalent to if true; ...; end. The begin command is used to group any number of commands into a block. The reason for doing so is usually either to introduce a new variable scope, to redirect the input or output of a set of commands as a group, or to specify precedence when using the conditional commands like and. 

 The begin command does not change the current exit status.

<h3>Example</h3>

 The following code sets a number of variables inside of a block scope. Since the variables are set inside the block and have local scope, they will be automatically deleted when the block ends. 

 

 <pre>
begin
        set -l PIRATE Yarrr
        ...
end
# This will not output anything, since the PIRATE variable went out
# of scope at the end of the block
echo $PIRATE
</pre> 

 

 In the following code, all output is redirected to the file out.html. 

 

 <pre>
begin
        echo $xml_header
        echo $html_header
        if test -e $file 
                ...
        end
        ...
</pre> 

 

 

 <pre>
end &gt; out.html
</pre> 

 
&nbsp;<wbr> 

<h2>Index</h2>


