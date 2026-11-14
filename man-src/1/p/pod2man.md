---
title: "pod2man(1)"
name: "pod2man"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2man/"
description: "pod2man – Convert POD data to formatted *roff input"
---

<h2 class="name">NAME</h2>
<p> pod2man &#8211; Convert POD data to formatted *roff input </p>
<h2>SYNOPSIS</h2>
<p> pod2man [<code>&#8211;center</code>=<i>string</i>] [<code>&#8211;date</code>=<i>string</i>] [<code>&#8211;errors</code>=<i>style</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;fixed</code>=<i>font</i>]&nbsp;[<code>&#8211;fixedbold</code>=<i>font</i>]&nbsp;[<code>&#8211;fixeditalic</code>=<i>font</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;fixedbolditalic</code>=<i>font</i>]&nbsp;[<code>&#8211;name</code>=<i>name</i>]&nbsp;[<code>&#8211;nourls</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;official</code>]&nbsp;[<code>&#8211;release</code>=<i>version</i>]&nbsp;[<code>&#8211;section</code>=<i>manext</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;quotes</code>=<i>quotes</i>]&nbsp;[<code>&#8211;lquote</code>=<i>quote</i>]&nbsp;[<code>&#8211;rquote</code>=<i>quote</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;stderr</code>]&nbsp;[<code>&#8211;utf8</code>]&nbsp;[<code>&#8211;verbose</code>]&nbsp;[<i>input</i>&nbsp;[<i>output</i>]&nbsp;&#8230;] </p>
<p> pod2man <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pod2man</code> is a front-end for Pod::Man, using it to generate *roff input from <font SIZE="-1">POD</font> source. The resulting *roff code is suitable for display on a terminal using <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), normally via <code><a href="/docs/linux/man/1-man/">man</a></code>(1), or printing using <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). </p>
<p> <i>input</i> is the file to read for <font SIZE="-1">POD</font> source (the <font SIZE="-1">POD</font> can be embedded in code). If <i>input</i> isn&#8217;t given, it defaults to <tt>&quot;STDIN&quot;</tt>. <i>output</i>, if given, is the file to which to write the formatted output. If <i>output</i> isn&#8217;t given, the formatted output is written to <tt>&quot;STDOUT&quot;</tt>. Several <font SIZE="-1">POD</font> files can be processed in the same <code>pod2man</code> invocation (saving module load and compile times) by providing multiple pairs of <i>input</i> and <i>output</i> files on the command line. </p>
<p> <code>&#8211;section</code>, <code>&#8211;release</code>, <code>&#8211;center</code>, <code>&#8211;date</code>, and <code>&#8211;official</code> can be used to set the headers and footers to use; if not given, Pod::Man will assume various defaults. See below or Pod::Man for details. </p>
<p> <code>pod2man</code> assumes that your *roff formatters have a fixed-width font named <tt>&quot;CW&quot;</tt>. If yours is called something else (like <tt>&quot;CR&quot;</tt>), use <code>&#8211;fixed</code> to specify it. This generally only matters for troff output for printing. Similarly, you can set the fonts used for bold, italic, and bold italic fixed-width output. </p>
<p> Besides the obvious pod conversions, Pod::Man, and therefore pod2man also takes care of formatting <code>func()</code>, <a href="/docs/linux/man/n-func/">func</a>(n), and simple variable references like <tt>$foo</tt> or <tt>@bar</tt> so you don&#8217;t have to use code escapes for them; complex expressions like <tt>$fred{'stuff'}</tt> will still need to be escaped, though. It also translates dashes that aren&#8217;t used as hyphens into en dashes, makes long dashes&#8212;like this&#8212;into proper em dashes, fixes &#8220;paired quotes,&#8221; and takes care of several other troff-specific tweaks. See Pod::Man for complete information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>string</i>, <code>&#8211;center</code>=<i>string</i></p>
<dd> Sets the centered page header for the <tt>&quot;.TH&quot;</tt> macro to <i>string</i>. The default is &#8220;User Contributed Perl Documentation&#8221;, but also see <code>&#8211;official</code> below.</p>
<dt><code>-d</code> <i>string</i>, <code>&#8211;date</code>=<i>string</i></p>
<dd> Set the left-hand footer string for the <tt>&quot;.TH&quot;</tt> macro to <i>string</i>. By default, the modification date of the input file will be used, or the current date if input comes from <tt>&quot;STDIN&quot;</tt>, and will be based on <font SIZE="-1">UTC</font> (so that the output will be reproducible regardless of local time zone).</p>
<dt><code>&#8211;errors</code>=<i>style</i></p>
<dd> Set the error handling style. <tt>&quot;die&quot;</tt> says to throw an exception on any <font SIZE="-1">POD</font> formatting error. <tt>&quot;stderr&quot;</tt> says to report errors on standard error, but not to throw an exception. <tt>&quot;pod&quot;</tt> says to include a <font SIZE="-1">POD ERRORS</font> section in the resulting documentation summarizing the errors. <tt>&quot;none&quot;</tt> ignores <font SIZE="-1">POD</font> errors entirely, as much as possible. </p>
<p> The default is <tt>&quot;die&quot;</tt>.</p>
<dt><code>&#8211;fixed</code>=<i>font</i></p>
<dd> The fixed-width font to use for verbatim text and code. Defaults to <tt>&quot;CW&quot;</tt>. Some systems may want <tt>&quot;CR&quot;</tt> instead. Only matters for <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) output.</p>
<dt><code>&#8211;fixedbold</code>=<i>font</i></p>
<dd> Bold version of the fixed-width font. Defaults to <tt>&quot;CB&quot;</tt>. Only matters for <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) output.</p>
<dt><code>&#8211;fixeditalic</code>=<i>font</i></p>
<dd> Italic version of the fixed-width font (actually, something of a misnomer, since most fixed-width fonts only have an oblique version, not an italic version). Defaults to <tt>&quot;CI&quot;</tt>. Only matters for <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) output.</p>
<dt><code>&#8211;fixedbolditalic</code>=<i>font</i></p>
<dd> Bold italic (probably actually oblique) version of the fixed-width font. Pod::Man doesn&#8217;t assume you have this, and defaults to <tt>&quot;CB&quot;</tt>. Some systems (such as Solaris) have this font available as <tt>&quot;CX&quot;</tt>. Only matters for <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out usage information.</p>
<dt><code>-l</code>, <code>&#8211;lax</code></p>
<dd> No longer used. <code>pod2man</code> used to check its input for validity as a manual page, but this should now be done by <code><a href="/docs/linux/man/1-podchecker/">podchecker</a></code>(1) instead. Accepted for backward compatibility; this option no longer does anything.</p>
<dt><code>&#8211;lquote</code>=<i>quote</i></p>
<dd>
<dt><code>&#8211;rquote</code>=<i>quote</i></p>
<dd> Sets the quote marks used to surround C&lt;&gt; text. <code>&#8211;lquote</code> sets the left quote mark and <code>&#8211;rquote</code> sets the right quote mark. Either may also be set to the special value <tt>&quot;none&quot;</tt>, in which case no quote mark is added on that side of C&lt;&gt; text (but the font is still changed for troff output). </p>
<p> Also see the <code>&#8211;quotes</code> option, which can be used to set both quotes at once. If both <code>&#8211;quotes</code> and one of the other options is set, <code>&#8211;lquote</code> or <code>&#8211;rquote</code> overrides <code>&#8211;quotes</code>.</p>
<dt><code>-n</code> <i>name</i>, <code>&#8211;name</code>=<i>name</i></p>
<dd> Set the name of the manual page for the <tt>&quot;.TH&quot;</tt> macro to <i>name</i>. Without this option, the manual name is set to the uppercased base name of the file being converted unless the manual section is 3, in which case the path is parsed to see if it is a Perl module path. If it is, a path like <tt>&quot;.../lib/Pod/Man.pm&quot;</tt> is converted into a name like <tt>&quot;Pod::Man&quot;</tt>. This option, if given, overrides any automatic determination of the name. </p>
<p> Although one does not have to follow this convention, be aware that the convention for <font SIZE="-1">UNIX</font> man pages for commands is for the man page title to be in all-uppercase, even if the command isn&#8217;t. </p>
<p> This option is probably not useful when converting multiple <font SIZE="-1">POD</font> files at once. </p>
<p> When converting <font SIZE="-1">POD</font> source from standard input, the name will be set to <tt>&quot;STDIN&quot;</tt> if this option is not provided. Providing this option is strongly recommended to set a meaningful manual page name.</p>
<dt><code>&#8211;nourls</code></p>
<dd> Normally, L&lt;&gt; formatting codes with a <font SIZE="-1">URL</font> but anchor text are formatted to show both the anchor text and the <font SIZE="-1">URL.</font> In other words: </p>
<pre>
    L&lt;foo|<a rel="nofollow" href="http://example.com/">http://example.com/</a>&gt;
</pre>
<p> is formatted as: </p>
<pre>
    foo &lt;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&gt;
</pre>
<p> This flag, if given, suppresses the <font SIZE="-1">URL</font> when anchor text is given, so this example would be formatted as just <tt>&quot;foo&quot;</tt>. This can produce less cluttered output in cases where the URLs are not particularly important.</p>
<dt><code>-o</code>, <code>&#8211;official</code></p>
<dd> Set the default header to indicate that this page is part of the standard Perl release, if <code>&#8211;center</code> is not also given.</p>
<dt><code>-q</code> <i>quotes</i>, <code>&#8211;quotes</code>=<i>quotes</i></p>
<dd> Sets the quote marks used to surround C&lt;&gt; text to <i>quotes</i>. If <i>quotes</i> is a single character, it is used as both the left and right quote. Otherwise, it is split in half, and the first half of the string is used as the left quote and the second is used as the right quote. </p>
<p> <i>quotes</i> may also be set to the special value <tt>&quot;none&quot;</tt>, in which case no quote marks are added around C&lt;&gt; text (but the font is still changed for troff output). </p>
<p> Also see the <code>&#8211;lquote</code> and <code>&#8211;rquote</code> options, which can be used to set the left and right quotes independently. If both <code>&#8211;quotes</code> and one of the other options is set, <code>&#8211;lquote</code> or <code>&#8211;rquote</code> overrides <code>&#8211;quotes</code>.</p>
<dt><code>-r</code> <i>version</i>, <code>&#8211;release</code>=<i>version</i></p>
<dd> Set the centered footer for the <tt>&quot;.TH&quot;</tt> macro to <i>version</i>. By default, this is set to the version of Perl you run <code>pod2man</code> under. Setting this to the empty string will cause some *roff implementations to use the system default value. </p>
<p> Note that some system <tt>&quot;an&quot;</tt> macro sets assume that the centered footer will be a modification date and will prepend something like &#8220;Last modified: &#8221;. If this is the case for your target system, you may want to set <code>&#8211;release</code> to the last modified date and <code>&#8211;date</code> to the version number.</p>
<dt><code>-s</code> <i>string</i>, <code>&#8211;section</code>=<i>string</i></p>
<dd> Set the section for the <tt>&quot;.TH&quot;</tt> macro. The standard section numbering convention is to use 1 for user commands, 2 for system calls, 3 for functions, 4 for devices, 5 for file formats, 6 for games, 7 for miscellaneous information, and 8 for administrator commands. There is a lot of variation here, however; some systems (like Solaris) use 4 for file formats, 5 for miscellaneous information, and 7 for devices. Still others use 1m instead of 8, or some mix of both. About the only section numbers that are reliably consistent are 1, 2, and 3. </p>
<p> By default, section 1 will be used unless the file ends in <tt>&quot;.pm&quot;</tt>, in which case section 3 will be selected.</p>
<dt><code>&#8211;stderr</code></p>
<dd> By default, <code>pod2man</code> dies if any errors are detected in the <font SIZE="-1">POD</font> input. If <code>&#8211;stderr</code> is given and no <code>&#8211;errors</code> flag is present, errors are sent to standard error, but <code>pod2man</code> does not abort. This is equivalent to <tt>&quot;--errors=stderr&quot;</tt> and is supported for backward compatibility.</p>
<dt><code>-u</code>, <code>&#8211;utf8</code></p>
<dd> By default, <code>pod2man</code> produces the most conservative possible *roff output to try to ensure that it will work with as many different *roff implementations as possible. Many *roff implementations cannot handle non-ASCII characters, so this means all non-ASCII characters are converted either to a *roff escape sequence that tries to create a properly accented character (at least for troff output) or to <tt>&quot;X&quot;</tt>. </p>
<p> This option says to instead output literal <font SIZE="-1">UTF-8</font> characters. If your *roff implementation can handle it, this is the best output format to use and avoids corruption of documents containing non-ASCII characters. However, be warned that *roff source with literal <font SIZE="-1">UTF-8</font> characters is not supported by many implementations and may even result in segfaults and other bad behavior. </p>
<p> Be aware that, when using this option, the input encoding of your <font SIZE="-1">POD</font> source should be properly declared unless it&#8217;s US-ASCII. Pod::Simple will attempt to guess the encoding and may be successful if it&#8217;s Latin-1 or <font SIZE="-1">UTF-8,</font> but it will warn, which by default results in a <code>pod2man</code> failure. Use the <tt>&quot;=encoding&quot;</tt> command to declare the encoding. See <code><a href="/docs/linux/man/1-perlpod/">perlpod</a></code>(1) for more information.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print out the name of each output file as it is being generated.</dl>
<h2>EXIT STATUS</h2>
<p> As long as all documents processed result in some output, even if that output includes errata (a <tt>&quot;POD ERRORS&quot;</tt> section generated with <tt>&quot;--errors=pod&quot;</tt>), <code>pod2man</code> will exit with status 0. If any of the documents being processed do not result in an output document, <code>pod2man</code> will exit with status 1. If there are syntax errors in a <font SIZE="-1">POD</font> document being processed and the error handling style is set to the default of <tt>&quot;die&quot;</tt>, <code>pod2man</code> will abort immediately with exit status 255.</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>pod2man</code> fails with errors, see Pod::Man and Pod::Simple for information about what those errors might mean.</p>
<h2>EXAMPLES</h2>
<pre>
    pod2man program &gt; program.1
    pod2man SomeModule.pm /usr/perl/man/man3/SomeModule.3
    pod2man --section=7 note.pod &gt; note.7
</pre>
<p> If you would like to print out a lot of man page continuously, you probably want to set the C and D registers to set contiguous page numbering and even/odd paging, at least on some versions of <code><a href="/docs/linux/man/7-man/">man</a></code>(7). </p>
<pre>
    troff -man -rC1 -rD1 perl.1 perldata.1 perlsyn.1 ...
</pre>
<p> To get index entries on <tt>&quot;STDERR&quot;</tt>, turn on the F register, as in: </p>
<pre>
    troff -man -rF1 perl.1
</pre>
<p> The indexing merely outputs messages via <tt>&quot;.tm&quot;</tt> for each major page, section, subsection, item, and any <tt>&quot;X&lt;&gt;&quot;</tt> directives. See Pod::Man for more details.</p>
<h2>BUGS</h2>
<p> Lots of this documentation is duplicated from Pod::Man.</p>
<h2>AUTHOR</h2>
<p> Russ Allbery &lt;rra [at] cpan.org&gt;, based <i>very</i> heavily on the original <code>pod2man</code> by Larry Wall and Tom Christiansen.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 1999-2001, 2004, 2006, 2008, 2010, 2012-2019 Russ Allbery &lt;rra [at] cpan.org&gt; </p>
<p> This program is free software; you may redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>SEE ALSO</h2>
<p> Pod::Man, Pod::Simple, <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-perlpod/">perlpod</a></code>(1), <code><a href="/docs/linux/man/1-podchecker/">podchecker</a></code>(1), <code><a href="/docs/linux/man/1-perlpodstyle/">perlpodstyle</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/7-man/">man</a></code>(7) </p>
<p> The man page documenting the an macro set may be <code><a href="/docs/linux/man/5-man/">man</a></code>(5) instead of <code><a href="/docs/linux/man/7-man/">man</a></code>(7) on your system. </p>
<p> The current version of this script is always available from its web site at &lt;<a rel="nofollow" href="https://www.eyrie.org/~eagle/software/podlators/">https://www.eyrie.org/~eagle/software/podlators/</a>&gt;. It is also part of the Perl core distribution as of 5.6.0. </p>
<h2>Index</h2>
