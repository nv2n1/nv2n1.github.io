---
title: "pthread_sigmask(3)"
name: "pthread_sigmask"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_sigmask/"
description: "pthread_sigmask – examine and change mask of blocked signals"
---

<p>pthread_sigmask &#8211; examine and change mask of blocked signals</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int pthread_sigmask(int how, const sigset_t *set, sigset_t *oldset);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_sigmask</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<h2>Description</h2>
<p>The <code>pthread_sigmask</code>() function is just like <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), with the difference that its use in multithreaded programs is explicitly specified by POSIX.1. Other differences are noted in this page. </p>
<p> For a description of the arguments and operation of this function, see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2).</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_sigmask</code>() returns 0; on error, it returns an error number.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2).</p>
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
<td> <code>pthread_sigmask</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>A new thread inherits a copy of its creator&#8217;s signal mask. </p>
<p> The glibc <code>pthread_sigmask</code>() function silently ignores attempts to block the two real-time signals that are used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details.</p>
<h2>Examples</h2>
<p>The program below blocks some signals in the main thread, and then creates a dedicated thread to fetch those signals via <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3). The following shell session demonstrates its use: </p>
<pre><code>$ ./a.out &amp;

[1] 5423
$ kill -QUIT %1

Signal handling thread got signal 3
$ kill -USR1 %1

Signal handling thread got signal 10
$ kill -TERM %1

[1]+  Terminated              ./a.out



Program source



#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;signal.h&gt;
#include &lt;errno.h&gt;
/* Simple error handling functions */
#define handle_error_en(en, msg) \
do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)
static void *
sig_thread(void *arg)
{
    sigset_t *set = arg;
    int s, sig;
    for (;;) {
        s = sigwait(set, &amp;sig);
        if (s != 0)
        handle_error_en(s, &quot;sigwait&quot;);
        printf(&quot;Signal handling thread got signal %d
&quot;, sig);
    }
}
int
main(int argc, char *argv[])
{
    pthread_t thread;
    sigset_t set;
    int s;
    /* Block SIGQUIT and SIGUSR1; other threads created by main()
    will inherit a copy of the signal mask. */
    sigemptyset(&amp;set);
    sigaddset(&amp;set, SIGQUIT);
    sigaddset(&amp;set, SIGUSR1);
    s = pthread_sigmask(SIG_BLOCK, &amp;set, NULL);
    if (s != 0)
    handle_error_en(s, &quot;pthread_sigmask&quot;);
    s = pthread_create(&amp;thread, NULL, &amp;sig_thread, &amp;set);
    if (s != 0)
    handle_error_en(s, &quot;pthread_create&quot;);
    /* Main thread carries on to create other threads and/or do
    other work */
    pause();            /* Dummy pause so we can test program */
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_setsigmask_np/">pthread_attr_setsigmask_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_kill/">pthread_kill</a></code>(3), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
