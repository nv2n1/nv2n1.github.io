---
title: "shorewall-params(5)"
name: "shorewall-params"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-params/"
description: "params – Shorewall parameters file"
---

<p>params &#8211; Shorewall parameters file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/params</code></dl>
<h2>Description</h2>
<dd>Assign any shell variables that you need in this file. The file is always processed by /bin/sh or by the shell specified through SHOREWALL_SHELL in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font> (5) so the full range of shell capabilities may be used. </p>
<p> It is suggested that variable names begin with an upper case letter to distinguish them from variables used internally within the Shorewall programs </p>
<p> The following variable names must be avoided. Those in <code>bold font</code> must be avoided in all Shorewall versions; those in regular font must be avoided in versions prior to 4.4.8.</p>
<dl>
<dd><code>Any option from </code><code>m[blue]shorewall.conf</code>m[]<font SIZE="-2">[1]</font><code><br />
(5)</code></dl>
<dl>
<dd><code>COMMAND</code></dl>
<dl>
<dd><code>CONFDIR</code></dl>
<dl>
<dd>DEBUG</dl>
<dl>
<dd>ECHO_E</dl>
<dl>
<dd>ECHO_N</dl>
<dl>
<dd>EXPORT</dl>
<dl>
<dd>FAST</dl>
<dl>
<dd>FILEMODE</dl>
<dl>
<dd>HOSTNAME</dl>
<dl>
<dd>IPT_OPTIONS</dl>
<dl>
<dd>NOROUTES</dl>
<dl>
<dd>PREVIEW</dl>
<dl>
<dd>PRODUCT</dl>
<dl>
<dd>PROFILE</dl>
<dl>
<dd>PURGE</dl>
<dl>
<dd>RECOVERING</dl>
<dl>
<dd>RESTOREPATH</dl>
<dl>
<dd>RING_BELL</dl>
<dl>
<dd><code>SHAREDIR</code></dl>
<dl>
<dd><code>Any name beginning with SHOREWALL_ or<br />
SW_</code></dl>
<dl>
<dd>STOPPING</dl>
<dl>
<dd>TEST</dl>
<dl>
<dd>TIMESTAMP</dl>
<dl>
<dd>USE_VERBOSITY</dl>
<dl>
<dd><code>VARDIR</code></dl>
<dl>
<dd>VERBOSE</dl>
<dl>
<dd>VERBOSE_OFFSET</dl>
<dl>
<dd>VERSION</dl>
<p> Example params file: </p>
<dl>
<dd>
<pre>NET_IF=eth0
NET_BCAST=130.252.100.255
NET_OPTIONS=routefilter,norfc1918</pre>
</dl>
<p> Example m[blue]<code>shorewall-interfaces</code>m[]<font SIZE="-2">[2]</font>(5) file. </p>
<dl>
<dd>
<pre>ZONE INTERFACE BROADCAST OPTIONS
net $NET_IF $NET_BCAST $NET_OPTIONS</pre>
</dl>
<p> This is the same as if the interfaces file had contained: </p>
<dl>
<dd>
<pre>ZONE INTERFACE BROADCAST OPTIONS
net eth0 130.252.100.255 routefilter,norfc1918</pre>
</dl>
<h2>Files</h2>
<p>/etc/shorewall/params</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Variables">http://www.shorewall.net/configuration_file_basics.htm#Variables</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 2.</p>
<dd>shorewall-interfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-interfaces.html">http://www.shorewall.net/manpages/shorewall-interfaces.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Variables">http://www.shorewall.net/configuration_file_basics.htm#Variables</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Variables">http://www.shorewall.net/configuration_file_basics.htm#Variables</a></dl>
