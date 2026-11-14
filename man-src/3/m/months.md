---
title: "months(3)"
name: "months"
section: "3"
letter: "m"
url: "/docs/linux/man/3-months/"
description: "QuantLib::Period –"
---

<p>QuantLib::Period &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/period.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Period</code> (Integer n, <code>TimeUnit</code> units) </p>
<p> <code>Period</code> (<code>Frequency</code> f) </p>
<p> Integer <code>length</code> () const </p>
<p> <code>TimeUnit</code> <code>units</code> () const </p>
<p> <code>Frequency</code> <code>frequency</code> () const </p>
<p> <code>Period</code> &amp; <code>operator+=</code> (const <code>Period</code> &amp;) </p>
<p> <code>Period</code> &amp; <code>operator-=</code> (const <code>Period</code> &amp;) </p>
<p> <code>Period</code> &amp; <code>operator/=</code> (Integer) </p>
<p> void <code>normalize</code> () </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 <code>Real</code> <code>years</code> (const <code>Period</code> &amp;) </p>
<p> <code>Real</code> <code>months</code> (const <code>Period</code> &amp;) </p>
<p> <code>Real</code> <code>weeks</code> (const <code>Period</code> &amp;) </p>
<p> <code>Real</code> <code>days</code> (const <code>Period</code> &amp;) </p>
<p> template&lt;typename T &gt; <code>Period</code> <code>operator*</code> (T n, <code>TimeUnit</code> units) </p>
<p> template&lt;typename T &gt; <code>Period</code> <code>operator*</code> (<code>TimeUnit</code> units, T n) </p>
<p> <code>Period</code> <code>operator-</code> (const <code>Period</code> &amp;) </p>
<p> <code>Period</code> <code>operator*</code> (Integer n, const <code>Period</code> &amp;) </p>
<p> <code>Period</code> <code>operator*</code> (const <code>Period</code> &amp;, Integer n) </p>
<p> <code>Period</code> <code>operator/</code> (const <code>Period</code> &amp;, Integer n) </p>
<p> <code>Period</code> <code>operator+</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> <code>Period</code> <code>operator-</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator&lt;</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator==</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator&gt;</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator&lt;=</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> bool <code>operator&gt;=</code> (const <code>Period</code> &amp;, const <code>Period</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Period</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>This class provides a <code>Period</code> (length + TimeUnit) class and implements a limited algebra. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>self-consistency of algebra is checked.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Friends And Related Function Documentation</h2>
<h3><code>Real</code> years (const <code>Period</code> &amp;) [related]</h3>
<h3><code>Real</code> months (const <code>Period</code> &amp;) [related]</h3>
<h3><code>Real</code> weeks (const <code>Period</code> &amp;) [related]</h3>
<h3><code>Real</code> days (const <code>Period</code> &amp;) [related]</h3>
<h3><code>Period</code> operator* (T n, <code>TimeUnit</code> units) [related]</h3>
<h3><code>Period</code> operator* (<code>TimeUnit</code> units, T n) [related]</h3>
<h3><code>Period</code> operator- (const <code>Period</code> &amp;) [related]</h3>
<h3><code>Period</code> operator* (Integer n, const <code>Period</code> &amp;) [related]</h3>
<h3><code>Period</code> operator* (const <code>Period</code> &amp;, Integer n) [related]</h3>
<h3><code>Period</code> operator/ (const <code>Period</code> &amp;, Integer n) [related]</h3>
<h3><code>Period</code> operator+ (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3><code>Period</code> operator- (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator&lt; (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator== (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator&gt; (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator&lt;= (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>bool operator&gt;= (const <code>Period</code> &amp;, const <code>Period</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Period</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
