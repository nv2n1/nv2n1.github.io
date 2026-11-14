---
title: "git-unpack-file(1)"
name: "git-unpack-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-unpack-file/"
description: "git-unpack-file – Creates a temporary file with a blob’s contents"
---

<h2 class="name">NAME</h2>
<p> git-unpack-file &#8211; Creates a temporary file with a blob&#8217;s contents </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git unpack-file</i> &lt;blob&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Creates a file holding the contents of the blob specified by sha1. It returns the name of the temporary file in the following format: .merge_file_XXXXX</p>
<h2>OPTIONS</h2>
<p> &lt;blob&gt;</p>
<dl>
<dt>
<dd> Must be a blob id</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
