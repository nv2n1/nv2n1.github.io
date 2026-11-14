---
title: "g_trjconv(1)"
name: "g_trjconv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_trjconv/"
description: "trjconv – converts and manipulates trajectory files"
---

<h2>NAME</h2>
<p> trjconv &#8211; converts and manipulates trajectory files </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>trjconv</code> <code>-f</code><i> traj.xtc </i> <code>-o</code><i> trajout.xtc </i> <code>-s</code><i> topol.tpr </i> <code>-n</code><i> index.ndx </i> <code>-fr</code><i> frames.ndx </i> <code>-sub</code><i> cluster.ndx </i> <code>-drop</code><i> drop.xvg </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-b</code><i> time </i> <code>-e</code><i> time </i> <code>-tu</code><i> enum </i> <code>-[no]w</code><i></i> <code>-[no]xvgr</code><i></i> <code>-skip</code><i> int </i> <code>-dt</code><i> time </i> <code>-dump</code><i> time </i> <code>-t0</code><i> time </i> <code>-timestep</code><i> time </i> <code>-pbc</code><i> enum </i> <code>-ur</code><i> enum </i> <code>-[no]center</code><i></i> <code>-boxcenter</code><i> enum </i> <code>-box</code><i> vector </i> <code>-trans</code><i> vector </i> <code>-shift</code><i> vector </i> <code>-fit</code><i> enum </i> <code>-ndec</code><i> int </i> <code>-[no]vel</code><i></i> <code>-[no]force</code><i></i> <code>-trunc</code><i> time </i> <code>-exec</code><i> string </i> <code>-[no]app</code><i></i> <code>-split</code><i> time </i> <code>-[no]sep</code><i></i> <code>-nzero</code><i> int </i> <code>-[no]ter</code><i></i> <code>-dropunder</code><i> real </i> <code>-dropover</code><i> real </i></p>
<h2>DESCRIPTION</h2>
<p> trjconv can convert trajectory files in many ways: </p>
<p> <code> 1.</code> from one format to another </p>
<p> <code> 2.</code> select a subset of atoms <code> 3.</code> change the periodicity representation </p>
<p> <code> 4.</code> keep multimeric molecules together </p>
<p> <code> 5.</code> center atoms in the box </p>
<p> <code> 6.</code> fit atoms to reference structure </p>
<p> <code> 7.</code> reduce the number of frames </p>
<p> <code> 8.</code> change the timestamps of the frames (<code> -t0</code> and <code> -timestep</code>) </p>
<p> <code> 9.</code> cut the trajectory in small subtrajectories according to information in an index file. This allows subsequent analysis of the subtrajectories that could, for example be the result of a cluster analysis. Use option <code> -sub</code>. This assumes that the entries in the index file are frame numbers and dumps each group in the index file to a separate trajectory file. </p>
<p> <code> 10.</code> select frames within a certain range of a quantity given in an <code> .xvg</code> file. </p>
<p> The program <code> trjcat</code> can concatenate multiple trajectory files. </p>
<p> Currently seven formats are supported for input and output: <code> .xtc</code>, <code> .trr</code>, <code> .trj</code>, <code> .gro</code>, <code> .g96</code>, <code> .pdb</code> and <code> .g87</code>. The file formats are detected from the file extension. The precision of <code> .xtc</code> and <code> .gro</code> output is taken from the input file for <code> .xtc</code>, <code> .gro</code> and <code> .pdb</code>, and from the <code> -ndec</code> option for other input formats. The precision is always taken from <code> -ndec</code>, when this option is set. All other formats have fixed precision. <code> .trr</code> and <code> .trj</code> output can be single or double precision, depending on the precision of the trjconv binary. Note that velocities are only supported in <code> .trr</code>, <code> .trj</code>, <code> .gro</code> and <code> .g96</code> files. </p>
<p> Option <code> -app</code> can be used to append output to an existing trajectory file. No checks are performed to ensure integrity of the resulting combined trajectory file. </p>
<p> Option <code> -sep</code> can be used to write every frame to a seperate .gro, .g96 or .pdb file, default all frames all written to one file. <code> .pdb</code> files with all frames concatenated can be viewed with <code> rasmol -nmrpdb</code>. </p>
<p> It is possible to select part of your trajectory and write it out to a new trajectory file in order to save disk space, e.g. for leaving out the water from a trajectory of a protein in water. <code> ALWAYS</code> put the original trajectory on tape! We recommend to use the portable <code> .xtc</code> format for your analysis to save disk space and to have portable files. </p>
<p> There are two options for fitting the trajectory to a reference either for essential dynamics analysis or for whatever. The first option is just plain fitting to a reference structure in the structure file, the second option is a progressive fit in which the first timeframe is fitted to the reference structure in the structure file to obtain and each subsequent timeframe is fitted to the previously fitted structure. This way a continuous trajectory is generated, which might not be the case when using the regular fit method, e.g. when your protein undergoes large conformational transitions. </p>
<p> Option <code> -pbc</code> sets the type of periodic boundary condition treatment: </p>
<p> * <code> mol</code> puts the center of mass of molecules in the box. </p>
<p> * <code> res</code> puts the center of mass of residues in the box. </p>
<p> * <code> atom</code> puts all the atoms in the box. </p>
<p> * <code> nojump</code> checks if atoms jump across the box and then puts them back. This has the effect that all molecules will remain whole (provided they were whole in the initial conformation), note that this ensures a continuous trajectory but molecules may diffuse out of the box. The starting configuration for this procedure is taken from the structure file, if one is supplied, otherwise it is the first frame. </p>
<p> * <code> cluster</code> clusters all the atoms in the selected index such that they are all closest to the center of mass of the cluster which is iteratively updated. Note that this will only give meaningful results if you in fact have a cluster. Luckily that can be checked afterwards using a trajectory viewer. Note also that if your molecules are broken this will not work either. </p>
<p> * <code> whole</code> only makes broken molecules whole. </p>
<p> Option <code> -ur</code> sets the unit cell representation for options <code> mol</code>, <code> res</code> and <code> atom</code> of <code> -pbc</code>. All three options give different results for triclinc boxes and identical results for rectangular boxes. <code> rect</code> is the ordinary brick shape. <code> tric</code> is the triclinic unit cell. <code> compact</code> puts all atoms at the closest distance from the center of the box. This can be useful for visualizing e.g. truncated octahedrons. The center for options <code> tric</code> and <code> compact</code> is <code> tric</code> (see below), unless the option <code> -boxcenter</code> is set differently. </p>
<p> Option <code> -center</code> centers the system in the box. The user can select the group which is used to determine the geometrical center. Option <code> -boxcenter</code> sets the location of the center of the box for options <code> -pbc</code> and <code> -center</code>. The center options are: <code> tric</code>: half of the sum of the box vectors, <code> rect</code>: half of the box diagonal, <code> zero</code>: zero. Use option <code> -pbc mol</code> in addition to <code> -center</code> when you want all molecules in the box after the centering. </p>
<p> With <code> -dt</code> it is possible to reduce the number of frames in the output. This option relies on the accuracy of the times in your input trajectory, so if these are inaccurate use the <code> -timestep</code> option to modify the time (this can be done simultaneously). For making smooth movies the program <code> g_filter</code> can reduce the number of frames while using low-pass frequency filtering, this reduces aliasing of high frequency motions. </p>
<p> Using <code> -trunc</code> trjconv can truncate <code> .trj</code> in place, i.e. without copying the file. This is useful when a run has crashed during disk I/O (one more disk full), or when two contiguous trajectories must be concatenated without have double frames. </p>
<p> <code> trjcat</code> is more suitable for concatenating trajectory files. </p>
<p> Option <code> -dump</code> can be used to extract a frame at or near one specific time from your trajectory. </p>
<p> Option <code> -drop</code> reads an <code> .xvg</code> file with times and values. When options <code> -dropunder</code> and/or <code> -dropover</code> are set, frames with a value below and above the value of the respective options will not be written.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> traj.xtc</i> <code>Input</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-o</code><i> trajout.xtc</i> <code>Output</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-s</code><i> topol.tpr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure+mass(db): tpr tpb tpa gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-fr</code><i> frames.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-sub</code><i> cluster.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-drop</code><i> drop.xvg</i> <code>Input, Opt.</code><br />
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
<p> <code>-tu</code><i> enum</i><code> ps</code><br />
&nbsp;<wbr>Time unit:&nbsp;<wbr><code>&nbsp;<wbr>ps</code>,&nbsp;<wbr><code>&nbsp;<wbr>fs</code>,&nbsp;<wbr><code>&nbsp;<wbr>ns</code>,&nbsp;<wbr><code>&nbsp;<wbr>us</code>,&nbsp;<wbr><code>&nbsp;<wbr>ms</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>s</code> </p>
<p> <code>-[no]w</code><i>no </i><br />
&nbsp;<wbr>View output xvg, xpm, eps and pdb files </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-skip</code><i> int</i><code> 1</code><br />
&nbsp;<wbr>Only write every nr-th frame </p>
<p> <code>-dt</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Only write frame when t MOD dt&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-dump</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>Dump frame nearest specified time&nbsp;<wbr>(ps) </p>
<p> <code>-t0</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Starting time&nbsp;<wbr>(ps)&nbsp;<wbr>(default: don&#8217;t change) </p>
<p> <code>-timestep</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Change time step between input frames&nbsp;<wbr>(ps) </p>
<p> <code>-pbc</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>PBC treatment&nbsp;<wbr>(see help text for full description):&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>mol</code>,&nbsp;<wbr><code>&nbsp;<wbr>res</code>,&nbsp;<wbr><code>&nbsp;<wbr>atom</code>,&nbsp;<wbr><code>&nbsp;<wbr>nojump</code>,&nbsp;<wbr><code>&nbsp;<wbr>cluster</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>whole</code> </p>
<p> <code>-ur</code><i> enum</i><code> rect</code><br />
&nbsp;<wbr>Unit-cell representation:&nbsp;<wbr><code>&nbsp;<wbr>rect</code>,&nbsp;<wbr><code>&nbsp;<wbr>tric</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>compact</code> </p>
<p> <code>-[no]center</code><i>no </i><br />
&nbsp;<wbr>Center atoms in box </p>
<p> <code>-boxcenter</code><i> enum</i><code> tric</code><br />
&nbsp;<wbr>Center for -pbc and -center:&nbsp;<wbr><code>&nbsp;<wbr>tric</code>,&nbsp;<wbr><code>&nbsp;<wbr>rect</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>zero</code> </p>
<p> <code>-box</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Size for new cubic box&nbsp;<wbr>(default: read from input) </p>
<p> <code>-trans</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>All coordinates will be translated by trans. This can advantageously be combined with -pbc mol -ur compact. </p>
<p> <code>-shift</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>All coordinates will be shifted by framenr*shift </p>
<p> <code>-fit</code><i> enum</i><code> none</code><br />
&nbsp;<wbr>Fit molecule to ref structure in the structure file:&nbsp;<wbr><code>&nbsp;<wbr>none</code>,&nbsp;<wbr><code>&nbsp;<wbr>rot+trans</code>,&nbsp;<wbr><code>&nbsp;<wbr>rotxy+transxy</code>,&nbsp;<wbr><code>&nbsp;<wbr>translation</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>progressive</code> </p>
<p> <code>-ndec</code><i> int</i><code> 3</code><br />
&nbsp;<wbr>Precision for .xtc and .gro writing in number of decimal places </p>
<p> <code>-[no]vel</code><i>yes </i><br />
&nbsp;<wbr>Read and write velocities if possible </p>
<p> <code>-[no]force</code><i>no </i><br />
&nbsp;<wbr>Read and write forces if possible </p>
<p> <code>-trunc</code><i> time</i><code> -1 </code><br />
&nbsp;<wbr>Truncate input trj file after this time&nbsp;<wbr>(ps) </p>
<p> <code>-exec</code><i> string</i><br />
&nbsp;<wbr>Execute command for every output frame with the frame number as argument </p>
<p> <code>-[no]app</code><i>no </i><br />
&nbsp;<wbr>Append output </p>
<p> <code>-split</code><i> time</i><code> 0 </code><br />
&nbsp;<wbr>Start writing new file when t MOD split&nbsp;<wbr>=&nbsp;<wbr>first time&nbsp;<wbr>(ps) </p>
<p> <code>-[no]sep</code><i>no </i><br />
&nbsp;<wbr>Write each frame to a separate .gro, .g96 or .pdb file </p>
<p> <code>-nzero</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Prepend file number in case you use the -sep flag with this number of zeroes </p>
<p> <code>-[no]ter</code><i>no </i><br />
&nbsp;<wbr>Use&nbsp;<wbr>&#8216;TER&#8217;&nbsp;<wbr>in pdb file as end of frame in stead of default&nbsp;<wbr>&#8216;ENDMDL&#8217; </p>
<p> <code>-dropunder</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Drop all frames below this value </p>
<p> <code>-dropover</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Drop all frames above this value </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
