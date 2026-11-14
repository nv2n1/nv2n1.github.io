---
title: "stdexperimentalrangesview(3)"
name: "stdexperimentalrangesview"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesview/"
---

std::experimental::ranges::View - std::experimental::ranges::View

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / range&gt;

    template &lt;class T&gt;

    concept bool View = Range&lt;T&gt; &amp;&amp; Semiregular&lt;T&gt;(ranges TS)

                                        &amp;&amp; /* view-predicate&lt;T&gt; */;

template &lt;class T&gt;
(ranges TS)

    struct enable_view {
};

struct view_base {
};
(ranges TS)</code></pre> 
The concept View&lt;T&gt; specifies the semiregular range T has constant-time copy, move, and assignment operations. 
The /* view-predicate&lt;T&gt; */ portion of the concept is determined as follows: 
* if the qualified-id ranges::enable_view&lt;T&gt;::type is valid and denotes a type, ranges::enable_view&lt;T&gt;::type::value; 
* otherwise, if std::is_base_of_v&lt;ranges::view_base, T&gt; is true, true; 
* otherwise, if T is a specialization of std::initializer_list, std::set, std::multiset, std::unordered_set, or std::unordered_multiset, false; 
* otherwise, if both T and const T satisfy Range and ranges::reference_t &lt;ranges::iterator_t&lt;T&gt;&gt; is not the same type as ranges::reference_t&lt;ranges::iterator_t&lt;const T&gt;&gt;, false; 
* otherwise, true. 
