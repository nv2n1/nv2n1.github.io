---
title: "gftp(1)"
name: "gftp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gftp/"
description: "gftp – file transfer client for *NIX based machines."
---

<h2>NAME</h2>
<p> gftp &#8211; file transfer client for *NIX based machines.</p>
<h2>SYNOPSIS</h2>
<p> <code>gftp [options] [[<a href="proto://][">proto://][</a></code> <i>user</i> <code>:</code> <i>[pass]</i> <code>@]</code> <i>server</i> <code>[:</code> <i>port</i> <code>][/</code> <i>directory</i> <code>]]</code></p>
<h2>DESCRIPTION</h2>
<p> gFTP is a file transfer client for *NIX based machines. It currently has a text interface and a GTK+ 1.2/2.x graphical interface. It currently supports the FTP, FTPS (control connection only), HTTP, HTTPS, SSH and FSP protocols.</p>
<h2>OPTIONS</h2>
<p> You may enter a url on the command line that gFTP will automatically connect to when it starts up.</p>
<dl>
<dt>&#8211;help, -h</p>
<dd> Display program usage.</p>
<dt>&#8211;info</p>
<dd> Display some information about how gFTP was built. Please send the output of this command when submitting a bug report.</p>
<dt>&#8211;version, -v</p>
<dd> Display the current version of gFTP.</p>
<dt>proto</p>
<dd> This specifies the protocol that should be used. It can currently be one of the following options: ftp, ftps, http, https, ssh, fsp, local and bookmark. If omitted, the protocol specified by the default_protocol option will be used.</p>
<dt>user</p>
<dd> The username that will be used to log into the remote server. If omitted, your current username will be used for most protocols. For the FTP protocol, the anonymous username will be used.</p>
<dt>pass</p>
<dd> The password that will be used to log into the remote server. If omitted, you will be prompted for the password. If you are using the FTP protocol, and the username is anonymous, then your email address will be used as the password.</p>
<dt>server</p>
<dd> The remote server to connect to.</p>
<dt>port</p>
<dd> The remote port on the server to connect to. If omitted, the default port for the protocol will be used. The port will be looked up in the <code><a href="/docs/linux/man/5-services/">services</a>(5)</code> file.</p>
<dt>directory</p>
<dd> The directory to change to once you are connected to the remote server.</dl>
<h2>FILES</h2>
<p> <i>~/.gftp/gftprc</i></p>
<dl>
<dt>
<dd> Per user configuration file. Most of these options can be edited inside gFTP. This file is also commented very well. <i>~/.gftp/bookmarks</i></p>
<dl>
<dt>
<dd> Per user bookmarks file.</dl>
</dl>
<h2>BUGS</h2>
<p> If you find any bugs in gFTP, please report them to GNOME&#8217;s Bugzilla at <a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a></p>
<h2>AUTHOR</h2>
<p> Brian Masney &lt;masneyb [at] gftp.org&gt; &#8211; <a rel="nofollow" href="http://www.gftp.org/">http://www.gftp.org/</a> </p>
<h2>Index</h2>
