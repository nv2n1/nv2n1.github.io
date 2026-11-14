---
title: "auvirt(8)"
name: "auvirt"
section: "8"
letter: "a"
url: "/docs/linux/man/8-auvirt/"
description: "auvirt – a program that shows data related to virtual machines"
---

<p>auvirt &#8211; a program that shows data related to virtual machines </p>
<h2>Synopsis</h2>
<p><code>auvirt</code> [ <i>OPTIONS</i> ] </p>
<h2>Description</h2>
<p><code>auvirt</code> shows a list of guest sessions found in the audit logs. If a guest is specified, only the events related to that guest is considered. To specify a guest, both UUID or VM name can be given. For each guest session the tool prints a record with the domain name, the user that started the guest, the time when the guest was started and the time when the guest was stopped. If the option &quot;&#8211;all-events&quot; is given a more detailed output is shown. In this mode other records are shown for guest&#8217;s stops, resource assignments, host shutdowns and AVC and anomaly events. The first field indicates the event type and can have the following values: start, stop, res, avc, anom and down (for host shutdowns). Resource assignments have the additional fields: resource type, reason and resource. And AVC records have the following additional fields: operation, result, command and target. By default, auvirt reads records from the system audit log file. But <code>&#8211;stdin</code> and <code>&#8211;file</code> options can be specified to change this behavior. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;all-events</code></p>
<dd>Show records for all virtualization related events.</p>
<dt><code>&#8211;debug</code></p>
<dd>Print debug messages to standard output.</p>
<dt><code>-f</code>, <code>&#8211;file</code> <i>file</i></p>
<dd>Read records from the given <i>file</i> instead from the system audit log file.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help message and exit.</p>
<dt><code>&#8211;proof</code></p>
<dd>Add after each event a line containing all the identifiers of the audit records used to calculate the event. Each identifier consists of unix time, milliseconds and serial number.</p>
<dt><code>&#8211;show-uuid</code></p>
<dd>Add the guest&#8217;s UUID to each record.</p>
<dt><code>&#8211;stdin</code></p>
<dd>Read records from the standard input instead from the system audit log file. This option cannot be specified with <code>&#8211;file</code>. The audit events must be in the raw format.</p>
<dt><code>&#8211;summary</code></p>
<dd>Print a summary with information about the events found. The summary contains the considered range of time, the number of guest starts and stops, the number of resource assignments, the number of AVC and anomaly events, the number of host shutdowns and the number of failed operations.</p>
<dt><code>-te</code>,&nbsp;<wbr><code>&#8211;end</code>&nbsp;<wbr>[<i>end-date</i>]&nbsp;<wbr>[<i>end-time</i>]</p>
<dd>Search for events with time stamps equal to or before the given end time. The format of end time depends on your locale. If the date is omitted, <code>today</code> is assumed. If the time is omitted, <code>now</code> is assumed. Use 24 hour clock time rather than AM or PM to specify time. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00. The date format accepted is influenced by the LC_TIME environmental variable. </p>
<p> You may also use the word: <code>now</code>, <code>recent</code>, <code>today</code>, <code>yesterday</code>, <code>this-week</code>, <code>week-ago</code>, <code>this-month</code>, <code>this-year</code>. <code>Today</code> means starting now. <code>Recent</code> is 10 minutes ago. <code>Yesterday</code> is 1 second after midnight the previous day. <code>This-week</code> means starting 1 second after midnight on day 0 of the week determined by your locale (see <code>localtime</code>). <code>This-month</code> means 1 second after midnight on day 1 of the month. <code>This-year</code> means the 1 second after midnight on the first day of the first month.</p>
<dt><code>-ts</code>,&nbsp;<wbr><code>&#8211;start</code>&nbsp;<wbr>[<i>start-date</i>]&nbsp;<wbr>[<i>start-time</i>]</p>
<dd>Search for events with time stamps equal to or after the given end time. The format of end time depends on your locale. If the date is omitted, <code>today</code> is assumed. If the time is omitted, <code>midnight</code> is assumed. Use 24 hour clock time rather than AM or PM to specify time. An example date using the en_US.utf8 locale is 09/03/2009. An example of time is 18:00:00. The date format accepted is influenced by the LC_TIME environmental variable. </p>
<p> You may also use the word: <code>now</code>, <code>recent</code>, <code>today</code>, <code>yesterday</code>, <code>this-week</code>, <code>this-month</code>, <code>this-year</code>. <code>Today</code> means starting at 1 second after midnight. <code>Recent</code> is 10 minutes ago. <code>Yesterday</code> is 1 second after midnight the previous day. <code>This-week</code> means starting 1 second after midnight on day 0 of the week determined by your locale (see <code>localtime</code>). <code>This-month</code> means 1 second after midnight on day 1 of the month. <code>This-year</code> means the 1 second after midnight on the first day of the first month.</p>
<dt><code>-u</code>, <code>&#8211;uuid</code> &nbsp;<wbr><i>UUID</i></p>
<dd>Only show events related to the guest with the given UUID.</p>
<dt><code>-v</code>, <code>&#8211;vm</code> &nbsp;<wbr><i>name</i></p>
<dd>Only show events related to the guest with the given name. </p>
</dl>
<h2>Examples</h2>
<p>To see all the records in this month for a guest <code>auvirt &#8211;start this-month &#8211;vm GuestVmName &#8211;all-events</code> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-aulast/">aulast</a></code>(8), <code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8). </p>
<h2>Author</h2>
<p>Marcelo Cerri</p>
