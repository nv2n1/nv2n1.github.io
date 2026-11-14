---
title: "sigevent(7)"
name: "sigevent"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sigevent/"
description: "sigevent – structure for notification from asynchronous routines"
---

<p>sigevent &#8211; structure for notification from asynchronous routines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

union sigval {       /* Data passed with notification */
    int sival_int;   /* Integer value */
    void *sival_ptr; /* Pointer value */
};

struct sigevent {
    int sigev_notify; /* Notification method */
    int sigev_signo;  /* Notification signal */
    union sigval sigev_value;
    /* Data passed with notification */
    void (*sigev_notify_function)(union sigval);
    /* Function used for thread
       notification (SIGEV_THREAD) */
    void *sigev_notify_attributes;
    /* Attributes for notification thread
       (SIGEV_THREAD) */
    pid_t sigev_notify_thread_id;
    /* ID of thread to signal
       (SIGEV_THREAD_ID); Linux-specific */
};</code></pre>
<h2>Description</h2>
<p>The <i>sigevent</i> structure is used by various APIs to describe the way a process is to be notified about an event (e.g., completion of an asynchronous request, expiration of a timer, or the arrival of a message). </p>
<p> The definition shown in the SYNOPSIS is approximate: some of the fields in the <i>sigevent</i> structure may be defined as part of a union. Programs should employ only those fields relevant to the value specified in <i>sigev_notify</i>. </p>
<p> The <i>sigev_notify</i> field specifies how notification is to be performed. This field can have one of the following values:</p>
<dl>
<dt><code>SIGEV_NONE</code></p>
<dd>A &quot;null&quot; notification: don&#8217;t do anything when the event occurs.</p>
<dt><code>SIGEV_SIGNAL</code></p>
<dd>Notify the process by sending the signal specified in <i>sigev_signo</i>.</p>
<dd>If the signal is caught with a signal handler that was registered using the <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) <code>SA_SIGINFO</code> flag, then the following fields are set in the <i>siginfo_t</i> structure that is passed as the second argument of the handler:</p>
<dl>
<dd>
<dl>
<dt><i>si_code</i></p>
<dd>This field is set to a value that depends on the API delivering the notification.</p>
<dt><i>si_signo</i></p>
<dd>This field is set to the signal number (i.e., the same value as in <i>sigev_signo</i>).</p>
<dt><i>si_value</i></p>
<dd>This field is set to the value specified in <i>sigev_value</i>.</dl>
</dl>
<dd>Depending on the API, other fields may also be set in the <i>siginfo_t</i> structure.</p>
<dd>The same information is also available if the signal is accepted using <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2).</p>
<dt><code>SIGEV_THREAD</code></p>
<dd>Notify the process by invoking <i>sigev_notify_function</i> &quot;as if&quot; it were the start function of a new thread. (Among the implementation possibilities here are that each timer notification could result in the creation of a new thread, or that a single thread is created to receive all notifications.) The function is invoked with <i>sigev_value</i> as its sole argument. If <i>sigev_notify_attributes</i> is not NULL, it should point to a <i>pthread_attr_t</i> structure that defines attributes for the new thread (see <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3)).</p>
<dt><code>SIGEV_THREAD_ID</code> (Linux-specific)</p>
<dd>Currently used only by POSIX timers; see <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-aio_fsync/">aio_fsync</a></code>(3), <code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3), <code><a href="/docs/linux/man/3-getaddrinfo_a/">getaddrinfo_a</a></code>(3), <code><a href="/docs/linux/man/3-lio_listio/">lio_listio</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/7-aio/">aio</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
