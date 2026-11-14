---
title: "backtrace_symbols(3)"
name: "backtrace_symbols"
section: "3"
letter: "b"
url: "/docs/linux/man/3-backtrace_symbols/"
description: "backtrace, backtrace_symbols, backtrace_symbols_fd – support for application self-debugging"
---

<h2 class="name">NAME</h2>
<p> backtrace, backtrace_symbols, backtrace_symbols_fd &#8211; support for application self-debugging </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;execinfo.h&gt;</code> </p>
<p> <code>int backtrace(void</code> <code>**</code><i>buffer</i><code>,</code> <code>int</code> <i>size</i><code>);</code> </p>
<p> <code>char **backtrace_symbols(void *const</code> <code>*</code><i>buffer</i><code>,</code> <code>int</code> <i>size</i><code>);</code> </p>
<p> <code>void backtrace_symbols_fd(void *const</code> <code>*</code><i>buffer</i><code>,</code> <code>int</code> <i>size</i><code>,</code> <code>int</code> <i>fd</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>backtrace</code>() returns a backtrace for the calling program, in the array pointed to by <i>buffer</i>. A backtrace is the series of currently active function calls for the program. Each item in the array pointed to by <i>buffer</i> is of type <i>void&nbsp;*</i>, and is the return address from the corresponding stack frame. The <i>size</i> argument specifies the maximum number of addresses that can be stored in <i>buffer</i>. If the backtrace is larger than <i>size</i>, then the addresses corresponding to the <i>size</i> most recent function calls are returned; to obtain the complete backtrace, make sure that <i>buffer</i> and <i>size</i> are large enough. </p>
<p> Given the set of addresses returned by <code>backtrace</code>() in <i>buffer</i>, <code>backtrace_symbols</code>() translates the addresses into an array of strings that describe the addresses symbolically. The <i>size</i> argument specifies the number of addresses in <i>buffer</i>. The symbolic representation of each address consists of the function name (if this can be determined), a hexadecimal offset into the function, and the actual return address (in hexadecimal). The address of the array of string pointers is returned as the function result of <code>backtrace_symbols</code>(). This array is <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)ed by <code>backtrace_symbols</code>(), and must be freed by the caller. (The strings pointed to by the array of pointers need not and should not be freed.) </p>
<p> <code>backtrace_symbols_fd</code>() takes the same <i>buffer</i> and <i>size</i> arguments as <code>backtrace_symbols</code>(), but instead of returning an array of strings to the caller, it writes the strings, one per line, to the file descriptor <i>fd</i>. <code>backtrace_symbols_fd</code>() does not call <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and so can be employed in situations where the latter function might fail, but see NOTES.</p>
<h2>RETURN VALUE</h2>
<p> <code>backtrace</code>() returns the number of addresses returned in <i>buffer</i>, which is not greater than <i>size</i>. If the return value is less than <i>size</i>, then the full backtrace was stored; if it is equal to <i>size</i>, then it may have been truncated, in which case the addresses of the oldest stack frames are not returned. </p>
<p> On success, <code>backtrace_symbols</code>() returns a pointer to the array <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)ed by the call; on error, NULL is returned.</p>
<h2>VERSIONS</h2>
<p> <code>backtrace</code>(), <code>backtrace_symbols</code>(), and <code>backtrace_symbols_fd</code>() are provided in glibc since version 2.1.</p>
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
<td> <code>backtrace</code>(),<br />
 <code>backtrace_symbols</code>(),<br />
 <code>backtrace_symbols_fd</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> These functions make some assumptions about how a function&#8217;s return address is stored on the stack. Note the following:</p>
<dl>
<dt>*</p>
<dd> Omission of the frame pointers (as implied by any of <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1)&#8217;s nonzero optimization levels) may cause these assumptions to be violated.</p>
<dt>*</p>
<dd> Inlined functions do not have stack frames.</p>
<dt>*</p>
<dd> Tail-call optimization causes one stack frame to replace another.</p>
<dt>*</p>
<dd> <code>backtrace</code>() and <code>backtrace_symbols_fd</code>() don&#8217;t call <code>malloc</code>() explicitly, but they are part of <i>libgcc</i>, which gets loaded dynamically when first used. Dynamic loading usually triggers a call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). If you need certain calls to these two functions to not allocate memory (in signal handlers, for example), you need to make sure <i>libgcc</i> is loaded beforehand.</dl>
<p> The symbol names may be unavailable without the use of special linker options. For systems using the GNU linker, it is necessary to use the <i>-rdynamic</i> linker option. Note that names of &quot;static&quot; functions are not exposed, and won&#8217;t be available in the backtrace.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>backtrace</code>() and <code>backtrace_symbols</code>(). The following shell session shows what we might see when running the program: </p>
<p> $<code> cc -rdynamic prog.c -o prog</code> $<code> ./prog 3</code> backtrace() returned 8 addresses ./prog(myfunc3+0x5c) [0x80487f0] ./prog [0x8048871] ./prog(myfunc+0x21) [0x8048894] ./prog(myfunc+0x1a) [0x804888d] ./prog(myfunc+0x1a) [0x804888d] ./prog(main+0x65) [0x80488fb] /lib/libc.so.6(__libc_start_main+0xdc) [0xb7e38f9c] ./prog [0x8048711]</p>
<h3>Program source</h3>
<p> #include &lt;execinfo.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define BT_BUF_SIZE 100 </p>
<p> void myfunc3(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nptrs;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*buffer[BT_BUF_SIZE];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;**strings; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nptrs&nbsp;=&nbsp;backtrace(buffer, BT_BUF_SIZE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;backtrace()&nbsp;returned&nbsp;%d addresses
&quot;, nptrs); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The call backtrace_symbols_fd(buffer, nptrs, STDOUT_FILENO)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;would produce similar output to the following:&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strings&nbsp;=&nbsp;backtrace_symbols(buffer, nptrs);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(strings&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;backtrace_symbols&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nptrs;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, strings[j]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(strings); } </p>
<p> static void /* &quot;static&quot; means don&#8217;t export the symbol&#8230; */ myfunc2(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;myfunc3(); } </p>
<p> void myfunc(int ncalls) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ncalls&nbsp;&gt;&nbsp;1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;myfunc(ncalls &#8211; 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;myfunc2(); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s num-calls
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;myfunc(atoi(argv[1]));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-addr2line/">addr2line</a></code>(1), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
