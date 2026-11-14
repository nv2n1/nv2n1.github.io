---
title: "kpac_dhcp_helper(7)"
name: "kpac_dhcp_helper"
section: "7"
letter: "k"
url: "/docs/linux/man/7-kpac_dhcp_helper/"
description: "kpac_dhcp_helper – provides Proxy Auto Configuration to KDE"
---

<p>kpac_dhcp_helper &#8211; provides Proxy Auto Configuration to KDE</p>
<h2>Synopsis</h2>
<pre><code>kpac_dhcp_helper</code></pre>
<h2>Description</h2>
<p>Provides Proxy Auto Configuration to KDE by requesting a JavaScript function that uses the requested URL to determine the proxy settings. Locating that JavaScript can be done by using DHCP or DNS.</p>
<dl>
<dt>DHCP is preferred for its flexibility over DNS, which requires a wpad hostname or a fixed location to a script. The only requirements for DHCP are a network that supports DHCP and a current DHCP configuration. <code>kpac_dhcp_helper</code> is the setuid application needed to support DHCP.</p>
<dd>
<dt>This tool is a support utility for KDE libraries and is not called from the command line.</p>
<dd></dl>
<h2>Options</h2>
<p>kpac_dhcp_helper takes no arguments.</p>
<h2>Security</h2>
<p><code>kpac_dhcp_helper</code> must be used as setuid root.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3), <code><a href="/docs/linux/man/8-dhclient/">dhclient</a></code>(8), <code><a href="/docs/linux/man/8-dhcpd/">dhcpd</a></code>(8), <code><a href="/docs/linux/man/8-named/">named</a></code>(8)</p>
<h2>Author</h2>
<p>Manpage written by Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</p>
