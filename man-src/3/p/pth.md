---
title: "pth(3)"
name: "pth"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pth/"
description: "pth – GNU Portable Threads"
---
<p> <code>pth</code> - GNU Portable Threads  </p>
<h2>VERSION</h2>
<p> <font SIZE="-1">GNU</font> Pth <font SIZE="-1">2.0.7 (08-Jun-2006)</font>  </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>Global Library Management</code></dt>
<dd> <p> pth_init, pth_kill, pth_ctrl, pth_version. </p>
 </dd>
<dt><code>Thread Attribute Handling</code></dt>
<dd> <p> pth_attr_of, pth_attr_new, pth_attr_init, pth_attr_set, pth_attr_get, pth_attr_destroy. </p>
 </dd>
<dt><code>Thread Control</code></dt>
<dd> <p> pth_spawn, pth_once, pth_self, pth_suspend, pth_resume, pth_yield, pth_nap, pth_wait, pth_cancel, pth_abort, pth_raise, pth_join, pth_exit. </p>
 </dd>
<dt><code>Utilities</code></dt>
<dd> <p> pth_fdmode, pth_time, pth_timeout, pth_sfiodisc. </p>
 </dd>
<dt><code>Cancellation Management</code></dt>
<dd> <p> pth_cancel_point, pth_cancel_state. </p>
 </dd>
<dt><code>Event Handling</code></dt>
<dd> <p> pth_event, pth_event_typeof, pth_event_extract, pth_event_concat, pth_event_isolate, pth_event_walk, pth_event_status, pth_event_free. </p>
 </dd>
<dt><code>Key-Based Storage</code></dt>
<dd> <p> pth_key_create, pth_key_delete, pth_key_setdata, pth_key_getdata. </p>
 </dd>
<dt><code>Message Port Communication</code></dt>
<dd> <p> pth_msgport_create, pth_msgport_destroy, pth_msgport_find, pth_msgport_pending, pth_msgport_put, pth_msgport_get, pth_msgport_reply. </p>
 </dd>
<dt><code>Thread Cleanups</code></dt>
<dd> <p> pth_cleanup_push, pth_cleanup_pop. </p>
 </dd>
<dt><code>Process Forking</code></dt>
<dd> <p> pth_atfork_push, pth_atfork_pop, pth_fork. </p>
 </dd>
<dt><code>Synchronization</code></dt>
<dd> <p> pth_mutex_init, pth_mutex_acquire, pth_mutex_release, pth_rwlock_init, pth_rwlock_acquire, pth_rwlock_release, pth_cond_init, pth_cond_await, pth_cond_notify, pth_barrier_init, pth_barrier_reach. </p>
 </dd>
<dt><code>User-Space Context</code></dt>
<dd> <p> pth_uctx_create, pth_uctx_make, pth_uctx_switch, pth_uctx_destroy. </p>
 </dd>
<dt><code>Generalized </code><font SIZE="-1"><code>POSIX</code></font><code> Replacement </code><font SIZE="-1"><code>API</code></font></dt>
<dd> <p> pth_sigwait_ev, pth_accept_ev, pth_connect_ev, pth_select_ev, pth_poll_ev, pth_read_ev, pth_readv_ev, pth_write_ev, pth_writev_ev, pth_recv_ev, pth_recvfrom_ev, pth_send_ev, pth_sendto_ev. </p>
 </dd>
<dt><code>Standard </code><font SIZE="-1"><code>POSIX</code></font><code> Replacement </code><font SIZE="-1"><code>API</code></font></dt>
<dd> <p> pth_nanosleep, pth_usleep, pth_sleep, pth_waitpid, pth_system, pth_sigmask, pth_sigwait, pth_accept, pth_connect, pth_select, pth_pselect, pth_poll, pth_read, pth_readv, pth_write, pth_writev, pth_pread, pth_pwrite, pth_recv, pth_recvfrom, pth_send, pth_sendto. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<pre><code>  ____ _ _
 | _ \| |_| |__
 | |_) | __| '_ \ ``Only those who attempt
 | __/| |_| | | | the absurd can achieve
 |_| \__|_| |_| the impossible.''
</code></pre>
<p> <code>Pth</code> is a very portable <font SIZE="-1">POSIX/ANSI-C</font> based library for Unix platforms which provides non-preemptive priority-based scheduling for multiple threads of execution (aka `multithreading&#8217;) inside event-driven applications. All threads run in the same address space of the application process, but each thread has its own individual program counter, run-time stack, signal mask and <code>&quot;errno&quot;</code> variable. </p>
<p>The thread scheduling itself is done in a cooperative way, i.e., the threads are managed and dispatched by a priority- and event-driven non-preemptive scheduler. The intention is that this way both better portability and run-time performance is achieved than with preemptive scheduling. The event facility allows threads to wait until various types of internal and external events occur, including pending I/O on file descriptors, asynchronous signals, elapsed timers, pending I/O on message ports, thread and process termination, and even results of customized callback functions. </p>
<p> <code>Pth</code> also provides an optional emulation <font SIZE="-1">API</font> for <font SIZE="-1">POSIX</font>.1c threads (`Pthreads&#8217;) which can be used for backward compatibility to existing multithreaded applications. See <code>Pth</code>&#8216;s <i>pthread</i>(3) manual page for details. <br />
 </p>
<p> <code>Threading Background</code> </p>
<p>When programming event-driven applications, usually servers, lots of regular jobs and one-shot requests have to be processed in parallel. To efficiently simulate this parallel processing on uniprocessor machines, we use `multitasking&#8217; --- that is, we have the application ask the operating system to spawn multiple instances of itself. On Unix, typically the kernel implements multitasking in a preemptive and priority-based way through heavy-weight processes spawned with <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2). These processes usually do <i>not</i> share a common address space. Instead they are clearly separated from each other, and are created by direct cloning a process address space (although modern kernels use memory segment mapping and copy-on-write semantics to avoid unnecessary copying of physical memory). </p>
<p>The drawbacks are obvious: Sharing data between the processes is complicated, and can usually only be done efficiently through shared memory (but which itself is not very portable). Synchronization is complicated because of the preemptive nature of the Unix scheduler (one has to use <i>atomic</i> locks, etc). The machine&#8217;s resources can be exhausted very quickly when the server application has to serve too many long-running requests (heavy-weight processes cost memory). And when each request spawns a sub-process to handle it, the server performance and responsiveness is horrible (heavy-weight processes cost time to spawn). Finally, the server application doesn&#8217;t scale very well with the load because of these resource problems. In practice, lots of tricks are usually used to overcome these problems - ranging from pre-forked sub-process pools to semi-serialized processing, etc. </p>
<p>One of the most elegant ways to solve these resource- and data-sharing problems is to have multiple <i>light-weight</i> threads of execution inside a single (heavy-weight) process, i.e., to use <i>multithreading</i>. Those <i>threads</i> usually improve responsiveness and performance of the application, often improve and simplify the internal program structure, and most important, require less system resources than heavy-weight processes. Threads are neither the optimal run-time facility for all types of applications, nor can all applications benefit from them. But at least event-driven server applications usually benefit greatly from using threads. <br />
 </p>
<p> <code>The World of Threading</code> </p>
<p>Even though lots of documents exists which describe and define the world of threading, to understand <code>Pth</code>, you need only basic knowledge about threading. The following definitions of thread-related terms should at least help you understand thread programming enough to allow you to use <code>Pth</code>. </p>
<dl>
<dt><code>o</code><code>process</code> vs. <code>thread</code></dt>
<dd> <p> A process on Unix systems consists of at least the following fundamental ingredients: <i>virtual memory table</i>, <i>program code</i>, <i>program counter</i>, <i>heap memory</i>, <i>stack memory</i>, <i>stack pointer</i>, <i>file descriptor set</i>, <i>signal table</i>. On every process switch, the kernel saves and restores these ingredients for the individual processes. On the other hand, a thread consists of only a private program counter, stack memory, stack pointer and signal table. All other ingredients, in particular the virtual memory, it shares with the other threads of the same process. </p>
 </dd>
<dt><code>o</code><code>kernel-space</code> vs. <code>user-space</code> threading</dt>
<dd> <p> Threads on a Unix platform traditionally can be implemented either inside kernel-space or user-space. When threads are implemented by the kernel, the thread context switches are performed by the kernel without the application&#8217;s knowledge. Similarly, when threads are implemented in user-space, the thread context switches are performed by an application library, without the kernel&#8217;s knowledge. There also are hybrid threading approaches where, typically, a user-space library binds one or more user-space threads to one or more kernel-space threads (there usually called light-weight processes - or in short LWPs). </p>
<p>User-space threads are usually more portable and can perform faster and cheaper context switches (for instance via <i><a href="/docs/linux/man/2-swapcontext/">swapcontext</a></i>(2) or <i><a href="/docs/linux/man/3-setjmp/">setjmp</a></i>(3)/<i><a href="/docs/linux/man/3-longjmp/">longjmp</a></i>(3)) than kernel based threads. On the other hand, kernel-space threads can take advantage of multiprocessor machines and don&#8217;t have any inherent I/O blocking problems. Kernel-space threads are usually scheduled in preemptive way side-by-side with the underlying processes. User-space threads on the other hand use either preemptive or non-preemptive scheduling. </p>
 </dd>
<dt><code>o</code><code>preemptive</code> vs. <code>non-preemptive</code> thread scheduling</dt>
<dd> <p> In preemptive scheduling, the scheduler lets a thread execute until a blocking situation occurs (usually a function call which would block) or the assigned timeslice elapses. Then it detracts control from the thread without a chance for the thread to object. This is usually realized by interrupting the thread through a hardware interrupt signal (for kernel-space threads) or a software interrupt signal (for user-space threads), like <code>&quot;SIGALRM&quot;</code> or <code>&quot;SIGVTALRM&quot;</code>. In non-preemptive scheduling, once a thread received control from the scheduler it keeps it until either a blocking situation occurs (again a function call which would block and instead switches back to the scheduler) or the thread explicitly yields control back to the scheduler in a cooperative way. </p>
 </dd>
<dt><code>o</code><code>concurrency</code> vs. <code>parallelism</code></dt>
<dd> <p> Concurrency exists when at least two threads are <i>in progress</i> at the same time. Parallelism arises when at least two threads are <i>executing</i> simultaneously. Real parallelism can be only achieved on multiprocessor machines, of course. But one also usually speaks of parallelism or <i>high concurrency</i> in the context of preemptive thread scheduling and of <i>low concurrency</i> in the context of non-preemptive thread scheduling. </p>
 </dd>
<dt><code>o</code><code>responsiveness</code></dt>
<dd> <p> The responsiveness of a system can be described by the user visible delay until the system responses to an external request. When this delay is small enough and the user doesn&#8217;t recognize a noticeable delay, the responsiveness of the system is considered good. When the user recognizes or is even annoyed by the delay, the responsiveness of the system is considered bad. </p>
 </dd>
<dt><code>o</code><code>reentrant</code>, <code>thread-safe</code> and <code>asynchronous-safe</code> functions</dt>
<dd> <p> A reentrant function is one that behaves correctly if it is called simultaneously by several threads and then also executes simultaneously. Functions that access global state, such as memory or files, of course, need to be carefully designed in order to be reentrant. Two traditional approaches to solve these problems are caller-supplied states and thread-specific data. </p>
<p>Thread-safety is the avoidance of <i>data races</i>, i.e., situations in which data is set to either correct or incorrect value depending upon the (unpredictable) order in which multiple threads access and modify the data. So a function is thread-safe when it still behaves semantically correct when called simultaneously by several threads (it is not required that the functions also execute simultaneously). The traditional approach to achieve thread-safety is to wrap a function body with an internal mutual exclusion lock (aka `mutex&#8217;). As you should recognize, reentrant is a stronger attribute than thread-safe, because it is harder to achieve and results especially in no run-time contention between threads. So, a reentrant function is always thread-safe, but not vice versa. </p>
<p>Additionally there is a related attribute for functions named asynchronous-safe, which comes into play in conjunction with signal handlers. This is very related to the problem of reentrant functions. An asynchronous-safe function is one that can be called safe and without side-effects from within a signal handler context. Usually very few functions are of this type, because an application is very restricted in what it can perform from within a signal handler (especially what system functions it is allowed to call). The reason mainly is, because only a few system functions are officially declared by <font SIZE="-1">POSIX</font> as guaranteed to be asynchronous-safe. Asynchronous-safe functions usually have to be already reentrant. <br />
 </p>
 </dd></dl>
<p> <code>User-Space Threads</code> </p>
<p>User-space threads can be implemented in various way. The two traditional approaches are: </p>
<dl>
<dt><code>1.</code></dt>
<dd> <p> <code>Matrix-based explicit dispatching between small units of execution:</code> </p>
<p>Here the global procedures of the application are split into small execution units (each is required to not run for more than a few milliseconds) and those units are implemented by separate functions. Then a global matrix is defined which describes the execution (and perhaps even dependency) order of these functions. The main server procedure then just dispatches between these units by calling one function after each other controlled by this matrix. The threads are created by more than one jump-trail through this matrix and by switching between these jump-trails controlled by corresponding occurred events. </p>
<p>This approach gives the best possible performance, because one can fine-tune the threads of execution by adjusting the matrix, and the scheduling is done explicitly by the application itself. It is also very portable, because the matrix is just an ordinary data structure, and functions are a standard feature of <font SIZE="-1">ANSI</font> C. </p>
<p>The disadvantage of this approach is that it is complicated to write large applications with this approach, because in those applications one quickly gets hundreds(!) of execution units and the control flow inside such an application is very hard to understand (because it is interrupted by function borders and one always has to remember the global dispatching matrix to follow it). Additionally, all threads operate on the same execution stack. Although this saves memory, it is often nasty, because one cannot switch between threads in the middle of a function. Thus the scheduling borders are the function borders. </p>
 </dd>
<dt><code>2.</code></dt>
<dd> <p> <code>Context-based implicit scheduling between threads of execution:</code> </p>
<p>Here the idea is that one programs the application as with forked processes, i.e., one spawns a thread of execution and this runs from the begin to the end without an interrupted control flow. But the control flow can be still interrupted &#8211; even in the middle of a function. Actually in a preemptive way, similar to what the kernel does for the heavy-weight processes, i.e., every few milliseconds the user-space scheduler switches between the threads of execution. But the thread itself doesn&#8217;t recognize this and usually (except for synchronization issues) doesn&#8217;t have to care about this. </p>
<p>The advantage of this approach is that it&#8217;s very easy to program, because the control flow and context of a thread directly follows a procedure without forced interrupts through function borders. Additionally, the programming is very similar to a traditional and well understood <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) based approach. </p>
<p>The disadvantage is that although the general performance is increased, compared to using approaches based on heavy-weight processes, it is decreased compared to the matrix-approach above. Because the implicit preemptive scheduling does usually a lot more context switches (every user-space context switch costs some overhead even when it is a lot cheaper than a kernel-level context switch) than the explicit cooperative/non-preemptive scheduling. Finally, there is no really portable <font SIZE="-1">POSIX/ANSI-C</font> based way to implement user-space preemptive threading. Either the platform already has threads, or one has to hope that some semi-portable package exists for it. And even those semi-portable packages usually have to deal with assembler code and other nasty internals and are not easy to port to forthcoming platforms. </p>
 </dd></dl>
<p>So, in short: the matrix-dispatching approach is portable and fast, but nasty to program. The thread scheduling approach is easy to program, but suffers from synchronization and portability problems caused by its preemptive nature. <br />
 </p>
<p> <code>The Compromise of Pth</code> </p>
<p>But why not combine the good aspects of both approaches while avoiding their bad aspects? That&#8217;s the goal of <code>Pth</code>. <code>Pth</code> implements easy-to-program threads of execution, but avoids the problems of preemptive scheduling by using non-preemptive scheduling instead. </p>
<p>This sounds like, and is, a useful approach. Nevertheless, one has to keep the implications of non-preemptive thread scheduling in mind when working with <code>Pth</code>. The following list summarizes a few essential points: </p>
<dl>
<dt><code>o</code></dt>
<dd> <p> <code>Pth provides maximum portability, but </code><font SIZE="-1"><code>NOT</code></font><code> the fanciest features</code>. </p>
<p>This is, because it uses a nifty and portable <font SIZE="-1">POSIX/ANSI-C</font> approach for thread creation (and this way doesn&#8217;t require any platform dependent assembler hacks) and schedules the threads in non-preemptive way (which doesn&#8217;t require unportable facilities like <code>&quot;SIGVTALRM&quot;</code>). On the other hand, this way not all fancy threading features can be implemented. Nevertheless the available facilities are enough to provide a robust and full-featured threading system. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> <code>Pth increases the responsiveness and concurrency of an event-driven application, but </code><font SIZE="-1"><code>NOT</code></font><code> the concurrency of number-crunching applications</code>. </p>
<p>The reason is the non-preemptive scheduling. Number-crunching applications usually require preemptive scheduling to achieve concurrency because of their long <font SIZE="-1">CPU</font> bursts. For them, non-preemptive scheduling (even together with explicit yielding) provides only the old concept of `coroutines&#8217;. On the other hand, event driven applications benefit greatly from non-preemptive scheduling. They have only short <font SIZE="-1">CPU</font> bursts and lots of events to wait on, and this way run faster under non-preemptive scheduling because no unnecessary context switching occurs, as it is the case for preemptive scheduling. That&#8217;s why <code>Pth</code> is mainly intended for server type applications, although there is no technical restriction. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> <code>Pth requires thread-safe functions, but </code><font SIZE="-1"><code>NOT</code></font><code> reentrant functions</code>. </p>
<p>This nice fact exists again because of the nature of non-preemptive scheduling, where a function isn&#8217;t interrupted and this way cannot be reentered before it returned. This is a great portability benefit, because thread-safety can be achieved more easily than reentrance possibility. Especially this means that under <code>Pth</code> more existing third-party libraries can be used without side-effects than it&#8217;s the case for other threading systems. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> <code>Pth doesn&#8217;t require any kernel support, but can </code><font SIZE="-1"><code>NOT</code></font><code> benefit from multiprocessor machines</code>. </p>
<p>This means that <code>Pth</code> runs on almost all Unix kernels, because the kernel does not need to be aware of the <code>Pth</code> threads (because they are implemented entirely in user-space). On the other hand, it cannot benefit from the existence of multiprocessors, because for this, kernel support would be needed. In practice, this is no problem, because multiprocessor systems are rare, and portability is almost more important than highest concurrency. <br />
 </p>
 </dd></dl>
<p> <code>The life cycle of a thread</code> </p>
<p>To understand the <code>Pth</code> Application Programming Interface (<font SIZE="-1">API</font>), it helps to first understand the life cycle of a thread in the <code>Pth</code> threading system. It can be illustrated with the following directed graph: </p>
<pre><code>             NEW
              |
              V
      +---&gt; READY ---+
      | ^ |
      | | V
   WAITING &lt;--+-- RUNNING
                     |
      : V
   SUSPENDED DEAD
</code></pre>
<p>When a new thread is created, it is moved into the <font SIZE="-1"><code>NEW</code></font> queue of the scheduler. On the next dispatching for this thread, the scheduler picks it up from there and moves it to the <font SIZE="-1"><code>READY</code></font> queue. This is a queue containing all threads which want to perform a <font SIZE="-1">CPU</font> burst. There they are queued in priority order. On each dispatching step, the scheduler always removes the thread with the highest priority only. It then increases the priority of all remaining threads by 1, to prevent them from `starving&#8217;. </p>
<p>The thread which was removed from the <font SIZE="-1"><code>READY</code></font> queue is the new <font SIZE="-1"><code>RUNNING</code></font> thread (there is always just one <font SIZE="-1"><code>RUNNING</code></font> thread, of course). The <font SIZE="-1"><code>RUNNING</code></font> thread is assigned execution control. After this thread yields execution (either explicitly by yielding execution or implicitly by calling a function which would block) there are three possibilities: Either it has terminated, then it is moved to the <font SIZE="-1"><code>DEAD</code></font> queue, or it has events on which it wants to wait, then it is moved into the <font SIZE="-1"><code>WAITING</code></font> queue. Else it is assumed it wants to perform more <font SIZE="-1">CPU</font> bursts and immediately enters the <font SIZE="-1"><code>READY</code></font> queue again. </p>
<p>Before the next thread is taken out of the <font SIZE="-1"><code>READY</code></font> queue, the <font SIZE="-1"><code>WAITING</code></font> queue is checked for pending events. If one or more events occurred, the threads that are waiting on them are immediately moved to the <font SIZE="-1"><code>READY</code></font> queue. </p>
<p>The purpose of the <font SIZE="-1"><code>NEW</code></font> queue has to do with the fact that in <code>Pth</code> a thread never directly switches to another thread. A thread always yields execution to the scheduler and the scheduler dispatches to the next thread. So a freshly spawned thread has to be kept somewhere until the scheduler gets a chance to pick it up for scheduling. That is what the <font SIZE="-1"><code>NEW</code></font> queue is for. </p>
<p>The purpose of the <font SIZE="-1"><code>DEAD</code></font> queue is to support thread joining. When a thread is marked to be unjoinable, it is directly kicked out of the system after it terminated. But when it is joinable, it enters the <font SIZE="-1"><code>DEAD</code></font> queue. There it remains until another thread joins it. </p>
<p>Finally, there is a special separated queue named <font SIZE="-1"><code>SUSPENDED</code></font>, to where threads can be manually moved from the <font SIZE="-1"><code>NEW</code></font>, <font SIZE="-1"><code>READY</code></font> or <font SIZE="-1"><code>WAITING</code></font> queues by the application. The purpose of this special queue is to temporarily absorb suspended threads until they are again resumed by the application. Suspended threads do not cost scheduling or event handling resources, because they are temporarily completely out of the scheduler&#8217;s scope. If a thread is resumed, it is moved back to the queue from where it originally came and this way again enters the schedulers scope.  </p>
<h2>APPLICATION PROGRAMMING INTERFACE (API)</h2>
<p> In the following the <code>Pth</code> <i>Application Programming Interface</i> (<font SIZE="-1">API</font>) is discussed in detail. With the knowledge given above, it should now be easy to understand how to program threads with this <font SIZE="-1">API</font>. In good Unix tradition, <code>Pth</code> functions use special return values (<code>&quot;NULL&quot;</code> in pointer context, <code>&quot;FALSE&quot;</code> in boolean context and <code>&quot;-1&quot;</code> in integer context) to indicate an error condition and set (or pass through) the <code>&quot;errno&quot;</code> system variable to pass more details about the error to the caller. <br />
 </p>
<p> <code>Global Library Management</code> </p>
<p>The following functions act on the library as a whole. They are used to initialize and shutdown the scheduler and fetch information from it. </p>
<dl>
<dt>int <code>pth_init</code>(void);</dt>
<dd> <p> This initializes the <code>Pth</code> library. It has to be the first <code>Pth</code> <font SIZE="-1">API</font> function call in an application, and is mandatory. It&#8217;s usually done at the begin of the <i>main()</i> function of the application. This implicitly spawns the internal scheduler thread and transforms the single execution unit of the current process into a thread (the `main&#8217; thread). It returns <code>&quot;TRUE&quot;</code> on success and <code>&quot;FALSE&quot;</code> on error. </p>
 </dd>
<dt>int <code>pth_kill</code>(void);</dt>
<dd> <p> This kills the <code>Pth</code> library. It should be the last <code>Pth</code> <font SIZE="-1">API</font> function call in an application, but is not really required. It&#8217;s usually done at the end of the main function of the application. At least, it has to be called from within the main thread. It implicitly kills all threads and transforms back the calling thread into the single execution unit of the underlying process. The usual way to terminate a <code>Pth</code> application is either a simple `<code>&quot;pth_exit(0);&quot;</code>&#8216; in the main thread (which waits for all other threads to terminate, kills the threading system and then terminates the process) or a `<code>&quot;pth_kill(); exit(0)&quot;</code>&#8216; (which immediately kills the threading system and terminates the process). The <i>pth_kill()</i> return immediately with a return code of <code>&quot;FALSE&quot;</code> if it is not called from within the main thread. Else it kills the threading system and returns <code>&quot;TRUE&quot;</code>. </p>
 </dd>
<dt>long <code>pth_ctrl</code>(unsigned long <i>query</i>, ...);</dt>
<dd> <p> This is a generalized query/control function for the <code>Pth</code> library. The argument <i>query</i> is a bitmask formed out of one or more <code>&quot;PTH_CTRL_&quot;</code><i></i><font SIZE="-1"><i>XXXX</i></font><i></i> queries. Currently the following queries are supported: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;PTH_CTRL_GETTHREADS&quot;</dt>
<dd> <p> This returns the total number of threads currently in existence. This query actually is formed out of the combination of queries for threads in a particular state, i.e., the <code>&quot;PTH_CTRL_GETTHREADS&quot;</code> query is equal to the OR-combination of all the following specialized queries: </p>
<p> <code>&quot;PTH_CTRL_GETTHREADS_NEW&quot;</code> for the number of threads in the new queue (threads created via <i>pth_spawn</i>(3) but still not scheduled once), <code>&quot;PTH_CTRL_GETTHREADS_READY&quot;</code> for the number of threads in the ready queue (threads who want to do <font SIZE="-1">CPU</font> bursts), <code>&quot;PTH_CTRL_GETTHREADS_RUNNING&quot;</code> for the number of running threads (always just one thread!), <code>&quot;PTH_CTRL_GETTHREADS_WAITING&quot;</code> for the number of threads in the waiting queue (threads waiting for events), <code>&quot;PTH_CTRL_GETTHREADS_SUSPENDED&quot;</code> for the number of threads in the suspended queue (threads waiting to be resumed) and <code>&quot;PTH_CTRL_GETTHREADS_DEAD&quot;</code> for the number of threads in the new queue (terminated threads waiting for a join). </p>
 </dd>
<dt>&quot;PTH_CTRL_GETAVLOAD&quot;</dt>
<dd> <p> This requires a second argument of type `<code>&quot;float *&quot;</code>&#8216; (pointer to a floating point variable). It stores a floating point value describing the exponential averaged load of the scheduler in this variable. The load is a function from the number of threads in the ready queue of the schedulers dispatching unit. So a load around 1.0 means there is only one ready thread (the standard situation when the application has no high load). A higher load value means there a more threads ready who want to do <font SIZE="-1">CPU</font> bursts. The average load value updates once per second only. The return value for this query is always 0. </p>
 </dd>
<dt>&quot;PTH_CTRL_GETPRIO&quot;</dt>
<dd> <p> This requires a second argument of type `<code>&quot;pth_t&quot;</code>&#8216; which identifies a thread. It returns the priority (ranging from <code>&quot;PTH_PRIO_MIN&quot;</code> to <code>&quot;PTH_PRIO_MAX&quot;</code>) of the given thread. </p>
 </dd>
<dt>&quot;PTH_CTRL_GETNAME&quot;</dt>
<dd> <p> This requires a second argument of type `<code>&quot;pth_t&quot;</code>&#8216; which identifies a thread. It returns the name of the given thread, i.e., the return value of <i>pth_ctrl</i>(3) should be casted to a `<code>&quot;char *&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_CTRL_DUMPSTATE&quot;</dt>
<dd> <p> This requires a second argument of type `<code>&quot;FILE *&quot;</code>&#8216; to which a summary of the internal <code>Pth</code> library state is written to. The main information which is currently written out is the current state of the thread pool. </p>
 </dd>
<dt>&quot;PTH_CTRL_FAVOURNEW&quot;</dt>
<dd> <p> This requires a second argument of type `<code>&quot;int&quot;</code>&#8216; which specified whether the <font SIZE="-1"><code>GNU</code></font><code> Pth</code> scheduler favours new threads on startup, i.e., whether they are moved from the new queue to the top (argument is <code>&quot;TRUE&quot;</code>) or middle (argument is <code>&quot;FALSE&quot;</code>) of the ready queue. The default is to favour new threads to make sure they do not starve already at startup, although this slightly violates the strict priority based scheduling. </p>
 </dd></dl>
</dl>
<dl>
<dd> <p>The function returns <code>&quot;-1&quot;</code> on error. </p>
 </dd></dl>
<dt>long <code>pth_version</code>(void);</dt>
<dd> <p> This function returns a hex-value `0x <i>V</i><i></i><font SIZE="-1"><i>RR</i></font><i></i><i>T</i><i></i><font SIZE="-1"><i>LL</i></font><i></i>&#8216; which describes the current <code>Pth</code> library version. <i>V</i> is the version, <i></i><font SIZE="-1"><i>RR</i></font><i></i> the revisions, <i></i><font SIZE="-1"><i>LL</i></font><i></i> the level and <i>T</i> the type of the level (alphalevel=0, betalevel=1, patchlevel=2, etc). For instance <code>Pth</code> version 1.0b1 is encoded as 0x100101. The reason for this unusual mapping is that this way the version number is steadily <i>increasing</i>. The same value is also available under compile time as <code>&quot;PTH_VERSION&quot;</code>. <br />
 </p>
 </dd></dl>
<p> <code>Thread Attribute Handling</code> </p>
<p>Attribute objects are used in <code>Pth</code> for two things: First stand-alone/unbound attribute objects are used to store attributes for to be spawned threads. Bounded attribute objects are used to modify attributes of already existing threads. The following attribute fields exists in attribute objects: </p>
<dl>
<dt>&quot;PTH_ATTR_PRIO&quot; (read-write) [<code>&quot;int&quot;]</dt>
<dd> <p> Thread Priority between &quot;PTH_PRIO_MIN&quot;</code> and <code>&quot;PTH_PRIO_MAX&quot;</code>. The default is <code>&quot;PTH_PRIO_STD&quot;</code>. </p>
 </dd>
<dt>&quot;PTH_ATTR_NAME&quot; (read-write) [<code>&quot;char *&quot;]</dt>
<dd> <p> Name of thread (up to 40 characters are stored only), mainly for debugging purposes. </p>
 </dd>
<dt>&quot;PTH_ATTR_DISPATCHES&quot;</code> (read-write) [<code>&quot;int&quot;]</dt>
<dd> <p> In bounded attribute objects, this field is incremented every time the context is switched to the associated thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_JOINABLE&quot;</code> (read-write&gt; [<code>&quot;int&quot;]</dt>
<dd> <p> The thread detachment type, &quot;TRUE&quot;</code> indicates a joinable thread, <code>&quot;FALSE&quot;</code> indicates a detached thread. When a thread is detached, after termination it is immediately kicked out of the system instead of inserted into the dead queue. </p>
 </dd>
<dt>&quot;PTH_ATTR_CANCEL_STATE&quot; (read-write) [<code>&quot;unsigned int&quot;]</dt>
<dd> <p> The thread cancellation state, i.e., a combination of &quot;PTH_CANCEL_ENABLE&quot;</code> or <code>&quot;PTH_CANCEL_DISABLE&quot;</code> and <code>&quot;PTH_CANCEL_DEFERRED&quot;</code> or <code>&quot;PTH_CANCEL_ASYNCHRONOUS&quot;</code>. </p>
 </dd>
<dt>&quot;PTH_ATTR_STACK_SIZE&quot; (read-write) [<code>&quot;unsigned int&quot;]</dt>
<dd> <p> The thread stack size in bytes. Use lower values than 64 </code><font SIZE="-1"><code>KB</code></font><code> with great care! </p>
 </dd>
<dt>&quot;PTH_ATTR_STACK_ADDR&quot;</code> (read-write) [<code>&quot;char *&quot;]</dt>
<dd> <p> A pointer to the lower address of a chunk of </code><i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3)&#8216;ed memory for the stack. </p>
 </dd>
<dt>&quot;PTH_ATTR_TIME_SPAWN&quot; (read-only) [<code>&quot;pth_time_t&quot;]</dt>
<dd> <p> The time when the thread was spawned. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_TIME_LAST&quot;</code> (read-only) [<code>&quot;pth_time_t&quot;]</dt>
<dd> <p> The time when the thread was last dispatched. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_TIME_RAN&quot;</code> (read-only) [<code>&quot;pth_time_t&quot;]</dt>
<dd> <p> The total time the thread was running. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_START_FUNC&quot;</code> (read-only) [<code>&quot;void *(*)(void *)&quot;]</dt>
<dd> <p> The thread start function. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_START_ARG&quot;</code> (read-only) [<code>&quot;void *&quot;]</dt>
<dd> <p> The thread start argument. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_STATE&quot;</code> (read-only) [<code>&quot;pth_state_t&quot;]</dt>
<dd> <p> The scheduling state of the thread, i.e., either &quot;PTH_STATE_NEW&quot;</code>, <code>&quot;PTH_STATE_READY&quot;</code>, <code>&quot;PTH_STATE_WAITING&quot;</code>, or <code>&quot;PTH_STATE_DEAD&quot;</code> This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_EVENTS&quot; (read-only) [<code>&quot;pth_event_t&quot;]</dt>
<dd> <p> The event ring the thread is waiting for. This can be queried only when the attribute object is bound to a thread. </p>
 </dd>
<dt>&quot;PTH_ATTR_BOUND&quot;</code> (read-only) [<code>&quot;int&quot;]</dt>
<dd> <p> Whether the attribute object is bound (&quot;TRUE&quot;</code>) to a thread or not (<code>&quot;FALSE&quot;</code>). </p>
 </dd></dl>
<p>The following <font SIZE="-1">API</font> functions can be used to handle the attribute objects: </p>
<dl>
<dt>pth_attr_t <code>pth_attr_of</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This returns a new attribute object <i>bound</i> to thread <i>tid</i>. Any queries on this object directly fetch attributes from <i>tid</i>. And attribute modifications directly change <i>tid</i>. Use such attribute objects to modify existing threads. </p>
 </dd>
<dt>pth_attr_t <code>pth_attr_new</code>(void);</dt>
<dd> <p> This returns a new <i>unbound</i> attribute object. An implicit <i>pth_attr_init()</i> is done on it. Any queries on this object just fetch stored attributes from it. And attribute modifications just change the stored attributes. Use such attribute objects to pre-configure attributes for to be spawned threads. </p>
 </dd>
<dt>int <code>pth_attr_init</code>(pth_attr_t <i>attr</i>);</dt>
<dd> <p> This initializes an attribute object <i>attr</i> to the default values: <code>&quot;PTH_ATTR_PRIO&quot;</code> := <code>&quot;PTH_PRIO_STD&quot;</code>, <code>&quot;PTH_ATTR_NAME&quot;</code> := `<code>&quot;unknown&quot;</code>&#8216;, <code>&quot;PTH_ATTR_DISPATCHES&quot;</code> := <code>0</code>, <code>&quot;PTH_ATTR_JOINABLE&quot;</code> := <code>&quot;TRUE&quot;</code>, <code>&quot;PTH_ATTR_CANCELSTATE&quot;</code> := <code>&quot;PTH_CANCEL_DEFAULT&quot;</code>, <code>&quot;PTH_ATTR_STACK_SIZE&quot;</code> := 64*1024 and <code>&quot;PTH_ATTR_STACK_ADDR&quot;</code> := <code>&quot;NULL&quot;</code>. All other <code>&quot;PTH_ATTR_*&quot;</code> attributes are read-only attributes and don&#8217;t receive default values in <i>attr</i>, because they exists only for bounded attribute objects. </p>
 </dd>
<dt>int <code>pth_attr_set</code>(pth_attr_t <i>attr</i>, int <i>field</i>, ...);</dt>
<dd> <p> This sets the attribute field <i>field</i> in <i>attr</i> to a value specified as an additional argument on the variable argument list. The following attribute <i>fields</i> and argument pairs can be used: </p>
<pre><code> PTH_ATTR_PRIO int
 PTH_ATTR_NAME char *
 PTH_ATTR_DISPATCHES int
 PTH_ATTR_JOINABLE int
 PTH_ATTR_CANCEL_STATE unsigned int
 PTH_ATTR_STACK_SIZE unsigned int
 PTH_ATTR_STACK_ADDR char *
</code></pre>
 </dd>
<dt>int <code>pth_attr_get</code>(pth_attr_t <i>attr</i>, int <i>field</i>, ...);</dt>
<dd> <p> This retrieves the attribute field <i>field</i> in <i>attr</i> and stores its value in the variable specified through a pointer in an additional argument on the variable argument list. The following <i>fields</i> and argument pairs can be used: </p>
<pre><code> PTH_ATTR_PRIO int *
 PTH_ATTR_NAME char **
 PTH_ATTR_DISPATCHES int *
 PTH_ATTR_JOINABLE int *
 PTH_ATTR_CANCEL_STATE unsigned int *
 PTH_ATTR_STACK_SIZE unsigned int *
 PTH_ATTR_STACK_ADDR char **
 PTH_ATTR_TIME_SPAWN pth_time_t *
 PTH_ATTR_TIME_LAST pth_time_t *
 PTH_ATTR_TIME_RAN pth_time_t *
 PTH_ATTR_START_FUNC void *(**)(void *)
 PTH_ATTR_START_ARG void **
 PTH_ATTR_STATE pth_state_t *
 PTH_ATTR_EVENTS pth_event_t *
 PTH_ATTR_BOUND int *
</code></pre>
 </dd>
<dt>int <code>pth_attr_destroy</code>(pth_attr_t <i>attr</i>);</dt>
<dd> <p> This destroys a attribute object <i>attr</i>. After this <i>attr</i> is no longer a valid attribute object. <br />
 </p>
 </dd></dl>
<p> <code>Thread Control</code> </p>
<p>The following functions control the threading itself and make up the main <font SIZE="-1">API</font> of the <code>Pth</code> library. </p>
<dl>
<dt>pth_t <code>pth_spawn</code>(pth_attr_t <i>attr</i>, void *(*<i>entry</i>)(void *), void *<i>arg</i>);</dt>
<dd> <p> This spawns a new thread with the attributes given in <i>attr</i> (or <code>&quot;PTH_ATTR_DEFAULT&quot;</code> for default attributes - which means that thread priority, joinability and cancel state are inherited from the current thread) with the starting point at routine <i>entry</i>; the dispatch count is not inherited from the current thread if <i>attr</i> is not specified - rather, it is initialized to zero. This entry routine is called as `pth_exit(<i>entry</i>(<i>arg</i>))&#8216; inside the new thread unit, i.e., <i>entry</i>&#8216;s return value is fed to an implicit <i>pth_exit</i>(3). So the thread can also exit by just returning. Nevertheless the thread can also exit explicitly at any time by calling <i>pth_exit</i>(3). But keep in mind that calling the <font SIZE="-1">POSIX</font> function <i><a href="/docs/linux/man/3-exit/">exit</a></i>(3) still terminates the complete process and not just the current thread. </p>
<p>There is no <code>Pth</code>-internal limit on the number of threads one can spawn, except the limit implied by the available virtual memory. <code>Pth</code> internally keeps track of thread in dynamic data structures. The function returns <code>&quot;NULL&quot;</code> on error. </p>
 </dd>
<dt>int <code>pth_once</code>(pth_once_t *<i>ctrlvar</i>, void (*<i>func</i>)(void *), void *<i>arg</i>);</dt>
<dd> <p> This is a convenience function which uses a control variable of type <code>&quot;pth_once_t&quot;</code> to make sure a constructor function <i>func</i> is called only once as `<i>func</i>(<i>arg</i>)&#8216; in the system. In other words: Only the first call to <i>pth_once</i>(3) by any thread in the system succeeds. The variable referenced via <i>ctrlvar</i> should be declared as `<code>&quot;pth_once_t&quot;</code> <i>variable-name</i> = <code>&quot;PTH_ONCE_INIT&quot;</code>;&#8216; before calling this function. </p>
 </dd>
<dt>pth_t <code>pth_self</code>(void);</dt>
<dd> <p> This just returns the unique thread handle of the currently running thread. This handle itself has to be treated as an opaque entity by the application. It&#8217;s usually used as an argument to other functions who require an argument of type <code>&quot;pth_t&quot;</code>. </p>
 </dd>
<dt>int <code>pth_suspend</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This suspends a thread <i>tid</i> until it is manually resumed again via <i>pth_resume</i>(3). For this, the thread is moved to the <font SIZE="-1"><code>SUSPENDED</code></font> queue and this way is completely out of the scheduler&#8217;s event handling and thread dispatching scope. Suspending the current thread is not allowed. The function returns <code>&quot;TRUE&quot;</code> on success and <code>&quot;FALSE&quot;</code> on errors. </p>
 </dd>
<dt>int <code>pth_resume</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This function resumes a previously suspended thread <i>tid</i>, i.e. <i>tid</i> has to stay on the <font SIZE="-1"><code>SUSPENDED</code></font> queue. The thread is moved to the <font SIZE="-1"><code>NEW</code></font>, <font SIZE="-1"><code>READY</code></font> or <font SIZE="-1"><code>WAITING</code></font> queue (dependent on what its state was when the <i>pth_suspend</i>(3) call were made) and this way again enters the event handling and thread dispatching scope of the scheduler. The function returns <code>&quot;TRUE&quot;</code> on success and <code>&quot;FALSE&quot;</code> on errors. </p>
 </dd>
<dt>int <code>pth_raise</code>(pth_t <i>tid</i>, int <i>sig</i>)</dt>
<dd> <p> This function raises a signal for delivery to thread <i>tid</i> only. When one just raises a signal via <i><a href="/docs/linux/man/3-raise/">raise</a></i>(3) or <i><a href="/docs/linux/man/2-kill/">kill</a></i>(2), its delivered to an arbitrary thread which has this signal not blocked. With <i>pth_raise</i>(3) one can send a signal to a thread and its guarantees that only this thread gets the signal delivered. But keep in mind that nevertheless the signals <i>action</i> is still configured <i>process</i>-wide. When <i>sig</i> is 0 plain thread checking is performed, i.e., `<code>&quot;pth_raise(tid, 0)&quot;</code>&#8216; returns <code>&quot;TRUE&quot;</code> when thread <i>tid</i> still exists in the <font SIZE="-1"><code>PTH</code></font> system but doesn&#8217;t send any signal to it. </p>
 </dd>
<dt>int <code>pth_yield</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This explicitly yields back the execution control to the scheduler thread. Usually the execution is implicitly transferred back to the scheduler when a thread waits for an event. But when a thread has to do larger <font SIZE="-1">CPU</font> bursts, it can be reasonable to interrupt it explicitly by doing a few <i>pth_yield</i>(3) calls to give other threads a chance to execute, too. This obviously is the cooperating part of <code>Pth</code>. A thread <i>has not</i> to yield execution, of course. But when you want to program a server application with good response times the threads should be cooperative, i.e., when they should split their <font SIZE="-1">CPU</font> bursts into smaller units with this call. </p>
<p>Usually one specifies <i>tid</i> as <code>&quot;NULL&quot;</code> to indicate to the scheduler that it can freely decide which thread to dispatch next. But if one wants to indicate to the scheduler that a particular thread should be favored on the next dispatching step, one can specify this thread explicitly. This allows the usage of the old concept of <i>coroutines</i> where a thread/routine switches to a particular cooperating thread. If <i>tid</i> is not <code>&quot;NULL&quot;</code> and points to a <i>new</i> or <i>ready</i> thread, it is guaranteed that this thread receives execution control on the next dispatching step. If <i>tid</i> is in a different state (that is, not in <code>&quot;PTH_STATE_NEW&quot;</code> or <code>&quot;PTH_STATE_READY&quot;</code>) an error is reported. </p>
<p>The function usually returns <code>&quot;TRUE&quot;</code> for success and only <code>&quot;FALSE&quot;</code> (with <code>&quot;errno&quot;</code> set to <code>&quot;EINVAL&quot;</code>) if <i>tid</i> specified an invalid or still not new or ready thread. </p>
 </dd>
<dt>int <code>pth_nap</code>(pth_time_t <i>naptime</i>);</dt>
<dd> <p> This functions suspends the execution of the current thread until <i>naptime</i> is elapsed. <i>naptime</i> is of type <code>&quot;pth_time_t&quot;</code> and this way has theoretically a resolution of one microsecond. In practice you should neither rely on this nor that the thread is awakened exactly after <i>naptime</i> has elapsed. It&#8217;s only guarantees that the thread will sleep at least <i>naptime</i>. But because of the non-preemptive nature of <code>Pth</code> it can last longer (when another thread kept the <font SIZE="-1">CPU</font> for a long time). Additionally the resolution is dependent of the implementation of timers by the operating system and these usually have only a resolution of 10 microseconds or larger. But usually this isn&#8217;t important for an application unless it tries to use this facility for real time tasks. </p>
 </dd>
<dt>int <code>pth_wait</code>(pth_event_t <i>ev</i>);</dt>
<dd> <p> This is the link between the scheduler and the event facility (see below for the various <i>pth_event_xxx()</i> functions). It&#8217;s modeled like <i><a href="/docs/linux/man/2-select/">select</a></i>(2), i.e., one gives this function one or more events (in the event ring specified by <i>ev</i>) on which the current thread wants to wait. The scheduler awakes the thread when one ore more of them occurred or failed after tagging them as such. The <i>ev</i> argument is a <i>pointer</i> to an event ring which isn&#8217;t changed except for the tagging. <i>pth_wait</i>(3) returns the number of occurred or failed events and the application can use <i>pth_event_status</i>(3) to test which events occurred or failed. </p>
 </dd>
<dt>int <code>pth_cancel</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This cancels a thread <i>tid</i>. How the cancellation is done depends on the cancellation state of <i>tid</i> which the thread can configure itself. When its state is <code>&quot;PTH_CANCEL_DISABLE&quot;</code> a cancellation request is just made pending. When it is <code>&quot;PTH_CANCEL_ENABLE&quot;</code> it depends on the cancellation type what is performed. When its <code>&quot;PTH_CANCEL_DEFERRED&quot;</code> again the cancellation request is just made pending. But when its <code>&quot;PTH_CANCEL_ASYNCHRONOUS&quot;</code> the thread is immediately canceled before <i>pth_cancel</i>(3) returns. The effect of a thread cancellation is equal to implicitly forcing the thread to call `<code>&quot;pth_exit(PTH_CANCELED)&quot;</code>&#8216; at one of his cancellation points. In <code>Pth</code> thread enter a cancellation point either explicitly via <i>pth_cancel_point</i>(3) or implicitly by waiting for an event. </p>
 </dd>
<dt>int <code>pth_abort</code>(pth_t <i>tid</i>);</dt>
<dd> <p> This is the cruel way to cancel a thread <i>tid</i>. When it&#8217;s already dead and waits to be joined it just joins it (via `<code>&quot;pth_join(&quot;</code><i>tid</i><code>&quot;, NULL)&quot;</code>&#8216;) and this way kicks it out of the system. Else it forces the thread to be not joinable and to allow asynchronous cancellation and then cancels it via `<code>&quot;pth_cancel(&quot;</code><i>tid</i><code>&quot;)&quot;</code>&#8216;. </p>
 </dd>
<dt>int <code>pth_join</code>(pth_t <i>tid</i>, void **<i>value</i>);</dt>
<dd> <p> This joins the current thread with the thread specified via <i>tid</i>. It first suspends the current thread until the <i>tid</i> thread has terminated. Then it is awakened and stores the value of <i>tid</i>&#8216;s <i>pth_exit</i>(3) call into *<i>value</i> (if <i>value</i> and not <code>&quot;NULL&quot;</code>) and returns to the caller. A thread can be joined only when it has the attribute <code>&quot;PTH_ATTR_JOINABLE&quot;</code> set to <code>&quot;TRUE&quot;</code> (the default). A thread can only be joined once, i.e., after the <i>pth_join</i>(3) call the thread <i>tid</i> is completely removed from the system. </p>
 </dd>
<dt>void <code>pth_exit</code>(void *<i>value</i>);</dt>
<dd> <p> This terminates the current thread. Whether it&#8217;s immediately removed from the system or inserted into the dead queue of the scheduler depends on its join type which was specified at spawning time. If it has the attribute <code>&quot;PTH_ATTR_JOINABLE&quot;</code> set to <code>&quot;FALSE&quot;</code>, it&#8217;s immediately removed and <i>value</i> is ignored. Else the thread is inserted into the dead queue and <i>value</i> remembered for a subsequent <i>pth_join</i>(3) call by another thread. <br />
 </p>
 </dd></dl>
<p> <code>Utilities</code> </p>
<p>Utility functions. </p>
<dl>
<dt>int <code>pth_fdmode</code>(int <i>fd</i>, int <i>mode</i>);</dt>
<dd> <p> This switches the non-blocking mode flag on file descriptor <i>fd</i>. The argument <i>mode</i> can be <code>&quot;PTH_FDMODE_BLOCK&quot;</code> for switching <i>fd</i> into blocking I/O mode, <code>&quot;PTH_FDMODE_NONBLOCK&quot;</code> for switching <i>fd</i> into non-blocking I/O mode or <code>&quot;PTH_FDMODE_POLL&quot;</code> for just polling the current mode. The current mode is returned (either <code>&quot;PTH_FDMODE_BLOCK&quot;</code> or <code>&quot;PTH_FDMODE_NONBLOCK&quot;</code>) or <code>&quot;PTH_FDMODE_ERROR&quot;</code> on error. Keep in mind that since <code>Pth</code> 1.1 there is no longer a requirement to manually switch a file descriptor into non-blocking mode in order to use it. This is automatically done temporarily inside <code>Pth</code>. Instead when you now switch a file descriptor explicitly into non-blocking mode, <i>pth_read</i>(3) or <i>pth_write</i>(3) will never block the current thread. </p>
 </dd>
<dt>pth_time_t <code>pth_time</code>(long <i>sec</i>, long <i>usec</i>);</dt>
<dd> <p> This is a constructor for a <code>&quot;pth_time_t&quot;</code> structure which is a convenient function to avoid temporary structure values. It returns a <i>pth_time_t</i> structure which holds the absolute time value specified by <i>sec</i> and <i>usec</i>. </p>
 </dd>
<dt>pth_time_t <code>pth_timeout</code>(long <i>sec</i>, long <i>usec</i>);</dt>
<dd> <p> This is a constructor for a <code>&quot;pth_time_t&quot;</code> structure which is a convenient function to avoid temporary structure values. It returns a <i>pth_time_t</i> structure which holds the absolute time value calculated by adding <i>sec</i> and <i>usec</i> to the current time. </p>
 </dd>
<dt>Sfdisc_t *<code>pth_sfiodisc</code>(void);</dt>
<dd> <p> This functions is always available, but only reasonably usable when <code>Pth</code> was built with <code>Sfio</code> support (<code>&quot;--with-sfio&quot;</code> option) and <code>&quot;PTH_EXT_SFIO&quot;</code> is then defined by <code>&quot;pth.h&quot;</code>. It is useful for applications which want to use the comprehensive <code>Sfio</code> I/O library with the <code>Pth</code> threading library. Then this function can be used to get an <code>Sfio</code> discipline structure (<code>&quot;Sfdisc_t&quot;</code>) which can be pushed onto <code>Sfio</code> streams (<code>&quot;Sfio_t&quot;</code>) in order to let this stream use <i>pth_read</i>(3)/<i>pth_write</i>(2) instead of <i><a href="/docs/linux/man/2-read/">read</a></i>(2)/<i><a href="/docs/linux/man/2-write/">write</a></i>(2). The benefit is that this way I/O on the <code>Sfio</code> stream does only block the current thread instead of the whole process. The application has to <i><a href="/docs/linux/man/3-free/">free</a></i>(3) the <code>&quot;Sfdisc_t&quot;</code> structure when it is no longer needed. The Sfio package can be found at <a rel="nofollow" href="http://www.research.att.com/sw/tools/sfio/.">http://www.research.att.com/sw/tools/sfio/.</a> <br />
 </p>
 </dd></dl>
<p> <code>Cancellation Management</code> </p>
<p> <code>Pth</code> supports <font SIZE="-1">POSIX</font> style thread cancellation via <i>pth_cancel</i>(3) and the following two related functions: </p>
<dl>
<dt>void <code>pth_cancel_state</code>(int <i>newstate</i>, int *<i>oldstate</i>);</dt>
<dd> <p> This manages the cancellation state of the current thread. When <i>oldstate</i> is not <code>&quot;NULL&quot;</code> the function stores the old cancellation state under the variable pointed to by <i>oldstate</i>. When <i>newstate</i> is not <code>0</code> it sets the new cancellation state. <i>oldstate</i> is created before <i>newstate</i> is set. A state is a combination of <code>&quot;PTH_CANCEL_ENABLE&quot;</code> or <code>&quot;PTH_CANCEL_DISABLE&quot;</code> and <code>&quot;PTH_CANCEL_DEFERRED&quot;</code> or <code>&quot;PTH_CANCEL_ASYNCHRONOUS&quot;</code>. <code>&quot;PTH_CANCEL_ENABLE|PTH_CANCEL_DEFERRED&quot;</code> (or <code>&quot;PTH_CANCEL_DEFAULT&quot;</code>) is the default state where cancellation is possible but only at cancellation points. Use <code>&quot;PTH_CANCEL_DISABLE&quot;</code> to complete disable cancellation for a thread and <code>&quot;PTH_CANCEL_ASYNCHRONOUS&quot;</code> for allowing asynchronous cancellations, i.e., cancellations which can happen at any time. </p>
 </dd>
<dt>void <code>pth_cancel_point</code>(void);</dt>
<dd> <p> This explicitly enter a cancellation point. When the current cancellation state is <code>&quot;PTH_CANCEL_DISABLE&quot;</code> or no cancellation request is pending, this has no side-effect and returns immediately. Else it calls `<code>&quot;pth_exit(PTH_CANCELED)&quot;</code>&#8216;. <br />
 </p>
 </dd></dl>
<p> <code>Event Handling</code> </p>
<p> <code>Pth</code> has a very flexible event facility which is linked into the scheduler through the <i>pth_wait</i>(3) function. The following functions provide the handling of event rings. </p>
<dl>
<dt>pth_event_t <code>pth_event</code>(unsigned long <i>spec</i>, ...);</dt>
<dd> <p> This creates a new event ring consisting of a single initial event. The type of the generated event is specified by <i>spec</i>. The following types are available: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;PTH_EVENT_FD&quot;</dt>
<dd> <p> This is a file descriptor event. One or more of <code>&quot;PTH_UNTIL_FD_READABLE&quot;</code>, <code>&quot;PTH_UNTIL_FD_WRITEABLE&quot;</code> or <code>&quot;PTH_UNTIL_FD_EXCEPTION&quot;</code> have to be OR-ed into <i>spec</i> to specify on which state of the file descriptor you want to wait. The file descriptor itself has to be given as an additional argument. Example: `<code>&quot;pth_event(PTH_EVENT_FD|PTH_UNTIL_FD_READABLE, fd)&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_EVENT_SELECT&quot;</dt>
<dd> <p> This is a multiple file descriptor event modeled directly after the <i><a href="/docs/linux/man/2-select/">select</a></i>(2) call (actually it is also used to implement <i>pth_select</i>(3) internally). It&#8217;s a convenient way to wait for a large set of file descriptors at once and at each file descriptor for a different type of state. Additionally as a nice side-effect one receives the number of file descriptors which causes the event to be occurred (using <font SIZE="-1">BSD</font> semantics, i.e., when a file descriptor occurred in two sets it&#8217;s counted twice). The arguments correspond directly to the <i><a href="/docs/linux/man/2-select/">select</a></i>(2) function arguments except that there is no timeout argument (because timeouts already can be handled via <code>&quot;PTH_EVENT_TIME&quot;</code> events). </p>
<p>Example: `<code>&quot;pth_event(PTH_EVENT_SELECT, &amp;rc, nfd, rfds, wfds, efds)&quot;</code>&#8216; where <code>&quot;rc&quot;</code> has to be of type `<code>&quot;int *&quot;</code>&#8216;, <code>&quot;nfd&quot;</code> has to be of type `<code>&quot;int&quot;</code>&#8216; and <code>&quot;rfds&quot;</code>, <code>&quot;wfds&quot;</code> and <code>&quot;efds&quot;</code> have to be of type `<code>&quot;fd_set *&quot;</code>&#8216; (see <i><a href="/docs/linux/man/2-select/">select</a></i>(2)). The number of occurred file descriptors are stored in <code>&quot;rc&quot;</code>. </p>
 </dd>
<dt>&quot;PTH_EVENT_SIGS&quot;</dt>
<dd> <p> This is a signal set event. The two additional arguments have to be a pointer to a signal set (type `<code>&quot;sigset_t *&quot;</code>&#8216;) and a pointer to a signal number variable (type `<code>&quot;int *&quot;</code>&#8216;). This event waits until one of the signals in the signal set occurred. As a result the occurred signal number is stored in the second additional argument. Keep in mind that the <code>Pth</code> scheduler doesn&#8217;t block signals automatically. So when you want to wait for a signal with this event you&#8217;ve to block it via <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2) or it will be delivered without your notice. Example: `<code>&quot;sigemptyset(&amp;set); sigaddset(&amp;set, SIGINT); pth_event(PTH_EVENT_SIG, &amp;set, &amp;sig);&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_EVENT_TIME&quot;</dt>
<dd> <p> This is a time point event. The additional argument has to be of type <code>&quot;pth_time_t&quot;</code> (usually on-the-fly generated via <i>pth_time</i>(3)). This events waits until the specified time point has elapsed. Keep in mind that the value is an absolute time point and not an offset. When you want to wait for a specified amount of time, you&#8217;ve to add the current time to the offset (usually on-the-fly achieved via <i>pth_timeout</i>(3)). Example: `<code>&quot;pth_event(PTH_EVENT_TIME, pth_timeout(2,0))&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_EVENT_MSG&quot;</dt>
<dd> <p> This is a message port event. The additional argument has to be of type <code>&quot;pth_msgport_t&quot;</code>. This events waits until one or more messages were received on the specified message port. Example: `<code>&quot;pth_event(PTH_EVENT_MSG, mp)&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_EVENT_TID&quot;</dt>
<dd> <p> This is a thread event. The additional argument has to be of type <code>&quot;pth_t&quot;</code>. One of <code>&quot;PTH_UNTIL_TID_NEW&quot;</code>, <code>&quot;PTH_UNTIL_TID_READY&quot;</code>, <code>&quot;PTH_UNTIL_TID_WAITING&quot;</code> or <code>&quot;PTH_UNTIL_TID_DEAD&quot;</code> has to be OR-ed into <i>spec</i> to specify on which state of the thread you want to wait. Example: `<code>&quot;pth_event(PTH_EVENT_TID|PTH_UNTIL_TID_DEAD, tid)&quot;</code>&#8216;. </p>
 </dd>
<dt>&quot;PTH_EVENT_FUNC&quot;</dt>
<dd> <p> This is a custom callback function event. Three additional arguments have to be given with the following types: `<code>&quot;int (*)(void *)&quot;</code>&#8216;, `<code>&quot;void *&quot;</code>&#8216; and `<code>&quot;pth_time_t&quot;</code>&#8216;. The first is a function pointer to a check function and the second argument is a user-supplied context value which is passed to this function. The scheduler calls this function on a regular basis (on his own scheduler stack, so be very careful!) and the thread is kept sleeping while the function returns <code>&quot;FALSE&quot;</code>. Once it returned <code>&quot;TRUE&quot;</code> the thread will be awakened. The check interval is defined by the third argument, i.e., the check function is polled again not until this amount of time elapsed. Example: `<code>&quot;pth_event(PTH_EVENT_FUNC, func, arg, pth_time(0,500000))&quot;</code>&#8216;. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>unsigned long <code>pth_event_typeof</code>(pth_event_t <i>ev</i>);</dt>
<dd> <p> This returns the type of event <i>ev</i>. It&#8217;s a combination of the describing <code>&quot;PTH_EVENT_XX&quot;</code> and <code>&quot;PTH_UNTIL_XX&quot;</code> value. This is especially useful to know which arguments have to be supplied to the <i>pth_event_extract</i>(3) function. </p>
 </dd>
<dt>int <code>pth_event_extract</code>(pth_event_t <i>ev</i>, ...);</dt>
<dd> <p> When <i>pth_event</i>(3) is treated like <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3), then this function is <i><a href="/docs/linux/man/3-sscanf/">sscanf</a></i>(3), i.e., it is the inverse operation of <i>pth_event</i>(3). This means that it can be used to extract the ingredients of an event. The ingredients are stored into variables which are given as pointers on the variable argument list. Which pointers have to be present depends on the event type and has to be determined by the caller before via <i>pth_event_typeof</i>(3). </p>
<p>To make it clear, when you constructed <i>ev</i> via `<code>&quot;ev = pth_event(PTH_EVENT_FD, fd);&quot;</code>&#8216; you have to extract it via `<code>&quot;pth_event_extract(ev, &amp;fd)&quot;</code>&#8216;, etc. For multiple arguments of an event the order of the pointer arguments is the same as for <i>pth_event</i>(3). But always keep in mind that you have to always supply <i>pointers</i> to <i>variables</i> and these variables have to be of the same type as the argument of <i>pth_event</i>(3) required. </p>
 </dd>
<dt>pth_event_t <code>pth_event_concat</code>(pth_event_t <i>ev</i>, ...);</dt>
<dd> <p> This concatenates one or more additional event rings to the event ring <i>ev</i> and returns <i>ev</i>. The end of the argument list has to be marked with a <code>&quot;NULL&quot;</code> argument. Use this function to create real events rings out of the single-event rings created by <i>pth_event</i>(3). </p>
 </dd>
<dt>pth_event_t <code>pth_event_isolate</code>(pth_event_t <i>ev</i>);</dt>
<dd> <p> This isolates the event <i>ev</i> from possibly appended events in the event ring. When in <i>ev</i> only one event exists, this returns <code>&quot;NULL&quot;</code>. When remaining events exists, they form a new event ring which is returned. </p>
 </dd>
<dt>pth_event_t <code>pth_event_walk</code>(pth_event_t <i>ev</i>, int <i>direction</i>);</dt>
<dd> <p> This walks to the next (when <i>direction</i> is <code>&quot;PTH_WALK_NEXT&quot;</code>) or previews (when <i>direction</i> is <code>&quot;PTH_WALK_PREV&quot;</code>) event in the event ring <i>ev</i> and returns this new reached event. Additionally <code>&quot;PTH_UNTIL_OCCURRED&quot;</code> can be OR-ed into <i>direction</i> to walk to the next/previous occurred event in the ring <i>ev</i>. </p>
 </dd>
<dt>pth_status_t <code>pth_event_status</code>(pth_event_t <i>ev</i>);</dt>
<dd> <p> This returns the status of event <i>ev</i>. This is a fast operation because only a tag on <i>ev</i> is checked which was either set or still not set by the scheduler. In other words: This doesn&#8217;t check the event itself, it just checks the last knowledge of the scheduler. The possible returned status codes are: <code>&quot;PTH_STATUS_PENDING&quot;</code> (event is still pending), <code>&quot;PTH_STATUS_OCCURRED&quot;</code> (event successfully occurred), <code>&quot;PTH_STATUS_FAILED&quot;</code> (event failed). </p>
 </dd>
<dt>int <code>pth_event_free</code>(pth_event_t <i>ev</i>, int <i>mode</i>);</dt>
<dd> <p> This deallocates the event <i>ev</i> (when <i>mode</i> is <code>&quot;PTH_FREE_THIS&quot;</code>) or all events appended to the event ring under <i>ev</i> (when <i>mode</i> is <code>&quot;PTH_FREE_ALL&quot;</code>). <br />
 </p>
 </dd></dl>
<p> <code>Key-Based Storage</code> </p>
<p>The following functions provide thread-local storage through unique keys similar to the <font SIZE="-1">POSIX</font> <code>Pthread</code> <font SIZE="-1">API</font>. Use this for thread specific global data. </p>
<dl>
<dt>int <code>pth_key_create</code>(pth_key_t *<i>key</i>, void (*<i>func</i>)(void *));</dt>
<dd> <p> This created a new unique key and stores it in <i>key</i>. Additionally <i>func</i> can specify a destructor function which is called on the current threads termination with the <i>key</i>. </p>
 </dd>
<dt>int <code>pth_key_delete</code>(pth_key_t <i>key</i>);</dt>
<dd> <p> This explicitly destroys a key <i>key</i>. </p>
 </dd>
<dt>int <code>pth_key_setdata</code>(pth_key_t <i>key</i>, const void *<i>value</i>);</dt>
<dd> <p> This stores <i>value</i> under <i>key</i>. </p>
 </dd>
<dt>void *<code>pth_key_getdata</code>(pth_key_t <i>key</i>);</dt>
<dd> <p> This retrieves the value under <i>key</i>. <br />
 </p>
 </dd></dl>
<p> <code>Message Port Communication</code> </p>
<p>The following functions provide message ports which can be used for efficient and flexible inter-thread communication. </p>
<dl>
<dt>pth_msgport_t <code>pth_msgport_create</code>(const char *<i>name</i>);</dt>
<dd> <p> This returns a pointer to a new message port. If name <i>name</i> is not <code>&quot;NULL&quot;</code>, the <i>name</i> can be used by other threads via <i>pth_msgport_find</i>(3) to find the message port in case they do not know directly the pointer to the message port. </p>
 </dd>
<dt>void <code>pth_msgport_destroy</code>(pth_msgport_t <i>mp</i>);</dt>
<dd> <p> This destroys a message port <i>mp</i>. Before all pending messages on it are replied to their origin message port. </p>
 </dd>
<dt>pth_msgport_t <code>pth_msgport_find</code>(const char *<i>name</i>);</dt>
<dd> <p> This finds a message port in the system by <i>name</i> and returns the pointer to it. </p>
 </dd>
<dt>int <code>pth_msgport_pending</code>(pth_msgport_t <i>mp</i>);</dt>
<dd> <p> This returns the number of pending messages on message port <i>mp</i>. </p>
 </dd>
<dt>int <code>pth_msgport_put</code>(pth_msgport_t <i>mp</i>, pth_message_t *<i>m</i>);</dt>
<dd> <p> This puts (or sends) a message <i>m</i> to message port <i>mp</i>. </p>
 </dd>
<dt>pth_message_t *<code>pth_msgport_get</code>(pth_msgport_t <i>mp</i>);</dt>
<dd> <p> This gets (or receives) the top message from message port <i>mp</i>. Incoming messages are always kept in a queue, so there can be more pending messages, of course. </p>
 </dd>
<dt>int <code>pth_msgport_reply</code>(pth_message_t *<i>m</i>);</dt>
<dd> <p> This replies a message <i>m</i> to the message port of the sender. <br />
 </p>
 </dd></dl>
<p> <code>Thread Cleanups</code> </p>
<p>Per-thread cleanup functions. </p>
<dl>
<dt>int <code>pth_cleanup_push</code>(void (*<i>handler</i>)(void *), void *<i>arg</i>);</dt>
<dd> <p> This pushes the routine <i>handler</i> onto the stack of cleanup routines for the current thread. These routines are called in <font SIZE="-1">LIFO</font> order when the thread terminates. </p>
 </dd>
<dt>int <code>pth_cleanup_pop</code>(int <i>execute</i>);</dt>
<dd> <p> This pops the top-most routine from the stack of cleanup routines for the current thread. When <i>execute</i> is <code>&quot;TRUE&quot;</code> the routine is additionally called. <br />
 </p>
 </dd></dl>
<p> <code>Process Forking</code> </p>
<p>The following functions provide some special support for process forking situations inside the threading environment. </p>
<dl>
<dt>int <code>pth_atfork_push</code>(void (*<i>prepare</i>)(void *), void (*)(void *<i>parent</i>), void (*)(void *<i>child</i>), void *<i>arg</i>);</dt>
<dd> <p> This function declares forking handlers to be called before and after <i>pth_fork</i>(3), in the context of the thread that called <i>pth_fork</i>(3). The <i>prepare</i> handler is called before <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) processing commences. The <i>parent</i> handler is called after <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) processing completes in the parent process. The <i>child</i> handler is called after <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) processing completed in the child process. If no handling is desired at one or more of these three points, the corresponding handler can be given as <code>&quot;NULL&quot;</code>. Each handler is called with <i>arg</i> as the argument. </p>
<p>The order of calls to <i>pth_atfork_push</i>(3) is significant. The <i>parent</i> and <i>child</i> handlers are called in the order in which they were established by calls to <i>pth_atfork_push</i>(3), i.e., <font SIZE="-1">FIFO</font>. The <i>prepare</i> fork handlers are called in the opposite order, i.e., <font SIZE="-1">LIFO</font>. </p>
 </dd>
<dt>int <code>pth_atfork_pop</code>(void);</dt>
<dd> <p> This removes the top-most handlers on the forking handler stack which were established with the last <i>pth_atfork_push</i>(3) call. It returns <code>&quot;FALSE&quot;</code> when no more handlers couldn&#8217;t be removed from the stack. </p>
 </dd>
<dt>pid_t <code>pth_fork</code>(void);</dt>
<dd> <p> This is a variant of <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) with the difference that the current thread only is forked into a separate process, i.e., in the parent process nothing changes while in the child process all threads are gone except for the scheduler and the calling thread. When you really want to duplicate all threads in the current process you should use <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) directly. But this is usually not reasonable. Additionally this function takes care of forking handlers as established by <i>pth_fork_push</i>(3). <br />
 </p>
 </dd></dl>
<p> <code>Synchronization</code> </p>
<p>The following functions provide synchronization support via mutual exclusion locks (<code>mutex</code>), read-write locks (<code>rwlock</code>), condition variables (<code>cond</code>) and barriers (<code>barrier</code>). Keep in mind that in a non-preemptive threading system like <code>Pth</code> this might sound unnecessary at the first look, because a thread isn&#8217;t interrupted by the system. Actually when you have a critical code section which doesn&#8217;t contain any <i>pth_xxx()</i> functions, you don&#8217;t need any mutex to protect it, of course. </p>
<p>But when your critical code section contains any <i>pth_xxx()</i> function the chance is high that these temporarily switch to the scheduler. And this way other threads can make progress and enter your critical code section, too. This is especially true for critical code sections which implicitly or explicitly use the event mechanism. </p>
<dl>
<dt>int <code>pth_mutex_init</code>(pth_mutex_t *<i>mutex</i>);</dt>
<dd> <p> This dynamically initializes a mutex variable of type `<code>&quot;pth_mutex_t&quot;</code>&#8216;. Alternatively one can also use static initialization via `<code>&quot;pth_mutex_t mutex = PTH_MUTEX_INIT&quot;</code>&#8216;. </p>
 </dd>
<dt>int <code>pth_mutex_acquire</code>(pth_mutex_t *<i>mutex</i>, int <i>try</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This acquires a mutex <i>mutex</i>. If the mutex is already locked by another thread, the current threads execution is suspended until the mutex is unlocked again or additionally the extra events in <i>ev</i> occurred (when <i>ev</i> is not <code>&quot;NULL&quot;</code>). Recursive locking is explicitly supported, i.e., a thread is allowed to acquire a mutex more than once before its released. But it then also has be released the same number of times until the mutex is again lockable by others. When <i>try</i> is <code>&quot;TRUE&quot;</code> this function never suspends execution. Instead it returns <code>&quot;FALSE&quot;</code> with <code>&quot;errno&quot;</code> set to <code>&quot;EBUSY&quot;</code>. </p>
 </dd>
<dt>int <code>pth_mutex_release</code>(pth_mutex_t *<i>mutex</i>);</dt>
<dd> <p> This decrements the recursion locking count on <i>mutex</i> and when it is zero it releases the mutex <i>mutex</i>. </p>
 </dd>
<dt>int <code>pth_rwlock_init</code>(pth_rwlock_t *<i>rwlock</i>);</dt>
<dd> <p> This dynamically initializes a read-write lock variable of type `<code>&quot;pth_rwlock_t&quot;</code>&#8216;. Alternatively one can also use static initialization via `<code>&quot;pth_rwlock_t rwlock = PTH_RWLOCK_INIT&quot;</code>&#8216;. </p>
 </dd>
<dt>int <code>pth_rwlock_acquire</code>(pth_rwlock_t *<i>rwlock</i>, int <i>op</i>, int <i>try</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This acquires a read-only (when <i>op</i> is <code>&quot;PTH_RWLOCK_RD&quot;</code>) or a read-write (when <i>op</i> is <code>&quot;PTH_RWLOCK_RW&quot;</code>) lock <i>rwlock</i>. When the lock is only locked by other threads in read-only mode, the lock succeeds. But when one thread holds a read-write lock, all locking attempts suspend the current thread until this lock is released again. Additionally in <i>ev</i> events can be given to let the locking timeout, etc. When <i>try</i> is <code>&quot;TRUE&quot;</code> this function never suspends execution. Instead it returns <code>&quot;FALSE&quot;</code> with <code>&quot;errno&quot;</code> set to <code>&quot;EBUSY&quot;</code>. </p>
 </dd>
<dt>int <code>pth_rwlock_release</code>(pth_rwlock_t *<i>rwlock</i>);</dt>
<dd> <p> This releases a previously acquired (read-only or read-write) lock. </p>
 </dd>
<dt>int <code>pth_cond_init</code>(pth_cond_t *<i>cond</i>);</dt>
<dd> <p> This dynamically initializes a condition variable variable of type `<code>&quot;pth_cond_t&quot;</code>&#8216;. Alternatively one can also use static initialization via `<code>&quot;pth_cond_t cond = PTH_COND_INIT&quot;</code>&#8216;. </p>
 </dd>
<dt>int <code>pth_cond_await</code>(pth_cond_t *<i>cond</i>, pth_mutex_t *<i>mutex</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This awaits a condition situation. The caller has to follow the semantics of the <font SIZE="-1">POSIX</font> condition variables: <i>mutex</i> has to be acquired before this function is called. The execution of the current thread is then suspended either until the events in <i>ev</i> occurred (when <i>ev</i> is not <code>&quot;NULL&quot;</code>) or <i>cond</i> was notified by another thread via <i>pth_cond_notify</i>(3). While the thread is waiting, <i>mutex</i> is released. Before it returns <i>mutex</i> is reacquired. </p>
 </dd>
<dt>int <code>pth_cond_notify</code>(pth_cond_t *<i>cond</i>, int <i>broadcast</i>);</dt>
<dd> <p> This notified one or all threads which are waiting on <i>cond</i>. When <i>broadcast</i> is <code>&quot;TRUE&quot;</code> all thread are notified, else only a single (unspecified) one. </p>
 </dd>
<dt>int <code>pth_barrier_init</code>(pth_barrier_t *<i>barrier</i>, int <i>threshold</i>);</dt>
<dd> <p> This dynamically initializes a barrier variable of type `<code>&quot;pth_barrier_t&quot;</code>&#8216;. Alternatively one can also use static initialization via `<code>&quot;pth_barrier_t barrier = PTH_BARRIER_INIT(&quot;</code><i>threadhold</i><code>&quot;)&quot;</code>&#8216;. </p>
 </dd>
<dt>int <code>pth_barrier_reach</code>(pth_barrier_t *<i>barrier</i>);</dt>
<dd> <p> This function reaches a barrier <i>barrier</i>. If this is the last thread (as specified by <i>threshold</i> on init of <i>barrier</i>) all threads are awakened. Else the current thread is suspended until the last thread reached the barrier and this way awakes all threads. The function returns (beside <code>&quot;FALSE&quot;</code> on error) the value <code>&quot;TRUE&quot;</code> for any thread which neither reached the barrier as the first nor the last thread; <code>&quot;PTH_BARRIER_HEADLIGHT&quot;</code> for the thread which reached the barrier as the first thread and <code>&quot;PTH_BARRIER_TAILLIGHT&quot;</code> for the thread which reached the barrier as the last thread. <br />
 </p>
 </dd></dl>
<p> <code>User-Space Context</code> </p>
<p>The following functions provide a stand-alone sub-API for user-space context switching. It internally is based on the same underlying machine context switching mechanism the threads in <font SIZE="-1"><code>GNU</code></font><code> Pth</code> are based on. Hence these functions you can use for implementing your own simple user-space threads. The <code>&quot;pth_uctx_t&quot;</code> context is somewhat modeled after <font SIZE="-1">POSIX</font> <i>ucontext</i>(3). </p>
<p>The time required to create (via <i>pth_uctx_make</i>(3)) a user-space context can range from just a few microseconds up to a more dramatical time (depending on the machine context switching method which is available on the platform). On the other hand, the raw performance in switching the user-space contexts is always very good (nearly independent of the used machine context switching method). For instance, on an Intel Pentium-III <font SIZE="-1">CPU</font> with 800Mhz running under FreeBSD 4 one usually achieves about 260,000 user-space context switches (via <i>pth_uctx_switch</i>(3)) per second. </p>
<dl>
<dt>int <code>pth_uctx_create</code>(pth_uctx_t *<i>uctx</i>);</dt>
<dd> <p> This function creates a user-space context and stores it into <i>uctx</i>. There is still no underlying user-space context configured. You still have to do this with <i>pth_uctx_make</i>(3). On success, this function returns <code>&quot;TRUE&quot;</code>, else <code>&quot;FALSE&quot;</code>. </p>
 </dd>
<dt>int <code>pth_uctx_make</code>(pth_uctx_t <i>uctx</i>, char *<i>sk_addr</i>, size_t <i>sk_size</i>, const sigset_t *<i>sigmask</i>, void (*<i>start_func</i>)(void *), void *<i>start_arg</i>, pth_uctx_t <i>uctx_after</i>);</dt>
<dd> <p> This function makes a new user-space context in <i>uctx</i> which will operate on the run-time stack <i>sk_addr</i> (which is of maximum size <i>sk_size</i>), with the signals in <i>sigmask</i> blocked (if <i>sigmask</i> is not <code>&quot;NULL&quot;</code>) and starting to execute with the call <i>start_func</i>(<i>start_arg</i>). If <i>sk_addr</i> is <code>&quot;NULL&quot;</code>, a stack is dynamically allocated. The stack size <i>sk_size</i> has to be at least 16384 (16KB). If the start function <i>start_func</i> returns and <i>uctx_after</i> is not <code>&quot;NULL&quot;</code>, an implicit user-space context switch to this context is performed. Else (if <i>uctx_after</i> is <code>&quot;NULL&quot;</code>) the process is terminated with <i><a href="/docs/linux/man/3-exit/">exit</a></i>(3). This function is somewhat modeled after <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/3-makecontext/">makecontext</a></i>(3). On success, this function returns <code>&quot;TRUE&quot;</code>, else <code>&quot;FALSE&quot;</code>. </p>
 </dd>
<dt>int <code>pth_uctx_switch</code>(pth_uctx_t <i>uctx_from</i>, pth_uctx_t <i>uctx_to</i>);</dt>
<dd> <p> This function saves the current user-space context in <i>uctx_from</i> for later restoring by another call to <i>pth_uctx_switch</i>(3) and restores the new user-space context from <i>uctx_to</i>, which previously had to be set with either a previous call to <i>pth_uctx_switch</i>(3) or initially by <i>pth_uctx_make</i>(3). This function is somewhat modeled after <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/3-swapcontext/">swapcontext</a></i>(3). If <i>uctx_from</i> or <i>uctx_to</i> are <code>&quot;NULL&quot;</code> or if <i>uctx_to</i> contains no valid user-space context, <code>&quot;FALSE&quot;</code> is returned instead of <code>&quot;TRUE&quot;</code>. These are the only errors possible. </p>
 </dd>
<dt>int <code>pth_uctx_destroy</code>(pth_uctx_t <i>uctx</i>);</dt>
<dd> <p> This function destroys the user-space context in <i>uctx</i>. The run-time stack associated with the user-space context is deallocated only if it was not given by the application (see <i>sk_addr</i> of <i>pth_uctx_create</i>(3)). If <i>uctx</i> is <code>&quot;NULL&quot;</code>, <code>&quot;FALSE&quot;</code> is returned instead of <code>&quot;TRUE&quot;</code>. This is the only error possible. <br />
 </p>
 </dd></dl>
<p> <code>Generalized <font SIZE="-1">POSIX</font> Replacement <font SIZE="-1">API</font></code> </p>
<p>The following functions are generalized replacements functions for the <font SIZE="-1">POSIX</font> <font SIZE="-1">API</font>, i.e., they are similar to the functions under `<code>Standard </code><font SIZE="-1"><code>POSIX</code></font><code> Replacement </code><font SIZE="-1"><code>API</code></font>&#8216; but all have an additional event argument which can be used for timeouts, etc. </p>
<dl>
<dt>int <code>pth_sigwait_ev</code>(const sigset_t *<i>set</i>, int *<i>sig</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_sigwait</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_sigwait</i>(3) suspends the current threads execution it usually only uses the signal event on <i>set</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>int <code>pth_connect_ev</code>(int <i>s</i>, const struct sockaddr *<i>addr</i>, socklen_t <i>addrlen</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_connect</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_connect</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>s</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>int <code>pth_accept_ev</code>(int <i>s</i>, struct sockaddr *<i>addr</i>, socklen_t *<i>addrlen</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_accept</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_accept</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>s</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>int <code>pth_select_ev</code>(int <i>nfd</i>, fd_set *<i>rfds</i>, fd_set *<i>wfds</i>, fd_set *<i>efds</i>, struct timeval *<i>timeout</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_select</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_select</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>rfds</i>, <i>wfds</i> and <i>efds</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>int <code>pth_poll_ev</code>(struct pollfd *<i>fds</i>, unsigned int <i>nfd</i>, int <i>timeout</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_poll</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_poll</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fds</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_read_ev</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_read</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_read</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_readv_ev</code>(int <i>fd</i>, const struct iovec *<i>iovec</i>, int <i>iovcnt</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_readv</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_readv</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_write_ev</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_write</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_write</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_writev_ev</code>(int <i>fd</i>, const struct iovec *<i>iovec</i>, int <i>iovcnt</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_writev</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_writev</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_recv_ev</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_recv</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_recv</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_recvfrom_ev</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, struct sockaddr *<i>from</i>, socklen_t *<i>fromlen</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_recvfrom</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_recvfrom</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_send_ev</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_send</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_send</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). </p>
 </dd>
<dt>ssize_t <code>pth_sendto_ev</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, const struct sockaddr *<i>to</i>, socklen_t <i>tolen</i>, pth_event_t <i>ev</i>);</dt>
<dd> <p> This is equal to <i>pth_sendto</i>(3) (see below), but has an additional event argument <i>ev</i>. When <i>pth_sendto</i>(3) suspends the current threads execution it usually only uses the I/O event on <i>fd</i> to awake. With this function any number of extra events can be used to awake the current thread (remember that <i>ev</i> actually is an event <i>ring</i>). <br />
 </p>
 </dd></dl>
<p> <code>Standard <font SIZE="-1">POSIX</font> Replacement <font SIZE="-1">API</font></code> </p>
<p>The following functions are standard replacements functions for the <font SIZE="-1">POSIX</font> <font SIZE="-1">API</font>. The difference is mainly that they suspend the current thread only instead of the whole process in case the file descriptors will block. </p>
<dl>
<dt>int <code>pth_nanosleep</code>(const struct timespec *<i>rqtp</i>, struct timespec *<i>rmtp</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i>nanosleep</i>(3) function. It suspends the current threads execution until the amount of time in <i>rqtp</i> elapsed. The thread is guaranteed to not wake up before this time, but because of the non-preemptive scheduling nature of <code>Pth</code>, it can be awakened later, of course. If <i>rmtp</i> is not <code>&quot;NULL&quot;</code>, the <code>&quot;timespec&quot;</code> structure it references is updated to contain the unslept amount (the request time minus the time actually slept time). The difference between <i>nanosleep</i>(3) and <i>pth_nanosleep</i>(3) is that that <i>pth_nanosleep</i>(3) suspends only the execution of the current thread and not the whole process. </p>
 </dd>
<dt>int <code>pth_usleep</code>(unsigned int <i>usec</i>);</dt>
<dd> <p> This is a variant of the 4.3BSD <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3) function. It suspends the current threads execution until <i>usec</i> microseconds (= <i>usec</i>*1/1000000 sec) elapsed. The thread is guaranteed to not wake up before this time, but because of the non-preemptive scheduling nature of <code>Pth</code>, it can be awakened later, of course. The difference between <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3) and <i>pth_usleep</i>(3) is that that <i>pth_usleep</i>(3) suspends only the execution of the current thread and not the whole process. </p>
 </dd>
<dt>unsigned int <code>pth_sleep</code>(unsigned int <i>sec</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/3-sleep/">sleep</a></i>(3) function. It suspends the current threads execution until <i>sec</i> seconds elapsed. The thread is guaranteed to not wake up before this time, but because of the non-preemptive scheduling nature of <code>Pth</code>, it can be awakened later, of course. The difference between <i><a href="/docs/linux/man/3-sleep/">sleep</a></i>(3) and <i>pth_sleep</i>(3) is that <i>pth_sleep</i>(3) suspends only the execution of the current thread and not the whole process. </p>
 </dd>
<dt>pid_t <code>pth_waitpid</code>(pid_t <i>pid</i>, int *<i>status</i>, int <i>options</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-waitpid/">waitpid</a></i>(2) function. It suspends the current threads execution until <i>status</i> information is available for a terminated child process <i>pid</i>. The difference between <i><a href="/docs/linux/man/2-waitpid/">waitpid</a></i>(2) and <i>pth_waitpid</i>(3) is that <i>pth_waitpid</i>(3) suspends only the execution of the current thread and not the whole process. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-waitpid/">waitpid</a></i>(2). </p>
 </dd>
<dt>int <code>pth_system</code>(const char *<i>cmd</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/3-system/">system</a></i>(3) function. It executes the shell command <i>cmd</i> with Bourne Shell (<code>&quot;sh&quot;</code>) and suspends the current threads execution until this command terminates. The difference between <i><a href="/docs/linux/man/3-system/">system</a></i>(3) and <i>pth_system</i>(3) is that <i>pth_system</i>(3) suspends only the execution of the current thread and not the whole process. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/3-system/">system</a></i>(3). </p>
 </dd>
<dt>int <code>pth_sigmask</code>(int <i>how</i>, const sigset_t *<i>set</i>, sigset_t *<i>oset</i>)</dt>
<dd> <p> This is the <code>Pth</code> thread-related equivalent of <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2) respectively <i><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></i>(3). The arguments <i>how</i>, <i>set</i> and <i>oset</i> directly relate to <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2), because <code>Pth</code> internally just uses <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2) here. So alternatively you can also directly call <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2), but for consistency reasons you should use this function <i>pth_sigmask</i>(3). </p>
 </dd>
<dt>int <code>pth_sigwait</code>(const sigset_t *<i>set</i>, int *<i>sig</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font>.1c <i><a href="/docs/linux/man/3-sigwait/">sigwait</a></i>(3) function. It suspends the current threads execution until a signal in <i>set</i> occurred and stores the signal number in <i>sig</i>. The important point is that the signal is not delivered to a signal handler. Instead it&#8217;s caught by the scheduler only in order to awake the <i>pth_sigwait()</i> call. The trick and noticeable point here is that this way you get an asynchronous aware application that is written completely synchronously. When you think about the problem of <i>asynchronous safe</i> functions you should recognize that this is a great benefit. </p>
 </dd>
<dt>int <code>pth_connect</code>(int <i>s</i>, const struct sockaddr *<i>addr</i>, socklen_t <i>addrlen</i>);</dt>
<dd> <p> This is a variant of the 4.2BSD <i><a href="/docs/linux/man/2-connect/">connect</a></i>(2) function. It establishes a connection on a socket <i>s</i> to target specified in <i>addr</i> and <i>addrlen</i>. The difference between <i><a href="/docs/linux/man/2-connect/">connect</a></i>(2) and <i>pth_connect</i>(3) is that <i>pth_connect</i>(3) suspends only the execution of the current thread and not the whole process. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-connect/">connect</a></i>(2). </p>
 </dd>
<dt>int <code>pth_accept</code>(int <i>s</i>, struct sockaddr *<i>addr</i>, socklen_t *<i>addrlen</i>);</dt>
<dd> <p> This is a variant of the 4.2BSD <i><a href="/docs/linux/man/2-accept/">accept</a></i>(2) function. It accepts a connection on a socket by extracting the first connection request on the queue of pending connections, creating a new socket with the same properties of <i>s</i> and allocates a new file descriptor for the socket (which is returned). The difference between <i><a href="/docs/linux/man/2-accept/">accept</a></i>(2) and <i>pth_accept</i>(3) is that <i>pth_accept</i>(3) suspends only the execution of the current thread and not the whole process. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-accept/">accept</a></i>(2). </p>
 </dd>
<dt>int <code>pth_select</code>(int <i>nfd</i>, fd_set *<i>rfds</i>, fd_set *<i>wfds</i>, fd_set *<i>efds</i>, struct timeval *<i>timeout</i>);</dt>
<dd> <p> This is a variant of the 4.2BSD <i><a href="/docs/linux/man/2-select/">select</a></i>(2) function. It examines the I/O descriptor sets whose addresses are passed in <i>rfds</i>, <i>wfds</i>, and <i>efds</i> to see if some of their descriptors are ready for reading, are ready for writing, or have an exceptional condition pending, respectively. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-select/">select</a></i>(2). </p>
 </dd>
<dt>int <code>pth_pselect</code>(int <i>nfd</i>, fd_set *<i>rfds</i>, fd_set *<i>wfds</i>, fd_set *<i>efds</i>, const struct timespec *<i>timeout</i>, const sigset_t *<i>sigmask</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-pselect/">pselect</a></i>(2) function, which in turn is a stronger variant of 4.2BSD <i><a href="/docs/linux/man/2-select/">select</a></i>(2). The difference is that the higher-resolution <code>&quot;struct timespec&quot;</code> is passed instead of the lower-resolution <code>&quot;struct timeval&quot;</code> and that a signal mask is specified which is temporarily set while waiting for input. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-pselect/">pselect</a></i>(2) and <i><a href="/docs/linux/man/2-select/">select</a></i>(2). </p>
 </dd>
<dt>int <code>pth_poll</code>(struct pollfd *<i>fds</i>, unsigned int <i>nfd</i>, int <i>timeout</i>);</dt>
<dd> <p> This is a variant of the SysV <i><a href="/docs/linux/man/2-poll/">poll</a></i>(2) function. It examines the I/O descriptors which are passed in the array <i>fds</i> to see if some of them are ready for reading, are ready for writing, or have an exceptional condition pending, respectively. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-poll/">poll</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_read</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-read/">read</a></i>(2) function. It reads up to <i>nbytes</i> bytes into <i>buf</i> from file descriptor <i>fd</i>. The difference between <i><a href="/docs/linux/man/2-read/">read</a></i>(2) and <i>pth_read</i>(2) is that <i>pth_read</i>(2) suspends execution of the current thread until the file descriptor is ready for reading. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-read/">read</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_readv</code>(int <i>fd</i>, const struct iovec *<i>iovec</i>, int <i>iovcnt</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-readv/">readv</a></i>(2) function. It reads data from file descriptor <i>fd</i> into the first <i>iovcnt</i> rows of the <i>iov</i> vector. The difference between <i><a href="/docs/linux/man/2-readv/">readv</a></i>(2) and <i>pth_readv</i>(2) is that <i>pth_readv</i>(2) suspends execution of the current thread until the file descriptor is ready for reading. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-readv/">readv</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_write</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-write/">write</a></i>(2) function. It writes <i>nbytes</i> bytes from <i>buf</i> to file descriptor <i>fd</i>. The difference between <i><a href="/docs/linux/man/2-write/">write</a></i>(2) and <i>pth_write</i>(2) is that <i>pth_write</i>(2) suspends execution of the current thread until the file descriptor is ready for writing. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-write/">write</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_writev</code>(int <i>fd</i>, const struct iovec *<i>iovec</i>, int <i>iovcnt</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i><a href="/docs/linux/man/2-writev/">writev</a></i>(2) function. It writes data to file descriptor <i>fd</i> from the first <i>iovcnt</i> rows of the <i>iov</i> vector. The difference between <i><a href="/docs/linux/man/2-writev/">writev</a></i>(2) and <i>pth_writev</i>(2) is that <i>pth_writev</i>(2) suspends execution of the current thread until the file descriptor is ready for reading. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-writev/">writev</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_pread</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, off_t <i>offset</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i>pread</i>(3) function. It performs the same action as a regular <i><a href="/docs/linux/man/2-read/">read</a></i>(2), except that it reads from a given position in the file without changing the file pointer. The first three arguments are the same as for <i>pth_read</i>(3) with the addition of a fourth argument <i>offset</i> for the desired position inside the file. </p>
 </dd>
<dt>ssize_t <code>pth_pwrite</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, off_t <i>offset</i>);</dt>
<dd> <p> This is a variant of the <font SIZE="-1">POSIX</font> <i>pwrite</i>(3) function. It performs the same action as a regular <i><a href="/docs/linux/man/2-write/">write</a></i>(2), except that it writes to a given position in the file without changing the file pointer. The first three arguments are the same as for <i>pth_write</i>(3) with the addition of a fourth argument <i>offset</i> for the desired position inside the file. </p>
 </dd>
<dt>ssize_t <code>pth_recv</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>);</dt>
<dd> <p> This is a variant of the SUSv2 <i><a href="/docs/linux/man/2-recv/">recv</a></i>(2) function and equal to ``pth_recvfrom(fd, buf, nbytes, flags, <font SIZE="-1">NULL</font>, 0)&#8216;&#8216;. </p>
 </dd>
<dt>ssize_t <code>pth_recvfrom</code>(int <i>fd</i>, void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, struct sockaddr *<i>from</i>, socklen_t *<i>fromlen</i>);</dt>
<dd> <p> This is a variant of the SUSv2 <i><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></i>(2) function. It reads up to <i>nbytes</i> bytes into <i>buf</i> from file descriptor <i>fd</i> while using <i>flags</i> and <i>from</i>/<i>fromlen</i>. The difference between <i><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></i>(2) and <i>pth_recvfrom</i>(2) is that <i>pth_recvfrom</i>(2) suspends execution of the current thread until the file descriptor is ready for reading. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></i>(2). </p>
 </dd>
<dt>ssize_t <code>pth_send</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>);</dt>
<dd> <p> This is a variant of the SUSv2 <i><a href="/docs/linux/man/2-send/">send</a></i>(2) function and equal to ``pth_sendto(fd, buf, nbytes, flags, <font SIZE="-1">NULL</font>, 0)&#8216;&#8216;. </p>
 </dd>
<dt>ssize_t <code>pth_sendto</code>(int <i>fd</i>, const void *<i>buf</i>, size_t <i>nbytes</i>, int <i>flags</i>, const struct sockaddr *<i>to</i>, socklen_t <i>tolen</i>);</dt>
<dd> <p> This is a variant of the SUSv2 <i><a href="/docs/linux/man/2-sendto/">sendto</a></i>(2) function. It writes <i>nbytes</i> bytes from <i>buf</i> to file descriptor <i>fd</i> while using <i>flags</i> and <i>to</i>/<i>tolen</i>. The difference between <i><a href="/docs/linux/man/2-sendto/">sendto</a></i>(2) and <i>pth_sendto</i>(2) is that <i>pth_sendto</i>(2) suspends execution of the current thread until the file descriptor is ready for writing. For more details about the arguments and return code semantics see <i><a href="/docs/linux/man/2-sendto/">sendto</a></i>(2). </p>
 </dd></dl>
<h2>EXAMPLE</h2>
<p> The following example is a useless server which does nothing more than listening on <font SIZE="-1">TCP</font> port 12345 and displaying the current time to the socket when a connection was established. For each incoming connection a thread is spawned. Additionally, to see more multithreading, a useless ticker thread runs simultaneously which outputs the current time to <code>&quot;stderr&quot;</code> every 5 seconds. The example contains <i>no</i> error checking and is <i>only</i> intended to show you the look and feel of <code>Pth</code>. </p>
<pre><code> #include &lt;stdio.h&gt;
 #include &lt;stdlib.h&gt;
 #include &lt;errno.h&gt;
 #include &lt;sys/types.h&gt;
 #include &lt;sys/socket.h&gt;
 #include &lt;netinet/in.h&gt;
 #include &lt;arpa/inet.h&gt;
 #include &lt;signal.h&gt;
 #include &lt;netdb.h&gt;
 #include &lt;unistd.h&gt;
 #include &quot;pth.h&quot;
</code></pre>
<pre><code> #define PORT 12345
</code></pre>
<pre><code> /* the socket connection handler thread */
 static void *handler(void *_arg)
 {
     int fd = (int)_arg;
     time_t now;
     char *ct;
</code></pre>
<pre><code>     now = time(NULL);
     ct = ctime(&amp;now);
     pth_write(fd, ct, strlen(ct));
     close(fd);
     return NULL;
 }
</code></pre>
<pre><code> /* the stderr time ticker thread */
 static void *ticker(void *_arg)
 {
     time_t now;
     char *ct;
     float load;
</code></pre>
<pre><code>     for (;;) {pth_sleep(5);
         now = time(NULL);
         ct = ctime(&amp;now);
         ct[strlen(ct)-1] = '\0';
         pth_ctrl(PTH_CTRL_GETAVLOAD, &amp;load);
         printf(&quot;ticker: time: %s, average load: %.2f\n&quot;, ct, load);
     }
 }
</code></pre>
<pre><code> /* the main thread/procedure */
 int main(int argc, char *argv[])
 {
     pth_attr_t attr;
     struct sockaddr_in sar;
     struct protoent *pe;
     struct sockaddr_in peer_addr;
     int peer_len;
     int sa, sw;
     int port;
</code></pre>
<pre><code>     pth_init();
     signal(SIGPIPE, SIG_IGN);
</code></pre>
<pre><code>     attr = pth_attr_new();
     pth_attr_set(attr, PTH_ATTR_NAME, &quot;ticker&quot;);
     pth_attr_set(attr, PTH_ATTR_STACK_SIZE, 64*1024);
     pth_attr_set(attr, PTH_ATTR_JOINABLE, FALSE);
     pth_spawn(attr, ticker, NULL);
</code></pre>
<pre><code>     pe = getprotobyname(&quot;tcp&quot;);
     sa = socket(AF_INET, SOCK_STREAM, pe-&gt;p_proto);
     sar.sin_family = AF_INET;
     sar.sin_addr.s_addr = INADDR_ANY;
     sar.sin_port = htons(PORT);
     bind(sa, (struct sockaddr *)&amp;sar, sizeof(struct sockaddr_in));
     listen(sa, 10);
</code></pre>
<pre><code>     pth_attr_set(attr, PTH_ATTR_NAME, &quot;handler&quot;);
     for (;;) {
         peer_len = sizeof(peer_addr);
         sw = pth_accept(sa, (struct sockaddr *)&amp;peer_addr, &amp;peer_len);
         pth_spawn(attr, handler, (void *)sw);
     }
 }
</code></pre>
<h2>BUILD ENVIRONMENTS</h2>
<p> In this section we will discuss the canonical ways to establish the build environment for a <code>Pth</code> based program. The possibilities supported by <code>Pth</code> range from very simple environments to rather complex ones. <br />
 </p>
<p> <code>Manual Build Environment (Novice)</code> </p>
<p>As a first example, assume we have the above test program staying in the source file <code>&quot;foo.c&quot;</code>. Then we can create a very simple build environment by just adding the following <code>&quot;Makefile&quot;</code>: </p>
<pre><code> $ vi Makefile
 | CC = cc
 | CFLAGS = `pth-config --cflags`
 | LDFLAGS = `pth-config --ldflags`
 | LIBS = `pth-config --libs`
 |
 | all: foo
 | foo: foo.o
 | $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 | foo.o: foo.c
 | $(CC) $(CFLAGS) -c foo.c
 | clean:
 | rm -f foo foo.o
</code></pre>
<p>This imports the necessary compiler and linker flags on-the-fly from the <code>Pth</code> installation via its <code>&quot;pth-config&quot;</code> program. This approach is straight-forward and works fine for small projects. <br />
 </p>
<p> <code>Autoconf Build Environment (Advanced)</code> </p>
<p>The previous approach is simple but inflexible. First, to speed up building, it would be nice to not expand the compiler and linker flags every time the compiler is started. Second, it would be useful to also be able to build against uninstalled <code>Pth</code>, that is, against a <code>Pth</code> source tree which was just configured and built, but not installed. Third, it would be also useful to allow checking of the <code>Pth</code> version to make sure it is at least a minimum required version. And finally, it would be also great to make sure <code>Pth</code> works correctly by first performing some sanity compile and run-time checks. All this can be done if we use <font SIZE="-1">GNU</font> <code>autoconf</code> and the <code>&quot;AC_CHECK_PTH&quot;</code> macro provided by <code>Pth</code>. For this, we establish the following three files: </p>
<p>First we again need the <code>&quot;Makefile&quot;</code>, but this time it contains <code>autoconf</code> placeholders and additional cleanup targets. And we create it under the name <code>&quot;Makefile.in&quot;</code>, because it is now an input file for <code>autoconf</code>: </p>
<pre><code> $ vi Makefile.in
 | CC = @CC@
 | CFLAGS = @CFLAGS@
 | LDFLAGS = @LDFLAGS@
 | LIBS = @LIBS@
 |
 | all: foo
 | foo: foo.o
 | $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 | foo.o: foo.c
 | $(CC) $(CFLAGS) -c foo.c
 | clean:
 | rm -f foo foo.o
 | distclean:
 | rm -f foo foo.o
 | rm -f config.log config.status config.cache
 | rm -f Makefile
</code></pre>
<p>Because <code>autoconf</code> generates additional files, we added a canonical <code>&quot;distclean&quot;</code> target which cleans this up. Secondly, we wrote <code>&quot;configure.ac&quot;</code>, a (minimal) <code>autoconf</code> script specification: </p>
<pre><code> $ vi configure.ac
 | AC_INIT(Makefile.in)
 | AC_CHECK_PTH(1.3.0)
 | AC_OUTPUT(Makefile)
</code></pre>
<p>Then we let <code>autoconf</code>&#8216;s <code>&quot;aclocal&quot;</code> program generate for us an <code>&quot;aclocal.m4&quot;</code> file containing <code>Pth</code>&#8216;s <code>&quot;AC_CHECK_PTH&quot;</code> macro. Then we generate the final <code>&quot;configure&quot;</code> script out of this <code>&quot;aclocal.m4&quot;</code> file and the <code>&quot;configure.ac&quot;</code> file: </p>
<pre><code> $ aclocal --acdir=`pth-config --acdir`
 $ autoconf
</code></pre>
<p>After these steps, the working directory should look similar to this: </p>
<pre><code> $ ls -l
 -rw-r--r-- 1 rse users 176 Nov 3 11:11 Makefile.in
 -rw-r--r-- 1 rse users 15314 Nov 3 11:16 aclocal.m4
 -rwxr-xr-x 1 rse users 52045 Nov 3 11:16 configure
 -rw-r--r-- 1 rse users 63 Nov 3 11:11 configure.ac
 -rw-r--r-- 1 rse users 4227 Nov 3 11:11 foo.c
</code></pre>
<p>If we now run <code>&quot;configure&quot;</code> we get a correct <code>&quot;Makefile&quot;</code> which immediately can be used to build <code>&quot;foo&quot;</code> (assuming that <code>Pth</code> is already installed somewhere, so that <code>&quot;pth-config&quot;</code> is in <code>$PATH</code>): </p>
<pre><code> $ ./configure
 creating cache ./config.cache
 checking for gcc... gcc
 checking whether the C compiler (gcc ) works... yes
 checking whether the C compiler (gcc ) is a cross-compiler... no
 checking whether we are using GNU C... yes
 checking whether gcc accepts -g... yes
 checking how to run the C preprocessor... gcc -E
 checking for GNU Pth... version 1.3.0, installed under /usr/local
 updating cache ./config.cache
 creating ./config.status
 creating Makefile
 rse@en1:/e/gnu/pth/ac
 $ make
 gcc -g -O2 -I/usr/local/include -c foo.c
 gcc -L/usr/local/lib -o foo foo.o -lpth
</code></pre>
<p>If <code>Pth</code> is installed in non-standard locations or <code>&quot;pth-config&quot;</code> is not in <code>$PATH</code>, one just has to drop the <code>&quot;configure&quot;</code> script a note about the location by running <code>&quot;configure&quot;</code> with the option <code>&quot;--with-pth=&quot;</code><i>dir</i> (where <i>dir</i> is the argument which was used with the <code>&quot;--prefix&quot;</code> option when <code>Pth</code> was installed). <br />
 </p>
<p> <code>Autoconf Build Environment with Local Copy of Pth (Expert)</code> </p>
<p>Finally let us assume the <code>&quot;foo&quot;</code> program stays under either a <i></i><font SIZE="-1"><i>GPL</i></font><i></i> or <i></i><font SIZE="-1"><i>LGPL</i></font><i></i> distribution license and we want to make it a stand-alone package for easier distribution and installation. That is, we don&#8217;t want to oblige the end-user to install <code>Pth</code> just to allow our <code>&quot;foo&quot;</code> package to compile. For this, it is a convenient practice to include the required libraries (here <code>Pth</code>) into the source tree of the package (here <code>&quot;foo&quot;</code>). <code>Pth</code> ships with all necessary support to allow us to easily achieve this approach. Say, we want <code>Pth</code> in a subdirectory named <code>&quot;pth/&quot;</code> and this directory should be seamlessly integrated into the configuration and build process of <code>&quot;foo&quot;</code>. </p>
<p>First we again start with the <code>&quot;Makefile.in&quot;</code>, but this time it is a more advanced version which supports subdirectory movement: </p>
<pre><code> $ vi Makefile.in
 | CC = @CC@
 | CFLAGS = @CFLAGS@
 | LDFLAGS = @LDFLAGS@
 | LIBS = @LIBS@
 |
 | SUBDIRS = pth
 |
 | all: subdirs_all foo
 |
 | subdirs_all:
 | @$(MAKE) $(MFLAGS) subdirs TARGET=all
 | subdirs_clean:
 | @$(MAKE) $(MFLAGS) subdirs TARGET=clean
 | subdirs_distclean:
 | @$(MAKE) $(MFLAGS) subdirs TARGET=distclean
 | subdirs:
 | @for subdir in $(SUBDIRS); do \
 | echo &quot;===&gt; $$subdir ($(TARGET))&quot;; \
 | (cd $$subdir; $(MAKE) $(MFLAGS) $(TARGET) || exit 1) || exit 1; \
 | echo &quot;&lt;=== $$subdir&quot;; \
 | done
 |
 | foo: foo.o
 | $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 | foo.o: foo.c
 | $(CC) $(CFLAGS) -c foo.c
 |
 | clean: subdirs_clean
 | rm -f foo foo.o
 | distclean: subdirs_distclean
 | rm -f foo foo.o
 | rm -f config.log config.status config.cache
 | rm -f Makefile
</code></pre>
<p>Then we create a slightly different <code>autoconf</code> script <code>&quot;configure.ac&quot;</code>: </p>
<pre><code> $ vi configure.ac
 | AC_INIT(Makefile.in)
 | AC_CONFIG_AUX_DIR(pth)
 | AC_CHECK_PTH(1.3.0, subdir:pth --disable-tests)
 | AC_CONFIG_SUBDIRS(pth)
 | AC_OUTPUT(Makefile)
</code></pre>
<p>Here we provided a default value for <code>&quot;foo&quot;</code>&#8216;s <code>&quot;--with-pth&quot;</code> option as the second argument to <code>&quot;AC_CHECK_PTH&quot;</code> which indicates that <code>Pth</code> can be found in the subdirectory named <code>&quot;pth/&quot;</code>. Additionally we specified that the <code>&quot;--disable-tests&quot;</code> option of <code>Pth</code> should be passed to the <code>&quot;pth/&quot;</code> subdirectory, because we need only to build the <code>Pth</code> library itself. And we added a <code>&quot;AC_CONFIG_SUBDIR&quot;</code> call which indicates to <code>autoconf</code> that it should configure the <code>&quot;pth/&quot;</code> subdirectory, too. The <code>&quot;AC_CONFIG_AUX_DIR&quot;</code> directive was added just to make <code>autoconf</code> happy, because it wants to find a <code>&quot;install.sh&quot;</code> or <code>&quot;shtool&quot;</code> script if <code>&quot;AC_CONFIG_SUBDIRS&quot;</code> is used. </p>
<p>Now we let <code>autoconf</code>&#8216;s <code>&quot;aclocal&quot;</code> program again generate for us an <code>&quot;aclocal.m4&quot;</code> file with the contents of <code>Pth</code>&#8216;s <code>&quot;AC_CHECK_PTH&quot;</code> macro. Finally we generate the <code>&quot;configure&quot;</code> script out of this <code>&quot;aclocal.m4&quot;</code> file and the <code>&quot;configure.ac&quot;</code> file. </p>
<pre><code> $ aclocal --acdir=`pth-config --acdir`
 $ autoconf
</code></pre>
<p>Now we have to create the <code>&quot;pth/&quot;</code> subdirectory itself. For this, we extract the <code>Pth</code> distribution to the <code>&quot;foo&quot;</code> source tree and just rename it to <code>&quot;pth/&quot;</code>: </p>
<pre><code> $ gunzip &lt;pth-X.Y.Z.tar.gz | tar xvf -
 $ mv pth-X.Y.Z pth
</code></pre>
<p>Optionally to reduce the size of the <code>&quot;pth/&quot;</code> subdirectory, we can strip down the <code>Pth</code> sources to a minimum with the <i>striptease</i> feature: </p>
<pre><code> $ cd pth
 $ ./configure
 $ make striptease
 $ cd ..
</code></pre>
<p>After this the source tree of <code>&quot;foo&quot;</code> should look similar to this: </p>
<pre><code> $ ls -l
 -rw-r--r-- 1 rse users 709 Nov 3 11:51 Makefile.in
 -rw-r--r-- 1 rse users 16431 Nov 3 12:20 aclocal.m4
 -rwxr-xr-x 1 rse users 57403 Nov 3 12:21 configure
 -rw-r--r-- 1 rse users 129 Nov 3 12:21 configure.ac
 -rw-r--r-- 1 rse users 4227 Nov 3 11:11 foo.c
 drwxr-xr-x 2 rse users 3584 Nov 3 12:36 pth
 $ ls -l pth/
 -rw-rw-r-- 1 rse users 26344 Nov 1 20:12 COPYING
 -rw-rw-r-- 1 rse users 2042 Nov 3 12:36 Makefile.in
 -rw-rw-r-- 1 rse users 3967 Nov 1 19:48 README
 -rw-rw-r-- 1 rse users 340 Nov 3 12:36 README.1st
 -rw-rw-r-- 1 rse users 28719 Oct 31 17:06 config.guess
 -rw-rw-r-- 1 rse users 24274 Aug 18 13:31 config.sub
 -rwxrwxr-x 1 rse users 155141 Nov 3 12:36 configure
 -rw-rw-r-- 1 rse users 162021 Nov 3 12:36 pth.c
 -rw-rw-r-- 1 rse users 18687 Nov 2 15:19 pth.h.in
 -rw-rw-r-- 1 rse users 5251 Oct 31 12:46 pth_acdef.h.in
 -rw-rw-r-- 1 rse users 2120 Nov 1 11:27 pth_acmac.h.in
 -rw-rw-r-- 1 rse users 2323 Nov 1 11:27 pth_p.h.in
 -rw-rw-r-- 1 rse users 946 Nov 1 11:27 pth_vers.c
 -rw-rw-r-- 1 rse users 26848 Nov 1 11:27 pthread.c
 -rw-rw-r-- 1 rse users 18772 Nov 1 11:27 pthread.h.in
 -rwxrwxr-x 1 rse users 26188 Nov 3 12:36 shtool
</code></pre>
<p>Now when we configure and build the <code>&quot;foo&quot;</code> package it looks similar to this: </p>
<pre><code> $ ./configure
 creating cache ./config.cache
 checking for gcc... gcc
 checking whether the C compiler (gcc ) works... yes
 checking whether the C compiler (gcc ) is a cross-compiler... no
 checking whether we are using GNU C... yes
 checking whether gcc accepts -g... yes
 checking how to run the C preprocessor... gcc -E
 checking for GNU Pth... version 1.3.0, local under pth
 updating cache ./config.cache
 creating ./config.status
 creating Makefile
 configuring in pth
 running /bin/sh ./configure --enable-subdir --enable-batch
 --disable-tests --cache-file=.././config.cache --srcdir=.
 loading cache .././config.cache
 checking for gcc... (cached) gcc
 checking whether the C compiler (gcc ) works... yes
 checking whether the C compiler (gcc ) is a cross-compiler... no
 [...]
 $ make
 ===&gt; pth (all)
 ./shtool scpp -o pth_p.h -t pth_p.h.in -Dcpp -Cintern -M '==#==' pth.c
 pth_vers.c
 gcc -c -I. -O2 -pipe pth.c
 gcc -c -I. -O2 -pipe pth_vers.c
 ar rc libpth.a pth.o pth_vers.o
 ranlib libpth.a
 &lt;=== pth
 gcc -g -O2 -Ipth -c foo.c
 gcc -Lpth -o foo foo.o -lpth
</code></pre>
<p>As you can see, <code>autoconf</code> now automatically configures the local (stripped down) copy of <code>Pth</code> in the subdirectory <code>&quot;pth/&quot;</code> and the <code>&quot;Makefile&quot;</code> automatically builds the subdirectory, too.  </p>
<h2>SYSTEM CALL WRAPPER FACILITY</h2>
<p> <code>Pth</code> per default uses an explicit <font SIZE="-1">API</font>, including the system calls. For instance you&#8217;ve to explicitly use <i>pth_read</i>(3) when you need a thread-aware <i>read</i>(3) and cannot expect that by just calling <i>read</i>(3) only the current thread is blocked. Instead with the standard <i>read</i>(3) call the whole process will be blocked. But because for some applications (mainly those consisting of lots of third-party stuff) this can be inconvenient. Here it&#8217;s required that a call to <i>read</i>(3) `magically&#8217; means <i>pth_read</i>(3). The problem here is that such magic <code>Pth</code> cannot provide per default because it&#8217;s not really portable. Nevertheless <code>Pth</code> provides a two step approach to solve this problem: <br />
 </p>
<p> <code>Soft System Call Mapping</code> </p>
<p>This variant is available on all platforms and can <i>always</i> be enabled by building <code>Pth</code> with <code>&quot;--enable-syscall-soft&quot;</code>. This then triggers some <code>&quot;#define&quot;</code>&#8216;s in the <code>&quot;pth.h&quot;</code> header which map for instance <i>read</i>(3) to <i>pth_read</i>(3), etc. Currently the following functions are mapped: <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2), <i>nanosleep</i>(3), <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3), <i><a href="/docs/linux/man/3-sleep/">sleep</a></i>(3), <i><a href="/docs/linux/man/3-sigwait/">sigwait</a></i>(3), <i><a href="/docs/linux/man/2-waitpid/">waitpid</a></i>(2), <i><a href="/docs/linux/man/3-system/">system</a></i>(3), <i><a href="/docs/linux/man/2-select/">select</a></i>(2), <i><a href="/docs/linux/man/2-poll/">poll</a></i>(2), <i><a href="/docs/linux/man/2-connect/">connect</a></i>(2), <i><a href="/docs/linux/man/2-accept/">accept</a></i>(2), <i><a href="/docs/linux/man/2-read/">read</a></i>(2), <i><a href="/docs/linux/man/2-write/">write</a></i>(2), <i><a href="/docs/linux/man/2-recv/">recv</a></i>(2), <i><a href="/docs/linux/man/2-send/">send</a></i>(2), <i><a href="/docs/linux/man/2-recvfrom/">recvfrom</a></i>(2), <i><a href="/docs/linux/man/2-sendto/">sendto</a></i>(2). </p>
<p>The drawback of this approach is just that really all source files of the application where these function calls occur have to include <code>&quot;pth.h&quot;</code>, of course. And this also means that existing libraries, including the vendor&#8217;s <code>stdio</code>, usually will still block the whole process if one of its I/O functions block. <br />
 </p>
<p> <code>Hard System Call Mapping</code> </p>
<p>This variant is available only on those platforms where the <i><a href="/docs/linux/man/2-syscall/">syscall</a></i>(2) function exists and there it can be enabled by building <code>Pth</code> with <code>&quot;--enable-syscall-hard&quot;</code>. This then builds wrapper functions (for instances <i>read</i>(3)) into the <code>Pth</code> library which internally call the real <code>Pth</code> replacement functions (<i>pth_read</i>(3)). Currently the following functions are mapped: <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2), <i>nanosleep</i>(3), <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3), <i><a href="/docs/linux/man/3-sleep/">sleep</a></i>(3), <i><a href="/docs/linux/man/2-waitpid/">waitpid</a></i>(2), <i><a href="/docs/linux/man/3-system/">system</a></i>(3), <i><a href="/docs/linux/man/2-select/">select</a></i>(2), <i><a href="/docs/linux/man/2-poll/">poll</a></i>(2), <i><a href="/docs/linux/man/2-connect/">connect</a></i>(2), <i><a href="/docs/linux/man/2-accept/">accept</a></i>(2), <i><a href="/docs/linux/man/2-read/">read</a></i>(2), <i><a href="/docs/linux/man/2-write/">write</a></i>(2). </p>
<p>The drawback of this approach is that it depends on <i><a href="/docs/linux/man/2-syscall/">syscall</a></i>(2) interface and prototype conflicts can occur while building the wrapper functions due to different function signatures in the vendor C header files. But the advantage of this mapping variant is that the source files of the application where these function calls occur have not to include <code>&quot;pth.h&quot;</code> and that existing libraries, including the vendor&#8217;s <code>stdio</code>, magically become thread-aware (and then block only the current thread).  </p>
<h2>IMPLEMENTATION NOTES</h2>
<p> <code>Pth</code> is very portable because it has only one part which perhaps has to be ported to new platforms (the machine context initialization). But it is written in a way which works on mostly all Unix platforms which support <i>makecontext</i>(2) or at least <i>sigstack</i>(2) or <i><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></i>(2) [see <code>&quot;pth_mctx.c&quot;</code> for details]. Any other <code>Pth</code> code is <font SIZE="-1">POSIX</font> and <font SIZE="-1">ANSI</font> C based only. </p>
<p>The context switching is done via either SUSv2 <i>makecontext</i>(2) or <font SIZE="-1">POSIX</font> make[sig]<i><a href="/docs/linux/man/3-setjmp/">setjmp</a></i>(3) and [sig]<i><a href="/docs/linux/man/3-longjmp/">longjmp</a></i>(3). Here all <font SIZE="-1">CPU</font> registers, the program counter and the stack pointer are switched. Additionally the <code>Pth</code> dispatcher switches also the global Unix <code>&quot;errno&quot;</code> variable [see <code>&quot;pth_mctx.c&quot;</code> for details] and the signal mask (either implicitly via <i><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></i>(3) or in an emulated way via explicit <i>setprocmask</i>(2) calls). </p>
<p>The <code>Pth</code> event manager is mainly <i><a href="/docs/linux/man/2-select/">select</a></i>(2) and <i><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></i>(2) based, i.e., the current time is fetched via <i><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></i>(2) once per context switch for time calculations and all I/O events are implemented via a single central <i><a href="/docs/linux/man/2-select/">select</a></i>(2) call [see <code>&quot;pth_sched.c&quot;</code> for details]. </p>
<p>The thread control block management is done via virtual priority queues without any additional data structure overhead. For this, the queue linkage attributes are part of the thread control blocks and the queues are actually implemented as rings with a selected element as the entry point [see <code>&quot;pth_tcb.h&quot;</code> and <code>&quot;pth_pqueue.c&quot;</code> for details]. </p>
<p>Most time critical code sections (especially the dispatcher and event manager) are speeded up by inline functions (implemented as <font SIZE="-1">ANSI</font> C pre-processor macros). Additionally any debugging code is <i>completely</i> removed from the source when not built with <code>&quot;-DPTH_DEBUG&quot;</code> (see Autoconf <code>&quot;--enable-debug&quot;</code> option), i.e., not only stub functions remain [see <code>&quot;pth_debug.c&quot;</code> for details].  </p>
<h2>RESTRICTIONS</h2>
<p> <code>Pth</code> (intentionally) provides no replacements for non-thread-safe functions (like <i><a href="/docs/linux/man/3-strtok/">strtok</a></i>(3) which uses a static internal buffer) or synchronous system functions (like <i><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></i>(3) which doesn&#8217;t provide an asynchronous mode where it doesn&#8217;t block). When you want to use those functions in your server application together with threads, you&#8217;ve to either link the application against special third-party libraries (or for thread-safe/reentrant functions possibly against an existing <code>&quot;libc_r&quot;</code> of the platform vendor). For an asynchronous <font SIZE="-1">DNS</font> resolver library use the <font SIZE="-1">GNU</font> <code>adns</code> package from Ian Jackson ( see <a rel="nofollow" href="http://www.gnu.org/software/adns/adns.html">http://www.gnu.org/software/adns/adns.html</a> ).  </p>
<h2>HISTORY</h2>
<p> The <code>Pth</code> library was designed and implemented between February and July 1999 by <i>Ralf S. Engelschall</i> after evaluating numerous (mostly preemptive) thread libraries and after intensive discussions with <i>Peter Simons</i>, <i>Martin Kraemer</i>, <i>Lars Eilebrecht</i> and <i>Ralph Babel</i> related to an experimental (matrix based) non-preemptive C<font SIZE="-2">++</font> scheduler class written by <i>Peter Simons</i>. </p>
<p> <code>Pth</code> was then implemented in order to combine the <i>non-preemptive</i> approach of multithreading (which provides better portability and performance) with an <font SIZE="-1">API</font> similar to the popular one found in <code>Pthread</code> libraries (which provides easy programming). </p>
<p>So the essential idea of the non-preemptive approach was taken over from <i>Peter Simons</i> scheduler. The priority based scheduling algorithm was suggested by <i>Martin Kraemer</i>. Some code inspiration also came from an experimental threading library (<code>rsthreads</code>) written by <i>Robert S. Thau</i> for an ancient internal test version of the Apache webserver. The concept and <font SIZE="-1">API</font> of message ports was borrowed from AmigaOS&#8217; <code>Exec</code> subsystem. The concept and idea for the flexible event mechanism came from <i>Paul Vixie</i>&#8216;s <code>eventlib</code> (which can be found as a part of <font SIZE="-1"><code>BIND</code></font> v8).  </p>
<h2>BUG REPORTS AND SUPPORT</h2>
<p> If you think you have found a bug in <code>Pth</code>, you should send a report as complete as possible to <i>bug-pth [at] gnu.org</i>. If you can, please try to fix the problem and include a patch, made with &#8216;<code>&quot;diff -u3&quot;</code>&#8216;, in your report. Always, at least, include a reasonable amount of description in your report to allow the author to deterministically reproduce the bug. </p>
<p>For further support you additionally can subscribe to the <i>pth-users [at] gnu.org</i> mailing list by sending an Email to <i>pth-users-request [at] gnu.org</i> with `<code>&quot;subscribe pth-users&quot;</code>&#8216; (or `<code>&quot;subscribe pth-users&quot;</code> <i>address</i>&#8216; if you want to subscribe from a particular Email <i>address</i>) in the body. Then you can discuss your issues with other <code>Pth</code> users by sending messages to <i>pth-users [at] gnu.org</i>. Currently (as of August 2000) you can reach about 110 Pth users on this mailing list. Old postings you can find at <i><a rel="nofollow" href="http://www.mail-archive.com/pth-users@gnu.org/">http://www.mail-archive.com/pth-users@gnu.org/</a></i>.  </p>
<h2>SEE ALSO</h2>
<p> <br />
 </p>
<p> <code>Related Web Locations</code> </p>
<p>`comp.programming.threads Newsgroup Archive&#8217;, <a rel="nofollow" href="http://www.deja.com/topics_if.xp?">http://www.deja.com/topics_if.xp?</a> search=topic&amp;group=comp.programming.threads </p>
<p>`comp.programming.threads Frequently Asked Questions (F.A.Q.)&#8216;, <a rel="nofollow" href="http://www.lambdacs.com/newsgroup/FAQ.html">http://www.lambdacs.com/newsgroup/FAQ.html</a> </p>
<p>`<i>Multithreading - Definitions and Guidelines</i>&#8216;, Numeric Quest Inc 1998; <a rel="nofollow" href="http://www.numeric-quest.com/lang/multi-frame.html">http://www.numeric-quest.com/lang/multi-frame.html</a> </p>
<p>`<i>The Single </i><font SIZE="-1"><i>UNIX</i></font><i> Specification, Version 2 - Threads</i>&#8216;, The Open Group 1997; <a rel="nofollow" href="http://www.opengroup.org/onlinepubs">http://www.opengroup.org/onlinepubs</a> /007908799/xsh/threads.html </p>
<p> <font SIZE="-1">SMI</font> Thread Resources, Sun Microsystems Inc; <a rel="nofollow" href="http://www.sun.com/workshop/threads/">http://www.sun.com/workshop/threads/</a> </p>
<p>Bibliography on threads and multithreading, Torsten Amundsen; <a rel="nofollow" href="http://liinwww.ira.uka.de/bibliography/Os/threads.html">http://liinwww.ira.uka.de/bibliography/Os/threads.html</a> <br />
 </p>
<p> <code>Related Books</code> </p>
<p>B. Nichols, D. Buttlar, J.P. Farrel: `<i>Pthreads Programming - A </i><font SIZE="-1"><i>POSIX</i></font><i> Standard for Better Multiprocessing</i>&#8216;, O&#8217;Reilly 1996; <font SIZE="-1">ISBN</font> 1-56592-115-1 </p>
<p>B. Lewis, D. J. Berg: `<i>Multithreaded Programming with Pthreads</i>&#8216;, Sun Microsystems Press, Prentice Hall 1998; <font SIZE="-1">ISBN</font> 0-13-680729-1 </p>
<p>B. Lewis, D. J. Berg: `<i>Threads Primer - A Guide To Multithreaded Programming</i>&#8216;, Prentice Hall 1996; <font SIZE="-1">ISBN</font> 0-13-443698-9 </p>
<p>S. J. Norton, M. D. Dipasquale: `<i>Thread Time - The Multithreaded Programming Guide</i>&#8216;, Prentice Hall 1997; <font SIZE="-1">ISBN</font> 0-13-190067-6 </p>
<p>D. R. Butenhof: `<i>Programming with </i><font SIZE="-1"><i>POSIX</i></font><i> Threads</i>&#8216;, Addison Wesley 1997; <font SIZE="-1">ISBN</font> 0-201-63392-2 <br />
 </p>
<p> <code>Related Manpages</code> </p>
<p> <i><a href="/docs/linux/man/1-pth-config/">pth-config</a></i>(1), <i>pthread</i>(3). </p>
<p> <i><a href="/docs/linux/man/2-getcontext/">getcontext</a></i>(2), <i><a href="/docs/linux/man/2-setcontext/">setcontext</a></i>(2), <i>makecontext</i>(2), <i><a href="/docs/linux/man/2-swapcontext/">swapcontext</a></i>(2), <i>sigstack</i>(2), <i><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></i>(2), <i><a href="/docs/linux/man/2-sigaction/">sigaction</a></i>(2), <i>sigemptyset</i>(2), <i>sigaddset</i>(2), <i><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></i>(2), <i><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></i>(2), <i><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></i>(3), <i><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></i>(3), <i><a href="/docs/linux/man/3-setjmp/">setjmp</a></i>(3), <i><a href="/docs/linux/man/3-longjmp/">longjmp</a></i>(3), <i><a href="/docs/linux/man/2-select/">select</a></i>(2), <i><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></i>(2).  </p>
<h2>AUTHOR</h2>
<pre><code> Ralf S. Engelschall
 rse [at] engelschall.comwww.engelschall.com
</code></pre>
