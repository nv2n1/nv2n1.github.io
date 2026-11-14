---
title: "globus_cond_init(3)"
name: "globus_cond_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_cond_init/"
description: "Condition Variables –"
---

<h2 class="name">NAME</h2>
<p> Condition Variables &#8211; </p>
<h3>Data Structures</h3>
<p> union <code>globus_cond_t</code><br />
 <i>Condition variable. </i><br />
 union <code>globus_condattr_t</code><br />
 <i>Condition variable attribute. </i></p>
<h3>Functions</h3>
<p> int <code>globus_cond_init</code> (<code>globus_cond_t</code> *cond, <code>globus_condattr_t</code> *attr)<br />
 <i>Initialize a condition variable</i> </p>
<p> The <code>globus_cond_init()</code> function creates a condition variable that can be used for event signalling between threads. &quot;<br />
 int <code>globus_cond_destroy</code> (<code>globus_cond_t</code> *cond)<br />
 <i>Destroy a condition variable. </i><br />
 int <code>globus_cond_wait</code> (<code>globus_cond_t</code> *cond, <code>globus_mutex_t</code> *mutex)<br />
 <i>Wait for a condition to be signalled. </i><br />
 int <code>globus_cond_timedwait</code> (<code>globus_cond_t</code> *cond, <code>globus_mutex_t</code> *mutex, globus_abstime_t *abstime)<br />
 <i>Wait for a condition to be signalled. </i><br />
 int <code>globus_cond_signal</code> (<code>globus_cond_t</code> *cond)<br />
 <i>Signal a condition to a thread. </i><br />
 int <code>globus_cond_broadcast</code> (<code>globus_cond_t</code> *cond)<br />
 <i>Signal a condition to multiple threads. </i><br />
 int <code>globus_condattr_init</code> (<code>globus_condattr_t</code> *cond_attr)<br />
 <i>Initialize a condition variable attribute. </i><br />
 int <code>globus_condattr_destroy</code> (<code>globus_condattr_t</code> *cond_attr)<br />
 <i>Destroy a condition attribute. </i><br />
 int <code>globus_condattr_setspace</code> (<code>globus_condattr_t</code> *cond_attr, int space)<br />
 <i>Set callback space associated with a condition variable attribute</i> </p>
<p> The <code>globus_condattr_setspace()</code> function sets the callback space to use with condition variables created with this attribute. Callback spaces are used to control how callbacks are issued to different threads. See <code>Callback Spaces </code> for more information on callback spaces. &quot;<br />
 int <code>globus_condattr_getspace</code> (<code>globus_condattr_t</code> *cond_attr, int *space)<br />
 <i>Get callback space associated with a condition variable attribute</i> </p>
<p> The <code>globus_condattr_getspace()</code> function copies the value of the callback space associated with a condition variable attribute to the integer pointed to by the <i>space</i> parameter. &quot;</p>
<h2>Detailed Description</h2>
<p> The <code>globus_cond_t</code> provides condition variables for signalling events between threads interested in particular state. One or many threads may wait on a condition variable until it is signalled, at which point they can attempt to lock a mutex related to that condition&#8217;s state and process the event. </p>
<p> In a non-threaded model, the condition variable wait operations are used to poll the event driver to handle any operations that have been scheduled for execution by the globus_callback system or I/O system. In this way, applications written to use those systems to handle nonblocking operations will work with either a threaded or nonthreaded runtime choice.</p>
<h2>Function Documentation</h2>
<h3>int globus_cond_broadcast (<code>globus_cond_t</code> *cond)</h3>
<p> Signal a condition to multiple threads. The <code>globus_cond_signal()</code> function signals a condition as occurring. This will unblock all threads waiting for that condition. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> A pointer to the condition variable to signal.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_cond_broadcast()</code> returns GLOBUS_SUCCESS. If an error occurs, <code>globus_cond_broadcast()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_cond_destroy (<code>globus_cond_t</code> *cond)</h3>
<p> Destroy a condition variable. The <code>globus_cond_destroy()</code> function destroys the condition variable pointed to by its <i>cond</i> parameter. After a condition variable is destroyed it may no longer be used unless it is again initialized by <code>globus_cond_init()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> The condition variable to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_cond_destroy()</code> returns GLOBUS_SUCCESS. Otherwise, a non-zero implementation-specific error value is returned.</dl>
<h3>int globus_cond_init (<code>globus_cond_t</code> *cond, <code>globus_condattr_t</code> *attr)</h3>
<p> Initialize a condition variable </p>
<p> The <code>globus_cond_init()</code> function creates a condition variable that can be used for event signalling between threads. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> Pointer to the condition variable to initialize.<br />
 <i>attr</i> Condition variable attributes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_cond_init()</code> initializes the condition variable and returns GLOBUS_SUCCESS. Otherwise, a non-0 value is returned.</dl>
<h3>int globus_cond_signal (<code>globus_cond_t</code> *cond)</h3>
<p> Signal a condition to a thread. The <code>globus_cond_signal()</code> function signals a condition as occurring. This will unblock at least one thread waiting for that condition. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> A pointer to the condition variable to signal.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_cond_signal()</code> returns GLOBUS_SUCCESS. If an error occurs, <code>globus_cond_signal()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_cond_timedwait (<code>globus_cond_t</code> *cond, <code>globus_mutex_t</code> *mutex, globus_abstime_t *abstime)</h3>
<p> Wait for a condition to be signalled. The <code>globus_cond_timedwait()</code> function atomically unlocks the mutex pointed to by the <i>mutex</i> parameter and blocks the current thread until either the condition variable pointed to by <i>cond</i> is signalled by another thread or the current time exceeds the value pointed to by the <i>abstime</i> parameter. If the timeout occurs before the condition is signalled, <code>globus_cond_timedwait()</code> returns ETIMEDOUT. Behavior is undefined if <code>globus_cond_timedwait()</code> is called with the mutex pointed to by the <i>mutex</i> variable unlocked. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> The condition variable to wait for.<br />
 <i>mutex</i> The mutex associated with the condition state.<br />
 <i>abstime</i> The absolute time to wait until.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_cond_timedwait()</code> unlocks the mutex and blocks the current thread until it has been signalled, returning GLOBUS_SUCCES. If a timeout occurs before signal, <code>globus_cond_timedwait()</code> unlocks the mutex and returns ETIMEDOUT. Otherwise, <code>globus_cond_timedwait()</code> returns an implementation-specific non-zero error value.</dl>
<h3>int globus_cond_wait (<code>globus_cond_t</code> *cond, <code>globus_mutex_t</code> *mutex)</h3>
<p> Wait for a condition to be signalled. The <code>globus_cond_wait()</code> function atomically unlocks the mutex pointed to by the <i>mutex</i> parameter and blocks the current thread until the condition variable pointed to by <i>cond</i> is signalled by either <code>globus_cond_signal()</code> or <code>globus_cond_broadcast()</code>. Behavior is undefined if <code>globus_cond_wait()</code> is called with the mutex pointed to by the <i>mutex</i> variable unlocked. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond</i> The condition variable to wait for.<br />
 <i>mutex</i> The mutex associated with the condition state.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_cond_wait()</code> unlocks the mutex and blocks the current thread until it has been signalled, returning GLOBUS_SUCCES. Otherwise, <code>globus_cond_wait()</code> returns an implementation-specific non-zero error value.</dl>
<h3>int globus_condattr_destroy (<code>globus_condattr_t</code> *cond_attr)</h3>
<p> Destroy a condition attribute. The <code>globus_condattr_destroy()</code> function destroys the condition variable attribute structure pointed to by its <i>cond_attr</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond_attr</i> Attribute structure to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_condattr_destroy()</code> returns GLOBUS_SUCCESS and modifies the attribute pointed to by <i>cond_attr</i>. If an error occurs, <code>globus_condattr_destroy()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_condattr_getspace (<code>globus_condattr_t</code> *cond_attr, int *space)</h3>
<p> Get callback space associated with a condition variable attribute </p>
<p> The <code>globus_condattr_getspace()</code> function copies the value of the callback space associated with a condition variable attribute to the integer pointed to by the <i>space</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond_attr</i> Condition variable attribute to modify.<br />
 <i>space</i> Pointer to an integer to be set to point to the callback space associated with cond_attr.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_condattr_getspace()</code> returns GLOBUS_SUCCESS and modifies the value pointed to by <i>space</i> to refer to the callback space associated with <i>cond_attr</i>. If an error occurs, <code>globus_condattr_getspace()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_condattr_init (<code>globus_condattr_t</code> *cond_attr)</h3>
<p> Initialize a condition variable attribute. The <code>globus_condattr_init()</code> function initializes the condition variable attribute structure pointed to by its <i>cond_attr</i> parameter to the system default values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond_attr</i> Attribute structure to initialize.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_condattr_init()</code> returns GLOBUS_SUCCESS and modifies the attribute pointed to by <i>cond_attr</i>. If an error occurs, <code>globus_condattr_init()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_condattr_setspace (<code>globus_condattr_t</code> *cond_attr, intspace)</h3>
<p> Set callback space associated with a condition variable attribute </p>
<p> The <code>globus_condattr_setspace()</code> function sets the callback space to use with condition variables created with this attribute. Callback spaces are used to control how callbacks are issued to different threads. See <code>Callback Spaces </code> for more information on callback spaces. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cond_attr</i> Condition variable attribute to modify.<br />
 <i>space</i> Callback space to associate with the attribute.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_condattr_setspace()</code> returns GLOBUS_SUCCESS and adds a reference to the callback space to the condition variable attribute. If an error occurs, <code>globus_condattr_setspace()</code> returns an implementation-specific non-zero error code.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
