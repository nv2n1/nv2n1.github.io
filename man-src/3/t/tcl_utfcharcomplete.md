---
title: "tcl_utfcharcomplete(3)"
name: "tcl_utfcharcomplete"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_utfcharcomplete/"
description: "Tcl_UniChar, Tcl_UniCharCaseMatch, Tcl_UniCharNcasecmp, Tcl_UniCharToUtf, Tcl_UtfToUniChar, Tcl_UniCharToUtfDString, Tcl_UtfToUniCharDString, Tcl_UniCharLen, Tcl_UniCharNcmp, Tcl_UtfCharComplete, T..."
---

<p>Tcl_UniChar, Tcl_UniCharCaseMatch, Tcl_UniCharNcasecmp, Tcl_UniCharToUtf, Tcl_UtfToUniChar, Tcl_UniCharToUtfDString, Tcl_UtfToUniCharDString, Tcl_UniCharLen, Tcl_UniCharNcmp, Tcl_UtfCharComplete, Tcl_NumUtfChars, Tcl_UtfFindFirst, Tcl_UtfFindLast, Tcl_UtfNext, Tcl_UtfPrev, Tcl_UniCharAtIndex, Tcl_UtfAtIndex, Tcl_UtfBackslash &#8211; routines for manipulating UTF-8 strings </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
typedef ... Tcl_UniChar;
int
<code>Tcl_UniCharToUtf</code>(<i>ch, buf</i>)
int
<code>Tcl_UtfToUniChar</code>(<i>src, chPtr</i>)
char *
<code>Tcl_UniCharToUtfDString</code>(<i>uniStr, uniLength, dsPtr</i>)
Tcl_UniChar *
<code>Tcl_UtfToUniCharDString</code>(<i>src, length, dsPtr</i>)
int
<code>Tcl_UniCharLen</code>(<i>uniStr</i>)
int
<code>Tcl_UniCharNcmp</code>(<i>ucs, uct, numChars</i>)
int
<code>Tcl_UniCharNcasecmp</code>(<i>ucs, uct, numChars</i>)
int
<code>Tcl_UniCharCaseMatch</code>(<i>uniStr, uniPattern, nocase</i>)
int
<code>Tcl_UtfNcmp</code>(<i>cs, ct, numChars</i>)
int
<code>Tcl_UtfNcasecmp</code>(<i>cs, ct, numChars</i>)
int
<code>Tcl_UtfCharComplete</code>(<i>src, length</i>)
int 
<code>Tcl_NumUtfChars</code>(<i>src, length</i>)
const char *
<code>Tcl_UtfFindFirst</code>(<i>src, ch</i>)
const char *
<code>Tcl_UtfFindLast</code>(<i>src, ch</i>)
const char *
<code>Tcl_UtfNext</code>(<i>src</i>)
const char *
<code>Tcl_UtfPrev</code>(<i>src, start</i>)
Tcl_UniChar
<code>Tcl_UniCharAtIndex</code>(<i>src, index</i>)
const char *
<code>Tcl_UtfAtIndex</code>(<i>src, index</i>)
int
<code>Tcl_UtfBackslash</code>(<i>src, readPtr, dst</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>char <i>*buf</i> (out) Buffer in which the UTF-8 representation of the Tcl_UniChar is stored. At most <code>TCL_UTF_MAX</code> bytes are stored in the buffer.</p>
<dd>int <i>ch</i> (in) The Tcl_UniChar to be converted or examined.</p>
<dd>Tcl_UniChar <i>*chPtr</i> (out) Filled with the Tcl_UniChar represented by the head of the UTF-8 string.</p>
<dd>const char <i>*src</i> (in) Pointer to a UTF-8 string.</p>
<dd>const char <i>*cs</i> (in) Pointer to a UTF-8 string.</p>
<dd>const char <i>*ct</i> (in) Pointer to a UTF-8 string.</p>
<dd>const Tcl_UniChar <i>*uniStr</i> (in) A null-terminated Unicode string.</p>
<dd>const Tcl_UniChar <i>*ucs</i> (in) A null-terminated Unicode string.</p>
<dd>const Tcl_UniChar <i>*uct</i> (in) A null-terminated Unicode string.</p>
<dd>const Tcl_UniChar <i>*uniPattern</i> (in) A null-terminated Unicode string.</p>
<dd>int <i>length</i> (in) The length of the UTF-8 string in bytes (not UTF-8 characters). If negative, all bytes up to the first null byte are used.</p>
<dd>int <i>uniLength</i> (in) The length of the Unicode string in characters. Must be greater than or equal to 0.</p>
<dd>Tcl_DString <i>*dsPtr</i> (in/out) A pointer to a previously initialized <code>Tcl_DString</code>.</p>
<dd>unsigned long <i>numChars</i> (in) The number of characters to compare.</p>
<dd>const char <i>*start</i> (in) Pointer to the beginning of a UTF-8 string.</p>
<dd>int <i>index</i> (in) The index of a character (not byte) in the UTF-8 string.</p>
<dd>int <i>*readPtr</i> (out) If non-NULL, filled with the number of bytes in the backslash sequence, including the backslash character.</p>
<dd>char <i>*dst</i> (out) Buffer in which the bytes represented by the backslash sequence are stored. At most <code>TCL_UTF_MAX</code> bytes are stored in the buffer.</p>
<dd>int <i>nocase</i> (in) Specifies whether the match should be done case-sensitive (0) or case-insensitive (1). </p>
</dl>
<h2>Description</h2>
<p>These routines convert between UTF-8 strings and Tcl_UniChars. A Tcl_UniChar is a Unicode character represented as an unsigned, fixed-size quantity. A UTF-8 character is a Unicode character represented as a varying-length sequence of up to <code>TCL_UTF_MAX</code> bytes. A multibyte UTF-8 sequence consists of a lead byte followed by some number of trail bytes. </p>
<p> <code>TCL_UTF_MAX</code> is the maximum number of bytes that it takes to represent one Unicode character in the UTF-8 representation. </p>
<p> <code>Tcl_UniCharToUtf</code> stores the Tcl_UniChar <i>ch</i> as a UTF-8 string in starting at <i>buf</i>. The return value is the number of bytes stored in <i>buf</i>. </p>
<p> <code>Tcl_UtfToUniChar</code> reads one UTF-8 character starting at <i>src</i> and stores it as a Tcl_UniChar in <i>*chPtr</i>. The return value is the number of bytes read from <i>src</i>. The caller must ensure that the source buffer is long enough such that this routine does not run off the end and dereference non-existent or random memory; if the source buffer is known to be null-terminated, this will not happen. If the input is not in proper UTF-8 format, <code>Tcl_UtfToUniChar</code> will store the first byte of <i>src</i> in <i>*chPtr</i> as a Tcl_UniChar between 0x0000 and 0x00ff and return 1. </p>
<p> <code>Tcl_UniCharToUtfDString</code> converts the given Unicode string to UTF-8, storing the result in a previously initialized <code>Tcl_DString</code>. You must specify <i>uniLength</i>, the length of the given Unicode string. The return value is a pointer to the UTF-8 representation of the Unicode string. Storage for the return value is appended to the end of the <code>Tcl_DString</code>. </p>
<p> <code>Tcl_UtfToUniCharDString</code> converts the given UTF-8 string to Unicode, storing the result in the previously initialized <code>Tcl_DString</code>. In the argument <i>length</i>, you may either specify the length of the given UTF-8 string in bytes or &#8220;-1&#8221;, in which case <code>Tcl_UtfToUniCharDString</code> uses <code>strlen</code> to calculate the length. The return value is a pointer to the Unicode representation of the UTF-8 string. Storage for the return value is appended to the end of the <code>Tcl_DString</code>. The Unicode string is terminated with a Unicode null character. </p>
<p> <code>Tcl_UniCharLen</code> corresponds to <code>strlen</code> for Unicode characters. It accepts a null-terminated Unicode string and returns the number of Unicode characters (not bytes) in that string. </p>
<p> <code>Tcl_UniCharNcmp</code> and <code>Tcl_UniCharNcasecmp</code> correspond to <code>strncmp</code> and <code>strncasecmp</code>, respectively, for Unicode characters. They accept two null-terminated Unicode strings and the number of characters to compare. Both strings are assumed to be at least <i>numChars</i> characters long. <code>Tcl_UniCharNcmp</code> compares the two strings character-by-character according to the Unicode character ordering. It returns an integer greater than, equal to, or less than 0 if the first string is greater than, equal to, or less than the second string respectively. <code>Tcl_UniCharNcasecmp</code> is the Unicode case insensitive version. </p>
<p> <code>Tcl_UniCharCaseMatch</code> is the Unicode equivalent to <code>Tcl_StringCaseMatch</code>. It accepts a null-terminated Unicode string, a Unicode pattern, and a boolean value specifying whether the match should be case sensitive and returns whether the string matches the pattern. </p>
<p> <code>Tcl_UtfNcmp</code> corresponds to <code>strncmp</code> for UTF-8 strings. It accepts two null-terminated UTF-8 strings and the number of characters to compare. (Both strings are assumed to be at least <i>numChars</i> characters long.) <code>Tcl_UtfNcmp</code> compares the two strings character-by-character according to the Unicode character ordering. It returns an integer greater than, equal to, or less than 0 if the first string is greater than, equal to, or less than the second string respectively. </p>
<p> <code>Tcl_UtfNcasecmp</code> corresponds to <code>strncasecmp</code> for UTF-8 strings. It is similar to <code>Tcl_UtfNcmp</code> except comparisons ignore differences in case when comparing upper, lower or title case characters. </p>
<p> <code>Tcl_UtfCharComplete</code> returns 1 if the source UTF-8 string <i>src</i> of <i>length</i> bytes is long enough to be decoded by <code>Tcl_UtfToUniChar</code>, or 0 otherwise. This function does not guarantee that the UTF-8 string is properly formed. This routine is used by procedures that are operating on a byte at a time and need to know if a full Tcl_UniChar has been seen. </p>
<p> <code>Tcl_NumUtfChars</code> corresponds to <code>strlen</code> for UTF-8 strings. It returns the number of Tcl_UniChars that are represented by the UTF-8 string <i>src</i>. The length of the source string is <i>length</i> bytes. If the length is negative, all bytes up to the first null byte are used. </p>
<p> <code>Tcl_UtfFindFirst</code> corresponds to <code>strchr</code> for UTF-8 strings. It returns a pointer to the first occurrence of the Tcl_UniChar <i>ch</i> in the null-terminated UTF-8 string <i>src</i>. The null terminator is considered part of the UTF-8 string. </p>
<p> <code>Tcl_UtfFindLast</code> corresponds to <code>strrchr</code> for UTF-8 strings. It returns a pointer to the last occurrence of the Tcl_UniChar <i>ch</i> in the null-terminated UTF-8 string <i>src</i>. The null terminator is considered part of the UTF-8 string. </p>
<p> Given <i>src</i>, a pointer to some location in a UTF-8 string, <code>Tcl_UtfNext</code> returns a pointer to the next UTF-8 character in the string. The caller must not ask for the next character after the last character in the string if the string is not terminated by a null character. </p>
<p> Given <i>src</i>, a pointer to some location in a UTF-8 string (or to a null byte immediately following such a string), <code>Tcl_UtfPrev</code> returns a pointer to the closest preceding byte that starts a UTF-8 character. This function will not back up to a position before <i>start</i>, the start of the UTF-8 string. If <i>src</i> was already at <i>start</i>, the return value will be <i>start</i>. </p>
<p> <code>Tcl_UniCharAtIndex</code> corresponds to a C string array dereference or the Pascal Ord() function. It returns the Tcl_UniChar represented at the specified character (not byte) <i>index</i> in the UTF-8 string <i>src</i>. The source string must contain at least <i>index</i> characters. Behavior is undefined if a negative <i>index</i> is given. </p>
<p> <code>Tcl_UtfAtIndex</code> returns a pointer to the specified character (not byte) <i>index</i> in the UTF-8 string <i>src</i>. The source string must contain at least <i>index</i> characters. This is equivalent to calling <code>Tcl_UtfNext</code> <i>index</i> times. If a negative <i>index</i> is given, the return pointer points to the first character in the source string. </p>
<p> <code>Tcl_UtfBackslash</code> is a utility procedure used by several of the Tcl commands. It parses a backslash sequence and stores the properly formed UTF-8 character represented by the backslash sequence in the output buffer <i>dst</i>. At most <code>TCL_UTF_MAX</code> bytes are stored in the buffer. <code>Tcl_UtfBackslash</code> modifies <i>*readPtr</i> to contain the number of bytes in the backslash sequence, including the backslash character. The return value is the number of bytes stored in the output buffer. </p>
<p> See the <code>Tcl</code> manual entry for information on the valid backslash sequences. All of the sequences described in the Tcl manual entry are supported by <code>Tcl_UtfBackslash</code>. </p>
<h2>Keywords</h2>
<p>utf, unicode, backslash</p>
