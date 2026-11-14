---
title: "xdriver(1)"
name: "xdriver"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdriver/"
description: "XDRIVER – GRASS Monitor – driver to display GRASS maps in X11 environment"
---

<h2>NAME</h2>
<p> <i></i><code>XDRIVER &#8211; GRASS Monitor</code> &#8211; driver to display GRASS maps in X11 environment </p>
<p>&nbsp;<wbr> <i>(drivers)</i></p>
<h2>DESCRIPTION</h2>
<p> The GRASS XDRIVER can be used to display GRASS maps in X11 environment.</p>
<h2>Usage in details</h2>
<p> Variables:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> GRASS_WIDTH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set the x size in pixel for the XDRIVER&nbsp;<wbr>(default: 640)</p>
<dt>
<dd> GRASS_HEIGHT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>set the y size in pixel for the XDRIVER&nbsp;<wbr>(default: 480)</p>
<dt>
<dd> XDRIVER_TRUECOLOR=[TRUE|FALSE] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Look for a TrueColor visual&nbsp;<wbr>(?)</p>
<dt>
<dd> XDRIVER_WINDOW </p>
<p>&nbsp;<wbr>&nbsp;<wbr>?</p>
<dt>
<dd> XDRIVER_PRIVATE_CMAP </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Private color map&nbsp;<wbr>(?)</p>
<dt>
<dd> XDRIVER_LEFT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>defines the left position of GRASS monitor&nbsp;<wbr>(<i>removed?</i>)</p>
<dt>
<dd> XDRIVER_TOP </p>
<p>&nbsp;<wbr>&nbsp;<wbr>define the upper position of GRASS monitor&nbsp;<wbr>(<i>removed?</i>)</dl>
</dl>
<h3>Set the XDRIVER size</h3>
<p> # bash shell syntax:<br />
 export GRASS_WIDTH=xxx<br />
 export GRASS_HEIGHT=yyy </p>
<p> # c shell syntax:<br />
 setenv GRASS_WIDTH xxx<br />
 setenv GRASS_HEIGHT yyy<br />
 To control the XDRIVER, use the d.mon module. </p>
<p> The maximum color depth depends on the current X Server settings.</p>
<h2>SEE ALSO</h2>
<p> <i> HTML map driver, PNG driver, PostScript driver<br />
 d.frame, d.mon, g.region </i> </p>
<h2>AUTHORS</h2>
<p> CERL<br />
 various improvements from several authors.<br />
 Rewritten 2001 by Glynn Clements </p>
<p> <i>Last changed: $Date: 2007-05-14 08:26:06 +0200 (Mon, 14 May 2007) $</i> </p>
<h2>Index</h2>
