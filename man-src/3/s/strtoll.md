---
title: "strtoll(3)"
name: "strtoll"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtoll/"
description: "strtol, strtoll, strtoq – convert a string to a long integer"
---

<p>strtol, strtoll, strtoq &#8211; convert a string to a long integer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;
long strtol(const char *nptr, char **endptr, int base);
long long strtoll(const char *nptr, char **endptr, int base);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strtoll</code>():</p>
<dl>
<dd>_ISOC99_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dd></dl>
<h2>Description</h2>
<p>The <code>strtol</code>() function converts the initial part of the string in <i>nptr</i> to a long integer value according to the given <i>base</i>, which must be between 2 and 36 inclusive, or be the special value 0. </p>
<p> The string may begin with an arbitrary amount of white space (as determined by <code>isspace</code>(3)) followed by a single optional &#8216;+&#8217; or &#8216;-&#8216; sign. If <i>base</i> is zero or 16, the string may then include a &quot;0x&quot; or &quot;0X&quot; prefix, and the number will be read in base 16; otherwise, a zero <i>base</i> is taken as 10 (decimal) unless the next character is &#8216;0&#8217;, in which case it is taken as 8 (octal). </p>
<p> The remainder of the string is converted to a <i>long</i> value in the obvious manner, stopping at the first character which is not a valid digit in the given base. (In bases above 10, the letter &#8216;A&#8217; in either uppercase or lowercase represents 10, &#8216;B&#8217; represents 11, and so forth, with &#8216;Z&#8217; representing 35.) </p>
<p> If <i>endptr</i> is not NULL, <code>strtol</code>() stores the address of the first invalid character in <i>*endptr</i>. If there were no digits at all, <code>strtol</code>() stores the original value of <i>nptr</i> in <i>*endptr</i> (and returns 0). In particular, if <i>*nptr</i> is not &#8216;\0&#8217; but <i>**endptr</i> is &#8216;\0&#8217; on return, the entire string is valid. </p>
<p> The <code>strtoll</code>() function works just like the <code>strtol</code>() function but returns a <i>long long</i> integer value.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strtol</code>() function returns the result of the conversion, unless the value would underflow or overflow. If an underflow occurs, <code>strtol</code>() returns <code>LONG_MIN</code>. If an overflow occurs, <code>strtol</code>() returns <code>LONG_MAX</code>. In both cases, <i>errno</i> is set to <code>ERANGE</code>. Precisely the same holds for <code>strtoll</code>() (with <code>LLONG_MIN</code> and <code>LLONG_MAX</code> instead of <code>LONG_MIN</code> and <code>LONG_MAX</code>).  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> <p> (not in C99) The given <i>base</i> contains an unsupported value. </p>
 </dd>
<dt><code>ERANGE</code></dt>
<dd> <p> The resulting value was out of range. </p>
 </dd></dl>
<p> The implementation may also set <i>errno</i> to <code>EINVAL</code> in case no conversion was performed (no digits seen, and 0 returned).  </p>
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
<td> <code>strtol</code>(), <code>strtoll</code>(), <code>strtoq</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>strtol</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99 SVr4, 4.3BSD. </p>
<p> <code>strtoll</code>(): POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> Since <code>strtol</code>() can legitimately return 0, <code>LONG_MAX</code>, or <code>LONG_MIN</code> (<code>LLONG_MAX</code> or <code>LLONG_MIN</code> for <code>strtoll</code>()) on both success and failure, the calling program should set <i>errno</i> to 0 before the call, and then determine if an error occurred by checking whether <i>errno</i> has a nonzero value after the call. </p>
<p> According to POSIX.1, in locales other than &quot;C&quot; and &quot;POSIX&quot;, these functions may accept other, implementation-defined numeric strings. </p>
<p> BSD also has </p>
<p> <code>quad_t strtoq(const char *</code><i>nptr</i><code>, char **</code><i>endptr</i><code>, int </code><i>base</i><code>);</code> </p>
<p> with completely analogous definition. Depending on the wordsize of the current architecture, this may be equivalent to <code>strtoll</code>() or to <code>strtol</code>().  </p>
<h2>EXAMPLES</h2>
<p> The program shown below demonstrates the use of <code>strtol</code>(). The first command-line argument specifies a string from which <code>strtol</code>() should parse a number. The second (optional) argument specifies the base to be used for the conversion. (This argument is converted to numeric form using <code><a href="/docs/linux/man/3-atoi/">atoi</a></code>(3), a function that performs no error checking and has a simpler interface than <code>strtol</code>().) Some examples of the results produced by this program are the following: </p>
<p> $<code> ./a.out 123</code> strtol() returned 123 $<code> ./a.out &#8216; 123&#8217;</code> strtol() returned 123 $<code> ./a.out 123abc</code> strtol() returned 123 Further characters after number: &quot;abc&quot; $<code> ./a.out 123abc 55</code> strtol: Invalid argument $<code> ./a.out &#8216;&#8216;</code> No digits were found $<code> ./a.out 4000000000</code> strtol: Numerical result out of range  </p>
<h3>Program source</h3>
<p> #include &lt;stdlib.h&gt; #include &lt;limits.h&gt; #include &lt;stdio.h&gt; #include &lt;errno.h&gt; </p>
<p> int main(int argc, char *argv[]) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int base; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*endptr,&nbsp;*str; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long val; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s str&nbsp;[base]\n&quot;, argv[0]); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;str&nbsp;=&nbsp;argv[1]; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;2)&nbsp;?&nbsp;atoi(argv[2])&nbsp;: 0; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno&nbsp;=&nbsp;0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;To distinguish success/failure after call&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;val&nbsp;=&nbsp;strtol(str,&nbsp;&amp;endptr, base); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Check for various possible errors&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;!=&nbsp;0)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;strtol&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(endptr&nbsp;==&nbsp;str)&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;No digits were found\n&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If we got here, strtol()&nbsp;successfully parsed a number&nbsp;*/ </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;strtol()&nbsp;returned&nbsp;%ld\n&quot;, val); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(*endptr&nbsp;!=&nbsp;&#8216;\0&#8217;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Not necessarily an error...&nbsp;*/ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Further characters after number:&nbsp;\&quot;%s\&quot;\n&quot;, endptr); </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atof/">atof</a></code>(3), <code><a href="/docs/linux/man/3-atoi/">atoi</a></code>(3), <code><a href="/docs/linux/man/3-atol/">atol</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3), <code><a href="/docs/linux/man/3-strtoimax/">strtoimax</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3),  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
