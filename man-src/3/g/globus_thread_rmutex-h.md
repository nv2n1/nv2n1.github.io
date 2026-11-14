---
title: "globus_thread_rmutex-h(3)"
name: "globus_thread_rmutex-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_thread_rmutex-h/"
description: "globus_thread_rmutex.h –"
---

<p>globus_thread_rmutex.h &#8211; </p>
<p> Recursive Mutex.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_thread.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_rmutex_t</code><br />
 <i>Recursive Mutex. </i></p>
<h3>Typedefs</h3>
<p>typedef int <code>globus_rmutexattr_t</code><br />
 <i>Recursive mutex attribute. </i></p>
<h3>Functions</h3>
<p>int <code>globus_rmutex_init</code> (<code>globus_rmutex_t</code> *rmutex, <code>globus_rmutexattr_t</code> *attr)<br />
 <i>Initialize a recursive mutex. </i><br />
 int <code>globus_rmutex_lock</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Lock a recursive mutex. </i><br />
 int <code>globus_rmutex_unlock</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Unlock a recursive mutex. </i><br />
 int <code>globus_rmutex_destroy</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Destroy a recursive mutex. </i></p>
<h2>Detailed Description</h2>
<p>Recursive Mutex. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
