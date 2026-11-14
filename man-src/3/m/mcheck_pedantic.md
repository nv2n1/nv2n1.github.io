---
title: "mcheck_pedantic(3)"
name: "mcheck_pedantic"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mcheck_pedantic/"
description: "mcheck, mcheck_check_all, mcheck_pedantic, mprobe – heap consistency checking"
---

<h2 class="name">NAME</h2>
<p> mcheck, mcheck_check_all, mcheck_pedantic, mprobe &#8211; heap consistency checking </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;mcheck.h&gt;
int mcheck(void (*abortfunc)(enum mcheck_status mstatus));
int mcheck_pedantic(void (*abortfunc)(enum mcheck_status mstatus));
void mcheck_check_all(void);
enum mcheck_status mprobe(void *ptr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>mcheck</code>() function installs a set of debugging hooks for the <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) family of memory-allocation functions. These hooks cause certain consistency checks to be performed on the state of the heap. The checks can detect application errors such as freeing a block of memory more than once or corrupting the bookkeeping data structures that immediately precede a block of allocated memory. </p>
<p> To be effective, the <code>mcheck</code>() function must be called before the first call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or a related function. In cases where this is difficult to ensure, linking the program with <i>-lmcheck</i> inserts an implicit call to <code>mcheck</code>() (with a NULL argument) before the first call to a memory-allocation function. </p>
<p> The <code>mcheck_pedantic</code>() function is similar to <code>mcheck</code>(), but performs checks on all allocated blocks whenever one of the memory-allocation functions is called. This can be very slow! </p>
<p> The <code>mcheck_check_all</code>() function causes an immediate check on all allocated blocks. This call is effective only if <code>mcheck</code>() is called beforehand. </p>
<p> If the system detects an inconsistency in the heap, the caller-supplied function pointed to by <i>abortfunc</i> is invoked with a single argument, <i>mstatus</i>, that indicates what type of inconsistency was detected. If <i>abortfunc</i> is NULL, a default function prints an error message on <i>stderr</i> and calls <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3). </p>
<p> The <code>mprobe</code>() function performs a consistency check on the block of allocated memory pointed to by <i>ptr</i>. The <code>mcheck</code>() function should be called beforehand (otherwise <code>mprobe</code>() returns <code>MCHECK_DISABLED</code>). </p>
<p> The following list describes the values returned by <code>mprobe</code>() or passed as the <i>mstatus</i> argument when <i>abortfunc</i> is invoked:</p>
<dl>
<dt><code>MCHECK_DISABLED</code> (<code>mprobe</code>() only)</p>
<dd> <code>mcheck</code>() was not called before the first memory allocation function was called. Consistency checking is not possible.</p>
<dt><code>MCHECK_OK</code> (<code>mprobe</code>() only)</p>
<dd> No inconsistency detected.</p>
<dt><code>MCHECK_HEAD</code></p>
<dd> Memory preceding an allocated block was clobbered.</p>
<dt><code>MCHECK_TAIL</code></p>
<dd> Memory following an allocated block was clobbered.</p>
<dt><code>MCHECK_FREE</code></p>
<dd> A block of memory was freed twice.</dl>
<h2>RETURN VALUE</h2>
<p> <code>mcheck</code>() and <code>mcheck_pedantic</code>() return 0 on success, or -1 on error.</p>
<h2>VERSIONS</h2>
<p> The <code>mcheck_pedantic</code>() and <code>mcheck_check_all</code>() functions are available since glibc 2.2. The <code>mcheck</code>() and <code>mprobe</code>() functions are present since at least glibc 2.0</p>
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
<td> <code>mcheck</code>(), <code>mcheck_pedantic</code>(),<br />
 <code>mcheck_check_all</code>(), <code>mprobe</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:mcheck<br />
 const:malloc_hooks
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> Linking a program with <i>-lmcheck</i> and using the <code>MALLOC_CHECK_</code> environment variable (described in <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)) cause the same kinds of errors to be detected. But, using <code>MALLOC_CHECK_</code> does not require the application to be relinked.</p>
<h2>EXAMPLES</h2>
<p> The program below calls <code>mcheck</code>() with a NULL argument and then frees the same block of memory twice. The following shell session demonstrates what happens when running the program: </p>
<p> $<code> ./a.out</code> About to free </p>
<p> About to free a second time block freed twice Aborted (core dumped)</p>
<h3>Program source</h3>
<p> #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;mcheck.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*p; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mcheck(NULL)&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;mcheck()&nbsp;failed
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p&nbsp;=&nbsp;malloc(1000); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;About to free
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;
About to free a second time
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3), <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
