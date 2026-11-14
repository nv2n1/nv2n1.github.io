---
title: "shtool-mkshadow(1)"
name: "shtool-mkshadow"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-mkshadow/"
description: "shtool mkshadow – GNU shtool create shadow tree using symlinks"
---

<h2 class="name">NAME</h2>
<p> shtool mkshadow &#8211; GNU shtool create shadow tree using symlinks </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool mkshadow</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] [<code>-a</code>|<code>&#8211;all</code>] <i>src-dir</i> <i>dst-dir</i></p>
<h2>DESCRIPTION</h2>
<p> This command creates a shadow tree of <i>src-dir</i> under <i>dst-dir</i> by recreating the directory hierarchy of <i>src-dir</i> under <i>dst-dir</i> and by creating the files of <i>src-dir</i> by linking them into the corresponding directories under <i>dst-dir</i> via symbolic links. When <i>src-dir</i> can be reached via relative paths from <i>dst-dir</i>, relative symbolic links are used, too. This high-level functionality is originally designed for developers to create copies of source trees.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Really shadow all files and directories in <i>src-dir</i>. Default is to skip <font SIZE="-1">CVS</font> related files and directories, backup files, object files, etc.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool mkshadow -v -a . /tmp/shadow
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>mkshadow</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1998 for <code>Apache</code>. It was later revised and taken over into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1). </p>
<h2>Index</h2>
