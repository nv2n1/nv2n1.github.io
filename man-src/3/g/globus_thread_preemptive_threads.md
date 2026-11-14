---
title: "globus_thread_preemptive_threads(3)"
name: "globus_thread_preemptive_threads"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_thread_preemptive_threads/"
description: "Threading –"
---

<h2 class="name">NAME</h2>
<p> Threading &#8211; </p>
<p> Portable Thread Abstraction.</p>
<h3>Modules</h3>
<p> <code>Mutual Exclusion</code> </p>
<p> <code>Condition Variables</code> </p>
<p> <code>Thread-Specific Storage</code> </p>
<p> <code>One-time execution</code> </p>
<h3>Data Structures</h3>
<p> union <code>globus_thread_t</code><br />
 <i>Thread ID. </i><br />
 union <code>globus_threadattr_t</code><br />
 <i>Thread attributes. </i><br />
 union <code>globus_thread_key_t</code><br />
 <i>Thread-specific data key. </i></p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_THREAD_CANCEL_DISABLE</code> 0<br />
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
 int <code>globus_thread_create</code> (<code>globus_thread_t</code> *thread, <code>globus_threadattr_t</code> *attr, globus_thread_func_t func, void *user_arg)<br />
 <i>Create a new thread. </i><br />
 void <code>globus_thread_yield</code> (void)<br />
 <i>Yield execution to another thread. </i><br />
 void <code>globus_thread_exit</code> (void *value)<br />
 <i>Terminate the current thread. </i><br />
 int <code>globus_thread_sigmask</code> (int how, const sigset_t *new_mask, sigset_t *old_mask)<br />
 <i>Modify the current thread&#8217;s signal mask. </i><br />
 int <code>globus_thread_kill</code> (<code>globus_thread_t</code> thread, int sig)<br />
 <i>Send a signal to a thread. </i><br />
 <code>globus_thread_t</code> <code>globus_thread_self</code> (void)<br />
 <i>Determine the current thread&#8217;s ID. </i><br />
 <code>globus_bool_t</code> <code>globus_thread_equal</code> (<code>globus_thread_t</code> thread1, <code>globus_thread_t</code> thread2)<br />
 <i>Check whether thread identifiers match. </i><br />
 <code>globus_bool_t</code> <code>globus_thread_preemptive_threads</code> (void)<br />
 <i>Indicate whether the active thread model supports preemption. </i><br />
 <code>globus_bool_t</code> <code>globus_i_am_only_thread</code> (void)<br />
 <i>Determine if threads are supported. </i><br />
 void * <code>globus_thread_cancellable_func</code> (void *(*func)(void *), void *arg, void(*cleanup_func)(void *), void *cleanup_arg, <code>globus_bool_t</code> execute_cleanup)<br />
 <i>Execute a function with thread cleanup in case of cancellation. </i><br />
 int <code>globus_thread_cancel</code> (<code>globus_thread_t</code> thr)<br />
 <i>Cancel a thread. </i><br />
 void <code>globus_thread_testcancel</code> (void)<br />
 <i>Thread cancellation point. </i><br />
 int <code>globus_thread_setcancelstate</code> (int state, int *oldstate)<br />
 <i>Set the thread&#8217;s cancellable state. </i></p>
<h2>Detailed Description</h2>
<p> Portable Thread Abstraction. </p>
<p> The Globus runtime includes support for portably creating threads on POSIX and Windows systems. It also provides a callback-driven system for applications that may use threads but don&#8217;t require them. The Globus Thread API is modeled closely after the POSIX threads API. </p>
<p> Applications can choose whether to run as threaded or non-threaded at runtime by either setting the GLOBUS_THREAD_MODEL environment variable or calling the <code>globus_thread_set_model()</code> function prior to activating any Globus modules. </p>
<p> The Globus thread system provides primitives for mutual exclusion (<code>globus_mutex_t</code>, <code>globus_rmutex_t</code>, globus_rw_mutex_t), event synchronization (<code>globus_cond_t</code>), one-time execution (globus_once_t), and threading (<code>globus_thread_t</code>). </p>
<p> In non-threaded operation, <code>globus_cond_wait()</code> and its variants will poll the callback queue and I/O system to allow event-driven programs to run in the absence of threads. The <code>globus_thread_create()</code> function will fail in that model. Other primitive operations will return success but not provide any thread exclusion as there is only one thread.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_THREAD_CANCEL_DISABLE 0</h3>
<p> Disable thread cancellation value. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_thread_setcancelstate()</code></dl>
<h3>#define GLOBUS_THREAD_CANCEL_ENABLE 1</h3>
<p> Enable thread cancellation value. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_thread_setcancelstate()</code></dl>
<h2>Function Documentation</h2>
<h3><code>globus_bool_t</code> globus_i_am_only_thread (void)</h3>
<p> Determine if threads are supported. The <code>globus_i_am_only_thread()</code> function determines whether multiple threads may be running in this process. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_i_am_only_thread()</code> function returns GLOBUS_TRUE if the current thread model is the &#8216;none&#8217; thread model; GLOBUS_FALSE otherwise.</dl>
<h3>int globus_thread_cancel (<code>globus_thread_t</code>thr)</h3>
<p> Cancel a thread. The <code>globus_thread_cancel()</code> function cancels the thread with the identifier <i>thr</i> if it is still executing. If it is running with a cancellation cleanup stack, the functions in that stack are executed. The target thread&#8217;s cancel state determines when the cancellation is delivered. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>thr</i> The id of the thread to cancel</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, the <code>globus_thread_cancel()</code> function delivers the cancellation to the target thread and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_cancel()</code> returns an implementation-specific non-zero error value.</dl>
<h3>void* globus_thread_cancellable_func (void *(*)(void *)func, void *arg, void(*)(void *)cleanup_func, void *cleanup_arg, <code>globus_bool_t</code>execute_cleanup)</h3>
<p> Execute a function with thread cleanup in case of cancellation. The <code>globus_thread_cancellable_func()</code> function provides an interface to POSIX thread cancellation points that does not rely on preprocessor macros. It is roughly equivalent to </p>
<pre><code>
*pthread_cleanup_push(cleanup_func, cleanup_arg);
*(*func)(arg);
*pthread_cleanup_pop(execute_cleanup)
    *
</code></pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>func</i> Pointer to a function which may be cancelled.<br />
 <i>arg</i> Parameter to the <i>func</i> function.<br />
 <i>cleanup_func</i> Pointer to a function to execute if thread cancellation occurs during <i>func</i>.<br />
 <i>cleanup_arg</i> Parameter to the <i>cleanup_func</i> function.<br />
 <i>execute_cleanup</i> Flag indicating whether the function pointed to by <i>cleanup_func</i> should be executed after <i>func</i> completes even if it is not cancelled.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> <code>globus_thread_cancellable_func()</code> returns the value returned by <i>func</i>.</dl>
<h3>int globus_thread_create (<code>globus_thread_t</code> *thread, <code>globus_threadattr_t</code> *attr, globus_thread_func_tfunc, void *user_arg)</h3>
<p> Create a new thread. The <code>globus_thread_create()</code> function creates a new thread of execution in the current process to run the function pointed to by the <i>func</i> parameter passed the <i>user_arg</i> value as its only parameter. This new thread will be detached, so that storage associated with the thread will be automatically reclaimed by the operating system. A thread identifier will be copied to the value pointed by the <i>thread</i> parameter if it is non-NULL. The caller may use this thread identifier to signal or cancel this thread. The <i>attr</i> parameter is ignored by this function. If the &#8216;none&#8217; threading model is used by an application, then this function will always fail. One alternative that will work both with and without threads is to use the functions in the <code>Globus Callback API </code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>thread</i> Pointer to a variable to contain the new thread&#8217;s identifier.<br />
 <i>attr</i> Ignored<br />
 <i>func</i> Pointer to a function to start in the new thread.<br />
 <i>user_arg</i> Argument to the new thread&#8217;s function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_create()</code> will start a new thread, invoking (*func)(user_arg), modify the value pointed to by the <i>thread</i> parameter to contain the new thread&#8217;s identifier and return GLOBUS_SUCCESS. If an error occurs, then the value of <i>thread</i> is undefined and <code>globus_thread_create()</code> returns an implementation-specific non-zero error value.</dl>
<h3><code>globus_bool_t</code> globus_thread_equal (<code>globus_thread_t</code>thread1, <code>globus_thread_t</code>thread2)</h3>
<p> Check whether thread identifiers match. The <code>globus_thread_equal()</code> function checks whether the thread identifiers passed as the <i>thread1</i> and <i>thread2</i> parameters refer to the same thread. If so, <code>globus_thread_equal()</code> returns GLOBUS_TRUE; otherwise GLOBUS_FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>thread1</i> Thread identifier to compare.<br />
 <i>thread2</i> Thread identifier to compare.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_TRUE</i> thread1 and thread2 refer to the same thread.<br />
 <i>GLOBUS_TRUE</i> thread1 and thread2 do not refer to the same thread.</dl>
<h3>void globus_thread_exit (void *value)</h3>
<p> Terminate the current thread. The <code>globus_thread_exit()</code> terminates the current thread with the value passed to it. This function does not return.</p>
<h3>int globus_thread_kill (<code>globus_thread_t</code>thread, intsig)</h3>
<p> Send a signal to a thread. The <code>globus_thread_kill()</code> function sends the signal specified by the <i>sig</i> number to the thread whose ID matches the <i>thread</i> parameter. Depending on the signal mask of that thread, this may result in a signal being delivered or not, and depending on the process&#8217;s signal actions, a signal handler, termination, or no operation will occur in that thread. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>thread</i> The thread identifier of the thread to signal.<br />
 <i>sig</i> The signal to send to the thread.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_kill()</code> queues the signal for delivery to the specified thread and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_kill()</code> returns an implementation-specific non-zero error value.</dl>
<h3><code>globus_bool_t</code> globus_thread_preemptive_threads (void)</h3>
<p> Indicate whether the active thread model supports preemption. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_thread_preemptive_threads()</code> function returns GLOBUS_TRUE if the current thread model supports thread preemption; otherwise it returns GLOBUS_FALSE.</dl>
<h3><code>globus_thread_t</code> globus_thread_self (void)</h3>
<p> Determine the current thread&#8217;s ID. The <code>globus_thread_self()</code> function returns the thread identifier of the current thread. This value is unique among all threads which are running at any given time. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_thread_self()</code> function returns the current thread&#8217;s ID.</dl>
<h3>int globus_thread_set_model (const char *model)</h3>
<p> Select threading model for an application. The <code>globus_thread_set_model()</code> function selects which runtime model the current application will use. By default, the Globus runtime uses a non-threaded model. Additional models may be available based on system support: pthread, or windows. This function must be called prior to activating any globus module, as it changes how certain functions (like <code>globus_mutex_lock()</code> and <code>globus_cond_wait()</code>) behave. This function overrides the value set by the GLOBUS_THREAD_MODEL environment variable. </p>
<p> The <code>globus_thread_set_model()</code> function will fail if a Globus module has been activated already. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>model</i> The name of the thread model to use. Depending on operating system capabilities, this may be &#8216;none&#8217;, &#8216;pthread&#8217;, &#8216;windows&#8217;, or some other custom thread implementation. The corresponding libtool module &#8216;libglobus_thread_pthread.la&#8217; or &#8216;libglobus_thread_windows.la&#8217; must be installed on the system for it to be used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_set_model()</code> sets the name of the thread model to use and returns GLOBUS_SUCCESS. If an error occurs, then <code>globus_thread_set_model()</code> returns GLOBUS_FAILURE.</dl>
<h3>int globus_thread_setcancelstate (intstate, int *oldstate)</h3>
<p> Set the thread&#8217;s cancellable state. The <code>globus_thread_setcancelstate()</code> function sets the current cancellation state to either GLOBUS_THREAD_CANCEL_DISABLE or GLOBUS_THREAD_CANCEL_ENABLE, do control whether <code>globus_thread_cancel()</code> is able to cancel this thread. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>state</i> The desired cancellation state. If the value is GLOBUS_THREAD_CANCEL_DISABLE, then cancellation will be disabled for this thread. If the value is GLOBUS_THREAD_CANCEL_ENABLE, then cancellation will be enabled for this thread.<br />
 <i>oldstate</i> A pointer to a value which will be set to the value of the thread&#8217;s cancellation state when this function call began. This may be NULL if the caller is not interested in the previous value.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, the <code>globus_thread_setcancelstate()</code> function modifies the thread cancellation state, modifies oldstate (if non-NULL) to the value of its previous state, and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_setcancelstate()</code> returns an implementation-specific non-zero error value.</dl>
<h3>int globus_thread_sigmask (inthow, const sigset_t *new_mask, sigset_t *old_mask)</h3>
<p> Modify the current thread&#8217;s signal mask. The <code>globus_thread_sigmask()</code> function modifies the current thread&#8217;s signal mask and returns the old value of the signal mask in the value pointed to by the <i>old_mask</i> parameter. The <i>how</i> parameter can be one of SIG_BLOCK, SIG_UNBLOCK, or SIG_SETMASK to control how the signal mask is modified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>how</i> Flag indicating how to interpret <i>new_mask</i> if it is non-NULL. If <i>how</i> is SIG_BLOCK, then all signals in <i>new_mask</i> are blocked, as well as any which were previously blocked. If <i>how</i> is SIG_UNBLOCK, then all signals in which were previously blocked in <i>new_mask</i> are unblocked. If <i>how</i> is SIG_SETMASK, then the old signal mask is replaced with the value of <i>new_mask</i>.<br />
 <i>new_mask</i> Set of signals to block or unblock, based on the <i>how</i> parameter.<br />
 <i>old_mask</i> A pointer to be set to the old signal mask associated with the current thread.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_thread_sigmask()</code> modifies the signal mask, modifies the value pointed to by <i>old_mask</i> with the signal mask prior to this function&#8217;s execution and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_thread_sigmask()</code> returns an implementation-specific non-zero error value.</dl>
<h3>void globus_thread_testcancel (void)</h3>
<p> Thread cancellation point. The <code>globus_thread_testcancel()</code> function acts as a cancellation point for the current thread. If a thread has called <code>globus_thread_cancel()</code> and cancellation is enabled, this will cause the thread to be cancelled and any functions on the thread&#8217;s cleanup stack to be executed. This function will not return if the thread is cancelled.</p>
<h3>void globus_thread_yield (void)</h3>
<p> Yield execution to another thread. The <code>globus_thread_yield()</code> function yields execution to other threads which are ready for execution. The current thread may continue to execute if there are no other threads in the system&#8217;s ready queue.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBA">Author</a></p>
<dd></dl>
