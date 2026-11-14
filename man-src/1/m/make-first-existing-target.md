---
title: "make-first-existing-target(1)"
name: "make-first-existing-target"
section: "1"
letter: "m"
url: "/docs/linux/man/1-make-first-existing-target/"
---

<h2 class="name">NAME</h2>
 

 make-first-existing-target - runs make on one of several targets 

<h2>SYNOPSIS</h2>

 make-first-existing-target [-c cmd] target1 [target2 ...] --- [make-options]

<h2>DESCRIPTION</h2>

 The design of <i><a HREF="/docs/linux/man/1-make/">make</a></i>(1) causes difficulty when you know that a Makefile probably has one of several standardized target names, and want build machinery to run exactly one of them, propagating any errors. <i><a HREF="/docs/linux/man/1-make/">make</a></i>(1) will exit 2 if a target does not exist, but an existing target may also exit 2 due to some other failure. Makefiles cannot be reliably parsed to find targets by anything less Turing-complete than make, and make itself does not provide a way to enumerate the targets in a Makefile. It may not even be possible to enumerate the targets in a Makefile without executing part of it. (Proof of this is left as an exercise for the reader.) 

 This program avoids the problems described above, by attempting to call each specified target in turn, until it observes make actually doing something for one of them.

<h2>OPTIONS</h2>

<dl>
<dt>-c cmd
<dd> This can be used to specify the make command to run. Default is ``make''.</dl>

<h2>EXIT STATUS</h2>

 The exit status is 0 if at least one target existed and was successfully run, and nonzero otherwise.

<h2>AUTHOR</h2>

 Joey Hess &lt;joey [at] kitenet.net&gt;

<h2>LICENSE</h2>

 Same as <font SIZE="-1">GNU</font> make.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-make/">make</a></i>(1) 

<h2>Index</h2>


