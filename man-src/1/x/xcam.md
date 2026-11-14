---
title: "xcam(1)"
name: "xcam"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcam/"
description: "xcam – a graphical camera frontend for SANE"
---

<h2 class="name">NAME</h2>
<p> xcam &#8211; a graphical camera frontend for SANE </p>
<h2>SYNOPSIS</h2>
<p> <code>xcam</code> [<code>&#8211;buffersize</code>|<code>-B</code>] [<code>&#8211;version</code>|<code>-V</code>] [<code>&#8211;help</code>|<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>xcam</code> provides a graphical user-interface to control an image acquisition device such as a flatbed scanner or a camera. It allows scanning invidual images and can be invoked directly from the command-line. </p>
<p> <code>xcam</code> acts as a stand-alone program that saves acquired images in a suitable PNM format (PBM for black-and-white images, PGM for grayscale images, and PPM for color images). </p>
<p> <code>xcam</code> accesses image acquisition devices through the SANE (Scanner Access Now Easy) interface. The list of available devices depends on installed hardware and configuration. </p>
<p> <code>xcam</code> presents a menu listing of all known and available devices. </p>
<h2>OPTIONS</h2>
<p> If the <code>&#8211;buffersize (-B)</code> option is given, <code>xcam </code> will use a 1024 kByte input buffer instead of the default 32 kByte. </p>
<p> If the <code>&#8211;version (-V)</code> option is given, <code>xcam</code> will output its version number. </p>
<p> The <code>&#8211;help (-h)</code> <code>xcam</code> flag prints a short summary of options. </p>
<dl>
<dt><code>SANE_DEBUG_XCAM</code></p>
<dd> This environment variable controls the debug level xscanimage. Higher debug levels increase the verbosity of the output. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Value&nbsp;<wbr>&nbsp;<wbr>Descsription<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print fatal errors<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print errors<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print warnings<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print information messages<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print everything </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Example:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SANE_DEBUG_XCAM=3 </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.sane/xcam/devicename.rc</i></p>
<dd> For each device, there is one rc-file that holds the saved settings for that particular device. Normally, this file should not be manipulated directly. Instead, the user should use the <code>xcam</code> interface to select appropriate values and then save the device settings using the &quot;Preferences-&gt;Save as default settings&quot; menubar entry. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-sane/">sane</a>(7), <a href="/docs/linux/man/1-xscanimage/">xscanimage</a>(1), <a href="/docs/linux/man/1-scanimage/">scanimage</a>(1), <a href="/docs/linux/man/5-sane-dll/">sane-dll</a>(5) and the backend manpages</p>
<h2>AUTHOR</h2>
<p> David Mosberger-Tang </p>
<p> Gerard Klaver (2005 update) </p>
<h2>Index</h2>
