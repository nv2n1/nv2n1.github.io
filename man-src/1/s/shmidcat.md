---
title: "shmidcat(1)"
name: "shmidcat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shmidcat/"
---

<h2>NAME</h2>

 

 shmidcat - Copies stdin/file to a shared memory block for <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1)

<h2>SYNTAX</h2>

 

 shmidcat [<i>VCDFILE</i>]

<h2>DESCRIPTION</h2>

 

 Copies either the file specified at the command line or stdin (if no file specified) line by line to a shared memory block. stdout will contain a shared memory ID which should be passed on to <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1).

<h2>EXAMPLES</h2>

 

 To run this program the standard way type:
<dl>
<dt>cat whatever.vcd | shmidcat
<dd> The shared memory ID is emitted to stdout.
<dt>shmidcat whatever.vcd | gtkwave -v -I whatever.sav
<dd> GTKWave directly grabs the ID from stdin.</dl>

<h2>LIMITATIONS</h2>

 This program is mainly for illustrative and testing purposes only. Its primary use is for people who wish to write interactive VCD dumpers for <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) as its source code may be examined, particularly the emit_string() function. It can also be used to test if an existing VCD file will load properly in interactive mode. Note that it can also be used to redirect VCD files which are written into a pipe to <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) in a non-blocking fashion. 

<h2>AUTHORS</h2>

 

 Anthony Bybell &lt;bybell [at] rocketmail.com&gt;

<h2>SEE ALSO</h2>

 

 <i><a HREF="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) 

<h2>Index</h2>


