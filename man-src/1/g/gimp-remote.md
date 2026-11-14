---
title: "gimp-remote(1)"
name: "gimp-remote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gimp-remote/"
description: "gimp-remote – tells a running GIMP to open a (local or remote) image file."
---

<h2 class="name">NAME</h2>
<p> gimp-remote &#8211; tells a running GIMP to open a (local or remote) image file. </p>
<h2>SYNOPSIS</h2>
<p> <code>gimp-remote</code> [-h] [&#8211;help] [-v] [&#8211;version] [&#8211;display <i>display</i>] [-e] [&#8211;existing] [-q] [&#8211;query] [-s] [&#8211;no-splash] [-p] [&#8211;print-xid] <i>filename</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>gimp-remote</i> is a small utility that tells a running GIMP to open one or more (local or remote) image files. It does so by searching for a GIMP toolbox on the active display. If it can find a GIMP toolbox, a synthetic drop event is created which makes GIMP think the files would have been dropped onto the toolbox. More than one filename or URL can be specified on the commandline. </p>
<p> If no GIMP window is found, <i>gimp-remote</i> will start a new GIMP instance and ask it to load the specified images. If no filename or URL is given, <i>gimp-remote</i> will start a new GIMP. This behaviour can be altered using the command-line options described below. </p>
<p> If you are using GIMP on Linux or another platform with the D-Bus message bus system, chances are good that this functionality is already built into the main GIMP executable and that you will not need to use <i>gimp-remote</i>. </p>
<h2>OPTIONS</h2>
<p> <i>gimp-remote</i> accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a list of all commandline options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Output the version info.</p>
<dt><code>&#8211;display </code><i>display</i></p>
<dd> Use the designated X display.</p>
<dt><code>-e, &#8211;existing</code></p>
<dd> If no running GIMP instance is found, don&#8217;t start a new one but exit.</p>
<dt><code>-q, &#8211;query</code></p>
<dd> Check if GIMP is running and exit. A status code of 0 indicates that a GIMP toolbox window has been found on this display.</p>
<dt><code>-p, &#8211;print-xid</code></p>
<dd> Like -q, but print the X Window ID of the toolbox window if GIMP is already running. If no such window exists nothing is printed.</p>
<dt><code>-s, &#8211;no-splash</code></p>
<dd> When starting GIMP, do not show the splash screen. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gimp-remote&nbsp;<wbr><a rel="nofollow" href="http://www.gimp.org/images/wilber_the_gimp.png">http://www.gimp.org/images/wilber_the_gimp.png</a></code></p>
<dd> Loads the image from the GIMP website into a running GIMP or starts a new one.</p>
<dt><code>gimp-remote wilber.xcf wilma.xcf</code></p>
<dd> Loads the local files wilber.xcf and wilma.xcf into a running GIMP or starts a new one. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number. </p>
</dl>
<h2>AUTHORS</h2>
<p> Sven Neumann and Simon Budig. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), <code><a href="/docs/linux/man/5-gimprc/">gimprc</a></code>(5), <code><a href="/docs/linux/man/1-gimptool/">gimptool</a></code>(1) </p>
<h2>Index</h2>
