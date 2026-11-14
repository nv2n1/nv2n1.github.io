---
title: "grdredpol(1)"
name: "grdredpol"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grdredpol/"
description: "grdredpol – Compute the Continuous Reduction To the Pole, AKA differential RTP."
---

<h2>NAME</h2>
<p> grdredpol &#8211; Compute the Continuous Reduction To the Pole, AKA differential RTP.</p>
<h2>SYNOPSIS</h2>
<p> <code>grdredpol</code> <i>anom_grd</i> <i>rtp_grd</i> [<i>dec/dip</i>] [ <i>dec_grd/dipgrd</i>] [ <i>&lt;m/n&gt;</i>] [ <i>m|r</i>] [ ] [ <i>win_width</i>] [ [<i>level</i>] ] [ <i>year</i> ] [ <i>filtergrd</i> ] [ [<i>level</i>] ] [ <code>-n</code><i>&lt;flags&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> <code>grdredpol</code> will take a <i>.nc</i> file with a magnetic anomaly and compute the reduction to the pole (RTP) anomaly. This anomaly is the one that would have been produce if the bodies were magnetized vertically and the anomalies were observed at the geomagnetic pole. Standard RTP procedure assumes the direction of magnetization to be uniform throughout the causative body, and the geomagnetic field to be uniform in direction throughout the study region. Although these assumptions are reasonable for small areas, they do not hold for large areas. </p>
<p> In the method used here computations are carried out in both the frequency and the space domains. The idea is that a large area may be decomposed in small size windows where both the ambient field and the magnetization vector change by a very small amount. Inside each of those windows, or bins, a set of filter coefficients are calculate and reconstruct for each individual point the component filter using a first order Taylor series expansion.</p>
<h2>REQUIRED ARGUMENTS</h2>
<dl>
<dt><i>anom_grd</i></p>
<dd> The anomaly grid to be converted.</p>
<dt><code>-G</code><i>rtp_grd</i></p>
<dd> is the filename for output grdfile with the RTP solution</dl>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-C</code><i>dec/dip</i></p>
<dd> Use this (constant) declination and inclination angles for both field and magnetization. This option consists in the classical RTP procedure.</p>
<dt><code>-E</code><i>dip_grd/dec_grd</i></p>
<dd> Get magnetization DIP &amp; DEC from these grids [default: use IGRF]. Note that these two grids do not need to have the same resolution as the anomaly grid. They can be coarser.</p>
<dt><code>-F</code><i>m/n</i></p>
<dd> The filter window size in terms of row/columns. The default value is 25&#215;25.</p>
<dt><code>-M</code><i>m|r</i></p>
<dd> Set boundary conditions. m|r stands for mirror or replicate edges (Default is zero padding).</p>
<dt><code>-N</code></p>
<dd> Do NOT use Taylor expansion.</p>
<dt><code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i></p>
<dd> defines the Region of the output points. [Default: Same as input.]</p>
<dt><code>-T</code><i>year</i></p>
<dd> Decimal year used by the IGRF routine to compute the declination and inclination at each point [default: 2000]</p>
<dt><code>-W</code><i>width</i></p>
<dd> The size of the moving window in degrees [5].</p>
<dt><code>-Z</code><i>filter_grd</i></p>
<dd> Write the filter file to disk.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c].</p>
<dt><code>-n</code>[<code>b</code>|<code>c</code>|<code>l</code>|<code>n</code>][<code>+a</code>][<code>+b</code><i>BC</i>][<code>+c</code>][<code>+t</code><i>threshold</i>] <i>(more &#8230;)</i></p>
<dd> Select interpolation mode for grids.</dl>
<h2>CONSEQUENCES OF GRID RESAMPLING</h2>
<p> Resample or sampling of grids will use various algorithms (see <code>-n</code>) that may lead to possible distortions or unexpected results in the resampled values. One expected effect of resampling with splines is the tendency for the new resampled values to slightly exceed the global min/max limits of the original grid. If this is unacceptable, you can impose clipping of the resampled values values so they do not exceed the input min/max values by adding <code>+c</code> to your <code>-n</code> option.</p>
<h2>EXAMPLES</h2>
<p> Suppose that <i>anom.grd</i> is a file with the magnetic anomaly reduced to the 2010 epoch and that the <i>dec.grd</i> and <i>dip.grd</i> contain the magnetization declination and inclination respectively for an area that encloses that of the <i>anom.grd</i>, compute the <i>RTP</i> using bins of 2 degrees and a filter of 45 coefficients. </p>
<pre>
gmt grdredpol anom.grd -Grtp.grd -W2 -F45/45 -T2010 -Edec.grd/dip.grd -V
</pre>
<p> To compute the same <i>RTP</i> but now with the field and magnetization vectors collinear and computed from IGRF : </p>
<pre>
gmt grdredpol anom.grd -Grtp.grd -W2 -F45/45 -T2010 -V
</pre>
<h2>REFERENCE</h2>
<p> Luis, J.L. and Miranda, J.M. (2008), Reevaluation of magnetic chrons in the North Atlantic between 35N and 47N: Implications for the formation of the Azores Triple Junction and associated plateau. <i>JGR</i>, VOL. <code>113</code>, B10105, doi:10.1029/2007JB005573</p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
