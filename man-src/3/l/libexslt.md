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
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/common">http://exslt.org/common</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/exsl/index.html">http://www.exslt.org/exsl/index.html</a> for a description.</dt>
<dd>
</dd><dt><code>node-set()</code></dt>
<dd> convert the given RTF into a node-set.</dd>
<dt><code>object-type()</code></dt>
<dd> returns the type of the given argument.</dd>
<dt><code>document</code></dt>
<dd> Create multiple output documents. See <a rel="nofollow" href="http://www.exslt.org/exsl/elements/document/index.html">http://www.exslt.org/exsl/elements/document/index.html</a> </dd>
</dl>
<h3>MATH</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/math">http://exslt.org/math</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/math/index.html">http://www.exslt.org/math/index.html</a> for a description.</dt>
<dd>
</dd><dt><code>min()</code></dt>
<dd> returns the minimum value of the given node-set</dd>
<dt><code>max()</code></dt>
<dd> returns the maximum value of the given node-set</dd>
<dt><code>highest()</code></dt>
<dd> returns the nodes in the node-set whose value is the maximum value for the node-set.</dd>
<dt><code>lowest()</code></dt>
<dd> returns the nodes in the node-set whose value is the minimum value for the node-set.</dd>
<dt><code>constant()</code></dt>
<dd> returns a number value of the given constant with the given precision. The constants are PI, E, SQRRT2, LN2, LN10, LOG2E, and SQRT1_2.</dd>
<dt><code>random()</code></dt>
<dd> returns a random number between 0 and 1 inclusive.</dd>
<dt><code>abs()</code></dt>
<dd> returns the absolute value of the argument.</dd>
<dt><code>sqrt()</code></dt>
<dd> returns the square root of the argument.</dd>
<dt><code>power()</code></dt>
<dd> returns the power base and power arguments.</dd>
<dt><code>log()</code></dt>
<dd> returns the natural log of the argument.</dd>
<dt><code>sin()</code></dt>
<dd> returns the sine of the argument.</dd>
<dt><code>cos()</code></dt>
<dd> returns the cosine of the argument.</dd>
<dt><code>tan()</code></dt>
<dd> returns the tangent of the argument.</dd>
<dt><code>asin()</code></dt>
<dd> returns the arc sine of the argument.</dd>
<dt><code>acos()</code></dt>
<dd> returns the arc cosine of the argument.</dd>
<dt><code>atan()</code></dt>
<dd> returns the arc tangent of the argument.</dd>
<dt><code>atan2()</code></dt>
<dd> returns the arc tangent function of the y/x arguments.</dd>
<dt><code>exp()</code></dt>
<dd> returns the exponential function of the argument. </dd>
</dl>
<h3>SETS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/sets">http://exslt.org/sets</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/set/index.html">http://www.exslt.org/set/index.html</a> for a description.</dt>
<dd>
</dd><dt><code>difference()</code></dt>
<dd> returns the difference between the two given node-sets.</dd>
<dt><code>intersection()</code></dt>
<dd> returns a node-set of the nodes within both given node-sets.</dd>
<dt><code>distinct()</code></dt>
<dd> returns a node-set of all nodes in the first argument that are not in the seconds argument.</dd>
<dt><code>has-same-node()</code></dt>
<dd> returns TRUE if there is an intersection between the two given node-sets.</dd>
<dt><code>leading()</code></dt>
<dd> returns a node-set of all nodes in the first argument that precede the first node in the second argument.</dd>
<dt><code>trailing()</code></dt>
<dd> returns a node-set of all nodes in the first argument that follow the first node in the second argument. </dd>
</dl>
<h3>DATES and TIMES</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/dates-and-times">http://exslt.org/dates-and-times</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/date/date.html">http://www.exslt.org/date/date.html</a> for a description.</dt>
<dd>
</dd><dt><code>date-time()</code></dt>
<dd> returns the current date and time as a date/time string.</dd>
<dt><code>date()</code></dt>
<dd> returns the date specified in the given date/time string.</dd>
<dt><code>time()</code></dt>
<dd> returns the time specified in the date/time string given as the argument.</dd>
<dt><code>year()</code></dt>
<dd> returns the year of a date as a number.</dd>
<dt><code>leap-year()</code></dt>
<dd> returns true if the year given in a date is a leap year.</dd>
<dt><code>month-in-year()</code></dt>
<dd> returns the month of a date as a number.</dd>
<dt><code>month-name()</code></dt>
<dd> returns the full name of the month of a date.</dd>
<dt><code>month-abbreviation()</code></dt>
<dd> returns the abbreviation of the month of a date.</dd>
<dt><code>week-in-year()</code></dt>
<dd> returns the week of the year as a number.</dd>
<dt><code>week-in-month()</code></dt>
<dd> returns the week in a month of a date as a number.</dd>
<dt><code>day-in-year()</code></dt>
<dd> returns the month of a date as a number.</dd>
<dt><code>day-in-month()</code></dt>
<dd> returns the day of a date as a number.</dd>
<dt><code>day-of-week-in-month()</code></dt>
<dd> returns the day-of-the-week in a month of a date as a number.</dd>
<dt><code>day-in-week()</code></dt>
<dd> returns the day of the week given in a date as a number.</dd>
<dt><code>day-name()</code></dt>
<dd> returns the full name of the day of the week of a date.</dd>
<dt><code>day-abbreviation()</code></dt>
<dd> returns the abbreviation of the day of the week of a date.</dd>
<dt><code>hour-in-day()</code></dt>
<dd> returns the hour of the day as a number.</dd>
<dt><code>minute-in-hour()</code></dt>
<dd> returns the minute of the hour as a number.</dd>
<dt><code>second-in-minute()</code></dt>
<dd> returns the second of the minute as a number.</dd>
<dt><code>seconds()</code></dt>
<dd> returns the number of seconds specified by the argument string.</dd>
<dt><code>add()</code></dt>
<dd> returns the date/time resulting from adding a duration to a date/time.</dd>
<dt><code>add-duration()</code></dt>
<dd> returns the duration resulting from adding two given durations together.</dd>
<dt><code>difference()</code></dt>
<dd> returns the duration between the first date and the second date.</dd>
<dt><code>duration()</code></dt>
<dd> returns a duration string that represents the given number of seconds since 1970-01-01T00:00:00. </dd>
</dl>
<h3>STRINGS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/strings">http://exslt.org/strings</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/str/index.html">http://www.exslt.org/str/index.html</a> for a description.</dt>
<dd>
</dd><dt><code>tokenize()</code></dt>
<dd> returns a node set of token elements, each containing one token from the string.</dd>
<dt><code>padding()</code></dt>
<dd> returns a string padded to a certain length.</dd>
<dt><code>align()</code></dt>
<dd> returns a string aligned within another string.</dd>
<dt><code>concat()</code></dt>
<dd> returns the concatenation of the string values of the nodes in that node set. </dd>
</dl>
<h3>FUNCTIONS</h3>
<dl>
<dt>Namespace: <a rel="nofollow" href="http://exslt.org/functions">http://exslt.org/functions</a></dt>
<dd>
</dd><dt>See <a rel="nofollow" href="http://www.exslt.org/func/index.html">http://www.exslt.org/func/index.html</a> for a description.</dt>
<dd>
</dd><dt><code>function</code></dt>
<dd> declares an extension function.</dd>
<dt><code>result</code></dt>
<dd> returns the result of an extension function declared in function().</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/bin/xslt-config</i></dt>
<dd> shell script giving pre-processor and linker flags.</dd>
<dt><i>/usr/lib/libexslt.a</i></dt>
<dd> static library</dd>
<dt><i>/usr/lib/libexslt.so</i></dt>
<dd> sharable library</dd></dl>
<h2>AUTHORS</h2>
<p> Manual page by Heiko W. Rupp (hwr [at] pilhuhn.de)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libxml/">libxml</a></code>(3), <code><a href="/docs/linux/man/3-libxslt/">libxslt</a></code>(3), <code><a href="/docs/linux/man/1-xmllint/">xmllint</a></code>(1) <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></code>(1), </p>
<h2>Index</h2>
