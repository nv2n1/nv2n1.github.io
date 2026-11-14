---
title: "fdestroy(3)"
name: "fdestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdestroy/"
description: "fDestroy – destroy a lock."
---

<p>fDestroy &#8211; destroy a lock. </p>
<h2>Synopsis</h2>
<pre>#include &lt;util/ulocks.h&gt;</pre>
<pre>void fDestroy(int lock);</pre>
<h2>Arguments</h2>
<p>lock &#8211; Lock to destroy. </p>
<h2>Description</h2>
<p>Destroys the lock &lt;lock&gt; that was created by fCreate() or fFind(). </p>
<p> MT-Level: Safe for unique &lt;lock&gt;. </p>
<h2>Return Value</h2>
<p>None. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mcreate/">mCreate</a></code>(3), <a href="/docs/linux/man/3-fcreate/">fCreate</a><code>(3), <a href="/docs/linux/man/3-munlock/">mUnlock</a></code>(3), <a href="/docs/linux/man/3-funlock/">fUnlock</a><code>(3), <a href="/docs/linux/man/3-cbroadcast/">cBroadcast</a></code>(3), <a href="/docs/linux/man/3-csignal/">cSignal</a><code>(3), <a href="/docs/linux/man/3-ffind/">fFind</a></code>(3), <a href="/docs/linux/man/3-cdestroy/">cDestroy</a><code>(3), <a href="/docs/linux/man/3-ccreate/">cCreate</a></code>(3), <a href="/docs/linux/man/3-mdestroy/">mDestroy</a><code>(3), <a href="/docs/linux/man/3-cwait/">cWait</a></code>(3), <a href="/docs/linux/man/3-flock/">fLock</a><code>(3), <a href="/docs/linux/man/3-fdestroy/">fDestroy</a></code>(3), mLock</p>
