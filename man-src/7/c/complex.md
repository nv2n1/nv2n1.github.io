---
title: "complex(7)"
name: "complex"
section: "7"
letter: "c"
url: "/docs/linux/man/7-complex/"
description: "complex – basics of complex mathematics"
---

<p>complex &#8211; basics of complex mathematics</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;complex.h&gt;</code></pre>
<h2>Description</h2>
<p>Complex numbers are numbers of the form z = a+b*i, where a and b are real numbers and i = sqrt(-1), so that i*i = -1. </p>
<p> There are other ways to represent that number. The pair (a,b) of real numbers may be viewed as a point in the plane, given by X- and Y-coordinates. This same point may also be described by giving the pair of real numbers (r,phi), where r is the distance to the origin O, and phi the angle between the X-axis and the line Oz. Now z = r*exp(i*phi) = r*(cos(phi)+i*sin(phi)). </p>
<p> The basic operations are defined on z = a+b*i and w = c+d*i as:</p>
<dl>
<dt><code>addition: z+w = (a+c) + (b+d)*i</code></p>
<dd>
<dt><code>multiplication: z*w = (a*c &#8211; b*d) + (a*d + b*c)*i</code></p>
<dd>
<dt><code>division: z/w = ((a*c + b*d)/(c*c + d*d)) + ((b*c &#8211; a*d)/(c*c + d*d))*i</code></p>
<dd></dl>
<p> Nearly all math function have a complex counterpart but there are some complex-only functions.</p>
<h2>Examples</h2>
<p>Your C-compiler can work with complex numbers if it supports the C99 standard. Link with <i>-lm</i>. The imaginary unit is represented by I. </p>
<pre><code>/* check that exp(i * pi) == -1 */
#include &lt;complex.h&gt;
#include &lt;math.h&gt; /* for atan */
#include &lt;stdio.h&gt;
int main(void)
{
    double pi = 4 * atan(1.0);
    double complex z = cexp(I * pi);
    printf(&quot;%f + %f * i
&quot;, creal(z), cimag(z));
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cabs/">cabs</a></code>(3), <code><a href="/docs/linux/man/3-cacos/">cacos</a></code>(3), <code><a href="/docs/linux/man/3-cacosh/">cacosh</a></code>(3), <code><a href="/docs/linux/man/3-carg/">carg</a></code>(3), <code><a href="/docs/linux/man/3-casin/">casin</a></code>(3), <code><a href="/docs/linux/man/3-casinh/">casinh</a></code>(3), <code><a href="/docs/linux/man/3-catan/">catan</a></code>(3), <code><a href="/docs/linux/man/3-catanh/">catanh</a></code>(3), <code><a href="/docs/linux/man/3-ccos/">ccos</a></code>(3), <code><a href="/docs/linux/man/3-ccosh/">ccosh</a></code>(3), <code><a href="/docs/linux/man/3-cerf/">cerf</a></code>(3), <code><a href="/docs/linux/man/3-cexp/">cexp</a></code>(3), <code><a href="/docs/linux/man/3-cexp2/">cexp2</a></code>(3), <code><a href="/docs/linux/man/3-cimag/">cimag</a></code>(3), <code><a href="/docs/linux/man/3-clog/">clog</a></code>(3), <code><a href="/docs/linux/man/3-clog10/">clog10</a></code>(3), <code><a href="/docs/linux/man/3-clog2/">clog2</a></code>(3), <code><a href="/docs/linux/man/3-conj/">conj</a></code>(3), <code><a href="/docs/linux/man/3-cpow/">cpow</a></code>(3), <code><a href="/docs/linux/man/3-cproj/">cproj</a></code>(3), <code><a href="/docs/linux/man/3-creal/">creal</a></code>(3), <code><a href="/docs/linux/man/3-csin/">csin</a></code>(3), <code><a href="/docs/linux/man/3-csinh/">csinh</a></code>(3), <code><a href="/docs/linux/man/3-csqrt/">csqrt</a></code>(3), <code><a href="/docs/linux/man/3-ctan/">ctan</a></code>(3), <code><a href="/docs/linux/man/3-ctanh/">ctanh</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
