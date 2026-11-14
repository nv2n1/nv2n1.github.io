---
title: "pcre2convert(3)"
name: "pcre2convert"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2convert/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Experimental Pattern Conversion Functions</h2>
<p>This document describes a set of functions that can be used to convert &quot;foreign&quot; patterns into PCRE2 regular expressions. This facility is currently experimental, and may be changed in future releases. Two kinds of pattern, globs and POSIX patterns, are supported.</p>
<h2>The Convert Context</h2>
<pre><code>pcre2_convert_context *pcre2_convert_context_create(</code>
<code> pcre2_general_context *</code><i>gcontext</i>);
<code>pcre2_convert_context *pcre2_convert_context_copy(</code>
<code> pcre2_convert_context *</code><i>cvcontext</i>);
<code>void pcre2_convert_context_free(pcre2_convert_context *</code><i>cvcontext</i>);
<code>int pcre2_set_glob_escape(pcre2_convert_context *</code><i>cvcontext</i>,
<code> uint32_t </code><i>escape_char</i>);
<code>int pcre2_set_glob_separator(pcre2_convert_context *</code><i>cvcontext</i>,
<code> uint32_t </code><i>separator_char</i>);</pre>
<p>A convert context is used to hold parameters that affect the way that pattern conversion works. Like all PCRE2 contexts, you need to use a context only if you want to override the defaults. There are the usual create, copy, and free functions. If custom memory management functions are set in a general context that is passed to <code>pcre2_convert_context_create()</code>, they are used for all memory management within the conversion functions. </p>
<p> There are only two parameters in the convert context at present. Both apply only to glob conversions. The escape character defaults to grave accent under Windows, otherwise backslash. It can be set to zero, meaning no escape character, or to any punctuation character with a code point less than 256. The separator character defaults to backslash under Windows, otherwise forward slash. It can be set to forward slash, backslash, or dot. </p>
<p> The two setting functions return zero on success, or PCRE2_ERROR_BADDATA if their second argument is invalid.</p>
<h2>The Conversion Function</h2>
<pre><code>int pcre2_pattern_convert(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, PCRE2_UCHAR **<i>buffer</i>,
<code> PCRE2_SIZE *</code><i>blength</i>, pcre2_convert_context *<i>cvcontext</i>);
<code>void pcre2_converted_pattern_free(PCRE2_UCHAR *</code><i>converted_pattern</i>);</pre>
<p>The first two arguments of <code>pcre2_pattern_convert()</code> define the foreign pattern that is to be converted. The length may be given as PCRE2_ZERO_TERMINATED. The <code>options</code> argument defines how the pattern is to be processed. If the input is UTF, the PCRE2_CONVERT_UTF option should be set. PCRE2_CONVERT_NO_UTF_CHECK may also be set if you are sure the input is valid. One or more of the glob options, or one of the following POSIX options must be set to define the type of conversion that is required: </p>
<p>&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB_NO_WILD_SEPARATOR<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_GLOB_NO_STARSTAR<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_POSIX_BASIC<br />
&nbsp;<wbr>&nbsp;PCRE2_CONVERT_POSIX_EXTENDED </p>
<p> Details of the conversions are given below. The <code>buffer</code> and <code>blength</code> arguments define how the output is handled: </p>
<p> If <code>buffer</code> is NULL, the function just returns the length of the converted pattern via <code>blength</code>. This is one less than the length of buffer needed, because a terminating zero is always added to the output. </p>
<p> If <code>buffer</code> points to a NULL pointer, an output buffer is obtained using the allocator in the context or <code>malloc()</code> if no context is supplied. A pointer to this buffer is placed in the variable to which <code>buffer</code> points. When no longer needed the output buffer must be freed by calling <code>pcre2_converted_pattern_free()</code>. If this function is called with a NULL argument, it returns immediately without doing anything. </p>
<p> If <code>buffer</code> points to a non-NULL pointer, <code>blength</code> must be set to the actual length of the buffer provided (in code units). </p>
<p> In all cases, after successful conversion, the variable pointed to by <code>blength</code> is updated to the length actually used (in code units), excluding the terminating zero that is always added. </p>
<p> If an error occurs, the length (via <code>blength</code>) is set to the offset within the input pattern where the error was detected. Only gross syntax errors are caught; there are plenty of errors that will get passed on for <code>pcre2_compile()</code> to discover. </p>
<p> The return from <code>pcre2_pattern_convert()</code> is zero on success or a non-zero PCRE2 error code. Note that PCRE2 error codes may be positive or negative: <code>pcre2_compile()</code> uses mostly positive codes and <code>pcre2_match()</code> negative ones; <code>pcre2_convert()</code> uses existing codes of both kinds. A textual error message can be obtained by calling <code>pcre2_get_error_message()</code>.</p>
<h2>Converting Globs</h2>
<p>Globs are used to match file names, and consequently have the concept of a &quot;path separator&quot;, which defaults to backslash under Windows and forward slash otherwise. If PCRE2_CONVERT_GLOB is set, the wildcards * and ? are not permitted to match separator characters, but the double-star (**) feature (which does match separators) is supported. </p>
<p> PCRE2_CONVERT_GLOB_NO_WILD_SEPARATOR matches globs with wildcards allowed to match separator characters. PCRE2_GLOB_NO_STARSTAR matches globs with the double-star feature disabled. These options may be given together.</p>
<h2>Converting Posix Patterns</h2>
<p>POSIX defines two kinds of regular expression pattern: basic and extended. These can be processed by setting PCRE2_CONVERT_POSIX_BASIC or PCRE2_CONVERT_POSIX_EXTENDED, respectively. </p>
<p> In POSIX patterns, backslash is not special in a character class. Unmatched closing parentheses are treated as literals. </p>
<p> In basic patterns, ? + | {} and () must be escaped to be recognized as metacharacters outside a character class. If the first character in the pattern is * it is treated as a literal. ^ is a metacharacter only at the start of a branch. </p>
<p> In extended patterns, a backslash not in a character class always makes the next character literal, whatever it is. There are no backreferences. </p>
<p> Note: POSIX mandates that the longest possible match at the first matching position must be found. This is not what <code>pcre2_match()</code> does; it yields the first match that is found. An application can use <code>pcre2_dfa_match()</code> to find the longest match, but that does not support backreferences (but then neither do POSIX extended patterns).</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 28 June 2018
Copyright (c) 1997-2018 University of Cambridge.</pre>
