---

title: "gjar(1)"
name: "gjar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjar/"
description: "gjar – – Archive tool for Java archives"
---

<p> gjar <code>-ctxui</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>jar-file</i> [<code>-C</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i> <i></i><font SIZE="-1"><i>FILE</i></font><i></i>] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;</p>
<p> <code>gjar</code> is an implementation of Sun&#8217;s jar utility that comes with the <font SIZE="-1">JDK</font>. </p>
<p> If any file is a directory then it is processed recursively. The manifest file name and the archive file name needs to be specified in the same order the <code>-m</code> and <code>-f</code> flags are specified.</p>
<h2>OPTIONS</h2>
<p> Operation mode:</p>
<dl>
<dt><code>-c</code></dt>
<dd> Create new archive.</dd>
<dt><code>-t</code></dt>
<dd> List table of contents for archive.</dd>
<dt><code>-x</code></dt>
<dd> Extract named (or all) files from archive.</dd>
<dt><code>-u</code></dt>
<dd> Update existing archive.</dd>
<dt><code>-i</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Compute archive index.</dd></dl>
<p> Operation modifiers:</p>
<dl>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Specify archive file name.</dd>
<dt><code>-0</code></dt>
<dd> Store only; use no <font SIZE="-1">ZIP</font> compression.</dd>
<dt><code>-v</code></dt>
<dd> Generate verbose output on standard output.</dd>
<dt><code>-M</code></dt>
<dd> Do not create a manifest file for the entries.</dd>
<dt><code>-m</code> <i>manifest</i></dt>
<dd> Include manifest information from specified <i>manifest</i> file.</dd></dl>
<p> File name selection:</p>
<dl>
<dt><code>-C</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i><i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Change to the <i></i><font SIZE="-1"><i>DIR</i></font><i></i> and include the following <i></i><font SIZE="-1"><i>FILE</i></font><i></i>.</dd>
<dt><code>-@</code></dt>
<dd> Read the names of the files to add to the archive from stdin. This option is supported only in combination with <code>-c</code> or <code>-u</code>. Non standard option added in the <font SIZE="-1">GCC</font> version.</dd></dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></dt>
<dd> Print help text, then exit.</dd>
<dt><code>-version</code></dt>
<dd> Print version number, then exit.</dd>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></dt>
<dd> Pass argument to the Java runtime.</dd></dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-java/">java</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
