---
title: "hpsa_lsmplugin(1)"
name: "hpsa_lsmplugin"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hpsa_lsmplugin/"
description: "hpsa_lsmplugin — LibstorageMgmt HP SmartArray plugin"
---

<h2>NAME</h2>
<p> hpsa_lsmplugin &#8212; LibstorageMgmt HP SmartArray plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt hpsa plugin allows user to manage HP SmartArray via vendor tool <code>hpssacli</code>[1]. The &#8216;hpsa_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client user specifies hpsa plugin in the URI. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    <code>hpsa://</code>
        or
    <code><a href="hpsa://?hpssacli=">hpsa://?hpssacli=</a>&lt;path_of_hpssacli&gt;</code>
</pre>
<dl>
<dt><code>URI parameters</code></p>
<dd> These URI parameters are supported by this plugin: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>hpssacli</code></p>
<dd> The &#8216;hpssacli&#8217; URI parameter is used to specified the path of hpssacli tool. By default, this plugin will try these paths used by hpssacli rpm: <code>/usr/sbin/hpssacli</code> and <code>/opt/hp/hpssacli/bld/hpssacli</code>. </p>
</dl>
</dl>
</dl>
<h2>ROOT PRIVILEGE</h2>
<p> This plugin requires both <code>lsmd</code> daemon and API client running as root user. Please check manpage <i>lsmd.conf (5)</i> for detail. </p>
<h2>SUPPORTED HARDWARES</h2>
<p> Please refer to HP website for hardware support status of hpssacli. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> This plugin only execute <code>hpssacli</code> on localhost. No network connection required. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></i>(1), <i><a href="/docs/linux/man/1-lsmd/">lsmd</a></i>(1), [1]<a rel="nofollow" href="http://downloads.linux.hpe.com/SDR/project/spp/">http://downloads.linux.hpe.com/SDR/project/spp/</a> </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.fedorahosted.org&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
