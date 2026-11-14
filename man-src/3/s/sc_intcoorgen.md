---
title: "sc_intcoorgen(3)"
name: "sc_intcoorgen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_intcoorgen/"
description: "sc::IntCoorGen –"
---

<p>sc::IntCoorGen &#8211; </p>
<p> <code>IntCoorGen</code> generates a set of simple internal coordinates for a molecule.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/coor.h">coor.h</a>&gt; </p>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>IntCoorGen</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, int nextra=0, int *extra=0)<br />
 <i>Create an </i><code>IntCoorGen</code> given a <code>Molecule</code> and, optionally, extra bonds.<br />
 <code>IntCoorGen</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 <code>IntCoorGen</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Standard member. </i><br />
 virtual void <code>generate</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;)<br />
 <i>This generates a set of internal coordinates. </i><br />
 virtual void <code>print</code> (std::ostream &amp;out=ExEnv::out0()) const<br />
 <i>Print out information about this. </i></p>
<h3>Protected Member Functions</h3>
<p> void <code>init_constants</code> () </p>
<p> double <code>cos_ijk</code> (<code>Molecule</code> &amp;m, int i, int j, int k) </p>
<p> int <code>hterminal</code> (<code>Molecule</code> &amp;m, <code>BitArrayLTri</code> &amp;bonds, int i) </p>
<p> int <code>nearest_contact</code> (int i, <code>Molecule</code> &amp;m) </p>
<p> void <code>add_bonds</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;list, <code>BitArrayLTri</code> &amp;bonds, <code>Molecule</code> &amp;m) </p>
<p> void <code>add_bends</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;list, <code>BitArrayLTri</code> &amp;bonds, <code>Molecule</code> &amp;m) </p>
<p> void <code>add_tors</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;list, <code>BitArrayLTri</code> &amp;bonds, <code>Molecule</code> &amp;m) </p>
<p> void <code>add_out</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;list, <code>BitArrayLTri</code> &amp;bonds, <code>Molecule</code> &amp;m) </p>
<h3>Protected Attributes</h3>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>molecule_</code> </p>
<p> int <code>linear_bends_</code> </p>
<p> int <code>linear_lbends_</code> </p>
<p> int <code>linear_tors_</code> </p>
<p> int <code>linear_stors_</code> </p>
<p> int <code>nextra_bonds_</code> </p>
<p> int * <code>extra_bonds_</code> </p>
<p> double <code>linear_bend_thres_</code> </p>
<p> double <code>linear_tors_thres_</code> </p>
<p> double <code>radius_scale_factor_</code> </p>
<h2>Detailed Description</h2>
<p> <code>IntCoorGen</code> generates a set of simple internal coordinates for a molecule. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::IntCoorGen::IntCoorGen (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, int nextra = 0, int * extra = 0)</h3>
<p> Create an <code>IntCoorGen</code> given a <code>Molecule</code> and, optionally, extra bonds. <code>IntCoorGen</code> keeps a reference to extra and deletes it when the destructor is called.</p>
<h3>sc::IntCoorGen::IntCoorGen (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p> The <code>KeyVal</code> constructor. .IP &quot;molecule&quot; 1c A <code>Molecule</code> object. There is no default. </p>
<dl COMPACT>
<dt>radius_scale_factor</p>
<dd> If the distance between two atoms is less than the radius scale factor times the sum of the atoms&#8217; atomic radii, then a bond is placed between the two atoms for the purpose of finding internal coordinates. The default is 1.1.</dl>
<dl COMPACT>
<dt>linear_bend_threshold</p>
<dd> A bend angle in degress greater than 180 minus this keyword&#8217;s floating <code>point</code> value is considered a linear bend. The default is 1.0.</dl>
<dl COMPACT>
<dt>linear_tors_threshold</p>
<dd> The angles formed by atoms a-b-c and b-c-d are checked for near linearity. If an angle in degrees is greater than 180 minus this keyword&#8217;s floating <code>point</code> value, then the torsion is classified as a linear torsion. The default is 1.0.</dl>
<dl COMPACT>
<dt>linear_bend</p>
<dd> Generate <code>BendSimpleCo</code> objects to describe linear bends. The default is false.</dl>
<dl COMPACT>
<dt>linear_lbend</p>
<dd> Generate pairs of <code>LinIPSimpleCo</code> and <code>LinIPSimpleCo</code> objects to describe linear bends. The default is true.</dl>
<dl COMPACT>
<dt>linear_tors</p>
<dd> Generate <code>TorsSimpleCo</code> objects to described linear torsions. The default is false.</dl>
<dl COMPACT>
<dt>linear_stors</p>
<dd> Generate <code>ScaledTorsSimpleCo</code> objects to described linear torsions. The default is true.</dl>
<dl COMPACT>
<dt>extra_bonds</p>
<dd> This is a vector of atom numbers, where elements $2 (i-1) + 1$ and $2 i$ specify the atoms which are bound in extra bond $i$. The extra_bonds keyword should only be needed for weakly interacting fragments, otherwise all the needed bonds will be found.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
