---
title: "sane-pie(5)"
name: "sane-pie"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-pie/"
description: "sane-pie – SANE backend for PIE, Devcom and AdLib SCSI flatbed scanners"
---

<p>sane-pie &#8211; SANE backend for PIE, Devcom and AdLib SCSI flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-pie</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to PIE, Devcom and AdLib SCSI flatbed scanners.<br />
 At present, the following scanners should work with this backend: </p>
<pre>Model: Status
---------------------- ------
Devcom 9636PRO OK
Devcom 9636S Untested
Devcom 9630S Untested
ScanAce 1236S Untested
ScanAce 1230S Untested
ScanAce II Untested
ScanAce III OK
ScanAce Plus Untested
ScanAce II Plus Untested
ScanAce III Plus Untested
ScanAce V Untested
ScanAce ScanMedia Untested
ScanAce ScanMedia II Untested
ScanAce 630S Untested
ScanAce 636S Untested
JetScan 630 OK
JetScan 636PRO Untested</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/pie.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pie.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pie.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Contact And Bug-Reports</h2>
<p>Please send any information and bug-reports to:<br />
 Simon Munton &lt;<i>simon [at] munton.demon.co.uk</i>&gt;</p>
