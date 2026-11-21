---

title: "rsvg(1)"
name: "rsvg"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rsvg/"
description: "rsvg – Turn SVG files into raster images."
---

<h2>NAME</h2>
<p> rsvg &#8211; Turn SVG files into raster images.</p>
<p> <code>rsvg</code> [options] in.svg out.png <i></i></p>
<p> RSVG coverts SVG images into PNG, JPEG, and ICO raster images.</p>
<h3>OPTIONS</h3>
<dl>
<dt><i>-d &#8211;dpi-x number</i></dt>
<dd> Set the X resolution of the image in pixels per inch. RSVG&#8217;s current default is 90dpi</dd>
<dt><i>-p &#8211;dpi-y number</i></dt>
<dd> Set the Y resolution of the image in pixels per inch. RSVG&#8217;s current default is 90dpi</dd>
<dt><i>-x &#8211;x-zoom number</i></dt>
<dd> X Zoom factor, as a percentage. If unspecified, 1.0 is used as the default.</dd>
<dt><i>-y &#8211;y-zoom number</i></dt>
<dd> Y Zoom factor, as a percentage. If unspecified, 1.0 is used as the default.</dd>
<dt><i>-w &#8211;width integer</i></dt>
<dd> Specify how wide you wish the image to be. If unspecified, the natural width of the image is used as the default.</dd>
<dt><i>-h &#8211;height integer</i></dt>
<dd> Specify how tall you wish the image to be. If unspecified, the natural height of the image is used as the default.</dd>
<dt><i>-f &#8211;format [png, jpeg, ico]</i></dt>
<dd> Specify the output format you wish the image to be saved in. If unspecified, PNG is used as the default.</dd>
<dt><i>-q &#8211;quality integer</i></dt>
<dd> Specify JPEG compression factor. Number must be between 1 and 100, inclusive.</dd>
<dt><i>-v &#8211;version</i></dt>
<dd> Display what version of rsvg this is.</dd></dl>
<h2>MORE INFORMATION</h2>
<p> <a rel="nofollow" href="http://librsvg.sourceforge.net/">http://librsvg.sourceforge.net/</a> <a rel="nofollow" href="http://www.w3.org/TR/SVG11/">http://www.w3.org/TR/SVG11/</a> <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a></p>
<h2>AUTHORS</h2>
<p> Dom Lachowicz (cinamod [at] hotmail.com), Caleb Moore (c.moore [at] student.unsw.edu.au), and a host of others. </p>
