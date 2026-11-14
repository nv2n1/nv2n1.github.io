---
title: "ocf_pacemaker_clustermon(7)"
name: "ocf_pacemaker_clustermon"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_clustermon/"
description: "ocf_pacemaker_ClusterMon – Runs crm_mon in the background, recording the cluster status to an HTML file"
---

<p>ocf_pacemaker_ClusterMon &#8211; Runs crm_mon in the background, recording the cluster status to an HTML file</p>
<h2>Synopsis</h2>
<p>[<code>OCF_RESKEY_user</code>=string] [<code>OCF_RESKEY_update</code>=integer] [<code>OCF_RESKEY_extra_options</code>=string] <code>OCF_RESKEY_pidfile</code>=string <code>OCF_RESKEY_htmlfile</code>=string <code>ClusterMon</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>This is a ClusterMon Resource Agent. It outputs current cluster status to the html.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_user</code> = string [root]</p>
<dl>
<dd>The user we want to run crm_mon as </p>
<p> The user we want to run crm_mon as</dl>
<p> <code>OCF_RESKEY_update</code> = integer [15]</p>
<dl>
<dd>Update interval </p>
<p> How frequently should we update the cluster status</dl>
<p> <code>OCF_RESKEY_extra_options</code> = string []</p>
<dl>
<dd>Extra options </p>
<p> Additional options to pass to crm_mon. Eg. -n -r</dl>
<p> <code>OCF_RESKEY_pidfile</code> = string [/tmp/ClusterMon_.pid]</p>
<dl>
<dd>PID file </p>
<p> PID file location to ensure only one instance is running</dl>
<p> <code>OCF_RESKEY_htmlfile</code> = string [/tmp/ClusterMon_.html]</p>
<dl>
<dd>HTML output </p>
<p> Location to write HTML output to.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
