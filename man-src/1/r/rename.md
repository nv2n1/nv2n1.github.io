---
title: "rename(1)"
name: "rename"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rename/"
description: "rename – rename files"
---

<h2>NAME</h2>
<p> rename &#8211; rename files</p>
<h2>SYNOPSIS</h2>
<p> <code>rename</code> [<i>options</i>]<i> expression replacement file</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>rename</code> will rename the specified files by replacing the first occurrence of <i>expression</i> in their name by <i>replacement</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Give visual feedback which files where renamed, if any.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-s</code>, <code>&#8211;symlink</code></p>
<dd> Peform rename on symlink target</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</dl>
<h2>EXAMPLES</h2>
<p> Given the files <i>foo1</i>, &#8230;, <i>foo9</i>, <i>foo10</i>, &#8230;, <i>foo278</i>, the commands</p>
<dl>
<dt>
<dd>
<pre>
rename foo foo0 foo?
rename foo foo0 foo??
</pre>
</dl>
<p> will turn them into <i>foo001</i>, &#8230;, <i>foo009</i>, <i>foo010</i>, &#8230;, <i>foo278</i>. And</p>
<dl>
<dt>
<dd>
<pre>
rename .htm .html *.htm
</pre>
</dl>
<p> will fix the extension of your html files.</p>
<h2>WARNING</h2>
<p> The renaming has no safeguards. If the user has permission to rewrite file names, the command will perform the action without any questions. For example, the result can be quite drastic when the command is run as root in the /lib directory. Always make a backup before running the command, unless you truly know what you are doing.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mmv/">mmv</a></code>(1), <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1)</p>
<h2>AVAILABILITY</h2>
<p> The rename command is part of the util-linux package and is available from <a href="ftp://ftp.kernel.org/pub/linux/utils/util-linux/.">ftp://ftp.kernel.org/pub/linux/utils/util-linux/.</a> </p>
<h2>Index</h2>
