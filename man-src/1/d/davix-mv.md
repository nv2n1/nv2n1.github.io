---

title: "davix-mv(1)"
name: "davix-mv"
section: "1"
letter: "d"
url: "/docs/linux/man/1-davix-mv/"
description: "davix-mv – Rename tool based on libdavix"
---

<p> davix-mv &#8211; Rename tool based on libdavix</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>davix-mv&nbsp;<wbr>[options]&#8230; original-url new-url </p>
<h2>DESCRIPTION</h2>
<p> <code>davix-mv</code> is a tool to rename/move resources with HTTP, Webdav or REST compatible services.<br />
 The commands can rename/move resources and resources containers. </p>
<p> davix-mv is powered by libdavix. See <a href="/docs/linux/man/3-libdavix/">libdavix</a>(3) for details. </p>
<h2>OPTIONS</h2>
<p> <code>Common Options:</code> </p>
<dl>
<dt>
</dt><dd> <code>&#8211;debug</code></dd></dl>
<dl>
<dt>
</dt><dd> Debug mode</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;header, -H</code></dd></dl>
<dl>
<dt>
</dt><dd> Add a header field to the request (eg: -H &quot;Depth: 1&quot; )</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;help, -h</code></dd></dl>
<dl>
<dt>
</dt><dd> Display this help message</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;metalink OPT </code></dd></dl>
<dl>
<dt>
</dt><dd> Metalink support. (OPT=failover[default]|no)</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;module, -P PLUGIN_NAME</code></dd></dl>
<dl>
<dt>
</dt><dd> Load a plugin or profile by name</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;redirection OPT </code></dd></dl>
<dl>
<dt>
</dt><dd> Transparent redirection support. (OPT=yes[default]|no)</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;proxy, -x URL</code></dd></dl>
<dl>
<dt>
</dt><dd> SOCKS5 proxy server URL. (ex: socks5://login:pass [at] socks.example.org)</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;trace</code></dd></dl>
<dl>
<dt>
</dt><dd> Traces specific scope(s), options include:</dd></dl>
<dl>
<dt>
</dt><dd> file &#8211; Davix file interface</dd></dl>
<dl>
<dt>
</dt><dd> posix &#8211; Davix POSIX interface</dd></dl>
<dl>
<dt>
</dt><dd> xml &#8211; XML parser output</dd></dl>
<dl>
<dt>
</dt><dd> ssl &#8211; SSL and certs details</dd></dl>
<dl>
<dt>
</dt><dd> header &#8211; HTTP queries headers</dd></dl>
<dl>
<dt>
</dt><dd> body &#8211; HTTP bodies</dd></dl>
<dl>
<dt>
</dt><dd> chain &#8211; IO chains info</dd></dl>
<dl>
<dt>
</dt><dd> core &#8211; Config and misc info</dd></dl>
<dl>
<dt>
</dt><dd> grid &#8211; Misc info from 3rd parties</dd></dl>
<dl>
<dt>
</dt><dd> socket &#8211; Socket info</dd></dl>
<dl>
<dt>
</dt><dd> locks &#8211; WebDAV locking info</dd></dl>
<dl>
<dt>
</dt><dd> all &#8211; Traces everything</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;version</code></dd></dl>
<dl>
<dt>
</dt><dd> Display version</dd></dl>
<p> <code>Security Options:</code> </p>
<dl>
<dt>
</dt><dd> <code>&#8211;capath CA_path</code></dd></dl>
<dl>
<dt>
</dt><dd> Add an additional certificate authority directory</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;cert, -E cred_path</code></dd></dl>
<dl>
<dt>
</dt><dd> Client Certificate in PEM format</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;key priv_path</code></dd></dl>
<dl>
<dt>
</dt><dd> Private key in PEM format</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;insecure, -k</code></dd></dl>
<dl>
<dt>
</dt><dd> Disable SSL credential checks</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;userlogin</code></dd></dl>
<dl>
<dt>
</dt><dd> User login for login/password authentication</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;userpass</code></dd></dl>
<dl>
<dt>
</dt><dd> User password for login/password authentication</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;s3secretkey</code></dd></dl>
<dl>
<dt>
</dt><dd> AWS S3 authentication: secret key</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;s3accesskey</code></dd></dl>
<dl>
<dt>
</dt><dd> AWS S3 authentication: access key</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;s3region</code></dd></dl>
<dl>
<dt>
</dt><dd> AWS S3 authentication: region</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;s3token</code></dd></dl>
<dl>
<dt>
</dt><dd> AWS S3 security token &#8211; used along with STS temporary credentials</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;s3alternate</code></dd></dl>
<dl>
<dt>
</dt><dd> Specify this flag if you need to use a path-based S3 URL</dd></dl>
<dl>
<dt>
</dt><dd> <code>&#8211;azurekey</code></dd></dl>
<dl>
<dt>
</dt><dd> Azure authentication key</dd></dl>
<h2>EXAMPLES</h2>
<p> <code> Rename a resource over HTTP<br />
&nbsp;<wbr>&nbsp;<wbr>davix-mv&nbsp;<wbr><a rel="nofollow" href="http://example.org/rename_me.txt">http://example.org/rename_me.txt</a>&nbsp;<wbr><a href="http://example.org/thanks.txt">http://example.org/thanks.txt</a> </p>
<p> Move a resource on a Grid Storage with VOMS authentication<br />
&nbsp;<wbr>&nbsp;<wbr>davix-mv -P grid&nbsp;<wbr><a href="davs://grid-storage.example.org/dir1/dir2/move_me.txt">davs://grid-storage.example.org/dir1/dir2/move_me.txt</a>&nbsp;<wbr><a href="davs://grid-storage.example.org/dir1/move_me.txt">davs://grid-storage.example.org/dir1/move_me.txt</a> </p>
<p> </code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libdavix/">libdavix</a>(3),</code><a href="/docs/linux/man/1-davix-ls/">davix-ls</a>(1),<code><a href="/docs/linux/man/1-davix-get/">davix-get</a>(1),</code><a href="/docs/linux/man/1-davix-put/">davix-put</a>(1), </p>
<h2>LINKS</h2>
<p> <code><a rel="nofollow" href="http://dmc.web.cern.ch/projects/davix/home">http://dmc.web.cern.ch/projects/davix/home</a></code> </p>
<h2>AUTHORS</h2>
<p> Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;, IT-SDC-ID, CERN </p>
