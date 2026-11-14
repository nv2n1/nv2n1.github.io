---
title: "g_cluster(1)"
name: "g_cluster"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_cluster/"
description: "g_cluster – clusters structures"
---

<h2>NAME</h2>
<p> g_cluster &#8211; clusters structures </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>g_cluster</code> <code>-f</code><i> traj.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-dm</code><i> rmsd.xpm </i> <code>-o</code><i> rmsd-clust.xpm </i> <code>-g</code><i> cluster.log </i> <code>-dist</code><i> rmsd-dist.xvg </i> <code>-ev</code><i> rmsd-eig.xvg </i> <code>-sz</code><i> clust-size.xvg </i> <code>-tr</code><i> clust-trans.xpm </i> <code>-ntr</code><i> clust-trans.xvg </i> <code>-clid</code><i> clust-id.xvg </i> <code>-cl</code><i> clusters.pdb </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-dt</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-[no]dista</code><i></i> <code>-nlevels</code><i> int </i> <code>-cutoff</code><i> real </i> <code>-[no]fit</code><i></i> <code>-max</code><i> real </i> <code>-skip</code><i> int </i> <code>-[no]av</code><i></i> <code>-wcl</code><i> int </i> <code>-nst</code><i> int </i> <code>-rmsmin</code><i> real </i> <code>-method</code><i> enum </i> <code>-minstruct</code><i> int </i> <code>-[no]binary</code><i></i> <code>-M</code><i> int </i> <code>-P</code><i> int </i> <code>-seed</code><i> int </i> <code>-niter</code><i> int </i> <code>-kT</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> g_cluster can cluster structures with several different methods. Distances between structures can be determined from a trajectory or read from an XPM matrix file with the <code> -dm</code> option. RMS deviation after fitting or RMS deviation of atom-pair distances can be used to define the distance between structures. </p>
<p> single linkage: add a structure to a cluster when its distance to any element of the cluster is less than <code> cutoff</code>. </p>
<p> Jarvis Patrick: add a structure to a cluster when this structure and a structure in the cluster have each other as neighbors and they have a least <code> P</code> neighbors in common. The neighbors of a structure are the M closest structures or all structures within <code> cutoff</code>. </p>
<p> Monte Carlo: reorder the RMSD matrix using Monte Carlo. </p>
<p> diagonalization: diagonalize the RMSD matrix. </p>
<p> gromos: use algorithm as described in Daura <i> et al.</i> (<i> Angew. Chem. Int. Ed.</i> <code> 1999</code>, <i> 38</i>, pp 236-240). Count number of neighbors using cut-off, take structure with largest number of neighbors with all its neighbors as cluster and eleminate it from the pool of clusters. Repeat for remaining structures in pool. </p>
<p> When the clustering algorithm assigns each structure to exactly one cluster (single linkage, Jarvis Patrick and gromos) and a trajectory file is supplied, the structure with the smallest average distance to the others or the average structure or all structures for each cluster will be written to a trajectory file. When writing all structures, separate numbered files are made for each cluster. </p>
<p> Two output files are always written: </p>
<p> <code> -o</code> writes the RMSD values in the upper left half of the matrix and a graphical depiction of the clusters in the lower right half When <code> -minstruct</code> = 1 the graphical depiction is black when two structures are in the same cluster. When <code> -minstruct</code> 1 different colors will be used for each cluster. </p>
<p> <code> -g</code> writes information on the options used and a detailed list of all clusters and their members. </p>
<p> Additionally, a number of optional output files can be written: </p>
<p> <code> -dist</code> writes the RMSD distribution. </p>
<p> <code> -ev</code> writes the eigenvectors of the RMSD matrix diagonalization. </p>
<p> <code> -sz</code> writes the cluster sizes. </p>
<p> <code> -tr</code> writes a matrix of the number transitions between cluster pairs. </p>
<p> <code> -ntr</code> writes the total number of transitions to or from each cluster. </p>
<p> <code> -clid</code> writes the cluster number as a function of time. </p>
<p> <code> -cl</code> writes average (with option <code> -av</code>) or central structure of each cluster or writes numbered files with cluster members for a selected set of clusters (with option <code> -wcl</code>, depends on <code> -nst</code> and <code> -rmsmin</code>). </p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-dm</code><i> rmsd.xpm</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-o</code><i> rmsd-clust.xpm</i> <code>Output</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-g</code><i> cluster.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-dist</code><i> rmsd-dist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ev</code><i> rmsd-eig.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-sz</code><i> clust-size.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-tr</code><i> clust-trans.xpm</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>X PixMap compatible matrix file&nbsp;<wbr> </p>
<p> <code>-ntr</code><i> clust-trans.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-clid</code><i> clust-id.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-cl</code><i> clusters.pdb</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
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
<p> <code>-[no]dista</code><i>no </i><br />
&nbsp;<wbr>Use RMSD of distances instead of RMS deviation </p>
<p> <code>-nlevels</code><i> int</i><code> 40</code><br />
&nbsp;<wbr>Discretize RMSD matrix in&nbsp;<wbr>&nbsp;<wbr>levels </p>
<p> <code>-cutoff</code><i> real</i><code> 0.1 </code><br />
&nbsp;<wbr>RMSD cut-off&nbsp;<wbr>(nm)&nbsp;<wbr>for two structures to be neighbor </p>
<p> <code>-[no]fit</code><i>yes </i><br />
&nbsp;<wbr>Use least squares fitting before RMSD calculation </p>
<p> <code>-max</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Maximum level in RMSD matrix </p>
<p> <code>-skip</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only analyze every nr-th frame </p>
<p> <code>-[no]av</code><i>no </i><br />
&nbsp;<wbr>Write average iso middle structure for each cluster </p>
<p> <code>-wcl</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Write all structures for first&nbsp;<wbr>&nbsp;<wbr>clusters to numbered files </p>
<p> <code>-nst</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only write all structures if more than&nbsp;<wbr>&nbsp;<wbr>per cluster </p>
<p> <code>-rmsmin</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>minimum rms difference with rest of cluster for writing structures </p>
<p> <code>-method</code><i> enum</i><code> linkage</code><br />
&nbsp;<wbr>Method for cluster determination:&nbsp;<wbr><code>&nbsp;<wbr>linkage</code>,&nbsp;<wbr><code>&nbsp;<wbr>jarvis-patrick</code>,&nbsp;<wbr><code>&nbsp;<wbr>monte-carlo</code>,&nbsp;<wbr><code>&nbsp;<wbr>diagonalization</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>gromos</code> </p>
<p> <code>-minstruct</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Minimum number of structures in cluster for coloring in the xpm file </p>
<p> <code>-[no]binary</code><i>no </i><br />
&nbsp;<wbr>Treat the RMSD matrix as consisting of 0 and 1, where the cut-off is given by -cutoff </p>
<p> <code>-M</code><i> int</i><code> 10</code><br />
&nbsp;<wbr>Number of nearest neighbors considered for Jarvis-Patrick algorithm, 0 is use cutoff </p>
<p> <code>-P</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Number of identical nearest neighbors required to form a cluster </p>
<p> <code>-seed</code><i> int</i><code> 1993</code><br />
&nbsp;<wbr>Random number seed for Monte Carlo clustering algorithm </p>
<p> <code>-niter</code><i> int</i><code> 10000</code><br />
&nbsp;<wbr>Number of iterations for MC </p>
<p> <code>-kT</code><i> real</i><code> 0.001 </code><br />
&nbsp;<wbr>Boltzmann weighting factor for Monte Carlo optimization&nbsp;<wbr>(zero turns off uphill steps) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
