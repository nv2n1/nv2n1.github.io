---
title: "stdexperimentalfilesystempathgeneric_stringgeneric_wstringgeneric_u8string(3)"
name: "stdexperimentalfilesystempathgeneric_stringgeneric_wstringgeneric_u8string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathgeneric_stringgeneric_wstringgeneric_u8string/"
---

std::experimental::filesystem::path::generic_string,generic_wstring,generic_u8string,... - std::experimental::filesystem::path::generic_string,generic_wstring,generic_u8string,...

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits = std::char_traits&lt;CharT&gt;,

          class Alloc = std::allocator&lt;CharT&gt;&gt;
(1)(filesystem TS)

    std::basic_string&lt;CharT, Traits, Alloc&gt;

    generic_string(const Alloc &amp;a = Alloc()) const;

std::string generic_string() const;

std::wstring generic_wstring() const;

std::string generic_u8string() const;
(2)(filesystem TS)

    std::u16string generic_u16string() const;

std::u32string generic_u32string() const;</code></pre> 
Returns the internal pathname in generic pathname format, converted to specific string type. Conversion, if any, is specified in todo. The / character is used as the directory separator. 
1) All memory allocations are performed by a. 
2) The encoding in the case of u8string() is always UTF-8. 

<h2>Parameters</h2>

a - allocator to construct the string with 
- 
CharT must be one of the encoded character types (char, wchar_t, char16_t and char32_t)

<h2>Return value</h2>

The internal pathname in generic pathname format, converted to specified string type. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>See also</h2>

string 
wstring returns the path in native pathname format converted to a string 
u8string <i>(public member function)</i> 
u16string 
u32string 
