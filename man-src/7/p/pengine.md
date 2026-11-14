---
title: "pengine(7)"
name: "pengine"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pengine/"
description: "pengine – Policy Engine Options"
---

<p>pengine &#8211; Policy Engine Options</p>
<h2>Synopsis</h2>
<p>[<code>no-quorum-policy</code>=enum] [<code>symmetric-cluster</code>=boolean] [<code>default-resource-stickiness</code>=integer] [<code>is-managed-default</code>=boolean] [<code>maintenance-mode</code>=boolean] [<code>start-failure-is-fatal</code>=boolean] [<code>enable-startup-probes</code>=boolean] [<code>stonith-enabled</code>=boolean] [<code>stonith-action</code>=enum] [<code>stonith-timeout</code>=time] [<code>have-watchdog</code>=boolean] [<code>concurrent-fencing</code>=boolean] [<code>startup-fencing</code>=boolean] [<code>cluster-delay</code>=time] [<code>batch-limit</code>=integer] [<code>migration-limit</code>=integer] [<code>default-action-timeout</code>=time] [<code>stop-all-resources</code>=boolean] [<code>stop-orphan-resources</code>=boolean] [<code>stop-orphan-actions</code>=boolean] [<code>remove-after-stop</code>=boolean] [<code>pe-error-series-max</code>=integer] [<code>pe-warn-series-max</code>=integer] [<code>pe-input-series-max</code>=integer] [<code>node-health-strategy</code>=enum] [<code>node-health-green</code>=integer] [<code>node-health-yellow</code>=integer] [<code>node-health-red</code>=integer] [<code>placement-strategy</code>=enum]</p>
<h2>Description</h2>
<p>This is a fake resource that details the options that can be configured for the Policy Engine.</p>
<h2>Supported Parameters</h2>
<p><code>no-quorum-policy</code> = enum [stop]</p>
<dl>
<dd>What to do when the cluster does not have quorum </p>
<p> What to do when the cluster does not have quorum Allowed values: stop, freeze, ignore, suicide</dl>
<p> <code>symmetric-cluster</code> = boolean [true]</p>
<dl>
<dd>All resources can run anywhere by default</dl>
<p> <code>default-resource-stickiness</code> = integer [0]</p>
<dl>
<dd></dl>
<p> <code>is-managed-default</code> = boolean [true]</p>
<dl>
<dd>Should the cluster start/stop resources as required</dl>
<p> <code>maintenance-mode</code> = boolean [false]</p>
<dl>
<dd>Should the cluster monitor resources and start/stop them as required</dl>
<p> <code>start-failure-is-fatal</code> = boolean [true]</p>
<dl>
<dd>Always treat start failures as fatal </p>
<p> This was the old default. However when set to FALSE, the cluster will instead use the resource&#8217;s failcount and value for resource-failure-stickiness</dl>
<p> <code>enable-startup-probes</code> = boolean [true]</p>
<dl>
<dd>Should the cluster check for active resources during startup</dl>
<p> <code>stonith-enabled</code> = boolean [true]</p>
<dl>
<dd>Failed nodes are STONITH&#8217;d</dl>
<p> <code>stonith-action</code> = enum [reboot]</p>
<dl>
<dd>Action to send to STONITH device </p>
<p> Action to send to STONITH device Allowed values: reboot, poweroff, off</dl>
<p> <code>stonith-timeout</code> = time [60s]</p>
<dl>
<dd>How long to wait for the STONITH action (reboot,on,off) to complete</dl>
<p> <code>have-watchdog</code> = boolean [false]</p>
<dl>
<dd>Enable watchdog integration </p>
<p> Set automatically by the cluster if SBD is detected. User configured values are ignored.</dl>
<p> <code>concurrent-fencing</code> = boolean [false]</p>
<dl>
<dd>Allow performing fencing operations in parallel</dl>
<p> <code>startup-fencing</code> = boolean [true]</p>
<dl>
<dd>STONITH unseen nodes </p>
<p> Advanced Use Only! Not using the default is very unsafe!</dl>
<p> <code>cluster-delay</code> = time [60s]</p>
<dl>
<dd>Round trip delay over the network (excluding action execution) </p>
<p> The &quot;correct&quot; value will depend on the speed and load of your network and cluster nodes.</dl>
<p> <code>batch-limit</code> = integer [0]</p>
<dl>
<dd>The number of jobs that the TE is allowed to execute in parallel </p>
<p> The &quot;correct&quot; value will depend on the speed and load of your network and cluster nodes.</dl>
<p> <code>migration-limit</code> = integer [-1]</p>
<dl>
<dd>The number of migration jobs that the TE is allowed to execute in parallel on a node</dl>
<p> <code>default-action-timeout</code> = time [20s]</p>
<dl>
<dd>How long to wait for actions to complete</dl>
<p> <code>stop-all-resources</code> = boolean [false]</p>
<dl>
<dd>Should the cluster stop all active resources (except those needed for fencing)</dl>
<p> <code>stop-orphan-resources</code> = boolean [true]</p>
<dl>
<dd>Should deleted resources be stopped</dl>
<p> <code>stop-orphan-actions</code> = boolean [true]</p>
<dl>
<dd>Should deleted actions be cancelled</dl>
<p> <code>remove-after-stop</code> = boolean [false]</p>
<dl>
<dd>Remove resources from the LRM after they are stopped </p>
<p> Always set this to false. Other values are, at best, poorly tested and potentially dangerous.</dl>
<p> <code>pe-error-series-max</code> = integer [-1]</p>
<dl>
<dd>The number of PE inputs resulting in ERRORs to save </p>
<p> Zero to disable, -1 to store unlimited.</dl>
<p> <code>pe-warn-series-max</code> = integer [5000]</p>
<dl>
<dd>The number of PE inputs resulting in WARNINGs to save </p>
<p> Zero to disable, -1 to store unlimited.</dl>
<p> <code>pe-input-series-max</code> = integer [4000]</p>
<dl>
<dd>The number of other PE inputs to save </p>
<p> Zero to disable, -1 to store unlimited.</dl>
<p> <code>node-health-strategy</code> = enum [none]</p>
<dl>
<dd>The strategy combining node attributes to determine overall node health. </p>
<p> Requires external entities to create node attributes (named with the prefix &#8216;#health&#8217;) with values: &#8216;red&#8217;, &#8216;yellow&#8217; or &#8216;green&#8217;. Allowed values: none, migrate-on-red, only-green, progressive, custom</dl>
<p> <code>node-health-green</code> = integer [0]</p>
<dl>
<dd>The score &#8216;green&#8217; translates to in rsc_location constraints </p>
<p> Only used when node-health-strategy is set to custom or progressive.</dl>
<p> <code>node-health-yellow</code> = integer [0]</p>
<dl>
<dd>The score &#8216;yellow&#8217; translates to in rsc_location constraints </p>
<p> Only used when node-health-strategy is set to custom or progressive.</dl>
<p> <code>node-health-red</code> = integer [-INFINITY]</p>
<dl>
<dd>The score &#8216;red&#8217; translates to in rsc_location constraints </p>
<p> Only used when node-health-strategy is set to custom or progressive.</dl>
<p> <code>placement-strategy</code> = enum [default]</p>
<dl>
<dd>The strategy to determine resource placement </p>
<p> The strategy to determine resource placement Allowed values: default, utilization, minimal, balanced</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
