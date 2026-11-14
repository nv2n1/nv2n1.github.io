---
title: "stdfilesystemswapstdfilesystempath(3)"
name: "stdfilesystemswapstdfilesystempath"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemswapstdfilesystempath/"
---

std::filesystem::swap(std::filesystem::path) - std::filesystem::swap(std::filesystem::path)

<h2>Synopsis</h2>

<pre><code>void swap(path &amp;lhs, path &amp;rhs) noexcept;
(since C++ 17)</code></pre> 
Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - paths whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two paths 
swap <i>(public member function)</i> 
