---
title: "g_energy_d(1)"
name: "g_energy_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_energy_d/"
description: "g_energy – writes energies to xvg files and displays averages"
---

<h2>NAME</h2>
<p> g_energy &#8211; writes energies to xvg files and displays averages </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_energy</code> <code>-f</code><i> ener.edr </i> <code>-f2</code><i> ener.edr </i> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> energy.xvg </i> <code>-viol</code><i> violaver.xvg </i> <code>-pairs</code><i> pairs.xvg </i> <code>-ora</code><i> orienta.xvg </i> <code>-ort</code><i> orientt.xvg </i> <code>-oda</code><i> orideva.xvg </i> <code>-odr</code><i> oridevr.xvg </i> <code>-odt</code><i> oridevt.xvg </i> <code>-oten</code><i> oriten.xvg </i> <code>-corr</code><i> enecorr.xvg </i> <code>-vis</code><i> visco.xvg </i> <code>-ravg</code><i> runavgdf.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]fee</code><i></i> <code>-fetemp</code><i> real </i> <code>-zero</code><i> real </i> <code>-[no]sum</code><i></i> <code>-[no]dp</code><i></i> <code>-[no]mutot</code><i></i> <code>-[no]uni</code><i></i> <code>-skip</code><i> int </i> <code>-[no]aver</code><i></i> <code>-nmol</code><i> int </i> <code>-ndf</code><i> int </i> <code>-[no]fluc</code><i></i> <code>-[no]orinst</code><i></i> <code>-[no]ovec</code><i></i> <code>-acflen</code><i> int </i> <code>-[no]normalize</code><i></i> <code>-P</code><i> enum </i> <code>-fitfn</code><i> enum </i> <code>-ncskip</code><i> int </i> <code>-beginfit</code><i> real </i> <code>-endfit</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_energy extracts energy components or distance restraint data from an energy file. The user is prompted to interactively select the energy terms she wants. </p>
<p> Average and RMSD are calculated with full precision from the simulation (see printed manual). Drift is calculated by performing a LSQ fit of the data to a straight line. Total drift is drift multiplied by total time. The term fluctuation gives the RMSD around the LSQ fit. </p>
<p> When the <code> -viol</code> option is set, the time averaged violations are plotted and the running time-averaged and instantaneous sum of violations are recalculated. Additionally running time-averaged and instantaneous distances between selected pairs can be plotted with the <code> -pairs</code> option. </p>
<p> Options <code> -ora</code>, <code> -ort</code>, <code> -oda</code>, <code> -odr</code> and <code> -odt</code> are used for analyzing orientation restraint data. The first two options plot the orientation, the last three the deviations of the orientations from the experimental values. The options that end on an &#8216;a&#8217; plot the average over time as a function of restraint. The options that end on a &#8216;t&#8217; prompt the user for restraint label numbers and plot the data as a function of time. Option <code> -odr</code> plots the RMS deviation as a function of restraint. When the run used time or ensemble averaged orientation restraints, option <code> -orinst</code> can be used to analyse the instantaneous, not ensemble-averaged orientations and deviations instead of the time and ensemble averages. </p>
<p> Option <code> -oten</code> plots the eigenvalues of the molecular order tensor for each orientation restraint experiment. With option <code> -ovec</code> also the eigenvectors are plotted. </p>
<p> With <code> -fee</code> an estimate is calculated for the free-energy difference with an ideal gas state: </p>
<p> Delta A = A(N,V,T) &#8211; A_idgas(N,V,T) = kT ln e(Upot/kT) </p>
<p> Delta G = G(N,p,T) &#8211; G_idgas(N,p,T) = kT ln e(Upot/kT) </p>
<p> where k is Boltzmann&#8217;s constant, T is set by <code> -fetemp</code> andthe average is over the ensemble (or time in a trajectory). Note that this is in principle only correct when averaging over the whole (Boltzmann) ensemble and using the potential energy. This also allows for an entropy estimate using: </p>
<p> Delta S(N,V,T) = S(N,V,T) &#8211; S_idgas(N,V,T) = (Upot &#8211; Delta A)/T </p>
<p> Delta S(N,p,T) = S(N,p,T) &#8211; S_idgas(N,p,T) = (Upot + pV &#8211; Delta G)/T </p>
<p> When a second energy file is specified (<code> -f2</code>), a free energy difference is calculated dF = -kT ln e -(EB-EA)/kT A , where EA and EB are the energies from the first and second energy files, and the average is over the ensemble A. <code> NOTE</code> that the energies must both be calculated from the same trajectory.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> ener.edr</i> <code>Input</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-f2</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> energy.xvg</i> <code>Output</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-viol</code><i> violaver.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-pairs</code><i> pairs.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ora</code><i> orienta.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ort</code><i> orientt.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oda</code><i> orideva.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-odr</code><i> oridevr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-odt</code><i> oridevt.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-oten</code><i> oriten.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-corr</code><i> enecorr.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-vis</code><i> visco.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ravg</code><i> runavgdf.xvg</i> <code>Output, Opt.</code><br />
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
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]fee</code><i>no </i><br />
&nbsp;<wbr>Do a free energy estimate </p>
<p> <code>-fetemp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>Reference temperature for free energy calculation </p>
<p> <code>-zero</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Subtract a zero-point energy </p>
<p> <code>-[no]sum</code><i>no </i><br />
&nbsp;<wbr>Sum the energy terms selected rather than display them all </p>
<p> <code>-[no]dp</code><i>no </i><br />
&nbsp;<wbr>Print energies in high precision </p>
<p> <code>-[no]mutot</code><i>no </i><br />
&nbsp;<wbr>Compute the total dipole moment from the components </p>
<p> <code>-[no]uni</code><i>yes </i><br />
&nbsp;<wbr>Skip non-uniformly spaced frames </p>
<p> <code>-skip</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Skip number of frames between data points </p>
<p> <code>-[no]aver</code><i>no </i><br />
&nbsp;<wbr>Print also the X1,t and sigma1,t, only if only 1 energy is requested </p>
<p> <code>-nmol</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Number of molecules in your sample: the energies are divided by this number </p>
<p> <code>-ndf</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Number of degrees of freedom per molecule. Necessary for calculating the heat capacity </p>
<p> <code>-[no]fluc</code><i>no </i><br />
&nbsp;<wbr>Calculate autocorrelation of energy fluctuations rather than energy itself </p>
<p> <code>-[no]orinst</code><i>no </i><br />
&nbsp;<wbr>Analyse instantaneous orientation data </p>
<p> <code>-[no]ovec</code><i>no </i><br />
&nbsp;<wbr>Also plot the eigenvectors with -oten </p>
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
