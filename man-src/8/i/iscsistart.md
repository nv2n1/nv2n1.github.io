---
title: "iscsistart(8)"
name: "iscsistart"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iscsistart/"
description: "iscsistart – iSCSI boot tool"
---

<p>iscsistart &#8211; iSCSI boot tool</p>
<h2>Synopsis</h2>
<p><code>iscsistart</code> [OPTION]</p>
<h2>Description</h2>
<p><code>iscsistart</code> will start a session using the settings passed in, or using the iBFT or Open Firmware [OF] boot information. This program should not be run to manage sessions. Its primary use is to start sessions used for iSCSI root boot.</p>
<h2>Options</h2>
<dl>
<dt><code>[-i|&#8211;initiatorname=]</code><i>name</i></p>
<dd>Set InitiatorName to name (Required if not using iBFT or OF)</p>
<dt><code>[-t|&#8211;targetname=]</code><i>name</i></p>
<dd>Set TargetName to name (Required if not using iBFT or OF)</p>
<dt><code>[-g|&#8211;tgpt=]</code><i>N</i></p>
<dd>Set target portal group tag to N (Required if not using iBFT or OF)</p>
<dt><code>[-a|&#8211;address=]</code><i>A.B.C.D</i></p>
<dd>Set IP address to A.B.C.D (Required if not using iBFT or OF)</p>
<dt><code>[-p|&#8211;port=]</code><i>N</i></p>
<dd>Set port to N (Optional. Default 3260)</p>
<dt><code>[-u|&#8211;username=]</code><i>N</i></p>
<dd>Set username to N (Optional)</p>
<dt><code>[-w|&#8211;password=]</code><i>N</i></p>
<dd>Set password to N (Optional)</p>
<dt><code>[-U|-username_in=]</code><i>N</i></p>
<dd>Set incoming username to N (Optional)</p>
<dt><code>[-W|&#8211;password_in=]</code><i>N</i></p>
<dd>Set incoming password to N (Optional)</p>
<dt><code>[-d|&#8211;debug=]</code><i>debug_level</i></p>
<dd>Print debugging information</p>
<dt><code>[-b|&#8211;fwparam_connect]</code></p>
<dd>Create a session to the target using the iBFT or OF info</p>
<dt><code>[-N|&#8211;fwparam_network]</code></p>
<dd>Bring up the network as specified by iBFT or OF</p>
<dt><code>[-f|&#8211;fwparam_print]</code></p>
<dd>Print the iBFT or OF info to STDOUT</p>
<dt><code>[-P|&#8211;param=]</code><i>NAME=VALUE</i></p>
<dd>Set the parameter with the name NAME to VALUE. NAME is one of the settings in the node record or iscsid.conf. Multiple params can be passed in.</p>
<dt><code>[-h|&#8211;help]</code></p>
<dd>Display this help and exit</p>
<dt><code>[-v|&#8211;version]</code></p>
<dd>Display version and exit </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iscsiadm/">iscsiadm</a></code>(8) </p>
<h2>Authors</h2>
<p>Open-iSCSI project &lt;<a rel="nofollow" href="http://www.open-iscsi.com/">http://www.open-iscsi.com/</a>&gt;<br />
 Mike Christie &lt;mchristi [at] redhat.com&gt;</p>
