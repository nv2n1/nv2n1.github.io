---
title: "flock(3)"
name: "flock"
section: "3"
letter: "f"
url: "/docs/linux/man/3-flock/"
description: "fLock – acquire file lock."
---

<p>fLock &#8211; acquire file lock. </p>
<h2>Synopsis</h2>
<pre>#include &lt;util/ulocks.h&gt;</pre>
<pre>NEOERR *fLock(int lock);</pre>
<h2>Arguments</h2>
<p>lock &#8211; Lock to acquire. </p>
<h2>Description</h2>
<p>Acquires the lock identified by &lt;lock&gt;. This call blocks until the lock is acquired. </p>
<p> MT-Level: Safe. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mcreate/">mCreate</a></code>(3), <a href="/docs/linux/man/3-fcreate/">fCreate</a><code>(3), <a href="/docs/linux/man/3-munlock/">mUnlock</a></code>(3), <a href="/docs/linux/man/3-funlock/">fUnlock</a><code>(3), <a href="/docs/linux/man/3-cbroadcast/">cBroadcast</a></code>(3), <a href="/docs/linux/man/3-csignal/">cSignal</a><code>(3), <a href="/docs/linux/man/3-ffind/">fFind</a></code>(3), <a href="/docs/linux/man/3-cdestroy/">cDestroy</a><code>(3), <a href="/docs/linux/man/3-ccreate/">cCreate</a></code>(3), <a href="/docs/linux/man/3-mdestroy/">mDestroy</a><code>(3), <a href="/docs/linux/man/3-cwait/">cWait</a></code>(3), <a href="/docs/linux/man/3-flock/">fLock</a><code>(3), <a href="/docs/linux/man/3-fdestroy/">fDestroy</a></code>(3), mLock</p>
