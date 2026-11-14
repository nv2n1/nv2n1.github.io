---
title: "perlsyn(1)"
name: "perlsyn"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsyn/"
description: "perlsyn – Perl syntax"
---

<h2 class="name">NAME</h2>
<p> perlsyn &#8211; Perl syntax </p>
<h2>DESCRIPTION</h2>
<p> A Perl program consists of a sequence of declarations and statements which run from the top to the bottom. Loops, subroutines, and other control structures allow you to jump around within the code. </p>
<p> Perl is a <code>free-form</code> language: you can format and indent it however you like. Whitespace serves mostly to separate tokens, unlike languages like Python where it is an important part of the syntax, or Fortran where it is immaterial. </p>
<p> Many of Perl&#8217;s syntactic elements are <code>optional</code>. Rather than requiring you to put parentheses around every function call and declare every variable, you can often leave such explicit elements off and Perl will figure out what you meant. This is known as <code>Do What I Mean</code>, abbreviated <font SIZE="-1"><code>DWIM</code></font>. It allows programmers to be <code>lazy</code> and to code in a style with which they are comfortable. </p>
<p> Perl <code>borrows syntax</code> and concepts from many languages: awk, sed, C, Bourne Shell, Smalltalk, Lisp and even English. Other languages have borrowed syntax from Perl, particularly its regular expression extensions. So if you have programmed in another language you will see familiar pieces in Perl. They often work the same, but see perltrap for information about how they differ.</p>
<h3>Declarations</h3>
<p> The only things you need to declare in Perl are report formats and subroutines (and sometimes not even subroutines). A scalar variable holds the undefined value (<tt>&quot;undef&quot;</tt>) until it has been assigned a defined value, which is anything other than <tt>&quot;undef&quot;</tt>. When used as a number, <tt>&quot;undef&quot;</tt> is treated as <tt>0</tt>; when used as a string, it is treated as the empty string, <tt>&quot;&quot;</tt>; and when used as a reference that isn&#8217;t being assigned to, it is treated as an error. If you enable warnings, you&#8217;ll be notified of an uninitialized value whenever you treat <tt>&quot;undef&quot;</tt> as a string or a number. Well, usually. Boolean contexts, such as: </p>
<pre>
    if ($a) {}
</pre>
<p> are exempt from warnings (because they care about truth rather than definedness). Operators such as <tt>&quot;++&quot;</tt>, <tt>&quot;--&quot;</tt>, <tt>&quot;+=&quot;</tt>, <tt>&quot;-=&quot;</tt>, and <tt>&quot;.=&quot;</tt>, that operate on undefined variables such as: </p>
<pre>
    undef $a;
    $a++;
</pre>
<p> are also always exempt from such warnings. </p>
<p> A declaration can be put anywhere a statement can, but has no effect on the execution of the primary sequence of statements: declarations all take effect at compile time. All declarations are typically put at the beginning or the end of the script. However, if you&#8217;re using lexically-scoped private variables created with <tt>&quot;my()&quot;</tt>, <tt>&quot;state()&quot;</tt>, or <tt>&quot;our()&quot;</tt>, you&#8217;ll have to make sure your format or subroutine definition is within the same block scope as the my if you expect to be able to access those private variables. </p>
<p> Declaring a subroutine allows a subroutine name to be used as if it were a list operator from that point forward in the program. You can declare a subroutine without defining it by saying <tt>&quot;sub name&quot;</tt>, thus: </p>
<pre>
    sub myname;
    $me = myname $0             or die &quot;can't get myname&quot;;
</pre>
<p> A bare declaration like that declares the function to be a list operator, not a unary operator, so you have to be careful to use parentheses (or <tt>&quot;or&quot;</tt> instead of <tt>&quot;||&quot;</tt>.) The <tt>&quot;||&quot;</tt> operator binds too tightly to use after list operators; it becomes part of the last element. You can always use parentheses around the list operators arguments to turn the list operator back into something that behaves more like a function call. Alternatively, you can use the prototype <tt>&quot;($)&quot;</tt> to turn the subroutine into a unary operator: </p>
<pre><code>
sub myname($);
$me = myname $0 || die "can't get myname";
</code></pre>
<p> That now parses as you&#8217;d expect, but you still ought to get in the habit of using parentheses in that situation. For more on prototypes, see perlsub. </p>
<p> Subroutines declarations can also be loaded up with the <tt>&quot;require&quot;</tt> statement or both loaded and imported into your namespace with a <tt>&quot;use&quot;</tt> statement. See perlmod for details on this. </p>
<p> A statement sequence may contain declarations of lexically-scoped variables, but apart from declaring a variable name, the declaration acts like an ordinary statement, and is elaborated within the sequence of statements as if it were an ordinary statement. That means it actually has both compile-time and run-time effects.</p>
<h3>Comments</h3>
<p> Text from a <tt>&quot;#&quot;</tt> character until the end of the line is a comment, and is ignored. Exceptions include <tt>&quot;#&quot;</tt> inside a string or regular expression.</p>
<h3>Simple Statements</h3>
<p> The only kind of simple statement is an expression evaluated for its side-effects. Every simple statement must be terminated with a semicolon, unless it is the final statement in a block, in which case the semicolon is optional. But put the semicolon in anyway if the block takes up more than one line, because you may eventually add another line. Note that there are operators like <tt>&quot;eval {}&quot;</tt>, <tt>&quot;sub {}&quot;</tt>, and <tt>&quot;do {}&quot;</tt> that <i>look</i> like compound statements, but aren&#8217;t&#8212;they&#8217;re just TERMs in an expression&#8212;and thus need an explicit termination when used as the last item in a statement.</p>
<h3>Statement Modifiers</h3>
<p> Any simple statement may optionally be followed by a <i></i><font SIZE="-1"><i>SINGLE</i></font><i></i> modifier, just before the terminating semicolon (or block ending). The possible modifiers are: </p>
<pre>
    if EXPR
    unless EXPR
    while EXPR
    until EXPR
    for LIST
    foreach LIST
    when EXPR
</pre>
<p> The <tt>&quot;EXPR&quot;</tt> following the modifier is referred to as the &#8220;condition&#8221;. Its truth or falsehood determines how the modifier will behave. </p>
<p> <tt>&quot;if&quot;</tt> executes the statement once <i>if</i> and only if the condition is true. <tt>&quot;unless&quot;</tt> is the opposite, it executes the statement <i>unless</i> the condition is true (that is, if the condition is false). </p>
<p>print &#8220;Basset hounds got long ears&#8221; if length $ear &gt;= 10;<br />
go_outside() and play() unless $is_raining;</p>
<p> The <tt>&quot;for(each)&quot;</tt> modifier is an iterator: it executes the statement once for each item in the <font SIZE="-1">LIST</font> (with <tt>$_</tt> aliased to each item in turn). </p>
<p>    print &#8220;Hello $_!
&#8221; for qw(world Dolly nurse);</p>
<p> <tt>&quot;while&quot;</tt> repeats the statement <i>while</i> the condition is true. Postfix <tt>&quot;while&quot;</tt> has the same magic treatment of some kinds of condition that prefix <tt>&quot;while&quot;</tt> has. <tt>&quot;until&quot;</tt> does the opposite, it repeats the statement <i>until</i> the condition is true (or while the condition is false): </p>
<p>#Both of these count from 0 to 10.<br />
print $i++ while $i &lt;= 10;<br />
print $j++ until $j &gt; 10;</p>
<p> The <tt>&quot;while&quot;</tt> and <tt>&quot;until&quot;</tt> modifiers have the usual &quot;<tt>&quot;while&quot;</tt> loop&quot; semantics (conditional evaluated first), except when applied to a <tt>&quot;do&quot;</tt>-BLOCK (or to the Perl4 <tt>&quot;do&quot;</tt>-SUBROUTINE statement), in which case the block executes once before the conditional is evaluated. </p>
<p> This is so that you can write loops like: </p>
<p>do {<br />
    $line = &lt;STDIN&gt;;<br />
    &#8230;<br />
}<br />
until !defined($line) || $line eq &#8220;.
&#8221;</p>
<p> See &#8220;do&#8221; in perlfunc. Note also that the loop control statements described later will <i></i><font SIZE="-1"><i>NOT</i></font><i></i> work in this construct, because modifiers don&#8217;t take loop labels. Sorry. You can always put another block inside of it (for <tt>&quot;next&quot;</tt>/<tt>&quot;redo&quot;</tt>) or around it (for <tt>&quot;last&quot;</tt>) to do that sort of thing. </p>
<p> For <tt>&quot;next&quot;</tt> or <tt>&quot;redo&quot;</tt>, just double the braces: </p>
<p>do {<br />
    {<br />
        next if $x == $y;<br />
#do something here<br />
    }<br />
}<br />
until $x++ &gt; $z;</p>
<p> For <tt>&quot;last&quot;</tt>, you have to be more elaborate and put braces around it: </p>
<p>{<br />
    do {<br />
        last if $x == $y * * 2;<br />
#do something here<br />
    } while $x++ &lt;= $z;<br />
}</p>
<p> If you need both <tt>&quot;next&quot;</tt> and <tt>&quot;last&quot;</tt>, you have to do both and also use a loop label: </p>
<p>LOOP:<br />
{<br />
    do {<br />
        {<br />
            next if $x == $y;<br />
            last LOOP if $x == $y * * 2;<br />
#do something here<br />
        }<br />
    }<br />
    until $x++ &gt; $z;<br />
}</p>
<p> <font SIZE="-1"><code>NOTE:</code></font> The behaviour of a <tt>&quot;my&quot;</tt>, <tt>&quot;state&quot;</tt>, or <tt>&quot;our&quot;</tt> modified with a statement modifier conditional or loop construct (for example, <tt>&quot;my $x if ...&quot;</tt>) is <code>undefined</code>. The value of the <tt>&quot;my&quot;</tt> variable may be <tt>&quot;undef&quot;</tt>, any previously assigned value, or possibly anything else. Don&#8217;t rely on it. Future versions of perl might do something different from the version of perl you try it out on. Here be dragons. </p>
<p> The <tt>&quot;when&quot;</tt> modifier is an experimental feature that first appeared in Perl 5.14. To use it, you should include a <tt>&quot;use v5.14&quot;</tt> declaration. (Technically, it requires only the <tt>&quot;switch&quot;</tt> feature, but that aspect of it was not available before 5.14.) Operative only from within a <tt>&quot;foreach&quot;</tt> loop or a <tt>&quot;given&quot;</tt> block, it executes the statement only if the smartmatch <tt>&quot;$_ ~~ </tt>EXPR<tt>&quot;</tt> is true. If the statement executes, it is followed by a <tt>&quot;next&quot;</tt> from inside a <tt>&quot;foreach&quot;</tt> and <tt>&quot;break&quot;</tt> from inside a <tt>&quot;given&quot;</tt>. </p>
<p> Under the current implementation, the <tt>&quot;foreach&quot;</tt> loop can be anywhere within the <tt>&quot;when&quot;</tt> modifier&#8217;s dynamic scope, but must be within the <tt>&quot;given&quot;</tt> block&#8217;s lexical scope. This restriction may be relaxed in a future release. See &#8220;Switch Statements&#8221; below.</p>
<h3>Compound Statements</h3>
<p> In Perl, a sequence of statements that defines a scope is called a block. Sometimes a block is delimited by the file containing it (in the case of a required file, or the program as a whole), and sometimes a block is delimited by the extent of a string (in the case of an eval). </p>
<p> But generally, a block is delimited by curly brackets, also known as braces. We will call this syntactic construct a <font SIZE="-1">BLOCK.</font> Because enclosing braces are also the syntax for hash reference constructor expressions (see perlref), you may occasionally need to disambiguate by placing a <tt>&quot;;&quot;</tt> immediately after an opening brace so that Perl realises the brace is the start of a block. You will more frequently need to disambiguate the other way, by placing a <tt>&quot;+&quot;</tt> immediately before an opening brace to force it to be interpreted as a hash reference constructor expression. It is considered good style to use these disambiguating mechanisms liberally, not only when Perl would otherwise guess incorrectly. </p>
<p> The following compound statements may be used to control flow: </p>
<p>if (EXPR)<br />
    BLOCK<br />
if (EXPR) BLOCK else BLOCK<br />
    if (EXPR) BLOCK elsif (EXPR) BLOCK &#8230;<br />
    if (EXPR) BLOCK elsif (EXPR) BLOCK &#8230; else BLOCK<br />
    unless (EXPR) BLOCK<br />
    unless (EXPR) BLOCK else BLOCK<br />
    unless (EXPR) BLOCK elsif (EXPR) BLOCK &#8230;<br />
    unless (EXPR) BLOCK elsif (EXPR) BLOCK &#8230; else BLOCK<br />
    given (EXPR) BLOCK<br />
    LABEL while (EXPR) BLOCK<br />
    LABEL while (EXPR) BLOCK continue BLOCK<br />
    LABEL until (EXPR) BLOCK<br />
    LABEL until (EXPR) BLOCK continue BLOCK<br />
    LABEL for (EXPR; EXPR; EXPR) BLOCK<br />
    LABEL for VAR (LIST) BLOCK<br />
    LABEL for VAR (LIST) BLOCK continue BLOCK<br />
    LABEL foreach (EXPR; EXPR; EXPR) BLOCK<br />
    LABEL foreach VAR (LIST) BLOCK<br />
    LABEL foreach VAR (LIST) BLOCK continue BLOCK<br />
    LABEL BLOCK<br />
    LABEL BLOCK continue BLOCK<br />
    PHASE BLOCK</p>
<p> The experimental <tt>&quot;given&quot;</tt> statement is <i>not automatically enabled</i>; see &#8220;Switch Statements&#8221; below for how to do so, and the attendant caveats. </p>
<p> Unlike in C and Pascal, in Perl these are all defined in terms of BLOCKs, not statements. This means that the curly brackets are <i>required</i>&#8211;no dangling statements allowed. If you want to write conditionals without curly brackets, there are several other ways to do it. The following all do the same thing: </p>
<p>if (!open(FOO)) {<br />
    die &#8220;Can&#8217;t open $FOO: $!&#8221;<br />
}<br />
die &#8220;Can&#8217;t open $FOO: $!&#8221; unless open(FOO);<br />
open(FOO) || die &#8220;Can&#8217;t open $FOO: $!&#8221;;<br />
open(FOO) ? () : die &#8220;Can&#8217;t open $FOO: $!&#8221;;<br />
#a bit exotic, that last one</p>
<p> The <tt>&quot;if&quot;</tt> statement is straightforward. Because BLOCKs are always bounded by curly brackets, there is never any ambiguity about which <tt>&quot;if&quot;</tt> an <tt>&quot;else&quot;</tt> goes with. If you use <tt>&quot;unless&quot;</tt> in place of <tt>&quot;if&quot;</tt>, the sense of the test is reversed. Like <tt>&quot;if&quot;</tt>, <tt>&quot;unless&quot;</tt> can be followed by <tt>&quot;else&quot;</tt>. <tt>&quot;unless&quot;</tt> can even be followed by one or more <tt>&quot;elsif&quot;</tt> statements, though you may want to think twice before using that particular language construct, as everyone reading your code will have to think at least twice before they can understand what&#8217;s going on. </p>
<p> The <tt>&quot;while&quot;</tt> statement executes the block as long as the expression is true. The <tt>&quot;until&quot;</tt> statement executes the block as long as the expression is false. The <font SIZE="-1">LABEL</font> is optional, and if present, consists of an identifier followed by a colon. The <font SIZE="-1">LABEL</font> identifies the loop for the loop control statements <tt>&quot;next&quot;</tt>, <tt>&quot;last&quot;</tt>, and <tt>&quot;redo&quot;</tt>. If the <font SIZE="-1">LABEL</font> is omitted, the loop control statement refers to the innermost enclosing loop. This may include dynamically looking back your call-stack at run time to find the <font SIZE="-1">LABEL.</font> Such desperate behavior triggers a warning if you use the <tt>&quot;use warnings&quot;</tt> pragma or the <code>-w</code> flag. </p>
<p> If the condition expression of a <tt>&quot;while&quot;</tt> statement is based on any of a group of iterative expression types then it gets some magic treatment. The affected iterative expression types are <tt>&quot;readline&quot;</tt>, the <tt>&quot;&lt;FILEHANDLE&gt;&quot;</tt> input operator, <tt>&quot;readdir&quot;</tt>, <tt>&quot;glob&quot;</tt>, the <tt>&quot;&lt;PATTERN&gt;&quot;</tt> globbing operator, and <tt>&quot;each&quot;</tt>. If the condition expression is one of these expression types, then the value yielded by the iterative operator will be implicitly assigned to <tt>$_</tt>. If the condition expression is one of these expression types or an explicit assignment of one of them to a scalar, then the condition actually tests for definedness of the expression&#8217;s value, not for its regular truth value. </p>
<p> If there is a <tt>&quot;continue&quot;</tt> <font SIZE="-1">BLOCK,</font> it is always executed just before the conditional is about to be evaluated again. Thus it can be used to increment a loop variable, even when the loop has been continued via the <tt>&quot;next&quot;</tt> statement. </p>
<p> When a block is preceded by a compilation phase keyword such as <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;END&quot;</tt>, <tt>&quot;INIT&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, or <tt>&quot;UNITCHECK&quot;</tt>, then the block will run only during the corresponding phase of execution. See perlmod for more details. </p>
<p> Extension modules can also hook into the Perl parser to define new kinds of compound statements. These are introduced by a keyword which the extension recognizes, and the syntax following the keyword is defined entirely by the extension. If you are an implementor, see &#8220;PL_keyword_plugin&#8221; in perlapi for the mechanism. If you are using such a module, see the module&#8217;s documentation for details of the syntax that it defines.</p>
<h3>Loop Control</h3>
<p> The <tt>&quot;next&quot;</tt> command starts the next iteration of the loop: </p>
<p>LINE : while (&lt;STDIN&gt;)<br />
{<br />
    next LINE if / ^# / ;<br />
#discard comments&#8230;<br />
}</p>
<p> The <tt>&quot;last&quot;</tt> command immediately exits the loop in question. The <tt>&quot;continue&quot;</tt> block, if any, is not executed: </p>
<p>LINE : while (&lt;STDIN&gt;)<br />
{<br />
    last LINE if / ^$ / ;<br />
#exit when done with header&#8230;<br />
}</p>
<p> The <tt>&quot;redo&quot;</tt> command restarts the loop block without evaluating the conditional again. The <tt>&quot;continue&quot;</tt> block, if any, is <i>not</i> executed. This command is normally used by programs that want to lie to themselves about what was just input. </p>
<p> For example, when processing a file like <i>/etc/termcap</i>. If your input lines might end in backslashes to indicate continuation, you want to skip ahead and get the next record. </p>
<p>while (&lt;&gt;) {<br />
    chomp;<br />
        if (s/\$//) {<br />
            $_ .= &lt;&gt;;<br />
            redo unless eof();<br />
}<br />
#now process $_<br />
}</p>
<p> which is Perl shorthand for the more explicitly written version: </p>
<p>LINE : while (defined($line = &lt;ARGV&gt;))<br />
{<br />
    chomp($line);<br />
        if ($line =~ s/\$//) {<br />
            $line .= &lt;ARGV&gt;;<br />
            redo LINE unless eof(); # not eof(ARGV)!<br />
}<br />
#now process $line<br />
}</p>
<p> Note that if there were a <tt>&quot;continue&quot;</tt> block on the above code, it would get executed only on lines discarded by the regex (since redo skips the continue block). A continue block is often used to reset line counters or <tt>&quot;m?pat?&quot;</tt> one-time matches: </p>
<p>#inspired by : 1, $g / fred / s // WILMA/<br />
while (&lt;&gt;) {<br />
    m ? (fred) ? &amp;&amp;s // WILMA $1 WILMA/;<br />
                     m<br />
        ? (barney)<br />
        ? &amp;&amp;s // BETTY $1 BETTY/;<br />
              m<br />
        ? (homer)<br />
        ? &amp;&amp;s // MARGE $1 MARGE/;<br />
}<br />
continue<br />
{<br />
    print &#8220;$ARGV $.: $_&#8221;;<br />
    close ARGV if eof;<br />
#reset $.reset if eof;<br />
#reset ? pat ?<br />
}</p>
<p> If the word <tt>&quot;while&quot;</tt> is replaced by the word <tt>&quot;until&quot;</tt>, the sense of the test is reversed, but the conditional is still tested before the first iteration. </p>
<p> Loop control statements don&#8217;t work in an <tt>&quot;if&quot;</tt> or <tt>&quot;unless&quot;</tt>, since they aren&#8217;t loops. You can double the braces to make them such, though. </p>
<p>if (/ pattern /) {<br />
    {<br />
        last if / fred / ;<br />
        next if / barney / ;<br />
#same effect as &#8220;last&#8221;,<br />
#but doesn&#8217;t document as well<br />
#do something here<br />
    }<br />
}</p>
<p> This is caused by the fact that a block by itself acts as a loop that executes once, see &#8220;Basic BLOCKs&#8221;. </p>
<p> The form <tt>&quot;while/if BLOCK BLOCK&quot;</tt>, available in Perl 4, is no longer available. Replace any occurrence of <tt>&quot;if BLOCK&quot;</tt> by <tt>&quot;if (do BLOCK)&quot;</tt>.</p>
<h3>For Loops</h3>
<p> Perl&#8217;s C-style <tt>&quot;for&quot;</tt> loop works like the corresponding <tt>&quot;while&quot;</tt> loop; that means that this: </p>
<p>for ($i = 1; $i &lt; 10; $i++) {<br />
    &#8230;<br />
}</p>
<p> is the same as this: </p>
<p>$i = 1;<br />
while ($i &lt; 10) {<br />
    &#8230;<br />
}<br />
continue<br />
{<br />
    $i++;<br />
}</p>
<p> There is one minor difference: if variables are declared with <tt>&quot;my&quot;</tt> in the initialization section of the <tt>&quot;for&quot;</tt>, the lexical scope of those variables is exactly the <tt>&quot;for&quot;</tt> loop (the body of the loop and the control sections). </p>
<p> As a special case, if the test in the <tt>&quot;for&quot;</tt> loop (or the corresponding <tt>&quot;while&quot;</tt> loop) is empty, it is treated as true. That is, both </p>
<p>for (;;) {<br />
    &#8230;<br />
}</p>
<p> and </p>
<pre>
    while () {
        ...
    }
</pre>
<p> are treated as infinite loops. </p>
<p> Besides the normal array index looping, <tt>&quot;for&quot;</tt> can lend itself to many other interesting applications. Here&#8217;s one that avoids the problem you get into if you explicitly test for end-of-file on an interactive file descriptor causing your program to appear to hang. </p>
<p>$on_a_tty = -t STDIN &amp;&amp; -t STDOUT;<br />
sub prompt<br />
{<br />
    print &#8220;yes? &#8221; if $on_a_tty<br />
}<br />
for (prompt();&lt;STDIN&gt;; prompt()) {<br />
#do something<br />
}</p>
<p> The condition expression of a <tt>&quot;for&quot;</tt> loop gets the same magic treatment of <tt>&quot;readline&quot;</tt> et al that the condition expression of a <tt>&quot;while&quot;</tt> loop gets.</p>
<h3>Foreach Loops</h3>
<p> The <tt>&quot;foreach&quot;</tt> loop iterates over a normal list value and sets the scalar variable <font SIZE="-1">VAR</font> to be each element of the list in turn. If the variable is preceded with the keyword <tt>&quot;my&quot;</tt>, then it is lexically scoped, and is therefore visible only within the loop. Otherwise, the variable is implicitly local to the loop and regains its former value upon exiting the loop. If the variable was previously declared with <tt>&quot;my&quot;</tt>, it uses that variable instead of the global one, but it&#8217;s still localized to the loop. This implicit localization occurs <i>only</i> in a <tt>&quot;foreach&quot;</tt> loop. </p>
<p> The <tt>&quot;foreach&quot;</tt> keyword is actually a synonym for the <tt>&quot;for&quot;</tt> keyword, so you can use either. If <font SIZE="-1">VAR</font> is omitted, <tt>$_</tt> is set to each value. </p>
<p> If any element of <font SIZE="-1">LIST</font> is an lvalue, you can modify it by modifying <font SIZE="-1">VAR</font> inside the loop. Conversely, if any element of <font SIZE="-1">LIST</font> is <font SIZE="-1">NOT</font> an lvalue, any attempt to modify that element will fail. In other words, the <tt>&quot;foreach&quot;</tt> loop index variable is an implicit alias for each item in the list that you&#8217;re looping over. </p>
<p> If any part of <font SIZE="-1">LIST</font> is an array, <tt>&quot;foreach&quot;</tt> will get very confused if you add or remove elements within the loop body, for example with <tt>&quot;splice&quot;</tt>. So don&#8217;t do that. </p>
<p> <tt>&quot;foreach&quot;</tt> probably won&#8217;t do what you expect if <font SIZE="-1">VAR</font> is a tied or other special variable. Don&#8217;t do that either. </p>
<p> As of Perl 5.22, there is an experimental variant of this loop that accepts a variable preceded by a backslash for <font SIZE="-1">VAR,</font> in which case the items in the <font SIZE="-1">LIST</font> must be references. The backslashed variable will become an alias to each referenced item in the <font SIZE="-1">LIST,</font> which must be of the correct type. The variable needn&#8217;t be a scalar in this case, and the backslash may be followed by <tt>&quot;my&quot;</tt>. To use this form, you must enable the <tt>&quot;refaliasing&quot;</tt> feature via <tt>&quot;use feature&quot;</tt>. (See feature. See also &#8220;Assigning to References&#8221; in perlref.) </p>
<p> Examples: </p>
<p>for (@ary) {<br />
    s / foo / bar /<br />
}<br />
    for<br />
        my $elem(@elements)<br />
        {<br />
            $elem *= 2;<br />
        }<br />
    for<br />
        $count(reverse(1..10), &#8220;BOOM&#8221;)<br />
        {<br />
            print $count, &#8220;
&#8221;;<br />
            sleep(1);<br />
        }<br />
    for (1..15) {<br />
        print &#8220;Merry Christmas
&#8221;;<br />
    }<br />
    foreach<br />
        $item(split(/<br />
                    : [\
:] * /, $ENV{TERMCAP}))<br />
        {<br />
            print &#8220;Item: $item
&#8221;;<br />
        }<br />
    use feature &#8220;refaliasing&#8221;;<br />
    no warnings &#8220;experimental::refaliasing&#8221;;<br />
    foreach<br />
        \my % hash(@array_of_hash_references)<br />
        {<br />
#do something which each % hash<br />
        }</p>
<p> Here&#8217;s how a C programmer might code up a particular algorithm in Perl: </p>
<p>for (my $i = 0; $i &lt; @ary1; $i++) {<br />
    for (my $j = 0; $j &lt; @ary2; $j++) {<br />
        if ($ary1[$i] &gt; $ary2[$j]) {<br />
            last;<br />
#can&#8217;t go to outer :-(<br />
        }<br />
        $ary1[$i] += $ary2[$j];<br />
    }<br />
#this is where that last takes me<br />
}</p>
<p> Whereas here&#8217;s how a Perl programmer more comfortable with the idiom might do it: </p>
<p>    OUTER: for my $wid (@ary1)<br />
    {<br />
    INNER:   for<br />
            my $jet(@ary2)<br />
            {<br />
                next OUTER if $wid &gt; $jet;<br />
                $wid += $jet;<br />
            }<br />
    }</p>
<p> See how much easier this is? It&#8217;s cleaner, safer, and faster. It&#8217;s cleaner because it&#8217;s less noisy. It&#8217;s safer because if code gets added between the inner and outer loops later on, the new code won&#8217;t be accidentally executed. The <tt>&quot;next&quot;</tt> explicitly iterates the other loop rather than merely terminating the inner one. And it&#8217;s faster because Perl executes a <tt>&quot;foreach&quot;</tt> statement more rapidly than it would the equivalent C-style <tt>&quot;for&quot;</tt> loop. </p>
<p> Perceptive Perl hackers may have noticed that a <tt>&quot;for&quot;</tt> loop has a return value, and that this value can be captured by wrapping the loop in a <tt>&quot;do&quot;</tt> block. The reward for this discovery is this cautionary advice: The return value of a <tt>&quot;for&quot;</tt> loop is unspecified and may change without notice. Do not rely on it.</p>
<h3>Basic BLOCKs</h3>
<p> A <font SIZE="-1">BLOCK</font> by itself (labeled or not) is semantically equivalent to a loop that executes once. Thus you can use any of the loop control statements in it to leave or restart the block. (Note that this is <i></i><font SIZE="-1"><i>NOT</i></font><i></i> true in <tt>&quot;eval{}&quot;</tt>, <tt>&quot;sub{}&quot;</tt>, or contrary to popular belief <tt>&quot;do{}&quot;</tt> blocks, which do <i></i><font SIZE="-1"><i>NOT</i></font><i></i> count as loops.) The <tt>&quot;continue&quot;</tt> block is optional. </p>
<p> The <font SIZE="-1">BLOCK</font> construct can be used to emulate case structures. </p>
<p>SWITCH:<br />
{<br />
    if (/ ^abc /) {<br />
        $abc = 1;<br />
        last SWITCH;<br />
    }<br />
    if (/ ^def /) {<br />
        $def = 1;<br />
        last SWITCH;<br />
    }<br />
    if (/ ^xyz /) {<br />
        $xyz = 1;<br />
        last SWITCH;<br />
    }<br />
    $nothing = 1;<br />
}</p>
<p> You&#8217;ll also find that <tt>&quot;foreach&quot;</tt> loop used to create a topicalizer and a switch: </p>
<p>SWITCH : for ($var)<br />
{<br />
    if (/ ^abc /) {<br />
        $abc = 1;<br />
        last SWITCH;<br />
    }<br />
    if (/ ^def /) {<br />
        $def = 1;<br />
        last SWITCH;<br />
    }<br />
    if (/ ^xyz /) {<br />
        $xyz = 1;<br />
        last SWITCH;<br />
    }<br />
    $nothing = 1;<br />
}</p>
<p> Such constructs are quite frequently used, both because older versions of Perl had no official <tt>&quot;switch&quot;</tt> statement, and also because the new version described immediately below remains experimental and can sometimes be confusing.</p>
<h3>Switch Statements</h3>
<p> Starting from Perl 5.10.1 (well, 5.10.0, but it didn&#8217;t work right), you can say </p>
<pre>
    use feature &quot;switch&quot;;
</pre>
<p> to enable an experimental switch feature. This is loosely based on an old version of a Perl 6 proposal, but it no longer resembles the Perl 6 construct. You also get the switch feature whenever you declare that your code prefers to run under a version of Perl that is 5.10 or later. For example: </p>
<pre>
    use v5.14;
</pre>
<p> Under the &#8220;switch&#8221; feature, Perl gains the experimental keywords <tt>&quot;given&quot;</tt>, <tt>&quot;when&quot;</tt>, <tt>&quot;default&quot;</tt>, <tt>&quot;continue&quot;</tt>, and <tt>&quot;break&quot;</tt>. Starting from Perl 5.16, one can prefix the switch keywords with <tt>&quot;CORE::&quot;</tt> to access the feature without a <tt>&quot;use feature&quot;</tt> statement. The keywords <tt>&quot;given&quot;</tt> and <tt>&quot;when&quot;</tt> are analogous to <tt>&quot;switch&quot;</tt> and <tt>&quot;case&quot;</tt> in other languages &#8212; though <tt>&quot;continue&quot;</tt> is not &#8212; so the code in the previous section could be rewritten as </p>
<p>use v5 .10.1;<br />
for ($var) {<br />
    when(/ ^abc /){$abc = 1} when(/ ^def /){$def = 1} when(/ ^xyz /)<br />
    {<br />
        $xyz = 1<br />
    }<br />
    default<br />
    {<br />
        $nothing = 1<br />
    }<br />
}</p>
<p> The <tt>&quot;foreach&quot;</tt> is the non-experimental way to set a topicalizer. If you wish to use the highly experimental <tt>&quot;given&quot;</tt>, that could be written like this: </p>
<p>use v5 .10.1;<br />
given($var)<br />
{<br />
    when(/ ^abc /){$abc = 1} when(/ ^def /){$def = 1} when(/ ^xyz /)<br />
    {<br />
        $xyz = 1<br />
    }<br />
    default<br />
    {<br />
        $nothing = 1<br />
    }<br />
}</p>
<p> As of 5.14, that can also be written this way: </p>
<p>use v5 .14;<br />
for ($var) {<br />
    $abc = 1 when / ^abc / ;<br />
    $def = 1 when / ^def / ;<br />
    $xyz = 1 when / ^xyz / ;<br />
    default<br />
    {<br />
        $nothing = 1<br />
    }<br />
}</p>
<p> Or if you don&#8217;t care to play it safe, like this: </p>
<p>use v5 .14;<br />
given($var)<br />
{<br />
    $abc = 1 when / ^abc / ;<br />
    $def = 1 when / ^def / ;<br />
    $xyz = 1 when / ^xyz / ;<br />
    default<br />
    {<br />
        $nothing = 1<br />
    }<br />
}</p>
<p> The arguments to <tt>&quot;given&quot;</tt> and <tt>&quot;when&quot;</tt> are in scalar context, and <tt>&quot;given&quot;</tt> assigns the <tt>$_</tt> variable its topic value. </p>
<p> Exactly what the <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> argument to <tt>&quot;when&quot;</tt> does is hard to describe precisely, but in general, it tries to guess what you want done. Sometimes it is interpreted as <tt>&quot;$_ ~~ </tt>EXPR<tt>&quot;</tt>, and sometimes it is not. It also behaves differently when lexically enclosed by a <tt>&quot;given&quot;</tt> block than it does when dynamically enclosed by a <tt>&quot;foreach&quot;</tt> loop. The rules are far too difficult to understand to be described here. See &#8220;Experimental Details on given and when&#8221; later on. </p>
<p> Due to an unfortunate bug in how <tt>&quot;given&quot;</tt> was implemented between Perl 5.10 and 5.16, under those implementations the version of <tt>$_</tt> governed by <tt>&quot;given&quot;</tt> is merely a lexically scoped copy of the original, not a dynamically scoped alias to the original, as it would be if it were a <tt>&quot;foreach&quot;</tt> or under both the original and the current Perl 6 language specification. This bug was fixed in Perl 5.18 (and lexicalized <tt>$_</tt> itself was removed in Perl 5.24). </p>
<p> If your code still needs to run on older versions, stick to <tt>&quot;foreach&quot;</tt> for your topicalizer and you will be less unhappy.</p>
<h3>Goto</h3>
<p> Although not for the faint of heart, Perl does support a <tt>&quot;goto&quot;</tt> statement. There are three forms: <tt>&quot;goto&quot;</tt>-LABEL, <tt>&quot;goto&quot;</tt>-EXPR, and <tt>&quot;goto&quot;</tt>-&amp;NAME. A loop&#8217;s <font SIZE="-1">LABEL</font> is not actually a valid target for a <tt>&quot;goto&quot;</tt>; it&#8217;s just the name of the loop. </p>
<p> The <tt>&quot;goto&quot;</tt>-LABEL form finds the statement labeled with <font SIZE="-1">LABEL</font> and resumes execution there. It may not be used to go into any construct that requires initialization, such as a subroutine or a <tt>&quot;foreach&quot;</tt> loop. It also can&#8217;t be used to go into a construct that is optimized away. It can be used to go almost anywhere else within the dynamic scope, including out of subroutines, but it&#8217;s usually better to use some other construct such as <tt>&quot;last&quot;</tt> or <tt>&quot;die&quot;</tt>. The author of Perl has never felt the need to use this form of <tt>&quot;goto&quot;</tt> (in Perl, that is&#8212;C is another matter). </p>
<p> The <tt>&quot;goto&quot;</tt>-EXPR form expects a label name, whose scope will be resolved dynamically. This allows for computed <tt>&quot;goto&quot;</tt>s per <font SIZE="-1">FORTRAN,</font> but isn&#8217;t necessarily recommended if you&#8217;re optimizing for maintainability: </p>
<pre>
    goto((&quot;FOO&quot;, &quot;BAR&quot;, &quot;GLARCH&quot;)[$i]);
</pre>
<p> The <tt>&quot;goto&quot;</tt>-&amp;NAME form is highly magical, and substitutes a call to the named subroutine for the currently running subroutine. This is used by <tt>&quot;AUTOLOAD()&quot;</tt> subroutines that wish to load another subroutine and then pretend that the other subroutine had been called in the first place (except that any modifications to <tt>@_</tt> in the current subroutine are propagated to the other subroutine.) After the <tt>&quot;goto&quot;</tt>, not even <tt>&quot;caller()&quot;</tt> will be able to tell that this routine was called first. </p>
<p> In almost all cases like this, it&#8217;s usually a far, far better idea to use the structured control flow mechanisms of <tt>&quot;next&quot;</tt>, <tt>&quot;last&quot;</tt>, or <tt>&quot;redo&quot;</tt> instead of resorting to a <tt>&quot;goto&quot;</tt>. For certain applications, the catch and throw pair of <tt>&quot;eval{}&quot;</tt> and <code>die()</code> for exception processing can also be a prudent approach.</p>
<h3>The Ellipsis Statement</h3>
<p> Beginning in Perl 5.12, Perl accepts an ellipsis, &quot;<tt>&quot;...&quot;</tt>&quot;, as a placeholder for code that you haven&#8217;t implemented yet. When Perl 5.12 or later encounters an ellipsis statement, it parses this without error, but if and when you should actually try to execute it, Perl throws an exception with the text <tt>&quot;Unimplemented&quot;</tt>: </p>
<p>use v5 .12;<br />
sub unimplemented{&#8230;} eval{unimplemented()};<br />
if ($ @ = ~ / ^Unimplemented at /) {<br />
    say &#8220;I found an ellipsis!&#8221;;<br />
}</p>
<p> You can only use the elliptical statement to stand in for a complete statement. Syntactically, &quot;<tt>&quot;...;&quot;</tt>&#8220; is a complete statement, but, as with other kinds of semicolon-terminated statement, the semicolon may be omitted if &#8221;<tt>&quot;...&quot;</tt>&quot; appears immediately before a closing brace. These examples show how the ellipsis works: </p>
<p>use v5 .12;<br />
{&#8230;} sub foo{&#8230;}&#8230;;<br />
eval{&#8230;};<br />
sub somemeth<br />
{<br />
    my $self = shift;<br />
    &#8230;;<br />
}<br />
$x = do<br />
{<br />
    my $n;<br />
    &#8230;;<br />
    say &#8220;Hurrah!&#8221;;<br />
    $n;<br />
};</p>
<p> The elliptical statement cannot stand in for an expression that is part of a larger statement. These examples of attempts to use an ellipsis are syntax errors: </p>
<p>use v5 .12;<br />
print&#8230;;<br />
open(my $fh, &#8220;&gt;&#8221;, &#8220;/dev/passwd&#8221;) or &#8230;;<br />
if ($condition &amp;&amp; &#8230;) {<br />
    say &#8220;Howdy&#8221;<br />
};<br />
&#8230; if $a &gt; $b;<br />
say &#8220;Cromulent&#8221; if&#8230;;<br />
$flub = 5 + &#8230;;</p>
<p> There are some cases where Perl can&#8217;t immediately tell the difference between an expression and a statement. For instance, the syntax for a block and an anonymous hash reference constructor look the same unless there&#8217;s something in the braces to give Perl a hint. The ellipsis is a syntax error if Perl doesn&#8217;t guess that the <tt>&quot;{ ... }&quot;</tt> is a block. Inside your block, you can use a <tt>&quot;;&quot;</tt> before the ellipsis to denote that the <tt>&quot;{ ... }&quot;</tt> is a block and not a hash reference constructor. </p>
<p> Note: Some folks colloquially refer to this bit of punctuation as a &#8220;yada-yada&#8221; or &#8220;triple-dot&#8221;, but its true name is actually an ellipsis.</p>
<h3>PODs: Embedded Documentation</h3>
<p> Perl has a mechanism for intermixing documentation with source code. While it&#8217;s expecting the beginning of a new statement, if the compiler encounters a line that begins with an equal sign and a word, like this </p>
<pre>
    =head1 Here There Be Pods!
</pre>
<p> Then that text and all remaining text up through and including a line beginning with <tt>&quot;=cut&quot;</tt> will be ignored. The format of the intervening text is described in perlpod. </p>
<p> This allows you to intermix your source code and your documentation text freely, as in </p>
<pre>
    =item snazzle($)
    The snazzle() function will behave in the most spectacular
    form that you can possibly imagine, not even excepting
    cybernetic pyrotechnics.
    =cut back to the compiler, nuff of this pod stuff!
    sub snazzle($) {
        my $thingie = shift;
        .........
    }
</pre>
<p> Note that pod translators should look at only paragraphs beginning with a pod directive (it makes parsing easier), whereas the compiler actually knows to look for pod escapes even in the middle of a paragraph. This means that the following secret stuff will be ignored by both the compiler and the translators. </p>
<pre>
    $a=3;
    =secret stuff
     warn &quot;Neither POD nor CODE!?&quot;
    =cut back
    print &quot;got $a
&quot;;
</pre>
<p> You probably shouldn&#8217;t rely upon the <tt>&quot;warn()&quot;</tt> being podded out forever. Not all pod translators are well-behaved in this regard, and perhaps the compiler will become pickier. </p>
<p> One may also use pod directives to quickly comment out a section of code.</p>
<h3>Plain Old Comments (Not!)</h3>
<p> Perl can process line directives, much like the C preprocessor. Using this, one can control Perl&#8217;s idea of filenames and line numbers in error or warning messages (especially for strings that are processed with <tt>&quot;eval()&quot;</tt>). The syntax for this mechanism is almost the same as for most C preprocessors: it matches the regular expression </p>
<pre>
    # example: '# line 42 &quot;new_filename.plx&quot;'
    /^\#   \s*
      line \s+ (\d+)   \s*
      (?:\s(&quot;?)([^&quot;]+)\g2)? \s*
     $/x
</pre>
<p> with <tt>$1</tt> being the line number for the next line, and <tt>$3</tt> being the optional filename (specified with or without quotes). Note that no whitespace may precede the <tt>&quot;#&quot;</tt>, unlike modern C preprocessors. </p>
<p> There is a fairly obvious gotcha included with the line directive: Debuggers and profilers will only show the last source line to appear at a particular line number in a given file. Care should be taken not to cause line number collisions in code you&#8217;d like to debug later. </p>
<p> Here are some examples that you should be able to type into your command shell: </p>
<p>% perl<br />
#line 200 &#8220;bzzzt&#8221;<br />
#the &#8216;#&#8217; on the previous line must be the first char on line<br />
        die &#8216;foo&#8217;;<br />
__END__<br />
foo at bzzzt line 201. % perl<br />
#line 200 &#8220;bzzzt&#8221;<br />
                             eval qq[
 #line 2001 &#8220;&#8221;
die &#8216;foo&#8217;];<br />
print $ @;<br />
__END__<br />
foo at &#8211; line 2001. % perl<br />
                          eval qq[
 #line 200 &#8220;foo bar&#8221;
die &#8216;foo&#8217;];<br />
print $ @;<br />
__END__<br />
foo at foo bar line 200. % perl<br />
#line 345 &#8220;goop&#8221;<br />
                               eval &#8220;
#line &#8220;.__LINE__.&#8217; &#8220;&#8216;.__FILE__.&#8221;\&#8221;
die &#8216;foo'&#8221;;<br />
print $ @;<br />
__END__<br />
foo at goop line 345.</p>
<h3>Experimental Details on given and when</h3>
<p> As previously mentioned, the &#8220;switch&#8221; feature is considered highly experimental; it is subject to change with little notice. In particular, <tt>&quot;when&quot;</tt> has tricky behaviours that are expected to change to become less tricky in the future. Do not rely upon its current (mis)implementation. Before Perl 5.18, <tt>&quot;given&quot;</tt> also had tricky behaviours that you should still beware of if your code must run on older versions of Perl. </p>
<p> Here is a longer example of <tt>&quot;given&quot;</tt>: </p>
<p>use feature &#8220;:5.10&#8221;;<br />
given($foo)<br />
{<br />
    when(undef)<br />
    {<br />
        say &#8216;$foo is undefined&#8217;;<br />
    }<br />
    when(&#8220;foo&#8221;)<br />
    {<br />
        say &#8216;$foo is the string &#8220;foo&#8221;&#8216;;<br />
    }<br />
    when([ 1, 3, 5, 7, 9 ])<br />
    {<br />
        say &#8216;$foo is an odd digit&#8217;;<br />
        continue;<br />
#Fall through<br />
    }<br />
    when($_ &lt; 100)<br />
    {<br />
        say &#8216;$foo is numerically less than 100&#8217;;<br />
    }<br />
    when(\&amp; complicated_check)<br />
    {<br />
        say &#8216;a complicated check for $foo is true&#8217;;<br />
    }<br />
    default<br />
    {<br />
            die q(I don&#8217;t know what to do with $foo);<br />
    }<br />
}</p>
<p> Before Perl 5.18, <tt>&quot;given(EXPR)&quot;</tt> assigned the value of <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> to merely a lexically scoped <i></i>copy<i></i> (!) of <tt>$_</tt>, not a dynamically scoped alias the way <tt>&quot;foreach&quot;</tt> does. That made it similar to </p>
<pre>
        do { my $_ = EXPR; ... }
</pre>
<p> except that the block was automatically broken out of by a successful <tt>&quot;when&quot;</tt> or an explicit <tt>&quot;break&quot;</tt>. Because it was only a copy, and because it was only lexically scoped, not dynamically scoped, you could not do the things with it that you are used to in a <tt>&quot;foreach&quot;</tt> loop. In particular, it did not work for arbitrary function calls if those functions might try to access <tt>$_</tt>. Best stick to <tt>&quot;foreach&quot;</tt> for that. </p>
<p> Most of the power comes from the implicit smartmatching that can sometimes apply. Most of the time, <tt>&quot;when(EXPR)&quot;</tt> is treated as an implicit smartmatch of <tt>$_</tt>, that is, <tt>&quot;$_ ~~ EXPR&quot;</tt>. (See &#8220;Smartmatch Operator&#8221; in perlop for more information on smartmatching.) But when <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> is one of the 10 exceptional cases (or things like them) listed below, it is used directly as a boolean.</p>
<dl>
<dt>1.</p>
<dd> A user-defined subroutine call or a method invocation.</p>
<dt>2.</p>
<dd> A regular expression match in the form of <tt>&quot;/REGEX/&quot;</tt>, <tt>&quot;$foo =~ /REGEX/&quot;</tt>, or <tt>&quot;$foo =~ EXPR&quot;</tt>. Also, a negated regular expression match in the form <tt>&quot;!/REGEX/&quot;</tt>, <tt>&quot;$foo !~ /REGEX/&quot;</tt>, or <tt>&quot;$foo !~ EXPR&quot;</tt>.</p>
<dt>3.</p>
<dd> A smart match that uses an explicit <tt>&quot;~~&quot;</tt> operator, such as <tt>&quot;EXPR ~~ EXPR&quot;</tt>. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> You will often have to use <tt>&quot;$c ~~ $_&quot;</tt> because the default case uses <tt>&quot;$_ ~~ $c&quot;</tt> , which is frequently the opposite of what you want.</p>
<dt>4.</p>
<dd> A boolean comparison operator such as <tt>&quot;$_ &lt; 10&quot;</tt> or <tt>&quot;$x eq &quot;abc&quot;&quot;</tt>. The relational operators that this applies to are the six numeric comparisons (<tt>&quot;&lt;&quot;</tt>, <tt>&quot;&gt;&quot;</tt>, <tt>&quot;&lt;=&quot;</tt>, <tt>&quot;&gt;=&quot;</tt>, <tt>&quot;==&quot;</tt>, and <tt>&quot;!=&quot;</tt>), and the six string comparisons (<tt>&quot;lt&quot;</tt>, <tt>&quot;gt&quot;</tt>, <tt>&quot;le&quot;</tt>, <tt>&quot;ge&quot;</tt>, <tt>&quot;eq&quot;</tt>, and <tt>&quot;ne&quot;</tt>).</p>
<dt>5.</p>
<dd> At least the three builtin functions <tt>&quot;defined(...)&quot;</tt>, <tt>&quot;exists(...)&quot;</tt>, and <tt>&quot;eof(...)&quot;</tt>. We might someday add more of these later if we think of them.</p>
<dt>6.</p>
<dd> A negated expression, whether <tt>&quot;!(EXPR)&quot;</tt> or <tt>&quot;not(EXPR)&quot;</tt>, or a logical exclusive-or, <tt>&quot;(EXPR1) xor (EXPR2)&quot;</tt>. The bitwise versions (<tt>&quot;~&quot;</tt> and <tt>&quot;^&quot;</tt>) are not included.</p>
<dt>7.</p>
<dd> A filetest operator, with exactly 4 exceptions: <tt>&quot;-s&quot;</tt>, <tt>&quot;-M&quot;</tt>, <tt>&quot;-A&quot;</tt>, and <tt>&quot;-C&quot;</tt>, as these return numerical values, not boolean ones. The <tt>&quot;-z&quot;</tt> filetest operator is not included in the exception list.</p>
<dt>8.</p>
<dd> The <tt>&quot;..&quot;</tt> and <tt>&quot;...&quot;</tt> flip-flop operators. Note that the <tt>&quot;...&quot;</tt> flip-flop operator is completely different from the <tt>&quot;...&quot;</tt> elliptical statement just described.</dl>
<p> In those 8 cases above, the value of <font SIZE="-1">EXPR</font> is used directly as a boolean, so no smartmatching is done. You may think of <tt>&quot;when&quot;</tt> as a smartsmartmatch. </p>
<p> Furthermore, Perl inspects the operands of logical operators to decide whether to use smartmatching for each one by applying the above test to the operands:</p>
<dl>
<dt>9.</p>
<dd> If <font SIZE="-1">EXPR</font> is <tt>&quot;EXPR1 &amp;&amp; EXPR2&quot;</tt> or <tt>&quot;EXPR1 and EXPR2&quot;</tt>, the test is applied <i>recursively</i> to both <font SIZE="-1">EXPR1</font> and <font SIZE="-1">EXPR2.</font> Only if <i>both</i> operands also pass the test, <i>recursively</i>, will the expression be treated as boolean. Otherwise, smartmatching is used.</p>
<dt>10.</p>
<dd> If <font SIZE="-1">EXPR</font> is <tt>&quot;EXPR1 || EXPR2&quot;</tt>, <tt>&quot;EXPR1 // EXPR2&quot;</tt>, or <tt>&quot;EXPR1 or EXPR2&quot;</tt>, the test is applied <i>recursively</i> to <font SIZE="-1">EXPR1</font> only (which might itself be a higher-precedence <font SIZE="-1">AND</font> operator, for example, and thus subject to the previous rule), not to <font SIZE="-1">EXPR2.</font> If <font SIZE="-1">EXPR1</font> is to use smartmatching, then <font SIZE="-1">EXPR2</font> also does so, no matter what <font SIZE="-1">EXPR2</font> contains. But if <font SIZE="-1">EXPR2</font> does not get to use smartmatching, then the second argument will not be either. This is quite different from the <tt>&quot;&amp;&amp;&quot;</tt> case just described, so be careful.</dl>
<p> These rules are complicated, but the goal is for them to do what you want (even if you don&#8217;t quite understand why they are doing it). For example: </p>
<pre>
    when (/^\d+$/ &amp;&amp; $_ &lt; 75) { ... }
</pre>
<p> will be treated as a boolean match because the rules say both a regex match and an explicit test on <tt>$_</tt> will be treated as boolean. </p>
<p> Also: </p>
<p>when([qw(foo bar)] &amp;&amp; / baz /)<br />
{<br />
    &#8230;<br />
}</p>
<p> will use smartmatching because only <i>one</i> of the operands is a boolean: the other uses smartmatching, and that wins. </p>
<p> Further: </p>
<p>when([qw(foo bar)] || / ^baz /)<br />
{<br />
    &#8230;<br />
}</p>
<p> will use smart matching (only the first operand is considered), whereas </p>
<p>when(/ ^baz / || [qw(foo bar)])<br />
{<br />
    &#8230;<br />
}</p>
<p> will test only the regex, which causes both operands to be treated as boolean. Watch out for this one, then, because an arrayref is always a true value, which makes it effectively redundant. Not a good idea. </p>
<p> Tautologous boolean operators are still going to be optimized away. Don&#8217;t be tempted to write </p>
<pre>
    when (&quot;foo&quot; or &quot;bar&quot;) { ... }
</pre>
<p> This will optimize down to <tt>&quot;foo&quot;</tt>, so <tt>&quot;bar&quot;</tt> will never be considered (even though the rules say to use a smartmatch on <tt>&quot;foo&quot;</tt>). For an alternation like this, an array ref will work, because this will instigate smartmatching: </p>
<p>    when ([qw(foo bar)] {<br />
    &#8230; }</p>
<p> This is somewhat equivalent to the C-style switch statement&#8217;s fallthrough functionality (not to be confused with <i>Perl&#8217;s</i> fallthrough functionality&#8212;see below), wherein the same block is used for several <tt>&quot;case&quot;</tt> statements. </p>
<p> Another useful shortcut is that, if you use a literal array or hash as the argument to <tt>&quot;given&quot;</tt>, it is turned into a reference. So <tt>&quot;given(@foo)&quot;</tt> is the same as <tt>&quot;given(\@foo)&quot;</tt>, for example. </p>
<p> <tt>&quot;default&quot;</tt> behaves exactly like <tt>&quot;when(1 == 1)&quot;</tt>, which is to say that it always matches. </p>
<p> <i>Breaking out</i> </p>
<p> You can use the <tt>&quot;break&quot;</tt> keyword to break out of the enclosing <tt>&quot;given&quot;</tt> block. Every <tt>&quot;when&quot;</tt> block is implicitly ended with a <tt>&quot;break&quot;</tt>. </p>
<p> <i>Fall-through</i> </p>
<p> You can use the <tt>&quot;continue&quot;</tt> keyword to fall through from one case to the next immediate <tt>&quot;when&quot;</tt> or <tt>&quot;default&quot;</tt>: </p>
<p>given($foo)<br />
{<br />
    when(/ x /)<br />
    {<br />
        say &#8216;$foo contains an x&#8217;;<br />
        continue<br />
    }<br />
    when(/ y /)<br />
    {<br />
        say &#8216;$foo contains a y&#8217;<br />
    }<br />
    default<br />
    {<br />
        say &#8216;$foo does not contain a y&#8217;<br />
    }<br />
}</p>
<p> <i>Return value</i> </p>
<p> When a <tt>&quot;given&quot;</tt> statement is also a valid expression (for example, when it&#8217;s the last statement of a block), it evaluates to:</p>
<dl>
<dt>&bull;</p>
<dd> An empty list as soon as an explicit <tt>&quot;break&quot;</tt> is encountered.</p>
<dt>&bull;</p>
<dd> The value of the last evaluated expression of the successful <tt>&quot;when&quot;</tt>/<tt>&quot;default&quot;</tt> clause, if there happens to be one.</p>
<dt>&bull;</p>
<dd> The value of the last evaluated expression of the <tt>&quot;given&quot;</tt> block if no condition is true.</dl>
<p> In both last cases, the last expression is evaluated in the context that was applied to the <tt>&quot;given&quot;</tt> block. </p>
<p> Note that, unlike <tt>&quot;if&quot;</tt> and <tt>&quot;unless&quot;</tt>, failed <tt>&quot;when&quot;</tt> statements always evaluate to an empty list. </p>
<p>my $price = do {<br />
    given($item){<br />
        when([ &#8220;pear&#8221;, &#8220;apple&#8221; ]){1} break when &#8220;vote&#8221;;<br />
#My vote cannot be bought 1e10 when / Mona Lisa / ;<br />
&#8220;unknown&#8221;;<br />
}<br />
}<br />
;</p>
<p> Currently, <tt>&quot;given&quot;</tt> blocks can&#8217;t always be used as proper expressions. This may be addressed in a future version of Perl. </p>
<p> <i>Switching in a loop</i> </p>
<p> Instead of using <tt>&quot;given()&quot;</tt>, you can use a <tt>&quot;foreach()&quot;</tt> loop. For example, here&#8217;s one way to count how many times a particular string occurs in an array: </p>
<p>use v5 .10.1;<br />
my $count = 0;<br />
for (@array) {<br />
    when(&#8220;foo&#8221;)<br />
    {<br />
        ++$count<br />
    }<br />
}<br />
print &#8220;\@array contains $count copies of &#8216;foo&#8217;
&#8221;;</p>
<p> Or in a more recent version: </p>
<p>use v5 .14;<br />
my $count = 0;<br />
for (@array) {<br />
    ++$count when &#8220;foo&#8221;;<br />
}<br />
print &#8220;\@array contains $count copies of &#8216;foo&#8217;
&#8221;;</p>
<p> At the end of all <tt>&quot;when&quot;</tt> blocks, there is an implicit <tt>&quot;next&quot;</tt>. You can override that with an explicit <tt>&quot;last&quot;</tt> if you&#8217;re interested in only the first match alone. </p>
<p> This doesn&#8217;t work if you explicitly specify a loop variable, as in <tt>&quot;for $item (@array)&quot;</tt>. You have to use the default variable <tt>$_</tt>. </p>
<p> <i>Differences from Perl 6</i> </p>
<p> The Perl 5 smartmatch and <tt>&quot;given&quot;</tt>/<tt>&quot;when&quot;</tt> constructs are not compatible with their Perl 6 analogues. The most visible difference and least important difference is that, in Perl 5, parentheses are required around the argument to <tt>&quot;given()&quot;</tt> and <tt>&quot;when()&quot;</tt> (except when this last one is used as a statement modifier). Parentheses in Perl 6 are always optional in a control construct such as <tt>&quot;if()&quot;</tt>, <tt>&quot;while()&quot;</tt>, or <tt>&quot;when()&quot;</tt>; they can&#8217;t be made optional in Perl 5 without a great deal of potential confusion, because Perl 5 would parse the expression </p>
<pre>
    given $foo {
        ...
    }
</pre>
<p> as though the argument to <tt>&quot;given&quot;</tt> were an element of the hash <tt>%foo</tt>, interpreting the braces as hash-element syntax. </p>
<p> However, their are many, many other differences. For example, this works in Perl 5: </p>
<p>use v5 .12;<br />
my @primary = (&#8220;red&#8221;, &#8220;blue&#8221;, &#8220;green&#8221;);<br />
if (@primary ~~&#8221;red&#8221;) {<br />
    say &#8220;primary smartmatches red&#8221;;<br />
}<br />
if (&#8220;red&#8221; ~~@primary) {<br />
    say &#8220;red smartmatches primary&#8221;;<br />
}<br />
say &#8220;that&#8217;s all, folks!&#8221;;</p>
<p> But it doesn&#8217;t work at all in Perl 6. Instead, you should use the (parallelizable) <tt>&quot;any&quot;</tt> operator: </p>
<pre><code>
if any (@primary)
    eq "red"
    {
        say "primary smartmatches red";
    }
if
    "red" eq any(@primary)
    {
        say "red smartmatches primary";
    }
</code></pre>
<p> The table of smartmatches in &#8220;Smartmatch Operator&#8221; in perlop is not identical to that proposed by the Perl 6 specification, mainly due to differences between Perl 6&#8217;s and Perl 5&#8217;s data models, but also because the Perl 6 spec has changed since Perl 5 rushed into early adoption. </p>
<p> In Perl 6, <tt>&quot;when()&quot;</tt> will always do an implicit smartmatch with its argument, while in Perl 5 it is convenient (albeit potentially confusing) to suppress this implicit smartmatch in various rather loosely-defined situations, as roughly outlined above. (The difference is largely because Perl 5 does not have, even internally, a boolean type.) </p>
<h2>Index</h2>
