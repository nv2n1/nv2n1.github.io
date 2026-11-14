---
title: "kpatch(1)"
name: "kpatch"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpatch/"
---

<h2>NAME</h2>

 kpatch - hot patch module management

<h2>SYNOPSIS</h2>

 kpatch &lt;command&gt; [&lt;args&gt;]

<h2>DESCRIPTION</h2>

 kpatch is a user script that manages installing, loading, and displaying information about kernel patch modules installed on the system.

<h2>COMMANDS</h2>

 

 install [-k|--kernel-version=&lt;kernel version&gt;] &lt;module&gt; 
&nbsp;<wbr>install patch module to the initrd to be loaded at boot 

 uninstall [-k|--kernel-version=&lt;kernel version&gt;] &lt;module&gt; 
&nbsp;<wbr>uninstall patch module from the initrd 

 load --all 
&nbsp;<wbr>load all installed patch modules into the running kernel 

 load &lt;module&gt; 
&nbsp;<wbr>load patch module into the running kernel 

 unload --all 
&nbsp;<wbr>unload all patch modules from the running kernel 

 unload &lt;module&gt; 
&nbsp;<wbr>unload patch module from the running kernel 

 info &lt;module&gt; 
&nbsp;<wbr>show information about a patch module 

 list 
&nbsp;<wbr>list installed patch modules 

 version 
&nbsp;<wbr>display the kpatch version 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-kpatch-build/">kpatch-build</a>(1)

<h2>BUGS</h2>

 No known bugs.

<h2>AUTHOR</h2>

 Udo Seidel (udoseidel [at] gmx.de)

<h2>COPYRIGHT</h2>

 Copyright (C) 2014: Seth Jennings &lt;sjenning [at] redhat.com&gt; and Josh Poimboeuf &lt;jpoimboe [at] redhat.com&gt; 

 

<h2>Index</h2>


