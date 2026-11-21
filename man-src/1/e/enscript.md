---

title: "enscript(1)"
name: "enscript"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enscript/"
description: "enscript – convert text files to PostScript, HTML, RTF, ANSI, and overstrikes"
---

<p> enscript - convert text files to PostScript, HTML, RTF, ANSI, and overstrikes  </p>
<h2>SYNOPSIS</h2>
<p> <code>enscript</code> [<code>-123456789BcgGhjkKlmOqrRvVzZ</code>] [<code>-# </code><i>copies</i>] [<code>-a </code><i>pages</i>] [<code>-A </code><i>align</i>] [<code>-b </code><i>header</i>] [<code>-C</code>[<i>start_line</i>]] [<code>-d </code><i>printer</i>] [<code>-D </code><i>key</i>[<code>:</code><i>value</i>]] [<code>-e</code>[<i>char</i>]] [<code>-E</code>[<i>lang</i>]] [<code>-f </code><i>font</i>] [<code>-F </code><i>header_font</i>] [<code>-H</code>[<i>num</i>]] [<code>-i </code><i>indent</i>] [<code>-I </code><i>filter</i>] [<code>-J </code><i>title</i>] [<code>-L </code><i>lines_per_page</i>] [<code>-M </code><i>media</i>] [<code>-n </code><i>copies</i>] [<code>-N </code><i>newline</i>] [<code>-o </code><i>outputfile</i>] [<code>-o -</code>] [<code>-p </code><i>outputfile</i>] [<code>-p -</code>] [<code>-P </code><i>printer</i>] [<code>-s </code><i>baselineskip</i>] [<code>-S </code><i>key</i>[<code>:</code><i>value</i>]] [<code>-t </code><i>title</i>] [<code>-T </code><i>tabsize</i>] [<code>-u</code>[<i>text</i>]] [<code>-U </code><i>num</i>] [<code>-w </code><i>language</i>] [<code>-X </code><i>encoding</i>] [<i>filename</i> ...] </p>
<h2>DESCRIPTION</h2>
<p> <code>Enscript</code> converts text files to PostScript or to other output languages. <code>Enscript</code> can spool the generated output directly to a specified printer or leave it to a file. If no input files are given, <code>enscript</code> processes the standard input <code>stdin</code>. <code>Enscript</code> can be extended to handle different output media and it has many options which can be used to customize the printouts. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-# </code><i>num</i></dt>
<dd> <p> Print <i>num</i> copies of each page. </p>
 </dd>
<dt><code>-1, -2, -3, -4, -5, -6, -7, -8, -9, --columns=</code><i>num</i></dt>
<dd> <p> Specify how many columns each page have. With the long option <code>--columns=</code><i>num</i> you can specify more than 9 columns per page. </p>
 </dd>
<dt><code>-a </code><i>pages</i><code>, --pages=</code><i>pages</i></dt>
<dd> <p> Specify which pages are printed. The page specification <i>pages</i> can be given in the following formats: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>begin</i>-<i>end</i></dt>
<dd> <p> print pages from <i>begin</i> to <i>end</i> </p>
 </dd>
<dt>-<i>end</i></dt>
<dd> <p> print pages from 0 to <i>end</i> </p>
 </dd>
<dt><i>begin</i>-</dt>
<dd> <p> print pages from <i>begin</i> to end </p>
 </dd>
<dt><i>page</i></dt>
<dd> <p> print page <i>page</i> </p>
 </dd>
<dt>odd</dt>
<dd> <p> print odd pages </p>
 </dd>
<dt>even</dt>
<dd> <p> print even pages </p>
 </dd></dl>
</dl>
<dt><code>-A </code><i>align</i><code>, --file-align=</code><i>align</i></dt>
<dd> <p> Align separate input files to even <i>align</i> page count. This option is useful in two-side and 2-up printings (--file-align=2). </p>
 </dd>
<dt><code>-b </code><i>header</i><code>, --header=</code><i>header</i></dt>
<dd> <p> Use the text <i>header</i> as a page header. The default page header is constructed from the name of the file and from its last modification time. </p>
<p> The header string <i>header</i> can contain the same formatting escapes which can be specified for the <code>%Format</code> directives in the user defined fancy headers. For example, the following option prints the file name, current date and page numbers: </p>
<p> <code>enscript --header=&#8216;$n %W Page $% of $=&#8216; *.c</code> </p>
<p> The header string can also contain left, center and right justified fields. The fields are separated by the <code>&#8216;|&#8216;</code> character: </p>
<p> <code>enscript --header=&#8216;$n|%W|Page $% of $=&#8216; *.c</code> </p>
<p> now the file name is printed left justified, the date is centered to the header and the page numbers are printed right justified. </p>
 </dd>
<dt><code>-B, --no-header</code></dt>
<dd> <p> Do not print page headers. </p>
 </dd>
<dt><code>-c, --truncate-lines</code></dt>
<dd> <p> Cut lines that are too long for the page. As a default, <code>enscript</code> wraps long lines to the next line so no information is lost. </p>
<p> You can also use the <code>--slice</code> option which slices long lines to separate pages. </p>
 </dd>
<dt><code>-C</code>[<i>start_line</i>]<code>, --line-numbers</code>[<code>=</code><i>start_line</i>] </dt>
<dd> <p> Precede each line with its line number. The optional argument <i>start_line</i> specifies the number of the first line in the input. The number of the first line defaults to 1. </p>
 </dd>
<dt><code>-d </code><i>name</i></dt>
<dd> <p> Spool output to the printer <i>name</i>. </p>
 </dd>
<dt><code>-D </code><i>key</i>[<code>:</code><i>value</i>]<code>, --setpagedevice=</code><i>key</i>[<code>:</code><i>value</i>] </dt>
<dd> <p> Pass a page device definition to the generated PostScript output. If no value is given, the key <i>key</i> is removed from the definitions. </p>
<p> For example, the command </p>
<p> <code>enscript -DDuplex:true foo.txt</code> </p>
<p> prints file foo.txt in duplex (two side) mode. </p>
<p> Page device operators are implementation dependent but they are standardized. See section <code>PAGE DEVICE OPTIONS</code> for the details. </p>
 </dd>
<dt><code>-e</code>[<i>char</i>]<code>, --escapes</code>[<code>=</code><i>char</i>] </dt>
<dd> <p> Enable special escapes interpretation (see section <code>SPECIAL ESCAPES</code>). If the argument <i>char</i> is given, it changes the escape character to <i>char</i>. The default escape character is 0. </p>
 </dd>
<dt><code>-E</code>[<i>lang</i>]<code>, --highlight</code>[<code>=</code><i>lang</i>] </dt>
<dd> <p> Highlight source code by creating a special input filter with the <code>states</code> program. The optional argument <i>lang</i> specifies the language to highlight. As a default the <code>states</code> makes an educated guess. </p>
<p> You can print a short description of the supported highlighting languages and file formats with the command: </p>
<p> <code>enscript --help-highlight</code> </p>
<p> The highlighting rules are defined in the `/usr/share/enscript/hl/*.st&#8217; files which can be edited to create highlighting definitions for new languages. </p>
<p> <code>Note!</code> You can not use your own input filters with this option. </p>
 </dd>
<dt><code>-f </code><i>name</i><code>, --font=</code><i>name</i></dt>
<dd> <p> Select a font that is used for the body text. The default body font is <code>Courier10</code>, unless multicolumn landscape printing mode is selected, in which case the default font is <code>Courier7</code>. </p>
<p> The font specification <i>name</i> contains two parts: the name of the font and its size in PostScript points. For example, &quot;<code>Times-Roman12</code>&quot; selects the &quot;Times-Roman&quot; font with size 12pt. </p>
<p> The font specification <i>name</i> can also be given in format `<i>name</i>@<i>ptsize</i>&#8216;, where the name of the font and its point size are separated by a `@&#8216; character. This allows <code>enscript</code> to use fonts which contain digit characters in their names. </p>
<p> The font point size can also be given in the format <i>width</i>/<i>height</i> where the <i>width</i> and the <i>height</i> specify the size of the font in x- and y-directions. For example, &quot;<code>Times-Roman@10/12</code>&quot; selects a 10 points wide and 12 points high &quot;Times-Roman&quot; font. </p>
<p> You can also give the font sizes as decimal numbers. For example, &quot;<code>Times-Roman10.2</code>&quot; selects a 10.2pt &quot;Times-Roman&quot; font. </p>
 </dd>
<dt><code>-F </code><i>name</i><code>, --header-font=</code><i>name</i></dt>
<dd> <p> Select a font for the header texts. </p>
 </dd>
<dt><code>-g, --print-anyway</code></dt>
<dd> <p> Print a file even if it contains binary data. The option is implemented only for compatibility purposes. <code>Enscript</code> prints binary files anyway regardless of the option. </p>
 </dd>
<dt><code>-G, --fancy-header</code>[<code>=</code><i>name</i>] </dt>
<dd> <p> Print a fancy page header <i>name</i> to the top of each page. The option <code>-G</code> specifies the default fancy header. See section <code>CONFIGURATION FILES</code> to see how the default fancy header can be changed. </p>
 </dd>
<dt><code>-h, --no-job-header</code></dt>
<dd> <p> Suppress printing of the job header page. </p>
 </dd>
<dt><code>-H</code>[<i>num</i>]<code>, --highlight-bars</code>[<code>=</code><i>num</i>] </dt>
<dd> <p> Specify how high the highlight bars are in lines. If the <i>num</i> is not given, the default value 2 is used. As a default, no highlight bars are printed. </p>
 </dd>
<dt><code>-i </code><i>num</i><code>, --indent=</code><i>num</i></dt>
<dd> <p> Indent every line <i>num</i> characters. The indentation can also be specified in other units by appending an unit specifier after the number. The possible unit specifiers and the corresponding units are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>c</code></dt>
<dd> <p> centimeters </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> inches </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> characters (default) </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> PostScript points </p>
 </dd></dl>
</dl>
<dt><code>-I </code><i>filter</i><code>, --filter=</code><i>filter</i></dt>
<dd> <p> Read all input files through an input filter <i>filter</i>. The input filter can be a single command or a command pipeline. The filter can refer to the name of the input file with the escape `<code>%s</code>&#8216;. The name of the standard input can be changed with the option `<code>--filter-stdin</code>&#8216;. </p>
<p> For example, the following command prints the file `foo.c&#8217; by using only upper-case characters: </p>
<p> <code>enscript --filter=cat %s | tr &#8216;a-z&#8217; &#8216;A-Z&#8217; foo.c</code> </p>
<p> The following command highlights changes which are made to files since the last checkout: </p>
<p> <code>enscript --filter=rcsdiff %s | diffpp %s -e *.c</code> </p>
<p> To include the string &quot;%s&quot; to the filter command, you must write it as &quot;%%s&quot;. </p>
 </dd>
<dt><code>-j, --borders</code></dt>
<dd> <p> Print borders around columns. </p>
 </dd>
<dt><code>-J </code><i>title</i></dt>
<dd> <p> An alias for the option <code>-t</code>, <code>--title</code>. </p>
 </dd>
<dt><code>-k, --page-prefeed</code></dt>
<dd> <p> Enable page prefeed. </p>
 </dd>
<dt><code>-K, --no-page-prefeed</code></dt>
<dd> <p> Disable page prefeed (default). </p>
 </dd>
<dt><code>-l, --lineprinter</code></dt>
<dd> <p> Emulate lineprinter. This option is a shortcut for the options <code>--lines-per-page=66</code>, and <code>--no-header</code>. </p>
 </dd>
<dt><code>-L </code><i>num</i><code>, --lines-per-page=</code><i>num</i></dt>
<dd> <p> Print only <i>num</i> lines for each page. As a default, the number of lines per page is computed from the height of the page and from the size of the font. </p>
 </dd>
<dt><code>-m, --mail</code></dt>
<dd> <p> Send a mail notification to user after the print job has been completed. </p>
 </dd>
<dt><code>-M </code><i>name</i><code>, --media=</code><i>name</i></dt>
<dd> <p> Select an output media <i>name</i>. <code>Enscript</code>&#8216;s default output media is determined from libpaper and falls back to <code>A4</code>. </p>
 </dd>
<dt><code>-n </code><i>num</i><code>, --copies=</code><i>num</i></dt>
<dd> <p> Print <i>num</i> copies of each page. </p>
 </dd>
<dt><code>-N </code><i>nl</i><code>, --newline=</code><i>nl</i></dt>
<dd> <p> Select the <i>newline</i> character. The possible values for <i>nl</i> are: <code>n</code> (unix newline, 0xa hex) and <code>r</code> (mac newline, 0xd hex). </p>
 </dd>
<dt><code>-o </code><i>file</i></dt>
<dd> <p> An alias for the option <code>-p</code>, <code>--output</code>. </p>
 </dd>
<dt><code>-O, --missing-characters</code></dt>
<dd> <p> Print a listing of character codes which couldn&#8217;t be printed. </p>
 </dd>
<dt><code>-p </code><i>file</i><code>, --output=</code><i>file</i></dt>
<dd> <p> Leave the output to file <i>file</i>. If the <i>file</i> is `-&#8216;, enscript sends the output to the standard output <code>stdout</code>. </p>
 </dd>
<dt><code>-P </code><i>name</i><code>, --printer=</code><i>name</i></dt>
<dd> <p> Spool the output to the printer <i>name</i>. </p>
 </dd>
<dt><code>-q, --quiet, --silent</code></dt>
<dd> <p> Make <code>enscript</code> really quiet. Only fatal error messages are printed to <i>stderr</i>. </p>
 </dd>
<dt><code>-r, --landscape</code></dt>
<dd> <p> Print in the landscape mode; rotate page 90 degrees. </p>
 </dd>
<dt><code>-R, --portrait</code></dt>
<dd> <p> Print in the portrait mode (default). </p>
 </dd>
<dt><code>-s </code><i>num</i><code>, --baselineskip=</code><i>num</i></dt>
<dd> <p> Specify the baseline skip in PostScript points. The number <i>num</i> can be given as a decimal number. When <code>enscript</code> moves from line to line, the current point <i>y</i> coordinate is moved (<i>font point size + baselineskip</i>) points down. The default baseline skip is 1. </p>
 </dd>
<dt><code>-S </code><i>key</i>[<code>:</code><i>value</i>]<code>, --statusdict=</code><i>key</i>[<code>:</code><i>value</i>] </dt>
<dd> <p> Pass a statusdict definition to the generated PostScript output. If no value is given, the key <i>key</i> is removed from the definitions. </p>
<p> The statusdict operators are implementation dependent; see the printer&#8217;s documentation for the details. </p>
<p> For example, the command </p>
<p> <code>enscript -Ssetpapertray:1 foo.txt</code> </p>
<p> prints the file <i>foo.txt</i> by using paper from the paper tray 1 (assuming that the printer supports paper tray selection). </p>
 </dd>
<dt><code>-t </code><i>title</i><code>, --title=</code><i>title</i></dt>
<dd> <p> Set banner page&#8217;s job title to <i>title</i>. The option sets also the name of the input file <code>stdin</code>. </p>
 </dd>
<dt><code>-T </code><i>num</i><code>, --tabsize=</code><i>num</i></dt>
<dd> <p> Set the tabulator size to <i>num</i> characters. The default is 8. </p>
 </dd>
<dt><code>-u</code>[<i>text</i>]<code>, --underlay</code>[<code>=</code><i>text</i>] </dt>
<dd> <p> Print the string <i>text</i> under every page. The properties of the text can be changed with the options <code>--ul-angle</code>, <code>--ul-font</code>, <code>--ul-gray</code>, <code>--ul-position</code>, and <code>--ul-style</code>. </p>
<p> If no <i>text</i> is given, the underlay is not printed. This can be used to remove an underlay text that was specified with the `<code>Underlay</code>&#8216; configuration file option. </p>
 </dd>
<dt><code>-U </code><i>num</i><code>, --nup=</code><i>num</i></dt>
<dd> <p> Print <i>num</i> logical pages on each output page (N-up printing). The values <i>num</i> must be a power of 2. </p>
 </dd>
<dt><code>-v, --verbose</code>[<code>=</code><i>level</i>] </dt>
<dd> <p> Tell what <code>enscript</code> is doing. </p>
 </dd>
<dt><code>-V, --version</code></dt>
<dd> <p> Print <code>enscript</code> version information and exit. </p>
 </dd>
<dt><code>-w </code>[<i>lang</i>]<code>, --language</code>[<code>=</code><i>lang</i>] </dt>
<dd> <p> Generate output for the language <i>lang</i>. The possible values for <i>lang</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>PostScript</code></dt>
<dd> <p> generate PostScript (default) </p>
 </dd>
<dt><code>html</code></dt>
<dd> <p> generate HTML </p>
 </dd>
<dt><code>overstrike</code></dt>
<dd> <p> generate overstrikes (line printers, less) </p>
 </dd>
<dt><code>rtf</code></dt>
<dd> <p> generate RTF (Rich Text Format) </p>
 </dd>
<dt><code>ansi</code></dt>
<dd> <p> generate ANSI terminal control codes </p>
 </dd></dl>
</dl>
<dt><code>-X </code><i>name</i><code>, --encoding=</code><i>name</i></dt>
<dd> <p> Use the input encoding <i>name</i>. Currently <code>enscript</code> supports the following encodings: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>88591, latin1</code></dt>
<dd> <p> ISO-8859-1 (ISO Latin1) (<code>enscript</code>&#8216;s default encoding). </p>
 </dd>
<dt><code>88592, latin2</code></dt>
<dd> <p> ISO-8859-2 (ISO Latin2) </p>
 </dd>
<dt><code>88593, latin3</code></dt>
<dd> <p> ISO-8859-3 (ISO Latin3) </p>
 </dd>
<dt><code>88594, latin4</code></dt>
<dd> <p> ISO-8859-4 (ISO Latin4) </p>
 </dd>
<dt><code>88595, cyrillic</code></dt>
<dd> <p> ISO-8859-5 (ISO Cyrillic) </p>
 </dd>
<dt><code>88597, greek</code></dt>
<dd> <p> ISO-8859-7 (ISO Greek) </p>
 </dd>
<dt><code>88599, latin5</code></dt>
<dd> <p> ISO-8859-9 (ISO Latin5) </p>
 </dd>
<dt><code>885910, latin6</code></dt>
<dd> <p> ISO-8859-10 (ISO Latin6) </p>
 </dd>
<dt><code>ascii</code></dt>
<dd> <p> 7-bit ascii </p>
 </dd>
<dt><code>asciifise, asciifi, asciise</code></dt>
<dd> <p> 7-bit ascii with some scandinavian (Finland, Sweden) extensions </p>
 </dd>
<dt><code>asciidkno, asciidk, asciino</code></dt>
<dd> <p> 7-bit ascii with some scandinavian (Denmark, Norway) extensions </p>
 </dd>
<dt><code>ibmpc, pc, dos</code></dt>
<dd> <p> IBM PC charset </p>
 </dd>
<dt><code>mac</code></dt>
<dd> <p> Mac charset </p>
 </dd>
<dt><code>vms</code></dt>
<dd> <p> VMS multinational charset </p>
 </dd>
<dt><code>hp8</code></dt>
<dd> <p> HP Roman-8 charset </p>
 </dd>
<dt><code>koi8</code></dt>
<dd> <p> Adobe Standard Cyrillic Font KOI8 charset </p>
 </dd>
<dt><code>ps, PS</code></dt>
<dd> <p> PostScript font&#8217;s default encoding </p>
 </dd>
<dt><code>pslatin1, ISOLatin1Encoding</code></dt>
<dd> <p> PostScript interpreter&#8217;s `ISOLatin1Encoding&#8217; </p>
 </dd></dl>
</dl>
<dt><code>-z, --no-formfeed</code></dt>
<dd> <p> Turn off the form feed character interpretation. </p>
 </dd>
<dt><code>-Z, --pass-through</code></dt>
<dd> <p> Pass through all PostScript and PCL files without any modifications. This allows that <code>enscript</code> can be used as a lp filter. </p>
<p> The PostScript files are recognized by looking up the `%!&#8216; magic cookie from the beginning of the file. <code>Note!</code> <code>Enscript</code> recognized also the Windoze damaged `^D%!&#8216; cookie. </p>
<p> The PCL files are recognized by looking up the `^[E&#8217; or `^[%&#8216; magic cookies from the beginning of the file. </p>
 </dd>
<dt><code>--color</code>[<code>=</code><i>bool</i>] </dt>
<dd> <p> Use colors in the highlighting outputs. </p>
 </dd>
<dt><code>--download-font=</code><i>fontname</i></dt>
<dd> <p> Include the font description file (<i>.pfa</i> or <i>.pfb</i> file) of the font <i>fontname</i> to the generated output. </p>
 </dd>
<dt><code>--extended-return-values</code></dt>
<dd> <p> Enable extended return values. As a default, <code>enscript</code> returns 1 on error and 0 otherwise. The extended return values give more details about the printing operation. See the section <code>RETURN VALUE</code> for the details. </p>
 </dd>
<dt><code>--filter-stdin=</code><i>name</i></dt>
<dd> <p> Specify how the <code>stdin</code> is shown to the input filter. The default value is an empty string (&quot;&quot;) but some programs require that the <code>stdin</code> is called something else, usually &quot;-&quot;. </p>
 </dd>
<dt><code>--footer=</code><i>footer</i></dt>
<dd> <p> Use the text <i>footer</i> as a page footer. Otherwise the option works like the <code>--header</code> option </p>
 </dd>
<dt><code>--h-column-height=</code><i>height</i></dt>
<dd> <p> Set the horizontal column height to be <i>height</i> PostScript points. The option sets the formfeed type to <code>horizontal-columns</code>. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print a short help message and exit. </p>
 </dd>
<dt><code>--help-highlight</code></dt>
<dd> <p> Describe all supported <code>--highlight</code> languages and file formats. </p>
 </dd>
<dt><code>--highlight-bar-gray=</code><i>gray</i></dt>
<dd> <p> Specify the gray level which is used in printing the highlight bars. </p>
 </dd>
<dt><code>--list-media</code></dt>
<dd> <p> List the names of all known output media and exit successfully. </p>
 </dd>
<dt><code>--margins=</code><i>left</i><code>:</code><i>right</i><code>:</code><i>top</i><code>:</code><i>bottom</i></dt>
<dd> <p> Adjust the page marginals to be exactly <i>left</i>, <i>right</i>, <i>top</i> and <i>bottom</i> PostScript points. Any of the arguments can be left empty in which case the default value is used. </p>
 </dd>
<dt><code>--mark-wrapped-lines</code>[<code>=</code><i>style</i>] </dt>
<dd> <p> Mark wrapped lines in the output with the style <i>style</i>. The possible values for the <i>style</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>none</code></dt>
<dd> <p> do not mark them (default) </p>
 </dd>
<dt><code>plus</code></dt>
<dd> <p> print a plus (+) character to the end of each wrapped line </p>
 </dd>
<dt><code>box</code></dt>
<dd> <p> print a black box to the end of each wrapped line </p>
 </dd>
<dt><code>arrow</code></dt>
<dd> <p> print a small arrow to the end of each wrapped line </p>
 </dd></dl>
</dl>
<dt><code>--non-printable-format=</code><i>format</i></dt>
<dd> <p> Specify how the non-printable characters are printed. The possible values for the <i>format</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>caret</code></dt>
<dd> <p> caret notation: `^@&#8216;, `^A&#8217;, `^B&#8217;, ... </p>
 </dd>
<dt><code>octal</code></dt>
<dd> <p> octal notation: `\000&#8217;, `\001&#8217;, `\002&#8217;, ... (default) </p>
 </dd>
<dt><code>questionmark</code></dt>
<dd> <p> replace non-printable characters with a question mark `?&#8216; </p>
 </dd>
<dt><code>space</code></dt>
<dd> <p> replace non-printable characters with a space ` &#8216; </p>
 </dd></dl>
</dl>
<dt><code>--nup-columnwise</code></dt>
<dd> <p> Change the layout of the sub-pages in the N-up printing from row-wise to columnwise. </p>
 </dd>
<dt><code>--nup-xpad=</code><i>num</i></dt>
<dd> <p> Set the page x-padding of the <i>n</i>-up printing to <i>num</i> PostScript points. The default is 10 points. </p>
 </dd>
<dt><code>--nup-ypad=</code><i>num</i></dt>
<dd> <p> Set the page y-padding of the <i>n</i>-up printing to <i>num</i> PostScript points. The default is 10 points. </p>
 </dd>
<dt><code>--page-label-format=</code><i>format</i></dt>
<dd> <p> Set the page label format to <i>format</i>. The page label format specifies how the labels for the `%%Page:&#8216; PostScript comments are formatted. The possible values are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>short</code></dt>
<dd> <p> Print the current pagenumber: `%%Page: (1) 1&#8217; (default) </p>
 </dd>
<dt><code>long</code></dt>
<dd> <p> Print the current filename and pagenumber: `%%Page: (main.c: 1) 1&#8217; </p>
 </dd></dl>
</dl>
<dt><code>--ps-level=</code><i>level</i></dt>
<dd> <p> Set the PostScript language level that <code>enscript</code> uses for its output to <i>level</i>. The possible values are <code>1</code>, and <code>2</code>. </p>
 </dd>
<dt><code>--printer-options=</code><i>options</i></dt>
<dd> <p> Pass extra options to the printer command. </p>
 </dd>
<dt><code>--rotate-even-pages</code></dt>
<dd> <p> Rotate each even-numbered page 180 degrees. </p>
 </dd>
<dt><code>--slice=</code><i>num</i></dt>
<dd> <p> Print the vertical slice <i>num</i>. The slices are vertical regions of input files. A new slice starts from the point where the line would otherwise be wrapped to the next line. The slice numbers start from 1. </p>
 </dd>
<dt><code>--style=</code><i>style</i></dt>
<dd> <p> Set the highlighting style to <i>style</i>. The possible values are: <code>a2ps</code>, <code>emacs</code>, <code>emacs_verbose</code>, <code>ifh</code>, and <code>msvc</code>. </p>
 </dd>
<dt><code>--swap-even-page-margins</code></dt>
<dd> <p> Swap left and right page margins for even-numbered pages. </p>
 </dd>
<dt><code>--toc</code></dt>
<dd> <p> Print a table of contents to the end of the output. </p>
 </dd>
<dt><code>--word-wrap</code></dt>
<dd> <p> Wrap long lines from word boundaries. </p>
 </dd>
<dt><code>--ul-angle=</code><i>angle</i></dt>
<dd> <p> Set the angle of the underlay text to <i>angle</i>. As a default, the angle is <code>atan(-d_page_h, d_page_w)</code>. </p>
 </dd>
<dt><code>--ul-font=</code><i>name</i></dt>
<dd> <p> Select a font for the underlay text. The default underlay font is <code>Times-Roman200</code>. </p>
 </dd>
<dt><code>--ul-gray=</code><i>num</i></dt>
<dd> <p> Print the underlay text with the gray value <i>num</i> (0 ... 1), the default gray value is .8. </p>
 </dd>
<dt><code>--ul-position=</code><i>position_spec</i></dt>
<dd> <p> Set the underlay text&#8217;s starting position according to the <i>position_spec</i>. The position specification must be given in format: `<i>sign</i> <i>xpos</i> <i>sign</i> <i>ypos</i>&#8216;, where the <i>sign</i> must be `+&#8216; or `-&#8216;. The positive dimensions are measured from the lower left corner and the negative dimensions from the upper right corner. For example, the specification `+0-0&#8217; specifies the upper left corner and `-0+0&#8217; specifies the lower right corner. </p>
 </dd>
<dt><code>--ul-style=</code><i>style</i></dt>
<dd> <p> Set the underlay text&#8217;s style to <i>style</i>. The possible values for <i>style</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>outline</code></dt>
<dd> <p> print outline underlay texts (default) </p>
 </dd>
<dt><code>filled</code></dt>
<dd> <p> print filled underlay texts </p>
 </dd></dl>
</dl>
<h2>CONFIGURATION FILES</h2>
<p> <code>Enscript</code> reads configuration information from the following sources (in this order): command line options, environment variable <code>ENSCRIPT</code>, user&#8217;s personal configuration file (<code>$HOME/.enscriptrc</code>), site configuration file (<code>/etc/enscriptsite.cfg</code>) and system&#8217;s global configuration file (<code>/etc/enscript.cfg</code>). </p>
<p> The configuration files have the following format: </p>
<p> Empty lines and lines starting with `#&#8216; are comments. </p>
<p> All other lines are option lines and have format: </p>
<p> <i>option</i> [<i>arguments ...</i>]. </p>
<p> The following options can be specified: </p>
<dl>
<dt><code>AcceptCompositeCharacters: </code><i>bool</i></dt>
<dd> <p> Specify whether PostScript font&#8217;s composite characters are accepted as printable or if they should be considered as non-existent. The default value is false (0). </p>
 </dd>
<dt><code>AFMPath: </code><i>path</i></dt>
<dd> <p> Specifies the search path for the <i>AFM</i> files. </p>
 </dd>
<dt><code>AppendCtrlD: </code><i>int</i></dt>
<dd> <p> Specify if the Control-D (^D) character should be appended to the end of the output. A value of 1 will append ^D followed by a newline, a value of 2 will omit the trailing newline. The default value is 0 for no ^D. </p>
 </dd>
<dt><code>Clean7Bit: </code><i>bool</i></dt>
<dd> <p> Specify how characters greater than 127 are printed. The valuee true (1) generates 7-bit clean code by escaping all characters greater than 127 to the backslash-octal notation (default). The value false (0) generates 8-bit PostScript code leaving all characters untouched. </p>
 </dd>
<dt><code>DefaultEncoding: </code><i>name</i></dt>
<dd> <p> Select the default input encoding. The encoding name <i>name</i> can be one of the values of the option <code>-X</code>, <code>--encoding</code>. </p>
 </dd>
<dt><code>DefaultFancyHeader: </code><i>name</i></dt>
<dd> <p> Select the default fancy header. The default header is used when the option <code>-G</code> is specified or the option <code>--fancy-header</code> is given without an argument. The system-wide default is `<code>enscript</code>&#8216;. </p>
 </dd>
<dt><code>DefaultMedia: </code><i>name</i></dt>
<dd> <p> Select the default output media. </p>
 </dd>
<dt><code>DefaultOutputMethod: </code><i>method</i></dt>
<dd> <p> Select the default target to which the generated output is sent. The possible values for the <i>method</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>printer</code></dt>
<dd> <p> send output to printer (default) </p>
 </dd>
<dt><code>stdout</code></dt>
<dd> <p> send output to <code>stdout</code> </p>
 </dd></dl>
</dl>
<dt><code>DownloadFont: </code><i>fontname</i></dt>
<dd> <p> Include the font description file of the font <i>fontname</i> to the generated output. </p>
 </dd>
<dt><code>EscapeChar: </code><i>num</i></dt>
<dd> <p> Specify the escape character for the special escapes. The default value is 0. </p>
 </dd>
<dt><code>FormFeedType: </code><i>type</i></dt>
<dd> <p> Specify what to do when a formfeed character is encountered from the input. The possible values for <i>type</i> are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>column</code></dt>
<dd> <p> move to the beginning of the next column (default) </p>
 </dd>
<dt><code>page</code></dt>
<dd> <p> move to the beginning of the next page </p>
 </dd></dl>
</dl>
<dt><code>GeneratePageSize: </code><i>bool</i></dt>
<dd> <p> Specify whether the <code>PageSize</code> page device setting is generated to the PostScript output. The default value is true (1). </p>
 </dd>
<dt><code>HighlightBarGray: </code><i>gray</i></dt>
<dd> <p> Specify the gray level which is used to print the highlight bars. </p>
 </dd>
<dt><code>HighlightBars: </code><i>num</i></dt>
<dd> <p> Specify how high the highlight bars are in lines. The default value is 0 which means that no highlight bars are printed. </p>
 </dd>
<dt><code>LibraryPath: </code><i>path</i></dt>
<dd> <p> Specifies the <code>enscript</code>&#8216;s library path that is used to lookup various resources. The default path is: `/usr/share/enscript:<i>home</i>/.enscript&#8217;. Where the <i>home</i> is the user&#8217;s home directory. </p>
 </dd>
<dt><code>MarkWrappedLines: </code><i>style</i></dt>
<dd> <p> Mark wraped lines in the output with the style <i>style</i>. The possible values for the <i>format</i> are the same which can be given for the <code>--mark-wrapped-lines</code> option. </p>
 </dd>
<dt><code>Media: </code><i>name</i><i>width</i><i>height</i><i>llx</i><i>lly</i><i>urx</i><i>ury</i><code></dt>
<dd> <p> Add a new output media with the name </code><i>name</i>. The physical dimensions of the media are <i>width</i> and <i>height</i>. The bounding box of the Media is specified by the points (<i>llx</i>, <i>lly</i>) and (<i>urx</i>, <i>ury</i>). <code>Enscript</code> prints all graphics inside the bounding box of the media. </p>
<p> User can select this media with option <code>-M </code><i>name</i>. </p>
 </dd>
<dt><code>NoJobHeaderSwitch: </code><i>switch</i></dt>
<dd> <p> Specify the spooler option to suppress the print job header page. This option is passed to the printer spooler when the <code>enscript</code>&#8216;s option <code>-h</code>, <code>--no-job-header</code> is selected. </p>
 </dd>
<dt><code>NonPrintableFormat: </code><i>format</i></dt>
<dd> <p> Specify how the non-printable characters are printed. The possible values for <i>format</i> are the same which can be given for the <code>--non-printable-format</code> option. </p>
 </dd>
<dt><code>OutputFirstLine: </code><i>line</i></dt>
<dd> <p> Set the PostScript output&#8217;s first line to <i>line</i>. The default value is <code>PS-Adobe-3.0</code>. Since some printers do not like DSC levels greater than 2.0, this option can be used to change the output first line to something more suitable like <code>%!PS-Adobe-2.0</code> or <code>%!</code>. </p>
 </dd>
<dt><code>PageLabelFormat: </code><i>format</i></dt>
<dd> <p> Set the page label format to <i>format</i>. The possible values for <i>format</i> are the same which can be given for the <code>--page-label-format</code> option. </p>
 </dd>
<dt><code>PagePrefeed: </code><i>bool</i></dt>
<dd> <p> Enable / disable page prefeed. The default value is false (0). </p>
 </dd>
<dt><code>PostScriptLevel: </code><i>level</i></dt>
<dd> <p> Set the PostScript language level, that <code>enscript</code> uses for its output, to <i>level</i>. The possible values for <i>level</i> are the same which can be given for the <code>--ps-level</code> option. </p>
 </dd>
<dt><code>Printer: </code><i>name</i></dt>
<dd> <p> Names the printer to which the output is spooled. </p>
 </dd>
<dt><code>QueueParam: </code><i>name</i></dt>
<dd> <p> The spooler command switch to select the printer queue, e.g. <code>-P</code> in <code>lpr -Pps</code>. This option can also be used to pass other flags to the spooler command. These options must be given before the queue switch. </p>
 </dd>
<dt><code>SetPageDevice: </code><i>key</i>[<code>:</code><i>value</i>] </dt>
<dd> <p> Pass a page device definition to the generated PostScript output. </p>
 </dd>
<dt><code>Spooler: </code><i>name</i></dt>
<dd> <p> Names the printer spooler command. <code>Enscript</code> pipes generated PostScript to the command <i>name</i>. </p>
 </dd>
<dt><code>StatesBinary: </code><i>path</i></dt>
<dd> <p> Define an absolute path to the <code>states</code> program. </p>
 </dd>
<dt><code>StatesColor: </code><i>bool</i></dt>
<dd> <p> Should the <code>states</code> program generate color outputs. </p>
 </dd>
<dt><code>StatesConfigFile: </code><i>file</i></dt>
<dd> <p> Read highlighting states configuration from the file <i>file</i>. The default config file is `/usr/share/enscript/hl/enscript.st&#8217;. </p>
 </dd>
<dt><code>StatesHighlightStyle: </code><i>style</i></dt>
<dd> <p> Set the highlight style to <i>style</i>. </p>
 </dd>
<dt><code>StatesPath: </code><i>path</i></dt>
<dd> <p> Define the path for the <code>states</code> program. The <code>states</code> program will lookup its state definition files from this path. The default value is `$HOME/.enscript:/usr/share/enscript/hl&#8217;. </p>
 </dd>
<dt><code>StatusDict: </code><i>key</i>[<code>:</code><i>value</i>] </dt>
<dd> <p> Pass a statusdict definition to the generated PostScript output. </p>
 </dd>
<dt><code>TOCFormat: </code><i>format</i></dt>
<dd> <p> Format table of contents entries with the format string <i>format</i>. The format string <i>format</i> can contain the same escapes which are used to format header strings with the `%Format&#8217; special comment. </p>
 </dd>
<dt><code>Underlay: </code><i>text</i></dt>
<dd> <p> Print string <i>text</i> under every page. </p>
 </dd>
<dt><code>UnderlayAngle: </code><i>num</i></dt>
<dd> <p> Set the angle of the underlay text to <i>num</i>. </p>
 </dd>
<dt><code>UnderlayFont: </code><i>fontspec</i></dt>
<dd> <p> Select a font for the underlay text. </p>
 </dd>
<dt><code>UnderlayGray: </code><i>num</i></dt>
<dd> <p> Print the underlay text with the gray value <i>num</i>. </p>
 </dd>
<dt><code>UnderlayPosition: </code><i>position_spec</i></dt>
<dd> <p> Set the underlay text&#8217;s starting position according to the <i>position_spec</i>. </p>
 </dd>
<dt><code>UnderlayStyle: </code><i>style</i></dt>
<dd> <p> Set the underlay text&#8217;s style to <i>style</i>. </p>
 </dd></dl>
<h2>FANCY HEADERS</h2>
<p> Users can create their own fancy headers by creating a header description file and placing it in a directory which is in <code>enscript</code>&#8216;s library path. The name of the header file must be in format: `<i>headername</i>.hdr&#8217;. Header can be selected by giving option: <code>--fancy-header=</code><i>headername</i>. </p>
<p> Header description file contains PostScript code that paints the header. Description file must provide procedure <code>do_header</code> which is called by <code>enscript</code> at the beginning of every page. </p>
<p> Header description file contains two parts: comments and code. Parts are separated by a line containing text: </p>
<p> % -- code follows this line -- </p>
<p> <code>Enscript</code> copies only the code part of description file to the generated PostScript output. The comments part can contain any data, it is not copied. If separator line is missing, no data is copied to output. </p>
<p> <code>Enscript</code> defines following constants which can be used in header description files: </p>
<dl>
<dt><code>d_page_w</code></dt>
<dd> <p> page width </p>
 </dd>
<dt><code>d_page_h</code></dt>
<dd> <p> page height </p>
 </dd>
<dt><code>d_header_x</code></dt>
<dd> <p> header lower left <i>x</i> coordinate </p>
 </dd>
<dt><code>d_header_y</code></dt>
<dd> <p> header lower left <i>y</i> coordinate </p>
 </dd>
<dt><code>d_header_w</code></dt>
<dd> <p> header width </p>
 </dd>
<dt><code>d_header_h</code></dt>
<dd> <p> header height </p>
 </dd>
<dt><code>d_footer_x</code></dt>
<dd> <p> footer lower left <i>x</i> coordinate </p>
 </dd>
<dt><code>d_footer_y</code></dt>
<dd> <p> footer lower left <i>y</i> coordinate </p>
 </dd>
<dt><code>d_footer_w</code></dt>
<dd> <p> footer width </p>
 </dd>
<dt><code>d_footer_h</code></dt>
<dd> <p> footer height </p>
 </dd>
<dt><code>d_output_w</code></dt>
<dd> <p> width of the text output area </p>
 </dd>
<dt><code>d_output_h</code></dt>
<dd> <p> height of the text output area </p>
 </dd>
<dt><code>user_header_p</code></dt>
<dd> <p> predicate which tells if user has defined his/her own header string: <code>true</code>/<code>false</code> </p>
 </dd>
<dt><code>user_header_left_str</code></dt>
<dd> <p> if <code>user_header_p</code> is <code>true</code>, this is the left field of the user supplied header string. </p>
 </dd>
<dt><code>user_header_center_str</code></dt>
<dd> <p> if <code>user_header_p</code> is <code>true</code>, this is the center field of the user supplied header string </p>
 </dd>
<dt><code>user_header_right_str</code></dt>
<dd> <p> if <code>user_header_p</code> is <code>true</code>, this is the right field of the user supplied header string </p>
 </dd>
<dt><code>user_footer_p</code></dt>
<dd> <p> predicate which tells if user has defined his/her own footer string: <code>true</code>/<code>false</code> </p>
 </dd>
<dt><code>user_footer_left_str</code></dt>
<dd> <p> if <code>user_footer_p</code> is <code>true</code>, this is the left field of the user supplied footer string. </p>
 </dd>
<dt><code>user_footer_center_str</code></dt>
<dd> <p> if <code>user_footer_p</code> is <code>true</code>, this is the center field of the user supplied footer string </p>
 </dd>
<dt><code>user_footer_right_str</code></dt>
<dd> <p> if <code>user_footer_p</code> is <code>true</code>, this is the right field of the user supplied footer string </p>
 </dd>
<dt><code>HF</code></dt>
<dd> <p> standard header font (from <code>-F</code>, <code>--header-font</code> option). This can be selected simply by invoking command: `<code>HF setfont</code>&#8216;. </p>
 </dd>
<dt><code>pagenum</code></dt>
<dd> <p> the number of the current page </p>
 </dd>
<dt><code>fname</code></dt>
<dd> <p> the full name of the printed file (/foo/bar.c) </p>
 </dd>
<dt><code>fdir</code></dt>
<dd> <p> the directory part of the file name (/foo) </p>
 </dd>
<dt><code>ftail</code></dt>
<dd> <p> file name without the directory part (bar.c) </p>
 </dd>
<dt><code>gs_languagelevel</code></dt>
<dd> <p> PostScript interpreter&#8217;s language level (currently 1 or 2) </p>
 </dd></dl>
<p> You can also use the following special comments to customize your headers and to specify some extra options. Special comments are like DSC comments but they start with a single `%&#8216; character; special comments start from the beginning of the line and they have the following syntax: </p>
<p> %<i>commentname</i>: <i>options</i> </p>
<p> Currently <code>enscript</code> support the following special comments: </p>
<dl>
<dt><code>%Format: </code><i>name</i><i>format</i></dt>
<dd> <p> Define a new string constant <i>name</i> according to the format string <i>format</i>. Format string start from the first non-space character and it ends to the end of the line. Format string can contain general `%&#8216; escapes and input file related `$&#8216; escapes. Currently following escapes are supported: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>%%</code></dt>
<dd> <p> character `%&#8216; </p>
 </dd>
<dt><code>$$</code></dt>
<dd> <p> character `$&#8216; </p>
 </dd>
<dt><code>$%</code></dt>
<dd> <p> current page number </p>
 </dd>
<dt><code>$=</code></dt>
<dd> <p> number of pages in the current file </p>
 </dd>
<dt><code>$p</code></dt>
<dd> <p> number of pages processed so far </p>
 </dd>
<dt><code>$(</code><i>VAR</i><code>)</code></dt>
<dd> <p> value of the environment variable <i>VAR</i>. </p>
 </dd>
<dt><code>%c</code></dt>
<dd> <p> trailing component of the current working directory </p>
 </dd>
<dt><code>%C </code>(<code>$C</code>) </dt>
<dd> <p> current time (file modification time) in `hh:mm:ss&#8217; format </p>
 </dd>
<dt><code>%d</code></dt>
<dd> <p> current working directory </p>
 </dd>
<dt><code>%D </code>(<code>$D</code>) </dt>
<dd> <p> current date (file modification date) in `yy-mm-dd&#8217; format </p>
 </dd>
<dt><code>%D{</code><i>string</i><code>} </code>(<code>$D{</code><i>string</i><code>}</code>) </dt>
<dd> <p> format string <i>string</i> with the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function. `<code>%D{}</code>&#8216; refers to the current date and `<code>$D{}</code>&#8216; to the input file&#8217;s last modification date. </p>
 </dd>
<dt><code>%E </code>(<code>$E</code>) </dt>
<dd> <p> current date (file modification date) in `yy/mm/dd&#8217; format </p>
 </dd>
<dt><code>%F </code>(<code>$F</code>) </dt>
<dd> <p> current date (file modification date) in `dd.mm.yyyy&#8217; format </p>
 </dd>
<dt><code>%H</code></dt>
<dd> <p> document title </p>
 </dd>
<dt><code>$L</code></dt>
<dd> <p> number of lines in the current input file. This is valid only for the toc entries, it can&#8217;t be used in header strings. </p>
 </dd>
<dt><code>%m</code></dt>
<dd> <p> the hostname up to the first `.&#8216; character </p>
 </dd>
<dt><code>%M</code></dt>
<dd> <p> the full hostname </p>
 </dd>
<dt><code>%n</code></dt>
<dd> <p> the user login name </p>
 </dd>
<dt><code>$n</code></dt>
<dd> <p> input file name without the directory part </p>
 </dd>
<dt><code>%N</code></dt>
<dd> <p> the user&#8217;s pw_gecos field up to the first `,&#8216; character </p>
 </dd>
<dt><code>$N</code></dt>
<dd> <p> the full input file name </p>
 </dd>
<dt><code>%t </code>(<code>$t</code>) </dt>
<dd> <p> current time (file modification time) in 12-hour am/pm format </p>
 </dd>
<dt><code>%T </code>(<code>$T</code>) </dt>
<dd> <p> current time (file modification time) in 24-hour format `hh:mm&#8217; </p>
 </dd>
<dt><code>%* </code>(<code>$*</code>) </dt>
<dd> <p> current time (file modification time) in 24-hour format with seconds `hh:mm:ss&#8217; </p>
 </dd>
<dt><code>$v</code></dt>
<dd> <p> the sequence number of the current input file </p>
 </dd>
<dt><code>$V</code></dt>
<dd> <p> the sequence number of the current input file in the `Table of Contents&#8217; format: if the <code>--toc</code> option is given, escape expands to `<i>num</i>-&#8216;; if the <code>--toc</code> is not given, escape expands to an empty string. </p>
 </dd>
<dt><code>%W </code>(<code>$W</code>) </dt>
<dd> <p> current date (file modification date) in `mm/dd/yy&#8217; format </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> All format directives except `$=&#8216; can also be given in format </p>
<p> <i>escape</i> <i>width</i> <i>directive</i> </p>
<p> where <i>width</i> specifies the width of the column to which the escape is printed. For example, escape &quot;$5%&quot; will expand to something like &quot; 12&quot;. If the width is negative, the value will be printed left-justified. </p>
<p> For example, the `emacs.hdr&#8217; defines its date string with the following format comment: </p>
<p> <code>%Format: eurdatestr %E</code> </p>
<p> which expands to: </p>
<p> <code>/eurdatestr (96/01/08) def</code> </p>
 </dd></dl>
</dl>
<dl>
<dt><code>%HeaderHeight: </code><i>height</i></dt>
<dd> <p> Allocate <i>height</i> points space for the page header. The default header height is 36 points. </p>
 </dd>
<dt><code>%FooterHeight: </code><i>height</i></dt>
<dd> <p> Allocate <i>height</i> points space for the page footer. The default footer height is 0 points. </p>
 </dd></dl>
<p> According to Adobe&#8217;s Document Structuring Conventions (DSC), all resources needed by a document must be listed in document&#8217;s prolog. Since user&#8217;s can create their own headers, <code>enscript</code> don&#8217;t know what resources those headers use. That&#8217;s why all headers must contain a standard DSC comment that lists all needed resources. For example, used fonts can be listed with following comment: </p>
<p> %%DocumentNeededResources: font <i>fontname1</i> <i>fontname2</i> </p>
<p> Comment can be continued to the next line with the standard continuation comment: </p>
<p> %%+ font <i>fontname3</i> </p>
<h2>SPECIAL ESCAPES</h2>
<p> <code>Enscript</code> supports special escape sequences which can be used to add some page formatting commands to ASCII documents. As a default, special escapes interpretation is off, so all ASCII files print out as everyone expects. Special escapes interpretation is activated by giving option <code>-e</code>, <code>--escapes</code> to <code>enscript</code>. </p>
<p> All special escapes start with the escape character. The default escape character is ^@ (octal 000); escape character can be changed with option <code>-e</code>, <code>--escapes</code>. Escape character is followed by escape&#8217;s name and optional options and arguments. </p>
<p> Currently <code>enscript</code> supports following escapes: </p>
<dl>
<dt><code>bgcolor</code></dt>
<dd> <p> change the text background color. The syntax of the escape is: </p>
<p> ^@bgcolor{<i>red</i> <i>green</i> <i>blue</i>} </p>
<p> where the color components <i>red</i>, <i>green</i>, and blue are given as decimal numbers between values 0 and 1. </p>
 </dd>
<dt><code>bggray</code></dt>
<dd> <p> change the text background color. The syntax of the escape is: </p>
<p> ^@bggray{<i>gray</i>} </p>
<p> where <i>gray</i> is the new text background gray value. The default value is 1.0 (white). </p>
 </dd>
<dt><code>color</code></dt>
<dd> <p> change the text color. The syntax of the escape is: </p>
<p> ^@color{<i>red</i> <i>green</i> <i>blue</i>} </p>
<p> where color components <i>red</i>, <i>green</i> and <i>blue</i> are given as decimal numbers between values 0 and 1. </p>
 </dd>
<dt><code>comment</code></dt>
<dd> <p> comment the rest of the line including the newline character. Escape&#8217;s syntax is: </p>
<p> ^@comment <i>text</i> <i>newline_character</i> </p>
 </dd>
<dt><code>escape</code></dt>
<dd> <p> change the escape character. The syntax of the escape is: </p>
<p> ^@escape{<i>code</i>} </p>
<p> where <i>code</i> is the decimal code of the new escape character. </p>
 </dd>
<dt><code>epsf</code></dt>
<dd> <p> inline EPS file to the document. The syntax of the escape is: </p>
<p> ^@epsf[<i>options</i>]{<i>filename</i>} </p>
<p> where <i>options</i> is an optional sequence of option characters and values enclosed with brackets and <i>filename</i> is the name of the EPS file. </p>
<p> If <i>filename</i> ends to the `|&#8216; character, then <i>filename</i> is assumed to name a command that prints EPS data to its standard output. In this case, <code>enscript</code> opens a pipe to the specified command and reads EPS data from pipe. </p>
<p> Following options can be given for the <code>epsf</code> escape: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>c</code></dt>
<dd> <p> print image centered </p>
 </dd>
<dt><code>r</code></dt>
<dd> <p> print image right justified </p>
 </dd>
<dt><code>n</code></dt>
<dd> <p> do not update current point. Following output is printed to that position where the current point was just before the <code>epsf</code> escape </p>
 </dd>
<dt><code>nx</code></dt>
<dd> <p> do not update current point <i>x</i> coordinate </p>
 </dd>
<dt><code>ny</code></dt>
<dd> <p> do not update current point <i>y</i> coordinate </p>
 </dd>
<dt><code>x</code><i>num</i></dt>
<dd> <p> move image&#8217;s top left <i>x</i> coordinate <i>num</i> characters from current point <i>x</i> coordinate (relative position) </p>
 </dd>
<dt><code>x</code><i>num</i><code>a</code></dt>
<dd> <p> set image&#8217;s top left <i>x</i> coordinate to column <i>num</i> (absolute position) </p>
 </dd>
<dt><code>y</code><i>num</i></dt>
<dd> <p> move image&#8217;s top left <i>y</i> coordinate <i>num</i> lines from current line (relative position) </p>
 </dd>
<dt><code>y</code><i>num</i><code>a</code></dt>
<dd> <p> set image&#8217;s top left <i>y</i> coordinate to line <i>num</i> (absolute position) </p>
 </dd>
<dt><code>h</code><i>num</i></dt>
<dd> <p> set image&#8217;s height to <i>num</i> lines </p>
 </dd>
<dt><code>s</code><i>num</i></dt>
<dd> <p> scale image with factor <i>num</i> </p>
 </dd>
<dt><code>sx</code><i>num</i></dt>
<dd> <p> scale image in <i>x</i> direction with factor <i>num</i> </p>
 </dd>
<dt><code>sy</code><i>num</i></dt>
<dd> <p> scale image in <i>y</i> direction with factor <i>num</i> </p>
 </dd></dl>
<p> As a default, all dimensions are given in lines (vertical) and characters (horizontal). You can also specify other units by appending an unit specifier after number. Possible unit specifiers and the corresponding units are: </p>
<dl>
<dt><code>c</code></dt>
<dd> <p> centimeters </p>
 </dd>
<dt><code>i</code></dt>
<dd> <p> inches </p>
 </dd>
<dt><code>l</code></dt>
<dd> <p> lines or characters (default) </p>
 </dd>
<dt><code>p</code></dt>
<dd> <p> PostScript points </p>
 </dd></dl>
<p> For example to print an image one inch high, you can specify height by following options: <code>h1i</code> (1 inch), <code>h2.54c</code> (2.54 cm), <code>h72p</code> (72 points). </dl>
 </p>
<dt><code>font</code></dt>
<dd> <p> select current font. The syntax of the escape is: </p>
<p> ^@font{<i>fontname</i>[:<i>encoding</i>]} </p>
<p> where <i>fontname</i> is a standard font specification. Special font specification <code>default</code> can be used to select the default body font (<code>enscript</code>&#8216;s default or the one specified by the command line option <code>-f</code>, <code>--font</code>). </p>
<p> The optional argument <i>encoding</i> specifies the encoding that should be used for the new font. Currently the encoding can only be the <code>enscript</code>&#8216;s global input encoding or <code>ps</code>. </p>
 </dd>
<dt><code>ps</code></dt>
<dd> <p> include raw PostScript code to the output. The syntax of the escape is: </p>
<p> ^@ps{<i>code</i>} </p>
 </dd>
<dt><code>shade</code></dt>
<dd> <p> highlight regions of text by changing the text background color. Escape&#8217;s syntax is: </p>
<p> ^@shade{<i>gray</i>} </p>
<p> where <i>gray</i> is the new text background gray value. The default value is 1.0 (white) which disables highlighting. </p>
 </dd></dl>
<h2>PAGE DEVICE OPTIONS</h2>
<p> Page device is a PostScript level 2 feature that offers an uniform interface to control printer&#8217;s output device. <code>Enscript</code> protects all page device options inside an if block so they have no effect in level 1 interpreters. Although all level 2 interpreters support page device, they do not have to support all page device options. For example some printers can print in duplex mode and some can not. Refer to the documentation of your printer for supported options. </p>
<p> Here are some usable page device options which can be selected with the <code>-D</code>, <code>--setpagedevice</code> option. For a complete listing, see <i>PostScript Language Reference Manual</i>: section 4.11 Device Setup. </p>
<dl>
<dt><code>Collate </code><i>boolean</i></dt>
<dd> <p> how output is organized when printing multiple copies </p>
 </dd>
<dt><code>Duplex </code><i>boolean</i></dt>
<dd> <p> duplex (two side) printing </p>
 </dd>
<dt><code>ManualFeed </code><i>boolean</i></dt>
<dd> <p> manual feed paper tray </p>
 </dd>
<dt><code>OutputFaceUp </code><i>boolean</i></dt>
<dd> <p> print output `face up&#8217; or `face down&#8217; </p>
 </dd>
<dt><code>Tumble </code><i>boolean</i></dt>
<dd> <p> how opposite sides are positioned in duplex printing </p>
 </dd></dl>
<h2>PRINTING EXAMPLES</h2>
<p> Following printing examples assume that <code>enscript</code> uses the default configuration. If default actions have been changed from the configuration files, some examples will behave differently. </p>
<dl>
<dt><code>enscript foo.txt</code></dt>
<dd> <p> Print file <code>foo.txt</code> to the default printer. </p>
 </dd>
<dt><code>enscript -Possu foo.txt</code></dt>
<dd> <p> Print file <code>foo.txt</code> to printer <code>ossu</code>. </p>
 </dd>
<dt><code>enscript -pfoo.ps foo.txt</code></dt>
<dd> <p> Print file <code>foo.txt</code>, but leave PostScript output to file <code>foo.ps</code>. </p>
 </dd>
<dt><code>enscript -2 foo.txt</code></dt>
<dd> <p> Print file <code>foo.txt</code> to two columns. </p>
 </dd>
<dt><code>enscript -2r foo.txt</code></dt>
<dd> <p> Print file to two columns and rotate output 90 degrees (landscape). </p>
 </dd>
<dt><code>enscript -DDuplex:true foo.txt</code></dt>
<dd> <p> Print file in duplex (two side) mode (printer dependent). </p>
 </dd>
<dt><code>enscript -G2rE -U2 foo.c</code></dt>
<dd> <p> My default code printing command: gaudy header, two columns, landscape, code highlighting, 2-up printing. </p>
 </dd>
<dt><code>enscript -E --color -whtml --toc -pfoo.html *.h *.c</code></dt>
<dd> <p> A nice HTML report of your project&#8217;s C source files. </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The environment variable <code>ENSCRIPT</code> can be used to pass default options for <code>enscript</code>. For example, to select the default body font to be Times-Roman 7pt, set the following value to the <code>ENSCRIPT</code> environment variable: </p>
<dl>
<dt><code>-fTimes-Roman7</code></dt>
<dd>  </dd></dl>
<p> The value of the <code>ENSCRIPT</code> variable is processed before the command line options, so command line options can be used to overwrite these defaults. </p>
<p> Variable <code>ENSCRIPT_LIBRARY</code> specifies the <code>enscript</code>&#8216;s library directory. It can be used to overwrite the build-in default `/usr/share/enscript&#8217;. </p>
<h2>RETURN VALUE</h2>
<p> <code>Enscript</code> returns value 1 to the shell if any errors were encountered or 0 otherwise. If the option <code>--extended-return-values</code> was specified, the return value is constructed from the following flags: </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> no errors or warnings </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> some lines were truncated or wrapped </p>
 </dd>
<dt><code>4</code></dt>
<dd> <p> some characters were missing from the used fonts </p>
 </dd>
<dt><code>8</code></dt>
<dd> <p> some characters were unprintable </p>
 </dd></dl>
<h2>FILES</h2>
<pre><code>/usr/share/enscript/*.hdr header files
/usr/share/enscript/*.enc input encoding vectors
/usr/share/enscript/enscript.pro PostScript prolog
/usr/share/enscript/afm/*.afm AFM files for PostScript fonts
/usr/share/enscript/font.map index for the AFM files
/usr/share/enscript/hl/*.st states definition files
/etc/enscript.cfg system-wide configuration file
/etc/enscriptsite.cfg site configuration file
~/.enscriptrc personal configuration file
~/.enscript/ personal resource directory
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-diffpp/">diffpp</a>(1), ghostview(1), <a href="/docs/linux/man/1-gs/">gs</a>(1), <a href="/docs/linux/man/1-lpq/">lpq</a>(1), <a href="/docs/linux/man/1-lpr/">lpr</a>(1), <a href="/docs/linux/man/1-lprm/">lprm</a>(1), <a href="/docs/linux/man/1-states/">states</a>(1) </p>
<h2>AUTHOR</h2>
<p> Markku Rossi &lt;mtr [at] iki.fi&gt; &lt;<a rel="nofollow" href="http://www.iki.fi/~mtr/">http://www.iki.fi/~mtr/</a>&gt; </p>
<p> GNU Enscript WWW home page: &lt;<a rel="nofollow" href="http://www.iki.fi/~mtr/genscript/">http://www.iki.fi/~mtr/genscript/</a>&gt; </p>
