---
title: "euca-confirm-product-instance(1)"
name: "euca-confirm-product-instance"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-confirm-product-instance/"
description: "euca-confirm-product-instance – Verify if a product code is associated with an instance"
---

<h2>NAME</h2>
<p> euca-confirm-product-instance &#8211; Verify if a product code is associated with an instance</p>
<h2>SYNOPSIS</h2>
<p> euca-confirm-product-instance <code>-i</code> INSTANCE [&#8211;show-empty-fields]</p>
<dl>
<dt>[-U URL] [&#8211;region USER [at] REGION]</dt>
<dd> [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] CODE</dd></dl>
<h2>DESCRIPTION</h2>
<p> Verify if a product code is associated with an instance</p>
<h3>positional arguments:</h3>
<dl>
<dt>CODE</dt>
<dd> product code to confirm (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-i</code> INSTANCE, <code>&#8211;instance</code> INSTANCE</dt>
<dd> ID of the instance to confirm (required)</dd>
<dt><code>&#8211;show-empty-fields</code></dt>
<dd> show empty values as &quot;(nil)&quot;</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> compute service endpoint URL</dd>
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
