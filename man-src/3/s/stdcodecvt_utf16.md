---
title: "stdcodecvt_utf16(3)"
name: "stdcodecvt_utf16"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcodecvt_utf16/"
description: "std::codecvt_utf16 – std::codecvt_utf16"
---

<p>std::codecvt_utf16 &#8211; std::codecvt_utf16</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;codecvt&gt;

    template &lt;class Elem,

              unsigned long Maxcode = 0x10ffff, (since C++ 11)

                                                    std::codecvt_mode Mode = (std::codecvt_mode)0&gt;
    (deprecated in C++ 17)

        class codecvt_utf16 : public std::codecvt&lt;Elem, char, std::mbstate_t&gt;;</code></pre>
<p>std::codecvt_utf16 is a std::codecvt facet which encapsulates conversion between a UTF-16 encoded byte string and UCS2 or UTF-32 character string (depending on the type of Elem). This codecvt facet can be used to read and write UTF-16 files in binary mode. </p>
<h2>Template Parameters</h2>
<p>Elem &#8211; either char16_t, char32_t, or wchar_t<br />
Maxcode &#8211; the largest value of Elem that this facet will read or write without error<br />
Mode &#8211; a constant of type std::codecvt_mode</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new codecvt_utf16 facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a codecvt_utf16 facet<br />
destructor <i>(public member function)</i> </p>
<p>&nbsp;std::codecvt_utf16::codecvt_utf16 </p>
<p>explicit codecvt_utf16( std::size_t refs = 0 ); </p>
<p>Constructs a new std::codecvt_utf16 facet, passes the initial reference counter refs to the base class.</p>
<h2>Parameters</h2>
<p>refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::codecvt_utf16::~codecvt_utf16 </p>
<p>~codecvt_utf16(); </p>
<p>Destroys the facet. Unlike the locale-managed facets, this facet&#8217;s destructor is public. </p>
<p>Inherited from std::codecvt</p>
<h2>Member types</h2>
<p>Member type Definition<br />
intern_type internT<br />
extern_type externT<br />
state_type stateT</p>
<h2>Member objects</h2>
<p>Member name Type<br />
id (static) std::locale::id</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_out<br />
out <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_in<br />
in <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_unshift<br />
unshift <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_encoding<br />
encoding <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_always_noconv<br />
always_noconv <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_length<br />
length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_max_length<br />
max_length <i>(public member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i></p>
<h2>Protected member functions</h2>
<p>do_out converts a string from internT to externT, such as when writing to file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_in converts a string from externT to internT, such as when reading from file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_unshift generates the termination character sequence of externT characters for incomplete conversion<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_encoding returns the number of externT characters necessary to produce one internT character, if constant<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_always_noconv tests if the facet encodes an identity conversion for all valid argument values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_length calculates the length of the externT string that would be consumed by conversion into given internT buffer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_max_length returns the maximum number of externT characters that could be converted into a single internT character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::codecvt&lt;InternT,ExternT,State&gt;)</i><br />
<code>[virtual]</code> </p>
<p>Inherited from std::codecvt_base </p>
<p>Member type Definition<br />
enum result { ok, partial, error, noconv }; Unscoped enumeration type </p>
<p>Enumeration constant Definition<br />
ok conversion was completed with no error<br />
partial not all source characters were converted<br />
error encountered an invalid character<br />
noconv no conversion required, input and output types are the same</p>
<h2>Notes</h2>
<p>Although the standard requires that this facet works with UCS2 when the size of Elem is 16 bits, some implementations use UTF-16 instead, making this a non-converting locale. The term &quot;UCS2&quot; was deprecated and removed from the Unicode standard. </p>
<h2>Example</h2>
<p>The following example demonstrates decoding of UTF-16le file on a system with 32-bit wchar_t. On a system with 16-bit wchar_t, decoding of the third character will fail because std::codecvt_utf16&lt;char16_t&gt; produces UCS2, not UTF-16.<br />
 // Run this code </p>
<pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;locale&gt;

#include &lt;codecvt&gt;
void prepare_file()

{
    // UTF-16le data (if host system is little-endian)
    char16_t utf16le[4] = {0x007a,          // latin small letter 'z' U+007a
                           0x6c34,          // CJK ideograph &quot;water&quot;  U+6c34
                           0xd834, 0xdd0b}; // musical sign segno U+1d10b
    // store in a file
    std::ofstream fout(&quot;text.txt&quot;);
    fout.write(reinterpret_cast&lt;char *&gt;(utf16le), sizeof utf16le);
}
int main()

{
    prepare_file();
    // open as a byte stream
    std::wifstream fin(&quot;text.txt&quot;, std::ios::binary);
    // apply facet
    fin.imbue(std::locale(fin.getloc(),
                          new std::codecvt_utf16&lt;wchar_t, 0x10ffff, std::little_endian&gt;));
    for (wchar_t c; fin.get(c);)
        std::cout &lt;&lt; std::showbase &lt;&lt; std::hex &lt;&lt; c &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;0x7a<br />
&nbsp;<wbr>&nbsp;0x6c34<br />
&nbsp;<wbr>&nbsp;0x1d10b</p>
<h2>See also</h2>
<p>Character locale-defined multibyte UTF-8 UTF-16<br />
conversions (UTF-8, GB18030)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt&lt;char16_t, char, mbstate_t&gt;<br />
UTF-16 mbrtoc16 / c16rtomb(with C11&#8217;s DR488) codecvt_utf8_utf16&lt;char16_t&gt; N/A<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8_utf16&lt;char32_t&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8_utf16&lt;wchar_t&gt;<br />
UCS2 c16rtomb(without C11&#8217;s DR488) codecvt_utf8&lt;char16_t&gt; codecvt_utf16&lt;char16_t&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8&lt;wchar_t&gt;(Windows) codecvt_utf16&lt;wchar_t&gt;(Windows)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt&lt;char32_t, char, mbstate_t&gt; codecvt_utf16&lt;char32_t&gt;<br />
UTF-32 mbrtoc32 / c32rtomb codecvt_utf8&lt;char32_t&gt; codecvt_utf16&lt;wchar_t&gt;(non-Windows)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;codecvt_utf8&lt;wchar_t&gt;(non-Windows)<br />
system wide: mbsrtowcs / wcsrtombs<br />
UTF-32(non-Windows) use_facet&lt;codecvt No No<br />
UCS2(Windows) &lt;wchar_t, char, mbstate_t&gt;&gt;(locale)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts between character encodings, including UTF-8, UTF-16, UTF-32<br />
codecvt <i>(class template)</i><br />
codecvt_mode tags to alter behavior of the standard codecvt facets<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++11)</i><br />
(deprecated in C++17)<br />
codecvt_utf8 converts between UTF-8 and UCS2/UCS4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
(deprecated in C++17)<br />
codecvt_utf8_utf16 converts between UTF-8 and UTF-16<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
(deprecated in C++17) </p>
