---

title: "eulb-delete-lb-listeners(1)"
name: "eulb-delete-lb-listeners"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-delete-lb-listeners/"
description: "eulb-delete-lb-listeners – Delete one or more listeners from a load balancer"
---

<p> eulb-delete-lb-listeners &#8211; Delete one or more listeners from a load balancer</p>
<h2>SYNOPSIS</h2>
<p> eulb-delete-lb-listeners <code>-l</code> PORT1,PORT2,&#8230; [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<h2>DESCRIPTION</h2>
<p> Delete one or more listeners from a load balancer</p>
<h2>DESCRIPTION</h2>
<p> If a listener named with <code>-l</code>/&#8211;lb-ports does not exist, this command still succeeds.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> PORT1,PORT2,&#8230;, <code>&#8211;lb-ports</code> PORT1,PORT2,&#8230;</dt>
<dd> port numbers of the listeners to remove (required)</dd>
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
