---
title: "stdexperimentalfilesystempathoperator(3)"
name: "stdexperimentalfilesystempathoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathoperator/"
description: "std::experimental::filesystem::path::operator= – std::experimental::filesystem::path::operator="
---

<p>std::experimental::filesystem::path::operator= &#8211; std::experimental::filesystem::path::operator=</p>
<h2>Synopsis</h2>
<pre><code>path &amp;operator=(const path &amp;p);
(1)(filesystem TS)

    path &amp;
    operator=(path &amp;&amp;p);
(2)(filesystem TS)

    template &lt;class Source&gt;
    (2)(filesystem TS)

        path &amp;
        operator=(const Source &amp;source);</code></pre>
<p>1) Replaces the contents of *this with a copy of the contents of p.<br />
2) Replaces the contents of *this with p, possibly using move semantics: p is left in valid, but unspecified state.<br />
3) Replaces the contents of *this with a new path value constructed from source as if by overload <code>(4)</code> of the path_constructor. Equivalent to assign(source). </p>
<h2>Parameters</h2>
<p>p &#8211; a path to assign<br />
source &#8211; a std::basic_string, pointer to a null-terminated character/wide character string, or an input iterator that points to a null-terminated character/wide character sequence. The character type must be one of char, char16_t, char32_t, wchar_t</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>1) <i>(none)</i><br />
2)<br />
noexcept specification:<br />
noexcept<br />
3) <i>(none)</i></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

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
