---
title: "globus_thread_key_destructor_func_t(3)"
name: "globus_thread_key_destructor_func_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_thread_key_destructor_func_t/"
description: "globus_thread.h –"
---

<h2 class="name">NAME</h2>
<p> globus_thread.h &#8211; </p>
<p> Globus Threading Abstraction.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_time.h&#8217;<br />
 #include &lt;unistd.h&gt; </p>
<h3>Data Structures</h3>
<p> union <code>globus_thread_t</code><br />
 <i>Thread ID. </i><br />
 union <code>globus_threadattr_t</code><br />
 <i>Thread attributes. </i><br />
 union <code>globus_mutex_t</code><br />
 <i>Mutex. </i><br />
 union <code>globus_cond_t</code><br />
 <i>Condition variable. </i><br />
 union <code>globus_mutexattr_t</code><br />
 <i>Mutex attribute. </i><br />
 union <code>globus_condattr_t</code><br />
 <i>Condition variable attribute. </i><br />
 union <code>globus_thread_key_t</code><br />
 <i>Thread-specific data key. </i><br />
 union <code>globus_thread_once_t</code><br />
 <i>Thread once structure. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_THREAD_ONCE_INIT</code> { .none = 0 }<br />
 <i>Thread once initializer value. </i><br />
 #define <code>GLOBUS_THREAD_CANCEL_DISABLE</code> 0<br />
 <i>Disable thread cancellation value. </i><br />
 #define <code>GLOBUS_THREAD_CANCEL_ENABLE</code> 1<br />
 <i>Enable thread cancellation value. </i><br />
 #define <code>GLOBUS_THREAD_MODULE</code> (&amp;globus_i_thread_module)<br />
 <i>Thread Module. </i></p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_thread_key_destructor_func_t</code> )(void *value)<br />
 <i>Thread-specific data destructor. </i></p>
<h3>Functions</h3>
<p> int <code>globus_thread_set_model</code> (const char *model)<br />
 <i>Select threading model for an application. </i><br />
 int <code>globus_mutex_init</code> (<code>globus_mutex_t</code> *mutex, <code>globus_mutexattr_t</code> *attr)<br />
 <i>Initialize a mutex. </i><br />
 int <code>globus_mutex_destroy</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Destroy a mutex. </i><br />
 int <code>globus_mutex_lock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Lock a mutex. </i><br />
 int <code>globus_mutex_unlock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Unlock a mutex. </i><br />
 int <code>globus_mutex_trylock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Lock a mutex if it is not locked. </i><br />
 int <code>globus_cond_init</code> (<code>globus_cond_t</code> *cond, <code>globus_condattr_t</code> *attr)<br />
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
<p> The <code>globus_condattr_getspace()</code> function copies the value of the callback space associated with a condition variable attribute to the integer pointed to by the <i>space</i> parameter. &quot;<br />
 int <code>globus_thread_create</code> (<code>globus_thread_t</code> *thread, <code>globus_threadattr_t</code> *attr, globus_thread_func_t func, void *user_arg)<br />
 <i>Create a new thread. </i><br />
 void * <code>globus_thread_getspecific</code> (<code>globus_thread_key_t</code> key)<br />
 <i>Get a thread-specific data value. </i><br />
 int <code>globus_thread_setspecific</code> (<code>globus_thread_key_t</code> key, void *value)<br />
 <i>Set a thread-specific data value. </i><br />
 int <code>globus_thread_key_create</code> (<code>globus_thread_key_t</code> *key, <code>globus_thread_key_destructor_func_t</code> func)<br />
 <i>Create a key for thread-specific storage. </i><br />
 int <code>globus_thread_key_delete</code> (<code>globus_thread_key_t</code> key)<br />
 <i>Delete a thread-local storage key. </i><br />
 int <code>globus_thread_once</code> (<code>globus_thread_once_t</code> *once, void(*init_routine)(void))<br />
 <i>Execute a function one time. </i><br />
 void <code>globus_thread_yield</code> (void)<br />
 <i>Yield execution to another thread. </i><br />
 int <code>globus_thread_sigmask</code> (int how, const sigset_t *newmask, sigset_t *oldmask)<br />
 <i>Modify the current thread&#8217;s signal mask. </i><br />
 int <code>globus_thread_kill</code> (<code>globus_thread_t</code> thread, int sig)<br />
 <i>Send a signal to a thread. </i><br />
 void <code>globus_thread_exit</code> (void *value)<br />
 <i>Terminate the current thread. </i><br />
 <code>globus_thread_t</code> <code>globus_thread_self</code> (void)<br />
 <i>Determine the current thread&#8217;s ID. </i><br />
 int <code>globus_thread_equal</code> (<code>globus_thread_t</code> thread1, <code>globus_thread_t</code> thread2)<br />
 <i>Check whether thread identifiers match. </i><br />
 <code>globus_bool_t</code> <code>globus_i_am_only_thread</code> (void)<br />
 <i>Determine if threads are supported. </i><br />
 <code>globus_bool_t</code> <code>globus_thread_preemptive_threads</code> (void)<br />
 <i>Indicate whether the active thread model supports preemption. </i><br />
 void * <code>globus_thread_cancellable_func</code> (void *(*func)(void *), void *arg, void(*cleanup_func)(void *), void *cleanup_arg, <code>globus_bool_t</code> execute_cleanup)<br />
 <i>Execute a function with thread cleanup in case of cancellation. </i><br />
 int <code>globus_thread_cancel</code> (<code>globus_thread_t</code> thr)<br />
 <i>Cancel a thread. </i><br />
 void <code>globus_thread_testcancel</code> (void)<br />
 <i>Thread cancellation point. </i><br />
 int <code>globus_thread_setcancelstate</code> (int state, int *oldstate)<br />
 <i>Set the thread&#8217;s cancellable state. </i></p>
<h2>Detailed Description</h2>
<p> Globus Threading Abstraction. </p>
<p> Globus threads package which can work with either pthreads or without threads, depending on runtime configuration</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
