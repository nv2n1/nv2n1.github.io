---
title: "perlreref(1)"
name: "perlreref"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreref/"
description: "perlreref – Perl Regular Expressions Reference"
---

<h2 class="name">NAME</h2>
<p> perlreref &#8211; Perl Regular Expressions Reference </p>
<h2>DESCRIPTION</h2>
<p> This is a quick reference to Perl&#8217;s regular expressions. For full information see perlre and perlop, as well as the &#8220;<font SIZE="-1">SEE ALSO&#8221;</font> section in this document.</p>
<h3><font SIZE="-1">OPERATORS</font></h3>
<p> <tt>&quot;=~&quot;</tt> determines to which variable the regex is applied. In its absence, <tt>$_</tt> is used. </p>
<pre>
    $var =~ /foo/;
</pre>
<p> <tt>&quot;!~&quot;</tt> determines to which variable the regex is applied, and negates the result of the match; it returns false if the match succeeds, and true if it fails. </p>
<pre>
    $var !~ /foo/;
</pre>
<p> <tt>&quot;m/pattern/msixpogcdualn&quot;</tt> searches a string for a pattern match, applying the given options. </p>
<pre><code>
    m  Multiline mode - ^ and $ match internal lines
    s  match as a Single line - . matches 

    i  case-Insensitive
    x  eXtended legibility - free whitespace and comments
    p  Preserve a copy of the matched string -
       ${^PREMATCH}, ${^MATCH}, ${^POSTMATCH} will be defined.
    o  compile pattern Once
    g  Global - all occurrences
    c  don't reset pos on failed matches when using /g
    a  restrict \d, \s, \w and [:posix:] to match ASCII only
    aa (two a's) also /i matches exclude ASCII/non-ASCII
    l  match according to current locale
    u  match according to Unicode rules
    d  match according to native rules unless something indicates
       Unicode
    n  Non-capture mode. Don't let () fill in $1, $2, etc...
</code></pre>
<p> If &#8216;pattern&#8217; is an empty string, the last <i>successfully</i> matched regex is used. Delimiters other than &#8216;/&#8217; may be used for both this operator and the following ones. The leading <tt>&quot;m&quot;</tt> can be omitted if the delimiter is &#8216;/&#8217;. </p>
<p> <tt>&quot;qr/pattern/msixpodualn&quot;</tt> lets you store a regex in a variable, or pass one around. Modifiers as for <tt>&quot;m//&quot;</tt>, and are stored within the regex. </p>
<p> <tt>&quot;s/pattern/replacement/msixpogcedual&quot;</tt> substitutes matches of &#8216;pattern&#8217; with &#8216;replacement&#8217;. Modifiers as for <tt>&quot;m//&quot;</tt>, with two additions: </p>
<pre>
    e  Evaluate 'replacement' as an expression
    r  Return substitution and leave the original string untouched.
</pre>
<p> &#8216;e&#8217; may be specified multiple times. &#8216;replacement&#8217; is interpreted as a double quoted string unless a single-quote (<tt>&quot;'&quot;</tt>) is the delimiter. </p>
<p> <tt>&quot;m?pattern?&quot;</tt> is like <tt>&quot;m/pattern/&quot;</tt> but matches only once. No alternate delimiters can be used. Must be reset with <code>reset()</code>.</p>
<h3><font SIZE="-1">SYNTAX</font></h3>
<p>\ Escapes the character immediately following it<br />
            .Matches any single character except a<br />
            newline(unless / s is<br />
                                 used) ^<br />
        Matches at the beginning of the string(or line, if / m is used)<br />
                $ Matches at the end of the string(or line, if / m is used) *<br />
            Matches the preceding element 0 or<br />
    more times<br />
        + Matches the preceding element 1 or<br />
    more times<br />
    ? Matches the preceding element 0 or 1 times{&#8230;} Specifies a range of occurrences for the element preceding it<br />
                                             [&#8230;] Matches any one of the characters contained within the brackets(&#8230;) Groups subexpressions for capturing to $1,<br />
    $2&#8230;(?: &#8230;) Groups subexpressions without capturing(cluster) | Matches either the subexpression preceding or following it<br />
 \g1 or \g{1}, \g2&#8230; Matches the text from the Nth group<br />
 \1, \2, \3 &#8230; Matches the text from the Nth group<br />
 \g &#8211; 1 or \g{-1}, \g &#8211; 2 &#8230; Matches the text from the Nth previous group<br />
 \g{name} Named backreference<br />
 \k&lt;name&gt; Named backreference<br />
 \k &#8216;name&#8217; Named backreference(? P = name) Named backreference(python syntax)</p>
<h3><font SIZE="-1">ESCAPE SEQUENCES</font></h3>
<p> These work as in normal strings. </p>
<p> Alarm(beep)<br />
    Escape<br />
    Formfeed<br />
   
 Newline<br />
    Carriage return<br />
   	 Tab<br />
    Char whose ordinal is the 3 octal digits, max \777<br />
   \o{2307} Char whose ordinal is the octal number, unrestricted<br />
    Char whose ordinal is the 2 hex digits, max �<br />
   
