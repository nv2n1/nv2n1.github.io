---
title: "stdexperimentalfilesystempathassign(3)"
name: "stdexperimentalfilesystempathassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathassign/"
---

std::experimental::filesystem::path::assign - std::experimental::filesystem::path::assign

<h2>Synopsis</h2>

<pre><code>template &lt;class Source&gt;
(1)(filesystem TS)

    path &amp;assign(const Source &amp;source);

template &lt;class InputIt&gt;
(2)(filesystem TS)

    path &amp;assign(InputIt first, InputIt last);</code></pre> 
Assigns the contents to the path object. 
1) Assigns the range of source. 
&nbsp;This section is incomplete 
2) Assigns the pathname identified by range [first, last). 

<h2>Parameters</h2>

source - a range to assign 
first, last - a range to assign

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
The value type of InputIt must be one of the encoded character types (char, wchar_t, char16_t and char32_t) 

 
|}

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

&nbsp;This section is incomplete

<h2>See also</h2>

<pre><code>assigns another path

operator= (public member function)




</code></pre>
