---
title: "euscale-update-auto-scaling-group(1)"
name: "euscale-update-auto-scaling-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-update-auto-scaling-group/"
description: "euscale-update-auto-scaling-group – Update an auto-scaling group’s parameters"
---

<h2>NAME</h2>
<p> euscale-update-auto-scaling-group &#8211; Update an auto-scaling group&#8217;s parameters</p>
<h2>SYNOPSIS</h2>
<p> euscale-update-auto-scaling-group [&#8211;default-cooldown SECONDS]</p>
<dl>
<dt>[&#8211;desired-capacity COUNT]</p>
<dd> [&#8211;grace-period SECONDS] [&#8211;health-check-type {EC2,ELB}] [-l LAUNCHCONFIG] [-M COUNT] [-m COUNT] [&#8211;placement-group PLACEMENTGROUP] [&#8211;termination-policies POLICY1,POLICY2,&#8230;] [&#8211;vpc-zone-identifier ZONE1,ZONE2,&#8230;] [-z ZONE1,ZONE2,&#8230;] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dl>
<h2>DESCRIPTION</h2>
<p> Update an auto-scaling group&#8217;s parameters</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</p>
<dd> name of the auto-scaling group to update (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;default-cooldown</code> SECONDS</p>
<dd> amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities may start</p>
<dt><code>&#8211;desired-capacity</code> COUNT</p>
<dd> number of running instances the group should contain</p>
<dt><code>&#8211;grace-period</code> SECONDS</p>
<dd> number of seconds to wait before starting health checks on newly-created instances</p>
<dt><code>&#8211;health-check-type</code> {EC2,ELB}</p>
<dd> service to obtain health check status from</p>
<dt><code>-l</code> LAUNCHCONFIG, <code>&#8211;launch-configuration</code> LAUNCHCONFIG</p>
<dd> name of the launch configuration to use with the new group (required)</p>
<dt><code>-M</code> COUNT, <code>&#8211;max-size</code> COUNT</p>
<dd> maximum group size (required)</p>
<dt><code>-m</code> COUNT, <code>&#8211;min-size</code> COUNT</p>
<dd> minimum group size (required)</p>
<dt><code>&#8211;placement-group</code> PLACEMENTGROUP</p>
<dd> placement group in which to launch new instances</p>
<dt><code>&#8211;termination-policies</code> POLICY1,POLICY2,&#8230;</p>
<dd> ordered list of termination policies. The first has the highest precedence.</p>
<dt><code>&#8211;vpc-zone-identifier</code> ZONE1,ZONE2,&#8230;</p>
<dd> comma-separated list of subnet identifiers. If you specify availability zones as well, ensure the subnets&#8217; availability zones match the ones you specified</p>
<dt><code>-z</code> ZONE1,ZONE2,&#8230;, <code>&#8211;availability-zones</code> ZONE1,ZONE2,&#8230;</p>
<dd> comma-separated list of availability zones for the new group (required unless subnets are supplied)</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> auto-scaling service endpoint URL</p>
<dt><code>&#8211;region</code> USER [at] REGION</p>
<dd> region and/or user names to search when looking up config file data</p>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</p>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</p>
<dt> <code>&#8211;security-token</code> TOKEN</p>
<dt><code>&#8211;debug</code></p>
<dd>
<dd>show debugging output</p>
<dt><code>&#8211;debugger</code></p>
<dd> launch interactive debugger on error</p>
<dt><code>&#8211;version</code></p>
<dd> show the program&#8217;s version and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit </p>
</dl>
<h2>Index</h2>
