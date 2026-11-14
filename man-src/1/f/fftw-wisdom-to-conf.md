---
title: "fftw-wisdom-to-conf(1)"
name: "fftw-wisdom-to-conf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fftw-wisdom-to-conf/"
description: "fftw-wisdom-to-conf – generate FFTW wisdom (pre-planned transforms)"
---

<h2>NAME</h2>
<p> fftw-wisdom-to-conf &#8211; generate FFTW wisdom (pre-planned transforms)</p>
<h2>SYNOPSIS</h2>
<p> <code>fftw-wisdom-to-conf</code> [&lt; <i>INPUT</i>] [&gt; <i>OUTPUT</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>fftw-wisdom-to-conf</i> is a utility to generate C <code>configuration</code> routines from FFTW <code>wisdom</code> files, where the latter contain saved information about how to optimally compute (Fourier) transforms of various sizes. A configuration routine is a C subroutine that you link into your program, replacing a routine of the same name in the FFTW library, that determines which parts of FFTW are callable by your program. </p>
<p> The reason to do this is that, if you only need transforms of a limited set of sizes and types, and if you are statically linking your program, then using a configuration file generated from wisdom for those types can substantially reduce the size of your executable. (Otherwise, because of FFTW&#8217;s dynamic nature, all of FFTW&#8217;s transform code must be linked into any program using FFTW.) </p>
<p> FFTW is a free library to compute discrete Fourier transforms in one or more dimensions, for arbitrary sizes, and of both real and complex data, among other related operations. More information on FFTW can be found at the FFTW home page: <i><a rel="nofollow" href="http://www.fftw.org">http://www.fftw.org</a></i> </p>
<p> <i>fftw-wisdom-to-conf</i> reads wisdom from standard input and writes the configuration to standard output. It can easily be combined with the <i>fftw-wisdom</i> tool, for example: </p>
<p> fftw-wisdom -n cof1024 cob1024 -o wisdom<br />
 fftw-wisdom-to-conf &lt; wisdom &gt; conf.c </p>
<p> will create a configuration &quot;conf.c&quot; containing only those parts of FFTW needed for the optimized complex forwards and backwards out-of-place transforms of size 1024 (also saving the wisdom itself in &quot;wisdom&quot;). </p>
<p> Alternatively, you can run your actual program, export wisdom for all plans that were created (ideally in FFTW_PATIENT or FFTW_EXHAUSTIVE mode), use this as input for <i>fftw-wisdom-to-conf</i>, and then re-link your program with the resulting configuration routine. </p>
<p> Note that the configuration routine does not contain the wisdom, only the routines necessary to implement the wisdom, so your program should also import the wisdom in order to benefit from the pre-optimized plans.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help on the command-line options and usage.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number and copyright information.</dl>
<h2>BUGS</h2>
<p> Send bug reports to fftw [at] fftw.org.</p>
<h2>AUTHORS</h2>
<p> Written by Steven G. Johnson and Matteo Frigo. </p>
<p> Copyright (c) 2003, 2007-11 Matteo Frigo<br />
 Copyright (c) 2003, 2007-11 Massachusetts Institute of Technology</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fftw-wisdom/">fftw-wisdom</a>(1) </p>
<h2>Index</h2>
