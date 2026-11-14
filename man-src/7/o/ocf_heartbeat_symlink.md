---
title: "ocf_heartbeat_symlink(7)"
name: "ocf_heartbeat_symlink"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_symlink/"
description: "ocf_heartbeat_symlink – Manages a symbolic link"
---

<p>ocf_heartbeat_symlink &#8211; Manages a symbolic link</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>symlink</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This resource agent that manages a symbolic link (symlink). </p>
<p> It is primarily intended to manage configuration files which should be enabled or disabled based on where the resource is running, such as cron job definitions and the like.</p>
<h2>Supported Parameters</h2>
<p><code>link</code></p>
<dl>
<dd>Full path of the symbolic link to be managed. This must obviously be in a filesystem that supports symbolic links. </p>
<p> (required, string, no default)</dl>
<p> <code>target</code></p>
<dl>
<dd>Full path to the link target (the file or directory which the symlink points to). </p>
<p> (required, string, no default)</dl>
<p> <code>backup_suffix</code></p>
<dl>
<dd>A suffix to append to any files that the resource agent moves out of the way because they clash with &quot;link&quot;. </p>
<p> If this is unset (the default), then the resource agent will simply refuse to create a symlink if it clashes with an existing file. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 15.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 15.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 15. Suggested interval: 60.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 10.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a symlink resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_symlink ocf:heartbeat:symlink \
 params \
 link=<i>string</i> \
 target=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;15&quot; interval=&quot;60&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a symlink resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_symlink ocf:heartbeat:symlink \
 link=<i>string</i> \
 target=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;15&quot; interval=&quot;60&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/symlink_(resource_agent)">http://www.linux-ha.org/wiki/symlink_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
