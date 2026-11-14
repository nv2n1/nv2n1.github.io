---
title: "pthread_attr_init(3)"
name: "pthread_attr_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_init/"
description: "pthread_attr_init, pthread_attr_destroy – initialize and destroy thread attributes object"
---

<p>pthread_attr_init, pthread_attr_destroy &#8211; initialize and destroy thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_init(pthread_attr_t *attr);
int pthread_attr_destroy(pthread_attr_t *attr);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_init</code>() function initializes the thread attributes object pointed to by <i>attr</i> with default attribute values. After this call, individual attributes of the object can be set using various related functions (listed under SEE ALSO), and then the object can be used in one or more <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) calls that create threads. </p>
<p> Calling <code>pthread_attr_init</code>() on a thread attributes object that has already been initialized results in undefined behavior. </p>
<p> When a thread attributes object is no longer required, it should be destroyed using the <code>pthread_attr_destroy</code>() function. Destroying a thread attributes object has no effect on threads that were created using that object. </p>
<p> Once a thread attributes object has been destroyed, it can be reinitialized using <code>pthread_attr_init</code>(). Any other use of a destroyed thread attributes object has undefined results.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p>POSIX.1 documents an <code>ENOMEM</code> error for <code>pthread_attr_init</code>(); on Linux these functions always succeed (but portable and future-proof applications should nevertheless handle a possible error return).</p>
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
<td> <code>pthread_attr_init</code>(), <code>pthread_attr_destroy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The <i>pthread_attr_t</i> type should be treated as opaque: any access to the object other than via pthreads functions is nonportable and produces undefined results.</p>
<h2>Examples</h2>
<p>The program below optionally makes use of <code>pthread_attr_init</code>() and various related functions to initialize a thread attributes object that is used to create a single thread. Once created, the thread uses the <code><a href="/docs/linux/man/3-pthread_getattr_np/">pthread_getattr_np</a></code>(3) function (a nonstandard GNU extension) to retrieve the thread&#8217;s attributes, and then displays those attributes. If the program is run with no command-line argument, then it passes NULL as the <i>attr</i> argument of <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), so that the thread is created with default attributes. Running the program on Linux/x86-32 with the NPTL threading implementation, we see the following: $<code> ulimit -s</code> # No stack limit ==&gt; default stack size is 2 MB unlimited $<code> ./a.out</code> Thread attributes:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Detach state&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;PTHREAD_CREATE_JOINABLE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Scope&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;PTHREAD_SCOPE_SYSTEM<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Inherit scheduler&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;PTHREAD_INHERIT_SCHED<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Scheduling policy&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;SCHED_OTHER<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Scheduling priority&nbsp;=&nbsp;0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Guard size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4096 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x40196000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x201000 bytes When we supply a stack size as a command-line argument, the program initializes a thread attributes object, sets various attributes in that object, and passes a pointer to the object in the call to <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3). Running the program on Linux/x86-32 with the NPTL threading implementation, we see the following: </p>
<pre><code>$ ./a.out 0x3000000

posix_memalign() allocated at 0x40197000
Thread attributes:
Detach state        = PTHREAD_CREATE_DETACHED
Scope               = PTHREAD_SCOPE_SYSTEM
Inherit scheduler   = PTHREAD_EXPLICIT_SCHED
Scheduling policy   = SCHED_OTHER
Scheduling priority = 0
Guard size          = 0 bytes
Stack address       = 0x40197000
Stack size          = 0x3000000 bytes



Program source



#define _GNU_SOURCE     /* To get pthread_getattr_np() declaration */
#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;errno.h&gt;
#define handle_error_en(en, msg) \
do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)
static void
display_pthread_attr(pthread_attr_t *attr, char *prefix)
{
    int s, i;
    size_t v;
    void *stkaddr;
    struct sched_param sp;
    s = pthread_attr_getdetachstate(attr, &amp;i);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getdetachstate&quot;);
    printf(&quot;%sDetach state        = %s
&quot;, prefix,
    (i == PTHREAD_CREATE_DETACHED) ? &quot;PTHREAD_CREATE_DETACHED&quot; :
    (i == PTHREAD_CREATE_JOINABLE) ? &quot;PTHREAD_CREATE_JOINABLE&quot; :
    &quot;???&quot;);
    s = pthread_attr_getscope(attr, &amp;i);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getscope&quot;);
    printf(&quot;%sScope               = %s
&quot;, prefix,
    (i == PTHREAD_SCOPE_SYSTEM)  ? &quot;PTHREAD_SCOPE_SYSTEM&quot; :
    (i == PTHREAD_SCOPE_PROCESS) ? &quot;PTHREAD_SCOPE_PROCESS&quot; :
    &quot;???&quot;);
    s = pthread_attr_getinheritsched(attr, &amp;i);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getinheritsched&quot;);
    printf(&quot;%sInherit scheduler   = %s
&quot;, prefix,
    (i == PTHREAD_INHERIT_SCHED)  ? &quot;PTHREAD_INHERIT_SCHED&quot; :
    (i == PTHREAD_EXPLICIT_SCHED) ? &quot;PTHREAD_EXPLICIT_SCHED&quot; :
    &quot;???&quot;);
    s = pthread_attr_getschedpolicy(attr, &amp;i);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getschedpolicy&quot;);
    printf(&quot;%sScheduling policy   = %s
&quot;, prefix,
    (i == SCHED_OTHER) ? &quot;SCHED_OTHER&quot; :
    (i == SCHED_FIFO)  ? &quot;SCHED_FIFO&quot; :
    (i == SCHED_RR)    ? &quot;SCHED_RR&quot; :
    &quot;???&quot;);
    s = pthread_attr_getschedparam(attr, &amp;sp);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getschedparam&quot;);
    printf(&quot;%sScheduling priority = %d
&quot;, prefix, sp.sched_priority);
    s = pthread_attr_getguardsize(attr, &amp;v);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getguardsize&quot;);
    printf(&quot;%sGuard size          = %zu bytes
&quot;, prefix, v);
    s = pthread_attr_getstack(attr, &amp;stkaddr, &amp;v);
    if (s != 0)
    handle_error_en(s, &quot;pthread_attr_getstack&quot;);
    printf(&quot;%sStack address       = %p
&quot;, prefix, stkaddr);
    printf(&quot;%sStack size          = %#zx bytes
&quot;, prefix, v);
}
static void *
thread_start(void *arg)
{
    int s;
    pthread_attr_t gattr;
    /* pthread_getattr_np() is a non-standard GNU extension that
    retrieves the attributes of the thread specified in its
    first argument */
    s = pthread_getattr_np(pthread_self(), &amp;gattr);
    if (s != 0)
    handle_error_en(s, &quot;pthread_getattr_np&quot;);
    printf(&quot;Thread attributes:
&quot;);
    display_pthread_attr(&amp;gattr, &quot;	&quot;);
    exit(EXIT_SUCCESS);         /* Terminate all threads */
}
int
main(int argc, char *argv[])
{
    pthread_t thr;
    pthread_attr_t attr;
    pthread_attr_t *attrp;      /* NULL or &amp;attr */
    int s;
    attrp = NULL;
    /* If a command-line argument was supplied, use it to set the
    stack-size attribute and set a few other thread attributes,
    and set attrp pointing to thread attributes object */
    if (argc &gt; 1) {
        size_t stack_size;
        void *sp;
        attrp = &amp;attr;
        s = pthread_attr_init(&amp;attr);
        if (s != 0)
        handle_error_en(s, &quot;pthread_attr_init&quot;);
        s = pthread_attr_setdetachstate(&amp;attr, PTHREAD_CREATE_DETACHED);
        if (s != 0)
        handle_error_en(s, &quot;pthread_attr_setdetachstate&quot;);
        s = pthread_attr_setinheritsched(&amp;attr, PTHREAD_EXPLICIT_SCHED);
        if (s != 0)
        handle_error_en(s, &quot;pthread_attr_setinheritsched&quot;);
        stack_size = strtoul(argv[1], NULL, 0);
        s = posix_memalign(&amp;sp, sysconf(_SC_PAGESIZE), stack_size);
        if (s != 0)
        handle_error_en(s, &quot;posix_memalign&quot;);
        printf(&quot;posix_memalign() allocated at %p
&quot;, sp);
        s = pthread_attr_setstack(&amp;attr, sp, stack_size);
        if (s != 0)
        handle_error_en(s, &quot;pthread_attr_setstack&quot;);
    }
    s = pthread_create(&amp;thr, attrp, &amp;thread_start, NULL);
    if (s != 0)
    handle_error_en(s, &quot;pthread_create&quot;);
    if (attrp != NULL) {
        s = pthread_attr_destroy(attrp);
        if (s != 0)
        handle_error_en(s, &quot;pthread_attr_destroy&quot;);
    }
    pause();    /* Terminates when other thread calls exit() */
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_setaffinity_np/">pthread_attr_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setdetachstate/">pthread_attr_setdetachstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setguardsize/">pthread_attr_setguardsize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setscope/">pthread_attr_setscope</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setsigmask_np/">pthread_attr_setsigmask_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstackaddr/">pthread_attr_setstackaddr</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_getattr_np/">pthread_getattr_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setattr_default_np/">pthread_setattr_default_np</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
