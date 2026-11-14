---
title: "glutsolidsierpinskisponge(3)"
name: "glutsolidsierpinskisponge"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glutsolidsierpinskisponge/"
description: "glutSolidSierpinskiSponge – Draw a solid Spierspinski’s sponge."
---

<p><code>glutSolidSierpinskiSponge</code> &#8211; Draw a solid Spierspinski&#8217;s sponge.</p>
<h2>Library</h2>
<p>OpenGLUT &#8211; geometry</p>
<h2>Synopsis</h2>
<p>In openglut.h Ft void Fn glutSolidSierpinskiSponge int num_levels const GLdouble offset[ 3 ] GLdouble scale</p>
<h2>Parameters</h2>
<p>Bf Em<br />
&nbsp;<wbr>num_levels Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Recursive depth. </p>
<p> Bf Em<br />
&nbsp;<wbr>offset Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Location vector. </p>
<p> Bf Em<br />
&nbsp;<wbr>scale Ef<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Relative size.</p>
<h2>Description</h2>
<p>This function recursively draws a few levels of a solid-shaded Sierpinski&#8217;s Sponge. If Bf Sy<br />
&nbsp;<wbr>num_levels Ef<br />
&nbsp;<wbr>is 0, draws 1 tetrahedron. The Bf Sy<br />
&nbsp;<wbr>offset Ef<br />
&nbsp;<wbr>is a translation. The Bf Sy<br />
&nbsp;<wbr>z Ef<br />
&nbsp;<wbr>axis is normal to the base. The sponge is centered at the origin. </p>
<h2>Caveats</h2>
<p>Runtime is exponential in Bf Sy<br />
&nbsp;<wbr>num_levels Ef<br />
&nbsp;<wbr>. </p>
<h2>Todo</h2>
<p>Consider removing the Bf Sy<br />
&nbsp;<wbr>offset Ef<br />
&nbsp;<wbr>parameter from the API&nbsp;<wbr>(use a helper function). </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-glutwiresierpinskisponge/">glutWireSierpinskiSponge</a>(3)</p>
