---

title: "nwdir(1)"
name: "nwdir"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwdir/"
description: "nwdir – Lists files in directory"
---

<h2>NAME</h2>
<p> nwdir &#8211; Lists files in directory</p>
<p> <code>nwdir</code> [<code>-h</code>] [<code>-v</code>] [<code>-l</code>] [<code>-t</code>] [<code>-d</code>] [<code>-e</code>] [<code>-f</code>] [<code>directory</code>] </p>
<p> <code>nwdir</code> lists files, directories and their attributes from the specified NetWare directory. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
</dt><dd> <code>-h</code> is used to print out a short help text.</dd></dl>
<p> <code>-d</code></p>
<dl>
<dt>
</dt><dd> List directories like other files, rather than listing their contents.</dd></dl>
<p> <code>-l</code></p>
<dl>
<dt>
</dt><dd> Show filename in all available namespaces.</dd></dl>
<p> <code>-v</code></p>
<dl>
<dt>
</dt><dd> Verbose listing, display everything possible.</dd></dl>
<p> <code>-e</code></p>
<dl>
<dt>
</dt><dd> Display <i>OS/2</i> Extended Attributes.</dd></dl>
<p> <code>-f</code></p>
<dl>
<dt>
</dt><dd> List connections using each file.</dd></dl>
<p> <code>-t</code></p>
<dl>
<dt>
</dt><dd> Show all informations (rights, attributes, file inodes) also as hexadecimal numbers.</dd></dl>
<p> <code>directory</code></p>
<dl>
<dt>
</dt><dd> You can specify the directory to list. Current working directory is used by default. You have to specify path in Linux format, not in NetWare format. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> nwdir -t -v /NetWare/server/sys </p>
<p> With this example, all files from directory /NetWare/server/sys are displayed. </p>
<h2>AUTHORS</h2>
<p> nwdir was written by Milan Vandrovec. See the Changes file of ncpfs for other contributors. </p>
<h2>BUGS</h2>
<p> Directory quotas are not displayed. User names are not taken from NDS, but only from bindery. </p>
