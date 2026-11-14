---
title: "weeks(3)"
name: "weeks"
section: "3"
letter: "w"
url: "/docs/linux/man/3-weeks/"
description: "QuantLib::Period –"
---

<p>QuantLib::Period &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/time/period.hpp&gt;</code></pre>
<h3>Public Member Functions</h3>
<pre><code>Period (Integer n, TimeUnit units)



Period (Frequency f)



Integer length () const



TimeUnit units () const



Frequency frequency () const



Period &amp; operator+= (const Period &amp;)



Period &amp; operator-= (const Period &amp;)



Period &amp; operator/= (Integer)



void normalize ()



Related Functions

(Note that these are not member functions.)


Real years (const Period &amp;)



Real months (const Period &amp;)



Real weeks (const Period &amp;)



Real days (const Period &amp;)



template&lt;typename T &gt; Period operator* (T n, TimeUnit units)



template&lt;typename T &gt; Period operator* (TimeUnit units, T n)



Period operator- (const Period &amp;)



Period operator* (Integer n, const Period &amp;)



Period operator* (const Period &amp;, Integer n)



Period operator/ (const Period &amp;, Integer n)



Period operator+ (const Period &amp;, const Period &amp;)



Period operator- (const Period &amp;, const Period &amp;)



bool operator&lt; (const Period &amp;, const Period &amp;)



bool operator== (const Period &amp;, const Period &amp;)



bool operator!= (const Period &amp;, const Period &amp;)



bool operator&gt; (const Period &amp;, const Period &amp;)



bool operator&lt;= (const Period &amp;, const Period &amp;)



bool operator&gt;= (const Period &amp;, const Period &amp;)



std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Period &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>This class provides a <code>Period</code> (length + TimeUnit) class and implements a limited algebra. </p>
<p> <code>Tests</code></p>
<dl>
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
