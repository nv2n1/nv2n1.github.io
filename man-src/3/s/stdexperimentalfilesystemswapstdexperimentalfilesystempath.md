---
title: "stdexperimentalfilesystemswapstdexperimentalfilesystempath(3)"
name: "stdexperimentalfilesystemswapstdexperimentalfilesystempath"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemswapstdexperimentalfilesystempath/"
---

std::experimental::filesystem::swap(std::experimental::filesystem::path) - std::experimental::filesystem::swap(std::experimental::filesystem::path)

<h2>Synopsis</h2>

<pre><code>void swap(path &amp;lhs, path &amp;rhs);
(filesystem TS)</code></pre> 
Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - paths whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two paths 
swap <i>(public member function)</i> 
