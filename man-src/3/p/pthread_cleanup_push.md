---
title: "pthread_cleanup_push(3)"
name: "pthread_cleanup_push"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_cleanup_push/"
description: "pthread_cleanup_push, pthread_cleanup_pop – push and pop thread cancellation clean-up handlers"
---

<p>pthread_cleanup_push, pthread_cleanup_pop &#8211; push and pop thread cancellation clean-up handlers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

void pthread_cleanup_push(void (*routine)(void *),
                          void *arg);
void pthread_cleanup_pop(int execute);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>These functions manipulate the calling thread&#8217;s stack of thread-cancellation clean-up handlers. A clean-up handler is a function that is automatically executed when a thread is canceled (or in various other circumstances described below); it might, for example, unlock a mutex so that it becomes available to other threads in the process. </p>
<p> The <code>pthread_cleanup_push</code>() function pushes <i>routine</i> onto the top of the stack of clean-up handlers. When <i>routine</i> is later invoked, it will be given <i>arg</i> as its argument. </p>
<p> The <code>pthread_cleanup_pop</code>() function removes the routine at the top of the stack of clean-up handlers, and optionally executes it if <i>execute</i> is nonzero. </p>
<p> A cancellation clean-up handler is popped from the stack and executed in the following circumstances:</p>
<dl>
<dt>1.</p>
<dd>When a thread is canceled, all of the stacked clean-up handlers are popped and executed in the reverse of the order in which they were pushed onto the stack.</p>
<dt>2.</p>
<dd>When a thread terminates by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), all clean-up handlers are executed as described in the preceding point. (Clean-up handlers are <i>not</i> called if the thread terminates by performing a <i>return</i> from the thread start function.)</p>
<dt>3.</p>
<dd>When a thread calls <code>pthread_cleanup_pop</code>() with a nonzero <i>execute</i> argument, the top-most clean-up handler is popped and executed.</dl>
<p> POSIX.1 permits <code>pthread_cleanup_push</code>() and <code>pthread_cleanup_pop</code>() to be implemented as macros that expand to text containing &#8216;<code>{</code>&#8216; and &#8216;<code>}</code>&#8216;, respectively. For this reason, the caller must ensure that calls to these functions are paired within the same function, and at the same lexical nesting level. (In other words, a clean-up handler is established only during the execution of a specified section of code.) </p>
<p> Calling <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) (<code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3)) produces undefined results if any call has been made to <code>pthread_cleanup_push</code>() or <code>pthread_cleanup_pop</code>() without the matching call of the pair since the jump buffer was filled by <code><a href="/docs/linux/man/3-setjmp/">setjmp</a></code>(3) (<code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)). Likewise, calling <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) (<code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3)) from inside a clean-up handler produces undefined results unless the jump buffer was also filled by <code><a href="/docs/linux/man/3-setjmp/">setjmp</a></code>(3) (<code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)) inside the handler.</p>
<h2>Return Value</h2>
<p>These functions do not return a value.</p>
<h2>Errors</h2>
<p>There are no errors.</p>
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
<td> <code>pthread_cleanup_push</code>(), <code>pthread_cleanup_pop</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, the <code>pthread_cleanup_push</code>() and <code>pthread_cleanup_pop</code>() functions <i>are</i> implemented as macros that expand to text containing &#8216;<code>{</code>&#8216; and &#8216;<code>}</code>&#8216;, respectively. This means that variables declared within the scope of paired calls to these functions will be visible within only that scope. </p>
<p> POSIX.1 says that the effect of using <i>return</i>, <i>break</i>, <i>continue</i>, or <i>goto</i> to prematurely leave a block bracketed <code>pthread_cleanup_push</code>() and <code>pthread_cleanup_pop</code>() is undefined. Portable applications should avoid doing this.</p>
<h2>Examples</h2>
<p>The program below provides a simple example of the use of the functions described in this page. The program creates a thread that executes a loop bracketed by <code>pthread_cleanup_push</code>() and <code>pthread_cleanup_pop</code>(). This loop increments a global variable, <i>cnt</i>, once each second. Depending on what command-line arguments are supplied, the main thread sends the other thread a cancellation request, or sets a global variable that causes the other thread to exit its loop and terminate normally (by doing a <i>return</i>). In the following shell session, the main thread sends a cancellation request to the other thread: $ <code>./a.out</code> New thread started cnt = 0 cnt = 1 Canceling thread Called clean-up handler Thread was canceled; cnt = 0 From the above, we see that the thread was canceled, and that the cancellation clean-up handler was called and it reset the value of the global variable <i>cnt</i> to 0. In the next run, the main program sets a global variable that causes other thread to terminate normally: $ <code>./a.out x</code> New thread started cnt = 0 cnt = 1 Thread terminated normally; cnt = 2 From the above, we see that the clean-up handler was not executed (because <i>cleanup_pop_arg</i> was 0), and therefore the value of <i>cnt</i> was not reset. In the next run, the main program sets a global variable that causes the other thread to terminate normally, and supplies a nonzero value for <i>cleanup_pop_arg</i>: $ <code>./a.out x 1</code> New thread started cnt = 0 cnt = 1 Called clean-up handler Thread terminated normally; cnt = 0 In the above, we see that although the thread was not canceled, the clean-up handler was executed, because the argument given to <code>pthread_cleanup_pop</code>() was nonzero.</p>
<h3>Program source</h3>
<p>#include &lt;pthread.h&gt; #include &lt;sys/types.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;errno.h&gt; </p>
<pre><code>#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)
static int done = 0;
static int cleanup_pop_arg = 0;
static int cnt = 0;
static void
cleanup_handler(void *arg)
{
    printf(&quot;Called clean-up handler
&quot;);
    cnt = 0;
}
static void *
thread_start(void *arg)
{
    time_t start, curr;
    printf(&quot;New thread started
&quot;);
    pthread_cleanup_push(cleanup_handler, NULL);
    curr = start = time(NULL);
    while (!done) {
        pthread_testcancel(); /* A cancellation point */
        if (curr &lt; time(NULL)) {
            curr = time(NULL);
            printf(&quot;cnt = %d
&quot;, cnt); /* A cancellation point */
            cnt++;
        }
    }
    pthread_cleanup_pop(cleanup_pop_arg);
    return NULL;
}
int main(int argc, char *argv[])
{
    pthread_t thr;
    int s;
    void *res;
    s = pthread_create(&amp;thr, NULL, thread_start, NULL);
    if (s != 0)
        handle_error_en(s, &quot;pthread_create&quot;);
    sleep(2); /* Allow new thread to run a while */
    if (argc &gt; 1) {
        if (argc &gt; 2)
            cleanup_pop_arg = atoi(argv[2]);
        done = 1;
    } else {
        printf(&quot;Canceling thread
&quot;);
        s = pthread_cancel(thr);
        if (s != 0)
            handle_error_en(s, &quot;pthread_cancel&quot;);
    }
    s = pthread_join(thr, &amp;res);
    if (s != 0)
        handle_error_en(s, &quot;pthread_join&quot;);
    if (res == PTHREAD_CANCELED)
        printf(&quot;Thread was canceled; cnt = %d
&quot;, cnt);
    else
        printf(&quot;Thread terminated normally; cnt = %d
&quot;, cnt);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cleanup_push_defer_np/">pthread_cleanup_push_defer_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_testcancel/">pthread_testcancel</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
