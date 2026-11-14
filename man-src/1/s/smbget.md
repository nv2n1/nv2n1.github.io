---
title: "smbget(1)"
name: "smbget"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbget/"
description: "smbget – wget-like utility for download files over SMB"
---

<h2 class="name">NAME</h2>
<p> smbget &#8211; wget-like utility for download files over SMB </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbget [-a, &#8211;guest] [-r, &#8211;resume] [-R, &#8211;recursive] [-U, &#8211;user=STRING] [-w, &#8211;workgroup=STRING] [-n, &#8211;nonprompt] [-d, &#8211;debuglevel=INT] [-D, &#8211;dots] [-o, &#8211;outputfile] [-f, &#8211;rcfile] [-q, &#8211;quiet] [-v, &#8211;verbose] [-b, &#8211;blocksize] [-O, &#8211;stdout] [-u, &#8211;update] [-?, &#8211;help] [&#8211;usage] {<a href="smb://host/share/path/to/file}">smb://host/share/path/to/file}</a> [<a href="smb://url2/]">smb://url2/]</a> [&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbget is a simple utility with wget-like semantics, that can download files from SMB servers. You can specify the files you would like to download on the command-line. </p>
<p> The files should be in the smb-URL standard, e.g. use <a href="smb://host/share/file">smb://host/share/file</a> for the UNC path <i>\\HOST\SHARE\file</i>.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;guest</p>
<dl>
<dt>
<dd> Work as user guest</dl>
<p> -r, &#8211;resume</p>
<dl>
<dt>
<dd> Automatically resume aborted files</dl>
<p> -R, &#8211;recursive</p>
<dl>
<dt>
<dd> Recursively download files</dl>
<p> -U, &#8211;user=<i>username[%password]</i></p>
<dl>
<dt>
<dd> Username (and password) to use</dl>
<p> -w, &#8211;workgroup=STRING</p>
<dl>
<dt>
<dd> Workgroup to use (optional)</dl>
<p> -n, &#8211;nonprompt</p>
<dl>
<dt>
<dd> Don&#8217;t ask anything (non-interactive)</dl>
<p> -d, &#8211;debuglevel=INT</p>
<dl>
<dt>
<dd> Debuglevel to use</dl>
<p> -D, &#8211;dots</p>
<dl>
<dt>
<dd> Show dots as progress indication</dl>
<p> -o, &#8211;outputfile</p>
<dl>
<dt>
<dd> Write the file that is being downloaded to the specified file. Can not be used together with -R.</dl>
<p> -O, &#8211;stdout</p>
<dl>
<dt>
<dd> Write the file that is being downloaded to standard output.</dl>
<p> -f, &#8211;rcfile</p>
<dl>
<dt>
<dd> Use specified rcfile. This will be loaded in the order it was specified &#8211; e.g. if you specify any options before this one, they might get overridden by the contents of the rcfile.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Be quiet</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose</dl>
<p> -b, &#8211;blocksize</p>
<dl>
<dt>
<dd> Number of bytes to download in a block. Defaults to 64000.</dl>
<p> -?, &#8211;help</p>
<dl>
<dt>
<dd> Show help message</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message</dl>
<p> -u, &#8211;update</p>
<dl>
<dt>
<dd> Download only when remote file is newer than local file or local file is missing.</dl>
<p> -e|&#8211;encrypt</p>
<dl>
<dt>
<dd> This command line parameter requires the remote server support the UNIX extensions or that the SMB3 protocol has been selected. Requests that the connection be encrypted. Negotiates SMB encryption using either SMB3 or POSIX extensions via GSSAPI. Uses the given credentials for the encryption negotiation (either kerberos or NTLMv1/v2 if given domain/username/password triple. Fails the connection if encryption cannot be negotiated.</dl>
<h2>SMB URLS</h2>
<p> SMB URL&#8217;s should be specified in the following format: </p>
<dl>
<dt>
<dd>
<pre><code>
smb: //[[[domain;]user[:password@]]server[/share[/path[/file]]]]
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
smb:// means all the workgroups
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<a href="smb://name/">smb://name/</a> means, if <i>name</i> is a workgroup, all the servers in this workgroup, or if <i>name</i> is a server, all the shares on this server.
</pre>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
# Recursively download 'src' directory
smbget -R <a href="smb://rhonwyn/jelmer/src">smb://rhonwyn/jelmer/src</a>
# Download FreeBSD ISO and enable resuming
smbget -r <a href="smb://rhonwyn/isos/FreeBSD5.1.iso">smb://rhonwyn/isos/FreeBSD5.1.iso</a>
# Recursively download all ISOs
smbget -Rr <a href="smb://rhonwyn/isos">smb://rhonwyn/isos</a>
# Backup my data on rhonwyn
smbget -Rr <a href="smb://rhonwyn/">smb://rhonwyn/</a>
</pre>
</dl>
<h2>BUGS</h2>
<p> Permission denied is returned in some cases where the cause of the error is unknown (such as an illegally formatted smb:// url or trying to get a directory without -R turned on).</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The smbget manpage was written by Jelmer Vernooij. </p>
<h2>Index</h2>
