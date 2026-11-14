---
title: "beginendstdbasic_string_view(3)"
name: "beginendstdbasic_string_view"
section: "3"
letter: "b"
url: "/docs/linux/man/3-beginendstdbasic_string_view/"
description: "begin,end(std::basic_string_view) – begin,end(std::basic_string_view)"
---

<p>begin,end(std::basic_string_view) &#8211; begin,end(std::basic_string_view)</p>
<h2>Synopsis</h2>
<p>constexpr const_iterator begin(basic_string_view sv) noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr const_iterator end(basic_string_view sv) noexcept; <code>(2)</code> <i>(since C++20)</i> </p>
<p>1) Returns an iterator to the first character of the view. Equivalent to sv.begin().<br />
2) Returns an iterator to the character following the last character of the view. Equivalent to sv.end().<br />
These functions are not visible to ordinary unqualified or qualified_lookup, and can only be found by argument-dependent_lookup when std::basic_string_view&lt;CharT, Traits&gt; is an associated class of the arguments. </p>
<h2>Parameters</h2>
<p>sv &#8211; a string_view </p>
<h2>Return value</h2>
<p>1) sv.begin()<br />
2) sv.end() </p>
<h2>Notes</h2>
<p>These functions are provided to make string_view rvalues work with std::ranges::begin and std::ranges::end, which reject rvalue arguments by default in order to prevent dangling iterator.</p>
