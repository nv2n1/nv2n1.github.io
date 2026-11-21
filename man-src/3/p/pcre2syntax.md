---
title: "pcre2syntax(3)"
name: "pcre2syntax"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2syntax/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---
<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API) </p>
<h2>PCRE2 REGULAR EXPRESSION SYNTAX SUMMARY</h2>
<p>The full syntax and semantics of the regular expressions that are supported by PCRE2 are described in the <code>pcre2pattern</code> documentation. This document contains a quick-reference summary of the syntax.  </p>
<h2>QUOTING</h2>
<p> <br />
&nbsp;<wbr>&nbsp;\x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;where x is non-alphanumeric is a literal x <br />
&nbsp;<wbr>&nbsp;\Q...\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;treat enclosed characters as literal  </p>
<h2>ESCAPED CHARACTERS</h2>
<p>This table applies to ASCII and Unicode environments. An unrecognized escape sequence causes an error. </p>
<p> <br />
&nbsp;<wbr>&nbsp;\a&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alarm, that is, the BEL character&nbsp;(hex 07) <br />
&nbsp;<wbr>&nbsp;\cx&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;control-x&quot;, where x is any ASCII printing character <br />
&nbsp;<wbr>&nbsp;\e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;escape&nbsp;(hex 1B) <br />
&nbsp;<wbr>&nbsp;\f&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;form feed&nbsp;(hex 0C) <br />
&nbsp;<wbr>&nbsp;\n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;newline&nbsp;(hex 0A) <br />
&nbsp;<wbr>&nbsp;\r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return&nbsp;(hex 0D) <br />
&nbsp;<wbr>&nbsp;\t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tab&nbsp;(hex 09) <br />
&nbsp;<wbr>&nbsp;\0dd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with octal code 0dd <br />
&nbsp;<wbr>&nbsp;\ddd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with octal code ddd, or backreference <br />
&nbsp;<wbr>&nbsp;\o{ddd..}&nbsp;<wbr>&nbsp;character with octal code ddd.. <br />
&nbsp;<wbr>&nbsp;\N{U+hh..}&nbsp;character with Unicode code point hh..&nbsp;(Unicode mode only) <br />
&nbsp;<wbr>&nbsp;\xhh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with hex code hh <br />
&nbsp;<wbr>&nbsp;\x{hh..}&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with hex code hh.. </p>
<p>If PCRE2_ALT_BSUX or PCRE2_EXTRA_ALT_BSUX is set (&quot;ALT_BSUX mode&quot;), the following are also recognized: </p>
<p> <br />
&nbsp;<wbr>&nbsp;\U&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the character&nbsp;&quot;U&quot; <br />
&nbsp;<wbr>&nbsp;\uhhhh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with hex code hhhh <br />
&nbsp;<wbr>&nbsp;\u{hh..}&nbsp;<wbr>&nbsp;<wbr>&nbsp;character with hex code hh.. but only for EXTRA_ALT_BSUX </p>
<p>When \x is not followed by {, from zero to two hexadecimal digits are read, but in ALT_BSUX mode \x must be followed by two hexadecimal digits to be recognized as a hexadecimal escape; otherwise it matches a literal &quot;x&quot;. Likewise, if \u (in ALT_BSUX mode) is not followed by four hexadecimal digits or (in EXTRA_ALT_BSUX mode) a sequence of hex digits in curly brackets, it matches a literal &quot;u&quot;. </p>
<p>Note that \0dd is always an octal code. The treatment of backslash followed by a non-zero digit is complicated; for details see the section &quot;Non-printing characters&quot; in the <code>pcre2pattern</code> documentation, where details of escape processing in EBCDIC environments are also given. \N{U+hh..} is synonymous with \x{hh..} in PCRE2 but is not supported in EBCDIC environments. Note that \N not followed by an opening curly bracket has a different meaning (see below).  </p>
<h2>CHARACTER TYPES</h2>
<p> <br />
&nbsp;<wbr>&nbsp;.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;any character except newline; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in dotall mode, any character whatsoever <br />
&nbsp;<wbr>&nbsp;\C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;one code unit, even in UTF mode&nbsp;(best avoided) <br />
&nbsp;<wbr>&nbsp;\d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a decimal digit <br />
&nbsp;<wbr>&nbsp;\D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character that is not a decimal digit <br />
&nbsp;<wbr>&nbsp;\h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a horizontal white space character <br />
&nbsp;<wbr>&nbsp;\H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character that is not a horizontal white space character <br />
&nbsp;<wbr>&nbsp;\N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character that is not a newline <br />
&nbsp;<wbr>&nbsp;\p{<i>xx</i>}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character with the&nbsp;<i>xx</i>&nbsp;property <br />
&nbsp;<wbr>&nbsp;\P{<i>xx</i>}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character without the&nbsp;<i>xx</i>&nbsp;property <br />
&nbsp;<wbr>&nbsp;\R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a newline sequence <br />
&nbsp;<wbr>&nbsp;\s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a white space character <br />
&nbsp;<wbr>&nbsp;\S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character that is not a white space character <br />
&nbsp;<wbr>&nbsp;\v&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a vertical white space character <br />
&nbsp;<wbr>&nbsp;\V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a character that is not a vertical white space character <br />
&nbsp;<wbr>&nbsp;\w&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;&quot;word&quot;&nbsp;character <br />
&nbsp;<wbr>&nbsp;\W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;&quot;non-word&quot;&nbsp;character <br />
&nbsp;<wbr>&nbsp;\X&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a Unicode extended grapheme cluster </p>
<p>\C is dangerous because it may leave the current matching point in the middle of a UTF-8 or UTF-16 character. The application can lock out the use of \C by setting the PCRE2_NEVER_BACKSLASH_C option. It is also possible to build PCRE2 with the use of \C permanently disabled. </p>
<p>By default, \d, \s, and \w match only ASCII characters, even in UTF-8 mode or in the 16-bit and 32-bit libraries. However, if locale-specific matching is happening, \s and \w may also match characters with code points in the range 128-255. If the PCRE2_UCP option is set, the behaviour of these escape sequences is changed to use Unicode properties and they match many more characters.  </p>
<h2>GENERAL CATEGORY PROPERTIES FOR \p and \P</h2>
<p> <br />
&nbsp;<wbr>&nbsp;C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Other <br />
&nbsp;<wbr>&nbsp;Cc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Control <br />
&nbsp;<wbr>&nbsp;Cf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Format <br />
&nbsp;<wbr>&nbsp;Cn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Unassigned <br />
&nbsp;<wbr>&nbsp;Co&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Private use <br />
&nbsp;<wbr>&nbsp;Cs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Surrogate </p>
<p> <br />
&nbsp;<wbr>&nbsp;L&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Letter <br />
&nbsp;<wbr>&nbsp;Ll&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Lower case letter <br />
&nbsp;<wbr>&nbsp;Lm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Modifier letter <br />
&nbsp;<wbr>&nbsp;Lo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Other letter <br />
&nbsp;<wbr>&nbsp;Lt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Title case letter <br />
&nbsp;<wbr>&nbsp;Lu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Upper case letter <br />
&nbsp;<wbr>&nbsp;L&amp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ll, Lu, or Lt </p>
<p> <br />
&nbsp;<wbr>&nbsp;M&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mark <br />
&nbsp;<wbr>&nbsp;Mc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Spacing mark <br />
&nbsp;<wbr>&nbsp;Me&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Enclosing mark <br />
&nbsp;<wbr>&nbsp;Mn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Non-spacing mark </p>
<p> <br />
&nbsp;<wbr>&nbsp;N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Number <br />
&nbsp;<wbr>&nbsp;Nd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Decimal number <br />
&nbsp;<wbr>&nbsp;Nl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Letter number <br />
&nbsp;<wbr>&nbsp;No&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Other number </p>
<p> <br />
&nbsp;<wbr>&nbsp;P&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Punctuation <br />
&nbsp;<wbr>&nbsp;Pc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Connector punctuation <br />
&nbsp;<wbr>&nbsp;Pd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Dash punctuation <br />
&nbsp;<wbr>&nbsp;Pe&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Close punctuation <br />
&nbsp;<wbr>&nbsp;Pf&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Final punctuation <br />
&nbsp;<wbr>&nbsp;Pi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Initial punctuation <br />
&nbsp;<wbr>&nbsp;Po&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Other punctuation <br />
&nbsp;<wbr>&nbsp;Ps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Open punctuation </p>
<p> <br />
&nbsp;<wbr>&nbsp;S&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Symbol <br />
&nbsp;<wbr>&nbsp;Sc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Currency symbol <br />
&nbsp;<wbr>&nbsp;Sk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Modifier symbol <br />
&nbsp;<wbr>&nbsp;Sm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Mathematical symbol <br />
&nbsp;<wbr>&nbsp;So&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Other symbol </p>
<p> <br />
&nbsp;<wbr>&nbsp;Z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Separator <br />
&nbsp;<wbr>&nbsp;Zl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Line separator <br />
&nbsp;<wbr>&nbsp;Zp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Paragraph separator <br />
&nbsp;<wbr>&nbsp;Zs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Space separator  </p>
<h2>PCRE2 SPECIAL CATEGORY PROPERTIES FOR \p and \P</h2>
<p> <br />
&nbsp;<wbr>&nbsp;Xan&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alphanumeric: union of properties L and N <br />
&nbsp;<wbr>&nbsp;Xps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX space: property Z or tab, NL, VT, FF, CR <br />
&nbsp;<wbr>&nbsp;Xsp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Perl space: property Z or tab, NL, VT, FF, CR <br />
&nbsp;<wbr>&nbsp;Xuc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Univerally-named character: one that can be <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represented by a Universal Character Name <br />
&nbsp;<wbr>&nbsp;Xwd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Perl word: property Xan or underscore </p>
<p>Perl and POSIX space are now the same. Perl added VT to its space character set at release 5.18.  </p>
<h2>SCRIPT NAMES FOR \p AND \P</h2>
<p>Adlam, Ahom, Anatolian_Hieroglyphs, Arabic, Armenian, Avestan, Balinese, Bamum, Bassa_Vah, Batak, Bengali, Bhaiksuki, Bopomofo, Brahmi, Braille, Buginese, Buhid, Canadian_Aboriginal, Carian, Caucasian_Albanian, Chakma, Cham, Cherokee, Common, Coptic, Cuneiform, Cypriot, Cyrillic, Deseret, Devanagari, Dogra, Duployan, Egyptian_Hieroglyphs, Elbasan, Elymaic, Ethiopic, Georgian, Glagolitic, Gothic, Grantha, Greek, Gujarati, Gunjala_Gondi, Gurmukhi, Han, Hangul, Hanifi_Rohingya, Hanunoo, Hatran, Hebrew, Hiragana, Imperial_Aramaic, Inherited, Inscriptional_Pahlavi, Inscriptional_Parthian, Javanese, Kaithi, Kannada, Katakana, Kayah_Li, Kharoshthi, Khmer, Khojki, Khudawadi, Lao, Latin, Lepcha, Limbu, Linear_A, Linear_B, Lisu, Lycian, Lydian, Mahajani, Makasar, Malayalam, Mandaic, Manichaean, Marchen, Masaram_Gondi, Medefaidrin, Meetei_Mayek, Mende_Kikakui, Meroitic_Cursive, Meroitic_Hieroglyphs, Miao, Modi, Mongolian, Mro, Multani, Myanmar, Nabataean, Nandinagari, New_Tai_Lue, Newa, Nko, Nushu, Nyakeng_Puachue_Hmong, Ogham, Ol_Chiki, Old_Hungarian, Old_Italic, Old_North_Arabian, Old_Permic, Old_Persian, Old_Sogdian, Old_South_Arabian, Old_Turkic, Oriya, Osage, Osmanya, Pahawh_Hmong, Palmyrene, Pau_Cin_Hau, Phags_Pa, Phoenician, Psalter_Pahlavi, Rejang, Runic, Samaritan, Saurashtra, Sharada, Shavian, Siddham, SignWriting, Sinhala, Sogdian, Sora_Sompeng, Soyombo, Sundanese, Syloti_Nagri, Syriac, Tagalog, Tagbanwa, Tai_Le, Tai_Tham, Tai_Viet, Takri, Tamil, Tangut, Telugu, Thaana, Thai, Tibetan, Tifinagh, Tirhuta, Ugaritic, Vai, Wancho, Warang_Citi, Yi, Zanabazar_Square.  </p>
<h2>CHARACTER CLASSES</h2>
<p> <br />
&nbsp;<wbr>&nbsp;[...]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;positive character class <br />
&nbsp;<wbr>&nbsp;[^...]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negative character class <br />
&nbsp;<wbr>&nbsp;[x-y]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;range&nbsp;(can be used for hex characters) <br />
&nbsp;<wbr>&nbsp;[[:xxx:]]&nbsp;<wbr>&nbsp;<wbr>&nbsp;positive POSIX named set <br />
&nbsp;<wbr>&nbsp;[[:^xxx:]]&nbsp;<wbr>&nbsp;negative POSIX named set </p>
<p> <br />
&nbsp;<wbr>&nbsp;alnum&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alphanumeric <br />
&nbsp;<wbr>&nbsp;alpha&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alphabetic <br />
&nbsp;<wbr>&nbsp;ascii&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0-127 <br />
&nbsp;<wbr>&nbsp;blank&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;space or tab <br />
&nbsp;<wbr>&nbsp;cntrl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;control character <br />
&nbsp;<wbr>&nbsp;digit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;decimal digit <br />
&nbsp;<wbr>&nbsp;graph&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printing, excluding space <br />
&nbsp;<wbr>&nbsp;lower&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lower case letter <br />
&nbsp;<wbr>&nbsp;print&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printing, including space <br />
&nbsp;<wbr>&nbsp;punct&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printing, excluding alphanumeric <br />
&nbsp;<wbr>&nbsp;space&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;white space <br />
&nbsp;<wbr>&nbsp;upper&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;upper case letter <br />
&nbsp;<wbr>&nbsp;word&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;same as&nbsp;\w <br />
&nbsp;<wbr>&nbsp;xdigit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;hexadecimal digit </p>
<p>In PCRE2, POSIX character set names recognize only ASCII characters by default, but some of them use Unicode properties if PCRE2_UCP is set. You can use \Q...\E inside a character class.  </p>
<h2>QUANTIFIERS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or 1, greedy <br />
&nbsp;<wbr>&nbsp;?+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or 1, possessive <br />
&nbsp;<wbr>&nbsp;??&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or 1, lazy <br />
&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or more, greedy <br />
&nbsp;<wbr>&nbsp;*+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or more, possessive <br />
&nbsp;<wbr>&nbsp;*?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or more, lazy <br />
&nbsp;<wbr>&nbsp;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 or more, greedy <br />
&nbsp;<wbr>&nbsp;++&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 or more, possessive <br />
&nbsp;<wbr>&nbsp;+?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 or more, lazy <br />
&nbsp;<wbr>&nbsp;{n}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exactly n <br />
&nbsp;<wbr>&nbsp;{n,m}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;at least n, no more than m, greedy <br />
&nbsp;<wbr>&nbsp;{n,m}+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;at least n, no more than m, possessive <br />
&nbsp;<wbr>&nbsp;{n,m}?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;at least n, no more than m, lazy <br />
&nbsp;<wbr>&nbsp;{n,}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n or more, greedy <br />
&nbsp;<wbr>&nbsp;{n,}+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n or more, possessive <br />
&nbsp;<wbr>&nbsp;{n,}?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n or more, lazy  </p>
<h2>ANCHORS AND SIMPLE ASSERTIONS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;\b&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;word boundary <br />
&nbsp;<wbr>&nbsp;\B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not a word boundary <br />
&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start of subject <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also after an internal newline in multiline mode <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(after any newline if PCRE2_ALT_CIRCUMFLEX is set) <br />
&nbsp;<wbr>&nbsp;\A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start of subject <br />
&nbsp;<wbr>&nbsp;$&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end of subject <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also before newline at end of subject <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also before internal newline in multiline mode <br />
&nbsp;<wbr>&nbsp;\Z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end of subject <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also before newline at end of subject <br />
&nbsp;<wbr>&nbsp;\z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end of subject <br />
&nbsp;<wbr>&nbsp;\G&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first matching position in subject  </p>
<h2>REPORTED MATCH POINT SETTING</h2>
<p> <br />
&nbsp;<wbr>&nbsp;\K&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set reported start of match </p>
<p>\K is honoured in positive assertions, but ignored in negative ones.  </p>
<h2>ALTERNATION</h2>
<p> <br />
&nbsp;<wbr>&nbsp;expr|expr|expr...  </p>
<h2>CAPTURING</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;capture group <br />
&nbsp;<wbr>&nbsp;(?&lt;name&gt;...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;named capture group&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;(?&#8216;name&#8217;...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;named capture group&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;(?P&lt;name&gt;...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;named capture group&nbsp;(Python) <br />
&nbsp;<wbr>&nbsp;(?:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-capture group <br />
&nbsp;<wbr>&nbsp;(?|...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;non-capture group;&nbsp;reset group numbers for <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;capture groups in each alternative </p>
<p>In non-UTF modes, names may contain underscores and ASCII letters and digits; in UTF modes, any Unicode letters and Unicode decimal digits are permitted. In both cases, a name must not start with a digit.  </p>
<h2>ATOMIC GROUPS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?&gt;...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomic non-capture group <br />
&nbsp;<wbr>&nbsp;(*atomic:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomic non-capture group  </p>
<h2>COMMENT</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?#....)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comment&nbsp;(not nestable)  </p>
<h2>OPTION SETTING</h2>
<p> Changes of these options within a group are automatically cancelled at the end of the group. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(?i)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;caseless <br />
&nbsp;<wbr>&nbsp;(?J)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allow duplicate names <br />
&nbsp;<wbr>&nbsp;(?m)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;multiline <br />
&nbsp;<wbr>&nbsp;(?n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no auto capture <br />
&nbsp;<wbr>&nbsp;(?s)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;single line&nbsp;(dotall) <br />
&nbsp;<wbr>&nbsp;(?U)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default ungreedy&nbsp;(lazy) <br />
&nbsp;<wbr>&nbsp;(?x)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extended: ignore white space except in classes <br />
&nbsp;<wbr>&nbsp;(?xx)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;as&nbsp;(?x)&nbsp;but also ignore space and tab in classes <br />
&nbsp;<wbr>&nbsp;(?-...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unset option(s) <br />
&nbsp;<wbr>&nbsp;(?^)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unset imnsx options </p>
<p>Unsetting x or xx unsets both. Several options may be set at once, and a mixture of setting and unsetting such as (?i-x) is allowed, but there may be only one hyphen. Setting (but no unsetting) is allowed after (?^ for example (?^in). An option setting may appear at the start of a non-capture group, for example (?i:...). </p>
<p>The following are recognized only at the very start of a pattern or after one of the newline or \R options with similar syntax. More than one of them may appear. For the first three, d is a decimal number. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*LIMIT_DEPTH=d)&nbsp;set the backtracking limit to d <br />
&nbsp;<wbr>&nbsp;(*LIMIT_HEAP=d)&nbsp;<wbr>&nbsp;set the heap size limit to d&nbsp;*&nbsp;1024 bytes <br />
&nbsp;<wbr>&nbsp;(*LIMIT_MATCH=d)&nbsp;set the match limit to d <br />
&nbsp;<wbr>&nbsp;(*NOTEMPTY)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set PCRE2_NOTEMPTY when matching <br />
&nbsp;<wbr>&nbsp;(*NOTEMPTY_ATSTART)&nbsp;set PCRE2_NOTEMPTY_ATSTART when matching <br />
&nbsp;<wbr>&nbsp;(*NO_AUTO_POSSESS)&nbsp;no auto-possessification&nbsp;(PCRE2_NO_AUTO_POSSESS) <br />
&nbsp;<wbr>&nbsp;(*NO_DOTSTAR_ANCHOR)&nbsp;no .*&nbsp;anchoring&nbsp;(PCRE2_NO_DOTSTAR_ANCHOR) <br />
&nbsp;<wbr>&nbsp;(*NO_JIT)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disable JIT optimization <br />
&nbsp;<wbr>&nbsp;(*NO_START_OPT)&nbsp;no start-match optimization&nbsp;(PCRE2_NO_START_OPTIMIZE) <br />
&nbsp;<wbr>&nbsp;(*UTF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set appropriate UTF mode for the library in use <br />
&nbsp;<wbr>&nbsp;(*UCP)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set PCRE2_UCP&nbsp;(use Unicode properties for&nbsp;\d etc) </p>
<p>Note that LIMIT_DEPTH, LIMIT_HEAP, and LIMIT_MATCH can only reduce the value of the limits set by the caller of <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code>, not increase them. LIMIT_RECURSION is an obsolete synonym for LIMIT_DEPTH. The application can lock out the use of (*UTF) and (*UCP) by setting the PCRE2_NEVER_UTF or PCRE2_NEVER_UCP options, respectively, at compile time.  </p>
<h2>NEWLINE CONVENTION</h2>
<p>These are recognized only at the very start of the pattern or after option settings with a similar syntax. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*CR)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return only <br />
&nbsp;<wbr>&nbsp;(*LF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linefeed only <br />
&nbsp;<wbr>&nbsp;(*CRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return followed by linefeed <br />
&nbsp;<wbr>&nbsp;(*ANYCRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;all three of the above <br />
&nbsp;<wbr>&nbsp;(*ANY)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;any Unicode newline sequence <br />
&nbsp;<wbr>&nbsp;(*NUL)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the NUL character&nbsp;(binary zero)  </p>
<h2>WHAT \R MATCHES</h2>
<p>These are recognized only at the very start of the pattern or after option setting with a similar syntax. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*BSR_ANYCRLF)&nbsp;<wbr>&nbsp;CR, LF, or CRLF <br />
&nbsp;<wbr>&nbsp;(*BSR_UNICODE)&nbsp;<wbr>&nbsp;any Unicode newline sequence  </p>
<h2>LOOKAHEAD AND LOOKBEHIND ASSERTIONS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?=...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;) <br />
&nbsp;<wbr>&nbsp;(*pla:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;positive lookahead <br />
&nbsp;<wbr>&nbsp;(*positive_lookahead:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(?!...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;) <br />
&nbsp;<wbr>&nbsp;(*nla:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;negative lookahead <br />
&nbsp;<wbr>&nbsp;(*negative_lookahead:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(?&lt;=...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;) <br />
&nbsp;<wbr>&nbsp;(*plb:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;positive lookbehind <br />
&nbsp;<wbr>&nbsp;(*positive_lookbehind:...)&nbsp;<wbr>&nbsp;) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(?&lt;!...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;) <br />
&nbsp;<wbr>&nbsp;(*nlb:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;negative lookbehind <br />
&nbsp;<wbr>&nbsp;(*negative_lookbehind:...)&nbsp;<wbr>&nbsp;) </p>
<p>Each top-level branch of a lookbehind must be of a fixed length.  </p>
<h2>NON-ATOMIC LOOKAROUND ASSERTIONS</h2>
<p>These assertions are specific to PCRE2 and are not Perl-compatible. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*napla:...) <br />
&nbsp;<wbr>&nbsp;(*non_atomic_positive_lookahead:...) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*naplb:...) <br />
&nbsp;<wbr>&nbsp;(*non_atomic_positive_lookbehind:...)  </p>
<h2>SCRIPT RUNS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(*script_run:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;script run, can be backtracked into <br />
&nbsp;<wbr>&nbsp;(*sr:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*atomic_script_run:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)&nbsp;atomic script run <br />
&nbsp;<wbr>&nbsp;(*asr:...)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;)  </p>
<h2>BACKREFERENCES</h2>
<p> <br />
&nbsp;<wbr>&nbsp;\n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by number&nbsp;(can be ambiguous) <br />
&nbsp;<wbr>&nbsp;\gn&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by number <br />
&nbsp;<wbr>&nbsp;\g{n}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by number <br />
&nbsp;<wbr>&nbsp;\g+n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference by number&nbsp;(PCRE2 extension) <br />
&nbsp;<wbr>&nbsp;\g-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference by number <br />
&nbsp;<wbr>&nbsp;\g{+n}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference by number&nbsp;(PCRE2 extension) <br />
&nbsp;<wbr>&nbsp;\g{-n}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference by number <br />
&nbsp;<wbr>&nbsp;\k&lt;name&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by name&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;\k&#8217;name&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by name&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;\g{name}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by name&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;\k{name}&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by name&nbsp;(.NET) <br />
&nbsp;<wbr>&nbsp;(?P=name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reference by name&nbsp;(Python)  </p>
<h2>SUBROUTINE REFERENCES (POSSIBLY RECURSIVE)</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?R)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;recurse whole pattern <br />
&nbsp;<wbr>&nbsp;(?n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by absolute number <br />
&nbsp;<wbr>&nbsp;(?+n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number <br />
&nbsp;<wbr>&nbsp;(?-n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number <br />
&nbsp;<wbr>&nbsp;(?&amp;name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by name&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;(?P&gt;name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by name&nbsp;(Python) <br />
&nbsp;<wbr>&nbsp;\g&lt;name&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by name&nbsp;(Oniguruma) <br />
&nbsp;<wbr>&nbsp;\g&#8217;name&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by name&nbsp;(Oniguruma) <br />
&nbsp;<wbr>&nbsp;\g&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by absolute number&nbsp;(Oniguruma) <br />
&nbsp;<wbr>&nbsp;\g&#8217;n&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by absolute number&nbsp;(Oniguruma) <br />
&nbsp;<wbr>&nbsp;\g&lt;+n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number&nbsp;(PCRE2 extension) <br />
&nbsp;<wbr>&nbsp;\g&#8217;+n&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number&nbsp;(PCRE2 extension) <br />
&nbsp;<wbr>&nbsp;\g&lt;-n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number&nbsp;(PCRE2 extension) <br />
&nbsp;<wbr>&nbsp;\g&#8217;-n&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;call subroutine by relative number&nbsp;(PCRE2 extension)  </p>
<h2>CONDITIONAL PATTERNS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?(condition)yes-pattern) <br />
&nbsp;<wbr>&nbsp;(?(condition)yes-pattern|no-pattern) </p>
<p> <br />
&nbsp;<wbr>&nbsp;(?(n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;absolute reference condition <br />
&nbsp;<wbr>&nbsp;(?(+n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference condition <br />
&nbsp;<wbr>&nbsp;(?(-n)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;relative reference condition <br />
&nbsp;<wbr>&nbsp;(?(&lt;name&gt;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;named reference condition&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;(?(&#8216;name&#8217;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;named reference condition&nbsp;(Perl) <br />
&nbsp;<wbr>&nbsp;(?(name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;named reference condition&nbsp;(PCRE2, deprecated) <br />
&nbsp;<wbr>&nbsp;(?(R)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overall recursion condition <br />
&nbsp;<wbr>&nbsp;(?(Rn)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specific numbered group recursion condition <br />
&nbsp;<wbr>&nbsp;(?(R&amp;name)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specific named group recursion condition <br />
&nbsp;<wbr>&nbsp;(?(DEFINE)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;define groups for reference <br />
&nbsp;<wbr>&nbsp;(?(VERSION[&gt;]=n.m)&nbsp;<wbr>&nbsp;test PCRE2 version <br />
&nbsp;<wbr>&nbsp;(?(assert)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assertion condition </p>
<p>Note the ambiguity of (?(R) and (?(Rn) which might be named reference conditions or recursion tests. Such a condition is interpreted as a reference condition if the relevant named group exists.  </p>
<h2>BACKTRACKING CONTROL</h2>
<p>All backtracking control verbs may be in the form (*VERB:NAME). For (*MARK) the name is mandatory, for the others it is optional. (*SKIP) changes its behaviour if :NAME is present. The others just set a name for passing back to the caller, but this is not a name that (*SKIP) can see. The following act immediately they are reached: </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*ACCEPT)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;force successful match <br />
&nbsp;<wbr>&nbsp;(*FAIL)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;force backtrack;&nbsp;synonym&nbsp;(*F) <br />
&nbsp;<wbr>&nbsp;(*MARK:NAME)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set name to be passed back;&nbsp;synonym&nbsp;(*:NAME) </p>
<p>The following act only when a subsequent match failure causes a backtrack to reach them. They all force a match failure, but they differ in what happens afterwards. Those that advance the start-of-match point do so only if the pattern is not anchored. </p>
<p> <br />
&nbsp;<wbr>&nbsp;(*COMMIT)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;overall failure, no advance of starting point <br />
&nbsp;<wbr>&nbsp;(*PRUNE)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advance to next starting character <br />
&nbsp;<wbr>&nbsp;(*SKIP)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advance to current matching position <br />
&nbsp;<wbr>&nbsp;(*SKIP:NAME)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advance to position corresponding to an earlier <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*MARK:NAME);&nbsp;if not found, the&nbsp;(*SKIP)&nbsp;is ignored <br />
&nbsp;<wbr>&nbsp;(*THEN)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;local failure, backtrack to next alternation </p>
<p>The effect of one of these verbs in a group called as a subroutine is confined to the subroutine call.  </p>
<h2>CALLOUTS</h2>
<p> <br />
&nbsp;<wbr>&nbsp;(?C)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;callout&nbsp;(assumed number 0) <br />
&nbsp;<wbr>&nbsp;(?Cn)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;callout with numerical data n <br />
&nbsp;<wbr>&nbsp;(?C&quot;text&quot;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;callout with string data </p>
<p>The allowed string delimiters are ` &#8216; &quot; ^ % # $ (which are the same for the start and the end), and the starting delimiter { matched with the ending delimiter }. To encode the ending delimiter within the string, double it.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pcre2pattern/">pcre2pattern</a></code>(3), <code><a href="/docs/linux/man/3-pcre2api/">pcre2api</a></code>(3), <code><a href="/docs/linux/man/3-pcre2callout/">pcre2callout</a></code>(3), <code><a href="/docs/linux/man/3-pcre2matching/">pcre2matching</a></code>(3), <code><a href="/docs/linux/man/3-pcre2/">pcre2</a></code>(3).  </p>
<h2>AUTHOR</h2>
<pre><code>Philip Hazel
University Computing Service
Cambridge, England.
</code></pre>
<h2>REVISION</h2>
<pre><code>Last updated: 29 July 2019
Copyright (c) 1997-2019 University of Cambridge.
</code></pre>
