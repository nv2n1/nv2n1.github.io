---
title: "atexit(3)"
name: "atexit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atexit/"
description: "atexit – register a function to be called at normal process termination"
---

<h2 class="name">NAME</h2>
<p> atexit &#8211; register a function to be called at normal process termination </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int atexit(void (*function)(void));
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>atexit</code>() function registers the given <i>function</i> to be called at normal process termination, either via <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) or via return from the program&#8217;s <i>main</i>(). Functions so registered are called in the reverse order of their registration; no arguments are passed. </p>
<p> The same function may be registered multiple times: it is called once for each registration. </p>
<p> POSIX.1 requires that an implementation allow at least <code>ATEXIT_MAX</code> (32) such functions to be registered. The actual limit supported by an implementation can be obtained using <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3). </p>
<p> When a child process is created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), it inherits copies of its parent&#8217;s registrations. Upon a successful call to one of the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) functions, all registrations are removed.</p>
<h2>RETURN VALUE</h2>
<p> The <code>atexit</code>() function returns the value 0 if successful; otherwise it returns a nonzero value.</p>
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
<td> <code>atexit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> Functions registered using <code>atexit</code>() (and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3)) are not called if a process terminates abnormally because of the delivery of a signal. </p>
<p> If one of the registered functions calls <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), then any remaining functions are not invoked, and the other process termination steps performed by <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) are not performed. </p>
<p> POSIX.1 says that the result of calling <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) more than once (i.e., calling <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) within a function registered using <code>atexit</code>()) is undefined. On some systems (but not Linux), this can result in an infinite recursion; portable programs should not invoke <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) inside a function registered using <code>atexit</code>(). </p>
<p> The <code>atexit</code>() and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3) functions register functions on the same list: at normal process termination, the registered functions are invoked in reverse order of their registration by these two functions. </p>
<p> According to POSIX.1, the result is undefined if <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) is used to terminate execution of one of the functions registered using <code>atexit</code>().</p>
<h3>Linux notes</h3>
<p> Since glibc 2.2.3, <code>atexit</code>() (and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3)) can be used within a shared library to establish functions that are called when the shared library is unloaded.</p>
<h2>EXAMPLES</h2>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> void bye(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;That was all, folks
&quot;); } </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long a;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;=&nbsp;sysconf(_SC_ATEXIT_MAX);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;ATEXIT_MAX&nbsp;=&nbsp;%ld
&quot;, a); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i&nbsp;=&nbsp;atexit(bye);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(i&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;cannot set exit function
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
