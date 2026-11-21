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
<p> This command can be used to submit a deletion job to FTS3. It supports simple and bulk submissions.</p>
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
<dt><code>-b/&#8211;blocking</code></dt>
<dd> Blocking mode. Wait until the operation completes.</dd>
<dl>
</dl>
<dt><code>-i/&#8211;interval</code></dt>
<dd> Interval between two poll operations in blocking mode.</dd>
<dl>
</dl>
<dt><code>-e/&#8211;expire</code></dt>
<dd> Expiration time of the delegation in minutes.</dd>
<dl>
</dl>
<dt><code>&#8211;job-metadata</code></dt>
<dd> Transfer job metadata.</dd>
<dl>
</dl>
<dt><code>&#8211;file-metadata</code></dt>
<dd> File metadata.</dd>
<dl>
</dl>
<dt><code>-S/&#8211;spacetoken</code></dt>
<dd> The space token or its description.</dd>
<dl>
</dl>
<dt><code>&#8211;dry-run</code></dt>
<dd> Do not send anything, just print the json message.</dd>
<dl>
</dl>
<dt><code>-f/&#8211;file</code></dt>
<dd> Name of configuration file</dd>
<dl>
</dl>
<dt><code>&#8211;retry</code></dt>
<dd> Number of retries. If 0, the server default will be used. If negative, there will be no retries.</dd>
<dl>
</dl>
<dt><code>&#8211;cloud-credentials</code></dt>
<dd> Use cloud credentials for the job (i. E. Dropbox).</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
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
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
