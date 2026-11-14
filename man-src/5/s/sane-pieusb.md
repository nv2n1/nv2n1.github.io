---
title: "sane-pieusb(5)"
name: "sane-pieusb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-pieusb/"
description: "sane-pieusb – SANE backend for USB-connected PIE PowerSlide and Reflecta DigitDia/CrystalScan/ProScan slide scanners"
---

<p>sane-pieusb &#8211; SANE backend for USB-connected PIE PowerSlide and Reflecta DigitDia/CrystalScan/ProScan slide scanners</p>
<h2>Description</h2>
<p>The <code>sane-pieusb</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to USB-connected PIE and Reflecta slide scanners.<br />
 At present, the following scanners should work with this backend: </p>
<pre>Model: Status
------------------------- ------
PIE PowerSlide 3600 Untested
PIE PowerSlide 3650 Untested
PIE PowerSlide 4000 Untested
PIE PowerSlide 5000 Untested
Reflecta CrystalScan 7200 Untested
Reflecta ProScan 4000 Untested
Reflecta ProScan 7200 Untested
Reflecta DigitDia 3600 Untested
Reflecta DigitDia 4000 Untested
Reflecta DigitDia 5000 Untested
Reflecta DigitDia 6000 Ok</pre>
<h2>Multiple Slides</h2>
<p>Support for multiple slide scanners (like the PowerSlide or DigitDia series) is done by auto-advancing (&#8216;Advance slide&#8217; setting) the slide after each scan. </p>
<p> However, for best results, it is recommended to do a preview for every slide since this sets gamma, brightness, and contrast to optimal values. </p>
<p> Attention: SANE does not have an automatic landscape/portrait detection and re-orientation when scanning multiple slides. You have to put all slides into one orientation first !</p>
<h2>Dirt Removal</h2>
<p>If available, <code>sane-pieusb</code> supports infrared scans for dirt detection and removal. This must be enabled via the &#8216;Clean image&#8217; setting.</p>
<h2>Known Problems</h2>
<p>The <code>sane-pieusb</code> backend supports dirt removal based on infrared scan information. Since SANE does not provide post-processing in the backend, <code>sane-pieusb</code> does the scanning and dirt removal during the setup phase. The &#8216;scan&#8217; phase is only used to transfer the completed image. Therefore <code>sane-pieusb</code> does not multi-thread making a typical frontend appear as &#8216;blocked&#8217;. Also cancel requests are only honored between scans.</p>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_PIEUSB</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<dl>
<dd>
<pre>level debug output
------- ------------------------------
 0 nothing
 1 errors
 2 warnings &amp; minor errors
 5 additional information
 7 SANE api calls
 9 backend functions
11 scanner functions
13 usb functions
15 image buffer functions</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/pieusb.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pieusb.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pieusb.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Contact And Bug-Reports</h2>
<p>Please send any information and bug-reports to:<br />
 Klaus Kämpf &lt;<i>kkaempf [at] suse.com</i>&gt;</p>
<h2>Authors</h2>
<p>The pieusb backend is based on work by Jan Vleeshouwers, Michael Rickmann, and Klaus Kämpf</p>
