---
title: "stdrangesviewemptystdrangesempty_view(3)"
name: "stdrangesviewemptystdrangesempty_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewemptystdrangesempty_view/"
description: "std::ranges::view::empty,std::ranges::empty_view – std::ranges::view::empty,std::ranges::empty_view"
---

<p>std::ranges::view::empty,std::ranges::empty_view &#8211; std::ranges::view::empty,std::ranges::empty_view</p>
<h2>Synopsis</h2>
<pre><code>template&lt;class T&gt;

requires is_object_v&lt;T&gt;                                   (1) (since C++20)

class empty_view : public view_interface&lt;empty_view&lt;T&gt;&gt;

namespace view {

    template&lt;class T&gt; inline constexpr empty_view&lt;T&gt; empty{}; (2) (since C++20)

}</code></pre>
<p>1) A range adaptor that produces a View of no elements of a particular type.<br />
2) Variable template for empty_view. </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::empty_view::begin </p>
<p>static constexpr T* begin() noexcept { return nullptr; } </p>
<p>empty_view does not reference any element. </p>
<p>&nbsp;std::ranges::empty_view::end </p>
<p>static constexpr T* end() noexcept { return nullptr; } </p>
<p>empty_view does not reference any element. </p>
<p>&nbsp;std::ranges::empty_view::data </p>
<p>static constexpr T* data() noexcept { return nullptr; } </p>
<p>empty_view does not reference any element. </p>
<p>&nbsp;std::ranges::empty_view::size </p>
<p>static constexpr std::ptrdiff_t size() noexcept { return 0; } </p>
<p>empty_view is always empty. </p>
<p>&nbsp;std::ranges::empty_view::empty </p>
<p>static constexpr bool empty() noexcept { return true; } </p>
<p>empty_view is always empty.</p>
<h2>Non-member functions</h2>
<p>&nbsp;begin, end(std::ranges::empty_view) </p>
<p>friend constexpr T* begin(empty_view) noexcept { return nullptr; } <code>(1)</code><br />
friend constexpr T* end(empty_view) noexcept { return nullptr; } <code>(2)</code> </p>
<p>These functions are not visible to ordinary unqualified or qualified_lookup, and can only be found by argument-dependent_lookup when std::ranges::empty_view&lt;T&gt; is an associated class of the arguments.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;ranges&gt;
int main()

{
    std::ranges::empty_view&lt;int&gt; e;
    static_assert(std::ranges::empty(e));
    static_assert(0 == e.size());
}
</code></pre>
