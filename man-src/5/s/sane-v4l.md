---
title: "sane-v4l(5)"
name: "sane-v4l"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-v4l/"
description: "sane-v4l – SANE interface for Video for Linux API"
---

<p>sane-v4l &#8211; SANE interface for Video for Linux API</p>
<h2>Description</h2>
<p>The <code>sane-v4l</code> library implements a SANE (Scanner Access Now Easy) backend that provides generic access to video cameras and similar equipment using the V4L (Video for Linux) API. This is ALPHA software. Really! Important features are missing and there are lots of bugs. The code is currently only tested on a Linux 2.4 system with a Hauppauge WinTV video card. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the UNIX path-name for the special device that corresponds to the v4l device. The special device name must be a v4l device or a symlink to such a device. For example, such a device name could be <i>/dev/video0</i> or <i>/dev/bttv0</i>.</p>
<h2>Configuration</h2>
<p>The contents of the <i>v4l.conf</i> file is a list of device names that correspond to v4l devices. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/bttv0<br />
 # this is a comment<br />
 /dev/video3</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/v4l.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib64/sane/libsane-v4l.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib64/sane/libsane-v4l.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. Under UNIX, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in /etc/sane.d. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories &quot;tmp/config&quot;, &quot;.&quot;, and &quot;/etc/sane.d&quot; being searched (in this order).</p>
<dt><code>SANE_DEBUG_V4L</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity.</dl>
<h2>Author</h2>
<p>Juergen G. Schimmer, Henning Meier-Geinitz</p>
<h2>Bugs:</h2>
<p>If more than one video card is present, a crash may occur. Frequency and geometry selection is missing.<br />
 Send bug reports to the SANE mailing list: sane-devel [at] lists.alioth.debian.org. You must be subscribed to the list to send mail. See <a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a> for details.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-sane/">sane</a>(7), <a href="/docs/linux/man/1-xcam/">xcam</a>(1). </p>
