---
title: "teachjove(1)"
name: "teachjove"
section: "1"
letter: "t"
url: "/docs/linux/man/1-teachjove/"
description: "teachjove – learn how to use the JOVE editor"
---

<h2 class="name">NAME</h2>
<p> teachjove &#8211; learn how to use the JOVE editor </p>
<h2>SYNOPSIS</h2>
<p> <code>teachjove</code> [ <code>-s</code><i>&nbsp;<wbr>sharedir</i> ]</p>
<h2>DESCRIPTION</h2>
<p> TEACHJOVE is a simple program that calls up the JOVE editor on a special file that is an interactive tutorial for the JOVE editor. Once in JOVE all you do is follow the instructions and by doing so you will learn all about JOVE! NOTE: TEACHJOVE actually makes a copy of the tutorial in your home directory; if you ever want to start over (if you trash the file by accident) all you need to do is remove the file <i>~/teach-jove</i> and run teachjove again. </p>
<p> TEACHJOVE recognizes the following switch:</p>
<dl>
<dt><code>-s</code><i>&nbsp;<wbr>sharedir</i></p>
<dd> Allows the user to specify the directory in which the special teach-jove file can be found (default /usr/share/jove).</dl>
<h2>FILES</h2>
<p> <i>/usr/share/jove/teach-jove</i> &#8212; THE special file.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-jove/">jove</a>(1)</i> &#8212; to learn about JOVE in general.</p>
<h2>AUTHOR</h2>
<p> Jonathan Payne </p>
<h2>Index</h2>
