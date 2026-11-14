---
title: "stdexperimentalfilesystempathconcat(3)"
name: "stdexperimentalfilesystempathconcat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathconcat/"
description: "std::experimental::filesystem::path::concat,std::experimental::filesystem::path::operator+= – std::experimental::filesystem::path::concat,std::experimental::filesystem::path::operator+="
---

<p>std::experimental::filesystem::path::concat,std::experimental::filesystem::path::operator+= &#8211; std::experimental::filesystem::path::concat,std::experimental::filesystem::path::operator+=</p>
<h2>Synopsis</h2>
<pre><code>path &amp;operator+=(const path &amp;p);
(1)(filesystem TS)

    path &amp;
    operator+=(const string_type &amp;str);
(2)(filesystem TS)

    path &amp;
    operator+=(const value_type *ptr);
(3)(filesystem TS)

    path &amp;
    operator+=(value_type x);
(4)(filesystem TS)

    template &lt;class Source&gt;
    (5)(filesystem TS)

        path &amp;
        operator+=(const Source &amp;source);

template &lt;class CharT&gt;
(6)(filesystem TS)

    path &amp;
    operator+=(CharT x);

template &lt;class Source&gt;
(7)(filesystem TS)

    path &amp;concat(const Source &amp;source);

template &lt;class InputIt&gt;
(8)(filesystem TS)

    path &amp;concat(InputIterator first, InputIterator last);</code></pre>
<p>Concatenates the current path and the argument<br />
1) Concatenates *this and p in such a way that native() of the result is exactly original native() concatenated with p.native()<br />
2) Same as <code>(1)</code>, except the resulting native() is a concatenation of the original {native() and the string str<br />
3) Same as <code>(1)</code>, except the resulting native() is a concatenation of the original native() and the null-terminated string whose first character is pointed to by ptr<br />
4) Same as <code>(1)</code>, except the resulting native() is a concatenation of the original native() and the single character x<br />
5) Same as <code>(1)</code>, except the resulting native() is a concatenation of the original native() and the sequence (which may be in portable or native format) represented by source, which may be std::basic_string, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence.<br />
6) Same as <code>(4)</code>, except that character conversion may be performed<br />
7) Same as <code>(5)</code><br />
8) Same as <code>(5)</code>, except that the sequence is represented by any iterator pair that designates a multicharacter string. </p>
<h2>Parameters</h2>
<p>p &#8211; path to append<br />
str &#8211; string to append<br />
ptr &#8211; pointer to the beginning of a null-terminated string to append<br />
x &#8211; single character to append<br />
source &#8211; std::basic_string, null-terminated multicharacter string, or an input iterator pointing to a null-terminated multicharacter sequence, which represents a path name (either in portable or in native format)<br />
first, last &#8211; pair of LegacyInputIterators that specify a multicharacter sequence that represents a path name</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
The value type of InputIt must be one of the encoded character types (char, wchar_t, char16_t and char32_t)<br />
&#8211;<br />
CharT must be one of the encoded character types (char, wchar_t, char16_t and char32_t)</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>May throw filesystem_error on underlying OS API errors or std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>Unlike with append() or operator/=, additional directory separators are never introduced. </p>
<h2>Example</h2>
<p>// Run this code #include &lt;iostream&gt;</p>
<p>#include &lt;experimental/filesystem&gt;</p>
<p>namespace fs = std::experimental::filesystem;</p>
<p>int main()<br />
{<br />
    fs::path p1; // empty path<br />
    p1 += &quot;var&quot;; // does not insert a separator<br />
    std::cout &lt;&lt; &quot;\&quot;\&quot; + \&quot;var\&quot; == &quot; &lt;&lt; p1 &lt;&lt; &#8216;
&#8217;;<br />
    p1 += &quot;lib&quot;; // does not insert a separator<br />
    std::cout &lt;&lt; &quot;\&quot;\&quot; + \&quot;var\&quot; + \&quot;lib\&quot; == &quot; &lt;&lt; p1 &lt;&lt; &#8216;
&#8217;;<br />
}</p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;&quot; + &quot;var&quot; == &quot;var&quot;<br />
&nbsp;<wbr>&nbsp;&quot;&quot; + &quot;var&quot; + &quot;lib&quot; == &quot;varlib&quot;</p>
<h2>See also</h2>
<pre><code>appends elements to the path

append     (public member function)

operator/=
concatenates two paths with a directory separator

operator/  (function)




</code></pre>
