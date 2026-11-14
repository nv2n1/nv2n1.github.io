---
title: "stdrangesviewiotastdrangesiota_view(3)"
name: "stdrangesviewiotastdrangesiota_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewiotastdrangesiota_view/"
description: "std::ranges::view::iota,std::ranges::iota_view – std::ranges::view::iota,std::ranges::iota_view"
---

<p>std::ranges::view::iota,std::ranges::iota_view &#8211; std::ranges::view::iota,std::ranges::iota_view</p>
<h2>Synopsis</h2>
<pre><code>template&lt;WeaklyIncrementable W, Semiregular Bound = unreachable_sentinel_t&gt;

requires _WeaklyEqualityComparableWith&lt;W, Bound&gt;                            (1) (since C++20)

class iota_view : public view_interface&lt;iota_view&lt;W, Bound&gt;&gt;

namespace view {

    inline constexpr /*unspecified*/ iota = /*unspecified*/;                    (2) (since C++20)

}</code></pre>
<p>1) A range factory that generates a sequence of elements by repeatedly incrementing an initial value. Can be both bounded and unbounded (infinite)<br />
2) view::iota(E) and view::iota(E, F) are expression-equivalent to (has the same effect as) iota_view{E} and iota_view{E, F} respectively for any suitable subexpressions E and F<br />
Data members<br />
&nbsp;std::ranges::iota_view::base_ W value_ = W(); /* exposition-only */<br />
the current value<br />
&nbsp;std::ranges::iota_view::pred_ Bound bound_ = Bound(); /* exposition-only */<br />
the bound (defaults to std::unreachable_sentinel_t) </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::iota_view::iota_view </p>
<p>iota_view() = default; <code>(1)</code><br />
constexpr explicit iota_view(W value); <code>(2)</code><br />
constexpr iota_view(std::type_identity_t&lt;W&gt; value, <code>(3)</code><br />
std::type_identity_t&lt;Bound&gt; bound); </p>
<p>1) Default-initializes value_ and bound_<br />
2) Initializes value_ with value and expects that Bound is either unreachable_­sentinel_­t (the default) or Bound() is reachable from value. This constructor is used to create unbounded iota views, e.g. iota<code>(0)</code> yields numbers 0,1,2&#8230;, infinitely.<br />
3) Initializes value_ with value and bound_ with bound. This constructor is used to create bounded iota views, e.g. iota(10, 20) yields numbers from 10 to 19.</p>
<h2>Parameters</h2>
<p>value &#8211; the starting value<br />
bound &#8211; the bound </p>
<p>&nbsp;std::ranges::iota_view::begin </p>
<p>constexpr iterator begin(); </p>
<p>Returns the iterator initialized with value_ </p>
<p>&nbsp;std::ranges::iota_view::end </p>
<p>constexpr sentinel end() const; <code>(1)</code><br />
constexpr iterator end() const requires Same&lt;W, Bound&gt;; <code>(2)</code> </p>
<p>Returns the iterator initialized with bound_ if this view is bounded, or the sentinel initialized with bound_ if this view is unbounded. </p>
<p>&nbsp;std::ranges::iota_view::size </p>
<p>constexpr auto size() const<br />
requires (Same&lt;W, Bound&gt; &amp;&amp; _Advanceable&lt;W&gt;) ||<br />
(Integral&lt;W&gt; &amp;&amp; Integral&lt;Bound&gt;) ||<br />
SizedSentinel&lt;Bound, W&gt;<br />
{ return bound_ &#8211; value_; } </p>
<p>Returns the size of the view if the view is bounded. </p>
<p>Deduction guides </p>
<p>template&lt;class W, class Bound&gt;<br />
requires (!Integral&lt;W&gt; || !Integral&lt;Bound&gt; || is_signed_v&lt;W&gt; == is_signed_v&lt;Bound&gt;)<br />
iota_view(W, Bound) -&gt; iota_view&lt;W, Bound&gt;; </p>
<p>Note that the guide protects itself against signed/unsigned mismatch bugs, like view::iota(0, v.size()), where 0 is a (signed) int and v.size() is an (unsigned) std::size_t. </p>
<p>Nested classes </p>
<p>&nbsp;std::ranges::iota_view::iterator </p>
<p>template&lt;class W, class Bound&gt;<br />
struct iota_view&lt;W, Bound&gt;::iterator /* exposition-only */ </p>
<p>The return type of iota_view::begin.<br />
This is a RandomAccessIterator if W models _Advanceable, a BidirectionalIterator if W models _Decrementable, a ForwardIterator if W models Incrementable, and InputIterator otherwise. </p>
<p>&nbsp;std::ranges::iota_view::iterator::iterator </p>
<p>constexpr explicit iterator(W value); </p>
<p>Initializes exposition-only data member value_ with value. This value will be returned by operator* and incremented by operator++ </p>
<p>&nbsp;std::ranges::iota_view::iterator::operator* </p>
<p>constexpr W operator*() const noexcept(is_nothrow_copy_constructible_v&lt;W&gt;); </p>
<p>returns the current value, by value (in other words, this is a read-only view) </p>
<p>&nbsp;std::ranges::iota_view::iterator::operator++ </p>
<p>constexpr iterator&amp; operator++() </p>
<p>Equivalent to </p>
<p>&nbsp;<wbr>&nbsp;++value_;<br />
&nbsp;<wbr>&nbsp;return *this; </p>
<p>&nbsp;std::ranges::iota_view::iterator::operator&#8211; </p>
<p>constexpr iterator&amp; operator&#8211;() requires _Decrementable&lt;W&gt;; </p>
<p>Equivalent to </p>
<p>&nbsp;<wbr>&nbsp;&#8211;value_;<br />
&nbsp;<wbr>&nbsp;return *this; </p>
<p>&nbsp;std::ranges::iota_view::iterator::operator[] </p>
<p>constexpr W operator[](difference_type n) const requires _Advanceable&lt;W&gt;; </p>
<p>Equivalent to </p>
<p>&nbsp;<wbr>&nbsp;return value_­ + n; </p>
<p>Other members as expected of an iterator. </p>
<p>&nbsp;std::ranges::iota_view::sentinel </p>
<p>template&lt;class W, class Bound&gt;<br />
struct iota_view&lt;W, Bound&gt;::sentinel /* exposition-only */ </p>
<p>The return type of iota_view::end. </p>
<p>&nbsp;std::ranges::iota_view::sentinel::bound_ </p>
<p>Bound bound_ = Bound();; /* exposition only */ </p>
<p>Exposition-only data member holding the sentinel (typically either a number, for a bounded iota view, or an instance of std::unreachable_sentinel_t for an unbounded iota view. </p>
<p>&nbsp;std::ranges::iota_view::sentinel::sentinel </p>
<p>entinel() = default;<br />
constexpr explicit sentinel(Bound bound); </p>
<p>Initializes exposition-only data member bound_ with bound. </p>
<p>&nbsp;std::ranges::iota_view::sentinel::operator== </p>
<p>friend constexpr bool operator==(const iterator&amp; x, const sentinel&amp; y);<br />
friend constexpr bool operator==(const sentinel&amp; x, const iterator&amp; y); </p>
<p>Equivalent to: x.value_­ == y.bound_­; and return y == x; respectively. </p>
<p>&nbsp;std::ranges::iota_view::sentinel::operator!= </p>
<p>friend constexpr bool operator!=(const iterator&amp; x, const sentinel&amp; y);<br />
friend constexpr bool operator!=(const sentinel&amp; x, const iterator&amp; y); </p>
<p>Equivalent to return !(x == y); and return !(y == x); respectively</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;ranges&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
int main()

{
    for (int i : std::view::iota{1, 10})
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    for (int i : std::view::iota(1) | std::view::take(9))
        std::cout &lt;&lt; i &lt;&lt; ' ';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 9<br />
&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 9</p>
