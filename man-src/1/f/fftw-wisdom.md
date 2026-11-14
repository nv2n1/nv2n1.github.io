---
title: "fftw-wisdom(1)"
name: "fftw-wisdom"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fftw-wisdom/"
description: "fftw-wisdom – create wisdom (pre-optimized FFTs)"
---

<h2>NAME</h2>
<p> fftw-wisdom &#8211; create wisdom (pre-optimized FFTs)</p>
<h2>SYNOPSIS</h2>
<p> <code>fftw-wisdom</code> [<i>OPTION</i>]&#8230; [<i>SIZE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>fftw-wisdom</i> is a utility to generate FFTW <code>wisdom</code> files, which contain saved information about how to optimally compute (Fourier) transforms of various sizes. FFTW is a free library to compute discrete Fourier transforms in one or more dimensions, for arbitrary sizes, and of both real and complex data, among other related operations. More information on FFTW can be found at the FFTW home page: <i><a rel="nofollow" href="http://www.fftw.org">http://www.fftw.org</a></i> </p>
<p> Programs using FFTW can be written to load wisdom from an arbitrary file, string, or other source. Moreover, it is likely that many FFTW-using programs will load the <code>system wisdom</code> file, which is stored in <i>/etc/fftw/wisdom</i> by default. <i>fftw-wisdom</i> can be used to create or add to such wisdom files. In its most typical usage, the wisdom file can be created to pre-plan a canonical set of sizes (see below) via: </p>
<p> <center> fftw-wisdom -v -c -o wisdom<br />
 </center> </p>
<p> (this will take many hours, which can be limited by the <code>-t</code> option) and the output <i>wisdom</i> file can then be copied (as root) to <i>/etc/fftw/</i> or whatever. </p>
<p> The <i>fftw-wisdom</i> program normally writes the wisdom directly to standard output, but this can be changed via the <code>-o</code> option, as in the example above. </p>
<p> If the system wisdom file <i>/etc/fftw/wisdom</i> already exists, then <i>fftw-wisdom</i> reads this existing wisdom (unless the <code>-n</code> option is specified) and outputs both the old wisdom and any newly created wisdom. In this way, it can be used to add new transform sizes to the existing system wisdom (or other wisdom file, with the <code>-w</code> option).</p>
<h2>SPECIFYING SIZES</h2>
<p> Although a canonical set of sizes to optimize is specified by the <code>-c</code> option, the user can also specify zero or more non-canonical transform sizes and types to optimize, via the <i>SIZE</i> arguments following the option flags. Alternatively, the sizes to optimize can be read from standard input (whitespace-separated), if a <i>SIZE</i> argument of &quot;-&quot; is supplied. </p>
<p> Sizes are specified by the syntax: </p>
<p> <center> &lt;<i>type</i>&gt;&lt;<i>inplace</i>&gt;&lt;<i>direction</i>&gt;&lt;<i>geometry</i>&gt;<br />
 </center> </p>
<p> &lt;<i>type</i>&gt; is either &#8216;c&#8217; (complex), &#8216;r&#8217; (real, r2c/c2r), or &#8216;k&#8217; (r2r, per-dimension kinds, specified in the geometry, below). </p>
<p> &lt;<i>inplace</i>&gt; is either &#8216;i&#8217; (in place) or &#8216;o&#8217; (out of place). </p>
<p> &lt;<i>direction</i>&gt; is either &#8216;f&#8217; (forward) or &#8216;b&#8217; (backward). The &lt;<i>direction</i>&gt; should be omitted for &#8216;k&#8217; transforms, where it is specified via the geometry instead. </p>
<p> &lt;<i>geometry</i>&gt; is the size and dimensionality of the transform, where different dimensions are separated by &#8216;x&#8217; (e.g. &#8217;16&#215;32&#8242; for a two-dimensional 16 by 32 transform). In the case of &#8216;k&#8217; transforms, the size of each dimension is followed by a &quot;type&quot; string, which can be one of f/b/h/e00/e01/e10/e11/o00/o01/o10/o11 for R2HC/HC2R/DHT/REDFT00/&#8230;/RODFT11, respectively, as defined in the FFTW manual. </p>
<p> For example, &#8216;cif12x13x14&#8217; is a three-dimensional 12 by 13 x 14 complex DFT operating in-place. &#8216;rob65536&#8217; is a one-dimensional size-65536 out-of-place complex-to-real (backwards) transform operating on Hermitian-symmetry input. &#8216;ki10hx20e01&#8217; is a two-dimensional 10 by 20 r2r transform where the first dimension is a DHT and the second dimension is an REDFT01 (DCT-III). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help on the command-line options and usage.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print the version number and copyright information.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose output. (You can specify this multiple times, or supply a numeric argument greater than 1, to increase the verbosity level.) Note that the verbose output will be mixed with the wisdom output (making it impossible to import), unless you write the wisdom to a file via the <code>-o</code> option.</p>
<dt><code>-c</code>, <code>&#8211;canonical</code></p>
<dd> Optimize/pre-plan a canonical set of sizes: all powers of two and ten up to 2^20 (1048576), including both real and complex, forward and backwards, in-place and out-of-place transforms. Also includes two- and three-dimensional transforms of equal-size dimensions (e.g. 16x16x16).</p>
<dt><code>-t</code> <i>hours</i>, <code>&#8211;time-limit</code>=<i>hours</i></p>
<dd> Stop after a time of <i>hours</i> (hours) has elapsed, outputting accumulated wisdom. (The problems are planned in increasing order of size.) Defaults to 0, indicating no time limit.</p>
<dt><code>-o</code> <i>file</i>, <code>&#8211;output-file</code>=<i>file</i></p>
<dd> Send wisdom output to <i>file</i> rather than to standard output (the default).</p>
<dt><code>-m</code>, <code>&#8211;measure</code>; <code>-e</code>, <code>&#8211;estimate</code>; <code>-x</code>, <code>&#8211;exhaustive</code></p>
<dd> Normally, <i>fftw-wisdom</i> creates plans in FFTW_PATIENT mode, but with these options you can instead use FFTW_MEASURE, FFTW_ESTIMATE, or FFTW_EXHAUSTIVE modes, respectively, as described in more detail by the FFTW manual. </p>
<p> Note that wisdom is tagged with the planning patience level, and a single file can mix different levels of wisdom (e.g. you can mostly use the patient default, but plan a few sizes that you especially care about in <code>&#8211;exhaustive</code> mode).</p>
<dt><code>-n</code>, <code>&#8211;no-system-wisdom</code></p>
<dd> Do not import the system wisdom from <i>/etc/fftw/wisdom</i> (which is normally read by default).</p>
<dt><code>-w</code> <i>file</i>, <code>&#8211;wisdom-file</code>=<i>file</i></p>
<dd> Import wisdom from <i>file</i> (in addition to the system wisdom, unless <code>-n</code> is specified). Multiple wisdom files can be read via multiple <code>-w</code> options. If <i>file</i> is &quot;-&quot;, then read wisdom from standard input.</dl>
<h2>BUGS</h2>
<p> Send bug reports to fftw [at] fftw.org.</p>
<h2>AUTHORS</h2>
<p> Written by Steven G. Johnson and Matteo Frigo. </p>
<p> Copyright (c) 2003, 2007-11 Matteo Frigo<br />
 Copyright (c) 2003, 2007-11 Massachusetts Institute of Technology</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fftw-wisdom-to-conf/">fftw-wisdom-to-conf</a>(1) </p>
<h2>Index</h2>
