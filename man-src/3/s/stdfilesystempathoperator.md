---
title: "stdfilesystempathoperator(3)"
name: "stdfilesystempathoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathoperator/"
description: "std::filesystem::path::operator= – std::filesystem::path::operator="
---

<p>std::filesystem::path::operator= &#8211; std::filesystem::path::operator=</p>
<h2>Synopsis</h2>
<pre><code>path &amp;operator=(const path &amp;p);
(1)(since C++ 17)

    path &amp;
    operator=(path &amp;&amp;p) noexcept;
(2)(since C++ 17)

    path &amp;
    operator=(string_type &amp;&amp;source);
(3)(since C++ 17)

    template &lt;class Source&gt;
    (4)(since C++ 17)

        path &amp;
        operator=(const Source &amp;source);</code></pre>
<p>1) Replaces the contents of *this with a pathname whose both native and generic format representations equal those of p.<br />
2) Replaces the contents of *this with a pathname whose both native and generic format representations equal those of p, possibly using move semantics: p is left in a valid, but unspecified state.<br />
3) Replaces the contents of *this with a new path value constructed from detected-format source, which is left in valid, but unspecified state. Equivalent to assign(std::move(source)).<br />
4) Replaces the contents of *this with a new path value constructed from detected-format source as if by overload <code>(4)</code> of the path_constructor. Equivalent to assign(source). </p>
<h2>Parameters</h2>
<p>p &#8211; a path to assign<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a std::basic_string, std::basic_string_view, pointer to a null-terminated character/wide character string, or an input iterator that points to a null-terminated character/wide character sequence. The character type must be one of char,<br />
source &#8211; char8_t,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++20)</i>char16_t, char32_t, wchar_t</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = &quot;C:/users/abcdef/AppData/Local&quot;;
    p = p / &quot;Temp&quot;; // move assignment
    const wchar_t *wstr = L&quot;D:/猫.txt&quot;;
    p = wstr; // assignment from a source
}
</code></pre>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents<br />
assign <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a path<br />
constructor <i>(public member function)</i> </p>
