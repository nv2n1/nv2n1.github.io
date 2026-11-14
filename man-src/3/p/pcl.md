---
title: "pcl(3)"
name: "pcl"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcl/"
description: "co_thread_init, co_thread_cleanup, co_create, co_call, co_resume, co_delete, co_exit_to, co_exit, co_current, co_get_data, co_set_data – C coroutine management"
---

<p>co_thread_init, co_thread_cleanup, co_create, co_call, co_resume, co_delete, co_exit_to, co_exit, co_current, co_get_data, co_set_data &#8211; C coroutine management </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcl.h&gt;

int co_thread_init(void);

void co_thread_cleanup(void);
coroutine_t co_create(void *func, void *data, void *stack, int stacksize);
void co_delete(coroutine_t co);
void co_call(coroutine_t co);
void co_resume(void);
void co_exit_to(coroutine_t co);
void co_exit(void);
coroutine_t co_current(void);
void *co_get_data(coroutine_t co);
void *co_set_data(coroutine_t co, void *data);</code></pre>
<p> Link with <i>-lpthread</i> if you are using a multi-thread version of <code>PCL</code>.</p>
<h2>Description</h2>
<p>The <code>Portable Coroutine Library (PCL)</code> implements the low level functionality for coroutines. For a definition of the term <code>coroutine</code> see <i>The Art of Computer Programming</i> by <i>Donald E. Knuth</i>. Coroutines are a very simple cooperative multitasking environment where the switch from one task to another is done explicitly by a function call. Coroutines are a lot faster than processes or threads switch, since there is no OS kernel involvement for the operation. This document defines an API for the low level handling of coroutines i.e. creating and deleting coroutines and switching between them. Higher level functionality (scheduler, etc.) is not covered.</p>
<h3>Functions</h3>
<p>The following functions are defined:</p>
<dl>
<dt><code>int co_thread_init(void);</code></p>
<dd>If the <code>PCL</code> library is built in multi-thread mode, and if multi threads are actually used, this function should be called before calling any <code>PCL</code> function. If the <code>PCL</code> library is built in multi-thread mode, but it is used only from one thread (the main one, likely), then it is possible to avoid to call <code>co_thread_init</code>(). Returns 0 in case of success, or an negative error code in case of error.</p>
<dt><code>void co_thread_cleanup(void);</code></p>
<dd>If the <code>PCL</code> library is built in multi-thread mode, and if multi threads are actually used, this function should be called before the thread exits, or whenever the thread decides it won&#8217;t call the <code>PCL</code> functions anymore. A failure in calling <code>co_thread_cleanup</code>() will result in resource leakage by the calling application.</p>
<dt><code>coroutine_t co_create(void *</code><i>func</i><code>, void *</code><i>data</i><code>, void *</code><i>stack</i><code>, int </code><i>stacksize</i><code>);</code></p>
<dd>This function creates a new coroutine. <i>func</i> is the entry point of the coroutine. It will be called with one arg, a <code>void *</code>, which holds the data passed through the <i>data</i> parameter. If <i>func</i> terminates, the associated coroutine is deleted. <i>stack</i> is the base of the stack this coroutine will use and <i>stacksize</i> its size in bytes. You may pass a <code>NULL</code> pointer for <i>stack</i> in which case the memory will be allocated by <code>co_create</code> itself. Both, <i>stack</i> and <i>stacksize</i> are aligned to system requirements. A <i>stacksize</i> of less then 4096 bytes will be rejected. You have to make sure, that the stack is large enough for your coroutine and possible signal handlers (see below). The stack will not grow! (Exception: the main coroutine uses the standard system stack which may still grow) On success, a handle (<code>coroutine_t</code>) for a new coroutine is returned, otherwise <code>NULL</code>. void *co_set_data(coroutine_t co, void *data); This function deletes the given coroutine <i>co</i>. If the stack for this coroutine was allocated by <code>co_create</code> it will be freed. After a coroutine handle was passed to <code>co_delete</code> it is invalid and may not be used any more. It is invalid for a coroutine to delete itself with this function.  This function passes execution to the given coroutine <i>co</i>. The first time the coroutine is executed, its entry point <i>func</i> is called, and the <i>data</i> parameter used during the call to <code>co_create</code> is passed to <i>func</i>. The current coroutine is suspended until another one restarts it with a <code>co_call</code> or <code>co_resume</code> call. Calling oneself returns immediately. void *co_set_data(coroutine_t co, void *data); This function passes execution back to the coroutine which either initially started this one or restarted it after a prior <code>co_resume</code>.  This function does the same a <code>co_delete(co_current())</code> followed by a <code>co_call</code> would do. That is, it deletes itself and then passes execution to another coroutine <i>co</i>. void *co_set_data(coroutine_t co, void *data); This function does the same a <code>co_delete(co_current())</code> followed by a <code>co_resume</code> would do. That is, it deletes itself and then passes execution back to the coroutine which either initially started this one or restarted it after a prior <code>co_resume</code>.</p>
<dt><code>coroutine_t co_current(void);</code></p>
<dd>This function returns the currently running coroutine.  This function returns the data associated with the <i>co</i><br />
&nbsp;<wbr>coroutine. The data associated with a coroutine is the <i>data</i> parameter passed to <code>co_create</code>(). </p>
<pre><code>void *co_set_data(coroutine_t co, void *data);</code></pre>
<p> Sets the <i>data</i> associated with the <i>co</i> coroutine, and returns the previously associated data.</dl>
<h3>Notes</h3>
<p>Some interactions with other parts of the system are covered here.</p>
<dl>
<dt><code>Threads</code></p>
<dd>If the <code>PCL</code> library has been built in multi-thread mode, then it is possible to use it in multi-thread software. A thread should call <code>co_thread_init</code>() before using the <code>PCL</code> APIs, and call <code>co_thread_cleanup</code>() before exiting, or when it has done using the <code>PCL</code> APIs.<br />
 <code>WARNING:</code> For no reason should two different threads run the same coroutine at the same time.</p>
<dt><code>Signals</code></p>
<dd>First, a signal handler is not defined to run in any specific coroutine. The only way to leave the signal handler is by a return statement. Second, the signal handler may run with the stack of any coroutine, even with the stack of library internal coroutines which have an undefined stack size (just enough to perform a kernel call). Using and alternate stack for signal processing (see <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)) is recommended! Conclusion: avoid signals like a plague. The only thing you may do reliable is setting some global variables and return. Simple kernel calls may work too, but nowadays it&#8217;s pretty hairy to tell, which function really is a kernel call. (Btw, all this applies to normal C programs, too. The coroutines just add one more problem)</p>
<dt><code>setjmp</code>/<code>longjmp</code></p>
<dd>The use of <code><a href="/docs/linux/man/2-setjmp/">setjmp</a></code>(2)/<code><a href="/docs/linux/man/2-longjmp/">longjmp</a></code>(2) is limited to jumping inside one coroutine. Never try to jump from one coroutine to another with <code><a href="/docs/linux/man/2-longjmp/">longjmp</a></code>(2). </p>
<h2>Diagnostics</h2>
<p>Some fatal errors are caught by the library. If one occurs, a short message is written to file descriptor 2 (stderr) and a segmentation violation is generated.</p>
<dl>
<dt><code>[PCL]: Cannot delete itself</code></p>
<dd>A coroutine has called <code>co_delete</code> with it&#8217;s own handle.</p>
<dt><code>[PCL]: Resume to deleted coroutine</code></p>
<dd>A coroutine has deleted itself with <code>co_exit</code> or <code>co_exit_to</code> and the coroutine that was activated by the exit tried a <code>co_resume</code>.</p>
<dt><code>[PCL]: Stale coroutine called</code></p>
<dd>Someone tried to active a coroutine that has already been deleted. This error is only detected, if the stack of the deleted coroutine is still resident in memory.</p>
<dt><code>[PCL]: Context switch failed</code></p>
<dd>Low level error generated by the library in case a context switch between two coroutines failes. </p>
</dl>
<h2>See Also</h2>
<p>Original <code>coroutine</code> library at <code><a rel="nofollow" href="http://www.goron.de/~froese/coro/coro.html">http://www.goron.de/~froese/coro/coro.html</a></code> . GNU Pth library at <code><a rel="nofollow" href="http://www.gnu.org/software/pth/">http://www.gnu.org/software/pth/</a></code> . </p>
<h2>Author</h2>
<p>Developed by Davide Libenzi &lt; <code>davidel [at] xmailserver.org</code> &gt;.<br />
 Ideas and man page base source taken by the coroutine library developed by E. Toernig &lt; <code>froese [at] gmx.de</code> &gt;.<br />
 Also some code and ideas comes from the GNU Pth library available at <code><a rel="nofollow" href="http://www.gnu.org/software/pth/">http://www.gnu.org/software/pth/</a></code> .</p>
<h2>Bugs</h2>
<p>There are no known bugs. But, this library is still in development even if it results very stable and pretty much ready for production use. Bug reports and comments to Davide Libenzi &lt; <code>davidel [at] xmailserver.org</code> &gt;. </p>
