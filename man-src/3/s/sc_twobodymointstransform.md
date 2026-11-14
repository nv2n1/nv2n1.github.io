---
title: "sc_twobodymointstransform(3)"
name: "sc_twobodymointstransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodymointstransform/"
description: "sc::TwoBodyMOIntsTransform –"
---

<p>sc::TwoBodyMOIntsTransform &#8211; </p>
<p> <code>TwoBodyMOIntsTransform</code> computes two-body integrals in MO basis using parallel integrals-direct AO-&gt;MO transformation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform_tbint.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::TwoBodyMOIntsTransform_ijxy</code>, <code>sc::TwoBodyMOIntsTransform_ikjy</code>, and <code>sc::TwoBodyMOIntsTransform_ixjy</code>.</p>
<h3>Classes</h3>
<pre><code>struct MOSpaces


Predefined enumerated type for the MO spaces.



Public Member Functions
TwoBodyMOIntsTransform (StateIn &amp;)



TwoBodyMOIntsTransform (const std::string &amp;name, const Ref&lt; MOIntsTransformFactory &gt; &amp;factory, const Ref&lt; MOIndexSpace &gt; &amp;space1, const Ref&lt; MOIndexSpace &gt; &amp;space2, const Ref&lt; MOIndexSpace &gt; &amp;space3, const Ref&lt; MOIndexSpace &gt; &amp;space4)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


std::string name () const


Returns the name of the transform.


virtual std::string type () const =0


Returns a short label which uniquely identifies the type of transform.


Ref&lt; MemoryGrp &gt; mem () const


Returns the MemoryGrp object.


Ref&lt; MessageGrp &gt; msg () const


Returns the MessageGrp object.


Ref&lt; R12IntsAcc &gt; ints_acc () const


Returns the integrals accumulator object.


Ref&lt; MOIndexSpace &gt; space1 () const


Returns MOIndexSpace object 1.


Ref&lt; MOIndexSpace &gt; space2 () const


Returns MOIndexSpace object 2.


Ref&lt; MOIndexSpace &gt; space3 () const


Returns MOIndexSpace object 3.


Ref&lt; MOIndexSpace &gt; space4 () const


Returns MOIndexSpace object 4.


double print_percent () const


Returns the update print frequency.


int batchsize () const


Returns the batchsize for each pass of the transformation.


int debug () const


Returns the debug level.


bool dynamic () const


Returns whether to use dynamic load balancing.


int num_te_types () const


Returns the number of types of two body integrals computed.


virtual const size_t memgrp_blksize () const =0


Returns the number of bytes allocated for each ij-block of integrals of one type in MemoryGrp.


void set_top_mole (const Ref&lt; MolecularEnergy &gt; &amp;top_mole)


Specifies the top-level MolecularEnergy object to use for checkpointing.


void set_num_te_types (const int num_te_types)


Specifies how many integral types computed by TwoBodyInt to be transformed Default is 1.


void set_memory (const size_t memory)



void set_debug (int debug)



void set_dynamic (bool dynamic)



void set_print_percent (double print_percent)



virtual void compute ()=0


Computes transformed integrals.


virtual void check_int_symm (double threshold=TwoBodyMOIntsTransform::zero_integral) const =0  throw (ProgrammingError)


Check symmetry of transformed integrals.


virtual void obsolete ()


Make the transform obsolete. Next call to compute() will recompute.


DistShellPair::SharedData * shell_pair_data ()


Returns a that data that must be shared between all DistShellPair objects.



Protected Member Functions
unsigned int restart_orbital () const


returns index in range of space1_ where to start the transformation


void init_vars ()



void reinit_acc ()



void alloc_mem (const size_t localmem)



void dealloc_mem ()



int compute_transform_batchsize_ (size_t mem_static, int rank_i)



void memory_report (std::ostream &amp;os=ExEnv::out0()) const


Generates a report on memory for the transform : user-specified limits, projected and actual use.


void mospace_report (std::ostream &amp;os=ExEnv::out0()) const


Generates a report on MO spaces for the transform.


void print_header (std::ostream &amp;os=ExEnv::out0()) const


Prints out standard header.


void print_footer (std::ostream &amp;os=ExEnv::out0()) const


Prints out standard footer.



Static Protected Member Functions
static int compute_nij (const int rank_i, const int rank_j, const int nproc, const int me)



Protected Attributes</code></pre>
<p> std::string <code>name_</code> </p>
<p> <code>Ref</code>&lt; <code>MOIntsTransformFactory</code> &gt; <code>factory_</code> </p>
<p> <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; <code>top_mole_</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>msg_</code> </p>
<p> <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; <code>mem_</code> </p>
<p> <code>Ref</code>&lt; <code>ThreadGrp</code> &gt; <code>thr_</code> </p>
<p> <code>Ref</code>&lt; <code>R12IntsAcc</code> &gt; <code>ints_acc_</code> </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space1_</code> </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space2_</code> </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space3_</code> </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>space4_</code> </p>
<p> int <code>num_te_types_</code> </p>
<p> size_t <code>memory_</code> </p>
<p> bool <code>dynamic_</code> </p>
<p> double <code>print_percent_</code> </p>
<p> <code>DistShellPair::SharedData</code> <code>spdata_</code> </p>
<p> int <code>debug_</code> </p>
<p> <code>MOIntsTransformFactory::StoreMethod</code> <code>ints_method_</code> </p>
<p> std::string <code>file_prefix_</code> </p>
<p> size_t <code>mem_static_</code> </p>
<p> int <code>batchsize_</code> </p>
<p> int <code>npass_</code></p>
<h3>Static Protected Attributes</h3>
<p>static const double <code>zero_integral</code> = 1.0e-12<br />
 <i>By default, integrals smaller than zero_integral are considered zero. </i></p>
<h2>Detailed Description</h2>
<p><code>TwoBodyMOIntsTransform</code> computes two-body integrals in MO basis using parallel integrals-direct AO-&gt;MO transformation.</p>
<h2>Member Function Documentation</h2>
<h3>virtual const size_t sc::TwoBodyMOIntsTransform::memgrp_blksize () const [pure virtual]</h3>
<p>Returns the number of bytes allocated for each ij-block of integrals of one type in <code>MemoryGrp</code>. It&#8217;s guaranteed to be divisible by sizeof(double). </p>
<p> Implemented in <code>sc::TwoBodyMOIntsTransform_ijxy</code>, <code>sc::TwoBodyMOIntsTransform_ikjy</code>, and <code>sc::TwoBodyMOIntsTransform_ixjy</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::memory_report (std::ostream &amp; os = ExEnv::out0()) const [protected]</h3>
<p>Generates a report on memory for the transform : user-specified limits, projected and actual use. Assumes formatting info from <code>ExEnv::out0()</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::mospace_report (std::ostream &amp; os = ExEnv::out0()) const [protected]</h3>
<p>Generates a report on MO spaces for the transform. Assumes formatting info from <code>ExEnv::out0()</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::print_footer (std::ostream &amp; os = ExEnv::out0()) const [protected]</h3>
<p>Prints out standard footer. Call at the end of <code>compute()</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::print_header (std::ostream &amp; os = ExEnv::out0()) const [protected]</h3>
<p>Prints out standard header. Call at the beginning of <code>compute()</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::TwoBodyMOIntsTransform_ijxy</code>, <code>sc::TwoBodyMOIntsTransform_ikjy</code>, and <code>sc::TwoBodyMOIntsTransform_ixjy</code>.</p>
<h3>void sc::TwoBodyMOIntsTransform::set_num_te_types (const int num_te_types)</h3>
<p>Specifies how many integral types computed by <code>TwoBodyInt</code> to be transformed Default is 1.</p>
<h3><code>DistShellPair::SharedData</code>* sc::TwoBodyMOIntsTransform::shell_pair_data () [inline]</h3>
<p>Returns a that data that must be shared between all <code>DistShellPair</code> objects.</p>
<h2>Member Data Documentation</h2>
<h3>const double <code>sc::TwoBodyMOIntsTransform::zero_integral</code> = 1.0e-12 [static, protected]</h3>
<p>By default, integrals smaller than zero_integral are considered zero. This constant is only used in checking integrals, not computing them.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
