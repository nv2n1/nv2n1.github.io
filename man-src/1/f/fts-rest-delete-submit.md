---
title: "fts-rest-delete-submit(1)"
name: "fts-rest-delete-submit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-delete-submit/"
description: "fts-rest-delete-submit"
---

<h2>NAME</h2>
<p> fts-rest-delete-submit</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-delete-submit [options] SURL1 [SURL2] [SURL3] [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to submit a deletion job to FTS3. It supports simple and bulk submissions.</p>
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
<dt><code>-b/&#8211;blocking</code></p>
<dd> Blocking mode. Wait until the operation completes.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-i/&#8211;interval</code></p>
<dd> Interval between two poll operations in blocking mode.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-e/&#8211;expire</code></p>
<dd> Expiration time of the delegation in minutes.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;job-metadata</code></p>
<dd> Transfer job metadata.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;file-metadata</code></p>
<dd> File metadata.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-S/&#8211;spacetoken</code></p>
<dd> The space token or its description.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;dry-run</code></p>
<dd> Do not send anything, just print the json message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-f/&#8211;file</code></p>
<dd> Name of configuration file</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;retry</code></p>
<dd> Number of retries. If 0, the server default will be used. If negative, there will be no retries.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;cloud-credentials</code></p>
<dd> Use cloud credentials for the job (i. E. Dropbox).</p>
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
fts - rest - delete - submit - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;gsiftp://source.host/file1&amp;nbsp;gsiftp://source.host/file2
        Job successfully submitted.Job id : 9fee8c1e-c46d -
    11e3 - 8299 - 02163e00a17a $ &amp;nbsp;
fts - rest - delete - submit - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;-f bulk.list
        Job successfully submitted.Job id : 9fee8c1e-c46d -
    11e3 - 8299 - 02163e00a17a
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
