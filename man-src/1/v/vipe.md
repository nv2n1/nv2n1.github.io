---

title: "vipe(1)"
name: "vipe"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vipe/"
---

vipe - edit pipe 

command1 | vipe | command2

vipe allows you to run your editor in the middle of a unix pipeline and edit the data that is being piped between programs. Your editor will have the full data being piped from command1 loaded into it, and when you close it, that data will be piped into command2.

<h2>ARGUMENTS</h2>

 vipe takes an argument --suffix that can be used to provide a file extension to the temp file generated. This enables editors to provide syntax highlighting and activate modes. For example, you can call vipe like 

 <pre>
  vipe --suffix csv
</pre> 

 to create a tempfile with .csv extensions which makes Emacs (or your favorite editor) launch in <font SIZE="-1">CSV</font> major mode.

<h2>ENVIRONMENT VARIABLES</h2>

<dl>
<dt><font SIZE="-1">EDITOR</font>
</dt><dd> Editor to use.
</dd><dt><font SIZE="-1">VISUAL</font>
</dt><dd> Also supported to determine what editor to use.</dd></dl>

<h2>AUTHOR</h2>

 Copyright 2006 by Joey Hess &lt;id [at] joeyh.name&gt; 

 Licensed under the <font SIZE="-1">GNU GPL.</font>
