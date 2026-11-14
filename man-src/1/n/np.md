---
title: "np(1)"
name: "np"
section: "1"
letter: "n"
url: "/docs/linux/man/1-np/"
---

<h2>NAME</h2>

 new_proj - create a new project

<h2>SYNOPSIS</h2>

 19 July 1999 <pre><code>
new[options] filename[template]
</code></pre> 

<h2>DESCRIPTION</h2>

 

 

 New_proj is a program to generate the files neccessary to begin a new project. 

 

 New_proj first looks for templates in <i>~/.new/projects.</i> Second, new looks for templates in <i>&lt;datadir&gt;/new/projects</i>, where datadir is defined by autoconf. This directory is usually <i>/usr/local/share</i> or <i>/usr/share</i>. 

 

 The projects directory contains several files describing different types of projects. Each file is a set of lines containing filenames and an optional template names. 

<h2>OPTIONS</h2>

 

 

 
&nbsp;<wbr> 

<dl>
<dt>-h, --help
<dd> Print a list of options 

<dt>-f, --force
<dd> Overwrite any existing files 

<dt>-l, --list
<dd> List projects available 

<dt>-g, --global
<dd> Use global projects instead of personal ones 
&nbsp;<wbr> 

</dl>

<h2>FILES</h2>

 

 

 
&nbsp;<wbr><i>${datadir}/new/projects</i>&nbsp;<wbr>System-wide project directory.&nbsp;<wbr><i>~/.new/projects</i>&nbsp;<wbr>User specific project directory. 

<h2>AUTHORS</h2>

 

 

 
&nbsp;<wbr> 

<dl>
<dt>E-Mail
<dd> &lt;new_proj [at] flyn.org&gt; 

<dt>HTTP
<dd> Flyn Computing: <i><a rel="nofollow" HREF="http://www.flyn.org">http://www.flyn.org</a></i> 
&nbsp;<wbr> 

 

</dl>

<h2>Index</h2>


