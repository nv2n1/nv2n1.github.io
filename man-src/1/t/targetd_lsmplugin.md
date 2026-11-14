---
title: "targetd_lsmplugin(1)"
name: "targetd_lsmplugin"
section: "1"
letter: "t"
url: "/docs/linux/man/1-targetd_lsmplugin/"
description: "targetd_lsmplugin — libStorageMgmt targetd plugin"
---

<h2>NAME</h2>
<p> targetd_lsmplugin &#8212; libStorageMgmt targetd plugin </p>
<h2>DESCRIPTION</h2>
<p> LibStorageMgmt targetd plugin allows user to manage storage using the targetd storage API [1]. The &#8216;targetd_lsmplugin&#8217; executable file is for libStorageMgmt daemon to execute when client user specifies targetd plugin in the URI. </p>
<h2>URI</h2>
<p> To use this plugin, users should set their URI to this format: </p>
<pre>
    # HTTP connection
    <code>targetd://&lt;username&gt;@&lt;targetd_server&gt;:&lt;port number&gt;</code>
    # HTTPS connection
    <code>targetd+ssl://&lt;username&gt;@&lt;targetd_server&gt;:&lt;port number&gt;</code>
</pre>
<dl>
<dt><code>username</code></p>
<dd>
<p> The <code>username</code> is the user account configured in targetd configuration file. </p>
<dt><code>targetd_server</code></p>
<dd>
<p> The <code>targetd_server</code> is the IP address or DNS name of server running targetd daemon. </p>
<dt><code>port number</code></p>
<dd>
<p> The <code>port number</code> is the listening port of the targetd daemon. The default port of 18700 is used if none is supplied on the URI. </p>
<dt><code>URI parameters</code></p>
<dd> No additional URI parameters are supported by this plugin. </p>
</dl>
<h2>SUPPORTED SOFTWARE</h2>
<p> Linux targetd 0.7.1 or later version. Detailed support status can be queried via: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr><code>lsm.Client.capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>(Python API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsm_capabilities()</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(C API)<br />
&nbsp;<wbr>*&nbsp;<wbr><code>lsmcli capabilities</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(lsmcli command line). </p>
<h2>FIREWALL RULES</h2>
<p> By default, this plugin requires access to the targetd server&#8217;s TCP 18700 port. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsmcli/">lsmcli</a></code>(1), <code><a href="/docs/linux/man/1-lsmd/">lsmd</a></code>(1), [1] <a rel="nofollow" href="https://github.com/agrover/targetd">https://github.com/agrover/targetd</a> </p>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.sourceforge.net&gt;</i> </p>
<h2>AUTHOR</h2>
<p> Gris Ge <i>&lt;fge [at] redhat.com&gt;</i><br />
 Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
