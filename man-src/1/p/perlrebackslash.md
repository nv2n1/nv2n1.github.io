---
title: "perlrebackslash(1)"
name: "perlrebackslash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrebackslash/"
description: "perlrebackslash – Perl Regular Expression Backslash Sequences and Escapes"
---

<h2>DESCRIPTION</h2>
<p> The top level documentation about Perl regular expressions is found in perlre. </p>
<p> This document describes all backslash and escape sequences. After explaining the role of the backslash, it lists all the sequences that have a special meaning in Perl regular expressions (in alphabetical order), then describes each of them. </p>
<p> Most sequences are described in detail in different documents; the primary purpose of this document is to have a quick reference guide describing all backslash and escape sequences.</p>
<h3>The backslash</h3>
<p> In a regular expression, the backslash can perform one of two tasks: it either takes away the special meaning of the character following it (for instance, <tt>&quot;\|&quot;</tt> matches a vertical bar, it&#8217;s not an alternation), or it is the start of a backslash or escape sequence. </p>
<p> The rules determining what it is are quite simple: if the character following the backslash is an <font SIZE="-1">ASCII</font> punctuation (non-word) character (that is, anything that is not a letter, digit, or underscore), then the backslash just takes away any special meaning of the character following it. </p>
<p> If the character following the backslash is an <font SIZE="-1">ASCII</font> letter or an <font SIZE="-1">ASCII</font> digit, then the sequence may be special; if so, it&#8217;s listed below. A few letters have not been used yet, so escaping them with a backslash doesn&#8217;t change them to be special. A future version of Perl may assign a special meaning to them, so if you have warnings turned on, Perl issues a warning if you use such a sequence. [1]. </p>
<p> It is however guaranteed that backslash or escape sequences never have a punctuation character following the backslash, not now, and not in a future version of Perl 5. So it is safe to put a backslash in front of a non-word character. </p>
<p> Note that the backslash itself is special; if you want to match a backslash, you have to escape the backslash with a backslash: <tt>&quot;/\/&quot;</tt> matches a single backslash.</p>
<dl>
<dt>[1]</dt>
<dd> There is one exception. If you use an alphanumeric character as the delimiter of your pattern (which you probably shouldn&#8217;t do for readability reasons), you have to escape the delimiter if you want to match it. Perl won&#8217;t warn then. See also &#8220;Gory details of parsing quoted constructs&#8221; in perlop.</dd></dl>
<h3>All the sequences and escapes</h3>
<p> Those not usable within a bracketed character class (like <tt>&quot;[\da-z]&quot;</tt>) are marked as <tt>&quot;Not in [].&quot;</tt> </p>
<pre><code></code> 
<pre><code> \000 Octal escape sequence. See also \o{}.
 \1 Absolute backreference. Not in [].
 \a Alarm or bell.
 \A Beginning of string. Not in [].
 \b{}, \b Boundary. (\b is a backspace in []).
 \B{}, \B Not a boundary. Not in [].
 \cX Control-X.
 \d Match any digit character.
 \D Match any character that isn't a digit.
 \e Escape character.
 \E Turn off \Q, \L and \U processing. Not in [].
 \f Form feed.
 \F Foldcase till \E. Not in [].
 \g{}, \g1 Named, absolute or relative backreference.
                   Not in [].
 \G Pos assertion. Not in [].
 \h Match any horizontal whitespace character.
 \H Match any character that isn't horizontal whitespace.
 \k{}, \k&lt;&gt;, \k'' Named backreference. Not in [].
 \K Keep the stuff left of \K. Not in [].
 \l Lowercase next character. Not in [].
 \L Lowercase till \E. Not in [].
 \n (Logical) newline character.
 \N Match any character but newline. Not in [].
 \N{} Named or numbered (Unicode) character or sequence.
 \o{} Octal escape sequence.
 \p{}, \pP Match any character with the given Unicode property.
 \P{}, \PP Match any character without the given property.
 \Q Quote (disable) pattern metacharacters till \E. Not
                   in [].
 \r Return character.
 \R Generic new line. Not in [].
 \s Match any whitespace character.
 \S Match any character that isn't a whitespace.
 \t Tab character.
 \u Titlecase next character. Not in [].
 \U Uppercase till \E. Not in [].
 \v Match any vertical whitespace character.
 \V Match any character that isn't vertical whitespace
 \w Match any word character.
 \W Match any character that isn't a word character.
 \x{}, \x00 Hexadecimal escape sequence.
 \X Unicode &quot;extended grapheme cluster&quot;. Not in [].
 \z End of string. Not in [].
 \Z End of string. Not in [].
</code></pre>
<h3>Character Escapes</h3>
<p> <i>Fixed characters</i> </p>
<p> A handful of characters have a dedicated <i>character escape</i>. The following table shows them, along with their <font SIZE="-1">ASCII</font> code points (in decimal and hex), their <font SIZE="-1">ASCII</font> name, the control escape on <font SIZE="-1">ASCII</font> platforms and a short description. (For <font SIZE="-1">EBCDIC</font> platforms, see ``<font SIZE="-1">OPERATOR DIFFERENCES&#8217;&#8216;</font> in perlebcdic.) </p>
<pre><code> Seq. Code Point ASCII Cntrl Description.
       Dec Hex
  \a 7 07 BEL \cG alarm or bell
  \b 8 08 BS \cH backspace [1]
  \e 27 1B ESC \c[ escape character
  \f 12 0C FF \cL form feed
  \n 10 0A LF \cJ line feed [2]
  \r 13 0D CR \cM carriage return
  \t 9 09 TAB \cI tab
</code></pre>
<dl>
<dt>[1]</dt>
<dd> <p> <code>&quot;\b&quot;</code> is the backspace character only inside a character class. Outside a character class, <code>&quot;\b&quot;</code> alone is a word-character/non-word-character boundary, and <code>&quot;\b{}&quot;</code> is some other type of boundary. </p>
 </dd>
<dt>[2]</dt>
<dd> <p> <code>&quot;\n&quot;</code> matches a logical newline. Perl converts between <code>&quot;\n&quot;</code> and your <font SIZE="-1">OS</font>&#8216;s native newline character when reading from or writing to text files. </p>
 </dd></dl>
<p> Example </p>
<pre><code> $str =~ /\t/; # Matches if $str contains a (horizontal) tab.
</code></pre>
<p> <i>Control characters</i> </p>
<p> <code>&quot;\c&quot;</code> is used to denote a control character; the character following <code>&quot;\c&quot;</code> determines the value of the construct. For example the value of <code>&quot;\cA&quot;</code> is <code><a href="/docs/linux/man/1-chr/">chr</a>(1)</code>, and the value of <code>&quot;\cb&quot;</code> is <code><a href="/docs/linux/man/2-chr/">chr</a>(2)</code>, etc. The gory details are in ``Regexp Quote-Like Operators&#8217;&#8216; in perlop. A complete list of what <code><a href="/docs/linux/man/1-chr/">chr</a>(1)</code>, etc. means for <font SIZE="-1">ASCII</font> and <font SIZE="-1">EBCDIC</font> platforms is in ``<font SIZE="-1">OPERATOR DIFFERENCES&#8217;&#8216;</font> in perlebcdic. </p>
<p> Note that <code>&quot;\c\&quot;</code> alone at the end of a regular expression (or doubled-quoted string) is not valid. The backslash must be followed by another character. That is, <code>&quot;\c\</code>X <code>&quot;</code> means <code>&quot;chr(28) . &#8216;</code>X <code>&#8216;&quot;</code> for all characters <i>X</i>. </p>
<p> To write platform-independent code, you must use <code>&quot;\N{</code>NAME <code>}&quot;</code> instead, like <code>&quot;\N{ESCAPE}&quot;</code> or <code>&quot;\N{U+001B}&quot;</code>, see charnames. </p>
<p> Mnemonic: <i>c</i>ontrol character. </p>
<p> Example </p>
<pre><code> $str =~ /\cK/; # Matches if $str contains a vertical tab (control-K).
</code></pre>
<p> <i>Named or numbered characters and character sequences</i> </p>
<p> Unicode characters have a Unicode name and numeric code point (ordinal) value. Use the <code>&quot;\N{}&quot;</code> construct to specify a character by either of these values. Certain sequences of characters also have names. </p>
<p> To specify by name, the name of the character or character sequence goes between the curly braces. </p>
<p> To specify a character by Unicode code point, use the form <code>&quot;\N{U+</code>code point <code>}&quot;</code>, where <i>code point</i> is a number in hexadecimal that gives the code point that Unicode has assigned to the desired character. It is customary but not required to use leading zeros to pad the number to 4 digits. Thus <code>&quot;\N{U+0041}&quot;</code> means <code>&quot;LATIN CAPITAL LETTER A&quot;</code>, and you will rarely see it written without the two leading zeros. <code>&quot;\N{U+0041}&quot;</code> means ``A&#8217;&#8216; even on <font SIZE="-1">EBCDIC</font> machines (where the ordinal value of ``A&#8217;&#8216; is not 0x41). </p>
<p> It is even possible to give your own names to characters and character sequences by using the charnames module. These custom names are lexically scoped, and so a given code point may have different names in different scopes. The name used is what is in effect at the time the <code>&quot;\N{}&quot;</code> is expanded. For patterns in double-quotish context, that means at the time the pattern is parsed. But for patterns that are delimitted by single quotes, the expansion is deferred until pattern compilation time, which may very well have a different <code>&quot;charnames&quot;</code> translator in effect. </p>
<p> (There is an expanded internal form that you may see in debug output: <code>&quot;\N{U+</code>code point <code>.</code>code point <code>...}&quot;</code>. The <code>&quot;...&quot;</code> means any number of these <i>code point</i>s separated by dots. This represents the sequence formed by the characters. This is an internal form only, subject to change, and you should not try to use it yourself.) </p>
<p> Mnemonic: <i>N</i>amed character. </p>
<p> Note that a character or character sequence expressed as a named or numbered character is considered a character without special meaning by the regex engine, and will match ``as is&#8217;&#8216;. </p>
<p> Example </p>
<pre><code> $str =~ /\N{THAI CHARACTER SO SO}/; # Matches the Thai SO SO character
 use charnames 'Cyrillic'; # Loads Cyrillic names.
 $str =~ /\N{ZHE}\N{KA}/; # Match &quot;ZHE&quot; followed by &quot;KA&quot;.
</code></pre>
<p> <i>Octal escapes</i> </p>
<p> There are two forms of octal escapes. Each is used to specify a character by its code point specified in octal notation. </p>
<p> One form, available starting in Perl 5.14 looks like <code>&quot;\o{...}&quot;</code>, where the dots represent one or more octal digits. It can be used for any Unicode character. </p>
<p> It was introduced to avoid the potential problems with the other form, available in all Perls. That form consists of a backslash followed by three octal digits. One problem with this form is that it can look exactly like an old-style backreference (see ``Disambiguation rules between old-style octal escapes and backreferences&#8217;&#8216; below.) You can avoid this by making the first of the three digits always a zero, but that makes \077 the largest code point specifiable. </p>
<p> In some contexts, a backslash followed by two or even one octal digits may be interpreted as an octal escape, sometimes with a warning, and because of some bugs, sometimes with surprising results. Also, if you are creating a regex out of smaller snippets concatenated together, and you use fewer than three digits, the beginning of one snippet may be interpreted as adding digits to the ending of the snippet before it. See ``Absolute referencing&#8217;&#8216; for more discussion and examples of the snippet problem. </p>
<p> Note that a character expressed as an octal escape is considered a character without special meaning by the regex engine, and will match ``as is&#8217;&#8216;. </p>
<p> To summarize, the <code>&quot;\o{}&quot;</code> form is always safe to use, and the other form is safe to use for code points through \077 when you use exactly three digits to specify them. </p>
<p> Mnemonic: <i>0</i>ctal or <i>o</i>ctal. </p>
<p> Examples (assuming an <font SIZE="-1">ASCII</font> platform) </p>
<pre><code> $str = &quot;Perl&quot;;
 $str =~ /\o{120}/; # Match, &quot;\120&quot; is &quot;P&quot;.
 $str =~ /\120/; # Same.
 $str =~ /\o{120}+/; # Match, &quot;\120&quot; is &quot;P&quot;,
                     # it's repeated at least once.
 $str =~ /\120+/; # Same.
 $str =~ /P\053/; # No match, &quot;\053&quot; is &quot;+&quot; and taken literally.
 /\o{23073}/ # Black foreground, white background smiling face.
 /\o{4801234567}/ # Raises a warning, and yieldschr(4).
</code></pre>
<p> Disambiguation rules between old-style octal escapes and backreferences </p>
<p> Octal escapes of the <code>&quot;\000&quot;</code> form outside of bracketed character classes potentially clash with old-style backreferences (see ``Absolute referencing&#8217;&#8216; below). They both consist of a backslash followed by numbers. So Perl has to use heuristics to determine whether it is a backreference or an octal escape. Perl uses the following rules to disambiguate: </p>
<dl>
<dt>1.</dt>
<dd> <p> If the backslash is followed by a single digit, it&#8217;s a backreference. </p>
 </dd>
<dt>2.</dt>
<dd> <p> If the first digit following the backslash is a 0, it&#8217;s an octal escape. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If the number following the backslash is N (in decimal), and Perl already has seen N capture groups, Perl considers this a backreference. Otherwise, it considers it an octal escape. If N has more than three digits, Perl takes only the first three for the octal escape; the rest are matched as is. </p>
<pre><code> my $pat = &quot;(&quot; x 999;
    $pat .= &quot;a&quot;;
    $pat .= &quot;)&quot; x 999;
 /^($pat)\1000$/; # Matches 'aa'; there are 1000 capture groups.
 /^$pat\1000$/; # Matches 'a@0'; there are 999 capture groups
                    # and \1000 is seen as \100 (a '@') and a '0'.
</code></pre>
 </dd></dl>
<p> You can force a backreference interpretation always by using the <code>&quot;\g{...}&quot;</code> form. You can the force an octal interpretation always by using the <code>&quot;\o{...}&quot;</code> form, or for numbers up through \077 (= 63 decimal), by using three digits, beginning with a ``0&#8217;&#8216;. </p>
<p> <i>Hexadecimal escapes</i> </p>
<p> Like octal escapes, there are two forms of hexadecimal escapes, but both start with the sequence <code>&quot;\x&quot;</code>. This is followed by either exactly two hexadecimal digits forming a number, or a hexadecimal number of arbitrary length surrounded by curly braces. The hexadecimal number is the code point of the character you want to express. </p>
<p> Note that a character expressed as one of these escapes is considered a character without special meaning by the regex engine, and will match ``as is&#8217;&#8216;. </p>
<p> Mnemonic: he <i>x</i>adecimal. </p>
<p> Examples (assuming an <font SIZE="-1">ASCII</font> platform) </p>
<pre><code> $str = &quot;Perl&quot;;
 $str =~ /\x50/; # Match, &quot;\x50&quot; is &quot;P&quot;.
 $str =~ /\x50+/; # Match, &quot;\x50&quot; is &quot;P&quot;, it is repeated at least once
 $str =~ /P\x2B/; # No match, &quot;\x2B&quot; is &quot;+&quot; and taken literally.
 /\x{2603}\x{2602}/ # Snowman with an umbrella.
                    # The Unicode character 2603 is a snowman,
                    # the Unicode character 2602 is an umbrella.
 /\x{263B}/ # Black smiling face.
 /\x{263b}/ # Same, the hex digits A - F are case insensitive.
</code></pre>
<h3>Modifiers</h3>
<p> A number of backslash sequences have to do with changing the character, or characters following them. <code>&quot;\l&quot;</code> will lowercase the character following it, while <code>&quot;\u&quot;</code> will uppercase (or, more accurately, titlecase) the character following it. They provide functionality similar to the functions <code>&quot;lcfirst&quot;</code> and <code>&quot;ucfirst&quot;</code>. </p>
<p> To uppercase or lowercase several characters, one might want to use <code>&quot;\L&quot;</code> or <code>&quot;\U&quot;</code>, which will lowercase/uppercase all characters following them, until either the end of the pattern or the next occurrence of <code>&quot;\E&quot;</code>, whichever comes first. They provide functionality similar to what the functions <code>&quot;lc&quot;</code> and <code>&quot;uc&quot;</code> provide. </p>
<p> <code>&quot;\Q&quot;</code> is used to quote (disable) pattern metacharacters, up to the next <code>&quot;\E&quot;</code> or the end of the pattern. <code>&quot;\Q&quot;</code> adds a backslash to any character that could have special meaning to Perl. In the <font SIZE="-1">ASCII</font> range, it quotes every character that isn&#8217;t a letter, digit, or underscore. See ``quotemeta&#8217;&#8216; in perlfunc for details on what gets quoted for non-ASCII code points. Using this ensures that any character between <code>&quot;\Q&quot;</code> and <code>&quot;\E&quot;</code> will be matched literally, not interpreted as a metacharacter by the regex engine. </p>
<p> <code>&quot;\F&quot;</code> can be used to casefold all characters following, up to the next <code>&quot;\E&quot;</code> or the end of the pattern. It provides the functionality similar to the <code>&quot;fc&quot;</code> function. </p>
<p> Mnemonic: <i>L</i>owercase, <i>U</i>ppercase, <i>F</i>old-case, <i>Q</i>uotemeta, <i>E</i>nd. </p>
<p> Examples </p>
<pre><code> $sid = &quot;sid&quot;;
 $greg = &quot;GrEg&quot;;
 $miranda = &quot;(Miranda)&quot;;
 $str =~ /\u$sid/; # Matches 'Sid'
 $str =~ /\L$greg/; # Matches 'greg'
 $str =~ /\Q$miranda\E/; # Matches '(Miranda)', as if the pattern
                              # had been written as /\(Miranda\)/
</code></pre>
<h3>Character classes</h3>
<p> Perl regular expressions have a large range of character classes. Some of the character classes are written as a backslash sequence. We will briefly discuss those here; full details of character classes can be found in perlrecharclass. </p>
<p> <code>&quot;\w&quot;</code> is a character class that matches any single <i>word</i> character (letters, digits, Unicode marks, and connector punctuation (like the underscore)). <code>&quot;\d&quot;</code> is a character class that matches any decimal digit, while the character class <code>&quot;\s&quot;</code> matches any whitespace character. New in perl 5.10.0 are the classes <code>&quot;\h&quot;</code> and <code>&quot;\v&quot;</code> which match horizontal and vertical whitespace characters. </p>
<p> The exact set of characters matched by <code>&quot;\d&quot;</code>, <code>&quot;\s&quot;</code>, and <code>&quot;\w&quot;</code> varies depending on various pragma and regular expression modifiers. It is possible to restrict the match to the <font SIZE="-1">ASCII</font> range by using the <code>&quot;/a&quot;</code> regular expression modifier. See perlrecharclass. </p>
<p> The uppercase variants (<code>&quot;\W&quot;</code>, <code>&quot;\D&quot;</code>, <code>&quot;\S&quot;</code>, <code>&quot;\H&quot;</code>, and <code>&quot;\V&quot;</code>) are character classes that match, respectively, any character that isn&#8217;t a word character, digit, whitespace, horizontal whitespace, or vertical whitespace. </p>
<p> Mnemonics: <i>w</i>ord, <i>d</i>igit, <i>s</i>pace, <i>h</i>orizontal, <i>v</i>ertical. </p>
<p> <i>Unicode classes</i> </p>
<p> <code>&quot;\pP&quot;</code> (where <code>&quot;P&quot;</code> is a single letter) and <code>&quot;\p{Property}&quot;</code> are used to match a character that matches the given Unicode property; properties include things like ``letter&#8217;&#8216;, or ``thai character&#8217;&#8216;. Capitalizing the sequence to <code>&quot;\PP&quot;</code> and <code>&quot;\P{Property}&quot;</code> make the sequence match a character that doesn&#8217;t match the given Unicode property. For more details, see ``Backslash sequences&#8217;&#8216; in perlrecharclass and ``Unicode Character Properties&#8217;&#8216; in perlunicode. </p>
<p> Mnemonic: <i>p</i>roperty.  </p>
<h3>Referencing</h3>
<p> If capturing parenthesis are used in a regular expression, we can refer to the part of the source string that was matched, and match exactly the same thing. There are three ways of referring to such <i>backreference</i>: absolutely, relatively, and by name. </p>
<p> <i>Absolute referencing</i> </p>
<p> Either <code>&quot;\g</code>N <code>&quot;</code> (starting in Perl 5.10.0), or <code>&quot;\</code>N <code>&quot;</code> (old-style) where <i>N</i> is a positive (unsigned) decimal number of any length is an absolute reference to a capturing group. </p>
<p> <i>N</i> refers to the Nth set of parentheses, so <code>&quot;\g</code>N <code>&quot;</code> refers to whatever has been matched by that set of parentheses. Thus <code>&quot;\g1&quot;</code> refers to the first capture group in the regex. </p>
<p> The <code>&quot;\g</code>N <code>&quot;</code> form can be equivalently written as <code>&quot;\g{</code>N <code>}&quot;</code> which avoids ambiguity when building a regex by concatenating shorter strings. Otherwise if you had a regex <code>&quot;qr/$a$b/&quot;</code>, and <code>$a</code> contained <code>&quot;\g1&quot;</code>, and <code>$b</code> contained <code>&quot;37&quot;</code>, you would get <code>&quot;/\g137/&quot;</code> which is probably not what you intended. </p>
<p> In the <code>&quot;\</code>N <code>&quot;</code> form, <i>N</i> must not begin with a ``0&#8217;&#8216;, and there must be at least <i>N</i> capturing groups, or else <i>N</i> is considered an octal escape (but something like <code>&quot;\18&quot;</code> is the same as <code>&quot;\0018&quot;</code>; that is, the octal escape <code>&quot;\001&quot;</code> followed by a literal digit <code>&quot;8&quot;</code>). </p>
<p> Mnemonic: <i>g</i>roup. </p>
<p> Examples </p>
<pre><code> /(\w+) \g1/; # Finds a duplicated word, (e.g. &quot;cat cat&quot;).
 /(\w+) \1/; # Same thing; written old-style.
 /(.)(.)\g2\g1/; # Match a four letter palindrome (e.g. &quot;ABBA&quot;).
</code></pre>
<p> <i>Relative referencing</i> </p>
<p> <code>&quot;\g-</code>N <code>&quot;</code> (starting in Perl 5.10.0) is used for relative addressing. (It can be written as <code>&quot;\g{-</code>N <code>&quot;</code>.) It refers to the <i>N</i>th group before the <code>&quot;\g{-</code>N <code>}&quot;</code>. </p>
<p> The big advantage of this form is that it makes it much easier to write patterns with references that can be interpolated in larger patterns, even if the larger pattern also contains capture groups. </p>
<p> Examples </p>
<pre><code> /(A) # Group 1
  ( # Group 2
    (B) # Group 3
    \g{-1} # Refers to group 3 (B)
    \g{-3} # Refers to group 1 (A)
  )
 /x; # Matches &quot;ABBA&quot;.
 my $qr = qr /(.)(.)\g{-2}\g{-1}/; # Matches 'abab', 'cdcd', etc.
 /$qr$qr/ # Matches 'ababcdcd'.
</code></pre>
<p> <i>Named referencing</i> </p>
<p> <code>&quot;\g{</code>name <code>}&quot;</code> (starting in Perl 5.10.0) can be used to back refer to a named capture group, dispensing completely with having to think about capture buffer positions. </p>
<p> To be compatible with .Net regular expressions, <code>&quot;\g{name}&quot;</code> may also be written as <code>&quot;\k{name}&quot;</code>, <code>&quot;\k&lt;name&gt;&quot;</code> or <code>&quot;\k&#8217;name&#8217;&quot;</code>. </p>
<p> To prevent any ambiguity, <i>name</i> must not start with a digit nor contain a hyphen. </p>
<p> Examples </p>
<pre><code> /(?&lt;word&gt;\w+) \g{word}/ # Finds duplicated word, (e.g. &quot;cat cat&quot;)
 /(?&lt;word&gt;\w+) \k{word}/ # Same.
 /(?&lt;word&gt;\w+) \k&lt;word&gt;/ # Same.
 /(?&lt;letter1&gt;.)(?&lt;letter2&gt;.)\g{letter2}\g{letter1}/
                         # Match a four letter palindrome (e.g. &quot;ABBA&quot;)
</code></pre>
<h3>Assertions</h3>
<p> Assertions are conditions that have to be true; they don&#8217;t actually match parts of the substring. There are six assertions that are written as backslash sequences. </p>
<dl>
<dt>\A</dt>
<dd> <p> <code>&quot;\A&quot;</code> only matches at the beginning of the string. If the <code>&quot;/m&quot;</code> modifier isn&#8217;t used, then <code>&quot;/\A/&quot;</code> is equivalent to <code>&quot;/^/&quot;</code>. However, if the <code>&quot;/m&quot;</code> modifier is used, then <code>&quot;/^/&quot;</code> matches internal newlines, but the meaning of <code>&quot;/\A/&quot;</code> isn&#8217;t changed by the <code>&quot;/m&quot;</code> modifier. <code>&quot;\A&quot;</code> matches at the beginning of the string regardless whether the <code>&quot;/m&quot;</code> modifier is used. </p>
 </dd>
<dt>\z, \Z</dt>
<dd> <p> <code>&quot;\z&quot;</code> and <code>&quot;\Z&quot;</code> match at the end of the string. If the <code>&quot;/m&quot;</code> modifier isn&#8217;t used, then <code>&quot;/\Z/&quot;</code> is equivalent to <code>&quot;/$/&quot;</code>; that is, it matches at the end of the string, or one before the newline at the end of the string. If the <code>&quot;/m&quot;</code> modifier is used, then <code>&quot;/$/&quot;</code> matches at internal newlines, but the meaning of <code>&quot;/\Z/&quot;</code> isn&#8217;t changed by the <code>&quot;/m&quot;</code> modifier. <code>&quot;\Z&quot;</code> matches at the end of the string (or just before a trailing newline) regardless whether the <code>&quot;/m&quot;</code> modifier is used. </p>
<p> <code>&quot;\z&quot;</code> is just like <code>&quot;\Z&quot;</code>, except that it does not match before a trailing newline. <code>&quot;\z&quot;</code> matches at the end of the string only, regardless of the modifiers used, and not just before a newline. It is how to anchor the match to the true end of the string under all conditions. </p>
 </dd>
<dt>\G</dt>
<dd> <p> <code>&quot;\G&quot;</code> is usually used only in combination with the <code>&quot;/g&quot;</code> modifier. If the <code>&quot;/g&quot;</code> modifier is used and the match is done in scalar context, Perl remembers where in the source string the last match ended, and the next time, it will start the match from where it ended the previous time. </p>
<p> <code>&quot;\G&quot;</code> matches the point where the previous match on that string ended, or the beginning of that string if there was no previous match. </p>
<p> Mnemonic: <i>G</i>lobal. </p>
 </dd>
<dt>\b{}, \b, \B{}, \B</dt>
<dd> <p> <code>&quot;\b{...}&quot;</code>, available starting in v5.22, matches a boundary (between two characters, or before the first character of the string, or after the final character of the string) based on the Unicode rules for the boundary type specified inside the braces. The boundary types are given a few paragraphs below. <code>&quot;\B{...}&quot;</code> matches at any place between characters where <code>&quot;\b{...}&quot;</code> of the same type doesn&#8217;t match. </p>
<p> <code>&quot;\b&quot;</code> when not immediately followed by a <code>&quot;{&quot;</code> matches at any place between a word (something matched by <code>&quot;\w&quot;</code>) and a non-word character (<code>&quot;\W&quot;</code>); <code>&quot;\B&quot;</code> when not immediately followed by a <code>&quot;{&quot;</code> matches at any place between characters where <code>&quot;\b&quot;</code> doesn&#8217;t match. To get better word matching of natural language text, see ``\b{wb}&#8216;&#8216; below. </p>
<p> <code>&quot;\b&quot;</code> and <code>&quot;\B&quot;</code> assume there&#8217;s a non-word character before the beginning and after the end of the source string; so <code>&quot;\b&quot;</code> will match at the beginning (or end) of the source string if the source string begins (or ends) with a word character. Otherwise, <code>&quot;\B&quot;</code> will match. </p>
<p> Do not use something like <code>&quot;\b=head\d\b&quot;</code> and expect it to match the beginning of a line. It can&#8217;t, because for there to be a boundary before the non-word ``=&#8216;&#8216;, there must be a word character immediately previous. All plain <code>&quot;\b&quot;</code> and <code>&quot;\B&quot;</code> boundary determinations look for word characters alone, not for non-word characters nor for string ends. It may help to understand how <code>&quot;\b&quot;</code> and <code>&quot;\B&quot;</code> work by equating them as follows: </p>
<pre><code>    \b really means (?:(?&lt;=\w)(?!\w)|(?&lt;!\w)(?=\w))
    \B really means (?:(?&lt;=\w)(?=\w)|(?&lt;!\w)(?!\w))
</code></pre>
<p> In contrast, <code>&quot;\b{...}&quot;</code> and <code>&quot;\B{...}&quot;</code> may or may not match at the beginning and end of the line, depending on the boundary type. These implement the Unicode default boundaries, specified in &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr14/">http://www.unicode.org/reports/tr14/</a>&gt; and &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;. The boundary types are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;\b{gcb}&quot; or &quot;\b{g}&quot;</dt>
<dd> <p> This matches a Unicode ``Grapheme Cluster Boundary&#8217;&#8216;. (Actually Perl always uses the improved ``extended&#8217;&#8216; grapheme cluster&quot;). These are explained below under &quot;<code>&quot;\X&quot;</code>&quot;. In fact, <code>&quot;\X&quot;</code> is another way to get the same functionality. It is equivalent to <code>&quot;/.+?\b{gcb}/&quot;</code>. Use whichever is most convenient for your situation. </p>
 </dd>
<dt>&quot;\b{lb}&quot;</dt>
<dd> <p> This matches according to the default Unicode Line Breaking Algorithm (&lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr14/">http://www.unicode.org/reports/tr14/</a>&gt;), as customized in that document (Example 7 of revision 35 &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr14/tr14-35.html#Example7">http://www.unicode.org/reports/tr14/tr14-35.html#Example7</a>&gt;) for better handling of numeric expressions. </p>
<p> This is suitable for many purposes, but the Unicode::LineBreak module is available on <font SIZE="-1">CPAN</font> that provides many more features, including customization. </p>
 </dd>
<dt>&quot;\b{sb}&quot;</dt>
<dd> <p> This matches a Unicode ``Sentence Boundary&#8217;&#8216;. This is an aid to parsing natural language sentences. It gives good, but imperfect results. For example, it thinks that ``Mr. Smith&#8217;&#8216; is two sentences. More details are at &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;. Note also that it thinks that anything matching ``\R&#8217;&#8216; (except form feed and vertical tab) is a sentence boundary. <code>&quot;\b{sb}&quot;</code> works with text designed for word-processors which wrap lines automatically for display, but hard-coded line boundaries are considered to be essentially the ends of text blocks (paragraphs really), and hence the ends of sentences. <code>&quot;\b{sb}&quot;</code> doesn&#8217;t do well with text containing embedded newlines, like the source text of the document you are reading. Such text needs to be preprocessed to get rid of the line separators before looking for sentence boundaries. Some people view this as a bug in the Unicode standard, and this behavior is quite subject to change in future Perl versions. </p>
 </dd>
<dt>&quot;\b{wb}&quot;</dt>
<dd> <p> This matches a Unicode ``Word Boundary&#8217;&#8216;, but tailored to Perl expectations. This gives better (though not perfect) results for natural language processing than plain <code>&quot;\b&quot;</code> (without braces) does. For example, it understands that apostrophes can be in the middle of words and that parentheses aren&#8217;t (see the examples below). More details are at &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;. </p>
<p> The current Unicode definition of a Word Boundary matches between every white space character. Perl tailors this, starting in version 5.24, to generally not break up spans of white space, just as plain <code>&quot;\b&quot;</code> has always functioned. This allows <code>&quot;\b{wb}&quot;</code> to be a drop-in replacement for <code>&quot;\b&quot;</code>, but with generally better results for natural language processing. (The exception to this tailoring is when a span of white space is immediately followed by something like U+0303, <font SIZE="-1">COMBINING TILDE.</font> If the final space character in the span is a horizontal white space, it is broken out so that it attaches instead to the combining character. To be precise, if a span of white space that ends in a horizontal space has the character immediately following it have any of the Word Boundary property values ``Extend&#8217;&#8216;, ``Format&#8217;&#8216; or ``<font SIZE="-1">ZWJ&#8217;&#8216;,</font> the boundary between the final horizontal space character and the rest of the span matches <code>&quot;\b{wb}&quot;</code>. In all other cases the boundary between two white space characters matches <code>&quot;\B{wb}&quot;</code>.) </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> It is important to realize when you use these Unicode boundaries, that you are taking a risk that a future version of Perl which contains a later version of the Unicode Standard will not work precisely the same way as it did when your code was written. These rules are not considered stable and have been somewhat more subject to change than the rest of the Standard. Unicode reserves the right to change them at will, and Perl reserves the right to update its implementation to Unicode&#8217;s new rules. In the past, some changes have been because new characters have been added to the Standard which have different characteristics than all previous characters, so new rules are formulated for handling them. These should not cause any backward compatibility issues. But some changes have changed the treatment of existing characters because the Unicode Technical Committee has decided that the change is warranted for whatever reason. This could be to fix a bug, or because they think better results are obtained with the new rule. </p>
<p> It is also important to realize that these are default boundary definitions, and that implementations may wish to tailor the results for particular purposes and locales. For example, some languages, such as Japanese and Thai, require dictionary lookup to accurately determine word boundaries. </p>
<p> Mnemonic: <i>b</i>oundary. </p>
 </dd></dl>
</dl>
<p> Examples </p>
<pre><code>  &quot;cat&quot; =~ /\Acat/; # Match.
  &quot;cat&quot; =~ /cat\Z/; # Match.
  &quot;cat\n&quot; =~ /cat\Z/; # Match.
  &quot;cat\n&quot; =~ /cat\z/; # No match.
  &quot;cat&quot; =~ /\bcat\b/; # Matches.
  &quot;cats&quot; =~ /\bcat\b/; # No match.
  &quot;cat&quot; =~ /\bcat\B/; # No match.
  &quot;cats&quot; =~ /\bcat\B/; # Match.
  while (&quot;cat dog&quot; =~ /(\w+)/g) {
      print $1; # Prints 'catdog'
  }
  while (&quot;cat dog&quot; =~ /\G(\w+)/g) {
      print $1; # Prints 'cat'
  }
  my $s = &quot;He said, \&quot;Is pi 3.14? (I'm not sure).\&quot;&quot;;
  print join(&quot;|&quot;, $s =~ m/ ( .+? \b ) /xg), &quot;\n&quot;;
  print join(&quot;|&quot;, $s =~ m/ ( .+? \b{wb} ) /xg), &quot;\n&quot;;
 prints
  He| |said|, &quot;|Is| |pi| |3|.|14|? (|I|'|m| |not| |sure
  He| |said|,| |&quot;|Is| |pi| |3.14|?| |(|I'm| |not| |sure|)|.|&quot;
</code></pre>
<h3>Misc</h3>
<p> Here we document the backslash sequences that don&#8217;t fall in one of the categories above. These are: </p>
<dl>
<dt>\K</dt>
<dd> <p> This appeared in perl 5.10.0. Anything matched left of <code>&quot;\K&quot;</code> is not included in <code>$&amp;</code>, and will not be replaced if the pattern is used in a substitution. This lets you write <code>&quot;s/PAT1 \K PAT2/REPL/x&quot;</code> instead of <code>&quot;s/(PAT1) PAT2/${1}REPL/x&quot;</code> or <code>&quot;s/(?&lt;=PAT1) PAT2/REPL/x&quot;</code>. </p>
<p> Mnemonic: <i>K</i>eep. </p>
 </dd>
<dt>\N</dt>
<dd> <p> This feature, available starting in v5.12, matches any character that is <code>not</code> a newline. It is a short-hand for writing <code>&quot;[^\n]&quot;</code>, and is identical to the <code>&quot;.&quot;</code> metasymbol, except under the <code>&quot;/s&quot;</code> flag, which changes the meaning of <code>&quot;.&quot;</code>, but not <code>&quot;\N&quot;</code>. </p>
<p> Note that <code>&quot;\N{...}&quot;</code> can mean a named or numbered character . </p>
<p> Mnemonic: Complement of <i>\n</i>. </p>
 </dd>
<dt>\R</dt>
<dd> <p> <code>&quot;\R&quot;</code> matches a <i>generic newline</i>; that is, anything considered a linebreak sequence by Unicode. This includes all characters matched by <code>&quot;\v&quot;</code> (vertical whitespace), and the multi character sequence <code>&quot;\x0D\x0A&quot;</code> (carriage return followed by a line feed, sometimes called the network newline; it&#8217;s the end of line sequence used in Microsoft text files opened in binary mode). <code>&quot;\R&quot;</code> is equivalent to <code>&quot;(?&gt;\x0D\x0A|\v)&quot;</code>. (The reason it doesn&#8217;t backtrack is that the sequence is considered inseparable. That means that </p>
<pre><code> &quot;\x0D\x0A&quot; =~ /^\R\x0A$/ # No match
</code></pre>
<p> fails, because the <code>&quot;\R&quot;</code> matches the entire string, and won&#8217;t backtrack to match just the <code>&quot;\x0D&quot;</code>.) Since <code>&quot;\R&quot;</code> can match a sequence of more than one character, it cannot be put inside a bracketed character class; <code>&quot;/[\R]/&quot;</code> is an error; use <code>&quot;\v&quot;</code> instead. <code>&quot;\R&quot;</code> was introduced in perl 5.10.0. </p>
<p> Note that this does not respect any locale that might be in effect; it matches according to the platform&#8217;s native character set. </p>
<p> Mnemonic: none really. <code>&quot;\R&quot;</code> was picked because <font SIZE="-1">PCRE</font> already uses <code>&quot;\R&quot;</code>, and more importantly because Unicode recommends such a regular expression metacharacter, and suggests <code>&quot;\R&quot;</code> as its notation. </p>
 </dd>
<dt>\X</dt>
<dd> <p> This matches a Unicode <i>extended grapheme cluster</i>. </p>
<p> <code>&quot;\X&quot;</code> matches quite well what normal (non-Unicode-programmer) usage would consider a single character. As an example, consider a G with some sort of diacritic mark, such as an arrow. There is no such single character in Unicode, but one can be composed by using a G followed by a Unicode ``<font SIZE="-1">COMBINING UPWARDS ARROW BELOW&#8217;&#8216;,</font> and would be displayed by Unicode-aware software as if it were a single character. </p>
<p> The match is greedy and non-backtracking, so that the cluster is never broken up into smaller components. </p>
<p> See also <code>&quot;\b{gcb}&quot;</code>. </p>
<p> Mnemonic: e <i>X</i>tended Unicode character. </p>
 </dd></dl>
<p> Examples </p>
<pre><code> $str =~ s/foo\Kbar/baz/g; # Change any 'bar' following a 'foo' to 'baz'
 $str =~ s/(.)\K\g1//g; # Delete duplicated characters.
 &quot;\n&quot; =~ /^\R$/; # Match, \n is a generic newline.
 &quot;\r&quot; =~ /^\R$/; # Match, \r is a generic newline.
 &quot;\r\n&quot; =~ /^\R$/; # Match, \r\n is a generic newline.
 &quot;P\x{307}&quot; =~ /^\X$/ # \X matches a P with a dot above.
</code></pre>
