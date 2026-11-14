---
title: "eulb-configure-healthcheck(1)"
name: "eulb-configure-healthcheck"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-configure-healthcheck/"
description: "eulb-configure-healthcheck – Configure health checking for instance registerd with a load balancer"
---

<h2>NAME</h2>
<p> eulb-configure-healthcheck &#8211; Configure health checking for instance registerd with a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-configure-healthcheck <code>&#8211;healthy-threshold</code> COUNT <code>&#8211;interval</code> SECONDS</p>
<dl>
<dt><code>-t</code> PROTOCOL:PORT[/PATH] <code>&#8211;timeout</code> SECONDS</p>
<dd> <code>&#8211;unhealthy-threshold</code> COUNT [&#8211;show-empty-fields] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Configure health checking for instance registerd with a load balancer</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;healthy-threshold</code> COUNT</p>
<dd> number of consecutive successful health checks that will mark instances as Healthy (required)</p>
<dt><code>&#8211;interval</code> SECONDS</p>
<dd> approximate interval between health checks (required)</p>
<dt><code>-t</code> PROTOCOL:PORT[/PATH], <code>&#8211;target</code> PROTOCOL:PORT[/PATH]</p>
<dd> connection target for health checks (required)</p>
<dt><code>&#8211;timeout</code> SECONDS</p>
<dd> maximum health check duration (required)</p>
<dt><code>&#8211;unhealthy-threshold</code> COUNT</p>
<dd> number of consecutive failed health checks that will mark instances as Unhealthy (required)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
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
