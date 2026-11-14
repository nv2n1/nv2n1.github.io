---
title: "cjdnslog(1)"
name: "cjdnslog"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cjdnslog/"
description: "cjdnslog — display cjdroute log messages"
---

<h2>NAME</h2>
<p> <code>cjdnslog</code> &#8212; display cjdroute log messages</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/cjdnslog</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdroute sends continuous log messages to the bit bucket. Cjdnslog captures that information in real time and sends it to stdout.</p>
<h2>OPTIONS</h2>
<p> With no options, cjdnslog logs everything.</p>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code> Print usage summary.</p>
<dt>&bull;</p>
<dd> <code>-f source_file.c</code> Restrict output to log messages generated in source_file.c.</p>
<dt>&bull;</p>
<dd> <code>-v log_level</code> Restrict output to messages at log_level or higher. Log levels include DEBUG, INFO, WARN, ERROR.</p>
<dt>&bull;</p>
<dd> <code>-l lineno</code> Restrict output to message generated on source line lineno. Normally used in conjunction with <code>-f</code>.</p>
<dt>
<dd></dl>
<h2>USAGE</h2>
<p> Running cjdnslog requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>FILES</h2>
<p> <code>~/.cjdnsadmin</code></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) <a href="/docs/linux/man/1-cjdnslog/">cjdnslog</a>(1) &#8212; display cjdroute log messages =============================================</p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/cjdnslog</code> [&lt;options&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Cjdroute has numerous log points. Cjdnslog enables and taps selected log points and sends the resulting log messages to stdout.</p>
<h2>OPTIONS</h2>
<p> With no options, cjdnslog logs everything.</p>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code> Print usage summary.</p>
<dt>&bull;</p>
<dd> <code>-f source_file.c</code> Restrict output to log messages generated in source_file.c.</p>
<dt>&bull;</p>
<dd> <code>-v log_level</code> Restrict output to messages at log_level or higher. Log levels include DEBUG, INFO, WARN, ERROR.</p>
<dt>&bull;</p>
<dd> <code>-l lineno</code> Restrict output to message generated on source line lineno. Normally used in conjunction with <code>-f</code>.</p>
<dt>
<dd></dl>
<h2>USAGE</h2>
<p> Running cjdnslog requires admin privilege. The cjdnsadmin lib will try to read <code>/etc/cjdroute.conf</code> for the admin password. This will normally succeed only for root. Otherwise, it tries <code>~/.cjdnsadmin</code></p>
<h2>FILES</h2>
<p> <code>~/.cjdnsadmin</code></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cjdroute/">cjdroute</a>(1) </p>
<h2>Index</h2>
