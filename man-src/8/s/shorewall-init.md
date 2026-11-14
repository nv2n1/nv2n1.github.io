---
title: "shorewall-init(8)"
name: "shorewall-init"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shorewall-init/"
description: "shorewall-init – Companion package"
---

<p>shorewall-init &#8211; Companion package</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/init.d/shorewall-init</code> [start|stop]</dl>
<h2>Description</h2>
<dd>Shorewall-init is an optional package (added in Shorewall 4.4.10) that can be installed along with Shorewall, Shorewall6, Shorewall-lite and/or Shorewall6-lite. It provides two key features:</p>
<dl>
<dd>1. It can close (stop) the firewall during boot prior to starting the network. This can prevent unwanted connections from being accepted after the network comes up but before the firewall is started.</dl>
<dl>
<dd>2. It can interface with your distribution&#8217;s ifup/ifdown scripts and/or NetworkManager to allow firewall actions when an interface starts or stops.</dl>
<p> These two capabilities can be enabled separately. After you install the shorewall-init package, you can activate it by modifying the Shorewall-init configuration file:</p>
<dl>
<dd>&bull; On Debian-based system, the file is /etc/default/shorewall-init.</dl>
<dl>
<dd>&bull; On other systems, the file is /etc/sysconfig/shorewall-init.</dl>
<p> To activate the safe boot feature, edit the configuration file and set PRODUCTS to a space-separated list of Shorewall products that you want to be closed before networking starts. </p>
<pre><code>Example:

PRODUCTS=&quot;shorewall shorewall6&quot;</code></pre>
<p> You also must insure that the compiled scripts for the listed products are compiled using Shorewall 4.4.10 or later. Shorewall</p>
<dl>
<dd><code>shorewall compile</code></dl>
<p> Shorewall6</p>
<dl>
<dd><code>shorewall6 compile</code></dl>
<p> Shorewall-lite</p>
<dl>
<dd>On the administrative system, enter the command <code>shorewall export firewall</code> from the firewall&#8217;s configuration directory.</dl>
<p> Shorewall6-lite</p>
<dl>
<dd>On the administrative system, enter the command <code>shorewall6 export firewall</code> from the firewall&#8217;s configuration directory.</dl>
<p> The second feature (ifup/ifdown and NetworkManager integration) should only be activated on systems that do not use a link status monitor line swping or LSM.</p>
<dl>
<dd>&bull; Edit the configuration file and set IFUPDOWN=1</dl>
<p> For NetworkManager integration, you will want to disable firewall startup at boot and delay it to when your interface comes up. For this to work correctly, you must set the required or the optional option on at least one interface then:</p>
<dl>
<dd>&bull; On Debian-based systems, edit /etc/default/<i>product</i> for each <i>product</i> listed in the PRODUCTS setting and set <code>startup=0</code>.</dl>
<dl>
<dd>&bull; On other systems, use the distribution&#8217;s service control tool (insserv, chkconfig, etc.) to disable startup of the products listed in the PRODUCTS setting.</dl>
<p> On a laptop with both Ethernet and wireless interfaces, you will want to make both interfaces optional and set the REQUIRE_INTERFACE option to Yes in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5) or m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[2]</font> (5). This causes the firewall to remain stopped until at least one of the interfaces comes up.</p>
<h2>Files</h2>
<p>/etc/default/shorewall-init (Debian-based systems) or /etc/sysconfig/shorewall-init (other distributions)</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 2.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
