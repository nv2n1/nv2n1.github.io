---
title: "sc_units(3)"
name: "sc_units"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_units/"
description: "sc::Units –"
---

<p>sc::Units &#8211; </p>
<p> The <code>Units</code> class is used to perform unit converions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;units.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Storage</code> { <code>Steal</code>, <code>Copy</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>Units (const char *strrep)


Create using a string representation, like 'kcal/mol'.


Units (char *strrep, Units::Storage=Units::Copy)


Create using a string representation, like 'kcal/mol'.


Units (StateIn &amp;s)


Restore the state of a Units object from s.


double to (const Ref&lt; Units &gt; &amp;u) const


The conversion factor from this to u.


double from (const Ref&lt; Units &gt; &amp;u) const


The conversion factor from u to this.


double to_atomic_units () const


The conversion factor from this to atomic units.


double from_atomic_units () const


The conversion factor from atom units to this.


const char * string_rep () const


The string representation of the units.


void save_data_state (StateOut &amp;s)


Save the state of the Units object to s.



Protected Member Functions
void parse_unit ()



Protected Attributes
char * strrep_



double to_atomic_units_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>Units</code> class is used to perform unit converions.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Units::Units (char * strrep, Units::Storage = Units::Copy)</h3>
<p>Create using a string representation, like &#8216;kcal/mol&#8217;. if Units::Steal is given is the second argment, the new <code>Units</code> object will delete the strrep argument when it is destroyed.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
