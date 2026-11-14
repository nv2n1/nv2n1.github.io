---
title: "ffind(3)"
name: "ffind"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ffind/"
description: "fFind – find a file lock."
---

<p>fFind &#8211; find a file lock. </p>
<h2>Synopsis</h2>
<pre>#include &lt;util/ulocks.h&gt;</pre>
<pre>NEOERR *fFind(int *plock, const char *file);</pre>
<h2>Arguments</h2>
<p>plock &#8211; place for lock.<br />
 file &#8211; path of file to use as lock. </p>
<h2>Description</h2>
<p>Find a file identified by the path &lt;file&gt;, and returns a lock identifier for it in &lt;plock&gt;. If the file doesn&#8217;t exist, returns true. </p>
<p> MT-Level: Safe. </p>
<h2>Return Value</h2>
<p>plock &#8211; set to lock identifier. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mcreate/">mCreate</a></code>(3), <a href="/docs/linux/man/3-fcreate/">fCreate</a><code>(3), <a href="/docs/linux/man/3-munlock/">mUnlock</a></code>(3), <a href="/docs/linux/man/3-funlock/">fUnlock</a><code>(3), <a href="/docs/linux/man/3-cbroadcast/">cBroadcast</a></code>(3), <a href="/docs/linux/man/3-csignal/">cSignal</a><code>(3), <a href="/docs/linux/man/3-ffind/">fFind</a></code>(3), <a href="/docs/linux/man/3-cdestroy/">cDestroy</a><code>(3), <a href="/docs/linux/man/3-ccreate/">cCreate</a></code>(3), <a href="/docs/linux/man/3-mdestroy/">mDestroy</a><code>(3), <a href="/docs/linux/man/3-cwait/">cWait</a></code>(3), <a href="/docs/linux/man/3-flock/">fLock</a><code>(3), <a href="/docs/linux/man/3-fdestroy/">fDestroy</a></code>(3), mLock</p>
