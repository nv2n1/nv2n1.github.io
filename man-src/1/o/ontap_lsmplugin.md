---
title: "ontap_lsmplugin(1)"
name: "ontap_lsmplugin"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ontap_lsmplugin/"
description: "ontap_lsmplugin — LibstorageMgmt ONTAP Plugin"
---

<h2>NAME</h2>
<p> ontap_lsmplugin &#8212; LibstorageMgmt ONTAP Plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt ontap plugin allows user to manage NetApp ONTAP storage arrays. The &#8216;ontap_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client specifies ontap plugin in the URI </p>
<p> This plugin requires NetApp ONTAP storage array to enable these options: </p>
<p>&nbsp;<wbr><code>options httpd.enable on</code><br />
&nbsp;<wbr><code>options httpd.admin.enable on</code> </p>
<p> This options is required for HTTPS connection: </p>
<p>&nbsp;<wbr><code>options httpd.admin.ssl.enable on</code> </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    # HTTP connection
    <code>ontap://&lt;username&gt;@&lt;ontap_filer&gt;</code>
    # HTTPS connection
    <code>ontap+ssl://&lt;username&gt;@&lt;ontap_filer&gt;</code>
</pre>
<dl>
<dt><code>username</code></p>
<dd>
<p> The <code>username</code> is the user account with administration privilege. </p>
<dt><code>ontap_filer_ip</code></p>
<dd>
<p> The <code>ontap_filer_ip</code> is the NetApp ONTAP filer IP address or DNS name. </p>
<dt><code>URI parameters</code></p>
<dd>
<p> No additional URI parameters are supported by this plugin. </p>
</dl>
<h2>Supported Hardware</h2>
<p> NetApp ONTAP 8.x is supported. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> This plugin requires the access to the NetApp ONTAP Filer&#8217;s TCP 80 port for HTTP connection and TCP 443 port for HTTPS connection. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1) </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
