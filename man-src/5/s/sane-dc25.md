---
title: "sane-dc25(5)"
name: "sane-dc25"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-dc25/"
description: "sane-dc25 – SANE backend for Kodak DC20/DC25 Digital Cameras"
---

<p>sane-dc25 &#8211; SANE backend for Kodak DC20/DC25 Digital Cameras</p>
<h2>Description</h2>
<p>The <code>sane-dc25</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Kodak DC20 and DC25 cameras. At present, only the DC25 has been tested, but since the code is based on a DC20 interface program, it is likely to work for that model also.</p>
<h2>Device Names</h2>
<p>The current version of the backend only allows one camera to be connected. The device name is always &quot;0&quot;.</p>
<h2>Configuration</h2>
<p>The contents of the <i>dc25.conf</i> specify the serial port and baud rate to use. The baud rate specifies the maximum rate to use while downloading pictures. (The camera is always initialized using 9600 baud, then switches to the higher rate). On my 90MHz Pentium, I usually have no problems downloading at 115200 baud as long as the system is not excessively busy and the &quot;interrupt-unmask flag&quot; is set in the IDE driver (<i>hdparm -u1</i>). Supported baud rates are: 9600, 19200, 38400, 57600, and 115200. </p>
<p> The dumpinquiry line causes some information about the camera to be printed to stderr during startup. Note: This is not compatible with saned, so make sure you don&#8217;t have any dumpinquiry lines if you are using saned (i.e. scanning on a remote machine using a network). </p>
<p> Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>port=/dev/ttyS0<br />
 # this is a comment<br />
 baud=115200<br />
 dumpinquiry</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/dc25.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dc25.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dc25.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_DC25</code></p>
<dd>If the library was compiled with debugging support enabled, this environment variable controls the debug level for this backend. A value of 128 requests maximally copious debug output; smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<p>Peter Fales, <i>dc25-devel [at] fales-lorenz.net</i>.</p>
<h2>Bugs</h2>
<p>Known bugs/limitations are: I haven&#8217;t figured out how to trigger an option reload following a &quot;scan.&quot; This causes problems when a new picture is snapped for example, the slider that is used to select the picture from the camera may not be updated immediately. More general comments, suggestions, and inquiries about frontends or SANE should go to the SANE Developers mailing list (see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details). You must be subscribed to the list, otherwise your mail won&#8217;t be sent to the subscribers. </p>
