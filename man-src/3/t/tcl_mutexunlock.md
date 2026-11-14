---
title: "tcl_mutexunlock(3)"
name: "tcl_mutexunlock"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_mutexunlock/"
description: "Tcl_ConditionNotify, Tcl_ConditionWait, Tcl_ConditionFinalize, Tcl_GetThreadData, Tcl_MutexLock, Tcl_MutexUnlock, Tcl_MutexFinalize, Tcl_CreateThread, Tcl_JoinThread – Tcl thread support"
---

<p>Tcl_ConditionNotify, Tcl_ConditionWait, Tcl_ConditionFinalize, Tcl_GetThreadData, Tcl_MutexLock, Tcl_MutexUnlock, Tcl_MutexFinalize, Tcl_CreateThread, Tcl_JoinThread &#8211; Tcl thread support </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_ConditionNotify</code>(<i>condPtr</i>)
void
<code>Tcl_ConditionWait</code>(<i>condPtr, mutexPtr, timePtr</i>)
void
<code>Tcl_ConditionFinalize</code>(<i>condPtr</i>)
Void *
<code>Tcl_GetThreadData</code>(<i>keyPtr, size</i>)
void
<code>Tcl_MutexLock</code>(<i>mutexPtr</i>)
void
<code>Tcl_MutexUnlock</code>(<i>mutexPtr</i>)
void
<code>Tcl_MutexFinalize</code>(<i>mutexPtr</i>)
int
<code>Tcl_CreateThread</code>(<i>idPtr, threadProc, clientData, stackSize, flags</i>)
int
<code>Tcl_JoinThread</code>(<i>id, result</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Condition <i>*condPtr</i> (in) A condition variable, which must be associated with a mutex lock.</p>
<dd>Tcl_Mutex <i>*mutexPtr</i> (in) A mutex lock.</p>
<dd>Tcl_Time <i>*timePtr</i> (in) A time limit on the condition wait. NULL to wait forever. Note that a polling value of 0 seconds does not make much sense.</p>
<dd>Tcl_ThreadDataKey <i>*keyPtr</i> (in) This identifies a block of thread local storage. The key should be static and process-wide, yet each thread will end up associating a different block of storage with this key.</p>
<dd>int <i>*size</i> (in) The size of the thread local storage block. This amount of data is allocated and initialized to zero the first time each thread calls <code>Tcl_GetThreadData</code>.</p>
<dd>Tcl_ThreadId <i>*idPtr</i> (out) The referred storage will contain the id of the newly created thread as returned by the operating system.</p>
<dd>Tcl_ThreadId <i>id</i> (in) Id of the thread waited upon.</p>
<dd>Tcl_ThreadCreateProc <i>threadProc</i> (in) This procedure will act as the <code>main()</code> of the newly created thread. The specified <i>clientData</i> will be its sole argument.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary information. Passed as sole argument to the <i>threadProc</i>.</p>
<dd>int <i>stackSize</i> (in) The size of the stack given to the new thread.</p>
<dd>int <i>flags</i> (in) Bitmask containing flags allowing the caller to modify behaviour of the new thread.</p>
<dd>int <i>*result</i> (out) The referred storage is used to place the exit code of the thread waited upon into it.
</dl>
<h2>Introduction</h2>
<p>Beginning with the 8.1 release, the Tcl core is thread safe, which allows you to incorporate Tcl into multithreaded applications without customizing the Tcl core. To enable Tcl multithreading support, you must include the <code>&#8211;enable-threads</code> option to <code>configure</code> when you configure and compile your Tcl core. </p>
<p> An important constraint of the Tcl threads implementation is that <i>only the thread that created a Tcl interpreter can use that interpreter</i>. In other words, multiple threads can not access the same Tcl interpreter. (However, a single thread can safely create and use multiple interpreters.)</p>
<h2>Description</h2>
<p>Tcl provides <code>Tcl_CreateThread</code> for creating threads. The caller can determine the size of the stack given to the new thread and modify the behaviour through the supplied <i>flags</i>. The value <code>TCL_THREAD_STACK_DEFAULT</code> for the <i>stackSize</i> indicates that the default size as specified by the operating system is to be used for the new thread. As for the flags, currently only the values <code>TCL_THREAD_NOFLAGS</code> and <code>TCL_THREAD_JOINABLE</code> are defined. The first of them invokes the default behaviour with no specialties. Using the second value marks the new thread as <i>joinable</i>. This means that another thread can wait for the such marked thread to exit and join it. </p>
<p> Restrictions: On some UNIX systems the pthread-library does not contain the functionality to specify the stack size of a thread. The specified value for the stack size is ignored on these systems. Windows currently does not support joinable threads. This flag value is therefore ignored on this platform. </p>
<p> Tcl provides the <code>Tcl_ExitThread</code> and <code>Tcl_FinalizeThread</code> functions for terminating threads and invoking optional per-thread exit handlers. See the <code>Tcl_Exit</code> page for more information on these procedures. </p>
<p> The <code>Tcl_JoinThread</code> function is provided to allow threads to wait upon the exit of another thread, which must have been marked as joinable through usage of the <code>TCL_THREAD_JOINABLE</code>-flag during its creation via <code>Tcl_CreateThread</code>. </p>
<p> Trying to wait for the exit of a non-joinable thread or a thread which is already waited upon will result in an error. Waiting for a joinable thread which already exited is possible, the system will retain the necessary information until after the call to <code>Tcl_JoinThread</code>. This means that not calling <code>Tcl_JoinThread</code> for a joinable thread will cause a memory leak. </p>
<p> The <code>Tcl_GetThreadData</code> call returns a pointer to a block of thread-private data. Its argument is a key that is shared by all threads and a size for the block of storage. The storage is automatically allocated and initialized to all zeros the first time each thread asks for it. The storage is automatically deallocated by <code>Tcl_FinalizeThread</code>.</p>
<h3>Synchronization And Communication</h3>
<p>Tcl provides <code>Tcl_ThreadQueueEvent</code> and <code>Tcl_ThreadAlert</code> for handling event queuing in multithreaded applications. See the <code>Notifier</code> manual page for more information on these procedures. </p>
<p> A mutex is a lock that is used to serialize all threads through a piece of code by calling <code>Tcl_MutexLock</code> and <code>Tcl_MutexUnlock</code>. If one thread holds a mutex, any other thread calling <code>Tcl_MutexLock</code> will block until <code>Tcl_MutexUnlock</code> is called. A mutex can be destroyed after its use by calling <code>Tcl_MutexFinalize</code>. The result of locking a mutex twice from the same thread is undefined. On some platforms it will result in a deadlock. The <code>Tcl_MutexLock</code>, <code>Tcl_MutexUnlock</code> and <code>Tcl_MutexFinalize</code> procedures are defined as empty macros if not compiling with threads enabled. For declaration of mutexes the <code>TCL_DECLARE_MUTEX</code> macro should be used. This macro assures correct mutex handling even when the core is compiled without threads enabled. </p>
<p> A condition variable is used as a signaling mechanism: a thread can lock a mutex and then wait on a condition variable with <code>Tcl_ConditionWait</code>. This atomically releases the mutex lock and blocks the waiting thread until another thread calls <code>Tcl_ConditionNotify</code>. The caller of <code>Tcl_ConditionNotify</code> should have the associated mutex held by previously calling <code>Tcl_MutexLock</code>, but this is not enforced. Notifying the condition variable unblocks all threads waiting on the condition variable, but they do not proceed until the mutex is released with <code>Tcl_MutexUnlock</code>. The implementation of <code>Tcl_ConditionWait</code> automatically locks the mutex before returning. </p>
<p> The caller of <code>Tcl_ConditionWait</code> should be prepared for spurious notifications by calling <code>Tcl_ConditionWait</code> within a while loop that tests some invariant. </p>
<p> A condition variable can be destroyed after its use by calling <code>Tcl_ConditionFinalize</code>. </p>
<p> The <code>Tcl_ConditionNotify</code>, <code>Tcl_ConditionWait</code> and <code>Tcl_ConditionFinalize</code> procedures are defined as empty macros if not compiling with threads enabled.</p>
<h3>Initialization</h3>
<p>All of these synchronization objects are self-initializing. They are implemented as opaque pointers that should be NULL upon first use. The mutexes and condition variables are either cleaned up by process exit handlers (if living that long) or explicitly by calls to <code>Tcl_MutexFinalize</code> or <code>Tcl_ConditionFinalize</code>. Thread local storage is reclaimed during <code>Tcl_FinalizeThread</code>.</p>
<h2>Script-Level Access To Threads</h2>
<p>Tcl provides no built-in commands for scripts to use to create, manage, or join threads, nor any script-level access to mutex or condition variables. It provides such facilities only via C interfaces, and leaves it up to packages to expose these matters to the script level. One such package is the <code>Thread</code> package.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_getcurrentthread/">Tcl_GetCurrentThread</a>(3), <a href="/docs/linux/man/3-tcl_threadqueueevent/">Tcl_ThreadQueueEvent</a>(3), <a href="/docs/linux/man/3-tcl_threadalert/">Tcl_ThreadAlert</a>(3), <a href="/docs/linux/man/3-tcl_exitthread/">Tcl_ExitThread</a>(3), <a href="/docs/linux/man/3-tcl_finalizethread/">Tcl_FinalizeThread</a>(3), <a href="/docs/linux/man/3-tcl_createthreadexithandler/">Tcl_CreateThreadExitHandler</a>(3), <a href="/docs/linux/man/3-tcl_deletethreadexithandler/">Tcl_DeleteThreadExitHandler</a>(3), Thread</p>
<h2>Keywords</h2>
<p>thread, mutex, condition variable, thread local storage</p>
