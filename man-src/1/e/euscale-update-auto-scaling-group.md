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
<p> euscale-update-auto-scaling-group [&#8211;default-cooldown SECONDS]</p>
<dl>
<dt>[&#8211;desired-capacity COUNT]</dt>
<dd> [&#8211;grace-period SECONDS] [&#8211;health-check-type {EC2,ELB}] [-l LAUNCHCONFIG] [-M COUNT] [-m COUNT] [&#8211;placement-group PLACEMENTGROUP] [&#8211;termination-policies POLICY1,POLICY2,&#8230;] [&#8211;vpc-zone-identifier ZONE1,ZONE2,&#8230;] [-z ZONE1,ZONE2,&#8230;] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ASGROUP</dd></dl>
<p> Update an auto-scaling group&#8217;s parameters</p>
<h3>positional arguments:</h3>
<dl>
<dt>ASGROUP</dt>
<dd> name of the auto-scaling group to update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;default-cooldown</code> SECONDS</dt>
<dd> amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities may start</dd>
<dt><code>&#8211;desired-capacity</code> COUNT</dt>
<dd> number of running instances the group should contain</dd>
<dt><code>&#8211;grace-period</code> SECONDS</dt>
<dd> number of seconds to wait before starting health checks on newly-created instances</dd>
<dt><code>&#8211;health-check-type</code> {EC2,ELB}</dt>
<dd> service to obtain health check status from</dd>
<dt><code>-l</code> LAUNCHCONFIG, <code>&#8211;launch-configuration</code> LAUNCHCONFIG</dt>
<dd> name of the launch configuration to use with the new group (required)</dd>
<dt><code>-M</code> COUNT, <code>&#8211;max-size</code> COUNT</dt>
<dd> maximum group size (required)</dd>
<dt><code>-m</code> COUNT, <code>&#8211;min-size</code> COUNT</dt>
<dd> minimum group size (required)</dd>
<dt><code>&#8211;placement-group</code> PLACEMENTGROUP</dt>
<dd> placement group in which to launch new instances</dd>
<dt><code>&#8211;termination-policies</code> POLICY1,POLICY2,&#8230;</dt>
<dd> ordered list of termination policies. The first has the highest precedence.</dd>
<dt><code>&#8211;vpc-zone-identifier</code> ZONE1,ZONE2,&#8230;</dt>
<dd> comma-separated list of subnet identifiers. If you specify availability zones as well, ensure the subnets&#8217; availability zones match the ones you specified</dd>
<dt><code>-z</code> ZONE1,ZONE2,&#8230;, <code>&#8211;availability-zones</code> ZONE1,ZONE2,&#8230;</dt>
<dd> comma-separated list of availability zones for the new group (required unless subnets are supplied)</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> auto-scaling service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
