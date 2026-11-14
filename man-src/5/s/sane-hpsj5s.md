---
title: "sane-hpsj5s(5)"
name: "sane-hpsj5s"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hpsj5s/"
description: "sane-hpsj5s – SANE backend for HP ScanJet 5S sheet-fed scanner"
---

<p>sane-hpsj5s &#8211; SANE backend for HP ScanJet 5S sheet-fed scanner</p>
<h2>Description</h2>
<p>The <code>sane-hpsj5s</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to a parallel port Hewlett-Packard ScanJet 5S scanner. IMPORTANT: this is alpha code. Don&#8217;t expect this to work correctly. Many functions are missing, others contain errors. In some cases, your computer might even hang. It cannot be excluded (although I consider it extremely improbable) that your scanner will be damaged. LIMITATIONS: For now this backend works only on Linux. This limitation is due to dependence on the <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3) library. If your system supports <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3) too, this backend should work. If you ported <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3) for your platform, please let me know. Your system should support <code>EPP</code> (or <code>EPP+ECP</code>) mode to operate this scanner. Future versions will support ECP and SPP (Nibble and Byte) modes also. It&#8217;s planned to support scanners not only at daisy-chain position 0, but anywhere. Support for multiple scanners could be implemented too. Current version implements only gray scale scanning. True Color and B/W modes are not supported for now. That said, TESTERS ARE WELCOME. Send your bug reports and comments to Max Vorobiev &lt;<i>pcwizard [at] yandex.ru</i>&gt;. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the parallel port name in form, <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3) expects. It seems to be system dependent. Under Linux it&#8217;s parport0, parport1, etc.</p>
<h2>Configuration</h2>
<p>The contents of the <i>hpsj5s.conf</i> file is a list of parport names that correspond to HP ScanJet 5S scanners. Empty lines and lines starting with a hash mark (#) are ignored. Only one device name can be listed in <i>hpsj5s.conf</i> for this moment. Future versions will support daisy chain selection.</p>
<h2>Tips</h2>
<p>It seems that HP ScanJet 5S scanner uses software noise correction. This feature, along with gamma correction and calibration, are not implemented for now. They will be handled in future versions. Native resolution for this scanner is 300 DPI. Other modes may present aliasing artifacts.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/hpsj5s.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hpsj5s.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hpsj5s.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_HPSJ5S</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3)<br />
 <i><a rel="nofollow" href="http://hpsj5s.sourceforge.net">http://hpsj5s.sourceforge.net</a></i><br />
 <i><a rel="nofollow" href="http://cyberelk.net/tim/libieee1284">http://cyberelk.net/tim/libieee1284</a></i></p>
<h2>Author</h2>
<p>Max Vorobiev<br />
 Man page mostly based on <i>canon.man</i>.</p>
