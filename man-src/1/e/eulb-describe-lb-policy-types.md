---

title: "eulb-describe-lb-policy-types(1)"
name: "eulb-describe-lb-policy-types"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-describe-lb-policy-types/"
description: "eulb-describe-lb-policy-types – Show information about load balancer policy types"
---

<p> eulb-describe-lb-policy-types &#8211; Show information about load balancer policy types</p>
<h2>SYNOPSIS</h2>
<p> eulb-describe-lb-policy-types [&#8211;show-long] [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] [POLTYPE [POLTYPE &#8230;]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> Show information about load balancer policy types</p>
<h3>positional arguments:</h3>
<dl>
<dt>POLTYPE</dt>
<dd> limit results to specific policy types</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;show-long</code></dt>
<dd> show all of the policy types&#8217; info</dd>
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
