---
title: "rearj(1)"
name: "rearj"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rearj/"
description: "rearj – Converts other archive formats to .arj files"
---

<h2 class="name">NAME</h2>
<p> rearj &#8211; Converts other archive formats to .arj files </p>
<h2>SYNOPSIS</h2>
<p> <code>rearj</code> [<i>options</i>] &lt;<i>!listfile(s)</i>|<i>filespec(s)</i>|<i>wildname(s)</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>rearj</code> command can repackage other archive formats to arj.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-+</code></dt>
<dd> Ignore REARJ_SW variable.</dd>
<dt><code>-a</code><i>[suffix]</i></dt>
<dd> Convert archives within archives (&quot;*&quot; for all formats).</dd>
<dt><code>-b</code><i>command</i></dt>
<dd> Execute command before extracting files.</dd>
<dt><code>-c</code><i>command</i></dt>
<dd> Execute command on extracted files before counting them.</dd>
<dt><code>-d</code></dt>
<dd> Delete original archives.</dd>
<dt><code>-e</code></dt>
<dd> No error switch.</dd>
<dt><code>-f</code></dt>
<dd> Convert diskette archives.</dd>
<dt><code>-g</code></dt>
<dd> Skip creation of output archive.</dd>
<dt><code>-i</code><i>[name]</i></dt>
<dd> Check integrity of <i>rearj</i> program.</dd>
<dt><code>-j</code></dt>
<dd> Skip if output archive size is larger than the original.</dd>
<dt><code>-k</code></dt>
<dd> Skip archive timestamping.</dd>
<dt><code>-l</code><i>[name]</i></dt>
<dd> Write append log file (default name is <i>rearj.log</i>).</dd>
<dt><code>-m</code><i>[date]</i></dt>
<dd> Select archives before date in <i>YYMMDDHHMMSS</i> format.</dd>
<dt><code>-n</code><i>[date]</i></dt>
<dd> Select archives on or after date in <i>YYMMDDHHMMSS</i> format.</dd>
<dt><code>-o</code></dt>
<dd> Allow overwrite of existing target archive.</dd>
<dt><code>-p</code></dt>
<dd> Ignore long filenames under Windows 95.</dd>
<dt><code>-q</code></dt>
<dd> Query for each archive to convert.</dd>
<dt><code>-r</code></dt>
<dd> Recurse through subdirectories.</dd>
<dt><code>-s</code></dt>
<dd> Skip verify of file count and total size.</dd>
<dt><code>-t</code><i>suffix</i></dt>
<dd> Create suffix type archives.</dd>
<dt><code>-u</code><i>[bak]</i></dt>
<dd> Allow update of archive with backup (default is <i>BAK</i>).</dd>
<dt><code>-v</code></dt>
<dd> Execute configured command on extracted files.</dd>
<dt><code>-w</code><i>dir</i></dt>
<dd> Assign work directory.</dd>
<dt><code>-x</code><i>[!]file</i></dt>
<dd> Exclude by filename, wildname, or listfile.</dd>
<dt><code>-y</code><i>[text]</i></dt>
<dd> Delete output archive and write text to log (testing mode).</dd>
<dt><code>-z</code></dt>
<dd> Simulate operation.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>REARJ_SW</code> If set, its value will be used as command line options.</p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> Success.</dd>
<dt><code>1</code></dt>
<dd> File not found.</dd>
<dt><code>2</code></dt>
<dd> File is not a configured archive type.</dd>
<dt><code>3</code></dt>
<dd> Target archive already exists.</dd>
<dt><code>4</code></dt>
<dd> Not enough disk space.</dd>
<dt><code>5</code></dt>
<dd> User skipped or user did not select update option.</dd>
<dt><code>6</code></dt>
<dd> UNPACK command error.</dd>
<dt><code>7</code></dt>
<dd> PACK command error.</dd>
<dt><code>8</code></dt>
<dd> Target cannot support directories.</dd>
<dt><code>9</code></dt>
<dd> Wrong file count.</dd>
<dt><code>10</code></dt>
<dd> Wrong total size.</dd>
<dt><code>11</code></dt>
<dd> Internal archive REARJ error.</dd>
<dt><code>12</code></dt>
<dd> Rename archive error.</dd>
<dt><code>13</code></dt>
<dd> Invoked -v command error (found a virus?).</dd>
<dt><code>14</code></dt>
<dd> Output archive is larger.</dd></dl>
<h2>EXAMPLE</h2>
<dl>
<dt><code>rearj * -r -d</code></dt>
<dd> Convert all archives to <code>ARJ</code> format, searching all subdirectories, deleting original archives.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arj/">arj</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ola Lundqvist &lt;opal [at] debian.org&gt; in pod format, then converted by Guillem Jover &lt;guillem [at] debian.org&gt; to nroff format. </p>
<h2>Index</h2>
