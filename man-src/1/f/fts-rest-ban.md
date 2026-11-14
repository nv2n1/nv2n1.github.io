---
title: "fts-rest-ban(1)"
name: "fts-rest-ban"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-ban/"
description: "fts-rest-ban"
---

<h2>NAME</h2>
<p> fts-rest-ban</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-ban [options]</p>
<h2>DESCRIPTION</h2>
<p> Ban and unban storage elements and users</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h/&#8211;help</code></p>
<dd> Show this help message and exit</p>
<dl>
<dt>
<dd></dl>
<dt><code>-v/&#8211;verbose</code></p>
<dd> Verbose output.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-s/&#8211;endpoint</code></p>
<dd> Fts3 rest endpoint.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j/&#8211;json</code></p>
<dd> Print the output in json format.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;key</code></p>
<dd> The user certificate private key.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;cert</code></p>
<dd> The user certificate.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;capath</code></p>
<dd> Use the specified directory to verify the peer</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;insecure</code></p>
<dd> Do not validate the server certificate</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;access-token</code></p>
<dd> Oauth2 access token (supported only by some endpoints, takes precedence)</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;storage</code></p>
<dd> Storage element</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;user</code></p>
<dd> User dn</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;unban</code></p>
<dd> Unban instead of ban</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;status</code></p>
<dd> Status of the jobs that are already in the queue: cancel or wait</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;timeout</code></p>
<dd> The timeout for the jobs that are already in the queue if status is wait</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;allow-submit</code></p>
<dd> Allow submissions if status is wait</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre><code>
$ &amp;nbsp;
fts - rest - ban - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;--storage&amp;nbsp;gsiftp://sample
        No jobs affected
            $ &amp;nbsp;
fts - rest - ban - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;--storage&amp;nbsp;gsiftp://sample&amp;nbsp;--unban
        $
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
