---
title: "americanexercise(3)"
name: "americanexercise"
section: "3"
letter: "a"
url: "/docs/linux/man/3-americanexercise/"
description: "QuantLib::AmericanExercise – American exercise."
---

<p>QuantLib::AmericanExercise &#8211; American exercise. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/exercise.hpp&gt; </p>
<p> Inherits <code>QuantLib::EarlyExercise</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AmericanExercise</code> (const <code>Date</code> &amp;earliestDate, const <code>Date</code> &amp;latestDate, bool payoffAtExpiry=false) </p>
<p> <code>AmericanExercise</code> (const <code>Date</code> &amp;latestDate, bool payoffAtExpiry=false) </p>
<h2>Detailed Description</h2>
<p>American exercise. </p>
<p> An American option can be exercised at any time between two predefined dates; the first date might be omitted, in which case the option can be exercised at any time before the expiry. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check that everywhere the American condition is applied from earliestDate and not earlier</dl>
<p> <code>Examples: </code> </p>
<p> <code>ConvertibleBonds.cpp</code>, and <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
