---
title: "stdfilesystempathgeneric_stringstdfilesystempathgeneric_wstring(3)"
name: "stdfilesystempathgeneric_stringstdfilesystempathgeneric_wstring"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathgeneric_stringstdfilesystempathgeneric_wstring/"
---

std::filesystem::path::generic_string,std::filesystem::path::generic_wstring, - std::filesystem::path::generic_string,std::filesystem::path::generic_wstring,

<h2>Synopsis</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::filesystem::path::generic_u32string <pre><code>template &lt;class CharT, class Traits =

                           std::char_traits&lt;CharT&gt;,
          (since

           class Alloc = std::allocator&lt;CharT&gt; &gt; (1)C++ 17)

              std::basic_string&lt;CharT, Traits, Alloc&gt;
                  generic_string(const Alloc &amp;a = Alloc()) const;

std::string generic_string() const;

std::wstring generic_wstring() const;

std::u16string generic_u16string() const;

std::u32string generic_u32string() const;
(2)(since(since

              std::string generic_u8string() const;
          C++ 17) C++ 17)(3)(until
                                 C++ 20)

    std::u8string generic_u8string() const;
(since
     C++ 20)</code></pre> 
Returns the internal pathname in generic pathname format, converted to specific 
string type. Conversion, if any, is specified as follows: 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>If path::value_type is char, conversion, if any, is system-dependent. This is 
&nbsp;<wbr>the case on typical POSIX systems&nbsp;<wbr>(such as Linux), where native encoding is 
&nbsp;<wbr>UTF-8 and string()&nbsp;<wbr>performs no conversion. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is wchar_t, conversion, if any, is unspecified. 
&nbsp;<wbr>This is the case on Windows, where wchar_t is 16 bit and the native encoding is 
&nbsp;<wbr>UTF-16. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char16_t, native encoding is UTF-16 and the 
&nbsp;<wbr>conversion method is unspecified. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char32_t, native encoding is UTF-32 and the 
&nbsp;<wbr>conversion method is unspecified. 
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Otherwise, if path::value_type is char8_t, native encoding is UTF-8 and the 
&nbsp;<wbr>conversion method is unspecified. 
The&nbsp;<wbr>/&nbsp;<wbr>character is used as the directory separator. 
1)&nbsp;<wbr>All memory allocations are performed by a. 
3)&nbsp;<wbr>The result encoding in the case of u8string()&nbsp;<wbr>is always UTF-8. 

<h2>Parameters</h2>

a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allocator to construct the string with

<h2>Type requirements</h2>

- 
CharT must be one of the encoded character types&nbsp;<wbr>(char, wchar_t, char16_t and 
char32_t)

<h2>Return value</h2>

The internal pathname in generic pathname format, converted to specified string 
type. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>See also</h2>

string 
wstring&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>returns the path in native pathname format converted to a string 
u8string&nbsp;<wbr>&nbsp;<wbr><i>(public member function)</i> 
u16string 
u32string 
