---

title: "lp-cups(1)"
name: "lp-cups"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lp-cups/"
description: "lp – print files"
---

<p> lp &#8211; print files</p>
<h2>SYNOPSIS</h2>
<p> <code>lp</code> [ -E ] [ -U <i>username</i> ] [ -c ] [ -d <i>destination[/instance]</i> ] [ -h <i>hostname[:port]</i> ] [ -m ] [ -n <i>num-copies</i> ] [ -o <i>option[=value]</i> ] [ -q <i>priority</i> ] [ -s ] [ -t <i>title</i> ] [ -H <i>handling</i> ] [ -P <i>page-list</i> ] [ &#8212; ] [ <i>file(s)</i> ]<br/>
 <code>lp</code> [ -E ] [ -U <i>username</i> ] [ -c ] [ -h <i>hostname[:port]</i> ] [ -i <i>job-id</i> ] [ -n <i>num-copies</i> ] [ -o <i>option[=value]</i> ] [ -q <i>priority</i> ] [ -t <i>title</i> ] [ -H <i>handling</i> ] [ -P <i>page-list</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lp</i> submits files for printing or alters a pending job. Use a filename of &quot;-&quot; to force printing from the standard input.</p>
<h2>THE DEFAULT DESTINATION</h2>
<p> CUPS provides many ways to set the default destination. The &quot;LPDEST&quot; and &quot;PRINTER&quot; environment variables are consulted first. If neither are set, the current default set using the <i><a href="/docs/linux/man/1-lpoptions/">lpoptions</a>(1)</i> command is used, followed by the default set using the <i><a href="/docs/linux/man/8-lpadmin/">lpadmin</a>(8)</i> command.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <i>lp</i>:</p>
<dl>
<dt>&#8212;</dt>
<dd>
 Marks the end of options; use this to print a file whose name begins with a dash (-).</dd>
<dt>-E</dt>
<dd>
 Forces encryption when connecting to the server.</dd>
<dt>-U username</dt>
<dd>
 Specifies the username to use when connecting to the server.</dd>
<dt>-c</dt>
<dd>
 This option is provided for backwards-compatibility only. On systems that support it, this option forces the print file to be copied to the spool directory before printing. In CUPS, print files are always sent to the scheduler via IPP which has the same effect.</dd>
<dt>-d destination</dt>
<dd>
 Prints files to the named printer.</dd>
<dt>-h hostname[:port]</dt>
<dd>
 Chooses an alternate server.</dd>
<dt>-i job-id</dt>
<dd>
 Specifies an existing job to modify.</dd>
<dt>-m</dt>
<dd>
 Sends an email when the job is completed.</dd>
<dt>-n copies</dt>
<dd>
 Sets the number of copies to print from 1 to 100.</dd>
<dt>-o &quot;name=value [name=value &#8230;]&quot;</dt>
<dd>
 Sets one or more job options.</dd>
<dt>-q priority</dt>
<dd>
 Sets the job priority from 1 (lowest) to 100 (highest). The default priority is 50.</dd>
<dt>-s</dt>
<dd>
 Do not report the resulting job IDs (silent mode.)</dd>
<dt>-t &quot;name&quot;</dt>
<dd>
 Sets the job name.</dd>
<dt>-H hh:mm</dt>
<dd>
</dd><dt>-H hold</dt>
<dd>
</dd><dt>-H immediate</dt>
<dd>
</dd><dt>-H restart</dt>
<dd>
</dd><dt>-H resume</dt>
<dd>
 Specifies when the job should be printed. A value of <i>immediate</i> will print the file immediately, a value of <i>hold</i> will hold the job indefinitely, and a UTC time value (HH:MM) will hold the job until the specified UTC (not local) time. Use a value of <i>resume</i> with the <i>-i</i> option to resume a held job. Use a value of <i>restart</i> with the <i>-i</i> option to restart a completed job.</dd>
<dt>-P page-list</dt>
<dd>
 Specifies which pages to print in the document. The list can contain a list of numbers and ranges (#-#) separated by commas (e.g. 1,3-5,16). The page numbers refer to the output pages and not the document&#8217;s original pages &#8211; options like &quot;number-up&quot; can affect the numbering of the pages.</dd></dl>
<h2>COMMON JOB OPTIONS</h2>
<p> Aside from the printer-specific options reported by the <i><a href="/docs/linux/man/1-lpoptions/">lpoptions</a>(1)</i> command, the following generic options are available:</p>
<dl>
<dt>-o media=size</dt>
<dd>
 Sets the page size to <i>size</i>. Most printers support at least the size names &quot;a4&quot;, &quot;letter&quot;, and &quot;legal&quot;.</dd>
<dt>-o landscape</dt>
<dd>
</dd><dt>-o orientation-requested=4</dt>
<dd>
 Prints the job in landscape (rotated 90 degrees).</dd>
<dt>-o sides=one-sided</dt>
<dd>
</dd><dt>-o sides=two-sided-long-edge</dt>
<dd>
</dd><dt>-o sides=two-sided-short-edge</dt>
<dd>
 Prints on one or two sides of the paper. The value &quot;two-sided-long-edge&quot; is normally used when printing portrait (unrotated) pages, while &quot;two-sided-short-edge&quot; is used for landscape pages.</dd>
<dt>-o fit-to-page</dt>
<dd>
 Scales the print file to fit on the page.</dd>
<dt>-o number-up=2</dt>
<dd>
</dd><dt>-o number-up=4</dt>
<dd>
</dd><dt>-o number-up=6</dt>
<dd>
</dd><dt>-o number-up=9</dt>
<dd>
</dd><dt>-o number-up=16</dt>
<dd>
 Prints multiple document pages on each output page.</dd>
<dt>-o cpi=N</dt>
<dd>
 Sets the number of characters per inch to use when printing a text file. The default is 10.</dd>
<dt>-o lpi=N</dt>
<dd>
 Sets the number of lines per inch to use when printing a text file. The default is 6.</dd>
<dt>-o page-bottom=N</dt>
<dd>
</dd><dt>-o page-left=N</dt>
<dd>
</dd><dt>-o page-right=N</dt>
<dd>
</dd><dt>-o page-top=N</dt>
<dd>
 Sets the page margins when printing text files. The values are in points &#8211; there are 72 points to the inch.</dd></dl>
<h2>EXAMPLES</h2>
<p> Print a double-sided legal document to a printer called &quot;foo&quot;: </p>
<pre>
    lp -d foo -o media=legal -o sides=two-sided-long-edge filename
</pre>
<p> Print an image across 4 pages: </p>
<pre>
    lp -d bar -o scaling=200 filename
</pre>
<p> Print a text file with 12 characters per inch, 8 lines per inch, and a 1 inch left margin: </p>
<pre>
    lp -d bar -o cpi=12 -o lpi=8 -o page-left=72 filename
</pre>
<h2>COMPATIBILITY</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> The &quot;q&quot; option accepts a different range of values than the Solaris lp command, matching the IPP job priority values (1-100, 100 is highest priority) instead of the Solaris values (0-39, 0 is highest priority).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/8-lpadmin/">lpadmin</a>(8)</i>, <i><a href="/docs/linux/man/8-lpmove/">lpmove</a>(8)</i>, <i><a href="/docs/linux/man/1-lpoptions/">lpoptions</a>(1)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br/>
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
