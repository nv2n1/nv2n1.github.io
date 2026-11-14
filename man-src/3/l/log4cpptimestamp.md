---
title: "log4cpptimestamp(3)"
name: "log4cpptimestamp"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpptimestamp/"
description: "log4cpp::TimeStamp –"
---

<p>log4cpp::TimeStamp &#8211; </p>
<p> A simple <code>TimeStamp</code> abstraction.</p>
<h2>Synopsis</h2>
<p>#include &lt;TimeStamp.hh&gt;</p>
<h3>Public Member Functions</h3>
<p><code>TimeStamp</code> ()<br />
 <i>Constructs a </i><code>TimeStamp</code> representing &#8216;now&#8217;.<br />
 <code>TimeStamp</code> (unsigned int seconds, unsigned int microSeconds=0)<br />
 <i>Constructs a </i><code>TimeStamp</code> representing the given offset since the epoch ( 00:00:00 1970/1/1 UTC).<br />
 int <code>getSeconds</code> () const<br />
 <i>Returns the &#8216;seconds&#8217; part of the </i><code>TimeStamp</code>.<br />
 int <code>getMilliSeconds</code> () const<br />
 <i>Returns the &#8216;subseconds&#8217; part of the </i><code>TimeStamp</code> in milliseconds, <code>getMilliSeconds()</code> == <code>getMicroSeconds()</code> / 1000.<br />
 int <code>getMicroSeconds</code> () const<br />
 <i>Returns the subsecond part of the </i><code>TimeStamp</code> in microseconds.</p>
<h3>Static Public Member Functions</h3>
<p>static const <code>TimeStamp</code> &amp; <code>getStartTime</code> ()<br />
 <i>Returns a </i><code>TimeStamp</code> representing the time at which the application started.</p>
<h3>Protected Attributes</h3>
<p>int <code>_seconds</code> </p>
<p> int <code>_microSeconds</code> </p>
<h3>Static Protected Attributes</h3>
<p>static <code>TimeStamp</code> <code>_startStamp</code> </p>
<h2>Detailed Description</h2>
<p>A simple <code>TimeStamp</code> abstraction.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>log4cpp::TimeStamp::TimeStamp ()</h3>
<p>Constructs a <code>TimeStamp</code> representing &#8216;now&#8217;.</p>
<h3>log4cpp::TimeStamp::TimeStamp (unsigned intseconds, unsigned intmicroSeconds = 0)</h3>
<p>Constructs a <code>TimeStamp</code> representing the given offset since the epoch ( 00:00:00 1970/1/1 UTC).</p>
<h2>Member Function Documentation</h2>
<h3>int log4cpp::TimeStamp::getMicroSeconds () const [inline]</h3>
<p>Returns the subsecond part of the <code>TimeStamp</code> in microseconds. The actual precision of this value depends on the platform and may be in the order of milliseconds rather than microseconds.</p>
<h3>int log4cpp::TimeStamp::getMilliSeconds () const [inline]</h3>
<p>Returns the &#8216;subseconds&#8217; part of the <code>TimeStamp</code> in milliseconds, <code>getMilliSeconds()</code> == <code>getMicroSeconds()</code> / 1000.</p>
<h3>int log4cpp::TimeStamp::getSeconds () const [inline]</h3>
<p>Returns the &#8216;seconds&#8217; part of the <code>TimeStamp</code>.</p>
<h3>static const <code>TimeStamp</code>&amp; log4cpp::TimeStamp::getStartTime () [inline], [static]</h3>
<p>Returns a <code>TimeStamp</code> representing the time at which the application started.</p>
<h2>Member Data Documentation</h2>
<h3>int log4cpp::TimeStamp::_microSeconds [protected]</h3>
<h3>int log4cpp::TimeStamp::_seconds [protected]</h3>
<h3><code>LOG4CPP_EXPORT</code> <code>TimeStamp</code> log4cpp::TimeStamp::_startStamp [static], [protected]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
