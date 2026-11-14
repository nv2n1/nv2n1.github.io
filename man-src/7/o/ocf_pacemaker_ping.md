---
title: "ocf_pacemaker_ping(7)"
name: "ocf_pacemaker_ping"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_ping/"
description: "ocf_pacemaker_ping – node connectivity"
---

<p>ocf_pacemaker_ping &#8211; node connectivity</p>
<h2>Synopsis</h2>
<p>[<code>OCF_RESKEY_pidfile</code>=string] [<code>OCF_RESKEY_dampen</code>=integer] [<code>OCF_RESKEY_name</code>=string] [<code>OCF_RESKEY_multiplier</code>=integer] [<code>OCF_RESKEY_host_list</code>=string] [<code>OCF_RESKEY_attempts</code>=integer] [<code>OCF_RESKEY_timeout</code>=integer] [<code>OCF_RESKEY_options</code>=string] [<code>OCF_RESKEY_failure_score</code>=integer] [<code>OCF_RESKEY_use_fping</code>=boolean] [<code>OCF_RESKEY_debug</code>=string] <code>ping</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>Every time the monitor action is run, this resource agent records (in the CIB) the current number of nodes the host can connect to using the system fping (preferred) or ping tool.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_pidfile</code> = string [/ping-]</p>
<dl>
<dd>PID file</dl>
<p> <code>OCF_RESKEY_dampen</code> = integer [5s]</p>
<dl>
<dd>Dampening interval </p>
<p> The time to wait (dampening) further changes occur</dl>
<p> <code>OCF_RESKEY_name</code> = string [pingd]</p>
<dl>
<dd>Attribute name </p>
<p> The name of the attributes to set. This is the name to be used in the constraints.</dl>
<p> <code>OCF_RESKEY_multiplier</code> = integer [1]</p>
<dl>
<dd>Value multiplier </p>
<p> The number by which to multiply the number of connected ping nodes by</dl>
<p> <code>OCF_RESKEY_host_list</code> = string []</p>
<dl>
<dd>Host list </p>
<p> A space separated list of ping nodes to count.</dl>
<p> <code>OCF_RESKEY_attempts</code> = integer [3]</p>
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
<p> A catch all for any other options that need to be passed to ping.</dl>
<p> <code>OCF_RESKEY_failure_score</code> = integer []</p>
<dl>
<dd>failure_score </p>
<p> Resource is failed if the score is less than failure_score. Default never fails.</dl>
<p> <code>OCF_RESKEY_use_fping</code> = boolean [1]</p>
<dl>
<dd>Use fping if available </p>
<p> Use fping rather than ping, if found. If set to 0, fping will not be used even if present.</dl>
<p> <code>OCF_RESKEY_debug</code> = string [false]</p>
<dl>
<dd>Verbose logging </p>
<p> Enables to use default attrd_updater verbose logging on every call.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
