---
title: "shorewall-modules(5)"
name: "shorewall-modules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-modules/"
description: "modules – Shorewall file"
---

<p>modules &#8211; Shorewall file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/share/shorewall/modules</code></p>
<dt> <code>/usr/share/shorewall/helpers</code></dl>
<h2>Description</h2>
<dd>These files specify which kernel modules Shorewall will load before trying to determine your iptables/kernel&#8217;s capabilities. The modules file is used when LOAD_HELPERS_ONLY=No in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(8); the helpers file is used when LOAD_HELPERS_ONLY=Yes Each record in the files has the following format:</p>
<dl>
<dt> <code>loadmodule</code> <i>modulename</i> [<i>moduleoption</i>&#8230;]</dl>
<dd>The <i>modulename</i> names a kernel module (without suffix). Shorewall will search for modules based on your MODULESDIR and MODULE_SUFFIX settings in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(8). The <i>moduleoption</i>s are passed to modprobe (if installed) or to insmod. The /usr/share/shorewall/modules file contains a large number of modules. Users are encouraged to copy the file to /etc/shorewall/modules and modify the copy to load only the modules required or to use LOAD_HELPERS_ONLY=Yes..if n</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 If you build monolithic kernels and have not installed module-init-tools, then create an empty /etc/shorewall/modules file; that will prevent Shorewall from trying to load modules at all. </p>
<h2>Example</h2>
<p>loadmodule ip_conntrack_ftp ports=21,221</p>
<h2>Files</h2>
<p>/usr/share/shorewall/modules </p>
<p> /usr/share/shorewall/helpers </p>
<p> /etc/shorewall/modules </p>
<p> /etc/shorewall/helpers</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
