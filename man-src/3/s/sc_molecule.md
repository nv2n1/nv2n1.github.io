---
title: "sc_molecule(3)"
name: "sc_molecule"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molecule/"
description: "sc::Molecule –"
---

<p>sc::Molecule &#8211; </p>
<p> The <code>Molecule</code> class contains information about molecules.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;molecule.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Molecule (const Molecule &amp;)



Molecule (StateIn &amp;)



Molecule (const Ref&lt; KeyVal &gt; &amp;input)


The Molecule KeyVal constructor is used to generate a Molecule object from the input.


Molecule &amp; operator= (const Molecule &amp;)



void add_atom (int Z, double x, double y, double z, const char *=0, double mass=0.0, int have_charge=0, double charge=0.0)


Add an AtomicCenter to the Molecule.


virtual void print (std::ostream &amp;=ExEnv::out0()) const


Print information about the molecule.


virtual void print_parsedkeyval (std::ostream &amp;=ExEnv::out0(), int print_pg=1, int print_unit=1, int number_atoms=1) const



int natom () const


Returns the number of atoms in the molcule.


int Z (int atom) const



double &amp; r (int atom, int xyz)



const double &amp; r (int atom, int xyz) const



double * r (int atom)



const double * r (int atom) const



double mass (int atom) const



const char * label (int atom) const


Returns the label explicitly assigned to atom.


int atom_at_position (double *, double tol=0.05) const


Takes an (x, y, z) postion and finds an atom within the given tolerance distance.


int atom_label_to_index (const char *label) const


Returns the index of the atom with the given label.


double * charges () const


Returns a double* containing the nuclear charges of the atoms.


double charge (int iatom) const


Return the charge of the atom.


double nuclear_charge () const


Returns the total nuclear charge.


void set_point_group (const Ref&lt; PointGroup &gt; &amp;, double tol=1.0e-7)


Sets the PointGroup of the molecule.


Ref&lt; PointGroup &gt; point_group () const


Returns the PointGroup of the molecule.


Ref&lt; PointGroup &gt; highest_point_group (double tol=1.0e-8) const


Find this molecules true point group (limited to abelian groups).


int is_axis (SCVector3 &amp;origin, SCVector3 &amp;udirection, int order, double tol=1.0e-8) const


Return 1 if this given axis is a symmetry element for the molecule.


int is_plane (SCVector3 &amp;origin, SCVector3 &amp;uperp, double tol=1.0e-8) const


Return 1 if the given plane is a symmetry element for the molecule.


int has_inversion (SCVector3 &amp;origin, double tol=1.0e-8) const


Return 1 if the molecule has an inversion center.


int is_linear (double tolerance=1.0e-5) const


Returns 1 if the molecule is linear, 0 otherwise.


int is_planar (double tolerance=1.0e-5) const


Returns 1 if the molecule is planar, 0 otherwise.


void is_linear_planar (int &amp;linear, int &amp;planar, double tol=1.0e-5) const


Sets linear to 1 if the molecular is linear, 0 otherwise.


SCVector3 center_of_mass () const


Returns a SCVector3 containing the cartesian coordinates of the center of mass for the molecule.


double nuclear_repulsion_energy ()


Returns the nuclear repulsion energy for the molecule.


void nuclear_repulsion_1der (int center, double xyz[3])


Compute the nuclear repulsion energy first derivative with respect to the given center.


void nuclear_efield (const double *position, double *efield)


Compute the electric field due to the nuclei at the given point.


void nuclear_charge_efield (const double *charges, const double *position, double *efield)


Compute the electric field due to the given charges at the positions of the nuclei at the given point.


void symmetrize (double tol=0.5)


If the molecule contains only symmetry unique atoms, this function will generate the other, redundant atoms.


void symmetrize (const Ref&lt; PointGroup &gt; &amp;pg, double tol=0.5)


Set the point group and then symmetrize.


void cleanup_molecule (double tol=0.1)


This will try to carefully correct symmetry errors in molecules.


void translate (const double *r)



void move_to_com ()



void transform_to_principal_axes (int trans_frame=1)



void transform_to_symmetry_frame ()



void print_pdb (std::ostream &amp;=ExEnv::out0(), char *title=0) const



void read_pdb (const char *filename)



void principal_moments_of_inertia (double *evals, double **evecs=0) const


Compute the principal moments of inertia and, possibly, the principal axes.


int nunique () const


Return information about symmetry unique and equivalent atoms.


int unique (int iuniq) const


Returns the overall number of the iuniq'th unique atom.


int nequivalent (int iuniq) const


Returns the number of atoms equivalent to iuniq.


int equivalent (int iuniq, int j) const


Returns the j'th atom equivalent to iuniq.


int atom_to_unique (int iatom) const


Converts an atom number to the number of its generating unique atom.


int atom_to_unique_offset (int iatom) const


Converts an atom number to the offset of this atom in the list of generated atoms.


int n_core_electrons ()


Return the number of core electrons.


int max_z ()


Return the maximum atomic number.


Ref&lt; AtomInfo &gt; atominfo () const


Return the molecule's AtomInfo object.


std::string atom_name (int iatom) const


Returns the element name of the atom.


std::string atom_symbol (int iatom) const


Returns the element symbol of the atom.


void set_include_q (bool iq)


If include_q is true, then include the 'Q' atoms in the charge and efield routines.


bool include_q () const


Returns include_q. See set_include_q.


void set_include_qq (bool iqq)


If include_qq is true, include the coupling between pairs of 'Q' atoms when computing nuclear repulsion energy and gradients.


bool include_qq () const


Returns include_qq. See set_include_qq.


int n_q_atom () const


Retrieve the number of 'Q' atoms.


int q_atom (int i) const


Retrieve the 'Q' atoms.


int n_non_q_atom () const


Retrieve the number of non-'Q' atoms.


int non_q_atom (int i) const


Retrieve the of non-'Q' atoms.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.



Protected Member Functions
void init_symmetry_info (double tol=0.5)



void clear_symmetry_info ()



void clear ()



void throw_if_atom_duplicated (int begin=0, double tol=1e-3)



Protected Attributes
int natoms_



Ref&lt; AtomInfo &gt; atominfo_



Ref&lt; PointGroup &gt; pg_



Ref&lt; Units &gt; geometry_units_



double ** r_



int * Z_



double * charges_



int nuniq_



int * nequiv_



int ** equiv_



int * atom_to_uniq_



double * mass_



char ** labels_



int q_Z_



bool include_q_



bool include_qq_



std::vector&lt; int &gt; q_atoms_



std::vector&lt; int &gt; non_q_atoms_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>Molecule</code> class contains information about molecules. </p>
<p> It has a <code>KeyVal</code> constructor that can create a new molecule from either a PDB file or from a list of Cartesian coordinates. </p>
<p> The following <code>ParsedKeyVal</code> input reads from the PDB file h2o.pdb: </p>
<pre>molecule&lt;Molecule&gt;: (
 pdb_file = 'h2o.pdb'
 )</pre>
<p>The following input explicitly gives the atom coordinates, using the <code>ParsedKeyVal</code> table notation: </p>
<pre>molecule&lt;Molecule&gt;: (
 unit=angstrom
 { atom_labels atoms geometry } = {
 O1 O [ 0.000000000 0 0.369372944 ]
 H1 H [ 0.783975899 0 -0.184686472 ]
 H2 H [-0.783975899 0 -0.184686472 ]
 }
 )
 )</pre>
<p>&nbsp;<wbr>The default units are Bohr which can be overridden with unit=angstrom. The atom_labels array can be omitted. The atoms and geometry arrays are required. </p>
<p> As a special case, an atom can be given with the symbol Q or the name charge. Such centers are treated as <code>point</code> charges and not given basis functions. The values of the charges must be specified with a charge vector in the <code>Molecule</code> input. Since the charge vector assign charges to all centers, including atoms, it is easiest to place all <code>point</code> charge centers first in the geometry, and then give a charge vector with a number of elements equal to the number of <code>point</code> charges. The following example shows a water molecule interacting with a <code>point</code> charge having value 0.1: </p>
<pre>molecule&lt;Molecule&gt;: (
 unit=angstrom
 charge = [ 0.1 ]
 { atom_labels atoms geometry } = {
 Q1 Q [ 0.0 0 10.0 ]
 O1 O [ 0.000000000 0 0.369372944 ]
 H1 H [ 0.783975899 0 -0.184686472 ]
 H2 H [-0.783975899 0 -0.184686472 ]
 }
 )
 )</pre>
<p>This feature is designed for doing QM/MM calculations, so, by default, methods will not include interactions between the Q centers when computing the energy or the gradient. To include these interactions, set include_qq=1. </p>
<p> The <code>Molecule</code> class has a <code>PointGroup</code> member object, which also has a <code>KeyVal</code> constructor that is called when a <code>Molecule</code> is made. The following example constructs a molecule with $C_{2v}$ symmetry: </p>
<pre>molecule&lt;Molecule&gt;: (
 symmetry=c2v
 unit=angstrom
 { atoms geometry } = {
 O [0.000000000 0 0.369372944 ]
 H [0.783975899 0 -0.184686472 ]
 }
 )
 )</pre>
<p>&nbsp;<wbr>Only the symmetry unique atoms need to be specified. Nonunique atoms can be given too, however, numerical errors in the geometry specification can result in the generation of extra atoms so be careful.&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Molecule::Molecule (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp; input)</h3>
<p>The <code>Molecule</code> <code>KeyVal</code> constructor is used to generate a <code>Molecule</code> object from the input. Several examples are given in the <code>Molecule</code> class overview. The full list of keywords that are accepted is below. </p>
<p> KeywordTypeDefaultDescription </p>
<p> include_qbooleanfalseSome of the atoms can be specified as Q and given a customizable charge. Such atoms are a <code>point</code> charge that do not have basis functions. If this option is true, then the Q atoms are included when computing the nuclear charge and the electric field due to the nuclear charge. </p>
<p> include_qqbooleanfalseSome of the atoms can be specified as Q and given a customizable charge. Such atoms are a <code>point</code> charge that do not have basis functions. If this option is true, then the Q atoms are included when computing the nuclear repulsion energy and its derivatives. </p>
<p> atominfo<code>AtomInfo</code>library valuesThis gives information about each atom, such as the symbol, name, and various atomic radii. </p>
<p> symmetrystringC1The Schoenflies symbol of the <code>point</code> group. This is case insensitive. It should be a subgroup of D2h . If it is auto, then the appropriate subgroup of D2h will be found. </p>
<p> symmetry_tolerancedouble1.0e-4When a molecule has symmetry, some atoms may be related by symmetry operations. The distance between given atoms and atoms generated by symmetry operations is compared to this threshold to determine if they are the same. If they are the same, then the coordinates are cleaned up to make them exactly symmetry equivalent. If the given molecule was produced by a optimization that started in C1 symmetry, but produced a roughly symmetric structure and you would like to begin using symmetry, then this may need to be increased a bit to properly symmetrize the molecule. </p>
<p> symmetry_framedouble[3][3][[1 0 0][0 1 0][0 0 1]]The symmetry frame. Ignored for symmetry = auto. </p>
<p> origindouble[3][0 0 0]The origin of the symmetry frame. Ignored for symmetry = auto. </p>
<p> redundant_atomsbooleanfalseIf true, do not generate symmetry equivalent atoms; they are already given in the input. It should not be necessary to specify this option, since, by default, if a symmetry operation duplicates an atom, the generated atom will not be added to the list of atoms. Ignored for symmetry = auto. </p>
<p> pdb_filestringundefinedThis gives the name of a PDB file, from which the nuclear coordinates will be read. If this is given, the following options will be ignored. </p>
<p> unitstringbohrThis gives the name of the units used for the geometry. See the <code>Units</code> class for information about the known units. This replaces deprecated keywords that are still recognized: angstrom and angstroms. This is ignored if pdb_file is given. </p>
<p> geometrydouble[][3]noneThis gives the Cartesian coordinates of the molecule. This is ignored if pdb_file is given. </p>
<p> atomsstring[]noneThis gives the Cartesian coordinates of the molecule. This is ignored if pdb_file is given. </p>
<p> ghostboolean[]noneIf true, the atom will be given zero charge. It will still have basis functions, however. This is used to estimate basis set superposition error. This is ignored if pdb_file is given. </p>
<p> chargedouble[]Z for each atomAllows specification of the charge for each atom. This is ignored if pdb_file is given. </p>
<p> atom_labelsstring[]noneThis gives a user defined atom label for each atom. This is ignored if pdb_file is given. </p>
<p> massdouble[]Taken from <code>AtomInfo</code> given by the atominfo keyword. This gives a user defined mass for each atom. This is ignored if pdb_file is given.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::Molecule::atom_at_position (double *, double tol = 0.05) const</h3>
<p>Takes an (x, y, z) postion and finds an atom within the given tolerance distance. If no atom is found -1 is returned.</p>
<h3>int sc::Molecule::atom_label_to_index (const char * label) const</h3>
<p>Returns the index of the atom with the given label. If the label cannot be found -1 is returned.</p>
<h3>int sc::Molecule::atom_to_unique (int iatom) const [inline]</h3>
<p>Converts an atom number to the number of its generating unique atom. The return value is in [0, nunique).</p>
<h3>int sc::Molecule::atom_to_unique_offset (int iatom) const</h3>
<p>Converts an atom number to the offset of this atom in the list of generated atoms. The unique atom itself is allows offset 0.</p>
<h3><code>SCVector3</code> sc::Molecule::center_of_mass () const</h3>
<p>Returns a <code>SCVector3</code> containing the cartesian coordinates of the center of mass for the molecule.</p>
<h3>double* sc::Molecule::charges () const</h3>
<p>Returns a double* containing the nuclear charges of the atoms. The caller is responsible for freeing the return value.</p>
<h3>void sc::Molecule::cleanup_molecule (double tol = 0.1)</h3>
<p>This will try to carefully correct symmetry errors in molecules. If any atom is out of place by more then tol, abort will be called.</p>
<h3><code>Ref</code>&lt;<code>PointGroup</code>&gt; sc::Molecule::highest_point_group (double tol = 1.0e-8) const</h3>
<p>Find this molecules true <code>point</code> group (limited to abelian groups). If the <code>point</code> group of this molecule is set to the highest <code>point</code> group, then the origin must first be set to the center of mass.</p>
<h3>int sc::Molecule::is_axis (<code>SCVector3</code> &amp; origin, <code>SCVector3</code> &amp; udirection, int order, double tol = 1.0e-8) const</h3>
<p>Return 1 if this given axis is a symmetry element for the molecule. The direction vector must be a unit vector.</p>
<h3>void sc::Molecule::is_linear_planar (int &amp; linear, int &amp; planar, double tol = 1.0e-5) const</h3>
<p>Sets linear to 1 if the molecular is linear, 0 otherwise. Sets planar to 1 if the molecular is planar, 0 otherwise.</p>
<h3>int sc::Molecule::is_plane (<code>SCVector3</code> &amp; origin, <code>SCVector3</code> &amp; uperp, double tol = 1.0e-8) const</h3>
<p>Return 1 if the given plane is a symmetry element for the molecule. The perpendicular vector must be a unit vector.</p>
<h3>const char* sc::Molecule::label (int atom) const</h3>
<p>Returns the label explicitly assigned to atom. If no label has been assigned, then null is returned.</p>
<h3>void sc::Molecule::nuclear_charge_efield (const double * charges, const double * position, double * efield)</h3>
<p><code>Compute</code> the electric field due to the given charges at the positions of the nuclei at the given <code>point</code>.</p>
<h3>void sc::Molecule::nuclear_repulsion_1der (int center, double xyz[3])</h3>
<p><code>Compute</code> the nuclear repulsion energy first derivative with respect to the given center.</p>
<h3>void sc::Molecule::principal_moments_of_inertia (double * evals, double ** evecs = 0) const</h3>
<p><code>Compute</code> the principal moments of inertia and, possibly, the principal axes.</p>
<h3>void sc::Molecule::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>void sc::Molecule::set_include_q (bool iq) [inline]</h3>
<p>If include_q is true, then include the &#8216;Q&#8217; atoms in the charge and efield routines.</p>
<h3>void sc::Molecule::set_include_qq (bool iqq) [inline]</h3>
<p>If include_qq is true, include the coupling between pairs of &#8216;Q&#8217; atoms when computing nuclear repulsion energy and gradients.</p>
<h3>void sc::Molecule::symmetrize (double tol = 0.5)</h3>
<p>If the molecule contains only symmetry unique atoms, this function will generate the other, redundant atoms. The redundant atom will only be generated if there is no other atoms within a distance of tol. If the is another atom and it is not identical, then abort will be called.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
