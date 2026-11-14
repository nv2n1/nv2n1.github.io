---
title: "stdrangesviewfilterstdrangesfilter_view(3)"
name: "stdrangesviewfilterstdrangesfilter_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewfilterstdrangesfilter_view/"
description: "std::ranges::view::filter,std::ranges::filter_view – std::ranges::view::filter,std::ranges::filter_view"
---

<p>std::ranges::view::filter,std::ranges::filter_view &#8211; std::ranges::view::filter,std::ranges::filter_view</p>
<h2>Synopsis</h2>
<pre><code>template&lt; InputRange V, IndirectUnaryPredicate&lt;iterator_t&lt;V&gt;&gt; Pred &gt;

requires View&lt;V&gt; &amp;&amp; std::is_object_v&lt;Pred&gt;                              (1) (since C++20)

class filter_view : public ranges::view_interface&lt;filter_view&lt;V, Pred&gt;&gt;

namespace view {

    inline constexpr /*unspecified*/ filter = /*unspecified*/;              (2) (since C++20)

}</code></pre>
<p>1) A range adaptor that represents View of an underlying sequence without the elements that fail to satisfy a predicate.<br />
2) The expression view::filter(E, P) is expression-equivalent to (has the same effect as) filter_view{E, P} for any suitable subexpressions E and P.<br />
filter_view models the concepts BidirectionalRange, ForwardRange, InputRange, and CommonRange when the underlying view V models respective concepts.<br />
Data members<br />
&nbsp;std::ranges::filter_view::base_ V base_ = V(); /* exposition-only */<br />
the underlying view<br />
&nbsp;std::ranges::filter_view::pred_<br />
semiregular&lt;Pred&gt; pred_; /* exposition-only */<br />
the predicate used to filter out elements of base_<br />
semiregular is a wrapper class template which behaves exactly like std::optional except for some small differences. The name semiregular is for exposition purposes only and not normative. </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::filter_view::filter_view </p>
<p>filter_view() = default; <code>(1)</code><br />
constexpr filter_view(V base, Pred pred); <code>(2)</code><br />
template&lt;InputRange R&gt;<br />
requires ViewableRange&lt;R&gt; &amp;&amp; Constructible&lt;V, all_view&lt;R&gt;&gt; <code>(3)</code><br />
constexpr filter_view(R&amp;&amp; r, Pred pred); </p>
<p>1) Default-initializes base_ and pred_<br />
2) Initializes base_ with std::move(base) and initializes pred_ with std::move(pred).<br />
3) Initializes base_ with view::all(std::forward&lt;R&gt;(r)) and initializes pred_ with std::move(pred).</p>
<h2>Parameters</h2>
<p>r &#8211; range to filter<br />
pred &#8211; predicate to filter out elements </p>
<p>&nbsp;std::ranges::filter_view::base </p>
<p>constexpr V base() const; </p>
<p>Equivalent to return base_; </p>
<p>&nbsp;std::ranges::filter_view::begin </p>
<p>constexpr iterator begin(); </p>
<p>Returns the iterator initialized with {*this, ranges::find_if(base_, std::ref(*pred_))}. In order to provide the amortized constant time complexity required by the Range concept, this function caches the result within the filter_view object for use on subsequent calls.<br />
The behavior is undefined unless pred_.has_value() </p>
<p>&nbsp;std::ranges::filter_view::end </p>
<p>constexpr auto end() {<br />
if constexpr (CommonRange&lt;V&gt;)<br />
return iterator{*this, ranges::end(base_)};<br />
else<br />
return sentinel{*this};<br />
} </p>
<p>Deduction guides </p>
<p>template&lt;class R, class Pred&gt;<br />
filter_view(R&amp;&amp;, Pred) -&gt; filter_view&lt;all_view&lt;R&gt;, Pred&gt;; </p>
<p>Nested classes </p>
<p>&nbsp;std::ranges::filter_view::iterator </p>
<p>template&lt;class V, class Pred&gt;<br />
class filter_view&lt;V, Pred&gt;::iterator /* exposition-only */ </p>
<p>The return type of filter_view::begin.<br />
This is a BidirectionalIterator if V models BidirectionalRange, a ForwardIterator if V models ForwardRange, and InputIterator otherwise.<br />
Modification of the element denoted by this iterator is permitted, but results in undefined behavior if the resulting value does not satisfy the filter&#8217;s predicate. </p>
<p>&nbsp;std::ranges::filter_view::iterator::iterator </p>
<p>iterator() = default;<br />
constexpr iterator(filter_view&amp; parent, iterator_t&lt;V&gt; current); </p>
<p>Initializes exposition-only data member current_ with current and exposition-only data members parent_ with addressof(parent). </p>
<p>&nbsp;std::ranges::filter_view::iterator::operator++ </p>
<p>constexpr iterator&amp; operator++() </p>
<p>Equivalent to </p>
<p>&nbsp;<wbr>&nbsp;current_ = ranges::find_if(++current_, ranges::end(parent_-&gt;base_), ref(*parent_-&gt;pred_));<br />
&nbsp;<wbr>&nbsp;return *this; </p>
<p>&nbsp;std::ranges::filter_view::iterator::operator&#8211; </p>
<p>constexpr iterator&amp; operator&#8211;() requires BidirectionalRange&lt;V&gt;; </p>
<p>Equivalent to </p>
<p>&nbsp;<wbr>&nbsp;do<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;current_;<br />
&nbsp;<wbr>&nbsp;while (!invoke(*parent_-&gt;pred_, *current_));<br />
&nbsp;<wbr>&nbsp;return *this; </p>
<p>Other members as expected of an iterator. </p>
<p>&nbsp;std::ranges::filter_view::sentinel </p>
<p>template&lt;class V, class Pred&gt;<br />
class filter_view&lt;V, Pred&gt;::sentinel /* exposition-only */ </p>
<p>The return type of filter_view::end. </p>
<p>&nbsp;std::ranges::filter_view::sentinel::end_ </p>
<p>sentinel_t&lt;V&gt; end_ = sentinel_t&lt;V&gt;(); /* exposition only */ </p>
<p>Exposition-only data member holding the sentinel of the underlying View. </p>
<p>&nbsp;std::ranges::filter_view::sentinel::sentinel </p>
<p>sentinel() = default;<br />
constexpr explicit sentinel(filter_view&amp; parent); </p>
<p>Initializes exposition-only data member end_ with parent. </p>
<p>&nbsp;std::ranges::filter_view::sentinel::base </p>
<p>constexpr sentinel_t&lt;V&gt; base() const; </p>
<p>Equivalent to: return end_; </p>
<p>&nbsp;std::ranges::filter_view::sentinel::operator== </p>
<p>friend constexpr bool operator==(const iterator&amp; x, const sentinel&amp; y);<br />
friend constexpr bool operator==(const sentinel&amp; x, const iterator&amp; y); </p>
<p>Equivalent to: return x.current_ == y.end_; and return y == x; respectively. </p>
<p>&nbsp;std::ranges::filter_view::sentinel::operator!= </p>
<p>friend constexpr bool operator!=(const iterator&amp; x, const sentinel&amp; y);<br />
friend constexpr bool operator!=(const sentinel&amp; x, const iterator&amp; y); </p>
<p>Equivalent to return !(x == y); and return !(y == x); respectively</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;vector&gt;

#include &lt;ranges&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; ints{0, 1, 2, 3, 4, 5};
    auto even = [](int i) { return 0 == i % 2; };
    auto square = [](int i) { return i * i; };
    for (int i : ints | std::view::filter(even) | std::view::transform(square)) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0 4 16</p>
