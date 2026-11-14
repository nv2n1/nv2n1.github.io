---
title: "ift-extract(1)"
name: "ift-extract"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ift-extract/"
description: "ift-extract.info – ift-extract.info"
---

<h2>NAME</h2>
<p> ift-extract.info &#8211; ift-extract.info</p>
<h2>Built-in iSight firmware extractor and patcher</h2>
<p> ift-extract extract the Built-in iSight firmware from Apple driver and patch it to avoid some bugs in it. The firmware is then ready to get loaded into the chip using ift-load. </p>
<p> * Menu: </p>
<p> Finding the Apple driver: see &#8220;Driver&#8221; </p>
<p> Command line options: see &#8220;Options&#8221; </p>
<p> See also &#8220;Copying&#8221;</p>
<h2>1 Finding the Apple driver</h2>
<p> ift-extract extract Built-in iSight firmware from Apple iSight driver. This driver is located at /System/Library/Extensions/IOUSBFamily.kext/Contents/PlugIns/AppleUSBVideoSupport.kext/Contents/MacOS/AppleUSBVideoSupport on your Mac <font SIZE="-1">OS</font> X root partition. </p>
<p> There is several version of this driver depending on driver version or host architecture (PowerPC or x86). Thus, ift-extract must determine know the variant of the driver in order to properly extract the firmware. </p>
<p> Any AppleUSBVideoSupport file starting with those shipped with iMac G5 iSight must work. If not, please report unknown AppleUSBVideoSupport at bugreport mail address with machine type and <font SIZE="-1">OS</font> X version.</p>
<h2>2 Command line options</h2>
<p> `<code>-a</code>&#8216; `<code>&#8211;apple-driver</code>&#8216; Apple driver filename where to extract the firmware. </p>
<p> `<code>-d</code>&#8216; `<code>&#8211;output-directory</code>&#8216; The directory where to output the firmware. Defaults to /lib/firmware. </p>
<p> `<code>-f</code>&#8216; `<code>&#8211;output-filename</code>&#8216; The output firmware name. Defaults to isight.fw </p>
<p> `<code>-?</code>&#8216; `<code>&#8211;help</code>&#8216; Shows option help and quit. </p>
<p> Since ift-extract defaults to output the firmware to /lib/firmware/isight.fw, ensure you have the right to do so.</p>
<h2>3 Copying</h2>
<p> isight-firmware-tools is a project developped by Étienne Bersac based on the work of Ronald S. Bultje, Johannes Berg and Ivan N. Zlatev. </p>
<p> This manual has been written by Étienne Bersac. </p>
<p> Copyright (C) 2007 Étienne Bersac &lt;bersace [at] gmail.com&gt; </p>
<h2>Index</h2>
