---
title: "pthread_getcpuclockid(3)"
name: "pthread_getcpuclockid"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_getcpuclockid/"
description: "pthread_getcpuclockid – retrieve ID of a thread’s CPU time clock"
---

<p>pthread_getcpuclockid &#8211; retrieve ID of a thread&#8217;s CPU time clock</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;
#include &lt;time.h&gt;

int pthread_getcpuclockid(pthread_t thread, clockid_t *clockid);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_getcpuclockid</code>() function obtains the ID of the CPU-time clock of the thread whose ID is given in <i>thread</i>, and returns it in the location pointed to by <i>clockid</i>.</p>
<h2>Return Value</h2>
<p>On success, this function returns 0; on error, it returns a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd>Per-thread CPU time clocks are not supported by the system.</p>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
<h2>Versions</h2>
<p>This function is available in glibc since version 2.2.</p>
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
<td> <code>pthread_getcpuclockid</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>When <i>thread</i> refers to the calling thread, this function returns an identifier that refers to the same clock manipulated by <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) and <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2) when given the clock ID <code>CLOCK_THREAD_CPUTIME_ID</code>.</p>
<h2>Examples</h2>
<p>The program below creates a thread and then uses <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) to retrieve the total process CPU time, and the per-thread CPU time consumed by the two threads. The following shell session shows an example run: $ <code>./a.out</code> Main thread sleeping Subthread starting infinite loop Main thread consuming some CPU time&#8230; Process total CPU time: 1.368 Main thread CPU time: 0.376 Subthread CPU time: 0.992</p>
<h3>Program source</h3>
<p>/* Link with &quot;-lrt&quot; */ </p>
<pre><code>#include &lt;errno.h&gt;
#include &lt;pthread.h&gt;
#include &lt;stdint.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;time.h&gt;
#include &lt;unistd.h&gt;
#define handle_error(msg)   \
    do {                    \
        perror(msg);        \
        exit(EXIT_FAILURE); \
    } while (0)
#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)
static void *
thread_start(void *arg)
{
    printf(&quot;Subthread starting infinite loop
&quot;);
    for (;;)
        continue;
}
static void
pclock(char *msg, clockid_t cid)
{
    struct timespec ts;
    printf(&quot;%s&quot;, msg);
    if (clock_gettime(cid, &amp;ts) == -1)
        handle_error(&quot;clock_gettime&quot;);
    printf(&quot;%4jd.%03ld
&quot;, (intmax_t)ts.tv_sec, ts.tv_nsec / 1000000);
}
int main(int argc, char *argv[])
{
    pthread_t thread;
    clockid_t cid;
    int s;
    s = pthread_create(&amp;thread, NULL, thread_start, NULL);
    if (s != 0)
        handle_error_en(s, &quot;pthread_create&quot;);
    printf(&quot;Main thread sleeping
&quot;);
    sleep(1);
    printf(&quot;Main thread consuming some CPU time...
&quot;);
    for (int j = 0; j &lt; 2000000; j++)
        getppid();
    pclock(&quot;Process total CPU time: &quot;, CLOCK_PROCESS_CPUTIME_ID);
    s = pthread_getcpuclockid(pthread_self(), &amp;cid);
    if (s != 0)
        handle_error_en(s, &quot;pthread_getcpuclockid&quot;);
    pclock(&quot;Main thread CPU time:   &quot;, cid);
    /* The preceding 4 lines of code could have been replaced by:
           pclock(&quot;Main thread CPU time:   &quot;, CLOCK_THREAD_CPUTIME_ID); */
    s = pthread_getcpuclockid(thread, &amp;cid);
    if (s != 0)
        handle_error_en(s, &quot;pthread_getcpuclockid&quot;);
    pclock(&quot;Subthread CPU time: 1    &quot;, cid);
    exit(EXIT_SUCCESS); /* Terminates both threads */
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-clock_getcpuclockid/">clock_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
