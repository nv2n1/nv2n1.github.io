---
title: "std-codecvt-9(3)"
name: "std-codecvt-9"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-9/"
description: "std::wstring_convert<Codecvt,Elem,Wide_alloc,Byte_alloc>::converted – std::wstring_convert<Codecvt,Elem,Wide_alloc,Byte_alloc>::converted"
---

<h2 class="name">NAME</h2>
<p> std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::converted &#8211; std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::converted</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
std::size_t converted() const; <i>(until C++14)</i><br />
std::size_t converted() const noexcept; <i>(since C++14)</i> </p>
<p>Returns the number of source characters that were processed by the most recent from_bytes() or to_bytes(). </p>
<h2>Return value</h2>
<p>The number of characters consumed by the most recent conversion operation. </p>
<h2>Example</h2>
<p> // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;string&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;locale&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;codecvt&gt;<br />
&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string utf8 = u8&quot;z\u00df\u6c34\U0001d10b&quot;; // or u8&quot;zß水&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// or &quot;\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;original UTF-8 string size: &quot; &lt;&lt; utf8.size() &lt;&lt; &#8216;\n&#8217;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// the UTF-8 &#8211; UTF-32 standard conversion facet<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wstring_convert&lt;std::codecvt_utf8&lt;char32_t&gt;, char32_t&gt; cvt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// UTF-8 to UTF-32<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::u32string utf32 = cvt.from_bytes(utf8);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;UTF-32 string size: &quot; &lt;&lt; utf32.size() &lt;&lt; &#8216;\n&#8217;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;converted() == &quot; &lt;&lt; cvt.converted() &lt;&lt; &#8216;\n&#8217;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// UTF-32 to UTF-8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;utf8 = cvt.to_bytes(utf32);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;new UTF-8 string size: &quot; &lt;&lt; utf8.size() &lt;&lt; &#8216;\n&#8217;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;converted() == &quot; &lt;&lt; cvt.converted() &lt;&lt; &#8216;\n&#8217;;<br />
&nbsp;<wbr>&nbsp;} </p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;original UTF-8 string size: 10<br />
&nbsp;<wbr>&nbsp;UTF-32 string size: 4<br />
&nbsp;<wbr>&nbsp;converted() == 10<br />
&nbsp;<wbr>&nbsp;new UTF-8 string size: 10<br />
&nbsp;<wbr>&nbsp;converted() == 4 </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a wide string into a byte string<br />
to_bytes <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string into a wide string<br />
from_bytes <i>(public member function)</i> </p>
<h2>Index</h2>


