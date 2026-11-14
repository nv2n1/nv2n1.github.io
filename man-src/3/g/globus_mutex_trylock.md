---
title: "globus_mutex_trylock(3)"
name: "globus_mutex_trylock"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_mutex_trylock/"
description: "Mutual Exclusion –"
---

<h2 class="name">NAME</h2>
<p> Mutual Exclusion &#8211; </p>
<h3>Data Structures</h3>
<p> union <code>globus_mutex_t</code><br />
 <i>Mutex. </i><br />
 union <code>globus_mutexattr_t</code><br />
 <i>Mutex attribute. </i><br />
 struct <code>globus_rmutex_t</code><br />
 <i>Recursive Mutex. </i></p>
<h3>Typedefs</h3>
<p> typedef int <code>globus_rmutexattr_t</code><br />
 <i>Recursive mutex attribute. </i></p>
<h3>Functions</h3>
<p> int <code>globus_mutex_init</code> (<code>globus_mutex_t</code> *mutex, <code>globus_mutexattr_t</code> *attr)<br />
 <i>Initialize a mutex. </i><br />
 int <code>globus_mutex_destroy</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Destroy a mutex. </i><br />
 int <code>globus_mutex_lock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Lock a mutex. </i><br />
 int <code>globus_mutex_unlock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Unlock a mutex. </i><br />
 int <code>globus_mutex_trylock</code> (<code>globus_mutex_t</code> *mutex)<br />
 <i>Lock a mutex if it is not locked. </i><br />
 int <code>globus_mutexattr_init</code> (<code>globus_mutexattr_t</code> *attr)<br />
 <i>Initialize a mutex attribute. </i><br />
 int <code>globus_mutexattr_destroy</code> (<code>globus_mutexattr_t</code> *attr)<br />
 <i>Destroy a mutex attribute. </i></p>
<h3>Recursive Mutex</h3>
<p> int <code>globus_rmutex_init</code> (<code>globus_rmutex_t</code> *rmutex, <code>globus_rmutexattr_t</code> *rattr)<br />
 <i>Initialize a recursive mutex. </i><br />
 int <code>globus_rmutex_lock</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Lock a recursive mutex. </i><br />
 int <code>globus_rmutex_unlock</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Unlock a recursive mutex. </i><br />
 int <code>globus_rmutex_destroy</code> (<code>globus_rmutex_t</code> *rmutex)<br />
 <i>Destroy a recursive mutex. </i></p>
<h2>Detailed Description</h2>
<p> The Globus runtime includes three portable, related mutual exclusion primitives that can be used in applications and libraries. These are</p>
<dl>
<dt>&bull;</p>
<dd> <code>globus_mutex_t</code>: a non-recursive, non-shared lock</p>
<dt>&bull;</p>
<dd> <code>globus_rmutex_t</code>: a recursive non-shared lock</p>
<dt>&bull;</p>
<dd> globus_rw_mutex_t: a reader-writer lock</dl>
<h2>Function Documentation</h2>
<h3>int globus_mutex_destroy (<code>globus_mutex_t</code> *mutex)</h3>
<p> Destroy a mutex. The <code>globus_mutex_destroy()</code> function destroys the mutex pointed to by its <i>mutex</i> parameter. After a mutex is destroyed it may no longer be used unless it is again initialized by <code>globus_mutex_init()</code>. Behavior is undefined if <code>globus_mutex_destroy()</code> is called with a pointer to a locked mutex. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mutex</i> The mutex to destroy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_mutex_destroy()</code> returns GLOBUS_SUCCESS. Otherwise, a non-zero implementation-specific error value is returned.</dl>
<h3>int globus_mutex_init (<code>globus_mutex_t</code> *mutex, <code>globus_mutexattr_t</code> *attr)</h3>
<p> Initialize a mutex. The <code>globus_mutex_init()</code> function creates a mutex variable that can be used for synchronization. Currently, the <i>attr</i> parameter is ignored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mutex</i> Pointer to the mutex to initialize.<br />
 <i>attr</i> Ignored.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_mutex_init()</code> initializes the mutex and returns GLOBUS_SUCCESS. Otherwise, a non-0 value is returned.</dl>
<h3>int globus_mutex_lock (<code>globus_mutex_t</code> *mutex)</h3>
<p> Lock a mutex. The <code>globus_mutex_lock()</code> function locks the mutex pointed to by its <i>mutex</i> parameter. </p>
<p> Upon successful return, the thread calling <code>globus_mutex_lock()</code> has an exclusive lock on the resources protected by <i>mutex</i>. Other threads calling <code>globus_mutex_lock()</code> will wait until that thread later calls <code>globus_mutex_unlock()</code> or <code>globus_cond_wait()</code> with that mutex. Depending on the thread model, calling globus_mutex_lock on a mutex locked by the current thread will either return an error or result in deadlock. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mutex</i> The mutex to lock.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_mutex_lock()</code> returns GLOBUS_SUCCESS. Otherwise, a non-zero implementation-specific error value is returned.</dl>
<h3>int globus_mutex_trylock (<code>globus_mutex_t</code> *mutex)</h3>
<p> Lock a mutex if it is not locked. The <code>globus_mutex_trylock()</code> function locks the mutex pointed to by its <i>mutex</i> parameter if no thread has already locked the mutex. If <i>mutex</i> is locked, then <code>globus_mutex_trylock()</code> returns EBUSY and does not block the current thread or lock the mutex. Upon successful return, the thread calling <code>globus_mutex_trylock()</code> has an exclusive lock on the resources protected by <i>mutex</i>. Other threads calling <code>globus_mutex_lock()</code> will wait until that thread later calls <code>globus_mutex_unlock()</code> or <code>globus_cond_wait()</code> with that mutex. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mutex</i> The mutex to lock.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_mutex_trylock()</code> returns GLOBUS_SUCCESS and locks the mutex. If another thread holds the lock, <code>globus_mutex_trylock()</code> returns EBUSY. Otherwise, a non-zero implementation-specific error value is returned.</dl>
<h3>int globus_mutex_unlock (<code>globus_mutex_t</code> *mutex)</h3>
<p> Unlock a mutex. The <code>globus_mutex_unlock()</code> function unlocks the mutex pointed to by its <i>mutex</i> parameter. Upon successful return, the thread calling <code>globus_mutex_unlock()</code> no longer has an exclusive lock on the resources protected by <i>mutex</i>. Another thread calling <code>globus_mutex_lock()</code> may be unblocked so that it may acquire the mutex. Behavior is undefined if globus_mutex_unlock is called with an unlocked mutex. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>mutex</i> The mutex to unlock.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_mutex_unlock()</code> returns GLOBUS_SUCCESS. Otherwise, a non-zero implementation-specific error value is returned.</dl>
<h3>int globus_mutexattr_destroy (<code>globus_mutexattr_t</code> *attr)</h3>
<p> Destroy a mutex attribute. The <code>globus_mutexattr_destroy()</code> function destroys the mutex attribute structure pointed to by its <i>attr</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute structure to destroy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_mutexattr_destroy()</code> returns GLOBUS_SUCCESS and modifies the attribute pointed to by <i>attr</i>. If an error occurs, <code>globus_mutexattr_destroy()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_mutexattr_init (<code>globus_mutexattr_t</code> *attr)</h3>
<p> Initialize a mutex attribute. The <code>globus_mutexattr_init()</code> function initializes the mutex attribute structure pointed to by its <i>attr</i> parameter. Currently there are no attribute values that can be set via this API, so there&#8217;s no real use to calling this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute structure to initialize.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_mutexattr_init()</code> returns GLOBUS_SUCCESS and modifies the attribute pointed to by <i>attr</i>. If an error occurs, <code>globus_mutexattr_init()</code> returns an implementation-specific non-zero error code.</dl>
<h3>int globus_rmutex_destroy (<code>globus_rmutex_t</code> *rmutex)</h3>
<p> Destroy a recursive mutex. </p>
<pre>
The globus_rmutex_destroy() function destroys a recursive mutex
If the mutex is currently locked, behavior is undefined.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rmutex</i> Mutex to unlock</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>int globus_rmutex_init (<code>globus_rmutex_t</code> *rmutex, <code>globus_rmutexattr_t</code> *rattr)</h3>
<p> Initialize a recursive mutex. </p>
<pre>
The globus_rmutex_init() function initializes a recursive mutex,
that is, one which may be locked multiple times by a single thread
without causing deadlock.
</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rmutex</i> A pointer to the mutex to initialize<br />
 <i>rattr</i> IGNORED</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_rmutex_init()</code> initializes the mutex and returns GLOBUS_SUCCESS; otherwise, it returns a non-zero error code.</dl>
<h3>int globus_rmutex_lock (<code>globus_rmutex_t</code> *rmutex)</h3>
<p> Lock a recursive mutex. </p>
<pre>
The globus_rmutex_lock() function acquires the lock controlled by
@a rmutex. This may be called multiple times in a single thread without 
causing deadlock, provided that a call to globus_rmutex_unlock() is
called the same number of times as globus_rmutex_lock(). Once acquired,
all other threads calling this function will be blocked until the
mutex is completely unlocked.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rmutex</i> A pointer to the mutex to lock</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> On success, <code>globus_rmutex_init()</code> increases the lock level for the mutex, blocks other threads trying to acquire the same mutex, and returns GLOBUS_SUCCESS; otherwise, it returns a non-zero error code.</dl>
<h3>int globus_rmutex_unlock (<code>globus_rmutex_t</code> *rmutex)</h3>
<p> Unlock a recursive mutex. </p>
<pre>
The globus_rmutex_unlock() function decrements the lock count for
the lock pointed to by @a rmutex. If the lock count is reduced to
zero, it also unblocks a thread which is trying to acquire the lock
if there is one.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rmutex</i> Mutex to unlock</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAT">Author</a></p>
<dd></dl>
