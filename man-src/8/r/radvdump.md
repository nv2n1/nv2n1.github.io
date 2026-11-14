---
title: "radvdump(8)"
name: "radvdump"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radvdump/"
description: "radvdump – dump router advertisements"
---

<p>radvdump &#8211; dump router advertisements</p>
<h2>Synopsis</h2>
<p><code>radvdump</code> <code>[ -vhfe ]</code> <code>[ -d </code><i>debuglevel</i><code> ]</code> </p>
<h2>Description</h2>
<p><code>radvdump</code> prints out the contents of incoming router advertisements sent by <code>radvd</code> or some other software implementing (parts of) &quot;Neighbor Discovery for IP Version 6 (IPv6)&quot; (RFC 4861). </p>
<h2>Options</h2>
<p>For every one character option there is also a long option, which is listed right next to the &quot;short&quot; option name: </p>
<dl>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd>Displays the version of <i>radvdump</i> and then aborts.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Displays a short usage description and then aborts.</p>
<dt><code>-f</code>,<code> &#8211;file-format</code></p>
<dd>Output received router advertisements in the format of the <code>radvd</code> configuration file. Since radvd 0.9, this is the default and the switch is provided for backward compatibility only.</p>
<dt><code>-e</code>,<code> &#8211;exclude-defaults</code></p>
<dd>Exclude default valued options from configuration file format. This option is ignored if option <code>-f</code> is not set.</p>
<dt><code>-d </code>debuglevel,<code> &#8211;debug </code>debuglevel</p>
<dd>With this option you turn on debugging information. The debugging level is an integer in the range from 1 to 4, from quiet to very verbose. A debugging level of 0 completely turns off debugging. </p>
<p> The default debugging level is 0. </p>
</dl>
<h2>Files</h2>
<pre>/usr/sbin/radvdump</pre>
<h2>Bugs</h2>
<p>There certainly are some bugs. If you find them or have other suggestions please contact Reuben Hawkins &lt;reubenhwk [at] gmail.com&gt;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radvd/">radvd</a></code>(8), <code><a href="/docs/linux/man/5-radvd-conf/">radvd.conf</a></code>(5)</p>
<h2>Authors</h2>
<pre>Lars Fenneberg &lt;lf [at] elemental.net&gt; - previous maintainer
Nathan Lutchansky &lt;lutchann [at] litech.org&gt; - previous maintainer
Reuben Hawkins &lt;reubenhwk [at] gmail.com&gt; - current maintainer
Marko Myllynen &lt;myllynen [at] lut.fi&gt; - Mobile IPv6 support</pre>
