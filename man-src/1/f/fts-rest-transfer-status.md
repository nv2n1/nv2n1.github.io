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
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
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
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
