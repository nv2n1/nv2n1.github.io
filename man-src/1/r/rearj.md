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
<dt><code>-+</code></p>
<dd> Ignore REARJ_SW variable.</p>
<dt><code>-a</code><i>[suffix]</i></p>
<dd> Convert archives within archives (&quot;*&quot; for all formats).</p>
<dt><code>-b</code><i>command</i></p>
<dd> Execute command before extracting files.</p>
<dt><code>-c</code><i>command</i></p>
<dd> Execute command on extracted files before counting them.</p>
<dt><code>-d</code></p>
<dd> Delete original archives.</p>
<dt><code>-e</code></p>
<dd> No error switch.</p>
<dt><code>-f</code></p>
<dd> Convert diskette archives.</p>
<dt><code>-g</code></p>
<dd> Skip creation of output archive.</p>
<dt><code>-i</code><i>[name]</i></p>
<dd> Check integrity of <i>rearj</i> program.</p>
<dt><code>-j</code></p>
<dd> Skip if output archive size is larger than the original.</p>
<dt><code>-k</code></p>
<dd> Skip archive timestamping.</p>
<dt><code>-l</code><i>[name]</i></p>
<dd> Write append log file (default name is <i>rearj.log</i>).</p>
<dt><code>-m</code><i>[date]</i></p>
<dd> Select archives before date in <i>YYMMDDHHMMSS</i> format.</p>
<dt><code>-n</code><i>[date]</i></p>
<dd> Select archives on or after date in <i>YYMMDDHHMMSS</i> format.</p>
<dt><code>-o</code></p>
<dd> Allow overwrite of existing target archive.</p>
<dt><code>-p</code></p>
<dd> Ignore long filenames under Windows 95.</p>
<dt><code>-q</code></p>
<dd> Query for each archive to convert.</p>
<dt><code>-r</code></p>
<dd> Recurse through subdirectories.</p>
<dt><code>-s</code></p>
<dd> Skip verify of file count and total size.</p>
<dt><code>-t</code><i>suffix</i></p>
<dd> Create suffix type archives.</p>
<dt><code>-u</code><i>[bak]</i></p>
<dd> Allow update of archive with backup (default is <i>BAK</i>).</p>
<dt><code>-v</code></p>
<dd> Execute configured command on extracted files.</p>
<dt><code>-w</code><i>dir</i></p>
<dd> Assign work directory.</p>
<dt><code>-x</code><i>[!]file</i></p>
<dd> Exclude by filename, wildname, or listfile.</p>
<dt><code>-y</code><i>[text]</i></p>
<dd> Delete output archive and write text to log (testing mode).</p>
<dt><code>-z</code></p>
<dd> Simulate operation.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>REARJ_SW</code> If set, its value will be used as command line options.</p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Success.</p>
<dt><code>1</code></p>
<dd> File not found.</p>
<dt><code>2</code></p>
<dd> File is not a configured archive type.</p>
<dt><code>3</code></p>
<dd> Target archive already exists.</p>
<dt><code>4</code></p>
<dd> Not enough disk space.</p>
<dt><code>5</code></p>
<dd> User skipped or user did not select update option.</p>
<dt><code>6</code></p>
<dd> UNPACK command error.</p>
<dt><code>7</code></p>
<dd> PACK command error.</p>
<dt><code>8</code></p>
<dd> Target cannot support directories.</p>
<dt><code>9</code></p>
<dd> Wrong file count.</p>
<dt><code>10</code></p>
<dd> Wrong total size.</p>
<dt><code>11</code></p>
<dd> Internal archive REARJ error.</p>
<dt><code>12</code></p>
<dd> Rename archive error.</p>
<dt><code>13</code></p>
<dd> Invoked -v command error (found a virus?).</p>
<dt><code>14</code></p>
<dd> Output archive is larger.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt><code>rearj * -r -d</code></p>
<dd> Convert all archives to <code>ARJ</code> format, searching all subdirectories, deleting original archives.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-arj/">arj</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Ola Lundqvist &lt;opal [at] debian.org&gt; in pod format, then converted by Guillem Jover &lt;guillem [at] debian.org&gt; to nroff format. </p>
<h2>Index</h2>
