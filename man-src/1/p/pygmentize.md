---
title: "pygmentize(1)"
name: "pygmentize"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pygmentize/"
description: "pygmentize – highlights the input file"
---

<h2 class="name">NAME</h2>
<p> pygmentize &#8211; highlights the input file</p>
<h2>SYNOPSIS</h2>
<p> <code>pygmentize</code> [-l&nbsp;<i>&lt;lexer&gt;</i>&nbsp;| -g]&nbsp;[-F&nbsp;<i>&lt;filter&gt;</i>[:<i>&lt;options&gt;</i>]]&nbsp;[-f&nbsp;<i>&lt;formatter&gt;</i>] [-O&nbsp;<i>&lt;options&gt;</i>]&nbsp;[-P&nbsp;<i>&lt;option=value&gt;</i>]&nbsp;[-o&nbsp;<i>&lt;outfile&gt;</i>]&nbsp;[<i>&lt;infile&gt;</i>]<br />
 <code>pygmentize</code> -S&nbsp;<i>&lt;style&gt;</i>&nbsp;-f&nbsp;<i>&lt;formatter&gt;</i>&nbsp;[-a&nbsp;<i>&lt;arg&gt;</i>]&nbsp;[-O&nbsp;<i>&lt;options&gt;</i>]&nbsp;[-P&nbsp;<i>&lt;option=value&gt;</i>]<br />
 <code>pygmentize</code> -L&nbsp;[<i>&lt;which&gt;</i>&nbsp;&#8230;]<br />
 <code>pygmentize</code> -N&nbsp;<i>&lt;filename&gt;</i><br />
 <code>pygmentize</code> -C<br />
 <code>pygmentize</code> -H&nbsp;<i>&lt;type&gt;</i>&nbsp;<i>&lt;name&gt;</i><br />
 <code>pygmentize</code> -h | -V </p>
<h2>DESCRIPTION</h2>
<p> Pygments is a generic syntax highlighter for general use in all kinds of software such as forum systems, wikis or other applications that need to prettify source code. </p>
<p> Its highlights are:<br />
&nbsp;<wbr>&nbsp;*&nbsp;a wide range of common languages and markup formats is supported<br />
&nbsp;<wbr>&nbsp;*&nbsp;special attention is paid to details, increasing quality by a fair amount<br />
&nbsp;<wbr>&nbsp;*&nbsp;support for new languages and formats are added easily<br />
&nbsp;<wbr>&nbsp;*&nbsp;a number of output formats, presently HTML, LaTeX and ANSI sequences<br />
&nbsp;<wbr>&nbsp;*&nbsp;it is usable as a command-line tool and as a library<br />
&nbsp;<wbr>&nbsp;*&nbsp;&#8230; and it highlights even Brainf**k! </p>
<p> <code>pygmentize</code> is a command that uses Pygments to highlight the input file and write the result to <i>&lt;outfile&gt;</i>. If no <i>&lt;infile&gt;</i> is given, stdin is used.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-l </code><i>&lt;lexer&gt;</i></p>
<dd> Set the lexer name. If not given, the lexer is guessed from the extension of the input file name (this obviously doesn&#8217;t work if the input is stdin).</p>
<dt><code>-g</code></p>
<dd> Attempt to guess the lexer from the file contents, or pass through as plain text if this fails (this option works for highlighting standard input).</p>
<dt><code>-F </code><i>&lt;filter&gt;</i>[:<i>&lt;options&gt;</i>]</p>
<dd> Add a filter to the token stream. You can give options in the same way as for -O after a colon (note: there must not be spaces around the colon). This option can be given multiple times.</p>
<dt><code>-f </code><i>&lt;formatter&gt;</i></p>
<dd> Set the formatter name. If not given, it will be guessed from the extension of the output file name. If no output file is given, the terminal formatter will be used by default.</p>
<dt><code>-o </code><i>&lt;outfile&gt;</i></p>
<dd> Set output file. If not given, stdout is used.</p>
<dt><code>-O </code><i>&lt;options&gt;</i></p>
<dd> With this option, you can give the lexer and formatter a comma-separated list of options, e.g. &quot;-O bg=light,python=cool&quot;. Which options are valid for which lexers and formatters can be found in the documentation. This option can be given multiple times.</p>
<dt><code>-P </code><i>&lt;option=value&gt;</i></p>
<dd> This option adds lexer and formatter options like the -O option, but you can only give one option per -P. That way, the option value may contain commas and equals signs, which it can&#8217;t with -O.</p>
<dt><code>-S </code><i>&lt;style&gt;</i></p>
<dd> Print out style definitions for style <i>&lt;style&gt;</i> and for formatter <i>&lt;formatter&gt;</i>. The meaning of the argument given by <code>-a </code><i>&lt;arg&gt;</i> is formatter dependent and can be found in the documentation.</p>
<dt><code>-L [</code><i>&lt;which&gt;</i> &#8230;]</p>
<dd> List lexers, formatters, styles or filters. Set <i>&lt;which&gt;</i> to the thing you want to list (e.g. &quot;styles&quot;), or omit it to list everything.</p>
<dt><code>-N </code><i>&lt;filename&gt;</i></p>
<dd> Guess and print out a lexer name based solely on the given filename. Does not take input or highlight anything. If no specific lexer can be found, &quot;text&quot; is printed.</p>
<dt><code>-C</code></p>
<dd> Like <i>-N</i>, but guess a lexer based on content read from standard input.</p>
<dt><code>-H </code><i>&lt;type&gt;</i> <i>&lt;name&gt;</i></p>
<dd> Print detailed help for the object <i>&lt;name&gt;</i> of type <i>&lt;type&gt;</i>, where <i>&lt;type&gt;</i> is one of &quot;lexer&quot;, &quot;formatter&quot; or &quot;filter&quot;.</p>
<dt><code>-h</code></p>
<dd> Show help screen.</p>
<dt><code>-V</code></p>
<dd> Show version of the Pygments package.</dl>
<h2>SEE ALSO</h2>
<p> /usr/share/doc/python-pygments-doc/index.html</p>
<h2>AUTHOR</h2>
<p> pygmentize was written by Georg Brandl &lt;g.brandl [at] gmx.net&gt;. </p>
<p> This manual page was written by Piotr Ozarowski &lt;ozarow [at] gmail.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
