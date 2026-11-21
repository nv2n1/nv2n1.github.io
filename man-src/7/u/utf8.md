---

title: "utf8(7)"
name: "utf8"
section: "7"
letter: "u"
url: "/docs/linux/man/7-utf8/"
description: "UTF-8 – an ASCII compatible multibyte Unicode encoding"
---

<p>UTF-8 &#8211; an ASCII compatible multibyte Unicode encoding </p>
<p> The Unicode 3.0 character set occupies a 16-bit code space. The most obvious Unicode encoding (known as UCS-2) consists of a sequence of 16-bit words. Such strings can contain---as part of many 16-bit characters---bytes such as &#8216;\0&#8217; or &#8216;/&#8216;, which have a special meaning in filenames and other C library function arguments. In addition, the majority of UNIX tools expect ASCII files and can&#8217;t read 16-bit words as characters without major modifications. For these reasons, UCS-2 is not a suitable external encoding of Unicode in filenames, text files, environment variables, and so on. The ISO 10646 Universal Character Set (UCS), a superset of Unicode, occupies an even larger code space---31 bits---and the obvious UCS-4 encoding for it (a sequence of 32-bit words) has the same problems. </p>
<p>The UTF-8 encoding of Unicode and UCS does not have these problems and is the common way in which Unicode is used on UNIX-style operating systems.  </p>
<h3>Properties</h3>
<p> The UTF-8 encoding has the following nice properties: </p>
<dl>
<dt>*</dt>
<dd> <p> UCS characters 0x00000000 to 0x0000007f (the classic US-ASCII characters) are encoded simply as bytes 0x00 to 0x7f (ASCII compatibility). This means that files and strings which contain only 7-bit ASCII characters have the same encoding under both ASCII and UTF-8 . </p>
 </dd>
<dt>*</dt>
<dd> <p> All UCS characters greater than 0x7f are encoded as a multibyte sequence consisting only of bytes in the range 0x80 to 0xfd, so no ASCII byte can appear as part of another character and there are no problems with, for example, &#8216;\0&#8217; or &#8216;/&#8216;. </p>
 </dd>
<dt>*</dt>
<dd> <p> The lexicographic sorting order of UCS-4 strings is preserved. </p>
 </dd>
<dt>*</dt>
<dd> <p> All possible 2^31 UCS codes can be encoded using UTF-8. </p>
 </dd>
<dt>*</dt>
<dd> <p> The bytes 0xc0, 0xc1, 0xfe, and 0xff are never used in the UTF-8 encoding. </p>
 </dd>
<dt>*</dt>
<dd> <p> The first byte of a multibyte sequence which represents a single non-ASCII UCS character is always in the range 0xc2 to 0xfd and indicates how long this multibyte sequence is. All further bytes in a multibyte sequence are in the range 0x80 to 0xbf. This allows easy resynchronization and makes the encoding stateless and robust against missing bytes. </p>
 </dd>
<dt>*</dt>
<dd> <p> UTF-8 encoded UCS characters may be up to six bytes long, however the Unicode standard specifies no characters above 0x10ffff, so Unicode characters can be only up to four bytes long in UTF-8. </p>
 </dd></dl>
<h3>Encoding</h3>
<p> The following byte sequences are used to represent a character. The sequence to be used depends on the UCS code number of the character: </p>
<dl>
<dt>0x00000000 - 0x0000007F:</dt>
<dd> <p> 0 <i>xxxxxxx</i> </p>
 </dd>
<dt>0x00000080 - 0x000007FF:</dt>
<dd> <p> 110 <i>xxxxx</i> 10 <i>xxxxxx</i> </p>
 </dd>
<dt>0x00000800 - 0x0000FFFF:</dt>
<dd> <p> 1110 <i>xxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> </p>
 </dd>
<dt>0x00010000 - 0x001FFFFF:</dt>
<dd> <p> 11110 <i>xxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> </p>
 </dd>
<dt>0x00200000 - 0x03FFFFFF:</dt>
<dd> <p> 111110 <i>xx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> </p>
 </dd>
<dt>0x04000000 - 0x7FFFFFFF:</dt>
<dd> <p> 1111110 <i>x</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> 10 <i>xxxxxx</i> </p>
 </dd></dl>
<p>The <i>xxx</i> bit positions are filled with the bits of the character code number in binary representation, most significant bit first (big-endian). Only the shortest possible multibyte sequence which can represent the code number of the character can be used. </p>
<p>The UCS code values 0xd800-0xdfff (UTF-16 surrogates) as well as 0xfffe and 0xffff (UCS noncharacters) should not appear in conforming UTF-8 streams. According to RFC 3629 no point above U+10FFFF should be used, which limits characters to four bytes.  </p>
<h3>Example</h3>
<p> The Unicode character 0xa9 = 1010 1001 (the copyright sign) is encoded in UTF-8 as </p>
<dl>
<dd> <p> 11000010 10101001 = 0xc2 0xa9 </p>
 </dd></dl>
<p>and character 0x2260 = 0010 0010 0110 0000 (the &quot;not equal&quot; symbol) is encoded as: </p>
<dl>
<dd> <p> 11100010 10001001 10100000 = 0xe2 0x89 0xa0 </p>
 </dd></dl>
<h3>Application notes</h3>
<p> Users have to select a UTF-8 locale, for example with </p>
<dl>
<dd> <p> export LANG=en_GB.UTF-8 </p>
 </dd></dl>
<p>in order to activate the UTF-8 support in applications. </p>
<p>Application software that has to be aware of the used character encoding should always set the locale with for example </p>
<dl>
<dd> <p> setlocale(LC_CTYPE, &quot;&quot;) </p>
 </dd></dl>
<p>and programmers can then test the expression </p>
<dl>
<dd> <p> strcmp(nl_langinfo(CODESET), &quot;UTF-8&quot;) == 0 </p>
 </dd></dl>
<p>to determine whether a UTF-8 locale has been selected and whether therefore all plaintext standard input and output, terminal communication, plaintext file content, filenames and environment variables are encoded in UTF-8. </p>
<p>Programmers accustomed to single-byte encodings such as US-ASCII or ISO 8859 have to be aware that two assumptions made so far are no longer valid in UTF-8 locales. Firstly, a single byte does not necessarily correspond any more to a single character. Secondly, since modern terminal emulators in UTF-8 mode also support Chinese, Japanese, and Korean double-width characters as well as nonspacing combining characters, outputting a single character does not necessarily advance the cursor by one position as it did in ASCII. Library functions such as <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3) and <code><a href="/docs/linux/man/3-wcswidth/">wcswidth</a></code>(3) should be used today to count characters and cursor positions. </p>
<p>The official ESC sequence to switch from an ISO 2022 encoding scheme (as used for instance by VT100 terminals) to UTF-8 is ESC % G (&quot;\x1b%G&quot;). The corresponding return sequence from UTF-8 to ISO 2022 is ESC % @ (&quot;\x1b%@&quot;). Other ISO 2022 sequences (such as for switching the G0 and G1 sets) are not applicable in UTF-8 mode.  </p>
<h3>Security</h3>
<p> The Unicode and UCS standards require that producers of UTF-8 shall use the shortest form possible, for example, producing a two-byte sequence with first byte 0xc0 is nonconforming. Unicode 3.1 has added the requirement that conforming programs must not accept non-shortest forms in their input. This is for security reasons: if user input is checked for possible security violations, a program might check only for the ASCII version of &quot;/../&quot; or &quot;;&quot; or NUL and overlook that there are many non-ASCII ways to represent these things in a non-shortest UTF-8 encoding.  </p>
<h3>Standards</h3>
<p> ISO/IEC 10646-1:2000, Unicode 3.1, RFC 3629, Plan 9.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
