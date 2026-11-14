---
title: "megaraid_lsmplugin(1)"
name: "megaraid_lsmplugin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-megaraid_lsmplugin/"
description: "megaraid_lsmplugin — LibstorageMgmt MegaRAID plugin"
---

<h2>NAME</h2>
<p> megaraid_lsmplugin &#8212; LibstorageMgmt MegaRAID plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt megaraid plugin allows user to manage LSI MegaRAID via vendor tool <code>storcli</code>[1] or Dell PERC via <code>perccli</code>[2]. The &#8216;megaraid_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client user specifies megaraid plugin in the URI. </p>
<p> Extra SELinux actions are required to allowing plugin access the hardware. </p>
<p> When both storcli and percli is installed, the plugin will use storcli by default even that will result in no system found on Dell PERC server. In this case, please remove storcli. </p>
<p> Please be noted, current volume ID is just for temperate use, we will change to use volume VPD83 as volume ID once vendor provide so. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    <code>megaraid://</code>
        or
    <code>megaraid://?storcli=&lt;path_of_storcli&gt;</code>
</pre>
<dl>
<dt><code>URI parameters</code></p>
<dd> These URI parameters are supported by this plugin: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>storcli</code></p>
<dd>
<p> The &#8216;storcli&#8217; URI parameter is used to specified the path of storcli/perccli tool. By default, this plugin will try these paths: </p>
<p> storcli rpm: </p>
<p> <code>/opt/MegaRAID/storcli/storcli64</code>, <code>/opt/MegaRAID/storcli/storcli</code> </p>
<p> perccli rpm: </p>
<p> <code>/opt/MegaRAID/perccli/perccli64</code>, <code>/opt/MegaRAID/perccli/perccli</code> </p>
</dl>
</dl>
</dl>
<h2>ROOT PRIVILEGE</h2>
<p> This plugin requires both <code>lsmd</code> daemon and API client running as root user. Please check manpage <i>lsmd.conf (5)</i> for detail. </p>
<h2>SUPPORTED HARDWARES</h2>
<p> Please refer to LSI or Dell website for hardware support status of storcli/perccli. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> This plugin only execute <code>storcli</code> on localhost. No network connection required. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></i>(1), <i><a href="/docs/linux/man/1-lsmd/">lsmd</a></i>(1), [1] <a rel="nofollow" href="http://www.lsi.com,">http://www.lsi.com,</a> [2] <a rel="nofollow" href="http://www.dell.com">http://www.dell.com</a> </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.fedorahosted.org&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
