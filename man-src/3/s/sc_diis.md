---
title: "sc_diis(3)"
name: "sc_diis"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_diis/"
description: "sc::DIIS –"
---

<p>sc::DIIS &#8211; </p>
<p> The <code>DIIS</code> class provides <code>DIIS</code> extrapolation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;diis.h&gt;</code></pre>
<p> Inherits <code>sc::SelfConsistentExtrapolation</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DIIS (int strt=1, int ndi=5, double dmp=0, int ngr=1, int ngrdiis=1)



DIIS (StateIn &amp;)



DIIS (const Ref&lt; KeyVal &gt; &amp;)


The DIIS KeyVal constructor recognizes the following keywords:.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int extrapolate (const Ref&lt; SCExtrapData &gt; &amp;data, const Ref&lt; SCExtrapError &gt; &amp;error)



void start_extrapolation ()



void reinitialize ()



void print (std::ostream &amp;=ExEnv::out0()) const


Override DescribedClass::print.



Protected Member Functions
void init ()



Protected Attributes
int start



int ndiis



int iter



int ngroup



int ngroupdiis



double damping_factor



double * btemp



double ** bold



double ** bmat



Ref&lt; SCExtrapData &gt; dtemp_data



Ref&lt; SCExtrapError &gt; dtemp_error



Ref&lt; SCExtrapData &gt; Ldata



Ref&lt; SCExtrapData &gt; * diism_data



Ref&lt; SCExtrapError &gt; * diism_error</code></pre>
<h2>Detailed Description</h2>
<p>The <code>DIIS</code> class provides <code>DIIS</code> extrapolation.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::DIIS::DIIS (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>DIIS</code> <code>KeyVal</code> constructor recognizes the following keywords:. .IP &quot;n&quot; 1c This integer maximum number of data sets to retain. The default is 5. </p>
<dl>
<dt>start</p>
<dd>The <code>DIIS</code> extrapolation will begin on the iteration given by this integer. The default is 1.</dl>
<dl>
<dt>damping_factor</p>
<dd>This nonnegative floating <code>point</code> number is used to dampen the <code>DIIS</code> extrapolation. The default is 0.0.</dl>
<dl>
<dt>ngroup</p>
<dd>The number of iterations in a <code>DIIS</code> group. <code>DIIS</code> extrapolation is only used for the first ngroupdiis of these interations. The default is 1. If ngroup is 1 and ngroupdiis is greater than 0, then <code>DIIS</code> will be used on all iterations after and including the start iteration.</dl>
<dl>
<dt>ngroupdiis</p>
<dd>The number of <code>DIIS</code> extrapolations to do at the beginning of an iteration group. See the documentation for ngroup.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::DIIS::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SelfConsistentExtrapolation</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
