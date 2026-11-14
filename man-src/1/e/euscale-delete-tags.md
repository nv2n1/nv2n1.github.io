---
title: "euscale-delete-tags(1)"
name: "euscale-delete-tags"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-delete-tags/"
description: "euscale-delete-tags – Delete one or more resource tags"
---

<h2>NAME</h2>
<p> euscale-delete-tags &#8211; Delete one or more resource tags</p>
<h2>SYNOPSIS</h2>
<p> euscale-delete-tags <code>&#8211;tag</code> &quot;k=VALUE, id=VALUE, t=VALUE, v=VALUE,</p>
<dl>
<dt>p={true,false}&quot; [-U URL] [&#8211;region USER [at] REGION]</p>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dl>
<h2>DESCRIPTION</h2>
<p> Delete one or more resource tags</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;tag</code> &quot;k=VALUE, id=VALUE, t=VALUE, v=VALUE, p={true,false}&quot;</p>
<dd> attributes of a tag to affect. Tags follow the following format: &quot;id=resource-name, t=resource-type, k=tag-key, v=tag-val, p=propagate-at-launch-flag&quot;, where k is the tag&#8217;s name, v is the tag&#8217;s value, id is a resource ID, t is a resource type, and p is whether to propagate tags to instances created by the group. A value for &#8216;k=&#8217; is required for each tag. The rest are optional. This argument may be used more than once. Each time affects a different tag. (at least 1 required)</p>
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
