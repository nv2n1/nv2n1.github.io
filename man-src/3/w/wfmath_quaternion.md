---
title: "wfmath_quaternion(3)"
name: "wfmath_quaternion"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_quaternion/"
description: "WFMath::Quaternion – A normalized quaterion."
---

<p>WFMath::Quaternion &#8211; A normalized quaterion. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/quaternion.h">quaternion.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Quaternion</code> ()<br />
 <i>Construct a Quatertion. </i><br />
 <code>Quaternion</code> (<code>CoordType</code> w_in, <code>CoordType</code> x_in, <code>CoordType</code> y_in, <code>CoordType</code> z_in)<br />
 <i>Construct a </i><code>Quaternion</code> from (w, x, y, z) components.<br />
 <code>Quaternion</code> (int axis, <code>CoordType</code> angle)<br />
 <i>Construct a </i><code>Quaternion</code> giving a rotation around axis by angle.<br />
 <code>Quaternion</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis, <code>CoordType</code> angle)<br />
 <i>Construct a </i><code>Quaternion</code> giving a rotation around the <code>Vector</code> axis by angle.<br />
 <code>Quaternion</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis)<br />
 <i>Construct a </i><code>Quaternion</code> giving a rotation around the <code>Vector</code> axis.<br />
 <code>Quaternion</code> (const <code>Quaternion</code> &amp;p)<br />
 <i>Construct a copy of a </i><code>Quaternion</code>.<br />
 <code>Quaternion</code> (const AtlasInType &amp;a)<br />
 <i>Construct a </i><code>Quaternion</code> from an Atlas::Message::Object.<br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the </i><code>Quaternion</code>.<br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the Quaternion&#8217;s value to that given by an Atlas object. </i><br />
 <code>Quaternion</code> &amp; <code>identity</code> ()<br />
 <i>Set the </i><code>Quaternion</code> to the identity rotation.<br />
 bool <code>fromRotMatrix</code> (const <code>RotMatrix</code>&lt; 3 &gt; &amp;m)<br />
 <i>set a Quaternion&#8217;s value from a </i><code>RotMatrix</code><br />
 <code>Quaternion</code> <code>inverse</code> () const<br />
 <i>returns the inverse of the </i><code>Quaternion</code><br />
 <code>Quaternion</code> &amp; <code>rotate</code> (const <code>RotMatrix</code>&lt; 3 &gt; &amp;)<br />
 <i>Rotate quaternion using the matrix. </i><br />
 <code>Quaternion</code> &amp; <code>rotate</code> (const <code>Quaternion</code> &amp;q)<br />
 <i>rotate the quaternion using another quaternion </i><br />
 <code>Quaternion</code> &amp; <code>rotation</code> (int axis, <code>CoordType</code> angle)<br />
 <i>sets the </i><code>Quaternion</code> to a rotation by angle around axis<br />
 <code>Quaternion</code> &amp; <code>rotation</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis, <code>CoordType</code> angle)<br />
 <i>sets the </i><code>Quaternion</code> to a rotation by angle around the <code>Vector</code> axis<br />
 <code>Quaternion</code> &amp; <code>rotation</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis)<br />
 <i>sets the </i><code>Quaternion</code> to a rotation around the <code>Vector</code> axis<br />
 <code>Quaternion</code> &amp; <code>rotation</code> (const <code>Vector</code>&lt; 3 &gt; &amp;from, const <code>Vector</code>&lt; 3 &gt; &amp;to)<br />
 <i>sets the </i><code>Quaternion</code> to rotate &#8216;from&#8217; to be parallel to &#8216;to&#8217;<br />
 <code>CoordType</code> <code>scalar</code> () const<br />
 <i>returns the scalar (w) part of the </i><code>Quaternion</code><br />
 const <code>Vector</code>&lt; 3 &gt; &amp; <code>vector</code> () const<br />
 <i>returns the </i><code>Vector</code> (x, y, z) part of the quaternion<br />
 void <code>normalize</code> ()<br />
 <i>normalize to remove accumulated round-off error </i><br />
 unsigned <code>age</code> () const<br />
 <i>current round-off age </i></p>
<h2>Detailed Description</h2>
<p>A normalized quaterion. </p>
<p> This class implements the &#8216;generic&#8217; subset of the interface in the fake class <code>Shape</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>WFMath::Quaternion::Quaternion (<code>CoordType</code> w_in, <code>CoordType</code> x_in, <code>CoordType</code> y_in, <code>CoordType</code> z_in)</h3>
<p>Construct a <code>Quaternion</code> from (w, x, y, z) components. </p>
<p> This normalizes the components so the sum of their squares is one.</p>
<h3>WFMath::Quaternion::Quaternion (const <code>Vector</code>&lt; 3 &gt; &amp; axis) [inline, explicit]</h3>
<p>Construct a <code>Quaternion</code> giving a rotation around the <code>Vector</code> axis. </p>
<p> The angle of rotating is equal to the magnitude of the <code>Vector</code> </p>
<p> References rotation().</p>
<h2>Member Function Documentation</h2>
<h3>bool WFMath::Quaternion::fromRotMatrix (const <code>RotMatrix</code>&lt; 3 &gt; &amp; m)</h3>
<p>set a Quaternion&#8217;s value from a <code>RotMatrix</code> </p>
<p> Since a <code>Quaternion</code> can only represent an even-parity <code>RotMatrix</code>, this function returns false if the parity of m is odd. In this case, the quaternion is set to the value of m multiplied by a fixed parity-odd <code>RotMatrix</code>, so the full <code>RotMatrix</code> can be recovered by passing the <code>Quaternion</code> and the value of &#8216;not_flip&#8217; returned by this function to <code>RotMatrix::fromQuaternion()</code>.</p>
<h3><code>Quaternion</code>&amp; WFMath::Quaternion::rotation (const <code>Vector</code>&lt; 3 &gt; &amp; axis)</h3>
<p>sets the <code>Quaternion</code> to a rotation around the <code>Vector</code> axis </p>
<p> The rotation angle is given by the magnitude of the <code>Vector</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
