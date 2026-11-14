---
title: "scsi_report_lun_scan(9)"
name: "scsi_report_lun_scan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_report_lun_scan/"
description: "scsi_report_lun_scan – Scan using SCSI REPORT LUN results"
---

<p>scsi_report_lun_scan &#8211; Scan using SCSI REPORT LUN results</p>
<h2>Synopsis</h2>
<pre><code>int scsi_report_lun_scan(struct scsi_target *starget, int bflags, enum scsi_scan_mode rescan);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>which target</dl>
<p> <i>bflags</i></p>
<dl>
<dd>Zero or a mix of BLIST_NOLUN, BLIST_REPORTLUN2, or BLIST_NOREPORTLUN</dl>
<p> <i>rescan</i></p>
<dl>
<dd>nonzero if we can skip code only needed on first scan</dl>
<h2>Description</h2>
<p>Fast scanning for modern (SCSI-3) devices by sending a REPORT LUN command. Scan the resulting list of LUNs by calling scsi_probe_and_add_lun. </p>
<p> If BLINK_REPORTLUN2 is set, scan a target that supports more than 8 LUNs even if it&#8217;s older than SCSI-3. If BLIST_NOREPORTLUN is set, return 1 always. If BLIST_NOLUN is set, return 0 always. If starget-&gt;no_report_luns is set, return 1 always.</p>
<h2>Return</h2>
<p>0: scan completed (or no memory, so further scanning is futile) 1: could not scan with REPORT LUN</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
