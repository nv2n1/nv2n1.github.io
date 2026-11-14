---
title: "smtpping(1)"
name: "smtpping"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smtpping/"
description: "smtpping – SMTP benchmarking and measurement tool"
---

<h2>NAME</h2>
<p> <code>smtpping</code> &#8211; SMTP benchmarking and measurement tool</p>
<h2>SYNOPSIS</h2>
<p> [-<code>dqrJ46</code> ] [-<code>p </code><i>port</i> ] [-<code>w </code><i>wait</i> ] [-<code>c </code><i>count</i> ] [-<code>P </code><i>parallell</i> ] [-<code>s </code><i>size</i> ] [-<code>f </code><i>file</i> ] [-<code>H </code><i>hello</i> ] [-<code>S </code><i>sender</i> ] <i>recipient</i> [<i>@server</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a small tool that performs SMTP server delay, delay variation and throughput measurements. </p>
<p> It must be invoked with the <i>recipient</i> email address. Normally, the <i>server</i> should also be specified (prefixed with @); otherwise will try to find the recipient domain&#8217;s MX record, falling back on A/AAAA records. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-4</code></p>
<dd> Use IPv4.</p>
<dt><code>-6</code></p>
<dd> Use IPv6.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Specifies the TCP port to use (default: 25).</p>
<dt><code>-w </code><i>wait</i></p>
<dd> Time in milliseconds to wait between pings (default: 1000).</p>
<dt><code>-c </code><i>count</i></p>
<dd> Number of pings to send (default: unlimited).</p>
<dt><code>-P </code><i>processes</i></p>
<dd> Number of parallell worker processes (default: 1). To measure throughput, it&#8217;s recommended to use &#8211;<code>r</code> and &#8211;<code>w0</code> with this option.</p>
<dt><code>-s </code><i>size</i></p>
<dd> Ping message size in kilobytes (default: 10). Cannot be used in conjunction with the &#8211;<code>f</code> option.</p>
<dt><code>-f </code><i>file</i></p>
<dd> Send the specified email file (message/rfc822) instead of a generated message. Cannot be used in conjunction with the &#8211;<code>s</code> option.</p>
<dt><code>-H </code><i>helo</i></p>
<dd> HELO name (default: localhost.localdomain).</p>
<dt><code>-S </code><i>sender</i></p>
<dd> Sender address (default: &lt;&gt;).</p>
<dt><code>-r</code></p>
<dd> Display rate instead of transaction delays. To measure throughput, it&#8217;s recommended to use &#8211;<code>w0</code> and possibly &#8211;<code>P</code> with this option.</p>
<dt><code>-q</code></p>
<dd> Display less verbose output.</p>
<dt><code>-d</code></p>
<dd> Display more verbose output.</dl>
<h2>AUTHORS</h2>
<p> An -nosplit The program was written by An Anders Berggren Aq Mt anders [at] desh.se and An Erik Lax Aq Mt erik [at] datahack.se for Halon Security AB. </p>
<h2>Index</h2>
