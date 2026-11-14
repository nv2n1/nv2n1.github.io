---
title: "wfmath_timediff(3)"
name: "wfmath_timediff"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_timediff/"
description: "WFMath::TimeDiff – The difference between two timestamps."
---

<p>WFMath::TimeDiff &#8211; The difference between two timestamps. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/timestamp.h">timestamp.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>TimeDiff</code> ()<br />
 <i>construct an uninitialized </i><code>TimeDiff</code><br />
 <code>TimeDiff</code> (long msec)<br />
 <i>construct a </i><code>TimeDiff</code> of a given number of milliseconds<br />
 long <code>milliseconds</code> () const<br />
 <i>Get the value of a </i><code>TimeDiff</code> in milliseconds.<br />
 std::pair&lt; long, long &gt; <code>full_time</code> () const<br />
 <i>Get the value of a </i><code>TimeDiff</code> in (seconds, microseconds).<br />
 <code>TimeDiff</code> <code>operator-</code> () const<br />
 <i>negate a </i><code>TimeDiff</code></p>
<h3>Friends</h3>
<p><code>TimeDiff</code> &amp; <code>operator+=</code> (<code>TimeDiff</code> &amp;, const <code>TimeDiff</code> &amp;)<br />
 <i>increment a </i><code>TimeDiff</code><br />
 <code>TimeDiff</code> &amp; <code>operator-=</code> (<code>TimeDiff</code> &amp;, const <code>TimeDiff</code> &amp;)<br />
 <i>decrement a </i><code>TimeDiff</code><br />
 <code>TimeDiff</code> <code>operator+</code> (const <code>TimeDiff</code> &amp;a, const <code>TimeDiff</code> &amp;b)<br />
 <i>add two </i><code>TimeDiff</code> instances<br />
 <code>TimeDiff</code> <code>operator-</code> (const <code>TimeDiff</code> &amp;a, const <code>TimeDiff</code> &amp;b)<br />
 <i>subtract two </i><code>TimeDiff</code> instances<br />
 <code>TimeStamp</code> &amp; <code>operator+=</code> (<code>TimeStamp</code> &amp;, const <code>TimeDiff</code> &amp;)<br />
 <i>advance a </i><code>TimeStamp</code> by a <code>TimeDiff</code><br />
 <code>TimeStamp</code> &amp; <code>operator-=</code> (<code>TimeStamp</code> &amp;, const <code>TimeDiff</code> &amp;)<br />
 <i>regress a </i><code>TimeStamp</code> by a <code>TimeDiff</code><br />
 <code>TimeStamp</code> <code>operator+</code> (const <code>TimeStamp</code> &amp;a, const <code>TimeDiff</code> &amp;msec)<br />
 <i>find the result of advancing a </i><code>TimeStamp</code><br />
 <code>TimeStamp</code> <code>operator-</code> (const <code>TimeStamp</code> &amp;a, const <code>TimeDiff</code> &amp;msec)<br />
 <i>find the result of regressing a </i><code>TimeStamp</code><br />
 <code>TimeDiff</code> <code>operator-</code> (const <code>TimeStamp</code> &amp;a, const <code>TimeStamp</code> &amp;b)<br />
 <i>find the time difference between two time stamps </i></p>
<h2>Detailed Description</h2>
<p>The difference between two timestamps. </p>
<p> This class implements the &#8216;generic&#8217; subset of the interface in the fake class <code>Shape</code>, with the exception of the stream operators. It also has the full set of comparison * operators (&lt;, &lt;=, &gt;, &gt;=, ==, !=).</p>
<h2>Member Function Documentation</h2>
<h3>long WFMath::TimeDiff::milliseconds () const</h3>
<p>Get the value of a <code>TimeDiff</code> in milliseconds. </p>
<p> WARNING! This function does not check for overflow, if the number of milliseconds is large </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
