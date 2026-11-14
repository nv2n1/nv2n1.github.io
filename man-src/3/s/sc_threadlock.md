---
title: "sc_threadlock(3)"
name: "sc_threadlock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_threadlock/"
description: "sc::ThreadLock –"
---

<p>sc::ThreadLock &#8211; </p>
<p> The <code>ThreadLock</code> abstract class provides mutex locks to be used in conjunction with ThreadGrp&#8217;s.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thread.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual void <code>lock</code> ()=0<br />
 <i>Obtain the lock. </i><br />
 virtual void <code>unlock</code> ()=0<br />
 <i>Release the lock. </i></p>
<h2>Detailed Description</h2>
<p>The <code>ThreadLock</code> abstract class provides mutex locks to be used in conjunction with ThreadGrp&#8217;s. </p>
<p> <code>ThreadLock</code> objects should be locked and unlocked with <code>ThreadLockHolder</code> objects to provide exception safety.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
