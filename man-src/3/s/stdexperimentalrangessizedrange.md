---
title: "stdexperimentalrangessizedrange(3)"
name: "stdexperimentalrangessizedrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessizedrange/"
---

std::experimental::ranges::SizedRange - std::experimental::ranges::SizedRange

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/range&gt;

template &lt;class T&gt;

concept bool SizedRange =

Range&lt;T&gt; &amp;&amp;

!ranges::disable_sized_range&lt;std::remove_cv_t&lt;std::remove_reference_t&lt;T&gt;&gt;&gt; &amp;&amp;  (ranges TS)

requires(T&amp; t) {

    { ranges::size(t) }

    -&gt; ConvertibleTo&lt;ranges::difference_type_t&lt;ranges::iterator_t&lt;T&gt;&gt;&gt;;

};
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
