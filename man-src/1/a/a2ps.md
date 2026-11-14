---
title: "a2ps(1)"
name: "a2ps"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a2ps/"
description: "a2ps – format files for printing on a PostScript printer"
---

<h2 class="name">NAME</h2>
<p> a2ps &#8211; format files for printing on a PostScript printer </p>
<h2>SYNOPSIS</h2>
<p> <code>a2ps</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Convert FILE(s) or standard input to PostScript. By default, the output is sent to the default printer. An output file may be specified with <code>-o</code>. </p>
<p> Mandatory arguments to long options are mandatory for short options too. Long options marked with * require a yes/no argument, corresponding short options stand for `yes&#8217;.</p>
<h3>Tasks:</h3>
<dl>
<dt><code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>&#8211;help</code></p>
<dd> display this help</p>
<dt><code>&#8211;guess</code></p>
<dd> report guessed types of FILES</p>
<dt><code>&#8211;which</code></p>
<dd> report the full path of library files named FILES</p>
<dt><code>&#8211;glob</code></p>
<dd> report the full path of library files matching FILES</p>
<dt><code>&#8211;list</code>=<i>defaults</i></p>
<dd> display default settings and parameters</p>
<dt><code>&#8211;list</code>=<i>TOPIC</i></p>
<dd> detailed list on TOPIC (delegations, encodings, features, variables, media, ppd, printers, prologues, style-sheets, user-options)</dl>
<p> After having performed the task, exit successfully. Detailed lists may provide additional help on specific features.</p>
<h3>Global:</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></p>
<dd> be really quiet</p>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>LEVEL</i>]</p>
<dd> set verbosity on, or to LEVEL</p>
<dt><code>-=</code>, <code>&#8211;user-option</code>=<i>OPTION</i></p>
<dd> use the user defined shortcut OPTION</p>
<dt><code>&#8211;debug</code></p>
<dd> enable debugging features</p>
<dt><code>-D</code>, <code>&#8211;define</code>=<i>KEY[</i>:VALUE]</p>
<dd> unset variable KEY or set to VALUE</dl>
<h3>Sheets:</h3>
<dl>
<dt><code>-M</code>, <code>&#8211;medium</code>=<i>NAME</i></p>
<dd> use output medium NAME</p>
<dt><code>-r</code>, <code>&#8211;landscape</code></p>
<dd> print in landscape mode</p>
<dt><code>-R</code>, <code>&#8211;portrait</code></p>
<dd> print in portrait mode</p>
<dt><code>&#8211;columns</code>=<i>NUM</i></p>
<dd> number of columns per sheet</p>
<dt><code>&#8211;rows</code>=<i>NUM</i></p>
<dd> number of rows per sheet</p>
<dt><code>&#8211;major</code>=<i>DIRECTION</i></p>
<dd> first fill (DIRECTION=) rows, or columns</p>
<dt><code>-1</code>, <code>-2</code>, &#8230;, <code>-9</code></p>
<dd> predefined font sizes and layouts for 1.. 9 virtuals</p>
<dt><code>-A</code>, <code>&#8211;file-align</code>=<i>MODE</i></p>
<dd> align separate files according to MODE (fill, rank page, sheet, or a number)</p>
<dt><code>-j</code>, <code>&#8211;borders</code>*</p>
<dd> print borders around columns</p>
<dt><code>&#8211;margin</code>[=<i>NUM</i>]</p>
<dd> define an interior margin of size NUM</dl>
<p> The options <code>-1</code>.. <code>-9</code> affect several primitive parameters to set up predefined layouts with 80 columns. Therefore the order matters: `-R <code>-f40</code> <code>-2</code>&#8216; is equivalent to `-2&#8242;. To modify the layout, use `-2Rf40&#8242;, or compose primitive options (`&#8211;columns&#8217;, `&#8211;font-size&#8217; etc.).</p>
<h3>Virtual pages:</h3>
<dl>
<dt><code>&#8211;line-numbers</code>=<i>NUM</i></p>
<dd> precede each NUM lines with its line number</p>
<dt><code>-C</code></p>
<dd> alias for <code>&#8211;line-numbers</code>=<i>5</i></p>
<dt><code>-f</code>, <code>&#8211;font-size</code>=<i>SIZE</i></p>
<dd> use font SIZE (float) for the body text</p>
<dt><code>-L</code>, <code>&#8211;lines-per-page</code>=<i>NUM</i></p>
<dd> scale the font to print NUM lines per virtual</p>
<dt><code>-l</code>, <code>&#8211;chars-per-line</code>=<i>NUM</i></p>
<dd> scale the font to print NUM columns per virtual</p>
<dt><code>-m</code>, <code>&#8211;catman</code></p>
<dd> process FILE as a man page (same as <code>-L66</code>)</p>
<dt><code>-T</code>, <code>&#8211;tabsize</code>=<i>NUM</i></p>
<dd> set tabulator size to NUM</p>
<dt> <code>&#8211;non-printable-format</code>=<i>FMT</i> specify how non-printable chars are printed</dl>
<h3>Headings:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;no-header</code></p>
<dd>
<dd>no page headers at all</p>
<dt><code>-b</code>, <code>&#8211;header</code>[=<i>TEXT</i>]</p>
<dd> set page header</p>
<dt><code>-u</code>, <code>&#8211;underlay</code>[=<i>TEXT</i>]</p>
<dd> print TEXT under every page</p>
<dt><code>&#8211;center-title</code>[=<i>TEXT</i>]</p>
<dd> set page title to TITLE</p>
<dt><code>&#8211;left-title</code>[=<i>TEXT</i>]</p>
<dd> set left and right page title to TEXT</p>
<dt> <code>&#8211;right-title</code>[=<i>TEXT</i>]</p>
<dt><code>&#8211;left-footer</code>[=<i>TEXT</i>]</p>
<dd>
<dd>set sheet footers to TEXT</p>
<dt> <code>&#8211;footer</code>[=<i>TEXT</i>]</p>
<dt> <code>&#8211;right-footer</code>[=<i>TEXT</i>]</dl>
<dd>The TEXTs may use special escapes.</p>
<h3>Input:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;pages</code>[=<i>RANGE</i>]</p>
<dd> select the pages to print</p>
<dt><code>-c</code>, <code>&#8211;truncate-lines</code>*</p>
<dd> cut long lines</p>
<dt><code>-i</code>, <code>&#8211;interpret</code>*</p>
<dd> interpret tab, bs and ff chars</p>
<dt><code>&#8211;end-of-line</code>=<i>TYPE</i></p>
<dd> specify the eol char (TYPE: r, n, nr, rn, any)</p>
<dt><code>-X</code>, <code>&#8211;encoding</code>=<i>NAME</i></p>
<dd> use input encoding NAME</p>
<dt><code>-t</code>, <code>&#8211;title</code>=<i>NAME</i></p>
<dd> set the name of the job</p>
<dt><code>&#8211;stdin</code>=<i>NAME</i></p>
<dd> set the name of the input file stdin</p>
<dt><code>&#8211;print-anyway</code>*</p>
<dd> force binary printing</p>
<dt><code>-Z</code>, <code>&#8211;delegate</code>*</p>
<dd> delegate files to another application</p>
<dt><code>&#8211;toc</code>[=<i>TEXT</i>]</p>
<dd> generate a table of content</dl>
<p> When delegations are enabled, a2ps may use other applications to handle the processing of files that should not be printed as raw information, e.g., HTML PostScript, PDF etc.</p>
<h3>Pretty-printing:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;pretty-print</code>[=<i>LANG</i>]</p>
<dd> enable pretty-printing (set style to LANG)</p>
<dt><code>&#8211;highlight-level</code>=<i>LEVEL</i></p>
<dd> set pretty printing highlight LEVEL LEVEL can be none, normal or heavy</p>
<dt><code>-g</code></p>
<dd> alias for <code>&#8211;highlight-level</code>=<i>heavy</i></p>
<dt><code>&#8211;strip-level</code>=<i>NUM</i></p>
<dd> level of comments stripping</dl>
<h3>Output:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> leave output to file FILE. If FILE is `-&#8216;, leave output to stdout.</p>
<dt><code>&#8211;version-control</code>=<i>WORD</i></p>
<dd> override the usual version control</p>
<dt><code>&#8211;suffix</code>=<i>SUFFIX</i></p>
<dd> override the usual backup suffix</p>
<dt><code>-P</code>, <code>&#8211;printer</code>=<i>NAME</i></p>
<dd> send output to printer NAME</p>
<dt><code>-d</code></p>
<dd> send output to the default printer (this is the default behavior)</dl>
<h3>PostScript:</h3>
<dl>
<dt><code>&#8211;prologue</code>=<i>FILE</i></p>
<dd> include FILE.pro as PostScript prologue</p>
<dt><code>&#8211;ppd</code>[=<i>KEY</i>]</p>
<dd> automatic PPD selection or set to KEY</p>
<dt><code>-n</code>, <code>&#8211;copies</code>=<i>NUM</i></p>
<dd> print NUM copies of each page</p>
<dt><code>-s</code>, <code>&#8211;sides</code>=<i>MODE</i></p>
<dd> set the duplex MODE (`1&#8242; or `simplex&#8217;, `2&#8242; or `duplex&#8217;, `tumble&#8217;)</p>
<dt><code>-S</code>, <code>&#8211;setpagedevice</code>=<i>K[</i>:V]</p>
<dd> pass a page device definition to output</p>
<dt><code>&#8211;statusdict</code>=<i>K[</i>:[:]V]</p>
<dd> pass a statusdict definition to the output</p>
<dt><code>-k</code>, <code>&#8211;page-prefeed</code></p>
<dd> enable page prefeed</p>
<dt><code>-K</code>, <code>&#8211;no-page-prefeed</code></p>
<dd> disable page prefeed</dl>
<p> By default a2ps is tuned to do what you want to, so trust it. To pretty print the content of the `src&#8217; directory and a table of content, and send the result to the printer `lw&#8217;,</p>
<dl>
<dt>
<dd> <tt>$ a2ps -P lw --toc src/*</tt></dl>
<p> To process the files `sample.ps&#8217; and `sample.html&#8217; and display the result,</p>
<dl>
<dt>
<dd> <tt>$ a2ps -P display sample.ps sample.html</tt></dl>
<p> To process a mailbox in 4 up,</p>
<dl>
<dt>
<dd> <tt>$ a2ps -=mail -4 mailbox</tt></dl>
<p> To print as a booklet on the default printer, which is Duplex capable,</p>
<dl>
<dt>
<dd> <tt>$ a2ps -=book paper.dvi.gz -d</tt></dl>
<p> News, updates and documentation: visit <a rel="nofollow" href="http://www.gnu.org/software/a2ps/.">http://www.gnu.org/software/a2ps/.</a></p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille, Miguel Santana.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-a2ps [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1988-1993 Miguel Santana<br />
 Copyright &#169; 1995-2000 Akim Demaille, Miguel Santana<br />
 Copyright &#169; 2007- Akim Demaille, Miguel Santana and Masayuki Hatta<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-a2ps/">a2ps</a></code>(1), <code><a href="/docs/linux/man/1-card/">card</a></code>(1), <code><a href="/docs/linux/man/1-fixps/">fixps</a></code>(1), <code><a href="/docs/linux/man/1-pdiff/">pdiff</a></code>(1), <code><a href="/docs/linux/man/1-psset/">psset</a></code>(1), <code><a href="/docs/linux/man/1-texi2dvi4a2ps/">texi2dvi4a2ps</a></code>(1). </p>
<p> The full documentation for <code>a2ps</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>a2ps</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info a2ps</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
