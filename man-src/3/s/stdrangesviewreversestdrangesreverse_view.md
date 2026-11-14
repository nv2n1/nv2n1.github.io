---
title: "stdrangesviewreversestdrangesreverse_view(3)"
name: "stdrangesviewreversestdrangesreverse_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewreversestdrangesreverse_view/"
description: "std::ranges::view::reverse,std::ranges::reverse_view – std::ranges::view::reverse,std::ranges::reverse_view"
---

<p>std::ranges::view::reverse,std::ranges::reverse_view &#8211; std::ranges::view::reverse,std::ranges::reverse_view</p>
<h2>Synopsis</h2>
<pre><code>template&lt; View V &gt;

requires BidirectionalRange&lt;V&gt;                                      (1) (since C++20)

class reverse_view : public ranges::view_interface&lt;reverse_view&lt;V&gt;&gt;

namespace view {

    inline constexpr /*unspecified*/ reverse = /*unspecified*/;         (2) (since C++20)

}</code></pre>
<p>1) A range adaptor that represents a view of underlying View with reversed order.<br />
2) The expression view::reverse(E) is expression-equivalent to (has the same effect as) one of the following expressions, except that E is evaluated only once:<br />
* E.base(), if the type of E is a (possibly cv-qualified) specialization of reverse_view;<br />
* otherwise, if the type of E is (possibly cv-qualified) ranges::subrange&lt;std::reverse_iterator&lt;I&gt;, std::reverse_iterator&lt;I&gt;, K&gt; for some iterator type I and value K of type ranges::subrange_kind: *ranges::subrange&lt;I, I, K&gt;(E.end().base(), E.begin().base(), E.size()), if K is ranges::subrange_kind::sized;<br />
*otherwise ranges::subrange&lt;I, I, K&gt;(E.end().base(), E.begin().base());</p>
<p>* otherwise ranges::reverse_­view{E}.<br />
In other words, view::reverse unwraps reversed views if possible.<br />
Data members<br />
&nbsp;std::ranges::reverse_view::base_ V base_ = V(); /* exposition-only */<br />
the underlying view </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::reverse_view::reverse_view </p>
<p>reverse_view() = default; <code>(1)</code><br />
constexpr reverse_view(V base); <code>(2)</code><br />
template&lt;ViewableRange R&gt;<br />
requires BidirectionalRange&lt;R&gt; &amp;&amp; Constructible&lt;V, all_view&lt;R&gt;&gt; <code>(3)</code><br />
constexpr reverse_view(R&amp;&amp; r); </p>
<p>1) Value-initializes base_<br />
2) Initializes base_ with std::move(base).<br />
3) Initializes base_ with view::all(std::forward&lt;R&gt;(r)).</p>
<h2>Parameters</h2>
<p>r &#8211; range to reverse </p>
<p>&nbsp;std::ranges::reverse_view::base </p>
<p>constexpr V base() const; </p>
<p>Equivalent to return base_; </p>
<p>&nbsp;std::ranges::reverse_view::begin </p>
<p>constexpr std::reverse_iterator&lt;ranges::iterator_t&lt;V&gt;&gt; begin(); <code>(1)</code><br />
constexpr std::reverse_iterator&lt;ranges::iterator_t&lt;V&gt;&gt; begin() <code>(2)</code><br />
requires CommonRange&lt;V&gt;;<br />
constexpr std::reverse_iterator&lt;ranges::iterator_t&lt;const V&gt;&gt; begin() const <code>(2)</code><br />
requires CommonRange&lt;const V&gt;; </p>
<p>1) Returns std::make_reverse_iterator(ranges::next(ranges::begin(base_), ranges::end(base_))). In order to provide the amortized constant time complexity required by the Range concept, this function caches the result within the reverse_view object for use on subsequent calls.<br />
2) Equivalent to return std::make_­reverse_­iterator(ranges::end(base_­));. </p>
<p>&nbsp;std::ranges::reverse_view::end </p>
<p>constexpr std::reverse_iterator&lt;ranges::iterator_t&lt;V&gt;&gt; end()<br />
requires CommonRange&lt;V&gt;;<br />
constexpr std::reverse_iterator&lt;ranges::iterator_t&lt;const V&gt;&gt; end() const<br />
requires CommonRange&lt;const V&gt;; </p>
<p>Equivalent to return std::make_­reverse_­iterator(ranges::begin(base_­));. </p>
<p>&nbsp;std::ranges::reverse_view::size </p>
<p>constexpr auto size() requires SizedRange&lt;V&gt; {<br />
return ranges::size(base_);<br />
}<br />
constexpr auto size() const requires SizedRange&lt;const V&gt; {<br />
return ranges::size(base_);<br />
} </p>
<p>Returns the size of the view if the view is bounded. </p>
<p>Deduction guides </p>
<p>template&lt;class R&gt;<br />
reverse_view(R&amp;&amp;) -&gt; reverse_view&lt;all_view&lt;R&gt;&gt;;</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;array&gt;

#include &lt;ranges&gt;

#include &lt;iostream&gt;
int main()

{
    std::array&lt;int, 6&gt; il{3, 1, 4, 1, 5, 9};
    std::ranges::reverse_view rv{il};
    for (int i : rv)
        std::cout &lt;&lt; i &lt;&lt; ' ';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;9 5 1 4 1 3</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for reverse-order traversal<br />
reverse_iterator <i>(class template)</i> </p>
