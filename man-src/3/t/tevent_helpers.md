---
title: "tevent_helpers(3)"
name: "tevent_helpers"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_helpers/"
description: "The tevent helper functiions –"
---

<p>The tevent helper functiions &#8211;</p>
<h3>Functions</h3>
<p>int <code>tevent_timeval_compare</code> (const struct timeval *tv1, const struct timeval *tv2)<br />
 <i>Compare two timeval values. </i><br />
 struct timeval <code>tevent_timeval_zero</code> (void)<br />
 <i>Get a zero timval value. </i><br />
 struct timeval <code>tevent_timeval_current</code> (void)<br />
 <i>Get a timeval value for the current time. </i><br />
 struct timeval <code>tevent_timeval_set</code> (uint32_t secs, uint32_t usecs)<br />
 <i>Get a timeval structure with the given values. </i><br />
 struct timeval <code>tevent_timeval_until</code> (const struct timeval *tv1, const struct timeval *tv2)<br />
 <i>Get the difference between two timeval values. </i><br />
 bool <code>tevent_timeval_is_zero</code> (const struct timeval *tv)<br />
 <i>Check if a given timeval structure is zero. </i><br />
 struct timeval <code>tevent_timeval_add</code> (const struct timeval *tv, uint32_t secs, uint32_t usecs)<br />
 <i>Add the given amount of time to a timeval structure. </i><br />
 struct timeval <code>tevent_timeval_current_ofs</code> (uint32_t secs, uint32_t usecs)<br />
 <i>Get a timeval in the future with a specified offset from now. </i></p>
<h2>Detailed Description</h2>
<p><code>Todo</code></p>
<dl>
<dd>description</dl>
<h2>Function Documentation</h2>
<h3>struct timeval tevent_timeval_add (const struct timeval *tv, uint32_tsecs, uint32_tusecs)</h3>
<p>Add the given amount of time to a timeval structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tv</i> The timeval structure to add the time.<br />
 <i>secs</i> The seconds to add to the timeval.<br />
 <i>usecs</i> The microseconds to add to the timeval.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The timeval structure with the new time.</dl>
<h3>int tevent_timeval_compare (const struct timeval *tv1, const struct timeval *tv2)</h3>
<p>Compare two timeval values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tv1</i> The first timeval value to compare.<br />
 <i>tv2</i> The second timeval value to compare.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if they are equal. 1 if the first time is greater than the second. -1 if the first time is smaller than the second.</dl>
<p> Compare two timeval values. </p>
<p> Return -1 if tv1 &lt; tv2 Return 0 if tv1 == tv2 Return 1 if tv1 &gt; tv2</p>
<h3>struct timeval tevent_timeval_current (void)</h3>
<p>Get a timeval value for the current time. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>A timval value with the current time.</dl>
<p> Get a timeval value for the current time.</p>
<h3>struct timeval tevent_timeval_current_ofs (uint32_tsecs, uint32_tusecs)</h3>
<p>Get a timeval in the future with a specified offset from now. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>secs</i> The seconds of the offset from now.<br />
 <i>usecs</i> The microseconds of the offset from now.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A timval with the given offset in the future.</dl>
<p> Get a timeval in the future with a specified offset from now.</p>
<h3>bool tevent_timeval_is_zero (const struct timeval *tv)</h3>
<p>Check if a given timeval structure is zero. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tv</i> The timeval to check if it is zero.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if it is zero, false otherwise.</dl>
<p> Check if a given timeval structure is zero.</p>
<h3>struct timeval tevent_timeval_set (uint32_tsecs, uint32_tusecs)</h3>
<p>Get a timeval structure with the given values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>secs</i> The seconds to set.<br />
 <i>usecs</i> The microseconds to set.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A timeval structure with the given values.</dl>
<p> Get a timeval structure with the given values.</p>
<h3>struct timeval tevent_timeval_until (const struct timeval *tv1, const struct timeval *tv2)</h3>
<p>Get the difference between two timeval values. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tv1</i> The first timeval.<br />
 <i>tv2</i> The second timeval.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A timeval structure with the difference between the first and the second value.</dl>
<p> Get the difference between two timeval values.</p>
<h3>struct timeval tevent_timeval_zero (void)</h3>
<p>Get a zero timval value. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>A zero timval value.</dl>
<p> Get a zero timval value.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for tevent from the source code.</p>
