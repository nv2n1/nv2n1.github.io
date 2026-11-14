---
title: "duplocale(3)"
name: "duplocale"
section: "3"
letter: "d"
url: "/docs/linux/man/3-duplocale/"
description: "duplocale – duplicate a locale object"
---

<h2 class="name">NAME</h2>
<p> duplocale &#8211; duplicate a locale object </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;locale.h&gt;
locale_t duplocale(locale_t locobj);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>duplocale</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>duplocale</code>() function creates a duplicate of the locale object referred to by <i>locobj</i>. </p>
<p> If <i>locobj</i> is <code>LC_GLOBAL_LOCALE</code>, <code>duplocale</code>() creates a locale object containing a copy of the global locale determined by <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>duplocale</code>() returns a handle for the new locale object. On error, it returns <i>(locale_t)&nbsp;0,</i> and sets <i>errno</i> to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to create the duplicate locale object.</dl>
<h2>VERSIONS</h2>
<p> The <code>duplocale</code>() function first appeared in version 2.3 of the GNU C library.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Duplicating a locale can serve the following purposes:</p>
<dl>
<dt>*</p>
<dd> To create a copy of a locale object in which one of more categories are to be modified (using <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3)).</p>
<dt>*</p>
<dd> To obtain a handle for the current locale which can used in other functions that employ a locale handle, such as <code><a href="/docs/linux/man/3-toupper_l/">toupper_l</a></code>(3). This is done by applying <code>duplocale</code>() to the value returned by the following call:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loc&nbsp;=&nbsp;uselocale((locale_t)&nbsp;0);</p>
<dt>
<dd> This technique is necessary, because the above <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3) call may return the value <code>LC_GLOBAL_LOCALE</code>, which results in undefined behavior if passed to functions such as <code><a href="/docs/linux/man/3-toupper_l/">toupper_l</a></code>(3). Calling <code>duplocale</code>() can be used to ensure that the <code>LC_GLOBAL_LOCALE</code> value is converted into a usable locale object. See EXAMPLES, below.</dl>
<p> Each locale object created by <code>duplocale</code>() should be deallocated using <code><a href="/docs/linux/man/3-freelocale/">freelocale</a></code>(3).</p>
<h2>EXAMPLES</h2>
<p> The program below uses <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3) and <code>duplocale</code>() to obtain a handle for the current locale which is then passed to <code><a href="/docs/linux/man/3-toupper_l/">toupper_l</a></code>(3). The program takes one command-line argument, a string of characters that is converted to uppercase and displayed on standard output. An example of its use is the following: </p>
<p> $ <code>./a.out abc</code> ABC</p>
<h3>Program source</h3>
<p> #define _XOPEN_SOURCE 700 #include &lt;ctype.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;locale.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locale_t loc, nloc; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s string
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;This sequence is necessary, because uselocale()&nbsp;might return<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the value LC_GLOBAL_LOCALE, which can&#8217;t be passed as an<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argument to toupper_l()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loc&nbsp;=&nbsp;uselocale((locale_t)&nbsp;0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(loc&nbsp;==&nbsp;(locale_t)&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;uselocale&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nloc&nbsp;=&nbsp;duplocale(loc);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nloc&nbsp;==&nbsp;(locale_t)&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;duplocale&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(char&nbsp;*p&nbsp;=&nbsp;argv[1];&nbsp;*p;&nbsp;p++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;putchar(toupper_l(*p, nloc)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;freelocale(nloc); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-freelocale/">freelocale</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
