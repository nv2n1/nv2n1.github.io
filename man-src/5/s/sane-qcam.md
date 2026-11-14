---
title: "sane-qcam(5)"
name: "sane-qcam"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-qcam/"
description: "sane-qcam – SANE backend for Connectix QuickCam cameras"
---

<p>sane-qcam &#8211; SANE backend for Connectix QuickCam cameras</p>
<h2>Description</h2>
<p>The <code>sane-qcam</code> library implements a SANE (Scanner Access Now Easy) backend that provides access Connectix QuickCam cameras.</p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>port</i></dl>
<p> where <i>port</i> is the I/O port address at which the device resides. This address is normally specified in hexadecimal using C syntax (e.g., 0x37b) and may be prefixed with the letter &quot;u&quot; (e.g., u0x37b) to force the backend to access the camera in uni-directional mode.</p>
<h2>Configuration</h2>
<p>The contents of the <i>qcam.conf</i> file is a list port addresses that may be connected to a Connectix QuickCam. Empty lines and everything starting from a hash mark (#) up to the end of a line are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>0x37b # /dev/lp0<br />
 0x378 # /dev/lp1<br />
 u0x278 # /dev/lp2 forced in uni-directional mode<br />
 0x3bc # /dev/lp0 (alternate address)</dl>
<p> In general, it is safest to list only the port addresses that really correspond to a QuickCam. For example, if one of the listed addresses actually connect to a printer, then starting up this backend will cause the printer to perform a device reset (which is generally undesirable).</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/qcam.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-qcam.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-qcam.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_QCAM</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Author</h2>
<p>David Mosberger</p>
<h2>Bugs</h2>
<p>Support is currently limited to the color version of the QuickCam. The black-and-white camera is starting to work too, but I don&#8217;t believe it works in all cases yet. Reportedly, acquiring images of certain sizes work fine, but others result in shifted images (sounds like a problem due to byte-padding). The program needs root-privileges since it needs to be able to access the camera&#8217;s I/O ports. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
