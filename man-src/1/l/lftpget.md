---

title: "lftpget(1)"
name: "lftpget"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lftpget/"
description: "lftpget – get a file with lftp(1)"
---

<p> lftpget &#8211; get a file with <a href="/docs/linux/man/1-lftp/">lftp</a>(1) </p>
<h2>SYNOPSIS</h2>
<p> <code>lftpget </code> [-c] [-d] [-v] <i>URL</i> [URL&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>lftpget</code> command. </p>
<p> <code>lftpget</code> is a shell script for downloading by URL, it calls `lftp -c&#8217;. It supports the same set of protocols as lftp does, including ftp, http, fish, sftp. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code></dt>
<dd> Continue a previous download.</dd>
<dt><code>-d</code></dt>
<dd> Debug output.</dd>
<dt><code>-v</code></dt>
<dd> Verbose messages. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lftp/">lftp</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> <code>lftpget</code> is Copyright (c) 1999-2000 Alexander V. Lukyanov &lt;lav [at] yars.free.net&gt;. </p>
<p> This manual page was initially written by Francois Wendling &lt;frwendling [at] free.fr&gt; and later updated by Alexander V. Lukyanov. </p>
