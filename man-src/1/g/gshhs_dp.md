---
title: "gshhs_dp(1)"
name: "gshhs_dp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gshhs_dp/"
description: "gshhs_dp – Line reduction using the Douglas-Peucker algorithm"
---

<h2>NAME</h2>
<p> gshhs_dp &#8211; Line reduction using the Douglas-Peucker algorithm</p>
<h2>SYNOPSIS</h2>
<p> <code>gshhs_dp</code> <i>input.b tolerance output.b</i> [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gshhs_dp</code> reads the binary coastline (GSHHS) or political boundary or river (WDBII) files and and reduces the complexity of the line by applying the Douglas-Peucker algorithm. It automatically handles byte-swabbing between different architectures.</p>
<dl>
<dt><i>input.b</i></p>
<dd> GSHHS or WDBII binary data file as distributed with the GSHHS data supplement. Any of the 5 standard resolutions (full, high, intermediate, low, crude) can be used.</p>
<dt><i>tolerance</i></p>
<dd> tolerance is maximum mismatch in km. The larger the value the more reduction will take place.</p>
<dt><i>output.b</i></p>
<dd> The reducted data set.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Reports progress and statistics while running.</dl>
<h2>EXAMPLES</h2>
<p> To simplify the full GSHHS data set with a custom tolerance of 2 km, try </p>
<p> <code>gshhs_dp</code> <i>gshhs_f.b 2 gshhs_2km.b</i></p>
<h2>REFERENCES</h2>
<p> Douglas, D. H., and T. K. Peucker, Algorithms for the reduction of the number of points required to represent a digitized line of its caricature, <i>Can. Cartogr., 10</i>, 112-122, 1973.</p>
<h2>AUTHOR</h2>
<p> This implementation of the D-P algorithm has been kindly provided by Dr. Gary J. Robinson, Environmental Systems Science Centre, University of Reading, Reading, UK (gazza [at] mail.nerc-essc.ac.uk); his subroutine forms the basis for this program.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gshhs/">gshhs</a></i>(1), <i><a href="/docs/linux/man/1-gshhstograss/">gshhstograss</a></i>(1) </p>
<h2>Index</h2>
