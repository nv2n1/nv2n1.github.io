---
title: "globus-rls-admin(8)"
name: "globus-rls-admin"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-rls-admin/"
description: "globus-rls-admin – Replica Location Service Administration"
---

<p>globus-rls-admin &#8211; Replica Location Service Administration</p>
<h2>Synopsis</h2>
<p><code>globus-rls-admin</code> <i>-A|-a|-C option value|-c option|-D|-d|-e|-p|-q|-r|-S|-s|-t timeout|-u|-v</i> [ <i>rli</i> ] [ <i>pattern</i> ] [ <i>server</i> ]</p>
<h2>Description</h2>
<p>The program <code>globus-rls-admin</code> performs administrative operations on a RLS server (see <a href="/docs/linux/man/8-globus-rls-server/">globus-rls-server</a>(8)).</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Add <i>rli</i> to list of RLI servers updated by an LRC <i>server</i> using Bloom filters. Note that partitions are not supported with Bloom filters, the LRC <i>server</i> maintains one Bloom filter for all LFNs in its database, which is sent to all RLI servers configured to receive Bloom filter updates with this option.</p>
<dt><code>-a</code></p>
<dd>Add <i>rli</i> and optionally <i>pattern</i> to the list of RLI servers that the LRC <i>server</i> sends updates to (using a list of LFNs). If <i>pattern</i> is specified then only LFNs matching it will be sent to <i>rli.</i> If <i>rli</i> is added with no patterns, then it is sent all updates. Pattern matching is done using standard Unix file globbing (see <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) or <a href="/docs/linux/man/1-sh/">sh</a>(1)).</p>
<dt><code>-C option value</code></p>
<dd>Set server <i>option</i> to <i>value.</i> Note this does not update the configuration file, the next time the server is restarted the configuration change will be lost.</p>
<dt><code>-c option</code></p>
<dd>Retrieve configuration value for specified option from server. If <i>option</i> is &quot;all&quot; then all options are retrieved.</p>
<dt><code>-D</code></p>
<dd>Remove <i>rli</i> and <i>pattern</i> from list of RLI servers that the RLI <i>server</i> sends updates to. If <i>pattern</i> is not specified then all entries for <i>rli</i> are removed. Note if all patterns are removed separately then <i>rli</i> is sent all updates. To stop any updates from being sent to <i>rli</i> do not specify <i>pattern</i></p>
<dt><code>-d</code></p>
<dd>Remove <i>rli</i> and <i>pattern</i> from list of RLI servers that the LRC <i>server</i> sends updates to. If <i>pattern</i> is not specified then all entries for <i>rli</i> are removed. Note if all patterns are removed separately then <i>rli</i> is sent all updates. To stop any updates from being sent to <i>rli</i> do not specify <i>pattern</i></p>
<dt><code>-e</code></p>
<dd>Clear LRC database. Removes all lfn,pfn mappings.</p>
<dt><code>-p</code></p>
<dd>Verifies that the <i>server</i> is responding.</p>
<dt><code>-q</code></p>
<dd>Cause RLS <i>server</i> to exit.</p>
<dt><code>-r</code></p>
<dd>Add <i>rli</i> and optionally <i>pattern</i> to the list of RLI servers that the RLI <i>server</i> sends updates to. If <i>pattern</i> is specified then only LFNs matching it will be sent to <i>rli.</i> If <i>rli</i> is added with no patterns, then it is sent all updates. Pattern matching is done using standard Unix file globbing (see <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) or <a href="/docs/linux/man/1-sh/">sh</a>(1)).</p>
<dt><code>-S</code></p>
<dd>Show statistics and other information gathered by RLS server. Intended to be input into GRIS.</p>
<dt><code>-s</code></p>
<dd>Show list of RLI servers and patterns being sent updates by the LRC <i>server.</i> If <i>rli</i> or <i>pattern</i> are not specified they are considered wildcards.</p>
<dt><code>-t timeout</code></p>
<dd>Set timeout (in seconds) for RLS server requests. Default is 30 seconds.</p>
<dt><code>-u</code></p>
<dd>Cause LRC server to immediately start full softstate updates to any RLI servers previously added with the -a option.</p>
<dt><code>-v</code></p>
<dd>Show version and exit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-globus-rls-server/">globus-rls-server</a>(8), globus_rls_client man pages </p>
