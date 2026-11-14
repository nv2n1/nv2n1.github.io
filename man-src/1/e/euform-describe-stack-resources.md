---
title: "euform-describe-stack-resources(1)"
name: "euform-describe-stack-resources"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euform-describe-stack-resources/"
description: "euform-describe-stack-resources – List all of the resources in one or more stacks"
---

<h2>NAME</h2>
<p> euform-describe-stack-resources &#8211; List all of the resources in one or more stacks</p>
<h2>SYNOPSIS</h2>
<p> euform-describe-stack-resources [-n STACK] [-l RESOURCE] [-p RESOURCE]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> List all of the resources in one or more stacks</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> STACK, <code>&#8211;name</code> STACK</p>
<dd> limit results to a specific stack</p>
<dt><code>-l</code> RESOURCE, <code>&#8211;logical-resource-id</code> RESOURCE</p>
<dd> logical ID of the resource to describe (required)</p>
<dt><code>-p</code> RESOURCE, <code>&#8211;physical-resource-id</code> RESOURCE</p>
<dd> physical ID of the resource to describe (required)</p>
<dt><code>&#8211;show-empty-fields</code></p>
<dd> show empty values as &quot;(nil)&quot;</p>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</p>
<dd> deployment templating service endpoint URL</p>
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
