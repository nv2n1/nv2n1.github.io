---
title: "sc_findispmolecularhessian(3)"
name: "sc_findispmolecularhessian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_findispmolecularhessian/"
description: "sc::FinDispMolecularHessian –"
---

<p>sc::FinDispMolecularHessian &#8211; </p>
<p> Computes the molecular hessian by finite displacements of gradients.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;fdhess.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularHessian</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FinDispMolecularHessian</code> (const <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; &amp;) </p>
<p> <code>FinDispMolecularHessian</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>FinDispMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>FinDispMolecularHessian</code> object from the input.<br />
 <code>FinDispMolecularHessian</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>RefSymmSCMatrix</code> <code>compute_hessian_from_gradients</code> ()<br />
 <i>These members are used to compute a cartesian hessian from gradients at finite displacements. </i><br />
 int <code>ndisplace</code> () const </p>
<p> int <code>ndisplacements_done</code> () const </p>
<p> <code>RefSCMatrix</code> <code>displacements</code> (int irrep) const </p>
<p> void <code>displace</code> (int disp) </p>
<p> void <code>original_geometry</code> () </p>
<p> void <code>set_gradient</code> (int disp, const <code>RefSCVector</code> &amp;grad) </p>
<p> void <code>checkpoint_displacements</code> (<code>StateOut</code> &amp;) </p>
<p> void <code>restore_displacements</code> (<code>StateIn</code> &amp;) </p>
<p> <code>RefSymmSCMatrix</code> <code>cartesian_hessian</code> ()<br />
 <i>This returns the cartesian hessian. </i><br />
 void <code>set_checkpoint</code> (int c)<br />
 <i>Set checkpoint option. </i><br />
 int <code>checkpoint</code> () const<br />
 <i>Return the current value of the checkpoint option. </i><br />
 void <code>set_energy</code> (const <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; &amp;energy)<br />
 <i>Some </i><code>MolecularHessian</code> specializations require a molecular energy object.<br />
 <code>MolecularEnergy</code> * <code>energy</code> () const<br />
 <i>This returns a </i><code>MolecularEnergy</code> object, if used by this specialization.<br />
 <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit</code> () const </p>
<p> <code>RefSCDimension</code> <code>d3natom</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>void get_disp (int disp, int &amp;irrep, int &amp;index, double &amp;coef)



void do_hess_for_irrep (int irrep, const RefSymmSCMatrix &amp;dhessian, const RefSymmSCMatrix &amp;xhessian)



void init ()



void restart ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; <code>mole_</code> </p>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>displacement_point_group_</code> </p>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>original_point_group_</code> </p>
<p> <code>RefSCVector</code> <code>original_geometry_</code> </p>
<p> double <code>disp_</code> </p>
<p> double <code>accuracy_</code> </p>
<p> int <code>ndisp_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int <code>restart_</code> </p>
<p> char * <code>restart_file_</code> </p>
<p> int <code>checkpoint_</code> </p>
<p> char * <code>checkpoint_file_</code> </p>
<p> int <code>only_totally_symmetric_</code> </p>
<p> int <code>eliminate_cubic_terms_</code> </p>
<p> int <code>do_null_displacement_</code> </p>
<p> int <code>debug_</code> </p>
<p> <code>RefSCMatrix</code> <code>symbasis_</code> </p>
<p> <code>RefSCVector</code> * <code>gradients_</code></p>
<h2>Detailed Description</h2>
<p>Computes the molecular hessian by finite displacements of gradients. </p>
<p> This will use the minimum number of displacements, each in the highest possible <code>point</code> group.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::FinDispMolecularHessian::FinDispMolecularHessian (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>FinDispMolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>FinDispMolecularHessian</code> object from the input. It reads the keywords below. </p>
<p> KeywordTypeDefaultDescription </p>
<p> energy<code>MolecularEnergy</code>noneThis gives an object which will be used to compute the gradients needed to form the hessian. If this is not specified, the object using <code>FinDispMolecularHessian</code> will, in some cases, fill it in appropriately. However, even in these cases, it may be desirable to specify this keyword. For example, this could be used in an optimization to compute frequencies using a lower level of theory. </p>
<p> debugbooleanfalseIf true, print out debugging information. </p>
<p> point_group<code>PointGroup</code>noneThe <code>point</code> group to use for generating the displacements. </p>
<p> restartbooleantrueIf true, and a checkpoint file exists, restart from that file. </p>
<p> restart_filestring <i>basename</i>.ckpt.hessThe name of the file where checkpoint information is written to or read from. </p>
<p> checkpointbooleantrueIf true, checkpoint intermediate data. </p>
<p> only_totally_symmetricbooleanfalse If true, only follow totally symmetric displacments. The hessian will not be complete, but it has enough information to use it in a geometry optimization. </p>
<p> eliminate_cubic_termsbooleantrueIf true, then cubic terms will be eliminated. This requires that two displacements are done for each totally symmetric coordinate, rather than one. Setting this to false will reduce the accuracy, but the results will still probably be accurate enough for a geometry optimization. </p>
<p> do_null_displacementbooleantrueRun the calculation at the given geometry as well. </p>
<p> displacementdouble1.0e-2The size of the displacement in Bohr. </p>
<p> gradient_accuracydoubledisplacement / 1000The accuracy to which the gradients will be computed.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefSymmSCMatrix</code> sc::FinDispMolecularHessian::cartesian_hessian () [virtual]</h3>
<p>This returns the cartesian hessian. If it has not yet been computed, it will be computed by finite displacements. </p>
<p> Implements <code>sc::MolecularHessian</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::FinDispMolecularHessian::compute_hessian_from_gradients ()</h3>
<p>These members are used to compute a cartesian hessian from gradients at finite displacements.</p>
<h3><code>MolecularEnergy</code>* sc::FinDispMolecularHessian::energy () const [virtual]</h3>
<p>This returns a <code>MolecularEnergy</code> object, if used by this specialization. Otherwise null is returned. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h3>void sc::FinDispMolecularHessian::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h3>void sc::FinDispMolecularHessian::set_energy (const <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; &amp; energy) [virtual]</h3>
<p>Some <code>MolecularHessian</code> specializations require a molecular energy object. The default implementations of this ignores the argument. </p>
<p> Reimplemented from <code>sc::MolecularHessian</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
