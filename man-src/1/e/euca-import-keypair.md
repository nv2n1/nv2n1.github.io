---

title: "euca-import-keypair(1)"
name: "euca-import-keypair"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-import-keypair/"
description: "euca-import-keypair – Import a public RSA key as a new key pair"
---

<h2>NAME</h2>
<p> euca-import-keypair &#8211; Import a public RSA key as a new key pair</p>
<p> euca-import-keypair <code>-f</code> FILE [&#8211;show-empty-fields] [-U URL]</p>
<dl>
<dt>[&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY]</dt>
<dd> [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] KEYPAIR</dd></dl>
<p> Import a public RSA key as a new key pair</p>
<h3>positional arguments:</h3>
<dl>
<dt>KEYPAIR</dt>
<dd> name for the new key pair (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-f</code> FILE, <code>&#8211;public-key-file</code> FILE</dt>
<dd> name of a file containing the public key to import (required)</dd>
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
