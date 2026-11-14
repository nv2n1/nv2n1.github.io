---
title: "pod2latex(1)"
name: "pod2latex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2latex/"
description: "pod2latex – convert pod documentation to latex format"
---

<h2 class="name">NAME</h2>
<p> pod2latex &#8211; convert pod documentation to latex format </p>
<h2>SYNOPSIS</h2>
<pre>
  pod2latex *.pm
  pod2latex -out mytex.tex *.pod
  pod2latex -full -sections 'DESCRIPTION|NAME' SomeDir
  pod2latex -prefile h.tex -postfile t.tex my.pod
</pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;pod2latex&quot;</tt> is a program to convert <font SIZE="-1">POD</font> format documentation (perlpod) into latex. It can process multiple input documents at a time and either generate a latex file per input document or a single combined output file.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> This section describes the supported command line options. Minimum matching is supported.</p>
<dl>
<dt><code>-out</code></p>
<dd> Name of the output file to be used. If there are multiple input pods it is assumed that the intention is to write all translated output into a single file. <tt>&quot;.tex&quot;</tt> is appended if not present. If the argument is not supplied, a single document will be created for each input file.</p>
<dt><code>-full</code></p>
<dd> Creates a complete <tt>&quot;latex&quot;</tt> file that can be processed immediately (unless <tt>&quot;=for/=begin&quot;</tt> directives are used that rely on extra packages). Table of contents and index generation commands are included in the wrapper <tt>&quot;latex&quot;</tt> code.</p>
<dt><code>-sections</code></p>
<dd> Specify pod sections to include (or remove if negated) in the translation. See &#8220;<font SIZE="-1">SECTION SPECIFICATIONS&#8221;</font> in Pod::Select for the format to use for <i>section-spec</i>. This option may be given multiple times on the command line.This is identical to the similar option in the <tt>&quot;podselect()&quot;</tt> command.</p>
<dt><code>-modify</code></p>
<dd> This option causes the output <tt>&quot;latex&quot;</tt> to be slightly modified from the input pod such that when a <tt>&quot;=head1 NAME&quot;</tt> is encountered a section is created containing the actual pod name (rather than <font SIZE="-1"><code>NAME</code></font>) and all subsequent <tt>&quot;=head1&quot;</tt> directives are treated as subsections. This has the advantage that the description of a module will be in its own section which is helpful for including module descriptions in documentation. Also forces <tt>&quot;latex&quot;</tt> label and index entries to be prefixed by the name of the module.</p>
<dt><code>-h1level</code></p>
<dd> Specifies the <tt>&quot;latex&quot;</tt> section that is equivalent to a <tt>&quot;H1&quot;</tt> pod directive. This is an integer between 0 and 5 with 0 equivalent to a <tt>&quot;latex&quot;</tt> chapter, 1 equivalent to a <tt>&quot;latex&quot;</tt> section etc. The default is 1 (<tt>&quot;H1&quot;</tt> equivalent to a latex section).</p>
<dt><code>-help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>-man</code></p>
<dd> Print the manual page and exit.</p>
<dt><code>-verbose</code></p>
<dd> Print information messages as each document is processed.</p>
<dt><code>-preamble</code></p>
<dd> A user-supplied preamble for the LaTeX code. Multiple values are supported and appended in order separated by &#8220;
&#8221;. See <code>-prefile</code> for reading the preamble from a file.</p>
<dt><code>-postamble</code></p>
<dd> A user supplied postamble for the LaTeX code. Multiple values are supported and appended in order separated by &#8220;
&#8221;. See <code>-postfile</code> for reading the postamble from a file.</p>
<dt><code>-prefile</code></p>
<dd> A user-supplied preamble for the LaTeX code to be read from the named file. Multiple values are supported and appended in order. See <code>-preamble</code>.</p>
<dt><code>-postfile</code></p>
<dd> A user-supplied postamble for the LaTeX code to be read from the named file. Multiple values are supported and appended in order. See <code>-postamble</code>.</dl>
<h2>BUGS</h2>
<p> Known bugs are:</p>
<dl>
<dt>&bull;</p>
<dd> Cross references between documents are not resolved when multiple pod documents are converted into a single output <tt>&quot;latex&quot;</tt> file.</p>
<dt>&bull;</p>
<dd> Functions and variables are not automatically recognized and they will therefore not be marked up in any special way unless instructed by an explicit pod command.</dl>
<h2>SEE ALSO</h2>
<p> Pod::LaTeX</p>
<h2>AUTHOR</h2>
<p> Tim Jenness &lt;tjenness [at] cpan.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Copyright (C) 2000, 2003, 2004 Tim Jenness. All Rights Reserved. </p>
<h2>Index</h2>
