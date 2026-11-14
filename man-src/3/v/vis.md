---
title: "vis(3)"
name: "vis"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vis/"
description: "vis strvis strnvis strvisx – visually encode characters"
---

<p><code>vis</code> <code>strvis</code> <code>strnvis</code> <code>strvisx</code> &#8211; visually encode characters</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In stdlib.h In bsd/vis.h Ft char * Fn vis char *dst int c int flag int nextc Ft int Fn strvis char *dst const char *src int flag Ft int Fn strnvis char *dst const char *src size_t size int flag Ft int Fn strvisx char *dst const char *src size_t len int flag</p>
<h2>Description</h2>
<p>The Fn vis function copies into Fa dst a string which represents the character Fa c . If Fa c needs no encoding, it is copied in unaltered. The string is NUL terminated and a pointer to the end of the string is returned. The maximum length of any encoding is four characters (not including the trailing NUL); thus, when encoding a set of characters into a buffer, the size of the buffer should be four times the number of characters encoded, plus one for the trailing NUL. The Fa flag parameter is used for altering the default range of characters considered for encoding and for altering the visual representation. The additional character, Fa nextc , is only used when selecting the <code>VIS_CSTYLE</code> encoding format (explained below). </p>
<p> The Fn strvis , Fn strnvis and Fn strvisx functions copy into Fa dst a visual representation of the string Fa src . The Fn strvis function encodes characters from Fa src up to the first NUL. The Fn strnvis function encodes characters from Fa src up to the first NUL or the end of Fa dst , as indicated by Fa size . The Fn strvisx function encodes exactly Fa len characters from Fa src (this is useful for encoding a block of data that may contain NULs). All three forms NUL terminate Fa dst , except for Fn strnvis when Fa size is zero, in which case Fa dst is not touched. For Fn strvis and Fn strvisx , the size of Fa dst must be four times the number of characters encoded from Fa src (plus one for the NUL). Fn strvis and Fn strvisx return the number of characters in Fa dst (not including the trailing NUL). Fn strnvis returns the length that Fa dst would become if it were of unlimited size (similar to <a href="/docs/linux/man/3-snprintf/">snprintf</a>(3) or <a href="/docs/linux/man/3-strlcpy/">strlcpy</a>(3)). This can be used to detect truncation but it also means that the return value of Fn strnvis must not be used without checking it against Fa size . </p>
<p> The encoding is a unique, invertible representation composed entirely of graphic characters; it can be decoded back into the original form using the <a href="/docs/linux/man/3-unvis/">unvis</a>(3) or <a href="/docs/linux/man/3-strunvis/">strunvis</a>(3) functions. </p>
<p> There are two parameters that can be controlled: the range of characters that are encoded, and the type of representation used. By default, all non-graphic characters except space, tab, and newline are encoded (see <a href="/docs/linux/man/3-isgraph/">isgraph</a>(3)). The following flags alter this:</p>
<dl>
<dt><code>VIS_GLOB</code></p>
<dd>Also encode magic characters recognized by <a href="/docs/linux/man/3-glob/">glob</a>(3) ( `*&#8217; `?&#8217; , `[&#8216; ) and `#&#8217;</p>
<dt><code>VIS_SP</code></p>
<dd>Also encode space.</p>
<dt><code>VIS_TAB</code></p>
<dd>Also encode tab.</p>
<dt><code>VIS_NL</code></p>
<dd>Also encode newline.</p>
<dt><code>VIS_WHITE</code></p>
<dd>Synonym for <code>VIS_SP</code> | <code>VIS_TAB</code> | <code>VIS_NL</code></p>
<dt><code>VIS_SAFE</code></p>
<dd>Only encode &#8220;unsafe&#8221; characters. These are control characters which may cause common terminals to perform unexpected functions. Currently this form allows space, tab, newline, backspace, bell, and return &#8212; in addition to all graphic characters &#8212; unencoded.</dl>
<p> There are three forms of encoding. All forms use the backslash `\&#8217; character to introduce a special sequence; two backslashes are used to represent a real backslash. These are the visual formats:</p>
<dl>
<dt><code>(default)</code></p>
<dd>Use an `M&#8217; to represent meta characters (characters with the 8th bit set), and use a caret `^&#8217; to represent control characters (see <a href="/docs/linux/man/3-iscntrl/">iscntrl</a>(3)). The following formats are used:</p>
<dl>
<dt><code>\^C</code></p>
<dd>Represents the control character `C&#8217; Spans characters `
