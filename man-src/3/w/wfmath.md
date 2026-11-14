---
title: "wfmath(3)"
name: "wfmath"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath/"
description: "WFMath – Generic library namespace."
---

<p>WFMath &#8211; Generic library namespace. </p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>AxisBox</code><br />
 <i>A dim dimensional axis-aligned box. </i><br />
 class <code>Ball</code><br />
 <i>A dim dimensional ball. </i><br />
 struct <code>ColinearVectors</code><br />
 <i>An error thrown by certain functions when passed parallel vectors. </i><br />
 struct <code>ParseError</code><br />
 <i>An error thrown by operator&gt;&gt;() when it fails to parse wfmath types. </i><br />
 class <code>Point</code><br />
 <i>A dim dimensional point. </i><br />
 class <code>Polygon&lt; 2 &gt;</code><br />
 <i>The 2D specialization of the Polygon&lt;&gt; template. </i><br />
 class <code>Polygon</code><br />
 <i>A polygon, all of whose points lie in a plane, embedded in dim dimensions. </i><br />
 class <code>Quaternion</code><br />
 <i>A normalized quaterion. </i><br />
 class <code>RotBox</code><br />
 <i>A dim dimensional box, lying at an arbitrary angle. </i><br />
 class <code>RotMatrix</code><br />
 <i>A dim dimensional rotation matrix. Technically, a member of the group O(dim). </i><br />
 class <code>Segment</code><br />
 <i>A line segment embedded in dim dimensions. </i><br />
 class <code>TimeDiff</code><br />
 <i>The difference between two timestamps. </i><br />
 class <code>TimeStamp</code><br />
 <i>A time stamp. </i><br />
 class <code>Vector</code><br />
 <i>A dim dimensional vector. </i><br />
 class <code>ZeroPrimitive</code><br />
 <i>Utility class for providing zero primitives. This class will only work with simple structures such as </i><code>Vector</code> or <code>Point</code> which provide a m_elem structure. In order for it to access the m_elem structure it must be declared as a friend class of the class it will provide an instance of.<br />
 class <code>Shape</code><br />
 <i>A fake class which documents the generic parts of the </i><code>WFMath</code> interface.</p>
<h3>Typedefs</h3>
<p>typedef float <code>CoordType</code><br />
 <i>Basic floating point type. </i></p>
<h3>Functions</h3>
<p>template&lt;const int dim, template&lt; class, class &gt; class container&gt; <code>AxisBox</code>&lt; dim &gt; <code>BoundingBox</code> (const container&lt; <code>AxisBox</code>&lt; dim &gt;, std::allocator&lt; <code>AxisBox</code>&lt; dim &gt; &gt; &gt; &amp;c)<br />
 <i>Get the axis-aligned bounding box for a set of boxes. </i><br />
 template&lt;const int dim, template&lt; class, class &gt; class container&gt; <code>AxisBox</code>&lt; dim &gt; <code>BoundingBox</code> (const container&lt; <code>Point</code>&lt; dim &gt;, std::allocator&lt; <code>Point</code>&lt; dim &gt; &gt; &gt; &amp;c)<br />
 <i>Get the axis-aligned bounding box for a set of points. </i><br />
 template&lt;const int dim, template&lt; class, class &gt; class container&gt; <code>Ball</code>&lt; dim &gt; <code>BoundingSphere</code> (const container&lt; <code>Point</code>&lt; dim &gt;, std::allocator&lt; <code>Point</code>&lt; dim &gt; &gt; &gt; &amp;c)<br />
 <i>get the minimal bounding sphere for a set of points </i><br />
 template&lt;const int dim, template&lt; class, class &gt; class container&gt; <code>Ball</code>&lt; dim &gt; <code>BoundingSphereSloppy</code> (const container&lt; <code>Point</code>&lt; dim &gt;, std::allocator&lt; <code>Point</code>&lt; dim &gt; &gt; &gt; &amp;c)<br />
 <i>get a bounding sphere for a set of points </i><br />
 template&lt;class C &gt; bool <code>Equal</code> (const C &amp;c1, const C &amp;c2, double epsilon=WFMATH_EPSILON)<br />
 <i>Test for equality up to precision epsilon. </i><br />
 template&lt;const int dim, template&lt; class, class &gt; class container&gt; <code>Point</code>&lt; dim &gt; <code>Barycenter</code> (const container&lt; <code>Point</code>&lt; dim &gt;, std::allocator&lt; <code>Point</code>&lt; dim &gt; &gt; &gt; &amp;c)<br />
 <i>Find the center of a set of points, all weighted equally. </i><br />
 template&lt;const int dim, template&lt; class, class &gt; class container, template&lt; class, class &gt; class container2&gt; <code>Point</code>&lt; dim &gt; <code>Barycenter</code> (const container&lt; <code>Point</code>&lt; dim &gt;, std::allocator&lt; <code>Point</code>&lt; dim &gt; &gt; &gt; &amp;c, const container2&lt; <code>CoordType</code>, std::allocator&lt; <code>CoordType</code> &gt; &gt; &amp;weights)<br />
 <i>Find the center of a set of points with the given weights. </i><br />
 template&lt;const int dim&gt; <code>Point</code>&lt; dim &gt; <code>Midpoint</code> (const <code>Point</code>&lt; dim &gt; &amp;p1, const <code>Point</code>&lt; dim &gt; &amp;p2, <code>CoordType</code> dist=0.5) </p>
<p> double <code>GaussianConditional</code> (double mean, double stddev, double val)<br />
 <i>Gives the conditional probability of the Gaussian distribution at position val. </i><br />
 double <code>Gaussian</code> (double mean, double stddev, double val)<br />
 <i>Gives the value of the Gaussian distribution at position val. </i><br />
 double <code>PoissonConditional</code> (double mean, unsigned int step)<br />
 <i>Gives the conditional probability of the Poisson distribution at position step. </i><br />
 double <code>Poisson</code> (double mean, unsigned int step)<br />
 <i>Gives the value of the Poisson distribution at position step. </i><br />
 double <code>LogFactorial</code> (unsigned int n)<br />
 <i>Gives the natural log of n! </i><br />
 double <code>Factorial</code> (unsigned int n)<br />
 <i>Gives n! </i><br />
 double <code>LogGamma</code> (double z)<br />
 <i>The natural log of Euler&#8217;s Gamma function. </i><br />
 double <code>Gamma</code> (double z)<br />
 <i>Euler&#8217;s Gamma function. </i><br />
 template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>Prod</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m1, const <code>RotMatrix</code>&lt; dim &gt; &amp;m2)<br />
 <i>returns m1 * m2 </i><br />
 template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>ProdInv</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m1, const <code>RotMatrix</code>&lt; dim &gt; &amp;m2)<br />
 <i>returns m1 * m2^-1 </i><br />
 template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>InvProd</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m1, const <code>RotMatrix</code>&lt; dim &gt; &amp;m2)<br />
 <i>returns m1^-1 * m2 </i><br />
 template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>InvProdInv</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m1, const <code>RotMatrix</code>&lt; dim &gt; &amp;m2)<br />
 <i>returns m1^-1 * m2^-1 </i><br />
 template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; <code>Prod</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>returns m * v </i><br />
 template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; <code>InvProd</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Vector</code>&lt; dim &gt; &amp;v)<br />
 <i>returns m^-1 * v </i><br />
 template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; <code>Prod</code> (const <code>Vector</code>&lt; dim &gt; &amp;v, const <code>RotMatrix</code>&lt; dim &gt; &amp;m)<br />
 <i>returns v * m </i><br />
 template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; <code>ProdInv</code> (const <code>Vector</code>&lt; dim &gt; &amp;v, const <code>RotMatrix</code>&lt; dim &gt; &amp;m)<br />
 <i>return v * m^-1 </i><br />
 template&lt;const int dim&gt; <code>RotMatrix</code>&lt; dim &gt; <code>operator*</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m1, const <code>RotMatrix</code>&lt; dim &gt; &amp;m2)<br />
 <i>returns m1 * m2 </i><br />
 template&lt;class C &gt; void <code>Shuffle</code> (std::vector&lt; C &gt; &amp;v)<br />
 <i>Randomly reorder the contents of a std::vector. </i><br />
 template&lt;class C &gt; std::string <code>ToString</code> (const C &amp;c, unsigned int precision=6)<br />
 <i>Output a </i><code>WFMath</code> type as a string.<br />
 template&lt;class C &gt; void <code>FromString</code> (C &amp;c, const std::string &amp;s, unsigned int precision=6)<br />
 <i>Parse a </i><code>WFMath</code> type from a string.<br />
 <code>CoordType</code> <code>Cross</code> (const <code>Vector</code>&lt; 2 &gt; &amp;v1, const <code>Vector</code>&lt; 2 &gt; &amp;v2)<br />
 <i>2D only: get the z component of the cross product of two vectors </i><br />
 <code>Vector</code>&lt; 3 &gt; <code>Cross</code> (const <code>Vector</code>&lt; 3 &gt; &amp;v1, const <code>Vector</code>&lt; 3 &gt; &amp;v2)<br />
 <i>3D only: get the cross product of two vectors </i><br />
 template&lt;const int dim&gt; bool <code>Parallel</code> (const <code>Vector</code>&lt; dim &gt; &amp;v1, const <code>Vector</code>&lt; dim &gt; &amp;v2, bool &amp;same_dir)<br />
 <i>Check if two vectors are parallel. </i><br />
 template&lt;const int dim&gt; bool <code>Parallel</code> (const <code>Vector</code>&lt; dim &gt; &amp;v1, const <code>Vector</code>&lt; dim &gt; &amp;v2)<br />
 <i>Check if two vectors are parallel. </i><br />
 template&lt;const int dim&gt; bool <code>Perpendicular</code> (const <code>Vector</code>&lt; dim &gt; &amp;v1, const <code>Vector</code>&lt; dim &gt; &amp;v2)<br />
 <i>Check if two vectors are perpendicular. </i></p>
<h3>Variables</h3>
<p>const double <code>Pi</code> = 3.14159265358979323846264338327950288419716939937508<br />
 <i>The constant pi. </i><br />
 const double <code>SqrtPi</code> = 1.77245385090551602729816748334114518279754945612237<br />
 <i>The square root of pi. </i><br />
 const double <code>LogPi</code> = 1.14472988584940017414342735135305871164729481291530<br />
 <i>The natural logarithm of pi. </i><br />
 const double <code>Sqrt2</code> = 1.41421356237309504880168872420969807856967187537693<br />
 <i>The square root of 2. </i><br />
 const double <code>Sqrt3</code> = 1.73205080756887729352744634150587236694280525381037<br />
 <i>The square root of 3. </i><br />
 const double <code>Log2</code> = 0.69314718055994530941723212145817656807550013436025<br />
 <i>The natural logarithm of 2. </i></p>
<h2>Detailed Description</h2>
<p>Generic library namespace. </p>
<p> Timing related primitives in a portable fashion &#8211; note this is for interval / elapsed time measurement, not displaying a human readable time. </p>
<h2>Function Documentation</h2>
<h3>template&lt;const int dim, template&lt; class, class &gt; class container, template&lt; class, class &gt; class container2&gt; <code>Point</code>&lt; dim &gt; WFMath::Barycenter (const container&lt; Point&lt; dim &gt;, std::allocator&lt; Point&lt; dim &gt; &gt; &gt; &amp; c, const container2&lt; CoordType, std::allocator&lt; CoordType &gt; &gt; &amp; weights) [inline]</h3>
<p>Find the center of a set of points with the given weights. </p>
<p> If the number of points and the number of weights are not equal, the excess of either is ignored. The weights (or that subset which is used, if there are more weights than points), must not sum to zero. </p>
<p> References WFMath::Point&lt; dim &gt;::setValid().</p>
<h3>template&lt;class C &gt; bool WFMath::Equal (const C &amp; c1, const C &amp; c2, double epsilon = WFMATH_EPSILON) [inline]</h3>
<p>Test for equality up to precision epsilon. </p>
<p> Returns true if the difference between the numbers is less than epsilon. Note that epsilon is multiplied by 2 raised to the power of the exponent of the smaller number. So, for example, Equal(0.00010000, 0.00010002, 1.0e-4) will not compare equal, but Equal(0.00010000, 0.00010002, 1.0e-3) will. </p>
<p> Referenced by Parallel().</p>
<h3>template&lt;class C &gt; void WFMath::FromString (C &amp; c, const std::string &amp; s, unsigned int precision = 6) [inline]</h3>
<p>Parse a <code>WFMath</code> type from a string. </p>
<p> This uses operator&gt;&gt;() in its backend.</p>
<h3>double WFMath::GaussianConditional (double mean, double stddev, double val)</h3>
<p>Gives the conditional probability of the Gaussian distribution at position val. </p>
<p> The probability that a Gaussian random variable will fall between val and val + delta, given that it is already known to be not less than val, is given by this function multiplied by delta (for small delta).</p>
<h3>template&lt;const int dim&gt; <code>Point</code>&lt; dim &gt; WFMath::Midpoint (const Point&lt; dim &gt; &amp; p1, const Point&lt; dim &gt; &amp; p2, CoordType dist = 0.5) [inline]</h3>
<p>The default value of 0.5 for dist gives the midpoint. A value of 0 gives p1, and 1 gives p2. Values of dist outside the [0, 1] range are allowed, and give points on the line which are not on the segment bounded by p1 and p2. </p>
<p> Referenced by BoundingSphereSloppy().</p>
<h3>template&lt;const int dim&gt; bool WFMath::Parallel (const Vector&lt; dim &gt; &amp; v1, const Vector&lt; dim &gt; &amp; v2) [inline]</h3>
<p>Check if two vectors are parallel. </p>
<p> Convienience wrapper if you don&#8217;t care about same_dir </p>
<p> References Parallel().</p>
<h3>template&lt;const int dim&gt; bool WFMath::Parallel (const Vector&lt; dim &gt; &amp; v1, const Vector&lt; dim &gt; &amp; v2, bool &amp; same_dir) [inline]</h3>
<p>Check if two vectors are parallel. </p>
<p> Returns true if the vectors are parallel. For parallel vectors, same_dir is set to true if they point the same direction, and false if they point opposite directions </p>
<p> References Equal(), and WFMath::Vector&lt; dim &gt;::sqrMag(). </p>
<p> Referenced by Parallel().</p>
<h3>double WFMath::PoissonConditional (double mean, unsigned int step)</h3>
<p>Gives the conditional probability of the Poisson distribution at position step. </p>
<p> Returns the probability that a Poisson random variable will have value step, given that it is already known not to be less than step.</p>
<h3>template&lt;const int dim&gt; <code>Vector</code>&lt; dim &gt; WFMath::Prod (const Vector&lt; dim &gt; &amp; v, const RotMatrix&lt; dim &gt; &amp; m) [inline]</h3>
<p>returns v * m </p>
<p> This is the function to use to rotate a <code>Vector</code> v using a Matrix m </p>
<p> References InvProd().</p>
<h3>template&lt;class C &gt; void WFMath::Shuffle (std::vector&lt; C &gt; &amp; v) [inline]</h3>
<p>Randomly reorder the contents of a std::vector. </p>
<p> For things like shuffling a deck of cards, etc.</p>
<h3>template&lt;class C &gt; std::string WFMath::ToString (const C &amp; c, unsigned int precision = 6) [inline]</h3>
<p>Output a <code>WFMath</code> type as a string. </p>
<p> This uses operator&lt;&lt;() in its backend.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
