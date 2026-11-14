---
title: "projects(5)"
name: "projects"
section: "5"
letter: "p"
url: "/docs/linux/man/5-projects/"
description: "projects – persistent project root definition"
---

<p>projects &#8211; persistent project root definition</p>
<h2>Description</h2>
<p>The <i>/etc/projects</i> file provides a mapping between numeric project identifiers and those directories which are the roots of the quota tree. Its format is simply: </p>
<pre># comments are hash-prefixed
# ...
10:/export/cage
42:/var/log</pre>
<p>The <i>/etc/projects</i> file is optional, instead <code><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></code>(8) can be used with the <code>-p</code> argument to specify a project root directly for each operation. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xfs_quota/">xfs_quota</a></code>(8), <code><a href="/docs/linux/man/3-xfsctl/">xfsctl</a></code>(3), <code><a href="/docs/linux/man/5-projid/">projid</a></code>(5). </p>
