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
<dt><code>[-i|&#8211;initiatorname=]</code><i>name</i></dt>
<dd>Set InitiatorName to name (Required if not using iBFT or OF)</dd>
<dt><code>[-t|&#8211;targetname=]</code><i>name</i></dt>
<dd>Set TargetName to name (Required if not using iBFT or OF)</dd>
<dt><code>[-g|&#8211;tgpt=]</code><i>N</i></dt>
<dd>Set target portal group tag to N (Required if not using iBFT or OF)</dd>
<dt><code>[-a|&#8211;address=]</code><i>A.B.C.D</i></dt>
<dd>Set IP address to A.B.C.D (Required if not using iBFT or OF)</dd>
<dt><code>[-p|&#8211;port=]</code><i>N</i></dt>
<dd>Set port to N (Optional. Default 3260)</dd>
<dt><code>[-u|&#8211;username=]</code><i>N</i></dt>
<dd>Set username to N (Optional)</dd>
<dt><code>[-w|&#8211;password=]</code><i>N</i></dt>
<dd>Set password to N (Optional)</dd>
<dt><code>[-U|-username_in=]</code><i>N</i></dt>
<dd>Set incoming username to N (Optional)</dd>
<dt><code>[-W|&#8211;password_in=]</code><i>N</i></dt>
<dd>Set incoming password to N (Optional)</dd>
<dt><code>[-d|&#8211;debug=]</code><i>debug_level</i></dt>
<dd>Print debugging information</dd>
<dt><code>[-b|&#8211;fwparam_connect]</code></dt>
<dd>Create a session to the target using the iBFT or OF info</dd>
<dt><code>[-N|&#8211;fwparam_network]</code></dt>
<dd>Bring up the network as specified by iBFT or OF</dd>
<dt><code>[-f|&#8211;fwparam_print]</code></dt>
<dd>Print the iBFT or OF info to STDOUT</dd>
<dt><code>[-P|&#8211;param=]</code><i>NAME=VALUE</i></dt>
<dd>Set the parameter with the name NAME to VALUE. NAME is one of the settings in the node record or iscsid.conf. Multiple params can be passed in.</dd>
<dt><code>[-h|&#8211;help]</code></dt>
<dd>Display this help and exit</dd>
<dt><code>[-v|&#8211;version]</code></dt>
<dd>Display version and exit </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iscsiadm/">iscsiadm</a></code>(8) </p>
<h2>Authors</h2>
<p>Open-iSCSI project &lt;<a rel="nofollow" href="http://www.open-iscsi.com/">http://www.open-iscsi.com/</a>&gt;<br />
 Mike Christie &lt;mchristi [at] redhat.com&gt;</p>
