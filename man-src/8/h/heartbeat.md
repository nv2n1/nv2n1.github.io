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
<dt><code>-d</code></dt>
<dd>Increment debugging level. Higher levels are more verbose.</dd>
<dt><code>-r</code></dt>
<dd>Reloads heartbeat. It just sends it a SIGHUP. If nothing has changed nothing will happen. If ha.cf or authkeys has changed it will start heartbeat or reread authkeys. May not be used with -R.</dd>
<dt><code>-k</code></dt>
<dd>Kill (stop) heartbeat.</dd>
<dt><code>-s</code></dt>
<dd>Report heartbeat status.</dd>
<dt><code>-R</code></dt>
<dd>Heartbeat restart exec flag (internal use only). May not be used with -r.</dd>
<dt><code>-C</code></dt>
<dd>Heartbeat current resource state for restart (internal use only). Only valid with -R.</dd>
<dt><code>-V</code></dt>
<dd>Print out heartbeat version.</dd></dl>
<p> Note that most of these options are used for supporting the heartbeat <i>init script</i>, which provides the conventional start, stop, status and restart options (among others). It is recommended to use this rather than invoking the heartbeat command directly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-cl_status/">cl_status</a>(1), <a href="/docs/linux/man/8-apphbd/">apphbd</a>(8) </p>
<h2>Documentation</h2>
<p>More information may be found at <a rel="nofollow" href="http://www.linux-ha.org.">http://www.linux-ha.org.</a></p>
<h2>Files</h2>
<dl>
<dt>/etc/ha.cf, /etc/haresources, /etc/authkeys</dt>
<dd></dd></dl>
<h2>Authors</h2>
<pre>heartbeat - Alan Robertson &lt;alanr [at] unix.sh&gt; et al.
man page - Juan Pedro Paredes Caballero &lt;juampe [at] retemail.es&gt;
 Horms &lt;horms [at] verge.net.au&gt;</pre>
