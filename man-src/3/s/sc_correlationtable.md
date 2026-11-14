---
title: "sc_correlationtable(3)"
name: "sc_correlationtable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_correlationtable/"
description: "sc::CorrelationTable –"
---

<p>sc::CorrelationTable &#8211; </p>
<p> The <code>CorrelationTable</code> class provides a correlation table between two <code>point</code> groups.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;corrtab.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CorrelationTable (const Ref&lt; PointGroup &gt; &amp;group, const Ref&lt; PointGroup &gt; &amp;subgroup)


Create a correlation table for the two groups.


Ref&lt; PointGroup &gt; group () const


Returns the higher order point group.


Ref&lt; PointGroup &gt; subgroup () const


Returns the lower order point group.


int initialize_table (const Ref&lt; PointGroup &gt; &amp;group, const Ref&lt; PointGroup &gt; &amp;subgroup)


Initalize the correlation table.


const char * error (int errcod)


Converts error codes from initialize_table into a text string.


int n () const


Returns the number of irreps in the high order group.


int subn () const


Returns the number of irreps in the subgroup.


int degen (int igamma) const


Returns the degeneracy of the irrep.


int subdegen (int igamma) const


Returns the degeneracy of the subgroup irrep.


int ngamma (int igamma) const


Returns the number of irreps in the low order group that an irrep.


int gamma (int igamma, int i) const


Returns the irreps in the low order group that an irrep from the high order group can be reduced to.


void print (std::ostream &amp;o=ExEnv::out0()) const</code></pre>
<h2>Detailed Description</h2>
<p>The <code>CorrelationTable</code> class provides a correlation table between two <code>point</code> groups.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::CorrelationTable::gamma (int igamma, int i) const [inline]</h3>
<p>Returns the irreps in the low order group that an irrep from the high order group can be reduced to.</p>
<h3>int sc::CorrelationTable::initialize_table (const <code>Ref</code>&lt; <code>PointGroup</code> &gt; &amp; group, const <code>Ref</code>&lt; <code>PointGroup</code> &gt; &amp; subgroup)</h3>
<p>Initalize the correlation table. Returns 0 for success and nonzero for failure. This will fail if the subgroup is not really a subgroup of group.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
