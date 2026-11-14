---
title: "log4cppthreadingmsscopedlock(3)"
name: "log4cppthreadingmsscopedlock"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cppthreadingmsscopedlock/"
description: "log4cpp::threading::MSScopedLock –"
---

<p>log4cpp::threading::MSScopedLock &#8211; </p>
<p> A simple object wrapper around WaitForSingleObject() and ReleaseMutex()</p>
<h2>Synopsis</h2>
<p>#include &lt;MSThreads.hh&gt;</p>
<h3>Public Member Functions</h3>
<p><code>MSScopedLock</code> (<code>MSMutex</code> &amp;mutex) </p>
<p> <code>~MSScopedLock</code> () </p>
<h2>Detailed Description</h2>
<p>A simple object wrapper around WaitForSingleObject() and ReleaseMutex()</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::threading::MSScopedLock::MSScopedLock (<code>MSMutex</code> &amp;mutex) [inline]</h3>
<h3>log4cpp::threading::MSScopedLock::~MSScopedLock () [inline]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
