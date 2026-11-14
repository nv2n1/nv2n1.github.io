---
title: "perlfaq6(1)"
name: "perlfaq6"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq6/"
description: "perlfaq6 – Regular Expressions"
---

<h2 class="name">NAME</h2>
<p> perlfaq6 &#8211; Regular Expressions </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section is surprisingly small because the rest of the <font SIZE="-1">FAQ</font> is littered with answers involving regular expressions. For example, decoding a <font SIZE="-1">URL</font> and checking whether something is a number can be handled with regular expressions, but those answers are found elsewhere in this document (in perlfaq9: &#8220;How do I decode or create those %-encodings on the web&#8221; and perlfaq4: &#8220;How do I determine whether a scalar is a number/whole/integer/float&#8221;, to be precise).</p>
<h3>How can I hope to use regular expressions without creating illegible and unmaintainable code?</h3>
<p> Three techniques can make regular expressions maintainable and understandable.</p>
<dl>
<dt>Comments Outside the Regex</p>
<dd> Describe what you&#8217;re doing and how you&#8217;re doing it, using normal Perl comments. </p>
<pre>
    # turn the line into the first word, a colon, and the
    # number of characters on the rest of the line
    s/^(\w+)(.*)/ lc($1) . &quot;:&quot; . length($2) /meg;
</pre>
<dt>Comments Inside the Regex</p>
<dd> The <tt>&quot;/x&quot;</tt> modifier causes whitespace to be ignored in a regex pattern (except in a character class and a few other places), and also allows you to use normal comments there, too. As you can imagine, whitespace and comments help a lot. </p>
<p> <tt>&quot;/x&quot;</tt> lets you turn this: </p>
<pre>
    s{&lt;(?:[^&gt;'&quot;]*|&quot;.*?&quot;|'.*?')+&gt;}{}gs;
</pre>
<p> into this: </p>
<pre><code>
    s{ &lt;                    # opening angle bracket
        (?:                 # Non-backreffing grouping paren
            [^&gt;'"] *        # 0 or more things that are neither &gt; nor ' nor "
                |           #    or else
            ".*?"           # a section between double quotes (stingy match)
                |           #    or else
            '.*?'           # a section between single quotes (stingy match)
        ) +                 #   all occurring one or more times
        &gt;                   # closing angle bracket
    }
    {
    }
    gsx;
#replace with nothing, i.e.delete
</code></pre>
<p> It&#8217;s still not quite so clear as prose, but it is very useful for describing the meaning of each part of the pattern.</p>
<dt>Different Delimiters</p>
<dd> While we normally think of patterns as being delimited with <tt>&quot;/&quot;</tt> characters, they can be delimited by almost any character. perlre describes this. For example, the <tt>&quot;s///&quot;</tt> above uses braces as delimiters. Selecting another delimiter can avoid quoting the delimiter within the pattern: </p>
<pre>
    s/\/usr\/local/\/usr\/share/g;    # bad delimiter choice
    s#/usr/local#/usr/share#g;        # better
</pre>
<p> Using logically paired delimiters can be even more readable: </p>
<p>s{ / usr / local / } { / usr / share} g;<br />
#better still
</dl>
<h3>I&#8217;m having trouble matching over more than one line. What&#8217;s wrong?</h3>
<p> Either you don&#8217;t have more than one line in the string you&#8217;re looking at (probably), or else you aren&#8217;t using the correct modifier(s) on your pattern (possibly). </p>
<p> There are many ways to get multiline data into a string. If you want it to happen automatically while reading input, you&#8217;ll want to set $/ (probably to &#8221; for paragraphs or <tt>&quot;undef&quot;</tt> for the whole file) to allow you to read more than one line at a time. </p>
<p> Read perlre to help you decide which of <tt>&quot;/s&quot;</tt> and <tt>&quot;/m&quot;</tt> (or both) you might want to use: <tt>&quot;/s&quot;</tt> allows dot to include newline, and <tt>&quot;/m&quot;</tt> allows caret and dollar to match next to a newline, not just at the end of the string. You do need to make sure that you&#8217;ve actually got a multiline string in there. </p>
<p> For example, this program detects duplicate words, even when they span line breaks (but not paragraph ones). For this example, we don&#8217;t need <tt>&quot;/s&quot;</tt> because we aren&#8217;t using dot in a regular expression that we want to cross line boundaries. Neither do we need <tt>&quot;/m&quot;</tt> because we don&#8217;t want caret or dollar to match at any point inside the record next to newlines. But it&#8217;s imperative that $/ be set to something other than the default, or else we won&#8217;t actually ever have a multiline record read in. </p>
<p>$ / = &#8221;;<br />
#read in whole paragraph, not just one line while (&lt;&gt;)<br />
{<br />
        while ( /([\w&#8217;-]+)(\s+\g1)+/gi ) {     # word starts alpha<br />
            print &#8220;Duplicate $1 at paragraph $.
&#8221;;<br />
}<br />
}</p>
<p> Here&#8217;s some code that finds sentences that begin with &#8220;From &#8221; (which would be mangled by many mailers): </p>
<p>$ / = &#8221;;<br />
#read in whole paragraph, not just one line while (&lt;&gt;)<br />
{<br />
    while (/ ^From / gm) {<br />
#/ m makes ^ match next to 
 print &#8220;leading From in paragraph $.
&#8221;;<br />
    }<br />
}</p>
<p> Here&#8217;s code that finds everything between <font SIZE="-1">START</font> and <font SIZE="-1">END</font> in a paragraph: </p>
<p>undef $ / ;<br />
#read in whole file, not just one line or paragraph while (&lt;&gt;)<br />
{<br />
        while ( /START(.*?)END/sgm ) {<br />
#/ s makes.cross line boundaries print &#8220;$1
&#8221;;<br />
        }<br />
}</p>
<h3>How can I pull out lines between two patterns that are themselves on different lines?</h3>
<p> You can use Perl&#8217;s somewhat exotic <tt>&quot;..&quot;</tt> operator (documented in perlop): </p>
<pre>
    perl -ne 'print if /START/ .. /END/' file1 file2 ...
</pre>
<p> If you wanted text and not lines, you would use </p>
<pre>
    perl -0777 -ne 'print &quot;$1
&quot; while /START(.*?)END/gs' file1 file2 ...
</pre>
<p> But if you want nested occurrences of <tt>&quot;START&quot;</tt> through <tt>&quot;END&quot;</tt>, you&#8217;ll run up against the problem described in the question in this section on matching balanced text. </p>
<p> Here&#8217;s another example of using <tt>&quot;..&quot;</tt>: </p>
<p>while (&lt;&gt;) {<br />
    my $in_header = 1../ ^$ / ;<br />
    my $in_body = / ^$ /..eof;<br />
#now choose between them<br />
}<br />
continue<br />
{<br />
    $.= 0 if eof;<br />
#fix $.<br />
}</p>
<h3>How do I match <font SIZE="-1">XML, HTML,</font> or other nasty, ugly things with a regex?</h3>
<p> Do not use regexes. Use a module and forget about the regular expressions. The XML::LibXML, HTML::TokeParser and HTML::TreeBuilder modules are good starts, although each namespace has other parsing modules specialized for certain tasks and different ways of doing it. Start at <font SIZE="-1">CPAN</font> Search ( &lt;<a rel="nofollow" href="http://metacpan.org/">http://metacpan.org/</a>&gt; ) and wonder at all the work people have done for you already! :)</p>
<h3>I put a regular expression into $/ but it didn&#8217;t work. What&#8217;s wrong?</h3>
<p> $/ has to be a string. You can use these examples if you really need to do this. </p>
<p> If you have File::Stream, this is easy. </p>
<p>use File::Stream;<br />
my $stream = File::Stream-&gt;new (<br />
    $filehandle,<br />
    separator = &gt; qr /\s *,\s * /, );<br />
print &#8220;$_
&#8221; while&lt;$stream&gt;;</p>
<p> If you don&#8217;t have File::Stream, you have to do a little more work. </p>
<p> You can use the four-argument form of sysread to continually add to a buffer. After you add to the buffer, you check if you have a complete line (using your regular expression). </p>
<p>local $_ = &#8220;&#8221;;<br />
while (sysread FH, $_, 8192, length) {<br />
        while( s/^((?s).*?)your_pattern// ) {<br />
            my $record = $1;<br />
#do stuff here.<br />
}<br />
}</p>
<p> You can do the same thing with foreach and a match using the c flag and the \G anchor, if you do not mind your entire file being in memory at the end. </p>
<p>local $_ = &#8220;&#8221;;<br />
while (sysread FH, $_, 8192, length) {<br />
    foreach my $record ( m/\G((?s).*?)your_pattern/gc ) {<br />
#do stuff here.<br />
        }<br />
        substr( $_, 0, pos ) = &#8220;&#8221; if pos;<br />
}</p>
<h3>How do I substitute case-insensitively on the <font SIZE="-1">LHS</font> while preserving case on the <font SIZE="-1">RHS</font>?</h3>
<p> Here&#8217;s a lovely Perlish solution by Larry Rosler. It exploits properties of bitwise xor on <font SIZE="-1">ASCII</font> strings. </p>
<p>$_ = &#8220;this is a TEsT case&#8221;;<br />
$old = &#8216;test&#8217;;<br />
$new = &#8216;success&#8217;;<br />
s{(\Q$old\E)} {uc $new | (uc $1 ^ $1).(uc(substr $1, -1) ^ substr $1, -1) x(length($new) &#8211; length $1)} egi;<br />
print;</p>
<p> And here it is as a subroutine, modeled after the above: </p>
<p>sub preserve_case<br />
{<br />
    my($old, $new) = @_;<br />
    my $mask = uc $old ^ $old;<br />
    uc $new | $mask.substr($mask, -1) x(length($new) &#8211; length($old))<br />
}<br />
$string = &#8220;this is a TEsT case&#8221;;<br />
$string = ~s / (test) / preserve_case($1, &#8220;success&#8221;) / egi;<br />
print &#8220;$string
&#8221;;</p>
<p> This prints: </p>
<pre>
    this is a SUcCESS case
</pre>
<p> As an alternative, to keep the case of the replacement word if it is longer than the original, you can use this code, by Jeff Pinyan: </p>
<p>sub preserve_case<br />
{<br />
    my($from, $to) = @_;<br />
    my($lf, $lt) = map length, @_;<br />
    if ($lt &lt; $lf) {<br />
        $from = substr $from, 0, $lt<br />
    } else {<br />
        $from.= substr $to, $lf<br />
    }<br />
    return uc $to | ($from ^ uc $from);<br />
}</p>
<p> This changes the sentence to &#8220;this is a SUcCess case.&#8221; </p>
<p> Just to show that C programmers can write C in any programming language, if you prefer a more C-like solution, the following script makes the substitution have the same case, letter by letter, as the original. (It also happens to run about 240% slower than the Perlish solution runs.) If the substitution has more characters than the string being substituted, the case of the last character is used for the rest of the substitution. </p>
<p>#Original by Nathan Torkington, massaged by Jeffrey Friedl<br />
#<br />
sub preserve_case<br />
{<br />
    my($old, $new) = @_;<br />
    my $state = 0;<br />
# 0 = no change;<br />
    1 = lc;<br />
    2 = uc<br />
        my($i, $oldlen, $newlen, $c) = (0, length($old), length($new));<br />
    my $len = $oldlen &lt; $newlen ? $oldlen : $newlen;<br />
    for ($i = 0; $i &lt; $len; $i++) {<br />
        if ($c = substr($old, $i, 1), $c = ~ / [\W\d_] /) {<br />
            $state = 0;<br />
        }<br />
        elsif(lc $c eq $c)<br />
        {<br />
            substr($new, $i, 1) = lc(substr($new, $i, 1));<br />
            $state = 1;<br />
        }<br />
        else<br />
        {<br />
            substr($new, $i, 1) = uc(substr($new, $i, 1));<br />
            $state = 2;<br />
        }<br />
    }<br />
#finish up with any remaining new (for when new is longer than old)<br />
    if ($newlen &gt; $oldlen) {<br />
        if ($state == 1) {<br />
            substr($new, $oldlen) = lc(substr($new, $oldlen));<br />
        }<br />
        elsif($state == 2)<br />
        {<br />
            substr($new, $oldlen) = uc(substr($new, $oldlen));<br />
        }<br />
    }<br />
    return $new;<br />
}</p>
<h3>How can I make \w match national character sets?</h3>
<p> Put <tt>&quot;use locale;&quot;</tt> in your script. The \w character class is taken from the current locale. </p>
<p> See perllocale for details.</p>
<h3>How can I match a locale-smart version of /[a-zA-Z]/?</h3>
<p> You can use the <font SIZE="-1">POSIX</font> character class syntax <tt>&quot;/[[:alpha:]]/&quot;</tt> documented in perlre. </p>
<p> No matter which locale you are in, the alphabetic characters are the characters in \w without the digits and the underscore. As a regex, that looks like <tt>&quot;/[^\W\d_]/&quot;</tt>. Its complement, the non-alphabetics, is then everything in \W along with the digits and the underscore, or <tt>&quot;/[\W\d_]/&quot;</tt>.</p>
<h3>How can I quote a variable to use in a regex?</h3>
<p> The Perl parser will expand <tt>$variable</tt> and <tt>@variable</tt> references in regular expressions unless the delimiter is a single quote. Remember, too, that the right-hand side of a <tt>&quot;s///&quot;</tt> substitution is considered a double-quoted string (see perlop for more details). Remember also that any regex special characters will be acted on unless you precede the substitution with \Q. Here&#8217;s an example: </p>
<pre>
    $string = &quot;Placido P. Octopus&quot;;
    $regex  = &quot;P.&quot;;
    $string =~ s/$regex/Polyp/;
    # $string is now &quot;Polypacido P. Octopus&quot;
</pre>
<p> Because <tt>&quot;.&quot;</tt> is special in regular expressions, and can match any single character, the regex <tt>&quot;P.&quot;</tt> here has matched the &lt;Pl&gt; in the original string. </p>
<p> To escape the special meaning of <tt>&quot;.&quot;</tt>, we use <tt>&quot;\Q&quot;</tt>: </p>
<pre>
    $string = &quot;Placido P. Octopus&quot;;
    $regex  = &quot;P.&quot;;
    $string =~ s/\Q$regex/Polyp/;
    # $string is now &quot;Placido Polyp Octopus&quot;
</pre>
<p> The use of <tt>&quot;\Q&quot;</tt> causes the <tt>&quot;.&quot;</tt> in the regex to be treated as a regular character, so that <tt>&quot;P.&quot;</tt> matches a <tt>&quot;P&quot;</tt> followed by a dot.</p>
<h3>What is /o really for?</h3>
<p> (contributed by brian d foy) </p>
<p> The <tt>&quot;/o&quot;</tt> option for regular expressions (documented in perlop and perlreref) tells Perl to compile the regular expression only once. This is only useful when the pattern contains a variable. Perls 5.6 and later handle this automatically if the pattern does not change. </p>
<p> Since the match operator <tt>&quot;m//&quot;</tt>, the substitution operator <tt>&quot;s///&quot;</tt>, and the regular expression quoting operator <tt>&quot;qr//&quot;</tt> are double-quotish constructs, you can interpolate variables into the pattern. See the answer to &#8220;How can I quote a variable to use in a regex?&#8221; for more details. </p>
<p> This example takes a regular expression from the argument list and prints the lines of input that match it: </p>
<p>my $pattern = shift @ARGV;<br />
while (&lt;&gt;) {<br />
    print if m / $pattern / ;<br />
}</p>
<p> Versions of Perl prior to 5.6 would recompile the regular expression for each iteration, even if <tt>$pattern</tt> had not changed. The <tt>&quot;/o&quot;</tt> would prevent this by telling Perl to compile the pattern the first time, then reuse that for subsequent iterations: </p>
<p>my $pattern = shift @ARGV;<br />
while (&lt;&gt;) {<br />
    print if m / $pattern / o;<br />
#useful for Perl &lt; 5.6<br />
}</p>
<p> In versions 5.6 and later, Perl won&#8217;t recompile the regular expression if the variable hasn&#8217;t changed, so you probably don&#8217;t need the <tt>&quot;/o&quot;</tt> option. It doesn&#8217;t hurt, but it doesn&#8217;t help either. If you want any version of Perl to compile the regular expression only once even if the variable changes (thus, only using its initial value), you still need the <tt>&quot;/o&quot;</tt>. </p>
<p> You can watch Perl&#8217;s regular expression engine at work to verify for yourself if Perl is recompiling a regular expression. The <tt>&quot;use re 'debug'&quot;</tt> pragma (comes with Perl 5.005 and later) shows the details. With Perls before 5.6, you should see <tt>&quot;re&quot;</tt> reporting that its compiling the regular expression on each iteration. With Perl 5.6 or later, you should only see <tt>&quot;re&quot;</tt> report that for the first iteration. </p>
<p>use re &#8216;debug&#8217;;<br />
my $regex = &#8216;Perl&#8217;;<br />
foreach (qw(Perl Java Ruby Python)) {<br />
    print STDERR &#8220;-&#8221; x 73, &#8220;
&#8221;;<br />
    print STDERR &#8220;Trying $_&#8230;
&#8221;;<br />
    print STDERR &#8220;	$_ is good!
&#8221; if m / $regex / ;<br />
}</p>
<h3>How do I use a regular expression to strip C-style comments from a file?</h3>
<p> While this actually can be done, it&#8217;s much harder than you&#8217;d think. For example, this one-liner </p>
<p>perl &#8211; 0777 &#8211; pe &#8216;s{/\*.*?\*/}{}gs&#8217; foo.c</p>
<p> will work in many but not all cases. You see, it&#8217;s too simple-minded for certain kinds of C programs, in particular, those with what appear to be comments in quoted strings. For that, you&#8217;d need something like this, created by Jeffrey Friedl and later modified by Fred Curtis. </p>
<p>$ / = undef;<br />
$_ = &lt;&gt;;<br />
    s#/\*[^*]*\*+([^/*][^*]*\*+)*/|(&#8220;(\.|[^&#8221;\])*&#8221;|'(\.|[^&#8217;\])*&#8217;|.[^/&#8221;&#8216;\]*)#defined $2 ? $2 : &#8220;&#8221;#gse;<br />
    print;</p>
<p> This could, of course, be more legibly written with the <tt>&quot;/x&quot;</tt> modifier, adding whitespace and comments. Here it is expanded, courtesy of Fred Curtis. </p>
<p>    s{<br />
       /\*         ##  Start of /* &#8230; */ comment<br />
       [^*]*\*+    ##  Non-* followed by 1-or-more *&#8217;s<br />
       (<br />
         [^/*][^*]*\*+<br />
       )*          ##  0-or-more things which don&#8217;t start with /<br />
                   ##    but do end with &#8216;*&#8217;<br />
       /           ##  End of /* &#8230; */ comment<br />
     |         ##     OR  various things which aren&#8217;t comments:<br />
       (<br />
         &#8221;           ##  Start of &#8221; &#8230; &#8221; string<br />
         (<br />
           \.           ##  Escaped char<br />
         |               ##    OR<br />
           [^&#8221;\]        ##  Non &#8220;\<br />
         )*<br />
         &#8221;           ##  End of &#8221; &#8230; &#8221; string<br />
       |         ##     OR<br />
         &#8216;           ##  Start of &#8216; &#8230; &#8216; string<br />
         (<br />
           \.           ##  Escaped char<br />
         |               ##    OR<br />
           [^&#8217;\]        ##  Non &#8216;\<br />
         )*<br />
         &#8216;           ##  End of &#8216; &#8230; &#8216; string<br />
       |         ##     OR<br />
         .           ##  Anything other char<br />
         [^/&#8221;&#8216;\]*   ##  Chars which doesn&#8217;t start a comment, string or escape<br />
       )<br />
     }{defined $2 ? $2 : &#8220;&#8221;}gxse;</p>
<p> A slight modification also removes C<font SIZE="-2">++</font> comments, possibly spanning multiple lines using a continuation character: </p>
<p> s#/\*[^*]*\*+([^/*][^*]*\*+)*/|//([^\]|[^
][
]?)*?
|(&#8220;(\.|[^&#8221;\])*&#8221;|'(\.|[^&#8217;\])*&#8217;|.[^/&#8221;&#8216;\]*)#defined $3 ? $3 : &#8220;&#8221;#gse;</p>
<h3>Can I use Perl regular expressions to match balanced text?</h3>
<p> (contributed by brian d foy) </p>
<p> Your first try should probably be the Text::Balanced module, which is in the Perl standard library since Perl 5.8. It has a variety of functions to deal with tricky text. The Regexp::Common module can also help by providing canned patterns you can use. </p>
<p> As of Perl 5.10, you can match balanced text with regular expressions using recursive patterns. Before Perl 5.10, you had to resort to various tricks such as using Perl code in <tt>&quot;(??{})&quot;</tt> sequences. </p>
<p> Here&#8217;s an example using a recursive regular expression. The goal is to capture all of the text within angle brackets, including the text in nested angle brackets. This sample text has two &#8220;major&#8221; groups: a group with one level of nesting and a group with two levels of nesting. There are five total groups in angle brackets: </p>
<pre>
    I have some &lt;brackets in &lt;nested brackets&gt; &gt; and
    &lt;another group &lt;nested once &lt;nested twice&gt; &gt; &gt;
    and that's it.
</pre>
<p> The regular expression to match the balanced text uses two new (to Perl 5.10) regular expression features. These are covered in perlre and this example is a modified version of one in that documentation. </p>
<p> First, adding the new possessive <tt>&quot;+&quot;</tt> to any quantifier finds the longest match and does not backtrack. That&#8217;s important since you want to handle any angle brackets through the recursion, not backtracking. The group <tt>&quot;[^&lt;&gt;]++&quot;</tt> finds one or more non-angle brackets without backtracking. </p>
<p> Second, the new <tt>&quot;(?PARNO)&quot;</tt> refers to the sub-pattern in the particular capture group given by <tt>&quot;PARNO&quot;</tt>. In the following regex, the first capture group finds (and remembers) the balanced text, and you need that same pattern within the first buffer to get past the nested text. That&#8217;s the recursive part. The <tt>&quot;(?1)&quot;</tt> uses the pattern in the outer capture group as an independent part of the regex. </p>
<p> Putting it all together, you have: </p>
<p>#!/ usr / local / bin / perl5 .10.0<br />
my $string = &lt;&lt; &#8220;HERE&#8221;;<br />
    I have some &lt;brackets in &lt;nested brackets&gt; &gt; and<br />
    &lt;another group &lt;nested once &lt;nested twice&gt; &gt; &gt;<br />
    and that&#8217;s it.<br />
    HERE<br />
    my @groups = $string =~ m/<br />
            (                   # start of capture group 1<br />
            &lt;                   # match an opening angle bracket<br />
                (?:<br />
                    [^&lt;&gt;]++     # one or more non angle brackets, non backtracking<br />
                      |<br />
                    (?1)        # found &lt; or &gt;, so recurse to capture group 1<br />
                )*<br />
            &gt;                   # match a closing angle bracket<br />
            )                   # end of capture group 1<br />
            /xg;<br />
    $ &#8221; = &#8220;
	 &#8220;;<br />
        print &#8220;Found:
	@groups
&#8221;;</p>
<p> The output shows that Perl found the two major groups: </p>
<pre>
    Found:
        &lt;brackets in &lt;nested brackets&gt; &gt;
        &lt;another group &lt;nested once &lt;nested twice&gt; &gt; &gt;
</pre>
<p> With a little extra work, you can get all of the groups in angle brackets even if they are in other angle brackets too. Each time you get a balanced match, remove its outer delimiter (that&#8217;s the one you just matched so don&#8217;t match it again) and add it to a queue of strings to process. Keep doing that until you get no matches: </p>
<p>#!/ usr / local / bin / perl5 .10.0<br />
my @queue = &lt;&lt; &#8220;HERE&#8221;;<br />
    I have some &lt;brackets in &lt;nested brackets&gt; &gt; and<br />
    &lt;another group &lt;nested once &lt;nested twice&gt; &gt; &gt;<br />
    and that&#8217;s it.<br />
    HERE<br />
    my $regex = qr/<br />
            (                   # start of bracket 1<br />
            &lt;                   # match an opening angle bracket<br />
                (?:<br />
                    [^&lt;&gt;]++     # one or more non angle brackets, non backtracking<br />
                      |<br />
                    (?1)        # recurse to bracket 1<br />
                )*<br />
            &gt;                   # match a closing angle bracket<br />
            )                   # end of bracket 1<br />
            /x;<br />
    $ &#8221; = &#8220;
	 &#8220;;<br />
        while (@queue)<br />
    {<br />
        my $string = shift @queue;<br />
        my @groups = $string = ~m / $regex / g;<br />
        print &#8220;Found:
	@groups

&#8221; if @groups;<br />
        unshift @queue, map<br />
        {<br />
            s / ^ &lt; //; s/&gt;$//; $_ } @groups;<br />
        }</p>
<p> The output shows all of the groups. The outermost matches show up first and the nested matches show up later: </p>
<pre>
    Found:
        &lt;brackets in &lt;nested brackets&gt; &gt;
        &lt;another group &lt;nested once &lt;nested twice&gt; &gt; &gt;
    Found:
        &lt;nested brackets&gt;
    Found:
        &lt;nested once &lt;nested twice&gt; &gt;
    Found:
        &lt;nested twice&gt;
</pre>
<h3>What does it mean that regexes are greedy? How can I get around it?</h3>
<p> Most people mean that greedy regexes match as much as they can. Technically speaking, it&#8217;s actually the quantifiers (<tt>&quot;?&quot;</tt>, <tt>&quot;*&quot;</tt>, <tt>&quot;+&quot;</tt>, <tt>&quot;{}&quot;</tt>) that are greedy rather than the whole pattern; Perl prefers local greed and immediate gratification to overall greed. To get non-greedy versions of the same quantifiers, use (<tt>&quot;??&quot;</tt>, <tt>&quot;*?&quot;</tt>, <tt>&quot;+?&quot;</tt>, <tt>&quot;{}?&quot;</tt>). </p>
<p> An example: </p>
<pre>
    my $s1 = my $s2 = &quot;I am very very cold&quot;;
    $s1 =~ s/ve.*y //;      # I am cold
    $s2 =~ s/ve.*?y //;     # I am very cold
</pre>
<p> Notice how the second substitution stopped matching as soon as it encountered &#8220;y &#8221;. The <tt>&quot;*?&quot;</tt> quantifier effectively tells the regular expression engine to find a match as quickly as possible and pass control on to whatever is next in line, as you would if you were playing hot potato.</p>
<h3>How do I process each word on each line?</h3>
<p> Use the split function: </p>
<p>while (&lt;&gt;) {<br />
    foreach<br />
        my $word(split)<br />
        {<br />
#do something with $word here<br />
        }<br />
}</p>
<p> Note that this isn&#8217;t really a word in the English sense; it&#8217;s just chunks of consecutive non-whitespace characters. </p>
<p> To work with only alphanumeric sequences (including underscores), you might consider </p>
<p>while (&lt;&gt;) {<br />
    foreach<br />
        $word(m / (\w +) / g)<br />
        {<br />
#do something with $word here<br />
        }<br />
}</p>
<h3>How can I print out a word-frequency or line-frequency summary?</h3>
<p> To do this, you have to parse out each word in the input stream. We&#8217;ll pretend that by word you mean chunk of alphabetics, hyphens, or apostrophes, rather than the non-whitespace chunk idea of a word given in the previous question: </p>
<p>my(% seen);<br />
while (&lt;&gt;) {<br />
        while ( /([^\W_\d][\w&#8217;-]+)/g ) {   # misses &#8220;`sheep'&#8221;<br />
            $seen{<br />
        $1}++;<br />
}<br />
}<br />
while (my($word, $count) = each % seen) {<br />
    print &#8220;$count $word
&#8221;;<br />
}</p>
<p> If you wanted to do the same thing for lines, you wouldn&#8217;t need a regular expression: </p>
<p>my(% seen);<br />
while (&lt;&gt;) {<br />
    $seen<br />
    {<br />
        $_<br />
    }<br />
    ++;<br />
}<br />
while (my($line, $count) = each % seen) {<br />
    print &#8220;$count $line&#8221;;<br />
}</p>
<p> If you want these output in a sorted order, see perlfaq4: &#8220;How do I sort a hash (optionally by value instead of key)?&#8221;.</p>
<h3>How can I do approximate matching?</h3>
<p> See the module String::Approx available from <font SIZE="-1">CPAN.</font></p>
<h3>How do I efficiently match many regular expressions at once?</h3>
<p> (contributed by brian d foy) </p>
<p> If you have Perl 5.10 or later, this is almost trivial. You just smart match against an array of regular expression objects: </p>
<p>my @patterns = (qr / Fr.d /, qr / B.rn.y /, qr / W.lm./);<br />
if ($string ~~@patterns) {<br />
    &#8230;<br />
};</p>
<p> The smart match stops when it finds a match, so it doesn&#8217;t have to try every expression. </p>
<p> Earlier than Perl 5.10, you have a bit of work to do. You want to avoid compiling a regular expression every time you want to match it. In this example, perl must recompile the regular expression for every iteration of the <tt>&quot;foreach&quot;</tt> loop since it has no way to know what <tt>$pattern</tt> will be: </p>
<p>my @patterns = qw(foo bar baz);<br />
LINE : while (&lt;DATA&gt;)<br />
{<br />
    foreach<br />
        $pattern(@patterns)<br />
        {<br />
            if (/$pattern / i) {<br />
                print;<br />
                next LINE;<br />
            }<br />
        }<br />
}</p>
<p> The <tt>&quot;qr//&quot;</tt> operator showed up in perl 5.005. It compiles a regular expression, but doesn&#8217;t apply it. When you use the pre-compiled version of the regex, perl does less work. In this example, I inserted a <tt>&quot;map&quot;</tt> to turn each pattern into its pre-compiled form. The rest of the script is the same, but faster: </p>
<p>my @patterns = map{qr /$_ / i} qw(foo bar baz);<br />
LINE : while (&lt;&gt;)<br />
{<br />
    foreach<br />
        $pattern(@patterns)<br />
        {<br />
            if (/ $pattern /) {<br />
                print;<br />
                next LINE;<br />
            }<br />
        }<br />
}</p>
<p> In some cases, you may be able to make several patterns into a single regular expression. Beware of situations that require backtracking though. </p>
<p>my $regex = join &#8216;|&#8217;, qw(foo bar baz);<br />
LINE : while (&lt;&gt;)<br />
{<br />
    print if /(?: $regex) / i;<br />
}</p>
<p> For more details on regular expression efficiency, see <i>Mastering Regular Expressions</i> by Jeffrey Friedl. He explains how the regular expressions engine works and why some patterns are surprisingly inefficient. Once you understand how perl applies regular expressions, you can tune them for individual situations.</p>
<h3>Why don&#8217;t word-boundary searches with  work for me?</h3>
<p> (contributed by brian d foy) </p>
<p> Ensure that you know what  really does: it&#8217;s the boundary between a word character, \w, and something that isn&#8217;t a word character. That thing that isn&#8217;t a word character might be \W, but it can also be the start or end of the string. </p>
<p> It&#8217;s not (not!) the boundary between whitespace and non-whitespace, and it&#8217;s not the stuff between words we use to create sentences. </p>
<p> In regex speak, a word boundary () is a &#8220;zero width assertion&#8221;, meaning that it doesn&#8217;t represent a character in the string, but a condition at a certain position. </p>
<p> For the regular expression, /Perl/, there has to be a word boundary before the &#8220;P&#8221; and after the &#8220;l&#8221;. As long as something other than a word character precedes the &#8220;P&#8221; and succeeds the &#8220;l&#8221;, the pattern will match. These strings match /Perl/. </p>
<pre>
    &quot;Perl&quot;    # no word char before &quot;P&quot; or after &quot;l&quot;
    &quot;Perl &quot;   # same as previous (space is not a word char)
    &quot;'Perl'&quot;  # the &quot;'&quot; char is not a word char
    &quot;Perl's&quot;  # no word char before &quot;P&quot;, non-word char after &quot;l&quot;
</pre>
<p> These strings do not match /Perl/. </p>
<pre>
    &quot;Perl_&quot;   # &quot;_&quot; is a word char!
    &quot;Perler&quot;  # no word char before &quot;P&quot;, but one after &quot;l&quot;
</pre>
<p> You don&#8217;t have to use  to match words though. You can look for non-word characters surrounded by word characters. These strings match the pattern /&#8217;/. </p>
<pre>
    &quot;don't&quot;   # the &quot;'&quot; char is surrounded by &quot;n&quot; and &quot;t&quot;
    &quot;qep'a'&quot;  # the &quot;'&quot; char is surrounded by &quot;p&quot; and &quot;a&quot;
</pre>
<p> These strings do not match /&#8217;/. </p>
<pre>
    &quot;foo'&quot;    # there is no word char after non-word &quot;'&quot;
</pre>
<p> You can also use the complement of , \B, to specify that there should not be a word boundary. </p>
<p> In the pattern /\Bam\B/, there must be a word character before the &#8220;a&#8221; and after the &#8220;m&#8221;. These patterns match /\Bam\B/: </p>
<pre>
    &quot;llama&quot;   # &quot;am&quot; surrounded by word chars
    &quot;Samuel&quot;  # same
</pre>
<p> These strings do not match /\Bam\B/ </p>
<pre>
    &quot;Sam&quot;      # no word boundary before &quot;a&quot;, but one after &quot;m&quot;
    &quot;I am Sam&quot; # &quot;am&quot; surrounded by non-word chars
</pre>
<h3>Why does using $&amp;, $`, or $&#8217; slow my program down?</h3>
<p> (contributed by Anno Siegel) </p>
<p> Once Perl sees that you need one of these variables anywhere in the program, it provides them on each and every pattern match. That means that on every pattern match the entire string will be copied, part of it to $`, part to $&amp;, and part to $&#8217;. Thus the penalty is most severe with long strings and patterns that match often. Avoid $&amp;, $&#8217;, and $` if you can, but if you can&#8217;t, once you&#8217;ve used them at all, use them at will because you&#8217;ve already paid the price. Remember that some algorithms really appreciate them. As of the 5.005 release, the $&amp; variable is no longer &#8220;expensive&#8221; the way the other two are. </p>
<p> Since Perl 5.6.1 the special variables @- and @+ can functionally replace $`, $&amp; and $&#8217;. These arrays contain pointers to the beginning and end of each match (see perlvar for the full story), so they give you essentially the same information, but without the risk of excessive string copying. </p>
<p> Perl 5.10 added three specials, <tt>&quot;${^MATCH}&quot;</tt>, <tt>&quot;${^PREMATCH}&quot;</tt>, and <tt>&quot;${^POSTMATCH}&quot;</tt> to do the same job but without the global performance penalty. Perl 5.10 only sets these variables if you compile or execute the regular expression with the <tt>&quot;/p&quot;</tt> modifier.</p>
<h3>What good is \G in a regular expression?</h3>
<p> You use the <tt>&quot;\G&quot;</tt> anchor to start the next match on the same string where the last match left off. The regular expression engine cannot skip over any characters to find the next match with this anchor, so <tt>&quot;\G&quot;</tt> is similar to the beginning of string anchor, <tt>&quot;^&quot;</tt>. The <tt>&quot;\G&quot;</tt> anchor is typically used with the <tt>&quot;g&quot;</tt> modifier. It uses the value of <tt>&quot;pos()&quot;</tt> as the position to start the next match. As the match operator makes successive matches, it updates <tt>&quot;pos()&quot;</tt> with the position of the next character past the last match (or the first character of the next match, depending on how you like to look at it). Each string has its own <tt>&quot;pos()&quot;</tt> value. </p>
<p> Suppose you want to match all of consecutive pairs of digits in a string like &#8220;1122a44&#8221; and stop matching when you encounter non-digits. You want to match <tt>11</tt> and <tt>22</tt> but the letter <tt>&quot;a&quot;</tt> shows up between <tt>22</tt> and <tt>44</tt> and you want to stop at <tt>&quot;a&quot;</tt>. Simply matching pairs of digits skips over the <tt>&quot;a&quot;</tt> and still matches <tt>44</tt>. </p>
<pre>
    $_ = &quot;1122a44&quot;;
    my @pairs = m/(\d\d)/g;   # qw( 11 22 44 )
</pre>
<p> If you use the <tt>&quot;\G&quot;</tt> anchor, you force the match after <tt>22</tt> to start with the <tt>&quot;a&quot;</tt>. The regular expression cannot match there since it does not find a digit, so the next match fails and the match operator returns the pairs it already found. </p>
<pre>
    $_ = &quot;1122a44&quot;;
    my @pairs = m/\G(\d\d)/g; # qw( 11 22 )
</pre>
<p> You can also use the <tt>&quot;\G&quot;</tt> anchor in scalar context. You still need the <tt>&quot;g&quot;</tt> modifier. </p>
<p>$_ = &#8220;1122a44&#8221;;<br />
while (m /\G(\d\d) / g) {<br />
    print &#8220;Found $1
&#8221;;<br />
}</p>
<p> After the match fails at the letter <tt>&quot;a&quot;</tt>, perl resets <tt>&quot;pos()&quot;</tt> and the next match on the same string starts at the beginning. </p>
<p>$_ = &#8220;1122a44&#8221;;<br />
while (m /\G(\d\d) / g) {<br />
    print &#8220;Found $1
&#8221;;<br />
}<br />
print &#8220;Found $1 after while&#8221; if m / (\d\d) / g;<br />
#finds &#8220;11&#8221;</p>
<p> You can disable <tt>&quot;pos()&quot;</tt> resets on fail with the <tt>&quot;c&quot;</tt> modifier, documented in perlop and perlreref. Subsequent matches start where the last successful match ended (the value of <tt>&quot;pos()&quot;</tt>) even if a match on the same string has failed in the meantime. In this case, the match after the <tt>&quot;while()&quot;</tt> loop starts at the <tt>&quot;a&quot;</tt> (where the last match stopped), and since it does not use any anchor it can skip over the <tt>&quot;a&quot;</tt> to find <tt>44</tt>. </p>
<p>$_ = &#8220;1122a44&#8221;;<br />
while (m /\G(\d\d) / gc) {<br />
    print &#8220;Found $1
&#8221;;<br />
}<br />
print &#8220;Found $1 after while&#8221; if m / (\d\d) / g;<br />
#finds &#8220;44&#8221;</p>
<p> Typically you use the <tt>&quot;\G&quot;</tt> anchor with the <tt>&quot;c&quot;</tt> modifier when you want to try a different match if one fails, such as in a tokenizer. Jeffrey Friedl offers this example which works in 5.004 or later. </p>
<p>while (&lt;&gt;) {<br />
    chomp;<br />
PARSER : {<br />
    m / \G( \d +) / gcx &amp;&amp;do<br />
    {<br />
        print &#8220;number: $1
&#8221;;<br />
        redo;<br />
    };<br />
    m / \G( \w +) / gcx &amp;&amp;do<br />
    {<br />
        print &#8220;word:   $1
&#8221;;<br />
        redo;<br />
    };<br />
    m / \G( \s +) / gcx &amp;&amp;do<br />
    {<br />
        print &#8220;space:  $1
&#8221;;<br />
        redo;<br />
    };<br />
    m / \G([^\w\d] +) / gcx &amp;&amp;do<br />
    {<br />
        print &#8220;other:  $1
&#8221;;<br />
        redo;<br />
    };<br />
}<br />
}</p>
<p> For each line, the <tt>&quot;PARSER&quot;</tt> loop first tries to match a series of digits followed by a word boundary. This match has to start at the place the last match left off (or the beginning of the string on the first match). Since <tt>&quot;m/ \G( \d+ )/gcx&quot;</tt> uses the <tt>&quot;c&quot;</tt> modifier, if the string does not match that regular expression, perl does not reset <code>pos()</code> and the next match starts at the same position to try a different pattern.</p>
<h3>Are Perl regexes DFAs or NFAs? Are they <font SIZE="-1">POSIX</font> compliant?</h3>
<p> While it&#8217;s true that Perl&#8217;s regular expressions resemble the DFAs (deterministic finite automata) of the <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) program, they are in fact implemented as NFAs (non-deterministic finite automata) to allow backtracking and backreferencing. And they aren&#8217;t POSIX-style either, because those guarantee worst-case behavior for all cases. (It seems that some people prefer guarantees of consistency, even when what&#8217;s guaranteed is slowness.) See the book &#8220;Mastering Regular Expressions&#8221; (from O&#8217;Reilly) by Jeffrey Friedl for all the details you could ever hope to know on these matters (a full citation appears in perlfaq2).</p>
<h3>What&#8217;s wrong with using grep in a void context?</h3>
<p> The problem is that grep builds a return list, regardless of the context. This means you&#8217;re making Perl go to the trouble of building a list that you then just throw away. If the list is large, you waste both time and space. If your intent is to iterate over the list, then use a for loop for this purpose. </p>
<p> In perls older than 5.8.1, map suffers from this problem as well. But since 5.8.1, this has been fixed, and map is context aware &#8211; in void context, no lists are constructed.</p>
<h3>How can I match strings with multibyte characters?</h3>
<p> Starting from Perl 5.6 Perl has had some level of multibyte character support. Perl 5.8 or later is recommended. Supported multibyte character repertoires include Unicode, and legacy encodings through the Encode module. See perluniintro, perlunicode, and Encode. </p>
<p> If you are stuck with older Perls, you can do Unicode with the Unicode::String module, and character conversions using the Unicode::Map8 and Unicode::Map modules. If you are using Japanese encodings, you might try using the jperl 5.005_03. </p>
<p> Finally, the following set of approaches was offered by Jeffrey Friedl, whose article in issue #5 of The Perl Journal talks about this very matter. </p>
<p> Let&#8217;s suppose you have some weird Martian encoding where pairs of <font SIZE="-1">ASCII</font> uppercase letters encode single Martian letters (i.e. the two bytes &#8220;<font SIZE="-1">CV&#8221;</font> make a single Martian letter, as do the two bytes &#8220;<font SIZE="-1">SG&#8221;, &#8220;VS&#8221;, &#8220;XX&#8221;,</font> etc.). Other bytes represent single characters, just like <font SIZE="-1">ASCII.</font> </p>
<p> So, the string of Martian &#8220;I am <font SIZE="-1">CVSGXX</font>!&#8221; uses 12 bytes to encode the nine characters &#8216;I&#8217;, &#8216; &#8216;, &#8216;a&#8217;, &#8216;m&#8217;, &#8216; &#8216;, &#8216;<font SIZE="-1">CV</font>&#8216;, &#8216;<font SIZE="-1">SG</font>&#8216;, &#8216;<font SIZE="-1">XX</font>&#8216;, &#8216;!&#8217;. </p>
<p> Now, say you want to search for the single character <tt>&quot;/GX/&quot;</tt>. Perl doesn&#8217;t know about Martian, so it&#8217;ll find the two bytes &#8220;<font SIZE="-1">GX&#8221;</font> in the &#8220;I am <font SIZE="-1">CVSGXX</font>!&#8221; string, even though that character isn&#8217;t there: it just looks like it is because &#8220;<font SIZE="-1">SG&#8221;</font> is next to &#8220;<font SIZE="-1">XX&#8221;,</font> but there&#8217;s no real &#8220;<font SIZE="-1">GX&#8221;.</font> This is a big problem. </p>
<p> Here are a few ways, all painful, to deal with it: </p>
<p>#Make sure adjacent &#8220;martian&#8221; bytes are no longer adjacent.<br />
$martian = ~s / ([A &#8211; Z][A &#8211; Z]) / $1 / g;<br />
print &#8220;found GX!
&#8221; if $martian = ~ / GX / ;</p>
<p> Or like this: </p>
<p>my @chars = $martian = ~m / ([A &#8211; Z][A &#8211; Z] | [^A &#8211; Z]) / g;<br />
#above is conceptually similar to : my @chars = $text = ~m / (.) / g;<br />
#<br />
foreach<br />
    my $char(@chars)<br />
    {<br />
        print &#8220;found GX!
&#8221;, last if $char eq &#8216;GX&#8217;;<br />
    }</p>
<p> Or like this: </p>
<p>while ($martian = ~m /\G([A &#8211; Z][A &#8211; Z] |.) / gs) {<br />
# \G probably unneeded if ($1 eq &#8216;GX&#8217;)<br />
    {<br />
        print &#8220;found GX!
&#8221;;<br />
        last;<br />
    }<br />
}</p>
<p> Here&#8217;s another, slightly less painful, way to do it from Benjamin Goldberg, who uses a zero-width negative look-behind assertion. </p>
<p>    print &#8220;found GX!
&#8221; if    $martian =~ m/<br />
        (?&lt;![A-Z])<br />
        (?:[A-Z][A-Z])*?<br />
        GX<br />
        /x;</p>
<p> This succeeds if the &#8220;martian&#8221; character <font SIZE="-1">GX</font> is in the string, and fails otherwise. If you don&#8217;t like using (?&lt;!), a zero-width negative look-behind assertion, you can replace (?&lt;![A-Z]) with (?:^|[^A-Z]). </p>
<p> It does have the drawback of putting the wrong thing in $-[0] and $+[0], but this usually can be worked around.</p>
<h3>How do I match a regular expression that&#8217;s in a variable?</h3>
<p> (contributed by brian d foy) </p>
<p> We don&#8217;t have to hard-code patterns into the match operator (or anything else that works with regular expressions). We can put the pattern in a variable for later use. </p>
<p> The match operator is a double quote context, so you can interpolate your variable just like a double quoted string. In this case, you read the regular expression as user input and store it in <tt>$regex</tt>. Once you have the pattern in <tt>$regex</tt>, you use that variable in the match operator. </p>
<p>chomp(my $regex = &lt;STDIN&gt;);<br />
if ($string = ~m / $regex /) {<br />
    &#8230;<br />
}</p>
<p> Any regular expression special characters in <tt>$regex</tt> are still special, and the pattern still has to be valid or Perl will complain. For instance, in this pattern there is an unpaired parenthesis. </p>
<pre>
    my $regex = &quot;Unmatched ( paren&quot;;
    &quot;Two parens to bind them all&quot; =~ m/$regex/;
</pre>
<p> When Perl compiles the regular expression, it treats the parenthesis as the start of a memory match. When it doesn&#8217;t find the closing parenthesis, it complains: </p>
<pre>
    Unmatched ( in regex; marked by &lt;-- HERE in m/Unmatched ( &lt;-- HERE  paren/ at script line 3.
</pre>
<p> You can get around this in several ways depending on our situation. First, if you don&#8217;t want any of the characters in the string to be special, you can escape them with <tt>&quot;quotemeta&quot;</tt> before you use the string. </p>
<p>chomp(my $regex = &lt;STDIN&gt;);<br />
$regex = quotemeta($regex);<br />
if ($string = ~m / $regex /) {<br />
    &#8230;<br />
}</p>
<p> You can also do this directly in the match operator using the <tt>&quot;\Q&quot;</tt> and <tt>&quot;\E&quot;</tt> sequences. The <tt>&quot;\Q&quot;</tt> tells Perl where to start escaping special characters, and the <tt>&quot;\E&quot;</tt> tells it where to stop (see perlop for more details). </p>
<p>chomp(my $regex = &lt;STDIN&gt;);<br />
if ($string = ~m /\Q$regex\E /) {<br />
    &#8230;<br />
}</p>
<p> Alternately, you can use <tt>&quot;qr//&quot;</tt>, the regular expression quote operator (see perlop for more details). It quotes and perhaps compiles the pattern, and you can apply regular expression flags to the pattern. </p>
<p>chomp(my $input = &lt;STDIN&gt;);<br />
my $regex = qr / $input / is;<br />
$string = ~m / $regex / #same as m / $input / is;</p>
<p> You might also want to trap any errors by wrapping an <tt>&quot;eval&quot;</tt> block around the whole thing. </p>
<p>chomp(my $input = &lt;STDIN&gt;);<br />
eval<br />
{<br />
    if ($string = ~m /\Q$input\E /) {<br />
        &#8230;<br />
    }<br />
};<br />
warn $ @ if $ @;</p>
<p> Or&#8230; </p>
<pre><code>
my $regex = eval{qr / $input / is};
if (defined $regex) {
    $string = ~m / $regex / ;
} else {
    warn $ @;
}
</code></pre>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in this file are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
<h2>Index</h2>
<dt><a href="#lbBC">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>
