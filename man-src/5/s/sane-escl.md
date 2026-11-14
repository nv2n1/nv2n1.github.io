---
title: "sane-escl(5)"
name: "sane-escl"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-escl/"
description: "sane-escl – SANE backend for eSCL scanners"
---

<p>sane-escl &#8211; SANE backend for eSCL scanners</p>
<h2>Description</h2>
<p>The <code>sane-escl</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to eSCL protocol scanners. Currently, the following models work with this backend (This list is not exhaustive):</p>
<dl>
<dd>BROTHER DCP-J772DW, DCP-L2530DW<br />
 BROTHER HL-L2590DW<br />
 CANON IR C3520<br />
 CANON PIXMA MG5765<br />
 CANON PIXMA G4511, G7050<br />
 CANON PIXMA TR4520, TR4540, TR4550, TR4551, TR7500, TR8500,<br />
 CANON PIXMA TR8520<br />
 CANON PIXMA TS3100, TS3150, TS3151, TS3152, TS3300, TS3350,<br />
 CANON PIXMA TS3351, TS3352, TS5350, TS5351, TS6150, TS8050,<br />
 CANON PIXMA TS9100<br />
 EPSON ET-2750, ET-3750, ET-4750<br />
 EPSON XP-6100<br />
 HP DESKJET 2710, DESKJET 2723, DESKJET 3760<br />
 HP LASERJET ENTREPRISE FLOW MFP M578,<br />
 HP LASERJET MFP M28W, LASERJET MFP M630<br />
 HP OFFICEJET 4630, OFFICEJET PRO 8610<br />
 RICOH SP3710S<br />
 XEROX VERSALINK C7220</dl>
<p> The. <code>sane-escl</code> backend for SANE supports AirScan/eSCL devices that announce themselves on mDNS as _uscan._utcp or _uscans._utcp. If the device is available, the <code>sane-escl</code> backend recovers these capacities. The user configures and starts scanning. A list of devices that use the eSCL protocol can be found at <i><a rel="nofollow" href="https://support.apple.com/en-us/HT201311">https://support.apple.com/en-us/HT201311</a></i>. While these devices are expected to work, your mileage may vary. </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/escl.conf</i></p>
<dd>The backend configuration file.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-escl.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-escl.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_ESCL</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Authors</h2>
<p>Touboul Nathane, Thierry HUCHARD</p>
