---
title: "antlr3-newsize(3)"
name: "antlr3-newsize"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-newsize/"
description: "ANTLR3_STRING_FACTORY_struct –"
---

<p>ANTLR3_STRING_FACTORY_struct &#8211; </p>
<p> Definition of the string factory interface, which creates and tracks strings for you of various shapes and sizes.</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt;</p>
<h3>Data Fields</h3>
<p>void(* <code>close</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory)<br />
 <i>Pointer to function that closes the factory. </i><br />
 void(* <code>destroy</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_STRING</code> string)<br />
 <i>Pointer to function that deletes the string altogether. </i><br />
 <code>ANTLR3_UINT32</code> <code>index</code> </p>
<p> <code>pANTLR3_STRING</code>(* <code>newPtr</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string, <code>ANTLR3_UINT32</code> size)<br />
 <i>Pointer to function that manufactures a string from a given pointer and length. </i><br />
 <code>pANTLR3_STRING</code>(* <code>newPtr8</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string, <code>ANTLR3_UINT32</code> size)<br />
 <i>Pointer to function that manufactures a string from a given pointer and length. </i><br />
 <code>pANTLR3_STRING</code>(* <code>newRaw</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory)<br />
 <i>Pointer to function that manufactures an empty string. </i><br />
 <code>pANTLR3_STRING</code>(* <code>newSize</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>ANTLR3_UINT32</code> size)<br />
 <i>Pointer to function that manufactures a raw string with no text in it but space for size characters. </i><br />
 <code>pANTLR3_STRING</code>(* <code>newStr</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string)<br />
 <i>Pointer to function that manufactures a string from a given pointer and works out the length. </i><br />
 <code>pANTLR3_STRING</code>(* <code>newStr8</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string)<br />
 <i>Pointer to function that manufactures a string from a given pointer and length. </i><br />
 <code>pANTLR3_STRING</code>(* <code>printable</code> )(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_STRING</code> string)<br />
 <i>Pointer to function that returns a copy of the string in printable form without any control characters in it. </i><br />
 <code>pANTLR3_VECTOR</code> <code>strings</code><br />
 <i>List of all the strings that have been allocated by the factory. </i></p>
<h2>Detailed Description</h2>
<p>Definition of the string factory interface, which creates and tracks strings for you of various shapes and sizes.</p>
<h2>Field Documentation</h2>
<h3>void(* <code>ANTLR3_STRING_FACTORY_struct::close</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory)</h3>
<p>Pointer to function that closes the factory. </p>
<p> Referenced by antlr3InputClose(), antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3>void(* <code>ANTLR3_STRING_FACTORY_struct::destroy</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_STRING</code> string)</h3>
<p>Pointer to function that deletes the string altogether. </p>
<p> Referenced by antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_STRING_FACTORY_struct::index</code></h3>
<p>Referenced by antlr3StringFactoryNew(), destroy(), newRaw16(), and newRaw8().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newPtr</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string, <code>ANTLR3_UINT32</code> size)</h3>
<p>Pointer to function that manufactures a string from a given pointer and length. The pointer is assumed to point to characters in the same encoding as the string type, hence if this is a 16 bit string the pointer should point to 16 bit characters. </p>
<p> Referenced by antlr3AsciiSubstr(), antlr3StringFactoryNew(), antlr3UCS2StringFactoryNew(), antlr3UCS2Substr(), createTokenFromToken(), newStr16_16(), subString16(), subString8(), toString(), and toUTF8_8().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newPtr8</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string, <code>ANTLR3_UINT32</code> size)</h3>
<p>Pointer to function that manufactures a string from a given pointer and length. The pointer is assumed to point at 8 bit characters which must be converted on the fly to the encoding of the actual string. </p>
<p> Referenced by antlr3StringFactoryNew(), antlr3UCS2StringFactoryNew(), newStr16_8(), and newStr8().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newRaw</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory)</h3>
<p>Pointer to function that manufactures an empty string. </p>
<p> Referenced by antlr3StringFactoryNew(), antlr3UCS2StringFactoryNew(), newSize16(), newSize8(), toString(), toStringSS(), and toStringTree().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newSize</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>ANTLR3_UINT32</code> size)</h3>
<p>Pointer to function that manufactures a raw string with no text in it but space for size characters. </p>
<p> Referenced by antlr3StringFactoryNew(), antlr3UCS2StringFactoryNew(), newPtr16_16(), newPtr16_8(), newPtr8(), printable16(), printable8(), serializeNode(), and serializeToken().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newStr</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string)</h3>
<p>Pointer to function that manufactures a string from a given pointer and works out the length. The pointer is assumed to point to characters in the same encoding as the string itself, i.e. 16 bit if a 16 bit string and so on. </p>
<p> Referenced by antlr3AsciiFileStreamNew(), antlr3NewAsciiStringCopyStream(), antlr3NewAsciiStringInPlaceStream(), antlr3NewUCS2StringInPlaceStream(), antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::newStr8</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_UINT8</code> string)</h3>
<p>Pointer to function that manufactures a string from a given pointer and length. The pointer should point to 8 bit characters regardless of the actual encoding of the string. The 8 bit characters will be converted to the actual string encoding on the fly. </p>
<p> Referenced by antlr3StringFactoryNew(), antlr3UCS2StringFactoryNew(), getText(), makeDot(), and toUTF8_16().</p>
<h3><code>pANTLR3_STRING</code>(* <code>ANTLR3_STRING_FACTORY_struct::printable</code>)(struct <code>ANTLR3_STRING_FACTORY_struct</code> *factory, <code>pANTLR3_STRING</code> string)</h3>
<p>Pointer to function that returns a copy of the string in printable form without any control characters in it. </p>
<p> Referenced by antlr3StringFactoryNew(), and antlr3UCS2StringFactoryNew().</p>
<h3><code>pANTLR3_VECTOR</code> <code>ANTLR3_STRING_FACTORY_struct::strings</code></h3>
<p>List of all the strings that have been allocated by the factory. </p>
<p> Referenced by antlr3StringFactoryNew(), closeFactory(), destroy(), newRaw16(), and newRaw8(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
