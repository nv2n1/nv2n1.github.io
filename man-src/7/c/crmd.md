---
title: "crmd(7)"
name: "crmd"
section: "7"
letter: "c"
url: "/docs/linux/man/7-crmd/"
description: "crmd – CRM Daemon Options"
---

<p>crmd &#8211; CRM Daemon Options</p>
<h2>Synopsis</h2>
<p>[<code>dc-version</code>=string] [<code>cluster-infrastructure</code>=string] [<code>dc-deadtime</code>=time] [<code>cluster-recheck-interval</code>=time] [<code>notification-agent</code>=string] [<code>notification-recipient</code>=string] [<code>load-threshold</code>=percentage] [<code>node-action-limit</code>=integer] [<code>election-timeout</code>=time] [<code>shutdown-escalation</code>=time] [<code>crmd-integration-timeout</code>=time] [<code>crmd-finalization-timeout</code>=time] [<code>crmd-transition-delay</code>=time] [<code>stonith-watchdog-timeout</code>=time]</p>
<h2>Description</h2>
<p>This is a fake resource that details the options that can be configured for the CRM Daemon.</p>
<h2>Supported Parameters</h2>
<p><code>dc-version</code> = string [none]</p>
<dl>
<dd>Version of Pacemaker on the cluster&#8217;s DC. </p>
<p> Includes the hash which identifies the exact changeset it was built from. Used for diagnostic purposes.</dl>
<p> <code>cluster-infrastructure</code> = string [heartbeat]</p>
<dl>
<dd>The messaging stack on which Pacemaker is currently running. </p>
<p> Used for informational and diagnostic purposes.</dl>
<p> <code>dc-deadtime</code> = time [20s]</p>
<dl>
<dd>How long to wait for a response from other nodes during startup. </p>
<p> The &quot;correct&quot; value will depend on the speed/load of your network and the type of switches used.</dl>
<p> <code>cluster-recheck-interval</code> = time [15min]</p>
<dl>
<dd>Polling interval for time based changes to options, resource parameters and constraints. </p>
<p> The Cluster is primarily event driven, however the configuration can have elements that change based on time. To ensure these changes take effect, we can optionally poll the cluster&#8217;s status for changes. Allowed values: Zero disables polling. Positive values are an interval in seconds (unless other SI units are specified. eg. 5min)</dl>
<p> <code>notification-agent</code> = string [/dev/null]</p>
<dl>
<dd>Deprecated </p>
<p> Use alert path in alerts section instead</dl>
<p> <code>notification-recipient</code> = string []</p>
<dl>
<dd>Deprecated </p>
<p> Use recipient value in alerts section instead</dl>
<p> <code>load-threshold</code> = percentage [80%]</p>
<dl>
<dd>The maximum amount of system resources that should be used by nodes in the cluster </p>
<p> The cluster will slow down its recovery process when the amount of system resources used (currently CPU) approaches this limit</dl>
<p> <code>node-action-limit</code> = integer [0]</p>
<dl>
<dd>The maximum number of jobs that can be scheduled per node. Defaults to 2x cores</dl>
<p> <code>election-timeout</code> = time [2min]</p>
<dl>
<dd>*** Advanced Use Only ***. </p>
<p> If need to adjust this value, it probably indicates the presence of a bug.</dl>
<p> <code>shutdown-escalation</code> = time [20min]</p>
<dl>
<dd>*** Advanced Use Only ***. </p>
<p> If need to adjust this value, it probably indicates the presence of a bug.</dl>
<p> <code>crmd-integration-timeout</code> = time [3min]</p>
<dl>
<dd>*** Advanced Use Only ***. </p>
<p> If need to adjust this value, it probably indicates the presence of a bug.</dl>
<p> <code>crmd-finalization-timeout</code> = time [30min]</p>
<dl>
<dd>*** Advanced Use Only ***. </p>
<p> If you need to adjust this value, it probably indicates the presence of a bug.</dl>
<p> <code>crmd-transition-delay</code> = time [0s]</p>
<dl>
<dd>*** Advanced Use Only *** Enabling this option will slow down cluster recovery under all conditions </p>
<p> Delay cluster recovery for the configured interval to allow for additional/related events to occur. Useful if your configuration is sensitive to the order in which ping updates arrive.</dl>
<p> <code>stonith-watchdog-timeout</code> = time [(null)]</p>
<dl>
<dd>How long to wait before we can assume nodes are safely down</dl>
<h2>Author</h2>
<p><code>Andrew Beekhof</code> &lt;andrew [at] beekhof.net&gt;</p>
<dl>
<dd>Author.</dl>
