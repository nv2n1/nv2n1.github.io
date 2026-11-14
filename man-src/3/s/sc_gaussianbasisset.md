---
title: "sc_gaussianbasisset(3)"
name: "sc_gaussianbasisset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gaussianbasisset/"
description: "sc::GaussianBasisSet –"
---

<p>sc::GaussianBasisSet &#8211; </p>
<p> The <code>GaussianBasisSet</code> class is used describe a basis set composed of atomic gaussian orbitals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;gaussbas.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Classes</h3>
<p>class <code>ValueData</code><br />
 <i>This holds scratch data needed to compute basis function values. </i></p>
<h3>Public Types</h3>
<p>enum <code>UnitType</code> { <code>Unit</code> }<br />
 <i>This can be given to a CTOR to construct a unit basis function. </i></p>
<h3>Public Member Functions</h3>
<pre><code>GaussianBasisSet (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


GaussianBasisSet (UnitType)


This can be given GaussianBasisSet::Unit to construct a basis set with a single basis function that is one everywhere.


GaussianBasisSet (StateIn &amp;)



Ref&lt; GaussianBasisSet &gt; operator+ (const Ref&lt; GaussianBasisSet &gt; &amp;B)


Returns a GaussianBasisSet object that consists of the basis functions for each atom in this followed by the basis functions in B for the corresponding atom.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


const char * name () const


Return the name of the basis set (is nonnull only if keyword 'name' was provided).


const char * label () const


Return the label of the basis set.


Ref&lt; Molecule &gt; molecule () const


Return the Molecule object.


Ref&lt; SCMatrixKit &gt; matrixkit ()


Returns the SCMatrixKit that is to be used for AO bases.


Ref&lt; SCMatrixKit &gt; so_matrixkit ()


Returns the SCMatrixKit that is to be used for SO bases.


RefSCDimension basisdim ()


Returns the SCDimension object for the dimension.


int ncenter () const


Return the number of centers.


int nshell () const


Return the number of shells.


int nshell_on_center (int icenter) const


Return the number of shells on the given center.


int shell_on_center (int icenter, int shell) const


Return an overall shell number, given a center and the shell number on that center.


int shell_to_center (int ishell) const


Return the center on which the given shell is located.


int shell_to_primitive (int ishell) const


Return the overall index of the first primitive from the given shell.


int nbasis () const


Return the number of basis functions.


int nbasis_on_center (int icenter) const


Return the number of basis functions on the given center.


int nprimitive () const


Return the number of primitive Gaussians.


int has_pure () const


Return true if basis contains solid harmonics Gaussians.


int max_nfunction_in_shell () const


Return the maximum number of functions that any shell has.


int max_ncartesian_in_shell (int aminc=0) const


Return the maximum number of Cartesian functions that any shell has.


int max_nprimitive_in_shell () const


Return the maximum number of primitive Gaussian that any shell has.


int max_angular_momentum () const


Return the highest angular momentum in any shell.


int max_ncontraction () const


Return the maximum number of Gaussians in a contraction in any shell.


int max_am_for_contraction (int con) const


Return the maximum angular momentum found in the given contraction number for any shell.


int max_cartesian () const


Return the maximum number of Cartesian functions in any shell.


int shell_to_function (int i) const


Return the number of the first function in the given shell.


int function_to_shell (int i) const


Return the shell to which the given function belongs.


const GaussianShell &amp; operator() (int i) const


Return a reference to GaussianShell number i.


GaussianShell &amp; operator() (int i)


Return a reference to GaussianShell number i.


const GaussianShell &amp; operator[] (int i) const


Return a reference to GaussianShell number i.


GaussianShell &amp; operator[] (int i)


Return a reference to GaussianShell number i.


const GaussianShell &amp; shell (int i) const


Return a reference to GaussianShell number i.


GaussianShell &amp; shell (int i)


Return a reference to GaussianShell number i.


const GaussianShell &amp; operator() (int icenter, int ishell) const


Return a reference to GaussianShell number ishell on center icenter.


GaussianShell &amp; operator() (int icenter, int ishell)


Return a reference to GaussianShell number ishell on center icenter.


const GaussianShell &amp; shell (int i, int j) const


Return a reference to GaussianShell number j on center i.


GaussianShell &amp; shell (int i, int j)


Return a reference to GaussianShell number j on center i.


double r (int icenter, int xyz) const


The location of center icenter.


int values (const SCVector3 &amp;r, ValueData *, double *basis_values) const


Compute the values for this basis set at position r.


int grad_values (const SCVector3 &amp;r, ValueData *, double *g_values, double *basis_values=0) const


Like values(.


int hessian_values (const SCVector3 &amp;r, ValueData *, double *h_values, double *g_values=0, double *basis_values=0) const


Like values(.


int shell_values (const SCVector3 &amp;r, int sh, ValueData *, double *basis_values) const


Compute the values for the given shell functions at position r.


int grad_shell_values (const SCVector3 &amp;r, int sh, ValueData *, double *g_values, double *basis_values=0) const


Like values(.


int hessian_shell_values (const SCVector3 &amp;r, int sh, ValueData *, double *h_values, double *g_values=0, double *basis_values=0) const


Like values(.


int equiv (const Ref&lt; GaussianBasisSet &gt; &amp;b)


Returns true if this and the argument are equivalent.


void print_brief (std::ostream &amp;=ExEnv::out0()) const


Print a brief description of the basis set.


void print (std::ostream &amp;=ExEnv::out0()) const


Print a detailed description of the basis set.



Protected Member Functions</code></pre>
<p> <code>GaussianBasisSet</code> (const <code>GaussianBasisSet</code> &amp;) </p>
<p> virtual void <code>set_matrixkit</code> (const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)</p>
<h2>Detailed Description</h2>
<p>The <code>GaussianBasisSet</code> class is used describe a basis set composed of atomic gaussian orbitals. </p>
<p> Inputs for common basis sets are included in the MPQC distribution. They have been obtained from the EMSL Basis Set Database and translated into the MPQC format. The citation for this database is below. The technical citation for each basis set is listed in the individual basis set data files, in MPQC&#8217;s lib/basis directory. </p>
<p> Following is a table with available basis sets listing the supported elements for each basis and the number of basis functions for H, $n_0$, first row, $n_1$, and second row, $n_2$, atoms. Basis sets with non-alpha-numerical characters in their name must be given in quotes. </p>
<p> Basis SetElements$n_0$$n_1$$n_2$ STO-2GH-Ca159 STO-3GH-Kr159 STO-3G*H-Ar1514 STO-6GH-Kr159 MINI (Huzinaga)H-Ca159 MINI (Scaled)H-Ca159 MIDI (Huzinaga)H-Na, Al-K2913 DZ (Dunning)H, Li, B-Ne, Al-Cl21018 DZP (Dunning)H, Li, B-Ne, Al-Cl51624 DZP + Diffuse (Dunning)H, B-Ne6193-21GH-Kr2913 3-21G*H-Ar2919 3-21++GH-Ar31317 3-21++G*H-Ar31323 4-31GH-Ne, P-Cl2913 6-31GH-Zn2913 6-31G*H-Zn21519 6-31G**H-Zn51519 6-31+G*H-Ar21923 6-31++GH-Ca31317 6-31++G*H-Ar31923 6-31++G**H-Ar61923 6-311GH-Ca, Ga-Kr31321 6-311G*H-Ca, Ga-Kr31826 6-311G**H-Ca, Ga-Kr61826 6-311G(2df,2pd)H-Ne, K, Ca14306-311++G**H-Ne7226-311++G(2d,2p)H-Ca102735 6-311++G(3df,3pd)H-Ar183947 cc-pVDZH-Ar, Ca, Ga-Kr51418 cc-pVTZH-Ar, Ca, Ga-Kr143034 cc-pVQZH-Ar, Ca, Ga-Kr305559 cc-pV5ZH-Ar, Ca, Ga-Kr559195 cc-pV6ZH, He, B-Ne, Al-Ar91140144 aug-cc-pVDZH, He, B-Ne, Al-Ar, Ga-Kr92327 aug-cc-pVTZH, He, B-Ne, Al-Ar, Ga-Kr234650 aug-cc-pVQZH, He, B-Ne, Al-Ar, Ga-Kr468084 aug-cc-pV5ZH, He, B-Ne, Al-Ar, Ga-Kr80127131 aug-cc-pV6ZH, He, B-Ne, Al-Ar127189193 cc-pCVDZLi, B-Ar1827 cc-pCVTZLi, B-Ar4359 cc-pCVQZLi, B-Ar84109 cc-pCV5ZB-Ne145aug-cc-pCVDZB-F, Al-Ar2736 aug-cc-pCVTZB-Ne, Al-Ar5975 aug-cc-pCVQZB-Ne, Al-Ar109134 aug-cc-pCV5ZB-F181NASA Ames ANOH, B-Ne, Al, P, Ti, Fe, Ni305559 pc-0H, C-F, Si-Cl2913 pc-1H, C-F, Si-Cl51418 pc-2H, C-F, Si-Cl143034 pc-3H, C-F, Si-Cl346464 pc-4H, C-F, Si-Cl63109105 pc-0-augH, C-F, Si-Cl31317 pc-1-augH, C-F, Si-Cl92327 pc-2-augH, C-F, Si-Cl234650 pc-3-augH, C-F, Si-Cl508989 pc-4-augH, C-F, Si-Cl88145141 </p>
<p> All basis sets except for the pc-<i>n</i> and pc-<i>n</i>-aug basis sets were obtained from the Extensible Computational Chemistry Environment Basis Set Database, Version 12/03/03, as developed and distributed by the Molecular Science Computing Facility, Environmental and Molecular Sciences Laboratory which is part of the Pacific Northwest Laboratory, P.O. Box 999, Richland, Washington 99352, USA, and funded by the U.S. Department of Energy. The Pacific Northwest Laboratory is a multi-program laboratory operated by Battelle Memorial Institute for the U.S. Department of Energy under contract DE-AC06-76RLO 1830. Contact David Feller or Karen Schuchardt for further information. </p>
<p> The pc-<i>n</i> and pc-<i>n</i>-aug basis sets are the polarization consistent basis sets of Frank Jensen. See J. Chem. Phys. 115 (2001) 9113; J. Chem. Phys. 116 (2002) 7372; J. Chem. Phys. 117 (2002) 9234; and J. Chem. Phys. 121 (2004) 3463.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::GaussianBasisSet::GaussianBasisSet (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;molecule&quot; 1c The gives a <code>Molecule</code> object. The is no default. </p>
<dl>
<dt>puream</p>
<dd>If this boolean parameter is true then 5D, 7F, etc. will be used. Otherwise all cartesian functions will be used. The default depends on the particular basis set.</dl>
<dl>
<dt>name</p>
<dd>This is a string giving the name of the basis set. The above table of basis sets gives some of the recognized basis set names. It may be necessary to put the name in double quotes. There is no default.</dl>
<dl>
<dt>basis</p>
<dd>This is a vector of basis set names that can give a different basis set to each atom in the molecule. If the element vector is given, then it gives different basis sets to different elements. The default is to give every atom the basis set specified in name.</dl>
<dl>
<dt>element</p>
<dd>This is a vector of elements. If it is given then it must have the same number of entries as the basis vector.</dl>
<dl>
<dt>basisdir</p>
<dd>A string giving a directory where basis set data files are to be sought. See the text below for a complete description of what directories are consulted.</dl>
<dl>
<dt>basisfiles</p>
<dd>Each keyword in this vector of files is appended to the directory specified with basisdir and basis set data is read from them.</dl>
<dl>
<dt>matrixkit</p>
<dd>Specifies a <code>SCMatrixKit</code> object. It is usually not necessary to give this keyword, as the default action should get the correct <code>SCMatrixKit</code>.</dl>
<p> Several files in various directories are checked for basis set data. First, basis sets can be given by the user in the basis section at the top level of the main input file. Next, if a path is given with the basisdir keyword, then all of the files given with the basisfiles keyword are read in after appending their names to the value of basisdir. Basis sets can be given in these files in the basis section at the top level as well. If the named basis set still cannot be found, then <code>GaussianBasisSet</code> will try convert the basis set name to a file name and check first in the directory given by basisdir. Next it checks for the environment variable SCLIBDIR. If it is set it will look for the basis file in $SCLIBDIR/basis. Otherwise it will look in the source code distribution in the directory SC/lib/basis. If the executable has changed machines or the source code has be moved, then it may be necessary to copy the library files to your machine and set the SCLIBDIR environmental variable. </p>
<p> The basis set itself is also given in the <code>ParsedKeyVal</code> format. There are two recognized formats for basis sets:</p>
<dl>
<dt><code>array of shells</code></p>
<dd>One must specify the keyword :basis: followed by the lowercase atomic name followed by : followed by the basis set name (which may need to be placed inside double quotes). The value for the keyword is an array of shells. Each shell reads the following keywords:</dl>
<dl>
<dt>type</p>
<dd>This is a vector that describes each component of this shell. For each element the following two keywords are read:</dl>
<dl>
<dt>am</p>
<dd>The angular momentum of the component. This can be given as the letter designation, s, p, d, etc. There is no default.</dl>
<dl>
<dt>puream</p>
<dd>If this boolean parameter is true then 5D, 7F, etc. shells are used. The default is false. This parameter can be overridden in the <code>GaussianBasisSet</code> specification.</dl>
<dl>
<dt>exp</p>
<dd>This is a vector giving the exponents of the primitive Gaussian functions.</dl>
<dl>
<dt>coef</p>
<dd>This is a matrix giving the coeffients of the primitive Gaussian functions. The first index gives the component number of the shell and the second gives the primitive number.</dl>
<dl>
<dd>An example might be easier to understand. This is a basis set specificition for STO-2G carbon:</dl>
<pre> basis: (
 carbon: 'STO-2G': [
 (type: [(am = s)]
 { exp coef:0 } = {
 27.38503303 0.43012850
 4.87452205 0.67891353
 })
 (type: [(am = p) (am = s)]
 { exp coef:1 coef:0 } = {
 1.13674819 0.04947177 0.51154071
 0.28830936 0.96378241 0.61281990
 })
 ]
 )</pre>
<dl>
<dt><code>basis set of even-tempered primitive Gaussians</code></p>
<dd>Such basis set format is given as a group of keywords. The name of the group is :basis: followed by the lowercase atomic name followed by : followed by the basis set name (which may need to be placed inside double quotes). The group of keywords must contain vectors am and nprim, which specify the angular momentum and the number of shells in each block of even-tempered primitives. In addition, one must provide any two of the following vectors:</dl>
<dl>
<dt>first_exp</p>
<dd>The exponent of the &#8216;tightest&#8217; primitive Gaussian in the block.</dl>
<dl>
<dt>last_exp</p>
<dd>The exponent of the most &#8216;diffuse&#8217; primitive Gaussian in the block.</dl>
<dl>
<dt>exp_ratio</p>
<dd>The ratio of exponents of consecutive primitive Gaussians in the block.</dl>
<dl>
<dd>Note that the dimensions of each vector must be the same.</dl>
<p> Here&#8217;s an example of a basis set composed of 2 blocks of even-tempered s-functions and 1 block of even-tempered p-functions. </p>
<pre> basis: (
 neon: '20s5s13p':(</pre>
<pre> am = [ 0 0 1 ]
 nprim = [ 20 5 13 ]
 first_exp = [ 1000.0 0.1 70.0 ]
 last_exp = [ 1.0 0.01 0.1 ]</pre>
<pre> )
 )</pre>
<h3>sc::GaussianBasisSet::GaussianBasisSet (<code>UnitType</code>)</h3>
<p>This can be given GaussianBasisSet::Unit to construct a basis set with a single basis function that is one everywhere. This can be used with integral evaluators to compute certain classes of integrals, with limitations.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::GaussianBasisSet::grad_shell_values (const <code>SCVector3</code> &amp; r, int sh, <code>ValueData</code> *, double * g_values, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes gradients of the shell function values, too. See the other grad_values(&#8230;) members for more information.</p>
<h3>int sc::GaussianBasisSet::grad_values (const <code>SCVector3</code> &amp; r, <code>ValueData</code> *, double * g_values, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes gradients of the basis function values, too. The g_values argument must be vector of length 3*nbasis. The data will be written in the order bf1_x, bf1_y, bf1_z, &#8230;</p>
<h3>int sc::GaussianBasisSet::hessian_shell_values (const <code>SCVector3</code> &amp; r, int sh, <code>ValueData</code> *, double * h_values, double * g_values = 0, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes first and second derivatives of the shell function values, too. See the other hessian_values(&#8230;) members for more information.</p>
<h3>int sc::GaussianBasisSet::hessian_values (const <code>SCVector3</code> &amp; r, <code>ValueData</code> *, double * h_values, double * g_values = 0, double * basis_values = 0) const</h3>
<p>Like values(. ..), but computes first and second derivatives of the basis function values, too. h_values must be vector of length 6*nbasis. The data will be written in the order bf1_xx, bf1_yx, bf1_yy, bf1_zx, bf1_zy, bf1_zz, &#8230;</p>
<h3>const char* sc::GaussianBasisSet::label () const [inline]</h3>
<p>Return the label of the basis set. <code>label()</code> return the same string as <code>name()</code> if keyword &#8216;name&#8217; was provided, otherwise it is a unique descriptive string which can be arbitrarily long. </p>
<p> References name().</p>
<h3>int sc::GaussianBasisSet::max_am_for_contraction (int con) const</h3>
<p>Return the maximum angular momentum found in the given contraction number for any shell.</p>
<h3>int sc::GaussianBasisSet::max_ncartesian_in_shell (int aminc = 0) const</h3>
<p>Return the maximum number of Cartesian functions that any shell has. The optional argument is an angular momentum increment.</p>
<h3><code>Ref</code>&lt;<code>GaussianBasisSet</code>&gt; sc::GaussianBasisSet::operator+ (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; B)</h3>
<p>Returns a <code>GaussianBasisSet</code> object that consists of the basis functions for each atom in this followed by the basis functions in B for the corresponding atom. The <code>Molecule</code> object for the two basis sets must be identical.</p>
<h3>double sc::GaussianBasisSet::r (int icenter, int xyz) const</h3>
<p>The location of center icenter. The xyz argument is 0 for x, 1 for y, and 2 for z.</p>
<h3>void sc::GaussianBasisSet::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>int sc::GaussianBasisSet::shell_on_center (int icenter, int shell) const</h3>
<p>Return an overall shell number, given a center and the shell number on that center.</p>
<h3>int sc::GaussianBasisSet::shell_values (const <code>SCVector3</code> &amp; r, int sh, <code>ValueData</code> *, double * basis_values) const</h3>
<p><code>Compute</code> the values for the given shell functions at position r. See the other values(&#8230;) members for more information.</p>
<h3>int sc::GaussianBasisSet::values (const <code>SCVector3</code> &amp; r, <code>ValueData</code> *, double * basis_values) const</h3>
<p><code>Compute</code> the values for this basis set at position r. The basis_values argument must be vector of length nbasis.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
