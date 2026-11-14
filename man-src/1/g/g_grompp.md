---
title: "g_grompp(1)"
name: "g_grompp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_grompp/"
description: "grompp – makes a run input file"
---

<h2>NAME</h2>
<p> grompp &#8211; makes a run input file </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>grompp</code> <code>-f</code><i> grompp.mdp </i> <code>-po</code><i> mdout.mdp </i> <code>-c</code><i> conf.gro </i> <code>-r</code><i> conf.gro </i> <code>-rb</code><i> conf.gro </i> <code>-n</code><i> index.ndx </i> <code>-p</code><i> topol.top </i> <code>-pp</code><i> processed.top </i> <code>-o</code><i> topol.tpr </i> <code>-t</code><i> traj.trr </i> <code>-e</code><i> ener.edr </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-[no]v</code><i></i> <code>-time</code><i> real </i> <code>-[no]rmvsbds</code><i></i> <code>-maxwarn</code><i> int </i> <code>-[no]zero</code><i></i> <code>-[no]renum</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> The gromacs preprocessor reads a molecular topology file, checks the validity of the file, expands the topology from a molecular description to an atomic description. The topology file contains information about molecule types and the number of molecules, the preprocessor copies each molecule as needed. There is no limitation on the number of molecule types. Bonds and bond-angles can be converted into constraints, separately for hydrogens and heavy atoms. Then a coordinate file is read and velocities can be generated from a Maxwellian distribution if requested. grompp also reads parameters for the mdrun (eg. number of MD steps, time step, cut-off), and others such as NEMD parameters, which are corrected so that the net acceleration is zero. Eventually a binary file is produced that can serve as the sole input file for the MD program. </p>
<p> grompp uses the atom names from the topology file. The atom names in the coordinate file (option <code> -c</code>) are only read to generate warnings when they do not match the atom names in the topology. Note that the atom names are irrelevant for the simulation as only the atom types are used for generating interaction parameters. </p>
<p> grompp calls a preprocessor to resolve includes, macros etcetera. By default we use the cpp in your path. To specify a different macro-preprocessor (e.g. m4) or alternative location you can put a line in your parameter file specifying the path to that program. Specifying <code> -pp</code> will get the pre-processed topology file written out. </p>
<p> If your system does not have a c-preprocessor, you can still use grompp, but you do not have access to the features from the cpp. Command line options to the c-preprocessor can be given in the <code> .mdp</code> file. See your local manual (man cpp). </p>
<p> When using position restraints a file with restraint coordinates can be supplied with <code> -r</code>, otherwise restraining will be done with respect to the conformation from the <code> -c</code> option. For free energy calculation the the coordinates for the B topology can be supplied with <code> -rb</code>, otherwise they will be equal to those of the A topology. </p>
<p> Starting coordinates can be read from trajectory with <code> -t</code>. The last frame with coordinates and velocities will be read, unless the <code> -time</code> option is used. Note that these velocities will not be used when <code> gen_vel = yes</code> in your <code> .mdp</code> file. An energy file can be supplied with <code> -e</code> to have exact restarts when using pressure and/or Nose-Hoover temperature coupling. For an exact restart do not forget to turn off velocity generation and turn on unconstrained starting when constraints are present in the system. If you want to continue a crashed run, it is easier to use <code> tpbconv</code>. </p>
<p> Using the <code> -morse</code> option grompp can convert the harmonic bonds in your topology to morse potentials. This makes it possible to break bonds. For this option to work you need an extra file in your $GMXLIB with dissociation energy. Use the -debug option to get more information on the workings of this option (look for MORSE in the grompp.log file using less or something like that). </p>
<p> By default all bonded interactions which have constant energy due to virtual site constructions will be removed. If this constant energy is not zero, this will result in a shift in the total energy. All bonded interactions can be kept by turning off <code> -rmvsbds</code>. Additionally, all constraints for distances which will be constant anyway because of virtual site constructions will be removed. If any constraints remain which involve virtual sites, a fatal error will result. </p>
<p> To verify your run input file, please make notice of all warnings on the screen, and correct where necessary. Do also look at the contents of the <code> mdout.mdp</code> file, this contains comment lines, as well as the input that <code> grompp</code> has read. If in doubt you can start grompp with the <code> -debug</code> option which will give you more information in a file called grompp.log (along with real debug info). Finally, you can see the contents of the run input file with the <code> gmxdump</code> program.</p>
<h2>FILES</h2>
<p> <code>-f</code><i> grompp.mdp</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>grompp input file with MD parameters&nbsp;<wbr> </p>
<p> <code>-po</code><i> mdout.mdp</i> <code>Output</code><br />
&nbsp;<wbr>grompp input file with MD parameters&nbsp;<wbr> </p>
<p> <code>-c</code><i> conf.gro</i> <code>Input</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-r</code><i> conf.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-rb</code><i> conf.gro</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-n</code><i> index.ndx</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<p> <code>-p</code><i> topol.top</i> <code>Input</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<p> <code>-pp</code><i> processed.top</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Topology file&nbsp;<wbr> </p>
<p> <code>-o</code><i> topol.tpr</i> <code>Output</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-t</code><i> traj.trr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-e</code><i> ener.edr</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-[no]v</code><i>yes </i><br />
&nbsp;<wbr>Be loud and noisy </p>
<p> <code>-time</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Take frame at or first after this time. </p>
<p> <code>-[no]rmvsbds</code><i>yes </i><br />
&nbsp;<wbr>Remove constant bonded interactions with virtual sites </p>
<p> <code>-maxwarn</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Number of allowed warnings during input processing </p>
<p> <code>-[no]zero</code><i>no </i><br />
&nbsp;<wbr>Set parameters for bonded interactions without defaults to zero instead of generating an error </p>
<p> <code>-[no]renum</code><i>yes </i><br />
&nbsp;<wbr>Renumber atomtypes and minimize number of atomtypes </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
