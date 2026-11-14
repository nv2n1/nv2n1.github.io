---
title: "huge_vall(3)"
name: "huge_vall"
section: "3"
letter: "h"
url: "/docs/linux/man/3-huge_vall/"
description: "INFINITY, NAN, HUGE_VAL, HUGE_VALF, HUGE_VALL – floating-point constants"
---

<p>INFINITY, NAN, HUGE_VAL, HUGE_VALF, HUGE_VALL &#8211; floating-point constants </p>
<h2>Synopsis</h2>
<pre><code>#define _ISOC99_SOURCE</code> /* See <a href="//www.systutorials.com/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */
<code>#include &lt;math.h&gt;</code>
<code>INFINITY</code>
<code>NAN</code>
<code>HUGE_VAL</code>
<code>HUGE_VALF</code>
<code>HUGE_VALL</code></pre>
<h2>Description</h2>
<p>The macro <code>INFINITY</code> expands to a <i>float</i> constant representing positive infinity. </p>
<p> The macro <code>NAN</code> expands to a <i>float</i> constant representing a quiet NaN (when supported). A <i>quiet</i> NaN is a NaN (&quot;not-a-number&quot;) that does not raise exceptions when it is used in arithmetic. The opposite is a <i>signaling</i> NaN. See IEC 60559:1989. </p>
<p> The macros <code>HUGE_VAL</code>, <code>HUGE_VALF</code>, <code>HUGE_VALL</code> expand to constants of types <i>double</i>, <i>float</i>, and <i>long double</i>, respectively, that represent a large positive value, possibly positive infinity.</p>
<h2>Conforming To</h2>
<p>C99. </p>
<p> On a glibc system, the macro <code>HUGE_VAL</code> is always available. Availability of the <code>NAN</code> macro can be tested using <code>#ifdef NAN</code>, and similarly for <code>INFINITY</code>, <code>HUGE_VALF</code>, <code>HUGE_VALL</code>. They will be defined by <i>&lt;math.h&gt;</i> if <code>_ISOC99_SOURCE</code> or <code>_GNU_SOURCE</code> is defined, or <code>__STDC_VERSION__</code> is defined and has a value not less than 199901L.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fpclassify/">fpclassify</a></code>(3), <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
