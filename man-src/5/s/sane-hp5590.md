---
title: "sane-hp5590(5)"
name: "sane-hp5590"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hp5590/"
description: "sane-hp5590 – SANE backend for Hewlett-Packard 4500C/4570C/5500C/5550C/5590/7650 Workgroup/Document scanners"
---

<p>sane-hp5590 &#8211; SANE backend for Hewlett-Packard 4500C/4570C/5500C/5550C/5590/7650 Workgroup/Document scanners</p>
<h2>Description</h2>
<p>The <code>sane-hp5590</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Hewlett-Packard Workgroup/Document scanners:</p>
<dl>
<dt>&bull;</p>
<dd>ScanJet 4500C</p>
<dt>&bull;</p>
<dd>ScanJet 4570C</p>
<dt>&bull;</p>
<dd>ScanJet 5500C</p>
<dt>&bull;</p>
<dd>ScanJet 5550C</p>
<dt>&bull;</p>
<dd>ScanJet 5590</p>
<dt>&bull;</p>
<dd>ScanJet 7650</dl>
<p> If you own a scanner other than the ones listed above that works with this backend, please let us know this by sending the scanner&#8217;s exact model name and the USB vendor and device ids (e.g. from <i>/sys/bus/usb/devices</i>, <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) or syslog) to us. Even if the scanner&#8217;s name is only slightly different from the models mentioned above, please let us know.</p>
<h2>Options</h2>
<p>The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). Valid command line options and their syntax can be listed by using:</p>
<dl>
<dd>
<pre>scanimage --help -d hp5590:interface:device</pre>
</dl>
<p> where interface and device specify the device in question, as in the configuration file. Add <code>&#8211;all-options</code> to also list the hardware read-out options. The <code>-d</code> parameter and its argument can be omitted to obtain information on the first scanner identified. </p>
<p> Use the command:</p>
<dl>
<dd>
<pre>scanimage -L</pre>
</dl>
<p> to list all devices recognized by your SANE installation.</p>
<h2>Device Specific Options</h2>
<dl>
<dt><code>-l </code>n</p>
<dd>Top-left X position of scan area in mm. Allowed range: 0 .. 215.889.</p>
<dt><code>-t </code>n</p>
<dd>Top-left Y position of scan area in mm. Allowed range: 0 .. 297.699.</p>
<dt><code>-x </code>n</p>
<dd>X width of scan-area in mm. Allowed range: 0 .. 215.889.</p>
<dt><code>-y </code>n</p>
<dd>Y height of scan-area in mm. Allowed range: 0 .. 297.699.</dl>
<p> By default, the maximum size will be scanned.</p>
<dl>
<dt><code>&#8211;mode </code>mode</p>
<dd>Select color mode. mode must be one of: &#8220;Color&#8221;, &#8220;Color (48 bits)&#8221;, &#8220;Gray&#8221;, &#8220;Lineart&#8221;.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>&#8220;Color&#8221; &#8211; Scanning is done with 3 * 8 bit RGB color values per pixel.</p>
<dt>&bull;</p>
<dd>&#8220;Color (48 bits)&#8221; &#8211; Scanning is done with 3 * 16 bit RGB color values per pixel.</p>
<dt>&bull;</p>
<dd>&#8220;Gray&#8221; &#8211; Scanning is done with 1 * 8 bit gray value per pixel.</p>
<dt>&bull;</p>
<dd>&#8220;Lineart&#8221; &#8211; Scanning is done with 1 bit black and white value per pixel.</dl>
</dl>
<dt><code>&#8211;source </code>source</p>
<dd>Select the source for scanning. source must be one of: &#8220;Flatbed&#8221;, &#8220;ADF&#8221;, &#8220;ADF Duplex&#8221;, &#8220;TMA Slides&#8221;, &#8220;TMA Negatives&#8221;.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>&#8220;Flatbed&#8221; &#8211; Scan document on the flat document glass.</p>
<dt>&bull;</p>
<dd>&#8220;ADF&#8221; &#8211; Scan frontsides of documents with automatic document feeder.</p>
<dt>&bull;</p>
<dd>&#8220;ADF Duplex&#8221; &#8211; Scan front- and backsides of documents with automatic document feeder. Note, the backside images must be rotated in a separate post process step.</p>
<dt>&bull;</p>
<dd>&#8220;TMA Slides&#8221; &#8211; Slide scanning with transparent media adapter. (Not fully supported by hp5590 backend).</p>
<dt>&bull;</p>
<dd>&#8220;TMA Negatives&#8221; &#8211; Negative film scanning with transparent media adapter. (Not fully supported by hp5590 backend).</dl>
</dl>
<dt><code>&#8211;resolution </code>res</p>
<dd>Set the resolution of the scanned image in dpi. res must be one of: 100, 200, 300, 600, 1200, 2400.</dl>
<p> Default settings: Lineart, Flatbed, 100dpi.</p>
<dl>
<dt><code>&#8211;extend-lamp-timeout[=yes|no]</code></p>
<dd>Extend lamp timeout period. no = 15 minutes, yes = 1 hour. (Default: no)</p>
<dt><code>&#8211;wait-for-button[=yes|no]</code></p>
<dd>Wait for button press before scanning starts. (Default: no)</p>
<dt><code>&#8211;preview[=yes|no]</code></p>
<dd>Request a preview-quality scan. (Default: no)</p>
<dt><code>&#8211;hide-eop-pixel[=yes|no]</code></p>
<dd>Hide end-of-page indicator pixels and overwrite with color of next neighbor pixels. (Default: yes)<br />
 The scanner uses the last pixel in every scan line for storing the end-of-page status. This is needed to detect the end of the document sheet when the automatic document feeder (ADF) is used. Unfortunately the end-of-page pixels are also generated in flatbed scans. It is recommended to hide these pixels.</p>
<dt><code>&#8211;trailing-lines-mode </code>mode</p>
<dd>Filling mode of trailing lines after end of page when automatic document feeder (ADF) is used. mode must be one of: &#8220;last&#8221;, &#8220;raw&#8221;, &#8220;raster&#8221;, &#8220;white&#8221;, &#8220;black&#8221;, &#8220;color&#8221;. (Default: &#8220;last&#8221;)</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>&#8220;last&#8221; = repeat the last scan line (recommended),</p>
<dt>&bull;</p>
<dd>&#8220;raw&#8221; = read raw scan data (not recommended),</p>
<dt>&bull;</p>
<dd>&#8220;raster&#8221; = generate black and white pixel pattern,</p>
<dt>&bull;</p>
<dd>&#8220;white&#8221; = white pixels,</p>
<dt>&bull;</p>
<dd>&#8220;black&#8221; = black pixels,</p>
<dt>&bull;</p>
<dd>&#8220;color&#8221; = RGB or gray colored pixels (see next option).</dl>
</dl>
<dt><code>&#8211;trailing-lines-color </code>n</p>
<dd>Set color value for filling trailing scan lines in trailing lines mode &#8220;color&#8221; (see previous option). (Default color: violet)<br />
 The RGB color value must be specified and calculated as 65536 * r + 256 * g + b, with r, g, b being values in the range of 0 .. 255.</dl>
<h2>Read Out Options</h2>
<p>The following options allow reading out the button state, counter value, color setting, and the state of document in ADF. This can be used to programmatically control corresponding scanner options like switching between flatbed and ADF mode, or triggering post processing tasks after scanning.</p>
<dl>
<dt><code>&#8211;button-pressed</code></p>
<dd>Get the id of the last button pressed. Id is one of &#8220;none&#8221;, &#8220;power&#8221;, &#8220;scan&#8221;, &#8220;collect&#8221;, &#8220;file&#8221;, &#8220;email&#8221;, &#8220;copy&#8221;, &#8220;up&#8221;, &#8220;down&#8221;, &#8220;mode&#8221;, &#8220;cancel&#8221;.<br />
 The scanner stores the id of the last button pressed until it is read. After read out, the state is reset and subsequent readings will return &#8220;none&#8221;. </p>
<dt><code>&#8211;color-led</code></p>
<dd>Get the state of the color LED indicators. The state is either &#8220;color&#8221; or &#8220;black_white&#8221;. </p>
<dt><code>&#8211;counter-value</code></p>
<dd>Get the counter value as shown on LCD. The value is in the range of 1 .. 99. </p>
<dt><code>&#8211;doc-in-adf</code></p>
<dd>Get the state of the document-available indicator of the automatic document feeder (ADF). The state is either &#8220;yes&#8221; or &#8220;no&#8221;. </p>
</dl>
<h2>Hints For Users Of Scanbd</h2>
<p><code><a href="/docs/linux/man/8-scanbd/">scanbd</a></code>(8) is a scanner button daemon, which can read scanner buttons and trigger scan actions. </p>
<p> Do not use the old <code><a href="/docs/linux/man/8-scanbuttond/">scanbuttond</a></code>(8) interface with hp5590. It is outdated and shall not be used any more. The regular interface of <code><a href="/docs/linux/man/8-scanbd/">scanbd</a></code>(8) is fully supported by the current version of the hp5590 backend. </p>
<p> This example shows a minimum configuration file and the corresponding script file for <code><a href="/docs/linux/man/8-scanbd/">scanbd</a></code>(8) to be included in <i>scanbd.conf</i>.</p>
<dl>
<dt>&bull;</p>
<dd><i>hp5590.conf</i></p>
<dd>
<pre>device hp5590 {
 # Device matching
 filter = &quot;hahp5590.*&quot;
 desc = &quot;HP5590 Scanner Family&quot;
 # Read out counter value and store in environment variable.
 function function_lcd_counter {
 filter = &quot;hacounter-value.*&quot;
 desc = &quot;hp5590: LCD counter&quot;
 env = &quot;SCANBD_FUNCTION_LCD_COUNTER&quot;
 }
 # Run scan script when button is pressed.
 action do-scan {
 filter = &quot;habutton-pressed.*&quot;
 desc = &quot;hp5590: Scan button pressed&quot;
 script = &quot;scan_action.script&quot;
 string-trigger {
 from-value = &quot;none&quot;
 to-value = &quot;scan&quot;
 }
 }
}</pre>
<dt>&bull;</p>
<dd>scan_action.script</p>
<dd>
<pre>#!/bin/bash
echo device = $SCANBD_DEVICE
echo action = $SCANBD_ACTION
echo counter = $SCANBD_FUNCTION_LCD_COUNTER
scanfile=&quot;$HOME/tmp/scans/scan-$(date +%s).pnm&quot;
case $SCANBD_ACTION in
do-scan)
 scanimage -d &quot;$SCANBD_DEVICE&quot; &gt; &quot;$scanfile&quot;
 ;;
*)
 echo Warning: Unknown scanbd action: &quot;$SCANBD_ACTION&quot;
 ;;
esac</pre>
</dl>
<h2>Files</h2>
<dl>
<dt>@LIBDIR@/libsane-hp5590.a</p>
<dd>The static library implementing this backend.</p>
<dt>@LIBDIR@/libsane-hp5590.so</p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<p>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. </p>
<p> SANE_DEBUG_HP5590 </p>
<p> Higher debug levels increase the verbosity of the output:</p>
<dl>
<dd>
<pre>10 - generic processing
20 - verbose backend messages
40 - HP5590 high-level commands
50 - HP5590 low-level (USB-in-USB) commands</pre>
<dt><code>Example:</code></p>
<dd>export SANE_DEBUG_HP5590=50</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) <code><a href="/docs/linux/man/8-scanbd/">scanbd</a></code>(8), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Authors</h2>
<p>Ilia Sotnikov &lt;<i>hostcc [at] gmail.com</i>&gt;.</p>
