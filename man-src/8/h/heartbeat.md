---
title: "heartbeat(8)"
name: "heartbeat"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heartbeat/"
description: "heartbeat – Heartbeat subsystem for High-Availability Linux"
---

<p>heartbeat &#8211; Heartbeat subsystem for High-Availability Linux</p>
<h2>Synopsis</h2>
<p><code>heartbeat</code></p>
<h2>Description</h2>
<p><code>heartbeat</code> is a basic heartbeat subsystem for Linux-HA. It will run scripts at initialisation, and when machines go up or down. This version will also perform IP address takeover using gratuitous ARPs. It works correctly for a 2-node configuration, and is extensible to larger configurations. </p>
<p> It implements the following kinds of heartbeats:<br />
*&nbsp;<wbr>Bidirectional Serial Rings&nbsp;<wbr>(&quot;raw&quot;&nbsp;<wbr>serial ports)<br />
*&nbsp;<wbr>UDP/IP broadcast&nbsp;<wbr>(ethernet, etc.)<br />
*&nbsp;<wbr>UDP/IP multicast&nbsp;<wbr>(ethernet, etc.)<br />
*&nbsp;<wbr>special&nbsp;<wbr>&quot;ping&quot;&nbsp;<wbr>heartbeats for routers, etc. </p>
<p> Comprehensive documentation on the configuration and running of <code>heartbeat</code> is supplied in HTML format with the distribution of the code. If this documentation is not installed on your system it can be found, with the latest distribution of heartbeat on <a rel="nofollow" href="http://www.linux-ha.org/">http://www.linux-ha.org/</a></p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Increment debugging level. Higher levels are more verbose.</p>
<dt><code>-r</code></p>
<dd>Reloads heartbeat. It just sends it a SIGHUP. If nothing has changed nothing will happen. If ha.cf or authkeys has changed it will start heartbeat or reread authkeys. May not be used with -R.</p>
<dt><code>-k</code></p>
<dd>Kill (stop) heartbeat.</p>
<dt><code>-s</code></p>
<dd>Report heartbeat status.</p>
<dt><code>-R</code></p>
<dd>Heartbeat restart exec flag (internal use only). May not be used with -r.</p>
<dt><code>-C</code></p>
<dd>Heartbeat current resource state for restart (internal use only). Only valid with -R.</p>
<dt><code>-V</code></p>
<dd>Print out heartbeat version.</dl>
<p> Note that most of these options are used for supporting the heartbeat <i>init script</i>, which provides the conventional start, stop, status and restart options (among others). It is recommended to use this rather than invoking the heartbeat command directly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cl_status/">cl_status</a>(1), <a href="/docs/linux/man/8-apphbd/">apphbd</a>(8) </p>
<h2>Documentation</h2>
<p>More information may be found at <a rel="nofollow" href="http://www.linux-ha.org.">http://www.linux-ha.org.</a></p>
<h2>Files</h2>
<dl>
<dt>/etc/ha.cf, /etc/haresources, /etc/authkeys</p>
<dd></dl>
<h2>Authors</h2>
<pre>heartbeat - Alan Robertson &lt;alanr [at] unix.sh&gt; et al.
man page - Juan Pedro Paredes Caballero &lt;juampe [at] retemail.es&gt;
 Horms &lt;horms [at] verge.net.au&gt;</pre>
