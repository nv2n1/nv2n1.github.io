---
title: "timezone(5)"
name: "timezone"
section: "5"
letter: "t"
url: "/docs/linux/man/5-timezone/"
description: "timezone – Local time zone configuration file"
---

<p>timezone &#8211; Local time zone configuration file</p>
<h2>Synopsis</h2>
<p>/etc/timezone</p>
<h2>Description</h2>
<p>The /etc/timezone file configures the system-wide time zone of the local system that is used by applications for presentation to the user. It should contain a single newline-terminated line consisting of a time zone identifier such as Europe/Berlin. The file /etc/localtime corresponds with /etc/timezone and contains the binary time zone data for the time zone. These files should always be changed simultaneously and kept in sync. </p>
<p> The time zone may be overridden for individual programs by using the TZ environment variable. See <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<h2>History</h2>
<p>The simple configuration file format of /etc/timezone originates from Debian GNU/Linux.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)</p>
<h2>Author</h2>
<p><code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dd>Developer</dl>
