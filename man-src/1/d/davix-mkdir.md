---
title: "davix-mkdir(1)"
name: "davix-mkdir"
section: "1"
letter: "d"
url: "/docs/linux/man/1-davix-mkdir/"
description: "davix-mkdir – Directory creation tool based on libdavix."
---

<h2>NAME</h2>
<p> davix-mkdir &#8211; Directory creation tool based on libdavix.</p>
<h2>SYNOPSIS</h2>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> davix-mkdir [options]&#8230; url</p>
<h2>DESCRIPTION</h2>
<p> <code>davix-mkdir</code> is a tool to creat directories or collections with HTTP, Webdav or REST compatible services.<br />
 The command supports the protocol Http (http(s)://), WebDav (dav(s)://) and S3 (s3(s)://). </p>
<p> davix-mkdir is powered by libdavix. See <a href="/docs/linux/man/3-libdavix/">libdavix</a>(3) for details. </p>
<h2>OPTIONS</h2>
<p> <code>Common Options:</code> </p>
<dl>
<dt>
<dd> <code>&#8211;debug</code></dl>
<dl>
<dt>
<dd> Debug mode</dl>
<dl>
<dt>
<dd> <code>&#8211;header, -H</code></dl>
<dl>
<dt>
<dd> Add a header field to the request (eg: -H &quot;Depth: 1&quot; )</dl>
<dl>
<dt>
<dd> <code>&#8211;help, -h</code></dl>
<dl>
<dt>
<dd> Display this help message</dl>
<dl>
<dt>
<dd> <code>&#8211;metalink OPT </code></dl>
<dl>
<dt>
<dd> Metalink support. (OPT=failover[default]|no)</dl>
<dl>
<dt>
<dd> <code>&#8211;module, -P PLUGIN_NAME</code></dl>
<dl>
<dt>
<dd> Load a plugin or profile by name</dl>
<dl>
<dt>
<dd> <code>&#8211;redirection OPT </code></dl>
<dl>
<dt>
<dd> Transparent redirection support. (OPT=yes[default]|no)</dl>
<dl>
<dt>
<dd> <code>&#8211;proxy, -x URL</code></dl>
<dl>
<dt>
<dd> SOCKS5 proxy server URL. (ex: socks5://login:pass [at] socks.example.org)</dl>
<dl>
<dt>
<dd> <code>&#8211;trace</code></dl>
<dl>
<dt>
<dd> Traces specific scope(s), options include:</dl>
<dl>
<dt>
<dd> file &#8211; Davix file interface</dl>
<dl>
<dt>
<dd> posix &#8211; Davix POSIX interface</dl>
<dl>
<dt>
<dd> xml &#8211; XML parser output</dl>
<dl>
<dt>
<dd> ssl &#8211; SSL and certs details</dl>
<dl>
<dt>
<dd> header &#8211; HTTP queries headers</dl>
<dl>
<dt>
<dd> body &#8211; HTTP bodies</dl>
<dl>
<dt>
<dd> chain &#8211; IO chains info</dl>
<dl>
<dt>
<dd> core &#8211; Config and misc info</dl>
<dl>
<dt>
<dd> grid &#8211; Misc info from 3rd parties</dl>
<dl>
<dt>
<dd> socket &#8211; Socket info</dl>
<dl>
<dt>
<dd> locks &#8211; WebDAV locking info</dl>
<dl>
<dt>
<dd> all &#8211; Traces everything</dl>
<dl>
<dt>
<dd> <code>&#8211;version</code></dl>
<dl>
<dt>
<dd> Display version</dl>
<p> <code>Security Options:</code> </p>
<dl>
<dt>
<dd> <code>&#8211;capath CA_path</code></dl>
<dl>
<dt>
<dd> Add an additional certificate authority directory</dl>
<dl>
<dt>
<dd> <code>&#8211;cert, -E cred_path</code></dl>
<dl>
<dt>
<dd> Client Certificate in PEM format</dl>
<dl>
<dt>
<dd> <code>&#8211;key priv_path</code></dl>
<dl>
<dt>
<dd> Private key in PEM format</dl>
<dl>
<dt>
<dd> <code>&#8211;insecure, -k</code></dl>
<dl>
<dt>
<dd> Disable SSL credential checks</dl>
<dl>
<dt>
<dd> <code>&#8211;userlogin</code></dl>
<dl>
<dt>
<dd> User login for login/password authentication</dl>
<dl>
<dt>
<dd> <code>&#8211;userpass</code></dl>
<dl>
<dt>
<dd> User password for login/password authentication</dl>
<dl>
<dt>
<dd> <code>&#8211;s3secretkey</code></dl>
<dl>
<dt>
<dd> AWS S3 authentication: secret key</dl>
<dl>
<dt>
<dd> <code>&#8211;s3accesskey</code></dl>
<dl>
<dt>
<dd> AWS S3 authentication: access key</dl>
<dl>
<dt>
<dd> <code>&#8211;s3region</code></dl>
<dl>
<dt>
<dd> AWS S3 authentication: region</dl>
<dl>
<dt>
<dd> <code>&#8211;s3token</code></dl>
<dl>
<dt>
<dd> AWS S3 security token &#8211; used along with STS temporary credentials</dl>
<dl>
<dt>
<dd> <code>&#8211;s3alternate</code></dl>
<dl>
<dt>
<dd> Specify this flag if you need to use a path-based S3 URL</dl>
<dl>
<dt>
<dd> <code>&#8211;azurekey</code></dl>
<dl>
<dt>
<dd> Azure authentication key</dl>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> </p>
<h2>EXAMPLES</h2>
<p> <code>Creat a directory over WebDav<br />
&nbsp;<wbr>&nbsp;<wbr>davix-mkdir&nbsp;<wbr><a href="dav://webdav.example.org/dir/directory_to_create">dav://webdav.example.org/dir/directory_to_create</a> </p>
<p> Creat a directory on a Grid Storage with VOMS authentication<br />
&nbsp;<wbr>&nbsp;<wbr>davix-mkdir -P grid&nbsp;<wbr><a href="davs://grid-storage.example.org/dir1/directory_to_create">davs://grid-storage.example.org/dir1/directory_to_create</a> </p>
<p> </code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libdavix/">libdavix</a>(3),</code><a href="/docs/linux/man/1-davix-rm/">davix-rm</a>(1),<code><a href="/docs/linux/man/1-davix-put/">davix-put</a>(1),</code> </p>
<h2>LINKS</h2>
<p> <code><a rel="nofollow" href="http://dmc.web.cern.ch/projects/davix/home">http://dmc.web.cern.ch/projects/davix/home</a></code> </p>
<h2>AUTHORS</h2>
<p> Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;, IT-SDC-ID, CERN </p>
<h2>Index</h2>
