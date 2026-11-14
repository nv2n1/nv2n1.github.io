---
title: "fts-rest-transfer-list(1)"
name: "fts-rest-transfer-list"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-transfer-list/"
description: "fts-rest-transfer-list"
---

<h2>NAME</h2>
<p> fts-rest-transfer-list</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-transfer-list [options]</p>
<h2>DESCRIPTION</h2>
<p> This command can be used to list the running jobs, allowing to filter by user dn or vo name</p>
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
<dt><code>-u/&#8211;userdn</code></p>
<dd> Query only for the given user</p>
<dl>
<dt>
<dd></dl>
<dt><code>-o/&#8211;voname</code></p>
<dd> Query only for the given vo</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;source</code></p>
<dd> Query only for the given source storage element</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;destination</code></p>
<dd> Query only for the given destination storage element</p>
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
fts - rest - transfer - list - s &amp;nbsp;
https : // fts3-devel.cern.ch:8446&amp;nbsp;-o atlas
        Request ID : ff294db7 -
                     655a - 4c0a - 9efb - 44a994677bb3 Status : ACTIVE Client DN : &amp;nbsp;
/ DC = ch / DC = cern / OU = Organic Units / OU = Users / CN = ddmadmin / CN = 531497 / CN = Robot : ATLAS Data Management
                                                                                                         Reason : None
                                                                                                                      Submission time : 2014 -
                                                                                                                  04 - 15T07 : 05 : 38 Priority : 3 VO Name : atlas Request ID : a2e4586c - 760a - 469e-8303 - d0f3d5aadc73 Status : READY Client DN : &amp;nbsp;
/ DC = ch / DC = cern / OU = Organic Units / OU = Users / CN = ddmadmin / CN = 531497 / CN = Robot : ATLAS Data Management
                                                                                                         Reason : None
                                                                                                                      Submission time : 2014 -
                                                                                                                  04 - 15T07 : 07 : 33 Priority : 3 VO Name : atlas
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
<h2>Index</h2>
