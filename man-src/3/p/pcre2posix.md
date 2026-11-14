---
title: "pcre2posix(3)"
name: "pcre2posix"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2posix/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2posix.h&gt;
int pcre2_regcomp(regex_t *preg, const char *pattern,
                  int cflags);

int pcre2_regexec(const regex_t *preg, const char *string,
                  size_t nmatch, regmatch_t pmatch[], int eflags);

size_t pcre2_regerror(int errcode, const regex_t *preg,
                      char *errbuf, size_t errbuf_size);

void pcre2_regfree(regex_t *preg);</code></pre>
<h2>Description</h2>
<p>This set of functions provides a POSIX-style API for the PCRE2 regular expression 8-bit library. There are no POSIX-style wrappers for PCRE2&#8217;s 16-bit and 32-bit libraries. See the <code>pcre2api</code> documentation for a description of PCRE2&#8217;s native API, which contains much additional functionality. </p>
<p> The functions described here are wrapper functions that ultimately call the PCRE2 native API. Their prototypes are defined in the <code>pcre2posix.h</code> header file, and they all have unique names starting with <code>pcre2_</code>. However, the <code>pcre2posix.h</code> header also contains macro definitions that convert the standard POSIX names such <code>regcomp()</code> into <code>pcre2_regcomp()</code> etc. This means that a program can use the usual POSIX names without running the risk of accidentally linking with POSIX functions from a different library. </p>
<p> On Unix-like systems the PCRE2 POSIX library is called <code>libpcre2-posix</code>, so can be accessed by adding <code>-lpcre2-posix</code> to the command for linking an application. Because the POSIX functions call the native ones, it is also necessary to add <code>-lpcre2-8</code>. </p>
<p> Although they are not defined as protypes in <code>pcre2posix.h</code>, the library does contain functions with the POSIX names <code>regcomp()</code> etc. These simply pass their arguments to the PCRE2 functions. These functions are provided for backwards compatibility with earlier versions of PCRE2, so that existing programs do not have to be recompiled. </p>
<p> Calling the header file <code>pcre2posix.h</code> avoids any conflict with other POSIX libraries. It can, of course, be renamed or aliased as <code>regex.h</code>, which is the &quot;correct&quot; name, if there is no clash. It provides two structure types, <i>regex_t</i> for compiled internal forms, and <i>regmatch_t</i> for returning captured substrings. It also defines some constants whose names start with &quot;REG_&quot;; these are used for setting options and identifying error codes.</p>
<h2>Using The Posix Functions</h2>
<p>Those POSIX option bits that can reasonably be mapped to PCRE2 native options have been implemented. In addition, the option REG_EXTENDED is defined with the value zero. This has no effect, but since programs that are written to the POSIX interface often use it, this makes it easier to slot in PCRE2 as a replacement library. Other POSIX options are not even defined. </p>
<p> There are also some options that are not defined by POSIX. These have been added at the request of users who want to make use of certain PCRE2-specific features via the POSIX calling interface or to add BSD or GNU functionality. </p>
<p> When PCRE2 is called via these functions, it is only the API that is POSIX-like in style. The syntax and semantics of the regular expressions themselves are still those of Perl, subject to the setting of various PCRE2 options, as described below. &quot;POSIX-like in style&quot; means that the API approximates to the POSIX definition; it is not fully POSIX-compatible, and in multi-unit encoding domains it is probably even less compatible. </p>
<p> The descriptions below use the actual names of the functions, but, as described above, the standard POSIX names (without the <code>pcre2_</code> prefix) may also be used.</p>
<h2>Compiling A Pattern</h2>
<p>The function <code>pcre2_regcomp()</code> is called to compile a pattern into an internal form. By default, the pattern is a C string terminated by a binary zero (but see REG_PEND below). The <i>preg</i> argument is a pointer to a <code>regex_t</code> structure that is used as a base for storing information about the compiled regular expression. (It is also used for input when REG_PEND is set.) </p>
<p> The argument <i>cflags</i> is either zero, or contains one or more of the bits defined by the following macros: </p>
<p>&nbsp;<wbr>&nbsp;REG_DOTALL </p>
<p> The PCRE2_DOTALL option is set when the regular expression is passed for compilation to the native function. Note that REG_DOTALL is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_ICASE </p>
<p> The PCRE2_CASELESS option is set when the regular expression is passed for compilation to the native function. </p>
<p>&nbsp;<wbr>&nbsp;REG_NEWLINE </p>
<p> The PCRE2_MULTILINE option is set when the regular expression is passed for compilation to the native function. Note that this does <i>not</i> mimic the defined POSIX behaviour for REG_NEWLINE (see the following section). </p>
<p>&nbsp;<wbr>&nbsp;REG_NOSPEC </p>
<p> The PCRE2_LITERAL option is set when the regular expression is passed for compilation to the native function. This disables all meta characters in the pattern, causing it to be treated as a literal string. The only other options that are allowed with REG_NOSPEC are REG_ICASE, REG_NOSUB, REG_PEND, and REG_UTF. Note that REG_NOSPEC is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_NOSUB </p>
<p> When a pattern that is compiled with this flag is passed to <code>pcre2_regexec()</code> for matching, the <i>nmatch</i> and <i>pmatch</i> arguments are ignored, and no captured strings are returned. Versions of the PCRE library prior to 10.22 used to set the PCRE2_NO_AUTO_CAPTURE compile option, but this no longer happens because it disables the use of backreferences. </p>
<p>&nbsp;<wbr>&nbsp;REG_PEND </p>
<p> If this option is set, the <code>reg_endp</code> field in the <i>preg</i> structure (which has the type const char *) must be set to point to the character beyond the end of the pattern before calling <code>pcre2_regcomp()</code>. The pattern itself may now contain binary zeros, which are treated as data characters. Without REG_PEND, a binary zero terminates the pattern and the <code>re_endp</code> field is ignored. This is a GNU extension to the POSIX standard and should be used with caution in software intended to be portable to other systems. </p>
<p>&nbsp;<wbr>&nbsp;REG_UCP </p>
<p> The PCRE2_UCP option is set when the regular expression is passed for compilation to the native function. This causes PCRE2 to use Unicode properties when matchine \d, \w, etc., instead of just recognizing ASCII values. Note that REG_UCP is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_UNGREEDY </p>
<p> The PCRE2_UNGREEDY option is set when the regular expression is passed for compilation to the native function. Note that REG_UNGREEDY is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_UTF </p>
<p> The PCRE2_UTF option is set when the regular expression is passed for compilation to the native function. This causes the pattern itself and all data strings used for matching it to be treated as UTF-8 strings. Note that REG_UTF is not part of the POSIX standard. </p>
<p> In the absence of these flags, no options are passed to the native function. This means the the regex is compiled with PCRE2 default semantics. In particular, the way it handles newline characters in the subject string is the Perl way, not the POSIX way. Note that setting PCRE2_MULTILINE has only <i>some</i> of the effects specified for REG_NEWLINE. It does not affect the way newlines are matched by the dot metacharacter (they are not) or by a negative class such as [^a] (they are). </p>
<p> The yield of <code>pcre2_regcomp()</code> is zero on success, and non-zero otherwise. The <i>preg</i> structure is filled in on success, and one other member of the structure (as well as <i>re_endp</i>) is public: <i>re_nsub</i> contains the number of capturing subpatterns in the regular expression. Various error codes are defined in the header file. </p>
<p> NOTE: If the yield of <code>pcre2_regcomp()</code> is non-zero, you must not attempt to use the contents of the <i>preg</i> structure. If, for example, you pass it to <code>pcre2_regexec()</code>, the result is undefined and your program is likely to crash.</p>
<h2>Matching Newline Characters</h2>
<p>This area is not simple, because POSIX and Perl take different views of things. It is not possible to get PCRE2 to obey POSIX semantics, but then PCRE2 was never intended to be a POSIX engine. The following table lists the different possibilities for matching newline characters in Perl and PCRE2: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default&nbsp;<wbr>&nbsp;<wbr>&nbsp;Change with </p>
<p>&nbsp;<wbr>&nbsp;. matches newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_DOTALL<br />
&nbsp;<wbr>&nbsp;newline matches&nbsp;[^a]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not changeable<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 at end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_DOLLAR_ENDONLY<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_MULTILINE<br />
&nbsp;<wbr>&nbsp;^&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2_MULTILINE </p>
<p> This is the equivalent table for a POSIX-compatible pattern matcher: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default&nbsp;<wbr>&nbsp;<wbr>&nbsp;Change with </p>
<p>&nbsp;<wbr>&nbsp;. matches newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;newline matches&nbsp;[^a]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 at end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;^&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE </p>
<p> This behaviour is not what happens when PCRE2 is called via its POSIX API. By default, PCRE2&#8217;s behaviour is the same as Perl&#8217;s, except that there is no equivalent for PCRE2_DOLLAR_ENDONLY in Perl. In both PCRE2 and Perl, there is no way to stop newline from matching [^a]. </p>
<p> Default POSIX newline handling can be obtained by setting PCRE2_DOTALL and PCRE2_DOLLAR_ENDONLY when calling <code>pcre2_compile()</code> directly, but there is no way to make PCRE2 behave exactly as for the REG_NEWLINE action. When using the POSIX API, passing REG_NEWLINE to PCRE2&#8217;s <code>pcre2_regcomp()</code> function causes PCRE2_MULTILINE to be passed to <code>pcre2_compile()</code>, and REG_DOTALL passes PCRE2_DOTALL. There is no way to pass PCRE2_DOLLAR_ENDONLY.</p>
<h2>Matching A Pattern</h2>
<p>The function <code>pcre2_regexec()</code> is called to match a compiled pattern <i>preg</i> against a given <i>string</i>, which is by default terminated by a zero byte (but see REG_STARTEND below), subject to the options in <i>eflags</i>. These can be: </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTBOL </p>
<p> The PCRE2_NOTBOL option is set when calling the underlying PCRE2 matching function. </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTEMPTY </p>
<p> The PCRE2_NOTEMPTY option is set when calling the underlying PCRE2 matching function. Note that REG_NOTEMPTY is not part of the POSIX standard. However, setting this option can give more POSIX-like behaviour in some situations. </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTEOL </p>
<p> The PCRE2_NOTEOL option is set when calling the underlying PCRE2 matching function. </p>
<p>&nbsp;<wbr>&nbsp;REG_STARTEND </p>
<p> When this option is set, the subject string starts at <i>string</i> + <i>pmatch[0].rm_so</i> and ends at <i>string</i> + <i>pmatch[0].rm_eo</i>, which should point to the first character beyond the string. There may be binary zeros within the subject string, and indeed, using REG_STARTEND is the only way to pass a subject string that contains a binary zero. </p>
<p> Whatever the value of <i>pmatch[0].rm_so</i>, the offsets of the matched string and any captured substrings are still given relative to the start of <i>string</i> itself. (Before PCRE2 release 10.30 these were given relative to <i>string</i> + <i>pmatch[0].rm_so</i>, but this differs from other implementations.) </p>
<p> This is a BSD extension, compatible with but not specified by IEEE Standard 1003.2 (POSIX.2), and should be used with caution in software intended to be portable to other systems. Note that a non-zero <i>rm_so</i> does not imply REG_NOTBOL; REG_STARTEND affects only the location and length of the string, not how it is matched. Setting REG_STARTEND and passing <i>pmatch</i> as NULL are mutually exclusive; the error REG_INVARG is returned. </p>
<p> If the pattern was compiled with the REG_NOSUB flag, no data about any matched strings is returned. The <i>nmatch</i> and <i>pmatch</i> arguments of <code>pcre2_regexec()</code> are ignored (except possibly as input for REG_STARTEND). </p>
<p> The value of <i>nmatch</i> may be zero, and the value <i>pmatch</i> may be NULL (unless REG_STARTEND is set); in both these cases no data about any matched strings is returned. </p>
<p> Otherwise, the portion of the string that was matched, and also any captured substrings, are returned via the <i>pmatch</i> argument, which points to an array of <i>nmatch</i> structures of type <i>regmatch_t</i>, containing the members <i>rm_so</i> and <i>rm_eo</i>. These contain the byte offset to the first character of each substring and the offset to the first character after the end of each substring, respectively. The 0th element of the vector relates to the entire portion of <i>string</i> that was matched; subsequent elements relate to the capturing subpatterns of the regular expression. Unused entries in the array have both structure members set to -1. </p>
<p> A successful match yields a zero return; various error codes are defined in the header file, of which REG_NOMATCH is the &quot;expected&quot; failure code.</p>
<h2>Error Messages</h2>
<p>The <code>pcre2_regerror()</code> function maps a non-zero errorcode from either <code>pcre2_regcomp()</code> or <code>pcre2_regexec()</code> to a printable message. If <i>preg</i> is not NULL, the error should have arisen from the use of that structure. A message terminated by a binary zero is placed in <i>errbuf</i>. If the buffer is too short, only the first <i>errbuf_size</i> &#8211; 1 characters of the error message are used. The yield of the function is the size of buffer needed to hold the whole message, including the terminating zero. This value is greater than <i>errbuf_size</i> if the message was truncated.</p>
<h2>Memory Usage</h2>
<p>Compiling a regular expression causes memory to be allocated and associated with the <i>preg</i> structure. The function <code>pcre2_regfree()</code> frees all such memory, after which <i>preg</i> may no longer be used as a compiled expression.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 30 January 2019
Copyright (c) 1997-2019 University of Cambridge.</pre>
