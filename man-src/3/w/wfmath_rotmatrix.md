---
title: "wfmath_rotmatrix(3)"
name: "wfmath_rotmatrix"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_rotmatrix/"
description: "WFMath::RotMatrix – A dim dimensional rotation matrix. Technically, a member of the group O(dim)."
---

<p>WFMath::RotMatrix &#8211; A dim dimensional rotation matrix. Technically, a member of the group O(dim). </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/rotmatrix.h">rotmatrix.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>RotMatrix</code> &amp; <code>identity</code> ()<br />
 <i>set the matrix to the identity matrix </i><br />
 <code>CoordType</code> <code>elem</code> (const int i, const int j) const<br />
 <i>get the (i, j) element of the matrix </i><br />
 bool <code>setVals</code> (const <code>CoordType</code> vals[dim][dim], double precision=WFMATH_EPSILON)<br />
 <i>Set the values of the elements of the matrix. </i><br />
 bool <code>setVals</code> (const <code>CoordType</code> vals[dim *dim], double precision=WFMATH_EPSILON)<br />
 <i>Set the values of the elements of the matrix. </i><br />
 <code>Vector</code>&lt; dim &gt; <code>row</code> (const int i) const<br />
 <i>Get a copy of the i&#8217;th row as a </i><code>Vector</code>.<br />
 <code>Vector</code>&lt; dim &gt; <code>column</code> (const int i) const<br />
 <i>Get a copy of the i&#8217;th column as a </i><code>Vector</code>.<br />
 <code>CoordType</code> <code>trace</code> () const<br />
 <i>Get the trace of the matrix. </i><br />
 <code>CoordType</code> <code>determinant</code> () const<br />
 <i>Get the determinant of the matrix. </i><br />
 <code>RotMatrix</code> <code>inverse</code> () const<br />
 <i>Get the inverse of the matrix. </i><br />
 bool <code>parity</code> () const<br />
 <i>Get the parity of the matrix. </i><br />
 <code>RotMatrix</code> &amp; <code>rotation</code> (const int i, const int j, <code>CoordType</code> theta)<br />
 <i>set the matrix to a rotation by the angle theta in the (i, j) plane </i><br />
 <code>RotMatrix</code> &amp; <code>rotation</code> (const <code>Vector</code>&lt; dim &gt; &amp;v1, const <code>Vector</code>&lt; dim &gt; &amp;v2, <code>CoordType</code> theta)<br />
 <i>set the matrix to a rotation by the angle theta in the v1, v2 plane </i><br />
 <code>RotMatrix</code> &amp; <code>rotation</code> (const <code>Vector</code>&lt; dim &gt; &amp;from, const <code>Vector</code>&lt; dim &gt; &amp;to)<br />
 <i>set the matrix to a rotation which will move &#8216;from&#8217; to lie parallel to &#8216;to&#8217; </i><br />
 <code>RotMatrix</code> &amp; <code>mirror</code> (const int i)<br />
 <i>set the matrix to a mirror perpendicular to the i&#8217;th axis </i><br />
 <code>RotMatrix</code> &amp; <code>mirror</code> (const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>set the matrix to a mirror perpendicular to the </i><code>Vector</code> v<br />
 <code>RotMatrix</code> &amp; <code>mirror</code> ()<br />
 <i>set the matrix to mirror all axes </i><br />
 <code>RotMatrix</code> &amp; <code>rotate</code> (const <code>RotMatrix</code> &amp;m)<br />
 <i>rotate the matrix using another matrix </i><br />
 void <code>normalize</code> ()<br />
 <i>normalize to remove accumulated round-off error </i><br />
 unsigned <code>age</code> () const<br />
 <i>current round-off age </i><br />
 <code>RotMatrix</code> (const <code>Quaternion</code> &amp;q, const bool not_flip=true)<br />
 <i>3D only: Construct a </i><code>RotMatrix</code> from a <code>Quaternion</code><br />
 <code>RotMatrix</code>&lt; 2 &gt; &amp; <code>rotation</code> (<code>CoordType</code> theta)<br />
 <i>2D only: Construct a </i><code>RotMatrix</code> from an angle theta<br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotationX</code> (<code>CoordType</code> theta)<br />
 <i>3D only: set a </i><code>RotMatrix</code> to a rotation about the x axis by angle theta<br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotationY</code> (<code>CoordType</code> theta)<br />
 <i>3D only: set a </i><code>RotMatrix</code> to a rotation about the y axis by angle theta<br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotationZ</code> (<code>CoordType</code> theta)<br />
 <i>3D only: set a </i><code>RotMatrix</code> to a rotation about the z axis by angle theta<br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotation</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis, <code>CoordType</code> theta)<br />
 <i>3D only: set a </i><code>RotMatrix</code> to a rotation about the axis given by the <code>Vector</code><br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotation</code> (const <code>Vector</code>&lt; 3 &gt; &amp;axis)<br />
 <i>3D only: set a </i><code>RotMatrix</code> to a rotation about the axis given by the <code>Vector</code><br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>fromQuaternion</code> (const <code>Quaternion</code> &amp;q, const bool not_flip=true)<br />
 <i>3D only: set a </i><code>RotMatrix</code> from a <code>Quaternion</code><br />
 <code>RotMatrix</code>&lt; 3 &gt; &amp; <code>rotate</code> (const <code>Quaternion</code> &amp;)<br />
 <i>rotate the matrix using the quaternion </i><br />
 <code>RotMatrix</code> &amp; <code>mirrorX</code> ()<br />
 <i>set a </i><code>RotMatrix</code> to a mirror perpendicular to the x axis<br />
 <code>RotMatrix</code> &amp; <code>mirrorY</code> ()<br />
 <i>set a </i><code>RotMatrix</code> to a mirror perpendicular to the y axis<br />
 <code>RotMatrix</code> &amp; <code>mirrorZ</code> ()<br />
 <i>set a </i><code>RotMatrix</code> to a mirror perpendicular to the z axis</p>
<h3>Friends</h3>
<p><code>RotMatrix</code> <code>Prod</code> (const <code>RotMatrix</code> &amp;m1, const <code>RotMatrix</code> &amp;m2)<br />
 <i>returns m1 * m2 </i><br />
 <code>RotMatrix</code> <code>ProdInv</code> (const <code>RotMatrix</code> &amp;m1, const <code>RotMatrix</code> &amp;m2)<br />
 <i>returns m1 * m2^-1 </i><br />
 <code>RotMatrix</code> <code>InvProd</code> (const <code>RotMatrix</code> &amp;m1, const <code>RotMatrix</code> &amp;m2)<br />
 <i>returns m1^-1 * m2 </i><br />
 <code>RotMatrix</code> <code>InvProdInv</code> (const <code>RotMatrix</code> &amp;m1, const <code>RotMatrix</code> &amp;m2)<br />
 <i>returns m1^-1 * m2^-1 </i><br />
 <code>Vector</code>&lt; dim &gt; <code>Prod</code> (const <code>RotMatrix</code> &amp;m, const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>returns m * v </i><br />
 <code>Vector</code>&lt; dim &gt; <code>InvProd</code> (const <code>RotMatrix</code> &amp;m, const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>returns m^-1 * v </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::RotMatrix&lt; dim &gt;</h3>
<p>A dim dimensional rotation matrix. Technically, a member of the group O(dim). </p>
<p> Elements of this class represent rotation matrices. The NxN dimensional rotation matrices form a group called O(N), the orthogonal matrices. They satisfy the following condition: </p>
<p> They are orthogonal. That is, their transpose is equal to their inverse. Hence, this class does not implement a transpose() method, only an <code>inverse()</code>. </p>
<p> A general N dimensional matrix of this type has N(N-1)/2 degrees of freedom. This gives one rotation angle in 2D, the three Euler angles in 3D, etc. </p>
<p> This class implements the &#8216;generic&#8217; subset of the interface in the fake class <code>Shape</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;const int dim&gt; <code>WFMath::RotMatrix</code>&lt; dim &gt;::<code>RotMatrix</code> (const <code>Quaternion</code> &amp; q, const bool not_flip = true) [inline]</h3>
<p>3D only: Construct a <code>RotMatrix</code> from a <code>Quaternion</code> </p>
<p> since Quaternions can only specify parity-even rotations, you can pass the return value of <code>Quaternion::fromRotMatrix()</code> as not_flip to recover the full <code>RotMatrix</code> </p>
<p> References WFMath::RotMatrix&lt; dim &gt;::fromQuaternion().</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;const int dim&gt; <code>CoordType</code> <code>WFMath::RotMatrix</code>&lt; dim &gt;::determinant () const [inline]</h3>
<p>Get the determinant of the matrix. </p>
<p> Since the matrix is orthogonal, the determinant is always either 1 or -1.</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt;3&gt;&amp; <code>WFMath::RotMatrix</code>&lt; dim &gt;::fromQuaternion (const <code>Quaternion</code> &amp; q, const bool not_flip = true)</h3>
<p>3D only: set a <code>RotMatrix</code> from a <code>Quaternion</code> </p>
<p> since Quaternions can only specify parity-even rotations, you can pass the return value of <code>Quaternion::fromRotMatrix()</code> as not_flip to recover the full <code>RotMatrix</code> </p>
<p> Referenced by WFMath::RotMatrix&lt; dim &gt;::RotMatrix().</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>WFMath::RotMatrix</code>&lt; dim &gt;::inverse () const [inline]</h3>
<p>Get the inverse of the matrix. </p>
<p> Since the matrix is orthogonal, the inverse is equal to the transpose.</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; &amp; <code>WFMath::RotMatrix</code>&lt; dim &gt;::mirror () [inline]</h3>
<p>set the matrix to mirror all axes </p>
<p> This is a good parity operator if dim is odd. </p>
<p> Referenced by WFMath::RotMatrix&lt; dim &gt;::mirrorX(), WFMath::RotMatrix&lt; dim &gt;::mirrorY(), and WFMath::RotMatrix&lt; dim &gt;::mirrorZ().</p>
<h3>template&lt;const int dim&gt; bool <code>WFMath::RotMatrix</code>&lt; dim &gt;::parity () const [inline]</h3>
<p>Get the parity of the matrix. </p>
<p> Returns true for odd parity, false for even.</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt;3&gt;&amp; <code>WFMath::RotMatrix</code>&lt; dim &gt;::rotation (const <code>Vector</code>&lt; 3 &gt; &amp; axis)</h3>
<p>3D only: set a <code>RotMatrix</code> to a rotation about the axis given by the <code>Vector</code> </p>
<p> the rotation angle is taken from the Vector&#8217;s magnitude</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; &amp; <code>WFMath::RotMatrix</code>&lt; dim &gt;::rotation (const <code>Vector</code>&lt; dim &gt; &amp; from, const <code>Vector</code>&lt; dim &gt; &amp; to) [inline]</h3>
<p>set the matrix to a rotation which will move &#8216;from&#8217; to lie parallel to &#8216;to&#8217; </p>
<p> Throws CollinearVectors if v1 and v2 are antiparallel (parallel but pointing in opposite directions). If v1 and v2 point in the same direction, the matrix is set to the identity. </p>
<p> References WFMath::Vector&lt; dim &gt;::sqrMag().</p>
<h3>template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; &amp; <code>WFMath::RotMatrix</code>&lt; dim &gt;::rotation (const <code>Vector</code>&lt; dim &gt; &amp; v1, const <code>Vector</code>&lt; dim &gt; &amp; v2, <code>CoordType</code> theta) [inline]</h3>
<p>set the matrix to a rotation by the angle theta in the v1, v2 plane </p>
<p> Throws CollinearVectors if v1 and v2 are parallel </p>
<p> References WFMath::RotMatrix&lt; dim &gt;::identity(), and WFMath::Vector&lt; dim &gt;::sqrMag().</p>
<h3>template&lt;const int dim&gt; bool <code>WFMath::RotMatrix</code>&lt; dim &gt;::setVals (const <code>CoordType</code> vals[dim *dim], double precision = WFMATH_EPSILON) [inline]</h3>
<p>Set the values of the elements of the matrix. </p>
<p> Can&#8217;t set one element at a time and keep it an O(N) matrix, but can try to set all values at once, and see if they match. This fails if the passed matrix is not orthogonal within the passed precision, and orthogonalizes the matrix to within precision WFMATH_EPSILON.</p>
<h3>template&lt;const int dim&gt; bool <code>WFMath::RotMatrix</code>&lt; dim &gt;::setVals (const <code>CoordType</code> vals[dim][dim], double precision = WFMATH_EPSILON) [inline]</h3>
<p>Set the values of the elements of the matrix. </p>
<p> Can&#8217;t set one element at a time and keep it an O(N) matrix, but can try to set all values at once, and see if they match. This fails if the passed matrix is not orthogonal within the passed precision, and orthogonalizes the matrix to within precision WFMATH_EPSILON. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
