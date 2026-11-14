---
title: "cacosf(3)"
name: "cacosf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cacosf/"
description: "cacos, cacosf, cacosl – complex arc cosine"
---

<h2 class="name">NAME</h2>
<p> cacos, cacosf, cacosl &#8211; complex arc cosine </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cacos(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cacosf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cacosl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex arc cosine of <i>z</i>. If <i>y&nbsp;=&nbsp;cacos(z)</i>, then <i>z&nbsp;=&nbsp;ccos(y)</i>. The real part of <i>y</i> is chosen in the interval [0,pi]. </p>
<p> One has: </p>
<pre>
    cacos(z) = -i * clog(z + i * csqrt(1 - z * z))
</pre>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>cacos</code>(), <code>cacosf</code>(), <code>cacosl</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C99, POSIX.1-2001, POSIX.1-2008.</p>
<h2>EXAMPLES</h2>
<p> /* Link with &quot;-lm&quot; */ </p>
<p> #include &lt;complex.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double complex z, c, f;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double complex i&nbsp;=&nbsp;I; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;real&gt;&nbsp;&lt;imag&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;z&nbsp;=&nbsp;atof(argv[1])&nbsp;+&nbsp;atof(argv[2])&nbsp;*&nbsp;I; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c&nbsp;=&nbsp;cacos(z); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;cacos()&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(c), cimag(c)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f&nbsp;=&nbsp;-i&nbsp;*&nbsp;clog(z&nbsp;+&nbsp;i&nbsp;*&nbsp;csqrt(1 &#8211; z&nbsp;*&nbsp;z)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;formula&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(f), cimag(f)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ccos/">ccos</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
