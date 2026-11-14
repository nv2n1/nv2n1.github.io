---
title: "bluetoothd(8)"
name: "bluetoothd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bluetoothd/"
description: "bluetoothd – Bluetooth daemon"
---

<p>bluetoothd &#8211; Bluetooth daemon</p>
<h2>Synopsis</h2>
<p><code>bluetoothd</code> [&#8211;version] | [&#8211;help] </p>
<p> <code>bluetoothd</code> [&#8211;nodetach] [&#8211;compat] [&#8211;experimental] [&#8211;debug=&lt;<i>files</i>&gt;] [&#8211;plugin=&lt;<i>plugins</i>&gt;] [&#8211;noplugin=&lt;<i>plugins</i>&gt;]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bluetoothd</code> daemon, which manages all the Bluetooth devices. <code>bluetoothd</code> can also provide a number of services via the D-Bus message bus system.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd>Print bluetoothd version and exit.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Print bluetoothd options and exit.</p>
<dt><code>-n</code>,<code> &#8211;nodetach</code></p>
<dd>Enable logging in foreground. Directs log output to the controlling terminal in addition to syslog.</p>
<dt><code>-f</code>,<code> &#8211;configfile</code></p>
<dd>Specifies an explicit config file path instead of relying on the default path(<i>/etc/bluetooth/main.conf</i>) for the config file.</p>
<dt><code>-d, &#8211;debug=&lt;file1&gt;:&lt;file2&gt;:&#8230;</code></p>
<dd>Sets how much information bluetoothd sends to the log destination (usually syslog&#8217;s &quot;daemon&quot; facility). If the file options are omitted, then debugging information from all the source files are printed. If file options are present, then only debug prints from that source file are printed. The option can be a pattern containing &quot;*&quot; and &quot;?&quot; characters. </p>
<p> Example: &#8211;debug=src/adapter.c:src/agent.c</p>
<dt><code>-p, &#8211;plugin=&lt;plugin1&gt;,&lt;plugin2&gt;,..</code></p>
<dd>Load these plugins only. The option can be a pattern containing &quot;*&quot; and &quot;?&quot; characters.</p>
<dt><code>-P, &#8211;noplugin=&lt;plugin1&gt;,&lt;plugin2&gt;,..</code></p>
<dd>Never load these plugins. The option can be a pattern containing &quot;*&quot; and &quot;?&quot; characters.</p>
<dt><code>-C</code>,<code> &#8211;compat</code></p>
<dd>Provide deprecated command line interfaces.</p>
<dt><code>-E</code>,<code> &#8211;experimental</code></p>
<dd>Enable experimental interfaces. Those interfaces are not guaranteed to be compatible or present in future releases.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/bluetooth/main.conf</i></p>
<dd>Location of the global configuration file.</dl>
<h2>Resources</h2>
<p><i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>Reporting Bugs</h2>
<p><i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>Author</h2>
<p>Marcel Holtmann, Philipp Matthias Hahn, Fredrik Noring</p>
<h2>Copyright</h2>
<p>Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL).</p>
