---
title: "pthread_spin_destroy(3)"
name: "pthread_spin_destroy"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_spin_destroy/"
description: "pthread_spin_init, pthread_spin_destroy – initialize or destroy a spin lock"
---

<p>pthread_spin_init, pthread_spin_destroy &#8211; initialize or destroy a spin lock</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_spin_init(pthread_spinlock_t *lock, int pshared);
int pthread_spin_destroy(pthread_spinlock_t *lock);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_spin_init</code>(), <code>pthread_spin_destroy</code>(): </p>
<dl>
<dd>_POSIX_C_SOURCE &gt;= 200112L</dl>
<h2>Description</h2>
<p><i>General note</i>: Most programs should use mutexes instead of spin locks. Spin locks are primarily useful in conjunction with real-time scheduling policies. See NOTES. </p>
<p> The <code>pthread_spin_init</code>() function allocates any resources required for the use of the spin lock referred to by <i>lock</i> and initializes the lock to be in the unlocked state. The <i>pshared</i> argument must have one of the following values:</p>
<dl>
<dt><code>PTHREAD_PROCESS_PRIVATE</code></p>
<dd>The spin lock is to be operated on only by threads in the same process as the thread that calls <code>pthread_spin_init</code>(). (Attempting to share the spin lock between processes results in undefined behavior.)</p>
<dt><code>PTHREAD_PROCESS_SHARED</code></p>
<dd>The spin lock may be operated on by any thread in any process that has access to the memory containing the lock (i.e., the lock may be in a shared memory object that is shared among multiple processes).</dl>
<p> Calling <code>pthread_spin_init</code>() on a spin lock that has already been initialized results in undefined behavior. </p>
<p> The <code>pthread_spin_destroy</code>() function destroys a previously initialized spin lock, freeing any resources that were allocated for that lock. Destroying a spin lock that has not been previously been initialized or destroying a spin lock while another thread holds the lock results in undefined behavior. </p>
<p> Once a spin lock has been destroyed, performing any operation on the lock other than once more initializing it with <code>pthread_spin_init</code>() results in undefined behavior. </p>
<p> The result of performing operations such as <code><a href="/docs/linux/man/3-pthread_spin_lock/">pthread_spin_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_unlock/">pthread_spin_unlock</a></code>(3), and <code>pthread_spin_destroy</code>() on <i>copies</i> of the object referred to by <i>lock</i> is undefined.</p>
<h2>Return Value</h2>
<p>On success, there functions return zero. On failure, they return an error number. In the event that <code>pthread_spin_init</code>() fails, the lock is not initialized.</p>
<h2>Errors</h2>
<p><code>pthread_spin_init</code>() may fail with the following errors:</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd>The system has insufficient resources to initialize a new spin lock.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory to initialize the spin lock.</dl>
<h2>Versions</h2>
<p>These functions first appeared in glibc in version 2.2.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2001. </p>
<p> Support for process-shared spin locks is a POSIX option. The option is supported in the glibc implementation.</p>
<h2>Notes</h2>
<p>Spin locks should be employed in conjunction with real-time scheduling policies (<code>SCHED_FIFO</code>, or possibly <code>SCHED_RR</code>). Use of spin locks with nondeterministic scheduling policies such as <code>SCHED_OTHER</code> probably indicates a design mistake. The problem is that if a thread operating under such a policy is scheduled off the CPU while it holds a spin lock, then other threads will waste time spinning on the lock until the lock holder is once more rescheduled and releases the lock. </p>
<p> If threads create a deadlock situation while employing spin locks, those threads will spin forever consuming CPU time. </p>
<p> User-space spin locks are <i>not</i> applicable as a general locking solution. They are, by definition, prone to priority inversion and unbounded spin times. A programmer using spin locks must be exceptionally careful not only in the code, but also in terms of system configuration, thread placement, and priority assignment.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_mutex_init/">pthread_mutex_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_lock/">pthread_spin_lock</a></code>(3), <code><a href="/docs/linux/man/3-pthread_spin_unlock/">pthread_spin_unlock</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
