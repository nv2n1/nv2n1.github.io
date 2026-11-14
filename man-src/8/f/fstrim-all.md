---
title: "fstrim-all(8)"
name: "fstrim-all"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fstrim-all/"
description: "fstrim-all – call fstrim on all mounted file systems which support it"
---

<p>fstrim-all &#8211; call fstrim on all mounted file systems which support it</p>
<h2>Description</h2>
<p>SSD drives need to be TRIMed, i. e. they need to be told which blocks the OS considers as &quot;unused&quot; (i. e. from deleted files). Withouth this, the write speed on SSDs becomes slower over time. <code>fstrim-all</code> detects which mounted partitions belong to drives that need/support trimming, and calls <code><a href="/docs/linux/man/1-fstrim/">fstrim</a></code>(1) on them. It is meant to be called from cron. There is no output on success. This only runs on Intel and Samsung SSDs as some SSDs with faulty firmware may encounter data loss problems when running fstrim under high I/O load (see e. g. <a rel="nofollow" href="https://launchpad.net/bugs/1259829">https://launchpad.net/bugs/1259829</a>). You can call <code>fstrim-all</code> with the <code>&#8211;no-model-check</code> option to disable the vendor check and run fstrim on all SSD drives. </p>
<h2>Author</h2>
<p>Martin Pitt &lt;martin.pitt [at] ubuntu.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8) </p>
