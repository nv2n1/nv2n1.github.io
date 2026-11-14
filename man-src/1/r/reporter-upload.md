---
title: "reporter-upload(1)"
name: "reporter-upload"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-upload/"
description: "reporter-upload – Uploads compressed tarball of problem directory."
---

<h2 class="name">NAME</h2>
<p> reporter-upload &#8211; Uploads compressed tarball of problem directory. </p>
<h2>SYNOPSIS</h2>
<p> <i>reporter-upload</i> [-c CONFFILE]&#8230; [-d DIR] [-u URL] [-b FILE] [-r FILE]</p>
<h2>DESCRIPTION</h2>
<p> The tool is used to create a compressed tarball of the problem directory and upload it to a URL. Supported protocols include FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP and FILE.</p>
<h3>Configuration file</h3>
<p> Configuration file contains entries in a format &quot;Option = Value&quot;. </p>
<p> The options are: </p>
<p> <i>URL</i></p>
<dl>
<dt>
<dd> The URL where tarball should be uploaded.</dl>
<p> <i>SSHPublicKey</i></p>
<dl>
<dt>
<dd> The SSH public key.</dl>
<p> <i>SSHPrivateKey</i></p>
<dl>
<dt>
<dd> The SSH private key.</dl>
<h3>Integration with ABRT events</h3>
<p> <i>reporter-upload</i> can be used as a reporter, to allow users to upload compressed tarballs of problem directories to a configured URL. This usage can be configured in /etc/libreport/report_event.conf: </p>
<dl>
<dt>
<dd>
<pre>
EVENT=report_Upload reporter-upload
</pre>
</dl>
<p> It can be also used on the <i>post-create</i> event to upload it automatically. </p>
<dl>
<dt>
<dd>
<pre>
EVENT=post-create reporter-upload
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -d DIR</p>
<dl>
<dt>
<dd> Path to problem directory.</dl>
<p> -c CONFFILE</p>
<dl>
<dt>
<dd> Path to configuration file. When used in ABRT event system, the file contains site-wide configuration. Users can change the values via environment variables.</dl>
<p> -u URL</p>
<dl>
<dt>
<dd> The URL where tarball should be uploaded. URL should have form protocol://[user[:pass]@]host/dir/[file.tar.gz] where protocol can be http(s), ftp, scp, or file. File protocol can&#8217;t have user and host parts: m[blue]<code>file.tar.gz</code>m[]<font SIZE="-2">[1]</font>. If URL ends with a slash, the archive name will be generated and appended to URL; otherwise, URL will be used as full file name.</dl>
<p> -b, &#8211;pubkey FILE</p>
<dl>
<dt>
<dd> Set SSH public key file.</dl>
<p> -r, &#8211;key FILE</p>
<dl>
<dt>
<dd> Set SSH private key file.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Environment variables take precedence over values provided in the configuration file. </p>
<p> <i>Upload_URL</i></p>
<dl>
<dt>
<dd> The URL where should be the tarball uploaded.</dl>
<p> <i>Upload_Username</i></p>
<dl>
<dt>
<dd> User name for the upload URL</dl>
<p> <i>Upload_Password</i></p>
<dl>
<dt>
<dd> Password for the upload URL</dl>
<p> <i>Upload_SSHPublicKey</i></p>
<dl>
<dt>
<dd> Path to SSH public key file</dl>
<p> <i>Upload_SSHPrivateKey</i></p>
<dl>
<dt>
<dd> Path to SSH private key file</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-uploader_event-conf/">uploader_event.conf</a>(5)</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; ABRT team</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> file.tar.gz</p>
<dl>
<dt>
<dd> file:///dir/</dl>
</dl>
<h2>Index</h2>
