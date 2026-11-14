---
title: "iscsid(8)"
name: "iscsid"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iscsid/"
description: "iscsid – Open-iSCSI daemon"
---

<p>iscsid &#8211; Open-iSCSI daemon</p>
<h2>Synopsis</h2>
<p><code>iscsid</code> [OPTION]</p>
<h2>Description</h2>
<p>The <code>iscsid</code> implements the control path of iSCSI protocol, plus some management facilities. For example, the daemon could be configured to automatically re-start discovery at startup, based on the contents of persistent iSCSI database.</p>
<h2>Options</h2>
<dl>
<dt><code>[-c|&#8211;config=]</code><i>config-file</i></p>
<dd>Read configuration from <i>config-file</i> rather than the default <i>/etc/iscsi/iscsid.conf</i> file.</p>
<dt><code>[-i|&#8211;initiatorname=]</code><i>iname-file</i></p>
<dd>Read initiator name from <i>iname-file</i> rather than the default <i>/etc/iscsi/initiatorname.iscsi</i> file.</p>
<dt><code>[-f|&#8211;foreground]</code></p>
<dd>run <code>iscsid</code> in the foreground.</p>
<dt><code>[-d|&#8211;debug=]</code><i>debug_level</i></p>
<dd>print debugging information. Valid values for debug_level are 0 to 8.</p>
<dt><code>[-u|&#8211;uid=]</code><i>uid</i></p>
<dd>run under user ID <i>uid</i> (default is the current user ID)</p>
<dt><code>[-g|&#8211;gid=]</code><i>gid</i></p>
<dd>run under user group ID <i>gid</i> (default is the current user group ID).</p>
<dt><code>[-n|&#8211;no-pid-file]</code></p>
<dd>do not write a process ID file.</p>
<dt><code>[-p|&#8211;pid=]</code><i>pid-file</i></p>
<dd>write process ID to <i>pid-file</i> rather than the default <i>/var/run/iscsid.pid</i></p>
<dt><code>[-h|&#8211;help]</code></p>
<dd>display this help and exit</p>
<dt><code>[-v|&#8211;version]</code></p>
<dd>display version and exit. </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/iscsi/iscsid.conf</p>
<dd>The configuration file read by <code>iscsid</code> and <code>iscsiadm</code> on startup.</p>
<dt>/etc/iscsi/initiatorname.iscsi</p>
<dd>The file containing the iSCSI initiatorname and initiatoralias read by <code>iscsid</code> and <code>iscsiadm</code> on startup.</p>
<dt>/etc/iscsi/nodes</p>
<dd>Open-iSCSI persistent configuration database </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iscsiadm/">iscsiadm</a></code>(8) </p>
<h2>Authors</h2>
<p>Open-iSCSI project &lt;<a rel="nofollow" href="http://www.open-iscsi.com/">http://www.open-iscsi.com/</a>&gt;<br />
 Alex Aizman &lt;itn780 [at] yahoo.com&gt;<br />
 Dmitry Yusupov &lt;dmitry_yus [at] yahoo.com&gt;</p>
