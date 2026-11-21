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
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> List all of the resources in one or more stacks</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> STACK, <code>&#8211;name</code> STACK</dt>
<dd> limit results to a specific stack</dd>
<dt><code>-l</code> RESOURCE, <code>&#8211;logical-resource-id</code> RESOURCE</dt>
<dd> logical ID of the resource to describe (required)</dd>
<dt><code>-p</code> RESOURCE, <code>&#8211;physical-resource-id</code> RESOURCE</dt>
<dd> physical ID of the resource to describe (required)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> deployment templating service endpoint URL</dd>
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
