---
title: "sane-dll(5)"
name: "sane-dll"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-dll/"
description: "sane-dll – SANE dynamic backend loader"
---

<p>sane-dll &#8211; SANE dynamic backend loader</p>
<h2>Description</h2>
<p>The <code>sane-dll</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to an arbitrary number of other SANE backends. These backends may either be pre-loaded at the time the <code>sane-dll</code> library is built or, on systems that support dynamic loading of shared libraries, the backends may be loaded at runtime. In the latter case, adding support for a new backend simply involves installing the relevant library in <i>/usr/lib/x86_64-linux-gnu/sane</i> and adding an entry to the <i>dll.conf</i> configuration file. In other words, no applications need to be modified or recompiled to add support for new devices.</p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>backend</i>:<i>device</i></dl>
<p> Where <i>backend</i> is the name of the backend and <i>device</i> is the name of the device in this backend that should be addressed. If the device name does not contain a colon (:), then the entire string is treated as the <i>device</i> string for the default backend. The default backend is the backend listed last in the configuration file (see below) or the first pre-loaded backend (if any).</p>
<h2>Configuration</h2>
<p>The contents of the <i>dll.conf</i> file is a list of backend names that may be loaded dynamically upon demand. Empty lines are ignored, also everything after a hash mark (#). A sample configuration file is shown below: </p>
<dl>
<dd>net<br />
 # this is a comment<br />
 pnm<br />
 mustek</dl>
<p> It is also possible to add a file in <i>/etc/sane.d/dll.d</i> that contains the list of backends to be added. Backends mentioned in a file included in this directory will be added before any backends listed in <i>dll.conf.</i> Files in <i>/etc/sane.d/dll.d</i> can be freely named. They shall follow the format conventions as apply for <i>dll.conf.</i> </p>
<p> Note that backends that were pre-loaded when building this library do not have to be listed in this configuration file. That is, if a backend was preloaded, then that backend will always be present, regardless of whether it&#8217;s listed in the configuration file or not. </p>
<p> The list of preloaded backends is determined by macro <code>PRELOADABLE_BACKENDS</code> in file backend/Makefile.in of the SANE source code distribution. After changing the value of this macro, it is necessary to reconfigure, rebuild, and reinstall SANE for the change to take effect. </p>
<p> Aliases are defined in the config file <i>dll.aliases</i>. It can contain entries of the form </p>
<dl>
<dd>alias SomeName SaneDeviceName<br />
 alias &quot;Some Name&quot; SaneDeviceName<br />
 hide SaneDeviceName</dl>
<p> For example: </p>
<dl>
<dd>alias Epson net:somehost:epson:/dev/sgX<br />
 alias &quot;Siemens ST400&quot; st400:/dev/sgY<br />
 hide net:somehost:pnm:0<br />
 hide net:somehost:pnm:1<br />
 alias &quot;Read from file&quot; pnm:0<br />
 hide pnm:1</dl>
<p> Aliased device names are automatically hidden. </p>
<p> The idea is that users don&#8217;t have to deal with complicated device names (especially for networked devices), and to hide other exported devices which might confuse them. Note that a hidden device can still be accessed if the device name is known, it just doesn&#8217;t appear on the list.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/dll.aliases</i></p>
<dd>The list of aliased or hidden backends.</p>
<dt><i>/etc/sane.d/dll.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dll.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dll.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_DLL</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
<pre>Value Description
0 print severe errors only
1 print normal errors and important messages
2 print normal messages
3 print debugging messages
4 print everything</pre>
<p>Example: export SANE_DEBUG_DLL=3 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5) </p>
<h2>Author</h2>
<p>David Mosberger</p>
