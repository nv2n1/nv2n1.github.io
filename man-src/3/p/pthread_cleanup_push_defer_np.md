---
title: "pthread_cleanup_push_defer_np(3)"
name: "pthread_cleanup_push_defer_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_cleanup_push_defer_np/"
description: "pthread_cleanup_push_defer_np, pthread_cleanup_pop_restore_np – push and pop thread cancellation clean-up handlers while saving cancelability type"
---

<p>pthread_cleanup_push_defer_np, pthread_cleanup_pop_restore_np &#8211; push and pop thread cancellation clean-up handlers while saving cancelability type</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

void pthread_cleanup_push_defer_np(void (*routine)(void *),
                                   void *arg);
void pthread_cleanup_pop_restore_np(int execute);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_cleanup_push_defer_np</code>(), <code>pthread_cleanup_pop_defer_np</code>():</p>
<dl>
<dd>_GNU_SOURCE</dl>
<h2>Description</h2>
<p>These functions are the same as <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_cleanup_pop/">pthread_cleanup_pop</a></code>(3), except for the differences noted on this page. Like <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code>pthread_cleanup_push_defer_np</code>() pushes <i>routine</i> onto the thread&#8217;s stack of cancellation clean-up handlers. In addition, it also saves the thread&#8217;s current cancelability type, and sets the cancelability type to &quot;deferred&quot; (see <code><a href="/docs/linux/man/3-pthread_setcanceltype/">pthread_setcanceltype</a></code>(3)); this ensures that cancellation clean-up will occur even if the thread&#8217;s cancelability type was &quot;asynchronous&quot; before the call. Like <code><a href="/docs/linux/man/3-pthread_cleanup_pop/">pthread_cleanup_pop</a></code>(3), <code>pthread_cleanup_pop_restore_np</code>() pops the top-most clean-up handler from the thread&#8217;s stack of cancellation clean-up handlers. In addition, it restores the thread&#8217;s cancelability type to its value at the time of the matching <code>pthread_cleanup_push_defer_np</code>(). The caller must ensure that calls to these functions are paired within the same function, and at the same lexical nesting level. Other restrictions apply, as described in <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3). This sequence of calls: pthread_cleanup_push_defer_np(routine, arg); pthread_cleanup_pop_restore_np(execute); is equivalent to (but shorter and more efficient than): </p>
<pre><code>int oldtype;</code></pre>
<p> pthread_cleanup_push(routine, arg); pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED, &amp;oldtype); &#8230; pthread_setcanceltype(oldtype, NULL); pthread_cleanup_pop(execute);</p>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_testcancel/">pthread_testcancel</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
