---
title: "stdfilesystempathconcatstdfilesystempathoperator(3)"
name: "stdfilesystempathconcatstdfilesystempathoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathconcatstdfilesystempathoperator/"
---

std::filesystem::path::concat,std::filesystem::path::operator+= - std::filesystem::path::concat,std::filesystem::path::operator+=

<h2>Synopsis</h2>

<pre><code>path &amp;operator+=(const path &amp;p);
(1)(since C++ 17)

    path &amp;
    operator+=(const string_type &amp;str);
(2)(since C++ 17)

    path &amp;
    operator+=(std::basic_string_view&lt;value_type&gt; str);

path &amp;operator+=(const value_type *ptr);
(3)(since C++ 17)

    path &amp;
    operator+=(value_type x);
(4)(since C++ 17)

    template &lt;class Source&gt;
    (5)(since C++ 17)

        path &amp;
        operator+=(const Source &amp;source);

template &lt;class CharT&gt;
(6)(since C++ 17)

    path &amp;
    operator+=(CharT x);

template &lt;class Source&gt;
(7)(since C++ 17)

    path &amp;concat(const Source &amp;source);

template &lt;class InputIt&gt;
(8)(since C++ 17)

    path &amp;concat(InputIterator first, InputIterator last);
Concatenates the current path and the argument

1-7) Appends path(other).native() to the pathname stored in *this in the native format. This directly manipulates the value of native() and may not be portable between operating systems.

8) Same as return *this += path(first, last)
</code></pre>

<h2>Parameters</h2>

p - path to append 
str - string or string view to append 
ptr - pointer to the beginning of a null-terminated string to append 
x - single character to append 
source - std::basic_string, std::basic_string_view, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence, which represents a path name (either in portable or in native format) 
first, last - pair of LegacyInputIterators that specify a multicharacter sequence that represents a path name

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
The value type of InputIt must be one of the encoded character types (char, wchar_t, char16_t and char32_t) 
- 
CharT must be one of the encoded character types (char, wchar_t, char16_t and char32_t)

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

May throw std::bad_alloc if memory allocation fails.

<h2>Notes</h2>

Unlike with append() or operator/=, additional directory separators are never introduced. 

<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()
{
    fs::path p1; // empty path
    p1 += &quot;var&quot;; // does not insert a separator
    std::cout &lt;&lt; &quot;\&quot;\&quot; + \&quot;var\&quot; == &quot; &lt;&lt; p1 &lt;&lt; '\n';
    p1 += &quot;lib&quot;; // does not insert a separator
    std::cout &lt;&lt; &quot;\&quot;\&quot; + \&quot;var\&quot; + \&quot;lib\&quot; == &quot; &lt;&lt; p1 &lt;&lt; '\n';
}


<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;&quot; + &quot;var&quot; == &quot;var&quot; 
&nbsp;<wbr>&nbsp;&quot;&quot; + &quot;var&quot; + &quot;lib&quot; == &quot;varlib&quot;

<h2>See also</h2>

<pre><code>appends elements to the path with a directory separator

append     (public member function)

operator/=
concatenates two paths with a directory separator

operator/  (function)




</code></pre>
