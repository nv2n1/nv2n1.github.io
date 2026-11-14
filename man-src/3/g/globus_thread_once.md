---
title: "globus_thread_once(3)"
name: "globus_thread_once"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_thread_once/"
description: "One-time execution –"
---

<h2 class="name">NAME</h2>
<p> One-time execution &#8211; </p>
<h3>Data Structures</h3>
<p> union <code>globus_thread_once_t</code><br />
 <i>Thread once structure. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_THREAD_ONCE_INIT</code> { .none = 0 }<br />
 <i>Thread once initializer value. </i></p>
<h3>Functions</h3>
<p> int <code>globus_thread_once</code> (<code>globus_thread_once_t</code> *once, void(*init_routine)(void))<br />
 <i>Execute a function one time. </i></p>
<h2>Detailed Description</h2>
<p> The <code>globus_thread_once_t</code> provides a way for applications and libraries to execute some code exactly one time, independent of the number of threads which attempt to execute it. To use this, statically initialize a <code>globus_thread_once_t</code> control with the value GLOBUS_THREAD_ONCE_INIT, and pass a pointer to a function to execute once, along with the control, to <code>globus_thread_once()</code>.</p>
<h2>Function Documentation</h2>
<h3>int globus_thread_once (<code>globus_thread_once_t</code> *once, void(*)(void)init_routine)</h3>
<p> Execute a function one time. The <code>globus_thread_once()</code> function will execute the function pointed to by its <i>init_routine</i> parameter one time for each unique <code>globus_thread_once_t</code> object passed to it, independent of the number of threads calling it. The <i>once</i> value must be a static value initialized to GLOBUS_THREAD_ONCE_INIT. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>once</i> A pointer to the value used to govern whether the function passed via the <i>init_routine</i> parameter has executed.<br />
 <i>init_routine</i> Function to execute one time. It is called with no parameters.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_once()</code> guarantees that the function pointed to by <i>init_routine</i> has run, and that subsequent calls to <code>globus_thread_once()</code> with the same value of <i>once</i> will not execute that function, and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_once()</code> returns an implementation-specific non-zero error value.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
