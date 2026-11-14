---
title: "sc_threadlockholder(3)"
name: "sc_threadlockholder"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_threadlockholder/"
description: "sc::ThreadLockHolder –"
---

<p>sc::ThreadLockHolder &#8211; </p>
<p> Acquire a lock on creation and release it on destruction.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thread.h&gt;

Public Member Functions</code></pre>
<p> <code>ThreadLockHolder</code> (const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp;l)<br />
 <i>Acquires the lock. </i><br />
 void <code>unlock</code> ()<br />
 <i>Release the lock before the DTOR is called, if it is still held. </i><br />
 void <code>lock</code> ()<br />
 <i>Acquire the lock once more. </i><br />
 <code>~ThreadLockHolder</code> ()<br />
 <i>Releases the lock if it is still held. </i></p>
<h2>Detailed Description</h2>
<p>Acquire a lock on creation and release it on destruction. </p>
<p> This should be used to lock and unlock <code>ThreadLock</code> objects to provide exception safety.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
