---
title: "g_angle(1)"
name: "g_angle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_angle/"
description: "g_angle – calculates distributions and correlations for angles and dihedrals"
---

<h2>NAME</h2>
<p> g_angle &#8211; calculates distributions and correlations for angles and dihedrals </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_angle</code> <code>-f</code><i> traj.xtc </i> <code>-n</code><i> angle.ndx </i> <code>-od</code><i> angdist.xvg </i> <code>-ov</code><i> angaver.xvg </i> <code>-of</code><i> dihfrac.xvg </i> <code>-ot</code><i> dihtrans.xvg </i> <code>-oh</code><i> trhisto.xvg </i> <code>-oc</code><i> dihcorr.xvg </i> <code>-or</code><i> traj.trr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-type</code><i> enum </i> <code>-[no]all</code><i></i> <code>-binwidth</code><i> real </i> <code>-[no]periodic</code><i></i> <code>-[no]chandler</code><i></i> <code>-[no]avercorr</code><i></i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_angle computes the angle distribution for a number of angles or dihedrals. This way you can check whether your simulation is correct. With option -ov you can plot the average angle of a group of angles as a function of time. With the -all option the first graph is the average, the rest are the individual angles. </p>
<p> With the -of option g_angle also calculates the fraction of trans dihedrals (only for dihedrals) as function of time, but this is probably only fun for a selected few. </p>
<p> With option -oc a dihedral correlation function is calculated. </p>
<p> It should be noted that the indexfile should contain atom-triples for angles or atom-quadruplets for dihedrals. If this is not the case, the program will crash. </p>
<p> With option <code> -or</code> a trajectory file is dumped containing cos andsin of selected dihedral angles which subsequently can be used as input for a PCA analysis using <code> g_covar</code>.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-n</code><i> angle.ndx</i> <code>Input</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-od</code><i> angdist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ov</code><i> angaver.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-of</code><i> dihfrac.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ot</code><i> dihtrans.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oh</code><i> trhisto.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oc</code><i> dihcorr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-or</code><i> traj.trr</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory in portable xdr format&nbsp;<wbr> </p>
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
<p> <code>-type</code><i> enum</i><code> angle</code><br />
&nbsp;<wbr>Type of angle to analyse:&nbsp;<wbr><code>&nbsp;<wbr>angle</code>,&nbsp;<wbr><code>&nbsp;<wbr>dihedral</code>,&nbsp;<wbr><code>&nbsp;<wbr>improper</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>ryckaert-bellemans</code> </p>
<p> <code>-[no]all</code><i>no </i><br />
&nbsp;<wbr>Plot all angles separately in the averages file, in the order of appearance in the index file. </p>
<p> <code>-binwidth</code><i> real</i><code> 1 </code><br />
&nbsp;<wbr>binwidth&nbsp;<wbr>(degrees)&nbsp;<wbr>for calculating the distribution </p>
<p> <code>-[no]periodic</code><i>yes </i><br />
&nbsp;<wbr>Print dihedral angles modulo 360 degrees </p>
<p> <code>-[no]chandler</code><i>no </i><br />
&nbsp;<wbr>Use Chandler correlation function&nbsp;<wbr>(N[trans]&nbsp;<wbr>=&nbsp;<wbr>1, N[gauche]&nbsp;<wbr>=&nbsp;<wbr>0)&nbsp;<wbr>rather than cosine correlation function. Trans is defined as phi&nbsp;<wbr>&nbsp;<wbr>-60 || phi&nbsp;<wbr>&nbsp;<wbr>60. </p>
<p> <code>-[no]avercorr</code><i>no </i><br />
&nbsp;<wbr>Average the correlation functions for the individual angles/dihedrals </p>
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
<p> &#8211; Counting transitions only works for dihedrals with multiplicity 3 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
