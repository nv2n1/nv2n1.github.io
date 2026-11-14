---
title: "rtmon(8)"
name: "rtmon"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtmon/"
description: "rtmon – listens to and monitors RTnetlink"
---

<p>rtmon &#8211; listens to and monitors RTnetlink</p>
<h2>Synopsis</h2>
<p><code>rtmon</code> [ options ] file FILE [ all | LISTofOBJECTS ]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>rtmon</code> command. <code>rtmon</code> listens on <i>netlink</i> socket and monitors routing table changes. <i>rtmon</i> can be started before the first network configuration command is issued. For example if you insert: <code>rtmon file /var/log/rtmon.log</code> in a startup script, you will be able to view the full history later. Certainly, it is possible to start rtmon at any time. It prepends the history with the state snapshot dumped at the moment of starting. </p>
<h2>Options</h2>
<p><i>rtmon supports the following options:</i></p>
<dl>
<dt><code>-Version</code></p>
<dd>Print version and exit.</p>
<dt><code>help</code></p>
<dd>Show summary of options.</p>
<dt><code>file FILE [ all | LISTofOBJECTS ]</code></p>
<dd>Log output to FILE. LISTofOBJECTS is the list of object types that we want to monitor. It may contain &#8216;link&#8217;, &#8216;address&#8217;, &#8216;route&#8217; and &#8216;all&#8217;. &#8216;link&#8217; specifies the network device, &#8216;address&#8217; the protocol (IP or IPv6) address on a device, &#8216;route&#8217; the routing table entry and &#8216;all&#8217; does what the name says.</p>
<dt><code>-family [ inet | inet6 | link | help ]</code></p>
<dd>Specify protocol family. &#8216;inet&#8217; is IPv4, &#8216;inet6&#8217; is IPv6, &#8216;link&#8217; means that no networking protocol is involved and &#8216;help&#8217; prints usage information.</p>
<dt><code>-4</code></p>
<dd>Use IPv4. Shortcut for -family inet.</p>
<dt><code>-6</code></p>
<dd>Use IPv6. Shortcut for -family inet6.</p>
<dt><code>-0</code></p>
<dd>Use a special family identifier meaning that no networking protocol is involved. Shortcut for -family link.</dl>
<h2>Usage Examples</h2>
<dl>
<dt><code># rtmon file /var/log/rtmon.log</code></p>
<dd>Log to file /var/log/rtmon.log, then run:</p>
<dt><code># ip monitor file /var/log/rtmon.log</code></p>
<dd>to display logged output from file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p><code>rtmon</code> was written by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;. </p>
<p> This manual page was written by Michael Prokop &lt;mika [at] grml.org&gt;, for the Debian project (but may be used by others).</p>
