---
title: "perlrequick(1)"
name: "perlrequick"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrequick/"
description: "perlrequick – Perl regular expressions quick start"
---

<h2 class="name">NAME</h2>
<p> perlrequick &#8211; Perl regular expressions quick start </p>
<h2>DESCRIPTION</h2>
<p> This page covers the very basics of understanding, creating and using regular expressions (&#8216;regexes&#8217;) in Perl.</p>
<h2>The Guide</h2>
<p> This page assumes you already know things, like what a &#8220;pattern&#8221; is, and the basic syntax of using them. If you don&#8217;t, see perlretut.</p>
<h3>Simple word matching</h3>
<p> The simplest regex is simply a word, or more generally, a string of characters. A regex consisting of a word matches any string that contains that word: </p>
<pre>
    &quot;Hello World&quot; =~ /World/;  # matches
</pre>
<p> In this statement, <tt>&quot;World&quot;</tt> is a regex and the <tt>&quot;//&quot;</tt> enclosing <tt>&quot;/World/&quot;</tt> tells Perl to search a string for a match. The operator <tt>&quot;=~&quot;</tt> associates the string with the regex match and produces a true value if the regex matched, or false if the regex did not match. In our case, <tt>&quot;World&quot;</tt> matches the second word in <tt>&quot;Hello World&quot;</tt>, so the expression is true. This idea has several variations. </p>
<p> Expressions like this are useful in conditionals: </p>
<pre>
    print &quot;It matches
&quot; if &quot;Hello World&quot; =~ /World/;
</pre>
<p> The sense of the match can be reversed by using <tt>&quot;!~&quot;</tt> operator: </p>
<pre>
    print &quot;It doesn't match
&quot; if &quot;Hello World&quot; !~ /World/;
</pre>
<p> The literal string in the regex can be replaced by a variable: </p>
<pre>
    $greeting = &quot;World&quot;;
    print &quot;It matches
&quot; if &quot;Hello World&quot; =~ /$greeting/;
</pre>
<p> If you&#8217;re matching against <tt>$_</tt>, the <tt>&quot;$_ =~&quot;</tt> part can be omitted: </p>
<pre>
    $_ = &quot;Hello World&quot;;
    print &quot;It matches
&quot; if /World/;
</pre>
<p> Finally, the <tt>&quot;//&quot;</tt> default delimiters for a match can be changed to arbitrary delimiters by putting an <tt>'m'</tt> out front: </p>
<pre><code>
"Hello World" = ~m !World !;
#matches, delimited by '!' "Hello World" = ~m{World };
#matches, note the matching '{}' "/usr/bin/perl" = ~m "/perl";
#matches after '/usr/bin',
#'/' becomes an ordinary char
</code></pre>
<p> Regexes must match a part of the string <i>exactly</i> in order for the statement to be true: </p>
<p>&#8220;Hello World&#8221; = ~ / world / ;<br />
#doesn&#8217;t match, case sensitive &#8220;Hello World&#8221; = ~ / o W / ;<br />
#matches, &#8216; &#8216; is an ordinary char &#8220;Hello World&#8221; = ~ / World / ;<br />
#doesn &#8216;t match, no &#8216; &#8216; at end</p>
<p> Perl will always match at the earliest possible point in the string: </p>
<pre>
    &quot;Hello World&quot; =~ /o/;       # matches 'o' in 'Hello'
    &quot;That hat is red&quot; =~ /hat/; # matches 'hat' in 'That'
</pre>
<p> Not all characters can be used &#8216;as is&#8217; in a match. Some characters, called <code>metacharacters</code>, are considered special, and reserved for use in regex notation. The metacharacters are </p>
<p>{}[]() ^ $.| *+?\</p>
<p> A metacharacter can be matched literally by putting a backslash before it: </p>
<p>&#8220;2+2=4&#8221; = ~ / 2 + 2 / ;<br />
#doesn&#8217;t match, + is a metacharacter &#8220;2+2=4&#8221; = ~ / 2\+ 2 / ;<br />
#matches, \+ is treated like an ordinary +<br />
              &#8216;C:\WIN32&#8217; = ~ / C :\WIN /<br />
    ;<br />
#matches<br />
    &#8220;/usr/bin/perl&#8221; = ~ /\/ usr\/ bin\/ perl /<br />
    ;<br />
#matches</p>
<p> In the last regex, the forward slash <tt>'/'</tt> is also backslashed, because it is used to delimit the regex. </p>
<p> Most of the metacharacters aren&#8217;t always special, and other characters (such as the ones delimitting the pattern) become special under various circumstances. This can be confusing and lead to unexpected results. <tt>&quot;use re 'strict'&quot;</tt> can notify you of potential pitfalls. </p>
<p> Non-printable <font SIZE="-1">ASCII</font> characters are represented by <code>escape sequences</code>. Common examples are <tt>&quot;	&quot;</tt> for a tab, <tt>&quot;
&quot;</tt> for a newline, and <tt>&quot;&quot;</tt> for a carriage return. Arbitrary bytes are represented by octal escape sequences, e.g., <tt>&quot;&quot;</tt>, or hexadecimal escape sequences, e.g., <tt>&quot;&quot;</tt>: </p>
<pre>
    &quot;1000	2000&quot; =~ m(0	2)  # matches
    &quot;cat&quot; =~ /\143at/  # matches in ASCII, but
                             # a weird way to spell cat
</pre>
<p> Regexes are treated mostly as double-quoted strings, so variable substitution works: </p>
<p>$foo = &#8216;house&#8217;;<br />
&#8216;cathouse&#8217; = ~ / cat$foo / ;<br />
#matches &#8216;housecat&#8217; = ~ / ${foo } cat / ;<br />
#matches</p>
<p> With all of the regexes above, if the regex matched anywhere in the string, it was considered a match. To specify <i>where</i> it should match, we would use the <code>anchor</code> metacharacters <tt>&quot;^&quot;</tt> and <tt>&quot;$&quot;</tt>. The anchor <tt>&quot;^&quot;</tt> means match at the beginning of the string and the anchor <tt>&quot;$&quot;</tt> means match at the end of the string, or before a newline at the end of the string. Some examples: </p>
<p>&#8220;housekeeper&#8221; = ~ / keeper / ;<br />
#matches<br />
    &#8220;housekeeper&#8221; = ~ / ^keeper /<br />
    ;<br />
#doesn&#8217;t match &#8220;housekeeper&#8221; = ~ / keeper$ / ;<br />
#matches<br />
    &#8220;housekeeper
&#8221; = ~ / keeper$ /<br />
    ;<br />
#matches<br />
    &#8220;housekeeper&#8221; = ~ / ^housekeeper$ /<br />
    ;<br />
#matches</p>
<h3>Using character classes</h3>
<p> A <code>character class</code> allows a set of possible characters, rather than just a single character, to match at a particular point in a regex. There are a number of different types of character classes, but usually when people use this term, they are referring to the type described in this section, which are technically called &#8220;Bracketed character classes&#8221;, because they are denoted by brackets <tt>&quot;[...]&quot;</tt>, with the set of characters to be possibly matched inside. But we&#8217;ll drop the &#8220;bracketed&#8221; below to correspond with common usage. Here are some examples of (bracketed) character classes: </p>
<p>/ cat / ;<br />
#matches &#8216;cat&#8217; / [bcr] at / ;<br />
#matches &#8216;bat&#8217;, &#8216;cat&#8217;, or &#8216;rat&#8217; &#8220;abc&#8221; = ~ / [cab] / ;<br />
#matches &#8216;a&#8217;</p>
<p> In the last statement, even though <tt>'c'</tt> is the first character in the class, the earliest point at which the regex can match is <tt>'a'</tt>. </p>
<p>/ [yY][eE][sS] / ;<br />
#match &#8216;yes&#8217; in a case -insensitive way<br />
#&#8217;yes&#8217;, &#8216;Yes&#8217;, &#8216;YES&#8217;, etc.<br />
    / yes / i;<br />
#also match &#8216;yes&#8217; in a case -insensitive way</p>
<p> The last example shows a match with an <tt>'i'</tt> <code>modifier</code>, which makes the match case-insensitive. </p>
<p> Character classes also have ordinary and special characters, but the sets of ordinary and special characters inside a character class are different than those outside a character class. The special characters for a character class are <tt>&quot;-]\^$&quot;</tt> and are matched using an escape: </p>
<p>   /[\]c]def/;<br />
#matches &#8216;]def&#8217; or &#8216;cdef&#8217; $x = &#8216;bcr&#8217;;<br />
   / [$x] at / ;<br />
#matches &#8216;bat, &#8216; cat &#8216;, or &#8216; rat&#8217; / [\$x] at / ;<br />
#matches &#8216;$at&#8217; or &#8216;xat&#8217; / [\$x] at / ;<br />
#matches &#8216;t&#8217;, &#8216;bat, &#8216; cat &#8216;, or &#8216; rat&#8217;</p>
<p> The special character <tt>'-'</tt> acts as a range operator within character classes, so that the unwieldy <tt>&quot;[0123456789]&quot;</tt> and <tt>&quot;[abc...xyz]&quot;</tt> become the svelte <tt>&quot;[0-9]&quot;</tt> and <tt>&quot;[a-z]&quot;</tt>: </p>
<p>/ item[0 &#8211; 9] / ;<br />
#matches &#8216;item0&#8217; or &#8230; or &#8216;item9&#8217; / [0 &#8211; 9a &#8211; fA &#8211; F] / ;<br />
#matches a hexadecimal digit</p>
<p> If <tt>'-'</tt> is the first or last character in a character class, it is treated as an ordinary character. </p>
<p> The special character <tt>&quot;^&quot;</tt> in the first position of a character class denotes a <code>negated character class</code>, which matches any character but those in the brackets. Both <tt>&quot;[...]&quot;</tt> and <tt>&quot;[^...]&quot;</tt> must match a character, or the match fails. Then </p>
<p>/ [^a] at / ;<br />
#doesn &#8216;t match &#8216; aat &#8216; or &#8216; at&#8217;, but matches<br />
#all other &#8216;bat&#8217;, &#8216;cat, &#8216; 0at &#8216;, &#8216; % at&#8217;, etc.<br />
    / [^0 &#8211; 9] / ;<br />
#matches a non &#8211; numeric character / [a ^ ] at / ;<br />
#matches &#8216;aat&#8217; or &#8216;^at&#8217;;<br />
here &#8216;^&#8217; is ordinary</p>
<p> Perl has several abbreviations for common character classes. (These definitions are those that Perl uses in ASCII-safe mode with the <tt>&quot;/a&quot;</tt> modifier. Otherwise they could match many more non-ASCII Unicode characters as well. See &#8220;Backslash sequences&#8221; in perlrecharclass for details.)</p>
<dl>
<dt>&bull;</p>
<dd> \d is a digit and represents </p>
<pre>
    [0-9]
</pre>
<dt>&bull;</p>
<dd> \s is a whitespace character and represents </p>
<pre>
    [\ 	
]
</pre>
<dt>&bull;</p>
<dd> \w is a word character (alphanumeric or _) and represents </p>
<pre>
    [0-9a-zA-Z_]
</pre>
<dt>&bull;</p>
<dd> \D is a negated \d; it represents any character but a digit </p>
<pre>
    [^0-9]
</pre>
<dt>&bull;</p>
<dd> \S is a negated \s; it represents any non-whitespace character </p>
<pre>
    [^\s]
</pre>
<dt>&bull;</p>
<dd> \W is a negated \w; it represents any non-word character </p>
<pre>
    [^\w]
</pre>
<dt>&bull;</p>
<dd> The period &#8216;.&#8217; matches any character but &#8220;
&#8221;</dl>
<p> The <tt>&quot;\d\s\w\D\S\W&quot;</tt> abbreviations can be used both inside and outside of character classes. Here are some in use: </p>
<p>/\d\d :\d\d :\d\d / ;<br />
#matches a hh : mm : ss time format / [\d\s] / ;<br />
#matches any digit or whitespace character /\w\W\w / ;<br />
#matches a word char, followed by a<br />
#non &#8211; word char, followed by a word char<br />
                          /..rt /<br />
    ;<br />
#matches any two chars, followed by &#8216;rt&#8217; / end\./ ;<br />
#matches &#8216;end.&#8217; / end[.] / ;<br />
#same thing, matches &#8216;end.&#8217;</p>
<p> The <code>word anchor</code>  <tt>&quot;&quot;</tt> matches a boundary between a word character and a non-word character <tt>&quot;\w\W&quot;</tt> or <tt>&quot;\W\w&quot;</tt>: </p>
<p>$x = &#8220;Housecat catenates house and cat&#8221;;<br />
$x = ~ /cat / ;<br />
#matches cat in &#8216;catenates&#8217; $x = ~ / cat / ;<br />
#matches cat in &#8216;housecat&#8217; $x = ~ /cat / ;<br />
#matches &#8216;cat&#8217; at end of string</p>
<p> In the last example, the end of the string is considered a word boundary. </p>
<p> For natural language processing (so that, for example, apostrophes are included in words), use instead <tt>&quot;{wb}&quot;</tt> </p>
<pre>
    &quot;don't&quot; =~ / .+? {wb} /x;  # matches the whole string
</pre>
<h3>Matching this or that</h3>
<p> We can match different character strings with the <code>alternation</code> metacharacter <tt>'|'</tt>. To match <tt>&quot;dog&quot;</tt> or <tt>&quot;cat&quot;</tt>, we form the regex <tt>&quot;dog|cat&quot;</tt>. As before, Perl will try to match the regex at the earliest possible point in the string. At each character position, Perl will first try to match the first alternative, <tt>&quot;dog&quot;</tt>. If <tt>&quot;dog&quot;</tt> doesn&#8217;t match, Perl will then try the next alternative, <tt>&quot;cat&quot;</tt>. If <tt>&quot;cat&quot;</tt> doesn&#8217;t match either, then the match fails and Perl moves to the next position in the string. Some examples: </p>
<pre>
    &quot;cats and dogs&quot; =~ /cat|dog|bird/;  # matches &quot;cat&quot;
    &quot;cats and dogs&quot; =~ /dog|cat|bird/;  # matches &quot;cat&quot;
</pre>
<p> Even though <tt>&quot;dog&quot;</tt> is the first alternative in the second regex, <tt>&quot;cat&quot;</tt> is able to match earlier in the string. </p>
<pre>
    &quot;cats&quot;          =~ /c|ca|cat|cats/; # matches &quot;c&quot;
    &quot;cats&quot;          =~ /cats|cat|ca|c/; # matches &quot;cats&quot;
</pre>
<p> At a given character position, the first alternative that allows the regex match to succeed will be the one that matches. Here, all the alternatives match at the first string position, so the first matches.</p>
<h3>Grouping things and hierarchical matching</h3>
<p> The <code>grouping</code> metacharacters <tt>&quot;()&quot;</tt> allow a part of a regex to be treated as a single unit. Parts of a regex are grouped by enclosing them in parentheses. The regex <tt>&quot;house(cat|keeper)&quot;</tt> means match <tt>&quot;house&quot;</tt> followed by either <tt>&quot;cat&quot;</tt> or <tt>&quot;keeper&quot;</tt>. Some more examples are </p>
<p>/ (a | b) b / ;<br />
#matches &#8216;ab&#8217; or &#8216;bb&#8217; / (^a | b) c / ;<br />
#matches &#8216;ac&#8217; at start of string or &#8216;bc&#8217; anywhere / house(cat |) / ;<br />
#matches either &#8216;housecat&#8217; or &#8216;house&#8217; / house(cat(s |) |) / ;<br />
#matches either &#8216;housecats&#8217; or &#8216;housecat&#8217; or<br />
#&#8217;house&#8217;.Note groups can be nested.<br />
    &#8220;20&#8221; = ~ / (19 | 20 |)\d\d /<br />
    ;<br />
#matches the null alternative &#8216;()\d\d&#8217;,<br />
#because &#8217;20\d\d&#8217; can&#8217;t match</p>
<h3>Extracting matches</h3>
<p> The grouping metacharacters <tt>&quot;()&quot;</tt> also allow the extraction of the parts of a string that matched. For each grouping, the part that matched inside goes into the special variables <tt>$1</tt>, <tt>$2</tt>, etc. They can be used just as ordinary variables: </p>
<p>#extract hours, minutes, seconds<br />
$time = ~ / (\d\d)<br />
    : (\d\d)<br />
    : (\d\d) /<br />
    ;<br />
#match hh : mm : ss format<br />
    $hours = $1;<br />
$minutes = $2;<br />
$seconds = $3;</p>
<p> In list context, a match <tt>&quot;/regex/&quot;</tt> with groupings will return the list of matched values <tt>&quot;($1,$2,...)&quot;</tt>. So we could rewrite it as </p>
<pre>
    ($hours, $minutes, $second) = ($time =~ /(\d\d):(\d\d):(\d\d)/);
</pre>
<p> If the groupings in a regex are nested, <tt>$1</tt> gets the group with the leftmost opening parenthesis, <tt>$2</tt> the next opening parenthesis, etc. For example, here is a complex regex and the matching variables indicated below it: </p>
<pre>
    /(ab(cd|ef)((gi)|j))/;
     1  2      34
</pre>
<p> Associated with the matching variables <tt>$1</tt>, <tt>$2</tt>, &#8230; are the <code>backreferences</code> <tt>&quot;\g1&quot;</tt>, <tt>&quot;\g2&quot;</tt>, &#8230; Backreferences are matching variables that can be used <i>inside</i> a regex: </p>
<pre>
    /(\w\w\w)\s\g1/; # find sequences like 'the the' in string
</pre>
<p> <tt>$1</tt>, <tt>$2</tt>, &#8230; should only be used outside of a regex, and <tt>&quot;\g1&quot;</tt>, <tt>&quot;\g2&quot;</tt>, &#8230; only inside a regex.</p>
<h3>Matching repetitions</h3>
<p> The <code>quantifier</code> metacharacters <tt>&quot;?&quot;</tt>, <tt>&quot;*&quot;</tt>, <tt>&quot;+&quot;</tt>, and <tt>&quot;{}&quot;</tt> allow us to determine the number of repeats of a portion of a regex we consider to be a match. Quantifiers are put immediately after the character, character class, or grouping that we want to specify. They have the following meanings:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;a?&quot;</tt> = match &#8216;a&#8217; 1 or 0 times</p>
<dt>&bull;</p>
<dd> <tt>&quot;a*&quot;</tt> = match &#8216;a&#8217; 0 or more times, i.e., any number of times</p>
<dt>&bull;</p>
<dd> <tt>&quot;a+&quot;</tt> = match &#8216;a&#8217; 1 or more times, i.e., at least once</p>
<dt>&bull;</p>
<dd> <tt>&quot;a{n,m}&quot;</tt> = match at least <tt>&quot;n&quot;</tt> times, but not more than <tt>&quot;m&quot;</tt> times.</p>
<dt>&bull;</p>
<dd> <tt>&quot;a{n,}&quot;</tt> = match at least <tt>&quot;n&quot;</tt> or more times</p>
<dt>&bull;</p>
<dd> <tt>&quot;a{n}&quot;</tt> = match exactly <tt>&quot;n&quot;</tt> times</dl>
<p> Here are some examples: </p>
<p>/ [a &#8211; z] +\s +\d * / ;<br />
#match a lowercase word, at least some space, and<br />
#any number of digits<br />
                                                      / (\w +)\s +\g1 /<br />
    ;<br />
#match doubled words of arbitrary length<br />
    $year = ~ / ^\d{2, 4 } $ / ;<br />
#make sure year is at least 2 but not more<br />
#than 4 digits<br />
    $year = ~ / ^\d{4 } $ | ^\d{2 } $ / ;<br />
#better match;<br />
throw out 3 digit dates</p>
<p> These quantifiers will try to match as much of the string as possible, while still allowing the regex to match. So we have </p>
<pre>
    $x = 'the cat in the hat';
    $x =~ /^(.*)(at)(.*)$/; # matches,
                            # $1 = 'the cat in the h'
                            # $2 = 'at'
                            # $3 = ''   (0 matches)
</pre>
<p> The first quantifier <tt>&quot;.*&quot;</tt> grabs as much of the string as possible while still having the regex match. The second quantifier <tt>&quot;.*&quot;</tt> has no string left to it, so it matches 0 times.</p>
<h3>More matching</h3>
<p> There are a few more things you might want to know about matching operators. The global modifier <tt>&quot;/g&quot;</tt> allows the matching operator to match within a string as many times as possible. In scalar context, successive matches against a string will have <tt>&quot;/g&quot;</tt> jump from match to match, keeping track of position in the string as it goes along. You can get or set the position with the <tt>&quot;pos()&quot;</tt> function. For example, </p>
<p>$x = &#8220;cat dog house&#8221;;<br />
# 3 words while ($x = ~/(\w +) / g)<br />
{<br />
    print &#8220;Word is $1, ends at position &#8220;, pos $x, &#8220;
&#8221;;<br />
}</p>
<p> prints </p>
<pre>
    Word is cat, ends at position 3
    Word is dog, ends at position 7
    Word is house, ends at position 13
</pre>
<p> A failed match or changing the target string resets the position. If you don&#8217;t want the position reset after failure to match, add the <tt>&quot;/c&quot;</tt>, as in <tt>&quot;/regex/gc&quot;</tt>. </p>
<p> In list context, <tt>&quot;/g&quot;</tt> returns a list of matched groupings, or if there are no groupings, a list of matches to the whole regex. So </p>
<p>@words = ($x = ~ / (\w +) / g);<br />
#matches,<br />
#$word[0] = &#8216;cat&#8217;<br />
#$word[1] = &#8216;dog&#8217;<br />
#$word[2] = &#8216;house&#8217;</p>
<h3>Search and replace</h3>
<p> Search and replace is performed using <tt>&quot;s/regex/replacement/modifiers&quot;</tt>. The <tt>&quot;replacement&quot;</tt> is a Perl double-quoted string that replaces in the string whatever is matched with the <tt>&quot;regex&quot;</tt>. The operator <tt>&quot;=~&quot;</tt> is also used here to associate a string with <tt>&quot;s///&quot;</tt>. If matching against <tt>$_</tt>, the <tt>&quot;$_ =~&quot;</tt> can be dropped. If there is a match, <tt>&quot;s///&quot;</tt> returns the number of substitutions made; otherwise it returns false. Here are a few examples: </p>
<p>$x = &#8220;Time to feed the cat!&#8221;;<br />
$x = ~s / cat / hacker / ;<br />
#$x contains &#8220;Time to feed the hacker!&#8221; $y = &#8220;&#8216;quoted words'&#8221;;<br />
$y = ~s / ^'(.*)&#8217; $ / $1 / ;<br />
#strip single quotes,<br />
#$y contains &#8220;quoted words&#8221;</p>
<p> With the <tt>&quot;s///&quot;</tt> operator, the matched variables <tt>$1</tt>, <tt>$2</tt>, etc. are immediately available for use in the replacement expression. With the global modifier, <tt>&quot;s///g&quot;</tt> will search and replace all occurrences of the regex in the string: </p>
<p>$x = &#8220;I batted 4 for 4&#8221;;<br />
$x = ~s / 4 / four / ;<br />
#$x contains &#8220;I batted four for 4&#8221; $x = &#8220;I batted 4 for 4&#8221;;<br />
$x = ~s / 4 / four / g;<br />
#$x contains &#8220;I batted four for four&#8221;</p>
<p> The non-destructive modifier <tt>&quot;s///r&quot;</tt> causes the result of the substitution to be returned instead of modifying <tt>$_</tt> (or whatever variable the substitute was bound to with <tt>&quot;=~&quot;</tt>): </p>
<p>$x = &#8220;I like dogs.&#8221;;<br />
$y = $x = ~s / dogs / cats / r;<br />
print &#8220;$x $y
&#8221;;<br />
#prints &#8220;I like dogs. I like cats.&#8221; $x = &#8220;Cats are great.&#8221;;<br />
print $x = ~s / Cats / Dogs / r = ~s / Dogs / Frogs / r = ~s / Frogs / Hedgehogs / r, &#8220;
&#8221;;<br />
#prints &#8220;Hedgehogs are great.&#8221;<br />
@foo = map{s / [a &#8211; z] / X / r} qw(a b c 1 2 3);<br />
#@foo is now qw(X X X 1 2 3)</p>
<p> The evaluation modifier <tt>&quot;s///e&quot;</tt> wraps an <tt>&quot;eval{...}&quot;</tt> around the replacement string and the evaluated result is substituted for the matched substring. Some examples: </p>
<p>#reverse all the words in a string<br />
$x = &#8220;the cat in the hat&#8221;;<br />
$x = ~s / (\w +) / reverse $1 / ge;<br />
#$x contains &#8220;eht tac ni eht tah&#8221;<br />
#convert percentage to decimal<br />
    $x = &#8220;A 39% hit rate&#8221;;<br />
$x = ~s !(\d +) % !$1 / 100 !e;<br />
#$x contains &#8220;A 0.39 hit rate&#8221;</p>
<p> The last example shows that <tt>&quot;s///&quot;</tt> can use other delimiters, such as <tt>&quot;s!!!&quot;</tt> and <tt>&quot;s{}{}&quot;</tt>, and even <tt>&quot;s{}//&quot;</tt>. If single quotes are used <tt>&quot;s'''&quot;</tt>, then the regex and replacement are treated as single-quoted strings.</p>
<h3>The split operator</h3>
<p> <tt>&quot;split /regex/, string&quot;</tt> splits <tt>&quot;string&quot;</tt> into a list of substrings and returns that list. The regex determines the character sequence that <tt>&quot;string&quot;</tt> is split with respect to. For example, to split a string into words, use </p>
<p>$x = &#8220;Calvin and Hobbes&#8221;;<br />
@word = split /\s + /, $x;<br />
#$word[0] = &#8216;Calvin&#8217;<br />
#$word[1] = &#8216;and&#8217;<br />
#$word[2] = &#8216;Hobbes&#8217;</p>
<p> To extract a comma-delimited list of numbers, use </p>
<p>$x = &#8220;1.618,2.718,   3.142&#8221;;<br />
@ const = split /,\s * /, $x;<br />
#$const[0] = &#8216;1.618&#8217;<br />
#$const[1] = &#8216;2.718&#8217;<br />
#$const[2] = &#8216;3.142&#8217;</p>
<p> If the empty regex <tt>&quot;//&quot;</tt> is used, the string is split into individual characters. If the regex has groupings, then the list produced contains the matched substrings from the groupings as well: </p>
<pre><code>
$x = "/usr/bin";
@parts = split m !(/) !, $x;
#$parts[0] = ''
#$parts[1] = '/'
#$parts[2] = 'usr'
#$parts[3] = '/'
#$parts[4] = 'bin'
</code></pre>
<p> Since the first character of <tt>$x</tt> matched the regex, <tt>&quot;split&quot;</tt> prepended an empty initial element to the list.</p>
<h3>use re &#8216;strict&#8217;</h3>
<p> New in v5.22, this applies stricter rules than otherwise when compiling regular expression patterns. It can find things that, while legal, may not be what you intended. </p>
<p> See &#8216;strict&#8217; in re.</p>
<h2>BUGS</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> This is just a quick start guide. For a more in-depth tutorial on regexes, see perlretut and for the reference page, see perlre.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 2000 Mark Kvale All rights reserved. </p>
<p> This document may be distributed under the same terms as Perl itself.</p>
<h3>Acknowledgments</h3>
<p> The author would like to thank Mark-Jason Dominus, Tom Christiansen, Ilya Zakharevich, Brad Hughes, and Mike Giroux for all their helpful comments. </p>
<h2>Index</h2>
