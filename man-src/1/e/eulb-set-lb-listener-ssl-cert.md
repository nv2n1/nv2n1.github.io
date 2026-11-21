---
title: "eulb-set-lb-listener-ssl-cert(1)"
name: "eulb-set-lb-listener-ssl-cert"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eulb-set-lb-listener-ssl-cert/"
description: "eulb-set-lb-listener-ssl-cert – Change the certificate that terminates a load balancer’slistener’s SSL connections"
---

<h2>NAME</h2>
<p> eulb-set-lb-listener-ssl-cert &#8211; Change the certificate that terminates a load balancer&#8217;slistener&#8217;s SSL connections</p>
<h2>SYNOPSIS</h2>
<p> eulb-set-lb-listener-ssl-cert <code>-l</code> PORT <code>-c</code> ARN [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID]</dt>
<dd> [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] ELB</dd></dl>
<h2>DESCRIPTION</h2>
<p> Change the certificate that terminates a load balancer&#8217;slistener&#8217;s SSL connections</p>
<h3>positional arguments:</h3>
<dl>
<dt>ELB</dt>
<dd> name of the load balancer to modify (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-l</code> PORT, <code>&#8211;lb-port</code> PORT</dt>
<dd> port that should use the certificate (required)</dd>
<dt><code>-c</code> ARN, <code>&#8211;cert-id</code> ARN</dt>
<dd> ARN for the server certificate to use (required)</dd>
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
