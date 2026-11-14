---
title: "closesttime(3)"
name: "closesttime"
section: "3"
letter: "c"
url: "/docs/linux/man/3-closesttime/"
description: "QuantLib::TimeGrid – time grid class"
---

<p>QuantLib::TimeGrid &#8211; time grid class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/timegrid.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>TimeGrid</code> () </p>
<p> <code>TimeGrid</code> (<code>Time</code> end, Size steps)<br />
 <i>Regularly spaced time-grid. </i><br />
 template&lt;class Iterator &gt; <code>TimeGrid</code> (Iterator begin, Iterator end)<br />
 <i>Time grid with mandatory time points. </i><br />
 template&lt;class Iterator &gt; <code>TimeGrid</code> (Iterator begin, Iterator end, Size steps)<br />
 <i>Time grid with mandatory time points. </i> </p>
<p> <code>Time grid interface</code> </p>
<p> Size <code>index</code> (<code>Time</code> t) const<br />
 <i>returns the index i such that grid[i] = t </i><br />
 Size <code>closestIndex</code> (<code>Time</code> t) const<br />
 <i>returns the index i such that grid[i] is closest to t </i><br />
 <code>Time</code> <code>closestTime</code> (<code>Time</code> t) const<br />
 <i>returns the time on the grid closest to the given t </i><br />
 const std::vector&lt; <code>Time</code> &gt; &amp; <code>mandatoryTimes</code> () const </p>
<p> <code>Time</code> <code>dt</code> (Size i) const </p>
<h3>sequence interface</h3>
<p>typedef std::vector&lt; <code>Time</code> &gt;::const_iterator <code>const_iterator</code> </p>
<p> typedef std::vector&lt; <code>Time</code> &gt;::const_reverse_iterator <code>const_reverse_iterator</code> </p>
<p> <code>Time</code> <code>operator[]</code> (Size i) const </p>
<p> <code>Time</code> <code>at</code> (Size i) const </p>
<p> Size <code>size</code> () const </p>
<p> bool <code>empty</code> () const </p>
<p> const_iterator <code>begin</code> () const </p>
<p> const_iterator <code>end</code> () const </p>
<p> const_reverse_iterator <code>rbegin</code> () const </p>
<p> const_reverse_iterator <code>rend</code> () const </p>
<p> <code>Time</code> <code>front</code> () const </p>
<p> <code>Time</code> <code>back</code> () const </p>
<h2>Detailed Description</h2>
<p>time grid class </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>what was the rationale for limiting the grid to positive times? Investigate and see whether we can use it for negative ones as well.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>TimeGrid</code> (Iterator begin, Iterator end)</h3>
<p>Time grid with mandatory time points. </p>
<p> Mandatory points are guaranteed to belong to the grid. No additional points are added.</p>
<h3><code>TimeGrid</code> (Iterator begin, Iterator end, Size steps)</h3>
<p>Time grid with mandatory time points. </p>
<p> Mandatory points are guaranteed to belong to the grid. Additional points are then added with regular spacing between pairs of mandatory times in order to reach the desired number of steps. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
