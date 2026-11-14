---
title: "robohdrs(1)"
name: "robohdrs"
section: "1"
letter: "r"
url: "/docs/linux/man/1-robohdrs/"
description: "robohdrs – insert ROBODoc headers to source code."
---

<h2>NAME</h2>
<p> robohdrs &#8211; insert ROBODoc headers to source code.</p>
<h2>SYNOPSIS</h2>
<p> <code>robohdrs</code> <code>[options]</code> &lt;source file&gt; </p>
<h2>DESCRIPTION</h2>
<p> robohdrs inserts ROBODoc headers to source code files. This program processes one source file at the time. Existing ROBODoc headers, if any, are not checked for. Beware since this may result in double headers. Current working directory should be the same as where the source file is located. </p>
<p> By default NAME and SYNOPSIS items are included in the template header. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> Show brief help on usage and exit.</p>
<dt>-i</p>
<dd> Specify an extra header item to be included in template header. Repeat if multiple extra items are desired.</p>
<dt>-l</p>
<dd> Specify source code language (default C/C++) Supported options are: fortran, fortran90, script, and tex.</p>
<dt>-p</p>
<dd> Specify project name for source file header.</p>
<dt>-s</p>
<dd> Include SOURCE item.</p>
<dt>-t</p>
<dd> Specify version control tag to be included in the main header.</p>
<dt>-x</p>
<dd> Specify path to ctags binary which is used. </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
robohdrs -s -p myproj -i &quot;MODIFICATION HISTORY&quot; -i IDEAS test.c
</pre>
<p> Specifies project name myproj and inserts extra items MODIFICATION HISTORY, IDEAS, and SOURCE to all template headers (excluding source file header). </p>
<pre>
robohdrs -s -p myproj -l script test.tcl
</pre>
<p> Insert headers to a Tcl/Tk script. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003 Frans Slothouber and Petteri Kettunen and Jacco van Weert.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-robodoc/">robodoc</a>(1)</code> </p>
<h2>Index</h2>
