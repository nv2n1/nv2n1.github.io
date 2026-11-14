---
title: "stdexperimentalsource_locationsource_location(3)"
name: "stdexperimentalsource_locationsource_location"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsource_locationsource_location/"
description: "std::experimental::source_location::source_location – std::experimental::source_location::source_location"
---

<p>std::experimental::source_location::source_location &#8211; std::experimental::source_location::source_location</p>
<h2>Synopsis</h2>
<pre><code>constexpr source_location() noexcept;
(1)(library fundamentals TS v2)

    source_location(const source_location &amp;other) = default;
(2)(library fundamentals TS v2)(implicitly declared)

    source_location(source_location &amp;&amp;other) = default;
(3)(library fundamentals TS v2)(implicitly declared)</code></pre>
<p>1) Constructs an source_location object whose values are implementation defined.<br />
2-3) Implicitly declared copy and move constructors. </p>
<h2>Parameters</h2>
<p>other &#8211; another source_location to copy from</p>
<h2>See also</h2>
<p>current constructs a new source_location<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
