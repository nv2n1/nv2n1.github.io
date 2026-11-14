---
title: "gpinyin(1)"
name: "gpinyin"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpinyin/"
description: "gpinyin – use Hanyu Pinyin Chinese in roff"
---

<h2 class="name">NAME</h2>
<p> gpinyin &#8211; use Hanyu Pinyin Chinese in roff </p>
<h2>SYNOPSIS</h2>
<p> [<i>input-file</i> &#8230;] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gpinyin</code> is a preprocessor for <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) that facilitates use of the Hanyu Pinyin <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) files. Pinyin is a method for writing the Chinese language with the Latin alphabet. The Chinese language consists of more than four hundred syllables, each with one of five different tones. In Pinyin, a syllable is written in the Latin alphabet and a numeric tone indicator can be appended to each syllable. </p>
<p> Each <i>input-file</i> is a file name or the hyphen-minus character &#8220;-&#8221; to indicate that standard input should be read. As usual, the argument &#8220;&#8211;&#8221; can be used in order to force interpretation of all remaining arguments as file names, even if an <i>input-file</i> argument begins with the hyphen-minus character.</p>
<h3>Pinyin Sections</h3>
<p> Pinyin sections in <i>groff</i> files are enclosed by two <code>.pinyin</code> requests with different arguments. The starting request is</p>
<dl>
<dt>
<dd> .pinyin start</dl>
<p> or</p>
<dl>
<dt>
<dd> .pinyin begin</dl>
<p> and the ending request is</p>
<dl>
<dt>
<dd> .pinyin stop</dl>
<p> or</p>
<dl>
<dt>
<dd> .pinyin end</dl>
<p> .</p>
<h3>Syllables</h3>
<p> The spoken Chinese language is based on about 411 <i>syllables</i>; see </p>
<p> In Pinyin, each syllable consists of one to six letters from the Latin alphabet; these letters comprise the fifty-two upper- and lowercase letters from the ASCII character set, plus the letter &#8220;U&#8221; with dieresis (umlaut) in both cases&#8212;in other words, the members of the set &#8220;[a-zA-Z&uuml;&Uuml;]&#8221;. </p>
<p> In <i>groff</i> input, all ASCII letters are written as themselves. The &#8220;u with dieresis&#8221; can be written as &#8220;\[:u]&#8221; in lowercase or &#8220;\[:U]&#8221; in uppercase. Within <code>.pinyin</code> sections, <i>gpinyin</i> supports the form &#8220;ue&#8221; for lowercase and the forms &#8220;Ue&#8221; and &#8220;UE&#8221; for uppercase.</p>
<h3>Tones</h3>
<p> Each syllable has exactly one of five <i>tones</i>. The fifth tone is not explicitly written at all, but each of the first through fourth tones is indicated with a diacritic above a specific vowel within the syllable. </p>
<p> In a <i>gpinyin</i> source file, these tones are written by adding a numeral in the range 0 to 5 after the syllable. The tone numbers 1 to 4 are transformed into accents above vowels in the output. The tone numbers 0 and 5 are synonymous. </p>
<p> The following table summarizes the tones. Some output devices will not be able to render every output example. </p>
<table>
<tr VALIGN=top>
<td>Tone</td>
<td>Description</td>
<td>Diacritic</td>
<td>Example Input</td>
<td>Example Output
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>first</td>
<td>flat</td>
<td>a-</td>
<td>ma1</td>
<td>m04
</td>
</tr>
<tr VALIGN=top>
<td>second</td>
<td>rising</td>
<td>&acute;</td>
<td>ma2</td>
<td>m01
</td>
</tr>
<tr VALIGN=top>
<td>third</td>
<td>falling-rising</td>
<td>ah</td>
<td>ma3</td>
<td>m0C
</td>
</tr>
<tr VALIGN=top>
<td>fourth</td>
<td>falling</td>
<td>`</td>
<td>ma4</td>
<td>m00
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>fifth</td>
<td VALIGN=center ROWSPAN=2>neutral</td>
<td VALIGN=center ROWSPAN=2>(none)</td>
<td>ma0</td>
<td VALIGN=center ROWSPAN=2>ma
</td>
</tr>
<tr VALIGN=top>
<td>ma5</td>
</tr>
</table>
<p> The neutral tone number can be omitted from a word-final syllable, but not otherwise.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> <code>&#8211;help</code> Print usage information and exit.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Print version information and exit.</dl>
<h2>AUTHORS</h2>
<p> <code>gpinyin</code> was written by Bernd Warken</p>
<h2>SEE ALSO</h2>
<p> Useful documents on the World Wide Web related to Pinyin include</p>
<dl>
<dt>
<dd>
 &#8220;Pinyin&#8221; (Wikipedia)<br />
 &#8220;Pinyin table&#8221; (Wikipedia)<br />
 <i>Pinyin to Unicode</i><br />
 <i>On-line Chinese Tools</i><br />
 <i>Pinyin.info: a guide to the writing of Mandarin Chinese in romanization</i><br />
 &#8220;Where do the tone marks go?&#8221; (Pinyin.info)<br />
 pinyin.txt from the CJK macro package for
</dl>
<p> and<br />
 pinyin.sty from the CJK macro package for </p>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1), and <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) explain how to view <i>roff</i> documents. </p>
<p> <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) and <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) are comprehensive references covering the language elements of GNU <i>roff</i> and the available glyph repertoire, respectively. </p>
<h2>Index</h2>
