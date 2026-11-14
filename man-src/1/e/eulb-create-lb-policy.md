---
title: "eulb-create-lb-policy(1)"
name: "eulb-create-lb-policy"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-create-lb-policy/"
description: "eulb-create-lb-policy – Add a new policy to a load balancer"
---

<h2>NAME</h2>
<p> eulb-create-lb-policy &#8211; Add a new policy to a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-create-lb-policy <code>-n</code> POLICY <code>-t</code> POLTYPE</p>
<dl>
<dt>[-a &quot;name=NAME, value=VALUE&quot;] [-A NAME=VALUE,&#8230;]</p>
<dd> [&#8211;attributes-from-file FILE] [-U URL] [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dl>
<h2>DESCRIPTION</h2>
<p> Add a new policy to a load balancer</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</p>
<dd> name of the load balancer to modify (required)</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-n</code> POLICY, <code>&#8211;policy-name</code> POLICY</p>
<dd> name of the new policy (required)</p>
<dt><code>-t</code> POLTYPE, <code>&#8211;policy-type</code> POLTYPE</p>
<dd> type of the new policy. For a list of policy types, use eulb-describe-lb-policy-types. (required)</p>
<dt><code>-a</code> &quot;name=NAME, value=VALUE&quot;, <code>&#8211;attribute</code> &quot;name=NAME, value=VALUE&quot;</p>
<dd> name and value for each attribute associated with the new policy. Use this option multiple times to supply multiple attributes.</p>
<dt><code>-A</code> NAME=VALUE,&#8230;, <code>&#8211;attributes</code> NAME=VALUE,&#8230;</p>
<dd> a comma-delimited list of attribute names and values to associate with the new policy, each pair of which is separated by &quot;=&quot;. This is a more concise alternative to the <code>-a</code>/&#8211;attribute option.</p>
<dt><code>&#8211;attributes-from-file</code> FILE</p>
<dd> a file containing attribute names and values to associate with the new policy, one per line, each pair of which is separated by &quot;=&quot;. Lines that are blank or begin with &quot;#&quot; are ignored.</p>
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
