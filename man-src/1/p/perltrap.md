---
title: "perltrap(1)"
name: "perltrap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltrap/"
description: "perltrap – Perl traps for the unwary"
---

<h2 class="name">NAME</h2>
<p> perltrap &#8211; Perl traps for the unwary </p>
<h2>DESCRIPTION</h2>
<p> The biggest trap of all is forgetting to <tt>&quot;use warnings&quot;</tt> or use the <code>-w</code> switch; see warnings and perlrun. The second biggest trap is not making your entire program runnable under <tt>&quot;use strict&quot;</tt>. The third biggest trap is not reading the list of changes in this version of Perl; see perldelta.</p>
<h3>Awk Traps</h3>
<p> Accustomed <code>awk</code> users should take special note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> A Perl program executes only once, not once for each input line. You can do an implicit loop with <tt>&quot;-n&quot;</tt> or <tt>&quot;-p&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The English module, loaded via </p>
<pre>
    use English;
</pre>
<p> allows you to refer to special variables (like <tt>$/</tt>) with names (like <tt>$RS</tt>), as though they were in <code>awk</code>; see perlvar for details.</p>
<dt>&bull;</p>
<dd> Semicolons are required after all simple statements in Perl (except at the end of a block). Newline is not a statement delimiter.</p>
<dt>&bull;</p>
<dd> Curly brackets are required on <tt>&quot;if&quot;</tt>s and <tt>&quot;while&quot;</tt>s.</p>
<dt>&bull;</p>
<dd> Variables begin with &#8220;$&#8221;, &#8220;@&#8221; or &#8220;%&#8221; in Perl.</p>
<dt>&bull;</p>
<dd> Arrays index from 0. Likewise string positions in <code>substr()</code> and <code>index()</code>.</p>
<dt>&bull;</p>
<dd> You have to decide whether your array has numeric or string indices.</p>
<dt>&bull;</p>
<dd> Hash values do not spring into existence upon mere reference.</p>
<dt>&bull;</p>
<dd> You have to decide whether you want to use string or numeric comparisons.</p>
<dt>&bull;</p>
<dd> Reading an input line does not split it for you. You get to split it to an array yourself. And the <code>split()</code> operator has different arguments than <code>awk</code>&#8216;s.</p>
<dt>&bull;</p>
<dd> The current input line is normally in <tt>$_</tt>, not <tt>$0</tt>. It generally does not have the newline stripped. ($0 is the name of the program executed.) See perlvar.</p>
<dt>&bull;</p>
<dd> $&lt;<i>digit</i>&gt; does not refer to fields&#8212;it refers to substrings matched by the last match pattern.</p>
<dt>&bull;</p>
<dd> The <code>print()</code> statement does not add field and record separators unless you set <tt>$,</tt> and <tt>&quot;$\&quot;</tt>. You can set <tt>$OFS</tt> and <tt>$ORS</tt> if you&#8217;re using the English module.</p>
<dt>&bull;</p>
<dd> You must open your files before you print to them.</p>
<dt>&bull;</p>
<dd> The range operator is &#8220;..&#8221;, not comma. The comma operator works as in C.</p>
<dt>&bull;</p>
<dd> The match operator is &#8220;=~&#8221;, not &#8220;~&#8221;. (&#8220;~&#8221; is the one&#8217;s complement operator, as in C.)</p>
<dt>&bull;</p>
<dd> The exponentiation operator is &#8220;**&#8221;, not &#8220;^&#8221;. &#8220;^&#8221; is the <font SIZE="-1">XOR</font> operator, as in C. (You know, one could get the feeling that <code>awk</code> is basically incompatible with C.)</p>
<dt>&bull;</p>
<dd> The concatenation operator is &#8220;.&#8221;, not the null string. (Using the null string would render <tt>&quot;/pat/ /pat/&quot;</tt> unparsable, because the third slash would be interpreted as a division operator&#8212;the tokenizer is in fact slightly context sensitive for operators like &#8220;/&#8221;, &#8220;?&#8221;, and &#8220;&gt;&#8221;. And in fact, &#8220;.&#8221; itself can be the beginning of a number.)</p>
<dt>&bull;</p>
<dd> The <tt>&quot;next&quot;</tt>, <tt>&quot;exit&quot;</tt>, and <tt>&quot;continue&quot;</tt> keywords work differently.</p>
<dt>&bull;</p>
<dd> The following variables work differently: </p>
<pre>
      Awk       Perl
      ARGC      scalar @ARGV (compare with $#ARGV)
      ARGV[0]   $0
      FILENAME  $ARGV
      FNR       $. - something
      FS        (whatever you like)
      NF        $#Fld, or some such
      NR        $.
      OFMT      $#
      OFS       $,
      ORS       $\
      RLENGTH   length($&amp;)
      RS        $/
      RSTART    length($`)
      SUBSEP    $;
</pre>
<dt>&bull;</p>
<dd> You cannot set <tt>$RS</tt> to a pattern, only a string.</p>
<dt>&bull;</p>
<dd> When in doubt, run the <code>awk</code> construct through <code>a2p</code> and see what it gives you.</dl>
<h3>C/C<font SIZE="-2">++</font> Traps</h3>
<p> Cerebral C and C<font SIZE="-2">++</font> programmers should take note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> Curly brackets are required on <tt>&quot;if&quot;</tt>&#8216;s and <tt>&quot;while&quot;</tt>&#8216;s.</p>
<dt>&bull;</p>
<dd> You must use <tt>&quot;elsif&quot;</tt> rather than <tt>&quot;else if&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;break&quot;</tt> and <tt>&quot;continue&quot;</tt> keywords from C become in Perl <tt>&quot;last&quot;</tt> and <tt>&quot;next&quot;</tt>, respectively. Unlike in C, these do <i>not</i> work within a <tt>&quot;do { } while&quot;</tt> construct. See &#8220;Loop Control&#8221; in perlsyn.</p>
<dt>&bull;</p>
<dd> The switch statement is called <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt> and only available in perl 5.10 or newer. See &#8220;Switch Statements&#8221; in perlsyn.</p>
<dt>&bull;</p>
<dd> Variables begin with &#8220;$&#8221;, &#8220;@&#8221; or &#8220;%&#8221; in Perl.</p>
<dt>&bull;</p>
<dd> Comments begin with &#8220;#&#8221;, not &#8220;/*&#8221; or &#8220;//&#8221;. Perl may interpret C/C<font SIZE="-2">++</font> comments as division operators, unterminated regular expressions or the defined-or operator.</p>
<dt>&bull;</p>
<dd> You can&#8217;t take the address of anything, although a similar operator in Perl is the backslash, which creates a reference.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ARGV&quot;</tt> must be capitalized. <tt>$ARGV[0]</tt> is C&#8217;s <tt>&quot;argv[1]&quot;</tt>, and <tt>&quot;argv[0]&quot;</tt> ends up in <tt>$0</tt>.</p>
<dt>&bull;</p>
<dd> System calls such as <code>link()</code>, <code>unlink()</code>, <code>rename()</code>, etc. return nonzero for success, not 0. (<code>system()</code>, however, returns zero for success.)</p>
<dt>&bull;</p>
<dd> Signal handlers deal with signal names, not numbers. Use <tt>&quot;kill -l&quot;</tt> to find their names on your system.</dl>
<h3>JavaScript Traps</h3>
<p> Judicious JavaScript programmers should take note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> In Perl, binary <tt>&quot;+&quot;</tt> is always addition. <tt>&quot;$string1 + $string2&quot;</tt> converts both strings to numbers and then adds them. To concatenate two strings, use the <tt>&quot;.&quot;</tt> operator.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;+&quot;</tt> unary operator doesn&#8217;t do anything in Perl. It exists to avoid syntactic ambiguities.</p>
<dt>&bull;</p>
<dd> Unlike <tt>&quot;for...in&quot;</tt>, Perl&#8217;s <tt>&quot;for&quot;</tt> (also spelled <tt>&quot;foreach&quot;</tt>) does not allow the left-hand side to be an arbitrary expression. It must be a variable: </p>
<pre>
   for my $variable (keys %hash) {
        ...
   }
</pre>
<p> Furthermore, don&#8217;t forget the <tt>&quot;keys&quot;</tt> in there, as <tt>&quot;foreach my $kv (%hash) {}&quot;</tt> iterates over the keys and values, and is generally not useful ($kv would be a key, then a value, and so on).</p>
<dt>&bull;</p>
<dd> To iterate over the indices of an array, use <tt>&quot;foreach my $i (0 .. $#array) {}&quot;</tt>. <tt>&quot;foreach my $v (@array) {}&quot;</tt> iterates over the values.</p>
<dt>&bull;</p>
<dd> Perl requires braces following <tt>&quot;if&quot;</tt>, <tt>&quot;while&quot;</tt>, <tt>&quot;foreach&quot;</tt>, etc.</p>
<dt>&bull;</p>
<dd> In Perl, <tt>&quot;else if&quot;</tt> is spelled <tt>&quot;elsif&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;? :&quot;</tt> has higher precedence than assignment. In JavaScript, one can write: </p>
<pre>
    condition ? do_something() : variable = 3
</pre>
<p> and the variable is only assigned if the condition is false. In Perl, you need parentheses: </p>
<pre>
    $condition ? do_something() : ($variable = 3);
</pre>
<p> Or just use <tt>&quot;if&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Perl requires semicolons to separate statements.</p>
<dt>&bull;</p>
<dd> Variables declared with <tt>&quot;my&quot;</tt> only affect code <i>after</i> the declaration. You cannot write <tt>&quot;$x = 1; my $x;&quot;</tt> and expect the first assignment to affect the same variable. It will instead assign to an <tt>$x</tt> declared previously in an outer scope, or to a global variable. </p>
<p> Note also that the variable is not visible until the following <i>statement</i>. This means that in <tt>&quot;my $x = 1 + $x&quot;</tt> the second <tt>$x</tt> refers to one declared previously.</p>
<dt>&bull;</p>
<dd> <tt>&quot;my&quot;</tt> variables are scoped to the current block, not to the current function. If you write <tt>&quot;{my $x;} $x;&quot;</tt>, the second <tt>$x</tt> does not refer to the one declared inside the block.</p>
<dt>&bull;</p>
<dd> An object&#8217;s members cannot be made accessible as variables. The closest Perl equivalent to <tt>&quot;with(object) { method() }&quot;</tt> is <tt>&quot;for&quot;</tt>, which can alias <tt>$_</tt> to the object: </p>
<pre><code>
for ($object) {
    $_-&gt;method;
}
</code></pre>
<dt>&bull;</p>
<dd> The object or class on which a method is called is passed as one of the method&#8217;s arguments, not as a separate <tt>&quot;this&quot;</tt> value.</dl>
<h3>Sed Traps</h3>
<p> Seasoned <code>sed</code> programmers should take note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> A Perl program executes only once, not once for each input line. You can do an implicit loop with <tt>&quot;-n&quot;</tt> or <tt>&quot;-p&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Backreferences in substitutions use &#8220;$&#8221; rather than &#8220;\&#8221;.</p>
<dt>&bull;</p>
<dd> The pattern matching metacharacters &#8220;(&#8221;, &#8220;)&#8221;, and &#8220;|&#8221; do not have backslashes in front.</p>
<dt>&bull;</p>
<dd> The range operator is <tt>&quot;...&quot;</tt>, rather than comma.</dl>
<h3>Shell Traps</h3>
<p> Sharp shell programmers should take note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> The backtick operator does variable interpolation without regard to the presence of single quotes in the command.</p>
<dt>&bull;</p>
<dd> The backtick operator does no translation of the return value, unlike <code>csh</code>.</p>
<dt>&bull;</p>
<dd> Shells (especially <code>csh</code>) do several levels of substitution on each command line. Perl does substitution in only certain constructs such as double quotes, backticks, angle brackets, and search patterns.</p>
<dt>&bull;</p>
<dd> Shells interpret scripts a little bit at a time. Perl compiles the entire program before executing it (except for <tt>&quot;BEGIN&quot;</tt> blocks, which execute at compile time).</p>
<dt>&bull;</p>
<dd> The arguments are available via <tt>@ARGV</tt>, not <tt>$1</tt>, <tt>$2</tt>, etc.</p>
<dt>&bull;</p>
<dd> The environment is not automatically made available as separate scalar variables.</p>
<dt>&bull;</p>
<dd> The shell&#8217;s <tt>&quot;test&quot;</tt> uses &#8220;=&#8221;, &#8220;!=&#8221;, &#8220;&lt;&#8221; etc for string comparisons and &#8220;-eq&#8221;, &#8220;-ne&#8221;, &#8220;-lt&#8221; etc for numeric comparisons. This is the reverse of Perl, which uses <tt>&quot;eq&quot;</tt>, <tt>&quot;ne&quot;</tt>, <tt>&quot;lt&quot;</tt> for string comparisons, and <tt>&quot;==&quot;</tt>, <tt>&quot;!=&quot;</tt> <tt>&quot;&lt;&quot;</tt> etc for numeric comparisons.</dl>
<h3>Perl Traps</h3>
<p> Practicing Perl Programmers should take note of the following:</p>
<dl>
<dt>&bull;</p>
<dd> Remember that many operations behave differently in a list context than they do in a scalar one. See perldata for details.</p>
<dt>&bull;</p>
<dd> Avoid barewords if you can, especially all lowercase ones. You can&#8217;t tell by just looking at it whether a bareword is a function or a string. By using quotes on strings and parentheses on function calls, you won&#8217;t ever get them confused.</p>
<dt>&bull;</p>
<dd> You cannot discern from mere inspection which builtins are unary operators (like <code>chop()</code> and <code>chdir()</code>) and which are list operators (like <code>print()</code> and <code>unlink()</code>). (Unless prototyped, user-defined subroutines can <code>only</code> be list operators, never unary ones.) See perlop and perlsub.</p>
<dt>&bull;</p>
<dd> People have a hard time remembering that some functions default to <tt>$_</tt>, or <tt>@ARGV</tt>, or whatever, but that others which you might expect to do not.</p>
<dt>&bull;</p>
<dd> The &lt;<font SIZE="-1">FH</font>&gt; construct is not the name of the filehandle, it is a readline operation on that handle. The data read is assigned to <tt>$_</tt> only if the file read is the sole condition in a while loop: </p>
<pre><code>
while (&lt;FH&gt;) {
}
while (defined($_ = &lt;FH&gt;)) {
}
..&lt;FH&gt;;
#data discarded !
</code></pre>
<dt>&bull;</p>
<dd> Remember not to use <tt>&quot;=&quot;</tt> when you need <tt>&quot;=~&quot;</tt>; these two constructs are quite different: </p>
<pre>
    $x =  /foo/;
    $x =~ /foo/;
</pre>
<dt>&bull;</p>
<dd> The <tt>&quot;do {}&quot;</tt> construct isn&#8217;t a real loop that you can use loop control on.</p>
<dt>&bull;</p>
<dd> Use <tt>&quot;my()&quot;</tt> for local variables whenever you can get away with it (but see perlform for where you can&#8217;t). Using <tt>&quot;local()&quot;</tt> actually gives a local value to a global variable, which leaves you open to unforeseen side-effects of dynamic scoping.</p>
<dt>&bull;</p>
<dd> If you localize an exported variable in a module, its exported value will not change. The local name becomes an alias to a new value but the external name is still an alias for the original.</dl>
<p> As always, if any of these are ever officially declared as bugs, they&#8217;ll be fixed and removed. </p>
<h2>Index</h2>
</dl>
