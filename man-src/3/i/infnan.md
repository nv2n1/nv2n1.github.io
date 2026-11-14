---
title: "infnan(3)"
name: "infnan"
section: "3"
letter: "i"
url: "/docs/linux/man/3-infnan/"
description: "infnan – deal with infinite or not-a-number (NaN) result"
---

<h2>NAME</h2>
<p> infnan &#8211; deal with infinite or not-a-number (NaN) result</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;math.h&gt;
double infnan(int error);
</code></pre>
<p> Link with <i>-lm</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>infnan</code>() function returns a suitable value for infinity and &quot;not-a-number&quot; (NaN) results. The value of <i>error</i> can be <code>ERANGE</code> to represent infinity or anything else to represent NaN. <i>errno</i> is also set.</p>
<h2>RETURN VALUE</h2>
<p> If <i>error</i> is <code>ERANGE</code> (Infinity), <code>HUGE_VAL</code> is returned. </p>
<p> If <i>error</i> is &#8211;<code>ERANGE</code> (-Infinity), &#8211;<code>HUGE_VAL</code> is returned. </p>
<p> If <i>error</i> is anything else, NAN is returned.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EDOM</code></p>
<dd> The value of <i>error</i> is &quot;not-a-number&quot; (NaN).</p>
<dt><code>ERANGE</code></p>
<dd> The value of <i>error</i> is positive infinity or negative infinity.</dl>
<h2>CONFORMING TO</h2>
<p> 4.3BSD.</p>
<h2>NOTES</h2>
<p> This obsolete function was provided in libc4 and libc5, but is not available in glibc2.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
