---
title: "antlr3-true(3)"
name: "antlr3-true"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-true/"
description: "src/antlr3convertutf.c –"
---

<h2 class="name">NAME</h2>
<p> src/antlr3convertutf.c &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;antlr3convertutf.h&#8217; </p>
<h3>Defines</h3>
<p> #define <code>false</code> 0 </p>
<p> #define <code>true</code> 1 </p>
<p> #define <code>UNI_SUR_HIGH_END</code> (<code>UTF32</code>)0xDBFF </p>
<p> #define <code>UNI_SUR_HIGH_START</code> (<code>UTF32</code>)0xD800 </p>
<p> #define <code>UNI_SUR_LOW_END</code> (<code>UTF32</code>)0xDFFF </p>
<p> #define <code>UNI_SUR_LOW_START</code> (<code>UTF32</code>)0xDC00 </p>
<h3>Functions</h3>
<p> <code>ConversionResult</code> <code>ConvertUTF16toUTF32</code> (const <code>UTF16</code> **sourceStart, const <code>UTF16</code> *sourceEnd, <code>UTF32</code> **targetStart, <code>UTF32</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF16toUTF8</code> (const <code>UTF16</code> **sourceStart, const <code>UTF16</code> *sourceEnd, <code>UTF8</code> **targetStart, <code>UTF8</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF32toUTF16</code> (const <code>UTF32</code> **sourceStart, const <code>UTF32</code> *sourceEnd, <code>UTF16</code> **targetStart, <code>UTF16</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF32toUTF8</code> (const <code>UTF32</code> **sourceStart, const <code>UTF32</code> *sourceEnd, <code>UTF8</code> **targetStart, <code>UTF8</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF8toUTF16</code> (const <code>UTF8</code> **sourceStart, const <code>UTF8</code> *sourceEnd, <code>UTF16</code> **targetStart, <code>UTF16</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> <code>ConversionResult</code> <code>ConvertUTF8toUTF32</code> (const <code>UTF8</code> **sourceStart, const <code>UTF8</code> *sourceEnd, <code>UTF32</code> **targetStart, <code>UTF32</code> *targetEnd, <code>ConversionFlags</code> flags) </p>
<p> static <code>ANTLR3_BOOLEAN</code> <code>isLegalUTF8</code> (const <code>UTF8</code> *source, int length) </p>
<p> <code>ANTLR3_BOOLEAN</code> <code>isLegalUTF8Sequence</code> (const <code>UTF8</code> *source, const <code>UTF8</code> *sourceEnd) </p>
<h3>Variables</h3>
<p> static const <code>UTF8</code> <code>firstByteMark</code> [7] = { 0x00, 0x00, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC } </p>
<p> static const <code>UTF32</code> <code>halfBase</code> = 0x0010000UL </p>
<p> static const <code>UTF32</code> <code>halfMask</code> = 0x3FFUL </p>
<p> static const int <code>halfShift</code> = 10 </p>
<p> static const <code>UTF32</code> <code>offsetsFromUTF8</code> [6] </p>
<p> static const char <code>trailingBytesForUTF8</code> [256] </p>
<h2>Define Documentation</h2>
<h3>#define false 0</h3>
<h3>#define true 1</h3>
<h3>#define UNI_SUR_HIGH_END (<code>UTF32</code>)0xDBFF</h3>
<p> Referenced by ConvertUTF16toUTF32(), and ConvertUTF16toUTF8().</p>
<h3>#define UNI_SUR_HIGH_START (<code>UTF32</code>)0xD800</h3>
<p> Referenced by ConvertUTF16toUTF32(), ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), ConvertUTF32toUTF8(), ConvertUTF8toUTF16(), and ConvertUTF8toUTF32().</p>
<h3>#define UNI_SUR_LOW_END (<code>UTF32</code>)0xDFFF</h3>
<p> Referenced by ConvertUTF16toUTF32(), ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), ConvertUTF32toUTF8(), ConvertUTF8toUTF16(), and ConvertUTF8toUTF32().</p>
<h3>#define UNI_SUR_LOW_START (<code>UTF32</code>)0xDC00</h3>
<p> Referenced by ConvertUTF16toUTF32(), ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), and ConvertUTF8toUTF16().</p>
<h2>Function Documentation</h2>
<h3><code>ConversionResult</code> ConvertUTF16toUTF32 (const <code>UTF16</code> ** sourceStart, const <code>UTF16</code> * sourceEnd, <code>UTF32</code> ** targetStart, <code>UTF32</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References ANTLR3_FPRINTF, conversionOK, halfBase, halfShift, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, UNI_SUR_HIGH_END, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF16toUTF8 (const <code>UTF16</code> ** sourceStart, const <code>UTF16</code> * sourceEnd, <code>UTF8</code> ** targetStart, <code>UTF8</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References conversionOK, firstByteMark, halfBase, halfShift, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_END, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START. </p>
<p> Referenced by toUTF8_16().</p>
<h3><code>ConversionResult</code> ConvertUTF32toUTF16 (const <code>UTF32</code> ** sourceStart, const <code>UTF32</code> * sourceEnd, <code>UTF16</code> ** targetStart, <code>UTF16</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References conversionOK, halfBase, halfMask, halfShift, sourceIllegal, strictConversion, targetExhausted, UNI_MAX_BMP, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF32toUTF8 (const <code>UTF32</code> ** sourceStart, const <code>UTF32</code> * sourceEnd, <code>UTF8</code> ** targetStart, <code>UTF8</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References conversionOK, firstByteMark, sourceIllegal, strictConversion, targetExhausted, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, and UNI_SUR_LOW_END.</p>
<h3><code>ConversionResult</code> ConvertUTF8toUTF16 (const <code>UTF8</code> ** sourceStart, const <code>UTF8</code> * sourceEnd, <code>UTF16</code> ** targetStart, <code>UTF16</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References conversionOK, halfBase, halfMask, halfShift, isLegalUTF8(), offsetsFromUTF8, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, trailingBytesForUTF8, UNI_MAX_BMP, UNI_MAX_UTF16, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, UNI_SUR_LOW_END, and UNI_SUR_LOW_START.</p>
<h3><code>ConversionResult</code> ConvertUTF8toUTF32 (const <code>UTF8</code> ** sourceStart, const <code>UTF8</code> * sourceEnd, <code>UTF32</code> ** targetStart, <code>UTF32</code> * targetEnd, <code>ConversionFlags</code> flags)</h3>
<p> References conversionOK, isLegalUTF8(), offsetsFromUTF8, sourceExhausted, sourceIllegal, strictConversion, targetExhausted, trailingBytesForUTF8, UNI_MAX_LEGAL_UTF32, UNI_REPLACEMENT_CHAR, UNI_SUR_HIGH_START, and UNI_SUR_LOW_END.</p>
<h3>static <code>ANTLR3_BOOLEAN</code> isLegalUTF8 (const <code>UTF8</code> * source, int length) [static]</h3>
<p> Referenced by ConvertUTF8toUTF16(), ConvertUTF8toUTF32(), and isLegalUTF8Sequence().</p>
<h3><code>ANTLR3_BOOLEAN</code> isLegalUTF8Sequence (const <code>UTF8</code> * source, const <code>UTF8</code> * sourceEnd)</h3>
<p> References isLegalUTF8(), and trailingBytesForUTF8.</p>
<h2>Variable Documentation</h2>
<h3>const <code>UTF8</code> <code>firstByteMark</code>[7] = { 0x00, 0x00, 0xC0, 0xE0, 0xF0, 0xF8, 0xFC } [static]</h3>
<p> Referenced by ConvertUTF16toUTF8(), and ConvertUTF32toUTF8().</p>
<h3>const <code>UTF32</code> <code>halfBase</code> = 0x0010000UL [static]</h3>
<p> Referenced by ConvertUTF16toUTF32(), ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), and ConvertUTF8toUTF16().</p>
<h3>const <code>UTF32</code> <code>halfMask</code> = 0x3FFUL [static]</h3>
<p> Referenced by ConvertUTF32toUTF16(), and ConvertUTF8toUTF16().</p>
<h3>const int <code>halfShift</code> = 10 [static]</h3>
<p> Referenced by ConvertUTF16toUTF32(), ConvertUTF16toUTF8(), ConvertUTF32toUTF16(), and ConvertUTF8toUTF16().</p>
<h3>const <code>UTF32</code> <code>offsetsFromUTF8</code>[6] [static]<code>Initial value:</code></h3>
<pre>
 { 0x00000000UL, 0x00003080UL, 0x000E2080UL, 
             0x03C82080UL, 0xFA082080UL, 0x82082080UL }
</pre>
<p> Referenced by ConvertUTF8toUTF16(), and ConvertUTF8toUTF32().</p>
<h3>const char <code>trailingBytesForUTF8</code>[256] [static]<code>Initial value:</code></h3>
<pre>
 {
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5
}
</pre>
<p> Referenced by ConvertUTF8toUTF16(), ConvertUTF8toUTF32(), and isLegalUTF8Sequence().</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Function Documentation</a></p>
<dd>
<dt><a href="#lbAW">Variable Documentation</a></p>
<dd>
<dt><a href="#lbBD">Author</a></p>
<dd></dl>
