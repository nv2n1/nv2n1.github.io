---
title: "eventlogadm(8)"
name: "eventlogadm"
section: "8"
letter: "e"
url: "/docs/linux/man/8-eventlogadm/"
description: "eventlogadm – push records into the Samba event log store"
---

<p>eventlogadm &#8211; push records into the Samba event log store</p>
<h2>Synopsis</h2>
<dl>
<dd>eventlogadm [<code>-s</code>] [<code>-d</code>] [<code>-h</code>] <code>-o</code>&nbsp;<wbr>addsource&nbsp;<wbr><i>EVENTLOG</i>&nbsp;<wbr><i>SOURCENAME</i>&nbsp;<wbr><i>MSGFILE</i></p>
<dd>eventlogadm [<code>-s</code>] [<code>-d</code>] [<code>-h</code>] <code>-o</code>&nbsp;<wbr>write&nbsp;<wbr><i>EVENTLOG</i></p>
<dd>eventlogadm [<code>-s</code>] [<code>-d</code>] [<code>-h</code>] <code>-o</code>&nbsp;<wbr>dump&nbsp;<wbr><i>EVENTLOG</i>&nbsp;<wbr><i>RECORD_NUMBER</i></dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/1-samba/">samba</a></code>(1) suite. </p>
<p> eventlogadm is a filter that accepts formatted event log records on standard input and writes them to the Samba event log store. Windows client can then manipulate these record using the usual administration tools.</p>
<h2>Options</h2>
<p><code>-s</code> <i>FILENAME</i></p>
<dl>
<dd>The -s option causes eventlogadm to load the configuration file given as FILENAME instead of the default one used by Samba.</dl>
<p> <code>-d</code></p>
<dl>
<dd>The -d option causes eventlogadm to emit debugging information.</dl>
<p> <code>-o</code> addsource <i>EVENTLOG</i> <i>SOURCENAME</i> <i>MSGFILE</i></p>
<dl>
<dd>The -o addsource option creates a new event log source.</dl>
<p> <code>-o</code> write <i>EVENTLOG</i></p>
<dl>
<dd>The -o write reads event log records from standard input and writes them to the Samba event log store named by EVENTLOG.</dl>
<p> <code>-o</code> dump <i>EVENTLOG</i> <i>RECORD_NUMBER</i></p>
<dl>
<dd>The -o dump reads event log records from a EVENTLOG tdb and dumps them to standard output on screen.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Print usage information.</dl>
<h2>Eventlog Record Format</h2>
<p>For the write operation, eventlogadm expects to be able to read structured records from standard input. These records are a sequence of lines, with the record key and data separated by a colon character. Records are separated by at least one or more blank line. </p>
<p> The event log record field are: </p>
<dl>
<dd>&bull; LEN &#8211; This field should be 0, since eventlogadm will calculate this value.</dl>
<dl>
<dd>&bull; RS1 &#8211; This must be the value 1699505740.</dl>
<dl>
<dd>&bull; RCN &#8211; This field should be 0.</dl>
<dl>
<dd>&bull; TMG &#8211; The time the eventlog record was generated; format is the number of seconds since 00:00:00 January 1, 1970, UTC.</dl>
<dl>
<dd>&bull; TMW &#8211; The time the eventlog record was written; format is the number of seconds since 00:00:00 January 1, 1970, UTC.</dl>
<dl>
<dd>&bull; EID &#8211; The eventlog ID.</dl>
<dl>
<dd>&bull; ETP &#8211; The event type &#8212; one of &quot;INFO&quot;, &quot;ERROR&quot;, &quot;WARNING&quot;, &quot;AUDIT SUCCESS&quot; or &quot;AUDIT FAILURE&quot;.</dl>
<dl>
<dd>&bull; ECT &#8211; The event category; this depends on the message file. It is primarily used as a means of filtering in the eventlog viewer.</dl>
<dl>
<dd>&bull; RS2 &#8211; This field should be 0.</dl>
<dl>
<dd>&bull; CRN &#8211; This field should be 0.</dl>
<dl>
<dd>&bull; USL &#8211; This field should be 0.</dl>
<dl>
<dd>&bull; SRC &#8211; This field contains the source name associated with the event log. If a message file is used with an event log, there will be a registry entry for associating this source name with a message file DLL.</dl>
<dl>
<dd>&bull; SRN &#8211; The name of the machine on which the eventlog was generated. This is typically the host name.</dl>
<dl>
<dd>&bull; STR &#8211; The text associated with the eventlog. There may be more than one string in a record.</dl>
<dl>
<dd>&bull; DAT &#8211; This field should be left unset.</dl>
<h2>Examples</h2>
<p>An example of the record format accepted by eventlogadm: </p>
<dl>
<dd>
<pre> LEN: 0
 RS1: 1699505740
 RCN: 0
 TMG: 1128631322
 TMW: 1128631322
 EID: 1000
 ETP: INFO
 ECT: 0
 RS2: 0
 CRN: 0
 USL: 0
 SRC: cron
 SRN: dmlinux
 STR: (root) CMD ( rm -f /var/spool/cron/lastrun/cron.hourly)
 DAT:</pre>
</dl>
<p> Set up an eventlog source, specifying a message file DLL: </p>
<dl>
<dd>
<pre> eventlogadm -o addsource Application MyApplication | \
 %SystemRoot%/system32/MyApplication.dll</pre>
</dl>
<p> Filter messages from the system log into an event log: </p>
<dl>
<dd>
<pre> tail -f /var/log/messages | \
 my_program_to_parse_into_eventlog_records | \
 eventlogadm SystemLogEvents</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.0.25 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
