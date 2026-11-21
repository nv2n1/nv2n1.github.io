---

title: "fulla(1)"
name: "fulla"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fulla/"
description: "fulla – Correct lens distortion, vignetting and chromatic aberration"
---

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
<dt><code>-g</code> <i>a:b:c:d</i></dt>
<dd> Radial distortion coefficient for all channels, (a, b, c, d)</dd>
<dt><code>-b</code> <i>a:b:c:d</i></dt>
<dd> Radial distortion coefficients for blue channel, (a, b, c, d). This is applied on top of the <code>-g</code> distortion coefficients, use for <font SIZE="-1">TCA</font> corr</dd>
<dt><code>-r</code> <i>a:b:c:d</i></dt>
<dd> Radial distortion coefficients for red channel, (a, b, c, d). This is applied on top of the <code>-g</code> distortion coefficients, use for <font SIZE="-1">TCA</font> corr</dd>
<dt><code>-p</code></dt>
<dd> Try to read radial distortion coefficients (usually supplied using -g) from the PTLens database. The environment variable <font SIZE="-1">PTLENS_PROFILE</font> should point to the profile.txt file. Since newer version of the PTLens database are incompatible with fulla, download the PTLens database from the hugin sourceforge website instead: <a rel="nofollow" href="http://www.sf.net/projects/hugin">http://www.sf.net/projects/hugin</a></dd>
<dt><code>-m</code> <i>Canon</i></dt>
<dd> Camera manufacturer, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given</dd>
<dt><code>-n</code> <i>Camera</i></dt>
<dd> Camera name, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given.</dd>
<dt><code>-l</code> <i>Lens</i></dt>
<dd> Lens name, for PTLens database query if not specified, a list of possible lenses is displayed</dd>
<dt><code>-d</code> <i>50</i></dt>
<dd> Specify focal length in mm, for PTLens database query. <font SIZE="-1">EXIF</font> data inside <font SIZE="-1">JPEG</font> files is read, if this option is not given.</dd>
<dt><code>-s</code></dt>
<dd> Do not rescale the image to avoid black borders.</dd>
<dt><code>-f</code> <i>filename</i></dt>
<dd> Vignetting correction by flat-field division </dd>
<pre>
    I = I / c,    c = flat-field / mean(flat-field)
</pre>
<dt><code>-c</code> <i>a:b:c:d</i></dt>
<dd> Radial vignetting correction by division: </dd>
<pre>
    I = I / c,    c = a + b*r^2 + c*r^4 + d*r^6
</pre>
<dt><code>-i</code> <i>value</i></dt>
<dd> Gamma of input data. used for gamma correction before and after flat-field correction</dd>
<dt><code>-t</code> <i>n</i></dt>
<dd> Number of threads that should be used during processing</dd>
<dt><code>-h</code></dt>
<dd> Display help summary.</dd>
<dt><code>-o</code> <i>name</i></dt>
<dd> Set output filename. If more than one image is given, the name will be uses as suffix (default suffix: _corr)</dd>
<dt><code>-e</code> <i>value</i></dt>
<dd> Compression of the output files</dd>
<dl>
<dl>
<dt>For <font SIZE="-1">JPEG</font> output: 0-100</dt>
<dd>
</dd><dt>For tiff output: <font SIZE="-1">DEFLATE, LZW</font></dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-v</code></dt>
<dd> Verbose</dd></dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo. Also contains contributions from Douglas Wilkins, Ippei Ukai, Ed Halley, Bruno Postle, Gerry Patterson and Brent Townshend. </p>
<p> This man page was written by Cyril Brulebois &lt;cyril.brulebois [at] enst-bretagne.fr&gt; and is licensed under the same terms as the hugin package itself. </p>
