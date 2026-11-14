---
title: "mimedb(1)"
name: "mimedb"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimedb/"
---

<h2 class="name">NAME</h2>
 

 mimedb - lookup file information via the mime database

<h3>Synopsis</h3>

 mimedb [OPTIONS] FILES...

<h3>Description</h3>

<dl>
<dt>*
<dd> FILES is a list of files to analyse
<dt>*
<dd> -t, --input-file-data the specified files type should be determined both by their filename and by their contents (Default)
<dt>*
<dd> -f, --input-filename the specified files type should be determined by their filename
<dt>*
<dd> -i, --input-mime the arguments are not files but mimetypes
<dt>*
<dd> -m, --output-mime the output will be the mimetype of each file (Default)
<dt>*
<dd> -f, --output-description the output will be the description of each mimetype
<dt>*
<dd> -a, --output-action the output will be the default action of each mimetype
<dt>*
<dd> -l, --launch launch the default action for the specified file(s)
<dt>*
<dd> -h, --help display a help message and exit
<dt>*
<dd> -v, --version display version number and exit</dl>
 

 

 The mimedb command is used to query the mimetype database and the .desktop files installed on the system in order to find information on a file. The information that mimedb can retrieve includes the mimetype for a file, a description of the type and what its default action is. mimedb can also be used to launch the default action for this file. 

<h2>Index</h2>


