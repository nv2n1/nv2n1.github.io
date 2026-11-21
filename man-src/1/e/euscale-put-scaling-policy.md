---

title: "euscale-put-scaling-policy(1)"
name: "euscale-put-scaling-policy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-put-scaling-policy/"
description: "euscale-put-scaling-policy – Create or update an auto-scaling group’s scaling policy"
---

<h2>NAME</h2>
<p> euscale-put-scaling-policy &#8211; Create or update an auto-scaling group&#8217;s scaling policy</p>
<p> euscale-put-scaling-policy <code>-g</code> ASGROUP <code>-a</code> SCALE <code>-t</code></p>
<dl>
<dt>{ChangeInCapacity,ExactCapacity,PercentChangeInCapacity}</dt>
<dd> [&#8211;cooldown SECONDS] [-s PERCENT] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] POLICY</dd></dl>
<p> Create or update an auto-scaling group&#8217;s scaling policy</p>
<h3>positional arguments:</h3>
<dl>
<dt>POLICY</dt>
<dd> name of the policy to create or update (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-g</code> ASGROUP, <code>&#8211;auto-scaling-group</code> ASGROUP</dt>
<dd> name of the auto-scaling group the policy is associated with (required)</dd>
<dt><code>-a</code> SCALE, <code>&#8211;adjustment</code> SCALE</dt>
<dd> amount to scale the group&#8217;s capacity of the group. Use a negative value, as in &quot;&#8211;adjustment=-1&quot;, to decrease capacity. (required)</dd>
<dt><code>-t</code> {ChangeInCapacity,ExactCapacity,PercentChangeInCapacity}, <code>&#8211;type</code> {ChangeInCapacity,ExactCapacity,PercentChangeInCapacity}</dt>
<dd> whether the adjustment is the new desired size or an increment to the group&#8217;s current capacity. An increment can either be a fixed number or a percentage of current capacity. (required)</dd>
<dt><code>&#8211;cooldown</code> SECONDS</dt>
<dd> waiting period after successful auto-scaling activities during which later auto-scaling activities will not execute</dd>
<dt><code>-s</code> PERCENT, <code>&#8211;min-adjustment-step</code> PERCENT</dt>
<dd> for a PercentChangeInCapacity type policy, guarantee that this policy will change the group&#8217;s desired capacity by at least this much</dd>
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
