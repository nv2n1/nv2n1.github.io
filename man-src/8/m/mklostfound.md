---
title: "mklostfound(8)"
name: "mklostfound"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mklostfound/"
description: "mklost+found – create a lost+found directory on a mounted Linux second extended file system"
---

<p>mklost+found &#8211; create a lost+found directory on a mounted Linux second extended file system</p>
<h2>Synopsis</h2>
<p><code>mklost+found</code></p>
<h2>Description</h2>
<p><code>mklost+found</code> is used to create a <i>lost+found</i> directory in the current working directory on a Linux second extended file system. There is normally a <i>lost+found</i> directory in the root directory of each file system. </p>
<p> <code>mklost+found</code> pre-allocates disk blocks to the <i>lost+found</i> directory so that when <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8) is being run to recover a file system, it does not need to allocate blocks in the file system to store a large number of unlinked files. This ensures that <code>e2fsck</code> will not have to allocate data blocks in the file system during recovery.</p>
<h2>Options</h2>
<p>There are none.</p>
<h2>Author</h2>
<p><code>mklost+found</code> has been written by Remy Card &lt;Remy.Card [at] linux.org&gt;. It is currently being maintained by Theodore Ts&#8217;o &lt;tytso [at] alum.mit.edu&gt;.</p>
<h2>Bugs</h2>
<p>There are none :-)</p>
<h2>Availability</h2>
<p><code>mklost+found</code> is part of the e2fsprogs package and is available from <a rel="nofollow" href="http://e2fsprogs.sourceforge.net.">http://e2fsprogs.sourceforge.net.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8) </p>
