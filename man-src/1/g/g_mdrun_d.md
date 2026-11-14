---
title: "g_mdrun_d(1)"
name: "g_mdrun_d"
section: "1"
letter: "g"
url: "/docs/linux/man/1-g_mdrun_d/"
description: "mdrun – performs a simulation, do a normal mode analysis or an energy minimization"
---

<h2>NAME</h2>
<p> mdrun &#8211; performs a simulation, do a normal mode analysis or an energy minimization </p>
<p> <code>VERSION 4.0.1</code></p>
<h2>SYNOPSIS</h2>
<p> <code>mdrun</code> <code>-s</code><i> topol.tpr </i> <code>-o</code><i> traj.trr </i> <code>-x</code><i> traj.xtc </i> <code>-cpi</code><i> state.cpt </i> <code>-cpo</code><i> state.cpt </i> <code>-c</code><i> confout.gro </i> <code>-e</code><i> ener.edr </i> <code>-g</code><i> md.log </i> <code>-dgdl</code><i> dgdl.xvg </i> <code>-field</code><i> field.xvg </i> <code>-table</code><i> table.xvg </i> <code>-tablep</code><i> tablep.xvg </i> <code>-tableb</code><i> table.xvg </i> <code>-rerun</code><i> rerun.xtc </i> <code>-tpi</code><i> tpi.xvg </i> <code>-tpid</code><i> tpidist.xvg </i> <code>-ei</code><i> sam.edi </i> <code>-eo</code><i> sam.edo </i> <code>-j</code><i> wham.gct </i> <code>-jo</code><i> bam.gct </i> <code>-ffout</code><i> gct.xvg </i> <code>-devout</code><i> deviatie.xvg </i> <code>-runav</code><i> runaver.xvg </i> <code>-px</code><i> pullx.xvg </i> <code>-pf</code><i> pullf.xvg </i> <code>-mtx</code><i> nm.mtx </i> <code>-dn</code><i> dipole.ndx </i> <code>-[no]h</code><i></i> <code>-nice</code><i> int </i> <code>-deffnm</code><i> string </i> <code>-[no]xvgr</code><i></i> <code>-[no]pd</code><i></i> <code>-dd</code><i> vector </i> <code>-npme</code><i> int </i> <code>-ddorder</code><i> enum </i> <code>-[no]ddcheck</code><i></i> <code>-rdd</code><i> real </i> <code>-rcon</code><i> real </i> <code>-dlb</code><i> enum </i> <code>-dds</code><i> real </i> <code>-[no]sum</code><i></i> <code>-[no]v</code><i></i> <code>-[no]compact</code><i></i> <code>-[no]seppot</code><i></i> <code>-pforce</code><i> real </i> <code>-[no]reprod</code><i></i> <code>-cpt</code><i> real </i> <code>-[no]append</code><i></i> <code>-maxh</code><i> real </i> <code>-multi</code><i> int </i> <code>-replex</code><i> int </i> <code>-reseed</code><i> int </i> <code>-[no]glas</code><i></i> <code>-[no]ionize</code><i></i></p>
<h2>DESCRIPTION</h2>
<p> The mdrun program is the main computational chemistry engine within GROMACS. Obviously, it performs Molecular Dynamics simulations, but it can also perform Stochastic Dynamics, Energy Minimization, test particle insertion or (re)calculation of energies. Normal mode analysis is another option. In this case mdrun builds a Hessian matrix from single conformation. For usual Normal Modes-like calculations, make sure that the structure provided is properly energy-minimized. The generated matrix can be diagonalized by g_nmeig. </p>
<p> The mdrun program reads the run input file (<code> -s</code>) and distributes the topology over nodes if needed. mdrun produces at least four output files. A single log file (<code> -g</code>) is written, unless the option <code> -seppot</code> is used, in which case each node writes a log file. The trajectory file (<code> -o</code>), contains coordinates, velocities and optionally forces. The structure file (<code> -c</code>) contains the coordinates and velocities of the last step. The energy file (<code> -e</code>) contains energies, the temperature, pressure, etc, a lot of these things are also printed in the log file. Optionally coordinates can be written to a compressed trajectory file (<code> -x</code>). </p>
<p> The option <code> -dgdl</code> is only used when free energy perturbation is turned on. </p>
<p> When mdrun is started using MPI with more than 1 node, parallelization is used. By default domain decomposition is used, unless the <code> -pd</code> option is set, which selects particle decomposition. </p>
<p> With domain decomposition, the spatial decomposition can be set with option <code> -dd</code>. By default mdrun selects a good decomposition. The user only needs to change this when the system is very inhomogeneous. Dynamic load balancing is set with the option <code> -dlb</code>, which can give a significant performance improvement, especially for inhomogeneous systems. The only disadvantage of dynamic load balancing is that runs are no longer binary reproducible, but in most cases this is not important. By default the dynamic load balancing is automatically turned on when the measured performance loss due to load imbalance is 5% or more. At low parallelization these are the only important options for domain decomposition. At high parallelization the options in the next two sections could be important for increasing the performace. </p>
<p> When PME is used with domain decomposition, separate nodes can be assigned to do only the PME mesh calculation; this is computationally more efficient starting at about 12 nodes. The number of PME nodes is set with option <code> -npme</code>, this can not be more than half of the nodes. By default mdrun makes a guess for the number of PME nodes when the number of nodes is larger than 11 or performance wise not compatible with the PME grid x dimension. But the user should optimize npme. Performance statistics on this issue are written at the end of the log file. For good load balancing at high parallelization, npme should be divisible by the number of PME nodes </p>
<p> This section lists all options that affect the domain decomposition. </p>
<p> Option <code> -rdd</code> can be used to set the required maximum distance for inter charge-group bonded interactions. Communication for two-body bonded interactions below the non-bonded cut-off distance always comes for free with the non-bonded communication. Atoms beyond the non-bonded cut-off are only communicated when they have missing bonded interactions; this means that the extra cost is minor and nearly indepedent of the value of <code> -rdd</code>. With dynamic load balancing option <code> -rdd</code> also sets the lower limit for the domain decomposition cell sizes. By default <code> -rdd</code> is determined by mdrun based on the initial coordinates. The chosen value will be a balance between interaction range and communication cost. </p>
<p> When inter charge-group bonded interactions are beyond the bonded cut-off distance, mdrun terminates with an error message. For pair interactions and tabulated bonds that do not generate exclusions, this check can be turned off with the option <code> -noddcheck</code>. </p>
<p> When constraints are present, option <code> -rcon</code> influences the cell size limit as well. Atoms connected by NC constraints, where NC is the LINCS order plus 1, should not be beyond the smallest cell size. A error message is generated when this happens and the user should change the decomposition or decrease the LINCS order and increase the number of LINCS iterations. By default mdrun estimates the minimum cell size required for P-LINCS in a conservative fashion. For high parallelization it can be useful to set the distance required for P-LINCS with the option <code> -rcon</code>. </p>
<p> The <code> -dds</code> option sets the minimum allowed x, y and/or z scaling of the cells with dynamic load balancing. mdrun will ensure that the cells can scale down by at least this factor. This option is used for the automated spatial decomposition (when not using <code> -dd</code>) as well as for determining the number of grid pulses, which in turn sets the minimum allowed cell size. Under certain circumstances the value of <code> -dds</code> might need to be adjusted to account for high or low spatial inhomogeneity of the system. </p>
<p> The option <code> -nosum</code> can be used to only sum the energies at every neighbor search step and energy output step. This can improve performance for highly parallel simulations where this global communication step becomes the bottleneck. For a global thermostat and/or barostat the temperature and/or pressure will also only be updated every nstlist steps. With this option the energy file will not contain averages and fluctuations over all integration steps. </p>
<p> With <code> -rerun</code> an input trajectory can be given for which forces and energies will be (re)calculated. Neighbor searching will be performed for every frame, unless <code> nstlist</code> is zero (see the <code> .mdp</code> file). </p>
<p> ED (essential dynamics) sampling is switched on by using the <code> -ei</code> flag followed by an <code> .edi</code> file. The <code> .edi</code> file can be produced using options in the essdyn menu of the WHAT IF program. mdrun produces a <code> .edo</code> file that contains projections of positions, velocities and forces onto selected eigenvectors. </p>
<p> When user-defined potential functions have been selected in the <code> .mdp</code> file the <code> -table</code> option is used to pass mdrun a formatted table with potential functions. The file is read from either the current directory or from the GMXLIB directory. A number of pre-formatted tables are presented in the GMXLIB dir, for 6-8, 6-9, 6-10, 6-11, 6-12 Lennard Jones potentials with normal Coulomb. When pair interactions are present a separate table for pair interaction functions is read using the <code> -tablep</code> option. </p>
<p> When tabulated bonded functions are present in the topology, interaction functions are read using the <code> -tableb</code> option. For each different tabulated interaction type the table file name is modified in a different way: before the file extension an underscore is appended, then a b for bonds, an a for angles or a d for dihedrals and finally the table number of the interaction type. </p>
<p> The options <code> -pi</code>, <code> -po</code>, <code> -pd</code>, <code> -pn</code> are used for potential of mean force calculations and umbrella sampling. See manual. </p>
<p> With <code> -multi</code> multiple systems are simulated in parallel. As many input files are required as the number of systems. The system number is appended to the run input and each output filename, for instance topol.tpr becomes topol0.tpr, topol1.tpr etc. The number of nodes per system is the total number of nodes divided by the number of systems. One use of this option is for NMR refinement: when distance or orientation restraints are present these can be ensemble averaged over all the systems. </p>
<p> With <code> -replex</code> replica exchange is attempted every given number of steps. The number of replicas is set with the <code> -multi</code> option, see above. All run input files should use a different coupling temperature, the order of the files is not important. The random seed is set with <code> -reseed</code>. The velocities are scaled and neighbor searching is performed after every exchange. </p>
<p> Finally some experimental algorithms can be tested when the appropriate options have been given. Currently under investigation are: polarizability, glass simulations and X-Ray bombardments. </p>
<p> The option <code> -pforce</code> is useful when you suspect a simulation crashes due to too large forces. With this option coordinates and forces of atoms with a force larger than a certain value will be printed to stderr. </p>
<p> Checkpoints containing the complete state of the system are written at regular intervals (option <code> -cpt</code>) to the file <code> -cpo</code>, unless option <code> -cpt</code> is set to -1. A simulation can be continued by reading the full state from file with option <code> -cpi</code>. This option is intelligent in the way that if no checkpoint file is found, Gromacs just assumes a normal run and starts from the first step of the tpr file. </p>
<p> With checkpointing you can also use the option <code> -append</code> to just continue writing to the previous output files. This is not enabled by default since it is potentially dangerous if you move files, but if you just leave all your files in place and restart mdrun with exactly the same command (with options <code> -cpi</code> and <code> -append</code>) the result will be the same as from a single run. The contents will be binary identical (unless you use dynamic load balancing), but for technical reasons there might be some extra energy frames when using checkpointing (necessary for restarts without appending). </p>
<p> With option <code> -maxh</code> a simulation is terminated and a checkpoint file is written at the first neighbor search step where the run time exceeds <code> -maxh</code>*0.99 hours. </p>
<p> When mdrun receives a TERM signal, it will set nsteps to the current step plus one. When mdrun receives a USR1 signal, it will stop after the next neighbor search step (with nstlist=0 at the next step). In both cases all the usual output will be written to file. When running with MPI, a signal to one of the mdrun processes is sufficient, this signal should not be sent to mpirun or the mdrun process that is the parent of the others. </p>
<p> When mdrun is started with MPI, it does not run niced by default.</p>
<h2>FILES</h2>
<p> <code>-s</code><i> topol.tpr</i> <code>Input</code><br />
&nbsp;<wbr>Run input file: tpr tpb tpa&nbsp;<wbr> </p>
<p> <code>-o</code><i> traj.trr</i> <code>Output</code><br />
&nbsp;<wbr>Full precision trajectory: trr trj cpt&nbsp;<wbr> </p>
<p> <code>-x</code><i> traj.xtc</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Compressed trajectory&nbsp;<wbr>(portable xdr format)&nbsp;<wbr> </p>
<p> <code>-cpi</code><i> state.cpt</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Checkpoint file&nbsp;<wbr> </p>
<p> <code>-cpo</code><i> state.cpt</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Checkpoint file&nbsp;<wbr> </p>
<p> <code>-c</code><i> confout.gro</i> <code>Output</code><br />
&nbsp;<wbr>Structure file: gro g96 pdb&nbsp;<wbr> </p>
<p> <code>-e</code><i> ener.edr</i> <code>Output</code><br />
&nbsp;<wbr>Energy file: edr ene&nbsp;<wbr> </p>
<p> <code>-g</code><i> md.log</i> <code>Output</code><br />
&nbsp;<wbr>Log file&nbsp;<wbr> </p>
<p> <code>-dgdl</code><i> dgdl.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-field</code><i> field.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-table</code><i> table.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-tablep</code><i> tablep.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-tableb</code><i> table.xvg</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-rerun</code><i> rerun.xtc</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>Trajectory: xtc trr trj gro g96 pdb cpt&nbsp;<wbr> </p>
<p> <code>-tpi</code><i> tpi.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-tpid</code><i> tpidist.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-ei</code><i> sam.edi</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>ED sampling input&nbsp;<wbr> </p>
<p> <code>-eo</code><i> sam.edo</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>ED sampling output&nbsp;<wbr> </p>
<p> <code>-j</code><i> wham.gct</i> <code>Input, Opt.</code><br />
&nbsp;<wbr>General coupling stuff&nbsp;<wbr> </p>
<p> <code>-jo</code><i> bam.gct</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>General coupling stuff&nbsp;<wbr> </p>
<p> <code>-ffout</code><i> gct.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-devout</code><i> deviatie.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-runav</code><i> runaver.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-px</code><i> pullx.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-pf</code><i> pullf.xvg</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>xvgr/xmgr file&nbsp;<wbr> </p>
<p> <code>-mtx</code><i> nm.mtx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Hessian matrix&nbsp;<wbr> </p>
<p> <code>-dn</code><i> dipole.ndx</i> <code>Output, Opt.</code><br />
&nbsp;<wbr>Index file&nbsp;<wbr> </p>
<h2>OTHER OPTIONS</h2>
<p> <code>-[no]h</code><i>no </i><br />
&nbsp;<wbr>Print help info and quit </p>
<p> <code>-nice</code><i> int</i><code> 19</code><br />
&nbsp;<wbr>Set the nicelevel </p>
<p> <code>-deffnm</code><i> string</i><br />
&nbsp;<wbr>Set the default filename for all file options </p>
<p> <code>-[no]xvgr</code><i>yes </i><br />
&nbsp;<wbr>Add specific codes&nbsp;<wbr>(legends etc.)&nbsp;<wbr>in the output xvg files for the xmgrace program </p>
<p> <code>-[no]pd</code><i>no </i><br />
&nbsp;<wbr>Use particle decompostion </p>
<p> <code>-dd</code><i> vector</i><code> 0 0 0</code><br />
&nbsp;<wbr>Domain decomposition grid, 0 is optimize </p>
<p> <code>-npme</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Number of separate nodes to be used for PME, -1 is guess </p>
<p> <code>-ddorder</code><i> enum</i><code> interleave</code><br />
&nbsp;<wbr>DD node order:&nbsp;<wbr><code>&nbsp;<wbr>interleave</code>,&nbsp;<wbr><code>&nbsp;<wbr>pp_pme</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>cartesian</code> </p>
<p> <code>-[no]ddcheck</code><i>yes </i><br />
&nbsp;<wbr>Check for all bonded interactions with DD </p>
<p> <code>-rdd</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>The maximum distance for bonded interactions with DD&nbsp;<wbr>(nm), 0 is determine from initial coordinates </p>
<p> <code>-rcon</code><i> real</i><code> 0 </code><br />
&nbsp;<wbr>Maximum distance for P-LINCS&nbsp;<wbr>(nm), 0 is estimate </p>
<p> <code>-dlb</code><i> enum</i><code> auto</code><br />
&nbsp;<wbr>Dynamic load balancing&nbsp;<wbr>(with DD):&nbsp;<wbr><code>&nbsp;<wbr>auto</code>,&nbsp;<wbr><code>&nbsp;<wbr>no</code>&nbsp;<wbr>or&nbsp;<wbr><code>&nbsp;<wbr>yes</code> </p>
<p> <code>-dds</code><i> real</i><code> 0.8 </code><br />
&nbsp;<wbr>Minimum allowed dlb scaling of the DD cell size </p>
<p> <code>-[no]sum</code><i>yes </i><br />
&nbsp;<wbr>Sum the energies at every step </p>
<p> <code>-[no]v</code><i>no </i><br />
&nbsp;<wbr>Be loud and noisy </p>
<p> <code>-[no]compact</code><i>yes </i><br />
&nbsp;<wbr>Write a compact log file </p>
<p> <code>-[no]seppot</code><i>no </i><br />
&nbsp;<wbr>Write separate V and dVdl terms for each interaction type and node to the log file(s) </p>
<p> <code>-pforce</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Print all forces larger than this&nbsp;<wbr>(kJ/mol nm) </p>
<p> <code>-[no]reprod</code><i>no </i><br />
&nbsp;<wbr>Try to avoid optimizations that affect binary reproducibility </p>
<p> <code>-cpt</code><i> real</i><code> 15 </code><br />
&nbsp;<wbr>Checkpoint interval&nbsp;<wbr>(minutes) </p>
<p> <code>-[no]append</code><i>no </i><br />
&nbsp;<wbr>Append to previous output files when restarting from checkpoint </p>
<p> <code>-maxh</code><i> real</i><code> -1 </code><br />
&nbsp;<wbr>Terminate after 0.99 times this time&nbsp;<wbr>(hours) </p>
<p> <code>-multi</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Do multiple simulations in parallel </p>
<p> <code>-replex</code><i> int</i><code> 0</code><br />
&nbsp;<wbr>Attempt replica exchange every&nbsp;<wbr>&nbsp;<wbr>steps </p>
<p> <code>-reseed</code><i> int</i><code> -1</code><br />
&nbsp;<wbr>Seed for replica exchange, -1 is generate a seed </p>
<p> <code>-[no]glas</code><i>no </i><br />
&nbsp;<wbr>Do glass simulation with special long range corrections </p>
<p> <code>-[no]ionize</code><i>no </i><br />
&nbsp;<wbr>Do a simulation including the effect of an X-Ray bombardment on your system </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gromacs/">gromacs</a>(7)</code> </p>
<p> More information about <code>GROMACS</code> is available at &lt;<i><a rel="nofollow" href="http://www.gromacs.org/">http://www.gromacs.org/</a></i>&gt;. </p>
<h2>Index</h2>
