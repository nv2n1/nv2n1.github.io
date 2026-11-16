---
title: "enscript(1)"
name: "enscript"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enscript/"
description: "enscript – convert text files to PostScript, HTML, RTF, ANSI, and overstrikes"
---

<h2 class="name">NAME</h2>
<p> enscript &#8211; convert text files to PostScript, HTML, RTF, ANSI, and overstrikes</p>
<h2>SYNOPSIS</h2>
<p> <code>enscript</code> [<code>-123456789BcgGhjkKlmOqrRvVzZ</code>] [<code>-# </code><i>copies</i>] [<code>-a </code><i>pages</i>] [<code>-A </code><i>align</i>] [<code>-b </code><i>header</i>] [<code>-C</code>[<i>start_line</i>]] [<code>-d </code><i>printer</i>] [<code>-D </code><i>key</i>[<code>:</code><i>value</i>]] [<code>-e</code>[<i>char</i>]] [<code>-E</code>[<i>lang</i>]] [<code>-f </code><i>font</i>] [<code>-F </code><i>header_font</i>] [<code>-H</code>[<i>num</i>]] [<code>-i </code><i>indent</i>] [<code>-I </code><i>filter</i>] [<code>-J </code><i>title</i>] [<code>-L </code><i>lines_per_page</i>] [<code>-M </code><i>media</i>] [<code>-n </code><i>copies</i>] [<code>-N </code><i>newline</i>] [<code>-o </code><i>outputfile</i>] [<code>-o &#8211;</code>] [<code>-p </code><i>outputfile</i>] [<code>-p &#8211;</code>] [<code>-P </code><i>printer</i>] [<code>-s </code><i>baselineskip</i>] [<code>-S </code><i>key</i>[<code>:</code><i>value</i>]] [<code>-t </code><i>title</i>] [<code>-T </code><i>tabsize</i>] [<code>-u</code>[<i>text</i>]] [<code>-U </code><i>num</i>] [<code>-w </code><i>language</i>] [<code>-X </code><i>encoding</i>] [<i>filename</i> &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>Enscript</code> converts text files to PostScript or to other output languages. <code>Enscript</code> can spool the generated output directly to a specified printer or leave it to a file. If no input files are given, <code>enscript</code> processes the standard input <code>stdin</code>. <code>Enscript</code> can be extended to handle different output media and it has many options which can be used to customize the printouts. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-# </code><i>num</i></dt>
<dd> Print <i>num</i> copies of each page.</dd>
<dt><code>-1, -2, -3, -4, -5, -6, -7, -8, -9, &#8211;columns=</code><i>num</i></dt>
<dd> Specify how many columns each page have. With the long option <code>&#8211;columns=</code><i>num</i> you can specify more than 9 columns per page.</dd>
<dt><code>-a </code><i>pages</i><code>, &#8211;pages=</code><i>pages</i></dt>
<dd> Specify which pages are printed. The page specification <i>pages</i> can be given in the following formats:</dd>
<dl>
<dl>
<dt><i>begin</i>&#8211;<i>end</i></dt>
<dd> print pages from <i>begin</i> to <i>end</i></dd>
<dt>&#8211;<i>end</i></dt>
<dd> print pages from 0 to <i>end</i></dd>
<dt><i>begin</i>&#8211;</dt>
<dd> print pages from <i>begin</i> to end</dd>
<dt><i>page</i></dt>
<dd> print page <i>page</i></dd>
<dt>odd</dt>
<dd> print odd pages</dd>
<dt>even</dt>
<dd> print even pages</dd></dl>
</dl>
<dt><code>-A </code><i>align</i><code>, &#8211;file-align=</code><i>align</i></dt>
<dd> Align separate input files to even <i>align</i> page count. This option is useful in two-side and 2-up printings (&#8211;file-align=2).</dd>
<dt><code>-b </code><i>header</i><code>, &#8211;header=</code><i>header</i></dt>
<dd> Use the text <i>header</i> as a page header. The default page header is constructed from the name of the file and from its last modification time. </dd>
<p> The header string <i>header</i> can contain the same formatting escapes which can be specified for the <code>%Format</code> directives in the user defined fancy headers. For example, the following option prints the file name, current date and page numbers: </p>
<p> <code>enscript &#8211;header=&#8217;$n %W Page $% of $=&#8217; *.c</code> </p>
<p> The header string can also contain left, center and right justified fields. The fields are separated by the <code>&#8216;|&#8217;</code> character: </p>
<p> <code>enscript &#8211;header=&#8217;$n|%W|Page $% of $=&#8217; *.c</code> </p>
<p> now the file name is printed left justified, the date is centered to the header and the page numbers are printed right justified.</p>
<dt><code>-B, &#8211;no-header</code></dt>
<dd> Do not print page headers.</dd>
<dt><code>-c, &#8211;truncate-lines</code></dt>
<dd> Cut lines that are too long for the page. As a default, <code>enscript</code> wraps long lines to the next line so no information is lost. </dd>
<p> You can also use the <code>&#8211;slice</code> option which slices long lines to separate pages.</p>
<dt><code>-C</code>[<i>start_line</i>]<code>, &#8211;line-numbers</code>[<code>=</code><i>start_line</i>]</dt>
<dd> Precede each line with its line number. The optional argument <i>start_line</i> specifies the number of the first line in the input. The number of the first line defaults to 1.</dd>
<dt><code>-d </code><i>name</i></dt>
<dd> Spool output to the printer <i>name</i>.</dd>
<dt><code>-D </code><i>key</i>[<code>:</code><i>value</i>]<code>, &#8211;setpagedevice=</code><i>key</i>[<code>:</code><i>value</i>]</dt>
<dd> Pass a page device definition to the generated PostScript output. If no value is given, the key <i>key</i> is removed from the definitions. </dd>
<p> For example, the command </p>
<p> <code>enscript -DDuplex:true foo.txt</code> </p>
<p> prints file foo.txt in duplex (two side) mode. </p>
<p> Page device operators are implementation dependent but they are standardized. See section <code>PAGE DEVICE OPTIONS</code> for the details.</p>
<dt><code>-e</code>[<i>char</i>]<code>, &#8211;escapes</code>[<code>=</code><i>char</i>]</dt>
<dd> Enable special escapes interpretation (see section <code>SPECIAL ESCAPES</code>). If the argument <i>char</i> is given, it changes the escape character to <i>char</i>. The default escape character is 0.</dd>
<dt><code>-E</code>[<i>lang</i>]<code>, &#8211;highlight</code>[<code>=</code><i>lang</i>]</dt>
<dd> Highlight source code by creating a special input filter with the <code>states</code> program. The optional argument <i>lang</i> specifies the language to highlight. As a default the <code>states</code> makes an educated guess. </dd>
<p> You can print a short description of the supported highlighting languages and file formats with the command: </p>
<p> <code>enscript &#8211;help-highlight</code> </p>
<p> The highlighting rules are defined in the `/usr/share/enscript/hl/*.st&#8217; files which can be edited to create highlighting definitions for new languages. </p>
<p> <code>Note!</code> You can not use your own input filters with this option.</p>
<dt><code>-f </code><i>name</i><code>, &#8211;font=</code><i>name</i></dt>
<dd> Select a font that is used for the body text. The default body font is <code>Courier10</code>, unless multicolumn landscape printing mode is selected, in which case the default font is <code>Courier7</code>. </dd>
<p> The font specification <i>name</i> contains two parts: the name of the font and its size in PostScript points. For example, &quot;<code>Times-Roman12</code>&quot; selects the &quot;Times-Roman&quot; font with size 12pt. </p>
<p> The font specification <i>name</i> can also be given in format `<i>name</i>@<i>ptsize</i>&#8216;, where the name of the font and its point size are separated by a `@&#8217; character. This allows <code>enscript</code> to use fonts which contain digit characters in their names. </p>
<p> The font point size can also be given in the format <i>width</i>/<i>height</i> where the <i>width</i> and the <i>height</i> specify the size of the font in x- and y-directions. For example, &quot;<code>Times-Roman@10/12</code>&quot; selects a 10 points wide and 12 points high &quot;Times-Roman&quot; font. </p>
<p> You can also give the font sizes as decimal numbers. For example, &quot;<code>Times-Roman10.2</code>&quot; selects a 10.2pt &quot;Times-Roman&quot; font.</p>
<dt><code>-F </code><i>name</i><code>, &#8211;header-font=</code><i>name</i></dt>
<dd> Select a font for the header texts.</dd>
<dt><code>-g, &#8211;print-anyway</code></dt>
<dd> Print a file even if it contains binary data. The option is implemented only for compatibility purposes. <code>Enscript</code> prints binary files anyway regardless of the option.</dd>
<dt><code>-G, &#8211;fancy-header</code>[<code>=</code><i>name</i>]</dt>
<dd> Print a fancy page header <i>name</i> to the top of each page. The option <code>-G</code> specifies the default fancy header. See section <code>CONFIGURATION FILES</code> to see how the default fancy header can be changed.</dd>
<dt><code>-h, &#8211;no-job-header</code></dt>
<dd> Suppress printing of the job header page.</dd>
<dt><code>-H</code>[<i>num</i>]<code>, &#8211;highlight-bars</code>[<code>=</code><i>num</i>]</dt>
<dd> Specify how high the highlight bars are in lines. If the <i>num</i> is not given, the default value 2 is used. As a default, no highlight bars are printed.</dd>
<dt><code>-i </code><i>num</i><code>, &#8211;indent=</code><i>num</i></dt>
<dd> Indent every line <i>num</i> characters. The indentation can also be specified in other units by appending an unit specifier after the number. The possible unit specifiers and the corresponding units are:</dd>
<dl>
<dl>
<dt><code>c</code></dt>
<dd> centimeters</dd>
<dt><code>i</code></dt>
<dd> inches</dd>
<dt><code>l</code></dt>
<dd> characters (default)</dd>
<dt><code>p</code></dt>
<dd> PostScript points</dd></dl>
</dl>
<dt><code>-I </code><i>filter</i><code>, &#8211;filter=</code><i>filter</i></dt>
<dd> Read all input files through an input filter <i>filter</i>. The input filter can be a single command or a command pipeline. The filter can refer to the name of the input file with the escape `<code>%s</code>&#8216;. The name of the standard input can be changed with the option `<code>&#8211;filter-stdin</code>&#8216;. </dd>
<p> For example, the following command prints the file `foo.c&#8217; by using only upper-case characters: </p>
<p> <code>enscript &#8211;filter=cat %s | tr &#8216;a-z&#8217; &#8216;A-Z&#8217; foo.c</code> </p>
<p> The following command highlights changes which are made to files since the last checkout: </p>
<p> <code>enscript &#8211;filter=rcsdiff %s | diffpp %s -e *.c</code> </p>
<p> To include the string &quot;%s&quot; to the filter command, you must write it as &quot;%%s&quot;.</p>
<dt><code>-j, &#8211;borders</code></dt>
<dd> Print borders around columns.</dd>
<dt><code>-J </code><i>title</i></dt>
<dd> An alias for the option <code>-t</code>, <code>&#8211;title</code>.</dd>
<dt><code>-k, &#8211;page-prefeed</code></dt>
<dd> Enable page prefeed.</dd>
<dt><code>-K, &#8211;no-page-prefeed</code></dt>
<dd> Disable page prefeed (default).</dd>
<dt><code>-l, &#8211;lineprinter</code></dt>
<dd> Emulate lineprinter. This option is a shortcut for the options <code>&#8211;lines-per-page=66</code>, and <code>&#8211;no-header</code>.</dd>
<dt><code>-L </code><i>num</i><code>, &#8211;lines-per-page=</code><i>num</i></dt>
<dd> Print only <i>num</i> lines for each page. As a default, the number of lines per page is computed from the height of the page and from the size of the font.</dd>
<dt><code>-m, &#8211;mail</code></dt>
<dd> Send a mail notification to user after the print job has been completed.</dd>
<dt><code>-M </code><i>name</i><code>, &#8211;media=</code><i>name</i></dt>
<dd> Select an output media <i>name</i>. <code>Enscript</code>&#8216;s default output media is determined from libpaper and falls back to <code>A4</code>.</dd>
<dt><code>-n </code><i>num</i><code>, &#8211;copies=</code><i>num</i></dt>
<dd> Print <i>num</i> copies of each page.</dd>
<dt><code>-N </code><i>nl</i><code>, &#8211;newline=</code><i>nl</i></dt>
<dd> Select the <i>newline</i> character. The possible values for <i>nl</i> are: <code>n</code> (unix newline, 0xa hex) and <code>r</code> (mac newline, 0xd hex).</dd>
<dt><code>-o </code><i>file</i></dt>
<dd> An alias for the option <code>-p</code>, <code>&#8211;output</code>.</dd>
<dt><code>-O, &#8211;missing-characters</code></dt>
<dd> Print a listing of character codes which couldn&#8217;t be printed.</dd>
<dt><code>-p </code><i>file</i><code>, &#8211;output=</code><i>file</i></dt>
<dd> Leave the output to file <i>file</i>. If the <i>file</i> is `-&#8216;, enscript sends the output to the standard output <code>stdout</code>.</dd>
<dt><code>-P </code><i>name</i><code>, &#8211;printer=</code><i>name</i></dt>
<dd> Spool the output to the printer <i>name</i>.</dd>
<dt><code>-q, &#8211;quiet, &#8211;silent</code></dt>
<dd> Make <code>enscript</code> really quiet. Only fatal error messages are printed to <i>stderr</i>.</dd>
<dt><code>-r, &#8211;landscape</code></dt>
<dd> Print in the landscape mode; rotate page 90 degrees.</dd>
<dt><code>-R, &#8211;portrait</code></dt>
<dd> Print in the portrait mode (default).</dd>
<dt><code>-s </code><i>num</i><code>, &#8211;baselineskip=</code><i>num</i></dt>
<dd> Specify the baseline skip in PostScript points. The number <i>num</i> can be given as a decimal number. When <code>enscript</code> moves from line to line, the current point <i>y</i> coordinate is moved (<i>font point size + baselineskip</i>) points down. The default baseline skip is 1.</dd>
<dt><code>-S </code><i>key</i>[<code>:</code><i>value</i>]<code>, &#8211;statusdict=</code><i>key</i>[<code>:</code><i>value</i>]</dt>
<dd> Pass a statusdict definition to the generated PostScript output. If no value is given, the key <i>key</i> is removed from the definitions. </dd>
<p> The statusdict operators are implementation dependent; see the printer&#8217;s documentation for the details. </p>
<p> For example, the command </p>
<p> <code>enscript -Ssetpapertray:1 foo.txt</code> </p>
<p> prints the file <i>foo.txt</i> by using paper from the paper tray 1 (assuming that the printer supports paper tray selection).</p>
<dt><code>-t </code><i>title</i><code>, &#8211;title=</code><i>title</i></dt>
<dd> Set banner page&#8217;s job title to <i>title</i>. The option sets also the name of the input file <code>stdin</code>.</dd>
<dt><code>-T </code><i>num</i><code>, &#8211;tabsize=</code><i>num</i></dt>
<dd> Set the tabulator size to <i>num</i> characters. The default is 8.</dd>
<dt><code>-u</code>[<i>text</i>]<code>, &#8211;underlay</code>[<code>=</code><i>text</i>]</dt>
<dd> Print the string <i>text</i> under every page. The properties of the text can be changed with the options <code>&#8211;ul-angle</code>, <code>&#8211;ul-font</code>, <code>&#8211;ul-gray</code>, <code>&#8211;ul-position</code>, and <code>&#8211;ul-style</code>. </dd>
<p> If no <i>text</i> is given, the underlay is not printed. This can be used to remove an underlay text that was specified with the `<code>Underlay</code>&#8216; configuration file option.</p>
<dt><code>-U </code><i>num</i><code>, &#8211;nup=</code><i>num</i></dt>
<dd> Print <i>num</i> logical pages on each output page (N-up printing). The values <i>num</i> must be a power of 2.</dd>
<dt><code>-v, &#8211;verbose</code>[<code>=</code><i>level</i>]</dt>
<dd> Tell what <code>enscript</code> is doing.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print <code>enscript</code> version information and exit.</dd>
<dt><code>-w </code>[<i>lang</i>]<code>, &#8211;language</code>[<code>=</code><i>lang</i>]</dt>
<dd> Generate output for the language <i>lang</i>. The possible values for <i>lang</i> are:</dd>
<dl>
<dl>
<dt><code>PostScript</code></dt>
<dd> generate PostScript (default)</dd>
<dt><code>html</code></dt>
<dd> generate HTML</dd>
<dt><code>overstrike</code></dt>
<dd> generate overstrikes (line printers, less)</dd>
<dt><code>rtf</code></dt>
<dd> generate RTF (Rich Text Format)</dd>
<dt><code>ansi</code></dt>
<dd> generate ANSI terminal control codes</dd></dl>
</dl>
<dt><code>-X </code><i>name</i><code>, &#8211;encoding=</code><i>name</i></dt>
<dd> Use the input encoding <i>name</i>. Currently <code>enscript</code> supports the following encodings:</dd>
<dl>
<dl>
<dt><code>88591, latin1</code></dt>
<dd> ISO-8859-1 (ISO Latin1) (<code>enscript</code>&#8216;s default encoding).</dd>
<dt><code>88592, latin2</code></dt>
<dd> ISO-8859-2 (ISO Latin2)</dd>
<dt><code>88593, latin3</code></dt>
<dd> ISO-8859-3 (ISO Latin3)</dd>
<dt><code>88594, latin4</code></dt>
<dd> ISO-8859-4 (ISO Latin4)</dd>
<dt><code>88595, cyrillic</code></dt>
<dd> ISO-8859-5 (ISO Cyrillic)</dd>
<dt><code>88597, greek</code></dt>
<dd> ISO-8859-7 (ISO Greek)</dd>
<dt><code>88599, latin5</code></dt>
<dd> ISO-8859-9 (ISO Latin5)</dd>
<dt><code>885910, latin6</code></dt>
<dd> ISO-8859-10 (ISO Latin6)</dd>
<dt><code>ascii</code></dt>
<dd> 7-bit ascii</dd>
<dt><code>asciifise, asciifi, asciise</code></dt>
<dd> 7-bit ascii with some scandinavian (Finland, Sweden) extensions</dd>
<dt><code>asciidkno, asciidk, asciino</code></dt>
<dd> 7-bit ascii with some scandinavian (Denmark, Norway) extensions</dd>
<dt><code>ibmpc, pc, dos</code></dt>
<dd> IBM PC charset</dd>
<dt><code>mac</code></dt>
<dd> Mac charset</dd>
<dt><code>vms</code></dt>
<dd> VMS multinational charset</dd>
<dt><code>hp8</code></dt>
<dd> HP Roman-8 charset</dd>
<dt><code>koi8</code></dt>
<dd> Adobe Standard Cyrillic Font KOI8 charset</dd>
<dt><code>ps, PS</code></dt>
<dd> PostScript font&#8217;s default encoding</dd>
<dt><code>pslatin1, ISOLatin1Encoding</code></dt>
<dd> PostScript interpreter&#8217;s `ISOLatin1Encoding&#8217;</dd></dl>
</dl>
<dt><code>-z, &#8211;no-formfeed</code></dt>
<dd> Turn off the form feed character interpretation.</dd>
<dt><code>-Z, &#8211;pass-through</code></dt>
<dd> Pass through all PostScript and PCL files without any modifications. This allows that <code>enscript</code> can be used as a lp filter. </dd>
<p> The PostScript files are recognized by looking up the `%!&#8217; magic cookie from the beginning of the file. <code>Note!</code> <code>Enscript</code> recognized also the Windoze damaged `^D%!&#8217; cookie. </p>
<p> The PCL files are recognized by looking up the `^[E&#8217; or `^[%&#8217; magic cookies from the beginning of the file.</p>
<dt><code>&#8211;color</code>[<code>=</code><i>bool</i>]</dt>
<dd> Use colors in the highlighting outputs.</dd>
<dt><code>&#8211;download-font=</code><i>fontname</i></dt>
<dd> Include the font description file (<i>.pfa</i> or <i>.pfb</i> file) of the font <i>fontname</i> to the generated output.</dd>
<dt><code>&#8211;extended-return-values</code></dt>
<dd> Enable extended return values. As a default, <code>enscript</code> returns 1 on error and 0 otherwise. The extended return values give more details about the printing operation. See the section <code>RETURN VALUE</code> for the details.</dd>
<dt><code>&#8211;filter-stdin=</code><i>name</i></dt>
<dd> Specify how the <code>stdin</code> is shown to the input filter. The default value is an empty string (&quot;&quot;) but some programs require that the <code>stdin</code> is called something else, usually &quot;-&quot;.</dd>
<dt><code>&#8211;footer=</code><i>footer</i></dt>
<dd> Use the text <i>footer</i> as a page footer. Otherwise the option works like the <code>&#8211;header</code> option</dd>
<dt><code>&#8211;h-column-height=</code><i>height</i></dt>
<dd> Set the horizontal column height to be <i>height</i> PostScript points. The option sets the formfeed type to <code>horizontal-columns</code>.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print a short help message and exit.</dd>
<dt><code>&#8211;help-highlight</code></dt>
<dd> Describe all supported <code>&#8211;highlight</code> languages and file formats.</dd>
<dt><code>&#8211;highlight-bar-gray=</code><i>gray</i></dt>
<dd> Specify the gray level which is used in printing the highlight bars.</dd>
<dt><code>&#8211;list-media</code></dt>
<dd> List the names of all known output media and exit successfully.</dd>
<dt><code>&#8211;margins=</code><i>left</i><code>:</code><i>right</i><code>:</code><i>top</i><code>:</code><i>bottom</i></dt>
<dd> Adjust the page marginals to be exactly <i>left</i>, <i>right</i>, <i>top</i> and <i>bottom</i> PostScript points. Any of the arguments can be left empty in which case the default value is used.</dd>
<dt><code>&#8211;mark-wrapped-lines</code>[<code>=</code><i>style</i>]</dt>
<dd> Mark wrapped lines in the output with the style <i>style</i>. The possible values for the <i>style</i> are:</dd>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> do not mark them (default)</dd>
<dt><code>plus</code></dt>
<dd> print a plus (+) character to the end of each wrapped line</dd>
<dt><code>box</code></dt>
<dd> print a black box to the end of each wrapped line</dd>
<dt><code>arrow</code></dt>
<dd> print a small arrow to the end of each wrapped line</dd></dl>
</dl>
<dt><code>&#8211;non-printable-format=</code><i>format</i></dt>
<dd> Specify how the non-printable characters are printed. The possible values for the <i>format</i> are:</dd>
<dl>
<dl>
<dt><code>caret</code></dt>
<dd> caret notation: `^@&#8217;, `^A&#8217;, `^B&#8217;, &#8230;</dd>
<dt><code>octal</code></dt>
<dd> octal notation: `
</dd></dl></dl></dl>