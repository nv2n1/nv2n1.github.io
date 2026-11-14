---
title: "zrun(1)"
name: "zrun"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zrun/"
---

<h2 class="name">NAME</h2>
 

 zrun - automatically uncompress arguments to command 

<h2>SYNOPSIS</h2>

 zrun command file.gz [...]

<h2>DESCRIPTION</h2>

 Prefixing a shell command with ``zrun'' causes any compressed files that are arguments of the command to be transparently uncompressed to temp files (not pipes) and the uncompressed files fed to the command. 

 This is a quick way to run a command that does not itself support compressed files, without manually uncompressing the files. 

 The following compression types are supported: gz bz2 Z xz lzma lzo 

 If zrun is linked to some name beginning with z, like zprog, and the link is executed, this is equivalent to executing ``zrun prog''.

<h2>BUGS</h2>

 Modifications to the uncompressed temporary file are not fed back into the input file, so using this as a quick way to make an editor support compressed files won't work.

<h2>AUTHOR</h2>

 Copyright 2006 by Chung-chieh Shan &lt;ccshan [at] post.harvard.edu&gt; 

<h2>Index</h2>


