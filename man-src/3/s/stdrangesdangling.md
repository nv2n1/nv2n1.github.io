---
title: "stdrangesdangling(3)"
name: "stdrangesdangling"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesdangling/"
description: "std::ranges::dangling – std::ranges::dangling"
---

<p>std::ranges::dangling &#8211; std::ranges::dangling</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;ranges&gt;<br />
struct dangling; <i>(since C++20)</i><br />
dangling is a placeholder type and an empty class type, used together with the template aliases ranges::safe_iterator_t and ranges::safe_subrange_t.<br />
When some constrain_algorithms that usually return an iterator or a subrange of a Range take a particular rvalue Range argument that does not models exposition-only concept __ForwardingRange, dangling will be returned instead to avoid returning potentially dangling results. </p>
<h2>Member functions</h2>
<p>&nbsp;std::ranges::dangling::dangling </p>
<p>constexpr dangling() noexcept = default; <code>(1)</code><br />
template&lt;class&#8230; Args&gt; <code>(2)</code><br />
constexpr dangling(Args&amp;&amp;&#8230;) noexcept { } </p>
<p>1) dangling is trivially default constructible.<br />
2) dangling can be constructed from arguments of arbitrary number and arbitrary non-void type. The construction does not have any side-effect itself.<br />
In other words, after replacing the type (e.g. an iterator type) in a well-formed non-aggregate initialization with dangling, the resulting initialization is also well-formed.</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains iterator type or subrange type of a Range which also models __ForwardingRange<br />
safe_iterator_t (alias template)<br />
safe_subrange_t </p>
