---
title: "sb_start_pagefault(9)"
name: "sb_start_pagefault"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sb_start_pagefault/"
description: "sb_start_pagefault – get write access to a superblock from a page fault"
---

<p>sb_start_pagefault &#8211; get write access to a superblock from a page fault</p>
<h2>Synopsis</h2>
<pre><code>void sb_start_pagefault(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the super we write to</dl>
<h2>Description</h2>
<p>When a process starts handling write page fault, it should embed the operation into <code>sb_start_pagefault</code> &#8211; <code>sb_end_pagefault</code> pair to get exclusion against file system freezing. This is needed since the page fault is going to dirty a page. This function increments number of running page faults preventing freezing. If the file system is already frozen, the function waits until the file system is thawed. </p>
<p> Since page fault freeze protection behaves as a lock, users have to preserve ordering of freeze protection and other filesystem locks. It is advised to put <code>sb_start_pagefault</code> close to mmap_sem in lock ordering. Page fault handling code implies lock dependency: </p>
<p> mmap_sem -&gt; sb_start_pagefault</p>
<h2>Copyright</h2>
