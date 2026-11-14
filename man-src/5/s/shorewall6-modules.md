---
title: "shorewall6-modules(5)"
name: "shorewall6-modules"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-modules/"
---

modules - shorewall6 file

<h2>Synopsis</h2>

<dl><dt> <b>/usr/share/shorewall6/modules</b>
<dt> <b>/usr/share/shorewall6/helpers</b></dl>

<h2>Description</h2>

<dd>These files specify which kernel modules shorewall6 will load before trying to determine your ip6tables/kernel's capabilities. The modules file is used when LOAD_HELPERS_ONLY=No in m[blue]<b>shorewall6.conf</b>m[]<font SIZE="-2">[1]</font>(5); the helpers file is used when LOAD_HELPERS_ONLY=Yes. Each record in the files has the following format:
<dl><dt> <b>loadmodule</b> <i>modulename</i> [<i>moduleoption</i>...]</dl><dd>The <i>modulename</i> names a kernel module (without suffix). shorewall6 will search for modules based on your MODULESDIR and MODULE_SUFFIX settings in m[blue]<b>shorewall6.conf</b>m[]<font SIZE="-2">[1]</font>(5). The <i>moduleoption</i>s are passed to modprobe (if installed) or to insmod. The /usr/share/shorewall6/modules file contains a large number of modules. Users are encouraged to copy the file to /etc/shorewall6/modules and modify the copy to load only the modules required or use LOAD_HELPERS_ONLY=Yes..if n
<dl><dd><font SIZE="+1"> <b>Note</b> </font> 
 If you build monolithic kernels and have not installed module-init-tools, then create an empty /etc/shorewall6/modules file; that will prevent shorewall6 from trying to load modules at all. 

<h2>Example</h2>

loadmodule ip_conntrack_ftp ports=21,221

<h2>Files</h2>

/usr/share/shorewall6/modules 

 /usr/share/shorewall6/helpers 

 /etc/shorewall6/modules 

 /etc/shorewall6/helpers

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a HREF="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a HREF="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a HREF="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a HREF="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a HREF="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a HREF="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a HREF="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a HREF="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a HREF="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a HREF="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a HREF="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a HREF="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a HREF="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a HREF="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a HREF="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a HREF="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a HREF="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)

<h2>Notes</h2>

<dl><dt> 1.
<dd>shorewall6.conf
<dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
 
