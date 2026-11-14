---
title: "shorewall6-lite-vardir(5)"
name: "shorewall6-lite-vardir"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-lite-vardir/"
description: "vardir – Shorewall6 Lite file"
---

<p>vardir &#8211; Shorewall6 Lite file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6-lite/vardir</code></dl>
<h2>Description</h2>
<dd>This file does not exist by default. You may create the file if you want to change the directory used by Shorewall6 Lite to store state information, including compiled firewall scripts. By default, the directory used is /var/lib/shorewall6-lite/. The file contains a single variable assignment: <code>VARDIR=</code><i>directory</i> where <i>directory</i> is the name of a directory. If you add this file, you should copy the files from /var/lib/shorewall6-lite to the new directory before performing a <code>shorewall6-lite restart</code>.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Beginning with Shorewall 4.5.2, use of this file is deprecated in favor of specifying VARDIR in the shorewallrc file used during installation of Shorewall Core. While the name of the variable remains VARDIR, the meaning is slightly different. When set in shorewallrc, Shorewall6 Lite will create a directory under the specified path name to hold state information. Example: VARDIR=/opt/var/lib/ The state directory for Shorewall Lite will be /opt/var/lib/shorewall6-lite. When VARDIR is set in /etc/shorewall6-lite/vardir, Shorewall Lite will save its state in the <i>directory</i> specified. </p>
<h2>Example</h2>
<p>VARDIR=/root/shorewall6</p>
<h2>Files</h2>
<p>/etc/shorewall6-lite/vardir</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-route_rules/">shorewall6-route_rules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-tcrules/">shorewall6-tcrules</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5) </p>
