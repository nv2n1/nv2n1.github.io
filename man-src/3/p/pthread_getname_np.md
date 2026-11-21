---
title: "pthread_getname_np(3)"
name: "pthread_getname_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_getname_np/"
description: "pthread_setname_np, pthread_getname_np – set/get the name of a thread"
---

<p>pthread_setname_np, pthread_getname_np &#8211; set/get the name of a thread</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;
int pthread_setname_np(pthread_t thread, const char *name);
int pthread_getname_np(pthread_t thread,
                       char *name, size_t len);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>By default, all the threads created using <code>pthread_create</code>() inherit the program name. The <code>pthread_setname_np</code>() function can be used to set a unique name for a thread, which can be useful for debugging multithreaded applications. The thread name is a meaningful C language string, whose length is restricted to 16 characters, including the terminating null byte (&#8216;\0&#8217;). The <i>thread</i> argument specifies the thread whose name is to be changed; <i>name</i> specifies the new name. </p>
<p> The <code>pthread_getname_np</code>() function can be used to retrieve the name of the thread. The <i>thread</i> argument specifies the thread whose name is to be retrieved. The buffer <i>name</i> is used to return the thread name; <i>len</i> specifies the number of bytes available in <i>name</i>. The buffer specified by <i>name</i> should be at least 16 characters in length. The returned thread name in the output buffer will be null terminated.  </p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return 0; on error, they return a nonzero error number.  </p>
<h2>ERRORS</h2>
<p> The <code>pthread_setname_np</code>() function can fail with the following error: </p>
<dl>
<dt><code>ERANGE</code></dt>
<dd> <p> The length of the string specified pointed to by <i>name</i> exceeds the allowed limit. </p>
 </dd></dl>
<p> The <code>pthread_getname_np</code>() function can fail with the following error: </p>
<dl>
<dt><code>ERANGE</code></dt>
<dd> <p> The buffer specified by <i>name</i> and <i>len</i> is too small to hold the thread name. </p>
 </dd></dl>
<p> If either of these functions fails to open <i>/proc/self/task/[tid]/comm</i>, then the call may fail with one of the errors described in <code><a href="/docs/linux/man/2-open/">open</a></code>(2).  </p>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.12.  </p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_setname_np</code>(), <code>pthread_getname_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard GNU extensions; hence the suffix &quot;_np&quot; (nonportable) in the names.  </p>
<h2>NOTES</h2>
<p> <code>pthread_setname_np</code>() internally writes to the thread-specific <i>comm</i> file under the <i>/proc</i> filesystem: <i>/proc/self/task/[tid]/comm</i>. <code>pthread_getname_np</code>() retrieves it from the same location.  </p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>pthread_setname_np</code>() and <code>pthread_getname_np</code>(). </p>
<p> The following shell session shows a sample run of the program: </p>
<p> $<code> ./a.out</code> Created a thread. Default name is: a.out The thread name after setting it is THREADFOO. <code>haZ</code> # Suspend the program [1]+ Stopped ./a.out $ <code>ps H -C a.out -o &#8216;pid tid cmd comm&#8217;</code> <br />
&nbsp;<wbr>&nbsp;PID&nbsp;<wbr>&nbsp;<wbr>&nbsp;TID CMD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;COMMAND <br />
&nbsp;5990&nbsp;<wbr>&nbsp;5990 ./a.out&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a.out <br />
&nbsp;5990&nbsp;<wbr>&nbsp;5991 ./a.out&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;THREADFOO $ <code>cat /proc/5990/task/5990/comm</code> a.out $ <code>cat /proc/5990/task/5991/comm</code> THREADFOO  </p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;pthread.h&gt; #include &lt;stdio.h&gt; #include &lt;string.h&gt; #include &lt;unistd.h&gt; #include &lt;errno.h&gt; #include &lt;stdlib.h&gt; </p>
<p> #define NAMELEN 16 </p>
<p> #define errExitEN(en, msg) \ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;errno&nbsp;=&nbsp;en;&nbsp;perror(msg);&nbsp;\ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void * threadfunc(void *parm) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/5-sleep/">sleep</a>(5);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;//&nbsp;allow main program to set the thread name <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return NULL; } </p>
<p> int main(int argc, char **argv) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pthread_t thread; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int rc; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char thread_name[NAMELEN]; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pthread_create(&amp;thread, NULL, threadfunc, NULL); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExitEN(rc,&nbsp;&quot;pthread_create&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pthread_getname_np(thread, thread_name, NAMELEN); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExitEN(rc,&nbsp;&quot;pthread_getname_np&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Created a thread. Default name is:&nbsp;%s\n&quot;, thread_name); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pthread_setname_np(thread,&nbsp;(argc&nbsp;&gt;&nbsp;1)&nbsp;?&nbsp;argv[1]&nbsp;:&nbsp;&quot;THREADFOO&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExitEN(rc,&nbsp;&quot;pthread_setname_np&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-sleep/">sleep</a>(2); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pthread_getname_np(thread, thread_name, <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(argc&nbsp;&gt;&nbsp;2)&nbsp;?&nbsp;atoi(argv[1])&nbsp;: NAMELEN); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExitEN(rc,&nbsp;&quot;pthread_getname_np&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;The thread name after setting it is&nbsp;%s.\n&quot;, thread_name); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pthread_join(thread, NULL); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;0) <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExitEN(rc,&nbsp;&quot;pthread_join&quot;); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Done\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
