---
title: "stdendian(3)"
name: "stdendian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdendian/"
---

std::endian - std::endian

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;type_traits&gt;

enum class endian

{

    little = /*implementation-defined*/, (1) (since C++20)

    big = /*implementation-defined*/,

    native = /*implementation-defined*/

};</code></pre> 
Indicates the endianness of all scalar_types: 
* If all scalar types are little-endian, std::endian::native equals std::endian::little 
* If all scalar types are big-endian, std::endian::native equals std::endian::big 
Corner case platforms are also supported: 
* If all scalar types have sizeof equal to 1, endianness does not matter and all three values, std::endian::little, std::endian::big, and std::endian::native are the same 
* If the platform uses mixed endian, std::endian::native does not equal either std::endian::big nor std::endian::little 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;enum class endian 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;#ifdef _WIN32 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;little = 0, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;big = 1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;native = little 
&nbsp;<wbr>&nbsp;#else 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;little = __ORDER_LITTLE_ENDIAN__, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;big = __ORDER_BIG_ENDIAN__, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;native = __BYTE_ORDER__ 
&nbsp;<wbr>&nbsp;#endif 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
