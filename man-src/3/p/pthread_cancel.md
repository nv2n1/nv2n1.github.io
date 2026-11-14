---
title: "pthread_cancel(3)"
name: "pthread_cancel"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_cancel/"
description: "pthread_cancel – send a cancellation request to a thread"
---

<p>pthread_cancel &#8211; send a cancellation request to a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_cancel(pthread_t thread);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_cancel</code>() function sends a cancellation request to the thread <i>thread</i>. Whether and when the target thread reacts to the cancellation request depends on two attributes that are under the control of that thread: its cancelability <i>state</i> and <i>type</i>. </p>
<p> A thread&#8217;s cancelability state, determined by <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), can be <i>enabled</i> (the default for new threads) or <i>disabled</i>. If a thread has disabled cancellation, then a cancellation request remains queued until the thread enables cancellation. If a thread has enabled cancellation, then its cancelability type determines when cancellation occurs. </p>
<p> A thread&#8217;s cancellation type, determined by <code><a href="/docs/linux/man/3-pthread_setcanceltype/">pthread_setcanceltype</a></code>(3), may be either <i>asynchronous</i> or <i>deferred</i> (the default for new threads). Asynchronous cancelability means that the thread can be canceled at any time (usually immediately, but the system does not guarantee this). Deferred cancelability means that cancellation will be delayed until the thread next calls a function that is a <i>cancellation point</i>. A list of functions that are or may be cancellation points is provided in <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7). </p>
<p> When a cancellation requested is acted on, the following steps occur for <i>thread</i> (in this order):</p>
<dl>
<dt>1.</p>
<dd>Cancellation clean-up handlers are popped (in the reverse of the order in which they were pushed) and called. (See <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3).)</p>
<dt>2.</p>
<dd>Thread-specific data destructors are called, in an unspecified order. (See <code><a href="/docs/linux/man/3-pthread_key_create/">pthread_key_create</a></code>(3).)</p>
<dt>3.</p>
<dd>The thread is terminated. (See <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3).)</dl>
<p> The above steps happen asynchronously with respect to the <code>pthread_cancel</code>() call; the return status of <code>pthread_cancel</code>() merely informs the caller whether the cancellation request was successfully queued. </p>
<p> After a canceled thread has terminated, a join with that thread using <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3) obtains <code>PTHREAD_CANCELED</code> as the thread&#8217;s exit status. (Joining with a thread is the only way to know that cancellation has completed.)</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_cancel</code>() returns 0; on error, it returns a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
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
<td> <code>pthread_cancel</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, cancellation is implemented using signals. Under the NPTL threading implementation, the first real-time signal (i.e., signal 32) is used for this purpose. On LinuxThreads, the second real-time signal is used, if real-time signals are available, otherwise <code>SIGUSR2</code> is used.</p>
<h2>Examples</h2>
<p>The program below creates a thread and then cancels it. The main thread joins with the canceled thread to check that its exit status was <code>PTHREAD_CANCELED</code>. The following shell session shows what happens when we run the program: </p>
<pre><code>$ ./a.out
thread_func(): started; cancellation disabled
main(): sending cancellation request
thread_func(): about to enable cancellation
main(): thread was canceled



Program source



#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;errno.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#define handle_error_en(en, msg) \
do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)
static void *
thread_func(void *ignored_argument)
{
    int s;
    /* Disable cancellation for a while, so that we don't
    immediately react to a cancellation request */
    s = pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);
    if (s != 0)
    handle_error_en(s, &quot;pthread_setcancelstate&quot;);
    printf(&quot;thread_func(): started; cancellation disabled
&quot;);
    sleep(5);
    printf(&quot;thread_func(): about to enable cancellation
&quot;);
    s = pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
    if (s != 0)
    handle_error_en(s, &quot;pthread_setcancelstate&quot;);
    /* sleep() is a cancellation point */
    sleep(1000);        /* Should get canceled while we sleep */
    /* Should never get here */
    printf(&quot;thread_func(): not canceled!
&quot;);
    return NULL;
}
int
main(void)
{
    pthread_t thr;
    void *res;
    int s;
    /* Start a thread and then send it a cancellation request */
    s = pthread_create(&amp;thr, NULL, &amp;thread_func, NULL);
    if (s != 0)
    handle_error_en(s, &quot;pthread_create&quot;);
    sleep(2);           /* Give thread a chance to get started */
    printf(&quot;main(): sending cancellation request
&quot;);
    s = pthread_cancel(thr);
    if (s != 0)
    handle_error_en(s, &quot;pthread_cancel&quot;);
    /* Join with thread to see what its exit status was */
    s = pthread_join(thr, &amp;res);
    if (s != 0)
    handle_error_en(s, &quot;pthread_join&quot;);
    if (res == PTHREAD_CANCELED)
    printf(&quot;main(): thread was canceled
&quot;);
    else
    printf(&quot;main(): thread wasn't canceled (shouldn't happen!)
&quot;);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), <code><a href="/docs/linux/man/3-pthread_key_create/">pthread_key_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcanceltype/">pthread_setcanceltype</a></code>(3), <code><a href="/docs/linux/man/3-pthread_testcancel/">pthread_testcancel</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
