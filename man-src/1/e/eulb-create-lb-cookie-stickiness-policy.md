---
title: "eulb-create-lb-cookie-stickiness-policy(1)"
name: "eulb-create-lb-cookie-stickiness-policy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-create-lb-cookie-stickiness-policy/"
description: "eulb-create-lb-cookie-stickiness-policy – Create a new stickiness policy for a load balancer, whereby the load balancer automatically generates cookies that it uses to route requests from each user..."
---

<h2>NAME</h2>
<p> eulb-create-lb-cookie-stickiness-policy &#8211; Create a new stickiness policy for a load balancer, whereby the load balancer automatically generates cookies that it uses to route requests from each user to the same back end instance. This type of policy can only be associated with HTTP or HTTPS listeners.</p>
<h2>SYNOPSIS</h2>
<p> eulb-create-lb-cookie-stickiness-policy <code>-e</code> SECONDS <code>-p</code> POLICY [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Create a new stickiness policy for a load balancer, whereby the load balancer automatically generates cookies that it uses to route requests from each user to the same back end instance. This type of policy can only be associated with HTTP or HTTPS listeners.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-e</code> SECONDS, <code>&#8211;expiration-period</code> SECONDS</p>
<dd> time period after which cookies should be considered stale (default: user&#8217;s session length) (required)</p>
<dt><code>-p</code> POLICY, <code>&#8211;policy-name</code> POLICY</p>
<dd> name of the new policy (required)</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> load balancing service endpoint URL</p>
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
