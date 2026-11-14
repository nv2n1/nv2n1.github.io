---
title: "nsd-patch(8)"
name: "nsd-patch"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-patch/"
description: "nsd-patch – NSD zone patcher version 3.2.4."
---

<p><code>nsd-patch</code> &#8211; NSD zone patcher version 3.2.4.</p>
<h2>Synopsis</h2>
<p><code>nsd-patch</code> [<code>-c</code> <i>configfile</i>] [<code>-f</code>] [<code>-h</code>] [<code>-l</code>] [<code>-o</code> <i>dbfile</i>] [<code>-s</code>] [<code>-x</code> <i>difffile</i>]</p>
<h2>Description</h2>
<p><code>Nsd-patch</code> is the zone patcher for <a href="/docs/linux/man/8-nsd/">nsd</a>(8). It reads in the nsd database (nsd.db) and difffile (ixfr.db), and overwrites the zone text files if they have been updated. Running this regularly ensures that the difffile does not grow infinitely.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> configfile</i></p>
<dd>Read specified configfile instead of the default <i>/etc/nsd/nsd.conf</i>.</p>
<dt><code>-f</code></p>
<dd>Forces writing zone files. Also zones that have not changed are written back to their zone files.</p>
<dt><code>-h</code></p>
<dd>Print usage help information and exit.</p>
<dt><code>-l</code></p>
<dd>List the journal entries from the difffile. Does not write to zone files.</p>
<dt><code>-o</code><i> dbfile</i></p>
<dd>Store the output directly to dbfile.</p>
<dt><code>-s</code></p>
<dd>Skip writing zone files. No zones are written back to their zone files.</p>
<dt><code>-x</code><i> difffile</i></p>
<dd>Read specified difffile. Overrides the config file setting.</dl>
<h2>Files</h2>
<dl>
<dt>/var/db/nsd/nsd.db</p>
<dd>default <code>NSD</code> database</p>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8), <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-notify/">nsd-notify</a>(8), <a href="/docs/linux/man/8-nsd-xfer/">nsd-xfer</a>(8), <a href="/docs/linux/man/8-zonec/">zonec</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
