---
title: "sane-dc210(5)"
name: "sane-dc210"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-dc210/"
description: "sane-dc210 – SANE backend for Kodak DC210 Digital Camera"
---

<p>sane-dc210 &#8211; SANE backend for Kodak DC210 Digital Camera</p>
<h2>Description</h2>
<p>The <code>sane-dc210</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Kodak DC210 camera. THIS IS EXTREMELY ALPHA CODE! USE AT YOUR OWN RISK!!</p>
<h2>Device Names</h2>
<p>The current version of the backend only allows one camera to be connected. The device name is always &quot;0&quot;.</p>
<h2>Configuration</h2>
<p>The contents of the <i>dc210.conf</i> specify the serial port and baud rate to use. The <code>baud</code> rate specifies the maximum rate to use while downloading pictures. (The camera is always initialized using 9600 baud, then switches to the higher rate). On my 90MHz Pentium, I usually have no problems downloading at 115200 baud as long as the system is not excessively busy and the &quot;interrupt-unmask flag&quot; is set in the IDE driver (<i>hdparm -u1</i>). Supported baud rates are: 9600, 19200, 38400, 57600, and 115200. </p>
<p> The <code>dumpinquiry</code> line causes some information about the camera to be printed. </p>
<p> <code>cmdrespause</code> specifies how many usec (1,000,000ths of a second) to wait between writing the command and reading the result. 125000 seems to be the lowest I could go reliably. </p>
<p> <code>breakpause</code> specifies how many usec (1,000,000ths of a second) between sending the &quot;back to default&quot; break and sending commands. </p>
<p> Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>port=/dev/ttyS0<br />
 # this is a comment<br />
 baud=115200<br />
 dumpinquiry<br />
 cmdrespause=125000<br />
 breakpause=1000000</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/dc210.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dc210.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dc210.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d.</i> If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config,</i> <i>.,</i> and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_DC210</code></p>
<dd>If the library was compiled with debugging support enabled, this environment variable controls the debug level for this backend. A value of 128 requests maximally copious debug output; smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<p>Brian J. Murrell </p>
<p> This backend is based somewhat on the dc25 backend included in this package by Peter Fales. </p>
<p> The manpage was copied from the dc25 backend and somewhat edited by Henning Meier-Geinitz.</p>
<h2>Bugs</h2>
<p>Known bugs/limitations are: ? More general comments, suggestions, and inquiries about frontends or SANE should go to the SANE Developers mailing list (see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details). You must be subscribed to the list, otherwise your mail won&#8217;t be sent to the subscribers. </p>
