---
title: "rdfdump(1)"
name: "rdfdump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdfdump/"
description: "rdfdump – dumps an RDOFF object in human-readable form"
---

<h2>NAME</h2>
<p> rdfdump &#8211; dumps an RDOFF object in human-readable form</p>
<h2>SYNOPSIS</h2>
<p> <code>rdfdump</code> [-v] &lt;<i>filename</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>rdfdump</code> prints a list of the header records in an RDOFF object in human-readable form, and optionally prints a hex dump of the contents of the segments. </p>
<p> <code>rdfdump</code> supports both version 1 and 2 of RDOFF. It will give warnings if the RDOFF2 format is violated (it looks for incorrect lengths for header records, and checks the overall length count at the start of the file).</p>
<h2>OPTIONS</h2>
<dl>
<dt>-v</p>
<dd> Print a hex dump of the contents of the segments.</dl>
<h2>AUTHORS</h2>
<p> Julian Hall &lt;jules [at] earthcorp.com&gt;. </p>
<p> This manual page was written by Matej Vela &lt;vela [at] debian.org&gt;. </p>
<h2>Index</h2>
