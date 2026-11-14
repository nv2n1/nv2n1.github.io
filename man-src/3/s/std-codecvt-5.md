---
title: "std-codecvt-5(3)"
name: "std-codecvt-5"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-5/"
description: "std::wbuffer_convert<Codecvt,Elem,Tr>::rdbuf – std::wbuffer_convert<Codecvt,Elem,Tr>::rdbuf"
---

<h2 class="name">NAME</h2>
<p> std::wbuffer_convert&lt;Codecvt,Elem,Tr&gt;::rdbuf &#8211; std::wbuffer_convert&lt;Codecvt,Elem,Tr&gt;::rdbuf</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
std::streambuf* rdbuf() const; <b>(1)</b><br />
std::streambuf* rdbuf( std::streambuf* bytebuf ); <b>(2)</b> </p>
<p>1) returns the pointer to the underlying byte stream<br />
2) replaces the associated byte stream with bytebuf . </p>
<h2>Return value</h2>
<p>1) the current underlying byte stream<br />
2) the previous byte stream </p>
<h2>Example</h2>
<p> // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;sstream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;locale&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;codecvt&gt;<br />
&nbsp;<wbr>&nbsp;int main()<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// convert UTF-8 to UCS4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::stringbuf utf8buf(u8&quot;z\u00df\u6c34\U0001d10b&quot;); // or u8&quot;zß水&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// or &quot;\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wbuffer_convert&lt;std::codecvt_utf8&lt;wchar_t&gt;&gt; conv(&amp;utf8buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wistream ucsbuf(&amp;conv);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;Reading from a UTF-8 stringbuf via wbuffer_convert:\n&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for(wchar_t c; ucsbuf.get(c); )<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; &#8216;\n&#8217;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// reuse the same wbuffer_convert to handle UCS4 to UTF-8 output<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;conv.rdbuf(std::cout.rdbuf());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::wostream out(&amp;conv);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;Sending UCS4 data to std::cout via wbuffer_convert:\n&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;out &lt;&lt; L&quot;z\u00df\u6c34\U0001d10b\n&quot;;<br />
&nbsp;<wbr>&nbsp;} </p>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Reading from a UTF-8 stringbuf via wbuffer_convert:<br />
&nbsp;<wbr>&nbsp;0x7a<br />
&nbsp;<wbr>&nbsp;0xdf<br />
&nbsp;<wbr>&nbsp;0x6c34<br />
&nbsp;<wbr>&nbsp;0x1d10b<br />
&nbsp;<wbr>&nbsp;Sending UCS4 data to std::cout via wbuffer_convert:<br />
&nbsp;<wbr>&nbsp;zß水 </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new wbuffer_convert<br />
constructor <i>(public member function)</i> </p>
<h2>Index</h2>


