---
title: "sadc(8)"
name: "sadc"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sadc/"
description: "sadc – System activity data collector."
---

<p>sadc &#8211; System activity data collector.</p>
<h2>Synopsis</h2>
<p><code>/usr/lib/sysstat/sadc [ -C</code> <i>comment</i> <code>] [ -D ] [ -F ] [ -f ] [ -L ] [ -V ] [ -S { </code><i>keyword</i><code>[,&#8230;] | ALL | XALL } ] [</code> <i>interval </i><code>[ </code><i>count </i><code>] ] [ </code><i>outfile </i><code>]</code> </p>
<h2>Description</h2>
<p>The <code>sadc</code> command samples system data a specified number of times (<i>count</i>) at a specified interval measured in seconds (<i>interval</i>). It writes in binary format to the specified <i>outfile </i>or to standard output. If <i>outfile</i> is set to <code>&#8211;</code>, then <code>sadc</code> uses the standard system activity daily data file (see below). In this case, if the file already exists, <code>sadc</code> will overwrite it if it is from a previous month. By default <code>sadc</code> collects most of the data available from the kernel. But there are also optional metrics, for which the relevant options must be explicitly passed to <code>sadc </code>to be collected (see option <code>-S </code>below). The standard system activity daily data file is named <i>saDD </i>unless option <code>-D</code> is used, in which case its name is <i>saYYYYMMDD</i>, where <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day. By default it is located in the <i>/var/log/sysstat</i> directory. Yet it is possible to specify an alternate location for it: If <i>outfile</i> is a directory (instead of a plain file) then it will be considered as the directory where the standard system activity daily data file will be saved. When the <i>count</i> parameter is not specified, <code>sadc</code> writes its data endlessly. When both <i>interval </i>and <i>count</i> are not specified, and option <code>-C</code> is not used, a dummy record, which is used at system startup to mark the time when the counter restarts from 0, will be written. For example, one of the system startup script may write the restart mark to the daily data file by the command entry: <code>/usr/lib/sysstat/sadc &#8211;</code> The <code>sadc </code>command is intended to be used as a backend to the <code>sar </code>command. Note: The <code>sadc</code> command only reports on local activities. </p>
<h2>Options</h2>
<dl>
<dt><code>-C </code><i>comment</i></p>
<dd>When neither the <i>interval </i>nor the <i>count</i> parameters are specified, this option tells <code>sadc</code> to write a dummy record containing the specified <i>comment</i> string. This comment can then be displayed with option <code>-C </code>of <code>sar</code>.</p>
<dt><code>-D</code></p>
<dd>Use <i>saYYYYMMDD </i>instead of <i>saDD</i> as the standard system activity daily data file name.</p>
<dt><code>-F</code></p>
<dd>The creation of <i>outfile</i> will be forced. If the file already exists and has a format unknown to <code>sadc</code> then it will be truncated. This may be useful for daily data files created by an older version of <code>sadc</code> and whose format is no longer compatible with current one.</p>
<dt><code>-f</code></p>
<dd>fdatasync() will be used to ensure data is written to disk. This differs from the normal operation in that a sudden system reset is less likely to result in the <i>saDD</i> datafiles being corrupted. However, this is at the expense of performance within the <code>sadc</code> process as forward progress will be blocked while data is written to underlying disk instead of just to cache.</p>
<dt><code>-L</code></p>
<dd><code>sadc</code> will try to get an exclusive lock on the <i>outfile</i> before writing to it or truncating it. Failure to get the lock is fatal, except in the case of trying to write a normal (i.e. not a dummy and not a header) record to an existing file, in which case <code>sadc</code> will try again at the next interval. Usually, the only reason a lock would fail would be if another <code>sadc </code>process were also writing to the file. This can happen when <code>cron</code> is used to launch <code>sadc</code>. If the system is under heavy load, an old <code>sadc</code> might still be running when <code>cron</code> starts a new one. Without locking, this situation can result in a corrupted system activity file.</p>
<dt><code>-S { </code><i>keyword</i><code>[,&#8230;] | ALL | XALL }</code></p>
<dd>Possible keywords are <code>DISK</code>, <code>INT</code>, <code>IPV6</code>, <code>POWER</code>, <code>SNMP</code>, <code>XDISK</code>, <code>ALL </code>and <code>XALL</code>.<br />
 Specify which optional activities should be collected by <code>sadc</code>. Some activities are optional to prevent data files from growing too large. The <code>DISK </code>keyword indicates that <code>sadc</code> should collect data for block devices. The <code>INT </code>keyword indicates that <code>sadc</code> should collect data for system interrupts. The <code>IPV6 </code>keyword indicates that IPv6 statistics should be collected by <code>sadc</code>. The <code>POWER </code>keyword indicates that <code>sadc</code> should collect power management statistics. The <code>SNMP </code>keyword indicates that SNMP statistics should be collected by <code>sadc</code>. The <code>ALL </code>keyword is equivalent to specifying all the keywords above and therefore all previous activities are collected.</p>
<dd>The <code>XDISK </code>keyword is an extension to the <code>DISK</code> one and indicates that partitions and filesystems statistics should be collected by <code>sadc</code> in addition to disk statistics. This option works only with kernels 2.6.25 and later. The <code>XALL</code> keyword is equivalent to specifying all the keywords above (including keyword extensions) and therefore all possible activities are collected.</p>
<dd>Important note: The activities (including optional ones) saved in an existing data file prevail over those selected with option <code>-S</code>. As a consequence, appending data to an existing data file will result in option <code>-S</code> being ignored.</p>
<dt><code>-V</code></p>
<dd>Print version number then exit. </p>
</dl>
<h2>Environment</h2>
<p>The <code>sadc</code> command takes into account the following environment variable:</p>
<dl>
<dt><code>S_TIME_DEF_TIME</code></p>
<dd>If this variable exists and its value is <code>UTC </code>then <code>sadc</code> will save its data in UTC time. <code>sadc</code> will also use UTC time instead of local time to determine the current daily data file located in the <i>/var/log/sysstat</i> directory. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>/usr/lib/sysstat/sadc 1 10 /tmp/datafile</code></p>
<dd>Write 10 records of one second intervals to the <i>/tmp/datafile </i>binary file.</p>
<dt><code>/usr/lib/sysstat/sadc -C Backup Start /tmp/datafile</code></p>
<dd>Insert the comment &quot;Backup Start&quot; into the file <i>/tmp/datafile</i>. </p>
<h2>Bugs</h2>
<p>The <i>/proc</i> filesystem must be mounted for the <code>sadc </code>command to work. All the statistics are not necessarily available, depending on the kernel version used. <code>sadc</code> assumes that you are using at least a 2.6 kernel. </p>
<h2>Files</h2>
<p><i>/var/log/sysstat/saDD</i><br />
 <i>/var/log/sysstat/saYYYYMMDD</i></p>
<dl>
<dd>The standard system activity daily data files and their default location. <i>YYYY </i>stands for the current year, <i>MM </i>for the current month and <i>DD</i> for the current day.</dl>
<p> <i>/proc </i>and <i>/sys </i>contain various files with system statistics.</p>
<h2>Author</h2>
<p>Sebastien Godard (sysstat &lt;at&gt; orange.fr)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/8-sa1/">sa1</a></code>(8), <code><a href="/docs/linux/man/8-sa2/">sa2</a></code>(8), <code><a href="/docs/linux/man/1-sadf/">sadf</a></code>(1), <code><a href="/docs/linux/man/5-sysstat/">sysstat</a></code>(5) <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
