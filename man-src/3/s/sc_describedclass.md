---
title: "sc_describedclass(3)"
name: "sc_describedclass"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_describedclass/"
description: "sc::DescribedClass –"
---

<p>sc::DescribedClass &#8211; </p>
<p> Classes which need runtime information about themselves and their relationship to other classes can virtually inherit from <code>DescribedClass</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;class.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::AnimatedObject</code>, <code>sc::Appearance</code>, <code>sc::BEMSolvent</code>, <code>sc::DescribedClassProxy</code>, <code>sc::DiagSCMatrix</code>, <code>sc::FileGrp</code>, <code>sc::GlobalMsgIter</code>, <code>sc::IntegralStorer</code>, <code>sc::MachineTopology</code>, <code>sc::Material</code>, <code>sc::MemoryGrp</code>, <code>sc::MessageGrp</code>, <code>sc::MoleculeColorizer</code>, <code>sc::PsiExEnv</code>, <code>sc::RegionTimer</code>, <code>sc::Render</code>, <code>sc::RenderedObject</code>, <code>sc::SavableState</code>, <code>sc::SCMatrix</code>, <code>sc::SCMatrixKit</code>, <code>sc::SCVector</code>, <code>sc::StateIn</code>, <code>sc::StateOut</code>, <code>sc::SymmSCMatrix</code>, <code>sc::ThreadGrp</code>, <code>sc::Transform</code>, <code>sc::TriangleIntegrator</code>, and <code>sc::TriangulatedSurface</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DescribedClass</code> (const <code>DescribedClass</code> &amp;) </p>
<p> <code>DescribedClass</code> &amp; <code>operator=</code> (const <code>DescribedClass</code> &amp;) </p>
<p> <code>ClassDesc</code> * <code>class_desc</code> () const throw ()<br />
 <i>This returns the unique pointer to the </i><code>ClassDesc</code> corresponding to the given type_info object.<br />
 const char * <code>class_name</code> () const<br />
 <i>Return the name of the object&#8217;s exact type. </i><br />
 int <code>class_version</code> () const<br />
 <i>Return the version of the class. </i><br />
 virtual void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the object. </i></p>
<h2>Detailed Description</h2>
<p>Classes which need runtime information about themselves and their relationship to other classes can virtually inherit from <code>DescribedClass</code>. </p>
<p> This will provide the class with the ability to query its name and its version. Furthermore, the class&#8217;s static <code>ClassDesc</code> can be obtained which permits several other operations. See <code>class</code> for more information.</p>
<h2>Member Function Documentation</h2>
<h3><code>ClassDesc</code>* sc::DescribedClass::class_desc () const throw ()</h3>
<p>This returns the unique pointer to the <code>ClassDesc</code> corresponding to the given type_info object. Null is returned if it fails.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
