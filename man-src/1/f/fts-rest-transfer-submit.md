---

title: "fts-rest-transfer-submit(1)"
name: "fts-rest-transfer-submit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-transfer-submit/"
description: "fts-rest-transfer-submit"
---

<p> fts-rest-transfer-submit</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-transfer-submit [options] SOURCE DESTINATION [CHECKSUM]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to submit new jobs to FTS3. It supports simple and bulk submissions. The bulk format is as follows:</p>
<dl>
<dt>
</dt><dd>
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
</dd></dl>
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
<dt><code>&#8211;delegate-when-lifetime-lt</code></dt>
<dd> Delegate the proxy when the remote lifetime is less than this value (in minutes)</dd>
<dl>
</dl>
<dt><code>-o/&#8211;overwrite</code></dt>
<dd> Overwrite files.</dd>
<dl>
</dl>
<dt><code>-r/&#8211;reuse</code></dt>
<dd> Enable session reuse for the transfer job.</dd>
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
<dt><code>&#8211;file-size</code></dt>
<dd> File size (in bytes)</dd>
<dl>
</dl>
<dt><code>-g/&#8211;gparam</code></dt>
<dd> Gridftp parameters.</dd>
<dl>
</dl>
<dt><code>-t/&#8211;dest-token</code></dt>
<dd> The destination space token or its description.</dd>
<dl>
</dl>
<dt><code>-S/&#8211;source-token</code></dt>
<dd> The source space token or its description.</dd>
<dl>
</dl>
<dt><code>-K/&#8211;compare-checksum</code></dt>
<dd> Compare checksums between source and destination.</dd>
<dl>
</dl>
<dt><code>&#8211;copy-pin-lifetime</code></dt>
<dd> Pin lifetime of the copy in seconds.</dd>
<dl>
</dl>
<dt><code>&#8211;bring-online</code></dt>
<dd> Bring online timeout in seconds.</dd>
<dl>
</dl>
<dt><code>&#8211;fail-nearline</code></dt>
<dd> Fail the transfer is the file is nearline.</dd>
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
<dt><code>-m/&#8211;multi-hop</code></dt>
<dd> Submit a multihop transfer.</dd>
<dl>
</dl>
<dt><code>&#8211;cloud-credentials</code></dt>
<dd> Use cloud credentials for the job (i. E. Dropbox).</dd>
<dl>
</dl>
<dt><code>&#8211;nostreams</code></dt>
<dd> Number of streams</dd>
<dl>
</dl>
<dt><code>&#8211;ipv4</code></dt>
<dd> Force ipv4</dd>
<dl>
</dl>
<dt><code>&#8211;ipv6</code></dt>
<dd> Force ipv6</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
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
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
