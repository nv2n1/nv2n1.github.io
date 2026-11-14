---
title: "mount_afp(1)"
name: "mount_afp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mount_afp/"
description: "mount_afp – mount an afp (AppleShare) filesystem using FUSE"
---

<h2 class="name">NAME</h2>
<p> <code>mount_afp</code> &#8211; mount an afp (AppleShare) filesystem using FUSE </p>
<h2>SYNOPSIS</h2>
<p> [-<code>o </code><i>options</i> ] <i>afp_url</i> <i>node</i></p>
<h2>DESCRIPTION</h2>
<p> The command mounts the AFP volume denoted by the afp_url <i><a href="afp://[user[;AUTH=uamname][:password]@]host[:port]/volumename">afp://[user[;AUTH=uamname][:password]@]host[:port]/volumename</a></i> at the mount point indicated by <i>node.</i> </p>
<p> This is normally a symlink to the afp_client1 executable, which is a full implementation to mount AFP volumes using the FUSE infrastructure. It communicates with afpfsd, a daemon that manages AFP sessions. Fp The arguments and options are:</p>
<dl>
<dt><code>-o</code></p>
<dd> Options passed to <a href="/docs/linux/man/2-mount/">mount</a>(2) are specified with the &#8211;<code>o</code> option followed by a comma separated string of options. man page for possible options and their meanings. Additional options supported by the AFP Client are as follows:</p>
<dl>
<dt><code>volpass=&lt;password&gt;</code></p>
<dd> The only available option is &quot;-o volpassword=XXX&quot; to set the volume password (since there is no facility for that in an AFP URL).</dl>
<dl>
<dt><code>rw</code></p>
<dd> Mount the volume as writeable. This is the default, so it has no effect.</dl>
<dl>
<dt><code>ro</code></p>
<dd> Mount the volume as readonly.</dl>
<dl>
<dt><code>group=&lt;groupname&gt;</code></p>
<dd> Mount the volume as groupname.</dl>
<dl>
<dt><code>user=&lt;username&gt;</code></p>
<dd> Mount the volume as username.</dl>
<dt><i>afp_url</i></p>
<dd> There are two forms of afp URL, one for TCP/IP and one for AppleTalk: </p>
<p> <a href="afp://[user[;AUTH=uamname][:password]@]host[:port]/volume">afp://[user[;AUTH=uamname][:password]@]host[:port]/volume</a> </p>
<p> afp:/at/[user[;AUTH=uamname][:password]@]servername[:zonename]/volume </p>
<p> Denotes the afp server and sharepoint to mount. It may also contain the username &amp; password required to log into the server. uamname is the protocol name of the authentication method. If port is not specified, then port 548 is used.</p>
<dt><i>node</i></p>
<dd> Path to mount point, which must be a directory that the user has write permissions for.</dl>
<h2>EXAMPLES</h2>
<p> The following example illustrates how to mount the afp volume server.company.com/volumename/ at the mount point /Volumes/mntpnt: </p>
<blockquote>
<pre>
mkdir /Volumes/mntpnt
mount_afp <a href="afp://username:userpass@server.company.com/volumename/">afp://username:userpass@server.company.com/volumename/</a> /Volumes/mntpnt
</pre>
</blockquote>
<p> This example shows the proper url to use to mount the volume guestVolume from the afp server myserver as guest: </p>
<blockquote>
<pre>
mkdir /Volumes/guest
mount_afp &quot;<a href="afp://;AUTH=No%20User%20Authent@myserver/guestVolume">afp://;AUTH=No%20User%20Authent@myserver/guestVolume</a>&quot; /Volumes/guest
The following shows how to use a username of &quot;user:name&quot; and password of &quot;p@ssword&quot;:
server.company.com/volumename/ at the mount point /Volumes/mntpnt:
<blockquote>
mkdir /Volumes/mntpnt
mount_afp <a href="afp://user::name:p@@ssword@server.company.com/volumename/">afp://user::name:p@@ssword@server.company.com/volumename/</a> /Volumes/mntpnt
</blockquote>
</blockquote>
This example shows the proper url to use to mount the volume myVolume from
the afp server myserver using Kerberos authentication:
<blockquote>
<pre>
mkdir /Volumes/myVolume
mount_afp &quot;<a href="afp://;AUTH=Client%20Krb%20v2@myserver/myVolume">afp://;AUTH=Client%20Krb%20v2@myserver/myVolume</a>&quot; /Volumes/myVolume
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> afp_client1(foramoreAFPcommands), <a href="/docs/linux/man/1-afpcmd/">afpcmd</a>(1)(foranon-FUSEcommandlineAFPclient),</p>
<h2>HISTORY</h2>
<p> The command first appeared Mac OS X version 10.0. Kerberos authentication was added in Mac OS X version 10.2. This syntax (and manpage) was used for afpfs-ng's fuse implementation.</p>
<h2>RETURN VALUES</h2>
<dl>
<dt><code>0</code></p>
<dd> successfully mounted the volume directory.</p>
<dt><code>-1</code></p>
<dd> The server volume could not be mounted.</dl>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-afp_client/">afp_client</a>(1), <a href="/docs/linux/man/1-afpfsd/">afpfsd</a>(1)</code> </p>
<h2>Index</h2>
