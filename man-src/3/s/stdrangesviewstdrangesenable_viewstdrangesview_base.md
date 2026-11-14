---
title: "stdrangesviewstdrangesenable_viewstdrangesview_base(3)"
name: "stdrangesviewstdrangesenable_viewstdrangesview_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewstdrangesenable_viewstdrangesview_base/"
---

std::ranges::View,std::ranges::enable_view,std::ranges::view_base - std::ranges::View,std::ranges::enable_view,std::ranges::view_base

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ranges&gt;

    template &lt;class T&gt;
    (1)

        concept View = Range&lt;T&gt; &amp;&amp; Semiregular&lt;T&gt; &amp;&amp; enable_view&lt;T&gt;;

template &lt;class T&gt;
(2)

    inline constexpr bool enable_view = /*see description*/;

struct view_base {
};
(3)</code></pre> 
1) The View concept specifies the requirements of a Range type that has constant time copy, move, and assignment operations (e.g. a pair of iterators, or a generator Range that creates its elements on-demand. Notably, the standard library containers are Ranges, but not Views) 
2) The enable_view variable template is used to indicate that whether a Range is a View, as follows: 
For a type T, the default value of enable_view&lt;T&gt; is: 
* If DerivedFrom&lt;T, view_base&gt; is true, enable_view&lt;T&gt; is true. 
* Otherwise, if T is a specialization of class template std::initializer_list, std::set, std::multiset, std::unordered_set, std::unordered_multiset, std::match_results, enable_view&lt;T&gt; is false 
* Otherwise, if both T and const T model Range and iter_reference_t&lt;iterator_t&lt;T&gt;&gt; is not the same type as iter_reference_t&lt;iterator_t&lt;const T&gt;&gt;, enable_view&lt;T&gt; is false. (in other words, deep constness implies element ownership, shallow constness implies reference (view) semantics) 
* Otherwise, enable_view&lt;T&gt; is true. 
3) Deriving from view_base enables Range types to model View. 

<h2>Notes</h2>

Users may derive from view_base or specialize enable_view to true for types which model View, and specialize enable_view to false for types which do not. 
