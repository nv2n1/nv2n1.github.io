---
title: "fetchlog(1)"
name: "fetchlog"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fetchlog/"
description: "fetchlog – fetch and convert new messages of a logfile"
---

<h2>NAME</h2>
<p> fetchlog &#8211; fetch and convert new messages of a logfile</p>
<h2>SYNOPSIS</h2>
<p> <code>fetchlog</code> -f <i>first:last:len:conv</i> <i>logfile</i> <i>bookmarkfile</i> [ <i>pattern ..</i> ] </p>
<p> <code>fetchlog</code> -F <i>first:last:len:conv</i> <i>logfile</i> <i>bookmarkfile</i> [ <i>pattern ..</i> ] </p>
<p> <code>fetchlog</code> [<code>-h</code>|<code>-V</code>] </p>
<h2>DESCRIPTION</h2>
<p> The <i>fetchlog </i> utility displays the last new messages of a logfile. It is similar like <i><a href="/docs/linux/man/1-tail/">tail</a></i>(1) but offers some extra functionality for output formatting. To show only the new messages appeared since the last call <i>fetchlog </i> uses a bookmark to remember which messages have been fetched. </p>
<p> <i>fetchlog </i> scans backwards <i>logfile</i> and collects all messages, optionally only those matching any of the given regex-style patterns. Then <i>fetchlog </i> converts found message lines for output. It stops scanning when one of these conditions become true: The bookmark from <i>bookmarkfile</i> is reached, or <i>len</i> characters are ready for output, or an error occurs. <i>fetchlog</i> knows about rotated and uncompressed logfiles and continues scanning in rotated logfiles by appending &#8216;.0&#8217;, &#8216;.1&#8217; upto &#8216;.9&#8217; to <i>logfile</i> when scanning in rotated logfiles. Scanning stops without error when a rotated logfile does not exist. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> do not update bookmark in <i>bookmarkfile.</i></p>
<dt><code>-F</code></p>
<dd> update bookmark in <i>bookmarkfile</i> : set bookmark to the very last line fetched from <i>logfile</i></p>
<dt><code>first</code></p>
<dd> The first column of text <i>fetchlog </i> will read from <i>logfile.</i> Lines shorter than <i>first</i> will be show up as a single newline. The column count starts with 1.</p>
<dt><code>last</code></p>
<dd> The maximum last column <i>fetchlog</i> will read from <i>logfile.</i> Lines longer than <i>last</i> will be cut off and a `~` will be set at column <i>last</i> for output. The column count starts with 1.</p>
<dt><code>len</code></p>
<dd> The maximum number of characters <i>fetchlog</i> will output. If more than <i>len</i> characters are available after cutting and conversion, the first line put out will start with &#8216;&#8230;&#8217;.</p>
<dt><code>conv</code></p>
<dd> Conversion: one ore more of characters &#8216;bpsno&#8217;.</p>
<dt>
<dd> <code>b</code> [brackets] convert &#8216;&lt;&#8216; and &#8216;&gt;&#8217; to &#8216;(&#8216; and &#8216;)&#8217; for safe HTML output.</p>
<dt>
<dd> <code>p</code> [percent] convert &#8216;%&#8217; to &#8216;p&#8217; for safe <i><a href="/docs/linux/man/1-printf/">printf</a></i>(1) output.</p>
<dt>
<dd> <code>s</code> [shell] convert &#8216;$&#8217;, &#8216;^&#8217;, and the three quotes (backquote, doublequote, singlequote) and &#8216;|&#8217; to &#8216;_&#8217; and &#8216;\&#8217; to &#8216;/&#8217;. This conversion is useful when passing the result of <i>fetchlog</i> to a shell command as a parameter.</p>
<dt>
<dd> <code>n</code> [newline] convert newline characters to &#8216;
&#8217; sequence to get a single line of output.</p>
<dt>
<dd> <code>o</code> [ok message] Show &#8216;OK: no messages&#8217; if no new messages are available for output.</p>
<dt><code>logfile</code></p>
<dd> Absolute path to the unrotated logfile to fetch data from. The user needs read access to <i>logfile.</i></p>
<dt><code>bookmarkfile</code></p>
<dd> Absolute path to the file holding the bookmark. The user needs read access to the file when using option <code>-f</code> and write access plus permission to create files in the directory of <i>bookarkfile</i> when using option <code>-F</code> (update bookmark).</p>
<dt>
<dd> If <i>bookmarkfile </i> does not exist <i>fetchlog </i> assumes an infinite old bookmark.</p>
<dt><code>pattern</code></p>
<dd> A extended regular expression pattern, see <i><a href="/docs/linux/man/7-re_format/">re_format</a></i>(7) for details. If one or more <i>pattern</i> are defined, <i>fetchlog</i> will only pick lines where any of these <i>pattern</i> match. Pattern matching is done after trimming the lines with respect to <i>first</i> and <i>last</i> and before any conversions takes place. In other words: pattern matching operates on data that <i>fetchlog </i> shows when no conversion is set.</p>
<dt>
<dt><code>-h</code></p>
<dd>
<dd> print help message</p>
<dt><code>-V</code></p>
<dd> print version</dl>
<h2>MULTIPLE FETCHING</h2>
<p> Fetching the same logfile with different bookmarks works without problem. Simultanously fetching with option <code>-F</code> (update mode) using the same bookmark file works too, but unpredictable results will occur. For safety reasons <i>bookmarkfile </i> will never be opened for writing directly, instead a temporary file will be used and renamed to <i>bookmarkfile </i> when writing has finished. </p>
<h2>PERFORMANCE</h2>
<p> Before opening logfiles for scanning <i>fetchlog</i> first checks the modification time of <i>logfile</i> and compares this time with the modification time stored in <i>bookmarkfile.</i> If both timestamps are the same then <i>fetchlog</i> exits with 0 (no messages). Otherwise the logfile(s) get mapped to memory step by step and are scanned backwards line by line until one of the end conditions become true. <i>fetchlog</i> uses the logfiles inode to distinguish different logs. </p>
<h2>NAGIOS</h2>
<p> <i>fetchlog</i> may be used as a local plugin for the <i>Nagios </i> network monitoring system to monitor a local logfile. It follows the calling convention for Nagios plugins if at least conversions <code>on</code> are set and <i>len</i> is &#8216;short&#8217; enough for Nagios. It is recommended to use conversion <code>s</code> also because shell metacharacters in fetched messages may confuse Nagios&#8217; notification system. </p>
<p> When using <i>fetchlog</i> as a local plugin for Nagios then return status is as follows:</p>
<dl>
<dt><code>OK</code></p>
<dd> No new messages in <i>logfile </i> where found. The single line &#8216;OK: no messages&#8217; will be send to stdout.</p>
<dt><code>WARNING</code></p>
<dd> <i>fetchlog</i> detected an internal error while fetching. A one line error message starting with &#8216;ERROR: fetchlog:&#8217; is send to stdout.</p>
<dt><code>CRITICAL</code></p>
<dd> New messages in <i>logfile </i> where found. A single line with the last new messages will be send to stdout.</p>
<dt><code>UNKNOWN</code></p>
<dd> <i>fetchlog</i> was called with wrong parameters. A multiline usage message is send to stdout.</dl>
<p> <i>Nagios</i> can monitor remote logfiles together with NET-SNMP and <i>fetchlog </i> using the check-snmp plugin. Please read the README files coming with fetchlog how to setup this. </p>
<h2>SNMP</h2>
<p> The motivation for <i>fetchlog</i> was to create a helper tool for NET-SNMP&#8217;s <i>snmpd </i> to enable monitoring of remote kernel syslogs using SNMP. If configured properly, <i>snmpd </i> replies to a specific SNMP request with the output of an external helper program. With <i>fetchlog</i> using update mode <code>-F </code> and conversions <code>on</code> one can peek at a remote syslog file and gets either &#8216;OK: no messages&#8217; or one line with the new syslog messages appeared since the last SNMP request. </p>
<p> Because of some limitiations of SNMP itself and the monitoring applications using SNMP, the length of the SNMP reply must not exceed a specific size. To ease the integration of SNMP in monitoring software it is useful to have the SNMP reply only consist of a single line of text rather than multiple lines. </p>
<h2>COMPRESSING OUTPUT</h2>
<p> The syslog messages fetched can be compressed by increasing <i>first</i> to skip the timestamp and host entry from syslog. Lowering <i>last</i> gives even more compression for long syslog lines. As a result one gets a very short message that gives an idea of what is going wrong. </p>
<h2>DIAGNOSTICS</h2>
<p> <i>fetchlog</i> sends all output and error messages to stdout. Exit codes:</p>
<dl>
<dt><code>0</code></p>
<dd> No new messages in <i>logfile </i> were found. If conversion <i>o</i> is set, the single line &#8216;OK: no messages&#8217; will be send to stdout.</p>
<dt><code>1</code></p>
<dd> An internal error in <i>fetchlog </i> occured. A one line error message will be send to stdout. The error message starts with &#8216;ERROR: fetchlog:&#8217; and shows detailed information about what went wrong. Length limitation by parameter <i>len </i> is applied, if an error message is too long the last part will be cut off and a &#8216;~&#8217; is appended.</p>
<dt><code>2</code></p>
<dd> New messages in <i>logfile</i> were found. The new messages will be send to stdout. If conversion <i>n</i> is set, a single line of text is send, else zero or more lines of converted syslog messages are send.</p>
<dt><code>3</code></p>
<dd> <i>fetchlog </i> was called with wrong parameters, a multiline usage message is print to stdout.</dl>
<p> Note: Since version 0.93 the meanings of exit code 1 and 2 have been exchanged. </p>
<h2>AUTHOR</h2>
<p> Alexander Haderer, LoeScap Technology GmbH, Berlin &#8211; Germany </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-tail/">tail</a></i>(1), <i><a href="/docs/linux/man/1-cat/">cat</a></i>(1), <i><a href="/docs/linux/man/1-head/">head</a></i>(1), <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1), <i><a href="/docs/linux/man/7-re_format/">re_format</a></i>(7), <i><a href="/docs/linux/man/8-syslogd/">syslogd</a></i>(8), <i><a href="/docs/linux/man/8-newsyslog/">newsyslog</a></i>(8) </p>
<p> NET-SNMP &#8211; Various tools relating to the Simple Network Management Protocol SNMP (NET-SNMP: formerly known as UCD-SNMP)<br />
 <a rel="nofollow" href="http://www.net-snmp.org">http://www.net-snmp.org</a> </p>
<p> Nagios &#8211; A Network monitoring system<br />
 <a rel="nofollow" href="http://www.nagios.org">http://www.nagios.org</a> </p>
<p> Nagios Plugins &#8211; Plugins for Nagios<br />
 <a rel="nofollow" href="http://nagiosplug.sourceforge.net">http://nagiosplug.sourceforge.net</a> </p>
<p> fetchlog homepage &#8211; download, support and bugtracking<br />
 <a rel="nofollow" href="http://fetchlog.sourceforge.net">http://fetchlog.sourceforge.net</a> </p>
<h2>BUGS</h2>
<p> Bookmarkfiles are not portable across plattforms or fetchlog versions. </p>
<p> Logfiles are expected not to shrink. </p>
<p> <i>fetchlog</i> does not work with compressed logfiles. </p>
<p> Fetching when logfile rotation takes place may result in some messages to appear twice. </p>
<p> If an regex error occurs during pattern matching this error is silently ignored and will be handled as non-match. </p>
<h2>LEGAL</h2>
<p> Nagios is a registered trademark of Ethan Galstad. </p>
<h2>Index</h2>
