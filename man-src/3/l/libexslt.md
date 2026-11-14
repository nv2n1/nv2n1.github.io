---
title: "libexslt(3)"
name: "libexslt"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libexslt/"
description: "libexslt – extension library for XSLT"
---

<h2>NAME</h2>
<p> libexslt &#8211; extension library for XSLT</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libexslt/exslt.h&gt;</code> </p>
<p> <code>void exsltCommonRegister(void);</code><br />
 <code>void exsltDateRegister(void);</code><br />
 <code>void exsltDynRegister(void);</code><br />
 <code>void exsltFuncRegister(void);</code><br />
 <code>void exsltMathRegister(void);</code><br />
 <code>void exsltSetsRegister(void);</code><br />
 <code>void exsltStrRegister(void);</code><br />
 <code>void exsltRegisterAll(void);</code><br />
 <code>void exsltSaxonRegister(void);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libexslt</code> library is used to provide extensions to <font SIZE="-1">XSLT</font> functions. These extensions come from the <font SIZE="-1">EXSLT</font> project &lt;<a rel="nofollow" href="http://www.exslt.org/">http://www.exslt.org/</a>&gt; </p>
<h2>USAGE</h2>
<p> To make use of these functions in <font SIZE="-1">XSLT</font> the appropriate namespace must be defined on the <code>xsl:stylesheet</code> element. To enable support for them in <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3) you must call the appropriate functions (listed in the <code>SYNOPSIS</code> section) to register the extensions. The <i>xslt-config</i> shell script can be used to obtain the necessary flags for the pre-processor and linker. The supported extensions are:</p>
<h3>COMMON</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/common">http://exslt.org/common</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/exsl/index.html">http://www.exslt.org/exsl/index.html</a> for a description.</p>
<dd>
<dt><code>node-set()</code></p>
<dd> convert the given RTF into a node-set.</p>
<dt><code>object-type()</code></p>
<dd> returns the type of the given argument.</p>
<dt><code>document</code></p>
<dd> Create multiple output documents. See <a rel="nofollow" href="http://www.exslt.org/exsl/elements/document/index.html">http://www.exslt.org/exsl/elements/document/index.html</a> </p>
</dl>
<h3>MATH</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/math">http://exslt.org/math</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/math/index.html">http://www.exslt.org/math/index.html</a> for a description.</p>
<dd>
<dt><code>min()</code></p>
<dd> returns the minimum value of the given node-set</p>
<dt><code>max()</code></p>
<dd> returns the maximum value of the given node-set</p>
<dt><code>highest()</code></p>
<dd> returns the nodes in the node-set whose value is the maximum value for the node-set.</p>
<dt><code>lowest()</code></p>
<dd> returns the nodes in the node-set whose value is the minimum value for the node-set.</p>
<dt><code>constant()</code></p>
<dd> returns a number value of the given constant with the given precision. The constants are PI, E, SQRRT2, LN2, LN10, LOG2E, and SQRT1_2.</p>
<dt><code>random()</code></p>
<dd> returns a random number between 0 and 1 inclusive.</p>
<dt><code>abs()</code></p>
<dd> returns the absolute value of the argument.</p>
<dt><code>sqrt()</code></p>
<dd> returns the square root of the argument.</p>
<dt><code>power()</code></p>
<dd> returns the power base and power arguments.</p>
<dt><code>log()</code></p>
<dd> returns the natural log of the argument.</p>
<dt><code>sin()</code></p>
<dd> returns the sine of the argument.</p>
<dt><code>cos()</code></p>
<dd> returns the cosine of the argument.</p>
<dt><code>tan()</code></p>
<dd> returns the tangent of the argument.</p>
<dt><code>asin()</code></p>
<dd> returns the arc sine of the argument.</p>
<dt><code>acos()</code></p>
<dd> returns the arc cosine of the argument.</p>
<dt><code>atan()</code></p>
<dd> returns the arc tangent of the argument.</p>
<dt><code>atan2()</code></p>
<dd> returns the arc tangent function of the y/x arguments.</p>
<dt><code>exp()</code></p>
<dd> returns the exponential function of the argument. </p>
</dl>
<h3>SETS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/sets">http://exslt.org/sets</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/set/index.html">http://www.exslt.org/set/index.html</a> for a description.</p>
<dd>
<dt><code>difference()</code></p>
<dd> returns the difference between the two given node-sets.</p>
<dt><code>intersection()</code></p>
<dd> returns a node-set of the nodes within both given node-sets.</p>
<dt><code>distinct()</code></p>
<dd> returns a node-set of all nodes in the first argument that are not in the seconds argument.</p>
<dt><code>has-same-node()</code></p>
<dd> returns TRUE if there is an intersection between the two given node-sets.</p>
<dt><code>leading()</code></p>
<dd> returns a node-set of all nodes in the first argument that precede the first node in the second argument.</p>
<dt><code>trailing()</code></p>
<dd> returns a node-set of all nodes in the first argument that follow the first node in the second argument. </p>
</dl>
<h3>DATES and TIMES</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/dates-and-times">http://exslt.org/dates-and-times</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/date/date.html">http://www.exslt.org/date/date.html</a> for a description.</p>
<dd>
<dt><code>date-time()</code></p>
<dd> returns the current date and time as a date/time string.</p>
<dt><code>date()</code></p>
<dd> returns the date specified in the given date/time string.</p>
<dt><code>time()</code></p>
<dd> returns the time specified in the date/time string given as the argument.</p>
<dt><code>year()</code></p>
<dd> returns the year of a date as a number.</p>
<dt><code>leap-year()</code></p>
<dd> returns true if the year given in a date is a leap year.</p>
<dt><code>month-in-year()</code></p>
<dd> returns the month of a date as a number.</p>
<dt><code>month-name()</code></p>
<dd> returns the full name of the month of a date.</p>
<dt><code>month-abbreviation()</code></p>
<dd> returns the abbreviation of the month of a date.</p>
<dt><code>week-in-year()</code></p>
<dd> returns the week of the year as a number.</p>
<dt><code>week-in-month()</code></p>
<dd> returns the week in a month of a date as a number.</p>
<dt><code>day-in-year()</code></p>
<dd> returns the month of a date as a number.</p>
<dt><code>day-in-month()</code></p>
<dd> returns the day of a date as a number.</p>
<dt><code>day-of-week-in-month()</code></p>
<dd> returns the day-of-the-week in a month of a date as a number.</p>
<dt><code>day-in-week()</code></p>
<dd> returns the day of the week given in a date as a number.</p>
<dt><code>day-name()</code></p>
<dd> returns the full name of the day of the week of a date.</p>
<dt><code>day-abbreviation()</code></p>
<dd> returns the abbreviation of the day of the week of a date.</p>
<dt><code>hour-in-day()</code></p>
<dd> returns the hour of the day as a number.</p>
<dt><code>minute-in-hour()</code></p>
<dd> returns the minute of the hour as a number.</p>
<dt><code>second-in-minute()</code></p>
<dd> returns the second of the minute as a number.</p>
<dt><code>seconds()</code></p>
<dd> returns the number of seconds specified by the argument string.</p>
<dt><code>add()</code></p>
<dd> returns the date/time resulting from adding a duration to a date/time.</p>
<dt><code>add-duration()</code></p>
<dd> returns the duration resulting from adding two given durations together.</p>
<dt><code>difference()</code></p>
<dd> returns the duration between the first date and the second date.</p>
<dt><code>duration()</code></p>
<dd> returns a duration string that represents the given number of seconds since 1970-01-01T00:00:00. </p>
</dl>
<h3>STRINGS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/strings">http://exslt.org/strings</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/str/index.html">http://www.exslt.org/str/index.html</a> for a description.</p>
<dd>
<dt><code>tokenize()</code></p>
<dd> returns a node set of token elements, each containing one token from the string.</p>
<dt><code>padding()</code></p>
<dd> returns a string padded to a certain length.</p>
<dt><code>align()</code></p>
<dd> returns a string aligned within another string.</p>
<dt><code>concat()</code></p>
<dd> returns the concatenation of the string values of the nodes in that node set. </p>
</dl>
<h3>FUNCTIONS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/functions">http://exslt.org/functions</a></p>
<dd>
<dt>See <a rel="nofollow" href="http://www.exslt.org/func/index.html">http://www.exslt.org/func/index.html</a> for a description.</p>
<dd>
<dt><code>function</code></p>
<dd> declares an extension function.</p>
<dt><code>result</code></p>
<dd> returns the result of an extension function declared in function().</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/bin/xslt-config</i></p>
<dd> shell script giving pre-processor and linker flags.</p>
<dt><i>/usr/lib/libexslt.a</i></p>
<dd> static library</p>
<dt><i>/usr/lib/libexslt.so</i></p>
<dd> sharable library</dl>
<h2>AUTHORS</h2>
<p> Manual page by Heiko W. Rupp (hwr [at] pilhuhn.de)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3), <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3), <code><a href="/docs/linux/man/1-xmllint/">xmllint</a></code>(1) <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></code>(1), </p>
<h2>Index</h2>
