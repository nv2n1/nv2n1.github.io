---
title: "perlcompile(1)"
name: "perlcompile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlcompile/"
description: "perlcompile – Introduction to the Perl Compiler-Translator"
---

<h2 class="name">NAME</h2>
<p> perlcompile &#8211; Introduction to the Perl Compiler-Translator </p>
<h2>DESCRIPTION</h2>
<p> Perl has always had a compiler: your source is compiled into an internal form (a parse tree) which is then optimized before being run. Since version 5.005, Perl has shipped with a module capable of inspecting the optimized parse tree (<tt>&quot;B&quot;</tt>), and this has been used to write many useful utilities, including a module that lets you turn your Perl into C source code that can be compiled into a native executable. </p>
<p> The <tt>&quot;B&quot;</tt> module provides access to the parse tree, and other modules (&#8220;back ends&#8221;) do things with the tree. Some write it out as semi-human-readable text. Another traverses the parse tree to build a cross-reference of which subroutines, formats, and variables are used where. Another checks your code for dubious constructs. Yet another back end dumps the parse tree back out as Perl source, acting as a source code beautifier or deobfuscator. </p>
<p> Because its original purpose was to be a way to produce C code corresponding to a Perl program, and in turn a native executable, the <tt>&quot;B&quot;</tt> module and its associated back ends are known as &#8220;the compiler&#8221;, even though they don&#8217;t really compile anything. Different parts of the compiler are more accurately a &#8220;translator&#8221;, or an &#8220;inspector&#8221;, but people want Perl to have a &#8220;compiler option&#8221; not an &#8220;inspector gadget&#8221;. What can you do? </p>
<p> This document covers the use of the Perl compiler: which modules it comprises, how to use the most important of the back end modules, what problems there are, and how to work around them.</p>
<h3>Layout</h3>
<p> The compiler back ends are in the <tt>&quot;B::&quot;</tt> hierarchy, and the front-end (the module that you, the user of the compiler, will sometimes interact with) is the O module. </p>
<p> Here are the important back ends to know about, with their status expressed as a number from 0 (outline for later implementation) to 10 (if there&#8217;s a bug in it, we&#8217;re very surprised):</p>
<dl>
<dt>B::Lint</p>
<dd> Complains if it finds dubious constructs in your source code. Status: 6 (it works adequately, but only has a very limited number of areas that it checks).</p>
<dt>B::Deparse</p>
<dd> Recreates the Perl source, making an attempt to format it coherently. Status: 8 (it works nicely, but a few obscure things are missing).</p>
<dt>B::Xref</p>
<dd> Reports on the declaration and use of subroutines and variables. Status: 8 (it works nicely, but still has a few lingering bugs).</dl>
<h2>Using The Back Ends</h2>
<p> The following sections describe how to use the various compiler back ends. They&#8217;re presented roughly in order of maturity, so that the most stable and proven back ends are described first, and the most experimental and incomplete back ends are described last. </p>
<p> The O module automatically enabled the <code>-c</code> flag to Perl, which prevents Perl from executing your code once it has been compiled. This is why all the back ends print: </p>
<pre>
  myperlprogram syntax OK
</pre>
<p> before producing any other output.</p>
<h3>The Cross-Referencing Back End</h3>
<p> The cross-referencing back end (B::Xref) produces a report on your program, breaking down declarations and uses of subroutines and variables (and formats) by file and subroutine. For instance, here&#8217;s part of the report from the <i>pod2man</i> program that comes with Perl: </p>
<pre>
  Subroutine clear_noremap
    Package (lexical)
      $ready_to_print   i1069, 1079
    Package main
      $&amp;                1086
      $.                1086
      $0                1086
      $1                1087
      $2                1085, 1085
      $3                1085, 1085
      $ARGV             1086
      %HTML_Escapes     1085, 1085
</pre>
<p> This shows the variables used in the subroutine <tt>&quot;clear_noremap&quot;</tt>. The variable <tt>$ready_to_print</tt> is a <i>my()</i> (lexical) variable, <code>i</code>ntroduced (first declared with <i>my()</i>) on line 1069, and used on line 1079. The variable <tt>$&amp;</tt> from the main package is used on 1086, and so on. </p>
<p> A line number may be prefixed by a single letter:</p>
<dl>
<dt>i</p>
<dd> Lexical variable introduced (declared with <i>my()</i>) for the first time.</p>
<dt>&amp;</p>
<dd> Subroutine or method call.</p>
<dt>s</p>
<dd> Subroutine defined.</p>
<dt>r</p>
<dd> Format defined.</dl>
<p> The most useful option the cross referencer has is to save the report to a separate file. For instance, to save the report on <i>myperlprogram</i> to the file <i>report</i>: </p>
<pre>
  $ perl -MO=Xref,-oreport myperlprogram
</pre>
<h3>The Decompiling Back End</h3>
<p> The Deparse back end turns your Perl source back into Perl source. It can reformat along the way, making it useful as a deobfuscator. The most basic way to use it is: </p>
<pre>
  $ perl -MO=Deparse myperlprogram
</pre>
<p> You&#8217;ll notice immediately that Perl has no idea of how to paragraph your code. You&#8217;ll have to separate chunks of code from each other with newlines by hand. However, watch what it will do with one-liners: </p>
<pre><code>
$ perl - MO = Deparse - e '$op=shift||die "usage: $0 code[...] ";chomp(@ARGV=&lt;&gt;)unless [at] ARGV; for(@ARGV){$was=$_;eval$op;
              die$ @if$ @;
rename$was, $_ unless$was eq $_
}
' - e syntax OK
        $op = shift @ARGV || die("usage: $0 code [...]");
chomp(@ARGV = &lt;ARGV&gt;) unless @ARGV;
foreach
    $_(@ARGV)
    {
        $was = $_;
        eval $op;
        die $ @ if $ @;
        rename $was, $_ unless $was eq $_;
    }
</code></pre>
<p> The decompiler has several options for the code it generates. For instance, you can set the size of each indent from 4 (as above) to 2 with: </p>
<pre>
  $ perl -MO=Deparse,-si2 myperlprogram
</pre>
<p> The <code>-p</code> option adds parentheses where normally they are omitted: </p>
<pre><code>
$ perl - MO = Deparse - e 'print "Hello, world
"' - e syntax OK print "Hello, world
";
$ perl - MO = Deparse, -p - e 'print "Hello, world
"' - e syntax OK print("Hello, world
");
</code></pre>
<p> See B::Deparse for more information on the formatting options.</p>
<h3>The Lint Back End</h3>
<p> The lint back end (B::Lint) inspects programs for poor style. One programmer&#8217;s bad style is another programmer&#8217;s useful tool, so options let you select what is complained about. </p>
<p> To run the style checker across your source code: </p>
<pre>
  $ perl -MO=Lint myperlprogram
</pre>
<p> To disable context checks and undefined subroutines: </p>
<pre>
  $ perl -MO=Lint,-context,-undefined-subs myperlprogram
</pre>
<p> See B::Lint for information on the options.</p>
<h2>Module List for the Compiler Suite</h2>
<dl>
<dt>B</p>
<dd> This module is the introspective (&#8220;reflective&#8221; in Java terms) module, which allows a Perl program to inspect its innards. The back end modules all use this module to gain access to the compiled parse tree. You, the user of a back end module, will not need to interact with B.</p>
<dt>O</p>
<dd> This module is the front-end to the compiler&#8217;s back ends. Normally called something like this: </p>
<pre>
  $ perl -MO=Deparse myperlprogram
</pre>
<p> This is like saying <tt>&quot;use O 'Deparse'&quot;</tt> in your Perl program.</p>
<dt>B::Concise</p>
<dd> This module prints a concise (but complete) version of the Perl parse tree. Its output is more customizable than the one of B::Terse or B::Debug (and it can emulate them). This module is useful for people who are writing their own back end, or who are learning about the Perl internals. It&#8217;s not useful to the average programmer.</p>
<dt>B::Debug</p>
<dd> This module dumps the Perl parse tree in verbose detail to <font SIZE="-1">STDOUT</font>. It&#8217;s useful for people who are writing their own back end, or who are learning about the Perl internals. It&#8217;s not useful to the average programmer.</p>
<dt>B::Deparse</p>
<dd> This module produces Perl source code from the compiled parse tree. It is useful in debugging and deconstructing other people&#8217;s code, also as a pretty-printer for your own source. See &#8220;The Decompiling Back End&#8221; for details about usage.</p>
<dt>B::Lint</p>
<dd> This module inspects the compiled form of your source code for things which, while some people frown on them, aren&#8217;t necessarily bad enough to justify a warning. For instance, use of an array in scalar context without explicitly saying <tt>&quot;scalar(@array)&quot;</tt> is something that Lint can identify. See &#8220;The Lint Back End&#8221; for details about usage.</p>
<dt>B::Showlex</p>
<dd> This module prints out the <i>my()</i> variables used in a function or a file. To get a list of the <i>my()</i> variables used in the subroutine <i>mysub()</i> defined in the file myperlprogram: </p>
<pre>
  $ perl -MO=Showlex,mysub myperlprogram
</pre>
<p> To get a list of the <i>my()</i> variables used in the file myperlprogram: </p>
<pre>
  $ perl -MO=Showlex myperlprogram
</pre>
<p> [<font SIZE="-1">BROKEN</font>]</p>
<dt>B::Terse</p>
<dd> This module prints the contents of the parse tree, but without as much information as B::Debug. For comparison, <tt>&quot;print &quot;Hello, world.&quot;&quot;</tt> produced 96 lines of output from B::Debug, but only 6 from B::Terse. </p>
<p> This module is useful for people who are writing their own back end, or who are learning about the Perl internals. It&#8217;s not useful to the average programmer.</p>
<dt>B::Xref</p>
<dd> This module prints a report on where the variables, subroutines, and formats are defined and used within a program and the modules it loads. See &#8220;The Cross-Referencing Back End&#8221; for details about usage.</dl>
<h2>KNOWN PROBLEMS</h2>
<p> BEGIN{} blocks are executed while compiling your code. Any external state that is initialized in BEGIN{}, such as opening files, initiating database connections etc., do not behave properly. To work around this, Perl has an INIT{} block that corresponds to code being executed before your program begins running but after your program has finished being compiled. Execution order: BEGIN{}, (possible save of state through compiler back-end), INIT{}, program runs, END{}.</p>
<h2>AUTHOR</h2>
<p> This document was originally written by Nathan Torkington, and is now maintained by the perl5-porters mailing list <i>perl5-porters [at] perl.org</i>. </p>
<h2>Index</h2>
