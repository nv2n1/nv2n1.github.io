---
title: "highlight(1)"
name: "highlight"
section: "1"
letter: "h"
url: "/docs/linux/man/1-highlight/"
description: "Highlight – a universal sourcecode to formatted text converter"
---

<h2 class="name">NAME</h2>
<p> Highlight &#8211; a universal sourcecode to formatted text converter</p>
<h2>SYNOPSIS</h2>
<p> <code>highlight</code> [OPTIONS]&#8230; [FILES]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>Highlight</code> converts sourcecode to HTML, XHTML, RTF, ODT, LaTeX, TeX, BBCode, SVG, XTERM or ANSI escape sequences. There are several colour themes available. <code>Highlight</code> recognizes keywords, numbers, strings, comments, symbols and preprocessor directives. It supports about 160 programming languages, which are defined in Lua scripts. </p>
<p> It&#8217;s easily possible to enhance highlight&#8217;s database of programming languages and colour themes. See the README file for details.</p>
<h2>General options</h2>
<dl>
<dt>-B, &#8211;batch-recursive=&lt;wildcard&gt;</p>
<dd> convert all files matching the wildcard (uses recursive search)</p>
<dt>-D, &#8211;data-dir=&lt;path&gt;</p>
<dd> set path to highlight data directory</p>
<dt>&#8211;add-config-dir=&lt;path&gt;</p>
<dd> set path to an additional configuration directory</p>
<dt>&#8211;config-file=&lt;file&gt;</p>
<dd> set path to a lang or theme file</p>
<dt>-h, &#8211;help</p>
<dd> print this help</p>
<dt>-i, &#8211;input=&lt;file&gt;</p>
<dd> name of input file</p>
<dt>-o, &#8211;output=&lt;file&gt;</p>
<dd> name of output file</p>
<dt>-d, &#8211;outdir=&lt;output directory&gt;</p>
<dd> name of output directory</p>
<dt>-P, &#8211;progress</p>
<dd> print progress bar in batch mode</p>
<dt>-S, &#8211;syntax=&lt;type&gt;</p>
<dd> set type of source code, necessary if input file suffix is missing</p>
<dt>-v, &#8211;verbose</p>
<dd> print debug info to stderr</p>
<dt>-p, &#8211;list-langs</p>
<dd> list installed language definitions</p>
<dt>-q, &#8211;quiet</p>
<dd> supress progress info in batch mode</p>
<dt>-w, &#8211;list-themes</p>
<dd> list installed themes</p>
<dt>&#8211;force</p>
<dd> generate output if input syntax is unknown</p>
<dt>&#8211;plug-in=&lt;script&gt;</p>
<dd> execute Lua plug-in script; repeat option to apply multiple plug-ins</p>
<dt>&#8211;plug-in-read</p>
<dd> set input file for a plug-in (e.g. &#8216;tags&#8217;)</p>
<dt>&#8211;print-config</p>
<dd> print path configuration</p>
<dt>&#8211;print-style</p>
<dd> print stylesheet only (see &#8211;style-outfile)</p>
<dt>&#8211;skip=&lt;list&gt;</p>
<dd> ignore listed unknown file types (Example: &#8211;skip=&#8217;bak;c~;h~&#8217;)</p>
<dt>&#8211;start-nested=&lt;lang&gt;</p>
<dd> define nested language which starts input without opening delimiter</p>
<dt>&#8211;validate-input</p>
<dd> test if input is a valid text file</p>
<dt>&#8211;version</p>
<dd> print version and copyright info </p>
</dl>
<h2>Output formatting options</h2>
<dl>
<dt>-O, &#8211;out-format=&lt;format&gt;</p>
<dd> output file in given format &lt;format&gt;=[html, xhtml, latex, tex, rtf, odt, ansi, xterm256, bbcode, svg]</p>
<dt>-c, &#8211;style-outfile=&lt;file&gt;</p>
<dd> name of style definition file or output to stdout, if &quot;stdout&quot; is given as file argument</p>
<dt>-T, &#8211;doc-title</p>
<dd> document title</p>
<dt>-e, &#8211;style-infile=&lt;file&gt;</p>
<dd> name of file to be included in style-outfile</p>
<dt>-f, &#8211;fragment</p>
<dd> omit header and footer of the output document</p>
<dt>-F, &#8211;reformat=&lt;style&gt;</p>
<dd> reformat output in given style. &lt;style&gt;=[allman, banner, gnu, java, kr, linux, stroustrup, whitesmith]</p>
<dt>-I, &#8211;include-style</p>
<dd> include style definition in output</p>
<dt>-J, &#8211;line-length=&lt;num&gt;</p>
<dd> line length before wrapping (see -W, -V)</p>
<dt>-j, &#8211;line-number-length=&lt;num&gt;</p>
<dd> line number length incl. left padding</p>
<dt>-k, &#8211;font=&lt;font&gt;</p>
<dd> set font (specific to output format)</p>
<dt>-K, &#8211;font-size=&lt;num?&gt;</p>
<dd> set font size (specific to output format)</p>
<dt>-l, &#8211;line-numbers</p>
<dd> print line numbers in output file</p>
<dt>-m, &#8211;line-number-start=&lt;cnt&gt;</p>
<dd> start line numbering with cnt (assumes -l)</p>
<dt>-s, &#8211;style=&lt;style name&gt;</p>
<dd> set highlighting style (see &#8211;list-themes)</p>
<dt>-t &#8211;replace-tabs=&lt;num&gt;</p>
<dd> replace tabs by num spaces</p>
<dt>-u, &#8211;encoding=&lt;enc&gt;</p>
<dd> set output encoding which matches input file encoding; omit encoding information if set to &quot;NONE&quot;</p>
<dt>-V, &#8211;wrap-simple</p>
<dd> wrap long lines without indenting function parameters and statements</p>
<dt>-W, &#8211;wrap</p>
<dd> wrap long lines (use with caution)</p>
<dt>-z, &#8211;zeroes</p>
<dd> fill leading space of line numbers with zeroes</p>
<dt>&#8211;kw-case=&lt;upper|lower|capitalize&gt;</p>
<dd> output all keywords in given case if language is not case sensitive</p>
<dt>&#8211;delim-cr</p>
<dd> set CR as end-of-line delimiter (MacOS 9)</p>
<dt>&#8211;no-trailing-nl</p>
<dd> omit trailing newline</p>
<dt>&#8211;wrap-no-numbers</p>
<dd> omit line numbers of wrapped lines (assumes -l) </p>
</dl>
<h2>(X)HTML OPTIONS</h2>
<dl>
<dt>-a, &#8211;anchors</p>
<dd> attach anchors to line numbers (HTML only)</p>
<dt>-y, &#8211;anchor-prefix=&lt;str&gt;</p>
<dd> set anchor name prefix</p>
<dt>-N, &#8211;anchor-filename</p>
<dd> use input file name as anchor name</p>
<dt>-C, &#8211;print-index</p>
<dd> print index file with links to all output files</p>
<dt>-n, &#8211;ordered-list</p>
<dd> print lines as ordered list items</p>
<dt>&#8211;class-name=&lt;str&gt;</p>
<dd> set CSS class name prefix; omit class name if set to &quot;NONE&quot;</p>
<dt>&#8211;inline-css</p>
<dd> output CSS within each tag (verbose output)</p>
<dt>&#8211;enclose-pre</p>
<dd> enclose fragmented output with pre tag (assumes -f) </p>
</dl>
<h2>LaTeX OPTIONS</h2>
<dl>
<dt>-b, &#8211;babel</p>
<dd> disable Babel package shorthands</p>
<dt>-r, &#8211;replace-quotes</p>
<dd> replace double quotes by \dq</p>
<dt>&#8211;pretty-symbols</p>
<dd> improve appearance of brackets and other symbols </p>
</dl>
<h2>RTF OPTIONS</h2>
<dl>
<dt>-x, &#8211;page-size=&lt;size&gt;</p>
<dd> set page size, &lt;size&gt;=[a3, a4, a5, b4, b5, b6, letter]</p>
<dt>&#8211;char-styles</p>
<dd> include character stylesheets </p>
</dl>
<h2>SVG OPTIONS</h2>
<dl>
<dt>&#8211;height=&lt;h&gt;</p>
<dd> set image height (units allowed)</p>
<dt>&#8211;width=&lt;w&gt;</p>
<dd> set image size (see &#8211;height) </p>
</dl>
<h2>GNU SOURCE-HIGHLIGHT COMPATIBILITY OPTIONS</h2>
<dl>
<dt>&#8211;doc</p>
<dd> create stand alone document</p>
<dt>&#8211;no-doc</p>
<dd> cancel the &#8211;doc option</p>
<dt>&#8211;css=filename</p>
<dd> the external style sheet filename</p>
<dt>&#8211;src-lang=STRING</p>
<dd> source language</p>
<dt> -t, &#8211;tab=INT</p>
<dd> specify tab length</p>
<dt> -n, &#8211;line-number[=0]</p>
<dd> number all output lines, optional padding</p>
<dt>&#8211;line-number-ref[=p]</p>
<dd> number all output lines and generate an anchor, made of the specified prefix<br />
&nbsp;<wbr>p&nbsp;<wbr>+&nbsp;<wbr>the line number&nbsp;<wbr>&nbsp;<wbr>(default=&#8217;line&#8217;)</p>
<dt>&#8211;output-dir=path</p>
<dd>
&nbsp;<wbr>output directory</p>
<dt>&#8211;failsafe</p>
<dd> if no language definition is found for the input, it is simply copied to the output </p>
</dl>
<p> If no in- or output files are specified, stdin and stdout will be used for in- or output. HTML will be generated unless an other output format is given. Style definitions are stored in highlight.css (HTML, XHTML, SVG) or highlight.sty (LaTeX, TeX) if neither -c nor -I is given. Reformatting code (-F) will only work with C, C++, C# and Java input files.</p>
<h2>BUGS</h2>
<p> The wrapping options might cause faulty highlighting of multi line comments.</p>
<h2>FILES</h2>
<p> The parsing information of the programming languages is stored in <i>/usr/share/highlight/langDefs/.</i> You may enhance <code>highlight&#8217;s</code> parsing capabilities by adding more *.lang &#8211; files to this directory. You can also define other directories with &#8211;data-dir. Documentation files are stored in <i>/usr/share/doc/highlight/</i> , configuration files in <i>/etc/highlight/.</i> </p>
<h2>Examples</h2>
<p> Single file conversion: </p>
<p> highlight -o hello.html -i hello.c </p>
<p> highlight -o hello.html hello.c </p>
<p> highlight -o hello.html -S c &lt; hello.c </p>
<p> highlight -S c &lt; hello.c &gt; hello.html </p>
<p> Note that a file highlight.css is created in the current directory. </p>
<p> Batch file processing: </p>
<p> highlight &#8211;out-format=xhtml -B &#8216;*.cpp&#8217; -d /home/you/html_code/ </p>
<p> converts all *.cpp files in the current directory and its subdirectories to xhtml files, and stores the output in /home/you/html_code. </p>
<p> highlight &#8211;out-format=latex * -d /home/you/latex_code/ </p>
<p> converts all files to LaTeX, stored in /home/you/latex_code/. </p>
<p> Use &#8211;quiet to improve performance of batch file processing (recommended for usage in shell scripts). </p>
<p> Use highlight &#8211;out-format=xterm256 &lt;yourfile&gt; | less -R to display a source file in a terminal.</p>
<h2>AUTHORS</h2>
<p> Andre Simon &lt;as [at] andre-simon.de&gt;</p>
<h2>SEE ALSO</h2>
<p> README file and highlight webpage at <a rel="nofollow" href="http://www.andre-simon.de/.">http://www.andre-simon.de/.</a> </p>
<h2>Index</h2>
