---
title: "fulla(1)"
name: "fulla"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fulla/"
description: "fulla – Correct lens distortion, vignetting and chromatic aberration"
---

<h2 class="name">NAME</h2>
<p> fulla &#8211; Correct lens distortion, vignetting and chromatic aberration </p>
<h2>SYNOPSIS</h2>
<p> <code>fulla</code> [options] <i>inputfile(s)</i></p>
<h2>DESCRIPTION</h2>
<p> Apply radial or flat-field vignetting correction as well as geometrical radial distortion and transversal chromatic aberration correction. </p>
<p> fulla can be used to batch correct a large number of files. Radial distortion coefficients can be read from a PTLens database (only database version 4.2 is supported). </p>
<p> Vignetting correction is done the same way as described in the nona script file documentation. Vignetting correction can be done based on a flat-field or a radial scaling. </p>
<p> Vignetting correction by flat-field division:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>I&nbsp;<wbr>=&nbsp;<wbr>I&nbsp;<wbr>/&nbsp;<wbr>c,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>=&nbsp;<wbr>flat-field&nbsp;<wbr>/&nbsp;<wbr>mean(flat-field) </p>
<p> Radial vignetting correction:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>I&nbsp;<wbr>=&nbsp;<wbr>I&nbsp;<wbr>/&nbsp;<wbr>c,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>=&nbsp;<wbr>a&nbsp;<wbr>+&nbsp;<wbr>b*r^2&nbsp;<wbr>+&nbsp;<wbr>c*r^4&nbsp;<wbr>+&nbsp;<wbr>d*r^6 </p>
<p> The radial distortion correction is identical to the one implemented by PanoTools: </p>
<p> r_new = a*r^4 + b*r^3 + c*r^2 + d*r [1] </p>
<p> Since transversal chromatic aberrations (<font SIZE="-1">TCA</font>) leads to differently scaled objects in the red, green and blue channel, it can be corrected by scaling the red and blue channel so that they match the green channel. Most applications, like Photoshop or Picture Window Pro offer <font SIZE="-1">TCA</font> correction by linear scaling. This is equal to varying the d parameter in equation [1]. </p>
<p> See <a rel="nofollow" href="http://hugin.sf.net/tutorials/tca">http://hugin.sf.net/tutorials/tca</a> for a method to determine these parameters.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-g</code> <i>a:b:c:d</i></p>
<dd> Radial distortion coefficient for all channels, (a, b, c, d)</p>
<dt><code>-b</code> <i>a:b:c:d</i></p>
<dd> Radial distortion coefficients for blue channel, (a, b, c, d). This is applied on top of the <code>-g</code> distortion coefficients, use for <font SIZE="-1">TCA</font> corr</p>
<dt><code>-r</code> <i>a:b:c:d</i></p>
<dd> Radial distortion coefficients for red channel, (a, b, c, d). This is applied on top of the <code>-g</code> distortion coefficients, use for <font SIZE="-1">TCA</font> corr</p>
<dt><code>-p</code></p>
<dd> Try to read radial distortion coefficients (usually supplied using -g) from the PTLens database. The environment variable <font SIZE="-1">PTLENS_PROFILE</font> should point to the profile.txt file. Since newer version of the PTLens database are incompatible with fulla, download the PTLens database from the hugin sourceforge website instead: <a rel="nofollow" href="http://www.sf.net/projects/hugin">http://www.sf.net/projects/hugin</a></p>
<dt><code>-m</code> <i>Canon</i></p>
<dd> Camera manufacturer, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given</p>
<dt><code>-n</code> <i>Camera</i></p>
<dd> Camera name, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given.</p>
<dt><code>-l</code> <i>Lens</i></p>
<dd> Lens name, for PTLens database query if not specified, a list of possible lenses is displayed</p>
<dt><code>-d</code> <i>50</i></p>
<dd> Specify focal length in mm, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given.</p>
<dt><code>-s</code></p>
<dd> Do not rescale the image to avoid black borders.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd> Vignetting correction by flat-field division </p>
<pre>
    I = I / c,    c = flat-field / mean(flat-field)
</pre>
<dt><code>-c</code> <i>a:b:c:d</i></p>
<dd> Radial vignetting correction by division: </p>
<pre>
    I = I / c,    c = a + b*r^2 + c*r^4 + d*r^6
</pre>
<dt><code>-i</code> <i>value</i></p>
<dd> Gamma of input data. used for gamma correction before and after flat-field correction</p>
<dt><code>-t</code> <i>n</i></p>
<dd> Number of threads that should be used during processing</p>
<dt><code>-h</code></p>
<dd> Display help summary.</p>
<dt><code>-o</code> <i>name</i></p>
<dd> Set output filename. If more than one image is given, the name will be uses as suffix (default suffix: _corr)</p>
<dt><code>-e</code> <i>value</i></p>
<dd> Compression of the output files</p>
<dl>
<dt>
<dd>
<dl>
<dt>For <font SIZE="-1">JPEG</font> output: 0-100</p>
<dd>
<dt>For tiff output: <font SIZE="-1">DEFLATE, LZW</font></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-v</code></p>
<dd> Verbose</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
<h2>Index</h2>
