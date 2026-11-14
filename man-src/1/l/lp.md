---
title: "lp(1)"
name: "lp"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lp/"
description: "lp – print files"
---

<h2 class="name">NAME</h2>
<p> lp &#8211; print files </p>
<h2>SYNOPSIS</h2>
<p> <code>lp</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-c</code> ] [ <code>-d </code><i>destination</i>[<code>/</code><i>instance</i>] ] [ <code>-h </code><i>hostname</i>[<code>:</code><i>port</i>] ] [ <code>-m</code> ] [ <code>-n</code> <i>num-copies</i> ] [ <code>-o </code><i>option</i>[<code>=</code><i>value</i>] ] [ <code>-q</code> <i>priority</i> ] [ <code>-s</code> ] [ <code>-t</code> <i>title</i> ] [ <code>-H</code> <i>handling</i> ] [ <code>-P</code> <i>page-list</i> ] [ <code>&#8212;</code> ] [ <i>file(s)</i> ]<br />
 <code>lp</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-c</code> ] [ <code>-h </code><i>hostname</i>[<code>:</code><i>port</i>] ] [ <code>-i</code> <i>job-id</i> ] [ <code>-n</code> <i>num-copies</i> ] [ <code>-o </code><i>option</i>[<code>=</code><i>value</i>] ] [ <code>-q</code> <i>priority</i> ] [ <code>-t</code> <i>title</i> ] [ <code>-H</code> <i>handling</i> ] [ <code>-P</code> <i>page-list</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lp</code> submits files for printing or alters a pending job. Use a filename of &quot;-&quot; to force printing from the standard input.</p>
<h3>THE DEFAULT DESTINATION</h3>
<p> CUPS provides many ways to set the default destination. The <code>LPDEST</code> and <code>PRINTER</code> environment variables are consulted first. If neither are set, the current default set using the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command is used, followed by the default set using the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) command.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <i>lp</i>:</p>
<dl>
<dt><code>&#8212;</code></p>
<dd> Marks the end of options; use this to print a file whose name begins with a dash (-).</p>
<dt><code>-E</code></p>
<dd> Forces encryption when connecting to the server.</p>
<dt><code>-U </code><i>username</i></p>
<dd> Specifies the username to use when connecting to the server.</p>
<dt><code>-c</code></p>
<dd> This option is provided for backwards-compatibility only. On systems that support it, this option forces the print file to be copied to the spool directory before printing. In CUPS, print files are always sent to the scheduler via IPP which has the same effect.</p>
<dt><code>-d </code><i>destination</i></p>
<dd> Prints files to the named printer.</p>
<dt><code>-h </code><i>hostname</i>[<code>:</code><i>port</i>]</p>
<dd> Chooses an alternate server.</p>
<dt><code>-i </code><i>job-id</i></p>
<dd> Specifies an existing job to modify.</p>
<dt><code>-m</code></p>
<dd> Sends an email when the job is completed.</p>
<dt><code>-n </code><i>copies</i></p>
<dd> Sets the number of copies to print.</p>
<dt><code>-o &quot;</code><i>name</i><code>=</code><i>value </i>[ &#8230; <i>name</i><code>=</code><i>value </i>]<code>&quot;</code></p>
<dd> Sets one or more job options. See &quot;COMMON JOB OPTIONS&quot; below.</p>
<dt><code>-q </code><i>priority</i></p>
<dd> Sets the job priority from 1 (lowest) to 100 (highest). The default priority is 50.</p>
<dt><code>-s</code></p>
<dd> Do not report the resulting job IDs (silent mode.)</p>
<dt><code>-t &quot;</code><i>name</i><code>&quot;</code></p>
<dd> Sets the job name.</p>
<dt><code>-H </code><i>hh:mm</i></p>
<dd>
<dt><code>-H hold</code></p>
<dd>
<dt><code>-H immediate</code></p>
<dd>
<dt><code>-H restart</code></p>
<dd>
<dt><code>-H resume</code></p>
<dd> Specifies when the job should be printed. A value of <i>immediate</i> will print the file immediately, a value of <i>hold</i> will hold the job indefinitely, and a UTC time value (HH:MM) will hold the job until the specified UTC (not local) time. Use a value of <i>resume</i> with the <i>-i</i> option to resume a held job. Use a value of <i>restart</i> with the <i>-i</i> option to restart a completed job.</p>
<dt><code>-P </code><i>page-list</i></p>
<dd> Specifies which pages to print in the document. The list can contain a list of numbers and ranges (#-#) separated by commas, e.g., &quot;1,3-5,16&quot;. The page numbers refer to the output pages and not the document&#8217;s original pages &#8211; options like &quot;number-up&quot; can affect the numbering of the pages.</dl>
<h3>COMMON JOB OPTIONS</h3>
<p> Aside from the printer-specific options reported by the <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1) command, the following generic options are available:</p>
<dl>
<dt><code>-o job-sheets=</code><i>name</i></p>
<dd> Prints a cover page (banner) with the document. The &quot;name&quot; can be &quot;classified&quot;, &quot;confidential&quot;, &quot;secret&quot;, &quot;standard&quot;, &quot;topsecret&quot;, or &quot;unclassified&quot;.</p>
<dt><code>-o media=</code><i>size</i></p>
<dd> Sets the page size to <i>size</i>. Most printers support at least the size names &quot;a4&quot;, &quot;letter&quot;, and &quot;legal&quot;.</p>
<dt><code>-o number-up=</code>{<i>2|4|6|9|16</i>}</p>
<dd> Prints 2, 4, 6, 9, or 16 document (input) pages on each output page.</p>
<dt><code>-o orientation-requested=4</code></p>
<dd> Prints the job in landscape (rotated 90 degrees counter-clockwise).</p>
<dt><code>-o orientation-requested=5</code></p>
<dd> Prints the job in landscape (rotated 90 degrees clockwise).</p>
<dt><code>-o orientation-requested=6</code></p>
<dd> Prints the job in reverse portrait (rotated 180 degrees).</p>
<dt><code>-o print-quality=3</code></p>
<dd>
<dt><code>-o print-quality=4</code></p>
<dd>
<dt><code>-o print-quality=5</code></p>
<dd> Specifies the output quality &#8211; draft (3), normal (4), or best (5).</p>
<dt><code>-o sides=one-sided</code></p>
<dd> Prints on one side of the paper.</p>
<dt><code>-o sides=two-sided-long-edge</code></p>
<dd> Prints on both sides of the paper for portrait output.</p>
<dt><code>-o sides=two-sided-short-edge</code></p>
<dd> Prints on both sides of the paper for landscape output.</dl>
<h2>CONFORMING TO</h2>
<p> Unlike the System V printing system, CUPS allows printer names to contain any printable character except SPACE, TAB, &quot;/&quot;, or &quot;#&quot;. Also, printer and class names are <i>not</i> case-sensitive. </p>
<p> The <i>-q</i> option accepts a different range of values than the Solaris lp command, matching the IPP job priority values (1-100, 100 is highest priority) instead of the Solaris values (0-39, 0 is highest priority).</p>
<h2>EXAMPLES</h2>
<p> Print two copies of a document to the default printer: </p>
<pre>
    lp -n 2 filename
</pre>
<p> Print a double-sided legal document to a printer called &quot;foo&quot;: </p>
<pre>
    lp -d foo -o media=legal -o sides=two-sided-long-edge filename
</pre>
<p> Print a presentation document 2-up to a printer called &quot;bar&quot;: </p>
<pre>
    lp -d bar -o number-up=2 filename
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpoptions/">lpoptions</a></code>(1), <code><a href="/docs/linux/man/1-lpq/">lpq</a></code>(1), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), <code><a href="/docs/linux/man/1-lpstat/">lpstat</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
