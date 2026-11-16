---
title: "fts-rest-transfer-cancel(1)"
name: "fts-rest-transfer-cancel"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-transfer-cancel/"
description: "fts-rest-transfer-cancel"
---

<h2>NAME</h2>
<p> fts-rest-transfer-cancel</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-transfer-cancel [options]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to cancel a running job. It returns the final state of the canceled job. Please, mind that if the job is already in a final state (FINISHEDDIRTY, FINISHED, FAILED), this command will return this state. You can additionally cancel only a subset appending a comma-separated list of file ids</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h/&#8211;help</code></dt>
<dd> Show this help message and exit</dd>
<dl>
</dl>
<dt><code>-v/&#8211;verbose</code></dt>
<dd> Verbose output.</dd>
<dl>
</dl>
<dt><code>-s/&#8211;endpoint</code></dt>
<dd> Fts3 rest endpoint.</dd>
<dl>
</dl>
<dt><code>-j/&#8211;json</code></dt>
<dd> Print the output in json format.</dd>
<dl>
</dl>
<dt><code>&#8211;key</code></dt>
<dd> The user certificate private key.</dd>
<dl>
</dl>
<dt><code>&#8211;cert</code></dt>
<dd> The user certificate.</dd>
<dl>
</dl>
<dt><code>&#8211;capath</code></dt>
<dd> Use the specified directory to verify the peer</dd>
<dl>
</dl>
<dt><code>&#8211;insecure</code></dt>
<dd> Do not validate the server certificate</dd>
<dl>
</dl>
<dt><code>&#8211;access-token</code></dt>
<dd> Oauth2 access token (supported only by some endpoints, takes precedence)</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
<pre><code>
$ &amp;nbsp;
fts - rest - transfer - cancel - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;c079a636-c363-11e3-b7e5-02163e009f5a
        FINISHED
            $ &amp;nbsp;
fts - rest - transfer - cancel - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;c079a636-c363-11e3-b7e5-02163e009f5a:5658,5659,5670
        CANCELED,
        CANCELED,
        CANCELED
</code></pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
