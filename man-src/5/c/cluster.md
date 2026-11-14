---
title: "cluster(5)"
name: "cluster"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cluster/"
description: "cluster.conf – configuration file for cman and related daemons"
---

<p>cluster.conf &#8211; configuration file for cman and related daemons</p>
<h2>Synopsis</h2>
<p><code>/etc/cluster/cluster.conf</code> </p>
<h2>Description</h2>
<p>When <code><a href="/docs/linux/man/8-cman_tool/">cman_tool</a></code>(8) starts the <code><a href="/docs/linux/man/8-corosync/">corosync</a></code>(8) daemon, the cluster.conf data is read into the corosync in-memory database (confdb). The configuration is used by corosync, cman and other related cluster daemons and programs. When cman configures corosync with cluster.conf, the <code><a href="/docs/linux/man/5-corosync-conf/">corosync.conf</a></code>(5) file is not used. A basic cluster configuration is described below. Configuration options for other daemons/programs are described in their own man pages. <code><a href="/docs/linux/man/8-ccs_tool/">ccs_tool</a></code>(8) can be used to do some basic cluster.conf editing. The cluster.rng schema is used to validate cluster.conf. Unrecognized items will produce a warning during cluster startup, and invalid xml structure will cause the cluster startup to fail. See <code><a href="/docs/linux/man/8-ccs_config_validate/">ccs_config_validate</a></code>(8) and <code><a href="/docs/linux/man/8-ccs_config_dump/">ccs_config_dump</a></code>(8).</p>
<h3>Cluster</h3>
<p>The top level <code>cluster</code> section contains all other sections and has two required attributes:</p>
<dl>
<dt><code>name</code></p>
<dd>The name of the cluster can be up to 15 characters long (16 including terminating null). It is important that this name be unique among clusters on the same network.</p>
<dt><code>config_version</code></p>
<dd>The config_version specifies the revision level of the file and should be increased each time the file is updated. </p>
<pre>&lt;cluster name=&quot;alpha&quot; config_version=&quot;1&quot;&gt;
&lt;/cluster&gt;</pre>
</dl>
<h3>Cluster Nodes</h3>
<p>The set of nodes that make up the cluster are defined in the <code>clusternodes</code> section which contains multiple <code>clusternode</code> sections. A clusternode has two required attributes:</p>
<dl>
<dt><code>name</code></p>
<dd>The node name should correspond to the hostname on the network interface to be used for cluster communication.</p>
<dt><code>nodeid</code></p>
<dd>The node id must be greater than zero and unique. </p>
<pre>&lt;cluster name=&quot;alpha&quot; config_version=&quot;1&quot;&gt;
 &lt;clusternodes&gt;
 &lt;clusternode name=&quot;node-01&quot; nodeid=&quot;1&quot;&gt;
 &lt;/clusternode&gt;
 &lt;clusternode name=&quot;node-02&quot; nodeid=&quot;2&quot;&gt;
 &lt;/clusternode&gt;
 &lt;clusternode name=&quot;node-03&quot; nodeid=&quot;3&quot;&gt;
 &lt;/clusternode&gt;
 &lt;/clusternodes&gt;
&lt;/cluster&gt;</pre>
</dl>
<h3>Logging</h3>
<p>Cluster daemons use a common <code>logging</code> section to configure their loggging behavior. </p>
<pre>&lt;cluster name=&quot;alpha&quot; config_version=&quot;1&quot;&gt;
 &lt;logging/&gt;
&lt;/cluster&gt;</pre>
<p>Global settings apply to all: </p>
<pre>&lt;logging debug=&quot;on&quot;/&gt;</pre>
<p>Per-daemon <code>logging_daemon</code> subsections override the global settings. Daemon names that can be configured include: corosync, qdiskd, groupd, fenced, dlm_controld, gfs_controld, rgmanager. </p>
<pre>&lt;logging&gt;
 &lt;logging_daemon name=&quot;qdiskd&quot; debug=&quot;on&quot;/&gt;
 &lt;logging_daemon name=&quot;fenced&quot; debug=&quot;on&quot;/&gt;
&lt;/logging&gt;</pre>
<p>Corosync daemon settings apply to all corosync subsystems by default, but subsystems can also be configured individually. These include CLM, CPG, MAIN, SERV, CMAN, TOTEM, QUORUM, CONFDB, CKPT, EVT. </p>
<pre>&lt;logging&gt;
 &lt;logging_daemon name=&quot;corosync&quot; subsys=&quot;QUORUM&quot; debug=&quot;on&quot;/&gt;
 &lt;logging_daemon name=&quot;corosync&quot; subsys=&quot;CONFDB&quot; debug=&quot;on&quot;/&gt;
&lt;/logging&gt;</pre>
<p>The attributes available at global, daemon and subsystem levels are:</p>
<dl>
<dt><code>to_syslog</code></p>
<dd>enable/disable messages to syslog (yes/no), default &quot;yes&quot;</p>
<dt><code>to_logfile</code></p>
<dd>enable/disable messages to log file (yes/no), default &quot;yes&quot;</p>
<dt><code>syslog_facility</code></p>
<dd>facility used for syslog messages, default &quot;daemon&quot;</p>
<dt><code>syslog_priority</code></p>
<dd>messages at this level and up will be sent to syslog, default &quot;info&quot;</p>
<dt><code>logfile_priority</code></p>
<dd>messages at this level and up will be written to log file, default &quot;info&quot;</p>
<dt><code>logfile &nbsp;<wbr> </code></p>
<dd>the log file name, default /var/log/cluster/&lt;daemon&gt;.log </p>
<pre><code>debug=on


a shortcut for logfile_priority=&quot;debug&quot;
</code></pre>
<h2>Example</h2>
<p>An explicit configuration for the default settings would be: </p>
<pre>&lt;logging to_syslog=&quot;yes&quot; to_logfile=&quot;yes&quot; syslog_facility=&quot;daemon&quot;
 syslog_priority=&quot;info&quot; logfile_priority=&quot;info&quot;&gt;
 &lt;logging_daemon name=&quot;qdiskd&quot;
 logfile=&quot;/var/log/cluster/qdiskd.log&quot;/&gt;
 &lt;logging_daemon name=&quot;fenced&quot;
 logfile=&quot;/var/log/cluster/fenced.log&quot;/&gt;
 &lt;logging_daemon name=&quot;dlm_controld&quot;
 logfile=&quot;/var/log/cluster/dlm_controld.log&quot;/&gt;
 &lt;logging_daemon name=&quot;gfs_controld&quot;
 logfile=&quot;/var/log/cluster/gfs_controld.log&quot;/&gt;
 &lt;logging_daemon name=&quot;rgmanager&quot;
 logfile=&quot;/var/log/cluster/rgmanager.log&quot;/&gt;
 &lt;logging_daemon name=&quot;corosync&quot;
 logfile=&quot;/var/log/cluster/corosync.log&quot;/&gt;
&lt;/logging&gt;</pre>
<p>To include debug messages (and above) from all daemons in their default log files, either of the following which are equivalent: </p>
<pre>&lt;logging debug=&quot;on&quot;/&gt;
&lt;logging logfile_priority=&quot;debug&quot;/&gt;</pre>
<p>To exclude all log messages from syslog: </p>
<pre>&lt;logging to_syslog=&quot;no&quot;/&gt;</pre>
<p>To disable logging to all log files: </p>
<pre>&lt;logging to_file=&quot;no&quot;/&gt;</pre>
<p>To include debug messages (and above) from all daemons in syslog: </p>
<pre>&lt;logging syslog_priority=&quot;debug&quot;/&gt;</pre>
<p>To limit syslog messages to error (and above), keeping info (and above) in log files (this logfile_priority setting is the default so could be omitted): </p>
<pre>&lt;logging syslog_priority=&quot;error&quot; logfile_priority=&quot;info&quot;/&gt;</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/cluster/cluster.conf</i></p>
<dd>standard location of cluster configuration file</p>
<dt><i>/usr/share/cluster/cluster.rng</i></p>
<dd>standard location of cluster.conf schema </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ccs_tool/">ccs_tool</a></code>(8), <code><a href="/docs/linux/man/8-ccs_config_dump/">ccs_config_dump</a></code>(8), <code><a href="/docs/linux/man/8-ccs_config_validate/">ccs_config_validate</a></code>(8), <code><a href="/docs/linux/man/8-cman_tool/">cman_tool</a></code>(8), <code><a href="/docs/linux/man/5-cman/">cman</a></code>(5), <code><a href="/docs/linux/man/5-qdisk/">qdisk</a></code>(5), <code><a href="/docs/linux/man/8-fenced/">fenced</a></code>(8), <code><a href="/docs/linux/man/8-fence_node/">fence_node</a></code>(8), <code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/8-gfs_controld/">gfs_controld</a></code>(8), <code><a href="/docs/linux/man/8-rgmanager/">rgmanager</a></code>(8) </p>
