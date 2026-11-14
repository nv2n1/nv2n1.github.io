---
title: "sc_timer(3)"
name: "sc_timer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_timer/"
description: "sc::Timer –"
---

<p>sc::Timer &#8211; </p>
<p> The <code>Timer</code> class uses <code>RegionTimer</code> to time intervals in an exception safe manner.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;regtime.h&gt;

Public Member Functions</code></pre>
<p> <code>Timer</code> (const char *name)<br />
 <i>Start timing a region using the default </i><code>RegionTimer</code> and activate the timer.<br />
 <code>Timer</code> (const <code>Ref</code>&lt; <code>RegionTimer</code> &gt; &amp;, const char *name)<br />
 <i>Start timing a region using the given </i><code>RegionTimer</code>.<br />
 <code>~Timer</code> ()<br />
 <i>Stop timing a region, if active. </i><br />
 void <code>reset</code> (const char *=0)<br />
 <i>Stop timing the current region, if active. </i></p>
<h2>Detailed Description</h2>
<p>The <code>Timer</code> class uses <code>RegionTimer</code> to time intervals in an exception safe manner. </p>
<p> It will automatically call RegionTimer::enter when its constructor is called and RegionTimer::exit when its destructor is called. The reset member can also result in RegionTimer&#8217;s enter and exit routines being called. The programmer is responsible for making sure that timers are exited in the reverse of the order that they are entered.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Timer::Timer (const char * name)</h3>
<p>Start timing a region using the default <code>RegionTimer</code> and activate the timer. If a null name pointer is given, then the timer will not be activated.</p>
<h3>sc::Timer::Timer (const <code>Ref</code>&lt; <code>RegionTimer</code> &gt; &amp;, const char * name)</h3>
<p>Start timing a region using the given <code>RegionTimer</code>. If a null name pointer is given, then the timer will not be activated.</p>
<h3>sc::Timer::~Timer ()</h3>
<p>Stop timing a region, if active.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::Timer::reset (const char * = 0)</h3>
<p>Stop timing the current region, if active. If a new region name is passed in, start timing with that name. If no region name is given, the <code>Timer</code> will be deactivated.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
