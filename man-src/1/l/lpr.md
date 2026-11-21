---

title: "lpr(1)"
name: "lpr"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpr/"
description: "lpr – print files"
---

<p> <code>lpr</code> [ <code>-E</code> ] [ <code>-H </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-U</code> <i>username</i> ] [ <code>-P </code><i>destination</i>[<code>/</code><i>instance</i>] ] [ <code>-#</code> <i>num-copies</i> [ <code>-h</code> ] [ <code>-l</code> ] [ <code>-m</code> ] [ <code>-o </code><i>option</i>[<code>=</code><i>value</i>] ] [ <code>-p</code> ] [ <code>-q</code> ] [ <code>-r</code> ] [ <code>-C</code> <i>title</i> ] [ <code>-J</code> <i>title</i> ] [ <code>-T</code> <i>title</i> ] [ <i>file(s)</i> ]</p>
<p> <code>lpr</code> submits files for printing. Files named on the command line are sent to the named printer or the default destination if no destination is specified. If no files are listed on the command-line, <code>lpr</code> reads the print file from the standard input.</p>
<h3>THE DEFAULT DESTINATION</h3>
<p> CUPS provides many ways to set the default destination. The <code>LPDEST</code> and <code>PRINTER</code> environment variables are consulted first. If neither are set, the current default set using the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command is used, followed by the default set using the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) command.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <i>lpr</i>:</p>
<dl>
<dt><code>-E</code></dt>
<dd> Forces encryption when connecting to the server.</dd>
<dt><code>-H </code><i>server</i>[<code>:</code><i>port</i>]</dt>
<dd> Specifies an alternate server.</dd>
<dt><code>-C &quot;</code><i>name</i><code>&quot;</code></dt>
<dd>
</dd><dt><code>-J &quot;</code><i>name</i><code>&quot;</code></dt>
<dd>
</dd><dt><code>-T &quot;</code><i>name</i><code>&quot;</code></dt>
<dd> Sets the job name/title.</dd>
<dt><code>-P </code><i>destination</i>[<code>/</code><i>instance</i>]</dt>
<dd> Prints files to the named printer.</dd>
<dt><code>-U </code><i>username</i></dt>
<dd> Specifies an alternate username.</dd>
<dt><code>-# </code><i>copies</i></dt>
<dd> Sets the number of copies to print.</dd>
<dt><code>-h</code></dt>
<dd> Disables banner printing. This option is equivalent to <i>-o job-sheets=none</i>.</dd>
<dt><code>-l</code></dt>
<dd> Specifies that the print file is already formatted for the destination and should be sent without filtering. This option is equivalent to <i>-o raw</i>.</dd>
<dt><code>-m</code></dt>
<dd> Send an email on job completion.</dd>
<dt><code>-o </code><i>option</i>[<code>=</code><i>value</i>]</dt>
<dd> Sets a job option. See &quot;COMMON JOB OPTIONS&quot; below.</dd>
<dt><code>-p</code></dt>
<dd> Specifies that the print file should be formatted with a shaded header with the date, time, job name, and page number. This option is equivalent to <i>-o prettyprint</i> and is only useful when printing text files.</dd>
<dt><code>-q</code></dt>
<dd> Hold job for printing.</dd>
<dt><code>-r</code></dt>
<dd> Specifies that the named print files should be deleted after submitting them.</dd></dl>
<h3>COMMON JOB OPTIONS</h3>
<p> Aside from the printer-specific options reported by the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command, the following generic options are available:</p>
<dl>
<dt><code>-o job-sheets=</code><i>name</i></dt>
<dd> Prints a cover page (banner) with the document. The &quot;name&quot; can be &quot;classified&quot;, &quot;confidential&quot;, &quot;secret&quot;, &quot;standard&quot;, &quot;topsecret&quot;, or &quot;unclassified&quot;.</dd>
<dt><code>-o media=</code><i>size</i></dt>
<dd> Sets the page size to <i>size</i>. Most printers support at least the size names &quot;a4&quot;, &quot;letter&quot;, and &quot;legal&quot;.</dd>
<dt><code>-o number-up=</code>{<i>2|4|6|9|16</i>}</dt>
<dd> Prints 2, 4, 6, 9, or 16 document (input) pages on each output page.</dd>
<dt><code>-o orientation-requested=4</code></dt>
<dd> Prints the job in landscape (rotated 90 degrees counter-clockwise).</dd>
<dt><code>-o orientation-requested=5</code></dt>
<dd> Prints the job in landscape (rotated 90 degrees clockwise).</dd>
<dt><code>-o orientation-requested=6</code></dt>
<dd> Prints the job in reverse portrait (rotated 180 degrees).</dd>
<dt><code>-o print-quality=3</code></dt>
<dd>
</dd><dt><code>-o print-quality=4</code></dt>
<dd>
</dd><dt><code>-o print-quality=5</code></dt>
<dd> Specifies the output quality &#8211; draft (3), normal (4), or best (5).</dd>
<dt><code>-o sides=one-sided</code></dt>
<dd> Prints on one side of the paper.</dd>
<dt><code>-o sides=two-sided-long-edge</code></dt>
<dd> Prints on both sides of the paper for portrait output.</dd>
<dt><code>-o sides=two-sided-short-edge</code></dt>
<dd> Prints on both sides of the paper for landscape output.</dd></dl>
<h2>NOTES</h2>
<p> The <i>-c</i>, <i>-d</i>, <i>-f</i>, <i>-g</i>, <i>-i</i>, <i>-n</i>, <i>-t</i>, <i>-v</i>, and <i>-w</i> options are not supported by CUPS and produce a warning message if used.</p>
<h2>EXAMPLES</h2>
<p> Print two copies of a document to the default printer: </p>
<pre>
    lpr -# 2 filename
</pre>
<p> Print a double-sided legal document to a printer called &quot;foo&quot;: </p>
<pre>
    lpr -P foo -o media=legal -o sides=two-sided-long-edge filename
</pre>
<p> Print a presentation document 2-up to a printer called &quot;foo&quot;: </p>
<pre>
    lpr -P foo -o number-up=2 filename
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1), <code><a href="/docs/linux/man/1-lpq/">lpq</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
