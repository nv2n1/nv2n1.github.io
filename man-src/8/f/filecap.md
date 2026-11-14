---
title: "filecap(8)"
name: "filecap"
section: "8"
letter: "f"
url: "/docs/linux/man/8-filecap/"
description: "filecap – a program to see capabilities"
---

<p>filecap &#8211; a program to see capabilities</p>
<h2>Synopsis</h2>
<p><code>filecap [ -a | -d | /dir | /dir/file [cap1 cap2 &#8230;] ]</code></p>
<h2>Description</h2>
<p><code>filecap</code> is a program that prints out a report of programs with file based capabilities. If a file is not in the report or there is no report at all, no capabilities were found. For expedience, the default is to check only the directories in the PATH environmental variable. If the -a command line option is given, then all directories will be checked. If a directory is passed, it will recursively check that directory. If a path to a file is given, it will only check that file. If the path to the file includes capabilities, then they are written to the file. </p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>This tells the program to show all capabilities starting from the / directory. Normally the PATH environmental variable is used to show you capabilities on files you are likely to execute.</p>
<dt><code>-d</code></p>
<dd>This dumps all capabilities for reference. </p>
</dl>
<h2>Examples</h2>
<pre><code>To check file capabilities in $PATH:</code>
<code>filecap</code>
<code>To check file capabilities of whole system:</code>
<code>filecap -a</code>
<code>To check file capabilities recursively in a directory:</code>
<code>filecap /usr</code>
<code>To check file capabilities of a specific program:</code>
<code>filecap /bin/passwd</code>
<code>To list all possible capabilities:</code>
<code>filecap -d</code>
<code>To set a file capability on a specific program:</code>
<code>filecap /bin/ping net_raw net_admin </code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pscap/">pscap</a></code>(8), <code><a href="/docs/linux/man/8-netcap/">netcap</a></code>(8), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
