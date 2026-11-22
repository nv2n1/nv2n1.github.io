---

title: "perlreref(1)"
name: "perlreref"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreref/"
description: "perlreref – Perl Regular Expressions Reference"
---

<p> perlreref - Perl Regular Expressions Reference </p>
<h2>DESCRIPTION</h2>
<p> This is a quick reference to Perl&#8217;s regular expressions. For full information see perlre and perlop, as well as the ``SEE ALSO&#8217;&#8216; section in this document.  </p>
<h3>OPERATORS</h3>
<p> <code>&quot;=~&quot;</code> determines to which variable the regex is applied. In its absence, <code>$_</code> is used. </p>
<pre><code>    $var =~ /foo/;
</code></pre>
<p> <code>&quot;!~&quot;</code> determines to which variable the regex is applied, and negates the result of the match; it returns false if the match succeeds, and true if it fails. </p>
<pre><code>    $var !~ /foo/;
</code></pre>
<p> <code>&quot;m/pattern/msixpogcdualn&quot;</code> searches a string for a pattern match, applying the given options. </p>
<pre><code>    m Multiline mode - ^ and $ match internal lines
    s match as a Single line - . matches \n
    i case-Insensitive
    x eXtended legibility - free whitespace and comments
    p Preserve a copy of the matched string -
       ${^PREMATCH}, ${^MATCH}, ${^POSTMATCH} will be defined.
    o compile pattern Once
    g Global - all occurrences
    c don't reset pos on failed matches when using /g
    a restrict \d, \s, \w and [:posix:] to match ASCII only
    aa (two a's) also /i matches exclude ASCII/non-ASCII
    l match according to current locale
    u match according to Unicode rules
    d match according to native rules unless something indicates
       Unicode
    n Non-capture mode. Don't let () fill in $1, $2, etc...
</code></pre>
<p> If &#8216;pattern&#8217; is an empty string, the last <i>successfully</i> matched regex is used. Delimiters other than &#8216;/&#8216; may be used for both this operator and the following ones. The leading <code>&quot;m&quot;</code> can be omitted if the delimiter is &#8216;/&#8216;. </p>
<p> <code>&quot;qr/pattern/msixpodualn&quot;</code> lets you store a regex in a variable, or pass one around. Modifiers as for <code>&quot;m//&quot;</code>, and are stored within the regex. </p>
<p> <code>&quot;s/pattern/replacement/msixpogcedual&quot;</code> substitutes matches of &#8216;pattern&#8217; with &#8216;replacement&#8217;. Modifiers as for <code>&quot;m//&quot;</code>, with two additions: </p>
<pre><code>    e Evaluate 'replacement' as an expression
    r Return substitution and leave the original string untouched.
</code></pre>
<p> &#8216;e&#8217; may be specified multiple times. &#8216;replacement&#8217; is interpreted as a double quoted string unless a single-quote (<code>&quot;&#8216;&quot;</code>) is the delimiter. </p>
<p> <code>&quot;m?pattern?&quot;</code> is like <code>&quot;m/pattern/&quot;</code> but matches only once. No alternate delimiters can be used. Must be reset with <code>reset()</code>.  </p>
<h3>SYNTAX</h3>
<pre><code> \ Escapes the character immediately following it
 . Matches any single character except a newline (unless /s is
           used)
 ^ Matches at the beginning of the string (or line, if /m is used)
 $ Matches at the end of the string (or line, if /m is used)
 * Matches the preceding element 0 or more times
 + Matches the preceding element 1 or more times
 ? Matches the preceding element 0 or 1 times
 {...} Specifies a range of occurrences for the element preceding it
 [...] Matches any one of the characters contained within the brackets
 (...) Groups subexpressions for capturing to $1, $2...
 (?:...) Groups subexpressions without capturing (cluster)
 | Matches either the subexpression preceding or following it
 \g1 or \g{1}, \g2 ... Matches the text from the Nth group
 \1, \2, \3 ... Matches the text from the Nth group
 \g-1 or \g{-1}, \g-2 ... Matches the text from the Nth previous group
 \g{name} Named backreference
 \k&lt;name&gt; Named backreference
 \k'name' Named backreference
 (?P=name) Named backreference (python syntax)
</code></pre>
<h3>ESCAPE SEQUENCES</h3>
<p> These work as in normal strings. </p>
<pre><code>   \a Alarm (beep)
   \e Escape
   \f Formfeed
   \n Newline
   \r Carriage return
   \t Tab
   \037 Char whose ordinal is the 3 octal digits, max \777
   \o{2307} Char whose ordinal is the octal number, unrestricted
   \x7f Char whose ordinal is the 2 hex digits, max \xFF
   \x{263a} Char whose ordinal is the hex number, unrestricted
   \cx Control-x
   \N{name} A named Unicode character or character sequence
   \N{U+263D} A Unicode character by hex ordinal
   \l Lowercase next character
   \u Titlecase next character
   \L Lowercase until \E
   \U Uppercase until \E
   \F Foldcase until \E
   \Q Disable pattern metacharacters until \E
   \E End modification
</code></pre>
<p> For Titlecase, see ``Titlecase&#8217;&#8216;. </p>
<p> This one works differently from normal strings: </p>
<pre><code>   \b An assertion, not backspace, except in a character class
</code></pre>
<h3>CHARACTER CLASSES</h3>
<pre><code>   [amy] Match 'a', 'm' or 'y'
   [f-j] Dash specifies &quot;range&quot;
   [f-j-] Dash escaped or at start or end means 'dash'
   [^f-j] Caret indicates &quot;match any character _except_ these&quot;
</code></pre>
<p> The following sequences (except <code>&quot;\N&quot;</code>) work within or without a character class. The first six are locale aware, all are Unicode aware. See perllocale and perlunicode for details. </p>
<pre><code>   \d A digit
   \D A nondigit
   \w A word character
   \W A non-word character
   \s A whitespace character
   \S A non-whitespace character
   \h A horizontal whitespace
   \H A non horizontal whitespace
   \N A non newline (when not followed by '{NAME}';;
           not valid in a character class; equivalent to [^\n]; it's
           like '.' without /s modifier)
   \v A vertical whitespace
   \V A non vertical whitespace
   \R A generic newline (?&gt;\v|\x0D\x0A)
   \pP Match P-named (Unicode) property
   \p{...} Match Unicode property with name longer than 1 character
   \PP Match non-P
   \P{...} Match lack of Unicode property with name longer than 1 char
   \X Match Unicode extended grapheme cluster
</code></pre>
<p> POSIX character classes and their Unicode and Perl equivalents: </p>
<pre><code>            ASCII- Full-
   POSIX range range backslash
 [[:...:]] \p{...} \p{...} sequence Description
 -----------------------------------------------------------------------
 alnum PosixAlnum XPosixAlnum 'alpha' plus 'digit'
 alpha PosixAlpha XPosixAlpha Alphabetic characters
 ascii ASCII Any ASCII character
 blank PosixBlank XPosixBlank \h Horizontal whitespace;
                                                   full-range also
                                                   written as
                                                   \p{HorizSpace} (GNU
                                                   extension)
 cntrl PosixCntrl XPosixCntrl Control characters
 digit PosixDigit XPosixDigit \d Decimal digits
 graph PosixGraph XPosixGraph 'alnum' plus 'punct'
 lower PosixLower XPosixLower Lowercase characters
 print PosixPrint XPosixPrint 'graph' plus 'space',
                                                   but not any Controls
 punct PosixPunct XPosixPunct Punctuation and Symbols
                                                   in ASCII-range; just
                                                   punct outside it
 space PosixSpace XPosixSpace \s Whitespace
 upper PosixUpper XPosixUpper Uppercase characters
 word PosixWord XPosixWord \w 'alnum' + Unicode marks
                                                    + connectors, like
                                                    '_' (Perl extension)
 xdigit ASCII_Hex_Digit XPosixDigit Hexadecimal digit,
                                                    ASCII-range is
                                                    [0-9A-Fa-f]
</code></pre>
<p> Also, various synonyms like <code>&quot;\p{Alpha}&quot;</code> for <code>&quot;\p{XPosixAlpha}&quot;</code>; all listed in ``Properties accessible through \p{} and \P{}&#8216;&#8216; in perluniprops </p>
<p> Within a character class: </p>
<pre><code>    POSIX traditional Unicode
  [:digit:] \d \p{Digit}
  [:^digit:] \D \P{Digit}
</code></pre>
<h3>ANCHORS</h3>
<p> All are zero-width assertions. </p>
<pre><code>   ^ Match string start (or line, if /m is used)
   $ Match string end (or line, if /m is used) or before newline
   \b{} Match boundary of type specified within the braces
   \B{} Match wherever \b{} doesn't match
   \b Match word boundary (between \w and \W)
   \B Match except at word boundary (between \w and \w or \W and \W)
   \A Match string start (regardless of /m)
   \Z Match string end (before optional newline)
   \z Match absolute string end
   \G Match where previous m//g left off
   \K Keep the stuff left of the \K, don't include it in $&amp;
</code></pre>
<h3>QUANTIFIERS</h3>
<p> Quantifiers are greedy by default and match the <code>longest</code> leftmost. </p>
<pre><code>   Maximal Minimal Possessive Allowed range
   ------- ------- ---------- -------------
   {n,m} {n,m}? {n,m}+ Must occur at least n times
                              but no more than m times
   {n,} {n,}? {n,}+ Must occur at least n times
   {n} {n}? {n}+ Must occur exactly n times
   * *? *+ 0 or more times (same as {0,})
   + +? ++ 1 or more times (same as {1,})
   ? ?? ?+ 0 or 1 time (same as {0,1})
</code></pre>
<p> The possessive forms (new in Perl 5.10) prevent backtracking: what gets matched by a pattern with a possessive quantifier will not be backtracked into, even if that causes the whole match to fail. </p>
<p> There is no quantifier <code>&quot;{,n}&quot;</code>. That&#8217;s interpreted as a literal string.  </p>
<h3>EXTENDED CONSTRUCTS</h3>
<pre><code>   (?#text) A comment
   (?:...) Groups subexpressions without capturing (cluster)
   (?pimsx-imsx:...) Enable/disable option (as per m// modifiers)
   (?=...) Zero-width positive lookahead assertion
   (?*pla:...) Same; avail experimentally starting in 5.28
   (?!...) Zero-width negative lookahead assertion
   (?*nla:...) Same; avail experimentally starting in 5.28
   (?&lt;=...) Zero-width positive lookbehind assertion
   (?*plb:...) Same; avail experimentally starting in 5.28
   (?&lt;!...) Zero-width negative lookbehind assertion
   (?*nlb:...) Same; avail experimentally starting in 5.28
   (?&gt;...) Grab what we can, prohibit backtracking
   (?*atomic:...) Same; avail experimentally starting in 5.28
   (?|...) Branch reset
   (?&lt;name&gt;...) Named capture
   (?'name'...) Named capture
   (?P&lt;name&gt;...) Named capture (python syntax)
   (?[...]) Extended bracketed character class
   (?{ code }) Embedded code, return value becomes $^R
   (??{ code }) Dynamic regex, return value used as regex
   (?N) Recurse into subpattern number N
   (?-N), (?+N) Recurse into Nth previous/next subpattern
   (?R), (?0) Recurse at the beginning of the whole pattern
   (?&amp;name) Recurse into a named subpattern
   (?P&gt;name) Recurse into a named subpattern (python syntax)
   (?(cond)yes|no)
   (?(cond)yes) Conditional expression, where &quot;(cond)&quot; can be:
                     (?=pat) lookahead
                     (?!pat) negative lookahead
                     (?&lt;=pat) lookbehind
                     (?&lt;!pat) negative lookbehind
                     (N) subpattern N has matched something
                     (&lt;name&gt;) named subpattern has matched something
                     ('name') named subpattern has matched something
                     (?{code}) code condition
                     (R) true if recursing
                     (RN) true if recursing into Nth subpattern
                     (R&amp;name) true if recursing into named subpattern
                     (DEFINE) always false, no no-pattern allowed
</code></pre>
<h3>VARIABLES</h3>
<pre><code>   $_ Default variable for operators to use
   $` Everything prior to matched string
   $&amp; Entire matched string
   $' Everything after to matched string
   ${^PREMATCH} Everything prior to matched string
   ${^MATCH} Entire matched string
   ${^POSTMATCH} Everything after to matched string
</code></pre>
<p> Note to those still using Perl 5.18 or earlier: The use of <code>&quot;$`&quot;</code>, <code>$&amp;</code> or <code>&quot;$&#8216;&quot;</code> will slow down <code>all</code> regex use within your program. Consult perlvar for <code>&quot;@-&quot;</code> to see equivalent expressions that won&#8217;t cause slow down. See also Devel::SawAmpersand. Starting with Perl 5.10, you can also use the equivalent variables <code>&quot;${^PREMATCH}&quot;</code>, <code>&quot;${^MATCH}&quot;</code> and <code>&quot;${^POSTMATCH}&quot;</code>, but for them to be defined, you have to specify the <code>&quot;/p&quot;</code> (preserve) modifier on your regular expression. In Perl 5.20, the use of <code>&quot;$`&quot;</code>, <code>$&amp;</code> and <code>&quot;$&#8216;&quot;</code> makes no speed difference. </p>
<pre><code>   $1, $2 ... hold the Xth captured expr
   $+ Last parenthesized pattern match
   $^N Holds the most recently closed capture
   $^R Holds the result of the last (?{...}) expr
   @- Offsets of starts of groups. $-[0] holds start of whole match
   @+ Offsets of ends of groups. $+[0] holds end of whole match
   %+ Named capture groups
   %- Named capture groups, as array refs
</code></pre>
<p> Captured groups are numbered according to their <i>opening</i> paren.  </p>
<h3>FUNCTIONS</h3>
<pre><code>   lc Lowercase a string
   lcfirst Lowercase first char of a string
   uc Uppercase a string
   ucfirst Titlecase first char of a string
   fc Foldcase a string
   pos Return or set current match position
   quotemeta Quote metacharacters
   reset Reset m?pattern? status
   study Analyze string for optimizing matching
   split Use a regex to split a string into parts
</code></pre>
<p> The first five of these are like the escape sequences <code>&quot;\L&quot;</code>, <code>&quot;\l&quot;</code>, <code>&quot;\U&quot;</code>, <code>&quot;\u&quot;</code>, and <code>&quot;\F&quot;</code>. For Titlecase, see ``Titlecase&#8217;&#8216;; For Foldcase, see ``Foldcase&#8217;&#8216;.  </p>
<h3>TERMINOLOGY</h3>
<p> <i>Titlecase</i> </p>
<p> Unicode concept which most often is equal to uppercase, but for certain characters like the German ``sharp s&#8217;&#8216; there is a difference. </p>
<p> <i>Foldcase</i> </p>
<p> Unicode form that is useful when comparing strings regardless of case, as certain characters have complex one-to-many case mappings. Primarily a variant of lowercase.  </p>
<h2>AUTHOR</h2>
<p> Iain Truskett. Updated by the Perl 5 Porters. </p>
<p> This document may be distributed under the same terms as Perl itself.  </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> perlretut for a tutorial on regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrequick for a rapid tutorial. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlre for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlvar for details on the variables. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlop for details on the operators. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfunc for details on the functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfaq6 for FAQs on regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrebackslash for a reference on backslash sequences. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrecharclass for a reference on character classes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The re module to alter behaviour and aid debugging. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``Debugging Regular Expressions&#8217;&#8216; in perldebug </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perluniintro, perlunicode, charnames and perllocale for details on regexes and internationalisation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Mastering Regular Expressions</i> by Jeffrey Friedl (&lt;<a rel="nofollow" href="http://oreilly.com/catalog/9780596528126/">http://oreilly.com/catalog/9780596528126/</a>&gt;) for a thorough grounding and reference on the topic. </p>
 </dd></dl>
<h2>THANKS</h2>
<p> David P.C. Wollmann, Richard Soderberg, Sean M. Burke, Tom Christiansen, Jim Cromie, and Jeffrey Goff for useful advice. </p>
