---
title: "dnsspoof(8)"
name: "dnsspoof"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnsspoof/"
description: "dnsspoof – forge replies to DNS address / pointer queries"
---

<p>dnsspoof &#8211; forge replies to DNS address / pointer queries</p>
<h2>Synopsis</h2>
<p><code>dnsspoof</code> [<code>-i </code><i>interface</i>] [<code>-f </code><i>hostsfile</i>] [<i>expression</i>]</p>
<h2>Description</h2>
<p><code>dnsspoof</code> forges replies to arbitrary DNS address / pointer queries on the LAN. This is useful in bypassing hostname-based access controls, or in implementing a variety of man-in-the-middle attacks.</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to use.</p>
<dt><code>-f </code><i>hostsfile</i></p>
<dd>Specify the pathname of a file in <a href="/docs/linux/man/5-hosts/">hosts</a>(5) format. Only one hostname allowed per line (no aliases), although hostnames may contain wildcards (such as <i>*.doubleclick.net</i>).</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select traffic to sniff.</dl>
<p> If no <i>hostsfile</i> is specified, replies will be forged for all address queries on the LAN with an answer of the local machine&#8217;s IP address.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/dsniff/dnsspoof.hosts</i></p>
<dd>Sample hosts file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/5-hosts/">hosts</a>(5)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
