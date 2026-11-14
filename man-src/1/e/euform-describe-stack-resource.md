---
title: "euform-describe-stack-resource(1)"
name: "euform-describe-stack-resource"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euform-describe-stack-resource/"
description: "euform-describe-stack-resource – Describe a resource from a particular stack"
---

<h2>NAME</h2>
<p> euform-describe-stack-resource &#8211; Describe a resource from a particular stack</p>
<h2>SYNOPSIS</h2>
<p> euform-describe-stack-resource <code>-l</code> RESOURCE [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] STACK</dl>
<h2>DESCRIPTION</h2>
<p> Describe a resource from a particular stack</p>
<h3>positional arguments:</h3>
<dl>
<dt>STACK</p>
<dd> name of the stack (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> RESOURCE, <code>&#8211;logical-resource-id</code> RESOURCE</p>
<dd> logical ID of the resource to describe (required)</p>
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
