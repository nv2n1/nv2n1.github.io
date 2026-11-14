---
title: "shorewall6-vardir(5)"
name: "shorewall6-vardir"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-vardir/"
description: "vardir – Shorewall6 file"
---

<p>vardir &#8211; Shorewall6 file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/vardir</code></dl>
<h2>Description</h2>
<dd>This file does not exist by default. You may create the file if you want to change the directory used by Shorewall6 to store state information, including compiled firewall scripts. By default, the directory used is /var/lib/shorewall6/. </p>
<p> The file contains a single variable assignment: </p>
<p> <code>VARDIR=</code><i>directory</i> </p>
<p> where <i>directory</i> is the name of a directory. If you add this file, you should copy the files from /var/lib/shorewall6 to the new directory before performing a <code>shorewall6 restart</code>.</p>
<h2>Example</h2>
<p>VARDIR=/root/shorewall6</p>
<h2>Files</h2>
<p>/etc/shorewall6/vardir</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5) </p>
