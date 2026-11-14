---
title: "podchecker(1)"
name: "podchecker"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podchecker/"
description: "podchecker – check the syntax of POD format documentation files"
---

<h2 class="name">NAME</h2>
<p> podchecker &#8211; check the syntax of POD format documentation files </p>
<h2>SYNOPSIS</h2>
<p> <code>podchecker</code> [<code>-help</code>] [<code>-man</code>] [<code>-(no)warnings</code>] [<i>file</i> &#8230;]</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>-man</code></p>
<dd> Print the manual page and exit.</p>
<dt><code>-warnings</code> <code>-nowarnings</code></p>
<dd> Turn on/off printing of warnings. Repeating <code>-warnings</code> increases the warning level, i.e. more warnings are printed. Currently increasing to level two causes flagging of unescaped &#8220;&lt;,&gt;&#8221; characters.</p>
<dt><i>file</i></p>
<dd> The pathname of a <font SIZE="-1">POD</font> file to syntax-check (defaults to standard input).</dl>
<h2>DESCRIPTION</h2>
<p> <code>podchecker</code> will read the given input files looking for <font SIZE="-1">POD</font> syntax errors in the <font SIZE="-1">POD</font> documentation and will print any errors it find to <font SIZE="-1">STDERR.</font> At the end, it will print a status message indicating the number of errors found. </p>
<p> Directories are ignored, an appropriate warning message is printed. </p>
<p> <code>podchecker</code> invokes the <code>podchecker()</code> function exported by <code>Pod::Checker</code> Please see &#8220;<code>podchecker()</code>&#8221; in Pod::Checker for more details.</p>
<h2>RETURN VALUE</h2>
<p> <code>podchecker</code> returns a 0 (zero) exit status if all specified <font SIZE="-1">POD</font> files are ok.</p>
<h2>ERRORS</h2>
<p> <code>podchecker</code> returns the exit status 1 if at least one of the given <font SIZE="-1">POD</font> files has syntax errors. </p>
<p> The status 2 indicates that at least one of the specified files does not contain <i>any</i> <font SIZE="-1">POD</font> commands. </p>
<p> Status 1 overrides status 2. If you want unambiguous results, call <code>podchecker</code> with one single argument only.</p>
<h2>SEE ALSO</h2>
<p> Pod::Simple and Pod::Checker</p>
<h2>AUTHORS</h2>
<p> Please report bugs using &lt;<a rel="nofollow" href="http://rt.cpan.org">http://rt.cpan.org</a>&gt;. </p>
<p> Brad Appleton &lt;bradapp [at] enteract.com&gt;, Marek Rouchal &lt;marekr [at] cpan.org&gt; </p>
<p> Based on code for <code><a href="/docs/linux/man/1-pod--text--pod2text/">Pod::Text::pod2text</a>(1)</code> written by Tom Christiansen &lt;tchrist [at] mox.perl.com&gt; </p>
<h2>Index</h2>
