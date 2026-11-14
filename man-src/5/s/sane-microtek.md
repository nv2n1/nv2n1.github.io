---
title: "sane-microtek(5)"
name: "sane-microtek"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-microtek/"
description: "sane-microtek – SANE backend for Microtek scanners"
---

<p>sane-microtek &#8211; SANE backend for Microtek scanners</p>
<h2>Description</h2>
<p>The <code>sane-microtek</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the &quot;second generation&quot; Microtek scanners. At present, the following hardware is known to work with this backend:</p>
<dl>
<dd>Microtek ScanMaker E2, E3, E6<br />
 Microtek ScanMaker II, IIG, IIHR, IISP, III<br />
 Microtek ScanMaker 35t, 35t+, 45t<br />
 Microtek ScanMaker 600GS, 600ZS (see bug notes)<br />
 Agfa StudioScan<br />
 Agfa StudioScan II, StudioScan IIsi<br />
 Agfa Arcus II (but not the &quot;Arcus&quot;)<br />
 Agfa DuoScan (preliminary)<br />
 Vobis &quot;Highscreen Realscan&quot;<br />
 Microtek Color PageWiz (preliminary)<br />
 Transparent Media Adapter<br />
 Document AutoFeeder
</dl>
<p> The driver supports line art, halftone, 8bpp gray, and 24bpp color scans at normal and &quot;expanded&quot; resolutions (i.e. 1200&#215;1200 on an E6), fast scans for color previews, and downloadable gamma tables. The supported scanners are all SCSI scanners. However, some parallel port models may work (under Linux), if they use a parport-&gt;scsi chip, and if you can find a scsi-&gt;parport driver. This is known to be the case for the Color PageWiz. The driver does <code>not</code> support the newest Microtek scanners, such as the V330 and V660, which use a new and very different SCSI-II command set. For those, try the alternate <code><a href="/docs/linux/man/5-microtek2/">microtek2</a></code>(5) backend. Most non-SCSI scanners would use the new command set. Most scanners newer than the Scanmaker E6 would use the new command set. If you own a Microtek scanner other than the ones listed above, tell us what happens &#8212; see the <code>BUGS</code> section at the end of this document. Although this manual page is generally updated with each release, up-to-date information on new releases and extraneous helpful hints are available from the backend homepage: </p>
<dl>
<dd><i><a rel="nofollow" href="http://www.mir.com/mtek/">http://www.mir.com/mtek/</a></i></dl>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the scanner. The special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example.</p>
<h2>Configuration</h2>
<p>The contents of the <i>microtek.conf</i> file is a list of device names that correspond to Microtek scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/scanner<br />
 # this is a comment<br />
 /dev/sge</dl>
<p> The configuration file may also contain the special tokens <i>norealcal</i> or <i>noprecal.</i> <i>norealcal</i> will disable the use of magic, undocumented scanner calibration commands which are known to work on the E6, but may not work with other models. <i>noprecal</i> will disable logic which tries to avoid scanner precalibration. This logic would only have been activated if the magic calibration code was turned off.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/microtek.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-microtek.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-microtek.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MICROTEK</code></p>
<dd>If the library was compiled with debugging support enabled, this environment variable controls the debug level for this backend. A value of 128 requests maximally copious debug output; smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5) </p>
<h2>Author</h2>
<p>Matt Marjanovic</p>
<h2>Bugs</h2>
<p>Known bugs/limitations are:</p>
<dl>
<dd>Brightness and contrast broken.<br />
 The 600GS is grayscale only, and will lock up if you select color. (Unfortunately, the 600GS and 600ZS are indistinguishable by software.)
</dl>
<p> i.e. don&#8217;t complain about these &#8212; but if brightness and/or contrast <code>do</code> work for you, please tell me. If your scanner locks up, try setting the <i>norealcal</i> or <i>noprecal</i> option in the configuration file (first one, then both), and see if it helps. (If it does, report it.) Send lengthy bug reports and new scanner information to <i>mtek-bugs [at] mir.com</i>. All bug reports and new scanner inquiries should include an error log file. You can generate copious stderr output by setting the <code>SANE_DEBUG_MICROTEK</code> environment variable described above. For example:</p>
<dl>
<dd>setenv SANE_DEBUG_MICROTEK 128</dl>
<p> More general comments, suggestions, and inquiries about frontends or SANE should go to <i>sane-devel [at] alioth-lists.debian.net</i>, the SANE Developers mailing list. Have a look at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> concerning subscription to sane-devel. </p>
