---
title: "pthread_setschedparam(3)"
name: "pthread_setschedparam"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_setschedparam/"
description: "pthread_setschedparam, pthread_getschedparam – set/get scheduling policy and parameters of a thread"
---

<p>pthread_setschedparam, pthread_getschedparam &#8211; set/get scheduling policy and parameters of a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_setschedparam(pthread_t thread, int policy,
                          const struct sched_param *param);
int pthread_getschedparam(pthread_t thread, int *policy,
                          struct sched_param *param);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_setschedparam</code>() function sets the scheduling policy and parameters of the thread <i>thread</i>. <i>policy</i> specifies the new scheduling policy for <i>thread</i>. The supported values for <i>policy</i>, and their semantics, are described in <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). The structure pointed to by <i>param</i> specifies the new scheduling parameters for <i>thread</i>. Scheduling parameters are maintained in the following structure: struct sched_param {<br />
    int sched_priority; /* Scheduling priority */<br />
}; As can be seen, only one scheduling parameter is supported. For details of the permitted ranges for scheduling priorities in each scheduling policy, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). The <code>pthread_getschedparam</code>() function returns the scheduling policy and parameters of the thread <i>thread</i>, in the buffers pointed to by <i>policy</i> and <i>param</i>, respectively. The returned priority value is that set by the most recent <code>pthread_setschedparam</code>(), <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), or <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) call that affected <i>thread</i>. The returned priority does not reflect any temporary priority adjustments as a result of calls to any priority inheritance or priority ceiling functions (see, for example, <code><a href="/docs/linux/man/3-pthread_mutexattr_setprioceiling/">pthread_mutexattr_setprioceiling</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_mutexattr_setprotocol/">pthread_mutexattr_setprotocol</a></code>(3)).</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number. If <code>pthread_setschedparam</code>() fails, the scheduling policy and parameters of <i>thread</i> are not changed.</p>
<h2>Errors</h2>
<p>Both of these functions can fail with the following error:</p>
<dl>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
<p> <code>pthread_setschedparam</code>() may additionally fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>policy</i> is not a recognized policy, or <i>param</i> does not make sense for the <i>policy</i>.</p>
<dt><code>EPERM</code></p>
<dd>The caller does not have appropriate privileges to set the specified scheduling policy and parameters.</dl>
<p> POSIX.1 also documents an <code>ENOTSUP</code> (&quot;attempt was made to set the policy or scheduling parameters to an unsupported value&quot;) error for <code>pthread_setschedparam</code>().</p>
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
<td> <code>pthread_setschedparam</code>(), <code>pthread_getschedparam</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>For a description of the permissions required to, and the effect of, changing a thread&#8217;s scheduling policy and priority, and details of the permitted ranges for priorities in each scheduling policy, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of <code>pthread_setschedparam</code>() and <code>pthread_getschedparam</code>(), as well as the use of a number of other scheduling-related pthreads functions. In the following run, the main thread sets its scheduling policy to <code>SCHED_FIFO</code> with a priority of 10, and initializes a thread attributes object with a scheduling policy attribute of <code>SCHED_RR</code> and a scheduling priority attribute of 20. The program then sets (using <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3)) the inherit scheduler attribute of the thread attributes object to <code>PTHREAD_EXPLICIT_SCHED</code>, meaning that threads created using this attributes object should take their scheduling attributes from the thread attributes object. The program then creates a thread using the thread attributes object, and that thread displays its scheduling policy and priority. $ <code>su</code> # Need privilege to set real-time scheduling policies Password: # <code>./a.out -mf10 -ar20 -i e</code> Scheduler settings of main thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_FIFO, priority=10 Scheduler settings in &#8216;attr&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_RR, priority=20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inheritsched is EXPLICIT Scheduler attributes of new thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_RR, priority=20 In the above output, one can see that the scheduling policy and priority were taken from the values specified in the thread attributes object. The next run is the same as the previous, except that the inherit scheduler attribute is set to <code>PTHREAD_INHERIT_SCHED</code>, meaning that threads created using the thread attributes object should ignore the scheduling attributes specified in the attributes object and instead take their scheduling attributes from the creating thread. # <code>./a.out -mf10 -ar20 -i i</code> Scheduler settings of main thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_FIFO, priority=10 Scheduler settings in &#8216;attr&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_RR, priority=20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inheritsched is INHERIT Scheduler attributes of new thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;policy=SCHED_FIFO, priority=10 In the above output, one can see that the scheduling policy and priority were taken from the creating thread, rather than the thread attributes object. Note that if we had omitted the <i>-i i</i> option, the output would have been the same, since <code>PTHREAD_INHERIT_SCHED</code> is the default for the inherit scheduler attribute.</p>
<h3>Program source</h3>
<p>/* pthreads_sched_test.c */ </p>
<pre><code>#include &lt;errno.h&gt;
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
usage(char *prog_name, char *msg)
{
    if (msg != NULL)
        fputs(msg, stderr);
    fprintf(stderr, &quot;Usage: %s [options]
&quot;, prog_name);
    fprintf(stderr, &quot;Options are:
&quot;);
#define fpe(msg) fprintf(stderr, &quot;	%s&quot;, msg); /* Shorter */
    fpe(&quot;-a&lt;policy&gt;&lt;prio&gt; Set scheduling policy and priority in
&quot;);
    fpe(&quot;                 thread attributes object
&quot;);
    fpe(&quot;                 &lt;policy&gt; can be
&quot;);
    fpe(&quot;                     f  SCHED_FIFO
&quot;);
    fpe(&quot;                     r  SCHED_RR
&quot;);
    fpe(&quot;                     o  SCHED_OTHER
&quot;);
    fpe(&quot;-A               Use default thread attributes object
&quot;);
    fpe(&quot;-i {e|i}         Set inherit scheduler attribute to
&quot;);
    fpe(&quot;                 'explicit' or 'inherit'
&quot;);
    fpe(&quot;-m&lt;policy&gt;&lt;prio&gt; Set scheduling policy and priority on
&quot;);
    fpe(&quot;                 main thread before pthread_create() call
&quot;);
    exit(EXIT_FAILURE);
}
static int
get_policy(char p, int *policy)
{
    switch (p) {
    case 'f':
        *policy = SCHED_FIFO;
        return 1;
    case 'r':
        *policy = SCHED_RR;
        return 1;
    case 'o':
        *policy = SCHED_OTHER;
        return 1;
    default:
        return 0;
    }
}
static void
display_sched_attr(int policy, struct sched_param *param)
{
    printf(&quot;    policy=%s, priority=%d
&quot;,
           (policy == SCHED_FIFO) ? &quot;SCHED_FIFO&quot; : (policy == SCHED_RR)  ? &quot;SCHED_RR&quot;
                                               : (policy == SCHED_OTHER) ? &quot;SCHED_OTHER&quot;
                                                                         : &quot;???&quot;,
           param-&gt;sched_priority);
}
static void
display_thread_sched_attr(char *msg)
{
    int policy, s;
    struct sched_param param;
    s = pthread_getschedparam(pthread_self(), &amp;policy, &amp;param);
    if (s != 0)
        handle_error_en(s, &quot;pthread_getschedparam&quot;);
    printf(&quot;%s
&quot;, msg);
    display_sched_attr(policy, &amp;param);
}
static void *
thread_start(void *arg)
{
    display_thread_sched_attr(&quot;Scheduler attributes of new thread&quot;);
    return NULL;
}
int main(int argc, char *argv[])
{
    int s, opt, inheritsched, use_null_attrib, policy;
    pthread_t thread;
    pthread_attr_t attr;
    pthread_attr_t *attrp;
    char *attr_sched_str, *main_sched_str, *inheritsched_str;
    struct sched_param param;
    /* Process command-line options */
    use_null_attrib = 0;
    attr_sched_str = NULL;
    main_sched_str = NULL;
    inheritsched_str = NULL;
    while ((opt = getopt(argc, argv, &quot;a:Ai:m:&quot;)) != -1) {
        switch (opt) {
        case 'a':
            attr_sched_str = optarg;
            break;
        case 'A':
            use_null_attrib = 1;
            break;
        case 'i':
            inheritsched_str = optarg;
            break;
        case 'm':
            main_sched_str = optarg;
            break;
        default:
            usage(argv[0], &quot;Unrecognized option
&quot;);
        }
    }
    if (use_null_attrib &amp;&amp;
        (inheritsched_str != NULL || attr_sched_str != NULL))
        usage(argv[0], &quot;Can't specify -A with -i or -a
&quot;);
    /* Optionally set scheduling attributes of main thread,
           and display the attributes */
    if (main_sched_str != NULL) {
        if (!get_policy(main_sched_str[0], &amp;policy))
            usage(argv[0], &quot;Bad policy for main thread (-m)
&quot;);
        param.sched_priority = strtol(&amp;main_sched_str[1], NULL, 0);
        s = pthread_setschedparam(pthread_self(), policy, &amp;param);
        if (s != 0)
            handle_error_en(s, &quot;pthread_setschedparam&quot;);
    }
    display_thread_sched_attr(&quot;Scheduler settings of main thread&quot;);
    printf(&quot;
&quot;);
    /* Initialize thread attributes object according to options */
    attrp = NULL;
    if (!use_null_attrib) {
        s = pthread_attr_init(&amp;attr);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_init&quot;);
        attrp = &amp;attr;
    }
    if (inheritsched_str != NULL) {
        if (inheritsched_str[0] == 'e')
            inheritsched = PTHREAD_EXPLICIT_SCHED;
        else if (inheritsched_str[0] == 'i')
            inheritsched = PTHREAD_INHERIT_SCHED;
        else
            usage(argv[0], &quot;Value for -i must be 'e' or 'i'
&quot;);
        s = pthread_attr_setinheritsched(&amp;attr, inheritsched);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_setinheritsched&quot;);
    }
    if (attr_sched_str != NULL) {
        if (!get_policy(attr_sched_str[0], &amp;policy))
            usage(argv[0],
                  &quot;Bad policy for 'attr' (-a)
&quot;);
        param.sched_priority = strtol(&amp;attr_sched_str[1], NULL, 0);
        s = pthread_attr_setschedpolicy(&amp;attr, policy);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_setschedpolicy&quot;);
        s = pthread_attr_setschedparam(&amp;attr, &amp;param);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_setschedparam&quot;);
    }
    /* If we initialized a thread attributes object, display
           the scheduling attributes that were set in the object */
    if (attrp != NULL) {
        s = pthread_attr_getschedparam(&amp;attr, &amp;param);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_getschedparam&quot;);
        s = pthread_attr_getschedpolicy(&amp;attr, &amp;policy);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_getschedpolicy&quot;);
        printf(&quot;Scheduler settings in 'attr'
&quot;);
        display_sched_attr(policy, &amp;param);
        s = pthread_attr_getinheritsched(&amp;attr, &amp;inheritsched);
        printf(&quot;    inheritsched is %s
&quot;,
               (inheritsched == PTHREAD_INHERIT_SCHED) ? &quot;INHERIT&quot; : (inheritsched == PTHREAD_EXPLICIT_SCHED) ? &quot;EXPLICIT&quot;
                                                                                                              : &quot;???&quot;);
        printf(&quot;
&quot;);
    }
    /* Create a thread that will display its scheduling attributes */
    s = pthread_create(&amp;thread, attrp, &amp;thread_start, NULL);
    if (s != 0)
        handle_error_en(s, &quot;pthread_create&quot;);
    /* Destroy unneeded thread attributes object */
    if (!use_null_attrib) {
        s = pthread_attr_destroy(&amp;attr);
        if (s != 0)
            handle_error_en(s, &quot;pthread_attr_destroy&quot;);
    }
    s = pthread_join(thread, NULL);
    if (s != 0)
        handle_error_en(s, &quot;pthread_join&quot;);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
