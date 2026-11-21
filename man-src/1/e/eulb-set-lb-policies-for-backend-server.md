---

title: "eulb-set-lb-policies-for-backend-server(1)"
name: "eulb-set-lb-policies-for-backend-server"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-set-lb-policies-for-backend-server/"
description: "eulb-set-lb-policies-for-backend-server – Change the policies associated with a port on which load-balanced back end servers listen."
---

<p> eulb-set-lb-policies-for-backend-server &#8211; Change the policies associated with a port on which load-balanced back end servers listen.</p>
<h2>SYNOPSIS</h2>
<p> eulb-set-lb-policies-for-backend-server <code>-i</code> PORT <code>-p</code> POLICY1,POLICY2,&#8230;</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<h2>DESCRIPTION</h2>
<p> Change the policies associated with a port on which load-balanced back end servers listen.</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> PORT, <code>&#8211;instance-port</code> PORT</dt>
<dd> port number of the back end server (required)</dd>
<dt><code>-p</code> POLICY1,POLICY2,&#8230;, <code>&#8211;policy-names</code> POLICY1,POLICY2,&#8230;</dt>
<dd> list of policies to associate with the back end server (required)</dd>
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
