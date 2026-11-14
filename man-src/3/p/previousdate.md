---
title: "previousdate(3)"
name: "previousdate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-previousdate/"
description: "QuantLib::Schedule – Payment schedule."
---

<p>QuantLib::Schedule &#8211; Payment schedule. </p>
<h2>Synopsis</h2>
<pre><code>typedef std::vector&lt; Date &gt;::const_iterator const_iterator



const_iterator begin () const



const_iterator end () const



const_iterator lower_bound (const Date &amp;d=Date()) const</code></pre>
<h3>Public Member Functions</h3>
<p>typedef std::vector&lt; Date &gt;::const_iterator const_iterator</p>
<p>const_iterator begin () const</p>
<p>const_iterator end () const</p>
<p>const_iterator lower_bound (const Date &amp;d=Date()) const <code>Date access</code> </p>
<p> Size <code>size</code> () const </p>
<p> const <code>Date</code> &amp; <code>operator[]</code> (Size i) const </p>
<p> const <code>Date</code> &amp; <code>at</code> (Size i) const </p>
<p> const <code>Date</code> &amp; <code>date</code> (Size i) const </p>
<p> <code>Date</code> <code>previousDate</code> (const <code>Date</code> &amp;refDate) const </p>
<p> <code>Date</code> <code>nextDate</code> (const <code>Date</code> &amp;refDate) const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> bool <code>isRegular</code> (Size i) const<br />
 <code>Other inspectors</code> </p>
<p> bool <code>empty</code> () const </p>
<p> const <code>Calendar</code> &amp; <code>calendar</code> () const </p>
<p> const <code>Date</code> &amp; <code>startDate</code> () const </p>
<p> const <code>Date</code> &amp; <code>endDate</code> () const </p>
<p> const <code>Period</code> &amp; <code>tenor</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>terminationDateBusinessDayConvention</code> () const </p>
<p> <code>DateGeneration::Rule</code> <code>rule</code> () const </p>
<p> bool <code>endOfMonth</code> () const</p>
<h3>Iterators</h3>
<pre><code>typedef std::vector&lt; Date &gt;::const_iterator const_iterator



const_iterator begin () const



const_iterator end () const



const_iterator lower_bound (const Date &amp;d=Date()) const</code></pre>
<h2>Detailed Description</h2>
<p>Payment schedule. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
