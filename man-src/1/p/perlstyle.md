---
title: "perlstyle(1)"
name: "perlstyle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlstyle/"
description: "perlstyle – Perl style guide"
---

<h2 class="name">NAME</h2>
<p> perlstyle &#8211; Perl style guide </p>
<h2>DESCRIPTION</h2>
<p> Each programmer will, of course, have his or her own preferences in regards to formatting, but there are some general guidelines that will make your programs easier to read, understand, and maintain. </p>
<p> The most important thing is to run your programs under the <code>-w</code> flag at all times. You may turn it off explicitly for particular portions of code via the <tt>&quot;no warnings&quot;</tt> pragma or the <tt>$^W</tt> variable if you must. You should also always run under <tt>&quot;use strict&quot;</tt> or know the reason why not. The <tt>&quot;use sigtrap&quot;</tt> and even <tt>&quot;use diagnostics&quot;</tt> pragmas may also prove useful. </p>
<p> Regarding aesthetics of code lay out, about the only thing Larry cares strongly about is that the closing curly bracket of a multi-line <font SIZE="-1">BLOCK</font> should line up with the keyword that started the construct. Beyond that, he has other preferences that aren&#8217;t so strong:</p>
<dl>
<dt>&bull;</p>
<dd> 4-column indent.</p>
<dt>&bull;</p>
<dd> Opening curly on same line as keyword, if possible, otherwise line up.</p>
<dt>&bull;</p>
<dd> Space before the opening curly of a multi-line <font SIZE="-1">BLOCK.</font></p>
<dt>&bull;</p>
<dd> One-line <font SIZE="-1">BLOCK</font> may be put on one line, including curlies.</p>
<dt>&bull;</p>
<dd> No space before the semicolon.</p>
<dt>&bull;</p>
<dd> Semicolon omitted in &#8220;short&#8221; one-line <font SIZE="-1">BLOCK.</font></p>
<dt>&bull;</p>
<dd> Space around most operators.</p>
<dt>&bull;</p>
<dd> Space around a &#8220;complex&#8221; subscript (inside brackets).</p>
<dt>&bull;</p>
<dd> Blank lines between chunks that do different things.</p>
<dt>&bull;</p>
<dd> Uncuddled elses.</p>
<dt>&bull;</p>
<dd> No space between function name and its opening parenthesis.</p>
<dt>&bull;</p>
<dd> Space after each comma.</p>
<dt>&bull;</p>
<dd> Long lines broken after an operator (except <tt>&quot;and&quot;</tt> and <tt>&quot;or&quot;</tt>).</p>
<dt>&bull;</p>
<dd> Space after last parenthesis matching on current line.</p>
<dt>&bull;</p>
<dd> Line up corresponding items vertically.</p>
<dt>&bull;</p>
<dd> Omit redundant punctuation as long as clarity doesn&#8217;t suffer.</dl>
<p> Larry has his reasons for each of these things, but he doesn&#8217;t claim that everyone else&#8217;s mind works the same as his does. </p>
<p> Here are some other more substantive style issues to think about:</p>
<dl>
<dt>&bull;</p>
<dd> Just because you <i></i><font SIZE="-1"><i>CAN</i></font><i></i> do something a particular way doesn&#8217;t mean that you <i></i><font SIZE="-1"><i>SHOULD</i></font><i></i> do it that way. Perl is designed to give you several ways to do anything, so consider picking the most readable one. For instance </p>
<pre>
    open(FOO,$foo) || die &quot;Can't open $foo: $!&quot;;
</pre>
<p> is better than </p>
<pre>
    die &quot;Can't open $foo: $!&quot; unless open(FOO,$foo);
</pre>
<p> because the second way hides the main point of the statement in a modifier. On the other hand </p>
<pre>
    print &quot;Starting analysis
&quot; if $verbose;
</pre>
<p> is better than </p>
<pre>
    $verbose &amp;&amp; print &quot;Starting analysis
&quot;;
</pre>
<p> because the main point isn&#8217;t whether the user typed <code>-v</code> or not. </p>
<p> Similarly, just because an operator lets you assume default arguments doesn&#8217;t mean that you have to make use of the defaults. The defaults are there for lazy systems programmers writing one-shot programs. If you want your program to be readable, consider supplying the argument. </p>
<p> Along the same lines, just because you <i></i><font SIZE="-1"><i>CAN</i></font><i></i> omit parentheses in many places doesn&#8217;t mean that you ought to: </p>
<pre><code>
return print reverse sort num values % array;
return print(reverse(sort num(values(% array))));
</code></pre>
<p> When in doubt, parenthesize. At the very least it will let some poor schmuck bounce on the % key in <code>vi</code>. </p>
<p> Even if you aren&#8217;t in doubt, consider the mental welfare of the person who has to maintain the code after you, and who will probably put parentheses in the wrong place.</p>
<dt>&bull;</p>
<dd> Don&#8217;t go through silly contortions to exit a loop at the top or the bottom, when Perl provides the <tt>&quot;last&quot;</tt> operator so you can exit in the middle. Just &#8220;outdent&#8221; it a little to make it more visible: </p>
<p>LINE : for (;;)<br />
{<br />
    statements;<br />
    last LINE if $foo;<br />
    next LINE if / ^# / ;<br />
    statements;<br />
}</p>
<dt>&bull;</p>
<dd> Don&#8217;t be afraid to use loop labels&#8212;they&#8217;re there to enhance readability as well as to allow multilevel loop breaks. See the previous example.</p>
<dt>&bull;</p>
<dd> Avoid using <tt>&quot;grep()&quot;</tt> (or <tt>&quot;map()&quot;</tt>) or `backticks` in a void context, that is, when you just throw away their return values. Those functions all have return values, so use them. Otherwise use a <tt>&quot;foreach()&quot;</tt> loop or the <tt>&quot;system()&quot;</tt> function instead.</p>
<dt>&bull;</p>
<dd> For portability, when using features that may not be implemented on every machine, test the construct in an eval to see if it fails. If you know what version or patchlevel a particular feature was implemented, you can test <tt>$]</tt> (<tt>$PERL_VERSION</tt> in <tt>&quot;English&quot;</tt>) to see if it will be there. The <tt>&quot;Config&quot;</tt> module will also let you interrogate values determined by the <code>Configure</code> program when Perl was installed.</p>
<dt>&bull;</p>
<dd> Choose mnemonic identifiers. If you can&#8217;t remember what mnemonic means, you&#8217;ve got a problem.</p>
<dt>&bull;</p>
<dd> While short identifiers like <tt>$gotit</tt> are probably ok, use underscores to separate words in longer identifiers. It is generally easier to read <tt>$var_names_like_this</tt> than <tt>$VarNamesLikeThis</tt>, especially for non-native speakers of English. It&#8217;s also a simple rule that works consistently with <tt>&quot;VAR_NAMES_LIKE_THIS&quot;</tt>. </p>
<p> Package names are sometimes an exception to this rule. Perl informally reserves lowercase module names for &#8220;pragma&#8221; modules like <tt>&quot;integer&quot;</tt> and <tt>&quot;strict&quot;</tt>. Other modules should begin with a capital letter and use mixed case, but probably without underscores due to limitations in primitive file systems&#8217; representations of module names as files that must fit into a few sparse bytes.</p>
<dt>&bull;</p>
<dd> You may find it helpful to use letter case to indicate the scope or nature of a variable. For example: </p>
<pre>
    $ALL_CAPS_HERE   constants only (beware clashes with perl vars!)
    $Some_Caps_Here  package-wide global/static
    $no_caps_here    function scope my() or local() variables
</pre>
<p> Function and method names seem to work best as all lowercase. E.g., <tt>&quot;$obj-&gt;as_string()&quot;</tt>. </p>
<p> You can use a leading underscore to indicate that a variable or function should not be used outside the package that defined it.</p>
<dt>&bull;</p>
<dd> If you have a really hairy regular expression, use the <tt>&quot;/x&quot;</tt> or <tt>&quot;/xx&quot;</tt> modifiers and put in some whitespace to make it look a little less like line noise. Don&#8217;t use slash as a delimiter when your regexp has slashes or backslashes.</p>
<dt>&bull;</p>
<dd> Use the new <tt>&quot;and&quot;</tt> and <tt>&quot;or&quot;</tt> operators to avoid having to parenthesize list operators so much, and to reduce the incidence of punctuation operators like <tt>&quot;&amp;&amp;&quot;</tt> and <tt>&quot;||&quot;</tt>. Call your subroutines as if they were functions or list operators to avoid excessive ampersands and parentheses.</p>
<dt>&bull;</p>
<dd> Use here documents instead of repeated <tt>&quot;print()&quot;</tt> statements.</p>
<dt>&bull;</p>
<dd> Line up corresponding things vertically, especially if it&#8217;d be too long to fit on one line anyway. </p>
<p>$IDX = $ST_MTIME;<br />
$IDX = $ST_ATIME if $opt_u;<br />
$IDX = $ST_CTIME if $opt_c;<br />
$IDX = $ST_SIZE if $opt_s;<br />
mkdir $tmpdir, 0700 or die &#8220;can&#8217;t mkdir $tmpdir: $!&#8221;;<br />
chdir($tmpdir) or die &#8220;can&#8217;t chdir $tmpdir: $!&#8221;;<br />
mkdir &#8216;tmp&#8217;, 0777 or die &#8220;can&#8217;t mkdir $tmpdir/tmp: $!&#8221;;</p>
<dt>&bull;</p>
<dd> Always check the return codes of system calls. Good error messages should go to <tt>&quot;STDERR&quot;</tt>, include which program caused the problem, what the failed system call and arguments were, and (<font SIZE="-1">VERY IMPORTANT</font>) should contain the standard system error message for what went wrong. Here&#8217;s a simple but sufficient example: </p>
<pre>
    opendir(D, $dir)     or die &quot;can't opendir $dir: $!&quot;;
</pre>
<dt>&bull;</p>
<dd> Line up your transliterations when it makes sense: </p>
<pre><code>
tr[abc]
  [xyz];
</code></pre>
<dt>&bull;</p>
<dd> Think about reusability. Why waste brainpower on a one-shot when you might want to do something like it again? Consider generalizing your code. Consider writing a module or object class. Consider making your code run cleanly with <tt>&quot;use strict&quot;</tt> and <tt>&quot;use warnings&quot;</tt> (or <code>-w</code>) in effect. Consider giving away your code. Consider changing your whole world view. Consider&#8230; oh, never mind.</p>
<dt>&bull;</p>
<dd> Try to document your code and use Pod formatting in a consistent way. Here are commonly expected conventions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> use <tt>&quot;C&lt;&gt;&quot;</tt> for function, variable and module names (and more generally anything that can be considered part of code, like filehandles or specific values). Note that function names are considered more readable with parentheses after their name, that is <tt>&quot;function()&quot;</tt>.</p>
<dt>&bull;</p>
<dd> use <tt>&quot;B&lt;&gt;&quot;</tt> for commands names like <code>cat</code> or <code>grep</code>.</p>
<dt>&bull;</p>
<dd> use <tt>&quot;F&lt;&gt;&quot;</tt> or <tt>&quot;C&lt;&gt;&quot;</tt> for file names. <tt>&quot;F&lt;&gt;&quot;</tt> should be the only Pod code for file names, but as most Pod formatters render it as italic, Unix and Windows paths with their slashes and backslashes may be less readable, and better rendered with <tt>&quot;C&lt;&gt;&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> Be consistent.</p>
<dt>&bull;</p>
<dd> Be nice. </p>
</dl>
<h2>Index</h2>
