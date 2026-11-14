---
title: "g_dipoles_d(1)"
name: "g_dipoles_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_dipoles_d/"
description: "g_dipoles – computes the total dipole plus fluctuations"
---

<h2>NAME</h2>
<p> g_dipoles &#8211; computes the total dipole plus fluctuations </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_dipoles</code> <code>-enx</code><i> ener.edr </i> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-o</code><i> Mtot.xvg </i> <code>-eps</code><i> epsilon.xvg </i> <code>-a</code><i> aver.xvg </i> <code>-d</code><i> dipdist.xvg </i> <code>-c</code><i> dipcorr.xvg </i> <code>-g</code><i> gkr.xvg </i> <code>-adip</code><i> adip.xvg </i> <code>-dip3d</code><i> dip3d.xvg </i> <code>-cos</code><i> cosaver.xvg </i> <code>-cmap</code><i> cmap.xpm </i> <code>-q</code><i> quadrupole.xvg </i> <code>-slab</code><i> slab.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-mu</code><i> real </i> <code>-mumax</code><i> real </i> <code>-epsilonRF</code><i> real </i> <code>-skip</code><i> int </i> <code>-temp</code><i> real </i> <code>-corr</code><i> enum </i> <code>-[no]pairs</code><i></i> <code>-ncos</code><i> int </i> <code>-axis</code><i> string </i> <code>-sl</code><i> int </i> <code>-gkratom</code><i> int </i> <code>-gkratom2</code><i> int </i> <code>-rcmax</code><i> real </i> <code>-[no]phi</code><i></i> <code>-nlevels</code><i> int </i> <code>-ndegrees</code><i> int </i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_dipoles computes the total dipole plus fluctuations of a simulation system. From this you can compute e.g. the dielectric constant for low dielectric media. For molecules with a net charge, the net charge is subtracted at center of mass of the molecule. </p>
<p> The file Mtot.xvg contains the total dipole moment of a frame, the components as well as the norm of the vector. The file aver.xvg contains |Mu|2 and |Mu| 2 during the simulation. The file dipdist.xvg contains the distribution of dipole moments during the simulation The mu_max is used as the highest value in the distribution graph. </p>
<p> Furthermore the dipole autocorrelation function will be computed when option -corr is used. The output file name is given with the <code> -c</code> option. The correlation functions can be averaged over all molecules (<code> mol</code>), plotted per molecule seperately (<code> molsep</code>) or it can be computed over the total dipole moment of the simulation box (<code> total</code>). </p>
<p> Option <code> -g</code> produces a plot of the distance dependent Kirkwood G-factor, as well as the average cosine of the angle between the dipoles as a function of the distance. The plot also includes gOO and hOO according to Nymand &amp; Linse, JCP 112 (2000) pp 6386-6395. In the same plot we also include the energy per scale computed by taking the inner product of the dipoles divided by the distance to the third power. </p>
<p> EXAMPLES </p>
<p> g_dipoles -corr mol -P1 -o dip_sqr -mu 2.273 -mumax 5.0 -nofft </p>
<p> This will calculate the autocorrelation function of the molecular dipoles using a first order Legendre polynomial of the angle of the dipole vector and itself a time t later. For this calculation 1001 frames will be used. Further the dielectric constant will be calculated using an epsilonRF of infinity (default), temperature of 300 K (default) and an average dipole moment of the molecule of 2.273 (SPC). For the distribution function a maximum of 5.0 will be used.</p>
<h2>FILES</h2>
<p> <code>-enx</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-o</code><i> Mtot.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-eps</code><i> epsilon.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-a</code><i> aver.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-d</code><i> dipdist.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-c</code><i> dipcorr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-g</code><i> gkr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-adip</code><i> adip.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-dip3d</code><i> dip3d.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cos</code><i> cosaver.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cmap</code><i> cmap.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-q</code><i> quadrupole.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-slab</code><i> slab.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-mu</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>dipole of a single molecule&nbsp;<wbr>(in Debye) </p>
<p> <code>-mumax</code><i> real</i><code> 5 </code><br />
&nbsp;<wbr>max dipole in Debye&nbsp;<wbr>(for histrogram) </p>
<p> <code>-epsilonRF</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>epsilon of the reaction field used during the simulation, needed for dieclectric constant calculation. WARNING: 0.0 means infinity&nbsp;<wbr>(default) </p>
<p> <code>-skip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip steps in the output&nbsp;<wbr>(but not in the computations) </p>
<p> <code>-temp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>Average temperature of the simulation&nbsp;<wbr>(needed for dielectric constant calculation) </p>
<p> <code>-corr</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Correlation function to calculate:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>mol</code>,&nbsp;<wbr><code>&nbsp;<wbr>molsep</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>total</code> </p>
<p> <code>-[no]pairs</code><i>yes </i><br />
&nbsp;<wbr>Calculate |cos theta| between all pairs of molecules. May be slow </p>
<p> <code>-ncos</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Must be 1 or 2. Determines whether the cos is computed between all mole cules in one group, or between molecules in two different groups. This turns on the -gkr flag. </p>
<p> <code>-axis</code><i> string</i><code> Z</code><br />
&nbsp;<wbr>Take the normal on the computational box in direction X, Y or Z. </p>
<p> <code>-sl</code><i> int</i><code> 10</code><br />
&nbsp;<wbr>Divide the box in nr slices. </p>
<p> <code>-gkratom</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Use the n-th atom of a molecule&nbsp;<wbr>(starting from 1)&nbsp;<wbr>to calculate the distance between molecules rather than the center of charge&nbsp;<wbr>(when 0)&nbsp;<wbr>in the calculation of distance dependent Kirkwood factors </p>
<p> <code>-gkratom2</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Same as previous option in case ncos&nbsp;<wbr>=&nbsp;<wbr>2, i.e. dipole interaction between two groups of molecules </p>
<p> <code>-rcmax</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum distance to use in the dipole orientation distribution&nbsp;<wbr>(with ncos&nbsp;<wbr>==&nbsp;<wbr>2). If zero, a criterium based on the box length will be used. </p>
<p> <code>-[no]phi</code><i>no </i><br />
&nbsp;<wbr>Plot the&nbsp;<wbr>&#8216;torsion angle&#8217;&nbsp;<wbr>defined as the rotation of the two dipole vectors around the distance vector between the two molecules in the xpm file from the -cmap option. By default the cosine of the angle between the dipoles is plotted. </p>
<p> <code>-nlevels</code><i> int</i><code> 20</code><br />
&nbsp;<wbr>Number of colors in the cmap output </p>
<p> <code>-ndegrees</code><i> int</i><code> 90</code><br />
&nbsp;<wbr>Number of divisions on the y-axis in the camp output&nbsp;<wbr>(for 180 degrees) </p>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
