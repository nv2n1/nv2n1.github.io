---
title: "euform-get-template-summary(1)"
name: "euform-get-template-summary"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euform-get-template-summary/"
description: "euform-get-template-summary – Summarize a template"
---

<h2>NAME</h2>
<p> euform-get-template-summary &#8211; Summarize a template</p>
<h2>SYNOPSIS</h2>
<p> euform-get-template-summary [&#8211;template-file FILE] [&#8211;template-url URL]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</p>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [STACK]</dl>
<h2>DESCRIPTION</h2>
<p> Summarize a template</p>
<h3>positional arguments:</h3>
<dl>
<dt>STACK</p>
<dd> name or ID of the stack (names cannot be used for deleted stacks)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;template-file</code> FILE</p>
<dd> file location containing JSON template</p>
<dt><code>&#8211;template-url</code> URL</p>
<dd> S3 URL for JSON template</p>
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
