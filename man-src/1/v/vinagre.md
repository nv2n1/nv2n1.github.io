---
title: "vinagre(1)"
name: "vinagre"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vinagre/"
description: "vinagre – a remote desktop viewer for the GNOME Desktop"
---

<h2>NAME</h2>
<p> vinagre &#8211; a remote desktop viewer for the GNOME Desktop</p>
<h2>SYNOPSYS</h2>
<p> <code>vinagre</code> [<code>OPTIONS</code>] [<i>server</i>][::<i>port</i>|:display]</p>
<h2>DESCRIPTION</h2>
<p> <code>vinagre</code> is a remote desktop viewer for the GNOME desktop. It can support many protocols using a plugin system. Current plugins exist for VNC and SSH. Vinagre has many features, among others:. </p>
<p> &#8211; Support for multiple connections simultaneously </p>
<p> &#8211; Bookmarks and history support </p>
<p> &#8211; Avahi integration </p>
<p> &#8211; GNOME keyring integration </p>
<p> &#8211; You can connect to a VNC server by double clicking on a .vnc file when using nautilus.</p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show help options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-F</code>, <code>&#8211;file</code>=<i>filename</i></p>
<dd> Opens a .vnc file</p>
<dt><code>-f</code>, <code>&#8211;fullscreen</code></p>
<dd> Open Vinagre in fullscreen mode</p>
<dt><code>&#8211;geometry</code>=<i>GEOMETRY</i></p>
<dd> Specify geometry of the Vinagre window in X11 format</p>
<dt>-n, <code>&#8211;new-window</code></p>
<dd> Create a new toplevel window in an existing instance of Vinagre</p>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</dl>
<p> Run &#8216;vinagre <code>&#8211;help</code>&#8216; to see a full list of available command line options</p>
<h2>OPERANDS</h2>
<p> The following operands are supported:</p>
<dl>
<dt><i></i>[server][::<i>port|:display</i>]</p>
<dd> Specifies the VNC server to connect to. The VNC server can be either a hostname, or an IP address. If the server is an IPv6 address, it must be enclosed by square brackets. The address can optionally be followed by two colons (::) and the VNC port number, or alternatively by one colon (:) and the display where Vinagre should run. If a port is not specified, default value of 5900 will be used. If the value is lower than 1024, 5900 will be added to it. For example, &quot;:0&quot; means &quot;5900&quot; and &quot;:1&quot; means &quot;:5901&quot;. If only a port is specified, but not the hostname, localhost will be assumed. Possible values for the display are between 0 and 1024. If a display number greater than 1024 is specified, it will be assumed to be a port. Note that you can&#8217;t specify the port and the display at the same time.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1: Start vinagre from the command line</code> </p>
<pre>
example% <code>vinagre</code>
</pre>
<p> <code>Example 2: Create a new top-level window</code> </p>
<pre>
example% <code>vinagre --new-window</code>
</pre>
<p> <code>Example 3: Connect to a specified VNC server and port</code> </p>
<pre>
example% <code>vinagre snoopy::5900</code>
</pre>
<p> <code>Example 4: Connect to a specified IPv4 address and port</code> </p>
<pre>
example% <code>vinagre 192.168.1.35::2700
</code></pre>
<p> <code>Example 5: Connect to a specified IPv6 address and port</code> </p>
<pre>
example% <code>vinagre [2001:0db8:0:0:0:0:1428:57ab]::2700
</code></pre>
<p> <code>Example 6: Connect to a VNC server specified by a .vnc file</code> </p>
<pre>
example% <code>vinagre -F snoopy.vnc</code>
</pre>
<p> <code>Example 7: Connect to localhost on a specified port in fullscreen mode</code> </p>
<pre>
example% <code>vinagre -f ::5900
</code></pre>
<h2>SEE ALSO</h2>
<p> Vinagre help manual</p>
<h2>AUTHOR</h2>
<p> Vinagre was written by Jonh Wendell &lt;wendell [at] bani.com.br&gt; and David King &lt;amigadave [at] amigadave.com&gt;</p>
<dl>
<dt>This manual page was written by Emilio Pozuelo Monfort &lt;pochu [at] ubuntu.com&gt; and Halton Huo &lt;halton.huo [at] sun.com&gt;.</p>
<dd>
</dl>
<h2>Index</h2>
