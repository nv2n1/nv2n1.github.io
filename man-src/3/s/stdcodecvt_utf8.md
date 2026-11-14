---
title: "stdcodecvt_utf8(3)"
name: "stdcodecvt_utf8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcodecvt_utf8/"
---

std::codecvt_utf8 - std::codecvt_utf8

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;codecvt&gt;

    template &lt;

        class Elem, (since C++ 11)

                        unsigned long Maxcode = 0x10ffff,
        (deprecated in C++ 17)

            std::codecvt_mode Mode = (std::codecvt_mode)0

        &gt;
    class codecvt_utf8 : public std::codecvt&lt;Elem, char, std::mbstate_t&gt;;</code></pre> 
std::codecvt_utf8 is a std::codecvt facet which encapsulates conversion between a UTF-8 encoded byte string and UCS2 or UTF-32 character string (depending on the type of Elem). This codecvt facet can be used to read and write UTF-8 files, both text and binary. 

<h2>Template Parameters</h2>

Elem - either char16_t, char32_t, or wchar_t 
Maxcode - the largest value of Elem that this facet will read or write without error 
Mode - a constant of type std::codecvt_mode

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new codecvt_utf8 facet 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a codecvt_utf8 facet 
destructor <i>(public member function)</i> 

 

 
&nbsp;std::codecvt_utf8::codecvt_utf8 

 

 
explicit codecvt_utf8( std::size_t refs = 0 ); 

 
Constructs a new std::codecvt_utf8 facet, passes the initial reference counter refs to the base class.

<h2>Parameters</h2>

refs - the number of references that link to the facet 

 

 
&nbsp;std::codecvt_utf8::~codecvt_utf8 

 

 
~codecvt_utf8(); 

 
Destroys the facet. Unlike the locale-managed facets, this facet's destructor is public. 

 
Inherited from std::codecvt

<h2>Member types</h2>

Member type Definition 
intern_type internT 
extern_type externT 
state_type stateT

<h2>Member objects</h2>

Member name Type 
id (static) std::locale::id

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_out 
out <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_in 
in <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_unshift 
unshift <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_encoding 
encoding <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_always_noconv 
always_noconv <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_length 
length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_max_length 
max_length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i>

<h2>Protected member functions</h2>

do_out converts a string from internT to externT, such as when writing to file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_in converts a string from externT to internT, such as when reading from file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_unshift generates the termination character sequence of externT characters for incomplete conversion 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_encoding returns the number of externT characters necessary to produce one internT character, if constant 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_always_noconv tests if the facet encodes an identity conversion for all valid argument values 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_length calculates the length of the externT string that would be consumed by conversion into given internT buffer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 
do_max_length returns the maximum number of externT characters that could be converted into a single internT character 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i> 
<b>[virtual]</b> 

 

 

 
Inherited from std::codecvt_base 

 

 
Member type Definition 
enum result { ok, partial, error, noconv }; Unscoped enumeration type 

 

 
Enumeration constant Definition 
ok conversion was completed with no error 
partial not all source characters were converted 
error encountered an invalid character 
noconv no conversion required, input and output types are the same

<h2>Notes</h2>

Although the standard requires that this facet works with UCS2 when the size of Elem is 16 bits, some implementations use UTF-16 instead. The term &quot;UCS2&quot; was deprecated and removed from the Unicode standard. 

<h2>Example</h2>

The following example demonstrates the difference between UCS2/UTF-8 and UTF-16/UTF-8 conversions: the third character in the string is not a valid UCS2 character. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;locale&gt;

#include &lt;codecvt&gt;
int main()

{
    // UTF-8 data. The character U+1d10b, musical sign segno, does not fit in UCS2
    std::string utf8 = u8&quot;z\u6c34\U0001d10b&quot;;
    // the UTF-8 / UTF-16 standard conversion facet
    std::wstring_convert&lt;std::codecvt_utf8_utf16&lt;char16_t&gt;, char16_t&gt; utf16conv;
    std::u16string utf16 = utf16conv.from_bytes(utf8);
    std::cout &lt;&lt; &quot;UTF16 conversion produced &quot; &lt;&lt; utf16.size() &lt;&lt; &quot; code units:\n&quot;;
    for (char16_t c : utf16)
        std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; '\n';
    // the UTF-8 / UCS2 standard conversion facet
    std::wstring_convert&lt;std::codecvt_utf8&lt;char16_t&gt;, char16_t&gt; ucs2conv;
    try {
        std::u16string ucs2 = ucs2conv.from_bytes(utf8);
    } catch (const std::range_error &amp;e) {
        std::u16string ucs2 = ucs2conv.from_bytes(utf8.substr(0, ucs2conv.converted()));
        std::cout &lt;&lt; &quot;UCS2 failed after producing &quot; &lt;&lt; std::dec &lt;&lt; ucs2.size() &lt;&lt; &quot; characters:\n&quot;;
        for (char16_t c : ucs2)
            std::cout &lt;&lt; std::hex &lt;&lt; std::showbase &lt;&lt; c &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;UTF16 conversion produced 4 code units: 
&nbsp;<wbr>&nbsp;0x7a 
&nbsp;<wbr>&nbsp;0x6c34 
&nbsp;<wbr>&nbsp;0xd834 
&nbsp;<wbr>&nbsp;0xdd0b 
&nbsp;<wbr>&nbsp;UCS2 failed after producing 2 characters: 
&nbsp;<wbr>&nbsp;0x7a 
&nbsp;<wbr>&nbsp;0x6c34

<h2>See also</h2>

Character locale-defined multibyte UTF-8 UTF-16 
conversions (UTF-8, GB18030) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt&lt;char16_t, char, mbstate_t&gt; 
UTF-16 mbrtoc16 / c16rtomb(with C11's DR488) codecvt_utf8_utf16&lt;char16_t&gt; N/A 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8_utf16&lt;char32_t&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8_utf16&lt;wchar_t&gt; 
UCS2 c16rtomb(without C11's DR488) codecvt_utf8&lt;char16_t&gt; codecvt_utf16&lt;char16_t&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8&lt;wchar_t&gt;(Windows) codecvt_utf16&lt;wchar_t&gt;(Windows) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt&lt;char32_t, char, mbstate_t&gt; codecvt_utf16&lt;char32_t&gt; 
UTF-32 mbrtoc32 / c32rtomb codecvt_utf8&lt;char32_t&gt; codecvt_utf16&lt;wchar_t&gt;(non-Windows) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8&lt;wchar_t&gt;(non-Windows) 
system wide: mbsrtowcs / wcsrtombs 
UTF-32(non-Windows) use_facet&lt;codecvt No No 
UCS2(Windows) &lt;wchar_t, char, mbstate_t&gt;&gt;(locale) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts between character encodings, including UTF-8, UTF-16, UTF-32 
codecvt <i>(class template)</i> 
codecvt_mode tags to alter behavior of the standard codecvt facets 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
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
