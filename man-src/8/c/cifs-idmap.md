---
title: "cifs-idmap(8)"
name: "cifs-idmap"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cifs-idmap/"
description: "cifs.idmap – Userspace helper for mapping ids for Common Internet File System (CIFS)"
---

<p>cifs.idmap &#8211; Userspace helper for mapping ids for Common Internet File System (CIFS)</p>
<h2>Synopsis</h2>
<dl>
<dd>cifs.idmap [&#8211;help|-h] [&#8211;timeout|-t] [&#8211;version|-v] {keyid}</dl>
<h2>Description</h2>
<p>This tool is part of the cifs-utils suite. </p>
<p> cifs.idmap is a userspace helper program for the linux CIFS client filesystem. There are a number of activities that the kernel cannot easily do itself. This program is a callout program that does these things for the kernel and then returns the result. </p>
<p> cifs.idmap is generally intended to be run when the kernel calls <a href="/docs/linux/man/8-request-key/">request-key</a>(8) for a particular key type. While it can be run directly from the command-line, it is not generally intended to be run that way. </p>
<p> This program is only called if a share is mounted with the <code>cifsacl</code> mount option. The kernel will only upcall to do this conversion if that mount option is specified. </p>
<p> cifs.idmap relies on a plugin to handle the ID mapping. If it can&#8217;t find the plugin then it will not work properly. The plugin (or a symlink to it) must be at <code>/etc/cifs-utils/idmap-plugin</code>. </p>
<p> In the case where cifs.idmap or the plugin are unavailable, file objects in a mounted share are assigned uid and gid of the credentials of the process that mounted the share. It is strongly recomemended to use mount options of uid and gid to specify a default uid and gid to map owner SIDs and group SIDs in this situation.</p>
<h2>Options</h2>
<p>&#8211;help|-h</p>
<dl>
<dd>Print the usage message and exit.</dl>
<p> &#8211;timeout|-t</p>
<dl>
<dd>Set the expiration timer, in seconds on the key. The default is 600 seconds (10 minutes). Setting this to 0 will cause the key to never expire.</dl>
<p> &#8211;version|-v</p>
<dl>
<dd>Print version number and exit.</dl>
<h2>Configuration For Keyctl</h2>
<p>cifs.idmap is designed to be called from the kernel via the request-key callout program. This requires that request-key be told where and how to call this program. Currently cifs.idmap handles a key type of: </p>
<p> cifs.idmap</p>
<dl>
<dd>This keytype is for mapping a SID to either an uid or a gid</dl>
<p> To make this program useful for CIFS, you will need to set up entry for it in <a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a>(5). Here is an example of an entry for this key type: </p>
<dl>
<dd>
<pre>#OPERATION TYPE D C PROGRAM ARG1 ARG2...
#========= ============= = = ================================
create cifs.idmap * * /usr/sbin/cifs.idmap %k</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) for more info on each field.</p>
<h2>Notes</h2>
<p>Support for upcalls to cifs.idmap was initially introduced in the 3.0 kernel.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount-cifs/">mount.cifs</a></code>(8)</p>
<h2>Author</h2>
<p>Shirish Pargaonkar wrote the cifs.idmap program. </p>
<p> The Linux CIFS Mailing list is the preferred place to ask questions regarding these programs.</p>
