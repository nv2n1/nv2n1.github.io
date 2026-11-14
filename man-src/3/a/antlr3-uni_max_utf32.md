---
title: "antlr3-uni_max_utf32(3)"
name: "antlr3-uni_max_utf32"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-uni_max_utf32/"
description: "include/antlr3convertutf.h –"
---

<p>include/antlr3convertutf.h &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/antlr3defs.h">antlr3defs.h</a>&gt; </p>
<h3>Defines</h3>
<p>#define <code>UNI_MAX_BMP</code> (<code>UTF32</code>)0x0000FFFF </p>
<p> #define <code>UNI_MAX_LEGAL_UTF32</code> (<code>UTF32</code>)0x0010FFFF </p>
<p> #define <code>UNI_MAX_UTF16</code> (<code>UTF32</code>)0x0010FFFF </p>
<p> #define <code>UNI_MAX_UTF32</code> (<code>UTF32</code>)0x7FFFFFFF </p>
<p> #define <code>UNI_REPLACEMENT_CHAR</code> (<code>UTF32</code>)0x0000FFFD </p>
<h3>Typedefs</h3>
<p>typedef <code>ANTLR3_UINT16</code> <code>UTF16</code> </p>
<p> typedef <code>ANTLR3_UINT32</code> <code>UTF32</code> </p>
<p> typedef <code>ANTLR3_UINT8</code> <code>UTF8</code> </p>
<h3>Enumerations</h3>
<p>enum <code>ConversionFlags</code> { <code>strictConversion</code> = 0, <code>lenientConversion</code> } </p>
<p> enum <code>ConversionResult</code> { <code>conversionOK</code>, <code>sourceExhausted</code>, <code>targetExhausted</code>, <code>sourceIllegal</code> } </p>
<h3>Functions</h3>
<p><code>ConversionResult</code> <code>ConvertUTF16toUTF32</code> (const <code>UTF16</code> **sourceStart, const <code>UTF16</code> *sourceEnd, <code>UTF32</code> **targetStart, <code>UTF32</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF16toUTF8</code> (const <code>UTF16</code> **sourceStart, const <code>UTF16</code> *sourceEnd, <code>UTF8</code> **targetStart, <code>UTF8</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF32toUTF16</code> (const <code>UTF32</code> **sourceStart, const <code>UTF32</code> *sourceEnd, <code>UTF16</code> **targetStart, <code>UTF16</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF32toUTF8</code> (const <code>UTF32</code> **sourceStart, const <code>UTF32</code> *sourceEnd, <code>UTF8</code> **targetStart, <code>UTF8</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF8toUTF16</code> (const <code>UTF8</code> **sourceStart, const <code>UTF8</code> *sourceEnd, <code>UTF16</code> **targetStart, <code>UTF16</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF8toUTF32</code> (const <code>UTF8</code> **sourceStart, const <code>UTF8</code> *sourceEnd, <code>UTF32</code> **targetStart, <code>UTF32</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>isLegalUTF8Sequence</code> (const <code>UTF8</code> *source, const <code>UTF8</code> *sourceEnd) </p>
<h2>Define Documentation</h2>
<h3>#define UNI_MAX_BMP (<code>UTF32</code>)0x0000FFFF</h3>
<p>Referenced by ConvertUTF32toUTF16(), and ConvertUTF8toUTF16().</p>
<h3>#define UNI_MAX_LEGAL_UTF32 (<code>UTF32</code>)0x0010FFFF</h3>
<p>Referenced by ConvertUTF32toUTF16(), ConvertUTF32toUTF8(), and ConvertUTF8toUTF32().</p>
<h3>#define UNI_MAX_UTF16 (<code>UTF32</code>)0x0010FFFF</h3>
<p>Referenced by ConvertUTF8toUTF16().</p>
<h3>#define UNI_MAX_UTF32 (<code>UTF32</code>)0x7FFFFFFF</h3>
<h3>#define UNI_REPLACEMENT_CHAR (<code>UTF32</code>)0x0000FFFD</h3>
<p>Referenced by ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), ConvertUTF32toUTF8(), ConvertUTF8toUTF16(), and ConvertUTF8toUTF32().</p>
<h2>Typedef Documentation</h2>
<h3>typedef <code>ANTLR3_UINT16</code> <code>UTF16</code></h3>
<h3>typedef <code>ANTLR3_UINT32</code> <code>UTF32</code></h3>
<h3>typedef <code>ANTLR3_UINT8</code> <code>UTF8</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>ConversionFlags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>strictConversion </i></p>
<dd>
<dt><i>lenientConversion </i></p>
<dd></dl>
<h3>enum <code>ConversionResult</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>conversionOK </i></p>
<dd>
<dt><i>sourceExhausted </i></p>
<dd>
<dt><i>targetExhausted </i></p>
<dd>
<dt><i>sourceIllegal </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3><code>ConversionResult</code> ConvertUTF16toUTF32 (const <code>UTF16</code> ** sourceStart, const <code>UTF16</code> * sourceEnd, <code>UTF32</code> ** targetStart, <code>UTF32</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References ANTLR3_FPRINTF, conversionOK, halfBase, halfShift, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, UNI_SUR_HIGH_END, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF16toUTF8 (const <code>UTF16</code> ** sourceStart, const <code>UTF16</code> * sourceEnd, <code>UTF8</code> ** targetStart, <code>UTF8</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References conversionOK, firstByteMark, halfBase, halfShift, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_END, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START. </p>
<p> Referenced by toUTF8_16().</p>
<h3><code>ConversionResult</code> ConvertUTF32toUTF16 (const <code>UTF32</code> ** sourceStart, const <code>UTF32</code> * sourceEnd, <code>UTF16</code> ** targetStart, <code>UTF16</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References conversionOK, halfBase, halfMask, halfShift, sourceIllegal, strictConversion, targetExhausted, UNI_MAX_BMP, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF32toUTF8 (const <code>UTF32</code> ** sourceStart, const <code>UTF32</code> * sourceEnd, <code>UTF8</code> ** targetStart, <code>UTF8</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References conversionOK, firstByteMark, sourceIllegal, strictConversion, targetExhausted, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, and UNI_SUR_LOW_END.</p>
<h3><code>ConversionResult</code> ConvertUTF8toUTF16 (const <code>UTF8</code> ** sourceStart, const <code>UTF8</code> * sourceEnd, <code>UTF16</code> ** targetStart, <code>UTF16</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References conversionOK, halfBase, halfMask, halfShift, isLegalUTF8(), offsetsFromUTF8, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, trailingBytesForUTF8, UNI_MAX_BMP, UNI_MAX_UTF16, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF8toUTF32 (const <code>UTF8</code> ** sourceStart, const <code>UTF8</code> * sourceEnd, <code>UTF32</code> ** targetStart, <code>UTF32</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p>References conversionOK, isLegalUTF8(), offsetsFromUTF8, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, trailingBytesForUTF8, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, and UNI_SUR_LOW_END.</p>
<h3><code>ANTLR3_BOOLEAN</code> isLegalUTF8Sequence (const <code>UTF8</code> * source, const <code>UTF8</code> * sourceEnd)</h3>
<p>References isLegalUTF8(), and trailingBytesForUTF8.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for ANTLR3C from the source code.</p>
