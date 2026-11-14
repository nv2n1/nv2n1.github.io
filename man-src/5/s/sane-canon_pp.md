---
title: "sane-canon_pp(5)"
name: "sane-canon_pp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-canon_pp/"
description: "sane-canon_pp – SANE backend for Canon CanoScan Parallel Port flatbed scanners"
---

<p>sane-canon_pp &#8211; SANE backend for Canon CanoScan Parallel Port flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-canon_pp</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Canon flatbed scanners:</p>
<dl>
<dd>CanoScan FB320P<br />
 CanoScan FB620P<br />
 CanoScan FB330P<br />
 CanoScan FB630P<br />
 CanoScan N340P<br />
 CanoScan N640P<br />
 CanoScan N640P ex
</dl>
<p> No USB scanners are supported and there are no plans to support them in the future. Other projects are working on support for USB scanners. See the <i>PROJECTS</i> file for more detail. The FB310P and FB610P are re-badged Avision scanners which use a different command set, so are unlikely to be supported by this backend in the future. IMPORTANT: this is alpha code. While we have made every effort to make it as reliable as possible, it will not always work as expected. Feedback is still appreciated. Please send any bug reports to the maintainers as listed on the web page (listed in <code>SEE ALSO</code> below). </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form presented by <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3). These names are highly dependent on operating system and version. </p>
<p> On Linux 2.4 kernels this will be of the form <i>parport0</i> or older (2.2 and before) kernels may produce names like <i>0x378</i> (the base address of your port) or simply <i>0</i> depending on your module configuration. Check the contents of <i>/proc/parport</i> if it exists. If you don&#8217;t want to specify a default port (or don&#8217;t know its name), the backend should be able to detect which port your scanner is on.</p>
<h2>Configuration</h2>
<p>The contents of the <i>canon_pp.conf</i> file is a list of options for the driver to use. Empty lines and lines starting with a hash mark (#) are ignored. </p>
<p> The supported options are currently <code>ieee1284</code>, <code>calibrate</code>, <code>init_mode</code>, and <code>force_nibble</code> </p>
<p> Option <code>ieee1284</code> <i>port-name</i> defines which port to use. The format of port-name is OS dependent, based on the names presented by libieee1284. Please only have one of these lines, or all but one will be ignored. </p>
<p> Option <code>calibrate</code> <i>cal-file</i> <i>[port-name]</i> defines which calibration file to use on a per-port basis. If you only have one parport, the port-name argument may be omitted &#8211; but be careful as this will cause problems on multi-scanner systems. You may have as many of these lines as you like, as long as each has a unique port name. The tilde (`~&#8217;) character is acceptable and will be expanded to the value of the HOME environment. </p>
<p> Option <code>init_mode</code> <i>&lt;AUTO|FB620P|FB630P&gt;</i> <i>[portname]</i> defines which initialisation (wake-up) mode to use on a per-port basis. If you only have one parport, the portname argument may be omitted &#8211; but be careful as this may cause problems on multi-scanner systems. You may have as many of these lines as you like, as long as each has a unique port name. The valid initialisation modes are FB620P (which strobes 10101010 and 01010101 on the data pins), FB630P (which strobes 11001100 and 00110011 on the data pins) and AUTO, which will try FB630P mode first then FB620P mode second. The FB620P mode is also used by the FB320P. The FB630P mode is used by the FB330P, N340P, and N640P. </p>
<p> Option <code>force_nibble</code> forces the driver to use nibble mode even if ECP mode is reported to work by libieee1284. This works-around the rare issue of ECP mode being reported to work by the library, then not working.</p>
<h2>Tips</h2>
<p>Hit the &quot;Calibrate&quot; button before scanning. It vastly improves the quality of scans. </p>
<p> To enable automatic detection of your scanner, uncomment the &quot;canon_pp&quot; line from <i>/etc/sane.d/dll.conf</i></p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/canon_pp.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon_pp.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-canon_pp.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_CANON_PP</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_CANON_PP=4</dl>
<h2>Notes</h2>
<p><code>Features available in the Windows interface</code></p>
<dl>
<dt><code>Brightness and Contrast</code></p>
<dd>These are not implemented, and probably never will be. These appear to be implemented entirely in software. Use GIMP or a similar program if you need these features.</p>
<dt><code>Descreen Mode</code></p>
<dd>This appears on our first analysis to be just oversampling with an anti-aliasing filter. Again, it seems to be implemented entirely in software, so GIMP is your best bet for now.</p>
<dt><code>Gamma Tables</code></p>
<dd>This is under investigation, but for now only a simple gamma profile (ie: the one returned during calibration) will be loaded.</dl>
<p> <code>Communication Problems</code> ECP mode in libieee1284 doesn&#8217;t always work properly, even with new hardware. We believe that this is a ppdev problem. If you change the configuration file to include <code>force_nibble</code> , the problem will go away, but you will only be able to scan in nibble mode. Sometimes the scanner can be left in a state where our code cannot revive it. If the backend reports no scanner present, try unplugging the power and plugging it back in. Also try unplugging printers from the pass-through port. The scanner will not respond correctly to our commands when you first plug in the power. You may find if you try a scan very soon after plugging in the power that the backend will incorrectly report that you have no scanner present. To avoid this, give it about 10 seconds to reset itself before attempting any scans. <code>Repeated Lines</code> Sometimes at high resolutions (ie. 600dpi) you will notice lines which appear twice. These lines correspond to points where the scanner head has stopped during the scan (it stops every time the internal 64kb buffer is full). Basically it&#8217;s a mechanical problem inside the scanner, that the tolerance of movement for a start/stop event is greater than 1/600 inches. I&#8217;ve never tried the windows driver so I&#8217;m not sure how (or if) it works around this problem, but as we don&#8217;t know how to rewind the scanner head to do these bits again, there&#8217;s currently no nice way to deal with the problem. <code>Grey-scale Scans</code> Be aware that the scanner uses the green LEDs to read grey-scale scans, meaning green coloured things will appear lighter than normal, and red and blue coloured items will appear darker than normal. For high-accuracy grey-scale scans of colour items, it&#8217;s best just to scan in colour and convert to grey-scale in graphics software such as the GIMP. <code>FB620P/FB320P Caveats</code> These models can not be reset in the same way as the others. The windows driver doesn&#8217;t know how to reset them either &#8211; when left with an inconsistent scanner, it will start scanning half way down the page! Aborting is known to work correctly on the FB*30P models, and is known to be broken on the FB*20P models. The FB620P which I tested on simply returns garbage after a scan has been aborted using the method we know. Aborting is able to leave the scanner in a state where it can be shut down, but not where another scan can be made. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a>(5),</code> <code><a href="/docs/linux/man/3-libieee1284/">libieee1284</a></code>(3),<br />
 <i><a rel="nofollow" href="http://canon-fb330p.sourceforge.net/">http://canon-fb330p.sourceforge.net/</a></i> </p>
<h2>Author</h2>
<p>This backend is primarily the work of Simon Krix (Reverse Engineering), and Matthew Duggan (SANE interface). </p>
<p> Many thanks to Kevin Easton for his comments and help, and Kent A. Signorini for his help with the N340P.</p>
