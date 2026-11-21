---
title: "pcre2_compile(3)"
name: "pcre2_compile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_compile/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_code *pcre2_compile(PCRE2_SPTR </code><i>pattern</i>, PCRE2_SIZE <i>length</i>,
<code> uint32_t </code><i>options</i>, int *<i>errorcode</i>, PCRE2_SIZE *<i>erroroffset,</i>
<code> pcre2_compile_context *</code><i>ccontext</i>);</pre>
<h2>Description</h2>
<p>This function compiles a regular expression pattern into an internal form. Its arguments are:<br />
&nbsp;<wbr>&nbsp;<i>pattern</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A string containing expression to be compiled<br />
&nbsp;<wbr>&nbsp;<i>length</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The length of the string or PCRE2_ZERO_TERMINATED<br />
&nbsp;<wbr>&nbsp;<i>options</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Option bits<br />
&nbsp;<wbr>&nbsp;<i>errorcode</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put an error code<br />
&nbsp;<wbr>&nbsp;<i>erroffset</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Where to put an error offset<br />
&nbsp;<wbr>&nbsp;<i>ccontext</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pointer to a compile context or NULL The length of the pattern and any error offset that is returned are in code units, not characters. A compile context is needed only if you want to provide custom memory allocation functions, or to provide an external function for system stack size checking, or to change one or more of these parameters:<br />
&nbsp;<wbr>&nbsp;What&nbsp;\R matches&nbsp;(Unicode newlines, or CR, LF, CRLF only);<br />
&nbsp;<wbr>&nbsp;PCRE2&#8217;s character tables;<br />
&nbsp;<wbr>&nbsp;The newline character sequence;<br />
&nbsp;<wbr>&nbsp;The compile time nested parentheses limit;<br />
&nbsp;<wbr>&nbsp;The maximum pattern length&nbsp;(in code units)&nbsp;that is allowed.<br />
&nbsp;<wbr>&nbsp;The additional options bits&nbsp;(see pcre2_set_compile_extra_options()) The option bits are:<br />
&nbsp;<wbr>&nbsp;PCRE2_ANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Force pattern anchoring<br />
&nbsp;<wbr>&nbsp;PCRE2_ALLOW_EMPTY_CLASS&nbsp;<wbr>&nbsp;Allow empty classes<br />
&nbsp;<wbr>&nbsp;PCRE2_ALT_BSUX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alternative handling of&nbsp;&nbsp;\u,&nbsp;\U, and&nbsp;\x <br />
&nbsp;<wbr>&nbsp;PCRE2_ALT_CIRCUMFLEX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Alternative handling of&nbsp;^&nbsp;in multiline mode <br />
&nbsp;<wbr>&nbsp;PCRE2_ALT_VERBNAMES&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Process backslashes in verb names <br />
&nbsp;<wbr>&nbsp;PCRE2_AUTO_CALLOUT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compile automatic callouts <br />
&nbsp;<wbr>&nbsp;PCRE2_CASELESS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do caseless matching <br />
&nbsp;<wbr>&nbsp;PCRE2_DOLLAR_ENDONLY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;$&nbsp;not to match newline at end <br />
&nbsp;<wbr>&nbsp;PCRE2_DOTALL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;. matches anything including NL <br />
&nbsp;<wbr>&nbsp;PCRE2_DUPNAMES&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Allow duplicate names for subpatterns <br />
&nbsp;<wbr>&nbsp;PCRE2_ENDANCHORED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pattern can match only at end of subject <br />
&nbsp;<wbr>&nbsp;PCRE2_EXTENDED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ignore white space and&nbsp;#&nbsp;comments <br />
&nbsp;<wbr>&nbsp;PCRE2_FIRSTLINE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Force matching to be before newline <br />
&nbsp;<wbr>&nbsp;PCRE2_LITERAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pattern characters are all literal <br />
&nbsp;<wbr>&nbsp;PCRE2_MATCH_INVALID_UTF&nbsp;<wbr>&nbsp;Enable support for matching invalid UTF <br />
&nbsp;<wbr>&nbsp;PCRE2_MATCH_UNSET_BACKREF&nbsp;<wbr>&nbsp;Match unset backreferences <br />
&nbsp;<wbr>&nbsp;PCRE2_MULTILINE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;^&nbsp;and&nbsp;$&nbsp;match newlines within data <br />
&nbsp;<wbr>&nbsp;PCRE2_NEVER_BACKSLASH_C&nbsp;<wbr>&nbsp;Lock out the use of&nbsp;\C in patterns <br />
&nbsp;<wbr>&nbsp;PCRE2_NEVER_UCP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Lock out PCRE2_UCP, e.g. via&nbsp;(*UCP) <br />
&nbsp;<wbr>&nbsp;PCRE2_NEVER_UTF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Lock out PCRE2_UTF, e.g. via&nbsp;(*UTF) <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_AUTO_CAPTURE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Disable numbered capturing paren- <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;theses&nbsp;(named ones available) <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_AUTO_POSSESS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Disable auto-possessification <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_DOTSTAR_ANCHOR&nbsp;<wbr>&nbsp;Disable automatic anchoring for .* <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_START_OPTIMIZE&nbsp;<wbr>&nbsp;Disable match-time start optimizations <br />
&nbsp;<wbr>&nbsp;PCRE2_NO_UTF_CHECK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not check the pattern for UTF validity <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(only relevant if PCRE2_UTF is set) <br />
&nbsp;<wbr>&nbsp;PCRE2_UCP&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Use Unicode properties for&nbsp;\d,&nbsp;\w, etc. <br />
&nbsp;<wbr>&nbsp;PCRE2_UNGREEDY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Invert greediness of quantifiers <br />
&nbsp;<wbr>&nbsp;PCRE2_USE_OFFSET_LIMIT&nbsp;<wbr>&nbsp;<wbr>&nbsp;Enable offset limit for unanchored matching <br />
&nbsp;<wbr>&nbsp;PCRE2_UTF&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Treat pattern and subjects as UTF strings </p>
<p> PCRE2 must be built with Unicode support (the default) in order to use PCRE2_UTF, PCRE2_UCP and related options. </p>
<p> Additional options may be set in the compile context via the <code>pcre2_set_compile_extra_options</code> function. </p>
<p> The yield of this function is a pointer to a private data structure that contains the compiled pattern, or NULL if an error was detected. </p>
<p> There is a complete description of the PCRE2 native API, with more detail on each option, in the <code>pcre2api</code> page, and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
