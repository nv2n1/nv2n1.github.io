---
title: "g_anaeig_d(1)"
name: "g_anaeig_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_anaeig_d/"
description: "g_anaeig – analyzes the eigenvectors"
---

<h2>NAME</h2>
<p> g_anaeig &#8211; analyzes the eigenvectors </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_anaeig</code> <code>-v</code><i> eigenvec.trr </i> <code>-v2</code><i> eigenvec2.trr </i> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-eig</code><i> eigenval.xvg </i> <code>-eig2</code><i> eigenval2.xvg </i> <code>-comp</code><i> eigcomp.xvg </i> <code>-rmsf</code><i> eigrmsf.xvg </i> <code>-proj</code><i> proj.xvg </i> <code>-2d</code><i> 2dproj.xvg </i> <code>-3d</code><i> 3dproj.pdb </i> <code>-filt</code><i> filtered.xtc </i> <code>-extr</code><i> extreme.pdb </i> <code>-over</code><i> overlap.xvg </i> <code>-inpr</code><i> inprod.xpm </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-first</code><i> int </i> <code>-last</code><i> int </i> <code>-skip</code><i> int </i> <code>-max</code><i> real </i> <code>-nframes</code><i> int </i> <code>-[no]split</code><i></i> <code>-[no]entropy</code><i></i> <code>-temp</code><i> real </i> <code>-nevskip</code><i> int </i></p>
<h2>DESCRIPTION</h2>
<p> <code> g_anaeig</code> analyzes eigenvectors. The eigenvectors can be of a covariance matrix (<code> g_covar</code>) or of a Normal Modes anaysis (<code> g_nmeig</code>). </p>
<p> When a trajectory is projected on eigenvectors, all structures are fitted to the structure in the eigenvector file, if present, otherwise to the structure in the structure file. When no run input file is supplied, periodicity will not be taken into account. Most analyses are performed on eigenvectors <code> -first</code> to <code> -last</code>, but when <code> -first</code> is set to -1 you will be prompted for a selection. </p>
<p> <code> -comp</code>: plot the vector components per atom of eigenvectors <code> -first</code> to <code> -last</code>. </p>
<p> <code> -rmsf</code>: plot the RMS fluctuation per atom of eigenvectors <code> -first</code> to <code> -last</code> (requires <code> -eig</code>). </p>
<p> <code> -proj</code>: calculate projections of a trajectory on eigenvectors <code> -first</code> to <code> -last</code>. The projections of a trajectory on the eigenvectors of its covariance matrix are called principal components (pc&#8217;s). It is often useful to check the cosine content the pc&#8217;s, since the pc&#8217;s of random diffusion are cosines with the number of periods equal to half the pc index. The cosine content of the pc&#8217;s can be calculated with the program <code> g_analyze</code>. </p>
<p> <code> -2d</code>: calculate a 2d projection of a trajectory on eigenvectors <code> -first</code> and <code> -last</code>. </p>
<p> <code> -3d</code>: calculate a 3d projection of a trajectory on the first three selected eigenvectors. </p>
<p> <code> -filt</code>: filter the trajectory to show only the motion along eigenvectors <code> -first</code> to <code> -last</code>. </p>
<p> <code> -extr</code>: calculate the two extreme projections along a trajectory on the average structure and interpolate <code> -nframes</code> frames between them, or set your own extremes with <code> -max</code>. The eigenvector <code> -first</code> will be written unless <code> -first</code> and <code> -last</code> have been set explicitly, in which case all eigenvectors will be written to separate files. Chain identifiers will be added when writing a <code> .pdb</code> file with two or three structures (you can use <code> rasmol -nmrpdb</code> to view such a pdb file). </p>
<p> Overlap calculations between covariance analysis: </p>
<p> NOTE: the analysis should use the same fitting structure </p>
<p> <code> -over</code>: calculate the subspace overlap of the eigenvectors in file <code> -v2</code> with eigenvectors <code> -first</code> to <code> -last</code> in file <code> -v</code>. </p>
<p> <code> -inpr</code>: calculate a matrix of inner-products between eigenvectors in files <code> -v</code> and <code> -v2</code>. All eigenvectors of both files will be used unless <code> -first</code> and <code> -last</code> have been set explicitly. </p>
<p> When <code> -v</code>, <code> -eig</code>, <code> -v2</code> and <code> -eig2</code> are given, a single number for the overlap between the covariance matrices is generated. The formulas are: </p>
<p> difference = sqrt(tr((sqrt(M1) &#8211; sqrt(M2))2)) </p>
<p> normalized overlap = 1 &#8211; difference/sqrt(tr(M1) + tr(M2)) </p>
<p> shape overlap = 1 &#8211; sqrt(tr((sqrt(M1/tr(M1)) &#8211; sqrt(M2/tr(M2)))2)) </p>
<p> where M1 and M2 are the two covariance matrices and tr is the trace of a matrix. The numbers are proportional to the overlap of the square root of the fluctuations. The normalized overlap is the most useful number, it is 1 for identical matrices and 0 when the sampled subspaces are orthogonal. </p>
<p> When the <code> -entropy</code> flag is given an entropy estimate will be computed based on the Quasiharmonic approach and based on Schlitter&#8217;s formula.</p>
<h2>FILES</h2>
<p> <code>-v</code><i> eigenvec.trr</i> <code>Input</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-v2</code><i> eigenvec2.trr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-eig</code><i> eigenval.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-eig2</code><i> eigenval2.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-comp</code><i> eigcomp.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-rmsf</code><i> eigrmsf.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-proj</code><i> proj.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-2d</code><i> 2dproj.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-3d</code><i> 3dproj.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-filt</code><i> filtered.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-extr</code><i> extreme.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-over</code><i> overlap.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-inpr</code><i> inprod.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-first</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>First eigenvector for analysis&nbsp;<wbr>(-1 is select) </p>
<p> <code>-last</code><i> int</i><code> 8</code><br />
&nbsp;<wbr>Last eigenvector for analysis&nbsp;<wbr>(-1 is till the last) </p>
<p> <code>-skip</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only analyse every nr-th frame </p>
<p> <code>-max</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum for projection of the eigenvector on the average structure, max=0 gives the extremes </p>
<p> <code>-nframes</code><i> int</i><code> 2</code><br />
&nbsp;<wbr>Number of frames for the extremes output </p>
<p> <code>-[no]split</code><i>no </i><br />
&nbsp;<wbr>Split eigenvector projections where time is zero </p>
<p> <code>-[no]entropy</code><i>no </i><br />
&nbsp;<wbr>Compute entropy according to the Quasiharmonic formula or Schlitter&#8217;s method. </p>
<p> <code>-temp</code><i> real</i><code> 298.15</code><br />
&nbsp;<wbr>Temperature for entropy calculations </p>
<p> <code>-nevskip</code><i> int</i><code> 6</code><br />
&nbsp;<wbr>Number of eigenvalues to skip when computing the entropy due to the quasi harmonic approximation. When you do a rotational and/or translational fit prior to the covariance analysis, you get 3 or 6 eigenvalues that are very close to zero, and which should not be taken into account when computing the entropy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
