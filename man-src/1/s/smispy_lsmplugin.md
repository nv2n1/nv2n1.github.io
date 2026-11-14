---
title: "smispy_lsmplugin(1)"
name: "smispy_lsmplugin"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smispy_lsmplugin/"
description: "smispy_lsmplugin — LibstorageMgmt SMI-S Plugin"
---

<h2>NAME</h2>
<p> smispy_lsmplugin &#8212; LibstorageMgmt SMI-S Plugin </p>
<h2>DESCRIPTION</h2>
<p> LibstorageMgmt SMI-S Plugin allows LibstorageMgmt user to manage storage arrays like: EMC VNX/VMAX, HDS AMS and LSI MegaRAID etc. via SNIA SMI-S standard. The &#8216;smispy_lsmplugin&#8217; executable file is for LibstorageMgmt daemon to execute when client user requests SMI-S plugin. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    # HTTP connection
    <code>smispy://&lt;username&gt;@&lt;smis_provder_host&gt;:&lt;port&gt;?&lt;uri_parameters&gt;</code>
    # HTTPS connection
    <code>smispy+ssl://&lt;username&gt;@&lt;smis_provder_host&gt;:&lt;port&gt;?&lt;uri_parameters&gt;</code>
</pre>
<dl>
<dt><code>username</code></p>
<dd>
<p> The <code>username</code> is the SMI-S provider user account. </p>
<dt><code>smis_provder_host</code></p>
<dd>
<p> The <code>smis_provder_host</code> is the SMI-S provider&#8217;s IP address or DNS name. </p>
<dt><code>port</code></p>
<dd>
<p> By default, SMI-S plugin will use port <code>5988</code> for HTTP connection and port <code>5989</code> for HTTPS connection. You can skip this in URI if your SMI-S provider is using default ports. </p>
<p> For non-default ports, SELinux will likely prevent the SMI-S plugin from making a network connection. </p>
<dt><code>URI parameters</code></p>
<dd> These URI parameters are supported by this plugin: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>namespace=&lt;name_space&gt;</code></p>
<dd> This URI parameter is for LSI MegaRAID and NetApp E-Series only. </p>
<dt><code>system=&lt;system_id&gt;</code></p>
<dd> For those SMI-S providers which support multi-systems(Example EMC ECIM), this URI parameter can be used to limit network communication for specified system only. The <code>system_id</code> is the ID of the system:<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm.System.id</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_system_id_get()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli list &#8211;systems</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line) </p>
<dt><code>no_ssl_verify=yes</code></p>
<dd> This URI parameter is for HTTPS connections only. With this URI parameter, the SMI-S plugin will not validate SMI-S provider&#8217;s server SSL certificate. It&#8217;s often used for self-signed CA environment, but it&#8217;s strongly suggested to remove this URI parameter and install self-signed CA properly. </p>
</dl>
</dl>
</dl>
<h2>Supported Hardware</h2>
<p> The LibstorageMgmt SMI-S plugin is based on &#8216;Block Services Package&#8217; profile , SNIA SMI-S 1.4 or later. Any storage system which implements that profile may be supported. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> By default, this plugin requires access to the SMI-S provider&#8217;s TCP 5988 port for HTTP conenction and TCP 5989 port for HTTPS connection. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1) </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
