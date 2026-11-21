---

title: "highlight(1)"
name: "highlight"
section: "1"
letter: "h"
url: "/docs/linux/man/1-highlight/"
description: "Highlight – a universal sourcecode to formatted text converter"
---

<p> <code>highlight</code> [OPTIONS]&#8230; [FILES]&#8230; </p>
<p> <code>Highlight</code> converts sourcecode to HTML, XHTML, RTF, ODT, LaTeX, TeX, BBCode, SVG, XTERM or ANSI escape sequences. There are several colour themes available. <code>Highlight</code> recognizes keywords, numbers, strings, comments, symbols and preprocessor directives. It supports about 160 programming languages, which are defined in Lua scripts. </p>
<p> It&#8217;s easily possible to enhance highlight&#8217;s database of programming languages and colour themes. See the README file for details.</p>
<h2>General options</h2>
<dl>
<dt>-B, &#8211;batch-recursive=&lt;wildcard&gt;</dt>
<dd> convert all files matching the wildcard (uses recursive search)</dd>
<dt>-D, &#8211;data-dir=&lt;path&gt;</dt>
<dd> set path to highlight data directory</dd>
<dt>&#8211;add-config-dir=&lt;path&gt;</dt>
<dd> set path to an additional configuration directory</dd>
<dt>&#8211;config-file=&lt;file&gt;</dt>
<dd> set path to a lang or theme file</dd>
<dt>-h, &#8211;help</dt>
<dd> print this help</dd>
<dt>-i, &#8211;input=&lt;file&gt;</dt>
<dd> name of input file</dd>
<dt>-o, &#8211;output=&lt;file&gt;</dt>
<dd> name of output file</dd>
<dt>-d, &#8211;outdir=&lt;output directory&gt;</dt>
<dd> name of output directory</dd>
<dt>-P, &#8211;progress</dt>
<dd> print progress bar in batch mode</dd>
<dt>-S, &#8211;syntax=&lt;type&gt;</dt>
<dd> set type of source code, necessary if input file suffix is missing</dd>
<dt>-v, &#8211;verbose</dt>
<dd> print debug info to stderr</dd>
<dt>-p, &#8211;list-langs</dt>
<dd> list installed language definitions</dd>
<dt>-q, &#8211;quiet</dt>
<dd> supress progress info in batch mode</dd>
<dt>-w, &#8211;list-themes</dt>
<dd> list installed themes</dd>
<dt>&#8211;force</dt>
<dd> generate output if input syntax is unknown</dd>
<dt>&#8211;plug-in=&lt;script&gt;</dt>
<dd> execute Lua plug-in script; repeat option to apply multiple plug-ins</dd>
<dt>&#8211;plug-in-read</dt>
<dd> set input file for a plug-in (e.g. &#8216;tags&#8217;)</dd>
<dt>&#8211;print-config</dt>
<dd> print path configuration</dd>
<dt>&#8211;print-style</dt>
<dd> print stylesheet only (see &#8211;style-outfile)</dd>
<dt>&#8211;skip=&lt;list&gt;</dt>
<dd> ignore listed unknown file types (Example: &#8211;skip=&#8217;bak;c~;h~&#8217;)</dd>
<dt>&#8211;start-nested=&lt;lang&gt;</dt>
<dd> define nested language which starts input without opening delimiter</dd>
<dt>&#8211;validate-input</dt>
<dd> test if input is a valid text file</dd>
<dt>&#8211;version</dt>
<dd> print version and copyright info </dd>
</dl>
<h2>Output formatting options</h2>
<dl>
<dt>-O, &#8211;out-format=&lt;format&gt;</dt>
<dd> output file in given format &lt;format&gt;=[html, xhtml, latex, tex, rtf, odt, ansi, xterm256, bbcode, svg]</dd>
<dt>-c, &#8211;style-outfile=&lt;file&gt;</dt>
<dd> name of style definition file or output to stdout, if &quot;stdout&quot; is given as file argument</dd>
<dt>-T, &#8211;doc-title</dt>
<dd> document title</dd>
<dt>-e, &#8211;style-infile=&lt;file&gt;</dt>
<dd> name of file to be included in style-outfile</dd>
<dt>-f, &#8211;fragment</dt>
<dd> omit header and footer of the output document</dd>
<dt>-F, &#8211;reformat=&lt;style&gt;</dt>
<dd> reformat output in given style. &lt;style&gt;=[allman, banner, gnu, java, kr, linux, stroustrup, whitesmith]</dd>
<dt>-I, &#8211;include-style</dt>
<dd> include style definition in output</dd>
<dt>-J, &#8211;line-length=&lt;num&gt;</dt>
<dd> line length before wrapping (see -W, -V)</dd>
<dt>-j, &#8211;line-number-length=&lt;num&gt;</dt>
<dd> line number length incl. left padding</dd>
<dt>-k, &#8211;font=&lt;font&gt;</dt>
<dd> set font (specific to output format)</dd>
<dt>-K, &#8211;font-size=&lt;num?&gt;</dt>
<dd> set font size (specific to output format)</dd>
<dt>-l, &#8211;line-numbers</dt>
<dd> print line numbers in output file</dd>
<dt>-m, &#8211;line-number-start=&lt;cnt&gt;</dt>
<dd> start line numbering with cnt (assumes -l)</dd>
<dt>-s, &#8211;style=&lt;style name&gt;</dt>
<dd> set highlighting style (see &#8211;list-themes)</dd>
<dt>-t &#8211;replace-tabs=&lt;num&gt;</dt>
<dd> replace tabs by num spaces</dd>
<dt>-u, &#8211;encoding=&lt;enc&gt;</dt>
<dd> set output encoding which matches input file encoding; omit encoding information if set to &quot;NONE&quot;</dd>
<dt>-V, &#8211;wrap-simple</dt>
<dd> wrap long lines without indenting function parameters and statements</dd>
<dt>-W, &#8211;wrap</dt>
<dd> wrap long lines (use with caution)</dd>
<dt>-z, &#8211;zeroes</dt>
<dd> fill leading space of line numbers with zeroes</dd>
<dt>&#8211;kw-case=&lt;upper|lower|capitalize&gt;</dt>
<dd> output all keywords in given case if language is not case sensitive</dd>
<dt>&#8211;delim-cr</dt>
<dd> set CR as end-of-line delimiter (MacOS 9)</dd>
<dt>&#8211;no-trailing-nl</dt>
<dd> omit trailing newline</dd>
<dt>&#8211;wrap-no-numbers</dt>
<dd> omit line numbers of wrapped lines (assumes -l) </dd>
</dl>
<h2>(X)HTML OPTIONS</h2>
<dl>
<dt>-a, &#8211;anchors</dt>
<dd> attach anchors to line numbers (HTML only)</dd>
<dt>-y, &#8211;anchor-prefix=&lt;str&gt;</dt>
<dd> set anchor name prefix</dd>
<dt>-N, &#8211;anchor-filename</dt>
<dd> use input file name as anchor name</dd>
<dt>-C, &#8211;print-index</dt>
<dd> print index file with links to all output files</dd>
<dt>-n, &#8211;ordered-list</dt>
<dd> print lines as ordered list items</dd>
<dt>&#8211;class-name=&lt;str&gt;</dt>
<dd> set CSS class name prefix; omit class name if set to &quot;NONE&quot;</dd>
<dt>&#8211;inline-css</dt>
<dd> output CSS within each tag (verbose output)</dd>
<dt>&#8211;enclose-pre</dt>
<dd> enclose fragmented output with pre tag (assumes -f) </dd>
</dl>
<h2>LaTeX OPTIONS</h2>
<dl>
<dt>-b, &#8211;babel</dt>
<dd> disable Babel package shorthands</dd>
<dt>-r, &#8211;replace-quotes</dt>
<dd> replace double quotes by \dq</dd>
<dt>&#8211;pretty-symbols</dt>
<dd> improve appearance of brackets and other symbols </dd>
</dl>
<h2>RTF OPTIONS</h2>
<dl>
<dt>-x, &#8211;page-size=&lt;size&gt;</dt>
<dd> set page size, &lt;size&gt;=[a3, a4, a5, b4, b5, b6, letter]</dd>
<dt>&#8211;char-styles</dt>
<dd> include character stylesheets </dd>
</dl>
<h2>SVG OPTIONS</h2>
<dl>
<dt>&#8211;height=&lt;h&gt;</dt>
<dd> set image height (units allowed)</dd>
<dt>&#8211;width=&lt;w&gt;</dt>
<dd> set image size (see &#8211;height) </dd>
</dl>
<h2>GNU SOURCE-HIGHLIGHT COMPATIBILITY OPTIONS</h2>
<dl>
<dt>&#8211;doc</dt>
<dd> create stand alone document</dd>
<dt>&#8211;no-doc</dt>
<dd> cancel the &#8211;doc option</dd>
<dt>&#8211;css=filename</dt>
<dd> the external style sheet filename</dd>
<dt>&#8211;src-lang=STRING</dt>
<dd> source language</dd>
<dt> -t, &#8211;tab=INT</dt>
<dd> specify tab length</dd>
<dt> -n, &#8211;line-number[=0]</dt>
<dd> number all output lines, optional padding</dd>
<dt>&#8211;line-number-ref[=p]</dt>
<dd> number all output lines and generate an anchor, made of the specified prefix<br />
&nbsp;<wbr>p&nbsp;<wbr>+&nbsp;<wbr>the line number&nbsp;<wbr>&nbsp;<wbr>(default=&#8217;line&#8217;)</dd>
<dt>&#8211;output-dir=path</dt>
<dd>
&nbsp;<wbr>output directory</dd>
<dt>&#8211;failsafe</dt>
<dd> if no language definition is found for the input, it is simply copied to the output </dd>
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
