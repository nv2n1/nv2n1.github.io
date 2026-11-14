---
title: "stdrangesref_view(3)"
name: "stdrangesref_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesref_view/"
description: "std::ranges::ref_view – std::ranges::ref_view"
---

<p>std::ranges::ref_view &#8211; std::ranges::ref_view</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ranges&gt;<br />
template&lt;Range R&gt;<br />
requires std::is_object_v&lt;R&gt; <i>(since C++20)</i><br />
class ref_view : public ranges::view_interface&lt;ref_view&lt;R&gt;&gt;<br />
ref_­view is a View of the elements of some other Range. It wraps a reference to that Range.<br />
Data members<br />
&nbsp;std::ranges::ref_view::r_ </p>
<pre><code>R* r_ = nullptr; /* exposition-only */</code></pre>
<p>pointer to the referenced range </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::ref_view::ref_view </p>
<p>constexpr ref_view() noexcept = default; <code>(1)</code><br />
template&lt;__NotSameAs&lt;ref_view&gt; T&gt;<br />
requires /* see below */ <code>(2)</code><br />
constexpr ref_view(T&amp;&amp; t); </p>
<p>1) Initializes r_ with nullptr. A default-initialized ref_view references no Range.<br />
2) Initializes r_ with std::addressof(static_­cast&lt;R&amp;&gt;(std::forward&lt;T&gt;(t))).<br />
__NotSameAs is an exposition-only_helper_concept.<br />
The expression in the requires-clause of <code>(2)</code> is equivalent to ConvertibleTo&lt;T, R&amp;&gt; &amp;&amp; requires { FUN(declval&lt;T&gt;()); }, where the exposition-only functions FUN are declared as void FUN(R&amp;); void FUN(R&amp;&amp;) = delete;.</p>
<h2>Parameters</h2>
<p>t &#8211; range to reference </p>
<p>&nbsp;std::ranges::rev_view::base </p>
<p>constexpr R&amp; base() const; </p>
<p>Equivalent to return *r_; </p>
<p>&nbsp;std::ranges::ref_view::begin </p>
<p>constexpr iterator_t&lt;R&gt; begin() const; </p>
<p>Equivalent to return ranges::begin(*r_); </p>
<p>&nbsp;std::ranges::ref_view::end </p>
<p>constexpr sentinel_t&lt;R&gt; end() const; </p>
<p>Equivalent to return ranges::end(*r_); </p>
<p>&nbsp;std::ranges::ref_view::empty </p>
<p>constexpr bool empty() const<br />
requires requires { ranges::empty(*r_); }; </p>
<p>Equivalent to return ranges::empty(*r_); </p>
<p>&nbsp;std::ranges::ref_view::size </p>
<p>constexpr auto size() const<br />
requires SizedRange&lt;R&gt;<br />
{ return ranges::size(*r_); } </p>
<p>&nbsp;std::ranges::ref_view::data </p>
<p>constexpr auto data() const<br />
requires ContiguousRange&lt;R&gt;<br />
{ return ranges::data(*r_); }</p>
<h2>Non-member functions</h2>
<p>&nbsp;begin, end(std::ranges::ref_view) </p>
<p>friend constexpr iterator_t&lt;R&gt; begin(ref_view r); <code>(1)</code><br />
friend constexpr sentinel_t&lt;R&gt; end(ref_view r); <code>(2)</code> </p>
<p>1) Equivalent to return r.begin();<br />
2) Equivalent to return r.end();<br />
These functions are not visible to ordinary unqualified or qualified_lookup, and can only be found by argument-dependent_lookup when std::ranges::ref_view&lt;R&gt; is an associated class of the arguments. </p>
<p>Deduction guides </p>
<p>template&lt;class R&gt;<br />
ref_view(R&amp;) -&gt; ref_view&lt;R&gt;;</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>reference_wrapper CopyConstructible and CopyAssignable reference wrapper<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a View that includes all elements of a Range<br />
all_view (alias template) (range adaptor object)<br />
view::all </p>
