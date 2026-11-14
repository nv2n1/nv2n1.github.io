---
title: "sc_molecularenergy(3)"
name: "sc_molecularenergy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molecularenergy/"
description: "sc::MolecularEnergy –"
---

<p>sc::MolecularEnergy &#8211; </p>
<p> The <code>MolecularEnergy</code> abstract class inherits from the <code>Function</code> class.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;energy.h&gt;</code></pre>
<p> Inherits <code>sc::Function</code>. Inherited by <code>sc::SumMolecularEnergy</code>, <code>sc::TaylorMolecularEnergy</code>, and <code>sc::Wavefunction</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MolecularEnergy(const MolecularEnergy &amp;)

        MolecularEnergy(const Ref&lt;KeyVal&gt; &amp;)

            The KeyVal constructor.

    MolecularEnergy(StateIn &amp;)

        void save_data_state(StateOut &amp;)

            Save the base classes(with save_data_state) and
    the members in the same order that the StateIn CTOR initializes them.

    void set_checkpoint()

        Set up checkpointing.

    void set_checkpoint_file(const char *)

        void set_checkpoint_freq(int freq)

            bool if_to_checkpoint() const

    Check if need to checkpoint.

    const char *checkpoint_file() const

    int checkpoint_freq() const

    MolecularEnergy &amp;
    operator=(const MolecularEnergy &amp;)

        virtual double energy()

            A wrapper around value();
.

    virtual Ref&lt;Molecule&gt;
    molecule() const

    virtual RefSCDimension moldim() const

    void guess_hessian(RefSymmSCMatrix &amp;)

        Compute a quick,
    approximate hessian.

    RefSymmSCMatrix inverse_hessian(RefSymmSCMatrix &amp;)

        RefSymmSCMatrix hessian()

            If a molecule hessian object is given,
    it will be used to provide a hessian.

    int hessian_implemented() const

    void set_x(const RefSCVector &amp;)

        Set and retrieve the coordinate values.

    RefSCVector get_cartesian_x()

        Return the cartesian coordinates.

    RefSCVector get_cartesian_gradient()

        Return the cartesian gradient.

    RefSymmSCMatrix get_cartesian_hessian()

        Return the cartesian hessian.

    Ref&lt;MolecularCoor&gt; molecularcoor()

        virtual void symmetry_changed()

            Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.

    Ref&lt;NonlinearTransform&gt; change_coordinates()

        An optimizer can call change coordinates periodically to give the function an opportunity to change its coordinate system.

    void print_natom_3(const RefSCVector &amp;, const char *t = 0, std::ostream &amp;o = ExEnv::out0()) const

    Nicely print n x 3 data that are stored in a vector.

    void print_natom_3(double **, const char *t = 0, std::ostream &amp;o = ExEnv::out0()) const

    void print_natom_3(double *, const char *t = 0, std::ostream &amp;o = ExEnv::out0()) const

    virtual void print(std::ostream &amp;= ExEnv::out0()) const

    Print information about the object.

    Protected Member Functions
    void failure(const char *)

        virtual void set_energy(double)

            This is just a wrapper around set_value()
                .

    virtual void set_gradient(RefSCVector &amp;)

        These are passed gradients and hessian in cartesian coordinates.

    virtual void set_hessian(RefSymmSCMatrix &amp;)

        void x_to_molecule()

            void molecule_to_x()

                Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>initial_pg_</code> </p>
<p> int <code>print_molecule_when_changed_</code></p>
<h2>Detailed Description</h2>
<p>The <code>MolecularEnergy</code> abstract class inherits from the <code>Function</code> class. </p>
<p> It computes the energy of the molecule as a function of the geometry. The coordinate system used can be either internal or cartesian.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MolecularEnergy::MolecularEnergy (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;molecule&quot; 1c A <code>Molecule</code> object. There is no default. </p>
<dl>
<dt>coor</p>
<dd>A <code>MolecularCoor</code> object that describes the coordinates. If this is not given cartesian coordinates will be used. For convenience, two keywords needed by the <code>MolecularCoor</code> object are automatically provided: natom3 and matrixkit.</dl>
<dl>
<dt>value_accuracy</p>
<dd>Sets the accuracy to which values are computed. The default is 1.0e-6 atomic units.</dl>
<dl>
<dt>gradient_accuracy</p>
<dd>Sets the accuracy to which gradients are computed. The default is 1.0e-6 atomic units.</dl>
<dl>
<dt>hessian_accuracy</p>
<dd>Sets the accuracy to which hessians are computed. The default is 1.0e-4 atomic units.</dl>
<dl>
<dt>hessian</p>
<dd>Specifies a <code>MolecularHessian</code> object that is used to compute the hessian. If this <code>MolecularEnergy</code> specialization does not provide a hessian of its own, and a hessian is needed, then this keyword must be specified.</dl>
<dl>
<dt>guess_hessian</p>
<dd>Specifies a <code>MolecularHessian</code> object that is used to compute a guess hessian. Guess hessians are used to improve the rate of convergence of optimizations. If this keyword is not specified, and a <code>MolecularCoor</code> object is given by coor, then the guess hessian is obtained from the <code>MolecularCoor</code> object. If neither this nor coor are given, then <code>Function::guess_hessian</code> is used, which returns a unit matrix.</dl>
<dl>
<dt>print_molecule_when_changed</p>
<dd>If true, then whenever the molecule&#8217;s coordinates are updated they will be printed. The default is true.</dl>
<dl>
<dt>checkpoint</p>
<dd>If true, then this object will be checkpointed during its evaluation. Not all implementations of <code>MolecularEnergy</code> support checkpointing. The default is false.</dl>
<dl>
<dt>checkpoint_file</p>
<dd>Specifies the name of the file into which this object will be checkpointed. Default is &#8216;&lt;inpubasename&gt;.ckpt&#8217;, where &#8216;&lt;inputbasename&gt;&#8217; is the name of the input file without &#8216;.in&#8217;.</dl>
<dl>
<dt>checkpoint_freq</p>
<dd>Specifies how often this object to be checkpointed. Only matters for objects which are computed iteratively. Default is 1.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>NonlinearTransform</code>&gt; sc::MolecularEnergy::change_coordinates () [virtual]</h3>
<p>An optimizer can call change coordinates periodically to give the function an opportunity to change its coordinate system. A return value of 0 means the coordinates were not changed. Otherwise, a transform object to the new coordinate system is return. The function object applies the transform to any objects it contains. This will obsolete the function data. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::MolecularEnergy::hessian () [virtual]</h3>
<p>If a molecule hessian object is given, it will be used to provide a hessian. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h3>void sc::MolecularEnergy::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Function</code>. </p>
<p> Reimplemented in <code>sc::SumMolecularEnergy</code>, <code>sc::TaylorMolecularEnergy</code>, <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::MBPT2</code>, <code>sc::MP2BasisExtrap</code>, <code>sc::MBPT2_R12</code>, <code>sc::PsiWavefunction</code>, <code>sc::PsiSCF</code>, <code>sc::PsiCCSD</code>, <code>sc::PsiCCSD_T</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, <code>sc::OneBodyWavefunction</code>, <code>sc::HCoreWfn</code>, and <code>sc::Wavefunction</code>.</p>
<h3>virtual void sc::MolecularEnergy::set_gradient (<code>RefSCVector</code> &amp;) [protected, virtual]</h3>
<p>These are passed gradients and hessian in cartesian coordinates. The gradient and hessian in internal coordinates are computed. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h3>virtual void sc::MolecularEnergy::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented in <code>sc::MBPT2</code>, <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCSCF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::OneBodyWavefunction</code>, and <code>sc::Wavefunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
