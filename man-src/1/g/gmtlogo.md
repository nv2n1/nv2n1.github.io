---
title: "gmtlogo(1)"
name: "gmtlogo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtlogo/"
description: "gmtlogo – Adding a GMT graphics logo overlay to an illustration"
---

<h2>NAME</h2>
<p> gmtlogo &#8211; Adding a GMT graphics logo overlay to an illustration</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtlogo</code> [ [<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+j</code><i>justify</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]] ] [ [<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]*pen*]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]] ] [ <i>parameters</i> ] [ <code>z</code>|<code>Z</code><i>parameters</i> ] [ ] [ ] [ ] [ <i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[/<i>zmin</i>/<i>zmax</i>][<code>r</code>] ] [ [<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] ] [ [<i>level</i>] ] [ <i>x_offset</i> ] [ <i>y_offset</i> ] [ <code>-c</code><i>copies</i> ] [ <code>-t</code><i>&lt;transp&gt;</i> ] </p>
<p> <code>Note:</code> No space is allowed between the option flag and the associated arguments.</p>
<h2>DESCRIPTION</h2>
<p> This module plots the GMT logo on a map. By default, the GMT logo is 2 inches wide and 1 inch high and will be positioned relative to the current plot origin. Use various options to change this and to place a transparent or opaque rectangular map panel behind the GMT logo.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> None.</p>
<h2>OPTIONAL ARGUMENTS</h2>
<dl>
<dt><code>-D</code>[<code>g</code>|<code>j</code>|<code>J</code>|<code>n</code>|<code>x</code>]<i>refpoint</i><code>+w</code><i>width</i>[<code>+j</code><i>justify</i>][<code>+o</code><i>dx</i>[/<i>dy</i>]]</p>
<dd> Sets reference point on the map for the image using one of four coordinate systems: (1) Use <code>-Dg</code> for map (user) coordinates, (2) use <code>-Dj</code> or <code>-DJ</code> for setting <i>refpoint</i> via a 2-char justification code that refers to the (invisible) map domain rectangle, (3) use <code>-Dn</code> for normalized (0-1) coordinates, or (4) use <code>-Dx</code> for plot coordinates (inches, cm, etc.). All but <code>-Dx</code> requires both <code>-R</code> and <code>-J</code> to be specified. Use <code>+w</code><i>width</i> to set the width of the GMT logo in plot coordinates (inches, cm, etc.). By default, the anchor point on the scale is assumed to be the bottom left corner (BL), but this can be changed by appending <code>+j</code> followed by a 2-char justification code <i>justify</i> (see <code>pstext</code>). Note: If <code>-Dj</code> is used then <i>justify</i> defaults to the same as <i>refpoint</i>, if <code>-DJ</code> is used then <i>justify</i> defaults to the mirror opposite of <i>refpoint</i>. Add <code>+o</code> to offset the color scale by <i>dx</i>/<i>dy</i> away from the <i>refpoint</i> point in the direction implied by <i>justify</i> (or the direction implied by <code>-Dj</code> or <code>-DJ</code>).</p>
<dt><code>-F</code>[<code>+c</code><i>clearances</i>][<code>+g</code><i>fill</i>][<code>+i</code>[[<i>gap</i>/]<i>pen</i>]][<code>+p</code>[<i>pen</i>]][<code>+r</code>[<i>radius</i>]][<code>+s</code>[[<i>dx</i>/<i>dy</i>/][<i>shade</i>]]]</p>
<dd> Without further options, draws a rectangular border around the GMT logo using <code>MAP_FRAME_PEN</code>; specify a different pen with <code>+p</code><i>pen</i>. Add <code>+g</code><i>fill</i> to fill the GMT logo box [no fill]. Append <code>+c</code><i>clearance</i> where <i>clearance</i> is either <i>gap</i>, <i>xgap</i>/<i>ygap</i>, or <i>lgap</i>/<i>rgap</i>/<i>bgap</i>/<i>tgap</i> where these items are uniform, separate in x- and y-direction, or individual side spacings between GMT logo and border. Append <code>+i</code> to draw a secondary, inner border as well. We use a uniform <i>gap</i> between borders of 2<code>p</code> and the <code>MAP_DEFAULTS_PEN</code> unless other values are specified. Append <code>+r</code> to draw rounded rectangular borders instead, with a 6<code>p</code> corner radius. You can override this radius by appending another value. Finally, append <code>+s</code> to draw an offset background shaded region. Here, <i>dx</i>/<i>dy</i> indicates the shift relative to the foreground frame [4<code>p</code>/-4<code>p</code>] and <i>shade</i> sets the fill style to use for shading [gray50O.</p>
<dt><code>-O</code> <i>(more &#8230;)</i></p>
<dd> Append to existing PostScript plot.</p>
<dt><code>-P</code> <i>(more &#8230;)</i></p>
<dd> Select &quot;Portrait&quot; plot orientation.</p>
<dt><code>-R</code>[<i>unit</i>]<i>xmin</i>/<i>xmax</i>/<i>ymin</i>/<i>ymax</i>[<code>r</code>] <i>(more &#8230;)</i></p>
<dd> Specify the region of interest. </p>
<p> For perspective view <code>p</code>, optionally append /<i>zmin</i>/<i>zmax</i>. <i>(more &#8230;)</i></p>
<dt><code>-U</code>[<i>just</i>/<i>dx</i>/<i>dy</i>/][<code>c</code>|<i>label</i>] <i>(more &#8230;)</i></p>
<dd> Draw GMT time stamp logo on plot.</p>
<dt><code>-V</code>[<i>level</i>] <i>(more &#8230;)</i></p>
<dd> Select verbosity level [c]. </p>
<p> <code>-X</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>x-shift</i>[<code>u</code>]]</p>
<dt><code>-Y</code>[<code>a</code>|<code>c</code>|<code>f</code>|<code>r</code>][<i>y-shift</i>[<code>u</code>]] <i>(more &#8230;)</i></p>
<dd> Shift plot origin.</p>
<dt><code>-c</code><i>copies</i> <i>(more &#8230;)</i></p>
<dd> Specify number of plot copies [Default is 1].</p>
<dt><code>-t</code>[<i>transp</i>] <i>(more &#8230;)</i></p>
<dd> Set PDF transparency level in percent.</p>
<dt><code>-^</code> or just <code>&#8211;</code></p>
<dd> Print a short message about the syntax of the command, then exits (NOTE: on Windows use just <code>&#8211;</code>).</p>
<dt><code>-+</code> or just <code>+</code></p>
<dd> Print an extensive usage (help) message, including the explanation of any module-specific option (but not the GMT common options), then exits.</p>
<dt><code>-?</code> or no arguments</p>
<dd> Print a complete usage (help) message, including the explanation of options, then exits.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> Print GMT version and exit.</p>
<dt><code>&#8211;</code><code>-show-datadir</code></p>
<dd> Print full path to GMT share directory and exit.</dl>
<h2>EXAMPLES</h2>
<p> To plot the GMT logo of a 2 inch width as a stand-alone plot, use </p>
<pre>
gmt logo -P -Dx0/0+w2i &gt; logo.ps
</pre>
<p> To append a GMT logo overlay in the upper right corner of the current map, but scaled up to be 3 inches wide and offset by 0.1 inches from the border, try </p>
<pre>
gmt logo -O -K -R -J -DjTR+o0.1i/0.1i+w3i &gt;&gt; bigmap.ps
</pre>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>pslegend</code>, <code>psimage</code>, <code>psscale</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
