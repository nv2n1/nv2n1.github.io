---
title: "sane-dmc(5)"
name: "sane-dmc"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-dmc/"
description: "sane-dmc – SANE backend for the Polaroid Digital Microscope Camera"
---

<p>sane-dmc &#8211; SANE backend for the Polaroid Digital Microscope Camera</p>
<h2>Description</h2>
<p>The <code>sane-dmc</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Polaroid Digital Microscope Camera.</p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the scanner. The special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example.</p>
<h2>Imaging Modes</h2>
<p>The Polaroid DMC supports a number of imaging modes. This driver supports five of the imaging modes: </p>
<dl>
<dt><code>Full Frame</code></p>
<dd>This mode corresponds to the 801-by-600 pixel full-color full-frame image.</p>
<dt><code>Viewfinder</code></p>
<dd>This mode corresponds to the 270-by-201 pixel grey-scale viewfinder image. This image is acquired very quickly.</p>
<dt><code>Raw</code></p>
<dd>This mode corresponds to the 1599-by-600 pixel &quot;raw&quot; image from the CCD. It is grey-scale, with pixels alternating horizontally between red, green and blue stripes. The pixels are twice as high as they are wide, so the image is distorted.</p>
<dt><code>Thumbnail</code></p>
<dd>This mode corresponds to the 80-by-60 pixel full-color thumbnail image.</p>
<dt><code>Super Resolution</code></p>
<dd>This image is a 1599-by-1200 pixel full-color image constructed by filtering and interpolating the &quot;raw&quot; image. The filtering and interpolation is done in software, so this mode is very slow. Also, this mode places restrictions on how the image is read which means that the &quot;preview&quot; mode of xscanimage does not work in Super Resolution mode. (<code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1) and the non-preview modes of <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) and <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) work fine, however.)</dl>
<h2>Other Settings</h2>
<dl>
<dt><code>ASA Setting</code></p>
<dd>This setting adjusts the camera&#8217;s sensitivity. You can choose one of 25, 50, or 100 &quot;equivalent&quot; ASA.</p>
<dt><code>Shutter Speed</code></p>
<dd>You can select a shutter speed from 8 to 1000 milliseconds. The shutter speed is quantized in units of 32 microseconds.</p>
<dt><code>White Balance</code></p>
<dd>You can choose one of &quot;Daylight&quot;, &quot;Incandescent&quot; or &quot;Fluorescent&quot; white balances. This setting more-or-less corresponds to the &quot;Color Temperature&quot; settings on Polaroid&#8217;s Windows and Mac software.</dl>
<h2>Configuration</h2>
<p>The contents of the <i>dmc.conf</i> file is a list of device names that correspond to DMC scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/scanner<br />
 # this is a comment<br />
 /dev/sge</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/dmc.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dmc.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-dmc.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config,</i> <i>.,</i> and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_DMC</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</dl>
<h2>Bugs</h2>
<p>In the &quot;Full Frame&quot; and &quot;Raw&quot; modes, images must be read in units of entire lines. The driver performs no buffering in these modes; if you ask sane_read to read a non-integral number of lines, it may read less than you ask for. If you ask sane_read to read less than a single line, it returns SANE_STATUS_INVAL. In the &quot;Super Resolution&quot; mode, images must be read in units of <i>two</i> lines (3198 pixels or 9594 bytes). If you try to read less than two lines, you get SANE_STATUS_INVAL. The Super Resolution mode is very slow. In the &quot;Viewfinder&quot; and &quot;Thumbnail&quot; modes, the entire image must be read in one SCSI transfer. In this case, the driver performs buffering and you can read the image in as small an increment as you like. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>David F. Skoll </p>
<p> The backend is derived from <code><a href="/docs/linux/man/5-sane-hp/">sane-hp</a></code>(5) by David Mosberger</p>
