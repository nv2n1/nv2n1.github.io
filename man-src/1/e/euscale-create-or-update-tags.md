---
title: "euscale-create-or-update-tags(1)"
name: "euscale-create-or-update-tags"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euscale-create-or-update-tags/"
description: "euscale-create-or-update-tags – Create or update one or more resource tags"
---

<h2>NAME</h2>
<p> euscale-create-or-update-tags &#8211; Create or update one or more resource tags</p>
<h2>SYNOPSIS</h2>
<p> euscale-create-or-update-tags <code>&#8211;tag</code> &quot;k=VALUE, id=VALUE, t=VALUE,</p>
<dl>
<dt>v=VALUE, p={true,false}&quot; [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Create or update one or more resource tags</p>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;tag</code> &quot;k=VALUE, id=VALUE, t=VALUE, v=VALUE, p={true,false}&quot;</dt>
<dd> attributes of a tag to affect. Tags follow the following format: &quot;id=resource-name, t=resource-type, k=tag-key, v=tag-val, p=propagate-at-launch-flag&quot;, where k is the tag&#8217;s name, v is the tag&#8217;s value, id is a resource ID, t is a resource type, and p is whether to propagate tags to instances created by the group. A value for &#8216;k=&#8217; is required for each tag. The rest are optional. This argument may be used more than once. Each time affects a different tag. (at least 1 required)</dd>
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
