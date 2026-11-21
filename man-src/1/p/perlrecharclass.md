---
title: "perlrecharclass(1)"
name: "perlrecharclass"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrecharclass/"
description: "perlrecharclass – Perl Regular Expression Character Classes"
---
<h2 class="name">NAME</h2>
<p> perlrecharclass - Perl Regular Expression Character Classes </p>
<h2>DESCRIPTION</h2>
<p> The top level documentation about Perl regular expressions is found in perlre. </p>
<p> This manual page discusses the syntax and use of character classes in Perl regular expressions. </p>
<p> A character class is a way of denoting a set of characters in such a way that one character of the set is matched. It&#8217;s important to remember that: matching a character class consumes exactly one character in the source string. (The source string is the string the regular expression is matched against.) </p>
<p> There are three types of character classes in Perl regular expressions: the dot, backslash sequences, and the form enclosed in square brackets. Keep in mind, though, that often the term ``character class&#8217;&#8216; is used to mean just the bracketed form. Certainly, most Perl documentation does that.  </p>
<h3>The dot</h3>
<p> The dot (or period), <code>&quot;.&quot;</code> is probably the most used, and certainly the most well-known character class. By default, a dot matches any character, except for the newline. That default can be changed to add matching the newline by using the <i>single line</i> modifier: for the entire regular expression with the <code>&quot;/s&quot;</code> modifier, or locally with <code>&quot;(?s)&quot;</code> (and even globally within the scope of <code>&quot;use re &#8216;/s&#8217;&quot;</code>). (The <code>&quot;\N&quot;</code> backslash sequence, described below, matches any character except newline without regard to the <i>single line</i> modifier.) </p>
<p> Here are some examples: </p>
<pre><code> &quot;a&quot; =~ /./ # Match
 &quot;.&quot; =~ /./ # Match
 &quot;&quot; =~ /./ # No match (dot has to match a character)
 &quot;\n&quot; =~ /./ # No match (dot does not match a newline)
 &quot;\n&quot; =~ /./s # Match (global 'single line' modifier)
 &quot;\n&quot; =~ /(?s:.)/ # Match (local 'single line' modifier)
 &quot;ab&quot; =~ /^.$/ # No match (dot matches one character)
</code></pre>
<h3>Backslash sequences</h3>
<p> A backslash sequence is a sequence of characters, the first one of which is a backslash. Perl ascribes special meaning to many such sequences, and some of these are character classes. That is, they match a single character each, provided that the character belongs to the specific set of characters defined by the sequence. </p>
<p> Here&#8217;s a list of the backslash sequences that are character classes. They are discussed in more detail below. (For the backslash sequences that aren&#8217;t character classes, see perlrebackslash.) </p>
<pre><code> \d Match a decimal digit character.
 \D Match a non-decimal-digit character.
 \w Match a &quot;word&quot; character.
 \W Match a non-&quot;word&quot; character.
 \s Match a whitespace character.
 \S Match a non-whitespace character.
 \h Match a horizontal whitespace character.
 \H Match a character that isn't horizontal whitespace.
 \v Match a vertical whitespace character.
 \V Match a character that isn't vertical whitespace.
 \N Match a character that isn't a newline.
 \pP, \p{Prop} Match a character that has the given Unicode property.
 \PP, \P{Prop} Match a character that doesn't have the Unicode property
</code></pre>
<p> <i>\N</i> </p>
<p> <code>&quot;\N&quot;</code>, available starting in v5.12, like the dot, matches any character that is not a newline. The difference is that <code>&quot;\N&quot;</code> is not influenced by the <i>single line</i> regular expression modifier (see ``The dot&#8217;&#8216; above). Note that the form <code>&quot;\N{...}&quot;</code> may mean something completely different. When the <code>&quot;{...}&quot;</code> is a quantifier, it means to match a non-newline character that many times. For example, <code>&quot;\N{3}&quot;</code> means to match 3 non-newlines; <code>&quot;\N{5,}&quot;</code> means to match 5 or more non-newlines. But if <code>&quot;{...}&quot;</code> is not a legal quantifier, it is presumed to be a named character. See charnames for those. For example, none of <code>&quot;\N{COLON}&quot;</code>, <code>&quot;\N{4F}&quot;</code>, and <code>&quot;\N{F4}&quot;</code> contain legal quantifiers, so Perl will try to find characters whose names are respectively <code>&quot;COLON&quot;</code>, <code>&quot;4F&quot;</code>, and <code>&quot;F4&quot;</code>. </p>
<p> <i>Digits</i> </p>
<p> <code>&quot;\d&quot;</code> matches a single character considered to be a decimal <i>digit</i>. If the <code>&quot;/a&quot;</code> regular expression modifier is in effect, it matches [0-9]. Otherwise, it matches anything that is matched by <code>&quot;\p{Digit}&quot;</code>, which includes [0-9]. (An unlikely possible exception is that under locale matching rules, the current locale might not have <code>&quot;[0-9]&quot;</code> matched by <code>&quot;\d&quot;</code>, and/or might match other characters whose code point is less than 256. The only such locale definitions that are legal would be to match <code>&quot;[0-9]&quot;</code> plus another set of 10 consecutive digit characters; anything else would be in violation of the C language standard, but Perl doesn&#8217;t currently assume anything in regard to this.) </p>
<p> What this means is that unless the <code>&quot;/a&quot;</code> modifier is in effect <code>&quot;\d&quot;</code> not only matches the digits &#8216;0&#8217; - &#8216;9&#8217;, but also Arabic, Devanagari, and digits from other languages. This may cause some confusion, and some security issues. </p>
<p> Some digits that <code>&quot;\d&quot;</code> matches look like some of the [0-9] ones, but have different values. For example, <font SIZE="-1">BENGALI DIGIT FOUR</font> (U+09EA) looks very much like an <font SIZE="-1">ASCII DIGIT EIGHT</font> (U+0038), and <font SIZE="-1">LEPCHA DIGIT SIX</font> (U+1C46) looks very much like an <font SIZE="-1">ASCII DIGIT FIVE</font> (U+0035). An application that is expecting only the <font SIZE="-1">ASCII</font> digits might be misled, or if the match is <code>&quot;\d+&quot;</code>, the matched string might contain a mixture of digits from different writing systems that look like they signify a number different than they actually do. ``<code>num()</code>&#8216;&#8216; in Unicode::UCD can be used to safely calculate the value, returning <code>&quot;undef&quot;</code> if the input string contains such a mixture. Otherwise, for example, a displayed price might be deliberately different than it appears. </p>
<p> What <code>&quot;\p{Digit}&quot;</code> means (and hence <code>&quot;\d&quot;</code> except under the <code>&quot;/a&quot;</code> modifier) is <code>&quot;\p{General_Category=Decimal_Number}&quot;</code>, or synonymously, <code>&quot;\p{General_Category=Digit}&quot;</code>. Starting with Unicode version 4.1, this is the same set of characters matched by <code>&quot;\p{Numeric_Type=Decimal}&quot;</code>. But Unicode also has a different property with a similar name, <code>&quot;\p{Numeric_Type=Digit}&quot;</code>, which matches a completely different set of characters. These characters are things such as <code>&quot;CIRCLED DIGIT ONE&quot;</code> or subscripts, or are from writing systems that lack all ten digits. </p>
<p> The design intent is for <code>&quot;\d&quot;</code> to exactly match the set of characters that can safely be used with ``normal&#8217;&#8216; big-endian positional decimal syntax, where, for example 123 means one &#8216;hundred&#8217;, plus two &#8216;tens&#8217;, plus three &#8216;ones&#8217;. This positional notation does not necessarily apply to characters that match the other type of ``digit&#8217;&#8216;, <code>&quot;\p{Numeric_Type=Digit}&quot;</code>, and so <code>&quot;\d&quot;</code> doesn&#8217;t match them. </p>
<p> The Tamil digits (U+0BE6 - U+0BEF) can also legally be used in old-style Tamil numbers in which they would appear no more than one in a row, separated by characters that mean ``times 10&#8217;&#8216;, ``times 100&#8217;&#8216;, etc. (See &lt;<a rel="nofollow" href="http://www.unicode.org/notes/tn21">http://www.unicode.org/notes/tn21</a>&gt;.) </p>
<p> Any character not matched by <code>&quot;\d&quot;</code> is matched by <code>&quot;\D&quot;</code>. </p>
<p> <i>Word characters</i> </p>
<p> A <code>&quot;\w&quot;</code> matches a single alphanumeric character (an alphabetic character, or a decimal digit); or a connecting punctuation character, such as an underscore (``_&#8216;&#8216;); or a ``mark&#8217;&#8216; character (like some sort of accent) that attaches to one of those. It does not match a whole word. To match a whole word, use <code>&quot;\w+&quot;</code>. This isn&#8217;t the same thing as matching an English word, but in the <font SIZE="-1">ASCII</font> range it is the same as a string of Perl-identifier characters. </p>
<dl>
<dt>If the &quot;/a&quot; modifier is in effect ...</dt>
<dd> <p> <code>&quot;\w&quot;</code> matches the 63 characters [a-zA-Z0-9_]. </p>
 </dd>
<dt>otherwise ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>For code points above 255 ...</dt>
<dd> <p> <code>&quot;\w&quot;</code> matches the same as <code>&quot;\p{Word}&quot;</code> matches in this range. That is, it matches Thai letters, Greek letters, etc. This includes connector punctuation (like the underscore) which connect two words together, or diacritics, such as a <code>&quot;COMBINING TILDE&quot;</code> and the modifier letters, which are generally used to add auxiliary markings to letters. </p>
 </dd>
<dt>For code points below 256 ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>if locale rules are in effect ...</dt>
<dd> <p> <code>&quot;\w&quot;</code> matches the platform&#8217;s native underscore character plus whatever the locale considers to be alphanumeric. </p>
 </dd>
<dt>if, instead, Unicode rules are in effect ...</dt>
<dd> <p> <code>&quot;\w&quot;</code> matches exactly what <code>&quot;\p{Word}&quot;</code> matches. </p>
 </dd>
<dt>otherwise ...</dt>
<dd> <p> <code>&quot;\w&quot;</code> matches [a-zA-Z0-9_]. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<p> Which rules apply are determined as described in ``Which character set modifier is in effect?&#8216;&#8216; in perlre. </p>
<p> There are a number of security issues with the full Unicode list of word characters. See &lt;<a rel="nofollow" href="http://unicode.org/reports/tr36">http://unicode.org/reports/tr36</a>&gt;. </p>
<p> Also, for a somewhat finer-grained set of characters that are in programming language identifiers beyond the <font SIZE="-1">ASCII</font> range, you may wish to instead use the more customized ``Unicode Properties&#8217;&#8216;, <code>&quot;\p{ID_Start}&quot;</code>, <code>&quot;\p{ID_Continue}&quot;</code>, <code>&quot;\p{XID_Start}&quot;</code>, and <code>&quot;\p{XID_Continue}&quot;</code>. See &lt;<a rel="nofollow" href="http://unicode.org/reports/tr31">http://unicode.org/reports/tr31</a>&gt;. </p>
<p> Any character not matched by <code>&quot;\w&quot;</code> is matched by <code>&quot;\W&quot;</code>. </p>
<p> <i>Whitespace</i> </p>
<p> <code>&quot;\s&quot;</code> matches any single character considered whitespace. </p>
<dl>
<dt>If the &quot;/a&quot; modifier is in effect ...</dt>
<dd> <p> In all Perl versions, <code>&quot;\s&quot;</code> matches the 5 characters [\t\n\f\r ]; that is, the horizontal tab, the newline, the form feed, the carriage return, and the space. Starting in Perl v5.18, it also matches the vertical tab, <code>&quot;\cK&quot;</code>. See note <code>&quot;[1]&quot;</code> below for a discussion of this. </p>
 </dd>
<dt>otherwise ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>For code points above 255 ...</dt>
<dd> <p> <code>&quot;\s&quot;</code> matches exactly the code points above 255 shown with an ``s&#8217;&#8216; column in the table below. </p>
 </dd>
<dt>For code points below 256 ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>if locale rules are in effect ...</dt>
<dd> <p> <code>&quot;\s&quot;</code> matches whatever the locale considers to be whitespace. </p>
 </dd>
<dt>if, instead, Unicode rules are in effect ...</dt>
<dd> <p> <code>&quot;\s&quot;</code> matches exactly the characters shown with an ``s&#8217;&#8216; column in the table below. </p>
 </dd>
<dt>otherwise ...</dt>
<dd> <p> <code>&quot;\s&quot;</code> matches [\t\n\f\r ] and, starting in Perl v5.18, the vertical tab, <code>&quot;\cK&quot;</code>. (See note <code>&quot;[1]&quot;</code> below for a discussion of this.) Note that this list doesn&#8217;t include the non-breaking space. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<p> Which rules apply are determined as described in ``Which character set modifier is in effect?&#8216;&#8216; in perlre. </p>
<p> Any character not matched by <code>&quot;\s&quot;</code> is matched by <code>&quot;\S&quot;</code>. </p>
<p> <code>&quot;\h&quot;</code> matches any character considered horizontal whitespace; this includes the platform&#8217;s space and tab characters and several others listed in the table below. <code>&quot;\H&quot;</code> matches any character not considered horizontal whitespace. They use the platform&#8217;s native character set, and do not consider any locale that may otherwise be in use. </p>
<p> <code>&quot;\v&quot;</code> matches any character considered vertical whitespace; this includes the platform&#8217;s carriage return and line feed characters (newline) plus several other characters, all listed in the table below. <code>&quot;\V&quot;</code> matches any character not considered vertical whitespace. They use the platform&#8217;s native character set, and do not consider any locale that may otherwise be in use. </p>
<p> <code>&quot;\R&quot;</code> matches anything that can be considered a newline under Unicode rules. It can match a multi-character sequence. It cannot be used inside a bracketed character class; use <code>&quot;\v&quot;</code> instead (vertical whitespace). It uses the platform&#8217;s native character set, and does not consider any locale that may otherwise be in use. Details are discussed in perlrebackslash. </p>
<p> Note that unlike <code>&quot;\s&quot;</code> (and <code>&quot;\d&quot;</code> and <code>&quot;\w&quot;</code>), <code>&quot;\h&quot;</code> and <code>&quot;\v&quot;</code> always match the same characters, without regard to other factors, such as the active locale or whether the source string is in <font SIZE="-1">UTF-8</font> format. </p>
<p> One might think that <code>&quot;\s&quot;</code> is equivalent to <code>&quot;[\h\v]&quot;</code>. This is indeed true starting in Perl v5.18, but prior to that, the sole difference was that the vertical tab (<code>&quot;\cK&quot;</code>) was not matched by <code>&quot;\s&quot;</code>. </p>
<p> The following table is a complete listing of characters matched by <code>&quot;\s&quot;</code>, <code>&quot;\h&quot;</code> and <code>&quot;\v&quot;</code> as of Unicode 6.3. </p>
<p> The first column gives the Unicode code point of the character (in hex format), the second column gives the (Unicode) name. The third column indicates by which class(es) the character is matched (assuming no locale is in effect that changes the <code>&quot;\s&quot;</code> matching). </p>
<pre><code> 0x0009 CHARACTER TABULATION h s
 0x000a LINE FEED (LF) vs
 0x000b LINE TABULATION vs [1]
 0x000c FORM FEED (FF) vs
 0x000d CARRIAGE RETURN (CR) vs
 0x0020 SPACE h s
 0x0085 NEXT LINE (NEL) vs [2]
 0x00a0 NO-BREAK SPACE h s [2]
 0x1680 OGHAM SPACE MARK h s
 0x2000 EN QUAD h s
 0x2001 EM QUAD h s
 0x2002 EN SPACE h s
 0x2003 EM SPACE h s
 0x2004 THREE-PER-EM SPACE h s
 0x2005 FOUR-PER-EM SPACE h s
 0x2006 SIX-PER-EM SPACE h s
 0x2007 FIGURE SPACE h s
 0x2008 PUNCTUATION SPACE h s
 0x2009 THIN SPACE h s
 0x200a HAIR SPACE h s
 0x2028 LINE SEPARATOR vs
 0x2029 PARAGRAPH SEPARATOR vs
 0x202f NARROW NO-BREAK SPACE h s
 0x205f MEDIUM MATHEMATICAL SPACE h s
 0x3000 IDEOGRAPHIC SPACE h s
</code></pre>
<dl>
<dt>[1]</dt>
<dd> <p> Prior to Perl v5.18, <code>&quot;\s&quot;</code> did not match the vertical tab. <code>&quot;[^\S\cK]&quot;</code> (obscurely) matches what <code>&quot;\s&quot;</code> traditionally did. </p>
 </dd>
<dt>[2]</dt>
<dd> <p> <font SIZE="-1">NEXT LINE</font> and NO-BREAK <font SIZE="-1">SPACE</font> may or may not match <code>&quot;\s&quot;</code> depending on the rules in effect. See the beginning of this section. </p>
 </dd></dl>
<p> <i>Unicode Properties</i> </p>
<p> <code>&quot;\pP&quot;</code> and <code>&quot;\p{Prop}&quot;</code> are character classes to match characters that fit given Unicode properties. One letter property names can be used in the <code>&quot;\pP&quot;</code> form, with the property name following the <code>&quot;\p&quot;</code>, otherwise, braces are required. When using braces, there is a single form, which is just the property name enclosed in the braces, and a compound form which looks like <code>&quot;\p{name=value}&quot;</code>, which means to match if the property ``name&#8217;&#8216; for the character has that particular ``value&#8217;&#8216;. For instance, a match for a number can be written as <code>&quot;/\pN/&quot;</code> or as <code>&quot;/\p{Number}/&quot;</code>, or as <code>&quot;/\p{Number=True}/&quot;</code>. Lowercase letters are matched by the property <i>Lowercase_Letter</i> which has the short form <i>Ll</i>. They need the braces, so are written as <code>&quot;/\p{Ll}/&quot;</code> or <code>&quot;/\p{Lowercase_Letter}/&quot;</code>, or <code>&quot;/\p{General_Category=Lowercase_Letter}/&quot;</code> (the underscores are optional). <code>&quot;/\pLl/&quot;</code> is valid, but means something different. It matches a two character string: a letter (Unicode property <code>&quot;\pL&quot;</code>), followed by a lowercase <code>&quot;l&quot;</code>. </p>
<p> What a Unicode property matches is never subject to locale rules, and if locale rules are not otherwise in effect, the use of a Unicode property will force the regular expression into using Unicode rules, if it isn&#8217;t already. </p>
<p> Note that almost all properties are immune to case-insensitive matching. That is, adding a <code>&quot;/i&quot;</code> regular expression modifier does not change what they match. There are two sets that are affected. The first set is <code>&quot;Uppercase_Letter&quot;</code>, <code>&quot;Lowercase_Letter&quot;</code>, and <code>&quot;Titlecase_Letter&quot;</code>, all of which match <code>&quot;Cased_Letter&quot;</code> under <code>&quot;/i&quot;</code> matching. The second set is <code>&quot;Uppercase&quot;</code>, <code>&quot;Lowercase&quot;</code>, and <code>&quot;Titlecase&quot;</code>, all of which match <code>&quot;Cased&quot;</code> under <code>&quot;/i&quot;</code> matching. (The difference between these sets is that some things, such as Roman numerals, come in both upper and lower case, so they are <code>&quot;Cased&quot;</code>, but aren&#8217;t considered to be letters, so they aren&#8217;t <code>&quot;Cased_Letter&quot;</code>s. They&#8217;re actually <code>&quot;Letter_Number&quot;</code>s.) This set also includes its subsets <code>&quot;PosixUpper&quot;</code> and <code>&quot;PosixLower&quot;</code>, both of which under <code>&quot;/i&quot;</code> match <code>&quot;PosixAlpha&quot;</code>. </p>
<p> For more details on Unicode properties, see ``Unicode Character Properties&#8217;&#8216; in perlunicode; for a complete list of possible properties, see ``Properties accessible through \p{} and \P{}&#8216;&#8216; in perluniprops, which notes all forms that have <code>&quot;/i&quot;</code> differences. It is also possible to define your own properties. This is discussed in ``User-Defined Character Properties&#8217;&#8216; in perlunicode. </p>
<p> Unicode properties are defined (surprise!) only on Unicode code points. Starting in v5.20, when matching against <code>&quot;\p&quot;</code> and <code>&quot;\P&quot;</code>, Perl treats non-Unicode code points (those above the legal Unicode maximum of 0x10FFFF) as if they were typical unassigned Unicode code points. </p>
<p> Prior to v5.20, Perl raised a warning and made all matches fail on non-Unicode code points. This could be somewhat surprising: </p>
<pre><code> chr(0x110000) =~ \p{ASCII_Hex_Digit=True} # Fails on Perls &lt; v5.20.
 chr(0x110000) =~ \p{ASCII_Hex_Digit=False} # Also fails on Perls
                                               # &lt; v5.20
</code></pre>
<p> Even though these two matches might be thought of as complements, until v5.20 they were so only on Unicode code points. </p>
<p> Starting in perl v5.30, wildcards are allowed in Unicode property values. See ``Wildcards in Property Values&#8217;&#8216; in perlunicode. </p>
<p> Examples </p>
<pre><code> &quot;a&quot; =~ /\w/ # Match, &quot;a&quot; is a 'word' character.
 &quot;7&quot; =~ /\w/ # Match, &quot;7&quot; is a 'word' character as well.
 &quot;a&quot; =~ /\d/ # No match, &quot;a&quot; isn't a digit.
 &quot;7&quot; =~ /\d/ # Match, &quot;7&quot; is a digit.
 &quot; &quot; =~ /\s/ # Match, a space is whitespace.
 &quot;a&quot; =~ /\D/ # Match, &quot;a&quot; is a non-digit.
 &quot;7&quot; =~ /\D/ # No match, &quot;7&quot; is not a non-digit.
 &quot; &quot; =~ /\S/ # No match, a space is not non-whitespace.
 &quot; &quot; =~ /\h/ # Match, space is horizontal whitespace.
 &quot; &quot; =~ /\v/ # No match, space is not vertical whitespace.
 &quot;\r&quot; =~ /\v/ # Match, a return is vertical whitespace.
 &quot;a&quot; =~ /\pL/ # Match, &quot;a&quot; is a letter.
 &quot;a&quot; =~ /\p{Lu}/ # No match, /\p{Lu}/ matches upper case letters.
 &quot;\x{0e0b}&quot; =~ /\p{Thai}/ # Match, \x{0e0b} is the character
                           # 'THAI CHARACTER SO SO', and that's in
                           # Thai Unicode class.
 &quot;a&quot; =~ /\P{Lao}/ # Match, as &quot;a&quot; is not a Laotian character.
</code></pre>
<p> It is worth emphasizing that <code>&quot;\d&quot;</code>, <code>&quot;\w&quot;</code>, etc, match single characters, not complete numbers or words. To match a number (that consists of digits), use <code>&quot;\d+&quot;</code>; to match a word, use <code>&quot;\w+&quot;</code>. But be aware of the security considerations in doing so, as mentioned above.  </p>
<h3>Bracketed Character Classes</h3>
<p> The third form of character class you can use in Perl regular expressions is the bracketed character class. In its simplest form, it lists the characters that may be matched, surrounded by square brackets, like this: <code>&quot;[aeiou]&quot;</code>. This matches one of <code>&quot;a&quot;</code>, <code>&quot;e&quot;</code>, <code>&quot;i&quot;</code>, <code>&quot;o&quot;</code> or <code>&quot;u&quot;</code>. Like the other character classes, exactly one character is matched.* To match a longer string consisting of characters mentioned in the character class, follow the character class with a quantifier. For instance, <code>&quot;[aeiou]+&quot;</code> matches one or more lowercase English vowels. </p>
<p> Repeating a character in a character class has no effect; it&#8217;s considered to be in the set only once. </p>
<p> Examples: </p>
<pre><code> &quot;e&quot; =~ /[aeiou]/ # Match, as &quot;e&quot; is listed in the class.
 &quot;p&quot; =~ /[aeiou]/ # No match, &quot;p&quot; is not listed in the class.
 &quot;ae&quot; =~ /^[aeiou]$/ # No match, a character class only matches
                           # a single character.
 &quot;ae&quot; =~ /^[aeiou]+$/ # Match, due to the quantifier.
 -------
</code></pre>
<p> * There are two exceptions to a bracketed character class matching a single character only. Each requires special handling by Perl to make things work: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> When the class is to match caselessly under <code>&quot;/i&quot;</code> matching rules, and a character that is explicitly mentioned inside the class matches a multiple-character sequence caselessly under Unicode rules, the class will also match that sequence. For example, Unicode says that the letter <code>&quot;LATIN SMALL LETTER SHARP S&quot;</code> should match the sequence <code>&quot;ss&quot;</code> under <code>&quot;/i&quot;</code> rules. Thus, </p>
<pre><code> 'ss' =~ /\A\N{LATIN SMALL LETTER SHARP S}\z/i # Matches
 'ss' =~ /\A[aeioust\N{LATIN SMALL LETTER SHARP S}]\z/i # Matches
</code></pre>
<p> For this to happen, the class must not be inverted (see ``Negation&#8217;&#8216;) and the character must be explicitly specified, and not be part of a multi-character range (not even as one of its endpoints). (``Character Ranges&#8217;&#8216; will be explained shortly.) Therefore, </p>
<pre><code> 'ss' =~ /\A[\0-\x{ff}]\z/ui # Doesn't match
 'ss' =~ /\A[\0-\N{LATIN SMALL LETTER SHARP S}]\z/ui # No match
 'ss' =~ /\A[\xDF-\xDF]\z/ui # Matches on ASCII platforms, since
                               # \xDF is LATIN SMALL LETTER SHARP S,
                               # and the range is just a single
                               # element
</code></pre>
<p> Note that it isn&#8217;t a good idea to specify these types of ranges anyway. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some names known to <code>&quot;\N{...}&quot;</code> refer to a sequence of multiple characters, instead of the usual single character. When one of these is included in the class, the entire sequence is matched. For example, </p>
<pre><code>  &quot;\N{TAMIL LETTER KA}\N{TAMIL VOWEL SIGN AU}&quot;
                              =~ / ^ [\N{TAMIL SYLLABLE KAU}] $ /x;
</code></pre>
<p> matches, because <code>&quot;\N{TAMIL SYLLABLE KAU}&quot;</code> is a named sequence consisting of the two characters matched against. Like the other instance where a bracketed class can match multiple characters, and for similar reasons, the class must not be inverted, and the named sequence may not appear in a range, even one where it is both endpoints. If these happen, it is a fatal error if the character class is within the scope of <code>&quot;use re &#8216;strict&quot;</code>, or within an extended <code>&quot;(?[...])&quot;</code> class; otherwise only the first code point is used (with a <code>&quot;regexp&quot;</code>-type warning raised). </p>
 </dd></dl>
<p> <i>Special Characters Inside a Bracketed Character Class</i> </p>
<p> Most characters that are meta characters in regular expressions (that is, characters that carry a special meaning like <code>&quot;.&quot;</code>, <code>&quot;*&quot;</code>, or <code>&quot;(&quot;</code>) lose their special meaning and can be used inside a character class without the need to escape them. For instance, <code>&quot;[()]&quot;</code> matches either an opening parenthesis, or a closing parenthesis, and the parens inside the character class don&#8217;t group or capture. Be aware that, unless the pattern is evaluated in single-quotish context, variable interpolation will take place before the bracketed class is parsed: </p>
<pre><code> $, = &quot;\t| &quot;;
 $a =~ m'[$,]'; # single-quotish: matches '$' or ','
 $a =~ q{[$,]}' # same
 $a =~ m/[$,]/; # double-quotish: matches &quot;\t&quot;, &quot;|&quot;, or &quot; &quot;
</code></pre>
<p> Characters that may carry a special meaning inside a character class are: <code>&quot;\&quot;</code>, <code>&quot;^&quot;</code>, <code>&quot;-&quot;</code>, <code>&quot;[&quot;</code> and <code>&quot;]&quot;</code>, and are discussed below. They can be escaped with a backslash, although this is sometimes not needed, in which case the backslash may be omitted. </p>
<p> The sequence <code>&quot;\b&quot;</code> is special inside a bracketed character class. While outside the character class, <code>&quot;\b&quot;</code> is an assertion indicating a point that does not have either two word characters or two non-word characters on either side, inside a bracketed character class, <code>&quot;\b&quot;</code> matches a backspace character. </p>
<p> The sequences <code>&quot;\a&quot;</code>, <code>&quot;\c&quot;</code>, <code>&quot;\e&quot;</code>, <code>&quot;\f&quot;</code>, <code>&quot;\n&quot;</code>, <code>&quot;\N{</code>NAME <code>}&quot;</code>, <code>&quot;\N{U+</code>hex char <code>}&quot;</code>, <code>&quot;\r&quot;</code>, <code>&quot;\t&quot;</code>, and <code>&quot;\x&quot;</code> are also special and have the same meanings as they do outside a bracketed character class. </p>
<p> Also, a backslash followed by two or three octal digits is considered an octal number. </p>
<p> A <code>&quot;[&quot;</code> is not special inside a character class, unless it&#8217;s the start of a <font SIZE="-1">POSIX</font> character class (see ``<font SIZE="-1">POSIX</font> Character Classes&#8217;&#8216; below). It normally does not need escaping. </p>
<p> A <code>&quot;]&quot;</code> is normally either the end of a <font SIZE="-1">POSIX</font> character class (see ``<font SIZE="-1">POSIX</font> Character Classes&#8217;&#8216; below), or it signals the end of the bracketed character class. If you want to include a <code>&quot;]&quot;</code> in the set of characters, you must generally escape it. </p>
<p> However, if the <code>&quot;]&quot;</code> is the <i>first</i> (or the second if the first character is a caret) character of a bracketed character class, it does not denote the end of the class (as you cannot have an empty class) and is considered part of the set of characters that can be matched without escaping. </p>
<p> Examples: </p>
<pre><code> &quot;+&quot; =~ /[+?*]/ # Match, &quot;+&quot; in a character class is not special.
 &quot;\cH&quot; =~ /[\b]/ # Match, \b inside in a character class
                      # is equivalent to a backspace.
 &quot;]&quot; =~ /[][]/ # Match, as the character class contains
                      # both [ and ].
 &quot;[]&quot; =~ /[[]]/ # Match, the pattern contains a character class
                      # containing just [, and the character class is
                      # followed by a ].
</code></pre>
<p> <i>Bracketed Character Classes and the </i>&quot;/xx&quot;<i> pattern modifier</i> </p>
<p> Normally <font SIZE="-1">SPACE</font> and <font SIZE="-1">TAB</font> characters have no special meaning inside a bracketed character class; they are just added to the list of characters matched by the class. But if the <code>&quot;/xx&quot;</code> pattern modifier is in effect, they are generally ignored and can be added to improve readability. They can&#8217;t be added in the middle of a single construct: </p>
<pre><code> / [ \x{10 FFFF} ] /xx # WRONG!
</code></pre>
<p> The <font SIZE="-1">SPACE</font> in the middle of the hex constant is illegal. </p>
<p> To specify a literal <font SIZE="-1">SPACE</font> character, you can escape it with a backslash, like: </p>
<pre><code> /[ a e i o u \ ]/xx
</code></pre>
<p> This matches the English vowels plus the <font SIZE="-1">SPACE</font> character. </p>
<p> For clarity, you should already have been using <code>&quot;\t&quot;</code> to specify a literal tab, and <code>&quot;\t&quot;</code> is unaffected by <code>&quot;/xx&quot;</code>. </p>
<p> <i>Character Ranges</i> </p>
<p> It is not uncommon to want to match a range of characters. Luckily, instead of listing all characters in the range, one may use the hyphen (<code>&quot;-&quot;</code>). If inside a bracketed character class you have two characters separated by a hyphen, it&#8217;s treated as if all characters between the two were in the class. For instance, <code>&quot;[0-9]&quot;</code> matches any <font SIZE="-1">ASCII</font> digit, and <code>&quot;[a-m]&quot;</code> matches any lowercase letter from the first half of the <font SIZE="-1">ASCII</font> alphabet. </p>
<p> Note that the two characters on either side of the hyphen are not necessarily both letters or both digits. Any character is possible, although not advisable. <code>&quot;[&#8216;-?]&quot;</code> contains a range of characters, but most people will not know which characters that means. Furthermore, such ranges may lead to portability problems if the code has to run on a platform that uses a different character set, such as <font SIZE="-1">EBCDIC.</font> </p>
<p> If a hyphen in a character class cannot syntactically be part of a range, for instance because it is the first or the last character of the character class, or if it immediately follows a range, the hyphen isn&#8217;t special, and so is considered a character to be matched literally. If you want a hyphen in your set of characters to be matched and its position in the class is such that it could be considered part of a range, you must escape that hyphen with a backslash. </p>
<p> Examples: </p>
<pre><code> [a-z] # Matches a character that is a lower case ASCII letter.
 [a-fz] # Matches any letter between 'a' and 'f' (inclusive) or
             # the letter 'z'.
 [-z] # Matches either a hyphen ('-') or the letter 'z'.
 [a-f-m] # Matches any letter between 'a' and 'f' (inclusive), the
             # hyphen ('-'), or the letter 'm'.
 ['-?] # Matches any of the characters '()*+,-./0123456789:;&lt;=&gt;?
             # (But not on an EBCDIC platform).
 [\N{APOSTROPHE}-\N{QUESTION MARK}]
             # Matches any of the characters '()*+,-./0123456789:;&lt;=&gt;?
             # even on an EBCDIC platform.
 [\N{U+27}-\N{U+3F}] # Same. (U+27 is &quot;'&quot;, and U+3F is &quot;?&quot;)
</code></pre>
<p> As the final two examples above show, you can achieve portability to non-ASCII platforms by using the <code>&quot;\N{...}&quot;</code> form for the range endpoints. These indicate that the specified range is to be interpreted using Unicode values, so <code>&quot;[\N{U+27}-\N{U+3F}]&quot;</code> means to match <code>&quot;\N{U+27}&quot;</code>, <code>&quot;\N{U+28}&quot;</code>, <code>&quot;\N{U+29}&quot;</code>, ..., <code>&quot;\N{U+3D}&quot;</code>, <code>&quot;\N{U+3E}&quot;</code>, and <code>&quot;\N{U+3F}&quot;</code>, whatever the native code point versions for those are. These are called ``Unicode&#8217;&#8216; ranges. If either end is of the <code>&quot;\N{...}&quot;</code> form, the range is considered Unicode. A <code>&quot;regexp&quot;</code> warning is raised under <code>&quot;use re &#8216;strict&#8217;&quot;</code> if the other endpoint is specified non-portably: </p>
<pre><code> [\N{U+00}-\x09] # Warning under re 'strict'; \x09 is non-portable
 [\N{U+00}-\t] # No warning;
</code></pre>
<p> Both of the above match the characters <code>&quot;\N{U+00}&quot;</code> <code>&quot;\N{U+01}&quot;</code>, ... <code>&quot;\N{U+08}&quot;</code>, <code>&quot;\N{U+09}&quot;</code>, but the <code>&quot;\x09&quot;</code> looks like it could be a mistake so the warning is raised (under <code>&quot;re &#8216;strict&#8217;&quot;</code>) for it. </p>
<p> Perl also guarantees that the ranges <code>&quot;A-Z&quot;</code>, <code>&quot;a-z&quot;</code>, <code>&quot;0-9&quot;</code>, and any subranges of these match what an English-only speaker would expect them to match on any platform. That is, <code>&quot;[A-Z]&quot;</code> matches the 26 <font SIZE="-1">ASCII</font> uppercase letters; <code>&quot;[a-z]&quot;</code> matches the 26 lowercase letters; and <code>&quot;[0-9]&quot;</code> matches the 10 digits. Subranges, like <code>&quot;[h-k]&quot;</code>, match correspondingly, in this case just the four letters <code>&quot;h&quot;</code>, <code>&quot;i&quot;</code>, <code>&quot;j&quot;</code>, and <code>&quot;k&quot;</code>. This is the natural behavior on <font SIZE="-1">ASCII</font> platforms where the code points (ordinal values) for <code>&quot;h&quot;</code> through <code>&quot;k&quot;</code> are consecutive integers (0x68 through 0x6B). But special handling to achieve this may be needed on platforms with a non-ASCII native character set. For example, on <font SIZE="-1">EBCDIC</font> platforms, the code point for <code>&quot;h&quot;</code> is 0x88, <code>&quot;i&quot;</code> is 0x89, <code>&quot;j&quot;</code> is 0x91, and <code>&quot;k&quot;</code> is 0x92. Perl specially treats <code>&quot;[h-k]&quot;</code> to exclude the seven code points in the gap: 0x8A through 0x90. This special handling is only invoked when the range is a subrange of one of the <font SIZE="-1">ASCII</font> uppercase, lowercase, and digit ranges, <font SIZE="-1">AND</font> each end of the range is expressed either as a literal, like <code>&quot;A&quot;</code>, or as a named character (<code>&quot;\N{...}&quot;</code>, including the <code>&quot;\N{U+...&quot;</code> form). </p>
<p> <font SIZE="-1">EBCDIC</font> Examples: </p>
<pre><code> [i-j] # Matches either &quot;i&quot; or &quot;j&quot;
 [i-\N{LATIN SMALL LETTER J}] # Same
 [i-\N{U+6A}] # Same
 [\N{U+69}-\N{U+6A}] # Same
 [\x{89}-\x{91}] # Matches 0x89 (&quot;i&quot;), 0x8A .. 0x90, 0x91 (&quot;j&quot;)
 [i-\x{91}] # Same
 [\x{89}-j] # Same
 [i-J] # Matches, 0x89 (&quot;i&quot;) .. 0xC1 (&quot;J&quot;); special
                     # handling doesn't apply because range is mixed
                     # case
</code></pre>
<p> <i>Negation</i> </p>
<p> It is also possible to instead list the characters you do not want to match. You can do so by using a caret (<code>&quot;^&quot;</code>) as the first character in the character class. For instance, <code>&quot;[^a-z]&quot;</code> matches any character that is not a lowercase <font SIZE="-1">ASCII</font> letter, which therefore includes more than a million Unicode code points. The class is said to be ``negated&#8217;&#8216; or ``inverted&#8217;&#8216;. </p>
<p> This syntax make the caret a special character inside a bracketed character class, but only if it is the first character of the class. So if you want the caret as one of the characters to match, either escape the caret or else don&#8217;t list it first. </p>
<p> In inverted bracketed character classes, Perl ignores the Unicode rules that normally say that named sequence, and certain characters should match a sequence of multiple characters use under caseless <code>&quot;/i&quot;</code> matching. Following those rules could lead to highly confusing situations: </p>
<pre><code> &quot;ss&quot; =~ /^[^\xDF]+$/ui; # Matches!
</code></pre>
<p> This should match any sequences of characters that aren&#8217;t <code>&quot;\xDF&quot;</code> nor what <code>&quot;\xDF&quot;</code> matches under <code>&quot;/i&quot;</code>. <code>&quot;s&quot;</code> isn&#8217;t <code>&quot;\xDF&quot;</code>, but Unicode says that <code>&quot;ss&quot;</code> is what <code>&quot;\xDF&quot;</code> matches under <code>&quot;/i&quot;</code>. So which one ``wins&#8217;&#8216;? Do you fail the match because the string has <code>&quot;ss&quot;</code> or accept it because it has an <code>&quot;s&quot;</code> followed by another <code>&quot;s&quot;</code>? Perl has chosen the latter. (See note in ``Bracketed Character Classes&#8217;&#8216; above.) </p>
<p> Examples: </p>
<pre><code> &quot;e&quot; =~ /[^aeiou]/ # No match, the 'e' is listed.
 &quot;x&quot; =~ /[^aeiou]/ # Match, as 'x' isn't a lowercase vowel.
 &quot;^&quot; =~ /[^^]/ # No match, matches anything that isn't a caret.
 &quot;^&quot; =~ /[x^]/ # Match, caret is not special here.
</code></pre>
<p> <i>Backslash Sequences</i> </p>
<p> You can put any backslash sequence character class (with the exception of <code>&quot;\N&quot;</code> and <code>&quot;\R&quot;</code>) inside a bracketed character class, and it will act just as if you had put all characters matched by the backslash sequence inside the character class. For instance, <code>&quot;[a-f\d]&quot;</code> matches any decimal digit, or any of the lowercase letters between &#8216;a&#8217; and &#8216;f&#8217; inclusive. </p>
<p> <code>&quot;\N&quot;</code> within a bracketed character class must be of the forms <code>&quot;\N{</code>name <code>}&quot;</code> or <code>&quot;\N{U+</code>hex char <code>}&quot;</code>, and <font SIZE="-1">NOT</font> be the form that matches non-newlines, for the same reason that a dot <code>&quot;.&quot;</code> inside a bracketed character class loses its special meaning: it matches nearly anything, which generally isn&#8217;t what you want to happen. </p>
<p> Examples: </p>
<pre><code> /[\p{Thai}\d]/ # Matches a character that is either a Thai
                    # character, or a digit.
 /[^\p{Arabic}()]/ # Matches a character that is neither an Arabic
                    # character, nor a parenthesis.
</code></pre>
<p> Backslash sequence character classes cannot form one of the endpoints of a range. Thus, you can&#8217;t say: </p>
<pre><code> /[\p{Thai}-\d]/ # Wrong!
</code></pre>
<p> <i></i><font SIZE="-1"><i>POSIX</i></font><i> Character Classes</i> </p>
<p> <font SIZE="-1">POSIX</font> character classes have the form <code>&quot;[:class:]&quot;</code>, where <i>class</i> is the name, and the <code>&quot;[:&quot;</code> and <code>&quot;:]&quot;</code> delimiters. <font SIZE="-1">POSIX</font> character classes only appear <i>inside</i> bracketed character classes, and are a convenient and descriptive way of listing a group of characters. </p>
<p> Be careful about the syntax, </p>
<pre><code> # Correct:
 $string =~ /[[:alpha:]]/
 # Incorrect (will warn):
 $string =~ /[:alpha:]/
</code></pre>
<p> The latter pattern would be a character class consisting of a colon, and the letters <code>&quot;a&quot;</code>, <code>&quot;l&quot;</code>, <code>&quot;p&quot;</code> and <code>&quot;h&quot;</code>. </p>
<p> <font SIZE="-1">POSIX</font> character classes can be part of a larger bracketed character class. For example, </p>
<pre><code> [01[:alpha:]%]
</code></pre>
<p> is valid and matches &#8216;0&#8217;, &#8216;1&#8217;, any alphabetic character, and the percent sign. </p>
<p> Perl recognizes the following <font SIZE="-1">POSIX</font> character classes: </p>
<pre><code> alpha Any alphabetical character (e.g., [A-Za-z]).
 alnum Any alphanumeric character (e.g., [A-Za-z0-9]).
 ascii Any character in the ASCII character set.
 blank A GNU extension, equal to a space or a horizontal tab (&quot;\t&quot;).
 cntrl Any control character. See Note [2] below.
 digit Any decimal digit (e.g., [0-9]), equivalent to &quot;\d&quot;.
 graph Any printable character, excluding a space. See Note [3] below.
 lower Any lowercase character (e.g., [a-z]).
 print Any printable character, including a space. See Note [4] below.
 punct Any graphical character excluding &quot;word&quot; characters. Note [5].
 space Any whitespace character. &quot;\s&quot; including the vertical tab
        (&quot;\cK&quot;).
 upper Any uppercase character (e.g., [A-Z]).
 word A Perl extension (e.g., [A-Za-z0-9_]), equivalent to &quot;\w&quot;.
 xdigit Any hexadecimal digit (e.g., [0-9a-fA-F]). Note [7].
</code></pre>
<p> Like the Unicode properties, most of the <font SIZE="-1">POSIX</font> properties match the same regardless of whether case-insensitive (<code>&quot;/i&quot;</code>) matching is in effect or not. The two exceptions are <code>&quot;[:upper:]&quot;</code> and <code>&quot;[:lower:]&quot;</code>. Under <code>&quot;/i&quot;</code>, they each match the union of <code>&quot;[:upper:]&quot;</code> and <code>&quot;[:lower:]&quot;</code>. </p>
<p> Most <font SIZE="-1">POSIX</font> character classes have two Unicode-style <code>&quot;\p&quot;</code> property counterparts. (They are not official Unicode properties, but Perl extensions derived from official Unicode properties.) The table below shows the relation between <font SIZE="-1">POSIX</font> character classes and these counterparts. </p>
<p> One counterpart, in the column labelled ``ASCII-range Unicode&#8217;&#8216; in the table, matches only characters in the <font SIZE="-1">ASCII</font> character set. </p>
<p> The other counterpart, in the column labelled ``Full-range Unicode&#8217;&#8216;, matches any appropriate characters in the full Unicode character set. For example, <code>&quot;\p{Alpha}&quot;</code> matches not just the <font SIZE="-1">ASCII</font> alphabetic characters, but any character in the entire Unicode character set considered alphabetic. An entry in the column labelled ``backslash sequence&#8217;&#8216; is a (short) equivalent. </p>
<pre><code> [[:...:]] ASCII-range Full-range backslash Note
                 Unicode Unicode sequence
 -----------------------------------------------------
   alpha \p{PosixAlpha} \p{XPosixAlpha}
   alnum \p{PosixAlnum} \p{XPosixAlnum}
   ascii \p{ASCII}
   blank \p{PosixBlank} \p{XPosixBlank} \h [1]
                                   or \p{HorizSpace} [1]
   cntrl \p{PosixCntrl} \p{XPosixCntrl} [2]
   digit \p{PosixDigit} \p{XPosixDigit} \d
   graph \p{PosixGraph} \p{XPosixGraph} [3]
   lower \p{PosixLower} \p{XPosixLower}
   print \p{PosixPrint} \p{XPosixPrint} [4]
   punct \p{PosixPunct} \p{XPosixPunct} [5]
              \p{PerlSpace} \p{XPerlSpace} \s [6]
   space \p{PosixSpace} \p{XPosixSpace} [6]
   upper \p{PosixUpper} \p{XPosixUpper}
   word \p{PosixWord} \p{XPosixWord} \w
   xdigit \p{PosixXDigit} \p{XPosixXDigit} [7]
</code></pre>
<dl>
<dt>[1]</dt>
<dd> <p> <code>&quot;\p{Blank}&quot;</code> and <code>&quot;\p{HorizSpace}&quot;</code> are synonyms. </p>
 </dd>
<dt>[2]</dt>
<dd> <p> Control characters don&#8217;t produce output as such, but instead usually control the terminal somehow: for example, newline and backspace are control characters. On <font SIZE="-1">ASCII</font> platforms, in the <font SIZE="-1">ASCII</font> range, characters whose code points are between 0 and 31 inclusive, plus 127 (<code>&quot;DEL&quot;</code>) are control characters; on <font SIZE="-1">EBCDIC</font> platforms, their counterparts are control characters. </p>
 </dd>
<dt>[3]</dt>
<dd> <p> Any character that is <i>graphical</i>, that is, visible. This class consists of all alphanumeric characters and all punctuation characters. </p>
 </dd>
<dt>[4]</dt>
<dd> <p> All printable characters, which is the set of all graphical characters plus those whitespace characters which are not also controls. </p>
 </dd>
<dt>[5]</dt>
<dd> <p> <code>&quot;\p{PosixPunct}&quot;</code> and <code>&quot;[[:punct:]]&quot;</code> in the <font SIZE="-1">ASCII</font> range match all non-controls, non-alphanumeric, non-space characters: <code>&quot;[-!&quot;#$%&amp;&#8216;()*+,./:;&lt;=&gt;?@[\\\]^_`{|}~]&quot;</code> (although if a locale is in effect, it could alter the behavior of <code>&quot;[[:punct:]]&quot;</code>). </p>
<p> The similarly named property, <code>&quot;\p{Punct}&quot;</code>, matches a somewhat different set in the <font SIZE="-1">ASCII</font> range, namely <code>&quot;[-!&quot;#%&amp;&#8216;()*,./:;?@[\\\]_{}]&quot;</code>. That is, it is missing the nine characters <code>&quot;[$+&lt;=&gt;^`|~]&quot;</code>. This is because Unicode splits what <font SIZE="-1">POSIX</font> considers to be punctuation into two categories, Punctuation and Symbols. </p>
<p> <code>&quot;\p{XPosixPunct}&quot;</code> and (under Unicode rules) <code>&quot;[[:punct:]]&quot;</code>, match what <code>&quot;\p{PosixPunct}&quot;</code> matches in the <font SIZE="-1">ASCII</font> range, plus what <code>&quot;\p{Punct}&quot;</code> matches. This is different than strictly matching according to <code>&quot;\p{Punct}&quot;</code>. Another way to say it is that if Unicode rules are in effect, <code>&quot;[[:punct:]]&quot;</code> matches all characters that Unicode considers punctuation, plus all ASCII-range characters that Unicode considers symbols. </p>
 </dd>
<dt>[6]</dt>
<dd> <p> <code>&quot;\p{XPerlSpace}&quot;</code> and <code>&quot;\p{Space}&quot;</code> match identically starting with Perl v5.18. In earlier versions, these differ only in that in non-locale matching, <code>&quot;\p{XPerlSpace}&quot;</code> did not match the vertical tab, <code>&quot;\cK&quot;</code>. Same for the two ASCII-only range forms. </p>
 </dd>
<dt>[7]</dt>
<dd> <p> Unlike <code>&quot;[[:digit:]]&quot;</code> which matches digits in many writing systems, such as Thai and Devanagari, there are currently only two sets of hexadecimal digits, and it is unlikely that more will be added. This is because you not only need the ten digits, but also the six <code>&quot;[A-F]&quot;</code> (and <code>&quot;[a-f]&quot;</code>) to correspond. That means only the Latin script is suitable for these, and Unicode has only two sets of these, the familiar <font SIZE="-1">ASCII</font> set, and the fullwidth forms starting at U+FF10 (<font SIZE="-1">FULLWIDTH DIGIT ZERO</font>). </p>
 </dd></dl>
<p> There are various other synonyms that can be used besides the names listed in the table. For example, <code>&quot;\p{XPosixAlpha}&quot;</code> can be written as <code>&quot;\p{Alpha}&quot;</code>. All are listed in ``Properties accessible through \p{} and \P{}&#8216;&#8216; in perluniprops. </p>
<p> Both the <code>&quot;\p&quot;</code> counterparts always assume Unicode rules are in effect. On <font SIZE="-1">ASCII</font> platforms, this means they assume that the code points from 128 to 255 are Latin-1, and that means that using them under locale rules is unwise unless the locale is guaranteed to be Latin-1 or <font SIZE="-1">UTF-8.</font> In contrast, the <font SIZE="-1">POSIX</font> character classes are useful under locale rules. They are affected by the actual rules in effect, as follows: </p>
<dl>
<dt>If the &quot;/a&quot; modifier, is in effect ...</dt>
<dd> <p> Each of the <font SIZE="-1">POSIX</font> classes matches exactly the same as their ASCII-range counterparts. </p>
 </dd>
<dt>otherwise ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>For code points above 255 ...</dt>
<dd> <p> The <font SIZE="-1">POSIX</font> class matches the same as its Full-range counterpart. </p>
 </dd>
<dt>For code points below 256 ...</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>if locale rules are in effect ...</dt>
<dd> <p> The <font SIZE="-1">POSIX</font> class matches according to the locale, except: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;word&quot;</dt>
<dd> <p> also includes the platform&#8217;s native underscore character, no matter what the locale is. </p>
 </dd>
<dt>&quot;ascii&quot;</dt>
<dd> <p> on platforms that don&#8217;t have the <font SIZE="-1">POSIX</font> <code>&quot;ascii&quot;</code> extension, this matches just the platform&#8217;s native ASCII-range characters. </p>
 </dd>
<dt>&quot;blank&quot;</dt>
<dd> <p> on platforms that don&#8217;t have the <font SIZE="-1">POSIX</font> <code>&quot;blank&quot;</code> extension, this matches just the platform&#8217;s native tab and space characters. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>if, instead, Unicode rules are in effect ...</dt>
<dd> <p> The <font SIZE="-1">POSIX</font> class matches the same as the Full-range counterpart. </p>
 </dd>
<dt>otherwise ...</dt>
<dd> <p> The <font SIZE="-1">POSIX</font> class matches the same as the <font SIZE="-1">ASCII</font> range counterpart. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<p> Which rules apply are determined as described in ``Which character set modifier is in effect?&#8216;&#8216; in perlre. </p>
<p> Negation of <font SIZE="-1">POSIX</font> character classes </p>
<p> A Perl extension to the <font SIZE="-1">POSIX</font> character class is the ability to negate it. This is done by prefixing the class name with a caret (<code>&quot;^&quot;</code>). Some examples: </p>
<pre><code>     POSIX ASCII-range Full-range backslash
                    Unicode Unicode sequence
 -----------------------------------------------------
 [[:^digit:]] \P{PosixDigit} \P{XPosixDigit} \D
 [[:^space:]] \P{PosixSpace} \P{XPosixSpace}
                \P{PerlSpace} \P{XPerlSpace} \S
 [[:^word:]] \P{PerlWord} \P{XPosixWord} \W
</code></pre>
<p> The backslash sequence can mean either <font SIZE="-1">ASCII-</font> or Full-range Unicode, depending on various factors as described in ``Which character set modifier is in effect?&#8216;&#8216; in perlre. </p>
<p> [= =] and [. .] </p>
<p> Perl recognizes the <font SIZE="-1">POSIX</font> character classes <code>&quot;[=class=]&quot;</code> and <code>&quot;[.class.]&quot;</code>, but does not (yet?) support them. Any attempt to use either construct raises an exception. </p>
<p> Examples </p>
<pre><code> /[[:digit:]]/ # Matches a character that is a digit.
 /[01[:lower:]]/ # Matches a character that is either a
                          # lowercase letter, or '0' or '1'.
 /[[:digit:][:^xdigit:]]/ # Matches a character that can be anything
                          # except the letters 'a' to 'f' and 'A' to
                          # 'F'. This is because the main character
                          # class is composed of two POSIX character
                          # classes that are ORed together, one that
                          # matches any digit, and the other that
                          # matches anything that isn't a hex digit.
                          # The OR adds the digits, leaving only the
                          # letters 'a' to 'f' and 'A' to 'F' excluded.
</code></pre>
<p> <i>Extended Bracketed Character Classes</i> </p>
<p> This is a fancy bracketed character class that can be used for more readable and less error-prone classes, and to perform set operations, such as intersection. An example is </p>
<pre><code> /(?[ \p{Thai} &amp; \p{Digit} ])/
</code></pre>
<p> This will match all the digit characters that are in the Thai script. </p>
<p> This is an experimental feature available starting in 5.18, and is subject to change as we gain field experience with it. Any attempt to use it will raise a warning, unless disabled via </p>
<pre><code> no warnings &quot;experimental::regex_sets&quot;;
</code></pre>
<p> Comments on this feature are welcome; send email to <code>&quot;perl5-porters [at] perl.org&quot;</code>. </p>
<p> The rules used by <code>&quot;use re &#8216;strict&quot;</code> apply to this construct. </p>
<p> We can extend the example above: </p>
<pre><code> /(?[ ( \p{Thai} + \p{Lao} ) &amp; \p{Digit} ])/
</code></pre>
<p> This matches digits that are in either the Thai or Laotian scripts. </p>
<p> Notice the white space in these examples. This construct always has the <code>&quot;/xx&quot;</code> modifier turned on within it. </p>
<p> The available binary operators are: </p>
<pre><code> &amp; intersection
 + union
 | another name for '+', hence means union
 - subtraction (the result matches the set consisting of those
      code points matched by the first operand, excluding any that
      are also matched by the second operand)
 ^ symmetric difference (the union minus the intersection). This
      is like an exclusive or, in that the result is the set of code
      points that are matched by either, but not both, of the
      operands.
</code></pre>
<p> There is one unary operator: </p>
<pre><code> ! complement
</code></pre>
<p> All the binary operators left associate; <code>&quot;&amp;&quot;</code> is higher precedence than the others, which all have equal precedence. The unary operator right associates, and has highest precedence. Thus this follows the normal Perl precedence rules for logical operators. Use parentheses to override the default precedence and associativity. </p>
<p> The main restriction is that everything is a metacharacter. Thus, you cannot refer to single characters by doing something like this: </p>
<pre><code> /(?[ a + b ])/ # Syntax error!
</code></pre>
<p> The easiest way to specify an individual typable character is to enclose it in brackets: </p>
<pre><code> /(?[ [a] + [b] ])/
</code></pre>
<p> (This is the same thing as <code>&quot;[ab]&quot;</code>.) You could also have said the equivalent: </p>
<pre><code> /(?[[ a b ]])/
</code></pre>
<p> (You can, of course, specify single characters by using, <code>&quot;\x{...}&quot;</code>, <code>&quot;\N{...}&quot;</code>, etc.) </p>
<p> This last example shows the use of this construct to specify an ordinary bracketed character class without additional set operations. Note the white space within it. This is allowed because <code>&quot;/xx&quot;</code> is automatically turned on within this construct. </p>
<p> All the other escapes accepted by normal bracketed character classes are accepted here as well. </p>
<p> Because this construct compiles under <code>&quot;use re &#8216;strict&quot;</code>, unrecognized escapes that generate warnings in normal classes are fatal errors here, as well as all other warnings from these class elements, as well as some practices that don&#8217;t currently warn outside <code>&quot;re &#8216;strict&#8217;&quot;</code>. For example you cannot say </p>
<pre><code> /(?[ [ \xF ] ])/ # Syntax error!
</code></pre>
<p> You have to have two hex digits after a braceless <code>&quot;\x&quot;</code> (use a leading zero to make two). These restrictions are to lower the incidence of typos causing the class to not match what you thought it would. </p>
<p> If a regular bracketed character class contains a <code>&quot;\p{}&quot;</code> or <code>&quot;\P{}&quot;</code> and is matched against a non-Unicode code point, a warning may be raised, as the result is not Unicode-defined. No such warning will come when using this extended form. </p>
<p> The final difference between regular bracketed character classes and these, is that it is not possible to get these to match a multi-character fold. Thus, </p>
<pre><code> /(?[ [\xDF] ])/iu
</code></pre>
<p> does not match the string <code>&quot;ss&quot;</code>. </p>
<p> You don&#8217;t have to enclose <font SIZE="-1">POSIX</font> class names inside double brackets, hence both of the following work: </p>
<pre><code> /(?[ [:word:] - [:lower:] ])/
 /(?[ [[:word:]] - [[:lower:]] ])/
</code></pre>
<p> Any contained <font SIZE="-1">POSIX</font> character classes, including things like <code>&quot;\w&quot;</code> and <code>&quot;\D&quot;</code> respect the <code>&quot;/a&quot;</code> (and <code>&quot;/aa&quot;</code>) modifiers. </p>
<p> Note that <code>&quot;(?[ ])&quot;</code> is a regex-compile-time construct. Any attempt to use something which isn&#8217;t knowable at the time the containing regular expression is compiled is a fatal error. In practice, this means just three limitations: </p>
<dl>
<dt>1.</dt>
<dd> <p> When compiled within the scope of <code>&quot;use locale&quot;</code> (or the <code>&quot;/l&quot;</code> regex modifier), this construct assumes that the execution-time locale will be a <font SIZE="-1">UTF-8</font> one, and the generated pattern always uses Unicode rules. What gets matched or not thus isn&#8217;t dependent on the actual runtime locale, so tainting is not enabled. But a <code>&quot;locale&quot;</code> category warning is raised if the runtime locale turns out to not be <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>2.</dt>
<dd> <p> Any user-defined property used must be already defined by the time the regular expression is compiled (but note that this construct can be used instead of such properties). </p>
 </dd>
<dt>3.</dt>
<dd> <p> A regular expression that otherwise would compile using <code>&quot;/d&quot;</code> rules, and which uses this construct will instead use <code>&quot;/u&quot;</code>. Thus this construct tells Perl that you don&#8217;t want <code>&quot;/d&quot;</code> rules for the entire regular expression containing it. </p>
 </dd></dl>
<p> Note that skipping white space applies only to the interior of this construct. There must not be any space between any of the characters that form the initial <code>&quot;(?[&quot;</code>. Nor may there be space between the closing <code>&quot;])&quot;</code> characters. </p>
<p> Just as in all regular expressions, the pattern can be built up by including variables that are interpolated at regex compilation time. But its best to compile each sub-component. </p>
<pre><code> my $thai_or_lao = qr/(?[ \p{Thai} + \p{Lao} ])/;
 my $lower = qr/(?[ \p{Lower} + \p{Digit} ])/;
</code></pre>
<p> When these are embedded in another pattern, what they match does not change, regardless of parenthesization or what modifiers are in effect in that outer pattern. If you fail to compile the subcomponents, you can get some nasty surprises. For example: </p>
<pre><code> my $thai_or_lao = '\p{Thai} + \p{Lao}';
 ...
 qr/(?[ \p{Digit} &amp; $thai_or_lao ])/;
</code></pre>
<p> compiles to </p>
<pre><code> qr/(?[ \p{Digit} &amp; \p{Thai} + \p{Lao} ])/;
</code></pre>
<p> But this does not have the effect that someone reading the source code would likely expect, as the intersection applies just to <code>&quot;\p{Thai}&quot;</code>, excluding the Laotian. Its best to compile the subcomponents, but you could also parenthesize the component pieces: </p>
<pre><code> my $thai_or_lao = '( \p{Thai} + \p{Lao} )';
</code></pre>
<p> But any modifiers will still apply to all the components: </p>
<pre><code> my $lower = '\p{Lower} + \p{Digit}';
 qr/(?[ \p{Greek} &amp; $lower ])/i;
</code></pre>
<p> matches upper case things. So just, compile the subcomponents, as illustrated above. </p>
<p> Due to the way that Perl parses things, your parentheses and brackets may need to be balanced, even including comments. If you run into any examples, please send them to <code>&quot;perlbug [at] perl.org&quot;</code>, so that we can have a concrete example for this man page. </p>
<p> We may change it so that things that remain legal uses in normal bracketed character classes might become illegal within this experimental construct. One proposal, for example, is to forbid adjacent uses of the same character, as in <code>&quot;(?[ [aa] ])&quot;</code>. The motivation for such a change is that this usage is likely a typo, as the second ``a&#8217;&#8216; adds nothing. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">The dot</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Backslash sequences</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Bracketed Character Classes</a></dt>
<dd>  </dd></dl>
</dl>
