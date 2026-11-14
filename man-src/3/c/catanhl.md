---
title: "catanhl(3)"
name: "catanhl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-catanhl/"
description: "catanh, catanhf, catanhl – complex arc tangents hyperbolic"
---

<h2 class="name">NAME</h2>
<p> catanh, catanhf, catanhl &#8211; complex arc tangents hyperbolic </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;complex.h&gt;</code> </p>
<p> <code>double complex catanh(double complex </code><i>z</i><code>);</code><br />
 <code>float complex catanhf(float complex </code><i>z</i><code>);</code><br />
 <code>long double complex catanhl(long double complex </code><i>z</i><code>);</code> </p>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> These functions calculate the complex arc hyperbolic tangent of <i>z</i>. If <i>y&nbsp;=&nbsp;catanh(z)</i>, then <i>z&nbsp;=&nbsp;ctanh(y)</i>. The imaginary part of <i>y</i> is chosen in the interval [-pi/2,pi/2]. </p>
<p> One has: </p>
<pre>
    catanh(z) = 0.5 * (clog(1 + z) - clog(1 - z))
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
<td> <code>catanh</code>(), <code>catanhf</code>(), <code>catanhl</code>() </td>
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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c&nbsp;=&nbsp;catanh(z);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;catanh()&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(c), cimag(c)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;f&nbsp;=&nbsp;0.5&nbsp;*&nbsp;(clog(1&nbsp;+&nbsp;z)&nbsp;&#8211; clog(1 &#8211; z));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;formula&nbsp;<wbr>&nbsp;=&nbsp;%6.3f&nbsp;%6.3f*i
&quot;, creal(f2), cimag(f2)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atanh/">atanh</a></code>(3), <code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cimag/">cimag</a></code>(3), <code><a href="/docs/linux/man/3-ctanh/">ctanh</a></code>(3), <code><a href="/docs/linux/man/7-complex/">complex</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
