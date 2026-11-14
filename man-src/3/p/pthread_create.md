---
title: "pthread_create(3)"
name: "pthread_create"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_create/"
description: "pthread_create – create a new thread"
---

<p>pthread_create &#8211; create a new thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine)(void *), void *arg);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>The <code>pthread_create</code>() function starts a new thread in the calling process. The new thread starts execution by invoking <i>start_routine</i>(); <i>arg</i> is passed as the sole argument of <i>start_routine</i>(). </p>
<p> The new thread terminates in one of the following ways:</p>
<dl>
<dt>*</p>
<dd>It calls <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), specifying an exit status value that is available to another thread in the same process that calls <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3).</p>
<dt>*</p>
<dd>It returns from <i>start_routine</i>(). This is equivalent to calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3) with the value supplied in the <i>return</i> statement.</p>
<dt>*</p>
<dd>It is canceled (see <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3)).</p>
<dt>*</p>
<dd>Any of the threads in the process calls <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), or the main thread performs a return from <i>main</i>(). This causes the termination of all threads in the process.</dl>
<p> The <i>attr</i> argument points to a <i>pthread_attr_t</i> structure whose contents are used at thread creation time to determine attributes for the new thread; this structure is initialized using <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3) and related functions. If <i>attr</i> is NULL, then the thread is created with default attributes. </p>
<p> Before returning, a successful call to <code>pthread_create</code>() stores the ID of the new thread in the buffer pointed to by <i>thread</i>; this identifier is used to refer to the thread in subsequent calls to other pthreads functions. </p>
<p> The new thread inherits a copy of the creating thread&#8217;s signal mask (<code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3)). The set of pending signals for the new thread is empty (<code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2)). The new thread does not inherit the creating thread&#8217;s alternate signal stack (<code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)). </p>
<p> The new thread inherits the calling thread&#8217;s floating-point environment (<code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)). </p>
<p> The initial value of the new thread&#8217;s CPU-time clock is 0 (see <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3)).</p>
<h3>Linux-specific details</h3>
<p>The new thread inherits copies of the calling thread&#8217;s capability sets (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)) and CPU affinity mask (see <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)).</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_create</code>() returns 0; on error, it returns an error number, and the contents of <i>*thread</i> are undefined.</p>
<h2>Errors</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd>Insufficient resources to create another thread.</p>
<dt><code>EAGAIN</code></p>
<dd>A system-imposed limit on the number of threads was encountered. There are a number of limits that may trigger this error: the <code>RLIMIT_NPROC</code> soft resource limit (set via <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)), which limits the number of processes and threads for a real user ID, was reached; the kernel&#8217;s system-wide limit on the number of processes and threads, <i>/proc/sys/kernel/threads-max</i>, was reached (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)); or the maximum number of PIDs, <i>/proc/sys/kernel/pid_max</i>, was reached (see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)).</p>
<dt><code>EINVAL</code></p>
<dd>Invalid settings in <i>attr</i>.</p>
<dd><code>EPERM</code> No permission to set the scheduling policy and parameters specified in <i>attr</i>.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_create</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3) for further information on the thread ID returned in <i>*thread</i> by <code>pthread_create</code>(). Unless real-time scheduling policies are being employed, after a call to <code>pthread_create</code>(), it is indeterminate which thread&#8212;the caller or the new thread&#8212;will next execute. </p>
<p> A thread may either be <i>joinable</i> or <i>detached</i>. If a thread is joinable, then another thread can call <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3) to wait for the thread to terminate and fetch its exit status. Only when a terminated joinable thread has been joined are the last of its resources released back to the system. When a detached thread terminates, its resources are automatically released back to the system: it is not possible to join with the thread in order to obtain its exit status. Making a thread detached is useful for some types of daemon threads whose exit status the application does not need to care about. By default, a new thread is created in a joinable state, unless <i>attr</i> was set to create the thread in a detached state (using <code><a href="/docs/linux/man/3-pthread_attr_setdetachstate/">pthread_attr_setdetachstate</a></code>(3)). </p>
<p> Under the NPTL threading implementation, if the <code>RLIMIT_STACK</code> soft resource limit <i>at the time the program started</i> has any value other than &quot;unlimited&quot;, then it determines the default stack size of new threads. Using <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3), the stack size attribute can be explicitly set in the <i>attr</i> argument used to create a thread, in order to obtain a stack size other than the default. If the <code>RLIMIT_STACK</code> resource limit is set to &quot;unlimited&quot;, a per-architecture value is used for the stack size. Here is the value for a few architectures:</p>
<dl>
<dd>
<table BORDER>
<tr VALIGN=top>
<td><code>Architecture</code></td>
<td><code>Default stack size</code>
</td>
</tr>
<tr VALIGN=top>
<td>i386</td>
<td ALIGN=right>2 MB
</td>
</tr>
<tr VALIGN=top>
<td>IA-64</td>
<td ALIGN=right>32 MB
</td>
</tr>
<tr VALIGN=top>
<td>PowerPC</td>
<td ALIGN=right>4 MB
</td>
</tr>
<tr VALIGN=top>
<td>S/390</td>
<td ALIGN=right>2 MB
</td>
</tr>
<tr VALIGN=top>
<td>Sparc-32</td>
<td ALIGN=right>2 MB
</td>
</tr>
<tr VALIGN=top>
<td>Sparc-64</td>
<td ALIGN=right>4 MB
</td>
</tr>
<tr VALIGN=top>
<td>x86_64</td>
<td ALIGN=right>2 MB
</td>
</tr>
</table>
</dl>
<h2>Bugs</h2>
<p>In the obsolete LinuxThreads implementation, each of the threads in a process has a different process ID. This is in violation of the POSIX threads specification, and is the source of many other nonconformances to the standard; see <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7).</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of <code>pthread_create</code>(), as well as a number of other functions in the pthreads API. In the following run, on a system providing the NPTL threading implementation, the stack size defaults to the value given by the &quot;stack size&quot; resource limit: $<code> ulimit -s</code> 8192 # The stack size limit is 8 MB (0x800000 bytes) $<code> ./a.out hola salut servus</code> Thread 1: top of stack near 0xb7dd03b8; argv_string=hola Thread 2: top of stack near 0xb75cf3b8; argv_string=salut Thread 3: top of stack near 0xb6dce3b8; argv_string=servus Joined with thread 1; returned value was HOLA Joined with thread 2; returned value was SALUT Joined with thread 3; returned value was SERVUS In the next run, the program explicitly sets a stack size of 1 MB (using <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3)) for the created threads: $ ./a.out -s 0x100000 hola salut servus</p>
<p>Thread 1: top of stack near 0xb7d723b8; argv_string=hola<br />
Thread 2: top of stack near 0xb7c713b8; argv_string=salut<br />
Thread 3: top of stack near 0xb7b703b8; argv_string=servus<br />
Joined with thread 1; returned value was HOLA<br />
Joined with thread 2; returned value was SALUT<br />
Joined with thread 3; returned value was SERVUS</p>
<p>Program source</p>
<p>#include &lt;pthread.h&gt;<br />
#include &lt;string.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;unistd.h&gt;<br />
#include &lt;errno.h&gt;<br />
#include &lt;ctype.h&gt;<br />
#define handle_error_en(en, msg) \<br />
do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)<br />
#define handle_error(msg) \<br />
do { perror(msg); exit(EXIT_FAILURE); } while (0)<br />
struct thread_info {    /* Used as argument to thread_start() */<br />
    pthread_t thread_id;        /* ID returned by pthread_create() */<br />
    int       thread_num;       /* Application-defined thread # */<br />
    char     *argv_string;      /* From command-line argument */<br />
}; /* Thread start function: display address near top of our stack,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;and return upper-cased copy of argv_string&nbsp;*/ </p>
<pre><code>static void *
thread_start(void *arg)
{
    struct thread_info *tinfo = arg;
    char *uargv;
    printf(&quot;Thread %d: top of stack near %p; argv_string=%s
&quot;,
           tinfo-&gt;thread_num, &amp;p, tinfo-&gt;argv_string);
    uargv = strdup(tinfo-&gt;argv_string);
    if (uargv == NULL)
        handle_error(&quot;strdup&quot;);
    for (char *p = uargv; *p != '
