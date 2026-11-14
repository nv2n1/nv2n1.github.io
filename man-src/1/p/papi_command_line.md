---
title: "papi_command_line(1)"
name: "papi_command_line"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_command_line/"
---

<h2 class="name">NAME</h2>
 

 papi_command_line - executes PAPI preset or native events from the command line. 

<h2>Synopsis</h2>

 

 papi_command_line &lt; event &gt; &lt; event &gt; ...

<h2>Description</h2>

 

 papi_command_line is a PAPI utility program that adds named events from the command line to a PAPI EventSet and does some work with that EventSet. This serves as a handy way to see if events can be counted together, and if they give reasonable results for known work.

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -u Display output values as unsigned integers
<dt>&bull;
<dd> -x Display output values as hexadecimal
<dt>&bull;
<dd> -h Display help information about this utility.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


