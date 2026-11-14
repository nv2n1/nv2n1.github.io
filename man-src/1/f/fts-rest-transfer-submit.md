---
title: "fts-rest-transfer-submit(1)"
name: "fts-rest-transfer-submit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-transfer-submit/"
description: "fts-rest-transfer-submit"
---

<h2>NAME</h2>
<p> fts-rest-transfer-submit</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-transfer-submit [options] SOURCE DESTINATION [CHECKSUM]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to submit new jobs to FTS3. It supports simple and bulk submissions. The bulk format is as follows:</p>
<dl>
<dt>
<dd>
<pre><code>
{
    &amp;nbsp;
    &amp;nbsp;
    "files" : &amp;nbsp;
    [
        &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; {
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"sources":&amp;nbsp;[
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"gsiftp://source.host/file"
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;],
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"destinations":&amp;nbsp;[
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"gsiftp://destination.host/file"
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;],
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"metadata":&amp;nbsp;"file-metadata",
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"checksum":&amp;nbsp;"ADLER32:1234",
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"filesize": 1024
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; },
                                    &amp;nbsp;
        &amp;nbsp; &amp;nbsp; &amp;nbsp; {
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"sources":&amp;nbsp;[
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"gsiftp://source.host/file2"
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;],
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"destinations":&amp;nbsp;[
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"gsiftp://destination.host/file2"
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;],
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"metadata":&amp;nbsp;"file2-metadata",
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"checksum":&amp;nbsp;"ADLER32:4321",
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"filesize": 2048,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;"activity":&amp;nbsp;"default"
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; } &amp; nbsp; &amp;nbsp;
    ]
}
</code></pre>
</dl>
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
<dt><code>&#8211;delegate-when-lifetime-lt</code></p>
<dd> Delegate the proxy when the remote lifetime is less than this value (in minutes)</p>
<dl>
<dt>
<dd></dl>
<dt><code>-o/&#8211;overwrite</code></p>
<dd> Overwrite files.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-r/&#8211;reuse</code></p>
<dd> Enable session reuse for the transfer job.</p>
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
<dt><code>&#8211;file-size</code></p>
<dd> File size (in bytes)</p>
<dl>
<dt>
<dd></dl>
<dt><code>-g/&#8211;gparam</code></p>
<dd> Gridftp parameters.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-t/&#8211;dest-token</code></p>
<dd> The destination space token or its description.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-S/&#8211;source-token</code></p>
<dd> The source space token or its description.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-K/&#8211;compare-checksum</code></p>
<dd> Compare checksums between source and destination.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;copy-pin-lifetime</code></p>
<dd> Pin lifetime of the copy in seconds.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bring-online</code></p>
<dd> Bring online timeout in seconds.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;fail-nearline</code></p>
<dd> Fail the transfer is the file is nearline.</p>
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
<dt><code>-m/&#8211;multi-hop</code></p>
<dd> Submit a multihop transfer.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;cloud-credentials</code></p>
<dd> Use cloud credentials for the job (i. E. Dropbox).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;nostreams</code></p>
<dd> Number of streams</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;ipv4</code></p>
<dd> Force ipv4</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;ipv6</code></p>
<dd> Force ipv6</p>
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
fts - rest - transfer - submit - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;gsiftp://source.host/file&amp;nbsp;gsiftp://destination.host/file
        Job successfully submitted.Job id : 9fee8c1e-c46d -
    11e3 - 8299 - 02163e00a17a $ &amp;nbsp;
fts - rest - transfer - submit - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;-f bulk.json
        Job successfully submitted.Job id : 9fee8c1e-c46d -
    11e3 - 8299 - 02163e00a17a
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
