---
title: "wfmath_ball(3)"
name: "wfmath_ball"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_ball/"
description: "WFMath::Ball – A dim dimensional ball."
---

<p>WFMath::Ball &#8211; A dim dimensional ball. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/ball.h">ball.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Ball</code> ()<br />
 <i>construct an uninitialized ball </i><br />
 <code>Ball</code> (const <code>Point</code>&lt; dim &gt; &amp;center, <code>CoordType</code> radius)<br />
 <i>construct a ball with the given center and radius </i><br />
 <code>Ball</code> (const <code>Ball</code> &amp;b)<br />
 <i>construct a copy of a ball </i><br />
 <code>Ball</code> (const AtlasInType &amp;a)<br />
 <i>Construct a ball from an object passed by Atlas. </i><br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the box. </i><br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the box&#8217;s value to that given by an Atlas object. </i><br />
 const <code>Point</code>&lt; dim &gt; &amp; <code>center</code> () const<br />
 <i>get the center of the ball </i><br />
 <code>Point</code>&lt; dim &gt; &amp; <code>center</code> ()<br />
 <i>get the center of the ball </i><br />
 <code>CoordType</code> <code>radius</code> () const<br />
 <i>get the radius of the ball </i><br />
 <code>CoordType</code> &amp; <code>radius</code> ()<br />
 <i>get the radius of the ball </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::Ball&lt; dim &gt;</h3>
<p>A dim dimensional ball. </p>
<p> This class implements the full shape interface, as described in the fake class <code>Shape</code>. </p>
<p> This class is called Ball&lt;&gt; instead of Sphere to be more in tune with the usual mathematical naming conventions, where a ball is a filled object, while a sphere is just the outer shell. It also helps that a Ball&lt;n&gt; corresponds to an n-ball, while a Sphere&lt;n&gt; would correspond to an (n-1)-sphere. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
