---
title: "pthread_getattr_default_np(3)"
name: "pthread_getattr_default_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_getattr_default_np/"
description: "pthread_getattr_default_np, pthread_setattr_default_np, – get or set default thread-creation attributes"
---

<p>pthread_getattr_default_np, pthread_setattr_default_np, &#8211; get or set default thread-creation attributes</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_getattr_default_np(pthread_attr_t *attr);
int pthread_setattr_default_np(pthread_attr_t *attr);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setattr_default_np</code>() function sets the default attributes used for creation of a new thread&#8212;that is, the attributes that are used when <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) is called with a second argument that is NULL. The default attributes are set using the attributes supplied in <i>*attr</i>, a previously initialized thread attributes object. Note the following details about the supplied attributes object:</p>
<dl>
<dt>*</p>
<dd>The attribute settings in the object must be valid.</p>
<dt>*</p>
<dd>The <i>stack address</i> attribute must not be set in the object.</p>
<dt>*</p>
<dd>Setting the <i>stack size</i> attribute to zero means leave the default stack size unchanged.</dl>
<p> The <code>pthread_getattr_default_np</code>() function initializes the thread attributes object referred to by <i>attr</i> so that it contains the default attributes used for thread creation.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>(<code>pthread_setattr_default_np</code>()) One of the attribute settings in <i>attr</i> is invalid, or the stack address attribute is set in <i>attr</i>.</p>
<dt><code>ENOMEM</code></p>
<dd>(<code>pthread_setattr_default_np</code>()) Insufficient memory.</dl>
<h2>Versions</h2>
<p>These functions are available in glibc since version 2.18.</p>
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
<td> <code>pthread_getattr_default_np</code>(), <code>pthread_setattr_default_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in their names.</p>
<h2>Examples</h2>
<p>The program below uses <code>pthread_getattr_default_np</code>() to fetch the default thread-creation attributes and then displays various settings from the returned thread attributes object. When running the program, we see the following output: </p>
<pre><code>$ ./a.out
Stack size:          8388608
Guard size:          4096
Scheduling policy:   SCHED_OTHER
Scheduling priority: 0
Detach state:        JOINABLE
Inherit scheduler:   INHERIT



Program source



#define _GNU_SOURCE
#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;errno.h&gt;
#define errExitEN(en, msg) \
do { errno = en; perror(msg); \
    exit(EXIT_FAILURE); } while (0)
static void
display_pthread_attr(pthread_attr_t *attr)
{
    int s;
    size_t stacksize;
    size_t guardsize;
    int policy;
    struct sched_param schedparam;
    int detachstate;
    int inheritsched;
    s = pthread_attr_getstacksize(attr, &amp;stacksize);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getstacksize&quot;);
    printf(&quot;Stack size:          %zd
&quot;, stacksize);
    s = pthread_attr_getguardsize(attr, &amp;guardsize);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getguardsize&quot;);
    printf(&quot;Guard size:          %zd
&quot;, guardsize);
    s = pthread_attr_getschedpolicy(attr, &amp;policy);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getschedpolicy&quot;);
    printf(&quot;Scheduling policy:   %s
&quot;,
    (policy == SCHED_FIFO) ? &quot;SCHED_FIFO&quot; :
    (policy == SCHED_RR) ? &quot;SCHED_RR&quot; :
    (policy == SCHED_OTHER) ? &quot;SCHED_OTHER&quot; : &quot;[unknown]&quot;);
    s = pthread_attr_getschedparam(attr, &amp;schedparam);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getschedparam&quot;);
    printf(&quot;Scheduling priority: %d
&quot;, schedparam.sched_priority);
    s = pthread_attr_getdetachstate(attr, &amp;detachstate);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getdetachstate&quot;);
    printf(&quot;Detach state:        %s
&quot;,
    (detachstate == PTHREAD_CREATE_DETACHED) ? &quot;DETACHED&quot; :
    (detachstate == PTHREAD_CREATE_JOINABLE) ? &quot;JOINABLE&quot; :
    &quot;???&quot;);
    s = pthread_attr_getinheritsched(attr, &amp;inheritsched);
    if (s != 0)
    errExitEN(s, &quot;pthread_attr_getinheritsched&quot;);
    printf(&quot;Inherit scheduler:   %s
&quot;,
    (inheritsched == PTHREAD_INHERIT_SCHED) ? &quot;INHERIT&quot; :
    (inheritsched == PTHREAD_EXPLICIT_SCHED) ? &quot;EXPLICIT&quot; :
    &quot;???&quot;);
}
int
main(int argc, char *argv[])
{
    int s;
    pthread_attr_t attr;
    s = pthread_getattr_default_np(&amp;attr);
    if (s != 0)
    errExitEN(s, &quot;pthread_getattr_default_np&quot;);
    display_pthread_attr(&amp;attr);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_getaffinity_np/">pthread_attr_getaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getdetachstate/">pthread_attr_getdetachstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getguardsize/">pthread_attr_getguardsize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getinheritsched/">pthread_attr_getinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getschedparam/">pthread_attr_getschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getschedpolicy/">pthread_attr_getschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getscope/">pthread_attr_getscope</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstack/">pthread_attr_getstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstackaddr/">pthread_attr_getstackaddr</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstacksize/">pthread_attr_getstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
