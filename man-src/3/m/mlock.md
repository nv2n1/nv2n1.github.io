---
title: "mlock(3)"
name: "mlock"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlock/"
description: "mLock – lock a mutex."
---

<p>mLock &#8211; lock a mutex. </p>
<h2>Synopsis</h2>
<pre>#include &lt;util/ulocks.h&gt;</pre>
<pre>NEOERR *mLock(pthread_mutex_t *mutex);</pre>
<h2>Arguments</h2>
<p>mutex &#8211; mutex to lock. </p>
<h2>Description</h2>
<p>Locks the mutex &lt;mutex&gt;. This call blocks until the mutex is acquired. </p>
<p> MT-Level: Safe. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mcreate/">mCreate</a></code>(3), <a href="/docs/linux/man/3-fcreate/">fCreate</a><code>(3), <a href="/docs/linux/man/3-munlock/">mUnlock</a></code>(3), <a href="/docs/linux/man/3-funlock/">fUnlock</a><code>(3), <a href="/docs/linux/man/3-cbroadcast/">cBroadcast</a></code>(3), <a href="/docs/linux/man/3-csignal/">cSignal</a><code>(3), <a href="/docs/linux/man/3-ffind/">fFind</a></code>(3), <a href="/docs/linux/man/3-cdestroy/">cDestroy</a><code>(3), <a href="/docs/linux/man/3-ccreate/">cCreate</a></code>(3), <a href="/docs/linux/man/3-mdestroy/">mDestroy</a><code>(3), <a href="/docs/linux/man/3-cwait/">cWait</a></code>(3), <a href="/docs/linux/man/3-flock/">fLock</a><code>(3), <a href="/docs/linux/man/3-fdestroy/">fDestroy</a></code>(3), mLock</p>
