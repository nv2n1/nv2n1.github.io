---
title: "stdchrono_v2_steady_clock(3)"
name: "stdchrono_v2_steady_clock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchrono_v2_steady_clock/"
description: "std::chrono::_V2::steady_clock –"
---

<p>std::chrono::_V2::steady_clock &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>chrono::nanoseconds</code> <code>duration</code> </p>
<p> typedef duration::period <code>period</code> </p>
<p> typedef duration::rep <code>rep</code> </p>
<p> typedef <code>chrono::time_point</code><br />
 &lt; <code>steady_clock</code>, <code>duration</code> &gt; <code>time_point</code>&quot;</p>
<h3>Static Public Member Functions</h3>
<pre><code>static time_point now () noexcept



Static Public Attributes
static constexpr bool is_steady</code></pre>
<h2>Detailed Description</h2>
<p>Monotonic clock. </p>
<p> Time returned has the property of only increasing at a uniform rate. </p>
<p> Definition at line 754 of file chrono.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
