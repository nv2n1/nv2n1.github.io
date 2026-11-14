---
title: "sane-p5(5)"
name: "sane-p5"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-p5/"
description: "sane-p5 – SANE backend for the Primax PagePartner"
---

<p>sane-p5 &#8211; SANE backend for the Primax PagePartner</p>
<h2>Description</h2>
<p>The <code>sane-p5</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Primax PagePartner parallel port sheet fed scanner. This backend handles 100, 150, 200, 300 and 600 dpi scan resolutions, in color and gray modes. The 600 dpi is actually 300&#215;600 with lines enlarged to match the vertical resolution. <code>EPP/ECP MODES ONLY</code> The current version of the backend uses only EPP or ECP mode to communicate with the scanner. It is recommended that you set your parallel port to EPP in BIOS with the current version of this backend. ECPEPP will only work if you use a 2.4 or 2.6 kernel with ppdev character device support. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>port value</i></dl>
<p> Where <code>value</code> is : </p>
<dl>
<dd>
<dl>
<dt>auto</p>
<dd>autodetect all parallel ports and probe them for scanner</p>
<dt>/dev/parport0</p>
<dd>uses linux ppdev device, depending on the number of available parallel port, you have to use /dev/parport1, /dev/parport2, &#8230;</dl>
</dl>
<p> You can rename any device using the </p>
<dl>
<dd><i>option name my_name</i></dl>
<p> option. This option apply to the last port option.</p>
<h2>Configuration</h2>
<p>Please make sure to edit <i>dll.conf</i> <code>before</code> you use the backend, since this backend isn&#8217;t enabled by default.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/p5.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-p5.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-p5.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_P5</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<dl>
<dd>
<pre>level debug output
------- ------------------------------
 0 critical errors
 1 errors
 2 warnings &amp; minor errors
 4 information messages
 8 start/stop of functions
 16 tracing messages
 32 I/O functions
 64 I/O functions with traces
 128 scanned/calibration data</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5), <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>Author</h2>
<p>St&eacute;phane Voltz &lt;<i>stef.dev [at] free.fr</i>&gt;</p>
<h2>Credits</h2>
<p>Support for the Prima PagePartner has been made possible thank to an hardware donation by S&eacute;bastien Lange.</p>
<h2>Bug Reports</h2>
<p>If something doesn&#8217;t work mail sane-devel [at] alioth-lists.debian.net or submit an issue via <i><a rel="nofollow" href="https://gitlab.com/sane-project/backends/issues/new">https://gitlab.com/sane-project/backends/issues/new</a></i> with a label of backend/p5. Please give as much information as you can. </p>
<dl>
<dt><i>SANE version</i></p>
<dd>run &quot;scanimage -V&quot; to determine this</p>
<dt><i>the backend version and your scanner hardware</i></p>
<dd>run <i>SANE_DEBUG_P5=255 scanimage -L 2&gt;log</i> as root. If you don&#8217;t get any output from the p5 backend, make sure a line &quot;p5&quot; is included into your <i>/etc/sane.d/dll.conf</i>. If your scanner isn&#8217;t detected, make sure you&#8217;ve defined the right port address, or the correct device in your p5.conf.</p>
<dt><i>the name of your scanner/vendor</i></p>
<dd>also a worthy information. Please also include the optical resolution and lamp type of your scanner, both can be found in the manual of your scanner.</p>
<dt><i>any further comments</i></p>
<dd>if you have comments about the documentation (what could be done better), or you think I should know something, please include it. </p>
</dl>
