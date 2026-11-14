---
title: "quantlib_timeseries(3)"
name: "quantlib_timeseries"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_timeseries/"
description: "QuantLib::TimeSeries – Container for historical data."
---

<p>QuantLib::TimeSeries &#8211; Container for historical data. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/timeseries.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Date</code> <code>key_type</code> </p>
<p> typedef T <code>value_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>TimeSeries</code> () </p>
<p> template&lt;class DateIterator , class ValueIterator &gt; <code>TimeSeries</code> (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin) </p>
<p> template&lt;class ValueIterator &gt; <code>TimeSeries</code> (const <code>Date</code> &amp;firstDate, ValueIterator begin, ValueIterator end) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Date</code> <code>firstDate</code> () const<br />
 <i>returns the first date for which a historical datum exists </i><br />
 <code>Date</code> <code>lastDate</code> () const<br />
 <i>returns the last date for which a historical datum exists </i><br />
 Size <code>size</code> () const<br />
 <i>returns the number of historical data including null ones </i><br />
 bool <code>empty</code> () const<br />
 <i>returns whether the series contains any data </i> </p>
<p> <code>Historical data access</code> </p>
<p> T <code>operator[]</code> (const <code>Date</code> &amp;d) const<br />
 <i>returns the (possibly null) datum corresponding to the given date </i><br />
 T &amp; <code>operator[]</code> (const <code>Date</code> &amp;d) </p>
<p> <code>Utilities</code> </p>
<p> const_iterator <code>find</code> (const <code>Date</code> &amp;) </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>dates</code> () const<br />
 <i>returns the dates for which historical data exist </i><br />
 std::vector&lt; T &gt; <code>values</code> () const<br />
 <i>returns the historical data </i></p>
<h3>Iterators</h3>
<p>typedef Container::const_iterator <code>const_iterator</code> </p>
<p> typedef Container::const_reverse_iterator <code>const_reverse_iterator</code> </p>
<p> const_iterator <code>begin</code> () const </p>
<p> const_iterator <code>end</code> () const </p>
<p> const_reverse_iterator <code>rbegin</code> () const </p>
<p> const_reverse_iterator <code>rend</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T, class Container = std::map&lt;Date, T&gt;&gt; class QuantLib::TimeSeries&lt; T, Container &gt;</h3>
<p>Container for historical data. </p>
<p> This class acts as a generic repository for a set of historical data. Any single datum can be accessed through its date, while sets of consecutive data can be accessed through iterators. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>The Container type must satisfy the requirements set by the C++ standard for associative containers.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>TimeSeries</code> ()</h3>
<p>Default constructor</p>
<h3><code>TimeSeries</code> (DateIterator dBegin, DateIterator dEnd, ValueIterator vBegin)</h3>
<p>This constructor initializes the history with a set of values passed as two sequences, the first containing dates and the second containing corresponding values.</p>
<h3><code>TimeSeries</code> (const <code>Date</code> &amp; firstDate, ValueIterator begin, ValueIterator end)</h3>
<p>This constructor initializes the history with a set of values. Such values are assigned to a corresponding number of consecutive dates starting from <i>firstDate</i> included. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
