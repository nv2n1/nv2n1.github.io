---
title: "pcrepattern(3)"
name: "pcrepattern"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrepattern/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Pcre Regular Expression Details</h2>
<p>The syntax and semantics of the regular expressions that are supported by PCRE are described in detail below. There is a quick-reference syntax summary in the <code>pcresyntax</code> page. PCRE tries to match Perl syntax and semantics as closely as it can. PCRE also supports some alternative regular expression syntax (which does not conflict with the Perl syntax) in order to provide some compatibility with regular expressions in Python, .NET, and Oniguruma. </p>
<p> Perl&#8217;s regular expressions are described in its own documentation, and regular expressions in general are covered in a number of books, some of which have copious examples. Jeffrey Friedl&#8217;s &quot;Mastering Regular Expressions&quot;, published by O&#8217;Reilly, covers regular expressions in great detail. This description of PCRE&#8217;s regular expressions is intended as reference material. </p>
<p> This document discusses the patterns that are supported by PCRE when one its main matching functions, <code>pcre_exec()</code> (8-bit) or <code>pcre[16|32]_exec()</code> (16- or 32-bit), is used. PCRE also has alternative matching functions, <code>pcre_dfa_exec()</code> and <code>pcre[16|32_dfa_exec()</code>, which match using a different algorithm that is not Perl-compatible. Some of the features discussed below are not available when DFA matching is used. The advantages and disadvantages of the alternative functions, and how they differ from the normal functions, are discussed in the <code>pcrematching</code> page.</p>
<h2>Special Start-Of-Pattern Items</h2>
<p>A number of options that can be passed to <code>pcre_compile()</code> can also be set by special items at the start of a pattern. These are not Perl-compatible, but are provided to make these options accessible to pattern writers who are not able to change the program that processes the pattern. Any number of these items may appear, but they must all be together right at the start of the pattern string, and the letters must be in upper case.</p>
<h3>UTF support</h3>
<p>The original operation of PCRE was on strings of one-byte characters. However, there is now also support for UTF-8 strings in the original library, an extra library that supports 16-bit and UTF-16 character strings, and a third library that supports 32-bit and UTF-32 character strings. To use these features, PCRE must be built to include appropriate support. When using UTF strings you must either call the compiling function with the PCRE_UTF8, PCRE_UTF16, or PCRE_UTF32 option, or the pattern must start with one of these special sequences: </p>
<p>&nbsp;<wbr>&nbsp;(*UTF8)<br />
&nbsp;<wbr>&nbsp;(*UTF16)<br />
&nbsp;<wbr>&nbsp;(*UTF32)<br />
&nbsp;<wbr>&nbsp;(*UTF) </p>
<p> (*UTF) is a generic sequence that can be used with any of the libraries. Starting a pattern with such a sequence is equivalent to setting the relevant option. How setting a UTF mode affects pattern matching is mentioned in several places below. There is also a summary of features in the <code>pcreunicode</code> page. </p>
<p> Some applications that allow their users to supply patterns may wish to restrict them to non-UTF data for security reasons. If the PCRE_NEVER_UTF option is set at compile time, (*UTF) etc. are not allowed, and their appearance causes an error.</p>
<h3>Unicode property support</h3>
<p>Another special sequence that may appear at the start of a pattern is (*UCP). This has the same effect as setting the PCRE_UCP option: it causes sequences such as \d and \w to use Unicode properties to determine character types, instead of recognizing only characters with codes less than 128 via a lookup table.</p>
<h3>Disabling auto-possessification</h3>
<p>If a pattern starts with (*NO_AUTO_POSSESS), it has the same effect as setting the PCRE_NO_AUTO_POSSESS option at compile time. This stops PCRE from making quantifiers possessive when what follows cannot match the repeated item. For example, by default a+b is treated as a++b. For more details, see the <code>pcreapi</code> documentation.</p>
<h3>Disabling start-up optimizations</h3>
<p>If a pattern starts with (*NO_START_OPT), it has the same effect as setting the PCRE_NO_START_OPTIMIZE option either at compile or matching time. This disables several optimizations for quickly reaching &quot;no match&quot; results. For more details, see the <code>pcreapi</code> documentation.</p>
<h3>Newline conventions</h3>
<p>PCRE supports five different conventions for indicating line breaks in strings: a single CR (carriage return) character, a single LF (linefeed) character, the two-character sequence CRLF, any of the three preceding, or any Unicode newline sequence. The <code>pcreapi</code> page has further discussion about newlines, and shows how to set the newline convention in the <i>options</i> arguments for the compiling and matching functions. </p>
<p> It is also possible to specify a newline convention by starting a pattern string with one of the following five sequences: </p>
<p>&nbsp;<wbr>&nbsp;(*CR)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return<br />
&nbsp;<wbr>&nbsp;(*LF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;linefeed<br />
&nbsp;<wbr>&nbsp;(*CRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;carriage return, followed by linefeed<br />
&nbsp;<wbr>&nbsp;(*ANYCRLF)&nbsp;<wbr>&nbsp;<wbr>&nbsp;any of the three above<br />
&nbsp;<wbr>&nbsp;(*ANY)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;all Unicode newline sequences </p>
<p> These override the default and the options given to the compiling function. For example, on a Unix system where LF is the default newline sequence, the pattern </p>
<p>&nbsp;<wbr>&nbsp;(*CR)a.b </p>
<p> changes the convention to CR. That pattern matches &quot;a
b&quot; because LF is no longer a newline. If more than one of these settings is present, the last one is used. </p>
<p> The newline convention affects where the circumflex and dollar assertions are true. It also affects the interpretation of the dot metacharacter when PCRE_DOTALL is not set, and the behaviour of \N. However, it does not affect what the \R escape sequence matches. By default, this is any Unicode newline sequence, for Perl compatibility. However, this can be changed; see the description of \R in the section entitled &quot;Newline sequences&quot; below. A change of \R setting can be combined with a change of newline convention.</p>
<h3>Setting match and recursion limits</h3>
<p>The caller of <code>pcre_exec()</code> can set a limit on the number of times the internal <code>match()</code> function is called and on the maximum depth of recursive calls. These facilities are provided to catch runaway matches that are provoked by patterns with huge matching trees (a typical example is a pattern with nested unlimited repeats) and to avoid running out of system stack by too much recursion. When one of these limits is reached, <code>pcre_exec()</code> gives an error return. The limits can also be set by items at the start of the pattern of the form </p>
<p>&nbsp;<wbr>&nbsp;(*LIMIT_MATCH=d)<br />
&nbsp;<wbr>&nbsp;(*LIMIT_RECURSION=d) </p>
<p> where d is any number of decimal digits. However, the value of the setting must be less than the value set (or defaulted) by the caller of <code>pcre_exec()</code> for it to have any effect. In other words, the pattern writer can lower the limits set by the programmer, but not raise them. If there is more than one setting of one of these limits, the lower value is used.</p>
<h2>Ebcdic Character Codes</h2>
<p>PCRE can be compiled to run in an environment that uses EBCDIC as its character code rather than ASCII or Unicode (typically a mainframe system). In the sections below, character code values are ASCII or Unicode; in an EBCDIC environment these characters may have different code values, and there are no code points greater than 255.</p>
<h2>Characters And Metacharacters</h2>
<p>A regular expression is a pattern that is matched against a subject string from left to right. Most characters stand for themselves in a pattern, and match the corresponding characters in the subject. As a trivial example, the pattern </p>
<p>&nbsp;<wbr>&nbsp;The quick brown fox </p>
<p> matches a portion of a subject string that is identical to itself. When caseless matching is specified (the PCRE_CASELESS option), letters are matched independently of case. In a UTF mode, PCRE always understands the concept of case for characters whose values are less than 128, so caseless matching is always possible. For characters with higher values, the concept of case is supported if PCRE is compiled with Unicode property support, but not otherwise. If you want to use caseless matching for characters 128 and above, you must ensure that PCRE is compiled with Unicode property support as well as with UTF support. </p>
<p> The power of regular expressions comes from the ability to include alternatives and repetitions in the pattern. These are encoded in the pattern by the use of <i>metacharacters</i>, which do not stand for themselves but instead are interpreted in some special way. </p>
<p> There are two different sets of metacharacters: those that are recognized anywhere in the pattern except within square brackets, and those that are recognized within square brackets. Outside square brackets, the metacharacters are as follows: </p>
<p>&nbsp;<wbr>&nbsp;\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;general escape character with several uses<br />
&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert start of string&nbsp;(or line, in multiline mode)<br />
&nbsp;<wbr>&nbsp;$&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assert end of string&nbsp;(or line, in multiline mode)<br />
&nbsp;<wbr>&nbsp;.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match any character except newline&nbsp;(by default)<br />
&nbsp;<wbr>&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start character class definition<br />
&nbsp;<wbr>&nbsp;|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start of alternative branch<br />
&nbsp;<wbr>&nbsp;(&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start subpattern<br />
&nbsp;<wbr>&nbsp;)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;end subpattern<br />
&nbsp;<wbr>&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extends the meaning of&nbsp;(<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also 0 or 1 quantifier<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also quantifier minimizer<br />
&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 or more quantifier<br />
&nbsp;<wbr>&nbsp;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 or more quantifier<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;also&nbsp;&quot;possessive quantifier&quot;<br />
&nbsp;<wbr>&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start min/max quantifier </p>
<p> Part of a pattern that is in square brackets is called a &quot;character class&quot;. In a character class the only metacharacters are: </p>
<p>&nbsp;<wbr>&nbsp;\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;general escape character<br />
&nbsp;<wbr>&nbsp;^&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;negate the class, but only if the first character<br />
&nbsp;<wbr>&nbsp;&#8211;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;indicates character range<br />
&nbsp;<wbr>&nbsp;[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;POSIX character class&nbsp;(only if followed by POSIX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;syntax)<br />
&nbsp;<wbr>&nbsp;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;terminates the character class </p>
<p> The following sections describe the use of each of the metacharacters.</p>
<h2>Backslash</h2>
<p>The backslash character has several uses. Firstly, if it is followed by a character that is not a number or a letter, it takes away any special meaning that character may have. This use of backslash as an escape character applies both inside and outside character classes. </p>
<p> For example, if you want to match a * character, you write \* in the pattern. This escaping action applies whether or not the following character would otherwise be interpreted as a metacharacter, so it is always safe to precede a non-alphanumeric with backslash to specify that it stands for itself. In particular, if you want to match a backslash, you write \. </p>
<p> In a UTF mode, only ASCII numbers and letters have any special meaning after a backslash. All other characters (in particular, those whose codepoints are greater than 127) are treated as literals. </p>
<p> If a pattern is compiled with the PCRE_EXTENDED option, most white space in the pattern (other than in a character class), and characters between a # outside a character class and the next newline, inclusive, are ignored. An escaping backslash can be used to include a white space or # character as part of the pattern. </p>
<p> If you want to remove the special meaning from a sequence of characters, you can do so by putting them between \Q and \E. This is different from Perl in that $ and @ are handled as literals in \Q&#8230;\E sequences in PCRE, whereas in Perl, $ and @ cause variable interpolation. Note the following examples: </p>
<p>&nbsp;<wbr>&nbsp;Pattern&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;PCRE matches&nbsp;<wbr>&nbsp;<wbr>&nbsp;Perl matches </p>
<p>&nbsp;<wbr>&nbsp;\Qabc$xyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc followed by the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;contents of&nbsp;$xyz<br />
&nbsp;<wbr>&nbsp;\Qabc\$xyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc\$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc\$xyz<br />
&nbsp;<wbr>&nbsp;\Qabc\E\$\Qxyz\E&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;abc$xyz </p>
<p> The \Q&#8230;\E sequence is recognized both inside and outside character classes. An isolated \E that is not preceded by \Q is ignored. If \Q is not followed by \E later in the pattern, the literal interpretation continues to the end of the pattern (that is, \E is assumed at the end). If the isolated \Q is inside a character class, this causes an error, because the character class is not terminated.</p>
<h3>Non-printing characters</h3>
<p>A second use of backslash provides a way of encoding non-printing characters in patterns in a visible manner. There is no restriction on the appearance of non-printing characters, apart from the binary zero that terminates a pattern, but when a pattern is being prepared by text editing, it is often easier to use one of the following escape sequences than the binary character it represents. In an ASCII or Unicode environment, these escapes are as follows: </p>
<p>&nbsp;<wbr>&nbsp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alarm, that is, the BEL character&nbsp;(hex 07)<br />
&nbsp;<wbr>&nbsp;
