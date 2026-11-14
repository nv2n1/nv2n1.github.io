---
title: "backup-manager-upload(8)"
name: "backup-manager-upload"
section: "8"
letter: "b"
url: "/docs/linux/man/8-backup-manager-upload/"
description: "backup-manager-upload – Multiprotocol uploader for backup-manager."
---

<p>backup-manager-upload &#8211; Multiprotocol uploader for backup-manager.</p>
<h2>Synopsis</h2>
<p>backup-manager-upload [options] date</p>
<h2>Description</h2>
<p><code>backup-manager-upload</code> will upload all the archives generated on the given date to the specified host with either ftp or scp. It&#8217;s also possible to use this program for uploading data to an Amazon S3 account. Some metadates are available like &#8220;today&#8221; or &#8220;yesterday&#8221;.</p>
<h2>Required Args</h2>
<dl>
<dt><code>&#8211;mode=</code><i>transfer-mode</i></p>
<dd>Select the transfer mode to use : ftp, scp, or s3.</p>
<dt><code>&#8211;host=</code><i>hostname1,hostname2,&#8230;,hostnameN</i></p>
<dd>Select a list of remote hosts to connect to.</p>
<dt><code>&#8211;user=</code><i>username</i></p>
<dd>Select the user to use for connection.</dl>
<h2>Optional Args</h2>
<dl>
<dt><code>&#8211;password=</code><i>password</i></p>
<dd>Select the ftp user&#8217;s password (only needed for ftp transfers).</p>
<dt><code>&#8211;key=</code><i>path_to_private_key</i></p>
<dd>Select the ssh private key file to use when opening the ssh session for scp transfer. Obviously, this is only needed for scp transfer mode. If you don&#8217;t specify a key file, the user&#8217;s default private key will be used.</p>
<dt><code>&#8211;directory=</code><i>directory</i></p>
<dd>Select the location on the remote host where files will be uploaded. Default is /backup/uploads.</p>
<dt><code>&#8211;bucket=</code><i>bucket</i></p>
<dd>Sets the bucket name for the Amazon S3 service backup into.</p>
<dt><code>&#8211;root=</code><i>directory</i></p>
<dd>Select the local directory where files are. Default is /var/archives</p>
<dt><code>&#8211;gpg-recipient=</code><i>gpg-recipient</i></p>
<dd>Select the gpg public key for encryptiong the archives when uploading with the method ssh-gpg. This can be a short or long key id or a descriptive name. The precise syntax is described in the gpg man page.</p>
<dt><code>&#8211;list</code></p>
<dd>Just list the files to upload.</p>
<dt><code>&#8211;ftp-purge</code></p>
<dd>Purge the remote directory before uploading files in <font SIZE="-1">FTP</font> mode.</p>
<dt><code>&#8211;s3-purge</code></p>
<dd>Purge the remote directory before uploading files in <font SIZE="-1">FTP</font> mode.</p>
<dt><code>&#8211;ssh-purge</code></p>
<dd>Purge the remote directory before uploading files in <font SIZE="-1">SSH</font> mode.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Flag to enable verbose mode.</p>
<dt><code>date</code></p>
<dd>Date pattern to select some files to upload, can be a valid date (<font SIZE="-1">YYYYMMDD</font>) or &#8216;today&#8217; or &#8216;yesterday&#8217;.</dl>
<h2>Error Codes</h2>
<p>If something goes wrong during an upload, backup-manager-upload will exit with a non null value. In such a case every error messages are sent to <font SIZE="-1">STDERR</font>. </p>
<p> Here are the possible error codes:</p>
<dl>
<dt>bad command line (wrong arguments) : 10</p>
<dd>
<dt><font SIZE="-1">FTP</font> transfer failure : 20</p>
<dd>
<dt><font SIZE="-1">SCP</font> transfer failure : 21</p>
<dd>
<dt>S3 transfer failure : 22</p>
<dd>
<dt>Unknown upload method: 23</p>
<dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-backup-manager/">backup-manager</a></i>(3)</p>
<h2>Authors</h2>
<p>Alexis Sukrieh &#8211; main code and design </p>
<p> Brad Dixon &#8211; Amazon S3 upload method </p>
<p> Jan Metzger &#8211; ssh-gpg upload method</p>
