---
title: "precision(3)"
name: "precision"
section: "3"
letter: "p"
url: "/docs/linux/man/3-precision/"
description: "QuantLib::Rounding – basic rounding class"
---

<p>QuantLib::Rounding &#8211; basic rounding class </p>
<h2>Synopsis</h2>
<pre><code>Rounding ()


default constructor


Rounding (Integer precision, Type type=Closest, Integer digit=5)



Decimal operator() (Decimal value) const


perform rounding



Inspectors</code></pre>
<p> Inherited by <code>CeilingTruncation</code>, <code>ClosestRounding</code>, <code>DownRounding</code>, <code>FloorTruncation</code>, and <code>UpRounding</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>None</code>, <code>Up</code>, <code>Down</code>, <code>Closest</code>, <code>Floor</code>, <code>Ceiling</code> }<br />
 <i>rounding methods </i></p>
<h3>Public Member Functions</h3>
<pre><code>Rounding ()


default constructor


Rounding (Integer precision, Type type=Closest, Integer digit=5)



Decimal operator() (Decimal value) const


perform rounding



Inspectors</code></pre>
<p> <code>Integer</code> <code>precision</code> () const </p>
<p> <code>Type</code> <code>type</code> () const </p>
<p> <code>Integer</code> <code>roundingDigit</code> () const</p>
<h2>Detailed Description</h2>
<p>basic rounding class </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned values is tested by checking them against known good results.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Type</code></h3>
<p>rounding methods </p>
<p> The rounding methods follow the OMG specification available at <a href="ftp://ftp.omg.org/pub/docs/formal/00-06-29.pdf">ftp://ftp.omg.org/pub/docs/formal/00-06-29.pdf</a> </p>
<p> <code>Warning</code></p>
<dl>
<dd>the names of the <code>Floor</code> and Ceiling methods might be misleading. Check the provided reference.</dl>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>None </i></p>
<dd>do not round: return the number unmodified</p>
<dt><i>Up </i></p>
<dd>the first decimal place past the precision will be rounded up. This differs from the OMG rule which rounds up only if the decimal to be rounded is greater than or equal to the rounding digit</p>
<dt><i>Down </i></p>
<dd>all decimal places past the precision will be truncated</p>
<dt><i>Closest </i></p>
<dd>the first decimal place past the precision will be rounded up if greater than or equal to the rounding digit; this corresponds to the OMG round-up rule. When the rounding digit is 5, the result will be the one closest to the original number, hence the name.</p>
<dt><i>Floor </i></p>
<dd>positive numbers will be rounded up and negative numbers will be rounded down using the OMG round up and round down rules</p>
<dt><i>Ceiling </i></p>
<dd>positive numbers will be rounded down and negative numbers will be rounded up using the OMG round up and round down rules</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Rounding</code> ()</h3>
<p>default constructor </p>
<p> Instances built through this constructor don&#8217;t perform any rounding.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
