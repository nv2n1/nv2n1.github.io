---
title: "uwildmat(3)"
name: "uwildmat"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uwildmat/"
description: "uwildmat, uwildmat_simple, uwildmat_poison – Perform wildmat matching"
---

<p>uwildmat, uwildmat_simple, uwildmat_poison &#8211; Perform wildmat matching</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;inn/libinn.h&gt;

bool uwildmat(const char *text, const char *pattern);

bool uwildmat_simple(const char *text, const char *pattern);

enum uwildmat uwildmat_poison(const char *text, const char *pattern);</code></pre>
<h2>Description</h2>
<p><code>uwildmat</code> compares <i>text</i> against the wildmat expression <i>pattern</i>, returning true if and only if the expression matches the text. <tt>&quot;@&quot;</tt> has no special meaning in <i>pattern</i> when passed to <code>uwildmat</code>. Both <i>text</i> and <i>pattern</i> are assumed to be in the <font SIZE="-1">UTF-8</font> character encoding, although malformed <font SIZE="-1">UTF-8</font> sequences are treated in a way that attempts to be mostly compatible with single-octet character sets like <font SIZE="-1">ISO</font> 8859-1. (In other words, if you try to match <font SIZE="-1">ISO</font> 8859-1 text with these routines everything should work as expected unless the <font SIZE="-1">ISO</font> 8859-1 text contains valid <font SIZE="-1">UTF-8</font> sequences, which thankfully is somewhat rare.) </p>
<p> <code>uwildmat_simple</code> is identical to <code>uwildmat</code> except that neither <tt>&quot;!&quot;</tt> nor <tt>&quot;,&quot;</tt> have any special meaning and <i>pattern</i> is always treated as a single pattern. This function exists solely to support legacy interfaces like <font SIZE="-1">NNTP</font>&#8216;s <font SIZE="-1">XPAT</font> command, and should be avoided when implementing new features. </p>
<p> <code>uwildmat_poison</code> works similarly to <code>uwildmat</code>, except that <tt>&quot;@&quot;</tt> as the first character of one of the patterns in the expression (see below) &#8220;poisons&#8221; the match if it matches. <code>uwildmat_poison</code> returns <font SIZE="-1"><code>UWILDMAT_MATCH</code></font> if the expression matches the text, <font SIZE="-1"><code>UWILDMAT_FAIL</code></font> if it doesn&#8217;t, and <font SIZE="-1"><code>UWILDMAT_POISON</code></font> if the expression doesn&#8217;t match because a poisoned pattern matched the text. These enumeration constants are defined in the <code>inn/libinn.h</code> header.</p>
<h2>Wildmat Expressions</h2>
<p>A wildmat expression follows rules similar to those of shell filename wildcards but with some additions and changes. A wildmat <i>expression</i> is composed of one or more wildmat <i>patterns</i> separated by commas. Each character in the wildmat pattern matches a literal occurrence of that same character in the text, with the exception of the following metacharacters:</p>
<dl>
<dt>?</p>
<dd>Matches any single character (including a single <font SIZE="-1">UTF-8</font> multibyte character, so <tt>&quot;?&quot;</tt> can match more than one byte).</p>
<dt>*</p>
<dd>Matches any sequence of zero or more characters.</p>
<dt>\</p>
<dd>Turns off any special meaning of the following character; the following character will match itself in the text. <tt>&quot;\&quot;</tt> will escape any character, including another backslash or a comma that otherwise would separate a pattern from the next pattern in an expression. Note that <tt>&quot;\&quot;</tt> is not special inside a character range (no metacharacters are).</p>
<dt>[&#8230;]</p>
<dd>A character set, which matches any single character that falls within that set. The presence of a character between the brackets adds that character to the set; for example, <tt>&quot;[amv]&quot;</tt> specifies the set containing the characters <tt>&quot;a&quot;</tt>, <tt>&quot;m&quot;</tt>, and <tt>&quot;v&quot;</tt>. A range of characters may be specified using <tt>&quot;-&quot;</tt>; for example, <tt>&quot;[0-5abc]&quot;</tt> is equivalent to <tt>&quot;[012345abc]&quot;</tt>. The order of characters is as defined in the <font SIZE="-1">UTF-8</font> character set, and if the start character of such a range falls after the ending character of the range in that ranking the results of attempting a match with that pattern are undefined. </p>
<p> In order to include a literal <tt>&quot;]&quot;</tt> character in the set, it must be the first character of the set (possibly following <tt>&quot;^&quot;</tt>); for example, <tt>&quot;[]a]&quot;</tt> matches either <tt>&quot;]&quot;</tt> or <tt>&quot;a&quot;</tt>. To include a literal <tt>&quot;-&quot;</tt> character in the set, it must be either the first or the last character of the set. Backslashes have no special meaning inside a character set, nor do any other of the wildmat metacharacters.</p>
<dt>[^&#8230;]</p>
<dd>A negated character set. Follows the same rules as a character set above, but matches any character <code>not</code> contained in the set. So, for example, <tt>&quot;[^]-]&quot;</tt> matches any character except <tt>&quot;]&quot;</tt> and <tt>&quot;-&quot;</tt>.</dl>
<p> In addition, <tt>&quot;!&quot;</tt> (and possibly <tt>&quot;@&quot;</tt>) have special meaning as the first character of a pattern; see below. </p>
<p> When matching a wildmat expression against some text, each comma-separated pattern is matched in order from left to right. In order to match, the pattern must match the whole text; in regular expression terminology, it&#8217;s implicitly anchored at both the beginning and the end. For example, the pattern <tt>&quot;a&quot;</tt> matches only the text <tt>&quot;a&quot;</tt>; it doesn&#8217;t match <tt>&quot;ab&quot;</tt> or <tt>&quot;ba&quot;</tt> or even <tt>&quot;aa&quot;</tt>. If none of the patterns match, the whole expression doesn&#8217;t match. Otherwise, whether the expression matches is determined entirely by the rightmost matching pattern; the expression matches the text if and only if the rightmost matching pattern is not negated. </p>
<p> For example, consider the text <tt>&quot;news.misc&quot;</tt>. The expression <tt>&quot;*&quot;</tt> matches this text, of course, as does <tt>&quot;comp.*,news.*&quot;</tt> (because the second pattern matches). <tt>&quot;news.*,!news.misc&quot;</tt> does not match this text because both patterns match, meaning that the rightmost takes precedence, and the rightmost matching pattern is negated. <tt>&quot;news.*,!news.misc,*.misc&quot;</tt> does match this text, since the rightmost matching pattern is not negated. </p>
<p> Note that the expression <tt>&quot;!news.misc&quot;</tt> can&#8217;t match anything. Either the pattern doesn&#8217;t match, in which case no patterns match and the expression doesn&#8217;t match, or the pattern does match, in which case because it&#8217;s negated the expression doesn&#8217;t match. <tt>&quot;*,!news.misc&quot;</tt>, on the other hand, is a useful pattern that matches anything except <tt>&quot;news.misc&quot;</tt>. </p>
<p> <tt>&quot;!&quot;</tt> has significance only as the first character of a pattern; anywhere else in the pattern, it matches a literal <tt>&quot;!&quot;</tt> in the text like any other non-metacharacter. </p>
<p> If the <code>uwildmat_poison</code> interface is used, then <tt>&quot;@&quot;</tt> behaves the same as <tt>&quot;!&quot;</tt> except that if an expression fails to match because the rightmost matching pattern began with <tt>&quot;@&quot;</tt>, <font SIZE="-1"><code>UWILDMAT_POISON</code></font> is returned instead of <font SIZE="-1"><code>UWILDMAT_FAIL</code></font>. </p>
<p> If the <code>uwildmat_simple</code> interface is used, the matching rules are the same as above except that none of <tt>&quot;!&quot;</tt>, <tt>&quot;@&quot;</tt>, or <tt>&quot;,&quot;</tt> have any special meaning at all and only match those literal characters.</p>
<h2>Bugs</h2>
<p>All of these functions internally convert the passed arguments to const unsigned char pointers. The only reason why they take regular char pointers instead of unsigned char is for the convenience of <font SIZE="-1">INN</font> and other callers that may not be using unsigned char everywhere they should. In a future revision, the public interface should be changed to just take unsigned char pointers.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; in 1986, and posted to Usenet several times since then, most notably in comp.sources.misc in March, 1991. </p>
<p> Lars Mathiesen &lt;thorinn [at] diku.dk&gt; enhanced the multi-asterisk failure mode in early 1991. </p>
<p> Rich and Lars increased the efficiency of star patterns and reposted it to comp.sources.misc in April, 1991. </p>
<p> Robert Elz &lt;kre [at] munnari.oz.au&gt; added minus sign and close bracket handling in June, 1991. </p>
<p> Russ Allbery &lt;eagle [at] eyrie.org&gt; added support for comma-separated patterns and the <tt>&quot;!&quot;</tt> and <tt>&quot;@&quot;</tt> metacharacters to the core wildmat routines in July, 2000. He also added support for <font SIZE="-1">UTF-8</font> characters, changed the default behavior to assume that both the text and the pattern are in <font SIZE="-1">UTF-8</font>, and largely rewrote this documentation to expand and clarify the description of how a wildmat expression matches. </p>
<p> Please note that the interfaces to these functions are named <code>uwildmat</code> and the like rather than <code>wildmat</code> to distinguish them from the <code>wildmat</code> function provided by Rich <tt>$alz</tt>&#8216;s original implementation. While this code is heavily based on Rich&#8217;s original code, it has substantial differences, including the extension to support <font SIZE="-1">UTF-8</font> characters, and has noticable functionality changes. Any bugs present in it aren&#8217;t Rich&#8217;s fault. </p>
<p> <tt>$Id:</tt> uwildmat.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-grep/">grep</a></i>(1), <i><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></i>(3), <i><a href="/docs/linux/man/3-regex/">regex</a></i>(3), <i><a href="/docs/linux/man/3-regexp/">regexp</a></i>(3). </p>
