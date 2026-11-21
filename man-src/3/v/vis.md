---
title: "vis(3)"
name: "vis"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vis/"
description: "vis strvis strnvis strvisx – visually encode characters"
---
<p> <code>vis</code> <code>strvis</code> <code>strnvis</code> <code>strvisx</code> - visually encode characters </p>
<h2>LIBRARY</h2>
<p> Lb libbsd  </p>
<h2>SYNOPSIS</h2>
<p> In stdlib.h In bsd/vis.h Ft char * Fn vis char *dst int c int flag int nextc Ft int Fn strvis char *dst const char *src int flag Ft int Fn strnvis char *dst const char *src size_t size int flag Ft int Fn strvisx char *dst const char *src size_t len int flag  </p>
<h2>DESCRIPTION</h2>
<p> The Fn vis function copies into Fa dst a string which represents the character Fa c . If Fa c needs no encoding, it is copied in unaltered. The string is NUL terminated and a pointer to the end of the string is returned. The maximum length of any encoding is four characters (not including the trailing NUL); thus, when encoding a set of characters into a buffer, the size of the buffer should be four times the number of characters encoded, plus one for the trailing NUL. The Fa flag parameter is used for altering the default range of characters considered for encoding and for altering the visual representation. The additional character, Fa nextc , is only used when selecting the <code>VIS_CSTYLE</code> encoding format (explained below). </p>
<p>The Fn strvis , Fn strnvis and Fn strvisx functions copy into Fa dst a visual representation of the string Fa src . The Fn strvis function encodes characters from Fa src up to the first NUL. The Fn strnvis function encodes characters from Fa src up to the first NUL or the end of Fa dst , as indicated by Fa size . The Fn strvisx function encodes exactly Fa len characters from Fa src (this is useful for encoding a block of data that may contain NULs). All three forms NUL terminate Fa dst , except for Fn strnvis when Fa size is zero, in which case Fa dst is not touched. For Fn strvis and Fn strvisx , the size of Fa dst must be four times the number of characters encoded from Fa src (plus one for the NUL). Fn strvis and Fn strvisx return the number of characters in Fa dst (not including the trailing NUL). Fn strnvis returns the length that Fa dst would become if it were of unlimited size (similar to <a href="/docs/linux/man/3-snprintf/">snprintf</a>(3) or <a href="/docs/linux/man/3-strlcpy/">strlcpy</a>(3)). This can be used to detect truncation but it also means that the return value of Fn strnvis must not be used without checking it against Fa size . </p>
<p>The encoding is a unique, invertible representation composed entirely of graphic characters; it can be decoded back into the original form using the <a href="/docs/linux/man/3-unvis/">unvis</a>(3) or strunvis(3) functions. </p>
<p>There are two parameters that can be controlled: the range of characters that are encoded, and the type of representation used. By default, all non-graphic characters except space, tab, and newline are encoded (see <a href="/docs/linux/man/3-isgraph/">isgraph</a>(3)). The following flags alter this: </p>
<dl>
<dt><code>VIS_GLOB</code></dt>
<dd> <p> Also encode magic characters recognized by <a href="/docs/linux/man/3-glob/">glob</a>(3) ( `*&#8216; `?&#8216; , `[&#8216; ) and `#&#8216; </p>
 </dd>
<dt><code>VIS_SP</code></dt>
<dd> <p> Also encode space. </p>
 </dd>
<dt><code>VIS_TAB</code></dt>
<dd> <p> Also encode tab. </p>
 </dd>
<dt><code>VIS_NL</code></dt>
<dd> <p> Also encode newline. </p>
 </dd>
<dt><code>VIS_WHITE</code></dt>
<dd> <p> Synonym for <code>VIS_SP</code> | <code>VIS_TAB</code> | <code>VIS_NL</code> </p>
 </dd>
<dt><code>VIS_SAFE</code></dt>
<dd> <p> Only encode ``unsafe&#8217;&#8216; characters. These are control characters which may cause common terminals to perform unexpected functions. Currently this form allows space, tab, newline, backspace, bell, and return -- in addition to all graphic characters -- unencoded. </p>
 </dd></dl>
<p>There are three forms of encoding. All forms use the backslash `\&#8216; character to introduce a special sequence; two backslashes are used to represent a real backslash. These are the visual formats: </p>
<dl>
<dt><code>(default)</code></dt>
<dd> <p> Use an `M&#8217; to represent meta characters (characters with the 8th bit set), and use a caret `^&#8216; to represent control characters (see <a href="/docs/linux/man/3-iscntrl/">iscntrl</a>(3)). The following formats are used: </p>
 </dd>
<dl>
<dt><code>\^C</code></dt>
<dd> <p> Represents the control character `C&#8217; Spans characters `\000&#8217; through `\037&#8217; , and `\177&#8217; (as `\^?&#8216; ) . </p>
 </dd>
<dt><code>\M-C</code></dt>
<dd> <p> Represents character `C&#8217; with the 8th bit set. Spans characters `\241&#8217; through `\376&#8217; </p>
 </dd>
<dt><code>\M^C</code></dt>
<dd> <p> Represents control character `C&#8217; with the 8th bit set. Spans characters `\200&#8217; through `\237&#8217; , and `\377&#8217; (as `\M^?&#8216; ) . </p>
 </dd>
<dt><code>\040</code></dt>
<dd> <p> Represents <code>ASCII</code> space. </p>
 </dd>
<dt><code>\240</code></dt>
<dd> <p> Represents Meta-space. </p>
 </dd></dl>
<dt><code>VIS_CSTYLE</code></dt>
<dd> <p> Use C-style backslash sequences to represent standard non-printable characters. The following sequences are used to represent the indicated characters: </p>
<blockquote><pre><code>
 \a - BEL (007) 
 \b - BS (010) 
 \f - NP (014) 
 \n - NL (012) 
 \r - CR (015) 
 \s - SP (040) 
 \t - HT (011) 
 \v - VT (013) 
 \0 - NUL (000) 
</code></pre>
</blockquote>
<p>When using this format, the Fa nextc parameter is looked at to determine if a NUL character can be encoded as `\0&#8217; instead of `\000&#8217; If Fa nextc is an octal digit, the latter representation is used to avoid ambiguity. </p>
 </dd>
<dt><code>VIS_OCTAL</code></dt>
<dd> <p> Use a three digit octal sequence. The form is `\ddd&#8217; where <i>d</i> represents an octal digit. </p>
 </dd></dl>
<p>There is one additional flag, <code>VIS_NOSLASH</code> which inhibits the doubling of backslashes and the backslash before the default format (that is, control characters are represented by `^C&#8217; and meta characters as `M-C&#8217; ) . With this flag set, the encoding is ambiguous and non-invertible.  </p>
<h2>SEE ALSO</h2>
<p> unvis(1), vis(1), <a href="/docs/linux/man/3-snprintf/">snprintf</a>(3), <a href="/docs/linux/man/3-strlcpy/">strlcpy</a>(3), <a href="/docs/linux/man/3-unvis/">unvis</a>(3)  </p>
<h2>HISTORY</h2>
<p> The Fn vis , Fn strvis and Fn strvisx functions first appeared in BSD 4.4 The Fn strnvis function first appeared in Ox 2.9 . </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">LIBRARY</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">HISTORY</a></dt>
<dd>  </dd></dl>
