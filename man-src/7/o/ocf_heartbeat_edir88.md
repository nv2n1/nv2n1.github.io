---
title: "ocf_heartbeat_edir88(7)"
name: "ocf_heartbeat_edir88"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_edir88/"
description: "ocf_heartbeat_eDir88 – Manages a Novell eDirectory directory server"
---

<p>ocf_heartbeat_eDir88 &#8211; Manages a Novell eDirectory directory server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>eDir88</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for managing an eDirectory instance. Manages a single instance of eDirectory as an HA resource. The &quot;multiple instances&quot; feature or eDirectory has been added in version 8.8. This script will not work for any version of eDirectory prior to 8.8. This RA can be used to load multiple eDirectory instances on the same host. It is very strongly recommended to put eDir configuration files (as per the eDir_config_file parameter) on local storage on each node. This is necessary for this RA to be able to handle situations where the shared storage has become unavailable. If the eDir configuration file is not available, this RA will fail, and heartbeat will be unable to manage the resource. Side effects include STONITH actions, unmanageable resources, etc&#8230; Setting a high action timeout value is _very_ _strongly_ recommended. eDir with IDM can take in excess of 10 minutes to start. If heartbeat times out before eDir has had a chance to start properly, mayhem _WILL ENSUE_. The LDAP module seems to be one of the very last to start. So this script will take even longer to start on installations with IDM and LDAP if the monitoring of IDM and/or LDAP is enabled, as the start command will wait for IDM and LDAP to be available.</p>
<h2>Supported Parameters</h2>
<p><code>eDir_config_file</code></p>
<dl>
<dd>Path to configuration file for eDirectory instance. (optional, string, default /etc/opt/novell/eDirectory/conf/nds.conf)</dl>
<p> <code>eDir_monitor_ldap</code></p>
<dl>
<dd>Should we monitor if LDAP is running for the eDirectory instance? (optional, boolean, default 0)</dl>
<p> <code>eDir_monitor_idm</code></p>
<dl>
<dd>Should we monitor if IDM is running for the eDirectory instance? (optional, boolean, default 0)</dl>
<p> <code>eDir_jvm_initial_heap</code></p>
<dl>
<dd>Value for the DHOST_INITIAL_HEAP java environment variable. If unset, java defaults will be used. (optional, integer, no default)</dl>
<p> <code>eDir_jvm_max_heap</code></p>
<dl>
<dd>Value for the DHOST_MAX_HEAP java environment variable. If unset, java defaults will be used. (optional, integer, no default)</dl>
<p> <code>eDir_jvm_options</code></p>
<dl>
<dd>Value for the DHOST_OPTIONS java environment variable. If unset, original values will be used. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 600.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 600.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 30.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a eDir88 resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_eDir88 ocf:heartbeat:eDir88 \

op monitor timeout=&quot;60&quot; interval=&quot;30&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/eDir88_(resource_agent)">http://www.linux-ha.org/wiki/eDir88_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
