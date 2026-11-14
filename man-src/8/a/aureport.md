---
title: "aureport(8)"
name: "aureport"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aureport/"
description: "aureport – a tool that produces summary reports of audit daemon logs"
---

<p>aureport &#8211; a tool that produces summary reports of audit daemon logs</p>
<h2>Synopsis</h2>
<p><code>aureport</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>aureport</code> is a tool that produces summary reports of the audit system logs. The aureport utility can also take input from stdin as long as the input is the raw log data. The reports have a column label at the top to help with interpretation of the various fields. Except for the main summary report, all reports have the audit event number. You can subsequently lookup the full event with ausearch <code>-a</code> <i>event number</i>. You may need to specify start &amp; stop times if you get multiple hits. The reports produced by aureport can be used as building blocks for more complicated analysis. </p>
<h2>Options</h2>
<dl>
<dt><code>-au</code>,&nbsp;<wbr><code>&#8211;auth</code></p>
<dd>Report about authentication attempts</p>
<dt><code>-a</code>,&nbsp;<wbr><code>&#8211;avc</code></p>
<dd>Report about avc messages</p>
<dt><code>&#8211;comm</code></p>
<dd>Report about commands run</p>
<dt><code>-c</code>,&nbsp;<wbr><code>&#8211;config</code></p>
<dd>Report about config changes</p>
<dt><code>-cr</code>,&nbsp;<wbr><code>&#8211;crypto</code></p>
<dd>Report about crypto events</p>
<dt><code>-e</code>,&nbsp;<wbr><code>&#8211;event</code></p>
<dd>Report about events</p>
<dt><code>&#8211;escape</code>&nbsp;<wbr><i>option</i></p>
<dd>This option determines if the output is escaped to make the content safer for certain uses. The options are <i>raw</i> , <i>tty</i> , <i>shell</i> , and <i>shell_quote</i>. Each mode includes the characters of the preceding mode and escapes more characters. That is to say <i>shell</i> includes all characters escaped by <i>tty</i> and adds more. <i>tty</i> is the default.</p>
<dt><code>-f</code>,&nbsp;<wbr><code>&#8211;file</code></p>
<dd>Report about files and af_unix sockets</p>
<dt><code>&#8211;failed</code></p>
<dd>Only select failed events for processing in the reports. The default is both success and failed events.</p>
<dt><code>-h</code>,&nbsp;<wbr><code>&#8211;host</code></p>
<dd>Report about hosts</p>
<dt><code>&#8211;help</code></p>
<dd>Print brief command summary</p>
<dt><code>-i</code>,&nbsp;<wbr><code>&#8211;interpret</code></p>
<dd>Interpret numeric entities into text. For example, uid is converted to account name. The conversion is done using the current resources of the machine where the search is being run. If you have renamed the accounts, or don&#8217;t have the same accounts on your machine, you could get misleading results.</p>
<dt><code>-if</code>,&nbsp;<wbr><code>&#8211;input</code>&nbsp;<wbr><i>file</i>&nbsp;<wbr>|&nbsp;<wbr><i>directory</i></p>
<dd>Use the given <i>file</i> or <i>directory</i> instead of the logs. This is to aid analysis where the logs have been moved to another machine or only part of a log was saved.</p>
<dt><code>&#8211;input-logs</code></p>
<dd>Use the log file location from auditd.conf as input for analysis. This is needed if you are using aureport from a cron job.</p>
<dt><code>&#8211;integrity</code></p>
<dd>Report about integrity events</p>
<dt><code>-k</code>,&nbsp;<wbr><code>&#8211;key</code></p>
<dd>Report about audit rule keys</p>
<dt><code>-l</code>,&nbsp;<wbr><code>&#8211;login</code></p>
<dd>Report about logins</p>
<dt><code>-m</code>,&nbsp;<wbr><code>&#8211;mods</code></p>
<dd>Report about account modifications</p>
<dt><code>-ma</code>,&nbsp;<wbr><code>&#8211;mac</code></p>
<dd>Report about Mandatory Access Control (MAC) events</p>
<dt><code>-n</code>,&nbsp;<wbr><code>&#8211;anomaly</code></p>
<dd>Report about anomaly events. These events include NIC going into promiscuous mode and programs segfaulting.</p>
<dt><code>&#8211;node</code>&nbsp;<wbr><i>node-name</i></p>
<dd>Only select events originating from <i>node name</i> string for processing in the reports. The default is to include all nodes. Multiple nodes are allowed.</p>
<dt><code>-nc</code>,&nbsp;<wbr><code>&#8211;no-config</code></p>
<dd>Do not include the CONFIG_CHANGE event. This is particularly useful for the key report because audit rules have key labels in many cases. Using this option gets rid of these false positives.</p>
<dt><code>-p</code>,&nbsp;<wbr><code>&#8211;pid</code></p>
<dd>Report about processes</p>
<dt><code>-r</code>,&nbsp;<wbr><code>&#8211;response</code></p>
<dd>Report about responses to anomaly events</p>
<dt><code>-s</code>,&nbsp;<wbr><code>&#8211;syscall</code></p>
<dd>Report about syscalls</p>
<dt><code>&#8211;success</code></p>
<dd>Only select successful events for processing in the reports. The default is both success and failed events.</p>
<dt><code>&#8211;summary</code></p>
<dd>Run the summary report that gives a total of the elements of the main report. Not all reports have a summary.</p>
<dt><code>-t</code>,&nbsp;<wbr><code>&#8211;log</code></p>
<dd>This option will output a report of the start and end times for each log.</p>
<dt><code>&#8211;tty</code></p>
<dd>Report about tty keystrokes</p>
<dt><code>-te</code>,&nbsp;<wbr><code>&#8211;end</code>&nbsp;<wbr>[<i>end-date</i>]&nbsp;<wbr>[<i>end-time</i>]</p>
<dd>Search for events with time stamps equal to or before the given end time. The format of end time depends on your locale. If the date is omitted, <code>today</code> is assumed. If the time is omitted, <code>now</code> is assumed. Use 24 hour clock time rather than AM or PM to specify time. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00. The date format accepted is influenced by the LC_TIME environmental variable. </p>
<p> You may also use the word: <code>now</code>, <code>recent</code>, <code>boot</code>, <code>today</code>, <code>yesterday</code>, <code>this-week</code>, <code>week-ago</code>, <code>this-month</code>, <code>this-year</code>. <code>Now</code> means starting now. <code>Recent</code> is 10 minutes ago. <code>Boot</code> means the time of day to the second when the system last booted. <code>Today</code> means now. <code>Yesterday</code> is 1 second after midnight the previous day. <code>This-week</code> means starting 1 second after midnight on day 0 of the week determined by your locale (see <code>localtime</code>). <code>Week-ago</code> means 1 second after midnight exactly 7 days ago. <code>This-month</code> means 1 second after midnight on day 1 of the month. <code>This-year</code> means the 1 second after midnight on the first day of the first month.</p>
<dt><code>-tm</code>,&nbsp;<wbr><code>&#8211;terminal</code></p>
<dd>Report about terminals</p>
<dt><code>-ts</code>,&nbsp;<wbr><code>&#8211;start</code>&nbsp;<wbr>[<i>start-date</i>]&nbsp;<wbr>[<i>start-time</i>]</p>
<dd>Search for events with time stamps equal to or after the given end time. The format of end time depends on your locale. If the date is omitted, <code>today</code> is assumed. If the time is omitted, <code>midnight</code> is assumed. Use 24 hour clock time rather than AM or PM to specify time. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00. The date format accepted is influenced by the LC_TIME environmental variable. </p>
<p> You may also use the word: <code>now</code>, <code>recent</code>, <code>boot</code>, <code>today</code>, <code>yesterday</code>, <code>this-week</code>, <code>week-ago</code>, <code>this-month</code>, <code>this-year</code>. <code>Boot</code> means the time of day to the second when the system last booted. <code>Today</code> means starting at 1 second after midnight. <code>Recent</code> is 10 minutes ago. <code>Yesterday</code> is 1 second after midnight the previous day. <code>This-week</code> means starting 1 second after midnight on day 0 of the week determined by your locale (see <code>localtime</code>). <code>Week-ago</code> means starting 1 second after midnight exactly 7 days ago. <code>This-month</code> means 1 second after midnight on day 1 of the month. <code>This-year</code> means the 1 second after midnight on the first day of the first month.</p>
<dt><code>-u</code>,&nbsp;<wbr><code>&#8211;user</code></p>
<dd>Report about users</p>
<dt><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code></p>
<dd>Print the version and exit</p>
<dt><code>&#8211;virt</code></p>
<dd>Report about Virtualization events</p>
<dt><code>-x</code>,&nbsp;<wbr><code>&#8211;executable</code></p>
<dd>Report about executables </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
