---

title: "vsscanf(3)"
name: "vsscanf"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vsscanf/"
description: "scanf, fscanf, sscanf, vscanf, vsscanf, vfscanf – input format conversion"
---

<p>scanf, fscanf, sscanf, vscanf, vsscanf, vfscanf &#8211; input format conversion </p>

<pre><code>
 #include &lt;stdio.h&gt; 
 int scanf(const char *  format  , ...); 
 int fscanf(FILE *  stream  , const char *  format  , ...); 
 int sscanf(const char *  str  , const char *  format  , ...); 
 #include &lt;stdarg.h&gt; 
 int vscanf(const char *  format  , va_list  ap  ); 
 int vsscanf(const char *  str  , const char *  format  , va_list  ap  ); 
 int vfscanf(FILE *  stream  , const char *  format  , va_list  ap  ); 
</code></pre>
<p>Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>vscanf</code>(), <code>vsscanf</code>(), <code>vfscanf</code>(): </p>
<dl>
<dd> <p> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>scanf</code>() family of functions scans input according to <i>format</i> as described below. This format may contain <i>conversion specifications</i>; the results from such conversions, if any, are stored in the locations pointed to by the <i>pointer</i> arguments that follow <i>format</i>. Each <i>pointer</i> argument must be of a type that is appropriate for the value returned by the corresponding conversion specification. </p>
<p>If the number of conversion specifications in <i>format</i> exceeds the number of <i>pointer</i> arguments, the results are undefined. If the number of <i>pointer</i> arguments exceeds the number of conversion specifications, then the excess <i>pointer</i> arguments are evaluated, but are otherwise ignored. </p>
<p>The <code>scanf</code>() function reads input from the standard input stream <i>stdin</i>, <code>fscanf</code>() reads input from the stream pointer <i>stream</i>, and <code>sscanf</code>() reads its input from the character string pointed to by <i>str</i>. </p>
<p>The <code>vfscanf</code>() function is analogous to <code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3) and reads input from the stream pointer <i>stream</i> using a variable argument list of pointers (see <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3). The <code>vscanf</code>() function scans a variable argument list from the standard input and the <code>vsscanf</code>() function scans it from a string; these are analogous to the <code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) functions respectively. </p>
<p>The <i>format</i> string consists of a sequence of <i>directives</i> which describe how to process the sequence of input characters. If processing of a directive fails, no further input is read, and <code>scanf</code>() returns. A &quot;failure&quot; can be either of the following: <i>input failure</i>, meaning that input characters were unavailable, or <i>matching failure</i>, meaning that the input was inappropriate (see below). </p>
<p>A directive is one of the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A sequence of white-space characters (space, tab, newline, etc.; see <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3)). This directive matches any amount of white space, including none, in the input. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An ordinary character (i.e., one other than white space or &#8216;%&#8216;). This character must exactly match the next character of input. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A conversion specification, which commences with a &#8216;%&#8216; (percent) character. A sequence of characters from the input is converted according to this specification, and the result is placed in the corresponding <i>pointer</i> argument. If the next item of input does not match the conversion specification, the conversion fails---this is a <i>matching failure</i>. </p>
 </dd></dl>
<p>Each <i>conversion specification</i> in <i>format</i> begins with either the character &#8216;%&#8216; or the character sequence &quot;<code>%</code><i>n</i><code>$</code>&quot; (see below for the distinction) followed by: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> An optional &#8216;*&#8216; assignment-suppression character: <code>scanf</code>() reads input as directed by the conversion specification, but discards the input. No corresponding <i>pointer</i> argument is required, and this specification is not included in the count of successful assignments returned by <code>scanf</code>(). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For decimal conversions, an optional quote character (&#8216;). This specifies that the input number may include thousands&#8217; separators as defined by the <code>LC_NUMERIC</code> category of the current locale. (See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3).) The quote character may precede or follow the &#8216;*&#8216; assignment-suppression character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optional &#8216;m&#8217; character. This is used with string conversions (<i>%s</i>, <i>%c</i>, <i>%[</i>), and relieves the caller of the need to allocate a corresponding buffer to hold the input: instead, <code>scanf</code>() allocates a buffer of sufficient size, and assigns the address of this buffer to the corresponding <i>pointer</i> argument, which should be a pointer to a <i>char&nbsp;*</i> variable (this variable does not need to be initialized before the call). The caller should subsequently <code><a href="/docs/linux/man/3-free/">free</a></code>(3) this buffer when it is no longer required. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optional decimal integer which specifies the <i>maximum field width</i>. Reading of characters stops either when this maximum is reached or when a nonmatching character is found, whichever happens first. Most conversions discard initial white space characters (the exceptions are noted below), and these discarded characters don&#8217;t count toward the maximum field width. String input conversions store a terminating null byte (&#8216;\0&#8217;) to mark the end of the input; the maximum field width does not include this terminator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optional <i>type modifier character</i>. For example, the <code>l</code> type modifier is used with integer conversions such as <code>%d</code> to specify that the corresponding <i>pointer</i> argument refers to a <i>long</i> rather than a pointer to an <i>int</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <i>conversion specifier</i> that specifies the type of input conversion to be performed. </p>
 </dd></dl>
<p>The conversion specifications in <i>format</i> are of two forms, either beginning with &#8216;%&#8216; or beginning with &quot;<code>%</code><i>n</i><code>$</code>&quot;. The two forms should not be mixed in the same <i>format</i> string, except that a string containing &quot;<code>%</code><i>n</i><code>$</code>&quot; specifications can include <code>%%</code> and <code>%*</code>. If <i>format</i> contains &#8216;%&#8216; specifications, then these correspond in order with successive <i>pointer</i> arguments. In the &quot;<code>%</code><i>n</i><code>$</code>&quot; form (which is specified in POSIX.1-2001, but not C99), <i>n</i> is a decimal integer that specifies that the converted input should be placed in the location referred to by the <i>n</i>-th <i>pointer</i> argument following <i>format</i>.  </p>
<h3>Conversions</h3>
<p> The following <i>type modifier characters</i> can appear in a conversion specification: </p>
<dl>
<dt><code>h</code></dt>
<dd> <p> Indicates that the conversion will be one of <code>d</code>, <code>i</code>, <code>o</code>, <code>u</code>, <code>x</code>, <code>X</code>, or <code>n</code> and the next pointer is a pointer to a <i>short</i> or <i>unsigned short</i> (rather than <i>int</i>). </p>
 </dd>
<dt><code>hh</code></dt>
<dd> <p> As for <code>h</code>, but the next pointer is a pointer to a <i>signed char</i> or <i>unsigned char</i>. </p>
 </dd>
<dt><code>j</code></dt>
<dd> <p> As for <code>h</code>, but the next pointer is a pointer to an <i>intmax_t</i> or a <i>uintmax_t</i>. This modifier was introduced in C99. </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> Indicates either that the conversion will be one of <code>d</code>, <code>i</code>, <code>o</code>, <code>u</code>, <code>x</code>, <code>X</code>, or <code>n</code> and the next pointer is a pointer to a <i>long</i> or <i>unsigned long</i> (rather than <i>int</i>), or that the conversion will be one of <code>e</code>, <code>f</code>, or <code>g</code> and the next pointer is a pointer to <i>double</i> (rather than <i>float</i>). Specifying two <code>l</code> characters is equivalent to <code>L</code>. If used with <code>%c</code> or <code>%s</code>, the corresponding parameter is considered as a pointer to a wide character or wide-character string respectively. </p>
 </dd>
<dt><code>L</code></dt>
<dd> <p> Indicates that the conversion will be either <code>e</code>, <code>f</code>, or <code>g</code> and the next pointer is a pointer to <i>long double</i> or the conversion will be <code>d</code>, <code>i</code>, <code>o</code>, <code>u</code>, or <code>x</code> and the next pointer is a pointer to <i>long long</i>. </p>
 </dd>
<dt><code>q</code></dt>
<dd> <p> equivalent to <code>L</code>. This specifier does not exist in ANSI C. </p>
 </dd>
<dt><code>t</code></dt>
<dd> <p> As for <code>h</code>, but the next pointer is a pointer to a <i>ptrdiff_t</i>. This modifier was introduced in C99. </p>
 </dd>
<dt><code>z</code></dt>
<dd> <p> As for <code>h</code>, but the next pointer is a pointer to a <i>size_t</i>. This modifier was introduced in C99. </p>
 </dd></dl>
<p>The following <i>conversion specifiers</i> are available: </p>
<dl>
<dt><code>%</code></dt>
<dd> <p> Matches a literal &#8216;%&#8216;. That is, <code>%%</code> in the format string matches a single input &#8216;%&#8216; character. No conversion is done (but initial white space characters are discarded), and assignment does not occur. </p>
 </dd>
<dt><code>d</code></dt>
<dd> <p> Matches an optionally signed decimal integer; the next pointer must be a pointer to <i>int</i>. </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> Matches an optionally signed integer; the next pointer must be a pointer to <i>int</i>. The integer is read in base 16 if it begins with <i>0x</i> or <i>0X</i>, in base 8 if it begins with <i>0</i>, and in base 10 otherwise. Only characters that correspond to the base are used. </p>
 </dd>
<dt><code>o</code></dt>
<dd> <p> Matches an unsigned octal integer; the next pointer must be a pointer to <i>unsigned int</i>. </p>
 </dd>
<dt><code>u</code></dt>
<dd> <p> Matches an unsigned decimal integer; the next pointer must be a pointer to <i>unsigned int</i>. </p>
 </dd>
<dt><code>x</code></dt>
<dd> <p> Matches an unsigned hexadecimal integer (that may optionally begin with a prefix of <i>0x</i> or <i>0X</i>, which is discarded); the next pointer must be a pointer to <i>unsigned int</i>. </p>
 </dd>
<dt><code>X</code></dt>
<dd> <p> Equivalent to <code>x</code>. </p>
 </dd>
<dt><code>f</code></dt>
<dd> <p> Matches an optionally signed floating-point number; the next pointer must be a pointer to <i>float</i>. </p>
 </dd>
<dt><code>e</code></dt>
<dd> <p> Equivalent to <code>f</code>. </p>
 </dd>
<dt><code>g</code></dt>
<dd> <p> Equivalent to <code>f</code>. </p>
 </dd>
<dt><code>E</code></dt>
<dd> <p> Equivalent to <code>f</code>. </p>
 </dd>
<dt><code>a</code></dt>
<dd> <p> (C99) Equivalent to <code>f</code>. </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> Matches a sequence of non-white-space characters; the next pointer must be a pointer to the initial element of a character array that is long enough to hold the input sequence and the terminating null byte (&#8216;\0&#8217;), which is added automatically. The input string stops at white space or at the maximum field width, whichever occurs first. </p>
 </dd>
<dt><code>c</code></dt>
<dd> <p> Matches a sequence of characters whose length is specified by the <i>maximum field width</i> (default 1); the next pointer must be a pointer to <i>char</i>, and there must be enough room for all the characters (no terminating null byte is added). The usual skip of leading white space is suppressed. To skip white space first, use an explicit space in the format. </p>
 </dd>
<dt><code>[</code></dt>
<dd> <p> Matches a nonempty sequence of characters from the specified set of accepted characters; the next pointer must be a pointer to <i>char</i>, and there must be enough room for all the characters in the string, plus a terminating null byte. The usual skip of leading white space is suppressed. The string is to be made up of characters in (or not in) a particular set; the set is defined by the characters between the open bracket <code>[</code> character and a close bracket <code>]</code> character. The set <i>excludes</i> those characters if the first character after the open bracket is a circumflex (<code>ha</code>). To include a close bracket in the set, make it the first character after the open bracket or the circumflex; any other position will end the set. The hyphen character <code>-</code> is also special; when placed between two other characters, it adds all intervening characters to the set. To include a hyphen, make it the last character before the final close bracket. For instance, <code>[ha]0-9-]</code> means the set &quot;everything except close bracket, zero through nine, and hyphen&quot;. The string ends with the appearance of a character not in the (or, with a circumflex, in) set or when the field width runs out. </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> Matches a pointer value (as printed by <code>%p</code> in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)); the next pointer must be a pointer to a pointer to <i>void</i>. </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> Nothing is expected; instead, the number of characters consumed thus far from the input is stored through the next pointer, which must be a pointer to <i>int</i>. This is <i>not</i> a conversion and does <i>not</i> increase the count returned by the function. The assignment can be suppressed with the <code>*</code> assignment-suppression character, but the effect on the return value is undefined. Therefore <code>%*n</code> conversions should not be used. </p>
 </dd></dl>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the number of input items successfully matched and assigned; this can be fewer than provided for, or even zero, in the event of an early matching failure. </p>
<p>The value <code>EOF</code> is returned if the end of input is reached before either the first successful conversion or a matching failure occurs. <code>EOF</code> is also returned if a read error occurs, in which case the error indicator for the stream (see <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3)) is set, and <i>errno</i> is set to indicate the error.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></dt>
<dd> <p> The file descriptor underlying <i>stream</i> is marked nonblocking, and the read operation would block. </p>
 </dd>
<dt><code>EBADF</code></dt>
<dd> <p> The file descriptor underlying <i>stream</i> is invalid, or not open for reading. </p>
 </dd>
<dt><code>EILSEQ</code></dt>
<dd> <p> Input byte sequence does not form a valid character. </p>
 </dd>
<dt><code>EINTR</code></dt>
<dd> <p> The read operation was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> Not enough arguments; or <i>format</i> is NULL. </p>
 </dd>
<dt><code>ENOMEM</code></dt>
<dd> <p> Out of memory. </p>
 </dd>
<dt><code>ERANGE</code></dt>
<dd> <p> The result of an integer conversion would exceed the size that can be stored in the corresponding integer type. </p>
 </dd></dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>scanf</code>(), <code>fscanf</code>(),  <code>sscanf</code>(), <code>vscanf</code>(),  <code>vsscanf</code>(), <code>vfscanf</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The functions <code>fscanf</code>(), <code>scanf</code>(), and <code>sscanf</code>() conform to C89 and C99 and POSIX.1-2001. These standards do not specify the <code>ERANGE</code> error. </p>
<p>The <code>q</code> specifier is the 4.4BSD notation for <i>long long</i>, while <code>ll</code> or the usage of <code>L</code> in integer conversions is the GNU notation. </p>
<p>The Linux version of these functions is based on the <i>GNU</i> <i>libio</i> library. Take a look at the <i>info</i> documentation of <i>GNU</i> <i>libc (glibc-1.08)</i> for a more concise description.  </p>
<h2>NOTES</h2>
<h3>The 'a' assignment-allocation modifier</h3>
<p> Originally, the GNU C library supported dynamic allocation for string inputs (as a nonstandard extension) via the <code>a</code> character. (This feature is present at least as far back as glibc 2.0.) Thus, one could write the following to have <code>scanf</code>() allocate a buffer for an input string, with a pointer to that buffer being returned in <i>*buf</i>: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*buf; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;scanf(&quot;%as&quot;,&nbsp;&amp;buf); </p>
<p>The use of the letter <code>a</code> for this purpose was problematic, since <code>a</code> is also specified by the ISO C standard as a synonym for <code>f</code> (floating-point input). POSIX.1-2008 instead specifies the <code>m</code> modifier for assignment allocation (as documented in DESCRIPTION, above). </p>
<p>Note that the <code>a</code> modifier is not available if the program is compiled with <i>gcc -std=c99</i> or <i>gcc -D_ISOC99_SOURCE</i> (unless <code>_GNU_SOURCE</code> is also specified), in which case the <code>a</code> is interpreted as a specifier for floating-point numbers (see above). </p>
<p>Support for the <code>m</code> modifier was added to glibc starting with version 2.7, and new programs should use that modifier instead of <code>a</code>. </p>
<p>As well as being standardized by POSIX, the <code>m</code> modifier has the following further advantages over the use of <code>a:</code> </p>
<dl>
<dt>*</dt>
<dd> <p> It may also be applied to <code>%c</code> conversion specifiers (e.g., <code>%3mc</code>). </p>
 </dd>
<dt>*</dt>
<dd> <p> It avoids ambiguity with respect to the <code>%a</code> floating-point conversion specifier (and is unaffected by <i>gcc -std=c99</i> etc.). </p>
 </dd></dl>
<h2>BUGS</h2>
<p> All functions are fully C89 conformant, but provide the additional specifiers <code>q</code> and <code>a</code> as well as an additional behavior of the <code>L</code> and <code>l</code> specifiers. The latter may be considered to be a bug, as it changes the behavior of specifiers defined in C89. </p>
<p>Some combinations of the type modifiers and conversion specifiers defined by ANSI C do not make sense (e.g., <code>%Ld</code>). While they may have a well-defined behavior on Linux, this need not to be so on other architectures. Therefore it usually is better to use modifiers that are not defined by ANSI C at all, that is, use <code>q</code> instead of <code>L</code> in combination with <code>d</code>, <code>i</code>, <code>o</code>, <code>u</code>, <code>x</code>, and <code>X</code> conversions or <code>ll</code>. </p>
<p>The usage of <code>q</code> is not the same as on 4.4BSD, as it may be used in float conversions equivalently to <code>L</code>.  </p>
<h2>EXAMPLES</h2>
<p> To use the dynamic allocation conversion specifier, specify <code>m</code> as a length modifier (thus <code>%ms</code> or <code>%m[</code><i>range</i><code>]</code>). The caller must <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the returned string, as in the following example: </p>
<p>char *p; int n; </p>
<p>errno = 0; n = scanf(&quot;%m[a-z]&quot;, &amp;p); if (n == 1) { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;read:&nbsp;%s\n&quot;, p); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(p); } else if (errno != 0) { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;scanf&quot;); } else { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;No matching characters\n&quot;); } </p>
<p>As shown in the above example, it is necessary to call <code><a href="/docs/linux/man/3-free/">free</a></code>(3) only if the <code>scanf</code>() call successfully read a string.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getc/">getc</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3), <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
