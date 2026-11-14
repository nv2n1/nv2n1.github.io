---
title: "sc_stddenfunctional(3)"
name: "sc_stddenfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stddenfunctional/"
description: "sc::StdDenFunctional –"
---

<p>sc::StdDenFunctional &#8211; </p>
<p> The <code>StdDenFunctional</code> class is used to construct the standard density functionals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::SumDenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>StdDenFunctional (const Ref&lt; KeyVal &gt; &amp;)


The name keyword is read from the input and is used to initialize the functional.


StdDenFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.



Protected Member Functions
void init_arrays (int n)



Protected Attributes
char * name_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>StdDenFunctional</code> class is used to construct the standard density functionals. </p>
<p> The table below lists the functional names and the equivalent functionals in other packages. The Name column gives the name as it is given in the input file (this is case sensitive). Functional names with non-alpha-numeric names should be given in double quotes. The description column gives the classes used to build up the functional and its coefficient, if it is other than one. The G98 column lists the equivalent functional in Gaussian 98 A.6. The NWChem column lists the equivalent functional in NWChem 3.3.1. </p>
<p> Name Description G98 NWChem XALPHA <code>XalphaFunctional</code> XALPHA HFS <code>SlaterXFunctional</code> HFS slater HFB <code>Becke88XFunctional</code> HFB becke88 HFG96 <code>G96XFunctional</code> G96LYP <code>G96XFunctional</code> +LYPCFunctional G96LYP BLYP <code>SlaterXFunctional</code> +Becke88XFunctional +LYPCFunctional BLYP SVWN1 <code>SlaterXFunctional</code> +VWN1LCFunctional slater vwn_1 SVWN1RPA<code>SlaterXFunctional</code> +<a href="/docs/linux/man/1-vwn1lcfunctional/">VWN1LCFunctional</a>(1) slater vwn_1_rpa SVWN2 <code>SlaterXFunctional</code> +VWN2LCFunctional slater vwn_2 SVWN3 <code>SlaterXFunctional</code> +VWN2LCFunctional slater vwn_3 SVWN4 <code>SlaterXFunctional</code> +VWN4LCFunctional slater vwn_4 SVWN5 <code>SlaterXFunctional</code> +VWN5LCFunctional SVWN5 slater vwn_5 SPZ81 <code>SlaterXFunctional</code> +PZ81LCFunctional SPL SPW92 <code>SlaterXFunctional</code> +PW92LCFunctional slater pw91lda BP86 <code>SlaterXFunctional</code> +Becke88XFunctional +P86CFunctional +PZ81LCFunctional becke88 perdue86 B3LYP 0.2 HF-Exchange + 0.8 <code>SlaterXFunctional</code> + 0.72 <code>Becke88XFunctional</code> + 0.19 VWN1<a href="/docs/linux/man/1-lcfunctional/">LCFunctional</a>(1) + 0.81 <code>LYPCFunctional</code> B3LYP b3lyp B3PW91 0.2 HF-Exchange + 0.8 <code>SlaterXFunctional</code> + 0.72 <code>Becke88XFunctional</code> + 0.19 <code>PW91CFunctional</code> + 0.81 <code>PW92LCFunctional</code> B3PW91 B3P86 0.2 HF-Exchange + 0.8 <code>SlaterXFunctional</code> + 0.72 <code>Becke88XFunctional</code> + 0.19 <code>P86CFunctional</code> + 0.81 <code>VWN1LCFunctional</code> (1)PBE <code>PBEXFunctional</code> +PBECFunctional xpbe96 cpbe96 PW91 <code>PW91XFunctional</code> +PW91CFunctional mPW(PW91)PW91 mPW91XFunctional(PW91) +PW91CFunctional PW91PW91mPWPW91 mPW91XFunctional(mPW91) +PW91CFunctional mPW1PW910.16 HF-Exchange + 0.84 mPW91XFunctional(mPW91) +PW91CFunctional</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::StdDenFunctional::StdDenFunctional (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The name keyword is read from the input and is used to initialize the functional. See the general <code>StdDenFunctional</code> description for a list of valid values for name.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::StdDenFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SumDenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
