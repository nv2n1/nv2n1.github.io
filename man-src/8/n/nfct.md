---
title: "nfct(8)"
name: "nfct"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfct/"
description: "nfct – command line tool to configure with the connection tracking system"
---

<p>nfct &#8211; command line tool to configure with the connection tracking system</p>
<h2>Synopsis</h2>
<p><code>nfct command subsystem [parameters]</code></p>
<h2>Description</h2>
<p><code>nfct</code> is the command line tool that allows to configure the Connection Tracking System.</p>
<h2>Commands</h2>
<dl>
<dt><code>list </code></p>
<dd>List the existing objects.</p>
<dt><code>add </code></p>
<dd>Add new object.</p>
<dt><code>delete </code></p>
<dd>Delete an object.</p>
<dt><code>get </code></p>
<dd>Get an existing object.</dl>
<h2>Subsys</h2>
<p>By the time this manpage has been written, the supported subsystem are <code>timeout</code></p>
<dl>
<dt><code>timeout </code></p>
<dd>The timeout subsystem allows you to define fine-grain timeout policies.</p>
<dt><code>helper </code></p>
<dd>The helper subsystem allows you to configure userspace helpers.</p>
<dt><code>version </code></p>
<dd>Displays the version information.</p>
<dt><code>help </code></p>
<dd>Displays the help message.</dl>
<h2>Example</h2>
<dl>
<dt><code>nfct add timeout test-tcp inet tcp established 100 close 10 close_wait 10</code></p>
<dd>
<dt>This creates a timeout policy for tcp using 100 seconds for the ESTABLISHED state, 10 seconds for CLOSE state and 10 seconds for the CLOSE_WAIT state.</p>
<dd>
<dt>Then, you can attach the timeout policy with the iptables CT target:</p>
<dd>
<dt><code>iptables -I PREROUTING -t raw -p tcp -j CT &#8211;timeout test-tcp</code></p>
<dd>
<dt><code>iptables -I OUTPUT -t raw -p tcp -j CT &#8211;timeout test-tcp</code></p>
<dd>
<dt>You can test that the timeout policy with:</p>
<dd>
<dt><code>conntrack -E -p tcp</code></p>
<dd>
<dt>It should display:</p>
<dd>
<dt><code>[UPDATE] tcp 6 100 ESTABLISHED src=192.168.39.100 dst=57.126.1.20 sport=56463 dport=80 src=57.126.1.20 dst=192.168.39.100 sport=80 dport=56463 [ASSURED]</code></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8),<code><a href="/docs/linux/man/8-conntrack/">conntrack</a></code>(8)</p>
<h2>Bugs</h2>
<p>Please, report them to netfilter-devel [at] vger.kernel.org or file a bug in Netfilter&#8217;s bugzilla (<a rel="nofollow" href="https://bugzilla.netfilter.org">https://bugzilla.netfilter.org</a>).</p>
<h2>Authors</h2>
<p>Pablo Neira Ayuso wrote and maintains the nfct tool. </p>
<p> Man page written by Pablo Neira Ayuso &lt;pablo [at] netfilter.org&gt;.</p>
