---
title: "beginendstdspan(3)"
name: "beginendstdspan"
section: "3"
letter: "b"
url: "/docs/linux/man/3-beginendstdspan/"
description: "begin,end(std::span) – begin,end(std::span)"
---

<p>begin,end(std::span) &#8211; begin,end(std::span)</p>
<h2>Synopsis</h2>
<p>constexpr iterator begin(span s) noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr iterator end(span s) noexcept; <code>(2)</code> <i>(since C++20)</i> </p>
<p>1) Returns an iterator to the first element of the span. Equivalent to s.begin().<br />
2) Returns an iterator to the element following the last element of the span. Equivalent to s.end().<br />
These functions are not visible to ordinary unqualified or qualified_lookup, and can only be found by argument-dependent_lookup when std::span&lt;T, Extent&gt; is an associated class of the arguments. </p>
<h2>Parameters</h2>
<p>s &#8211; a span </p>
<h2>Return value</h2>
<p>1) s.begin()<br />
2) s.end() </p>
<h2>Notes</h2>
<p>These functions are provided to make span rvalues work with std::ranges::begin and std::ranges::end, which reject rvalue arguments by default in order to prevent dangling iterator.</p>
