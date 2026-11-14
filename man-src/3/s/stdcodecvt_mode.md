---
title: "stdcodecvt_mode(3)"
name: "stdcodecvt_mode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcodecvt_mode/"
---

std::codecvt_mode - std::codecvt_mode

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;codecvt&gt;

enum codecvt_mode {

    consume_header = 4,          (since C++11)

    generate_header = 2,         (deprecated in C++17)

    little_endian = 1

};</code></pre> 
The facets std::codecvt_utf8, std::codecvt_utf16, and std::codecvt_utf8_utf16 accept an optional value of type std::codecvt_mode as a template argument, which specifies optional features of the unicode string conversion. 

<h2>Constants</h2>

Defined in header &lt;locale&gt; 
Value Meaning 
little_endian assume the input is in little-endian byte order (applies to UTF-16 input only, the default is big-endian) 
consume_header consume the byte order mark, if present at the start of input sequence, and (in case of UTF-16), rely on the byte order it specifies for decoding the rest of the input 
generate_header output the byte order mark at the start of the output sequence 

 
The recognized byte order marks are: 

 
0xfe 0xff UTF-16 big-endian 
0xff 0xfe UTF-16 little-endian 
0xef 0xbb 0xbf UTF-8 (no effect on endianness) 

 
If std::consume_header is not selected when reading a file beginning with byte order mark, the Unicode character U+FEFF (Zero width non-breaking space) will be read as the first character of the string content.

<h2>Example</h2>

The following example demonstrates consuming the UTF-8 BOM 
 // Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;locale&gt;

#include &lt;codecvt&gt;
int main()

{
    // UTF-8 data with BOM
    std::ofstream(&quot;text.txt&quot;) &lt;&lt; u8&quot;\ufeffz\u6c34\U0001d10b&quot;;
    // read the UTF8 file, skipping the BOM
    std::wifstream fin(&quot;text.txt&quot;);
    fin.imbue(std::locale(fin.getloc(),
                          new std::codecvt_utf8&lt;wchar_t, 0x10ffff, std::consume_header&gt;));
    for (wchar_t c; fin.get(c);)
        std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0x7a 
&nbsp;<wbr>&nbsp;0x6c34 
&nbsp;<wbr>&nbsp;0x1d10b

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts between character encodings, including UTF-8, UTF-16, UTF-32 
codecvt <i>(class template)</i> 
codecvt_utf8 converts between UTF-8 and UCS2/UCS4 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(deprecated in C++17) 
codecvt_utf16 converts between UTF-16 and UCS2/UCS4 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(deprecated in C++17) 
codecvt_utf8_utf16 converts between UTF-8 and UTF-16 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(deprecated in C++17) 
