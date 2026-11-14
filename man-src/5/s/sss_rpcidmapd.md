---
title: "sss_rpcidmapd(5)"
name: "sss_rpcidmapd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sss_rpcidmapd/"
description: "sss_rpcidmapd – sss plugin configuration directives for rpc.idmapd"
---

<p>sss_rpcidmapd &#8211; sss plugin configuration directives for rpc.idmapd</p>
<h2>Configuration File</h2>
<p>rpc.idmapd configuration file is usually found at <i>/etc/idmapd.conf</i>. See <code><a href="/docs/linux/man/5-idmapd-conf/">idmapd.conf</a></code>(5) for more information.</p>
<h2>Sss Configuration Extension</h2>
<h3>Enable SSS plugin</h3>
<p>In section &#8220;[Translation]&#8221;, modify/set &#8220;Method&#8221; attribute to contain <i>sss</i>.</p>
<h3>[sss] config section</h3>
<p>In order to change the default of one of the configuration attributes of the <i>sss</i> plugin listed below you will need to create a config section for it, named &#8220;[sss]&#8221;. </p>
<p> <code>Configuration attributes</code> </p>
<p> memcache (bool)</p>
<dl>
<dd>Indicates whether or not to use memcache optimisation technique. </p>
<p> Default: True</dl>
<h2>Sssd Integration</h2>
<p>The sss plugin requires the <i>NSS Responder</i> to be enabled in sssd. </p>
<p> The attribute &#8220;use_fully_qualified_names&#8221; must be enabled on all domains (NFSv4 clients expect a fully qualified name to be sent on the wire).</p>
<h2>Example</h2>
<p>The following example shows a minimal idmapd.conf which makes use of the sss plugin.</p>
<dl>
<dd>
<pre>[General]
Verbosity = 2
# domain must be synced between NFSv4 server and clients
# Solaris/Illumos/AIX use &quot;localdomain&quot; as default!
Domain = default
[Mapping]
Nobody-User = nfsnobody
Nobody-Group = nfsnobody
[Translation]
Method = sss</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-idmapd-conf/">idmapd.conf</a></code>(5)</p>
<h2>Authors</h2>
<p><code>Noam Meltzer</code><br />
 Primary Data Inc.</p>
<dl>
<dd>Developer (2013-2014)</dl>
<p> <code>Noam Meltzer</code> &lt;tsnoam [at] gmail.com&gt;</p>
<dl>
<dd>Developer (2014-)</dl>
