---
title: "lpr-cups(1)"
name: "lpr-cups"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpr-cups/"
description: "lpr – print files"
---

<h2>NAME</h2>
<p> lpr &#8211; print files</p>
<h2>SYNOPSIS</h2>
<p> <code>lpr</code> [ -E ] [ -H <i>server[:port]</i> ] [ -U <i>username</i> ] [ -P <i>destination[/instance]</i> ] [ -# <i>num-copies</i> [ -h ] [ -l ] [ -m ] [ -o <i>option[=value]</i> ] [ -p] [ -q ] [ -r ] [ -C/J/T <i>title</i> ] [ <i>file(s)</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>lpr</i> submits files for printing. Files named on the command line are sent to the named printer (or the default destination if no destination is specified). If no files are listed on the command-line, <i>lpr</i> reads the print file from the standard input.</p>
<h2>THE DEFAULT DESTINATION</h2>
<p> CUPS provides many ways to set the default destination. The &quot;LPDEST&quot; and &quot;PRINTER&quot; environment variables are consulted first. If neither are set, the current default set using the <i><a href="/docs/linux/man/1-lpoptions/">lpoptions</a>(1)</i> command is used, followed by the default set using the <i><a href="/docs/linux/man/8-lpadmin/">lpadmin</a>(8)</i> command.</p>
<h2>OPTIONS</h2>
<p> The following options are recognized by <i>lpr</i>:</p>
<dl>
<dt>-E</p>
<dd>
 Forces encryption when connecting to the server.</p>
<dt>-H server[:port]</p>
<dd>
 Specifies an alternate server.</p>
<dt>-C &quot;name&quot;</p>
<dd>
<dt>-J &quot;name&quot;</p>
<dd>
<dt>-T &quot;name&quot;</p>
<dd>
 Sets the job name.</p>
<dt>-P destination[/instance]</p>
<dd>
 Prints files to the named printer.</p>
<dt>-U username</p>
<dd>
 Specifies an alternate username.</p>
<dt>-# <i>copies</i></p>
<dd>
 Sets the number of copies to print from 1 to 100.</p>
<dt>-h</p>
<dd>
 Disables banner printing. This option is equivalent to &quot;-o job-sheets=none&quot;.</p>
<dt>-l</p>
<dd>
 Specifies that the print file is already formatted for the destination and should be sent without filtering. This option is equivalent to &quot;-o raw&quot;.</p>
<dt>-m</p>
<dd>
 Send an email on job completion.</p>
<dt>-o option[=value]</p>
<dd>
 Sets a job option.</p>
<dt>-p</p>
<dd>
 Specifies that the print file should be formatted with a shaded header with the date, time, job name, and page number. This option is equivalent to &quot;-o prettyprint&quot; and is only useful when printing text files.</p>
<dt>-q</p>
<dd>
 Hold job for printing.</p>
<dt>-r</p>
<dd>
 Specifies that the named print files should be deleted after printing them.</dl>
<h2>COMPATIBILITY</h2>
<p> The &quot;c&quot;, &quot;d&quot;, &quot;f&quot;, &quot;g&quot;, &quot;i&quot;, &quot;n&quot;, &quot;t&quot;, &quot;v&quot;, and &quot;w&quot; options are not supported by CUPS and produce a warning message if used.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-cancel/">cancel</a>(1)</i>, <i><a href="/docs/linux/man/1-lp/">lp</a>(1)</i>, <i><a href="/docs/linux/man/8-lpadmin/">lpadmin</a>(8)</i>, <i><a href="/docs/linux/man/1-lpoptions/">lpoptions</a>(1)</i>, <i><a href="/docs/linux/man/1-lpq/">lpq</a>(1)</i>, <i><a href="/docs/linux/man/1-lprm/">lprm</a>(1)</i>, <i><a href="/docs/linux/man/1-lpstat/">lpstat</a>(1)</i>,<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2007-2013 by Apple Inc. </p>
<h2>Index</h2>
