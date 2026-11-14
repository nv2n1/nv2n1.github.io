---
title: "nstor_lsmplugin(1)"
name: "nstor_lsmplugin"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nstor_lsmplugin/"
description: "nstor_lsmplugin — LibstorageMgmt nstor plugin"
---

<h2>NAME</h2>
<p> nstor_lsmplugin &#8212; LibstorageMgmt nstor plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt nstor plugin allows user to manage NexentaStor 3.x storage software [1]. The &#8216;nstor_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client user specifies nstor plugin in the URI. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    # HTTP connection
    <code>nstor://&lt;username&gt;@&lt;nstor_server&gt;:&lt;port&gt;</code>
    # HTTPS connection
    <code>nstor+ssl://&lt;username&gt;@&lt;nstor_server&gt;:&lt;port&gt;</code>
</pre>
<dl>
<dt><code>username</code></p>
<dd>
<p> The <code>username</code> is the user account with &#8216;Can_use_restapi&#8217; permission. </p>
<dt><code>nstor_server</code></p>
<dd>
<p> The <code>nstor_server</code> is IP address or DNS name of NexentaStor server. </p>
<dt><code>port number</code></p>
<dd>
<p> The <code>port number</code> is the listening port of the nexenta server REST API. The default port of 2000 is used if none is supplied on the URI. </p>
<p> For non-default ports, SELinux will likely prevent the SMI-S plugin from making a network connection. </p>
<dt><code>URI parameters</code></p>
<dd> No additional URI parameters are supported by this plugin. </p>
</dl>
<h2>SUPPORTED SOFTWARE</h2>
<p> NexentaStor 3.x is supported. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> By default, this plugin requires the access to the nstor array&#8217;s TCP 2000 port. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1), [1] <a rel="nofollow" href="http://nexentastor.org">http://nexentastor.org</a> </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
