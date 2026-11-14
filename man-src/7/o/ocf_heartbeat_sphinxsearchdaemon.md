---
title: "ocf_heartbeat_sphinxsearchdaemon(7)"
name: "ocf_heartbeat_sphinxsearchdaemon"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sphinxsearchdaemon/"
description: "ocf_heartbeat_SphinxSearchDaemon – Manages the Sphinx search daemon."
---

<p>ocf_heartbeat_SphinxSearchDaemon &#8211; Manages the Sphinx search daemon.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SphinxSearchDaemon</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a searchd Resource Agent. It manages the Sphinx Search Daemon.</p>
<h2>Supported Parameters</h2>
<p><code>config</code></p>
<dl>
<dd>searchd configuration file (optional, string, default /etc/sphinx/sphinx.conf)</dl>
<p> <code>searchd</code></p>
<dl>
<dd>searchd binary (optional, string, default /usr/local/bin/searchd)</dl>
<p> <code>search</code></p>
<dl>
<dd>Search binary for functional testing in the monitor action. (optional, string, default /usr/local/bin/search)</dl>
<p> <code>testQuery</code></p>
<dl>
<dd>Test query for functional testing in the monitor action. The query does not need to match any documents in the index. The purpose is merely to test whether the search daemon is is able to query its indices and respond properly. (optional, string, default Heartbeat_Monitor_Query_Match_string)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a SphinxSearchDaemon resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_SphinxSearchDaemon ocf:heartbeat:SphinxSearchDaemon \

op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/SphinxSearchDaemon_(resource_agent)">http://www.linux-ha.org/wiki/SphinxSearchDaemon_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
