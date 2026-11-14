---
title: "pthread_mutexattr_getrobust_np(3)"
name: "pthread_mutexattr_getrobust_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_mutexattr_getrobust_np/"
description: "pthread_mutexattr_getrobust, pthread_mutexattr_setrobust – get and set the robustness attribute of a mutex attributes object"
---

<p>pthread_mutexattr_getrobust, pthread_mutexattr_setrobust &#8211; get and set the robustness attribute of a mutex attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_mutexattr_getrobust(const pthread_mutexattr_t *attr,
                                int *robustness);
int pthread_mutexattr_setrobust(const pthread_mutexattr_t *attr,
                                int robustness);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_mutexattr_getrobust</code>(), <code>pthread_mutexattr_setrobust</code>(): </p>
<dl>
<dd>_POSIX_C_SOURCE &gt;= 200809L</dl>
<h2>Description</h2>
<p>The <code>pthread_mutexattr_getrobust</code>() function places the value of the robustness attribute of the mutex attributes object referred to by <i>attr</i> in <i>*robustness</i>. The <code>pthread_mutexattr_setrobust</code>() function sets the value of the robustness attribute of the mutex attributes object referred to by <i>attr</i> to the value specified in <i>*robustness</i>. </p>
<p> The robustness attribute specifies the behavior of the mutex when the owning thread dies without unlocking the mutex. The following values are valid for <i>robustness</i>:</p>
<dl>
<dt><code>PTHREAD_MUTEX_STALLED</code></p>
<dd>This is the default value for a mutex attributes object. If a mutex is initialized with the <code>PTHREAD_MUTEX_STALLED</code> attribute and its owner dies without unlocking it, the mutex remains locked afterwards and any future attempts to call <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3) on the mutex will block indefinitely.</p>
<dt><code>PTHREAD_MUTEX_ROBUST</code></p>
<dd>If a mutex is initialized with the <code>PTHREAD_MUTEX_ROBUST</code> attribute and its owner dies without unlocking it, any future attempts to call <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3) on this mutex will succeed and return <code>EOWNERDEAD</code> to indicate that the original owner no longer exists and the mutex is in an inconsistent state. Usually after <code>EOWNERDEAD</code> is returned, the next owner should call <code><a href="/docs/linux/man/3-pthread_mutex_consistent/">pthread_mutex_consistent</a></code>(3) on the acquired mutex to make it consistent again before using it any further.</p>
<dd>If the next owner unlocks the mutex using <code><a href="/docs/linux/man/3-pthread_mutex_unlock/">pthread_mutex_unlock</a></code>(3) before making it consistent, the mutex will be permanently unusable and any subsequent attempts to lock it using <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3) will fail with the error <code>ENOTRECOVERABLE</code>. The only permitted operation on such a mutex is <code><a href="/docs/linux/man/3-pthread_mutex_destroy/">pthread_mutex_destroy</a></code>(3).</p>
<dd>If the next owner terminates before calling <code><a href="/docs/linux/man/3-pthread_mutex_consistent/">pthread_mutex_consistent</a></code>(3), further <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3) operations on this mutex will still return <code>EOWNERDEAD</code>.</dl>
<p> Note that the <i>attr</i> argument of <code>pthread_mutexattr_getrobust</code>() and <code>pthread_mutexattr_setrobust</code>() should refer to a mutex attributes object that was initialized by <code><a href="/docs/linux/man/3-pthread_mutexattr_init/">pthread_mutexattr_init</a></code>(3), otherwise the behavior is undefined.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0. On error, they return a positive error number. </p>
<p> In the glibc implementation, <code>pthread_mutexattr_getrobust</code>() always return zero.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>A value other than <code>PTHREAD_MUTEX_STALLED</code> or <code>PTHREAD_MUTEX_ROBUST</code> was passed to <code>pthread_mutexattr_setrobust</code>().</dl>
<h2>Versions</h2>
<p><code>pthread_mutexattr_getrobust</code>() and <code>pthread_mutexattr_setrobust</code>() were added to glibc in version 2.12.</p>
<h2>Conforming To</h2>
<p>POSIX.1-2008.</p>
<h2>Notes</h2>
<p>In the Linux implementation, when using process-shared robust mutexes, a waiting thread also receives the <code>EOWNERDEAD</code> notification if the owner of a robust mutex performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) without first unlocking the mutex. POSIX.1 does not specify this detail, but the same behavior also occurs in at least some other implementations. Before the addition of <code>pthread_mutexattr_getrobust</code>() and <code>pthread_mutexattr_setrobust</code>() to POSIX, glibc defined the following equivalent nonstandard functions if <code>_GNU_SOURCE</code> was defined: int pthread_mutexattr_getrobust_np(const pthread_mutexattr_t *attr,<br />
                                   int *robustness);<br />
int pthread_mutexattr_setrobust_np(const pthread_mutexattr_t *attr,<br />
                                   int robustness); Correspondingly, the constants <code>PTHREAD_MUTEX_STALLED_NP</code> and <code>PTHREAD_MUTEX_ROBUST_NP</code> were also defined. These GNU-specific APIs, which first appeared in glibc 2.4, are nowadays obsolete and should not be used in new programs.</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of the robustness attribute of a mutex attributes object. In this program, a thread holding the mutex dies prematurely without unlocking the mutex. The main thread subsequently acquires the mutex successfully and gets the error <code>EOWNERDEAD</code>, after which it makes the mutex consistent. The following shell session shows what we see when running this program: </p>
<pre><code>$ ./a.out
[original owner] Setting lock...
[original owner] Locked. Now exiting without unlocking.
[main] Attempting to lock the robust mutex.
[main] pthread_mutex_lock() returned EOWNERDEAD
[main] Now make the mutex consistent
[main] Mutex is now consistent; unlocking



Program source


#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;
#include &lt;errno.h&gt;
#define handle_error_en(en, msg) \
do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)
static pthread_mutex_t mtx;
static void *
original_owner_thread(void *ptr)
{
    printf(&quot;[original owner] Setting lock...
&quot;);
    pthread_mutex_lock(&amp;mtx);
    printf(&quot;[original owner] Locked. Now exiting without unlocking.
&quot;);
    pthread_exit(NULL);
}
int
main(int argc, char *argv[])
{
    pthread_t thr;
    pthread_mutexattr_t attr;
    int s;
    pthread_mutexattr_init(&amp;attr);
    /* initialize the attributes object */
    pthread_mutexattr_setrobust(&amp;attr, PTHREAD_MUTEX_ROBUST);
    /* set robustness */
    pthread_mutex_init(&amp;mtx, &amp;attr);   /* initialize the mutex */
    pthread_create(&amp;thr, NULL, original_owner_thread, NULL);
    sleep(2);
    /* &quot;original_owner_thread&quot; should have exited by now */
    printf(&quot;[main] Attempting to lock the robust mutex.
&quot;);
    s = pthread_mutex_lock(&amp;mtx);
    if (s == EOWNERDEAD) {
        printf(&quot;[main] pthread_mutex_lock() returned EOWNERDEAD
&quot;);
        printf(&quot;[main] Now make the mutex consistent
&quot;);
        s = pthread_mutex_consistent(&amp;mtx);
        if (s != 0)
        handle_error_en(s, &quot;pthread_mutex_consistent&quot;);
        printf(&quot;[main] Mutex is now consistent; unlocking
&quot;);
        s = pthread_mutex_unlock(&amp;mtx);
        if (s != 0)
        handle_error_en(s, &quot;pthread_mutex_unlock&quot;);
        exit(EXIT_SUCCESS);
    } else if (s == 0) {
        printf(&quot;[main] pthread_mutex_lock() unexpectedly succeeded
&quot;);
        exit(EXIT_FAILURE);
    } else {
        printf(&quot;[main] pthread_mutex_lock() unexpectedly failed
&quot;);
        handle_error_en(s, &quot;pthread_mutex_lock&quot;);
    }
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-set_robust_list/">set_robust_list</a></code>(2), <code><a href="/docs/linux/man/3-pthread_mutex_consistent/">pthread_mutex_consistent</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_init/">pthread_mutex_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_mutex_lock/">pthread_mutex_lock</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
