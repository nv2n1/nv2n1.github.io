---
title: "sc_intmolecularcoor(3)"
name: "sc_intmolecularcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_intmolecularcoor/"
description: "sc::IntMolecularCoor –"
---

<p>sc::IntMolecularCoor &#8211; </p>
<p> The <code>IntMolecularCoor</code> abstract class describes a molecule&#8217;s coordinates in terms of internal coordinates.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/coor.h">coor.h</a>&gt; </p>
<p> Inherits <code>sc::MolecularCoor</code>. </p>
<p> Inherited by <code>sc::RedundMolecularCoor</code>, and <code>sc::SymmMolecularCoor</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>IntMolecularCoor</code> (<code>StateIn</code> &amp;) </p>
<p> <code>IntMolecularCoor</code> (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;mol) </p>
<p> <code>IntMolecularCoor</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual void <code>form_coordinates</code> (int keep_variable=0)=0<br />
 <i>Actually form the variable and constant internal coordinates from the simple internal coordinates. </i><br />
 virtual int <code>all_to_cartesian</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCVector</code> &amp;internal)<br />
 <i>Like to_cartesians(), except all internal coordinates are considered, not just the variable ones. </i><br />
 virtual int <code>all_to_internal</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCVector</code> &amp;internal)<br />
 <i>Like </i><code>to_internal()</code>, except all internal coordinates are considered, not just the variable ones.<br />
 virtual <code>RefSCDimension</code> <code>dim</code> ()<br />
 <i>These implement the virtual functions inherited from </i><code>MolecularCoor</code>.<br />
 virtual int <code>to_cartesian</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, const <code>RefSCVector</code> &amp;internal) </p>
<p> virtual int <code>to_internal</code> (<code>RefSCVector</code> &amp;internal)<br />
 <i>Fill in the vector &#8220;internal&#8221; with the current internal coordinates. </i><br />
 virtual int <code>to_cartesian</code> (<code>RefSCVector</code> &amp;cartesian, <code>RefSCVector</code> &amp;internal)<br />
 <i>Convert the internal coordinate gradients in &#8220;internal&#8221; to Cartesian coordinates and copy these Cartesian coordinate gradients to &#8220;cartesian&#8221;. </i><br />
 virtual int <code>to_internal</code> (<code>RefSCVector</code> &amp;internal, <code>RefSCVector</code> &amp;cartesian)<br />
 <i>Convert the Cartesian coordinate gradients in &#8220;cartesian&#8221; to internal coordinates and copy these internal coordinate gradients to &#8220;internal&#8221;. </i><br />
 virtual int <code>to_cartesian</code> (<code>RefSymmSCMatrix</code> &amp;cart, <code>RefSymmSCMatrix</code> &amp;internal)<br />
 <i>Convert the internal coordinate Hessian &#8220;internal&#8221; to Cartesian coordinates and copy the result to &#8220;cartesian&#8221;. </i><br />
 virtual int <code>to_internal</code> (<code>RefSymmSCMatrix</code> &amp;internal, <code>RefSymmSCMatrix</code> &amp;cart)<br />
 <i>Convert the Cartesian coordinate Hessian &#8220;cartesian&#8221; to internal coordinates and copy the result to &#8220;internal&#8221;. </i><br />
 virtual void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the coordinate. </i><br />
 virtual void <code>print_simples</code> (std::ostream &amp;=ExEnv::out0()) const </p>
<p> virtual void <code>print_variable</code> (std::ostream &amp;=ExEnv::out0()) const </p>
<p> virtual void <code>print_constant</code> (std::ostream &amp;=ExEnv::out0()) const </p>
<p> int <code>nconstrained</code> ()<br />
 <i>Returns the number of constrained coordinates. </i></p>
<h3>Protected Member Functions</h3>
<p> void <code>form_K_matrix</code> (<code>RefSCDimension</code> &amp;dredundant, <code>RefSCDimension</code> &amp;dfixed, <code>RefSCMatrix</code> &amp;K, int *&amp;is_totally_symmetric) </p>
<p> virtual void <code>init</code> ()<br />
 <i>This is called by the constructors of classes derived from </i><code>IntMolecularCoor</code>.<br />
 virtual void <code>new_coords</code> ()<br />
 <i>Allocates memory for the SetIntCoor&#8217;s used to store the simple and internal coordinates. </i><br />
 virtual void <code>read_keyval</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Reads the </i><code>KeyVal</code> input.</p>
<h3>Protected Attributes</h3>
<p> <code>Ref</code>&lt; <code>IntCoorGen</code> &gt; <code>generator_</code> </p>
<p> <code>RefSCDimension</code> <code>dim_</code> </p>
<p> <code>RefSCDimension</code> <code>dvc_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>variable_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>constant_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>fixed_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>watched_</code> </p>
<p> <code>Ref</code>&lt; <code>IntCoor</code> &gt; <code>followed_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>bonds_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>bends_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>tors_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>outs_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>extras_</code> </p>
<p> <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; <code>all_</code> </p>
<p> int <code>update_bmat_</code> </p>
<p> int <code>only_totally_symmetric_</code> </p>
<p> double <code>symmetry_tolerance_</code> </p>
<p> double <code>simple_tolerance_</code> </p>
<p> double <code>coordinate_tolerance_</code> </p>
<p> double <code>cartesian_tolerance_</code> </p>
<p> double <code>scale_bonds_</code> </p>
<p> double <code>scale_bends_</code> </p>
<p> double <code>scale_tors_</code> </p>
<p> double <code>scale_outs_</code> </p>
<p> int <code>nextra_bonds_</code> </p>
<p> int * <code>extra_bonds_</code> </p>
<p> int <code>given_fixed_values_</code> </p>
<p> int <code>decouple_bonds_</code> </p>
<p> int <code>decouple_bends_</code> </p>
<p> int <code>max_update_steps_</code> </p>
<p> double <code>max_update_disp_</code> </p>
<p> int <code>form_print_simples_</code> </p>
<p> int <code>form_print_variable_</code> </p>
<p> int <code>form_print_constant_</code> </p>
<p> int <code>form_print_molecule_</code> </p>
<h2>Detailed Description</h2>
<p> The <code>IntMolecularCoor</code> abstract class describes a molecule&#8217;s coordinates in terms of internal coordinates. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::IntMolecularCoor::IntMolecularCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p> The <code>KeyVal</code> constructor. .IP &quot;variable&quot; 1c Gives a <code>SetIntCoor</code> object that specifies the internal coordinates that can be varied. If this is not given, the variable coordinates will be generated. </p>
<dl COMPACT>
<dt>followed</p>
<dd> Gives a <code>IntCoor</code> object that specifies a coordinate to used as the first coordinate in the variable coordinate list. The remaining coordinates will be automatically generated. The default is no followed coordinate. This option is usually used to set the initial search direction for a transition state optimization, where it is used in conjunction with the mode_following keyword read by the <code>EFCOpt</code> class.</dl>
<dl COMPACT>
<dt>fixed</p>
<dd> Gives a <code>SetIntCoor</code> object that specifies the internal coordinates that will be fixed. The default is no fixed coordinates.</dl>
<dl COMPACT>
<dt>watched</p>
<dd> Gives a <code>SetIntCoor</code> object that specifies internal coordinates that will be printed out whenever the coordinates are changed. The default is none.</dl>
<dl COMPACT>
<dt>have_fixed_values</p>
<dd> If true, then values for the fixed coordinates must be given in fixed and an attempt will be made to displace the initial geometry to the given fixed values. The default is false.</dl>
<dl COMPACT>
<dt>extra_bonds</p>
<dd> This is only read if the generator keyword is not given. It is a vector of atom numbers, where elements $(i-1) imes 2 + 1$ and $i imes 2$ specify the atoms which are bound in extra bond $i$. The extra_bonds keyword should only be needed for weakly interacting fragments, otherwise all the needed bonds will be found.</dl>
<dl COMPACT>
<dt>generator</p>
<dd> Specifies an <code>IntCoorGen</code> object that creates simple, redundant internal coordinates. If this keyword is not given, then a vector giving extra bonds to be added is read from extra_bonds and this is used to create an <code>IntCoorGen</code> object.</dl>
<dl COMPACT>
<dt>decouple_bonds</p>
<dd> Automatically generated internal coordinates are linear combinations of possibly any mix of simple internal coordinates. If decouple_bonds is true, an attempt will be made to form some of the internal coordinates from just stretch simple coordinates. The default is false.</dl>
<dl COMPACT>
<dt>decouple_bends</p>
<dd> This is like decouple_bonds except it applies to the bend-like coordinates. The default is false.</dl>
<dl COMPACT>
<dt>max_update_disp</p>
<dd> The maximum displacement to be used in the displacement to fixed internal coordinates values. Larger displacements will be broken into several smaller displacements and new coordinates will be formed for each of these displacments. This is only used when fixed and have_fixed_values are given. The default is 0.5.</dl>
<dl COMPACT>
<dt>max_update_steps</p>
<dd> The maximum number of steps permitted to convert internal coordinate displacements to cartesian coordinate displacements. The default is 100.</dl>
<dl COMPACT>
<dt>update_bmat</p>
<dd> Displacements in internal coordinates are converted to a cartesian displacements iteratively. If there are large changes in the cartesian coordinates during conversion, then recompute the $B$ matrix, which is using to do the conversion. The default is false.</dl>
<dl COMPACT>
<dt>only_totally_symmetric</p>
<dd> If a simple test reveals that an internal coordinate is not totally symmetric, then it will not be added to the internal coordinate list. The default is true.</dl>
<dl COMPACT>
<dt>simple_tolerance</p>
<dd> The internal coordinates are formed as linear combinations of simple, redundant internal coordinates. Coordinates with coefficients smaller then simple_tolerance will be omitted. The default is 1.0e-3.</dl>
<dl COMPACT>
<dt>cartesian_tolerance</p>
<dd> The tolerance for conversion of internal coordinate displacements to cartesian displacements. The default is 1.0e-12.</dl>
<dl COMPACT>
<dt>form:print_simple</p>
<dd> Print the simple internal coordinates. The default is false.</dl>
<dl COMPACT>
<dt>form:print_variable</p>
<dd> Print the variable internal coordinates. The default is false.</dl>
<dl COMPACT>
<dt>form:print_constant</p>
<dd> Print the constant internal coordinates. The default is false.</dl>
<dl COMPACT>
<dt>form:print_molecule</p>
<dd> Print the molecule when forming coordinates. The default is false.</dl>
<dl COMPACT>
<dt>scale_bonds</p>
<dd> Obsolete. The default value is 1.0.</dl>
<dl COMPACT>
<dt>scale_bends</p>
<dd> Obsolete. The default value is 1.0.</dl>
<dl COMPACT>
<dt>scale_tors</p>
<dd> Obsolete. The default value is 1.0.</dl>
<dl COMPACT>
<dt>scale_outs</p>
<dd> Obsolete. The default value is 1.0.</dl>
<dl COMPACT>
<dt>symmetry_tolerance</p>
<dd> Obsolete. The default is 1.0e-5.</dl>
<dl COMPACT>
<dt>coordinate_tolerance</p>
<dd> Obsolete. The default is 1.0e-7.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::IntMolecularCoor::all_to_cartesian (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p> Like to_cartesians(), except all internal coordinates are considered, not just the variable ones.</p>
<h3>virtual int sc::IntMolecularCoor::all_to_internal (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p> Like <code>to_internal()</code>, except all internal coordinates are considered, not just the variable ones.</p>
<h3>virtual <code>RefSCDimension</code> sc::IntMolecularCoor::dim () [virtual]</h3>
<p> These implement the virtual functions inherited from <code>MolecularCoor</code>. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual void sc::IntMolecularCoor::form_coordinates (int keep_variable = 0) [pure virtual]</h3>
<p> Actually form the variable and constant internal coordinates from the simple internal coordinates. </p>
<p> Implemented in <code>sc::SymmMolecularCoor</code>, and <code>sc::RedundMolecularCoor</code>.</p>
<h3>virtual void sc::IntMolecularCoor::init () [protected, virtual]</h3>
<p> This is called by the constructors of classes derived from <code>IntMolecularCoor</code>. It initialized the lists of simple internal coordinates, and then calls the <code>form_coordinates()</code> member. </p>
<p> Reimplemented in <code>sc::SymmMolecularCoor</code>.</p>
<h3>virtual void sc::IntMolecularCoor::new_coords () [protected, virtual]</h3>
<p> Allocates memory for the SetIntCoor&#8217;s used to store the simple and internal coordinates.</p>
<h3>void sc::IntMolecularCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p> Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularCoor</code>. </p>
<p> Reimplemented in <code>sc::SymmMolecularCoor</code>, and <code>sc::RedundMolecularCoor</code>.</p>
<h3>virtual int sc::IntMolecularCoor::to_cartesian (<code>RefSymmSCMatrix</code> &amp; cartesian, <code>RefSymmSCMatrix</code> &amp; internal) [virtual]</h3>
<p> Convert the internal coordinate Hessian &#8220;internal&#8221; to Cartesian coordinates and copy the result to &#8220;cartesian&#8221;. Only the variable internal coordinate force constants are transformed. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::IntMolecularCoor::to_cartesian (<code>RefSCVector</code> &amp; cartesian, <code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p> Convert the internal coordinate gradients in &#8220;internal&#8221; to Cartesian coordinates and copy these Cartesian coordinate gradients to &#8220;cartesian&#8221;. Only the variable internal coordinate gradients are transformed. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::IntMolecularCoor::to_internal (<code>RefSymmSCMatrix</code> &amp; internal, <code>RefSymmSCMatrix</code> &amp; cartesian) [virtual]</h3>
<p> Convert the Cartesian coordinate Hessian &#8220;cartesian&#8221; to internal coordinates and copy the result to &#8220;internal&#8221;. Only the variable internal coordinate force constants are calculated. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::IntMolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal, <code>RefSCVector</code> &amp; cartesian) [virtual]</h3>
<p> Convert the Cartesian coordinate gradients in &#8220;cartesian&#8221; to internal coordinates and copy these internal coordinate gradients to &#8220;internal&#8221;. Only the variable internal coordinate gradients are calculated. </p>
<p> Implements <code>sc::MolecularCoor</code>.</p>
<h3>virtual int sc::IntMolecularCoor::to_internal (<code>RefSCVector</code> &amp; internal) [virtual]</h3>
<p> Fill in the vector &#8220;internal&#8221; with the current internal coordinates. Note that this member will update the values of the variable internal coordinates. </p>
<p> Implements <code>sc::MolecularCoor</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
