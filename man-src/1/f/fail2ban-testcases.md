---
title: "fail2ban-testcases(1)"
name: "fail2ban-testcases"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fail2ban-testcases/"
description: "fail2ban-testcases – run Fail2Ban unit-tests"
---

<h2>NAME</h2>
<p> fail2ban-testcases &#8211; run Fail2Ban unit-tests</p>
<h2>SYNOPSIS</h2>
<p> <code>fail2ban-testcases</code> [<i>,OPTIONS/</i>] [<i>,regexps/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Script to run Fail2Ban tests battery</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-l</code> LOG_LEVEL, <code>&#8211;log-level</code>=<i>,LOG_LEVEL/</i></p>
<dd> Log level for the logger to use during running tests</p>
<dt><code>-n</code>, <code>&#8211;no-network</code></p>
<dd> Do not run tests that require the network</p>
<dt><code>-t</code>, <code>&#8211;log-traceback</code></p>
<dd> Enrich log-messages with compressed tracebacks</p>
<dt><code>&#8211;full-traceback</code></p>
<dd> Either to make the tracebacks full, not compressed (as by default)</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fail2ban-client/">fail2ban-client</a>(1) <a href="/docs/linux/man/1-fail2ban-server/">fail2ban-server</a>(1) <a href="/docs/linux/man/1-fail2ban-regex/">fail2ban-regex</a>(1) </p>
<h2>Index</h2>
