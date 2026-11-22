---
title: "strtok_r(3)"
name: "strtok_r"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtok_r/"
description: "strtok, strtok_r – extract tokens from strings"
---

<p>strtok, strtok_r &#8211; extract tokens from strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strtok(char *str, const char *delim);
char *strtok_r(char *str, const char *delim, char **saveptr);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strtok_r</code>(): _POSIX_C_SOURCE<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>strtok</code>() function breaks a string into a sequence of zero or more nonempty tokens. On the first call to <code>strtok</code>(), the string to be parsed should be specified in <i>str</i>. In each subsequent call that should parse the same string, <i>str</i> must be NULL. </p>
<p> The <i>delim</i> argument specifies a set of bytes that delimit the tokens in the parsed string. The caller may specify different strings in <i>delim</i> in successive calls that parse the same string. </p>
<p> Each call to <code>strtok</code>() returns a pointer to a null-terminated string containing the next token. This string does not include the delimiting byte. If no more tokens are found, <code>strtok</code>() returns NULL. </p>
<p> A sequence of calls to <code>strtok</code>() that operate on the same string maintains a pointer that determines the point from which to start searching for the next token. The first call to <code>strtok</code>() sets this pointer to point to the first byte of the string. The start of the next token is determined by scanning forward for the next nondelimiter byte in <i>str</i>. If such a byte is found, it is taken as the start of the next token. If no such byte is found, then there are no more tokens, and <code>strtok</code>() returns NULL. (A string that is empty or that contains only delimiters will thus cause <code>strtok</code>() to return NULL on the first call.) </p>
<p> The end of each token is found by scanning forward until either the next delimiter byte is found or until the terminating null byte (&#8216;\0&#8217;) is encountered. If a delimiter byte is found, it is overwritten with a null byte to terminate the current token, and <code>strtok</code>() saves a pointer to the following byte; that pointer will be used as the starting point when searching for the next token. In this case, <code>strtok</code>() returns a pointer to the start of the found token. </p>
<p> From the above description, it follows that a sequence of two or more contiguous delimiter bytes in the parsed string is considered to be a single delimiter, and that delimiter bytes at the start or end of the string are ignored. Put another way: the tokens returned by <code>strtok</code>() are always nonempty strings. Thus, for example, given the string &quot;<i>aaa;;bbb,</i>&quot;, successive calls to <code>strtok</code>() that specify the delimiter string &quot;<i>;,</i>&quot; would return the strings &quot;<i>aaa</i>&quot; and &quot;<i>bbb</i>&quot;, and then a null pointer. </p>
<p> The <code>strtok_r</code>() function is a reentrant version of <code>strtok</code>(). The <i>saveptr</i> argument is a pointer to a <i>char&nbsp;*</i> variable that is used internally by <code>strtok_r</code>() in order to maintain context between successive calls that parse the same string. </p>
<p> On the first call to <code>strtok_r</code>(), <i>str</i> should point to the string to be parsed, and the value of <i>*saveptr</i> is ignored (but see NOTES). In subsequent calls, <i>str</i> should be NULL, and <i>saveptr</i> (and the buffer that it points to) should be unchanged since the previous call. </p>
<p> Different strings may be parsed concurrently using sequences of calls to <code>strtok_r</code>() that specify different <i>saveptr</i> arguments.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strtok</code>() and <code>strtok_r</code>() functions return a pointer to the next token, or NULL if there are no more tokens.  </p>
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
<td> <code>strtok</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:strtok
</td>
</tr>
<tr VALIGN=top>
<td> <code>strtok_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<dl>
<dt><code>strtok</code>() </dt>
<dd> <p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD. </p>
 </dd>
<dt><code>strtok_r</code>() </dt>
<dd> <p> POSIX.1-2001, POSIX.1-2008. </p>
 </dd></dl>
<h2>NOTES</h2>
<p> On some implementations, <i>*saveptr</i> is required to be NULL on the first call to <code>strtok_r</code>() that is being used to parse <i>str</i>.  </p>
<h2>BUGS</h2>
<p> Be cautious when using these functions. If you do use them, note that: </p>
<dl>
<dt>*</dt>
<dd> <p> These functions modify their first argument. </p>
 </dd>
<dt>*</dt>
<dd> <p> These functions cannot be used on constant strings. </p>
 </dd>
<dt>*</dt>
<dd> <p> The identity of the delimiting byte is lost. </p>
 </dd>
<dt>*</dt>
<dd> <p> The <code>strtok</code>() function uses a static buffer while parsing, so it&#8217;s not thread safe. Use <code>strtok_r</code>() if this matters to you. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> The program below uses nested loops that employ <code>strtok_r</code>() to break a string into a two-level hierarchy of tokens. The first command-line argument specifies the string to be parsed. The second argument specifies the delimiter byte(s) to be used to separate that string into &quot;major&quot; tokens. The third argument specifies the delimiter byte(s) to be used to separate the &quot;major&quot; tokens into subtokens. </p>
<p> An example of the output produced by this program is the following: </p>
<p> $<code> ./a.out &#8216;a/bbb///cc;xxx:yyy:&#8216; &#8216;:;&#8216; &#8216;/&#8216;</code> 1: a/bbb///cc <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;--&gt;&nbsp;a <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;--&gt;&nbsp;bbb <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;--&gt;&nbsp;cc 2: xxx <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;--&gt;&nbsp;xxx 3: yyy <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;--&gt;&nbsp;yyy  </p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> int main(int argc, char *argv[]) { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*str1,&nbsp;*str2,&nbsp;*token,&nbsp;*subtoken; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*saveptr1,&nbsp;*saveptr2; </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;4)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s string delim subdelim\n&quot;, <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;1, str1&nbsp;=&nbsp;argv[1];&nbsp;;&nbsp;j++, str1&nbsp;=&nbsp;NULL)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;token&nbsp;=&nbsp;strtok_r(str1, argv[2],&nbsp;&amp;saveptr1); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(token&nbsp;==&nbsp;NULL) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d:&nbsp;%s\n&quot;, j, token); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(str2&nbsp;=&nbsp;token;&nbsp;;&nbsp;str2&nbsp;=&nbsp;NULL)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subtoken&nbsp;=&nbsp;strtok_r(str2, argv[3],&nbsp;&amp;saveptr2); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(subtoken&nbsp;==&nbsp;NULL) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot; &nbsp;--&gt;&nbsp;%s\n&quot;, subtoken); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> Another example program using <code>strtok</code>() can be found in <code><a href="/docs/linux/man/3-getaddrinfo_a/">getaddrinfo_a</a></code>(3).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-wcstok/">wcstok</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
