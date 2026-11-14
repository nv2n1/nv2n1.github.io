---
title: "g_chi_d(1)"
name: "g_chi_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_chi_d/"
description: "g_chi – calculates everything you want to know about chi and other dihedrals"
---

<h2>NAME</h2>
<p> g_chi &#8211; calculates everything you want to know about chi and other dihedrals </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_chi</code> <code>-s</code><i> conf.gro </i> <code>-f</code><i> traj.xtc </i> <code>-o</code><i> order.xvg </i> <code>-p</code><i> order.pdb </i> <code>-ss</code><i> ssdump.dat </i> <code>-jc</code><i> Jcoupling.xvg </i> <code>-corr</code><i> dihcorr.xvg </i> <code>-g</code><i> chi.log </i> <code>-ot</code><i> dihtrans.xvg </i> <code>-oh</code><i> trhisto.xvg </i> <code>-rt</code><i> restrans.xvg </i> <code>-cp</code><i> chiprodhisto.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-r0</code><i> int </i> <code>-[no]phi</code><i></i> <code>-[no]psi</code><i></i> <code>-[no]omega</code><i></i> <code>-[no]rama</code><i></i> <code>-[no]viol</code><i></i> <code>-[no]periodic</code><i></i> <code>-[no]all</code><i></i> <code>-[no]rad</code><i></i> <code>-[no]shift</code><i></i> <code>-binwidth</code><i> int </i> <code>-core_rotamer</code><i> real </i> <code>-maxchi</code><i> enum </i> <code>-[no]normhisto</code><i></i> <code>-[no]ramomega</code><i></i> <code>-bfact</code><i> real </i> <code>-[no]chi_prod</code><i></i> <code>-[no]HChi</code><i></i> <code>-bmax</code><i> real </i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_chi computes phi, psi, omega and chi dihedrals for all your amino acid backbone and sidechains. It can compute dihedral angle as a function of time, and as histogram distributions. The distributions (histo-(dihedral)(RESIDUE).xvg) are cumulative over all residues of each type. </p>
<p> If option <code> -corr</code> is given, the program will calculate dihedral autocorrelation functions. The function used is C(t) = cos(chi(tau)) cos(chi(tau+t)) . The use of cosines rather than angles themselves, resolves the problem of periodicity. (Van der Spoel &amp; Berendsen (1997), <code> Biophys. J. 72</code>, 2032-2041). Separate files for each dihedral of each residue (corr(dihedral)(RESIDUE)(nresnr).xvg) are output, as well as a file containing the information for all residues (argument of <code> -corr</code>). </p>
<p> With option <code> -all</code>, the angles themselves as a function of time for each residue are printed to separate files (dihedral)(RESIDUE)(nresnr).xvg. These can be in radians or degrees. </p>
<p> A log file (argument <code> -g</code>) is also written. This contains </p>
<p> (a) information about the number of residues of each type. </p>
<p> (b) The NMR 3J coupling constants from the Karplus equation. </p>
<p> (c) a table for each residue of the number of transitions between rotamers per nanosecond, and the order parameter S2 of each dihedral. </p>
<p> (d) a table for each residue of the rotamer occupancy. </p>
<p> All rotamers are taken as 3-fold, except for omegas and chi-dihedrals to planar groups (i.e. chi2 of aromatics asp and asn, chi3 of glu and gln, and chi4 of arg), which are 2-fold. &quot;rotamer 0&quot; means that the dihedral was not in the core region of each rotamer. The width of the core region can be set with <code> -core_rotamer</code> </p>
<p> The S2 order parameters are also output to an xvg file (argument <code> -o</code> ) and optionally as a pdb file with the S2 values as B-factor (argument <code> -p</code>). The total number of rotamer transitions per timestep (argument <code> -ot</code>), the number of transitions per rotamer (argument <code> -rt</code>), and the 3J couplings (argument <code> -jc</code>), can also be written to .xvg files. </p>
<p> If <code> -chi_prod</code> is set (and maxchi 0), cumulative rotamers, e.g. 1+9(chi1-1)+3(chi2-1)+(chi3-1) (if the residue has three 3-fold dihedrals and maxchi = 3) are calculated. As before, if any dihedral is not in the core region, the rotamer is taken to be 0. The occupancies of these cumulative rotamers (starting with rotamer 0) are written to the file that is the argument of <code> -cp</code>, and if the <code> -all</code> flag is given, the rotamers as functions of time are written to chiproduct(RESIDUE)(nresnr).xvg and their occupancies to histo-chiproduct(RESIDUE)(nresnr).xvg. </p>
<p> The option <code> -r</code> generates a contour plot of the average omega angle as a function of the phi and psi angles, that is, in a Ramachandran plot the average omega angle is plotted using color coding.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-o</code><i> order.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-p</code><i> order.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Protein data bank file&nbsp;<wbr> </p>
<p> <code>-ss</code><i> ssdump.dat</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Generic data file&nbsp;<wbr> </p>
<p> <code>-jc</code><i> Jcoupling.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-corr</code><i> dihcorr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> chi.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> dihtrans.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oh</code><i> trhisto.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-rt</code><i> restrans.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cp</code><i> chiprodhisto.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-b</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>First frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-e</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Last frame&nbsp;<wbr>(ps)&nbsp;<wbr>to read from trajectory </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only use frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-r0</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>starting residue </p>
<p> <code>-[no]phi</code><i>no </i><br />
&nbsp;<wbr>Output for Phi dihedral angles </p>
<p> <code>-[no]psi</code><i>no </i><br />
&nbsp;<wbr>Output for Psi dihedral angles </p>
<p> <code>-[no]omega</code><i>no </i><br />
&nbsp;<wbr>Output for Omega dihedrals&nbsp;<wbr>(peptide bonds) </p>
<p> <code>-[no]rama</code><i>no </i><br />
&nbsp;<wbr>Generate Phi/Psi and Chi1/Chi2 ramachandran plots </p>
<p> <code>-[no]viol</code><i>no </i><br />
&nbsp;<wbr>Write a file that gives 0 or 1 for violated Ramachandran angles </p>
<p> <code>-[no]periodic</code><i>yes </i><br />
&nbsp;<wbr>Print dihedral angles modulo 360 degrees </p>
<p> <code>-[no]all</code><i>no </i><br />
&nbsp;<wbr>Output separate files for every dihedral. </p>
<p> <code>-[no]rad</code><i>no </i><br />
&nbsp;<wbr>in angle vs time files, use radians rather than degrees. </p>
<p> <code>-[no]shift</code><i>no </i><br />
&nbsp;<wbr>Compute chemical shifts from Phi/Psi angles </p>
<p> <code>-binwidth</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>bin width for histograms&nbsp;<wbr>(degrees) </p>
<p> <code>-core_rotamer</code><i> real</i><code> 0.5 </code><br />
&nbsp;<wbr>only the central -core_rotamer*(360/multiplicity)&nbsp;<wbr>belongs to each rotamer&nbsp;<wbr>(the rest is assigned to rotamer 0) </p>
<p> <code>-maxchi</code><i> enum</i><code> 0</code><br />
&nbsp;<wbr>calculate first ndih Chi dihedrals:&nbsp;<wbr><code>&nbsp;<wbr>0</code>,&nbsp;<wbr><code>&nbsp;<wbr>1</code>,&nbsp;<wbr><code>&nbsp;<wbr>2</code>,&nbsp;<wbr><code>&nbsp;<wbr>3</code>,&nbsp;<wbr><code>&nbsp;<wbr>4</code>,&nbsp;<wbr><code>&nbsp;<wbr>5</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>6</code> </p>
<p> <code>-[no]normhisto</code><i>yes </i><br />
&nbsp;<wbr>Normalize histograms </p>
<p> <code>-[no]ramomega</code><i>no </i><br />
&nbsp;<wbr>compute average omega as a function of phi/psi and plot it in an xpm plot </p>
<p> <code>-bfact</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>B-factor value for pdb file for atoms with no calculated dihedral order parameter </p>
<p> <code>-[no]chi_prod</code><i>no </i><br />
&nbsp;<wbr>compute a single cumulative rotamer for each residue </p>
<p> <code>-[no]HChi</code><i>no </i><br />
&nbsp;<wbr>Include dihedrals to sidechain hydrogens </p>
<p> <code>-bmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum B-factor on any of the atoms that make up a dihedral, for the dihedral angle to be considere in the statistics. Applies to database work where a number of X-Ray structures is analyzed. -bmax&nbsp;<wbr>=&nbsp;<wbr>0 means no limit. </p>
<p> <code>-acflen</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Length of the ACF, default is half the number of frames </p>
<p> <code>-[no]normalize</code><i>yes </i><br />
&nbsp;<wbr>Normalize ACF </p>
<p> <code>-P</code><i> enum</i><code> 0</code><br />
&nbsp;<wbr>Order of Legendre polynomial for ACF&nbsp;<wbr>(0 indicates none):&nbsp;<wbr><code>&nbsp;<wbr>0</code>,&nbsp;<wbr><code>&nbsp;<wbr>1</code>,&nbsp;<wbr><code>&nbsp;<wbr>2</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>3</code> </p>
<p> <code>-fitfn</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Fit function:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>aexp</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp_exp</code>,&nbsp;<wbr><code>&nbsp;<wbr>vac</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp5</code>,&nbsp;<wbr><code>&nbsp;<wbr>exp7</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>exp9</code> </p>
<p> <code>-ncskip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip N points in the output file of correlation functions </p>
<p> <code>-beginfit</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Time where to begin the exponential fit of the correlation function </p>
<p> <code>-endfit</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Time where to end the exponential fit of the correlation function, -1 is till the end </p>
<h2>KNOWN PROBLEMS</h2>
<p> &#8211; Produces MANY output files (up to about 4 times the number of residues in the protein, twice that if autocorrelation functions are calculated). Typically several hundred files are output. </p>
<p> &#8211; Phi and psi dihedrals are calculated in a non-standard way, using H-N-CA-C for phi instead of C(-)-N-CA-C, and N-CA-C-O for psi instead of N-CA-C-N(+). This causes (usually small) discrepancies with the output of other tools like g_rama. </p>
<p> &#8211; -r0 option does not work properly </p>
<p> &#8211; Rotamers with multiplicity 2 are printed in chi.log as if they had multiplicity 3, with the 3rd (g(+)) always having probability 0 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
