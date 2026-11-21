---
title: "eulb-describe-lb-policies(1)"
name: "eulb-describe-lb-policies"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-describe-lb-policies/"
description: "eulb-describe-lb-policies – Show information about load balancer policies"
---

<h2>NAME</h2>
<p> eulb-describe-lb-policies &#8211; Show information about load balancer policies</p>
<h2>SYNOPSIS</h2>
<p> eulb-describe-lb-policies [-p POLICY1,POLICY2,&#8230;] [&#8211;show-long]</p>
<dl>
<dt>[&#8211;show-empty-fields] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [ELB]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about load balancer policies</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> show policies associated with a specific load balancer (default: only describe sample policies provided by the service)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-p</code> POLICY1,POLICY2,&#8230;, <code>&#8211;policy-names</code> POLICY1,POLICY2,&#8230;</dt>
<dd> limit results to specific policies</dd>
<dt><code>&#8211;show-long</code></dt>
<dd> show all of the policies&#8217; info</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
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
