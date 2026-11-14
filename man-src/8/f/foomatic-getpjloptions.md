---
title: "foomatic-getpjloptions(8)"
name: "foomatic-getpjloptions"
section: "8"
letter: "f"
url: "/docs/linux/man/8-foomatic-getpjloptions/"
description: "foomatic-getpjloptions – <put a short description here>"
---

<p>foomatic-getpjloptions &#8211; &lt;put a short description here&gt;</p>
<h2>Synopsis</h2>
<p><code>foomatic-getpjloptions</code><i> device</i> <code>foomatic-getpjloptions</code><i> hostname port</i> </p>
<h2>Description</h2>
<p><code>foomatic-getpjloptions</code> Sends a set of PJL commands and reads back the PJL options and status from a printer over a network connection or device bidirectional interface such as parallel, USB, serial. printers to standard output. The output can be piped into foomatic-addpjloptions to add options to the database.</p>
<h3>Options</h3>
<dl>
<dt><code>device</code></p>
<dd>The interface to which a local printer is connected, e.g. /dev/lp0, /dev/usb/lp0, /dev/tty00, etc. For a parallel port, you must have bidirectional support enabled at the BIOS level and the parallel port driver must support the bidirectional mode. Check your parallel port BIOS settings for EPP/bi-directional mode.</p>
<dt><code>hostname</code></p>
<dd>Host name or IP address of a network printer (HP JetDirect, DLINK, etc.).</p>
<dt><code>port</code></p>
<dd>Port on which your network printer listens for socket (Appsocket) connections. Most common ports are 9100 (JetDirect), 10000 (DLINK). Usually you can configure the port via a configuration interface. </p>
<h2>Exit Status</h2>
<p><code>foomatic-getpjloptions</code> returns ???</p>
<h2>Author</h2>
<p>Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; for the foomatic project using output from the associated binary. Modified by Patrick Powell &lt;papowell at lprng.com&gt; to provide betters support for network printers, error messages, and remove CR and FF from output.</p>
<h2>Warnings</h2>
<p>Uni-directional protocols as remote LPD are not supported as no status is returned. Some network print servers which attach to a printer parallel port do not support bidirectional mode.</p>
