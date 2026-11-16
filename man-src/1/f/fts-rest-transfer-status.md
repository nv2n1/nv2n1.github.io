---
title: "fts-rest-transfer-status(1)"
name: "fts-rest-transfer-status"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-transfer-status/"
description: "fts-rest-transfer-status"
---

<h2>NAME</h2>
<p> fts-rest-transfer-status</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-transfer-status [options] JOB_ID</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to check the current status of a given job</p>
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
fts - rest - transfer - status - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;c079a636-c363-11e3-b7e5-02163e009f5a
        Request ID : c079a636 -
                     c363 - 11e3 - b7e5 - 02163e009f5a Status : FINISHED Client DN : &amp;nbsp;
/ DC = ch / DC = cern / OU = Organic Units / OU = Users / CN = saketag / CN = 678984 / CN = Alejandro Alvarez Ayllon
                                                                                                Reason : Submission time : 2014 -
                                                                                                         04 - 13T23 : 31 : 34 Priority : 3 VO Name : dteam
</code></pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
