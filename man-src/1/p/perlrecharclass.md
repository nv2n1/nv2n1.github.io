---
title: "perlrecharclass(1)"
name: "perlrecharclass"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrecharclass/"
description: "perlrecharclass – Perl Regular Expression Character Classes"
---

<h2 class="name">NAME</h2>
<p> perlrecharclass &#8211; Perl Regular Expression Character Classes </p>
<h2>DESCRIPTION</h2>
<p> The top level documentation about Perl regular expressions is found in perlre. </p>
<p> This manual page discusses the syntax and use of character classes in Perl regular expressions. </p>
<p> A character class is a way of denoting a set of characters in such a way that one character of the set is matched. It&#8217;s important to remember that: matching a character class consumes exactly one character in the source string. (The source string is the string the regular expression is matched against.) </p>
<p> There are three types of character classes in Perl regular expressions: the dot, backslash sequences, and the form enclosed in square brackets. Keep in mind, though, that often the term &#8220;character class&#8221; is used to mean just the bracketed form. Certainly, most Perl documentation does that.</p>
<h3>The dot</h3>
<p> The dot (or period), <tt>&quot;.&quot;</tt> is probably the most used, and certainly the most well-known character class. By default, a dot matches any character, except for the newline. That default can be changed to add matching the newline by using the <i>single line</i> modifier: for the entire regular expression with the <tt>&quot;/s&quot;</tt> modifier, or locally with <tt>&quot;(?s)&quot;</tt> (and even globally within the scope of <tt>&quot;use re '/s'&quot;</tt>). (The <tt>&quot;\N&quot;</tt> backslash sequence, described below, matches any character except newline without regard to the <i>single line</i> modifier.) </p>
<p> Here are some examples: </p>
<pre>
 &quot;a&quot;  =~  /./       # Match
 &quot;.&quot;  =~  /./       # Match
 &quot;&quot;   =~  /./       # No match (dot has to match a character)
 &quot;
&quot; =~  /./       # No match (dot does not match a newline)
 &quot;
&quot; =~  /./s      # Match (global 'single line' modifier)
 &quot;
&quot; =~  /(?s:.)/  # Match (local 'single line' modifier)
 &quot;ab&quot; =~  /^.$/     # No match (dot matches one character)
</pre>
<h3>Backslash sequences</h3>
<p> A backslash sequence is a sequence of characters, the first one of which is a backslash. Perl ascribes special meaning to many such sequences, and some of these are character classes. That is, they match a single character each, provided that the character belongs to the specific set of characters defined by the sequence. </p>
<p> Here&#8217;s a list of the backslash sequences that are character classes. They are discussed in more detail below. (For the backslash sequences that aren&#8217;t character classes, see perlrebackslash.) </p>
<pre><code>
\d Match a decimal digit character.
 \D Match a non - decimal - digit character.
 \w Match a "word" character.
 \W Match a non - "word" character.
 \s Match a whitespace character.
 \S Match a non - whitespace character.
 \h Match a horizontal whitespace character.
 \H Match a character that isn't horizontal whitespace.
  Match a vertical whitespace character.
 \V Match a character that isn't vertical whitespace.
 \N Match a character that isn't a newline.
 \pP, \p{Prop} Match a character that has the given Unicode property.
 \PP, \P{Prop} Match a character that doesn't have the Unicode property
</code></pre>
<p> <i>\N</i> </p>
<p> <tt>&quot;\N&quot;</tt>, available starting in v5.12, like the dot, matches any character that is not a newline. The difference is that <tt>&quot;\N&quot;</tt> is not influenced by the <i>single line</i> regular expression modifier (see &#8220;The dot&#8221; above). Note that the form <tt>&quot;\N{...}&quot;</tt> may mean something completely different. When the <tt>&quot;{...}&quot;</tt> is a quantifier, it means to match a non-newline character that many times. For example, <tt>&quot;\N{3}&quot;</tt> means to match 3 non-newlines; <tt>&quot;\N{5,}&quot;</tt> means to match 5 or more non-newlines. But if <tt>&quot;{...}&quot;</tt> is not a legal quantifier, it is presumed to be a named character. See charnames for those. For example, none of <tt>&quot;\N{COLON}&quot;</tt>, <tt>&quot;\N{4F}&quot;</tt>, and <tt>&quot;\N{F4}&quot;</tt> contain legal quantifiers, so Perl will try to find characters whose names are respectively <tt>&quot;COLON&quot;</tt>, <tt>&quot;4F&quot;</tt>, and <tt>&quot;F4&quot;</tt>. </p>
<p> <i>Digits</i> </p>
<p> <tt>&quot;\d&quot;</tt> matches a single character considered to be a decimal <i>digit</i>. If the <tt>&quot;/a&quot;</tt> regular expression modifier is in effect, it matches [0-9]. Otherwise, it matches anything that is matched by <tt>&quot;\p{Digit}&quot;</tt>, which includes [0-9]. (An unlikely possible exception is that under locale matching rules, the current locale might not have <tt>&quot;[0-9]&quot;</tt> matched by <tt>&quot;\d&quot;</tt>, and/or might match other characters whose code point is less than 256. The only such locale definitions that are legal would be to match <tt>&quot;[0-9]&quot;</tt> plus another set of 10 consecutive digit characters; anything else would be in violation of the C language standard, but Perl doesn&#8217;t currently assume anything in regard to this.) </p>
<p> What this means is that unless the <tt>&quot;/a&quot;</tt> modifier is in effect <tt>&quot;\d&quot;</tt> not only matches the digits &#8216;0&#8217; &#8211; &#8216;9&#8217;, but also Arabic, Devanagari, and digits from other languages. This may cause some confusion, and some security issues. </p>
<p> Some digits that <tt>&quot;\d&quot;</tt> matches look like some of the [0-9] ones, but have different values. For example, <font SIZE="-1">BENGALI DIGIT FOUR</font> (U+09EA) looks very much like an <font SIZE="-1">ASCII DIGIT EIGHT</font> (U+0038), and <font SIZE="-1">LEPCHA DIGIT SIX</font> (U+1C46) looks very much like an <font SIZE="-1">ASCII DIGIT FIVE</font> (U+0035). An application that is expecting only the <font SIZE="-1">ASCII</font> digits might be misled, or if the match is <tt>&quot;\d+&quot;</tt>, the matched string might contain a mixture of digits from different writing systems that look like they signify a number different than they actually do. &#8220;<code>num()</code>&#8221; in Unicode::UCD can be used to safely calculate the value, returning <tt>&quot;undef&quot;</tt> if the input string contains such a mixture. Otherwise, for example, a displayed price might be deliberately different than it appears. </p>
<p> What <tt>&quot;\p{Digit}&quot;</tt> means (and hence <tt>&quot;\d&quot;</tt> except under the <tt>&quot;/a&quot;</tt> modifier) is <tt>&quot;\p{General_Category=Decimal_Number}&quot;</tt>, or synonymously, <tt>&quot;\p{General_Category=Digit}&quot;</tt>. Starting with Unicode version 4.1, this is the same set of characters matched by <tt>&quot;\p{Numeric_Type=Decimal}&quot;</tt>. But Unicode also has a different property with a similar name, <tt>&quot;\p{Numeric_Type=Digit}&quot;</tt>, which matches a completely different set of characters. These characters are things such as <tt>&quot;CIRCLED DIGIT ONE&quot;</tt> or subscripts, or are from writing systems that lack all ten digits. </p>
<p> The design intent is for <tt>&quot;\d&quot;</tt> to exactly match the set of characters that can safely be used with &#8220;normal&#8221; big-endian positional decimal syntax, where, for example 123 means one &#8216;hundred&#8217;, plus two &#8216;tens&#8217;, plus three &#8216;ones&#8217;. This positional notation does not necessarily apply to characters that match the other type of &#8220;digit&#8221;, <tt>&quot;\p{Numeric_Type=Digit}&quot;</tt>, and so <tt>&quot;\d&quot;</tt> doesn&#8217;t match them. </p>
<p> The Tamil digits (U+0BE6 &#8211; U+0BEF) can also legally be used in old-style Tamil numbers in which they would appear no more than one in a row, separated by characters that mean &#8220;times 10&#8221;, &#8220;times 100&#8221;, etc. (See &lt;<a rel="nofollow" href="http://www.unicode.org/notes/tn21">http://www.unicode.org/notes/tn21</a>&gt;.) </p>
<p> Any character not matched by <tt>&quot;\d&quot;</tt> is matched by <tt>&quot;\D&quot;</tt>. </p>
<p> <i>Word characters</i> </p>
<p> A <tt>&quot;\w&quot;</tt> matches a single alphanumeric character (an alphabetic character, or a decimal digit); or a connecting punctuation character, such as an underscore (&#8220;_&#8221;); or a &#8220;mark&#8221; character (like some sort of accent) that attaches to one of those. It does not match a whole word. To match a whole word, use <tt>&quot;\w+&quot;</tt>. This isn&#8217;t the same thing as matching an English word, but in the <font SIZE="-1">ASCII</font> range it is the same as a string of Perl-identifier characters.</p>
<dl>
<dt>If the &quot;/a&quot; modifier is in effect &#8230;</p>
<dd> <tt>&quot;\w&quot;</tt> matches the 63 characters [a-zA-Z0-9_].</p>
<dt>otherwise &#8230;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>For code points above 255 &#8230;</p>
<dd> <tt>&quot;\w&quot;</tt> matches the same as <tt>&quot;\p{Word}&quot;</tt> matches in this range. That is, it matches Thai letters, Greek letters, etc. This includes connector punctuation (like the underscore) which connect two words together, or diacritics, such as a <tt>&quot;COMBINING TILDE&quot;</tt> and the modifier letters, which are generally used to add auxiliary markings to letters.</p>
<dt>For code points below 256 &#8230;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>if locale rules are in effect &#8230;</p>
<dd> <tt>&quot;\w&quot;</tt> matches the platform&#8217;s native underscore character plus whatever the locale considers to be alphanumeric.</p>
<dt>if, instead, Unicode rules are in effect &#8230;</p>
<dd> <tt>&quot;\w&quot;</tt> matches exactly what <tt>&quot;\p{Word}&quot;</tt> matches.</p>
<dt>otherwise &#8230;</p>
<dd> <tt>&quot;\w&quot;</tt> matches [a-zA-Z0-9_].</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Which rules apply are determined as described in &#8220;Which character set modifier is in effect?&#8221; in perlre. </p>
<p> There are a number of security issues with the full Unicode list of word characters. See &lt;<a rel="nofollow" href="http://unicode.org/reports/tr36">http://unicode.org/reports/tr36</a>&gt;. </p>
<p> Also, for a somewhat finer-grained set of characters that are in programming language identifiers beyond the <font SIZE="-1">ASCII</font> range, you may wish to instead use the more customized &#8220;Unicode Properties&#8221;, <tt>&quot;\p{ID_Start}&quot;</tt>, <tt>&quot;\p{ID_Continue}&quot;</tt>, <tt>&quot;\p{XID_Start}&quot;</tt>, and <tt>&quot;\p{XID_Continue}&quot;</tt>. See &lt;<a rel="nofollow" href="http://unicode.org/reports/tr31">http://unicode.org/reports/tr31</a>&gt;. </p>
<p> Any character not matched by <tt>&quot;\w&quot;</tt> is matched by <tt>&quot;\W&quot;</tt>. </p>
<p> <i>Whitespace</i> </p>
<p> <tt>&quot;\s&quot;</tt> matches any single character considered whitespace.</p>
<dl>
<dt>If the &quot;/a&quot; modifier is in effect &#8230;</p>
<dd> In all Perl versions, <tt>&quot;\s&quot;</tt> matches the 5 characters [	
 ]; that is, the horizontal tab, the newline, the form feed, the carriage return, and the space. Starting in Perl v5.18, it also matches the vertical tab, <tt>&quot;
