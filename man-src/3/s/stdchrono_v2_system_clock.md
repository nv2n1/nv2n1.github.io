---
title: "stdchrono_v2_system_clock(3)"
name: "stdchrono_v2_system_clock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchrono_v2_system_clock/"
description: "std::chrono::_V2::system_clock –"
---

<p>std::chrono::_V2::system_clock &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>chrono::nanoseconds</code> <code>duration</code> </p>
<p> typedef duration::period <code>period</code> </p>
<p> typedef duration::rep <code>rep</code> </p>
<p> typedef <code>chrono::time_point</code><br />
 &lt; <code>system_clock</code>, <code>duration</code> &gt; <code>time_point</code>&quot;</p>
<h3>Public Member Functions</h3>
<p>&lt; system_clock::duration::zero(),&#8217;aclock&#8217;sminimumdurationcannotbelessthanitsepoch&#8217;);staticconstexprboolis_steady=false;statictime_pointnow()<br />
 noexcept;staticstd::time_tto_time_t(consttime_point<br />
 &amp;__t) noexcept{returnstd::time_t(<code>duration_cast</code><br />
 &lt; <code>chrono::seconds</code> &gt; __t <code>time_since_epoch</code> ()).<code>count</code>())&quot;</p>
<h3>Static Public Member Functions</h3>
<pre><code>static time_point from_time_t (std::time_t __t) noexcept</code></pre>
<h2>Detailed Description</h2>
<p>System clock. </p>
<p> Time returned represents wall time from the system-wide clock. </p>
<p> Definition at line 715 of file chrono.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
