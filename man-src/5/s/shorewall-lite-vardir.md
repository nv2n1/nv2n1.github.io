---
title: "shorewall-lite-vardir(5)"
name: "shorewall-lite-vardir"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-lite-vardir/"
description: "vardir – Shorewall Lite file"
---

<p>vardir &#8211; Shorewall Lite file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall-lite/vardir</code></dl>
<h2>Description</h2>
<dd>This file does not exist by default. You may create the file if you want to change the directory used by Shorewall Lite to store state information, including compiled firewall scripts. By default, the directory used is /var/lib/shorewall-lite/. The file contains a single variable assignment: <code>VARDIR=</code><i>directory</i> where <i>directory</i> is the name of a directory. If you add this file, you should copy the files from /var/lib/shorewall-lite to the new directory before performing a <code>shorewall-lite restart</code>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Beginning with Shorewall 4.5.2, use of this file is deprecated in favor of specifying VARDIR in the shorewallrc file used during installation of Shorewall Core. While the name of the variable remains VARDIR, the meaning is slightly different. When set in shorewallrc, Shorewall Lite, will create a directory under the specified path name to hold state information. Example: VARDIR=/opt/var/lib/ The state directory for Shorewall Lite will be /opt/var/lib/shorewall-lite/. When VARDIR is set in /etc/shorewall-lite/vardir, Shorewall Lite will save its state in the <i>directory</i> specified. </p>
<h2>Example</h2>
<p>VARDIR=/root/shorewall</p>
<h2>Files</h2>
<p>/etc/shorewall-lite/vardir</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall-interfaces/">shorewall-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsec/">shorewall-ipsec</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-route_rules/">shorewall-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-tcrules/">shorewall-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5) </p>
