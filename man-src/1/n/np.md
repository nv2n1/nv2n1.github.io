---

title: "np(1)"
name: "np"
section: "1"
letter: "n"
url: "/docs/linux/man/1-np/"
---

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
</dt><dd> Print a list of options 
</dd><dt>-f, --force
</dt><dd> Overwrite any existing files 
</dd><dt>-l, --list
</dt><dd> List projects available 
</dd><dt>-g, --global
</dt><dd> Use global projects instead of personal ones 
&nbsp;<wbr> 
</dd></dl>

<h2>FILES</h2>

 

 

 
&nbsp;<wbr><i>${datadir}/new/projects</i>&nbsp;<wbr>System-wide project directory.&nbsp;<wbr><i>~/.new/projects</i>&nbsp;<wbr>User specific project directory. 

<h2>AUTHORS</h2>

 

 

 
&nbsp;<wbr> 

<dl>
<dt>E-Mail
</dt><dd> &lt;new_proj [at] flyn.org&gt; 
</dd><dt>HTTP
</dt><dd> Flyn Computing: <i><a rel="nofollow" HREF="http://www.flyn.org">http://www.flyn.org</a></i> 
&nbsp;<wbr> 
</dd></dl>
