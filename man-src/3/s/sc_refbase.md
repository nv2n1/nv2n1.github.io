---
title: "sc_refbase(3)"
name: "sc_refbase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refbase/"
description: "sc::RefBase –"
---

<p>sc::RefBase &#8211; </p>
<p> Provides a few utility routines common to all <code>Ref</code> template instantiations.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;ref.h&gt;</code></pre>
<p> Inherited by <code>sc::Ref&lt; AccumH &gt;</code>, <code>sc::Ref&lt; AngularIntegrator &gt;</code>, <code>sc::Ref&lt; Appearance &gt;</code>, <code>sc::Ref&lt; AtomInfo &gt;</code>, <code>sc::Ref&lt; BatchElectronDensity &gt;</code>, <code>sc::Ref&lt; BEMSolvent &gt;</code>, <code>sc::Ref&lt; Convergence &gt;</code>, <code>sc::Ref&lt; DenFunctional &gt;</code>, <code>sc::Ref&lt; DenIntegrator &gt;</code>, <code>sc::Ref&lt; DescribedClass &gt;</code>, <code>sc::Ref&lt; DiagSCMatrix &gt;</code>, <code>sc::Ref&lt; DipoleData &gt;</code>, <code>sc::Ref&lt; Edge &gt;</code>, <code>sc::Ref&lt; EfieldDotVectorData &gt;</code>, <code>sc::Ref&lt; FJT &gt;</code>, <code>sc::Ref&lt; Function &gt;</code>, <code>sc::Ref&lt; GaussianBasisSet &gt;</code>, <code>sc::Ref&lt; HessianUpdate &gt;</code>, <code>sc::Ref&lt; Int1eCCA &gt;</code>, <code>sc::Ref&lt; Int1eCints &gt;</code>, <code>sc::Ref&lt; Int1eV3 &gt;</code>, <code>sc::Ref&lt; Int2eCCA &gt;</code>, <code>sc::Ref&lt; Int2eCints &gt;</code>, <code>sc::Ref&lt; Int2eV3 &gt;</code>, <code>sc::Ref&lt; IntCoor &gt;</code>, <code>sc::Ref&lt; IntCoorGen &gt;</code>, <code>sc::Ref&lt; Integral &gt;</code>, <code>sc::Ref&lt; IntegralStorer &gt;</code>, <code>sc::Ref&lt; IntegrationWeight &gt;</code>, <code>sc::Ref&lt; KeyVal &gt;</code>, <code>sc::Ref&lt; LineOpt &gt;</code>, <code>sc::Ref&lt; LSDACFunctional &gt;</code>, <code>sc::Ref&lt; MachineTopology &gt;</code>, <code>sc::Ref&lt; Material &gt;</code>, <code>sc::Ref&lt; MemoryGrp &gt;</code>, <code>sc::Ref&lt; MessageGrp &gt;</code>, <code>sc::Ref&lt; MOIndexSpace &gt;</code>, <code>sc::Ref&lt; MOIntsTransformFactory &gt;</code>, <code>sc::Ref&lt; MolecularCoor &gt;</code>, <code>sc::Ref&lt; MolecularEnergy &gt;</code>, <code>sc::Ref&lt; MolecularFrequencies &gt;</code>, <code>sc::Ref&lt; MolecularHessian &gt;</code>, <code>sc::Ref&lt; Molecule &gt;</code>, <code>sc::Ref&lt; MoleculeColorizer &gt;</code>, <code>sc::Ref&lt; MP2R12Energy &gt;</code>, <code>sc::Ref&lt; OneBodyInt &gt;</code>, <code>sc::Ref&lt; OneBodyIntIter &gt;</code>, <code>sc::Ref&lt; OneBodyWavefunction &gt;</code>, <code>sc::Ref&lt; OverlapOrthog &gt;</code>, <code>sc::Ref&lt; PetiteList &gt;</code>, <code>sc::Ref&lt; PointChargeData &gt;</code>, <code>sc::Ref&lt; PointGroup &gt;</code>, <code>sc::Ref&lt; PrimPairsCints &gt;</code>, <code>sc::Ref&lt; PsiExEnv &gt;</code>, <code>sc::Ref&lt; PsiFile11 &gt;</code>, <code>sc::Ref&lt; PsiInput &gt;</code>, <code>sc::Ref&lt; PsiSCF &gt;</code>, <code>sc::Ref&lt; R12Amplitudes &gt;</code>, <code>sc::Ref&lt; R12IntEval &gt;</code>, <code>sc::Ref&lt; R12IntEvalInfo &gt;</code>, <code>sc::Ref&lt; R12IntsAcc &gt;</code>, <code>sc::Ref&lt; RadialIntegrator &gt;</code>, <code>sc::Ref&lt; RegionTimer &gt;</code>, <code>sc::Ref&lt; RenderedMolecule &gt;</code>, <code>sc::Ref&lt; RenderedObject &gt;</code>, <code>sc::Ref&lt; SavableState &gt;</code>, <code>sc::Ref&lt; sc::Int1eCCA &gt;</code>, <code>sc::Ref&lt; SCBlockInfo &gt;</code>, <code>sc::Ref&lt; SCDimension &gt;</code>, <code>sc::Ref&lt; SCExtrapData &gt;</code>, <code>sc::Ref&lt; SCExtrapError &gt;</code>, <code>sc::Ref&lt; SCF &gt;</code>, <code>sc::Ref&lt; SCMatrix &gt;</code>, <code>sc::Ref&lt; SCMatrixBlock &gt;</code>, <code>sc::Ref&lt; SCMatrixBlockList &gt;</code>, <code>sc::Ref&lt; SCMatrixDiagBlock &gt;</code>, <code>sc::Ref&lt; SCMatrixKit &gt;</code>, <code>sc::Ref&lt; SCMatrixLTriBlock &gt;</code>, <code>sc::Ref&lt; SCMatrixRectBlock &gt;</code>, <code>sc::Ref&lt; SCMatrixSubblockIter &gt;</code>, <code>sc::Ref&lt; SCVector &gt;</code>, <code>sc::Ref&lt; SCVectorSimpleBlock &gt;</code>, <code>sc::Ref&lt; SelfConsistentExtrapolation &gt;</code>, <code>sc::Ref&lt; SetIntCoor &gt;</code>, <code>sc::Ref&lt; ShellPairCints &gt;</code>, <code>sc::Ref&lt; ShellPairsCints &gt;</code>, <code>sc::Ref&lt; SOBasis &gt;</code>, <code>sc::Ref&lt; SymmSCMatrix &gt;</code>, <code>sc::Ref&lt; ThreadGrp &gt;</code>, <code>sc::Ref&lt; ThreadLock &gt;</code>, <code>sc::Ref&lt; Transform &gt;</code>, <code>sc::Ref&lt; TriangleIntegrator &gt;</code>, <code>sc::Ref&lt; TriangulatedImplicitSurface &gt;</code>, <code>sc::Ref&lt; TriangulatedSurface &gt;</code>, <code>sc::Ref&lt; TriInterpCoef &gt;</code>, <code>sc::Ref&lt; TwoBodyDerivInt &gt;</code>, <code>sc::Ref&lt; TwoBodyGrid &gt;</code>, <code>sc::Ref&lt; TwoBodyInt &gt;</code>, <code>sc::Ref&lt; TwoBodyMOIntsTransform &gt;</code>, <code>sc::Ref&lt; Units &gt;</code>, <code>sc::Ref&lt; Vertex &gt;</code>, <code>sc::Ref&lt; Volume &gt;</code>, <code>sc::Ref&lt; Wavefunction &gt;</code>, and <code>sc::Ref&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual RefCount * parentpointer () const =0


Returns the DescribedClass pointer for the contained object.


void require_nonnull () const


Requires that a nonnull reference is held.



Protected Member Functions
void warn (const char *msg) const


Print a warning message.


void warn_ref_to_stack () const


Called when stack data is referenced.


void warn_skip_stack_delete () const


Called when the deletion of stack data is skipped.


void warn_bad_ref_count () const


Called when the reference count is corrupted.


void ref_info (RefCount *p, std::ostream &amp;os) const


Print information about the reference.


void ref_info (std::ostream &amp;os) const



void check_pointer () const



void reference (RefCount *)



int dereference (RefCount *)</code></pre>
<h2>Detailed Description</h2>
<p>Provides a few utility routines common to all <code>Ref</code> template instantiations.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::RefBase::require_nonnull () const</h3>
<p>Requires that a nonnull reference is held. If not, the program will abort.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
