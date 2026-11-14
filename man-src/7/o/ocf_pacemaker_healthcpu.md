---
title: "ocf_pacemaker_healthcpu(7)"
name: "ocf_pacemaker_healthcpu"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_pacemaker_healthcpu/"
description: "ocf_pacemaker_HealthCPU – System health CPU usage"
---

<p>ocf_pacemaker_HealthCPU &#8211; System health CPU usage</p>
<h2>Synopsis</h2>
<p><code>OCF_RESKEY_state</code>=string <code>OCF_RESKEY_yellow_limit</code>=string <code>OCF_RESKEY_red_limit</code>=string <code>HealthCPU</code> [start | stop | monitor | meta-data | validate-all]</p>
<h2>Description</h2>
<p>Systhem health agent that measures the CPU idling and updates the #health-cpu attribute.</p>
<h2>Supported Parameters</h2>
<p><code>OCF_RESKEY_state</code> = string [/health-cpu-.state]</p>
<dl>
<dd>State file </p>
<p> Location to store the resource state in.</dl>
<p> <code>OCF_RESKEY_yellow_limit</code> = string [50]</p>
<dl>
<dd>Lower limit for yellow health attribute </p>
<p> Lower (!) limit of idle percentage to switch the health attribute to yellow. I.e. the #health-cpu will go yellow if the %idle of the CPU falls below 50%.</dl>
<p> <code>OCF_RESKEY_red_limit</code> = string [10]</p>
<dl>
<dd>Lower limit for red health attribute </p>
<p> Lower (!) limit of idle percentage to switch the health attribute to red. I.e. the #health-cpu will go red if the %idle of the CPU falls below 10%.</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
