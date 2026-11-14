---
title: "projid(5)"
name: "projid"
section: "5"
letter: "p"
url: "/docs/linux/man/5-projid/"
description: "projid – the project name mapping file"
---

<p>projid &#8211; the project name mapping file</p>
<h2>Description</h2>
<p>The <i>/etc/projid</i> file provides a mapping between numeric project identifiers and a simple human readable name (similar relationship to the one that exists between usernames and uids). Its format is simply: </p>
<pre># comments are hash-prefixed
# ...
cage:10
logfiles:42</pre>
<p>This file is optional, if a project identifier cannot be mapped to a name, it will be parsed and displayed as a numeric value. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></code>(8), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/5-projects/">projects</a></code>(5). </p>
