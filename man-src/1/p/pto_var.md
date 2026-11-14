---
title: "pto_var(1)"
name: "pto_var"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto_var/"
description: "pto_var – change image variables inside Hugin .pto project files"
---

<h2 class="name">NAME</h2>
<p> pto_var &#8211; change image variables inside Hugin .pto project files </p>
<h2>SYNOPSIS</h2>
<p> <code>pto_var</code> [options] &#8211;opt|&#8211;link|&#8211;unlink|&#8211;set &quot;image variables list input.pto</p>
<h2>DESCRIPTION</h2>
<p> <code>pto_var</code> is a command line tool, suitable for inclusion in shell scripts, and allows the change of image variables inside a Hugin .pto project file. Optimisation variables can be set, altered, linked and unlinked, The following image variables are allowed: </p>
<pre>
  position: y, p, r, TrX, TrY, TrZ
  lens parameters: v, a, b, c, d, e, g, t
  photometric parameters: EeV, Er, Eb, Vb, Vc, Vd, Vx, Vy, Ra, Rb, Rc, Rd, Re (Vignetting and response parameter will treated as group.)
</pre>
<p> The image numbers start with zero. If the number is missing this applies to the variables of all images (In this case a special treatment applies to the position of the anchor image). An exclamation mark before the variable will remove the variable from the list of variables to optimised.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o|&#8211;output</code> = file.pto</p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &lt;filename&gt;_var.pto</p>
<dt><code>-h|&#8211;help</code></p>
<dd> Shows help</p>
<dt><code>&#8211;opt</code> varlist</p>
<dd>
<pre>
 Change optimizer variables
</pre>
<dt><code>&#8211;modify-opt</code></p>
<dd>
<pre><code>
   Modify the existing optimizer variables
   (without pto_var will start with an 
    empty variables set)
   Examples:
   --opt y,p,r           Optimize yaw, pitch and roll of all images
                         (special treatment for anchor image applies)
   --opt v0,b2           Optimize hfov of image 0 and barrel distortion
                         of image 2
   --opt v,!v0           Optimize field of view for all images except
                         for the first image
   --modify-opt --opt !v will not optimize field of view.
   --opt !a,!b,!c        Don't optimise distortion (works only with
                         switch --modify-opt together)
</code></pre>
<dt><code>&#8211;link varlist</code></p>
<dd>
<pre>
   Example:
   --link v3          Link hfov of image 3
   --link a1,b1,c1    Link distortions parameter for image 1
</pre>
<dt><code>&#8211;unlink varlist</code></p>
<dd>
   Examples:<br />
   &#8211;unlink v5        Unlink hfov for image 5<br />
   &#8211;unlink a2,b2,c2  Unlink distortions parameters for image 2</p>
<dt><code>&#8211;set varlist</code></p>
<dd>
<pre><code>
   Examples:
   --set y0=0,r0=0,p0=0  Resets position of image 0
   --set Vx4=-10,Vy4=10  Sets vignetting offset for image 4
   --set v=20            Sets the field of view to 20 for all images
   --set y=val+20        Increase yaw by 20 deg for all images
   --set v=val*1.1       Increase fov by 10 % for all images
   --set y=i*20          Set yaw to 0, 20, 40, ...
</code></pre>
<dt><code>&#8211;set-from-file filename</code></p>
<dd>
<pre>
                         Sets variables to new values
                         It reads the varlist from a file
</pre>
</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
