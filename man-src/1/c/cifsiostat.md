---
title: "cifsiostat(1)"
name: "cifsiostat"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cifsiostat/"
description: "cifsiostat – Report CIFS statistics."
---

<h2 class="name">NAME</h2>
<p> cifsiostat &#8211; Report CIFS statistics.</p>
<h2>SYNOPSIS</h2>
<p> <code>cifsiostat [ -h ] [ -k | -m ] [ -t ] [ -V ] [ &#8211;dec={ 0 | 1 | 2 } ] [ &#8211;human ] [ &#8211;pretty ] [</code> <i>interval </i><code>[ </code><i>count </i><code>] ]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cifsiostat</code> command displays statistics about read and write operations on CIFS filesystems. </p>
<p> The <i>interval</i> parameter specifies the amount of time in seconds between each report. The first report contains statistics for the time since system startup (boot). Each subsequent report contains statistics collected during the interval since the previous report. A report consists of a CIFS header row followed by a line of statistics for each CIFS filesystem that is mounted. The <i>count </i>parameter can be specified in conjunction with the <i>interval </i> parameter. If the <i>count </i>parameter is specified, the value of <i>count </i> determines the number of reports generated at <i>interval </i>seconds apart. If the <i>interval </i> parameter is specified without the <i>count </i>parameter, the <code>cifsiostat </code>command generates reports continuously. </p>
<h2>REPORT</h2>
<p> The CIFS report provides statistics for each mounted CIFS filesystem. The report shows the following fields: </p>
<dl>
<dt>Filesystem:</p>
<dd> This columns shows the mount point of the CIFS filesystem.</p>
<dt>rB/s (rkB/s, rMB/s)</p>
<dd> Indicate the average number of bytes (kilobytes, megabytes) read per second.</p>
<dt>wB/s (wkB/s, wMB/s)</p>
<dd> Indicate the average number of bytes (kilobytes, megabytes) written per second.</p>
<dt>rop/s</p>
<dd> Indicate the number of &#8216;read&#8217; operations that were issued to the filesystem per second.</p>
<dt>wop/s</p>
<dd> Indicate the number of &#8216;write&#8217; operations that were issued to the filesystem per second.</p>
<dt>fo/s</p>
<dd> Indicate the number of open files per second.</p>
<dt>fc/s</p>
<dd> Indicate the number of closed files per second.</p>
<dt>fd/s</p>
<dd> Indicate the number of deleted files per second. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;dec={ 0 | 1 | 2 }</code></p>
<dd> Specify the number of decimal places to use (0 to 2, default value is 2).</p>
<dt><code>-h</code></p>
<dd> This option is equivalent to specifying <code>&#8211;human &#8211;pretty</code>.</p>
<dt><code>&#8211;human</code></p>
<dd> Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g. kilobytes, sectors&#8230;) associated with the metrics.</p>
<dt><code>-k</code></p>
<dd> Display statistics in kilobytes per second.</p>
<dt><code>-m</code></p>
<dd> Display statistics in megabytes per second.</p>
<dt><code>&#8211;pretty</code></p>
<dd> Make the CIFS report easier to read by a human.</p>
<dt><code>-t</code></p>
<dd> Print the time for each report displayed. The timestamp format may depend on the value of the <code>S_TIME_FORMAT </code>environment variable (see below).</p>
<dt><code>-V</code></p>
<dd> Print version number then exit. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>cifsiostat </code>command takes into account the following environment variables:</p>
<dl>
<dt><code>S_COLORS</code></p>
<dd> By default statistics are displayed in color when the output is connected to a terminal. Use this variable to change the settings. Possible values for this variable are <code>never</code>, <code>always </code>or <code>auto </code>(the latter is equivalent to the default settings).<br />
 Please note that the color (being red, yellow, or some other color) used to display a value is not indicative of any kind of issue simply because of the color. It only indicates different ranges of values.</p>
<dt><code>S_COLORS_SGR</code></p>
<dd> Specify the colors and other attributes used to display statistics on the terminal. Its value is a colon-separated list of capabilities that defaults to <code>I=32;22:N=34;1:Z=34;22</code>. Supported capabilities are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>I=</code></p>
<dd> SGR substring for filesystem names.</p>
<dt><code>N=</code></p>
<dd> SGR substring for non-zero statistics values.</p>
<dt><code>Z=</code></p>
<dd> SGR substring for zero values.</dl>
</dl>
<dt><code>S_TIME_FORMAT</code></p>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>cifsiostat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp displayed with option <code>-t </code>will also be compliant with ISO 8601 format. </p>
</dl>
<h2>BUG</h2>
<p> <i>/proc </i>filesystem must be mounted for <code>cifsiostat </code>to work. </p>
<p> Although <code>cifsiostat</code> speaks of kilobytes (kB), megabytes (MB)&#8230;, it actually uses kibibytes (kiB), mebibytes (MiB)&#8230; A kibibyte is equal to 1024 bytes, and a mebibyte is equal to 1024 kibibytes. </p>
<h2>FILE</h2>
<p> <i>/proc/fs/cifs/Stats </i>contains CIFS statistics. </p>
<h2>AUTHORS</h2>
<p> Written by Ivana Varekova (varekova &lt;at&gt; redhat.com)<br />
 Maintained by Sebastien Godard (sysstat &lt;at&gt; orange.fr) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/1-pidstat/">pidstat</a></code>(1), <code><a href="/docs/linux/man/1-mpstat/">mpstat</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/1-tapestat/">tapestat</a></code>(1), <code><a href="/docs/linux/man/1-nfsiostat/">nfsiostat</a></code>(1) </p>
<p> <i><a rel="nofollow" href="https://github.com/sysstat/sysstat">https://github.com/sysstat/sysstat</a></i><br />
 <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
