---
title: "perlretut(1)"
name: "perlretut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlretut/"
description: "perlretut – Perl regular expressions tutorial"
---

<h2 class="name">NAME</h2>
<p> perlretut &#8211; Perl regular expressions tutorial </p>
<h2>DESCRIPTION</h2>
<p> This page provides a basic tutorial on understanding, creating and using regular expressions in Perl. It serves as a complement to the reference page on regular expressions perlre. Regular expressions are an integral part of the <tt>&quot;m//&quot;</tt>, <tt>&quot;s///&quot;</tt>, <tt>&quot;qr//&quot;</tt> and <tt>&quot;split&quot;</tt> operators and so this tutorial also overlaps with &#8220;Regexp Quote-Like Operators&#8221; in perlop and &#8220;split&#8221; in perlfunc. </p>
<p> Perl is widely renowned for excellence in text processing, and regular expressions are one of the big factors behind this fame. Perl regular expressions display an efficiency and flexibility unknown in most other computer languages. Mastering even the basics of regular expressions will allow you to manipulate text with surprising ease. </p>
<p> What is a regular expression? At its most basic, a regular expression is a template that is used to determine if a string has certain characteristics. The string is most often some text, such as a line, sentence, web page, or even a whole book, but less commonly it could be some binary data as well. Suppose we want to determine if the text in variable, <tt>$var</tt> contains the sequence of characters <tt>&quot;m u s h r o o m&quot;</tt> (blanks added for legibility). We can write in Perl </p>
<pre>
 $var =~ m/mushroom/
</pre>
<p> The value of this expression will be <font SIZE="-1">TRUE</font> if <tt>$var</tt> contains that sequence of characters, and <font SIZE="-1">FALSE</font> otherwise. The portion enclosed in <tt>'/'</tt> characters denotes the characteristic we are looking for. We use the term <i>pattern</i> for it. The process of looking to see if the pattern occurs in the string is called <i>matching</i>, and the <tt>&quot;=~&quot;</tt> operator along with the <tt>&quot;m//&quot;</tt> tell Perl to try to match the pattern against the string. Note that the pattern is also a string, but a very special kind of one, as we will see. Patterns are in common use these days; examples are the patterns typed into a search engine to find web pages and the patterns used to list files in a directory, <i>e.g.</i>, &quot;<tt>&quot;ls *.txt&quot;</tt>&#8220; or &#8221;<tt>&quot;dir *.*&quot;</tt>&quot;. In Perl, the patterns described by regular expressions are used not only to search strings, but to also extract desired parts of strings, and to do search and replace operations. </p>
<p> Regular expressions have the undeserved reputation of being abstract and difficult to understand. This really stems simply because the notation used to express them tends to be terse and dense, and not because of inherent complexity. We recommend using the <tt>&quot;/x&quot;</tt> regular expression modifier (described below) along with plenty of white space to make them less dense, and easier to read. Regular expressions are constructed using simple concepts like conditionals and loops and are no more difficult to understand than the corresponding <tt>&quot;if&quot;</tt> conditionals and <tt>&quot;while&quot;</tt> loops in the Perl language itself. </p>
<p> This tutorial flattens the learning curve by discussing regular expression concepts, along with their notation, one at a time and with many examples. The first part of the tutorial will progress from the simplest word searches to the basic regular expression concepts. If you master the first part, you will have all the tools needed to solve about 98% of your needs. The second part of the tutorial is for those comfortable with the basics and hungry for more power tools. It discusses the more advanced regular expression operators and introduces the latest cutting-edge innovations. </p>
<p> A note: to save time, &#8220;regular expression&#8221; is often abbreviated as regexp or regex. Regexp is a more natural abbreviation than regex, but is harder to pronounce. The Perl pod documentation is evenly split on regexp vs regex; in Perl, there is more than one way to abbreviate it. We&#8217;ll use regexp in this tutorial. </p>
<p> New in v5.22, <tt>&quot;use re 'strict'&quot;</tt> applies stricter rules than otherwise when compiling regular expression patterns. It can find things that, while legal, may not be what you intended.</p>
<h2>Part 1: The basics</h2>
<h3>Simple word matching</h3>
<p> The simplest regexp is simply a word, or more generally, a string of characters. A regexp consisting of just a word matches any string that contains that word: </p>
<pre>
    &quot;Hello World&quot; =~ /World/;  # matches
</pre>
<p> What is this Perl statement all about? <tt>&quot;Hello World&quot;</tt> is a simple double-quoted string. <tt>&quot;World&quot;</tt> is the regular expression and the <tt>&quot;//&quot;</tt> enclosing <tt>&quot;/World/&quot;</tt> tells Perl to search a string for a match. The operator <tt>&quot;=~&quot;</tt> associates the string with the regexp match and produces a true value if the regexp matched, or false if the regexp did not match. In our case, <tt>&quot;World&quot;</tt> matches the second word in <tt>&quot;Hello World&quot;</tt>, so the expression is true. Expressions like this are useful in conditionals: </p>
<pre><code>
if ("Hello World" = ~ / World /) {
    print "It matches
";
} else {
    print "It doesn't match
";
}
</code></pre>
<p> There are useful variations on this theme. The sense of the match can be reversed by using the <tt>&quot;!~&quot;</tt> operator: </p>
<p>if (&#8220;Hello World&#8221; !~ / World /) {<br />
    print &#8220;It doesn&#8217;t match
&#8221;;<br />
} else {<br />
    print &#8220;It matches
&#8221;;<br />
}</p>
<p> The literal string in the regexp can be replaced by a variable: </p>
<p>my $greeting = &#8220;World&#8221;;<br />
if (&#8220;Hello World&#8221; = ~ / $greeting /) {<br />
    print &#8220;It matches
&#8221;;<br />
} else {<br />
    print &#8220;It doesn&#8217;t match
&#8221;;<br />
}</p>
<p> If you&#8217;re matching against the special default variable <tt>$_</tt>, the <tt>&quot;$_ =~&quot;</tt> part can be omitted: </p>
<p>$_ = &#8220;Hello World&#8221;;<br />
if (/ World /) {<br />
    print &#8220;It matches
&#8221;;<br />
} else {<br />
    print &#8220;It doesn&#8217;t match
&#8221;;<br />
}</p>
<p> And finally, the <tt>&quot;//&quot;</tt> default delimiters for a match can be changed to arbitrary delimiters by putting an <tt>'m'</tt> out front: </p>
<p>&#8220;Hello World&#8221; = ~m !World !;<br />
#matches, delimited by &#8216;!&#8217; &#8220;Hello World&#8221; = ~m{World };<br />
#matches, note the matching &#8216;{}&#8217; &#8220;/usr/bin/perl&#8221; = ~m &#8220;/perl&#8221;;<br />
#matches after &#8216;/usr/bin&#8217;,<br />
#&#8217;/&#8217; becomes an ordinary char</p>
<p> <tt>&quot;/World/&quot;</tt>, <tt>&quot;m!World!&quot;</tt>, and <tt>&quot;m{World}&quot;</tt> all represent the same thing. When, <i>e.g.</i>, the quote (<tt>'&quot;'</tt>) is used as a delimiter, the forward slash <tt>'/'</tt> becomes an ordinary character and can be used in this regexp without trouble. </p>
<p> Let&#8217;s consider how different regexps would match <tt>&quot;Hello World&quot;</tt>: </p>
<p>&#8220;Hello World&#8221; = ~ / world / ;<br />
#doesn&#8217;t match &#8220;Hello World&#8221; = ~ / o W / ;<br />
#matches<br />
    &#8220;Hello World&#8221; = ~ / oW /<br />
    ;<br />
#doesn&#8217;t match &#8220;Hello World&#8221; = ~ / World / ;<br />
#doesn&#8217;t match</p>
<p> The first regexp <tt>&quot;world&quot;</tt> doesn&#8217;t match because regexps are case-sensitive. The second regexp matches because the substring <tt>'o W'</tt> occurs in the string <tt>&quot;Hello World&quot;</tt>. The space character <tt>' '</tt> is treated like any other character in a regexp and is needed to match in this case. The lack of a space character is the reason the third regexp <tt>'oW'</tt> doesn&#8217;t match. The fourth regexp &quot;<tt>&quot;World &quot;</tt>&quot; doesn&#8217;t match because there is a space at the end of the regexp, but not at the end of the string. The lesson here is that regexps must match a part of the string <i>exactly</i> in order for the statement to be true. </p>
<p> If a regexp matches in more than one place in the string, Perl will always match at the earliest possible point in the string: </p>
<pre>
    &quot;Hello World&quot; =~ /o/;       # matches 'o' in 'Hello'
    &quot;That hat is red&quot; =~ /hat/; # matches 'hat' in 'That'
</pre>
<p> With respect to character matching, there are a few more points you need to know about. First of all, not all characters can be used &#8220;as is&#8221; in a match. Some characters, called <i>metacharacters</i>, are generally reserved for use in regexp notation. The metacharacters are </p>
<p>{}[]() ^ $.| *+? -#\</p>
<p> This list is not as definitive as it may appear (or be claimed to be in other documentation). For example, <tt>&quot;#&quot;</tt> is a metacharacter only when the <tt>&quot;/x&quot;</tt> pattern modifier (described below) is used, and both <tt>&quot;}&quot;</tt> and <tt>&quot;]&quot;</tt> are metacharacters only when paired with opening <tt>&quot;{&quot;</tt> or <tt>&quot;[&quot;</tt> respectively; other gotchas apply. </p>
<p> The significance of each of these will be explained in the rest of the tutorial, but for now, it is important only to know that a metacharacter can be matched as-is by putting a backslash before it: </p>
<p>&#8220;2+2=4&#8221; = ~ / 2 + 2 / ;<br />
#doesn&#8217;t match, + is a metacharacter &#8220;2+2=4&#8221; = ~ / 2\+ 2 / ;<br />
#matches, \+ is treated like an ordinary +<br />
              &#8220;The interval is [0,1).&#8221; = ~ / [0, 1)./ #is a syntax error !&#8221;The interval is [0,1).&#8221; = ~ /\[0, 1\)\./ #matches<br />
                                                                                                             &#8220;#!/usr/bin/perl&#8221; = ~ / #!\/ usr\/ bin\/ perl /<br />
                                                                                                     ; #matches</p>
<p> In the last regexp, the forward slash <tt>'/'</tt> is also backslashed, because it is used to delimit the regexp. This can lead to <font SIZE="-1">LTS</font> (leaning toothpick syndrome), however, and it is often more readable to change delimiters. </p>
<pre>
    &quot;#!/usr/bin/perl&quot; =~ m!#\!/usr/bin/perl!;  # easier to read
</pre>
<p> The backslash character <tt>'\'</tt> is a metacharacter itself and needs to be backslashed: </p>
<pre>
    'C:\WIN32' =~ /C:\WIN/;   # matches
</pre>
<p> In situations where it doesn&#8217;t make sense for a particular metacharacter to mean what it normally does, it automatically loses its metacharacter-ness and becomes an ordinary character that is to be matched literally. For example, the <tt>'}'</tt> is a metacharacter only when it is the mate of a <tt>'{'</tt> metacharacter. Otherwise it is treated as a literal <font SIZE="-1">RIGHT CURLY BRACKET.</font> This may lead to unexpected results. <tt>&quot;use re 'strict'&quot;</tt> can catch some of these. </p>
<p> In addition to the metacharacters, there are some <font SIZE="-1">ASCII</font> characters which don&#8217;t have printable character equivalents and are instead represented by <i>escape sequences</i>. Common examples are <tt>&quot;	&quot;</tt> for a tab, <tt>&quot;
&quot;</tt> for a newline, <tt>&quot;&quot;</tt> for a carriage return and <tt>&quot;&quot;</tt> for a bell (or alert). If your string is better thought of as a sequence of arbitrary bytes, the octal escape sequence, <i>e.g.</i>, <tt>&quot;&quot;</tt>, or hexadecimal escape sequence, <i>e.g.</i>, <tt>&quot;&quot;</tt> may be a more natural representation for your bytes. Here are some examples of escapes: </p>
<pre>
    &quot;1000	2000&quot; =~ m(0	2)   # matches
    &quot;1000
2000&quot; =~ /0
20/   # matches
    &quot;1000	2000&quot; =~ /
