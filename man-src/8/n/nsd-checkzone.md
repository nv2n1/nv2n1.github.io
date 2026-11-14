---
title: "nsd-checkzone(8)"
name: "nsd-checkzone"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-checkzone/"
description: "nsd-checkzone – NSD zone file syntax checker."
---

<p><code>nsd-checkzone</code> &#8211; NSD zone file syntax checker.</p>
<h2>Synopsis</h2>
<p><code>nsd-checkzone</code> [<code>-h</code>] <i>zonename</i> <i>zonefile</i></p>
<h2>Description</h2>
<p><code>nsd-checkzone</code> reads a DNS zone file and checks it for errors. It prints errors to stderr. On failure it exits with nonzero exit status. </p>
<p> This is used to check files before feeding them to the <a href="/docs/linux/man/8-nsd/">nsd</a>(8) daemon.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print usage help information and exit.</p>
<dt><i>zonename</i></p>
<dd>The name of the zone to check, eg. &quot;example.com&quot;.</p>
<dt><i>zonefile</i></p>
<dd>The file to read, eg. &quot;zones/example.com.zone.signed&quot;.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8), <i><a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a></i>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
