---
title: "qwtsystemclock(3)"
name: "qwtsystemclock"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsystemclock/"
description: "QwtSystemClock –"
---

<p>QwtSystemClock &#8211; </p>
<p> <code>QwtSystemClock</code> provides high resolution clock time functions.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_system_clock.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtSystemClock</code> ()<br />
 <i>Constructs a null clock object. </i><br />
 virtual <code>~QwtSystemClock</code> ()<br />
 <i>Destructor. </i><br />
 bool <code>isNull</code> () const </p>
<p> void <code>start</code> () </p>
<p> double <code>restart</code> () </p>
<p> double <code>elapsed</code> () const </p>
<h2>Detailed Description</h2>
<p><code>QwtSystemClock</code> provides high resolution clock time functions. </p>
<p> Sometimes the resolution offered by QTime ( millisecond ) is not accurate enough for implementing time measurements ( f.e. sampling ). <code>QwtSystemClock</code> offers a subset of the QTime functionality using higher resolution timers ( if possible ). </p>
<p> Precision and time intervals are multiples of milliseconds (ms). </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The implementation uses high-resolution performance counter on Windows, mach_absolute_time() on the Mac or POSIX timers on other systems. If none is available it falls back on QTimer.</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtSystemClock::elapsed () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of milliseconds that have elapsed since the last time <code>start()</code> or <code>restart()</code> was called or 0.0 for null clocks.</dl>
<h3>bool QwtSystemClock::isNull () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if the clock has never been started.</dl>
<h3>double QwtSystemClock::restart ()</h3>
<p>Set the start time to the current time </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Time, that is elapsed since the previous start time.</dl>
<h3>void QwtSystemClock::start ()</h3>
<p>Sets the start time to the current time. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
