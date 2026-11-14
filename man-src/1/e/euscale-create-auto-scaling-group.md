---
title: "euscale-create-auto-scaling-group(1)"
name: "euscale-create-auto-scaling-group"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-create-auto-scaling-group/"
description: "euscale-create-auto-scaling-group – Create a new auto-scaling group"
---

<h2>NAME</h2>
<p> euscale-create-auto-scaling-group &#8211; Create a new auto-scaling group</p>
<h2>SYNOPSIS</h2>
<p> euscale-create-auto-scaling-group <code>-l</code> LAUNCHCONFIG <code>-M</code> COUNT <code>-m</code> COUNT</p>
<dl>
<dt>[&#8211;default-cooldown SECONDS]</p>
<dd> [&#8211;desired-capacity COUNT] [&#8211;grace-period SECONDS] [&#8211;health-check-type {EC2,ELB}] [&#8211;load-balancers ELB1,ELB2,&#8230;] [&#8211;placement-group PLACEMENTGROUP] [&#8211;tag &quot;k=VALUE, id=VALUE, t=VALUE, v=VALUE, p={true,false}&quot;] [&#8211;termination-policies POLICY1,POLICY2,&#8230;] [&#8211;vpc-zone-identifier ZONE1,ZONE2,&#8230;] [-z ZONE1,ZONE2,&#8230;] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dl>
<h2>DESCRIPTION</h2>
<p> Create a new auto-scaling group</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</p>
<dd> name of the new auto-scaling group (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> LAUNCHCONFIG, <code>&#8211;launch-configuration</code> LAUNCHCONFIG</p>
<dd> name of the launch configuration to use with the new group (required)</p>
<dt><code>-M</code> COUNT, <code>&#8211;max-size</code> COUNT</p>
<dd> maximum group size (required)</p>
<dt><code>-m</code> COUNT, <code>&#8211;min-size</code> COUNT</p>
<dd> minimum group size (required)</p>
<dt><code>&#8211;default-cooldown</code> SECONDS</p>
<dd> amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities may start</p>
<dt><code>&#8211;desired-capacity</code> COUNT</p>
<dd> number of running instances the group should contain</p>
<dt><code>&#8211;grace-period</code> SECONDS</p>
<dd> number of seconds to wait before starting health checks on newly-created instances</p>
<dt><code>&#8211;health-check-type</code> {EC2,ELB}</p>
<dd> service to obtain health check status from</p>
<dt><code>&#8211;load-balancers</code> ELB1,ELB2,&#8230;</p>
<dd> comma-separated list of load balancers to use</p>
<dt><code>&#8211;placement-group</code> PLACEMENTGROUP</p>
<dd> placement group in which to launch new instances</p>
<dt><code>&#8211;tag</code> &quot;k=VALUE, id=VALUE, t=VALUE, v=VALUE, p={true,false}&quot;</p>
<dd> attributes of a tag to affect. Tags follow the following format: &quot;id=resource-name, t=resource-type, k=tag-key, v=tag-val, p=propagate-at-launch-flag&quot;, where k is the tag&#8217;s name, v is the tag&#8217;s value, id is a resource ID, t is a resource type, and p is whether to propagate tags to instances created by the group. A value for &#8216;k=&#8217; is required for each tag. The rest are optional. This argument may be used more than once. Each time affects a different tag.</p>
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
