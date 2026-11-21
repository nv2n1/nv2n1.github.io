---

title: "fts-rest-ban(1)"
name: "fts-rest-ban"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-rest-ban/"
description: "fts-rest-ban"
---

<p> fts-rest-ban</p>
<h2>SYNOPIS</h2>
<p> Usage: fts-rest-ban [options]</p>
<h2>DESCRIPTION</h2>
<p> Ban and unban storage elements and users</p>
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
<dt><code>&#8211;storage</code></dt>
<dd> Storage element</dd>
<dl>
</dl>
<dt><code>&#8211;user</code></dt>
<dd> User dn</dd>
<dl>
</dl>
<dt><code>&#8211;unban</code></dt>
<dd> Unban instead of ban</dd>
<dl>
</dl>
<dt><code>&#8211;status</code></dt>
<dd> Status of the jobs that are already in the queue: cancel or wait</dd>
<dl>
</dl>
<dt><code>&#8211;timeout</code></dt>
<dd> The timeout for the jobs that are already in the queue if status is wait</dd>
<dl>
</dl>
<dt><code>&#8211;allow-submit</code></dt>
<dd> Allow submissions if status is wait</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
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
</dd></dl>
<h2>AUTHORS</h2>
<p> fts-devel [at] cern.ch. </p>
