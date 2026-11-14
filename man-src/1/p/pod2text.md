---
title: "pod2text(1)"
name: "pod2text"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2text/"
description: "pod2text – Convert POD data to formatted ASCII text"
---

<h2 class="name">NAME</h2>
<p> pod2text &#8211; Convert POD data to formatted ASCII text </p>
<h2>SYNOPSIS</h2>
<p> pod2text [<code>-aclostu</code>] [<code>&#8211;code</code>] [<code>&#8211;errors</code>=<i>style</i>] [<code>-i</code> <i>indent</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-q</code> <i>quotes</i>]&nbsp;[<code>&#8211;nourls</code>]&nbsp;[<code>&#8211;stderr</code>]&nbsp;[<code>-w</code> <i>width</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<i>input</i>&nbsp;[<i>output</i>&nbsp;&#8230;]] </p>
<p> pod2text <code>-h</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pod2text</code> is a front-end for Pod::Text and its subclasses. It uses them to generate formatted <font SIZE="-1">ASCII</font> text from <font SIZE="-1">POD</font> source. It can optionally use either termcap sequences or <font SIZE="-1">ANSI</font> color escape sequences to format the text. </p>
<p> <i>input</i> is the file to read for <font SIZE="-1">POD</font> source (the <font SIZE="-1">POD</font> can be embedded in code). If <i>input</i> isn&#8217;t given, it defaults to <tt>&quot;STDIN&quot;</tt>. <i>output</i>, if given, is the file to which to write the formatted output. If <i>output</i> isn&#8217;t given, the formatted output is written to <tt>&quot;STDOUT&quot;</tt>. Several <font SIZE="-1">POD</font> files can be processed in the same <code>pod2text</code> invocation (saving module load and compile times) by providing multiple pairs of <i>input</i> and <i>output</i> files on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;alt</code></p>
<dd> Use an alternate output format that, among other things, uses a different heading style and marks <tt>&quot;=item&quot;</tt> entries with a colon in the left margin.</p>
<dt><code>&#8211;code</code></p>
<dd> Include any non-POD text from the input file in the output as well. Useful for viewing code documented with <font SIZE="-1">POD</font> blocks with the <font SIZE="-1">POD</font> rendered and the code left intact.</p>
<dt><code>-c</code>, <code>&#8211;color</code></p>
<dd> Format the output with <font SIZE="-1">ANSI</font> color escape sequences. Using this option requires that Term::ANSIColor be installed on your system.</p>
<dt><code>&#8211;errors</code>=<i>style</i></p>
<dd> Set the error handling style. <tt>&quot;die&quot;</tt> says to throw an exception on any <font SIZE="-1">POD</font> formatting error. <tt>&quot;stderr&quot;</tt> says to report errors on standard error, but not to throw an exception. <tt>&quot;pod&quot;</tt> says to include a <font SIZE="-1">POD ERRORS</font> section in the resulting documentation summarizing the errors. <tt>&quot;none&quot;</tt> ignores <font SIZE="-1">POD</font> errors entirely, as much as possible. </p>
<p> The default is <tt>&quot;die&quot;</tt>.</p>
<dt><code>-i</code> <i>indent</i>, <code>&#8211;indent=</code><i>indent</i></p>
<dd> Set the number of spaces to indent regular text, and the default indentation for <tt>&quot;=over&quot;</tt> blocks. Defaults to 4 spaces if this option isn&#8217;t given.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print out usage information and exit.</p>
<dt><code>-l</code>, <code>&#8211;loose</code></p>
<dd> Print a blank line after a <tt>&quot;=head1&quot;</tt> heading. Normally, no blank line is printed after <tt>&quot;=head1&quot;</tt>, although one is still printed after <tt>&quot;=head2&quot;</tt>, because this is the expected formatting for manual pages; if you&#8217;re formatting arbitrary text documents, using this option is recommended.</p>
<dt><code>-m</code> <i>width</i>, <code>&#8211;left-margin</code>=<i>width</i>, <code>&#8211;margin</code>=<i>width</i></p>
<dd> The width of the left margin in spaces. Defaults to 0. This is the margin for all text, including headings, not the amount by which regular text is indented; for the latter, see <code>-i</code> option.</p>
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
<dt><code>-o</code>, <code>&#8211;overstrike</code></p>
<dd> Format the output with overstrike printing. Bold text is rendered as character, backspace, character. Italics and file names are rendered as underscore, backspace, character. Many pagers, such as <code>less</code>, know how to convert this to bold or underlined text.</p>
<dt><code>-q</code> <i>quotes</i>, <code>&#8211;quotes</code>=<i>quotes</i></p>
<dd> Sets the quote marks used to surround C&lt;&gt; text to <i>quotes</i>. If <i>quotes</i> is a single character, it is used as both the left and right quote. Otherwise, it is split in half, and the first half of the string is used as the left quote and the second is used as the right quote. </p>
<p> <i>quotes</i> may also be set to the special value <tt>&quot;none&quot;</tt>, in which case no quote marks are added around C&lt;&gt; text.</p>
<dt><code>-s</code>, <code>&#8211;sentence</code></p>
<dd> Assume each sentence ends with two spaces and try to preserve that spacing. Without this option, all consecutive whitespace in non-verbatim paragraphs is compressed into a single space.</p>
<dt><code>&#8211;stderr</code></p>
<dd> By default, <code>pod2text</code> dies if any errors are detected in the <font SIZE="-1">POD</font> input. If <code>&#8211;stderr</code> is given and no <code>&#8211;errors</code> flag is present, errors are sent to standard error, but <code>pod2text</code> does not abort. This is equivalent to <tt>&quot;--errors=stderr&quot;</tt> and is supported for backward compatibility.</p>
<dt><code>-t</code>, <code>&#8211;termcap</code></p>
<dd> Try to determine the width of the screen and the bold and underline sequences for the terminal from termcap, and use that information in formatting the output. Output will be wrapped at two columns less than the width of your terminal device. Using this option requires that your system have a termcap file somewhere where Term::Cap can find it and requires that your system support termios. With this option, the output of <code>pod2text</code> will contain terminal control sequences for your current terminal type.</p>
<dt><code>-u</code>, <code>&#8211;utf8</code></p>
<dd> By default, <code>pod2text</code> tries to use the same output encoding as its input encoding (to be backward-compatible with older versions). This option says to instead force the output encoding to <font SIZE="-1">UTF-8.</font> </p>
<p> Be aware that, when using this option, the input encoding of your <font SIZE="-1">POD</font> source should be properly declared unless it&#8217;s US-ASCII. Pod::Simple will attempt to guess the encoding and may be successful if it&#8217;s Latin-1 or <font SIZE="-1">UTF-8,</font> but it will warn, which by default results in a <code>pod2text</code> failure. Use the <tt>&quot;=encoding&quot;</tt> command to declare the encoding. See <code><a href="/docs/linux/man/1-perlpod/">perlpod</a></code>(1) for more information.</p>
<dt><code>-w</code>, <code>&#8211;width=</code><i>width</i>, <code>&#8211;</code><i>width</i></p>
<dd> The column at which to wrap text on the right-hand side. Defaults to 76, unless <code>-t</code> is given, in which case it&#8217;s two columns less than the width of your terminal device.</dl>
<h2>EXIT STATUS</h2>
<p> As long as all documents processed result in some output, even if that output includes errata (a <tt>&quot;POD ERRORS&quot;</tt> section generated with <tt>&quot;--errors=pod&quot;</tt>), <code>pod2text</code> will exit with status 0. If any of the documents being processed do not result in an output document, <code>pod2text</code> will exit with status 1. If there are syntax errors in a <font SIZE="-1">POD</font> document being processed and the error handling style is set to the default of <tt>&quot;die&quot;</tt>, <code>pod2text</code> will abort immediately with exit status 255.</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>pod2text</code> fails with errors, see Pod::Text and Pod::Simple for information about what those errors might mean. Internally, it can also produce the following diagnostics:</p>
<dl>
<dt>-c (&#8211;color) requires Term::ANSIColor be installed</p>
<dd> (F) <code>-c</code> or <code>&#8211;color</code> were given, but Term::ANSIColor could not be loaded.</p>
<dt>Unknown option: %s</p>
<dd> (F) An unknown command line option was given.</dl>
<p> In addition, other Getopt::Long error messages may result from invalid command-line options.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">COLUMNS</font></p>
<dd> If <code>-t</code> is given, <code>pod2text</code> will take the current width of your screen from this environment variable, if available. It overrides terminal width information in <font SIZE="-1">TERMCAP.</font></p>
<dt><font SIZE="-1">TERMCAP</font></p>
<dd> If <code>-t</code> is given, <code>pod2text</code> will use the contents of this environment variable if available to determine the correct formatting sequences for your current terminal device.</dl>
<h2>AUTHOR</h2>
<p> Russ Allbery &lt;rra [at] cpan.org&gt;.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright 1999-2001, 2004, 2006, 2008, 2010, 2012-2019 Russ Allbery &lt;rra [at] cpan.org&gt; </p>
<p> This program is free software; you may redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>SEE ALSO</h2>
<p> Pod::Text, Pod::Text::Color, Pod::Text::Overstrike, Pod::Text::Termcap, Pod::Simple, <code><a href="/docs/linux/man/1-perlpod/">perlpod</a></code>(1) </p>
<p> The current version of this script is always available from its web site at &lt;<a rel="nofollow" href="https://www.eyrie.org/~eagle/software/podlators/">https://www.eyrie.org/~eagle/software/podlators/</a>&gt;. It is also part of the Perl core distribution as of 5.6.0. </p>
<h2>Index</h2>
