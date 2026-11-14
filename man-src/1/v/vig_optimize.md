---
title: "vig_optimize(1)"
name: "vig_optimize"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vig_optimize/"
description: "vig_optimize – Optimise photometric parameters"
---

<h2 class="name">NAME</h2>
<p> vig_optimize &#8211; Optimise photometric parameters </p>
<h2>SYNOPSIS</h2>
<p> <code>vig_optimize</code> [options] <code>-o</code> <i>output.pto</i> <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> Photometric calculation can be performed on the command-line with the vig_optimize tool. This functionally is configured via &#8216;v&#8217; variable lines in the .pto project file in a similar way to the autooptimiser tool: </p>
<p> The camera response curve is simplified using the EMoR sensor model which reduces the variation to five numbers, these are the Ra, Rb, Rc, Rd &amp; Re image (i) parameters (the default values of 0.0 are equivalent to an &#8216;average&#8217; generic sensor). </p>
<p> The vignetting model is represented by a polynomial with four parameters: Va (this is always 1.0 and doesn&#8217;t need to be optimised) and Vb, Vc &amp; Vd (which default to 0.0 &#8211; equivalent to no vignetting). The vignetting centre can also be different from the geometrical centre, this is specified by Vx &amp; Vy (both default to 0.0). </p>
<p> Exposure (<font SIZE="-1">EV</font>) is represented by a single value Ev (defaults 0.0, equivalent to no-change). </p>
<p> The white balance is represented by multipliers for the red and blue channels Er and Eb (the defaults of 1.0 are equivalent to no-change). </p>
<p> A typical &#8216;v&#8217; variable line configuration would look like this, i.e. optimise camera response curve and vignetting for image 0 and exposure for images 1, 2, 3 and 4: </p>
<pre>
  v Ra0 Rb0 Rc0 Rd0 Re0 Vb0 Vc0 Vd0
  v Ev1 Ev2 Ev3 Ev4
</pre>
<p> (vignetting centre and white balance are left unchanged)</p>
<h2>OPTIONS</h2>
<p> General options:</p>
<dl>
<dt><code>-o</code> <i>file</i></p>
<dd> Write results to output project</p>
<dt><code>-v</code></p>
<dd> Verbose, print progress messages</p>
<dt><code>-p</code> <i>n</i></p>
<dd> Number of points to extract</p>
<dt><code>-r</code></p>
<dd> Extract random point (faster, but less accurate)</p>
<dt><code>-s</code> <i>level</i></p>
<dd> Work on downscaled images, every step halves width and height</p>
<dt><code>-h</code></p>
<dd> Display help summary.</dl>
<p> Expert and debugging options:</p>
<dl>
<dt><code>-i</code> <i>file</i></p>
<dd> Read corresponding points from file</p>
<dt><code>-w</code> <i>file</i></p>
<dd> Dump corresponding points to file</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
