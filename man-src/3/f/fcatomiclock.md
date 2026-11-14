---
title: "fcatomiclock(3)"
name: "fcatomiclock"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcatomiclock/"
description: "FcAtomicLock – lock a file"
---

<p>FcAtomicLock &#8211; lock a file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcAtomicLock (FcAtomic *</code><i>atomic</i><code>); </code></p>
<h2>Description</h2>
<p>Attempts to lock the file referenced by <i>atomic</i>. Returns FcFalse if the file is already locked, else returns FcTrue and leaves the file locked.</p>
