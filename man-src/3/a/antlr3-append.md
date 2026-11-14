---
title: "antlr3-append(3)"
name: "antlr3-append"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-append/"
description: "ANTLR3_STRING_struct –"
---

<h2 class="name">NAME</h2>
<p> ANTLR3_STRING_struct &#8211; </p>
<p> Base string class tracks the allocations and provides simple string tracking functions.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;<a href="file:/usr/include/antlr3string.h">antlr3string.h</a>&gt;</p>
<h3>Data Fields</h3>
<p> <code>pANTLR3_UINT8</code>(* <code>addc</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> c)<br />
 <i>Pointer to function that adds a single character to the end of the string, in the encoding of the string &#8211; 8 bit, 16 bit, utf-8 etc. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>addi</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_INT32</code> i)<br />
 <i>Pointer to function that adds the stringified representation of an integer to the string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>append</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *newbit)<br />
 <i>Pointer to function adds a raw char * type pointer in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>append8</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *newbit)<br />
 <i>Pointer to function adds a raw char * type pointer in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>appendS</code> )(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *newbit)<br />
 <i>Pointer to function appends a copy of the characters contained in another string. </i><br />
 <code>ANTLR3_UCHAR</code>(* <code>charAt</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> offset)<br />
 <i>Pointer to a function that returns the character indexed at the supplied offset as a 32 bit character. </i><br />
 <code>pANTLR3_UINT8</code> <code>chars</code><br />
 <i>Pointer to the current string value (starts at NULL unless the string allocator is told to create it with a pre known size. </i><br />
 <code>ANTLR3_UINT32</code>(* <code>compare</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *compStr)<br />
 <i>Pointer to a function that compares the text of a string with the supplied character string (which is assumed to be in the same encoding as the string itself) and returns a result a la strcmp(). </i><br />
 <code>ANTLR3_UINT32</code>(* <code>compare8</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *compStr)<br />
 <i>Pointer to function that compares the text of a string to the supplied 8 bit character string and returns a result a la strcmp(). </i><br />
 <code>ANTLR3_UINT32</code>(* <code>compareS</code> )(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *compStr)<br />
 <i>Pointer to a function that compares the text of a string with the supplied string (which is assumed to be in the same encoding as the string itself) and returns a result a la strcmp(). </i><br />
 <code>ANTLR3_UINT8</code> <code>encoding</code><br />
 <i>Occasionally it is useful to know what the encoding of the string actually is, hence it is stored here as one the ANTLR3_ENCODING_ values. </i><br />
 <code>pANTLR3_STRING_FACTORY</code> <code>factory</code><br />
 <i>The factory that created this string. </i><br />
 <code>ANTLR3_UINT32</code> <code>index</code><br />
 <i>Index of string (allocation number) in case someone wants to explicitly release it. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>insert</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, const char *newbit)<br />
 <i>Pointer to function that inserts the supplied string at the specified offset in the current string in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>insert8</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, const char *newbit)<br />
 <i>Pointer to function that inserts the supplied string at the specified offset in the current string in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>inserti</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i)<br />
 <i>Pointer to function that inserts the supplied integer in string form at the specified offset in the current string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>insertS</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, struct <code>ANTLR3_STRING_struct</code> *newbit)<br />
 <i>Pointer to function that inserts a copy of the characters in the supplied string at the specified offset in the current string. </i><br />
 <code>ANTLR3_UINT32</code> <code>len</code><br />
 <i>Current length of the string up to and not including, the trailing &#8221; Note that the actual allocation (-&gt;size) is always at least one byte more than this to accommodate trailing &#8221;. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>set</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *<code>chars</code>)<br />
 <i>Pointer to function that sets the string value to a specific string in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>set8</code> )(struct <code>ANTLR3_STRING_struct</code> *string, const char *<code>chars</code>)<br />
 <i>Pointer to function that sets the string value to a specific 8 bit string in the default encoding for this string. </i><br />
 <code>pANTLR3_UINT8</code>(* <code>setS</code> )(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *<code>chars</code>)<br />
 <i>Pointer to function that sets the string value to a copy of the supplied string (strings must be in the same encoding. </i><br />
 <code>ANTLR3_UINT32</code> <code>size</code><br />
 <i>Current size of the string in bytes including the trailing &#8221;. </i><br />
 struct <code>ANTLR3_STRING_struct</code> *(* <code>subString</code> )(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex)<br />
 <i>Pointer to a function that returns a substring of the supplied string a la .subString(s,e) in the Java language. </i><br />
 struct <code>ANTLR3_STRING_struct</code> *(* <code>to8</code> )(struct <code>ANTLR3_STRING_struct</code> *string)<br />
 <i>Pointer to a function that yields an 8 bit string regardless of the encoding of the supplied string. </i><br />
 <code>ANTLR3_INT32</code>(* <code>toInt32</code> )(struct <code>ANTLR3_STRING_struct</code> *string)<br />
 <i>Pointer to a function that returns the integer representation of any numeric characters at the beginning of the string. </i><br />
 struct <code>ANTLR3_STRING_struct</code> *(* <code>toUTF8</code> )(struct <code>ANTLR3_STRING_struct</code> *string)<br />
 <i>Pointer to a function that yields a UT8 encoded string of the current string, regardless of the current encoding of the string. </i></p>
<h2>Detailed Description</h2>
<p> Base string class tracks the allocations and provides simple string tracking functions. </p>
<p> Mostly you can work directly on the string for things that don&#8217;t reallocate it, like strchr() etc. Perhaps someone will want to provide implementations for UTF8 and so on.</p>
<h2>Field Documentation</h2>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::addc</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> c)</h3>
<p> Pointer to function that adds a single character to the end of the string, in the encoding of the string &#8211; 8 bit, 16 bit, utf-8 etc. Input is a single UTF32 (32 bits wide integer) character. </p>
<p> Referenced by consumeHiddenToken(), consumeToken(), defineDotEdges(), defineDotNodes(), makeDot(), serializeNode(), serializeText(), serializeToken(), and toString().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::addi</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_INT32</code> i)</h3>
<p> Pointer to function that adds the stringified representation of an integer to the string. </p>
<p> Referenced by serializeNode(), serializeToken(), and toString().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::append</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *newbit)</h3>
<p> Pointer to function adds a raw char * type pointer in the default encoding for this string. For instance, if this is ASCII 8 bit, then this function is the same as append8 but if the encoding is 16 bit, then the pointer is assumed to point to 16 bit characters not 8 bit. </p>
<p> Referenced by serializeText().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::append8</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *newbit)</h3>
<p> Pointer to function adds a raw char * type pointer in the default encoding for this string. For instance, if this is a 16 bit string, then this function assumes the pointer points to 8 bit characters that must be converted on the fly. </p>
<p> Referenced by defineDotEdges(), defineDotNodes(), getMissingSymbol(), makeDot(), toString(), and toStringTree().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::appendS</code>)(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *newbit)</h3>
<p> Pointer to function appends a copy of the characters contained in another string. Strings must be in the same encoding. </p>
<p> Referenced by toString().</p>
<h3><code>ANTLR3_UCHAR</code>(* <code>ANTLR3_STRING_struct::charAt</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> offset)</h3>
<p> Pointer to a function that returns the character indexed at the supplied offset as a 32 bit character. </p>
<p> Referenced by defineDotEdges(), defineDotNodes(), makeDot(), and serializeText().</p>
<h3><code>pANTLR3_UINT8</code> <code>ANTLR3_STRING_struct::chars</code></h3>
<p> Pointer to the current string value (starts at NULL unless the string allocator is told to create it with a pre known size. </p>
<p> Referenced by addc16(), append16_16(), append16_8(), append8(), appendS(), charAt16(), compare16_16(), compare16_8(), compare8(), compareS(), consumeHiddenToken(), consumeToken(), createTokenFromToken(), displayRecognitionError(), handshake(), insert16_16(), insert16_8(), insert8(), insertS(), newPtr16_16(), newPtr16_8(), newPtr8(), newSize16(), newSize8(), printable16(), printable8(), replaceChildren(), set16_16(), set16_8(), set8(), setS(), stringFree(), subString16(), subString8(), to8_16(), toInt32_16(), toInt32_8(), toUTF8_16(), and toUTF8_8().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_STRING_struct::compare</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *compStr)</h3>
<p> Pointer to a function that compares the text of a string with the supplied character string (which is assumed to be in the same encoding as the string itself) and returns a result a la strcmp().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_STRING_struct::compare8</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *compStr)</h3>
<p> Pointer to function that compares the text of a string to the supplied 8 bit character string and returns a result a la strcmp().</p>
<h3><code>ANTLR3_UINT32</code>(* <code>ANTLR3_STRING_struct::compareS</code>)(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *compStr)</h3>
<p> Pointer to a function that compares the text of a string with the supplied string (which is assumed to be in the same encoding as the string itself) and returns a result a la strcmp(). </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3><code>ANTLR3_UINT8</code> <code>ANTLR3_STRING_struct::encoding</code></h3>
<p> Occasionally it is useful to know what the encoding of the string actually is, hence it is stored here as one the ANTLR3_ENCODING_ values.</p>
<h3><code>pANTLR3_STRING_FACTORY</code> <code>ANTLR3_STRING_struct::factory</code></h3>
<p> The factory that created this string. </p>
<p> Referenced by serializeNode(), serializeToken(), subString16(), subString8(), to8_16(), toString(), toUTF8_16(), and toUTF8_8().</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_STRING_struct::index</code></h3>
<p> Index of string (allocation number) in case someone wants to explicitly release it.</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::insert</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, const char *newbit)</h3>
<p> Pointer to function that inserts the supplied string at the specified offset in the current string in the default encoding for this string. For instance, if this is an 8 bit string, then this is the same as insert8, but if this is a 16 bit string, then the poitner must point to 16 bit characters.</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::insert8</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, const char *newbit)</h3>
<p> Pointer to function that inserts the supplied string at the specified offset in the current string in the default encoding for this string. For instance, if this is a 16 bit string then the pointer is assumed to point at 8 bit characteres that must be converted on the fly. </p>
<p> Referenced by consumeHiddenToken(), and consumeToken().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::inserti</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, <code>ANTLR3_INT32</code> i)</h3>
<p> Pointer to function that inserts the supplied integer in string form at the specified offset in the current string.</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::insertS</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> point, struct <code>ANTLR3_STRING_struct</code> *newbit)</h3>
<p> Pointer to function that inserts a copy of the characters in the supplied string at the specified offset in the current string. strings must be in the same encoding.</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_STRING_struct::len</code></h3>
<p> Current length of the string up to and not including, the trailing &#8221; Note that the actual allocation (-&gt;size) is always at least one byte more than this to accommodate trailing &#8221;. </p>
<p> Referenced by addc16(), addc8(), append16_16(), append16_8(), append8(), appendS(), charAt16(), charAt8(), createTokenFromToken(), defineDotEdges(), defineDotNodes(), insert16_16(), insert16_8(), insert8(), makeDot(), printable16(), printable8(), serializeText(), subString16(), subString8(), to8_16(), toUTF8_16(), and toUTF8_8().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::set</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *<code>chars</code>)</h3>
<p> Pointer to function that sets the string value to a specific string in the default encoding for this string. For instance, if this is ASCII 8 bit, then this function is the same as set8 but if the encoding is 16 bit, then the pointer is assumed to point to 16 bit characters not 8 bit. </p>
<p> Referenced by serializeNode(), and serializeToken().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::set8</code>)(struct <code>ANTLR3_STRING_struct</code> *string, const char *<code>chars</code>)</h3>
<p> Pointer to function that sets the string value to a specific 8 bit string in the default encoding for this string. For instance, if this is a 16 bit string, then this function is the same as set8 but if the encoding is 16 bit, then the pointer is assumed to point to 8 bit characters that must be converted to 16 bit characters on the fly. </p>
<p> Referenced by setText8().</p>
<h3><code>pANTLR3_UINT8</code>(* <code>ANTLR3_STRING_struct::setS</code>)(struct <code>ANTLR3_STRING_struct</code> *string, struct <code>ANTLR3_STRING_struct</code> *<code>chars</code>)</h3>
<p> Pointer to function that sets the string value to a copy of the supplied string (strings must be in the same encoding.</p>
<h3><code>ANTLR3_UINT32</code> <code>ANTLR3_STRING_struct::size</code></h3>
<p> Current size of the string in bytes including the trailing &#8221;. </p>
<p> Referenced by addc16(), addc8(), append16_16(), append16_8(), append8(), appendS(), insert16_16(), insert16_8(), insert8(), set16_16(), set16_8(), set8(), to8_16(), and toUTF8_16().</p>
<h3>struct <code>ANTLR3_STRING_struct</code>*(* <code>ANTLR3_STRING_struct::subString</code>)(struct <code>ANTLR3_STRING_struct</code> *string, <code>ANTLR3_UINT32</code> startIndex, <code>ANTLR3_UINT32</code> endIndex) [read]</h3>
<p> Pointer to a function that returns a substring of the supplied string a la .subString(s,e) in the Java language.</p>
<h3>struct <code>ANTLR3_STRING_struct</code>*(* <code>ANTLR3_STRING_struct::to8</code>)(struct <code>ANTLR3_STRING_struct</code> *string) [read]</h3>
<p> Pointer to a function that yields an 8 bit string regardless of the encoding of the supplied string. This is useful when you want to use the text of a token in some way that requires an 8 bit value, such as the key for a hashtable. The function is required to produce a usable string even if the text given as input has characters that do not fit in 8 bit space, it will replace them with some arbitrary character such as &#8216;?&#8217; </p>
<p> Referenced by displayRecognitionError().</p>
<h3><code>ANTLR3_INT32</code>(* <code>ANTLR3_STRING_struct::toInt32</code>)(struct <code>ANTLR3_STRING_struct</code> *string)</h3>
<p> Pointer to a function that returns the integer representation of any numeric characters at the beginning of the string. </p>
<p> Referenced by stringInit16(), and stringInit8().</p>
<h3>struct <code>ANTLR3_STRING_struct</code>*(* <code>ANTLR3_STRING_struct::toUTF8</code>)(struct <code>ANTLR3_STRING_struct</code> *string) [read]</h3>
<p> Pointer to a function that yields a UT8 encoded string of the current string, regardless of the current encoding of the string. Because there is currently no UTF8 handling in the string class, it creates therefore, a string that is useful only for read only applications as it will not contain methods that deal with UTF8 at the moment. </p>
<p> Referenced by serializeNode(), serializeToken(), stringInit16(), and stringInit8(). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBG">Author</a></p>
<dd></dl>
