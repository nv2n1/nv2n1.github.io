---
title: "sane-gphoto2(5)"
name: "sane-gphoto2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-gphoto2/"
description: "sane-gphoto2 – SANE backend for gphoto2 supported cameras"
---

<p>sane-gphoto2 &#8211; SANE backend for gphoto2 supported cameras</p>
<h2>Description</h2>
<p>The <code>sane-gphoto2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the digital cameras supported by gphoto2. This backend has only been tested with a handful of cameras so far. Patches to support other models are welcome. </p>
<p> Because of the limited testing of this backend, it is commented out in <i>/etc/sane.d/dll.conf</i> by default. Either the comment character must be removed or the backend must be called explicitly. E.g. <i>scanimage -d gphoto2</i> or <i>xscanimage gphoto2</i>.</p>
<h2>Device Names</h2>
<p>The current version of the backend only allows one camera to be connected. The device name is always &quot;0&quot;.</p>
<h2>Configuration</h2>
<p>The contents of the <i>gphoto2.conf</i> specify the characteristics of the camera to be used. Resolutions (high resolution, low resolution, and thumbnail size) are required since they are needed by the sane frontends, but can&#8217;t be obtained through the gphoto2 interface. Valid ports and cameras can be obtained by <i>gphoto2 &#8211;list-cameras</i> and <i>gphoto2 &#8211;list-ports.</i> </p>
<p> The <code>dumpinquiry</code> line causes some information about the camera to be printed. </p>
<p> Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<p> The <code>topfolder</code> line specifies the &quot;fixed&quot; part of the file path. For example, on the Kodak DC-240, files are stored in the directory <i>/DCIM/100DC240.</i> The <i>/DCIM</i> portion is constant, but 100DC240 will change and must be read from the camera. In this case, the line would read &quot;topfolder=/DCIM&quot; </p>
<p> Some cameras don&#8217;t implement a file structure and store all pictures in the <i>/</i> directory. This is indicated by setting &quot;subdirs=0&quot; with &quot;topfolder=/&quot; </p>
<dl>
<dd>port=usb:<br />
 camera=Kodak DC240<br />
 # this is a comment<br />
 high_resolution=1280&#215;960<br />
 low_resolution=640&#215;480<br />
 thumb_resolution=160&#215;120<br />
 dumpinquiry</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/gphoto2.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-gphoto2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-gphoto2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (<i>.</i>) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_GPHOTO2</code></p>
<dd>If the library was compiled with debugging support enabled, this environment variable controls the debug level for this backend. A value of 128 requests maximally copious debug output; smaller levels reduce verbosity.</p>
<dt><code>GP_DEBUG</code></p>
<dd>Set to 1, 2, or 3, to enable various levels of debugging within the gphoto2 libraries. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7)<code>,</code> <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/3-libgphoto2/">libgphoto2</a></code>(3) </p>
<h2>Author</h2>
<p>Peter S. Fales </p>
<p> The manpage was largely copied from the <code><a href="/docs/linux/man/5-sane-dc210/">sane-dc210</a></code>(5) manpage.</p>
<h2>Bugs</h2>
<p>Many, no doubt. More general comments, suggestions, and inquiries about frontends or SANE should go to the SANE Developers mailing list (see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details). You must be subscribed to the list, otherwise your mail won&#8217;t be sent to the subscribers. </p>
