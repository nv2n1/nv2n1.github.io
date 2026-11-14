---
title: "sc_atominfo(3)"
name: "sc_atominfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_atominfo/"
description: "sc::AtomInfo –"
---

<p>sc::AtomInfo &#8211; </p>
<p> The <code>AtomInfo</code> class provides information about atoms.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;atominfo.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Classes</h3>
<pre><code>struct atom



Public Member Functions</code></pre>
<p> <code>AtomInfo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>AtomInfo</code> <code>KeyVal</code> constructor is used to generate a <code>AtomInfo</code> object from the input.<br />
 <code>AtomInfo</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;s)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 double <code>vdw_radius</code> (int Z) const<br />
 <i>These return various measures of the atom&#8217;s radius. </i><br />
 double <code>bragg_radius</code> (int Z) const </p>
<p> double <code>atomic_radius</code> (int Z) const </p>
<p> double <code>maxprob_radius</code> (int Z) const </p>
<p> double <code>ip</code> (int Z) const<br />
 <i>Returns the atomization potential for atomic number Z. </i><br />
 double <code>vdw_radius_scale</code> () const<br />
 <i>Return the scale factor for the VdW radii. </i><br />
 double <code>bragg_radius_scale</code> () const<br />
 <i>Return the scale factor for the Bragg radii. </i><br />
 double <code>atomic_radius_scale</code> () const<br />
 <i>Return the scale factor for the atomic radii. </i><br />
 double <code>maxprob_radius_scale</code> () const<br />
 <i>Return the scale factor for the maximum probability radii. </i><br />
 double <code>rgb</code> (int Z, int color) const<br />
 <i>These return information about the color of the atom for visualization programs. </i><br />
 double <code>red</code> (int Z) const </p>
<p> double <code>green</code> (int Z) const </p>
<p> double <code>blue</code> (int Z) const </p>
<p> double <code>mass</code> (int Z) const<br />
 <i>This returns the mass of the most abundant isotope. </i><br />
 std::string <code>name</code> (int Z)<br />
 <i>This returns the full name of the element. </i><br />
 std::string <code>symbol</code> (int Z)<br />
 <i>This returns the symbol for the element. </i><br />
 int <code>string_to_Z</code> (const std::string &amp;, int allow_exceptions=1)<br />
 <i>This converts a name or symbol to the atomic number. </i></p>
<h2>Detailed Description</h2>
<p>The <code>AtomInfo</code> class provides information about atoms. </p>
<p> The information is kept in a file named atominfo.kv in the SC library directory. That information can be overridden by the user.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::AtomInfo::AtomInfo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>AtomInfo</code> <code>KeyVal</code> constructor is used to generate a <code>AtomInfo</code> object from the input. Default values will be read in from the atominfo.kv file in library directory. These can be overridden by specifying the keyword below. The library file is also read using a <code>KeyVal</code> constructor syntax, so consult that file for an example. </p>
<p> KeywordTypeDefaultDescription </p>
<p> mass:unitstringamuThe unit to be used for masses. See the <code>Units</code> class for more information about units. </p>
<p> mass:<i>symbol</i>doublelibrary valueThe mass associated with the given atomic symbol. </p>
<p> vdw_radius:unitstringbohrThe unit to be used for van der Waals radii. See the <code>Units</code> class for more information about units. </p>
<p> vdw_radius:scaling_factordouble1.0The scaling factor to be used for all van der Waals radii, including library values. </p>
<p> vdw_radius:<i>symbol</i>doublelibrary value The van der Waals radius associated with the given atomic symbol. </p>
<p> atomic_radius:unitstringbohrThe unit to be used for atomic radii. See the <code>Units</code> class for more information about units. </p>
<p> atomic_radius:scaling_factordouble1.0The scaling factor to be used for all atomic radii, including library values. </p>
<p> atomic_radius:<i>symbol</i>doublelibrary value The atomic radius associated with the given atomic symbol. </p>
<p> bragg_radius:unitstringbohrThe unit to be used for Bragg radii. See the <code>Units</code> class for more information about units. </p>
<p> bragg_radius:scaling_factordouble1.0The scaling factor to be used for all Bragg radii, including library values. </p>
<p> bragg_radius:<i>symbol</i>doublelibrary value The Bragg radius associated with the given atomic symbol. </p>
<p> maxprob_radius:unitstringbohrThe unit to be used for maximum probability radii. See the <code>Units</code> class for more information about units. </p>
<p> maxprob_radius:scaling_factordouble1.0The scaling factor to be used for all maximum probability radii, including library values. </p>
<p> maxprob_radius:<i>symbol</i>doublelibrary valueThe maximum probability radius associated with the given atomic symbol. </p>
<p> ip:unitstringHartreeThe unit to be used for ionization potentials. See the <code>Units</code> class for more information about units. </p>
<p> ip:<i>symbol</i>doublelibrary valueThe ionization potential for the given atom. </p>
<p> rgb:<i>symbol</i>double[3]library valueA vector with the red, green, and blue values used to color each atom. Each element is between 0 (off) and 1 (on).</p>
<h2>Member Function Documentation</h2>
<h3>double sc::AtomInfo::rgb (int Z, int color) const</h3>
<p>These return information about the color of the atom for visualization programs.</p>
<h3>void sc::AtomInfo::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
