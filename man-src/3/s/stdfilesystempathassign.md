---
title: "stdfilesystempathassign(3)"
name: "stdfilesystempathassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathassign/"
---

std::filesystem::path::assign - std::filesystem::path::assign

<h2>Synopsis</h2>

<pre><code>path &amp;assign(string_type &amp;&amp;source);
(1)(since C++ 17)

    template &lt;class Source&gt;
    (2)(since C++ 17)

        path &amp;assign(const Source &amp;source);

template &lt;class InputIt&gt;
(3)(since C++ 17)

    path &amp;assign(InputIt first, InputIt last);</code></pre> 
Replaces the contents to the path object by a new pathname constructed from the given character sequence. 
1) Assigns the pathname identified by the detected-format string source, which is left in valid, but unspecified state. 
2) Assigns the pathname identified by the detected-format character range source. 
3) Assigns the pathname identified by detected-format character range [first, last). 

<h2>Parameters</h2>

source - a character range to use, represented as std::string, std::string_view, pointer to a null-terminated multibyte string, or as an input iterator with char value type that points to a null-terminated multibyte string 
first, last - a character range to use

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
The value type of InputIt must be one of the encoded character types (char, wchar_t, char16_t and char32_t)

<h2>Return value</h2>

*this 

<h2>See also</h2>

<pre><code>assigns another path

operator= (public member function)




</code></pre>
