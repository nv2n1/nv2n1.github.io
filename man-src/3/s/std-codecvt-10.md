---
title: "std-codecvt-10(3)"
name: "std-codecvt-10"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-10/"
description: "std::wstring_convert<Codecvt,Elem,Wide_alloc,Byte_alloc>::from_bytes – std::wstring_convert<Codecvt,Elem,Wide_alloc,Byte_alloc>::from_bytes"
---

<h2 id="name">NAME</h2>
<p>std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::from_bytes &#8211; std::wstring_convert&lt;Codecvt,Elem,Wide_alloc,Byte_alloc&gt;::from_bytes</p>
<h2 id="synopsis">SYNOPSIS</h2>
<p>Defined in header <code>&lt;locale&gt;</code></p>
<pre><code>wide_string from_bytes(char byte);          // (1)
wide_string from_bytes(const char* ptr);  // (2)
wide_string from_bytes(const byte_string&amp; str);  // (3)
wide_string from_bytes(const char* first, const char* last);  // (4)</code></pre>
<p>Performs multibyte to wide conversion, using the codecvt facet supplied at construction.</p>
<dl>
<dt>(1)</dt>
<dd>Converts byte as if it was a string of length 1 to wide_string</dd>
<dt>(2)</dt>
<dd>Converts the null-terminated multibyte character sequence beginning at the character pointed to by ptr to wide_string</dd>
<dt>(3)</dt>
<dd>Converts the narrow string str to wide_string.</dd>
<dt>(4)</dt>
<dd>Converts the narrow multibyte character sequence [first, last) to wide_string</dd>
</dl>
<p>In all cases, the conversion begins in initial shift state, unless non-initial starting state was provided to this wstring_convert constructor. The number of characters converted and the final value of the conversion state are remembered and can be accessed with <code>state()</code> and <code>converted()</code>.</p>
<h2 id="return-value">Return value</h2>
<p>A wide_string object containing the results of multibyte to wide conversion. If the conversion failed and there was a user-supplied wide-error string provided to the constructor of this wstring_convert, returns that wide-error string.</p>
<h2 id="exceptions">Exceptions</h2>
<p>If this wstring_convert object was constructed without a user-supplied wide-error string, throws <code>std::range_error</code> on conversion failure.</p>
<h2 id="example">Example</h2>
<pre><code>// Run this code
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;locale&gt;
#include &lt;codecvt&gt;

int main()
{
    std::string utf8 = u8"zß水\U0001d10b"; // or u8"zß水"
                                            // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b";

    // the UTF-8 / UTF-16 standard conversion facet
    std::u16string utf16 = std::wstring_convert&lt;std::codecvt_utf8_utf16&lt;char16_t&gt;, char16_t&gt;{}.from_bytes(utf8.data());
    std::cout &lt;&lt; "UTF16 conversion produced " &lt;&lt; utf16.size() &lt;&lt; " code units:\n";
    for (char16_t c : utf16)
        std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; '\n';

    // the UTF-8 / UTF-32 standard conversion facet
    std::u32string utf32 = std::wstring_convert&lt;std::codecvt_utf8&lt;char32_t&gt;, char32_t&gt;{}.from_bytes(utf8);
    std::cout &lt;&lt; "UTF32 conversion produced " &lt;&lt; std::dec &lt;&lt; utf32.size() &lt;&lt; " code units:\n";
    for (char32_t c : utf32)
        std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; '\n';
}</code></pre>
<h2 id="output">Output</h2>
<pre><code>UTF16 conversion produced 5 code units:
0x7a
0xdf
0x6c34
0xd834
0xdd0b
UTF32 conversion produced 4 code units:
0x7a
0xdf
0x6c34
0x1d10b</code></pre>
<h2 id="see-also">See also</h2>
<dl>
<dt>to_bytes (public member function)</dt>
<dd>converts a wide string into a byte string</dd>
<dt>mbsrtowcs (function)</dt>
<dd>converts a narrow multibyte character string to wide string, given state</dd>
<dt>do_in (virtual protected member function of <code>std::codecvt&lt;InternT,ExternT,State&gt;</code>)</dt>
<dd>converts a string from externT to internT, such as when reading from file</dd>
</dl>
<h2 id="index">Index</h2>
