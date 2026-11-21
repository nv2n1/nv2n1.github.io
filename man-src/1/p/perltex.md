---
title: "perltex(1)"
name: "perltex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltex/"
description: "perltex – enable LaTeX macros to be defined in terms of Perl code"
---

<h2 class="name">NAME</h2>
<p> perltex &#8211; enable LaTeX macros to be defined in terms of Perl code </p>
<h2>SYNOPSIS</h2>
<p> perltex [<code>&#8211;help</code>] [<code>&#8211;latex</code>=<i>program</i>] [<code>&#8212;</code>[<code>no</code>]<code>safe</code>] [<code>&#8211;permit</code>=<i>feature</i>] [<code>&#8211;makesty</code>] [<i>latex options</i>]</p>
<h2>DESCRIPTION</h2>
<p> LaTeX &#8212; through the underlying TeX typesetting system &#8212; produces beautifully typeset documents but has a macro language that is difficult to program. In particular, support for complex string manipulation is largely lacking. Perl is a popular general-purpose programming language whose forte is string manipulation. However, it has no typesetting capabilities whatsoever. </p>
<p> Clearly, Perl&#8217;s programmability could complement LaTeX&#8217;s typesetting strengths. <code>perltex</code> is the tool that enables a symbiosis between the two systems. All a user needs to do is compile a LaTeX document using <code>perltex</code> instead of <code>latex</code>. (<code>perltex</code> is actually a wrapper for <code>latex</code>, so no <code>latex</code> functionality is lost.) If the document includes a <tt>&quot;</tt>\usepackage{perltex}&quot;</code> in its preamble, then <code>&quot;\perlnewcommand&quot;</code> and <code>&quot;\perlrenewcommand&quot;</code> macros will be made available. These behave just like LaTeX&#8217;s <code>&quot;\newcommand&quot;</code> and <code>&quot;\renewcommand&quot;</code> except that the macro body contains Perl code instead of LaTeX code.  </p>
<h2>OPTIONS</h2>
<p> <code>perltex</code> accepts the following command-line options: </p>
<dl>
<dt><code>--help</code></dt>
<dd> <p> Display basic usage information. </p>
 </dd>
<dt><code>--latex</code>=<i>program</i></dt>
<dd> <p> Specify a program to use instead of <code>latex</code>. For example, <code>&quot;--latex=pdflatex&quot;</code> would typeset the given document using <code>pdflatex</code> instead of ordinary <code>latex</code>. </p>
 </dd>
<dt><code>--</code>[<code>no</code>]<code>safe</code></dt>
<dd> <p> Enable or disable sandboxing. With the default of <code>--safe</code>, <code>perltex</code> executes the code from a <code>&quot;\perlnewcommand&quot;</code> or <code>&quot;\perlrenewcommand&quot;</code> macro within a protected environment that prohibits ``unsafe&#8217;&#8216; operations such as accessing files or executing external programs. Specifying <code>--nosafe</code> gives the LaTeX document <i>carte blanche</i> to execute any arbitrary Perl code, including that which can harm the user&#8217;s files. See Safe for more information. </p>
 </dd>
<dt><code>--permit</code>=<i>feature</i></dt>
<dd> <p> Permit particular Perl operations to be performed. The <code>--permit</code> option, which can be specified more than once on the command line, enables finer-grained control over the <code>perltex</code> sandbox. See Opcode for more information. </p>
 </dd>
<dt><code>--makesty</code></dt>
<dd> <p> Generate a LaTeX style file called <i>noperltex.sty</i>. Replacing the document&#8217;s <code>&quot;\usepackage{perltex}&quot;</code> line with <code>&quot;\usepackage{noperltex}&quot;</code> produces the same output but does not require PerlTeX, making the document suitable for distribution to people who do not have PerlTeX installed. The disadvantage is that <i>noperltex.sty</i> is specific to the document that produced it. Any changes to the document&#8217;s PerlTeX macro definitions or macro invocations necessitates rerunning <code>perltex</code> with the <code>--makesty</code> option. </p>
 </dd></dl>
<p> These options are then followed by whatever options are normally passed to <code>latex</code> (or whatever program was specified with <code>&quot;--latex&quot;</code>), including, for instance, the name of the <i>.tex</i> file to compile.  </p>
<h2>EXAMPLES</h2>
<p> In its simplest form, <code>perltex</code> is run just like <code>latex</code>: </p>
<pre><code>    perltex myfile.tex
</code></pre>
<p> To use <code>pdflatex</code> instead of regular <code>latex</code>, use the <code>--latex</code> option: </p>
<pre><code>    perltex --latex=pdflatex myfile.tex
</code></pre>
<p> If LaTeX gives a ``<code>&quot;trapped by operation mask&quot;</code>&#8216;&#8216; error and you trust the <i>.tex</i> file you&#8217;re trying to compile not to execute malicious Perl code (e.g., because you wrote it yourself), you can disable <code>perltex</code>&#8216;s safety mechansisms with <code>--nosafe</code>: </p>
<pre><code>    perltex --nosafe myfile.tex
</code></pre>
<p> The following command gives documents only <code>perltex</code>&#8216;s default permissions (<code>&quot;:browse&quot;</code>) plus the ability to open files and invoke the <code>&quot;time&quot;</code> command: </p>
<pre><code>    perltex --permit=:browse --permit=:filesys_open
      --permit=time myfile.tex
</code></pre>
<h2>ENVIRONMENT</h2>
<p> <code>perltex</code> honors the following environment variables: </p>
<dl>
<dt><font SIZE="-1">PERLTEX</font></dt>
<dd> <p> Specify the filename of the LaTeX compiler. The LaTeX compiler defaults to ``<code>&quot;latex&quot;</code>&#8216;&#8216;. The <code>&quot;PERLTEX&quot;</code> environment variable overrides this default, and the <code>--latex</code> command-line option (see ``<font SIZE="-1">OPTIONS&#8217;&#8216;</font>) overrides that. </p>
 </dd></dl>
<h2>FILES</h2>
<p> While compiling <i>jobname.tex</i>, <code>perltex</code> makes use of the following files: </p>
<dl>
<dt><i>jobname.lgpl</i></dt>
<dd> <p> log file written by Perl; helpful for debugging Perl macros </p>
 </dd>
<dt><i>jobname.topl</i></dt>
<dd> <p> information sent from LaTeX to Perl </p>
 </dd>
<dt><i>jobname.frpl</i></dt>
<dd> <p> information sent from Perl to LaTeX </p>
 </dd>
<dt><i>jobname.tfpl</i></dt>
<dd> <p> ``flag&#8217;&#8216; file whose existence indicates that <i>jobname.topl</i> contains valid data </p>
 </dd>
<dt><i>jobname.ffpl</i></dt>
<dd> <p> ``flag&#8217;&#8216; file whose existence indicates that <i>jobname.frpl</i> contains valid data </p>
 </dd>
<dt><i>jobname.dfpl</i></dt>
<dd> <p> ``flag&#8217;&#8216; file whose existence indicates that <i>jobname.ffpl</i> has been deleted </p>
 </dd>
<dt><i>noperltex-#.tex</i></dt>
<dd> <p> file generated by <i>noperltex.sty</i> for each PerlTeX macro invocation </p>
 </dd></dl>
<h2>NOTES</h2>
<p> <code>perltex</code>&#8216;s sandbox defaults to what Opcode calls ``<code>&quot;:browse&quot;</code>&#8216;&#8216;.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-pdflatex/">pdflatex</a></code>(1), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/3pm-Safe/">Safe</a></code>(3pm), <code><a href="/docs/linux/man/3pm-Opcode/">Opcode</a></code>(3pm)  </p>
<h2>AUTHOR</h2>
<p> Scott Pakin, <i>scott+pt [at] pakin.org</i> </p>
