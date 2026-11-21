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
<p> [-<code>dqrJ46</code> ] [-<code>p </code><i>port</i> ] [-<code>w </code><i>wait</i> ] [-<code>c </code><i>count</i> ] [-<code>P </code><i>parallell</i> ] [-<code>s </code><i>size</i> ] [-<code>f </code><i>file</i> ] [-<code>H </code><i>hello</i> ] [-<code>S </code><i>sender</i> ] <i>recipient</i> [<i>@server</i> ]</p>
<p> is a small tool that performs SMTP server delay, delay variation and throughput measurements. </p>
<p> It must be invoked with the <i>recipient</i> email address. Normally, the <i>server</i> should also be specified (prefixed with @); otherwise will try to find the recipient domain&#8217;s MX record, falling back on A/AAAA records. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-4</code></dt>
<dd> Use IPv4.</dd>
<dt><code>-6</code></dt>
<dd> Use IPv6.</dd>
<dt><code>-p </code><i>port</i></dt>
<dd> Specifies the TCP port to use (default: 25).</dd>
<dt><code>-w </code><i>wait</i></dt>
<dd> Time in milliseconds to wait between pings (default: 1000).</dd>
<dt><code>-c </code><i>count</i></dt>
<dd> Number of pings to send (default: unlimited).</dd>
<dt><code>-P </code><i>processes</i></dt>
<dd> Number of parallell worker processes (default: 1). To measure throughput, it&#8217;s recommended to use &#8211;<code>r</code> and &#8211;<code>w0</code> with this option.</dd>
<dt><code>-s </code><i>size</i></dt>
<dd> Ping message size in kilobytes (default: 10). Cannot be used in conjunction with the &#8211;<code>f</code> option.</dd>
<dt><code>-f </code><i>file</i></dt>
<dd> Send the specified email file (message/rfc822) instead of a generated message. Cannot be used in conjunction with the &#8211;<code>s</code> option.</dd>
<dt><code>-H </code><i>helo</i></dt>
<dd> HELO name (default: localhost.localdomain).</dd>
<dt><code>-S </code><i>sender</i></dt>
<dd> Sender address (default: &lt;&gt;).</dd>
<dt><code>-r</code></dt>
<dd> Display rate instead of transaction delays. To measure throughput, it&#8217;s recommended to use &#8211;<code>w0</code> and possibly &#8211;<code>P</code> with this option.</dd>
<dt><code>-q</code></dt>
<dd> Display less verbose output.</dd>
<dt><code>-d</code></dt>
<dd> Display more verbose output.</dd></dl>
<h2>AUTHORS</h2>
<p> An -nosplit The program was written by An Anders Berggren Aq Mt anders [at] desh.se and An Erik Lax Aq Mt erik [at] datahack.se for Halon Security AB. </p>
