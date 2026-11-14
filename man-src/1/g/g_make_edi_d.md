---
title: "g_make_edi_d(1)"
name: "g_make_edi_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_make_edi_d/"
description: "make_edi – generate input files for essential dynamics sampling"
---

<h2>NAME</h2>
<p> make_edi &#8211; generate input files for essential dynamics sampling </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>make_edi</code> <code>-f</code><i> eigenvec.trr </i> <code>-eig</code><i> eigenval.xvg </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-tar</code><i> target.gro </i> <code>-ori</code><i> origin.gro </i> <code>-o</code><i> sam.edi </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]xvgr</code><i></i> <code>-mon</code><i> string </i> <code>-linfix</code><i> string </i> <code>-linacc</code><i> string </i> <code>-flood</code><i> string </i> <code>-radfix</code><i> string </i> <code>-radacc</code><i> string </i> <code>-radcon</code><i> string </i> <code>-outfrq</code><i> int </i> <code>-slope</code><i> real </i> <code>-maxedsteps</code><i> int </i> <code>-deltaF0</code><i> real </i> <code>-deltaF</code><i> real </i> <code>-tau</code><i> real </i> <code>-eqsteps</code><i> int </i> <code>-Eflnull</code><i> real </i> <code>-T</code><i> real </i> <code>-alpha</code><i> real </i> <code>-linstep</code><i> string </i> <code>-accdir</code><i> string </i> <code>-radstep</code><i> real </i> <code>-[no]restrain</code><i></i> <code>-[no]hessian</code><i></i> <code>-[no]harmonic</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> <code> make_edi</code> generates an essential dynamics (ED) sampling input file to be used with mdrun based on eigenvectors of a covariance matrix (<code> g_covar</code>) or from a normal modes anaysis (<code> g_nmeig</code>). ED sampling can be used to manipulate the position along collective coordinates (eigenvectors) of (biological) macromolecules during a simulation. Particularly, it may be used to enhance the sampling efficiency of MD simulations by stimulating the system to explore new regions along these collective coordinates. A number of different algorithms are implemented to drive the system along the eigenvectors (<code> -linfix</code>, <code> -linacc</code>, <code> -radfix</code>, <code> -radacc</code>, <code> -radcon</code>), to keep the position along a certain (set of) coordinate(s) fixed (<code> -linfix</code>), or to only monitor the projections of the positions onto these coordinates (<code> -mon</code>). </p>
<p> References: </p>
<p> A. Amadei, A.B.M. Linssen, B.L. de Groot, D.M.F. van Aalten and H.J.C. Berendsen; An efficient method for sampling the essential subspace of proteins., J. Biomol. Struct. Dyn. 13:615-626 (1996) </p>
<p> B.L. de Groot, A. Amadei, D.M.F. van Aalten and H.J.C. Berendsen; Towards an exhaustive sampling of the configurational spaces of the two forms of the peptide hormone guanylin,J. Biomol. Struct. Dyn. 13 : 741-751 (1996) </p>
<p> B.L. de Groot, A.Amadei, R.M. Scheek, N.A.J. van Nuland and H.J.C. Berendsen; An extended sampling of the configurational space of HPr from E. coli PROTEINS: Struct. Funct. Gen. 26: 314-322 (1996) </p>
<p> You will be prompted for one or more index groups that correspond to the eigenvectors, reference structure, target positions, etc. </p>
<p> <code> -mon</code>: monitor projections of the coordinates onto selected eigenvectors. </p>
<p> <code> -linfix</code>: perform fixed-step linear expansion along selected eigenvectors. </p>
<p> <code> -linacc</code>: perform acceptance linear expansion along selected eigenvectors. (steps in the desired directions will be accepted, others will be rejected). </p>
<p> <code> -radfix</code>: perform fixed-step radius expansion along selected eigenvectors. </p>
<p> <code> -radacc</code>: perform acceptance radius expansion along selected eigenvectors. (steps in the desired direction will be accepted, others will be rejected). Note: by default the starting MD structure will be taken as origin of the first expansion cycle for radius expansion. If <code> -ori</code> is specified, you will be able to read in a structure file that defines an external origin. </p>
<p> <code> -radcon</code>: perform acceptance radius contraction along selected eigenvectors towards a target structure specified with <code> -tar</code>. </p>
<p> NOTE: each eigenvector can be selected only once. </p>
<p> <code> -outfrq</code>: frequency (in steps) of writing out projections etc. to .edo file </p>
<p> <code> -slope</code>: minimal slope in acceptance radius expansion. A new expansion cycle will be started if the spontaneous increase of the radius (in nm/step) is less than the value specified. </p>
<p> <code> -maxedsteps</code>: maximum number of steps per cycle in radius expansion before a new cycle is started. </p>
<p> Note on the parallel implementation: since ED sampling is a &#8216;global&#8217; thing (collective coordinates etc.), at least on the &#8216;protein&#8217; side, ED sampling is not very parallel-friendly from an implentation point of view. Because parallel ED requires much extra communication, expect the performance to be lower as in a free MD simulation, especially on a large number of nodes. </p>
<p> All output of mdrun (specify with -eo) is written to a .edo file. In the output file, per OUTFRQ step the following information is present: </p>
<p> * the step number </p>
<p> * the number of the ED dataset. (Note that you can impose multiple ED constraints in a single simulation &#8211; on different molecules e.g. &#8211; if several .edi files were concatenated first. The constraints are applied in the order they appear in the .edi file.) </p>
<p> * RMSD (for atoms involved in fitting prior to calculating the ED constraints) </p>
<p> * projections of the positions onto selected eigenvectors </p>
<p> FLOODING: </p>
<p> with -flood you can specify which eigenvectors are used to compute a flooding potential, which will lead to extra forces expelling the structure out of the region described by the covariance matrix. If you switch -restrain the potential is inverted and the structure is kept in that region. </p>
<p> The origin is normally the average structure stored in the eigvec.trr file. It can be changed with -ori to an arbitrary position in configurational space. With -tau, -deltaF0 and -Eflnull you control the flooding behaviour. Efl is the flooding strength, it is updated according to the rule of adaptive flooding. Tau is the time constant of adaptive flooding, high tau means slow adaption (i.e. growth). DeltaF0 is the flooding strength you want to reach after tau ps of simulation. To use constant Efl set -tau to zero. </p>
<p> -alpha is a fudge parameter to control the width of the flooding potential. A value of 2 has been found to give good results for most standard cases in flooding of proteins. Alpha basically accounts for incomplete sampling, if you sampled further the width of the ensemble would increase, this is mimicked by alpha1. For restraining alpha1 can give you smaller width in the restraining potential. </p>
<p> RESTART and FLOODING: If you want to restart a crashed flooding simulation please find the values deltaF and Efl in the output file and manually put them into the .edi file under DELTA_F0 and EFL_NULL.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> eigenvec.trr</i> <code>Input</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-eig</code><i> eigenval.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-tar</code><i> target.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-ori</code><i> origin.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> sam.edi</i> <code>Output</code><br />
&nbsp;<wbr>ED sampling input&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-mon</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for projections of x&nbsp;<wbr>(e.g. 1,2-5,9)&nbsp;<wbr>or 1-100:10 means 1 11 21 31 &#8230; 91 </p>
<p> <code>-linfix</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for fixed increment linear sampling </p>
<p> <code>-linacc</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for acceptance linear sampling </p>
<p> <code>-flood</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for flooding </p>
<p> <code>-radfix</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for fixed increment radius expansion </p>
<p> <code>-radacc</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for acceptance radius expansion </p>
<p> <code>-radcon</code><i> string</i><br />
&nbsp;<wbr>Indices of eigenvectors for acceptance radius contraction </p>
<p> <code>-outfrq</code><i> int</i><code> 100</code><br />
&nbsp;<wbr>Freqency&nbsp;<wbr>(in steps)&nbsp;<wbr>of writing output in .edo file </p>
<p> <code>-slope</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Minimal slope in acceptance radius expansion </p>
<p> <code>-maxedsteps</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Max nr of steps per cycle </p>
<p> <code>-deltaF0</code><i> real</i><code> 150 </code><br />
&nbsp;<wbr>Target destabilization energy&nbsp;<wbr>&nbsp;<wbr>&#8211; used for flooding </p>
<p> <code>-deltaF</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Start deltaF with this parameter &#8211; default 0, i.e. nonzero values only needed for restart </p>
<p> <code>-tau</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>Coupling constant for adaption of flooding strength according to deltaF0, 0&nbsp;<wbr>=&nbsp;<wbr>infinity i.e. constant flooding strength </p>
<p> <code>-eqsteps</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of steps to run without any perturbations&nbsp;<wbr> </p>
<p> <code>-Eflnull</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>This is the starting value of the flooding strength. The flooding strength is updated according to the adaptive flooding scheme. To use a constant flooding strength use -tau 0.&nbsp;<wbr> </p>
<p> <code>-T</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>T is temperature, the value is needed if you want to do flooding&nbsp;<wbr> </p>
<p> <code>-alpha</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Scale width of gaussian flooding potential with alpha2&nbsp;<wbr> </p>
<p> <code>-linstep</code><i> string</i><br />
&nbsp;<wbr>Stepsizes&nbsp;<wbr>(nm/step)&nbsp;<wbr>for fixed increment linear sampling&nbsp;<wbr>(put in quotes!&nbsp;<wbr>&quot;1.0 2.3 5.1 -3.1&quot;) </p>
<p> <code>-accdir</code><i> string</i><br />
&nbsp;<wbr>Directions for acceptance linear sampling &#8211; only sign counts!&nbsp;<wbr>(put in quotes!&nbsp;<wbr>&quot;-1&nbsp;<wbr>+1 -1.1&quot;) </p>
<p> <code>-radstep</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Stepsize&nbsp;<wbr>(nm/step)&nbsp;<wbr>for fixed increment radius expansion </p>
<p> <code>-[no]restrain</code><i>no </i><br />
&nbsp;<wbr>Use the flooding potential with inverted sign &#8211; effects as quasiharmonic restraining potential </p>
<p> <code>-[no]hessian</code><i>no </i><br />
&nbsp;<wbr>The eigenvectors and eigenvalues are from a Hessian matrix </p>
<p> <code>-[no]harmonic</code><i>no </i><br />
&nbsp;<wbr>The eigenvalues are interpreted as spring constant </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
