---
title: "stdrangessafe_iterator_tstdrangessafe_subrange_t(3)"
name: "stdrangessafe_iterator_tstdrangessafe_subrange_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangessafe_iterator_tstdrangessafe_subrange_t/"
description: "std::ranges::safe_iterator_t,std::ranges::safe_subrange_t – std::ranges::safe_iterator_t,std::ranges::safe_subrange_t"
---

<p>std::ranges::safe_iterator_t,std::ranges::safe_subrange_t &#8211; std::ranges::safe_iterator_t,std::ranges::safe_subrange_t</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;ranges&gt;

template&lt;Range R&gt;

using safe_iterator_t = std::conditional_t&lt;__ForwardingRange&lt;R&gt;, (1) (since C++20)

ranges::iterator_t&lt;R&gt;, ranges::dangling&gt;;

template&lt;Range R&gt;

using safe_subrange_t = std::conditional_t&lt;__ForwardingRange&lt;R&gt;, (2) (since C++20)

ranges::subrange&lt;ranges::iterator_t&lt;R&gt;&gt;, ranges::dangling&gt;;</code></pre>
<p>1) Same as ranges::iterator_t when R models exposition-only concept __ForwardingRange, otherwise yields ranges::dangling instead.<br />
2) Similar to <code>(1)</code>, but it yields a specialization of ranges::subrange when the the same condition is met.<br />
These two alias templates are used by some constrained_algorithms to avoid returning potentially dangling iterators or views. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a placeholder type indicating that an iterator or a subrange should not be returned since it would be dangling<br />
dangling <i>(class)</i> </p>
