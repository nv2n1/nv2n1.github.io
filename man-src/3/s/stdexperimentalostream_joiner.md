---
title: "stdexperimentalostream_joiner(3)"
name: "stdexperimentalostream_joiner"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalostream_joiner/"
---

std::experimental::ostream_joiner&lt;DelimT,CharT,Traits&gt;::ostream_joiner - std::experimental::ostream_joiner&lt;DelimT,CharT,Traits&gt;::ostream_joiner

<h2>Synopsis</h2>

<pre><code>ostream_joiner(ostream_type &amp;stream, const DelimT &amp;delimiter);
(1)(library fundamentals TS v2)

    ostream_joiner(ostream_type &amp;stream, DelimT &amp;&amp;delimiter);
(2)(library fundamentals TS v2)

    ostream_joiner(const ostream_joiner &amp;other) = default;
(3)(library fundamentals TS v2)(implicitly declared)

    ostream_joiner(ostream_joiner &amp;&amp;other) = default;
(4)(library fundamentals TS v2)(implicitly declared)</code></pre> 
1) Constructs the iterator with the private ostream_type* member initialized with std::addressof(stream), the private delimiter member initialized with delimiter, and the private &quot;first element&quot; flag set to true. 
2) Constructs the iterator with the private ostream_type* member initialized with std::addressof(stream), the private delimiter member initialized with std::move(delimiter), and the private &quot;first element&quot; flag set to true. 
3-4) Implicitly declared copy/move constructor that copy/move constructs the private stream pointer, delimiter, and &quot;first element&quot; flag members. 

<h2>Parameters</h2>

stream - the output stream to be accessed by this iterator 
delimiter - the delimiter to be inserted into the stream in between two outputs 
other - the ostream_joiner object from which this object is to be copy- or move-constructed

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
