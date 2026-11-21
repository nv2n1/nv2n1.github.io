---

title: "euca-fingerprint-key(1)"
name: "euca-fingerprint-key"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euca-fingerprint-key/"
description: "euca-fingerprint-key – Show the fingerprint of a private key as it would appear in the output of euca-describe-keypairs."
---

<h2>NAME</h2>
<p> euca-fingerprint-key &#8211; Show the fingerprint of a private key as it would appear in the output of euca-describe-keypairs.</p>
<p> euca-fingerprint-key [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] FILE</p>
<p> Show the fingerprint of a private key as it would appear in the output of euca-describe-keypairs.</p>
<h2>DESCRIPTION</h2>
<p> Note that this will differ from the key&#8217;s SSH key fingerprint.</p>
<h3>positional arguments:</h3>
<dl>
<dt>FILE</dt>
<dd> file containing the private key (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>&#8211;debug</code></dt>
<dd> show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
