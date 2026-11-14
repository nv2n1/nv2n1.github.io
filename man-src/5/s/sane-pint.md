---
title: "sane-pint(5)"
name: "sane-pint"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-pint/"
description: "sane-pint – SANE backend for scanners that use the PINT device driver"
---

<p>sane-pint &#8211; SANE backend for scanners that use the PINT device driver</p>
<h2>Description</h2>
<p>The <code>sane-pint</code> library implements a SANE (Scanner Access Now Easy) backend that provides generic access to hand-held and flatbed scanners using the PINT (PINT Is Not Twain) device driver. The PINT driver is being actively developed on the OpenBSD platform, and has been ported to a few other *nix-like operating systems. PINT is designed to provide an <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) interface to many different scanner types. However, this backend has only been tested with flatbed single-pass scanners, and more work will probably be required to get it to use other scanner types successfully. If have successfully used the PINT driver with your scanner, but it does not work using this SANE backend, please let us know. To do this, send a mail with the relevant information for your scanner to <i>sane-devel [at] alioth-lists.debian.net</i>. Have a look at <a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a> concerning subscription to sane-devel. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the scanner. The special device name must be a PINT device or a symlink to such a device. For example, under NetBSD or OpenBSD, such a device name could be <i>/dev/ss0</i> or <i>/dev/scan0</i>.</p>
<h2>Configuration</h2>
<p>The contents of the <i>pint.conf</i>. file is a list of device names that correspond to PINT scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/scanner<br />
 # this is a comment<br />
 /dev/ss1</dl>
<h2>Files</h2>
<dl>
<dt><i>@CONFIGDIR@/pint.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>@LIBDIR@/libsane-pint.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>@LIBDIR@/libsane-pint.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. Under UNIX, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in @CONFIGDIR@. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories &quot;tmp/config&quot;, &quot;.&quot;, and &quot;@CONFIGDIR@&quot; being searched (in this order).</p>
<dt><code>SANE_DEBUG_PINT</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-sane/">sane</a>(7)</p>
<h2>Author</h2>
<p>Gordon Matzigkeit, adapted from existing backends written by David Mosberger.</p>
<h2>Bugs</h2>
<p>There are minor roundoff errors when adjusting the ranges, since PINT uses units of 1/1200 of an inch, and SANE normally uses millimeters. Symptoms of these errors are skewed images. This should really be fixed (no pun intended) as soon as possible, but I just don&#8217;t know/care enough about fixed-point representation and roundoff errors to do this correctly. Workaround: use inches as the scanning unit, and everything usually works fine. The PINT 0.5e interface does not provide a way to determine valid ranges for DPI, modes, and scan sizes. So, the SANE backend queries the PINT device, and dynamically discovers valid ranges by doing a binary search. This means that the driver takes longer to initialize than seems necessary. Resetting the scanner does not seem to work (at least not on my HP ScanJet 4p). For that reason, the driver sends a SCIOCRESTART, then gobbles up any remaining input until it hits EOF. Not all of the scanners have been identified (i.e. whether they are flatbed or handheld). X and Y resolutions are assumed to be the same. No testing has been done on three-pass or handheld scanners, or with Automatic Document Feeder support. </p>
