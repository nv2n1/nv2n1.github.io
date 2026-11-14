---
title: "sane-net(5)"
name: "sane-net"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-net/"
description: "sane-net – SANE network backend"
---

<p>sane-net &#8211; SANE network backend</p>
<h2>Description</h2>
<p>The <code>sane-net</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to image acquisition devices through a network connection. This makes it possible to control devices attached to a remote host and also provides a means to grant users access to protected resources. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>host</i>:<i>device</i></dl>
<p> Where <i>host</i> is the name (or IP address) of the (remote) host and <i>device</i> is the name of the device on this host that should be addressed. If the device name does not contain a colon (:), then the entire string is treated as the <i>device</i> string for the default host. The default host is the host listed last in the configuration file (see below). </p>
<p> An IPv6 address can be specified enclosed in square brackets: </p>
<dl>
<dd><i>[::1]</i>:<i>device</i></dl>
<h2>Configuration</h2>
<p>The <i>net.conf</i> file contains both backend options and a list of host names (or IP addresses) that should be contacted for scan requests. Anything that isn&#8217;t one of the options listed below will be treated as an host name. </p>
<dl>
<dt><code>connect_timeout = nsecs</code></p>
<dd>Timeout (in seconds) for the initial connection to the <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) server. This will prevent the backend from blocking for several minutes trying to connect to an unresponsive <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) host (network outage, host down, &#8230;). The environment variable <code>SANE_NET_TIMEOUT</code> can also be used to specify the timeout at runtime.</dl>
<p> Empty lines and lines starting with a hash mark (#) are ignored. Note that IPv6 addresses in this file do not need to be enclosed in square brackets. A sample configuration file is shown below: </p>
<dl>
<dd>scan-server.somedomain.firm<br />
 192.168.0.1<br />
 # this is a comment<br />
 localhost<br />
 ::1</dl>
<p> The above list of hosts can be extended at run-time using environment variable <code>SANE_NET_HOSTS</code>. This environment variable is a colon-separated list of hostnames or IP addresses that should be contacted in addition to the hosts mentioned in the configuration file. For example, a user could set the environment variable to the string: </p>
<dl>
<dd>new.scanner.com:[::1]:192.168.0.2:scanner.univ.edu</dl>
<p> To request that hosts <i>new.scanner.com</i> , <i>[::1]</i> , <i>192.168.0.2</i> and <i>scanner.univ.edu</i> are contacted in addition to the hosts listed above. </p>
<p> For this backend to function properly, it is also necessary to define the <code>sane-port</code> service in <i>/etc/services</i>. The <code>sane</code> service should be defined using a line of the following form: </p>
<dl>
<dd>sane-port 6566/tcp # SANE network scanner daemon</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/net.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-net.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-net.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_NET_HOSTS</code></p>
<dd>A colon-separated list of host names or IP addresses to be contacted by this backend.</p>
<dt><code>SANE_NET_TIMEOUT</code></p>
<dd>Number of seconds to wait for a response from the <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) server for the initial connection request.</p>
<dt><code>SANE_DEBUG_NET</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</dl>
<h2>Bugs</h2>
<p>If <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) has timed out, the net backend may loop with authorization requests. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8), <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<p> <i><a rel="nofollow" href="http://www.penguin-breeder.org/?page=sane-net">http://www.penguin-breeder.org/?page=sane-net</a></i></p>
<h2>Author</h2>
<p>David Mosberger and Andreas Beck</p>
