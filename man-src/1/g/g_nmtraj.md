---
title: "g_nmtraj(1)"
name: "g_nmtraj"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_nmtraj/"
description: "g_nmtraj – generate oscillating trajectory of an eigenmode"
---

<h2>NAME</h2>
<p> g_nmtraj &#8211; generate oscillating trajectory of an eigenmode </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_nmtraj</code> <code>-s</code><i> topol.tpr </i> <code>-v</code><i> eigenvec.trr </i> <code>-o</code><i> nmtraj.xtc </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-eignr</code><i> string </i> <code>-phases</code><i> string </i> <code>-temp</code><i> real </i> <code>-amplitude</code><i> real </i> <code>-nframes</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> <code> g_nmtraj</code> generates an virtual trajectory from an eigenvector, corresponding to a harmonic cartesian oscillation around the average structure. The eigenvectors should normally be mass-weighted, but you can use non-weighted eigenvectors to generate orthogonal motions. The output frames are written as a trajectory file covering an entire period, and the first frame is the average structure. If you write the trajectory in (or convert to) PDB format you can view it directly in PyMol and also render a photorealistic movie. Motion amplitudes are calculated from the eigenvalues and a preset temperature, assuming equipartition of the energy over all modes. To make the motion clearly visible in PyMol you might want to amplify it by setting an unrealistic high temperature. However, be aware that both the linear cartesian displacements and mass weighting will lead to serious structure deformation for high amplitudes &#8211; this is is simply a limitation of the cartesian normal mode model. By default the selected eigenvector is set to 7, since the first six normal modes are the translational and rotational degrees of freedom.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-v</code><i> eigenvec.trr</i> <code>Input</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-o</code><i> nmtraj.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-eignr</code><i> string</i><code> 7</code><br />
&nbsp;<wbr>String of eigenvectors to use&nbsp;<wbr>(first is 1) </p>
<p> <code>-phases</code><i> string</i><code> 0.0</code><br />
&nbsp;<wbr>String of phases&nbsp;<wbr>(default is 0.0) </p>
<p> <code>-temp</code><i> real</i><code> 300 </code><br />
&nbsp;<wbr>Temperature in Kelvin </p>
<p> <code>-amplitude</code><i> real</i><code> 0.25 </code><br />
&nbsp;<wbr>Amplitude for modes with eigenvalue=0 </p>
<p> <code>-nframes</code><i> int</i><code> 30</code><br />
&nbsp;<wbr>Number of frames to generate </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
