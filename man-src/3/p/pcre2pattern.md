---
title: "pcre2pattern(3)"
name: "pcre2pattern"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2pattern/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Pcre2 Regular Expression Details</h2>
<p>The syntax and semantics of the regular expressions that are supported by PCRE2 are described in detail below. There is a quick-reference syntax summary in the <code>pcre2syntax</code> page. PCRE2 tries to match Perl syntax and semantics as closely as it can. PCRE2 also supports some alternative regular expression syntax (which does not conflict with the Perl syntax) in order to provide some compatibility with regular expressions in Python, .NET, and Oniguruma. </p>
<p> Perl&#8217;s regular expressions are described in its own documentation, and regular expressions in general are covered in a number of books, some of which have copious examples. Jeffrey Friedl&#8217;s &quot;Mastering Regular Expressions&quot;, published by O&#8217;Reilly, covers regular expressions in great detail. This description of PCRE2&#8217;s regular expressions is intended as reference material. </p>
<p> This document discusses the regular expression patterns that are supported by PCRE2 when its main matching function, <code>pcre2_match()</code>, is used. PCRE2 also has an alternative matching function, <code>pcre2_dfa_match()</code>, which matches using a different algorithm that is not Perl-compatible. Some of the features discussed below are not available when DFA matching is used. The advantages and disadvantages of the alternative function, and how it differs from the normal function, are discussed in the <code>pcre2matching</code> page.</p>
<h2>Special Start-Of-Pattern Items</h2>
<p>A number of options that can be passed to <code>pcre2_compile()</code> can also be set by special items at the start of a pattern. These are not Perl-compatible, but are provided to make these options accessible to pattern writers who are not able to change the program that processes the pattern. Any number of these items may appear, but they must all be together right at the start of the pattern string, and the letters must be in upper case.</p>
<h3>UTF support</h3>
<p>In the 8-bit and 16-bit PCRE2 libraries, characters may be coded either as single code units, or as multiple UTF-8 or UTF-16 code units. UTF-32 can be specified for the 32-bit library, in which case it constrains the character values to valid Unicode code points. To process UTF strings, PCRE2 must be built to include Unicode support (which is the default). When using UTF strings you must either call the compiling function with one or both of the PCRE2_UTF or PCRE2_MATCH_INVALID_UTF options, or the pattern must start with the special sequence (*UTF), which is equivalent to setting the relevant PCRE2_UTF. How setting a UTF mode affects pattern matching is mentioned in several places below. There is also a summary of features in the <code>pcre2unicode</code> page. </p>
<p> Some applications that allow their users to supply patterns may wish to restrict them to non-UTF data for security reasons. If the PCRE2_NEVER_UTF option is passed to <code>pcre2_compile()</code>, (*UTF) is not allowed, and its appearance in a pattern causes an error.</p>
<h3>Unicode property support</h3>
<p>Another special sequence that may appear at the start of a pattern is (*UCP). This has the same effect as setting the PCRE2_UCP option: it causes sequences such as \d and \w to use Unicode properties to determine character types, instead of recognizing only characters with codes less than 256 via a lookup table. </p>
<p> Some applications that allow their users to supply patterns may wish to restrict them for security reasons. If the PCRE2_NEVER_UCP option is passed to <code>pcre2_compile()</code>, (*UCP) is not allowed, and its appearance in a pattern causes an error.</p>
<h3>Locking out empty string matching</h3>
<p>Starting a pattern with (*NOTEMPTY) or (*NOTEMPTY_ATSTART) has the same effect as passing the PCRE2_NOTEMPTY or PCRE2_NOTEMPTY_ATSTART option to whichever matching function is subsequently called to match the pattern. These options lock out the matching of empty strings, either entirely, or only at the start of the subject.</p>
<h3>Disabling auto-possessification</h3>
<p>If a pattern starts with (*NO_AUTO_POSSESS), it has the same effect as setting the PCRE2_NO_AUTO_POSSESS option. This stops PCRE2 from making quantifiers possessive when what follows cannot match the repeated item. For example, by default a+b is treated as a++b. For more details, see the <code>pcre2api</code> documentation.</p>
<h3>Disabling start-up optimizations</h3>
<p>If a pattern starts with (*NO_START_OPT), it has the same effect as setting the PCRE2_NO_START_OPTIMIZE option. This disables several optimizations for quickly reaching &quot;no match&quot; results. For more details, see the <code>pcre2api</code> documentation.</p>
<h3>Disabling automatic anchoring</h3>
<p>If a pattern starts with (*NO_DOTSTAR_ANCHOR), it has the same effect as setting the PCRE2_NO_DOTSTAR_ANCHOR option. This disables optimizations that apply to patterns whose top-level branches all start with .* (match any number of arbitrary characters). For more details, see the <code>pcre2api</code> documentation.</p>
<h3>Disabling JIT compilation</h3>
<p>If a pattern that starts with (*NO_JIT) is successfully compiled, an attempt by the application to apply the JIT optimization by calling <code>pcre2_jit_compile()</code> is ignored.</p>
<h3>Setting match resource limits</h3>
<p>The <code>pcre2_match()</code> function contains a counter that is incremented every time it goes round its main loop. The caller of <code>pcre2_match()</code> can set a limit on this counter, which therefore limits the amount of computing resource used for a match. The maximum depth of nested backtracking can also be limited; this indirectly restricts the amount of heap memory that is used, but there is also an explicit memory limit that can be set. </p>
<p> These facilities are provided to catch runaway matches that are provoked by patterns with huge matching trees. A common example is a pattern with nested unlimited repeats applied to a long string that does not match. When one of these limits is reached, <code>pcre2_match()</code> gives an error return. The limits can also be set by items at the start of the pattern of the form </p>
<p>&nbsp;<wbr>&nbsp;(*LIMIT_HEAP=d)<br />
&nbsp;<wbr>&nbsp;(*LIMIT_MATCH=d)<br />
&nbsp;<wbr>&nbsp;(*LIMIT_DEPTH=d) </p>
<p> where d is any number of decimal digits. However, the value of the setting must be less than the value set (or defaulted) by the caller of <code>pcre2_match()</code> for it to have any effect. In other words, the pattern writer can lower the limits set by the programmer, but not raise them. If there is more than one setting of one of these limits, the lower value is used. The heap limit is specified in kibibytes (units of 1024 bytes). </p>
<p> Prior to release 10.30, LIMIT_DEPTH was called LIMIT_RECURSION. This name is still recognized for backwards compatibility. </p>
<p> The heap limit applies only when the <code>pcre2_match()</code> or <code>pcre2_dfa_match()</code> interpreters are used for matching. It does not apply to JIT. The match limit is used (but in a different way) when JIT is being used, or when <code>pcre2_dfa_match()</code> is called, to limit computing resource usage by those matching functions. The depth limit is ignored by JIT but is relevant for DFA matching, which uses function recursion for recursions within the pattern and for lookaround assertions and atomic groups. In this case, the depth limit controls the depth of such recursion.</p>
<h3>Newline conventions</h3>
<p>PCRE2 supports six different conventions for indicating line breaks in strings: a single CR (carriage return) character, a single LF (linefeed) character, the two-character sequence CRLF, any of the three preceding, any Unicode newline sequence, or the NUL character (binary zero). The <code>pcre2api</code> page has further discussion about newlines, and shows how to set the newline convention when calling <code>pcre2_compile()</code>. </p>
<p> It is also possible to specify a newline convention by starting a pattern string with one of the following sequences: </p>
<p>&nbsp;<wbr>&nbsp;(*CR)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return<br />
&nbsp;<wbr>&nbsp;(*LF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linefeed<br />
&nbsp;<wbr>&nbsp;(*CRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return, followed by linefeed<br />
&nbsp;<wbr>&nbsp;(*ANYCRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;any of the three above<br />
&nbsp;<wbr>&nbsp;(*ANY)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;all Unicode newline sequences<br />
&nbsp;<wbr>&nbsp;(*NUL)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the NUL character&nbsp;(binary zero) </p>
<p> These override the default and the options given to the compiling function. For example, on a Unix system where LF is the default newline sequence, the pattern </p>
<p>&nbsp;<wbr>&nbsp;(*CR)a.b </p>
<p> changes the convention to CR. That pattern matches &quot;a
b&quot; because LF is no longer a newline. If more than one of these settings is present, the last one is used. </p>
<p> The newline convention affects where the circumflex and dollar assertions are true. It also affects the interpretation of the dot metacharacter when PCRE2_DOTALL is not set, and the behaviour of \N when not followed by an opening brace. However, it does not affect what the \R escape sequence matches. By default, this is any Unicode newline sequence, for Perl compatibility. However, this can be changed; see the next section and the description of \R in the section entitled &quot;Newline sequences&quot; below. A change of \R setting can be combined with a change of newline convention.</p>
<h3>Specifying what \R matches</h3>
<p>It is possible to restrict \R to match only CR, LF, or CRLF (instead of the complete set of Unicode line endings) by setting the option PCRE2_BSR_ANYCRLF at compile time. This effect can also be achieved by starting a pattern with (*BSR_ANYCRLF). For completeness, (*BSR_UNICODE) is also recognized, corresponding to PCRE2_BSR_UNICODE.</p>
<h2>Ebcdic Character Codes</h2>
<p>PCRE2 can be compiled to run in an environment that uses EBCDIC as its character code instead of ASCII or Unicode (typically a mainframe system). In the sections below, character code values are ASCII or Unicode; in an EBCDIC environment these characters may have different code values, and there are no code points greater than 255.</p>
<h2>Characters And Metacharacters</h2>
<p>A regular expression is a pattern that is matched against a subject string from left to right. Most characters stand for themselves in a pattern, and match the corresponding characters in the subject. As a trivial example, the pattern </p>
<p>&nbsp;<wbr>&nbsp;The quick brown fox </p>
<p> matches a portion of a subject string that is identical to itself. When caseless matching is specified (the PCRE2_CASELESS option), letters are matched independently of case. </p>
<p> The power of regular expressions comes from the ability to include wild cards, character classes, alternatives, and repetitions in the pattern. These are encoded in the pattern by the use of <i>metacharacters</i>, which do not stand for themselves but instead are interpreted in some special way. </p>
<p> There are two different sets of metacharacters: those that are recognized anywhere in the pattern except within square brackets, and those that are recognized within square brackets. Outside square brackets, the metacharacters are as follows: </p>
<p>&nbsp;<wbr>&nbsp;\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;general escape character with several uses<br />
&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert start of string&nbsp;(or line, in multiline mode)<br />
&nbsp;<wbr>&nbsp;$&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert end of string&nbsp;(or line, in multiline mode)<br />
&nbsp;<wbr>&nbsp;.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match any character except newline&nbsp;(by default)<br />
&nbsp;<wbr>&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start character class definition<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start of alternative branch<br />
&nbsp;<wbr>&nbsp;(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start group or control verb<br />
&nbsp;<wbr>&nbsp;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end group or control verb<br />
&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or more quantifier<br />
&nbsp;<wbr>&nbsp;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 or more quantifier;&nbsp;also&nbsp;&quot;possessive quantifier&quot;<br />
&nbsp;<wbr>&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or 1 quantifier;&nbsp;also quantifier minimizer<br />
&nbsp;<wbr>&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start min/max quantifier </p>
<p> Part of a pattern that is in square brackets is called a &quot;character class&quot;. In a character class the only metacharacters are: </p>
<p>&nbsp;<wbr>&nbsp;\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;general escape character<br />
&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negate the class, but only if the first character<br />
&nbsp;<wbr>&nbsp;&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates character range<br />
&nbsp;<wbr>&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX character class&nbsp;(if followed by POSIX syntax)<br />
&nbsp;<wbr>&nbsp;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;terminates the character class </p>
<p> The following sections describe the use of each of the metacharacters.</p>
<h2>Backslash</h2>
<p>The backslash character has several uses. Firstly, if it is followed by a character that is not a digit or a letter, it takes away any special meaning that character may have. This use of backslash as an escape character applies both inside and outside character classes. </p>
<p> For example, if you want to match a * character, you must write \* in the pattern. This escaping action applies whether or not the following character would otherwise be interpreted as a metacharacter, so it is always safe to precede a non-alphanumeric with backslash to specify that it stands for itself. In particular, if you want to match a backslash, you write \. </p>
<p> In a UTF mode, only ASCII digits and letters have any special meaning after a backslash. All other characters (in particular, those whose code points are greater than 127) are treated as literals. </p>
<p> If a pattern is compiled with the PCRE2_EXTENDED option, most white space in the pattern (other than in a character class), and characters between a # outside a character class and the next newline, inclusive, are ignored. An escaping backslash can be used to include a white space or # character as part of the pattern. </p>
<p> If you want to treat all characters in a sequence as literals, you can do so by putting them between \Q and \E. This is different from Perl in that $ and @ are handled as literals in \Q&#8230;\E sequences in PCRE2, whereas in Perl, $ and @ cause variable interpolation. Also, Perl does &quot;double-quotish backslash interpolation&quot; on any backslashes between \Q and \E which, its documentation says, &quot;may lead to confusing results&quot;. PCRE2 treats a backslash between \Q and \E just like any other character. Note the following examples: </p>
<p>&nbsp;<wbr>&nbsp;Pattern&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE2 matches&nbsp;<wbr>&nbsp;<wbr>&nbsp;Perl matches </p>
<p>&nbsp;<wbr>&nbsp;\Qabc$xyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc followed by the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;contents of&nbsp;$xyz<br />
&nbsp;<wbr>&nbsp;\Qabc\$xyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc\$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc\$xyz<br />
&nbsp;<wbr>&nbsp;\Qabc\E\$\Qxyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz<br />
&nbsp;<wbr>&nbsp;\QA\B\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A\B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A\B<br />
&nbsp;<wbr>&nbsp;\Q\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\E </p>
<p> The \Q&#8230;\E sequence is recognized both inside and outside character classes. An isolated \E that is not preceded by \Q is ignored. If \Q is not followed by \E later in the pattern, the literal interpretation continues to the end of the pattern (that is, \E is assumed at the end). If the isolated \Q is inside a character class, this causes an error, because the character class is not terminated by a closing square bracket.</p>
<h3>Non-printing characters</h3>
<p>A second use of backslash provides a way of encoding non-printing characters in patterns in a visible manner. There is no restriction on the appearance of non-printing characters in a pattern, but when a pattern is being prepared by text editing, it is often easier to use one of the following escape sequences instead of the binary character it represents. In an ASCII or Unicode environment, these escapes are as follows: </p>
<p>&nbsp;<wbr>&nbsp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alarm, that is, the BEL character&nbsp;(hex 07)<br />
&nbsp;<wbr>&nbsp;
