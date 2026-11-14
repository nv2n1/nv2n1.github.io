---
title: "re_format(7)"
name: "re_format"
section: "7"
letter: "r"
url: "/docs/linux/man/7-re_format/"
description: "regex – POSIX.2 regular expressions"
---

<p>regex &#8211; POSIX.2 regular expressions</p>
<h2>Description</h2>
<p>Regular expressions (&quot;RE&quot;s), as defined in POSIX.2, come in two forms: modern REs (roughly those of <i>egrep</i>; POSIX.2 calls these &quot;extended&quot; REs) and obsolete REs (roughly those of <code><a href="/docs/linux/man/1-ed/">ed</a></code>(1); POSIX.2 &quot;basic&quot; REs). Obsolete REs mostly exist for backward compatibility in some old programs; they will be discussed at the end. POSIX.2 leaves some aspects of RE syntax and semantics open; &quot;(!)&quot; marks decisions on these aspects that may not be fully portable to other POSIX.2 implementations. </p>
<p> A (modern) RE is one(!) or more nonempty(!) <i>branches</i>, separated by &#8216;|&#8217;. It matches anything that matches one of the branches. </p>
<p> A branch is one(!) or more <i>pieces</i>, concatenated. It matches a match for the first, followed by a match for the second, and so on. </p>
<p> A piece is an <i>atom</i> possibly followed by a single(!) &#8216;*&#8217;, &#8216;+&#8217;, &#8216;?&#8217;, or <i>bound</i>. An atom followed by &#8216;*&#8217; matches a sequence of 0 or more matches of the atom. An atom followed by &#8216;+&#8217; matches a sequence of 1 or more matches of the atom. An atom followed by &#8216;?&#8217; matches a sequence of 0 or 1 matches of the atom. </p>
<p> A <i>bound</i> is &#8216;{&#8216; followed by an unsigned decimal integer, possibly followed by &#8216;,&#8217; possibly followed by another unsigned decimal integer, always followed by &#8216;}&#8217;. The integers must lie between 0 and <code>RE_DUP_MAX</code> (255(!)) inclusive, and if there are two of them, the first may not exceed the second. An atom followed by a bound containing one integer <i>i</i> and no comma matches a sequence of exactly <i>i</i> matches of the atom. An atom followed by a bound containing one integer <i>i</i> and a comma matches a sequence of <i>i</i> or more matches of the atom. An atom followed by a bound containing two integers <i>i</i> and <i>j</i> matches a sequence of <i>i</i> through <i>j</i> (inclusive) matches of the atom. </p>
<p> An atom is a regular expression enclosed in &quot;<i>()</i>&quot; (matching a match for the regular expression), an empty set of &quot;<i>()</i>&quot; (matching the null string)(!), a <i>bracket expression</i> (see below), &#8216;.&#8217; (matching any single character), &#8216;ha&#8217; (matching the null string at the beginning of a line), &#8216;$&#8217; (matching the null string at the end of a line), a &#8216;\&#8217; followed by one of the characters &quot;<i>ha.[$()|*+?{\</i>&quot; (matching that character taken as an ordinary character), a &#8216;\&#8217; followed by any other character(!) (matching that character taken as an ordinary character, as if the &#8216;\&#8217; had not been present(!)), or a single character with no other significance (matching that character). A &#8216;{&#8216; followed by a character other than a digit is an ordinary character, not the beginning of a bound(!). It is illegal to end an RE with &#8216;\&#8217;. </p>
<p> A <i>bracket expression</i> is a list of characters enclosed in &quot;<i>[]</i>&quot;. It normally matches any single character from the list (but see below). If the list begins with &#8216;ha&#8217;, it matches any single character (but see below) <i>not</i> from the rest of the list. If two characters in the list are separated by &#8216;-&#8216;, this is shorthand for the full <i>range</i> of characters between those two (inclusive) in the collating sequence, for example, &quot;<i>[0-9]</i>&quot; in ASCII matches any decimal digit. It is illegal(!) for two ranges to share an endpoint, for example, &quot;<i>a-c-e</i>&quot;. Ranges are very collating-sequence-dependent, and portable programs should avoid relying on them. </p>
<p> To include a literal &#8216;]&#8217; in the list, make it the first character (following a possible &#8216;ha&#8217;). To include a literal &#8216;-&#8216;, make it the first or last character, or the second endpoint of a range. To use a literal &#8216;-&#8216; as the first endpoint of a range, enclose it in &quot;<i>[.</i>&quot; and &quot;<i>.]</i>&quot; to make it a collating element (see below). With the exception of these and some combinations using &#8216;[&#8216; (see next paragraphs), all other special characters, including &#8216;\&#8217;, lose their special significance within a bracket expression. </p>
<p> Within a bracket expression, a collating element (a character, a multicharacter sequence that collates as if it were a single character, or a collating-sequence name for either) enclosed in &quot;<i>[.</i>&quot; and &quot;<i>.]</i>&quot; stands for the sequence of characters of that collating element. The sequence is a single element of the bracket expression&#8217;s list. A bracket expression containing a multicharacter collating element can thus match more than one character, for example, if the collating sequence includes a &quot;ch&quot; collating element, then the RE &quot;<i>[[.ch.]]*c</i>&quot; matches the first five characters of &quot;chchcc&quot;. </p>
<p> Within a bracket expression, a collating element enclosed in &quot;<i>[=</i>&quot; and &quot;<i>=]</i>&quot; is an equivalence class, standing for the sequences of characters of all collating elements equivalent to that one, including itself. (If there are no other equivalent collating elements, the treatment is as if the enclosing delimiters were &quot;<i>[.</i>&quot; and &quot;<i>.]</i>&quot;.) For example, if o and are the members of an equivalence class, then &quot;<i>[[=o=]]</i>&quot;, &quot;<i>[[==]]</i>&quot;, and &quot;<i>[o]</i>&quot; are all synonymous. An equivalence class may not(!) be an endpoint of a range. </p>
<p> Within a bracket expression, the name of a <i>character class</i> enclosed in &quot;<i>[:</i>&quot; and &quot;<i>:]</i>&quot; stands for the list of all characters belonging to that class. Standard character class names are: </p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td>alnum</td>
<td>digit</td>
<td>punct
</td>
</tr>
<tr VALIGN=top>
<td>alpha</td>
<td>graph</td>
<td>space
</td>
</tr>
<tr VALIGN=top>
<td>blank</td>
<td>lower</td>
<td>upper
</td>
</tr>
<tr VALIGN=top>
<td>cntrl</td>
<td>print</td>
<td>xdigit
</td>
</tr>
</table>
</dl>
<p> These stand for the character classes defined in <code><a href="/docs/linux/man/3-wctype/">wctype</a></code>(3). A locale may provide others. A character class may not be used as an endpoint of a range. </p>
<p> In the event that an RE could match more than one substring of a given string, the RE matches the one starting earliest in the string. If the RE could match more than one substring starting at that point, it matches the longest. Subexpressions also match the longest possible substrings, subject to the constraint that the whole match be as long as possible, with subexpressions starting earlier in the RE taking priority over ones starting later. Note that higher-level subexpressions thus take priority over their lower-level component subexpressions. </p>
<p> Match lengths are measured in characters, not collating elements. A null string is considered longer than no match at all. For example, &quot;<i>bb*</i>&quot; matches the three middle characters of &quot;abbbc&quot;, &quot;<i>(wee|week)(knights|nights)</i>&quot; matches all ten characters of &quot;weeknights&quot;, when &quot;<i>(.*).*</i>&quot; is matched against &quot;abc&quot; the parenthesized subexpression matches all three characters, and when &quot;<i>(a*)*</i>&quot; is matched against &quot;bc&quot; both the whole RE and the parenthesized subexpression match the null string. </p>
<p> If case-independent matching is specified, the effect is much as if all case distinctions had vanished from the alphabet. When an alphabetic that exists in multiple cases appears as an ordinary character outside a bracket expression, it is effectively transformed into a bracket expression containing both cases, for example, &#8216;x&#8217; becomes &quot;<i>[xX]</i>&quot;. When it appears inside a bracket expression, all case counterparts of it are added to the bracket expression, so that, for example, &quot;<i>[x]</i>&quot; becomes &quot;<i>[xX]</i>&quot; and &quot;<i>[hax]</i>&quot; becomes &quot;<i>[haxX]</i>&quot;. </p>
<p> No particular limit is imposed on the length of REs(!). Programs intended to be portable should not employ REs longer than 256 bytes, as an implementation can refuse to accept such REs and remain POSIX-compliant. </p>
<p> Obsolete (&quot;basic&quot;) regular expressions differ in several respects. &#8216;|&#8217;, &#8216;+&#8217;, and &#8216;?&#8217; are ordinary characters and there is no equivalent for their functionality. The delimiters for bounds are &quot;<i>\{</i>&quot; and &quot;<i>\}</i>&quot;, with &#8216;{&#8216; and &#8216;}&#8217; by themselves ordinary characters. The parentheses for nested subexpressions are &quot;<i>\(</i>&quot; and &quot;<i>\)</i>&quot;, with &#8216;(&#8216; and &#8216;)&#8217; by themselves ordinary characters. &#8216;ha&#8217; is an ordinary character except at the beginning of the RE or(!) the beginning of a parenthesized subexpression, &#8216;$&#8217; is an ordinary character except at the end of the RE or(!) the end of a parenthesized subexpression, and &#8216;*&#8217; is an ordinary character if it appears at the beginning of the RE or the beginning of a parenthesized subexpression (after a possible leading &#8216;ha&#8217;). </p>
<p> Finally, there is one new type of atom, a <i>back reference</i>: &#8216;\&#8217; followed by a nonzero decimal digit <i>d</i> matches the same sequence of characters matched by the <i>d</i>th parenthesized subexpression (numbering subexpressions by the positions of their opening parentheses, left to right), so that, for example, &quot;<i>\([bc]\)\1</i>&quot; matches &quot;bb&quot; or &quot;cc&quot; but not &quot;bc&quot;.</p>
<h2>Bugs</h2>
<p>Having two kinds of REs is a botch. </p>
<p> The current POSIX.2 spec says that &#8216;)&#8217; is an ordinary character in the absence of an unmatched &#8216;(&#8216;; this was an unintentional result of a wording error, and change is likely. Avoid relying on it. </p>
<p> Back references are a dreadful botch, posing major problems for efficient implementations. They are also somewhat vaguely defined (does &quot;<i>a\(\(b\)*\2\)*d</i>&quot; match &quot;abbbd&quot;?). Avoid using them. </p>
<p> POSIX.2&#8217;s specification of case-independent matching is vague. The &quot;one case implies all cases&quot; definition given above is current consensus among implementors as to the right interpretation.</p>
<h2>Author</h2>
<p>This page was taken from Henry Spencer&#8217;s regex package.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/3-regex/">regex</a></code>(3) </p>
<p> POSIX.2, section 2.8 (Regular Expression Notation).</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
