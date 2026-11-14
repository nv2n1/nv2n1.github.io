---
title: "posixoptions(7)"
name: "posixoptions"
section: "7"
letter: "p"
url: "/docs/linux/man/7-posixoptions/"
description: "posixoptions – optional parts of the POSIX standard"
---

<p>posixoptions &#8211; optional parts of the POSIX standard</p>
<h2>Description</h2>
<p>The POSIX standard (the information below is from POSIX.1-2001) describes a set of behaviors and interfaces for a compliant system. However, many interfaces are optional and there are feature test macros to test the availability of interfaces at compile time, and functions <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/3-fpathconf/">fpathconf</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3) to do this at run time. From shell scripts one can use <code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1). For more detail, see <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3). </p>
<p> We give the name of the POSIX abbreviation, the option, the name of the <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) parameter used to inquire about the option, and possibly a very short description. Much more precise detail can be found in the POSIX standard itself, versions of which can nowadays be accessed freely on the web.</p>
<h3>Adv &#8211; _Posix_Advisory_Info &#8211; _Sc_Advisory_Info</h3>
<p>The following advisory functions are present: </p>
<pre><i>posix_fadvise</i>()
<i>posix_fallocate</i>()
<i>posix_memalign</i>()
<i>posix_madvise</i>()</pre>
<h3>Aio &#8211; _Posix_Asynchronous_Io &#8211; _Sc_Asynchronous_Io</h3>
<p>The header <i>&lt;aio.h&gt;</i> is present. The following functions are present: </p>
<pre><i>aio_cancel</i>()
<i>aio_error</i>()
<i>aio_fsync</i>()
<i>aio_read</i>()
<i>aio_return</i>()
<i>aio_suspend</i>()
<i>aio_write</i>()
<i>lio_listio</i>()</pre>
<h3>Bar &#8211; _Posix_Barriers &#8211; _Sc_Barriers</h3>
<p>This option implies the <code>_POSIX_THREADS</code> and <code>_POSIX_THREAD_SAFE_FUNCTIONS</code> options. The following functions are present: </p>
<pre><i>pthread_barrier_destroy</i>()
<i>pthread_barrier_init</i>()
<i>pthread_barrier_wait</i>()
<i>pthread_barrierattr_destroy</i>()
<i>pthread_barrierattr_init</i>()</pre>
<h3>&#8212; &#8211; Posix_Chown_Restricted</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), then only root may change the owner of a file, and nonroot can set the group of a file only to one of the groups it belongs to. This affects the following functions </p>
<pre><i>chown</i>()
<i>fchown</i>()</pre>
<h3>Cs &#8211; _Posix_Clock_Selection &#8211; _Sc_Clock_Selection</h3>
<p>This option implies the <code>_POSIX_TIMERS</code> option. The following functions are present: </p>
<pre><i>pthread_condattr_getclock</i>()
<i>pthread_condattr_setclock</i>()
<i>clock_nanosleep</i>()</pre>
<p>If <code>CLOCK_REALTIME</code> is changed by the function <i>clock_settime</i>(), then this affects all timers set for an absolute time.</p>
<h3>Cpt &#8211; _Posix_Cputime &#8211; _Sc_Cputime</h3>
<p>The <code>CLOCK_PROCESS_CPUTIME_ID</code> clock ID is supported. The initial value of this clock is 0 for each process. This option implies the <code>_POSIX_TIMERS</code> option. The function <i>clock_getcpuclockid</i>() is present.</p>
<h3>&#8212; &#8211; _Posix_File_Locking &#8211; _Sc_File_Locking</h3>
<p>This option has been deleted. Not in final XPG6.</p>
<h3>Fsc &#8211; _Posix_Fsync &#8211; _Sc_Fsync</h3>
<p>The function <i>fsync</i>() is present.</p>
<h3>Ip6 &#8211; _Posix_Ipv6 &#8211; _Sc_Ipv6</h3>
<p>Internet Protocol Version 6 is supported.</p>
<h3>&#8212; &#8211; _Posix_Job_Control &#8211; _Sc_Job_Control</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), then the system implements POSIX-style job control, and the following functions are present: </p>
<pre><i>setpgid</i>()
<i>tcdrain</i>()
<i>tcflush</i>()
<i>tcgetpgrp</i>()
<i>tcsendbreak</i>()
<i>tcsetattr</i>()
<i>tcsetpgrp</i>()</pre>
<h3>Mf &#8211; _Posix_Mapped_Files &#8211; _Sc_Mapped_Files</h3>
<p>Shared memory is supported. The include file <i>&lt;sys/mman.h&gt;</i> is present. The following functions are present: </p>
<pre><i>mmap</i>()
<i>msync</i>()
<i>munmap</i>()</pre>
<h3>Ml &#8211; _Posix_Memlock &#8211; _Sc_Memlock</h3>
<p>Shared memory can be locked into core. The following functions are present: </p>
<pre><i>mlockall</i>()
<i>munlockall</i>()</pre>
<h3>Mr/Mlr &#8211; _Posix_Memlock_Range &#8211; _Sc_Memlock_Range</h3>
<p>More precisely, ranges can be locked into core. The following functions are present: </p>
<pre><i>mlock</i>()
<i>munlock</i>()</pre>
<h3>Mpr &#8211; _Posix_Memory_Protection &#8211; _Sc_Memory_Protection</h3>
<p>The function <i>mprotect</i>() is present.</p>
<h3>Msg &#8211; _Posix_Message_Passing &#8211; _Sc_Message_Passing</h3>
<p>The include file <i>&lt;mqueue.h&gt;</i> is present. The following functions are present: </p>
<pre><i>mq_close</i>()
<i>mq_getattr</i>()
<i>mq_notify</i>()
<i>mq_open</i>()
<i>mq_receive</i>()
<i>mq_send</i>()
<i>mq_setattr</i>()
<i>mq_unlink</i>()</pre>
<h3>Mon &#8211; _Posix_Monotonic_Clock &#8211; _Sc_Monotonic_Clock</h3>
<p><code>CLOCK_MONOTONIC</code> is supported. This option implies the <code>_POSIX_TIMERS</code> option. The following functions are affected: </p>
<pre><i>aio_suspend</i>()
<i>clock_getres</i>()
<i>clock_gettime</i>()
<i>clock_settime</i>()
<i>timer_create</i>()</pre>
<h3>&#8212; &#8211; _Posix_Multi_Process &#8211; _Sc_Multi_Process</h3>
<p>This option has been deleted. Not in final XPG6.</p>
<h3>&#8212; &#8211; _Posix_No_Trunc</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), then pathname components longer than <code>NAME_MAX</code> are not truncated, but give an error. This property may be dependent on the path prefix of the component.</p>
<h3>Pio &#8211; _Posix_Prioritized_Io &#8211; _Sc_Prioritized_Io</h3>
<p>This option says that one can specify priorities for asynchronous I/O. This affects the functions </p>
<pre><i>aio_read</i>()
<i>aio_write</i>()</pre>
<h3>Ps &#8211; _Posix_Priority_Scheduling &#8211; _Sc_Priority_Scheduling</h3>
<p>The include file <i>&lt;sched.h&gt;</i> is present. The following functions are present: </p>
<pre><i>sched_get_priority_max</i>()
<i>sched_get_priority_min</i>()
<i>sched_getparam</i>()
<i>sched_getscheduler</i>()
<i>sched_rr_get_interval</i>()
<i>sched_setparam</i>()
<i>sched_setscheduler</i>()
<i>sched_yield</i>()</pre>
<p>If also <code>_POSIX_SPAWN</code> is in effect, then the following functions are present: </p>
<pre><i>posix_spawnattr_getschedparam</i>()
<i>posix_spawnattr_getschedpolicy</i>()
<i>posix_spawnattr_setschedparam</i>()
<i>posix_spawnattr_setschedpolicy</i>()</pre>
<h3>Rs &#8211; _Posix_Raw_Sockets</h3>
<p>Raw sockets are supported. The following functions are affected: </p>
<pre><i>getsockopt</i>()
<i>setsockopt</i>()</pre>
<h3>&#8212; &#8211; _Posix_Reader_Writer_Locks &#8211; _Sc_Reader_Writer_Locks</h3>
<p>This option implies the <code>_POSIX_THREADS</code> option. Conversely, under POSIX.1-2001 the <code>_POSIX_THREADS</code> option implies this option. </p>
<p> The following functions are present: </p>
<pre><i>pthread_rwlock_destroy</i>()
<i>pthread_rwlock_init</i>()
<i>pthread_rwlock_rdlock</i>()
<i>pthread_rwlock_tryrdlock</i>()
<i>pthread_rwlock_trywrlock</i>()
<i>pthread_rwlock_unlock</i>()
<i>pthread_rwlock_wrlock</i>()
<i>pthread_rwlockattr_destroy</i>()
<i>pthread_rwlockattr_init</i>()</pre>
<h3>Rts &#8211; _Posix_Realtime_Signals &#8211; _Sc_Realtime_Signals</h3>
<p>Realtime signals are supported. The following functions are present: </p>
<pre><i>sigqueue</i>()
<i>sigtimedwait</i>()
<i>sigwaitinfo</i>()</pre>
<h3>&#8212; &#8211; _Posix_Regexp &#8211; _Sc_Regexp</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), then POSIX regular expressions are supported and the following functions are present: </p>
<pre><i>regcomp</i>()
<i>regerror</i>()
<i>regexec</i>()
<i>regfree</i>()</pre>
<h3>&#8212; &#8211; _Posix_Saved_Ids &#8211; _Sc_Saved_Ids</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), then a process has a saved set-user-ID and a saved set-group-ID. The following functions are affected: </p>
<pre><i>exec</i>()
<i>kill</i>()
<i>seteuid</i>()
<i>setegid</i>()
<i>setgid</i>()
<i>setuid</i>()</pre>
<h3>Sem &#8211; _Posix_Semaphores &#8211; _Sc_Semaphores</h3>
<p>The include file <i>&lt;semaphore.h&gt;</i> is present. The following functions are present: </p>
<pre><i>sem_close</i>()
<i>sem_destroy</i>()
<i>sem_getvalue</i>()
<i>sem_init</i>()
<i>sem_open</i>()
<i>sem_post</i>()
<i>sem_trywait</i>()
<i>sem_unlink</i>()
<i>sem_wait</i>()</pre>
<h3>Shm &#8211; _Posix_Shared_Memory_Objects &#8211; _Sc_Shared_Memory_Objects</h3>
<p>The following functions are present: </p>
<pre><i>mmap</i>()
<i>munmap</i>()
<i>shm_open</i>()
<i>shm_unlink</i>()</pre>
<h3>&#8212; &#8211; _Posix_Shell &#8211; _Sc_Shell</h3>
<p>If this option is in effect (as it always is under POSIX.1-2001), the function <i>system</i>() is present.</p>
<h3>Spn &#8211; _Posix_Spawn &#8211; _Sc_Spawn</h3>
<p>This option describes support for process creation in a context where it is difficult or impossible to use <i>fork</i>(), for example, because no MMU is present. </p>
<p> If <code>_POSIX_SPAWN</code> is in effect, then the include file <i>&lt;spawn.h&gt;</i> and the following functions are present: </p>
<pre><i>posix_spawn</i>()
<i>posix_spawn_file_actions_addclose</i>()
<i>posix_spawn_file_actions_adddup2</i>()
<i>posix_spawn_file_actions_addopen</i>()
<i>posix_spawn_file_actions_destroy</i>()
<i>posix_spawn_file_actions_init</i>()
<i>posix_spawnattr_destroy</i>()
<i>posix_spawnattr_getsigdefault</i>()
<i>posix_spawnattr_getflags</i>()
<i>posix_spawnattr_getpgroup</i>()
<i>posix_spawnattr_getsigmask</i>()
<i>posix_spawnattr_init</i>()
<i>posix_spawnattr_setsigdefault</i>()
<i>posix_spawnattr_setflags</i>()
<i>posix_spawnattr_setpgroup</i>()
<i>posix_spawnattr_setsigmask</i>()
<i>posix_spawnp</i>()</pre>
<p>If also <code>_POSIX_PRIORITY_SCHEDULING</code> is in effect, then the following functions are present: </p>
<pre><i>posix_spawnattr_getschedparam</i>()
<i>posix_spawnattr_getschedpolicy</i>()
<i>posix_spawnattr_setschedparam</i>()
<i>posix_spawnattr_setschedpolicy</i>()</pre>
<h3>Spi &#8211; _Posix_Spin_Locks &#8211; _Sc_Spin_Locks</h3>
<p>This option implies the <code>_POSIX_THREADS</code> and <code>_POSIX_THREAD_SAFE_FUNCTIONS</code> options. The following functions are present: </p>
<pre><i>pthread_spin_destroy</i>()
<i>pthread_spin_init</i>()
<i>pthread_spin_lock</i>()
<i>pthread_spin_trylock</i>()
<i>pthread_spin_unlock</i>()</pre>
<h3>Ss &#8211; _Posix_Sporadic_Server &#8211; _Sc_Sporadic_Server</h3>
<p>The scheduling policy <code>SCHED_SPORADIC</code> is supported. This option implies the <code>_POSIX_PRIORITY_SCHEDULING</code> option. The following functions are affected: </p>
<pre><i>sched_setparam</i>()
<i>sched_setscheduler</i>()</pre>
<h3>Sio &#8211; _Posix_Synchronized_Io &#8211; _Sc_Synchronized_Io</h3>
<p>The following functions are affected: </p>
<pre><i>open</i>()
<i>msync</i>()
<i>fsync</i>()
<i>fdatasync</i>()</pre>
<h3>Tsa &#8211; _Posix_Thread_Attr_Stackaddr &#8211; _Sc_Thread_Attr_Stackaddr</h3>
<p>The following functions are affected: </p>
<pre><i>pthread_attr_getstack</i>()
<i>pthread_attr_getstackaddr</i>()
<i>pthread_attr_setstack</i>()
<i>pthread_attr_setstackaddr</i>()</pre>
<h3>Tss &#8211; _Posix_Thread_Attr_Stacksize &#8211; _Sc_Thread_Attr_Stacksize</h3>
<p>The following functions are affected: </p>
<pre><i>pthread_attr_getstack</i>()
<i>pthread_attr_getstacksize</i>()
<i>pthread_attr_setstack</i>()
<i>pthread_attr_setstacksize</i>()</pre>
<h3>Tct &#8211; _Posix_Thread_Cputime &#8211; _Sc_Thread_Cputime</h3>
<p>The clockID CLOCK_THREAD_CPUTIME_ID is supported. This option implies the <code>_POSIX_TIMERS</code> option. The following functions are affected: </p>
<pre><i>pthread_getcpuclockid</i>()
<i>clock_getres</i>()
<i>clock_gettime</i>()
<i>clock_settime</i>()
<i>timer_create</i>()</pre>
<h3>Tpi &#8211; _Posix_Thread_Prio_Inherit &#8211; _Sc_Thread_Prio_Inherit</h3>
<p>The following functions are affected: </p>
<pre><i>pthread_mutexattr_getprotocol</i>()
<i>pthread_mutexattr_setprotocol</i>()</pre>
<h3>Tpp &#8211; _Posix_Thread_Prio_Protect &#8211; _Sc_Thread_Prio_Protect</h3>
<p>The following functions are affected: </p>
<pre><i>pthread_mutex_getprioceiling</i>()
<i>pthread_mutex_setprioceiling</i>()
<i>pthread_mutexattr_getprioceiling</i>()
<i>pthread_mutexattr_getprotocol</i>()
<i>pthread_mutexattr_setprioceiling</i>()
<i>pthread_mutexattr_setprotocol</i>()</pre>
<h3>Tps &#8211; _Posix_Thread_Priority_Scheduling &#8211; _Sc_Thread_Priority_Scheduling</h3>
<p>If this option is in effect, the different threads inside a process can run with different priorities and/or different schedulers. The following functions are affected: </p>
<pre><i>pthread_attr_getinheritsched</i>()
<i>pthread_attr_getschedpolicy</i>()
<i>pthread_attr_getscope</i>()
<i>pthread_attr_setinheritsched</i>()
<i>pthread_attr_setschedpolicy</i>()
<i>pthread_attr_setscope</i>()
<i>pthread_getschedparam</i>()
<i>pthread_setschedparam</i>()
<i>pthread_setschedprio</i>()</pre>
<h3>Tsh &#8211; _Posix_Thread_Process_Shared &#8211; _Sc_Thread_Process_Shared</h3>
<p>The following functions are affected: </p>
<pre><i>pthread_barrierattr_getpshared</i>()
<i>pthread_barrierattr_setpshared</i>()
<i>pthread_condattr_getpshared</i>()
<i>pthread_condattr_setpshared</i>()
<i>pthread_mutexattr_getpshared</i>()
<i>pthread_mutexattr_setpshared</i>()
<i>pthread_rwlockattr_getpshared</i>()
<i>pthread_rwlockattr_setpshared</i>()</pre>
<h3>Tsf &#8211; _Posix_Thread_Safe_Functions &#8211; _Sc_Thread_Safe_Functions</h3>
<p>The following functions are affected: </p>
<pre><i>readdir_r</i>()
<i>getgrgid_r</i>()
<i>getgrnam_r</i>()
<i>getpwnam_r</i>()
<i>getpwuid_r</i>()
<i>flockfile</i>()
<i>ftrylockfile</i>()
<i>funlockfile</i>()
<i>getc_unlocked</i>()
<i>getchar_unlocked</i>()
<i>putc_unlocked</i>()
<i>putchar_unlocked</i>()
<i>rand_r</i>()
<i>strerror_r</i>()
<i>strtok_r</i>()
<i>asctime_r</i>()
<i>ctime_r</i>()
<i>gmtime_r</i>()
<i>localtime_r</i>()</pre>
<h3>Tsp &#8211; _Posix_Thread_Sporadic_Server &#8211; _Sc_Thread_Sporadic_Server</h3>
<p>This option implies the <code>_POSIX_THREAD_PRIORITY_SCHEDULING</code> option. The following functions are affected: </p>
<pre><i>sched_getparam</i>()
<i>sched_setparam</i>()
<i>sched_setscheduler</i>()</pre>
<h3>Thr &#8211; _Posix_Threads &#8211; _Sc_Threads</h3>
<p>Basic support for POSIX threads is available. The following functions are present: </p>
<pre><i>pthread_atfork</i>()
<i>pthread_attr_destroy</i>()
<i>pthread_attr_getdetachstate</i>()
<i>pthread_attr_getschedparam</i>()
<i>pthread_attr_init</i>()
<i>pthread_attr_setdetachstate</i>()
<i>pthread_attr_setschedparam</i>()
<i>pthread_cancel</i>()
<i>pthread_cleanup_push</i>()
<i>pthread_cleanup_pop</i>()
<i>pthread_cond_broadcast</i>()
<i>pthread_cond_destroy</i>()
<i>pthread_cond_init</i>()
<i>pthread_cond_signal</i>()
<i>pthread_cond_timedwait</i>()
<i>pthread_cond_wait</i>()
<i>pthread_condattr_destroy</i>()
<i>pthread_condattr_init</i>()
<i>pthread_create</i>()
<i>pthread_detach</i>()
<i>pthread_equal</i>()
<i>pthread_exit</i>()
<i>pthread_getspecific</i>()
<i>pthread_join</i>()
<i>pthread_key_create</i>()
<i>pthread_key_delete</i>()
<i>pthread_mutex_destroy</i>()
<i>pthread_mutex_init</i>()
<i>pthread_mutex_lock</i>()
<i>pthread_mutex_trylock</i>()
<i>pthread_mutex_unlock</i>()
<i>pthread_mutexattr_destroy</i>()
<i>pthread_mutexattr_init</i>()
<i>pthread_once</i>()
<i>pthread_rwlock_destroy</i>()
<i>pthread_rwlock_init</i>()
<i>pthread_rwlock_rdlock</i>()
<i>pthread_rwlock_tryrdlock</i>()
<i>pthread_rwlock_trywrlock</i>()
<i>pthread_rwlock_unlock</i>()
<i>pthread_rwlock_wrlock</i>()
<i>pthread_rwlockattr_destroy</i>()
<i>pthread_rwlockattr_init</i>()
<i>pthread_self</i>()
<i>pthread_setcancelstate</i>()
<i>pthread_setcanceltype</i>()
<i>pthread_setspecific</i>()
<i>pthread_testcancel</i>()</pre>
<h3>Tmo &#8211; _Posix_Timeouts &#8211; _Sc_Timeouts</h3>
<p>The following functions are present: </p>
<pre><i>mq_timedreceive</i>()
<i>mq_timedsend</i>()
<i>pthread_mutex_timedlock</i>()
<i>pthread_rwlock_timedrdlock</i>()
<i>pthread_rwlock_timedwrlock</i>()
<i>sem_timedwait</i>()
<i>posix_trace_timedgetnext_event</i>()</pre>
<h3>Tmr &#8211; _Posix_Timers &#8211; _Sc_Timers</h3>
<p>The following functions are present: </p>
<pre><i>clock_getres</i>()
<i>clock_gettime</i>()
<i>clock_settime</i>()
<i>nanosleep</i>()
<i>timer_create</i>()
<i>timer_delete</i>()
<i>timer_gettime</i>()
<i>timer_getoverrun</i>()
<i>timer_settime</i>()</pre>
<h3>Trc &#8211; _Posix_Trace &#8211; _Sc_Trace</h3>
<p>POSIX tracing is available. The following functions are present: </p>
<pre><i>posix_trace_attr_destroy</i>()
<i>posix_trace_attr_getclockres</i>()
<i>posix_trace_attr_getcreatetime</i>()
<i>posix_trace_attr_getgenversion</i>()
<i>posix_trace_attr_getmaxdatasize</i>()
<i>posix_trace_attr_getmaxsystemeventsize</i>()
<i>posix_trace_attr_getmaxusereventsize</i>()
<i>posix_trace_attr_getname</i>()
<i>posix_trace_attr_getstreamfullpolicy</i>()
<i>posix_trace_attr_getstreamsize</i>()
<i>posix_trace_attr_init</i>()
<i>posix_trace_attr_setmaxdatasize</i>()
<i>posix_trace_attr_setname</i>()
<i>posix_trace_attr_setstreamsize</i>()
<i>posix_trace_attr_setstreamfullpolicy</i>()
<i>posix_trace_clear</i>()
<i>posix_trace_create</i>()
<i>posix_trace_event</i>()
<i>posix_trace_eventid_equal</i>()
<i>posix_trace_eventid_get_name</i>()
<i>posix_trace_eventid_open</i>()
<i>posix_trace_eventtypelist_getnext_id</i>()
<i>posix_trace_eventtypelist_rewind</i>()
<i>posix_trace_flush</i>()
<i>posix_trace_get_attr</i>()
<i>posix_trace_get_status</i>()
<i>posix_trace_getnext_event</i>()
<i>posix_trace_shutdown</i>()
<i>posix_trace_start</i>()
<i>posix_trace_stop</i>()
<i>posix_trace_trygetnext_event</i>()</pre>
<h3>Tef &#8211; _Posix_Trace_Event_Filter &#8211; _Sc_Trace_Event_Filter</h3>
<p>This option implies the <code>_POSIX_TRACE</code> option. The following functions are present: </p>
<pre><i>posix_trace_eventset_add</i>()
<i>posix_trace_eventset_del</i>()
<i>posix_trace_eventset_empty</i>()
<i>posix_trace_eventset_fill</i>()
<i>posix_trace_eventset_ismember</i>()
<i>posix_trace_get_filter</i>()
<i>posix_trace_set_filter</i>()
<i>posix_trace_trid_eventid_open</i>()</pre>
<h3>Tri &#8211; _Posix_Trace_Inherit &#8211; _Sc_Trace_Inherit</h3>
<p>Tracing children of the traced process is supported. This option implies the <code>_POSIX_TRACE</code> option. The following functions are present: </p>
<pre><i>posix_trace_attr_getinherited</i>()
<i>posix_trace_attr_setinherited</i>()</pre>
<h3>Trl &#8211; _Posix_Trace_Log &#8211; _Sc_Trace_Log</h3>
<p>This option implies the <code>_POSIX_TRACE</code> option. The following functions are present: </p>
<pre><i>posix_trace_attr_getlogfullpolicy</i>()
<i>posix_trace_attr_getlogsize</i>()
<i>posix_trace_attr_setlogfullpolicy</i>()
<i>posix_trace_attr_setlogsize</i>()
<i>posix_trace_close</i>()
<i>posix_trace_create_withlog</i>()
<i>posix_trace_open</i>()
<i>posix_trace_rewind</i>()</pre>
<h3>Tym &#8211; _Posix_Typed_Memory_Objects &#8211; _Sc_Typed_Memory_Object</h3>
<p>The following functions are present: </p>
<pre><i>posix_mem_offset</i>()
<i>posix_typed_mem_get_info</i>()
<i>posix_typed_mem_open</i>()</pre>
<h3>&#8212; &#8211; _Posix_Vdisable</h3>
<p>Always present (probably 0). Value to set a changeable special control character to indicate that it is disabled.</p>
<h2>X/Open System Interface Extensions</h2>
<h3>Xsi &#8211; _Xopen_Crypt &#8211; _Sc_Xopen_Crypt</h3>
<p>The following functions are present: </p>
<pre><i>crypt</i>()
<i>encrypt</i>()
<i>setkey</i>()</pre>
<h3>Xsi &#8211; _Xopen_Realtime &#8211; _Sc_Xopen_Realtime</h3>
<p>This option implies the following options: </p>
<dl>
<dt><code>_POSIX_ASYNCHRONOUS_IO</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_FSYNC</code></p>
<dd>
<dt><code>_POSIX_MAPPED_FILES</code></p>
<dd>
<dt><code>_POSIX_MEMLOCK</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_MEMLOCK_RANGE</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_MEMORY_PROTECTION</code></p>
<dd>
<dt><code>_POSIX_MESSAGE_PASSING</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_PRIORITIZED_IO</code></p>
<dd>
<dt><code>_POSIX_PRIORITY_SCHEDULING</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_REALTIME_SIGNALS</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_SEMAPHORES</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_SHARED_MEMORY_OBJECTS</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_SYNCHRONIZED_IO</code>==<code>200112L</code></p>
<dd>
<dt><code>_POSIX_TIMERS</code>==<code>200112L</code></p>
<dd></dl>
<h3>Adv &#8211; &#8212; &#8211; &#8212;</h3>
<p>The Advanced Realtime option group implies that the following options are all defined to 200112L: </p>
<dl>
<dt><code>_POSIX_ADVISORY_INFO</code></p>
<dd>
<dt><code>_POSIX_CLOCK_SELECTION</code></p>
<dd>(implies <code>_POSIX_TIMERS</code>)</p>
<dt><code>_POSIX_CPUTIME</code></p>
<dd>(implies <code>_POSIX_TIMERS</code>)</p>
<dt><code>_POSIX_MONOTONIC_CLOCK</code></p>
<dd>(implies <code>_POSIX_TIMERS</code>)</p>
<dt><code>_POSIX_SPAWN</code></p>
<dd>
<dt><code>_POSIX_SPORADIC_SERVER</code></p>
<dd>(implies <code>_POSIX_PRIORITY_SCHEDULING</code>)</p>
<dt><code>_POSIX_TIMEOUTS</code></p>
<dd>
<dt><code>_POSIX_TYPED_MEMORY_OBJECTS</code></p>
<dd></dl>
<h3>Xsi &#8211; _Xopen_Realtime_Threads &#8211; _Sc_Xopen_Realtime_Threads</h3>
<p>This option implies that the following options are all defined to 200112L: </p>
<dl>
<dt><code>_POSIX_THREAD_PRIO_INHERIT</code></p>
<dd>
<dt><code>_POSIX_THREAD_PRIO_PROTECT</code></p>
<dd>
<dt><code>_POSIX_THREAD_PRIORITY_SCHEDULING</code></p>
<dd></dl>
<h3>Advanced Realtime Threads &#8211; &#8212; &#8211; &#8212;</h3>
<p>This option implies that the following options are all defined to 200112L: </p>
<dl>
<dt><code>_POSIX_BARRIERS</code></p>
<dd>(implies <code>_POSIX_THREADS</code>, <code>_POSIX_THREAD_SAFE_FUNCTIONS</code>)</p>
<dt><code>_POSIX_SPIN_LOCKS</code></p>
<dd>(implies <code>_POSIX_THREADS</code>, <code>_POSIX_THREAD_SAFE_FUNCTIONS</code>)</p>
<dt><code>_POSIX_THREAD_CPUTIME</code></p>
<dd>(implies <code>_POSIX_TIMERS</code>)</p>
<dt><code>_POSIX_THREAD_SPORADIC_SERVER</code></p>
<dd>(implies <code>_POSIX_THREAD_PRIORITY_SCHEDULING</code>)</dl>
<h3>Tracing &#8211; &#8212; &#8211; &#8212;</h3>
<p>This option implies that the following options are all defined to 200112L: </p>
<dl>
<dt><code>_POSIX_TRACE</code></p>
<dd>
<dt><code>_POSIX_TRACE_EVENT_FILTER</code></p>
<dd>
<dt><code>_POSIX_TRACE_LOG</code></p>
<dd>
<dt><code>_POSIX_TRACE_INHERIT</code></p>
<dd></dl>
<h3>Streams &#8211; _Xopen_Streams &#8211; _Sc_Xopen_Streams</h3>
<p>The following functions are present: </p>
<pre><i>fattach</i>()
<i>fdetach</i>()
<i>getmsg</i>()
<i>getpmsg</i>()
<i>ioctl</i>()
<i>isastream</i>()
<i>putmsg</i>()
<i>putpmsg</i>()</pre>
<h3>Xsi &#8211; _Xopen_Legacy &#8211; _Sc_Xopen_Legacy</h3>
<p>Functions included in the legacy option group were previously mandatory, but are now optional in this version. The following functions are present: </p>
<pre><i>bcmp</i>()
<i>bcopy</i>()
<i>bzero</i>()
<i>ecvt</i>()
<i>fcvt</i>()
<i>ftime</i>()
<i>gcvt</i>()
<i>getcwd</i>()
<i>index</i>()
<i>mktemp</i>()
<i>rindex</i>()
<i>utimes</i>()
<i>wcswcs</i>()</pre>
<h3>Xsi &#8211; _Xopen_Unix &#8211; _Sc_Xopen_Unix</h3>
<p>The following functions are present: </p>
<pre><i>mmap</i>()
<i>munmap</i>()
<i>msync</i>()</pre>
<p>This option implies the following options: </p>
<dl>
<dt><code>_POSIX_FSYNC</code></p>
<dd>
<dt><code>_POSIX_MAPPED_FILES</code></p>
<dd>
<dt><code>_POSIX_MEMORY_PROTECTION</code></p>
<dd>
<dt><code>_POSIX_THREAD_ATTR_STACKADDR</code></p>
<dd>
<dt><code>_POSIX_THREAD_ATTR_STACKSIZE</code></p>
<dd>
<dt><code>_POSIX_THREAD_PROCESS_SHARED</code></p>
<dd>
<dt><code>_POSIX_THREAD_SAFE_FUNCTIONS</code></p>
<dd>
<dt><code>_POSIX_THREADS</code></p>
<dd></dl>
<p> This option may imply the following options from the XSI option groups: </p>
<dl>
<dt>Encryption (<code>_XOPEN_CRYPT</code>)</p>
<dd>
<dt>Realtime (<code>_XOPEN_REALTIME</code>)</p>
<dd>
<dt>Advanced Realtime (<code>ADB</code>)</p>
<dd>
<dt>Realtime Threads (<code>_XOPEN_REALTIME_THREADS</code>)</p>
<dd>
<dt>Advanced Realtime Threads (<code>ADVANCED REALTIME THREADS</code>)</p>
<dd>
<dt>Tracing (<code>TRACING</code>)</p>
<dd>
<dt>XSI Streams (<code>STREAMS</code>)</p>
<dd>
<dt>Legacy (<code>_XOPEN_LEGACY</code>)</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
