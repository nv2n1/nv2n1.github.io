---
title: "fcreate(3)"
name: "fcreate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcreate/"
description: "fCreate – create a file lock."
---

<p>fCreate &#8211; create a file lock. </p>
<h2>Synopsis</h2>
<pre>#include &lt;util/ulocks.h&gt;</pre>
<pre>NEOERR *fCreate(int *plock, const char *file);</pre>
<h2>Arguments</h2>
<p>plock &#8211; place for lock.<br />
 file &#8211; path of file to use as lock. </p>
<h2>Description</h2>
<p>Creates a file lock on named file &lt;file&gt;. The lock is returned in &lt;plock&gt;. </p>
<p> MT-Level: Safe. </p>
<h2>Return Value</h2>
<p>plock &#8211; set to lock identifier. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mcreate/">mCreate</a></code>(3), <a href="/docs/linux/man/3-fcreate/">fCreate</a><code>(3), <a href="/docs/linux/man/3-munlock/">mUnlock</a></code>(3), <a href="/docs/linux/man/3-funlock/">fUnlock</a><code>(3), <a href="/docs/linux/man/3-cbroadcast/">cBroadcast</a></code>(3), <a href="/docs/linux/man/3-csignal/">cSignal</a><code>(3), <a href="/docs/linux/man/3-ffind/">fFind</a></code>(3), <a href="/docs/linux/man/3-cdestroy/">cDestroy</a><code>(3), <a href="/docs/linux/man/3-ccreate/">cCreate</a></code>(3), <a href="/docs/linux/man/3-mdestroy/">mDestroy</a><code>(3), <a href="/docs/linux/man/3-cwait/">cWait</a></code>(3), <a href="/docs/linux/man/3-flock/">fLock</a><code>(3), <a href="/docs/linux/man/3-fdestroy/">fDestroy</a></code>(3), mLock</p>
