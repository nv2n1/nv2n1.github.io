---
title: "ustat(2)"
name: "ustat"
section: "2"
letter: "u"
url: "/docs/linux/man/2-ustat/"
description: "ustat – get filesystem statistics"
---

<h2 class="name">NAME</h2>
<p> ustat &#8211; get filesystem statistics </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt; /* libc[45] */
#include &lt;ustat.h&gt;  /* glibc2 */
int ustat(dev_t dev, struct ustat *ubuf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ustat</code>() returns information about a mounted filesystem. <i>dev</i> is a device number identifying a device containing a mounted filesystem. <i>ubuf</i> is a pointer to a <i>ustat</i> structure that contains the following members: </p>
<p> daddr_t f_tfree; /* Total free blocks */ ino_t f_tinode; /* Number of free inodes */ char f_fname[6]; /* Filsys name */ char f_fpack[6]; /* Filsys pack name */ </p>
<p> The last two fields, <i>f_fname</i> and <i>f_fpack</i>, are not implemented and will always be filled with null bytes (&#8216;
