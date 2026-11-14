---
title: "cifs-upcall(8)"
name: "cifs-upcall"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cifs-upcall/"
description: "cifs.upcall – Userspace upcall helper for Common Internet File System (CIFS)"
---

<p>cifs.upcall &#8211; Userspace upcall helper for Common Internet File System (CIFS)</p>
<h2>Synopsis</h2>
<pre><code>cifs.upcall [--trust-dns|-t] [--version|-v] [--legacy-uid|-l] [--krb5conf=/path/to/krb5.conf|-k /path/to/krb5.conf] [--keytab=/path/to/keytab|-K /path/to/keytab] {keyid}</code></pre>
<h2>Description</h2>
<p>This tool is part of the cifs-utils suite. </p>
<p> cifs.upcall is a userspace helper program for the linux CIFS client filesystem. There are a number of activities that the kernel cannot easily do itself. This program is a callout program that does these things for the kernel and then returns the result. </p>
<p> cifs.upcall is generally intended to be run when the kernel calls <a href="/docs/linux/man/8-request-key/">request-key</a>(8) for a particular key type. While it can be run directly from the command-line, it&#8217;s not generally intended to be run that way.</p>
<h2>Options</h2>
<p>-c</p>
<dl>
<dd>This option is deprecated and is currently ignored.</dl>
<p> &#8211;krb5conf=/path/to/krb5.conf|-k /path/to/krb5.conf</p>
<dl>
<dd>This option allows administrators to set an alternate location for the krb5.conf file that cifs.upcall will use.</dl>
<p> &#8211;keytab=/path/to/keytab|-K /path/to/keytab</p>
<dl>
<dd>This option allows administrators to specify a keytab file to be used. When a user has no credential cache already established, cifs.upcall will attempt to use this keytab to acquire them. The default is the system-wide keytab /etc/krb5.keytab.</dl>
<p> &#8211;trust-dns|-t</p>
<dl>
<dd>With krb5 upcalls, the name used as the host portion of the service principal defaults to the hostname portion of the UNC. This option allows the upcall program to reverse resolve the network address of the server in order to get the hostname. </p>
<p> This is less secure than not trusting DNS. When using this option, it&#8217;s possible that an attacker could get control of DNS and trick the client into mounting a different server altogether. It&#8217;s preferable to instead add server principals to the KDC for every possible hostname, but this option exists for cases where that isn&#8217;t possible. The default is to not trust reverse hostname lookups in this fashion.</dl>
<p> &#8211;legacy-uid|-l</p>
<dl>
<dd>Traditionally, the kernel has sent only a single uid= parameter to the upcall for the SPNEGO upcall that&#8217;s used to determine what user&#8217;s credential cache to use. This parameter is affected by the uid= mount option, which also governs the ownership of files on the mount. </p>
<p> Newer kernels send a creduid= option as well, which contains what uid it thinks actually owns the credentials that it&#8217;s looking for. At mount time, this is generally set to the real uid of the user doing the mount. For multisession mounts, it&#8217;s set to the fsuid of the mount user. Set this option if you want cifs.upcall to use the older uid= parameter instead of the creduid= parameter.</dl>
<p> &#8211;version|-v</p>
<dl>
<dd>Print version number and exit.</dl>
<h2>Configuration For Keyctl</h2>
<p>cifs.upcall is designed to be called from the kernel via the request-key callout program. This requires that request-key be told where and how to call this program. The current cifs.upcall program handles two different key types: </p>
<p> cifs.spnego</p>
<dl>
<dd>This keytype is for retrieving kerberos session keys</dl>
<p> dns_resolver</p>
<dl>
<dd>This key type is for resolving hostnames into IP addresses. Support for this key type may eventually be deprecated (see below).</dl>
<p> To make this program useful for CIFS, you&#8217;ll need to set up entries for them in <a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a>(5). Here&#8217;s an example of an entry for each key type: </p>
<dl>
<dd>
<pre>#OPERATION TYPE D C PROGRAM ARG1 ARG2...
#========= ============= = = ================================
create cifs.spnego * * /usr/sbin/cifs.upcall %k
create dns_resolver * * /usr/sbin/cifs.upcall %k</pre>
</dl>
<p> See <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) for more info on each field. </p>
<p> The keyutils package has also started including a dns_resolver handling program as well that is preferred over the one in cifs.upcall. If you are using a keyutils version equal to or greater than 1.5, you should use key.dns_resolver to handle the dns_resolver keytype instead of cifs.upcall. See <code><a href="/docs/linux/man/8-key-dns_resolver/">key.dns_resolver</a></code>(8) for more info.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5), <code><a href="/docs/linux/man/8-mount-cifs/">mount.cifs</a></code>(8), <code><a href="/docs/linux/man/8-key-dns_resolver/">key.dns_resolver</a></code>(8)</p>
<h2>Author</h2>
<p>Igor Mammedov wrote the cifs.upcall program. </p>
<p> Jeff Layton authored this manpage. </p>
<p> The maintainer of the Linux CIFS VFS is Steve French. </p>
<p> The Linux CIFS Mailing list is the preferred place to ask questions regarding these programs.</p>
