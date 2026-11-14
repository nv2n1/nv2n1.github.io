---
title: "sc_savablestate(3)"
name: "sc_savablestate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_savablestate/"
description: "sc::SavableState –"
---

<p>sc::SavableState &#8211; </p>
<p> Base class for objects that can save/restore state.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;state.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::AccumH</code> [virtual], <code>sc::AngularIntegrator</code> [virtual], <code>sc::AtomInfo</code>, <code>sc::Convergence</code> [virtual], <code>sc::Debugger</code>, <code>sc::DenFunctional</code> [virtual], <code>sc::DenIntegrator</code> [virtual], <code>sc::Function</code> [virtual], <code>sc::GaussianBasisSet</code>, <code>sc::GaussianShell</code>, <code>sc::HessianUpdate</code> [virtual], <code>sc::IntCoor</code>, <code>sc::IntCoorGen</code>, <code>sc::Integral</code>, <code>sc::IntegrationWeight</code> [virtual], <code>sc::MOIndexSpace</code> [virtual], <code>sc::MOIntsTransformFactory</code> [virtual], <code>sc::MolecularCoor</code>, <code>sc::MolecularFrequencies</code>, <code>sc::MolecularHessian</code> [virtual], <code>sc::Molecule</code>, <code>sc::MP2R12Energy</code> [virtual], <code>sc::Optimize</code> [virtual], <code>sc::OverlapOrthog</code> [virtual], <code>sc::PointGroup</code>, <code>sc::R12IntEval</code> [virtual], <code>sc::R12IntEvalInfo</code> [virtual], <code>sc::R12IntsAcc</code> [virtual], <code>sc::RadialIntegrator</code> [virtual], <code>sc::SCBlockInfo</code>, <code>sc::SCDimension</code>, <code>sc::SCElementOp</code>, <code>sc::SCElementOp2</code>, <code>sc::SCElementOp3</code>, <code>sc::SCExtrapData</code>, <code>sc::SCExtrapError</code>, <code>sc::SCMatrixBlock</code>, <code>sc::SCMatrixBlockList</code>, <code>sc::SelfConsistentExtrapolation</code>, <code>sc::SetIntCoor</code>, <code>sc::ShellPairCints</code> [virtual], <code>sc::ShellPairsCints</code> [virtual], <code>sc::TwoBodyGrid</code> [virtual], <code>sc::TwoBodyMOIntsTransform</code> [virtual], and <code>sc::Units</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SavableState &amp; operator= (const SavableState &amp;)



void save_state (StateOut &amp;)


Save the state of the object as specified by the StateOut object.


void save_object_state (StateOut &amp;)


This can be used for saving state when the exact type of the object is known for both the save and the restore.


virtual void save_vbase_state (StateOut &amp;)


Save the virtual bases for the object.


virtual void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.



Static Public Member Functions
static void save_state (SavableState *s, StateOut &amp;)



static SavableState * restore_state (StateIn &amp;si)


Restores objects saved with save_state.


static SavableState * key_restore_state (StateIn &amp;si, const char *keyword)


Like restore_state, but keyword is used to override values while restoring.


static SavableState * dir_restore_state (StateIn &amp;si, const char *objectname, const char *keyword=0)



Protected Member Functions</code></pre>
<p> <code>SavableState</code> (const <code>SavableState</code> &amp;) </p>
<p> <code>SavableState</code> (<code>StateIn</code> &amp;)<br />
 <i>Each derived class </i><code>StateIn</code> CTOR handles the restore corresponding to calling save_object_state, save_vbase_state, and save_data_state listed above.</p>
<h2>Detailed Description</h2>
<p>Base class for objects that can save/restore state.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SavableState::SavableState (<code>StateIn</code> &amp;) [protected]</h3>
<p>Each derived class <code>StateIn</code> CTOR handles the restore corresponding to calling save_object_state, save_vbase_state, and save_data_state listed above. All derived class <code>StateIn</code>&amp; constructors must invoke the <code>SavableState(StateIn&amp;)</code> constructor.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>SavableState</code>* sc::SavableState::key_restore_state (<code>StateIn</code> &amp; si, const char * keyword) [static]</h3>
<p>Like restore_state, but keyword is used to override values while restoring.</p>
<h3>static <code>SavableState</code>* sc::SavableState::restore_state (<code>StateIn</code> &amp; si) [static]</h3>
<p>Restores objects saved with save_state. The exact type of the next object in si can be any type publically derived from the <code>SavableState</code>. Derived classes implement a similar static function that returns a pointer to the derived class. If the objectname is given the directory will be consulted to find and restore that object.</p>
<h3>virtual void sc::SavableState::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented in <code>sc::AtomInfo</code>, <code>sc::IntCoor</code>, <code>sc::SumIntCoor</code>, <code>sc::SetIntCoor</code>, <code>sc::IntCoorGen</code>, <code>sc::MolecularCoor</code>, <code>sc::IntMolecularCoor</code>, <code>sc::SymmMolecularCoor</code>, <code>sc::RedundMolecularCoor</code>, <code>sc::CartMolecularCoor</code>, <code>sc::MolecularEnergy</code>, <code>sc::SumMolecularEnergy</code>, <code>sc::MolEnergyConvergence</code>, <code>sc::FinDispMolecularHessian</code>, <code>sc::MolecularHessian</code>, <code>sc::ReadMolecularHessian</code>, <code>sc::GuessMolecularHessian</code>, <code>sc::DiagMolecularHessian</code>, <code>sc::Molecule</code>, <code>sc::MolecularFrequencies</code>, <code>sc::SimpleCo</code>, <code>sc::TaylorMolecularEnergy</code>, <code>sc::GaussianBasisSet</code>, <code>sc::GaussianShell</code>, <code>sc::Integral</code>, <code>sc::OverlapOrthog</code>, <code>sc::IntegralCints</code>, <code>sc::ShellPairCints</code>, <code>sc::ShellPairsCints</code>, <code>sc::CLKS</code>, <code>sc::DenFunctional</code>, <code>sc::NElFunctional</code>, <code>sc::SumDenFunctional</code>, <code>sc::StdDenFunctional</code>, <code>sc::LSDACFunctional</code>, <code>sc::PBECFunctional</code>, <code>sc::PW91CFunctional</code>, <code>sc::P86CFunctional</code>, <code>sc::NewP86CFunctional</code>, <code>sc::SlaterXFunctional</code>, <code>sc::VWNLCFunctional</code>, <code>sc::VWN1LCFunctional</code>, <code>sc::VWN2LCFunctional</code>, <code>sc::VWN3LCFunctional</code>, <code>sc::VWN4LCFunctional</code>, <code>sc::VWN5LCFunctional</code>, <code>sc::PW92LCFunctional</code>, <code>sc::PZ81LCFunctional</code>, <code>sc::XalphaFunctional</code>, <code>sc::Becke88XFunctional</code>, <code>sc::LYPCFunctional</code>, <code>sc::PW86XFunctional</code>, <code>sc::PBEXFunctional</code>, <code>sc::PW91XFunctional</code>, <code>sc::mPW91XFunctional</code>, <code>sc::G96XFunctional</code>, <code>sc::HSOSKS</code>, <code>sc::DenIntegrator</code>, <code>sc::IntegrationWeight</code>, <code>sc::BeckeIntegrationWeight</code>, <code>sc::RadialIntegrator</code>, <code>sc::AngularIntegrator</code>, <code>sc::EulerMaclaurinRadialIntegrator</code>, <code>sc::LebedevLaikovIntegrator</code>, <code>sc::GaussLegendreAngularIntegrator</code>, <code>sc::RadialAngularIntegrator</code>, <code>sc::UKS</code>, <code>sc::IntegralCCA</code>, <code>sc::IntegralV3</code>, <code>sc::MBPT2</code>, <code>sc::MP2BasisExtrap</code>, <code>sc::MBPT2_R12</code>, <code>sc::MOIndexSpace</code>, <code>sc::MP2R12Energy</code>, <code>sc::R12IntsAcc</code>, <code>sc::R12IntsAcc_MemoryGrp</code>, <code>sc::R12IntsAcc_MPIIOFile</code>, <code>sc::R12IntsAcc_MPIIOFile_Ind</code>, <code>sc::R12IntsAcc_Node0File</code>, <code>sc::R12IntEval</code>, <code>sc::MOIntsTransformFactory</code>, <code>sc::TwoBodyMOIntsTransform_ijxy</code>, <code>sc::TwoBodyMOIntsTransform_ikjy</code>, <code>sc::TwoBodyMOIntsTransform_ixjy</code>, <code>sc::TwoBodyMOIntsTransform</code>, <code>sc::TwoBodyGrid</code>, <code>sc::R12IntEvalInfo</code>, <code>sc::PsiWavefunction</code>, <code>sc::PsiSCF</code>, <code>sc::PsiCCSD</code>, <code>sc::PsiCCSD_T</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::AccumH</code>, <code>sc::AccumHNull</code>, <code>sc::SumAccumH</code>, <code>sc::ExtendedHuckelWfn</code>, <code>sc::OneBodyWavefunction</code>, <code>sc::HCoreWfn</code>, <code>sc::BEMSolventH</code>, <code>sc::Wavefunction</code>, <code>sc::Convergence</code>, <code>sc::DIIS</code>, <code>sc::EFCOpt</code>, <code>sc::Function</code>, <code>sc::GDIISOpt</code>, <code>sc::NewtonOpt</code>, <code>sc::Optimize</code>, <code>sc::LineOpt</code>, <code>sc::QNewtonOpt</code>, <code>sc::SCExtrapData</code>, <code>sc::SCExtrapError</code>, <code>sc::SelfConsistentExtrapolation</code>, <code>sc::SymmSCMatrixSCExtrapData</code>, <code>sc::SymmSCMatrix2SCExtrapData</code>, <code>sc::SymmSCMatrix4SCExtrapData</code>, <code>sc::SymmSCMatrixNSCExtrapData</code>, <code>sc::SymmSCMatrixSCExtrapError</code>, <code>sc::SteepestDescentOpt</code>, <code>sc::HessianUpdate</code>, <code>sc::DFPUpdate</code>, <code>sc::BFGSUpdate</code>, <code>sc::PowellUpdate</code>, <code>sc::SCMatrixBlock</code>, <code>sc::SCMatrixBlockList</code>, <code>sc::SCVectorSimpleBlock</code>, <code>sc::SCVectorSimpleSubBlock</code>, <code>sc::SCMatrixRectBlock</code>, <code>sc::SCMatrixRectSubBlock</code>, <code>sc::SCMatrixLTriBlock</code>, <code>sc::SCMatrixLTriSubBlock</code>, <code>sc::SCMatrixDiagBlock</code>, <code>sc::SCMatrixDiagSubBlock</code>, <code>sc::SCBlockInfo</code>, <code>sc::SCDimension</code>, <code>sc::SCElementScalarProduct</code>, <code>sc::SCDestructiveElementProduct</code>, <code>sc::SCElementScale</code>, <code>sc::SCElementRandomize</code>, <code>sc::SCElementAssign</code>, <code>sc::SCElementSquareRoot</code>, <code>sc::SCElementInvert</code>, <code>sc::SCElementScaleDiagonal</code>, <code>sc::SCElementShiftDiagonal</code>, <code>sc::SCElementMaxAbs</code>, <code>sc::SCElementMinAbs</code>, <code>sc::SCElementSumAbs</code>, <code>sc::SCElementKNorm</code>, <code>sc::SCElementDot</code>, <code>sc::PointGroup</code>, <code>sc::Debugger</code>, and <code>sc::Units</code>.</p>
<h3>void sc::SavableState::save_object_state (<code>StateOut</code> &amp;)</h3>
<p>This can be used for saving state when the exact type of the object is known for both the save and the restore. To restore objects saved in this way the user must directly invoke the object&#8217;s <code>StateIn</code>&amp; constructor.</p>
<h3>void sc::SavableState::save_state (<code>StateOut</code> &amp;)</h3>
<p>Save the state of the object as specified by the <code>StateOut</code> object. This routine saves the state of the object (which includes the nonvirtual bases), the virtual bases, and type information. The default implementation should be adequate.</p>
<h3>virtual void sc::SavableState::save_vbase_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the virtual bases for the object. This must be done in the same order that the ctor initializes the virtual bases. This does not include the <code>DescribedClass</code> and <code>SavableState</code> virtual base classes. This must be implemented by the user if the class has other virtual bases. (These virtual bases must come after <code>SavableState</code>, if <code>SavableState</code> is virtual.)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
