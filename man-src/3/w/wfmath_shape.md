---
title: "wfmath_shape(3)"
name: "wfmath_shape"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_shape/"
description: "WFMath::Shape – A fake class which documents the generic parts of the WFMath interface."
---

<p>WFMath::Shape &#8211; A fake class which documents the generic parts of the <code>WFMath</code> interface. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/shape.h">shape.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p>bool <code>isEqualTo</code> (const <code>Shape</code> &amp;s, double tolerance=WFMATH_EPSILON) const<br />
 <i>generic: check if two classes are equal, up to a given tolerance </i><br />
 bool <code>operator==</code> (const <code>Shape</code> &amp;s) const<br />
 <i>generic: check if two classes are equal, up to tolerance WFMATH_EPSILON </i><br />
 bool <code>operator!=</code> (const <code>Shape</code> &amp;s) const<br />
 <i>generic: check if two classes are not equal, up to tolerance WFMATH_EPSILON </i><br />
 bool <code>isValid</code> () const<br />
 <i>generic: returns true if the class instance has been initialized </i><br />
 int <code>numCorners</code> () const<br />
 <i>shape: return the number of corners in the shape. </i><br />
 <code>Point</code>&lt; dim &gt; <code>getCorner</code> (int i) const<br />
 <i>shape: return the position of the i&#8217;th corner, where 0 &lt;= i &lt; </i><code>numCorners()</code><br />
 <code>Point</code>&lt; dim &gt; <code>getCenter</code> () const<br />
 <i>shape: return the position of the center of the shape </i><br />
 <code>Shape</code> &amp; <code>shift</code> (const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>shape: move the shape by an amount given by the </i><code>Vector</code> v<br />
 <code>Shape</code> &amp; <code>moveCornerTo</code> (const <code>Point</code>&lt; dim &gt; &amp;p, int corner)<br />
 <i>shape: move the shape, moving the given corner to the </i><code>Point</code> p<br />
 <code>Shape</code> &amp; <code>moveCenterTo</code> (const <code>Point</code>&lt; dim &gt; &amp;p)<br />
 <i>shape: move the shape, moving the center to the </i><code>Point</code> p<br />
 <code>Shape</code> &amp; <code>rotateCorner</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, int corner)<br />
 <i>shape: rotate the shape while holding the given corner fixed </i><br />
 <code>Shape</code> &amp; <code>rotateCenter</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m)<br />
 <i>shape: rotate the shape while holding the center fixed </i><br />
 <code>Shape</code> &amp; <code>rotatePoint</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Point</code>&lt; dim &gt; &amp;p)<br />
 <i>shape: rotate the shape while holding the </i><code>Point</code> p fixed.<br />
 <code>AxisBox</code>&lt; dim &gt; <code>boundingBox</code> () const<br />
 <i>shape: return the minimal axis-aligned bounding box </i><br />
 <code>Ball</code>&lt; dim &gt; <code>boundingSphere</code> () const<br />
 <i>shape: return the minimal bounding sphere </i><br />
 <code>Ball</code>&lt; dim &gt; <code>boundingSphereSloppy</code> () const </p>
<h3>Friends</h3>
<p>std::ostream &amp; <code>operator</code> (std::ostream &amp;os, const <code>Shape</code> &amp;s)<br />
 <i>generic: Print an instance to a stream </i><br />
 std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;is, <code>Shape</code> &amp;s)<br />
 <i>generic: Parse an instance from a stream </i><br />
 bool <code>Intersect</code> (<code>Shape</code>&lt; dim &gt; &amp;s1, <code>Shape</code>&lt; dim &gt; &amp;s2, bool proper)<br />
 <i>shape: Returns true if the two shapes intersect. </i><br />
 bool <code>Contains</code> (<code>Shape</code>&lt; dim &gt; &amp;s1, <code>Shape</code>&lt; dim &gt; &amp;s2, bool proper)<br />
 <i>shape: Returns true if the first shape contains the second. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::Shape&lt; dim &gt;</h3>
<p>A fake class which documents the generic parts of the <code>WFMath</code> interface. </p>
<p> This fake class documents two parts of the <code>WFMath</code> generic class interface. With a few exceptions (e.g. classes derived from std::exception), every class in <code>WFMath</code> implements the part of the interface labeled as &#8216;generic&#8217;. The &#8216;shape&#8217; interface is implemented by several classes, which identify themselves in their own documentation. Every class which implements the &#8216;shape&#8217; interface also implements the &#8216;generic&#8217; interface. Classes will not generally document their generic and shape interface functions.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;const int dim&gt; <code>Ball</code>&lt;dim&gt; <code>WFMath::Shape</code>&lt; dim &gt;::boundingSphereSloppy () const</h3>
<p>shape: return an approximate bounding sphere, guaranteed to contain the minimal bounding sphere <code>boundingSphereSloppy()</code> uses SloppyDistance() instead of Distance() to calculate it&#8217;s radius, except in cases like Point&lt;&gt; and Ball&lt;&gt; where it would be silly. Thus, the result of <code>boundingSphereSloppy()</code> is guaranteed to contain the result of <code>boundingSphere()</code>.</p>
<h3>template&lt;const int dim&gt; <code>Shape</code>&amp; <code>WFMath::Shape</code>&lt; dim &gt;::moveCenterTo (const <code>Point</code>&lt; dim &gt; &amp; p) [inline]</h3>
<p>shape: move the shape, moving the center to the <code>Point</code> p </p>
<p> The center is defined by <code>getCenter()</code> </p>
<p> References WFMath::Shape&lt; dim &gt;::getCenter(), and WFMath::Shape&lt; dim &gt;::shift().</p>
<h3>template&lt;const int dim&gt; <code>Shape</code>&amp; <code>WFMath::Shape</code>&lt; dim &gt;::moveCornerTo (const <code>Point</code>&lt; dim &gt; &amp; p, int corner) [inline]</h3>
<p>shape: move the shape, moving the given corner to the <code>Point</code> p </p>
<p> The corner in question is getCorner(corner). </p>
<p> References WFMath::Shape&lt; dim &gt;::getCorner(), and WFMath::Shape&lt; dim &gt;::shift().</p>
<h3>template&lt;const int dim&gt; int <code>WFMath::Shape</code>&lt; dim &gt;::numCorners () const</h3>
<p>shape: return the number of corners in the shape. </p>
<p> For many shape classes, this is a fixed constant</p>
<h3>template&lt;const int dim&gt; <code>Shape</code>&amp; <code>WFMath::Shape</code>&lt; dim &gt;::rotateCenter (const <code>RotMatrix</code>&lt; dim &gt; &amp; m) [inline]</h3>
<p>shape: rotate the shape while holding the center fixed </p>
<p> The center is defined by <code>getCenter()</code> </p>
<p> References WFMath::Shape&lt; dim &gt;::getCenter(), and WFMath::Shape&lt; dim &gt;::rotatePoint().</p>
<h3>template&lt;const int dim&gt; <code>Shape</code>&amp; <code>WFMath::Shape</code>&lt; dim &gt;::rotateCorner (const <code>RotMatrix</code>&lt; dim &gt; &amp; m, int corner) [inline]</h3>
<p>shape: rotate the shape while holding the given corner fixed </p>
<p> The corner in question is getCorner(corner). </p>
<p> References WFMath::Shape&lt; dim &gt;::getCorner(), and WFMath::Shape&lt; dim &gt;::rotatePoint().</p>
<h3>template&lt;const int dim&gt; <code>Shape</code>&amp; <code>WFMath::Shape</code>&lt; dim &gt;::rotatePoint (const <code>RotMatrix</code>&lt; dim &gt; &amp; m, const <code>Point</code>&lt; dim &gt; &amp; p)</h3>
<p>shape: rotate the shape while holding the <code>Point</code> p fixed. </p>
<p> Note that p can be any <code>Point</code>, it does not have to lie within the shape. </p>
<p> Referenced by WFMath::Shape&lt; dim &gt;::rotateCenter(), and WFMath::Shape&lt; dim &gt;::rotateCorner().</p>
<h2>Friends And Related Function Documentation</h2>
<h3>template&lt;const int dim&gt; bool Contains (<code>Shape</code>&lt; dim &gt; &amp; s1, <code>Shape</code>&lt; dim &gt; &amp; s2, bool proper) [friend]</h3>
<p>shape: Returns true if the first shape contains the second. </p>
<p> If the &#8216;proper&#8217; argument is true, the inner shape is not contained if it touches the boundary of the outer shape. Otherwise, it does. Therefore, any shape contains itself (Contains(foo, foo, false) == true), but no shape contains itself properly (Contains(foo, foo, true) == false). Because of this, an empty shape (e.g. a <code>Polygon</code> with zero corners) is properly contained by any other shape. A <code>Point</code>, or any single point shape (e.g. a <code>Segment</code> where the endpoints are equal) properly contains an empty shape, and contains (but not properly) any other single point shape which occupies the same point. The two shapes do not have to be the same class, but must have the same dimension.</p>
<h3>template&lt;const int dim&gt; bool Intersect (<code>Shape</code>&lt; dim &gt; &amp; s1, <code>Shape</code>&lt; dim &gt; &amp; s2, bool proper) [friend]</h3>
<p>shape: Returns true if the two shapes intersect. </p>
<p> If the &#8216;proper&#8217; argument is true, shapes which only touch on their boundary do not count as intersecting. If it is false, they do. This function is symmetric in its first two arguments (Intersect(a, b, proper) == Intersect(b, a, proper)). The two shapes do not have to be the same class, but must have the same dimension. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
