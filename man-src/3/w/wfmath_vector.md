---
title: "wfmath_vector(3)"
name: "wfmath_vector"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_vector/"
description: "WFMath::Vector – A dim dimensional vector."
---

<p>WFMath::Vector &#8211; A dim dimensional vector. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/vector.h">vector.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Vector</code> ()<br />
 <i>Construct an uninitialized vector. </i><br />
 <code>Vector</code> (const <code>Vector</code> &amp;v)<br />
 <i>Construct a copy of a vector. </i><br />
 <code>Vector</code> (const AtlasInType &amp;a)<br />
 <i>Construct a vector from an object passed by Atlas. </i><br />
 <code>Vector</code> (const <code>Point</code>&lt; dim &gt; point)<br />
 <i>Construct a vector from a point. </i><br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the vector. </i><br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the vector&#8217;s value to that given by an Atlas object. </i><br />
 void <code>setValid</code> (bool valid=true)<br />
 <i>make isValid() return true if you&#8217;ve initialized the vector by hand </i><br />
 <code>Vector</code> &amp; <code>zero</code> ()<br />
 <i>Zero the components of a vector. </i><br />
 <code>CoordType</code> <code>operator[]</code> (const int i) const<br />
 <i>Get the i&#8217;th element of the vector. </i><br />
 <code>CoordType</code> &amp; <code>operator[]</code> (const int i)<br />
 <i>Get the i&#8217;th element of the vector. </i><br />
 <code>CoordType</code> <code>sqrMag</code> () const<br />
 <i>The squared magnitude of a vector. </i><br />
 <code>CoordType</code> <code>mag</code> () const<br />
 <i>The magnitude of a vector. </i><br />
 <code>Vector</code> &amp; <code>normalize</code> (<code>CoordType</code> norm=1.0)<br />
 <i>Normalize a vector. </i><br />
 <code>CoordType</code> <code>sloppyMag</code> () const<br />
 <i>An approximation to the magnitude of a vector. </i><br />
 <code>Vector</code> &amp; <code>sloppyNorm</code> (<code>CoordType</code> norm=1.0)<br />
 <i>Approximately normalize a vector. </i><br />
 <code>Vector</code> &amp; <code>rotate</code> (int axis1, int axis2, <code>CoordType</code> theta)<br />
 <i>Rotate the vector in the (axis1, axis2) plane by the angle theta. </i><br />
 <code>Vector</code> &amp; <code>rotate</code> (const <code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2, <code>CoordType</code> theta)<br />
 <i>Rotate the vector in the (v1, v2) plane by the angle theta. </i><br />
 <code>Vector</code> &amp; <code>rotate</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;)<br />
 <i>Rotate the vector using a matrix. </i><br />
 <code>Vector</code> &amp; <code>mirror</code> (const int i)<br />
 <i>Reflect a vector in the direction of the i&#8217;th axis. </i><br />
 <code>Vector</code> &amp; <code>mirror</code> (const <code>Vector</code> &amp;v)<br />
 <i>Reflect a vector in the direction specified by v. </i><br />
 <code>Vector</code> &amp; <code>mirror</code> ()<br />
 <i>Reflect a vector in all directions simultaneously. </i><br />
 <code>Vector</code> (<code>CoordType</code> x, <code>CoordType</code> y)<br />
 <i>2D only: construct a vector from (x, y) coordinates </i><br />
 <code>Vector</code> (<code>CoordType</code> x, <code>CoordType</code> y, <code>CoordType</code> z)<br />
 <i>3D only: construct a vector from (x, y, z) coordinates </i><br />
 <code>Vector</code>&lt; 2 &gt; &amp; <code>rotate</code> (<code>CoordType</code> theta)<br />
 <i>2D only: rotate a vector by an angle theta </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>rotateX</code> (<code>CoordType</code> theta)<br />
 <i>3D only: rotate a vector about the x axis by an angle theta </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>rotateY</code> (<code>CoordType</code> theta)<br />
 <i>3D only: rotate a vector about the y axis by an angle theta </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>rotateZ</code> (<code>CoordType</code> theta)<br />
 <i>3D only: rotate a vector about the z axis by an angle theta </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>rotate</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis, <code>CoordType</code> theta)<br />
 <i>3D only: rotate a vector about the i&#8217;th axis by an angle theta </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>rotate</code> (const <code>Quaternion</code> &amp;q)<br />
 <i>3D only: rotate a vector using a </i><code>Quaternion</code><br />
 <code>CoordType</code> <code>x</code> () const<br />
 <i>Access the first component of a vector. </i><br />
 <code>CoordType</code> &amp; <code>x</code> ()<br />
 <i>Access the first component of a vector. </i><br />
 <code>CoordType</code> <code>y</code> () const<br />
 <i>Access the second component of a vector. </i><br />
 <code>CoordType</code> &amp; <code>y</code> ()<br />
 <i>Access the second component of a vector. </i><br />
 <code>CoordType</code> <code>z</code> () const<br />
 <i>Access the third component of a vector. </i><br />
 <code>CoordType</code> &amp; <code>z</code> ()<br />
 <i>Access the third component of a vector. </i><br />
 <code>Vector</code> &amp; <code>mirrorX</code> ()<br />
 <i>Flip the x component of a vector. </i><br />
 <code>Vector</code> &amp; <code>mirrorY</code> ()<br />
 <i>Flip the y component of a vector. </i><br />
 <code>Vector</code> &amp; <code>mirrorZ</code> ()<br />
 <i>Flip the z component of a vector. </i><br />
 <code>Vector</code>&lt; 2 &gt; &amp; <code>polar</code> (<code>CoordType</code> r, <code>CoordType</code> theta)<br />
 <i>2D only: construct a vector from polar coordinates </i><br />
 void <code>asPolar</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta) const<br />
 <i>2D only: convert a vector to polar coordinates </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>polar</code> (<code>CoordType</code> r, <code>CoordType</code> theta, <code>CoordType</code> z)<br />
 <i>3D only: construct a vector from polar coordinates </i><br />
 void <code>asPolar</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta, <code>CoordType</code> &amp;z) const<br />
 <i>3D only: convert a vector to polar coordinates </i><br />
 <code>Vector</code>&lt; 3 &gt; &amp; <code>spherical</code> (<code>CoordType</code> r, <code>CoordType</code> theta, <code>CoordType</code> phi)<br />
 <i>3D only: construct a vector from shperical coordinates </i><br />
 void <code>asSpherical</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta, <code>CoordType</code> &amp;phi) const<br />
 <i>3D only: convert a vector to shperical coordinates </i></p>
<h3>Static Public Member Functions</h3>
<p>static const <code>Vector</code>&lt; dim &gt; &amp; <code>ZERO</code> ()<br />
 <i>Provides a global instance preset to zero. </i><br />
 static const <code>CoordType</code> <code>sloppyMagMax</code> ()<br />
 <i>The maximum ratio of the return value of </i><code>sloppyMag()</code> to the true magnitude.<br />
 static const <code>CoordType</code> <code>sloppyMagMaxSqrt</code> ()<br />
 <i>The square root of </i><code>sloppyMagMax()</code>.</p>
<h3>Friends</h3>
<p><code>Vector</code> &amp; <code>operator+=</code> (<code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2)<br />
 <i>Add the second vector to the first. </i><br />
 <code>Vector</code> &amp; <code>operator-=</code> (<code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2)<br />
 <i>Subtract the second vector from the first. </i><br />
 <code>Vector</code> &amp; <code>operator*=</code> (<code>Vector</code> &amp;v, <code>CoordType</code> d)<br />
 <i>Multiply the magnitude of v by d. </i><br />
 <code>Vector</code> &amp; <code>operator/=</code> (<code>Vector</code> &amp;v, <code>CoordType</code> d)<br />
 <i>Divide the magnitude of v by d. </i><br />
 <code>Vector</code> <code>operator+</code> (const <code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2)<br />
 <i>Take the sum of two vectors. </i><br />
 <code>Vector</code> <code>operator-</code> (const <code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2)<br />
 <i>Take the difference of two vectors. </i><br />
 <code>Vector</code> <code>operator-</code> (const <code>Vector</code> &amp;v)<br />
 <i>Reverse the direction of a vector. </i><br />
 <code>Vector</code> <code>operator*</code> (<code>CoordType</code> d, const <code>Vector</code> &amp;v)<br />
 <i>Multiply a vector by a scalar. </i><br />
 <code>Vector</code> <code>operator*</code> (const <code>Vector</code> &amp;v, <code>CoordType</code> d)<br />
 <i>Multiply a vector by a scalar. </i><br />
 <code>Vector</code> <code>operator/</code> (const <code>Vector</code> &amp;v, <code>CoordType</code> d)<br />
 <i>Divide a vector by a scalar. </i><br />
 <code>Vector</code> <code>Prod</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Vector</code> &amp;v)<br />
 <i>returns m * v </i><br />
 <code>Vector</code> <code>InvProd</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Vector</code> &amp;v)<br />
 <i>returns m^-1 * v </i><br />
 <code>Vector</code> <code>operator-</code> (const <code>Point</code>&lt; dim &gt; &amp;c1, const <code>Point</code>&lt; dim &gt; &amp;c2)<br />
 <i>Find the vector which gives the offset between two points. </i><br />
 <code>Point</code>&lt; dim &gt; <code>operator+</code> (const <code>Point</code>&lt; dim &gt; &amp;c, const <code>Vector</code> &amp;v)<br />
 <i>Find the point at the offset v from the point c. </i><br />
 <code>Point</code>&lt; dim &gt; <code>operator-</code> (const <code>Point</code>&lt; dim &gt; &amp;c, const <code>Vector</code> &amp;v)<br />
 <i>Find the point at the offset -v from the point c. </i><br />
 <code>Point</code>&lt; dim &gt; <code>operator+</code> (const <code>Vector</code> &amp;v, const <code>Point</code>&lt; dim &gt; &amp;c)<br />
 <i>Find the point at the offset v from the point c. </i><br />
 <code>Point</code>&lt; dim &gt; &amp; <code>operator+=</code> (<code>Point</code>&lt; dim &gt; &amp;p, const <code>Vector</code> &amp;rhs)<br />
 <i>Shift a point by a vector. </i><br />
 <code>Point</code>&lt; dim &gt; &amp; <code>operator-=</code> (<code>Point</code>&lt; dim &gt; &amp;p, const <code>Vector</code> &amp;rhs)<br />
 <i>Shift a point by a vector, in the opposite direction. </i><br />
 <code>CoordType</code> <code>Dot</code> (const <code>Vector</code> &amp;v1, const <code>Vector</code> &amp;v2)<br />
 <i>The dot product of two vectors. </i><br />
 <code>CoordType</code> <code>Angle</code> (const <code>Vector</code> &amp;v, const <code>Vector</code> &amp;u)<br />
 <i>The angle between two vectors. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::Vector&lt; dim &gt;</h3>
<p>A dim dimensional vector. </p>
<p> This class implements the &#8216;generic&#8217; subset of the interface in the fake class <code>Shape</code>.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;const int dim&gt; <code>Vector</code>&amp; <code>WFMath::Vector</code>&lt; dim &gt;::mirror () [inline]</h3>
<p>Reflect a vector in all directions simultaneously. </p>
<p> This is a nice way to implement the parity operation if dim is odd. </p>
<p> Referenced by WFMath::Vector&lt; 3 &gt;::mirrorX(), WFMath::Vector&lt; 3 &gt;::mirrorY(), and WFMath::Vector&lt; 3 &gt;::mirrorZ().</p>
<h3>template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; &amp; <code>WFMath::Vector</code>&lt; dim &gt;::rotate (const <code>Vector</code>&lt; dim &gt; &amp; v1, const <code>Vector</code>&lt; dim &gt; &amp; v2, <code>CoordType</code> theta) [inline]</h3>
<p>Rotate the vector in the (v1, v2) plane by the angle theta. </p>
<p> This throws CollinearVectors if v1 and v2 are parallel. </p>
<p> References WFMath::Vector&lt; dim &gt;::Prod, and WFMath::RotMatrix&lt; dim &gt;::rotation().</p>
<h3>template&lt;const int dim&gt; <code>CoordType</code> <code>WFMath::Vector</code>&lt; dim &gt;::sloppyMag () const</h3>
<p>An approximation to the magnitude of a vector. </p>
<p> The <code>sloppyMag()</code> function gives a value between the true magnitude and sloppyMagMax multiplied by the true magnitude. <code>sloppyNorm()</code> uses <code>sloppyMag()</code> to normalize the vector. This is currently only implemented for dim = {1, 2, 3}. For all current implementations, sloppyMagMax is greater than or equal to one. The constant sloppyMagMaxSqrt is provided for those who want to most closely approximate the true magnitude, without caring whether it&#8217;s too low or too high. </p>
<p> Referenced by WFMath::Vector&lt; dim &gt;::sloppyNorm().</p>
<h3>template&lt;const int dim&gt; static const <code>CoordType</code> <code>WFMath::Vector</code>&lt; dim &gt;::sloppyMagMaxSqrt () [static]</h3>
<p>The square root of <code>sloppyMagMax()</code>. </p>
<p> This is provided for people who want to obtain maximum accuracy from <code>sloppyMag()</code>, without caring whether the answer is high or low. The result <code>sloppyMag()</code>/sloppyMagMaxSqrt() will be within <code>sloppyMagMaxSqrt()</code> of the true magnitude.</p>
<h3>template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; &amp; <code>WFMath::Vector</code>&lt; dim &gt;::sloppyNorm (<code>CoordType</code> norm = 1.0) [inline]</h3>
<p>Approximately normalize a vector. </p>
<p> Normalize a vector using <code>sloppyMag()</code> instead of the true magnitude. The new length of the vector will be between norm/sloppyMagMax() and norm. </p>
<p> References WFMath::Vector&lt; dim &gt;::mag(), and WFMath::Vector&lt; dim &gt;::sloppyMag(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
