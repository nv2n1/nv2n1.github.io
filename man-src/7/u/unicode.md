---
title: "unicode(7)"
name: "unicode"
section: "7"
letter: "u"
url: "/docs/linux/man/7-unicode/"
description: "unicode – universal character set"
---

<p>unicode &#8211; universal character set</p>
<h2>Description</h2>
<p>The international standard ISO 10646 defines the Universal Character Set (UCS). UCS contains all characters of all other character set standards. It also guarantees &quot;round-trip compatibility&quot;; in other words, conversion tables can be built such that no information is lost when a string is converted from any other encoding to UCS and back. </p>
<p> UCS contains the characters required to represent practically all known languages. This includes not only the Latin, Greek, Cyrillic, Hebrew, Arabic, Armenian, and Georgian scripts, but also Chinese, Japanese and Korean Han ideographs as well as scripts such as Hiragana, Katakana, Hangul, Devanagari, Bengali, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, Malayalam, Thai, Lao, Khmer, Bopomofo, Tibetan, Runic, Ethiopic, Canadian Syllabics, Cherokee, Mongolian, Ogham, Myanmar, Sinhala, Thaana, Yi, and others. For scripts not yet covered, research on how to best encode them for computer usage is still going on and they will be added eventually. This might eventually include not only Hieroglyphs and various historic Indo-European languages, but even some selected artistic scripts such as Tengwar, Cirth, and Klingon. UCS also covers a large number of graphical, typographical, mathematical, and scientific symbols, including those provided by TeX, Postscript, APL, MS-DOS, MS-Windows, Macintosh, OCR fonts, as well as many word processing and publishing systems, and more are being added. </p>
<p> The UCS standard (ISO 10646) describes a 31-bit character set architecture consisting of 128 24-bit <i>groups</i>, each divided into 256 16-bit <i>planes</i> made up of 256 8-bit <i>rows</i> with 256 <i>column</i> positions, one for each character. Part 1 of the standard (ISO 10646-1) defines the first 65534 code positions (0x0000 to 0xfffd), which form the <i>Basic Multilingual Plane</i> (BMP), that is plane 0 in group 0. Part 2 of the standard (ISO 10646-2) adds characters to group 0 outside the BMP in several <i>supplementary planes</i> in the range 0x10000 to 0x10ffff. There are no plans to add characters beyond 0x10ffff to the standard, therefore of the entire code space, only a small fraction of group 0 will ever be actually used in the foreseeable future. The BMP contains all characters found in the commonly used other character sets. The supplemental planes added by ISO 10646-2 cover only more exotic characters for special scientific, dictionary printing, publishing industry, higher-level protocol and enthusiast needs. </p>
<p> The representation of each UCS character as a 2-byte word is referred to as the UCS-2 form (only for BMP characters), whereas UCS-4 is the representation of each character by a 4-byte word. In addition, there exist two encoding forms UTF-8 for backward compatibility with ASCII processing software and UTF-16 for the backward-compatible handling of non-BMP characters up to 0x10ffff by UCS-2 software. </p>
<p> The UCS characters 0x0000 to 0x007f are identical to those of the classic US-ASCII character set and the characters in the range 0x0000 to 0x00ff are identical to those in ISO 8859-1 (Latin-1).</p>
<h3>Combining characters</h3>
<p>Some code points in UCS have been assigned to <i>combining characters</i>. These are similar to the nonspacing accent keys on a typewriter. A combining character just adds an accent to the previous character. The most important accented characters have codes of their own in UCS, however, the combining character mechanism allows us to add accents and other diacritical marks to any character. The combining characters always follow the character which they modify. For example, the German character Umlaut-A (&quot;Latin capital letter A with diaeresis&quot;) can either be represented by the precomposed UCS code 0x00c4, or alternatively as the combination of a normal &quot;Latin capital letter A&quot; followed by a &quot;combining diaeresis&quot;: 0x0041 0x0308. </p>
<p> Combining characters are essential for instance for encoding the Thai script or for mathematical typesetting and users of the International Phonetic Alphabet.</p>
<h3>Implementation levels</h3>
<p>As not all systems are expected to support advanced mechanisms like combining characters, ISO 10646-1 specifies the following three <i>implementation levels</i> of UCS:</p>
<dl>
<dt>Level 1</p>
<dd>Combining characters and Hangul Jamo (a variant encoding of the Korean script, where a Hangul syllable glyph is coded as a triplet or pair of vowel/consonant codes) are not supported.</p>
<dt>Level 2</p>
<dd>In addition to level 1, combining characters are now allowed for some languages where they are essential (e.g., Thai, Lao, Hebrew, Arabic, Devanagari, Malayalam).</p>
<dt>Level 3</p>
<dd>All UCS characters are supported.</dl>
<p> The Unicode 3.0 Standard published by the Unicode Consortium contains exactly the UCS Basic Multilingual Plane at implementation level 3, as described in ISO 10646-1:2000. Unicode 3.1 added the supplemental planes of ISO 10646-2. The Unicode standard and technical reports published by the Unicode Consortium provide much additional information on the semantics and recommended usages of various characters. They provide guidelines and algorithms for editing, sorting, comparing, normalizing, converting, and displaying Unicode strings.</p>
<h3>Unicode under Linux</h3>
<p>Under GNU/Linux, the C type <i>wchar_t</i> is a signed 32-bit integer type. Its values are always interpreted by the C library as UCS code values (in all locales), a convention that is signaled by the GNU C library to applications by defining the constant <code>__STDC_ISO_10646__</code> as specified in the ISO C99 standard. </p>
<p> UCS/Unicode can be used just like ASCII in input/output streams, terminal communication, plaintext files, filenames, and environment variables in the ASCII compatible UTF-8 multibyte encoding. To signal the use of UTF-8 as the character encoding to all applications, a suitable <i>locale</i> has to be selected via environment variables (e.g., &quot;LANG=en_GB.UTF-8&quot;). </p>
<p> The <code>nl_langinfo(CODESET)</code> function returns the name of the selected encoding. Library functions such as <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3) and <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3) can be used to transform the internal <i>wchar_t</i> characters and strings into the system character encoding and back and <code><a href="/docs/linux/man/3-wcwidth/">wcwidth</a></code>(3) tells, how many positions (0-2) the cursor is advanced by the output of a character.</p>
<h3>Private Use Areas (PUA)</h3>
<p>In the Basic Multilingual Plane, the range 0xe000 to 0xf8ff will never be assigned to any characters by the standard and is reserved for private usage. For the Linux community, this private area has been subdivided further into the range 0xe000 to 0xefff which can be used individually by any end-user and the Linux zone in the range 0xf000 to 0xf8ff where extensions are coordinated among all Linux users. The registry of the characters assigned to the Linux zone is maintained by LANANA and the registry itself is <i>Documentation/admin-guide/unicode.rst</i> in the Linux kernel sources (or <i>Documentation/unicode.txt</i> before Linux 4.10). </p>
<p> Two other planes are reserved for private usage, plane 15 (Supplementary Private Use Area-A, range 0xf0000 to 0xffffd) and plane 16 (Supplementary Private Use Area-B, range 0x100000 to 0x10fffd).</p>
<h3>Literature</h3>
<dl>
<dt>*</p>
<dd>Information technology &#8212; Universal Multiple-Octet Coded Character Set (UCS) &#8212; Part 1: Architecture and Basic Multilingual Plane. International Standard ISO/IEC 10646-1, International Organization for Standardization, Geneva, 2000.</p>
<dd>This is the official specification of UCS . Available from</p>
<dt>*</p>
<dd>The Unicode Standard, Version 3.0. The Unicode Consortium, Addison-Wesley, Reading, MA, 2000, ISBN 0-201-61633-5.</p>
<dt>*</p>
<dd>S. Harbison, G. Steele. C: A Reference Manual. Fourth edition, Prentice Hall, Englewood Cliffs, 1995, ISBN 0-13-326224-3.</p>
<dd>A good reference book about the C programming language. The fourth edition covers the 1994 Amendment 1 to the ISO C90 standard, which adds a large number of new C library functions for handling wide and multibyte character encodings, but it does not yet cover ISO C99, which improved wide and multibyte character support even further.</p>
<dt>*</p>
<dd>Unicode Technical Reports.</p>
<dl>
<dd></dl>
<dt>*</p>
<dd>Markus Kuhn: UTF-8 and Unicode FAQ for UNIX/Linux.</p>
<dl>
<dd></dl>
<dt>*</p>
<dd>Bruno Haible: Unicode HOWTO.</p>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
