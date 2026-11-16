---
title: "wcshead(1)"
name: "wcshead"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wcshead/"
description: "wcshead – Print WCS part of FITS or IRAF image header"
---

<h2>Name</h2>
<p> wcshead &#8211; Print WCS part of FITS or IRAF image header</p>
<h2>Synopsis</h2>
<p> wcshead [-hrtvsz] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> <i>wcshead</i> is a utility for printing the world coordinate system information in IRAF and FITS image headers. It converts IRAF .imh image headers to FITS format before extracting the information. For IRAF files, the image dimensions and the object name are set from the binary portion of the header.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Print CRVALs as hh:mm:ss and dd:mm:ss instead of degrees</dd>
<dt><code>-r</code></dt>
<dd> Print first dimension as rest wavelength limiting values</dd>
<dt><code>-t</code></dt>
<dd> Print tab-separated table output, with headers</dd>
<dt><code>-v</code></dt>
<dd> Print more intermediate information for debugging</dd>
<dt><code>-w</code></dt>
<dd> Print only first dimension limiting values (wavelength for spectra)</dd>
<dt><code>-z</code></dt>
<dd> Use AIPS classic projections instead of WCSLIB </dd>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
