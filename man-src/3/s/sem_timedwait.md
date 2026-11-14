---
title: "sem_timedwait(3)"
name: "sem_timedwait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sem_timedwait/"
description: "sem_wait, sem_timedwait, sem_trywait – lock a semaphore"
---

<p>sem_wait, sem_timedwait, sem_trywait &#8211; lock a semaphore</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;semaphore.h&gt;

int sem_wait(sem_t *sem);

int sem_trywait(sem_t *sem);

int sem_timedwait(sem_t *sem, const struct timespec *abs_timeout);</code></pre>
<p> Link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sem_timedwait</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</p>
<h2>Description</h2>
<p><code>sem_wait</code>() decrements (locks) the semaphore pointed to by <i>sem</i>. If the semaphore&#8217;s value is greater than zero, then the decrement proceeds, and the function returns, immediately. If the semaphore currently has the value zero, then the call blocks until either it becomes possible to perform the decrement (i.e., the semaphore value rises above zero), or a signal handler interrupts the call. <code>sem_trywait</code>() is the same as <code>sem_wait</code>(), except that if the decrement cannot be immediately performed, then call returns an error (<i>errno</i> set to <code>EAGAIN</code>) instead of blocking. <code>sem_timedwait</code>() is the same as <code>sem_wait</code>(), except that <i>abs_timeout</i> specifies a limit on the amount of time that the call should block if the decrement cannot be immediately performed. The <i>abs_timeout</i> argument points to a structure that specifies an absolute timeout in seconds and nanoseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). This structure is defined as follows: struct timespec {<br />
    time_t tv_sec; /* Seconds */<br />
    long tv_nsec;  /* Nanoseconds [0 .. 999999999] */<br />
}; If the timeout has already expired by the time of the call, and the semaphore could not be locked immediately, then <code>sem_timedwait</code>() fails with a timeout error (<i>errno</i> set to <code>ETIMEDOUT</code>). If the operation can be performed immediately, then <code>sem_timedwait</code>() never fails with a timeout error, regardless of the value of <i>abs_timeout</i>. Furthermore, the validity of <i>abs_timeout</i> is not checked in this case.</p>
<h2>Return Value</h2>
<p>All of these functions return 0 on success; on error, the value of the semaphore is left unchanged, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINTR</code></p>
<dd>The call was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd><i>sem</i> is not a valid semaphore.</dl>
<p> The following additional error can occur for <code>sem_trywait</code>():</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd>The operation could not be performed without blocking (i.e., the semaphore currently has the value zero).</dl>
<p> The following additional errors can occur for <code>sem_timedwait</code>():</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>The value of <i>abs_timeout.tv_nsecs</i> is less than 0, or greater than or equal to 1000 million.</p>
<dt><code>ETIMEDOUT</code></p>
<dd>The call timed out before the semaphore could be locked.</dl>
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
<td> <code>sem_wait</code>(), <code>sem_trywait</code>(), <code>sem_timedwait</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Examples</h2>
<p>The (somewhat trivial) program shown below operates on an unnamed semaphore. The program expects two command-line arguments. The first argument specifies a seconds value that is used to set an alarm timer to generate a <code>SIGALRM</code> signal. This handler performs a <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3) to increment the semaphore that is being waited on in <i>main()</i> using <code>sem_timedwait</code>(). The second command-line argument specifies the length of the timeout, in seconds, for <code>sem_timedwait</code>(). The following shows what happens on two different runs of the program: $ ./a.out 2 3</p>
<p>About to call sem_timedwait()<br />
sem_post() from handler<br />
sem_timedwait() succeeded<br />
$ ./a.out 2 1</p>
<p>About to call sem_timedwait()<br />
sem_timedwait() timed out</p>
<p>Program source</p>
<p>#include &lt;unistd.h&gt;<br />
#include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;semaphore.h&gt;<br />
#include &lt;time.h&gt;<br />
#include &lt;assert.h&gt;<br />
#include &lt;errno.h&gt;<br />
#include &lt;signal.h&gt; sem_t sem; </p>
<pre><code>#define handle_error(msg)   \
    do {                    \
        perror(msg);        \
        exit(EXIT_FAILURE); \
    } while (0)
static void
handler(int sig)
{
    write(STDOUT_FILENO, &quot;sem_post() from handler
&quot;, 24);
    if (sem_post(&amp;sem) == -1) {
        write(STDERR_FILENO, &quot;sem_post() failed
&quot;, 18);
        _exit(EXIT_FAILURE);
    }
}
int main(int argc, char *argv[])
{
    struct sigaction sa;
    struct timespec ts;
    int s;
    if (argc != 3) {
        fprintf(stderr, &quot;Usage: %s &lt;alarm-secs&gt; &lt;wait-secs&gt;
&quot;,
                argv[0]);
        exit(EXIT_FAILURE);
    }
    if (sem_init(&amp;sem, 0, 0) == -1)
        handle_error(&quot;sem_init&quot;);
    /* Establish SIGALRM handler; set alarm timer using argv[1] */
    sa.sa_handler = handler;
    sigemptyset(&amp;sa.sa_mask);
    sa.sa_flags = 0;
    if (sigaction(SIGALRM, &amp;sa, NULL) == -1)
        handle_error(&quot;sigaction&quot;);
    alarm(atoi(argv[1]));
    /* Calculate relative interval as current time plus
           number of seconds given argv[2] */
    if (clock_gettime(CLOCK_REALTIME, &amp;ts) == -1)
        handle_error(&quot;clock_gettime&quot;);
    ts.tv_sec += atoi(argv[2]);
    printf(&quot;main() about to call sem_timedwait()
&quot;);
    while ((s = sem_timedwait(&amp;sem, &amp;ts)) == -1 &amp;&amp; errno == EINTR)
        continue; /* Restart if interrupted by handler */
    /* Check what happened */
    if (s == -1) {
        if (errno == ETIMEDOUT)
            printf(&quot;sem_timedwait() timed out
&quot;);
        else
            perror(&quot;sem_timedwait&quot;);
    } else
        printf(&quot;sem_timedwait() succeeded
&quot;);
    exit((s == 0) ? EXIT_SUCCESS : EXIT_FAILURE);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/3-sem_getvalue/">sem_getvalue</a></code>(3), <code><a href="/docs/linux/man/3-sem_post/">sem_post</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
