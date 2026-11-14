---
title: "vdsclient(1)"
name: "vdsclient"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdsclient/"
description: "vdsClient – VDSM’s command line interface"
---

<p>vdsClient &#8211; VDSM&#8217;s command line interface</p>
<h2>Synopsis</h2>
<p><code>vdsClient [-s] &lt;host&gt; &lt;command&gt; [args]</code></p>
<h2>Description</h2>
<p>The <code>vdsClient</code> is a command-line client to <a href="/docs/linux/man/8-vdsmd/">vdsmd</a>(8) xml-rpc API. It is intended to assist testing and debugging of the Red Hat Enterprise Virtualization Manager (RHEV-M) suite. </p>
<p> For example, <code>vdsClient -s 0 list table</code> will print a succinct list of all running virtual machines on the local host (assuming it is using secure connection). </p>
<h2>Warning</h2>
<p><code>vdsClient</code> is a debug tool, which is capable of harming the operation of a single RHEV node and even a complete RHEV cluster. Its use is not supported or endorsed by Red Hat. </p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h</code></p>
<dd>Display vdsClient&#8217;s help</p>
<dt><code>-m</code></p>
<dd>List supported methods and their params (Short help)</p>
<dt><code>-s</code></p>
<dd>Connect to server with SSL.</p>
<dt><code>&#8211;truststore &lt;path&gt;</code></p>
<dd>Specify the location of VDSM&#8217;s trust store. The default location is /etc/pki/vdsm. </p>
</dl>
<h2>Files</h2>
<dl COMPACT>
<dt> <i>/etc/pki/vdsm</i></p>
<dd>VDSM&#8217;s trust store. Used to obtain SSL key for secure communication with VDSM. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vdsmd/">vdsmd</a>(8)</code> </p>
<h2>Author</h2>
<p>vdsClient was written by Ayal Baron, Barak Azulay, Cyril Plisko, Dan Kenigsberg, Doron Fediuck, Igor Lvovsky, Shahar Frank, Simon Grinberg, and probably others. </p>
<h2>Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt; </p>
<h2>Copyright</h2>
<p>Copyright 2010 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.</p>
