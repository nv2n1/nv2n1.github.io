---
title: "ocf_pacemaker_pingd(7)"
name: "ocf_pacemaker_pingd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_pingd/"
description: "ocf_pacemaker_pingd – pingd resource agent"
---

<p>ocf_pacemaker_pingd &#8211; pingd resource agent</p>
<h2>Synopsis</h2>
<p>[<code>OCF_RESKEY_pidfile</code>=string] [<code>OCF_RESKEY_user</code>=string] [<code>OCF_RESKEY_dampen</code>=integer] [<code>OCF_RESKEY_set</code>=string] [<code>OCF_RESKEY_name</code>=string] [<code>OCF_RESKEY_section</code>=string] [<code>OCF_RESKEY_multiplier</code>=integer] [<code>OCF_RESKEY_host_list</code>=string] [<code>OCF_RESKEY_interval</code>=integer] [<code>OCF_RESKEY_attempts</code>=integer] [<code>OCF_RESKEY_timeout</code>=integer] [<code>OCF_RESKEY_options</code>=string] <code>pingd</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>This agent (ocf:pacemaker:pingd) has been replaced by the more reliable ocf:pacemaker:ping. It records (in the CIB) the current number of ping nodes (specified in the &#8216;host_list&#8217; parameter) a cluster node can connect to.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_pidfile</code> = string [/pingd-]</p>
<dl>
<dd>PID file</dl>
<p> <code>OCF_RESKEY_user</code> = string [root]</p>
<dl>
<dd>The user we want to run pingd as </p>
<p> The user we want to run pingd as</dl>
<p> <code>OCF_RESKEY_dampen</code> = integer [5s]</p>
<dl>
<dd>Dampening interval </p>
<p> The time to wait (dampening) further changes occur</dl>
<p> <code>OCF_RESKEY_set</code> = string []</p>
<dl>
<dd>Set name </p>
<p> The name of the instance_attributes set to place the value in. Rarely needs to be specified.</dl>
<p> <code>OCF_RESKEY_name</code> = string [pingd]</p>
<dl>
<dd>Attribute name </p>
<p> The name of the attributes to set. This is the name to be used in the constraints.</dl>
<p> <code>OCF_RESKEY_section</code> = string []</p>
<dl>
<dd>Section name </p>
<p> The section place the value in. Rarely needs to be specified.</dl>
<p> <code>OCF_RESKEY_multiplier</code> = integer []</p>
<dl>
<dd>Value multiplier </p>
<p> The number by which to multiply the number of connected ping nodes by</dl>
<p> <code>OCF_RESKEY_host_list</code> = string []</p>
<dl>
<dd>Host list </p>
<p> The list of ping nodes to count. Defaults to all configured ping nodes. Rarely needs to be specified.</dl>
<p> <code>OCF_RESKEY_interval</code> = integer [1]</p>
<dl>
<dd>ping interval in seconds </p>
<p> How often, in seconds, to check for node liveliness</dl>
<p> <code>OCF_RESKEY_attempts</code> = integer [2]</p>
<dl>
<dd>no. of ping attempts </p>
<p> Number of ping attempts, per host, before declaring it dead</dl>
<p> <code>OCF_RESKEY_timeout</code> = integer [2]</p>
<dl>
<dd>ping timeout in seconds </p>
<p> How long, in seconds, to wait before declaring a ping lost</dl>
<p> <code>OCF_RESKEY_options</code> = string []</p>
<dl>
<dd>Extra Options </p>
<p> A catch all for any other options that need to be passed to pingd.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
