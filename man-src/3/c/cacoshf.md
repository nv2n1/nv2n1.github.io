---
title: "cacoshf(3)"
name: "cacoshf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cacoshf/"
description: "cacosh, cacoshf, cacoshl – complex arc hyperbolic cosine"
---

<h2 class="name">NAME</h2>
<p> cacosh, cacoshf, cacoshl &#8211; complex arc hyperbolic cosine </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex cacosh(double complex </code><i>z</i><code>);</code><br />
 <code>float complex cacoshf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex cacoshl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex arc hyperbolic cosine of <i>z</i>. If <i>y&nbsp;=&nbsp;cacosh(z)</i>, then <i>z&nbsp;=&nbsp;ccosh(y)</i>. The imaginary part of <i>y</i> is chosen in the interval [-pi,pi]. The real part of <i>y</i> is chosen nonnegative. </p>
<p> One has: </p>
<pre>
    cacosh(z) = 2 * clog(csqrt((z + 1) / 2) + csqrt((z - 1) / 2))
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
<td> <code>cacosh</code>(), <code>cacoshf</code>(), <code>cacoshl</code>() </td>
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
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;double complex z, c, f; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;real&gt;&nbsp;&lt;imag&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;z&nbsp;=&nbsp;atof(argv[1])&nbsp;+&nbsp;atof(argv[2])&nbsp;*&nbsp;I; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c&nbsp;=&nbsp;cacosh(z);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;cacosh()&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(c), cimag(c)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f&nbsp;=&nbsp;2&nbsp;*&nbsp;clog(csqrt((z&nbsp;+&nbsp;1)/2)&nbsp;+&nbsp;csqrt((z &#8211; 1)/2));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;formula&nbsp;<wbr>&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(f2), cimag(f2)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-acosh/">acosh</a></code>(3), <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-ccosh/">ccosh</a></code>(3), <code><a href="/docs/linux/man/3-cimag/">cimag</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
