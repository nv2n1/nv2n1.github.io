---
title: "mpage(1)"
name: "mpage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpage/"
description: "mpage – print multiple pages per sheet on PostScript printer"
---

<h2 class="name">NAME</h2>
<p> mpage &#8211; print multiple pages per sheet on PostScript printer</p>
<h2>SYNOPSIS</h2>
<p> <code>mpage</code> [<code>-1248aAceEfHloOrRStTuUvVxX</code>] [<code>-b</code><i>&nbsp;<wbr>papersize</i>] [<code>-B</code>[<i>num</i>[<code>lrtb</code>]]&#8230;] [<code>-C</code> [<i>encoding</i>]] [<code>-da</code><i>|</i><code>p</code>] [<code>-D</code><i>&nbsp;<wbr>dateformat</i>] [<code>-F</code><i>&nbsp;<wbr>fontname</i>] [<code>-h</code><i>&nbsp;<wbr>header</i>] [<code>-j</code><i>&nbsp;<wbr>first</i>[-<i>last</i>][%<i>interval</i>]] [<code>-J</code><i>&nbsp;<wbr>startpageno</i>] [<code>-L</code><i>&nbsp;<wbr>lines</i>] [<code>-m</code>[<i>num</i>[<code>lrtb</code>]]&#8230;] [<code>-M</code>[<i>num</i>[<code>lrtb</code>]]&#8230;] [<code>-p</code>[<i>prprog</i>]] [<code>-P</code>[<i>printer</i>]] [<code>-s</code><i>&nbsp;<wbr>tabstop</i>] [<code>-W</code><i>&nbsp;<wbr>width</i>] [<code>-z</code><i>&nbsp;<wbr>printcmd</i>] [<code>-Z</code><i>&nbsp;<wbr>printcmd_args</i>] [<i>file</i>&nbsp;<wbr>&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <i>mpage</i> reads plain text files or PostScript documents and prints them on a PostScript printer with the text reduced in size so that several pages appear on one sheet of paper. This is useful for viewing large printouts on a small amount of paper. It uses ISO 8859.1 to print 8-bit characters. </p>
<p> The following options are recognized (note that arguments to options may be separated from the option by spaces, except for <code>-B</code>, <code>-m</code>, <code>-M</code>, <code>-p</code> and <code>-P</code>): Also when mpage encounters &#8212; as option it will stop parsing arguments and the remaining arguments are interpreted as filenames. </p>
<dl>
<dt><code>-1</code></p>
<dd> Print 1 normal page per sheet (included for symmetry). </p>
<dt><code>-2</code></p>
<dd> Print 2 normal pages per sheet. </p>
<dt><code>-4</code></p>
<dd> Print 4 normal pages per sheet <i>(default)</i>. </p>
<dt><code>-8</code></p>
<dd> Print 8 normal pages per sheet. </p>
<dt><code>-a</code></p>
<dd> Toggle layout of the pages on the sheet so that successively numbered pages run down the sheet, as opposed to left to right. (<i>default</i> updown) . </p>
<dt><code>-A</code></p>
<dd> This option is deprecated, see <code>-b</code>. Prepare output for A4 sized paper. For default see &#8216;mpage -x&#8217;. </p>
<dt><code>-b</code><i>papertype</i></p>
<dd> Prepare output for selected paper type. <i>Papersize</i> can be <i>A3</i> for European A3, <i>A4</i> for European A4, <i>Letter</i> for US Letter or <i>Legal</i> for Legal sized paper. For default see &#8216;mpage -x&#8217;. To see the list of currently available types, just give the &#8216;mpage -bl&#8217; or &#8216;mpage -b?&#8217; command (Note: mpage exits after finding such option use.) </p>
<dt><code>-B</code>[<i>&lt;num&gt;</i>[<code>lrtb</code>]*]</p>
<dd> Setup a box around a particular part of your page. Specify text box margins and line thickness. The default is 0 columns (lines) for both left and right (top and bottom) margins and 0 line thickness. Specifying <code>-B </code> solely toggles printing of the box. <i>l</i>, <i>r</i>, <i>t</i> or <i>b</i> set the left, right, top or bottom margin respectively to <i>&lt;num&gt;</i> columns (lines). Not specifying any of the sides, will set the line thickness when <i>&lt;num&gt; </i> is given. For example <code>-B</code><i>1</i> sets the line thickness to 1. Sides with negative margins will not print. </p>
<dt><code>-c</code></p>
<dd> Toggle concatenation off pages from different files on single sheets (<i>default</i> off). </p>
<dt><code>-C</code>[<i>encodingfile</i>]</p>
<dd> Specify the character encoding file. The file should be in the mpage library directory (<i>/usr/share/mpage</i>). <i>Mpage</i> has an internal default encoding based on Latin-1 or IBM codepage 850. Depending on compile time option this encoding definition is on or not. Not specifying an encodingfile will toggle the usage of the internal encoding. </p>
<dt><code>-d</code><i>a</i>|<i>p</i></p>
<dd> Force input to be taken as ascii (<i>a</i>) or postscript (<i>p</i>) text. This way you can print your postscript code as text, or print postscript code that mpage does not recognise. When using <code>-d</code><i>p</i>, make sure that the the postscript code contains <i>%Page</i> page separators or else things will probably look odd. </p>
<dt><code>-D</code><i>dateformat</i></p>
<dd> Set the date format as in <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) to be used in date/time representations (e.g. in headers). (Note: to be useful you probably need the <code>-H</code> option.) </p>
<dt><code>-e</code></p>
<dd> Print 2 normal pages per sheet in duplex mode. Every first and fourth page or on one side and every second and third on the other side. This is more or less a combination of the -O and -E option but then in one pass. </p>
<dt><code>-E</code></p>
<dd> Print 2 normal pages per sheet. However, this option will print every second and third page of every set of four pages. This option will ignore <code>-a</code> and <code>-l</code>. See also the -O option. Using these options double sided prints can be created without a duplex printer. </p>
<dt><code>-f</code></p>
<dd> Toggles folding lines longer than page width (<i>default</i> off) . </p>
<dt><code>-F</code><i>fontname</i></p>
<dd> Specify font. (<i>default</i> Courier). Check your printer for supported fonts. Note: this has almost nothing to do with the fonts used for your X-windows/KDE/Gnome environment. </p>
<dt><code>-h</code><i>header</i></p>
<dd> This is used only when the <code>-p</code> or <code>-H</code> switch is used and is passed as the &quot;<code>-h</code><i>&nbsp;<wbr>header</i>&quot; option to <code>pr</code>(<code>1</code>) or as the header for <code>-H</code>. </p>
<dt><code>-H</code></p>
<dd> Create header line for each logical page separated from page text by a horizontal line. Unless <code>-h</code> is given, the header consist of last file modification time, filename and page number, all in bold and slightly larger font. This option only applies to non-postscript files. </p>
<dt><code>-I</code><i>indent</i></p>
<dd> Indent text by <i>indent</i> characters. </p>
<dt><code>-j</code><i>first</i>[<i>-last</i>][<i>%interval</i>]</p>
<dd> Print just the selected sheets, specified by a number, starting at 1. Here <i>last</i> defaults to the end of data, <i>interval</i> to 1. Several <code>-j</code> options can be given (upto MAXJARGS, default 100) to create a complex selection of pages. Thus <code>-j</code><i>1-10</i> selects the first 10 sheets, while <code>-j</code><i> 1%2</i> prints just the odd-numbered sheets and <code>-j</code><i> 2%2</i> prints just the even ones. </p>
<p> You can do double-sided printing, in two passes, as follows. If you use 3-hole punched paper, put it in the printer such that the holes will appear at the top of the page &#8212; on the right as you pull out the printer tray, in our Laser writer II NTX. Print the odd-numbered sheets with</p>
<dt>
<dd>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> mpage &#8230; -j 1%2 &#8230;</p>
<dt>
<dd> Note the number of pages it reports. (Only half this many will really be printed). When printing finishes, if mpage reported an <i>odd</i> number of pages, remove the last one from the stack, since there will be no even-numbered sheet to match it. Then arrange the stack of paper for printing on the other side. (If it&#8217;s punched, the holes will now be on the left.) On our II NTX, the paper comes out blank-side up; replace it in the tray still blank-side up but rotated 180 degrees. For other printers, you figure it out. Now print the even-numbered sheets in reverse order with</p>
<dt>
<dd>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> mpage &#8230; -r -j 2%2 &#8230;</p>
<dt>
<dd> hoping no one else reaches the printer before you do. </p>
<dt><code>-J</code><i>startpageno</i></p>
<dd> Set the start value of the sheet page count to <i>startpageno</i> instead of 1. </p>
<dt><code>-k</code></p>
<dd> When mpage finds a %%TRailer or %%PSTrailer in the postscript input file it normally assumes this is the end of the postscript file and stops reading the input file. But when the PS file includes EPS files, %%Trailers might be anywhere. Using this option ignores the %%TRailer and %%PSTRailer lines.</p>
<dt><code>-l</code></p>
<dd> Toggle printing landscape or portrait mode. Landscape pages are 55 lines long by 132 characters wide by default. Portrait pages are 66 lines long by 80 characters wide by default. (<i>default</i> portrait.) </p>
<dt><code>-L</code><i>lines</i></p>
<dd> Adjust the page reduction parameters so that <i>lines</i> lines will fit in the space of one page. This overrides the default values normally supplied. (See <code>-l</code>.) If used in conjunction with <code>-p</code> then this value is passed to the <code><a href="/docs/linux/man/1-pr/">pr</a></code>(1) as well. As a side effect this changes the font size as well (as will the <code>-W</code> option.) So while there is an option to change font family, there is no explicit option to change font size! </p>
<dt><code>-m</code>[<i>&lt;num&gt;</i>[<code>lrtb</code>]*]</p>
<dd> Specify sheet margin. The default margin is 20 points. Only specifying <code>-m </code> sets left margin to 40 points. <i>l</i>, <i>r</i>, <i>t</i> or <i>b</i> set left, right, top or bottom margin respectively to <i>&lt;num&gt;</i> points. Not specifying any of the sides will set all sides when <i>&lt;num&gt; </i> is given. <i>&lt;num&gt;</i> defaults to 40 points. For example <code>-m</code><i>10</i> sets all margins to 10 points. <code>-m</code><i>l50tb</i> sets left margin to default 40 and top and bottom margin to 50 points. <code>-m</code><i>50l25bt30r</i> set bottom and top margin to 25, left margin to 50 and right margin to 30 points. Margins can have negative numbers. </p>
<dt><code>-M</code>[<i>&lt;num&gt;</i>[<code>lrtb</code>]*]</p>
<dd> Specify logical page margins. For syntax, see <code>-m</code> option. Defaults are 4 for <code>-M </code> solely, and 8 for <i>&lt;num&gt;</i>. Margins can be negative. This way large white borders in your (postscript) documents can be reduced. </p>
<dt><code>-o</code></p>
<dd> Toggle printing of outlines around each reduced page (<i>default</i> on). </p>
<dt><code>-O</code></p>
<dd> Print 2 normal pages per sheet. However, this option will print every first and fourth page of every set of four pages. This option will ignore <code>-a</code> and <code>-l</code>. See also the -E option. Using these options double sided prints can be created without a duplex printer. </p>
<dt><code>-p</code>[<i>prprog</i>]</p>
<dd> Pipe input through <i>prprog</i> command (including specified options) before printing (assumes the input is a text file). When no command is specified, it defaults to <code><a href="/docs/linux/man/1-pr/">pr</a></code>(1). </p>
<dt><code>-P</code>[<i>printer</i>]</p>
<dd> Specify the printer to which the PostScript output will be sent (e.g.lpr -P<i>printer</i>). Using <code>-P</code> with no printer specified will send the PostScript to the default printer queue (e.g. lpr). Using -P- will return output to stdout, useful in combination with MPAGE environment variable. Without <code>-P</code> output will be send to standard output. </p>
<dt><code>-r</code></p>
<dd> Reverse printing. The last sheet is printed first. The way of arranging reduced pages on the sheets doesn&#8217;t change. </p>
<dt><code>-R</code></p>
<dd> Switch to left to right mode, starting first page on left bottom corner. This might be useful for landscape postscript files. (Note: using <code>-l</code> after <code>-R</code> undoes <code>-R</code>, and switches to normal landscape mode. </p>
<dt><code>-s</code><i>tabstop</i></p>
<dd> Set tabstop width (<i>default</i> 8 characters). Should by &gt;= 2. </p>
<dt><code>-S</code></p>
<dd> Accept non-square page reduction. By default, pages are shrunk equally in X and Y, even if this wastes some space on the sheet. With <code>-S</code>, reduced pages are larger but slightly distorted. (only used when printing postscript files.) </p>
<dt><code>-t</code></p>
<dd> Toggle printing on both sides of the paper. This will toggle duplex mode of the printer. Use this option only if your printer is capable of printing in duplex mode. (<i>default</i> off). </p>
<dt><code>-T</code></p>
<dd> Toggle tumble of every second pages when printing in duplex mode. Use this option only if your printer is capable of printing in duplex mode and together with <code>-t</code>. </p>
<dt><code>-u</code></p>
<dd> Toggle checking for UTF-8 input (not relevant for postscript input). </p>
<dt><code>-U</code></p>
<dd> This option is deprecated, see <code>-b</code>. Prepare output for US Letter sized paper. For default see &#8216;mpage -x&#8217;. </p>
<dt><code>-v</code></p>
<dd> Toggle printing a count of the number of sheets produced for printing (<i>default</i> off.) </p>
<dt><code>-V</code></p>
<dd> Print version information and exit. </p>
<dt><code>-W</code><i>width</i></p>
<dd> Adjust the page reduction parameters so that a line with <i>width</i> characters long will fit in the space of one page. This overrides the default values normally supplied. (See <code>-l</code>.) If used in conjunction with <code>-p</code> then this value is passed to the s <code><a href="/docs/linux/man/1-pr/">pr</a></code>(1) program as well. See also the <code>-L</code>&nbsp;<wbr>option on font sizes. </p>
<dt><code>-x</code></p>
<dd> Force usage display, which also shows current defaults. </p>
<dt><code>-X [header]</code></p>
<dd> Print header on the left and the page number on the right of each physical page (sheet). If no header is given, the default is the current filename (note influence of <code>-c</code>), the filename of the first file on the page is used. </p>
<dt><code>-z</code><i>printcommand</i></p>
<dd> Specify command to use to send output to. Default is <code>lpr </code> (1) for BSD style spooler, <code>lp</code> (1) for SYSV style spooler. You can specify command line options, but note <code>-Z</code>. For example <code>-zlp</code> for system V Unix. </p>
<dt><code>-Z</code><i>printprog_queuename_arg</i></p>
<dd> Specify what option to use for the &quot;<code>-z</code><i>&nbsp;<wbr>printcommand</i>&quot; to specify a printqueue. For example <code>-zlp -Z-d</code> for system V Unix. Default is <code>-P</code> for BSD style spooler, <code>-d</code> for SYSV style spooler. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> <i>mpage</i> examines the <code>PRINTER</code> (or <code>LPDEST</code> for SYSV style spooler) environment variable to override its default printer. </p>
<p> The <code>MPAGE_LIB</code> environment variable can be used to control where the character encoding files (<code>-C</code>) can be found. </p>
<p> <i>mpage</i> also examines the <code>MPAGE</code> environment variable for default option settings. Any option or combination of options can be specified in the <code>MPAGE</code> environment variable. For example, if MPAGE is set to the string:</p>
<dl>
<dt>
<dd> <code>-2oPqms -L60</code></dl>
<p> it would (in the absence of other command line arguments) print 2 pages per sheet, 60 lines per page, with outlines, on the printer named <code>qms</code> (overriding the <code>PRINTER</code>/<code>LPDEST</code> environment variable, if it exists.) In the environment variable, white space is used as an option delimiter, and no quoting is recognized. </p>
<p> Any command line options will override both the <code>PRINTER</code> and <code>MPAGE</code> environment variables. </p>
<h2>FILES</h2>
<p> /usr/tmp/mpageXXXXXX<br />
 /usr/share/mpage </p>
<h2>BUGS</h2>
<p> Suffers under the burden of far too many switches. (But <code>you</code> wanted the choices!) </p>
<p> NULL characters in a postscript input file will cause mpage to crash! </p>
<p> Many others, we&#8217;re sure. </p>
<p> Mpage is year 2000 compliant, as long as the underlying operating system is!!! </p>
<h2>VERSION</h2>
<p> Version 2.5.6, Released Januari 2008.<br />
 Location:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.mesa.nl/pub/mpage">http://www.mesa.nl/pub/mpage</a><br />
 <a href="ftp://ftp.mesa.nl/pub/mpage">ftp://ftp.mesa.nl/pub/mpage</a></dl>
<h2>AUTHORS</h2>
<p> Marcel Mol &lt;marcel [at] mesa.nl&gt; (current maintainer). </p>
<p> Mark P. Hahn (Original author) </p>
<h2>Index</h2>
