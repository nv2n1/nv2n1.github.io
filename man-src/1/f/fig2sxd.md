---
title: "fig2sxd(1)"
name: "fig2sxd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2sxd/"
description: "fig2sxd – utility to convert .fig to .sxd"
---

<h2>NAME</h2>
<p> fig2sxd &#8211; utility to convert .fig to .sxd</p>
<h2>SYNOPSIS</h2>
<p> <code>fig2sxd</code> <i>[-w] [-l(ine)w(idth)1 l] figfile sxdfile</i></p>
<h2>DESCRIPTION</h2>
<p> The program tries to convert the given file in xfig format into a sxd file for OpenOffice.org Draw. If figfile ends with <code>.fig</code> or <code>.xfig</code> and sxdfile is omitted, the output file will be named like figfile ending with <code>.sxd</code> instead of <code>.(x)fig</code>. Using <code>&#8211;</code> for <i>figfile</i> makes the program read from stdin so that it is possible to use</p>
<dl>
<dt>
<dd>
<p> pstoedit -f fig <i>file.ps</i> &#8211; | fig2sxd &#8211; <i>file.sxd</i> </p>
</dl>
<p> to convert ps files. (For files with many objects you might want to use something like</p>
<dl>
<dt>
<dd>
<p> pstoedit -f <code>&#8216;fig:-startdepth 9999&#8217;</code> <i>file.ps</i> &#8211; | fig2sxd &#8211; <i>file.sxd</i> </p>
</dl>
<p> to get more layers; the output of pstoedit then is no longer a valid xfig file, but it makes the z ordering of the objects in OpenOffice.org Draw stay correct.) Using <code>&#8211;</code> for <i>sxdfile</i> makes the program write to stdout. With the <code>-linewidth1</code> (or <code>-lw1</code>) option, the width of lines with thickness 1 in xfig can be set, unit is 1 cm. Using 0 here gives fine lines. Example:</p>
<dl>
<dt>
<dd>
<p> pstoedit -f <code>&#8216;fig:-startdepth 9999&#8217;</code> <i>file.ps</i> &#8211; | fig2sxd -lw1 0 &#8211; <i>file.sxd</i> </p>
</dl>
<p> With the <code>-w</code> option, out-of-specification values are only warnings but will be sanitized.</p>
<h2>DEFICIENCIES</h2>
<p> Not all of the .fig objects are converted correctly: splines look quite similar, but are not exactly the same; text placement might be a little bit wrong, especially for very small font sizes; hatches look different in many cases; hollow arrows are not supported and replaced by their filled counterparts. There are various other things that could be improved. </p>
<p> It looks like OpenOffice.org cannot read xml attribute values longer than 64kB as they might appear for very long polygons/-lines. For unfilled polylines, fig2sxd therefore creates several smaller polylines of 500 points each and groups them together. Splitting an arbitrary filled polygon is not trivial and not implemented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pstoedit/">pstoedit</a></code>(1), <code><a href="/docs/linux/man/1-xfig/">xfig</a></code>(1) and <code><a rel="nofollow" href="http://fig2sxd.sourceforge.net/">http://fig2sxd.sourceforge.net/</a></code> (for updates).</p>
<h2>AUTHOR</h2>
<p> Program and manual page were written by Alexander B[:u]rger &lt;acfb [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
