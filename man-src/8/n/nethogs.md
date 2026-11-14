---
title: "nethogs(8)"
name: "nethogs"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nethogs/"
description: "nethogs – Net top tool grouping bandwidth per process"
---

<p>nethogs &#8211; Net top tool grouping bandwidth per process</p>
<h2>Synopsis</h2>
<p><code> nethogs</code> [<code>-h</code>] [<code>-V</code>] [<code>-d</code>] [<code>-v</code>] [<code>-t</code>] [<code>-c</code>] [<code>-p</code>] [<code>-s</code>] [device(s)]</p>
<h2>Description</h2>
<p>NetHogs is a small &#8216;net top&#8217; tool. Instead of breaking the traffic down per protocol or per subnet, like most such tools do, it groups bandwidth by process &#8211; and does not rely on a special kernel module to be loaded. So if there&#8217;s suddenly a lot of network traffic, you can fire up NetHogs and immediately see which PID is causing this, and if it&#8217;s some kind of spinning process, kill it.</p>
<h3>Options</h3>
<dl>
<dt><code>-h</code></p>
<dd>display available commands usage.</p>
<dt><code>-V</code></p>
<dd>prints Version info.</p>
<dt><code>-d</code></p>
<dd>delay for refresh rate.</p>
<dt><code>-v</code></p>
<dd>select view mode</p>
<dt><code>-p</code></p>
<dd>sniff in promiscious mode (not recommended).</p>
<dt><code>-t</code></p>
<dd>tracemode.</p>
<dt><code>-c</code></p>
<dd>limit number of refreshes</p>
<dt><code>-s</code></p>
<dd>sort by traffic sent</dl>
<p> <i>device(s)</i> to monitor. By default eth0 is being used. </p>
<h2>Interactive Control</h2>
<dl>
<dt>m</p>
<dd>cycle between display modes (kb/s, kb, b, mb)</p>
<dt>r</p>
<dd>sort by &#8216;received&#8217;</p>
<dt>s</p>
<dd>sort by &#8216;sent&#8217;</p>
<dt>q</p>
<dd>quit</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-netstat/">netstat</a>(8) <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1) <a href="/docs/linux/man/3-pcap/">pcap</a>(3)</i></p>
<h2>Author</h2>
<pre>Written by Arnout Engelen &lt;arnouten [at] bzzt.net&gt;.</pre>
