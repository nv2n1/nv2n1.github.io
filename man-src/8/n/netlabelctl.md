---
title: "netlabelctl(8)"
name: "netlabelctl"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netlabelctl/"
description: "netlabelctl – NetLabel management utility"
---

<p>netlabelctl &#8211; NetLabel management utility</p>
<h2>Synopsis</h2>
<p><code>netlabelctl</code> [&lt;global_flags&gt;] &lt;module&gt; [&lt;module_commands&gt;]</p>
<h2>Description</h2>
<p>The NetLabel management utility, netlabelctl, is a command line program designed to allow system administrators to configure the NetLabel system in the kernel. The utility is based around different &quot;modules&quot; which correspond to the different types of NetLabel commands supported by the kernel.</p>
<h2>Options</h2>
<h3>Global Flags</h3>
<dl>
<dt><code>-h</code></p>
<dd>Help message</p>
<dt><code>-p</code></p>
<dd>Attempt to make the output human readable or &quot;pretty&quot;</p>
<dt><code>-t &lt;seconds&gt;</code></p>
<dd>Set a timeout to be used when waiting for the NetLabel subsystem to respond</p>
<dt><code>-v</code></p>
<dd>Enable extra output</p>
<dt><code>-V</code></p>
<dd>Display the version information</dl>
<h3>Modules and Commands</h3>
<dl>
<dt><code>mgmt</code></p>
<dd></dl>
<p> The management module is used to perform general queries about the NetLabel subsystem within the kernel. The different commands and their syntax are listed below.</p>
<dl>
<dt> <i>version</i></p>
<dd>
<dd>Display the kernel&#8217;s NetLabel management protocol version.</p>
<dt> <i>protocols</i></p>
<dd>
<dd>Display the kernel&#8217;s list of supported labeling protocols.</p>
<dt><code>map</code></p>
<dd></dl>
<p> The domain mapping module is used to map different NetLabel labeling protocols to either individual LSM domains or the default domain mapping. It is up to each LSM to determine what defines a domain. With SELinux, the normal SELinux domain should be used, i.e. &quot;ping_t&quot;. In addition to protocol selection based only on the LSM domain, it is also possible to select the labeling protocol based on both the LSM domain and destination address. The network address selectors can specify either single hosts or entire networks and work for both IPv4 and IPv6, although the labeling protocol chosen must support the IP version chosen. When specifying the labeling protocol to use for each mapping there is an optional &quot;extra&quot; field which is used to further identify the specific labeling protocol configuration. When specifying the unlabeled protocol, &quot;unlbl&quot;, there is no extra identification needed. When specifying the CIPSO/IPv4 protocol, &quot;cipsov4&quot;, the DOI value should be specified; see the EXAMPLES section for details. The different commands and their syntax are listed below.</p>
<dl>
<dt> <i>add default|domain:&lt;domain&gt; [address:&lt;ADDR&gt;[/&lt;MASK&gt;]] protocol:&lt;protocol&gt;[,&lt;extra&gt;]</i></p>
<dd>
<dd>Add a new LSM domain / network address to NetLabel protocol mapping.</p>
<dt> <i>del default|domain:&lt;domain&gt;</i></p>
<dd>
<dd>Delete an existing LSM domain to NetLabel protocol mapping.</p>
<dt> <i>list</i></p>
<dd>
<dd>Display all of the configured LSM domain to NetLabel protocol mappings.</p>
<dt><code>unlbl</code></p>
<dd></dl>
<p> The unlabeled (unlbl) module controls the unlabeled protocol which is used both when labeling outgoing traffic is not desired as well as when unlabeled traffic is received by the system. This module allows administrators to block all unlabeled packets from the system through the &quot;accept&quot; flag and assign static, or fallback, security labels to unlabeled traffic based on the inbound network interface and source address.</p>
<dl>
<dt> <i>accept on|off</i></p>
<dd>
<dd>Toggle the unlabeled traffic accept flag.</p>
<dt> <i>add default|interface:&lt;dev&gt; address:&lt;addr&gt;[/&lt;mask&gt;] label:&lt;label&gt;</i></p>
<dd>
<dd>Add a new static/fallback entry.</p>
<dt> <i>del default|interface:&lt;dev&gt; address:&lt;addr&gt;[/&lt;mask&gt;]</i></p>
<dd>
<dd>Delete an existing static/fallback entry.</p>
<dt> <i>list</i></p>
<dd>
<dd>Display the status of the unlabeled accept flag.</p>
<dt><code>cipsov4</code></p>
<dd></dl>
<p> The CIPSO/IPv4 (cipsov4) module controls the CIPSO/IPv4 labeling engine in the kernel. The CIPSO/IPv4 engine provided by NetLabel supports multiple Domains Of Interpretation (DOI) and the CIPSO/IPv4 module allows for different configurations for each DOI. At present there are three types of configurations, the &quot;trans&quot; configuration which allows on-the-fly translation of MLS sensitivity labels, the &quot;pass&quot; configuration which does not perform any translation of the MLS sensitivity label and the &quot;local&quot; configuration which conveys the full LSM security label over localhost/loopback connections. Regardless of which configuration type is chosen a DOI value must be specified and if the &quot;trans&quot; or &quot;pass&quot; configurations are specified then a list of the CIPSO/IPv4 tag types to use when generating the CIPSO/IPv4 packet labels must also be specified. The list of CIPSO/IPv4 tags is ordered such that when possible the first tag type listed is used when a CIPSO/IPv4 label is generated. However, if it is not possible to use the first tag type then each tag type is checked, in order, until a suitable tag type is found. If a valid tag type can not be found then the operation causing the CIPSO/IPv4 label will fail, typically this occurs whenever a new socket is created. The different commands and their syntax are listed below.</p>
<dl>
<dt> <i>add trans doi:&lt;DOI&gt; tags:&lt;T1&gt;,&lt;Tn&gt; levels:&lt;LL1&gt;=&lt;RL1&gt;,&lt;LLn&gt;=&lt;RLn&gt; categories:&lt;LC1&gt;=&lt;RC1&gt;,&lt;LCn&gt;=&lt;RCn&gt;</i></p>
<dd>
<dd>Add a new CIPSO/IPv4 configuration using the standard/translated mapping with the given level and category translations. The levels are translated in such a way that the local level &quot;LLn&quot; is translated to the remote, on-the-wire level of &quot;RLn&quot;; the reverse translation is done for incoming packets. The same translation is done for the categories using &quot;LCn&quot; and &quot;RCn&quot;. In order for a packet to be accepted, or a socket created by an application, there must be a translation for the sensitivity level and all the categories present in the MLS sensitivity label; if the entire requested sensitivity label can not be translated the application will fail.</p>
<dt> <i>add pass doi:&lt;DOI&gt; tags:&lt;T1&gt;,&lt;Tn&gt;</i></p>
<dd>
<dd>Add a new CIPSO/IPv4 configuration without any level or category translations.</p>
<dt> <i>add local doi:&lt;DOI&gt;</i></p>
<dd>
<dd>Add a new CIPSO/IPv4 configuration for localhost/loopback connections.</p>
<dt> <i>del doi:&lt;DOI&gt;</i></p>
<dd>
<dd>Delete an existing CIPSO/IPv4 configuration with the given DOI value. If any LSM domain mappings are present which make use of this DOI they will also be deleted.</p>
<dt> <i>list [doi:&lt;DOI&gt;]</i></p>
<dd>
<dd>Display a list of all the CIPSO/IPv4 configurations or just the configuration matching the optionally specified DOI.</dl>
<h2>Exit Status</h2>
<p>Returns zero on success, errno values on failure.</p>
<h2>Examples</h2>
<dl>
<dt><i>netlabelctl cipsov4 add pass doi:16 tags:1</i></p>
<dd>Add a CIPSO/IPv4 configuration with a DOI value of &quot;16&quot;, using CIPSO tag &quot;1&quot; (the permissive bitmap tag). The CIPSO and LSM levels/categories are passed through the NetLabel subsystem without any translation.</p>
<dt> <i>netlabelctl cipsov4 add trans doi:8 tags:1 levels:0=0,1=1 categories:0=1,1=0</i></p>
<dd>
<dd>Add a CIPSO/IPv4 configuration with a DOI value of &quot;8&quot;, using CIPSO tag &quot;1&quot; (the permissive bitmap tag). The specified mapping converts local LSM levels &quot;0&quot; and &quot;1&quot; to CIPSO levels &quot;0&quot; and &quot;1&quot; respectively while local LSM categories &quot;0&quot; and &quot;1&quot; are mapped to CIPSO categories &quot;1&quot; and &quot;0&quot; respectively.</p>
<dt> <i>netlabelctl -p cipsov4 list</i></p>
<dd>
<dd>Display all of the CIPSO/IPv4 configurations in a human readable format.</p>
<dt> <i>netlabelctl -p cipsov4 list doi:16</i></p>
<dd>
<dd>Display specific information about the CIPSO/IPv4 DOI 16 configuration.</p>
<dt> <i>netlabelctl cipsov4 del doi:8</i></p>
<dd>
<dd>Delete the CIPSO/IPv4 configuration assigned to DOI 8. In addition to removing the CIPSO/IPv4 configuration any domain mappings using this configuration will also be removed.</p>
<dt> <i>netlabelctl map add domain:lsm_domain protocol:cipsov4,8</i></p>
<dd>
<dd>Add a domain mapping so that all outgoing packets sent from the &quot;lsm_domain&quot; will be labeled according to the CIPSO/IPv4 protocol using DOI 8.</p>
<dt> <i>netlabelctl map add domain:lsm_domain address:192.168.1.0/24 protocol:cipsov4,8</i></p>
<dd>
<dd>Add a mapping so that all outgoing packets sent from the &quot;lsm_domain&quot; to the 192.168.1.0/24 network will be labeled according to the CIPSO/IPv4 protocol using DOI 8.</p>
<dt> <i>netlabelctl -p map list</i></p>
<dd>
<dd>Display all of the domain mappings in a human readable format.</p>
<dt> <i>netlabelctl del domain:lsm_domain</i></p>
<dd>
<dd>Delete the domain mapping for the &quot;lsm_domain&quot;, packets sent from the &quot;lsm_domain&quot; will fallback to the default NetLabel mapping.</p>
<dt> <i>netlabelctl unlbl add interface:lo address:::1 label:foo</i></p>
<dd>
<dd>Add a static/fallback label to assign the &quot;foo&quot; security label to unlabeled packets entering the system over the &quot;lo&quot; (loopback) interface with an IPv6 source address of &quot;::1&quot; (localhost).</p>
<dt> <i>netlabelctl unlbl add default address:192.168.0.0/16 label:bar</i></p>
<dd>
<dd>Add a static/fallback label to assign the &quot;bar&quot; security label to unlabeled packets entering the system over any interface with an IPv4 source address in the 192.168.0.0/16 network.</dl>
<h2>Notes</h2>
<p>The NetLabel subsystem is supported on Linux Kernels version 2.6.19 and later. The static, or fallback, labels are only supported on Linux Kernels version 2.6.25 and later. The domain mapping address selectors are only supported on Linux Kernels 2.6.28 and later. </p>
<p> The NetLabel project site, with more information including the source code repository, can be found at <a rel="nofollow" href="http://netlabel.sf.net.">http://netlabel.sf.net.</a> This program is currently under development, please report any bugs at the project site or directly to the author.</p>
<h2>Author</h2>
<p>Paul Moore &lt;paul [at] paul-moore.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netlabel-config/">netlabel-config</a></code>(8) </p>
