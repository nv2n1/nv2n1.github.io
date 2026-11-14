---
title: "antlr3-newraw16(3)"
name: "antlr3-newraw16"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-newraw16/"
description: "src/antlr3string.c –"
---

<p>src/antlr3string.c &#8211; </p>
<p> Implementation of the ANTLR3 string and string factory classes.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt; </p>
<h3>Functions</h3>
<p>static <code>pANTLR3_UINT8</code> <code>addc16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> c) </p>
<p> static <code>pANTLR3_UINT8</code> <code>addc8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> c) </p>
<p> static <code>pANTLR3_UINT8</code> <code>addi16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>pANTLR3_UINT8</code> <code>addi8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_INT32</code> i) </p>
<p> ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> <code>antlr3StringFactoryNew</code> () </p>
<p> ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> <code>antlr3UCS2StringFactoryNew</code> ()<br />
 <i>Create a string factory that is UCS2 (16 bit) encoding based. </i><br />
 static <code>pANTLR3_UINT8</code> <code>append16_16</code> (<code>pANTLR3_STRING</code> string, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>append16_8</code> (<code>pANTLR3_STRING</code> string, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>append8</code> (<code>pANTLR3_STRING</code> string, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>appendS</code> (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> newbit) </p>
<p> static <code>ANTLR3_UCHAR</code> <code>charAt16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> offset) </p>
<p> static <code>ANTLR3_UCHAR</code> <code>charAt8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> offset) </p>
<p> static void <code>closeFactory</code> (<code>pANTLR3_STRING_FACTORY</code> factory)<br />
 <i>Fascist Capitalist Pig function created to oppress the workers comrade. </i><br />
 static <code>ANTLR3_UINT32</code> <code>compare16_16</code> (<code>pANTLR3_STRING</code> string, const char *compStr) </p>
<p> static <code>ANTLR3_UINT32</code> <code>compare16_8</code> (<code>pANTLR3_STRING</code> string, const char *compStr) </p>
<p> static <code>ANTLR3_UINT32</code> <code>compare8</code> (<code>pANTLR3_STRING</code> string, const char *compStr) </p>
<p> static <code>ANTLR3_UINT32</code> <code>compareS</code> (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> compStr) </p>
<p> static void <code>destroy</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_UINT8</code> <code>insert16_16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>insert16_8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>insert8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char *newbit) </p>
<p> static <code>pANTLR3_UINT8</code> <code>inserti16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>pANTLR3_UINT8</code> <code>inserti8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i) </p>
<p> static <code>pANTLR3_UINT8</code> <code>insertS</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>pANTLR3_STRING</code> newbit) </p>
<p> static <code>pANTLR3_STRING</code> <code>newPtr16_16</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size)<br />
 <i>Creates a new 16 bit string initialized with the 16 bit characters at the supplied ptr, of pre-determined size. </i><br />
 static <code>pANTLR3_STRING</code> <code>newPtr16_8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size)<br />
 <i>Creates a new 16 bit string initialized with the 8 bit characters at the supplied 8 bit character ptr, of pre-determined size. </i><br />
 static <code>pANTLR3_STRING</code> <code>newPtr8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size)<br />
 <i>Creates a new 8 bit string initialized with the 8 bit characters at the supplied ptr, of pre-determined size. </i><br />
 static <code>pANTLR3_STRING</code> <code>newRaw16</code> (<code>pANTLR3_STRING_FACTORY</code> factory) </p>
<p> static <code>pANTLR3_STRING</code> <code>newRaw8</code> (<code>pANTLR3_STRING_FACTORY</code> factory) </p>
<p> static <code>pANTLR3_STRING</code> <code>newSize16</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>ANTLR3_UINT32</code> size)<br />
 <i>Creates a new string with enough capacity for size 16 bit characters plus a terminator. </i><br />
 static <code>pANTLR3_STRING</code> <code>newSize8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>ANTLR3_UINT32</code> size)<br />
 <i>Creates a new string with enough capacity for size 8 bit characters plus a terminator. </i><br />
 static <code>pANTLR3_STRING</code> <code>newStr16_16</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr)<br />
 <i>Create a new 16 bit string from the supplied, null terminated, 16 bit string pointer. </i><br />
 static <code>pANTLR3_STRING</code> <code>newStr16_8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr)<br />
 <i>Create a new 16 bit string from the supplied, null terminated, 8 bit string pointer. </i><br />
 static <code>pANTLR3_STRING</code> <code>newStr8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr)<br />
 <i>Create a new 8 bit string from the supplied, null terminated, 8 bit string pointer. </i><br />
 static <code>pANTLR3_STRING</code> <code>printable16</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_STRING</code> <code>printable8</code> (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_UINT8</code> <code>set16_16</code> (<code>pANTLR3_STRING</code> string, const char *chars) </p>
<p> static <code>pANTLR3_UINT8</code> <code>set16_8</code> (<code>pANTLR3_STRING</code> string, const char *chars) </p>
<p> static <code>pANTLR3_UINT8</code> <code>set8</code> (<code>pANTLR3_STRING</code> string, const char *chars) </p>
<p> static <code>pANTLR3_UINT8</code> <code>setS</code> (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> chars) </p>
<p> static void ANTLR3_CDECL <code>stringFree</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static void <code>stringInit16</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static void <code>stringInit8</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static void <code>stringInitUTF8</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_STRING</code> <code>subString16</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex) </p>
<p> static <code>pANTLR3_STRING</code> <code>subString8</code> (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex) </p>
<p> static <code>pANTLR3_STRING</code> <code>to8_16</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_STRING</code> <code>to8_8</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>ANTLR3_INT32</code> <code>toInt32_16</code> (struct <code>ANTLR3_STRING_struct</code> *string) </p>
<p> static <code>ANTLR3_INT32</code> <code>toInt32_16</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>ANTLR3_INT32</code> <code>toInt32_8</code> (struct <code>ANTLR3_STRING_struct</code> *string) </p>
<p> static <code>ANTLR3_INT32</code> <code>toInt32_8</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_STRING</code> <code>toUTF8_16</code> (<code>pANTLR3_STRING</code> string) </p>
<p> static <code>pANTLR3_STRING</code> <code>toUTF8_8</code> (<code>pANTLR3_STRING</code> string) </p>
<h2>Detailed Description</h2>
<p>Implementation of the ANTLR3 string and string factory classes. </p>
<h2>Function Documentation</h2>
<h3>static <code>pANTLR3_UINT8</code> addc16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> c) [static]</h3>
<p>References ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> addc8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> c) [static]</h3>
<p>References ANTLR3_REALLOC, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_UINT8</code> addi16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> addi8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by stringInit8().</p>
<h3>ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> antlr3StringFactoryNew (void)</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, antlr3VectorNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::index, ANTLR3_STRING_FACTORY_struct::newPtr, ANTLR3_STRING_FACTORY_struct::newPtr8, newPtr8(), ANTLR3_STRING_FACTORY_struct::newRaw, newRaw8(), ANTLR3_STRING_FACTORY_struct::newSize, newSize8(), ANTLR3_STRING_FACTORY_struct::newStr, ANTLR3_STRING_FACTORY_struct::newStr8, newStr8(), ANTLR3_STRING_FACTORY_struct::printable, printable8(), and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3AsciiSetupStream(), and antlr3UCS2StringFactoryNew().</p>
<h3>ANTLR3_API <code>pANTLR3_STRING_FACTORY</code> antlr3UCS2StringFactoryNew (void)</h3>
<p>Create a string factory that is UCS2 (16 bit) encoding based. </p>
<p> References antlr3StringFactoryNew(), ANTLR3_STRING_FACTORY_struct::close, closeFactory(), destroy(), ANTLR3_STRING_FACTORY_struct::destroy, ANTLR3_STRING_FACTORY_struct::newPtr, newPtr16_16(), newPtr16_8(), ANTLR3_STRING_FACTORY_struct::newPtr8, ANTLR3_STRING_FACTORY_struct::newRaw, newRaw16(), ANTLR3_STRING_FACTORY_struct::newSize, newSize16(), ANTLR3_STRING_FACTORY_struct::newStr, newStr16_16(), newStr16_8(), ANTLR3_STRING_FACTORY_struct::newStr8, ANTLR3_STRING_FACTORY_struct::printable, and printable16(). </p>
<p> Referenced by antlr3UCS2SetupStream().</p>
<h3>static <code>pANTLR3_UINT8</code> append16_16 (<code>pANTLR3_STRING</code> string, const char * newbit) [static]</h3>
<p>First, determine the length of the input string </p>
<p> References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> append16_8 (<code>pANTLR3_STRING</code> string, const char * newbit) [static]</h3>
<p>References ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> append8 (<code>pANTLR3_STRING</code> string, const char * newbit) [static]</h3>
<p>References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_UINT8</code> appendS (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> newbit) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3>static <code>ANTLR3_UCHAR</code> charAt16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> offset) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, and ANTLR3_STRING_struct::len. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>ANTLR3_UCHAR</code> charAt8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> offset) [static]</h3>
<p>References ANTLR3_STRING_struct::len. </p>
<p> Referenced by stringInit8().</p>
<h3>static void closeFactory (<code>pANTLR3_STRING_FACTORY</code> factory) [static]</h3>
<p>Fascist Capitalist Pig function created to oppress the workers comrade. </p>
<p> References ANTLR3_FREE, and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3>static <code>ANTLR3_UINT32</code> compare16_16 (<code>pANTLR3_STRING</code> string, const char * compStr) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>ANTLR3_UINT32</code> compare16_8 (<code>pANTLR3_STRING</code> string, const char * compStr) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>ANTLR3_UINT32</code> compare8 (<code>pANTLR3_STRING</code> string, const char * compStr) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>ANTLR3_UINT32</code> compareS (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> compStr) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3>static void destroy (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_VECTOR_struct::del, ANTLR3_VECTOR_ELEMENT_struct::element, ANTLR3_VECTOR_struct::elements, ANTLR3_STRING_FACTORY_struct::index, and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_UINT8</code> insert16_16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char * newbit) [static]</h3>
<p>First, determine the length of the input string </p>
<p> References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> insert16_8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char * newbit) [static]</h3>
<p>References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> insert8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, const char * newbit) [static]</h3>
<p>References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_UINT8</code> inserti16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> inserti8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i) [static]</h3>
<p>Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_UINT8</code> insertS (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> point, <code>pANTLR3_STRING</code> newbit) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3>static <code>pANTLR3_STRING</code> newPtr16_16 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size) [static]</h3>
<p>Creates a new 16 bit string initialized with the 16 bit characters at the supplied ptr, of pre-determined size. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns the strings<br />
 <i>ptr</i> &#8211; Pointer to 16 bit encoded characters</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to the new string</dl>
<p> References ANTLR3_MEMMOVE, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_FACTORY_struct::newSize. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newPtr16_8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size) [static]</h3>
<p>Creates a new 16 bit string initialized with the 8 bit characters at the supplied 8 bit character ptr, of pre-determined size. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns the strings<br />
 <i>ptr</i> &#8211; Pointer to 8 bit encoded characters</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to the new string</dl>
<p> References ANTLR3_STRING_struct::chars, and ANTLR3_STRING_FACTORY_struct::newSize. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newPtr8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr, <code>ANTLR3_UINT32</code> size) [static]</h3>
<p>Creates a new 8 bit string initialized with the 8 bit characters at the supplied ptr, of pre-determined size. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns the strings<br />
 <i>ptr</i> &#8211; Pointer to 8 bit encoded characters</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to the new string</dl>
<p> References ANTLR3_MEMMOVE, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_FACTORY_struct::newSize. </p>
<p> Referenced by antlr3StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newRaw16 (<code>pANTLR3_STRING_FACTORY</code> factory) [static]<code>Parameters:</code></h3>
<dl COMPACT>
<dd><i>factory</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd></dl>
<p> References ANTLR3_CDECL, ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_STRING_FACTORY_struct::index, ANTLR3_VECTOR_struct::set, stringFree(), stringInit16(), and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newRaw8 (<code>pANTLR3_STRING_FACTORY</code> factory) [static]<code>Parameters:</code></h3>
<dl COMPACT>
<dd><i>factory</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd></dl>
<p> References ANTLR3_CDECL, ANTLR3_MALLOC, ANTLR3_TRUE, ANTLR3_STRING_FACTORY_struct::index, ANTLR3_VECTOR_struct::set, stringFree(), stringInit8(), and ANTLR3_STRING_FACTORY_struct::strings. </p>
<p> Referenced by antlr3StringFactoryNew(), and to8_16().</p>
<h3>static <code>pANTLR3_STRING</code> newSize16 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>ANTLR3_UINT32</code> size) [static]</h3>
<p>Creates a new string with enough capacity for size 16 bit characters plus a terminator. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; POitner to the string factory that owns strings<br />
 <i>size</i> &#8211; In characters</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to the new string.</dl>
<p> References ANTLR3_MALLOC, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_FACTORY_struct::newRaw. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newSize8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>ANTLR3_UINT32</code> size) [static]</h3>
<p>Creates a new string with enough capacity for size 8 bit characters plus a terminator. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns strings<br />
 <i>size</i> &#8211; In characters</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>pointer to the new string.</dl>
<p> References ANTLR3_MALLOC, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_FACTORY_struct::newRaw. </p>
<p> Referenced by antlr3StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newStr16_16 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr) [static]</h3>
<p>Create a new 16 bit string from the supplied, null terminated, 16 bit string pointer. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns strings.<br />
 <i>ptr</i> &#8211; Pointer to the 16 bit encoded string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to the newly initialized string</dl>
<p> First, determine the length of the input string </p>
<p> References ANTLR3_STRING_FACTORY_struct::newPtr. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newStr16_8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr) [static]</h3>
<p>Create a new 16 bit string from the supplied, null terminated, 8 bit string pointer. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns strings.<br />
 <i>ptr</i> &#8211; Pointer to the 8 bit encoded string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>POinter to the newly initialized string</dl>
<p> References ANTLR3_STRING_FACTORY_struct::newPtr8. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> newStr8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_UINT8</code> ptr) [static]</h3>
<p>Create a new 8 bit string from the supplied, null terminated, 8 bit string pointer. <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factory</i> &#8211; Pointer to the string factory that owns strings.<br />
 <i>ptr</i> &#8211; Pointer to the 8 bit encoded string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to the newly initialized string</dl>
<p> References ANTLR3_STRING_FACTORY_struct::newPtr8. </p>
<p> Referenced by antlr3StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> printable16 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_FACTORY_struct::newSize. </p>
<p> Referenced by antlr3UCS2StringFactoryNew().</p>
<h3>static <code>pANTLR3_STRING</code> printable8 (<code>pANTLR3_STRING_FACTORY</code> factory, <code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::len, and ANTLR3_STRING_FACTORY_struct::newSize. </p>
<p> Referenced by antlr3StringFactoryNew().</p>
<h3>static <code>pANTLR3_UINT8</code> set16_16 (<code>pANTLR3_STRING</code> string, const char * chars) [static]</h3>
<p>First, determine the length of the input string </p>
<p> References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> set16_8 (<code>pANTLR3_STRING</code> string, const char * chars) [static]</h3>
<p>References ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_UINT8</code> set8 (<code>pANTLR3_STRING</code> string, const char * chars) [static]</h3>
<p>References ANTLR3_MEMMOVE, ANTLR3_REALLOC, ANTLR3_STRING_struct::chars, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_UINT8</code> setS (<code>pANTLR3_STRING</code> string, <code>pANTLR3_STRING</code> chars) [static]</h3>
<p>References ANTLR3_STRING_struct::chars. </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3>static void ANTLR3_CDECL stringFree (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_FREE, and ANTLR3_STRING_struct::chars. </p>
<p> Referenced by newRaw16(), and newRaw8().</p>
<h3>static void stringInit16 (<code>pANTLR3_STRING</code> string) [static]<code>Parameters:</code></h3>
<dl COMPACT>
<dd><i>string</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd></dl>
<p> References addc16(), addi16(), ANTLR3_ENCODING_UCS2, append16_16(), append16_8(), appendS(), charAt16(), compare16_16(), compare16_8(), compareS(), ANTLR3_STRING_struct::compareS, insert16_16(), insert16_8(), inserti16(), insertS(), set16_16(), set16_8(), setS(), subString16(), to8_16(), ANTLR3_STRING_struct::toInt32, toInt32_16(), ANTLR3_STRING_struct::toUTF8, and toUTF8_16(). </p>
<p> Referenced by newRaw16().</p>
<h3>static void stringInit8 (<code>pANTLR3_STRING</code> string) [static]<code>Parameters:</code></h3>
<dl COMPACT>
<dd><i>string</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd></dl>
<p> References addc8(), addi8(), ANTLR3_ENCODING_LATIN1, append8(), appendS(), charAt8(), compare8(), compareS(), ANTLR3_STRING_struct::compareS, insert8(), inserti8(), insertS(), set8(), setS(), subString8(), to8_8(), ANTLR3_STRING_struct::toInt32, toInt32_8(), ANTLR3_STRING_struct::toUTF8, and toUTF8_8(). </p>
<p> Referenced by newRaw8().</p>
<h3>static void stringInitUTF8 (<code>pANTLR3_STRING</code> string) [static]<code>Parameters:</code></h3>
<dl COMPACT>
<dd><i>string</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>TODO: Implement UTF-8</dl>
<h3>static <code>pANTLR3_STRING</code> subString16 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::factory, ANTLR3_STRING_struct::len, and ANTLR3_STRING_FACTORY_struct::newPtr. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_STRING</code> subString8 (<code>pANTLR3_STRING</code> string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::factory, ANTLR3_STRING_struct::len, and ANTLR3_STRING_FACTORY_struct::newPtr. </p>
<p> Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_STRING</code> to8_16 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_MALLOC, ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::factory, ANTLR3_STRING_struct::len, newRaw8(), and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_STRING</code> to8_8 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>Referenced by stringInit8().</p>
<h3>static <code>ANTLR3_INT32</code> toInt32_16 (struct <code>ANTLR3_STRING_struct</code> * string) [static]</h3>
<p>References ANTLR3_FALSE, ANTLR3_TRUE, and ANTLR3_STRING_struct::chars.</p>
<h3>static <code>ANTLR3_INT32</code> toInt32_16 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>Referenced by stringInit16().</p>
<h3>static <code>ANTLR3_INT32</code> toInt32_8 (struct <code>ANTLR3_STRING_struct</code> * string) [static]</h3>
<p>References ANTLR3_STRING_struct::chars.</p>
<h3>static <code>ANTLR3_INT32</code> toInt32_8 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>Referenced by stringInit8().</p>
<h3>static <code>pANTLR3_STRING</code> toUTF8_16 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_FREE, ANTLR3_MALLOC, ANTLR3_UINT32_CAST, ANTLR3_STRING_struct::chars, ConvertUTF16toUTF8(), ANTLR3_STRING_struct::factory, ANTLR3_STRING_struct::len, lenientConversion, ANTLR3_STRING_FACTORY_struct::newStr8, and ANTLR3_STRING_struct::size. </p>
<p> Referenced by stringInit16().</p>
<h3>static <code>pANTLR3_STRING</code> toUTF8_8 (<code>pANTLR3_STRING</code> string) [static]</h3>
<p>References ANTLR3_STRING_struct::chars, ANTLR3_STRING_struct::factory, ANTLR3_STRING_struct::len, and ANTLR3_STRING_FACTORY_struct::newPtr. </p>
<p> Referenced by stringInit8().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
