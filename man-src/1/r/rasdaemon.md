---
title: "rasdaemon(1)"
name: "rasdaemon"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rasdaemon/"
description: "rasdaemon – RAS daemon to log the RAS events."
---

<h2>SYNOPSIS</h2>
<p> <code>rasdaemon</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> The <code>rasdaemon</code> program is a daemon which monitors the platform Reliablity, Availability and Serviceability (RAS) reports from the Linux kernel trace events. These trace events are logged in /sys/kernel/debug/tracing, reporting them via syslog/journald. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;usage</code></dt>
<dd> Display a brief usage message and exit.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a help message and exit.</dd>
<dt><code>&#8211;disable</code></dt>
<dd> Disable RAS tracing events and exit.</dd>
<dt><code>&#8211;enable</code></dt>
<dd> Enable RAS tracing events and exit.</dd>
<dt><code>&#8211;foreground</code></dt>
<dd> Executes in foreground, printing the events at console. Useful for testing it, and to be used by systemd or Unix System V respan. If not specified, the program runs in daemon mode.</dd>
<dt><code>&#8211;record</code></dt>
<dd> Record RAS events via Sqlite3. The Sqlite3 database has the benefit of keeping a persistent record of the RAS events. This feature is used with the ras-mc-ctl utility. Note that rasdaemon may be compiled without this feature.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the program version and exit. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ras-mc-ctl/">ras-mc-ctl</a></code>(8) </p>
