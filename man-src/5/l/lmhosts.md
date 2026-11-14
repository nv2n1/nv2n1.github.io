---
title: "lmhosts(5)"
name: "lmhosts"
section: "5"
letter: "l"
url: "/docs/linux/man/5-lmhosts/"
description: "lmhosts – The Samba NetBIOS hosts file"
---

<p>lmhosts &#8211; The Samba NetBIOS hosts file</p>
<h2>Synopsis</h2>
<p>lmhosts is the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) NetBIOS name to IP address mapping file.</p>
<h2>Description</h2>
<p>This file is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> lmhosts is the <i>Samba </i> NetBIOS name to IP address mapping file. It is very similar to the /etc/hosts file format, except that the hostname component must correspond to the NetBIOS naming format.</p>
<h2>File Format</h2>
<p>It is an ASCII file containing one line for NetBIOS name. The two fields on each line are separated from each other by white space. Any entry beginning with &#8216;#&#8217; is ignored. Each line in the lmhosts file contains the following information:</p>
<dl>
<dd>
<dl>
<dd>&bull; IP Address &#8211; in dotted decimal format.</dl>
<dl>
<dd>&bull; NetBIOS Name &#8211; This name format is a maximum fifteen character host name, with an optional trailing &#8216;#&#8217; character followed by the NetBIOS name type as two hexadecimal digits. </p>
<p> If the trailing &#8216;#&#8217; is omitted then the given IP address will be returned for all names that match the given name, whatever the NetBIOS name type in the lookup.</dl>
</dl>
<p> An example follows: </p>
<dl>
<dd>
<pre>#
# Sample Samba lmhosts file.
#
192.9.200.1 TESTPC
192.9.200.20 NTSERVER#20
192.9.200.21 SAMBASERVER</pre>
</dl>
<p> Contains three IP to NetBIOS name mappings. The first and third will be returned for any queries for the names &quot;TESTPC&quot; and &quot;SAMBASERVER&quot; respectively, whatever the type component of the NetBIOS name requested. </p>
<p> The second mapping will be returned only when the &quot;0x20&quot; name type for a name &quot;NTSERVER&quot; is queried. Any other name type will not be resolved. </p>
<p> The default location of the lmhosts file is in the same directory as the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file.</p>
<h2>Files</h2>
<p>lmhosts is loaded from the configuration directory. This is usually /etc/samba or /usr/local/samba/lib.</p>
<h2>Version</h2>
<p>This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), and <code><a href="/docs/linux/man/8-smbpasswd/">smbpasswd</a></code>(8)</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
