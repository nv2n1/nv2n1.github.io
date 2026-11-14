---
title: "perlsh(1)"
name: "perlsh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlsh/"
---

<h2 class="name">NAME</h2>
 

 perlsh - one-line perl evaluator with line editing function and <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> variable name completion function
 

<h2>SYNOPSIS</h2>

 <pre>
  perlsh
</pre>

<h2>DESCRIPTION</h2>

 This program reads input a line, and evaluates it by perl interpreter, and prints the result. If the result is a list value then each value of the list is printed line by line. This program can be used as a very strong calculator which has whole perl functions. 

 This is a sample program Term::ReadLine::Gnu module. When you input a line, the line editing function of <font SIZE="-1">GNU</font> Readline Library is available. Perl symbol name completion function is also available. 

 Before invoking, this program reads <i>~/.perlshrc</i> and evaluates the content of the file. 

 When this program is terminated, the content of the history buffer is saved in a file <i>~/.perlsh_history</i>, and it is read at next invoking.

<h2>VARIABLES</h2>

 You can customize the behavior of <tt>&quot;perlsh&quot;</tt> by setting following variables in <i>~/.perlshrc</i>;
<dl>
<dt>$PerlSh::PS1
<dd> The primary prompt string. The following backslash-escaped special characters can be used. 

 <pre>
        \h: host name
        \u: user name
        \w: package name
        \!: history number
</pre> 

 The default value is `<tt>&quot;\w[\!]$ &quot;</tt>'.
<dt>$PerlSh::PS2
<dd> The secondary prompt string. The default value is `<tt>&quot;&gt; &quot;</tt>'.
<dt>$PerlSh::HISTFILE
<dd> The name of the file to which the command history is saved. The default value is <tt>&quot;~/.perlsh_history&quot;</tt>.
<dt>$PerlSh::HISTSIZE
<dd> If not <tt>&quot;undef&quot;</tt>, this is the maximum number of commands to remember in the history. The default value is 256.
<dt>$PerlSh::STRICT
<dd> If true, restrict unsafe constructs. See <tt>&quot;use strict&quot;</tt> in perl man page. The default value is 0;</dl>

<h2>FILES</h2>

<dl>
<dt><i>~/.perlshrc</i>
<dd> This file is eval-ed at initialization. If a subroutine <tt>&quot;afterinit&quot;</tt> is defined in this file, it will be eval-ed after initialization. Here is a sample. 

 <pre><code>
#- * - mode : perl - * -
#decimal to hexa
sub h
{
    map
    {
        sprintf("0x%x", $_)
    }
    @_;
}
sub tk
{
    $t-&gt;tkRunning(1);
    use Tk;
    $mw = MainWindow-&gt;new ();
}
#for debugging Term::ReadLine::Gnu
sub afterinit
{
    *t = \$PerlSh::term;
    *a = \$PerlSh::attribs;
}
</code></pre>
<dt><i>~/.perlsh_history</i>
<dd>
<dt><i>~/.inputrc</i>
<dd> A initialization file for the <font SIZE="-1">GNU</font> Readline Library. Refer its manual for details.</dl>

<h2>SEE ALSO</h2>

 Term::ReadLine::Gnu &lt;<a rel="nofollow" HREF="http://search.cpan.org/dist/Term-ReadLine-Gnu/">http://search.cpan.org/dist/Term-ReadLine-Gnu/</a>&gt; 

 <font SIZE="-1">GNU</font> Readline Library &lt;<a rel="nofollow" HREF="http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html">http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html</a>&gt;

<h2>AUTHOR</h2>

 Hiroo Hayashi &lt;hiroo.hayashi [at] computer.org&gt; 

<h2>Index</h2>


