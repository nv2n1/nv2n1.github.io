---
title: "g_hbond(1)"
name: "g_hbond"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_hbond/"
description: "g_hbond – computes and analyzes hydrogen bonds"
---

<h2>NAME</h2>
<p> g_hbond &#8211; computes and analyzes hydrogen bonds </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_hbond</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-num</code><i> hbnum.xvg </i> <code>-g</code><i> hbond.log </i> <code>-ac</code><i> hbac.xvg </i> <code>-dist</code><i> hbdist.xvg </i> <code>-ang</code><i> hbang.xvg </i> <code>-hx</code><i> hbhelix.xvg </i> <code>-hbn</code><i> hbond.ndx </i> <code>-hbm</code><i> hbmap.xpm </i> <code>-don</code><i> donor.xvg </i> <code>-dan</code><i> danum.xvg </i> <code>-life</code><i> hblife.xvg </i> <code>-nhbdist</code><i> nhbdist.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]xvgr</code><i></i> <code>-[no]ins</code><i></i> <code>-a</code><i> real </i> <code>-r</code><i> real </i> <code>-[no]da</code><i></i> <code>-r2</code><i> real </i> <code>-abin</code><i> real </i> <code>-rbin</code><i> real </i> <code>-[no]nitacc</code><i></i> <code>-[no]contact</code><i></i> <code>-shell</code><i> real </i> <code>-fitstart</code><i> real </i> <code>-temp</code><i> real </i> <code>-smooth</code><i> real </i> <code>-dump</code><i> int </i> <code>-max_hb</code><i> real </i> <code>-[no]merge</code><i></i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_hbond computes and analyzes hydrogen bonds. Hydrogen bonds are determined based on cutoffs for the angle Acceptor &#8211; Donor &#8211; Hydrogen (zero is extended) and the distance Hydrogen &#8211; Acceptor. OH and NH groups are regarded as donors, O is an acceptor always, N is an acceptor by default, but this can be switched using <code> -nitacc</code>. Dummy hydrogen atoms are assumed to be connected to the first preceding non-hydrogen atom. </p>
<p> You need to specify two groups for analysis, which must be either identical or non-overlapping. All hydrogen bonds between the two groups are analyzed. </p>
<p> If you set -shell, you will be asked for an additional index group which should contain exactly one atom. In this case, only hydrogen bonds between atoms within the shell distance from the one atom are considered. </p>
<p> <code> [ selected ] </p>
<p> 20 21 24 </p>
<p> 25 26 29 </p>
<p> 1 3 6 </p>
<p> </code> </p>
<p> Note that the triplets need not be on separate lines. Each atom triplet specifies a hydrogen bond to be analyzed, note also that no check is made for the types of atoms. </p>
<p> <code> -ins</code> turns on computing solvent insertion into hydrogen bonds. In this case an additional group must be selected, specifying the solvent molecules. </p>
<p> <code> Output:</code> </p>
<p> <code> -num</code>: number of hydrogen bonds as a function of time. </p>
<p> <code> -ac</code>: average over all autocorrelations of the existence functions (either 0 or 1) of all hydrogen bonds. </p>
<p> <code> -dist</code>: distance distribution of all hydrogen bonds. </p>
<p> <code> -ang</code>: angle distribution of all hydrogen bonds. </p>
<p> <code> -hx</code>: the number of n-n+i hydrogen bonds as a function of time where n and n+i stand for residue numbers and i ranges from 0 to 6. This includes the n-n+3, n-n+4 and n-n+5 hydrogen bonds associated with helices in proteins. </p>
<p> <code> -hbn</code>: all selected groups, donors, hydrogens and acceptors for selected groups, all hydrogen bonded atoms from all groups and all solvent atoms involved in insertion. </p>
<p> <code> -hbm</code>: existence matrix for all hydrogen bonds over all frames, this also contains information on solvent insertion into hydrogen bonds. Ordering is identical to that in <code> -hbn</code> index file. </p>
<p> <code> -dan</code>: write out the number of donors and acceptors analyzed for each timeframe. This is especially usefull when using <code> -shell</code>. </p>
<p> <code> -nhbdist</code>: compute the number of HBonds per hydrogen in order to compare results to Raman Spectroscopy. </p>
<p> Note: options <code> -ac</code>, <code> -life</code>, <code> -hbn</code> and <code> -hbm</code> require an amount of memory proportional to the total numbers of donors times the total number of acceptors in the selected group(s).</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-num</code><i> hbnum.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> hbond.log</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-ac</code><i> hbac.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dist</code><i> hbdist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ang</code><i> hbang.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-hx</code><i> hbhelix.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-hbn</code><i> hbond.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-hbm</code><i> hbmap.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-don</code><i> donor.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dan</code><i> danum.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-life</code><i> hblife.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-nhbdist</code><i> nhbdist.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]ins</code><i>no </i><br />
&nbsp;<wbr>Analyze solvent insertion </p>
<p> <code>-a</code><i> real</i><code> 30 </code><br />
&nbsp;<wbr>Cutoff angle&nbsp;<wbr>(degrees, Acceptor &#8211; Donor &#8211; Hydrogen) </p>
<p> <code>-r</code><i> real</i><code> 0.35 </code><br />
&nbsp;<wbr>Cutoff radius&nbsp;<wbr>(nm, X &#8211; Acceptor, see next option) </p>
<p> <code>-[no]da</code><i>yes </i><br />
&nbsp;<wbr>Use distance Donor-Acceptor&nbsp;<wbr>(if TRUE)&nbsp;<wbr>or Hydrogen-Acceptor&nbsp;<wbr>(FALSE) </p>
<p> <code>-r2</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Second cutoff radius. Mainly useful with -contact and -ac </p>
<p> <code>-abin</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Binwidth angle distribution&nbsp;<wbr>(degrees) </p>
<p> <code>-rbin</code><i> real</i><code> 0.005 </code><br />
&nbsp;<wbr>Binwidth distance distribution&nbsp;<wbr>(nm) </p>
<p> <code>-[no]nitacc</code><i>yes </i><br />
&nbsp;<wbr>Regard nitrogen atoms as acceptors </p>
<p> <code>-[no]contact</code><i>no </i><br />
&nbsp;<wbr>Do not look for hydrogen bonds, but merely for contacts within the cut-off distance </p>
<p> <code>-shell</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>when&nbsp;<wbr>&nbsp;<wbr>0, only calculate hydrogen bonds within&nbsp;<wbr>&nbsp;<wbr>nm shell around one particle </p>
<p> <code>-fitstart</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>Time&nbsp;<wbr>(ps)&nbsp;<wbr>from which to start fitting the correlation functions in order to obtain the forward and backward rate constants for HB breaking and formation </p>
<p> <code>-temp</code><i> real</i><code> 298.15</code><br />
&nbsp;<wbr>Temperature&nbsp;<wbr>(K)&nbsp;<wbr>for computing the Gibbs energy corresponding to HB breaking and reforming </p>
<p> <code>-smooth</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>If&nbsp;<wbr>=&nbsp;<wbr>0, the tail of the ACF will be smoothed by fitting it to an exponential function: y&nbsp;<wbr>=&nbsp;<wbr>A exp(-x/tau) </p>
<p> <code>-dump</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Dump the first N hydrogen bond ACFs in a single xvg file for debugging </p>
<p> <code>-max_hb</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Theoretical maximum number of hydrogen bonds used for normalizing HB autocorrelation function. Can be useful in case the program estimates it wrongly </p>
<p> <code>-[no]merge</code><i>yes </i><br />
&nbsp;<wbr>H-bonds between the same donor and acceptor, but with different hydrogen are treated as a single H-bond. Mainly important for the ACF. </p>
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
<p> &#8211; The option <code> -sel</code> that used to work on selected hbonds is out of order, and therefore not available for the time being. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
