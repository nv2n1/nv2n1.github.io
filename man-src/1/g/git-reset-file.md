---
title: "git-reset-file(1)"
name: "git-reset-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-reset-file/"
description: "git-reset-file – Reset one file"
---

<h2>NAME</h2>
<p> <code>git-reset-file</code> &#8211; Reset one file</p>
<h2>SYNOPSIS</h2>
<p> <code>git-reset-file</code> [&lt;filename&gt;] commit-hash</p>
<h2>DESCRIPTION</h2>
<p> Reset one file to HEAD or certain commit-hash</p>
<h2>OPTIONS</h2>
<p> &lt;filename&gt; </p>
<p> The name of the file to reset. </p>
<p> &lt;commit-hash&gt; </p>
<p> (Optional) Hash of commit to reset the file to. Defaults to HEAD.</p>
<h2>EXAMPLES</h2>
<p> Reset one file to HEAD</p>
<dl>
<dt>
<dd>
<pre>
$ git reset-file .htaccess
</pre>
<dt>
<dd></dl>
<p> or reset one file to certain commit</p>
<dl>
<dt>
<dd>
<pre>
$ git reset-file .htaccess dc82b19
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Sasha Khamkov &lt;<i>sanusart [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
