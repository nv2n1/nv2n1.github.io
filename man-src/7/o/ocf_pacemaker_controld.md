---
title: "ocf_pacemaker_controld(7)"
name: "ocf_pacemaker_controld"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_controld/"
description: "ocf_pacemaker_controld – DLM Agent for cluster file systems"
---

<p>ocf_pacemaker_controld &#8211; DLM Agent for cluster file systems</p>
<h2>Synopsis</h2>
<p><code>OCF_RESKEY_args</code>=string <code>OCF_RESKEY_configdir</code>=string <code>OCF_RESKEY_daemon</code>=string [<code>OCF_RESKEY_allow_stonith_disabled</code>=string] <code>controld</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>This Resource Agent can control the dlm_controld services needed by cluster-aware file systems. It assumes that dlm_controld is in your default PATH. In most cases, it should be run as an anonymous clone.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_args</code> = string [-s 0]</p>
<dl>
<dd>DLM Options </p>
<p> Any additional options to start the dlm_controld service with</dl>
<p> <code>OCF_RESKEY_configdir</code> = string [/sys/kernel/config]</p>
<dl>
<dd>Location of configfs </p>
<p> The location where configfs is or should be mounted</dl>
<p> <code>OCF_RESKEY_daemon</code> = string [dlm_controld.pcmk]</p>
<dl>
<dd>The daemon to start </p>
<p> The daemon to start &#8211; supports gfs_controld(.pcmk) and dlm_controld(.pcmk)</dl>
<p> <code>OCF_RESKEY_allow_stonith_disabled</code> = string [false]</p>
<dl>
<dd>Allow start-up even without STONITH/fencing </p>
<p> Allow DLM start-up even if STONITH/fencing is disabled in the cluster. Setting this option to true will cause cluster malfunction and hangs on fail-over for DLM clients that require fencing (such as GFS2, OCFS2, and cLVM2). This option is advanced use only.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
