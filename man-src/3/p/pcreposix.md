---
title: "pcreposix(3)"
name: "pcreposix"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcreposix/"
description: "PCRE – Perl-compatible regular expressions."
---

<p>PCRE &#8211; Perl-compatible regular expressions.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcreposix.h&gt;
int regcomp(regex_t *preg, const char *pattern,
            int cflags);

int regexec(regex_t *preg, const char *string,
            size_t nmatch, regmatch_t pmatch[], int eflags);
size_t regerror(int errcode, const regex_t *preg,
                char *errbuf, size_t errbuf_size);

void regfree(regex_t *preg);</code></pre>
<h2>Description</h2>
<p>This set of functions provides a POSIX-style API for the PCRE regular expression 8-bit library. See the <code>pcreapi</code> documentation for a description of PCRE&#8217;s native API, which contains much additional functionality. There is no POSIX-style wrapper for PCRE&#8217;s 16-bit and 32-bit library. </p>
<p> The functions described here are just wrapper functions that ultimately call the PCRE native API. Their prototypes are defined in the <code>pcreposix.h</code> header file, and on Unix systems the library itself is called <code>pcreposix.a</code>, so can be accessed by adding <code>-lpcreposix</code> to the command for linking an application that uses them. Because the POSIX functions call the native ones, it is also necessary to add <code>-lpcre</code>. </p>
<p> I have implemented only those POSIX option bits that can be reasonably mapped to PCRE native options. In addition, the option REG_EXTENDED is defined with the value zero. This has no effect, but since programs that are written to the POSIX interface often use it, this makes it easier to slot in PCRE as a replacement library. Other POSIX options are not even defined. </p>
<p> There are also some other options that are not defined by POSIX. These have been added at the request of users who want to make use of certain PCRE-specific features via the POSIX calling interface. </p>
<p> When PCRE is called via these functions, it is only the API that is POSIX-like in style. The syntax and semantics of the regular expressions themselves are still those of Perl, subject to the setting of various PCRE options, as described below. &quot;POSIX-like in style&quot; means that the API approximates to the POSIX definition; it is not fully POSIX-compatible, and in multi-byte encoding domains it is probably even less compatible. </p>
<p> The header for these functions is supplied as <code>pcreposix.h</code> to avoid any potential clash with other POSIX libraries. It can, of course, be renamed or aliased as <code>regex.h</code>, which is the &quot;correct&quot; name. It provides two structure types, <i>regex_t</i> for compiled internal forms, and <i>regmatch_t</i> for returning captured substrings. It also defines some constants whose names start with &quot;REG_&quot;; these are used for setting options and identifying error codes.</p>
<h2>Compiling A Pattern</h2>
<p>The function <code>regcomp()</code> is called to compile a pattern into an internal form. The pattern is a C string terminated by a binary zero, and is passed in the argument <i>pattern</i>. The <i>preg</i> argument is a pointer to a <code>regex_t</code> structure that is used as a base for storing information about the compiled regular expression. </p>
<p> The argument <i>cflags</i> is either zero, or contains one or more of the bits defined by the following macros: </p>
<p>&nbsp;<wbr>&nbsp;REG_DOTALL </p>
<p> The PCRE_DOTALL option is set when the regular expression is passed for compilation to the native function. Note that REG_DOTALL is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_ICASE </p>
<p> The PCRE_CASELESS option is set when the regular expression is passed for compilation to the native function. </p>
<p>&nbsp;<wbr>&nbsp;REG_NEWLINE </p>
<p> The PCRE_MULTILINE option is set when the regular expression is passed for compilation to the native function. Note that this does <i>not</i> mimic the defined POSIX behaviour for REG_NEWLINE (see the following section). </p>
<p>&nbsp;<wbr>&nbsp;REG_NOSUB </p>
<p> The PCRE_NO_AUTO_CAPTURE option is set when the regular expression is passed for compilation to the native function. In addition, when a pattern that is compiled with this flag is passed to <code>regexec()</code> for matching, the <i>nmatch</i> and <i>pmatch</i> arguments are ignored, and no captured strings are returned. </p>
<p>&nbsp;<wbr>&nbsp;REG_UCP </p>
<p> The PCRE_UCP option is set when the regular expression is passed for compilation to the native function. This causes PCRE to use Unicode properties when matchine \d, \w, etc., instead of just recognizing ASCII values. Note that REG_UTF8 is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_UNGREEDY </p>
<p> The PCRE_UNGREEDY option is set when the regular expression is passed for compilation to the native function. Note that REG_UNGREEDY is not part of the POSIX standard. </p>
<p>&nbsp;<wbr>&nbsp;REG_UTF8 </p>
<p> The PCRE_UTF8 option is set when the regular expression is passed for compilation to the native function. This causes the pattern itself and all data strings used for matching it to be treated as UTF-8 strings. Note that REG_UTF8 is not part of the POSIX standard. </p>
<p> In the absence of these flags, no options are passed to the native function. This means the the regex is compiled with PCRE default semantics. In particular, the way it handles newline characters in the subject string is the Perl way, not the POSIX way. Note that setting PCRE_MULTILINE has only <i>some</i> of the effects specified for REG_NEWLINE. It does not affect the way newlines are matched by . (they are not) or by a negative class such as [^a] (they are). </p>
<p> The yield of <code>regcomp()</code> is zero on success, and non-zero otherwise. The <i>preg</i> structure is filled in on success, and one member of the structure is public: <i>re_nsub</i> contains the number of capturing subpatterns in the regular expression. Various error codes are defined in the header file. </p>
<p> NOTE: If the yield of <code>regcomp()</code> is non-zero, you must not attempt to use the contents of the <i>preg</i> structure. If, for example, you pass it to <code>regexec()</code>, the result is undefined and your program is likely to crash.</p>
<h2>Matching Newline Characters</h2>
<p>This area is not simple, because POSIX and Perl take different views of things. It is not possible to get PCRE to obey POSIX semantics, but then PCRE was never intended to be a POSIX engine. The following table lists the different possibilities for matching newline characters in PCRE: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default&nbsp;<wbr>&nbsp;<wbr>&nbsp;Change with </p>
<p>&nbsp;<wbr>&nbsp;. matches newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_DOTALL<br />
&nbsp;<wbr>&nbsp;newline matches&nbsp;[^a]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;not changeable<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 at end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_DOLLARENDONLY<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_MULTILINE<br />
&nbsp;<wbr>&nbsp;^&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE_MULTILINE </p>
<p> This is the equivalent table for POSIX: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Default&nbsp;<wbr>&nbsp;<wbr>&nbsp;Change with </p>
<p>&nbsp;<wbr>&nbsp;. matches newline&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;newline matches&nbsp;[^a]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;yes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 at end&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;$&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE<br />
&nbsp;<wbr>&nbsp;^&nbsp;matches&nbsp;
 in middle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;REG_NEWLINE </p>
<p> PCRE&#8217;s behaviour is the same as Perl&#8217;s, except that there is no equivalent for PCRE_DOLLAR_ENDONLY in Perl. In both PCRE and Perl, there is no way to stop newline from matching [^a]. </p>
<p> The default POSIX newline handling can be obtained by setting PCRE_DOTALL and PCRE_DOLLAR_ENDONLY, but there is no way to make PCRE behave exactly as for the REG_NEWLINE action.</p>
<h2>Matching A Pattern</h2>
<p>The function <code>regexec()</code> is called to match a compiled pattern <i>preg</i> against a given <i>string</i>, which is by default terminated by a zero byte (but see REG_STARTEND below), subject to the options in <i>eflags</i>. These can be: </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTBOL </p>
<p> The PCRE_NOTBOL option is set when calling the underlying PCRE matching function. </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTEMPTY </p>
<p> The PCRE_NOTEMPTY option is set when calling the underlying PCRE matching function. Note that REG_NOTEMPTY is not part of the POSIX standard. However, setting this option can give more POSIX-like behaviour in some situations. </p>
<p>&nbsp;<wbr>&nbsp;REG_NOTEOL </p>
<p> The PCRE_NOTEOL option is set when calling the underlying PCRE matching function. </p>
<p>&nbsp;<wbr>&nbsp;REG_STARTEND </p>
<p> The string is considered to start at <i>string</i> + <i>pmatch[0].rm_so</i> and to have a terminating NUL located at <i>string</i> + <i>pmatch[0].rm_eo</i> (there need not actually be a NUL at that location), regardless of the value of <i>nmatch</i>. This is a BSD extension, compatible with but not specified by IEEE Standard 1003.2 (POSIX.2), and should be used with caution in software intended to be portable to other systems. Note that a non-zero <i>rm_so</i> does not imply REG_NOTBOL; REG_STARTEND affects only the location of the string, not how it is matched. </p>
<p> If the pattern was compiled with the REG_NOSUB flag, no data about any matched strings is returned. The <i>nmatch</i> and <i>pmatch</i> arguments of <code>regexec()</code> are ignored. </p>
<p> If the value of <i>nmatch</i> is zero, or if the value <i>pmatch</i> is NULL, no data about any matched strings is returned. </p>
<p> Otherwise,the portion of the string that was matched, and also any captured substrings, are returned via the <i>pmatch</i> argument, which points to an array of <i>nmatch</i> structures of type <i>regmatch_t</i>, containing the members <i>rm_so</i> and <i>rm_eo</i>. These contain the offset to the first character of each substring and the offset to the first character after the end of each substring, respectively. The 0th element of the vector relates to the entire portion of <i>string</i> that was matched; subsequent elements relate to the capturing subpatterns of the regular expression. Unused entries in the array have both structure members set to -1. </p>
<p> A successful match yields a zero return; various error codes are defined in the header file, of which REG_NOMATCH is the &quot;expected&quot; failure code.</p>
<h2>Error Messages</h2>
<p>The <code>regerror()</code> function maps a non-zero errorcode from either <code>regcomp()</code> or <code>regexec()</code> to a printable message. If <i>preg</i> is not NULL, the error should have arisen from the use of that structure. A message terminated by a binary zero is placed in <i>errbuf</i>. The length of the message, including the zero, is limited to <i>errbuf_size</i>. The yield of the function is the size of buffer needed to hold the whole message.</p>
<h2>Memory Usage</h2>
<p>Compiling a regular expression causes memory to be allocated and associated with the <i>preg</i> structure. The function <code>regfree()</code> frees all such memory, after which <i>preg</i> may no longer be used as a compiled expression.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 09 January 2012
Copyright (c) 1997-2012 University of Cambridge.</pre>
