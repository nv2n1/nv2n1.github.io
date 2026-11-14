---
title: "sane-sp15c(5)"
name: "sane-sp15c"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-sp15c/"
description: "sane-sp15c – SANE backend for Fujitsu ScanPartner 15C flatbed scanner"
---

<p>sane-sp15c &#8211; SANE backend for Fujitsu ScanPartner 15C flatbed scanner</p>
<h2>Description</h2>
<p>The <code>sane-sp15c</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to the Fujitsu flatbed scanners. At present, the following scanner is known to work with these backend:</p>
<dl>
<dd>
<pre>Vendor: Model: Rev:
-------- ---------------- -----
FCPA ScanPartner 15C 1.01</pre>
</dl>
<p> The ScanPartner 15C driver supports lineart (1-bit), halftone (1-bit), grayscale (4-bit and 8-bit), and color (3 x 8-bit) scanning. Other scanners in these families may work. The ScanPartner 15C seems to be a repackaging of the ScanPartner 600C. People are encouraged to try these driver with the other scanners and to contact the author with test results. </p>
<h2>Configuration</h2>
<p>A modest effort has been made to expose the standard options to the API. This allows frontends such as <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) to set scanning region, resolution, bit-depth (and color), and enable the automatic document feeder.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-fujitsu/">sane-fujitsu</a></code>(5), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)<br />
 Fujitsu ScanPartner 15C OEM Manual, Doc. No. 250-0081-0<br />
 Fujitsu M3096G OEM Manual, part number 50FH5028E-05<br />
 Fujitsu M3096GX/M3093GX/M3093DG OEM Manual, part number C150-E015&#8230;03 </p>
<h2>Author</h2>
<p>Randolph Bentson &lt;<i>bentson [at] holmsjoen.com</i>&gt;, with credit to the unnamed author of the coolscan driver</p>
<h2>Limitations</h2>
<p>Testing limited to a Linux 2.2.5 kernel<br />
 Can&#8217;t quite get the scan page/minute performance in ADF modes. This may be due to limited system buffer size.</p>
<h2>Bugs</h2>
<p>I&#8217;m sure there are plenty, and not too well hidden, but I haven&#8217;t seen them yet.<br />
 Both scanners claim to have separate control of resolution in X and Y directions. I confess I haven&#8217;t tested this yet. I have found that <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) doesn&#8217;t even display this capability.<br />
 Threshold settings on the SP15C don&#8217;t seem to affect the results of lineart mode scans.<br />
 It might be possible to merge these two drivers without much effort since the SP15C driver was derived from the M3096G driver. They were split so as to keep the second driver development from breaking the working first driver. Watch this space for changes. </p>
