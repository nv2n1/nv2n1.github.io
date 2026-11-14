---
title: "sc_refcount(3)"
name: "sc_refcount"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refcount/"
description: "sc::RefCount –"
---

<p>sc::RefCount &#8211; </p>
<p> The base class for all reference counted objects.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;ref.h&gt;</code></pre>
<p> Inherits <code>sc::Identity</code>. Inherited by <code>sc::CorrelationTable</code>, <code>sc::DescribedClass</code>, <code>sc::DipoleData</code>, <code>sc::Edge</code>, <code>sc::EfieldDotVectorData</code>, <code>sc::FJT</code>, <code>sc::GenPetite4</code>, <code>sc::Int1eCCA</code>, <code>sc::Int1eCints</code>, <code>sc::Int1eV3</code>, <code>sc::Int2eCCA</code>, <code>sc::Int2eCints</code>, <code>sc::Int2eV3</code>, <code>sc::KeyVal</code>, <code>sc::KeyValValue</code>, <code>sc::MOPairIter</code>, <code>sc::NonlinearTransform</code>, <code>sc::OneBodyDerivInt</code>, <code>sc::OneBodyInt</code>, <code>sc::OneBodyIntIter</code>, <code>sc::OneBodyOneCenterDerivInt</code>, <code>sc::OneBodyOneCenterInt</code>, <code>sc::OneBodySOInt</code>, <code>sc::PetiteList</code>, <code>sc::PointChargeData</code>, <code>sc::PrimPairsCints</code>, <code>sc::PsiFile11</code>, <code>sc::PsiInput</code>, <code>sc::R12Amplitudes</code>, <code>sc::SCMatrixSubblockIter</code>, <code>sc::ShellExtent</code>, <code>sc::SOBasis</code>, <code>sc::ThreadLock</code>, <code>sc::Triangle</code>, <code>sc::TriInterpCoef</code>, <code>sc::TwoBodyDerivInt</code>, <code>sc::TwoBodyInt</code>, <code>sc::TwoBodySOInt</code>, <code>sc::TwoBodyThreeCenterDerivInt</code>, <code>sc::TwoBodyThreeCenterInt</code>, <code>sc::TwoBodyTwoCenterDerivInt</code>, <code>sc::TwoBodyTwoCenterInt</code>, <code>sc::Vertex</code>, and <code>sc::X</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int lock_ptr () const


Lock this object.


int unlock_ptr () const


Unlock this object.


void use_locks (bool inVal)


start and stop using locks on this object


refcount_t nreference () const


Return the reference count.


refcount_t reference ()


Increment the reference count and return the new count.


refcount_t dereference ()


Decrement the reference count and return the new count.


int managed () const



void unmanage ()


Turn off the reference counting mechanism for this object.


int managed () const


Return 1 if the object is managed. Otherwise return 0.



Protected Member Functions
RefCount (const RefCount &amp;)



RefCount &amp; operator= (const RefCount &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>The base class for all reference counted objects. </p>
<p> If multiple inheritance is used, <code>RefCount</code> must be virtually inherited from, otherwise references to invalid memory will likely result. </p>
<p> Reference counting information is usually maintained by smart pointer classes <code>Ref</code>, however this mechanism can be supplemented or replaced by directly using the public interface to <code>RefCount</code>. </p>
<p> The <code>unmanage()</code> member is only needed for special cases where memory management must be turned off. For example, if a reference counted object is created on the stack, memory management mechanisms based on reference counting must be prohibited from deleting it. The <code>unmanage()</code> member accomplishes this, but a better solution would be to allocate the object on the heap with new and let a smart pointer manage the memory for the object. </p>
<p> When using a debugger to look at reference counted objects the count is maintained in the _reference_count_ member. However, this member is encoded so that memory overwrites can be sometimes detected. Thus, interpretation of _reference_count_ is not always straightforward.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::RefCount::unmanage () [inline]</h3>
<p>Turn off the reference counting mechanism for this object. The value returned by <code>nreference()</code> will always be 1 after this is called. The ability to <code>unmanage()</code> objects must be turned on at compile time by defining REF_MANAGE. There is a slight performance penalty.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
