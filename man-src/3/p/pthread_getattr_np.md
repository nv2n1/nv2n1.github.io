---
title: "pthread_getattr_np(3)"
name: "pthread_getattr_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_getattr_np/"
description: "pthread_getattr_np – get attributes of created thread"
---

<p>pthread_getattr_np &#8211; get attributes of created thread</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;

int pthread_getattr_np(pthread_t thread, pthread_attr_t *attr);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_getattr_np</code>() function initializes the thread attributes object referred to by <i>attr</i> so that it contains actual attribute values describing the running thread <i>thread</i>. </p>
<p> The returned attribute values may differ from the corresponding attribute values passed in the <i>attr</i> object that was used to create the thread using <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3). In particular, the following attributes may differ:</p>
<dl>
<dt>*</p>
<dd>the detach state, since a joinable thread may have detached itself after creation;</p>
<dt>*</p>
<dd>the stack size, which the implementation may align to a suitable boundary.</p>
<dt>*</p>
<dd>and the guard size, which the implementation may round upward to a multiple of the page size, or ignore (i.e., treat as 0), if the application is allocating its own stack.</dl>
<p> Furthermore, if the stack address attribute was not set in the thread attributes object used to create the thread, then the returned thread attributes object will report the actual stack address that the implementation selected for the thread. </p>
<p> When the thread attributes object returned by <code>pthread_getattr_np</code>() is no longer required, it should be destroyed using <code><a href="/docs/linux/man/3-pthread_attr_destroy/">pthread_attr_destroy</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, this function returns 0; on error, it returns a nonzero error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory.</dl>
<p> In addition, if <i>thread</i> refers to the main thread, then <code>pthread_getattr_np</code>() can fail because of errors from various underlying calls: <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), if <i>/proc/self/maps</i> can&#8217;t be opened; and <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), if the <code>RLIMIT_STACK</code> resource limit is not supported.</p>
<h2>Versions</h2>
<p>This function is available in glibc since version 2.2.3.</p>
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
<td> <code>pthread_getattr_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a nonstandard GNU extension; hence the suffix &quot;_np&quot; (nonportable) in the name.</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of <code>pthread_getattr_np</code>(). The program creates a thread that then uses <code>pthread_getattr_np</code>() to retrieve and display its guard size, stack address, and stack size attributes. Command-line arguments can be used to set these attributes to values other than the default when creating the thread. The shell sessions below demonstrate the use of the program. In the first run, on an x86-32 system, a thread is created using default attributes: $<code> ulimit -s</code> # No stack limit ==&gt; default stack size is 2 MB unlimited $<code> ./a.out</code> Attributes of created thread:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Guard size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4096 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x40196000&nbsp;(EOS&nbsp;=&nbsp;0x40397000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x201000&nbsp;(2101248)&nbsp;bytes In the following run, we see that if a guard size is specified, it is rounded up to the next multiple of the system page size (4096 bytes on x86-32): $<code> ./a.out -g 4097</code> Thread attributes object after initializations:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Guard size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4097 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;(nil)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x0&nbsp;(0)&nbsp;bytes Attributes of created thread:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Guard size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;8192 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x40196000&nbsp;(EOS&nbsp;=&nbsp;0x40397000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x201000&nbsp;(2101248)&nbsp;bytes In the last run, the program manually allocates a stack for the thread. In this case, the guard size attribute is ignored. $<code> ./a.out -g 4096 -s 0x8000 -a</code> Allocated thread stack at 0x804d000 Thread attributes object after initializations:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Guard size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;4096 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x804d000&nbsp;(EOS&nbsp;=&nbsp;0x8055000)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Stack size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;0x8000&nbsp;(32768)&nbsp;bytes </p>
<pre><code>Attributes of created thread : Guard size = 0 bytes
                                   Stack address = 0x804d000(EOS = 0x8055000)
                                       Stack size = 0x8000(32768)bytes

                                           Program source

#define _GNU_SOURCE /* To get pthread_getattr_np() declaration */
#include &lt;errno.h&gt;
#include &lt;pthread.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#define handle_error_en(en, msg) \
    do {                         \
        errno = en;              \
        perror(msg);             \
        exit(EXIT_FAILURE);      \
    } while (0)
                               static void
                               display_stack_related_attributes(pthread_attr_t * attr, char *prefix)
{
    int s;
    size_t stack_size, guard_size;
    void *stack_addr;
    s = pthread_attr_getguardsize(attr, &amp;guard_size);
    if (s != 0)
        handle_error_en(s, &quot;pthread_attr_getguardsize&quot;);
    printf(&quot;%sGuard size          = %zu bytes
&quot;, prefix, guard_size);
    s = pthread_attr_getstack(attr, &amp;stack_addr, &amp;stack_size);
    if (s != 0)
        handle_error_en(s, &quot;pthread_attr_getstack&quot;);
    printf(&quot;%sStack address       = %p&quot;, prefix, stack_addr);
    if (stack_size &gt; 0)
        printf(&quot; (EOS = %p)&quot;, (char *)stack_addr + stack_size);
    printf(&quot;
&quot;);
    printf(&quot;%sStack size          = %#zx (%zu) bytes
&quot;,
           prefix, stack_size, stack_size);
}
static void
display_thread_attributes(pthread_t thread, char *prefix)
{
    int s;
    pthread_attr_t attr;
    s = pthread_getattr_np(thread, &amp;attr);
    if (s != 0)
        handle_error_en(s, &quot;pthread_getattr_np&quot;);
    display_stack_related_attributes(&amp;attr, prefix);
    s = pthread_attr_destroy(&amp;attr);
    if (s != 0)
        handle_error_en(s, &quot;pthread_attr_destroy&quot;);
}
static void * /* Start function for thread we create */
thread_start(void *arg)
{
    printf(&quot;Attributes of created thread:
&quot;);
    display_thread_attributes(pthread_self(), &quot;	&quot;);
    exit(EXIT_SUCCESS); /* Terminate all threads */
}
static void
usage(char *pname, char *msg)
{
    if (msg != NULL)
        fputs(msg, stderr);
    fprintf(stderr, &quot;Usage: %s [-s stack-size [-a]]&quot;
                    &quot; [-g guard-size]
&quot;,
            pname);
    fprintf(stderr, &quot;		-a means program should allocate stack
&quot;);
    exit(EXIT_FAILURE);
}
static pthread_attr_t * /* Get thread attributes from command line */
get_thread_attributes_from_cl(int argc, char *argv[],
                              pthread_attr_t *attrp)
{
    int s, opt, allocate_stack;
    size_t stack_size, guard_size;
    void *stack_addr;
    pthread_attr_t *ret_attrp = NULL; /* Set to attrp if we initialize
                                         a thread attributes object */
    allocate_stack = 0;
    stack_size = -1;
    guard_size = -1;
    while ((opt = getopt(argc, argv, &quot;ag:s:&quot;)) != -1) {
        switch (opt) {
        case 'a':
            allocate_stack = 1;
            break;
        case 'g':
            guard_size = strtoul(optarg, NULL, 0);
            break;
        case 's':
            stack_size = strtoul(optarg, NULL, 0);
            break;
        default:
            usage(argv[0], NULL);
        }
    }
    if (allocate_stack &amp;&amp; stack_size == -1)
        usage(argv[0], &quot;Specifying -a without -s makes no sense
&quot;);
    if (argc &gt; optind)
        usage(argv[0], &quot;Extraneous command-line arguments
&quot;);
    if (stack_size &gt;= 0 || guard_size &gt; 0) {
        ret_attrp = attrp;
        s = pthread_attr_init(attrp);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_init&quot;);
    }
    if (stack_size &gt;= 0) {
        if (!allocate_stack) {
            s = pthread_attr_setstacksize(attrp, stack_size);
            if (s != 0)
                handle_error_en(s, &quot;pthread_attr_setstacksize&quot;);
        } else {
            s = posix_memalign(&amp;stack_addr, sysconf(_SC_PAGESIZE),
                               stack_size);
            if (s != 0)
                handle_error_en(s, &quot;posix_memalign&quot;);
            printf(&quot;Allocated thread stack at %p

&quot;, stack_addr);
            s = pthread_attr_setstack(attrp, stack_addr, stack_size);
            if (s != 0)
                handle_error_en(s, &quot;pthread_attr_setstacksize&quot;);
        }
    }
    if (guard_size &gt;= 0) {
        s = pthread_attr_setguardsize(attrp, guard_size);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_setstacksize&quot;);
    }
    return ret_attrp;
}
int main(int argc, char *argv[])
{
    int s;
    pthread_t thr;
    pthread_attr_t attr;
    pthread_attr_t *attrp = NULL; /* Set to &amp;attr if we initialize
                                     a thread attributes object */
    attrp = get_thread_attributes_from_cl(argc, argv, &amp;attr);
    if (attrp != NULL) {
        printf(&quot;Thread attributes object after initializations:
&quot;);
        display_stack_related_attributes(attrp, &quot;	&quot;);
        printf(&quot;
&quot;);
    }
    s = pthread_create(&amp;thr, attrp, &amp;thread_start, NULL);
    if (s != 0)
        handle_error_en(s, &quot;pthread_create&quot;);
    if (attrp != NULL) {
        s = pthread_attr_destroy(attrp);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_destroy&quot;);
    }
    pause(); /* Terminates when other thread calls exit() */
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_getaffinity_np/">pthread_attr_getaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getdetachstate/">pthread_attr_getdetachstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getguardsize/">pthread_attr_getguardsize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getinheritsched/">pthread_attr_getinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getschedparam/">pthread_attr_getschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getschedpolicy/">pthread_attr_getschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getscope/">pthread_attr_getscope</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstack/">pthread_attr_getstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstackaddr/">pthread_attr_getstackaddr</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_getstacksize/">pthread_attr_getstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
