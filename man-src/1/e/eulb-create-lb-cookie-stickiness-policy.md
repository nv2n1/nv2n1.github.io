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
<dt>[&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create a new stickiness policy for a load balancer, whereby the load balancer automatically generates cookies that it uses to route requests from each user to the same back end instance. This type of policy can only be associated with HTTP or HTTPS listeners.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-e</code> SECONDS, <code>&#8211;expiration-period</code> SECONDS</dt>
<dd> time period after which cookies should be considered stale (default: user&#8217;s session length) (required)</dd>
<dt><code>-p</code> POLICY, <code>&#8211;policy-name</code> POLICY</dt>
<dd> name of the new policy (required)</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> load balancing service endpoint URL</dd>
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
