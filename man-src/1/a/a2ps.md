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
<dt><code>&#8211;version</code></dt>
<dd> display version</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help</dd>
<dt><code>&#8211;guess</code></dt>
<dd> report guessed types of FILES</dd>
<dt><code>&#8211;which</code></dt>
<dd> report the full path of library files named FILES</dd>
<dt><code>&#8211;glob</code></dt>
<dd> report the full path of library files matching FILES</dd>
<dt><code>&#8211;list</code>=<i>defaults</i></dt>
<dd> display default settings and parameters</dd>
<dt><code>&#8211;list</code>=<i>TOPIC</i></dt>
<dd> detailed list on TOPIC (delegations, encodings, features, variables, media, ppd, printers, prologues, style-sheets, user-options)</dd></dl>
<p> After having performed the task, exit successfully. Detailed lists may provide additional help on specific features.</p>
<h3>Global:</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code>, <code>&#8211;silent</code></dt>
<dd> be really quiet</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>LEVEL</i>]</dt>
<dd> set verbosity on, or to LEVEL</dd>
<dt><code>-=</code>, <code>&#8211;user-option</code>=<i>OPTION</i></dt>
<dd> use the user defined shortcut OPTION</dd>
<dt><code>&#8211;debug</code></dt>
<dd> enable debugging features</dd>
<dt><code>-D</code>, <code>&#8211;define</code>=<i>KEY[</i>:VALUE]</dt>
<dd> unset variable KEY or set to VALUE</dd></dl>
<h3>Sheets:</h3>
<dl>
<dt><code>-M</code>, <code>&#8211;medium</code>=<i>NAME</i></dt>
<dd> use output medium NAME</dd>
<dt><code>-r</code>, <code>&#8211;landscape</code></dt>
<dd> print in landscape mode</dd>
<dt><code>-R</code>, <code>&#8211;portrait</code></dt>
<dd> print in portrait mode</dd>
<dt><code>&#8211;columns</code>=<i>NUM</i></dt>
<dd> number of columns per sheet</dd>
<dt><code>&#8211;rows</code>=<i>NUM</i></dt>
<dd> number of rows per sheet</dd>
<dt><code>&#8211;major</code>=<i>DIRECTION</i></dt>
<dd> first fill (DIRECTION=) rows, or columns</dd>
<dt><code>-1</code>, <code>-2</code>, &#8230;, <code>-9</code></dt>
<dd> predefined font sizes and layouts for 1.. 9 virtuals</dd>
<dt><code>-A</code>, <code>&#8211;file-align</code>=<i>MODE</i></dt>
<dd> align separate files according to MODE (fill, rank page, sheet, or a number)</dd>
<dt><code>-j</code>, <code>&#8211;borders</code>*</dt>
<dd> print borders around columns</dd>
<dt><code>&#8211;margin</code>[=<i>NUM</i>]</dt>
<dd> define an interior margin of size NUM</dd></dl>
<p> The options <code>-1</code>.. <code>-9</code> affect several primitive parameters to set up predefined layouts with 80 columns. Therefore the order matters: `-R <code>-f40</code> <code>-2</code>&#8216; is equivalent to `-2&#8242;. To modify the layout, use `-2Rf40&#8242;, or compose primitive options (`&#8211;columns&#8217;, `&#8211;font-size&#8217; etc.).</p>
<h3>Virtual pages:</h3>
<dl>
<dt><code>&#8211;line-numbers</code>=<i>NUM</i></dt>
<dd> precede each NUM lines with its line number</dd>
<dt><code>-C</code></dt>
<dd> alias for <code>&#8211;line-numbers</code>=<i>5</i></dd>
<dt><code>-f</code>, <code>&#8211;font-size</code>=<i>SIZE</i></dt>
<dd> use font SIZE (float) for the body text</dd>
<dt><code>-L</code>, <code>&#8211;lines-per-page</code>=<i>NUM</i></dt>
<dd> scale the font to print NUM lines per virtual</dd>
<dt><code>-l</code>, <code>&#8211;chars-per-line</code>=<i>NUM</i></dt>
<dd> scale the font to print NUM columns per virtual</dd>
<dt><code>-m</code>, <code>&#8211;catman</code></dt>
<dd> process FILE as a man page (same as <code>-L66</code>)</dd>
<dt><code>-T</code>, <code>&#8211;tabsize</code>=<i>NUM</i></dt>
<dd> set tabulator size to NUM</dd>
<dt> <code>&#8211;non-printable-format</code>=<i>FMT</i> specify how non-printable chars are printed</dt></dl>
<h3>Headings:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;no-header</code></dt>
<dd>
</dd><dd>no page headers at all</dd>
<dt><code>-b</code>, <code>&#8211;header</code>[=<i>TEXT</i>]</dt>
<dd> set page header</dd>
<dt><code>-u</code>, <code>&#8211;underlay</code>[=<i>TEXT</i>]</dt>
<dd> print TEXT under every page</dd>
<dt><code>&#8211;center-title</code>[=<i>TEXT</i>]</dt>
<dd> set page title to TITLE</dd>
<dt><code>&#8211;left-title</code>[=<i>TEXT</i>]</dt>
<dd> set left and right page title to TEXT</dd>
<dt> <code>&#8211;right-title</code>[=<i>TEXT</i>]</dt>
<dt><code>&#8211;left-footer</code>[=<i>TEXT</i>]</dt>
<dd>
</dd><dd>set sheet footers to TEXT</dd>
<dt> <code>&#8211;footer</code>[=<i>TEXT</i>]</dt>
<dt> <code>&#8211;right-footer</code>[=<i>TEXT</i>]</dt></dl>
<dd>The TEXTs may use special escapes.</dd>
<h3>Input:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;pages</code>[=<i>RANGE</i>]</dt>
<dd> select the pages to print</dd>
<dt><code>-c</code>, <code>&#8211;truncate-lines</code>*</dt>
<dd> cut long lines</dd>
<dt><code>-i</code>, <code>&#8211;interpret</code>*</dt>
<dd> interpret tab, bs and ff chars</dd>
<dt><code>&#8211;end-of-line</code>=<i>TYPE</i></dt>
<dd> specify the eol char (TYPE: r, n, nr, rn, any)</dd>
<dt><code>-X</code>, <code>&#8211;encoding</code>=<i>NAME</i></dt>
<dd> use input encoding NAME</dd>
<dt><code>-t</code>, <code>&#8211;title</code>=<i>NAME</i></dt>
<dd> set the name of the job</dd>
<dt><code>&#8211;stdin</code>=<i>NAME</i></dt>
<dd> set the name of the input file stdin</dd>
<dt><code>&#8211;print-anyway</code>*</dt>
<dd> force binary printing</dd>
<dt><code>-Z</code>, <code>&#8211;delegate</code>*</dt>
<dd> delegate files to another application</dd>
<dt><code>&#8211;toc</code>[=<i>TEXT</i>]</dt>
<dd> generate a table of content</dd></dl>
<p> When delegations are enabled, a2ps may use other applications to handle the processing of files that should not be printed as raw information, e.g., HTML PostScript, PDF etc.</p>
<h3>Pretty-printing:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;pretty-print</code>[=<i>LANG</i>]</dt>
<dd> enable pretty-printing (set style to LANG)</dd>
<dt><code>&#8211;highlight-level</code>=<i>LEVEL</i></dt>
<dd> set pretty printing highlight LEVEL LEVEL can be none, normal or heavy</dd>
<dt><code>-g</code></dt>
<dd> alias for <code>&#8211;highlight-level</code>=<i>heavy</i></dd>
<dt><code>&#8211;strip-level</code>=<i>NUM</i></dt>
<dd> level of comments stripping</dd></dl>
<h3>Output:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> leave output to file FILE. If FILE is `-&#8216;, leave output to stdout.</dd>
<dt><code>&#8211;version-control</code>=<i>WORD</i></dt>
<dd> override the usual version control</dd>
<dt><code>&#8211;suffix</code>=<i>SUFFIX</i></dt>
<dd> override the usual backup suffix</dd>
<dt><code>-P</code>, <code>&#8211;printer</code>=<i>NAME</i></dt>
<dd> send output to printer NAME</dd>
<dt><code>-d</code></dt>
<dd> send output to the default printer (this is the default behavior)</dd></dl>
<h3>PostScript:</h3>
<dl>
<dt><code>&#8211;prologue</code>=<i>FILE</i></dt>
<dd> include FILE.pro as PostScript prologue</dd>
<dt><code>&#8211;ppd</code>[=<i>KEY</i>]</dt>
<dd> automatic PPD selection or set to KEY</dd>
<dt><code>-n</code>, <code>&#8211;copies</code>=<i>NUM</i></dt>
<dd> print NUM copies of each page</dd>
<dt><code>-s</code>, <code>&#8211;sides</code>=<i>MODE</i></dt>
<dd> set the duplex MODE (`1&#8242; or `simplex&#8217;, `2&#8242; or `duplex&#8217;, `tumble&#8217;)</dd>
<dt><code>-S</code>, <code>&#8211;setpagedevice</code>=<i>K[</i>:V]</dt>
<dd> pass a page device definition to output</dd>
<dt><code>&#8211;statusdict</code>=<i>K[</i>:[:]V]</dt>
<dd> pass a statusdict definition to the output</dd>
<dt><code>-k</code>, <code>&#8211;page-prefeed</code></dt>
<dd> enable page prefeed</dd>
<dt><code>-K</code>, <code>&#8211;no-page-prefeed</code></dt>
<dd> disable page prefeed</dd></dl>
<p> By default a2ps is tuned to do what you want to, so trust it. To pretty print the content of the `src&#8217; directory and a table of content, and send the result to the printer `lw&#8217;,</p>
<dl>
<dt>
</dt><dd> <tt>$ a2ps -P lw --toc src/*</tt></dd></dl>
<p> To process the files `sample.ps&#8217; and `sample.html&#8217; and display the result,</p>
<dl>
<dt>
</dt><dd> <tt>$ a2ps -P display sample.ps sample.html</tt></dd></dl>
<p> To process a mailbox in 4 up,</p>
<dl>
<dt>
</dt><dd> <tt>$ a2ps -=mail -4 mailbox</tt></dd></dl>
<p> To print as a booklet on the default printer, which is Duplex capable,</p>
<dl>
<dt>
</dt><dd> <tt>$ a2ps -=book paper.dvi.gz -d</tt></dd></dl>
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
</dt><dd> <code>info a2ps</code></dd></dl>
<p> should give you access to the complete manual. </p>
