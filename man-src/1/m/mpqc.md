---
title: "mpqc(1)"
name: "mpqc"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpqc/"
description: "mpqc – The Massively Parallel Quantum Chemistry program (MPQC) computes the properties of molecules from first principles."
---

<h2 class="name">NAME</h2>
<p> mpqc &#8211; The Massively Parallel Quantum Chemistry program (MPQC) computes the properties of molecules from first principles. </p>
<p> This documentation is divided into the following chapters: </p>
<dl>
<dt>o</p>
<dd> <code>MPQC Overview</code></p>
<dt>o</p>
<dd> <code>Running MPQC</code></p>
<dt>o</p>
<dd> <code>MPQC Input</code></p>
<dt>o</p>
<dd> <code>Validating MPQC</code></p>
<dt>o</p>
<dd> <code>Running Psi 3 from MPQC</code></p>
<dt>o</p>
<dd> <code>CCA Components</code></p>
<dt>o</p>
<dd> <code>MPQC License</code></p>
<dt>o</p>
<dd> <code>MPQC Warranty</code></dl>
<h2>MPQC Overview</h2>
<p> The Massively Parallel Quantum Chemistry program (MPQC) computes the properties of molecules, <i>ab initio</i>, on a wide variety of computer architectures. </p>
<p> MPQC can compute closed shell and general restricted open-shell Hartree-Fock energies and gradients, second order open-shell perturbation theory (OPT2[2]) and Z-averaged perturbation theory (ZAPT2) energies, and second order closed shell Moeller-Plesset perturbation theory energies and gradients. It also includes methods for optimizing molecules in either Cartesian or internal coordinates. </p>
<p> MPQC is designed using object-oriented programming techniques and implemented in the C++ programming language. </p>
<h2>Running MPQC</h2>
<p> This chapter explains how to run MPQC in a variety of environments. </p>
<p> The first two sections give general information on running MPQC: </p>
<dl>
<dt>o</p>
<dd> <code>Command Line Options</code></p>
<dt>o</p>
<dd> <code>Environmental Variables</code></dl>
<p> The final sections given specific information on running MPQC in different environments: </p>
<dl>
<dt>o</p>
<dd> <code>Shared Memory Multiprocessor with SysV IPC</code></p>
<dt>o</p>
<dd> <code>Shared Memory Multiprocessor with POSIX Threads</code></p>
<dt>o</p>
<dd> <code>Shared or Distributed Memory Multiprocessor with MPI</code></p>
<dt>o</p>
<dd> <code>Special Notes for MP2 Gradients</code></p>
<dt>o</p>
<dd> <code>Special Notes for MP2-R12 energies</code></p>
<dt>o</p>
<dd> <code>Special Notes for CCA Components</code></dl>
<h3>Command Line Options</h3>
<p> MPQC can be given options followed by an optional input file name. If the input file name is not given, it will default to &#8216;mpqc.in&#8217;. The following command line options are recognized: </p>
<dl>
<dt>-o</p>
<dd> Gives the name of the output file. The default is the console.</dl>
<dl>
<dt>-i</p>
<dd> Convert a simple input file to an object oriented input file and write the result to the ouput. No calculations are done.</dl>
<dl>
<dt>-messagegrp</p>
<dd> A ParsedKeyVal specification of a MessageGrp object. The default depends on how MPQC was compiled.</dl>
<dl>
<dt>-memorygrp</p>
<dd> A ParsedKeyVal specification of a MemoryGrp object. The default depends on how MPQC was compiled.</dl>
<dl>
<dt>-threadgrp</p>
<dd> A ParsedKeyVal specification of a ThreadGrp object. The default depends on how MPQC was compiled.</dl>
<dl>
<dt>-integral</p>
<dd> A ParsedKeyVal specification of an Integral object. The default is IntegralV3. Note that some MolecularEnergy specializations require specific choices of Integral specializations and may not work with IntegralV3.</dl>
<dl>
<dt>-l</p>
<dd> Sets a limit on the number of basis functions. The default is zero, which means an unlimited number of basis functions.</dl>
<dl>
<dt>-W</p>
<dd> Sets the working directory. The default is the current directory.</dl>
<dl>
<dt>-c</p>
<dd> Check the input and exit.</dl>
<dl>
<dt>-v</p>
<dd> Print the version number.</dl>
<dl>
<dt>-w</p>
<dd> Print the warranty information (there is no warranty).</dl>
<dl>
<dt>-d</p>
<dd> If a debugger object was given in the input, start the debugger running as soon as MPQC is started.</dl>
<dl>
<dt>-h</p>
<dd> Print a list of options.</dl>
<dl>
<dt>-f</p>
<dd> The name of an object-oriented input file. The default is mpqc.in. This cannot be used if another input file is specified. This option is deprecated, as both input file formats can be read by given the input file name on the command line without any option flags.</dl>
<dl>
<dt>-cca-path</p>
<dd> A colon-separated list of directories in which CCA component libraries may be found.</dl>
<dl>
<dt>-cca-load</p>
<dd> A colon-separated list of sidl class names for CCA components which will be instantiated from the libraries found in the path given by -cca-path</dl>
<p> Some MPI environments do not pass the command line to slave programs, but supply it when MPI_Init is called. To make MPQC call MPI_Init with the correct arguments as early as possible use the configure option &#8211;enable-always-use-mpi.</p>
<h3>Environmental Variables</h3>
<p> MPQC looks at five environmental variables to set up communication, find library files, and specify the default Integral object. Machine specific libraries and utilities to run programs in parallel might look at other environment variables as well. The five that apply on all platforms are: </p>
<dl>
<dt>SCLIBDIR</p>
<dd> The name of the library directory. See the GaussianBasisSet documentation and look below for more information.</dl>
<dl>
<dt>MESSAGEGRP</p>
<dd> A ParsedKeyVal specification of a MessageGrp object. The default depends on how MPQC was compiled. See the MessageGrp class documentation for more information.</dl>
<dl>
<dt>MEMORYGRP</p>
<dd> A ParsedKeyVal specification of a MemoryGrp object. The default depends on how MPQC was compiled and the MessageGrp in use.</dl>
<dl>
<dt>THREADGRP</p>
<dd> A ParsedKeyVal specification of a ThreadGrp object. The default depends on how MPQC was compiled.</dl>
<dl>
<dt>INTEGRAL</p>
<dd> A ParsedKeyVal specification of an Integral object. The default is IntegralV3. Note that some MolecularEnergy specializations require specific choices of Integral specializations and may not work with IntegralV3.</dl>
<p> By default, MPQC tries to find library files first in the lib subdirectory of the installation directory and then the source code directory. If the library files cannot be found, MPQC must be notified of the new location with the environmental variable SCLIBDIR. </p>
<p> For example, if you need to run MPQC on a machine that doesn&#8217;t have the source code distribution in the same place as it was located on the machine on which MPQC is compiled you must do something like the following on the machine with the source code: </p>
<pre>
cd mpqc/lib
tar cvf ../sclib.tar basis atominfo.kv
</pre>
<p> Then transfer sclib.tar to the machine on which you want to run MPQC and do something like </p>
<pre>
mkdir ~/sclib
cd ~/sclib
tar xvf ../sclib.tar
setenv SCLIBDIR ~/sclib
</pre>
<p> The setenv command is specific to the C-shell. You will need to do what is appropriate for your shell. </p>
<p> The other three keywords specify objects. This is done by giving a mini ParsedKeyVal input in a string. The object is anonymous, that is, no keyword is associated with it. Here is an example: </p>
<pre>
setenv MESSAGEGRP '&lt;ShmMessageGrp&gt;:(n = 4)'
</pre>
<h3>Shared Memory Multiprocessor with SysV IPC</h3>
<p> By default, MPQC will run on only one CPU. To specify more, you can give a ShmMessageGrp object on the command line. The following would run MPQC in four processes: </p>
<pre>
mpqc -messagegrp '&lt;ShmMessageGrp&gt;:(n = 4)' input_file
</pre>
<p> Alternately, the ShmMessageGrp object can be given as an environmental variable: </p>
<pre>
setenv MESSAGEGRP '&lt;ShmMessageGrp&gt;:(n = 4)'
mpqc input_file
</pre>
<p> If MPQC should unexpectedly die, shared memory segments and semaphores will be left on the machine. These should be promptly cleaned up or other jobs may be prevented from running successfully. To see if you have any of these resources allocated, use the ipcs command. The output will look something like: </p>
<pre><code>
IPC status from / dev / kmem as of Wed Mar 13 14 : 42 : 18 1996 T ID KEY MODE OWNER GROUP Message Queues : Shared Memory : m 288800 0x00000000 --rw-- -- -- -cljanss user Semaphores : s 390 0x00000000 --ra-- -- -- -cljanss user s 391 0x00000000 --ra-- -- -- -cljanss user
</code></pre>
<p> To remove the IPC resources used by cljanss in the above example on IRIX, type: </p>
<pre>
ipcrm -m 288800
ipcrm -s 390
ipcrm -s 391
</pre>
<p> And on Linux, type: </p>
<pre>
ipcrm shm 288800
ipcrm sem 390
ipcrm sem 391
</pre>
<h3>Shared Memory Multiprocessor with POSIX Threads</h3>
<p> By default, MPQC will run with only one thread. To specify more, you can give a PthreadThreadGrp object on the command line. MPQC is not parallelized to as large an extent with threads as it is with the more conventional distributed memory model, so you might not get the best performance using this technique. On the other the memory overhead is lower and no interprocess communication is needed. </p>
<p> The following would run MPQC in four threads: </p>
<pre>
mpqc -threadgrp '&lt;PthreadThreadGrp&gt;:(num_threads = 4)' input_file
</pre>
<p> Alternately, the PthreadThreadGrp object can be given as an environmental variable: </p>
<pre>
setenv THREADGRP '&lt;PthreadThreadGrp&gt;:(num_threads = 4)'
mpqc input_file
</pre>
<h3>Shared or Distributed Memory Multiprocessor with MPI</h3>
<p> A MPIMessageGrp object is used to run using MPI. The number of nodes used is determined by the MPI run-time and is not specified as input data to MPIMessageGrp. </p>
<pre>
mpqc -messagegrp '&lt;MPIMessageGrp&gt;:()' input_file
</pre>
<p> Alternately, the MPIMessageGrp object can be given as an environmental variable: </p>
<pre>
setenv MESSAGEGRP '&lt;MPIMessageGrp&gt;:()'
mpqc input_file
</pre>
<p> Usually, a special command is needed to start MPI jobs; typically it is named mpirun.</p>
<h3>Special Notes for MP2 Gradients</h3>
<p> The MP2 gradient algorithm uses MemoryGrp object to access distributed shared memory. The MTMPIMemoryGrp class is the most efficient and reliable implementation of MemoryGrp. It requires a multi-thread aware MPI implementation, which is still not common. To run MP2 gradients on a machine with POSIX threads and an multi-thread aware MPI, use: </p>
<pre>
mpqc -messagegrp '&lt;MPIMessageGrp&gt;:()' \
     -threadgrp '&lt;PthreadThreadGrp&gt;:()' \
     -memorygrp '&lt;MTMPIMemoryGrp&gt;:()' \
     input_file
</pre>
<p> or </p>
<pre>
setenv MESSAGEGRP '&lt;MPIMessageGrp&gt;:()'
setenv THREADGRP '&lt;PthreadThreadGrp&gt;:()'
setenv MEMORYGRP '&lt;MTMPIMemoryGrp&gt;:()'
mpqc input_file
</pre>
<h3>Special Notes for MP2-R12 energies</h3>
<p> <code>Distributed Memory</code> </p>
<p> The MP2-R12 energy algorithm is similar to the MP2 energy algorithm that uses MemoryGrp object to access distributed memory. Hence the MTMPIMemoryGrp is the recommended implementation of MemoryGrp for such computations (see <code>Special Notes for MP2 Gradients</code>). </p>
<p> <code>Disk I/O</code> </p>
<p> In contrast to the MP2 energy and gradient algorithms, the MP2-R12 energy algorithm may have to use disk to store transformed MO integrals if a single pass through the AO integrals is not possible due to insufficient memory. The best option in such case is to increase the total amount of memory available to the computation by either increasing the number of tasks or the amount of memory per task or both. </p>
<p> When increasing memory further is not possible, the user has to specify which type of disk I/O should be used for the MP2-R12 energy algorithm. It is done through the r12ints keyword in input for the MBPT2_R12 object. The default choice is to use POSIX I/O on the node on which task 0 resides. This kind of disk I/O is guaranteed to work on all parallel machines, provided there&#8217;s enough disk space on the node. However, this is hardly most efficient on machines with some sort of parallel I/O available. On machines which have an efficient implementation of MPI-IO the r12ints should be set instead to mpi-mem. This will force the MBPT2_R12 object to use MPI-IO for disk I/O. It is user&#8217;s responsibility to make sure that the MO integrals file resides on an MPI-IO-compatible file system. Hence the r12ints_file keyword, which specifies the name of the MO integrals file, should be set to a location which is guaranteed to work properly with MPI-IO. For example, on IBM SP and other IBM machines which have General Parallel File System (GPFS), the user should set r12ints = mpi-mem and r12ints_file to a file on a GPFS file system. </p>
<p> <code>Integral object</code> </p>
<p> At the moment, MBPT2_R12 objects require specific specialization of Integral, IntegralCints. Thus in order to compute MP2-R12 energies, your version of MPQC needs to be compiled with support for IntegralCints. A free, open-source library called libint is a prerequisite for IntegralCints. In order to use IntegralCints as the default Integral object, add -integral &#8216;&lt;IntegralCints&gt;:()&#8217; to the command line, or set environmental variable INTEGRAL to &#8216;&lt;IntegralCints&gt;:()&#8217;.</p>
<h3>Special Notes for CCA Components</h3>
<p> <code>Common Component Architecture (CCA)</code> </p>
<p> Portions of MPQC functionality are being packaged into CCA components. For general overviews of CCA technology and framework usage, please see <a rel="nofollow" href="http://www.cca-forum.org">www.cca-forum.org</a> (the tutorial in particular) and the cca-chem-apps documentation. MPQC components may be utilized directly within the ccaffeine framework, while some components may be instantiated and used within MPQC itself, making use of an embedded CCA framework. </p>
<p> <code>CCA Runtime Environment</code> </p>
<p> For MPQC runs utilizing embedded components, the runtime environment for the CCA framework must be specified. The colon-separated path used to locate component libraries must be specified either using the -cca-path command-line option or using the cca_path key within the mpqc section of a keyval input. The colon-separated list of component sidl class names which will be referenced within the input must be specified using either the -cca-load command-line option or using the cca_load key within the mpqc section of a keyval input. If defaults for the cca-path and cca-load options are desired, do_cca must be set to yes in the keyval input. </p>
<h2>MPQC Input</h2>
<p> MPQC supports two input formats. The primary input is an object oriented format which gives users access to all of MPQC&#8217;s options. The second format allows access to a subset of MPQC&#8217;s capabilities, but is more intuitive and easier to learn. New users are advised to start with the simplified format. MPQC can be used to convert the simplified format to the full object-oriented format with the -i option. </p>
<p> Each of these input formats is described in the following two chapters: </p>
<dl>
<dt>o</p>
<dd> <code>Simple Input</code></p>
<dt>o</p>
<dd> <code>Object-Oriented Input</code></dl>
<h2>Simple Input</h2>
<p> The simple input format consists of keywords followed by a &#8216;:&#8217; followed by a value. The keywords are case sensitive. The values might be modified by options found in parenthesis. For example, the following input performs an optimization of water using density functional theory with the B3LYP exchange-correlation functional: </p>
<pre>
% B3LYP optimization of water
optimize: yes
method: KS (xc = B3LYP)
basis: 3-21G*
molecule: (angstrom)
    O    0.172   0.000   0.000
    H    0.745   0.000   0.754
    H    0.745   0.000  -0.754
</pre>
<p>&nbsp;<wbr> </p>
<p> Comments begin with a % and continue to the end of the line. Basis set names containing special characters, such as a space or parentheses, must be quoted inside a pair of double quotes. The accepted keywords are: </p>
<dl>
<dt>molecule</p>
<dd> Gives the atoms types and coordinates. The following options can be used</dl>
<dl>
<dt>bohr</p>
<dd> The coordinates are given in Bohr.</p>
<dt>angstrom</p>
<dd> The coordinates are given in Angstroms (the default).</p>
<dt>charge</p>
<dd> This option can be given after an &#8216;element x y z&#8217; quadruple. This will override the charge on the atom. For example, (charge = 0) can be given for the ghost atoms in a counterpoise correction calculation.</dl>
<dl>
<dt>multiplicity</p>
<dd> Gives the multiplicity of the molecule. The default is 1.</dl>
<dl>
<dt>optimize</p>
<dd> If yes, then an optimization will be performed. The default is no. The following options can be given.</dl>
<dl>
<dt>cartesian</p>
<dd> Use Cartesian coordinates.</p>
<dt>internal</p>
<dd> Use internal coordinates.</p>
<dt>redundant</p>
<dd> Use redundant internal coordinates.</dl>
<dl>
<dt>gradient</p>
<dd> If yes, then a gradient calculation will be performed. The default is no.</dl>
<dl>
<dt>frequencies</p>
<dd> If yes, then the frequencies will be obtained. The default is no.</dl>
<dl>
<dt>charge</p>
<dd> Specificies the charge on the molecule. The default is 0.</dl>
<dl>
<dt>method</p>
<dd> Specifices the method. There is no default and the possible values are:</dl>
<dl>
<dt>HF</p>
<dd> Hartree-Fock. Unrestricted HF is used if multiplicity &gt; 1</p>
<dt>RHF</p>
<dd> Restricted Hartree-Fock.</p>
<dt>UHF</p>
<dd> Unrestricted Hartree-Fock.</p>
<dt>KS</p>
<dd> Kohn-Sham. Unrestricted KS is used if multiplicity &gt; 1</p>
<dt>RKS</p>
<dd> Restricted Kohn-Sham.</p>
<dt>UKS</p>
<dd> Unrestricted Kohn-Sham.</p>
<dt>MP2</p>
<dd> Second order Moeller-Plesset perturbation theory. Only available for multiplicity = 1.</p>
<dt>MP2-R12/A</p>
<dd> The A version of MP2-R12. Only available for multiplicity = 1. An auxiliary basis may be specified. No gradient, optimization, or frequencies are possible.</p>
<dt>MP2-R12/A&#8217;</p>
<dd> The A&#8217; version of MP2-R12. Only available for multiplicity = 1. An auxiliary basis may be specified. No gradient, optimization, or frequencies are possible.</p>
<dt>ZAPT2</p>
<dd> Z-averaged perturbation theory. Only available for multiplicity &gt; 1. No gradient, optimization, or frequencies are possible.</dl>
<p> The following options are valid with the KS, RKS, and UKS methods: </p>
<dl>
<dt>grid</p>
<dd> Specifies the grid to be used for numerical integrations. The following values can be given:</p>
<dt>xcoarse</p>
<dd>
<dt>coarse</p>
<dd>
<dt>medium</p>
<dd>
<dt>fine</p>
<dd>
<dt>xfine</p>
<dd>
<dt>ultrafine</p>
<dd></dl>
<dl>
<dt>xc</p>
<dd> Specifies the exchange-correlation functional. There is no default. See the table in the StdDenFunctional class documentation for the possible values.</dl>
<p> The following options are valid with the MP2-R12/A and MP2-R12/A&#8217; methods. These options are mutually exclusive: </p>
<dl>
<dt>abs</p>
<dd> Use the standard Auxiliary Basis Set method.</p>
<dt>abs+</p>
<dd> Use the standard Auxiliary Basis Set method, but use the union of the orbital and the given auxiliary basis as the actual auxiliary basis set used.</p>
<dt>cabs</p>
<dd> Use the Complementary Auxiliary Basis Set method.</p>
<dt>cabs+</p>
<dd> Use the Complementary Auxiliary Basis Set method, but use the union of the orbital and the given auxiliary basis as the actual auxiliary basis set used.</dl>
<p> The following options are valid with the MP2-R12/A&#8217; method: </p>
<dl>
<dt>ebc</p>
<dd> Assume the Extended Brillion Condition to hold. This is the default.</p>
<dt>gbc</p>
<dd> Assume the Generalized Brillion Condition to hold. This is the default.</p>
<dt>!ebc</p>
<dd> Do not assume the Extended Brillion Condition to hold.</p>
<dt>!gbc</p>
<dd> Do not assume the Generalized Brillion Condition to hold.</dl>
<dl>
<dt>basis</p>
<dd> Specifies the basis set. There is no default. See the table in the GaussianBasisSet class documentation for the available basis sets.</dl>
<dl>
<dt>auxbasis</p>
<dd> Specifies the auxiliary basis set for MP2-R12 methods. There is no default. See the table in the GaussianBasisSet class documentation for the available basis sets.</dl>
<dl>
<dt>restart</p>
<dd> Set to yes to restart an optimization. The default is no.</dl>
<dl>
<dt>checkpoint</p>
<dd> Set to no to not save checkpoint files during an optimization. The default is yes.</dl>
<dl>
<dt>symmetry</p>
<dd> Specifices the Schoenflies symbol of the point group of the molecule. The default is auto, which will cause to program to find the highest order Abelian subgroup of the molecule.</dl>
<dl>
<dt>docc</p>
<dd> Gives the number of doubly occupied orbitals in each each irreducible representation in a parenthesized list. The symmetry must be specified and not be auto. The method must be restricted.</dl>
<dl>
<dt>socc</p>
<dd> Gives the number of single occupied orbitals in each each irreducible representation in a parenthesized list. The symmetry must be specified and not be auto. The method must be restricted.</dl>
<dl>
<dt>alpha</p>
<dd> Gives the number of alpha occupied orbitals in each each irreducible representation in a parenthesized list. The symmetry must be specified and not be auto. The method must be unrestricted.</dl>
<dl>
<dt>beta</p>
<dd> Gives the number of beta occupied orbitals in each each irreducible representation in a parenthesized list. The symmetry must be specified and not be auto. The method must be unrestricted.</dl>
<dl>
<dt>frozen_docc</p>
<dd> Gives the number of frozen core orbitals. Can be either a single integer or a parenthesized list giving the frozen core orbitals in each irreducible representation. In the latter case the symmetry must be given and not be auto.</dl>
<dl>
<dt>frozen_uocc</p>
<dd> Gives the number of frozen virtual orbitals. Can be either a single integer or a parenthesized list giving the frozen virtual orbitals in each irreducible representation. In the latter case the symmetry must be given and not be auto.</dl>
<dl>
<dt>memory</p>
<dd> Gives a hint for the amount of memory in bytes that can be used. This is typically a lower bound, more memory will be used in practice and the exact amount cannot be precisely controlled. The format is a fixed or floating point number optionally followed (without spaces) by one of the following suffixes: KB, MB, GB, KIB, MIB, or GIB.</dl>
<h2>Object-Oriented Input</h2>
<p> MPQC is an object-oriented program that directly allows the user to specify objects that MPQC then manipulates to obtain energies, properties, etc. This makes the input very flexible, but very complex. However, most calculations should be quite similar to the one of the examples given later in this chapter. The best way to get started is to use one of the example input files and modify it to meet your needs. </p>
<p> The object-oriented input format is described in the following sections: </p>
<dl>
<dt>o</p>
<dd> <code>Overview of the Object-Oriented Input</code></p>
<dt>o</p>
<dd> <code>A Walk-Through of an Object-Oriented Input File</code></p>
<dt>o</p>
<dd> <code>Sample Object-Oriented Input Files</code></dl>
<h3>Overview of the Object-Oriented Input</h3>
<p> MPQC starts off by creating a ParsedKeyVal object that parses the input file specified on the command line. The format of the input file is documented in the KeyVal documentation. It is basically a free format input that associates keywords and logical groupings of keywords with values. The values can be scalars, arrays, or objects. </p>
<p> The keywords recognized by MPQC begin with the mpqc prefix. That is, they must be nested between an mpqc:( and a ). Alternately, each keyword can be individually prefixed by mpqc:. The primary keywords are given below. Some of the keywords specify objects, in which case the object will require more ParsedKeyVal input. These objects are created from the input by using their ParsedKeyVal constructors. These constructors are documented with the source code documentation for the class. </p>
<dl>
<dt>mole</p>
<dd> This is the most important keyword for MPQC. It specifies the MolecularEnergy object. This is an object that knows how to compute the energy of a molecule. The specializations of MolecularEnergy that are most commonly used are CLKS, HSOSKS, UKS, CLHF, HSOSHF, UHF, and MBPT2.</dl>
<dl>
<dt>opt</p>
<dd> This keyword must be specified for optimizations. It specifies an Optimize object. Usually, QNewtonOpt is best for finding minima and EFCOpt is best for transition states.</dl>
<dl>
<dt>freq</p>
<dd> This keyword must be specified to compute frequencies. It specifies a MolecularFrequencies object.</dl>
<dl>
<dt>thread</p>
<dd> This specifies an object of type ThreadGrp that can be used to advantage on shared-memory multiprocessor machines for certain types of calculations. This keyword can be overridden by giving the ThreadGrp in the environment or command line. See the section on running MPQC for more information.</dl>
<dl>
<dt>integrals</p>
<dd> This specifies an object of type Integral that will be used as the default integral evaluator. If MP2-R12 is used, then this should be set to use IntegralCints with a line like integrals&lt;IntegralCints&gt;: ().</dl>
<dl>
<dt>checkpoint</p>
<dd> The value of this keyword is boolean.</dl>
<dl>
<dt>o</p>
<dd> true and optimization is to be performed
</dl>
<p> opt object will be checkpointed after each iteration. The checkpoint file suffix is &#8216;.ckpt&#8217;. </p>
<dl>
<dt>o</p>
<dd> true and optimization is not performed
</dl>
<p> mole object will be checkpointed at intermediate points. The manner in which mole will be checkpointed depends on its particular type. The checkpoint file suffix is usually &#8216;.wfn&#8217;, however in general it will depend on the particular specialization of MolecularEnergy. </p>
<p> The default is to not checkpoint. </p>
<dl>
<dt>checkpoint_freq</p>
<dd> This specifies how often to checkpoint certain MolecularEnergy specializations which compute iteratively. Currently, mole objects of SCF type can use this keyword. The default is 1, which means to checkpoint after every iteration.</dl>
<dl>
<dt>savestate</p>
<dd> The value of this keyword is boolean. If true, then the states of the Optimize and MolecularEnergy objects will be saved after the calculation completes. The output file suffixes are &#8216;.ckpt&#8217; and &#8216;.wfn&#8217;, respectively. The default is to save state.</dl>
<dl>
<dt>restart</p>
<dd> The value of this keyword is boolean. If true, mpqc will attempt to restart the calculation. If the checkpoint file is not found, the calculation will continue as if the value were false. The default is true.</dl>
<dl>
<dt>restart_file</p>
<dd> This gives the name of a file from which restart information is read. If the file name ends with &#8216;.wfn&#8217; then MPQC will try to restore a MolecularEnergy object from it and query for the opt object in the input file. If the file name ends with &#8216;.ckpt&#8217; MPQC will try to restore an Optimize object from this file. The default file name is formed by appending &#8216;.ckpt&#8217; to the input file name with the extension removed.</dl>
<dl>
<dt>do_energy</p>
<dd> The value of this keyword is boolean. If true a single point energy calculation will be done for the MolecularEnergy object given with the mole keyword. The default is true.</dl>
<dl>
<dt>do_gradient</p>
<dd> The value of this keyword is boolean. If true a single point gradient calculation will be done for the MolecularEnergy object given with the mole keyword. The default is false.</dl>
<dl>
<dt>do_cca</p>
<dd> The value of this keywork is boolean. If true the cca embedded framework will be initialized. The default is false.</dl>
<dl>
<dt>cca_path</p>
<dd> The value of this keyword is a string that provides a colon-separated list of directories in which CCA component libraries may be found.</dl>
<dl>
<dt>cca_load</p>
<dd> The value of this keyword is a string that provides a colon-separated list of sidl class names for CCA components which will be instantiated from the libraries found in the path given by cca_path.</dl>
<dl>
<dt>optimize</p>
<dd> The value of this keyword is boolean. If true and the opt keyword was set to a valid value, then an optimization will be performed. The default is true.</dl>
<dl>
<dt>write_pdb</p>
<dd> The value of this keyword is boolean. If true a PDB file with the molecular coordinates will be written.</dl>
<dl>
<dt>filename</p>
<dd> The value of this keyword is a string that gives a name from which checkpoint and other filenames are constructed. The default is the basename of the input file.</dl>
<dl>
<dt>print_timings</p>
<dd> If this is true, timing information is printed at the end of the run. The default is true.</dl>
<p> There are also some utility keywords that tell mpqc some technical details about how to do the calculation:</p>
<dl>
<dt>debug</p>
<dd> This optional keyword gives a Debugger object which can be used to help find the problem if MPQC encounters a catastrophic error.</p>
<dt>matrixkit</p>
<dd> This optional keyword gives a SCMatrixKit specialization which is used to produce matrices of the desired type. The default is a ReplSCMatrixKit which replicates matrices on all of the nodes. Other choices are not thoroughly tested.</dl>
<h3>A Walk-Through of an Object-Oriented Input File</h3>
<p> This example input does a Hartree-Fock calculation on water. Following is the entire input, followed by a breakdown with descriptions. </p>
<p>% This input does a Hartree &#8211; Fock calculation on water.molecule&lt;Molecule&gt; : (<br />
                                                                                 symmetry = C2V<br />
                                                                                     unit = angstrom{atoms geometry} = {<br />
                                                                                         O[0.00000000 0.00000000 0.37000000] H[0.78000000 0.00000000 &#8211; 0.18000000] H[-0.78000000 0.00000000 &#8211; 0.18000000]}) basis&lt;GaussianBasisSet&gt; : (name = &#8216;STO-3G&#8217; molecule = $<br />
                                                                                                                                                                                                                                       : molecule) mpqc : (mole&lt;CLHF&gt;<br />
                                                                                                                                                                                                                                                           : (molecule = $<br />
                                                                                                                                                                                                                                                              : molecule basis = $<br />
                                                                                                                                                                                                                                                              : basis))</p>
<p>&nbsp;<wbr> </p>
<p> We start with a descriptive comment. Comments begin with a %. Everything from the % to the end of the line is ignored. </p>
<pre>
% This input does a Hartree-Fock calculation on water.
</pre>
<p>&nbsp;<wbr> </p>
<p> Now lets set up a Molecule object. The name of the object comes first, it is molecule. Then, in angle brackets, comes the type of the molecule, which is the class Molecule. The keyword and class name are followed by a : and then several pieces of input grouped between a pair of matching parentheses. These parentheses contain the information that will be given to Molecule KeyVal constructor. </p>
<pre>
molecule&lt;Molecule&gt;: (
</pre>
<p>&nbsp;<wbr> </p>
<p> The point group of the molecule is needed. This is done by assigning symmetry to a case insensitive Schoenflies symbol that is used to initialize a PointGroup object. An Abelian point group should be used. </p>
<pre>
  symmetry = C2V
</pre>
<p>&nbsp;<wbr> </p>
<p> The default unit for the Cartesian coordinates is Bohr. You can specify other units by assigned unit to a string that will be used to initialize a Units object. </p>
<pre>
  unit = angstrom
</pre>
<p>&nbsp;<wbr> </p>
<p> Finally, the atoms and coordinates are given. This can be given in the shorthand table syntax shown below. The headings of the table are the keywords between the first pair of brackets. These are followed by an = and another pair of brackets that contain the data. The first datum is assigned to the first element of the array that corresponds to the first heading, atom. The second datum is assigned to the first element of the array associated with the second heading, geometry, and so on. Here the second datum is actually a vector: the x, y and z coordinates of the first atom. </p>
<p>  { atoms                       geometry                   } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)</p>
<p>&nbsp;<wbr> </p>
<p> Next, a basis set object is given. </p>
<pre>
basis&lt;GaussianBasisSet&gt;: (
  name = 'STO-3G'
  molecule = $:molecule
)
</pre>
<p>&nbsp;<wbr> </p>
<p> Now we will give the main body of input. All the subsequent keywords will be grouped in the mpqc section of the input (that is, each keyword will be prefixed with mpqc:). </p>
<pre>
mpqc: (
</pre>
<p>&nbsp;<wbr> </p>
<p> Next we give the mole keyword which provides a specialization of the MolecularEnergy class. In this case we will do a closed-shell Hartree-Fock calculation. That is done with an object of type CLHF. The keywords that CLHF accepts are given with the documentation for the CLHF class, usually in the description of the const RefKeyVal&amp; constructor for the class. Also with the CLHF documentation is a list of parent classes. Each of the parent classes may also have input. This input is included with the rest of the input for the child class. </p>
<pre>
  mole&lt;CLHF&gt;: (
</pre>
<p>&nbsp;<wbr> </p>
<p> The next line specifies the molecule to be used. There are two things to note, first that this is actually a reference to complete molecule specification elsewhere in the input file. The $ indicates that this is a reference and the keyword following the $ is the actual location of the molecule. The : in front of the keyword means that the keyword is not relative to the current location in the input, but rather relative to the root of the tree of keywords. Thus, this line grabs the molecule that was specified above. The molecule object could have been placed here, but frequently it is necessary that several objects refer to the exact same object and this can only be done using references. </p>
<p> The second point is that if you look at the documentation for CLHF, you will see that it doesn&#8217;t read molecule keyword. However, if you follow its parent classes up to MolecularEnergy, you&#8217;ll find that molecule is indeed read. </p>
<pre>
    molecule = $:molecule
</pre>
<p>&nbsp;<wbr> </p>
<p> Just as we gave molecule, specify the basis set with the basis keyword as follows: </p>
<pre>
    basis = $:basis
</pre>
<p>&nbsp;<wbr> </p>
<p> Now we close off the parentheses we opened above and we are finished. </p>
<pre>
  )
)
</pre>
<p>&nbsp;<wbr> </p>
<h3>Sample Object-Oriented Input Files</h3>
<p> The easiest way to get started with mpqc is to start with one of sample inputs that most nearly matches your problem. The src/bin/mpqc/samples contains all of the sample inputs below: </p>
<dl>
<dt>o</p>
<dd> <code>Hartree-Fock Energy</code></p>
<dt>o</p>
<dd> <code>MP2 Energy</code></p>
<dt>o</p>
<dd> <code>MP2-R12 energy</code></p>
<dt>o</p>
<dd> <code>Hartree-Fock Optimization</code></p>
<dt>o</p>
<dd> <code>Optimization with a Computed Guess Hessian</code></p>
<dt>o</p>
<dd> <code>Optimization Using Newton&#8217;s Method</code></p>
<dt>o</p>
<dd> <code>Hartree-Fock Frequencies</code></p>
<dt>o</p>
<dd> <code>Giving Coordinates and a Guess Hessian</code></p>
<dt>o</p>
<dd> <code>Optimization with a Hydrogen Bond</code></p>
<dt>o</p>
<dd> <code>Fixed Coordinate Optimization</code></p>
<dt>o</p>
<dd> <code>Transition State Optimization</code></p>
<dt>o</p>
<dd> <code>Transition State Optimization with a Computed Guess Hessian</code></p>
<dt>o</p>
<dd> <code>Hartree-Fock energy with intermediate checkpointing</code></p>
<dt>o</p>
<dd> <code>MP2-R12 energy with intermediate checkpointing</code></p>
<dt>o</p>
<dd> <code>HF gradient computed from a previously computed HF wave funtion</code></p>
<dt>o</p>
<dd> <code>MP2 Energy computed using precomputed Hartree-Fock wave function</code></p>
<dt>o</p>
<dd> <code>CLHF energy using a CCA integrals component</code></dl>
<h3>Hartree-Fock Energy</h3>
<p> The following input will compute the Hartree-Fock energy of water. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>MP2 Energy</h3>
<p> The following input will compute the MP2 energy of water. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;MBPT2&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
    % reference wavefunction<br />
    reference&lt;CLHF&gt;: (<br />
      molecule = $:molecule<br />
      basis = $:basis<br />
      memory = 16000000<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>MP2-R12 energy</h3>
<p> The following will compute the MP2-R12 energy of water in standard approximation A&#8217; (MP2-R12/A&#8217;). </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;cc-pVDZ&#8217;<br />
  molecule = $:molecule<br />
)<br />
% auxiliary basis set specification<br />
abasis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;aug-cc-pVDZ&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;MBPT2_R12&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    aux_basis = $:abasis<br />
    stdapprox = &#8216;A&#8221;<br />
    nfzc = 1<br />
    memory = 16000000<br />
    integrals&lt;IntegralCints&gt;:()<br />
    % reference wavefunction<br />
    reference&lt;CLHF&gt;: (<br />
      molecule = $:molecule<br />
      basis = $:basis<br />
      memory = 16000000<br />
      integrals&lt;IntegralCints&gt;:()<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Hartree-Fock Optimization</h3>
<p> The following input will optimize the geometry of water using the quasi-Newton method. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;6-31G*&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
  )<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;QNewtonOpt&gt;: (<br />
    function = $..:mole<br />
    update&lt;BFGSUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Optimization with a Computed Guess Hessian</h3>
<p> The following input will optimize the geometry of water using the quasi-Newton method. The guess Hessian will be computed at a lower level of theory. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;6-31G*&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
  )<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
    guess_hessian&lt;FinDispMolecularHessian&gt;: (<br />
      molecule = $:molecule<br />
      only_totally_symmetric = yes<br />
      eliminate_cubic_terms = no<br />
      checkpoint = no<br />
      energy&lt;CLHF&gt;: (<br />
        molecule = $:molecule<br />
        memory = 16000000<br />
        basis&lt;GaussianBasisSet&gt;: (<br />
          name = &#8216;3-21G&#8217;<br />
          molecule = $:molecule<br />
        )<br />
      )<br />
    )<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;QNewtonOpt&gt;: (<br />
    function = $..:mole<br />
    update&lt;BFGSUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Optimization Using Newton&#8217;s Method</h3>
<p> The following input will optimize the geometry of water using the Newton&#8217;s method. The Hessian will be computed at each step in the optimization. However, Hessian recomputation is usually not worth the cost; try using the computed Hessian as a guess Hessian for a quasi-Newton method before resorting to a Newton optimization. </p>
<p>% Emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = c2v<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
     O     [     0.00000000     0.00000000     0.36937294 ]<br />
     H     [     0.78397590     0.00000000    -0.18468647 ]<br />
     H     [    -0.78397590     0.00000000    -0.18468647 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;3-21G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  restart = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
  )<br />
  do_energy = no<br />
  do_gradient = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
    coor = $..:coor<br />
    guess_wavefunction&lt;CLHF&gt;: (<br />
      molecule = $:molecule<br />
      total_charge = 0<br />
      basis&lt;GaussianBasisSet&gt;: (<br />
        molecule = $:molecule<br />
        name = &#8216;STO-3G&#8217;<br />
      )<br />
      memory = 16000000<br />
    )<br />
    hessian&lt;FinDispMolecularHessian&gt;: (<br />
      only_totally_symmetric = yes<br />
      eliminate_cubic_terms = no<br />
      checkpoint = no<br />
    )<br />
  )<br />
  optimize = yes<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;NewtonOpt&gt;: (<br />
    print_hessian = yes<br />
    max_iterations = 20<br />
    function = $..:mole<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Hartree-Fock Frequencies</h3>
<p> The following input will compute Hartree-Fock frequencies by finite displacements. A thermodynamic analysis will also be performed. If optimization input is also provided, then the optimization will be run first, then the frequencies. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C1<br />
  { atoms geometry } = {<br />
    O     [  0.0000000000    0.0000000000    0.8072934188 ]<br />
    H     [  1.4325589285    0.0000000000   -0.3941980761 ]<br />
    H     [ -1.4325589285    0.0000000000   -0.3941980761 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
  )<br />
% vibrational frequency input<br />
  freq&lt;MolecularFrequencies&gt;: (<br />
    molecule = $:molecule<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Giving Coordinates and a Guess Hessian</h3>
<p> The following example shows several features that are really independent. The variable coordinates are explicitly given, rather than generated automatically. This is especially useful when a guess Hessian is to be provided, as it is here. This Hessian, as given by the user, is not complete and the QNewtonOpt object will fill in the missing values using a guess the Hessian provided by the MolecularEnergy object. Also, fixed coordinates are given in this sample input. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C1<br />
  { atoms geometry } = {<br />
      H    [ 0.088    2.006    1.438 ]<br />
      O    [ 0.123    3.193    0.000 ]<br />
      H    [ 0.088    2.006   -1.438 ]<br />
      O    [ 4.502    5.955   -0.000 ]<br />
      H    [ 2.917    4.963   -0.000 ]<br />
      H    [ 3.812    7.691   -0.000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
  )<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
      extra_bonds = [ 2 5 ]<br />
    )<br />
    % use these instead of generated coordinates<br />
    variable&lt;SetIntCoor&gt;: [<br />
      &lt;StreSimpleCo&gt;:( atoms = [ 2 5 ] )<br />
      &lt;BendSimpleCo&gt;:( atoms = [ 2 5 4 ] )<br />
      &lt;OutSimpleCo&gt;: ( atoms = [ 5 2 1 3 ] )<br />
      &lt;SumIntCoor&gt;: (<br />
        coor: [<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 1 2 ] )<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 2 3 ] )<br />
          ]<br />
        coef = [ 1.0 1.0 ]<br />
        )<br />
      &lt;SumIntCoor&gt;: (<br />
        coor: [<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 4 5 ] )<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 4 6 ] )<br />
          ]<br />
        coef = [ 1.0 1.0 ]<br />
        )<br />
      &lt;BendSimpleCo&gt;:( atoms = [ 1 2 3 ] )<br />
      &lt;BendSimpleCo&gt;:( atoms = [ 5 4 6 ] )<br />
    ]<br />
    % these are fixed by symmetry anyway,<br />
    fixed&lt;SetIntCoor&gt;: [<br />
      &lt;SumIntCoor&gt;: (<br />
        coor: [<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 1 2 ] )<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 2 3 ] )<br />
          ]<br />
        coef = [ 1.0 -1.0 ]<br />
        )<br />
      &lt;SumIntCoor&gt;: (<br />
        coor: [<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 4 5 ] )<br />
          &lt;StreSimpleCo&gt;:( atoms = [ 4 6 ] )<br />
          ]<br />
        coef = [ 1.0 -1.0 ]<br />
        )<br />
      &lt;TorsSimpleCo&gt;:( atoms = [ 2 5 4 6] )<br />
      &lt;OutSimpleCo&gt;:( atoms = [ 3 2 6 4 ] )<br />
      &lt;OutSimpleCo&gt;:( atoms = [ 1 2 6 4 ] )<br />
    ]<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;QNewtonOpt&gt;: (<br />
    function = $..:mole<br />
    update&lt;BFGSUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
    % give a partial guess hessian in internal coordinates<br />
    % the missing elements will be filled in automatically<br />
    hessian = [<br />
        [  0.0109261670 ]<br />
        [ -0.0004214845    0.0102746106  ]<br />
        [ -0.0008600592    0.0030051330    0.0043149957 ]<br />
        [  0.0             0.0             0.0          ]<br />
        [  0.0             0.0             0.0          ]<br />
        [  0.0             0.0             0.0          ]<br />
        [  0.0             0.0             0.0          ]<br />
     ]<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Optimization with a Hydrogen Bond</h3>
<p> The automatic internal coordinate generator will fail if it cannot find enough redundant internal coordinates. In this case, the internal coordinate generator must be explicitly created in the input and given extra connectivity information, as is shown below. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C1<br />
  { atoms geometry } = {<br />
      H    [ 0.088    2.006    1.438 ]<br />
      O    [ 0.123    3.193    0.000 ]<br />
      H    [ 0.088    2.006   -1.438 ]<br />
      O    [ 4.502    5.955   -0.000 ]<br />
      H    [ 2.917    4.963   -0.000 ]<br />
      H    [ 3.812    7.691   -0.000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
  )<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    % give an internal coordinate generator that knows about the<br />
    % hydrogen bond between atoms 2 and 5<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
      extra_bonds = [ 2 5 ]<br />
    )<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;QNewtonOpt&gt;: (<br />
    function = $..:mole<br />
    update&lt;BFGSUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Fixed Coordinate Optimization</h3>
<p> This example shows how to selectively fix internal coordinates in an optimization. Any number of linearly independent coordinates can be given. These coordinates must remain linearly independent throughout the optimization, a condition that might not hold since the coordinates can be nonlinear. </p>
<p> By default, the initial fixed coordinates&#8217; values are taken from the cartesian geometry given by the Molecule object; however, the molecule will be displaced to the internal coordinate values given with the fixed internal coordinates if have_fixed_values keyword is set to true, as shown in this example. In this case, the initial cartesian geometry should be reasonably close to the desired initial geometry and all of the variable coordinates will be frozen to their original values during the initial displacement. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = CS<br />
  { atoms geometry } = {<br />
    H [  3.04 -0.69 -1.59 ]<br />
    H [  3.04 -0.69  1.59 ]<br />
    N [  2.09 -0.48 -0.00 ]<br />
    C [ -0.58 -0.15  0.00 ]<br />
    H [ -1.17  1.82  0.00 ]<br />
    H [ -1.41 -1.04 -1.64 ]<br />
    H [ -1.41 -1.04  1.64 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;3-21G*&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
    have_fixed_values = yes<br />
    fixed&lt;SetIntCoor&gt;: [<br />
      &lt;OutSimpleCo&gt;: ( value = -0.1<br />
                       label = &#8216;N-inversion&#8217;<br />
                       atoms = [4 3 2 1] )<br />
      ]<br />
  )<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;QNewtonOpt&gt;: (<br />
    max_iterations = 20<br />
    function = $..:mole<br />
    update&lt;BFGSUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Transition State Optimization</h3>
<p> This example shows a transition state optimization of the N-inversion in $mathrm{CH}_3mathrm{NH}_2$ using mode following. The initial geometry was obtained by doing a few fixed coordinate optimizations along the inversion coordinate. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = CS<br />
  { atoms geometry } = {<br />
    H [  3.045436 -0.697438 -1.596748 ]<br />
    H [  3.045436 -0.697438  1.596748 ]<br />
    N [  2.098157 -0.482779 -0.000000 ]<br />
    C [ -0.582616 -0.151798  0.000000 ]<br />
    H [ -1.171620  1.822306  0.000000 ]<br />
    H [ -1.417337 -1.042238 -1.647529 ]<br />
    H [ -1.417337 -1.042238  1.647529 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;3-21G*&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
    followed&lt;OutSimpleCo&gt; = [ &#8216;N-inversion&#8217; 4 3 2 1 ]<br />
  )<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;EFCOpt&gt;: (<br />
    transition_state = yes<br />
    mode_following = yes<br />
    max_iterations = 20<br />
    function = $..:mole<br />
    update&lt;PowellUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Transition State Optimization with a Computed Guess Hessian</h3>
<p> This example shows a transition state optimization of the N-inversion in $mathrm{CH}_3mathrm{NH}_2$ using mode following. The initial geometry was obtained by doing a few fixed coordinate optimizations along the inversion coordinate. An approximate guess Hessian will be computed, which makes the optimiziation converge much faster in this case. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = CS<br />
  { atoms geometry } = {<br />
    H [  3.045436 -0.697438 -1.596748 ]<br />
    H [  3.045436 -0.697438  1.596748 ]<br />
    N [  2.098157 -0.482779 -0.000000 ]<br />
    C [ -0.582616 -0.151798  0.000000 ]<br />
    H [ -1.171620  1.822306  0.000000 ]<br />
    H [ -1.417337 -1.042238 -1.647529 ]<br />
    H [ -1.417337 -1.042238  1.647529 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;3-21G*&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % molecular coordinates for optimization<br />
  coor&lt;SymmMolecularCoor&gt;: (<br />
    molecule = $:molecule<br />
    generator&lt;IntCoorGen&gt;: (<br />
      molecule = $:molecule<br />
    )<br />
    followed&lt;OutSimpleCo&gt; = [ &#8216;N-inversion&#8217; 4 3 2 1 ]<br />
  )<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    coor = $..:coor<br />
    memory = 16000000<br />
    guess_hessian&lt;FinDispMolecularHessian&gt;: (<br />
      molecule = $:molecule<br />
      only_totally_symmetric = yes<br />
      eliminate_cubic_terms = no<br />
      checkpoint = no<br />
      energy&lt;CLHF&gt;: (<br />
        molecule = $:molecule<br />
        memory = 16000000<br />
        basis&lt;GaussianBasisSet&gt;: (<br />
          name = &#8216;3-21G&#8217;<br />
          molecule = $:molecule<br />
        )<br />
      )<br />
    )<br />
  )<br />
  % optimizer object for the molecular geometry<br />
  opt&lt;EFCOpt&gt;: (<br />
    transition_state = yes<br />
    mode_following = yes<br />
    max_iterations = 20<br />
    function = $..:mole<br />
    update&lt;PowellUpdate&gt;: ()<br />
    convergence&lt;MolEnergyConvergence&gt;: (<br />
      cartesian = yes<br />
      energy = $..:..:mole<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<h3>Hartree-Fock energy with intermediate checkpointing</h3>
<p> The following two sections demonstrate how MPQC can be used to save the mole object periodically. This input will compute the Hartree-Fock energy of water while saving the mole object every 3 iterations. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = yes<br />
  filename = &#8216;h2o-rhf-STO3G&#8217;<br />
  checkpoint_freq = 3<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<p> The mole object will be saved to files named &#8216;h2o-rhf-STO3G.wfn.&lt;iter#&gt;.tmp&#8217; where &lt;iter#&gt; is the SCF iteration number (3, 6, etc.). Only the most recent file is kept, files from previous iterations are removed automatically. Keyword filename here is used to set the default file name prefix.</p>
<h3>MP2-R12 energy with intermediate checkpointing</h3>
<p> The following input will compute the MP2-R12 energy of water in standard approximation A&#8217; (MP2-R12/A&#8217;) while saving the mole object at intermediate checkpoints. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;cc-pVDZ&#8217;<br />
  molecule = $:molecule<br />
)<br />
% auxiliary basis set specification<br />
abasis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;aug-cc-pVDZ&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = yes<br />
  filename = &#8216;h2o-mp2r12ap-vdz-avdz&#8217;<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;MBPT2_R12&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    aux_basis = $:abasis<br />
    stdapprox = &#8216;A&#8221;<br />
    nfzc = 1<br />
    memory = 16000000<br />
    integrals&lt;IntegralCints&gt;:()<br />
    % reference wavefunction<br />
    reference&lt;CLHF&gt;: (<br />
      molecule = $:molecule<br />
      basis = $:basis<br />
      memory = 16000000<br />
      integrals&lt;IntegralCints&gt;:()<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<p> The mole object will be saved to a file named h2o-mp2r12ap-vdz-avdz.wfn. Keyword filename here is used to set the default file name prefix. Objects of the MBPT2_R12 type are checkpointed after the HF procedure, after the first integrals (SBS) transformation, and after the optional second (ABS) transformation.</p>
<h3>HF gradient computed from a previously computed HF wave funtion</h3>
<p> The following will illustrate how to reuse previously computed MolecularEnergy objects in subsequent computations. The first input computes Hartree-Fock energy for water and saves the mole object to file h2o-rhf-sto3g.wfn. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = yes<br />
  filename = &#8216;h2o-rhf-sto3g&#8217;<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<p> The second input reuses the mole object from the previous run to compute the gradient of the Hartree-Fock energy. </p>
<pre>
% emacs should use -*- KeyVal -*- mode
mpqc: (
  checkpoint = no
  savestate = no
  restart = yes
  restart_file = 'h2o-rhf-sto3g.wfn'
  do_gradient = yes
)
</pre>
<p>&nbsp;<wbr> </p>
<h3>MP2 Energy computed using precomputed Hartree-Fock wave function</h3>
<p> The following input will compute the MP2 energy of water using a saved Hartree-Fock wave function obtained using the first input from <code>HF gradient computed from a previously computed HF wave funtion</code>. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
% wave function file object specification<br />
wfnfile&lt;BcastStateInBin&gt;:file = &#8216;h2o-rhf-sto3g.wfn&#8217;<br />
mpqc: (<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;MBPT2&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    memory = 16000000<br />
    % reference wavefunction<br />
    reference&lt;SavableStateProxy&gt;: (<br />
      statein = $:wfnfile<br />
      object = &#8216;CLHF&#8217;<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<p> Note that now object reference is of type SavableStateProxy, rather than CLHF. SavableStateProxy is a special object type that can be converted at runtime into the desired type (in this case, CLHF, as indicated by object).</p>
<h3>CLHF energy using a CCA integrals component</h3>
<p> The following input will compute the CLHF energy of water using a CCA integrals component via the IntegralCCA adaptor class. </p>
<p>% emacs should use -*- KeyVal -*- mode<br />
% molecule specification<br />
molecule&lt;Molecule&gt;: (<br />
  symmetry = C2V<br />
  unit = angstrom<br />
  { atoms geometry } = {<br />
    O     [     0.00000000     0.00000000     0.37000000 ]<br />
    H     [     0.78000000     0.00000000    -0.18000000 ]<br />
    H     [    -0.78000000     0.00000000    -0.18000000 ]<br />
  }<br />
)<br />
% basis set specification<br />
basis&lt;GaussianBasisSet&gt;: (<br />
  name = &#8216;STO-3G&#8217;<br />
  molecule = $:molecule<br />
)<br />
mpqc: (<br />
  % path to component libraries<br />
  cca_path = /usr/local/lib/cca<br />
  % sidl class names of components which will be instantiated<br />
  cca_load = MPQC.IntegralEvaluatorFactory<br />
  do_cca = yes<br />
  checkpoint = no<br />
  savestate = no<br />
  % method for computing the molecule&#8217;s energy<br />
  mole&lt;CLHF&gt;: (<br />
    molecule = $:molecule<br />
    basis = $:basis<br />
    % cca integrals adaptor class<br />
    integrals&lt;IntegralCCA&gt;: (<br />
      molecule = $:molecule<br />
      % integral buffer type<br />
      integral_buffer = opaque<br />
      % integral package<br />
      integral_package = intv3<br />
      % factory component sidl class name<br />
      evaluator_factory = MPQC.IntegralEvaluatorFactory<br />
    )<br />
  )<br />
)</p>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr></p>
<h2>Validating MPQC</h2>
<p> After you compile MPQC, you should run the validation suite. You should also run the validation suite if you upgrade your operating system software, since this could change shared libraries that are linking with MPQC and could affect the results. Note that the reference validation suite has not been verified relative to an independent code, except for a few spot checks. If you find that MPQC doesn&#8217;t produce the same answer as another quantum chemistry program that you trust, then please promptly notify us and send all the details. </p>
<p> The top-level Makefile has several targets that can be used to check an MPQC build. MPQC must be built before one of these targets is used:</p>
<dl>
<dt>check</p>
<dd> The same as check0 below. This is only available from the top-level directory and src/bin/mpqc/validate.</p>
<dt>check0</p>
<dd> Run the smallest MPQC verification suite. It tests basic functionality. This is only available from the top-level directory and src/bin/mpqc/validate.</p>
<dt>check1</p>
<dd> Run the intermediate MPQC verification suite. It runs most of the tests, only leaving out very expensive runs. This is only available from the top-level directory and src/bin/mpqc/validate.</p>
<dt>check2</p>
<dd> Run the complete MPQC verification suite. Depending on the compilation and runtime environment, tests that are not expected to work will be omitted. This is only available from the top-level directory and src/bin/mpqc/validate.</p>
<dt>check_clean</p>
<dd> Remove MPQC verification suite output files. This is only available from the top-level directory and src/bin/mpqc/validate.</p>
<dt>testbuild</p>
<dd> Verify that a variety of small test programs compile. If static libraries are used, this will require a substantial amount of disk space.</p>
<dt>testrun</p>
<dd> Run a variety of small test programs. This will build them if necessary.</dl>
<p> The check targets will run mpqc with the mpqcrun (see <code>mpqcrun</code>) command. You can give arguments to mpqcrun by setting the MPQCRUN_ARGS variable on the make command line. </p>
<p> The verification suite is in src/bin/mpqc/validate. After running it, the output files can be found in src/bin/mpqc/validate/run. The check targets will compare outputs that your build produced to the reference files in src/bin/mpqc/validate/ref. The input files can be found with the reference files. For each comparison, first the status (ok, missing, or failed) for each file is printed. If both statuses are ok then an E: is printed followed by the number of digits to which the energies agree. If they agree to all digits 99 is printed. If a gradient was computed, then Grad: is printed followed by the number of digits to which the gradients in least agreement agree. Other properties checked in this way include frequencies, diagnostics, and populations. </p>
<p> If two numbers do not agree to the expected accuracy, then an asterisk, *, is printed after the number of digits in agreement. </p>
<p> Finally, you can do a detailed comparison of the contents of the ref and run subdirectories by typing make diff. </p>
<p> The input files in the verification suite are divided into several categories:</p>
<dl>
<dt>h2o</p>
<dd> These are simple tests that exercise many of MPQC&#8217;s features.</dl>
<dl>
<dt>h2omp2</p>
<dd> Tests that further exercise MP2.</dl>
<dl>
<dt>h2ofrq</p>
<dd> Tests of H2 O frequencies with a variety of methods.</dl>
<dl>
<dt>mbpt</p>
<dd> These tests exercise MP2 as well as the open-shell perturbation theory methods. The various available algorithms are tested as well.</dl>
<dl>
<dt>ckpt</p>
<dd> Tests the checkpoint and restart capabilities.</dl>
<dl>
<dt>symm1</p>
<dd> Tests of point group symmetry.</dl>
<dl>
<dt>symm2</p>
<dd> More point group symmetry tests. These use basis sets with higher angular momentum than symm1#.</dl>
<dl>
<dt>symm3</p>
<dd> Tests automatic point group determination.</dl>
<dl>
<dt>basis1</p>
<dd> A variety of basis sets are tested for first row atoms along with hydrogen and helium.</dl>
<dl>
<dt>basis2</p>
<dd> Basis sets test for second row atoms.</dl>
<dl>
<dt>methods</p>
<dd> Basic tests of several of MPQC&#8217;s methods.</dl>
<dl>
<dt>clscf</p>
<dd> More tests of methods based on CLSCF.</dl>
<dl>
<dt>hsosscf</p>
<dd> More tests of methods based on HSOSSCF.</dl>
<dl>
<dt>uscf</p>
<dd> More tests of methods based on UnrestrictedSCF.</dl>
<dl>
<dt>dft</p>
<dd> More tests of the CLKS method.</dl>
<dl>
<dt>mp2r12</p>
<dd> More tests of MP2-R12.</dl>
<dl>
<dt>ccaintv3</p>
<dd> Tests of embedded CCA integrals components using intv3.</dl>
<dl>
<dt>ccacints</p>
<dd> Tests of embedded CCA integrals components using cints.</dl>
<h2>Running Psi 3 from MPQC</h2>
<p> Psi 3 is a suite of <i>ab initio</i> codes related to the original Psi package started in Prof. Fritz Schaefer&#8217;s group at UC Berkeley. Current version of MPQC works with stable versions of Psi 3 starting with 3.2.0. From now on we will refer to Psi 3 as simply Psi. Psi is written primarily in C and executes in serial mode only. The interface between Psi and MPQC is intended mainly for Psi users who wish to exploit MPQC&#8217;s geometry optimization and frequency analyses capabilities with Psi energies and gradients. </p>
<p> The following sections explain how to use Psi from MPQC: </p>
<dl>
<dt>o</p>
<dd> <code>How the MPQC-Psi interface works</code></p>
<dt>o</p>
<dd> <code>Environmental Variables</code></p>
<dt>o</p>
<dd> <code>Preparing an input file</code></p>
<dt>o</p>
<dd> <code>Psi Execution Environment</code></p>
<dt>o</p>
<dd> <code>PsiWavefunction specializations</code></p>
<dt>o</p>
<dd> <code>More examples</code></dl>
<h3>How the MPQC-Psi interface works</h3>
<p> The current version of the interface is rather slim. It is only possible to import energies and gradients computed with Psi into MPQC, i.e. wave functions cannot be imported. All MPQC-Psi interaction happens via text files and system calls. MPQC generates input file for Psi, calls appropriate Psi modules, and then parses the output files for energies and gradients.</p>
<h3>Environmental Variables</h3>
<p> Several environmental variables are used to control MPQC-Psi interaction:</p>
<dl>
<dt>PSIBIN</p>
<dd> By default, MPQC will try to find Psi binaries under /usr/local/psi/bin. Use PSIBIN environmental variable to point to the right location.</dl>
<p> The rest of the Psi environment is job specific and specified in the input file.</p>
<h3>Preparing an input file</h3>
<p> As noted above, MPQC parses the input file, and as such the input file has to be in the MPQC OO input format. All features of usual MPQC input files are there (mpqc section, mole MolecularEnergy object, etc.). In addition the following rules apply: </p>
<dl>
<dt>o</p>
<dd> instead of using MPQC Wavefunction objects (CLHF, MBPT2, etc.), the Psi specific Wavefunction types (i.e. specializations of PsiWavefunction) have to be used. Presently the following specializations are supported: PsiCLHF, PsiHSOSHF, PsiUHF, PsiCCSD, PsiCCSD_T . The first three are directly analogous to MPQC Wavefunction types CLHF, HSOSHF, and UHF. The latter two do not have MPQC analogs yet. See appropriate class documentation on how to specify them properly.</p>
<dt>o</p>
<dd> each Psi-specific Wavefunction object has to have a member object psienv of type PsiExEnv. PsiExEnv contains job specific information, such as the directory in which Psi input, output, and checkpoint files will be kept, filename prefix, scratch directories, etc. It makes sense to define one such object and simply refer to it from all PsiWavefunction objects. See PsiExEnv class documentation for more info.</dl>
<h3>Psi Execution Environment</h3>
<p> Each PsiWavefunction-derived class has to have a member object called psienv of type PsiExEnv. The following keywords are used by its KeyVal constructor:</p>
<dl>
<dt>cwd</p>
<dd> The directory where to keep Psi input, checkpoint, stdout, stderr, and other files. Default is /tmp.</p>
<dt>fileprefix</p>
<dd> The file prefix to use for Psi checkpoint, scratch, and some ASCII files. Equivalent to keyword name in Psi psi:files:default section. Defaults to psi.</p>
<dt>stdout</p>
<dd> The file into which to redirect standard output of Psi modules. Defaults to psi.stdout.</p>
<dt>stderr</p>
<dd> The file into which to redirect standard error of Psi modules. Defaults to psi.stderr.</p>
<dt>nscratch</p>
<dd> The number of locations over which to stripe Psi binary files. Equivalent to keyword nvolume in Psi psi:files:default section. Default is 1.</p>
<dt>scratch</p>
<dd> The locations over which to stripe Psi binary files. Equivalent to keyword volume<i>x</i> in Psi psi:files:default section. There&#8217;s no default.</dl>
<p> Here&#8217;s an example: </p>
<pre>
  psienv&lt;PsiExEnv&gt;: (
    cwd = ./
    fileprefix = psi.test
    nscratch = 2
    scratch = [ '/scratch1/' '/scratch2/' ]
  )
</pre>
<p>&nbsp;<wbr> </p>
<h3>PsiWavefunction specializations</h3>
<p> Class PsiWavefunction is derived from class Wavefunction, hence its KeyVal constructor uses all keywords that Wavefunction&#8217;s KeyVal constructor uses (basis, molecule, etc.). In addition, PsiWavefunction&#8217;s KeyVal constructor looks for the following keywords in the input file:</p>
<dl>
<dt>psienv</p>
<dd> The PsiExEnv object that provides job specific Psi environment. There&#8217;s no default.</p>
<dt>docc</p>
<dd> An optional array of integers that specifies the number of doubly-occupied orbitals in each irrep.</p>
<dt>socc</p>
<dd> An optional array of integers that specifies the number of singly-occupied orbitals in each irrep.</p>
<dt>frozen_docc</p>
<dd> An optional array of integers that specifies the number of doubly-occupied orbitals in each irrep frozen in correlated computations.</p>
<dt>frozen_uocc</p>
<dd> An optional array of integers that specifies the number of unoccupied orbitals in each irrep frozen in correlated computations.</p>
<dt>total_charge</p>
<dd> The total charge of the system. This keyword is queried only if neither docc nor socc are given.</p>
<dt>multiplicity</p>
<dd> The spin multiplicity of the system (2*M_S+1). This keyword is queried only if neither docc nor socc are given.</p>
<dt>memory</p>
<dd> The number of bytes of memory Psi modules associated with this PsiWavefunction are allowed to use. Default is 2000000 (2 million bytes, approximately 2 MB).</dl>
<p> Note that keywords docc, socc, frozen_docc, frozen_uocc, total_charge, and multiplicity are used by appropriate specializations of PsiWavefunctions, i.e. PsiCLHF only checks for docc, etc. </p>
<p> PsiWavefunction specializations PsiCCSD and PsiCCSD_T also look for keyword reference which specifies the reference wave function (an object of type PsiSCF). All classes for correlated Psi wave functions will require such an object. </p>
<p> Here are a few examples of PsiWavefunctions: </p>
<p>  %<br />
  % ROHF DZ on F atom<br />
  %<br />
  mole&lt;PsiHSOSHF&gt;: (<br />
    docc = [ 2 0 0 0 0 1 1 0 ] socc = [ 0 0 0 0 0 0 0 1]<br />
    memory = 10000000</p>
<pre>
    % Psi Environment data
    psienv&lt;PsiExEnv&gt;: (
      cwd = ./
      fileprefix = f.dz.test
      stdout = f.dz.test.stdout
      stderr = f.dz.test.stderr
      nscratch = 1
      scratch = [ '/scratch/mpqc/' ]
    )
</pre>
<p>% MolecularEnergy input<br />
        molecule&lt;Molecule&gt; : (<br />
                                 {atoms geometry} = {<br />
                                     F[0.0 0.0 0.0]})</p>
<pre>
    % Basis input
    basis&lt;GaussianBasisSet&gt;: (
        molecule = $..:molecule
        name = 'DZ (Dunning)'
      )
</pre>
<pre>
  )
</pre>
<p>&nbsp;<wbr> </p>
<pre>
  %
  % RHF CCSD/cc-pVDZ on water
  %
  mole&lt;PsiCCSD&gt;: (
    frozen_docc = [1 0 0 0]
    memory = 40000000
</pre>
<pre>
    % Psi Environment data
    psienv&lt;PsiExEnv&gt;: (
      cwd = ./
      fileprefix = h2o.ccpvdz.ccsd.test
      nscratch = 1
      scratch = [ '/tmp/' ]
    )
</pre>
<p>% MolecularEnergy input<br />
        molecule&lt;Molecule&gt; : (<br />
                                 {atoms geometry} = {<br />
                                     H[-1.5 0.0 &#8211; 0.3] H[1.5 0.0 &#8211; 0.3] O[0.0 0.0 1.0]})</p>
<pre>
    % Basis input
    basis&lt;GaussianBasisSet&gt;: (
        molecule = $..:molecule
        name = 'cc-pVDZ'
      )
</pre>
<pre>
    reference&lt;PsiCLHF&gt;: (
      psienv = $..:psienv
      molecule = $..:molecule
      basis = $..:basis
      total_charge = 0
      multiplicity = 1
    )
  )
</pre>
<p>&nbsp;<wbr> </p>
<h3>More examples</h3>
<p> This section contains some examples of complete inputs that specify an MPQC/Psi computations. </p>
<p> Here&#8217;s an optimization + subsequent frequency analysis on water molecule at the RHF CCSD 6-311G** level: </p>
<pre><code>
% Emacs should use - *-KeyVal - *-mode % this file was automatically generated % label : water test series % molecule specification molecule&lt;Molecule&gt; : (symmetry = C2V unit = angstrom{atoms geometry} = {O[0.000000000000 0.000000000000 0.369372944000] H[0.783975899000 0.000000000000 - 0.184686472000] H[-0.783975899000 0.000000000000 - 0.184686472000]}) % basis set specification basis&lt;GaussianBasisSet&gt; : (name = '6-311G**' molecule = $
                                                                                                                                                                                                                                                                                                                                                                                                                        : molecule) %
                                                                                                                                                                                                                                                                                                                                                                                                                       Psi environment specification psienv&lt;PsiExEnv&gt; : (cwd =./ fileprefix = mpqcpsi stdout = mpqcpsi.stdout stderr = mpqcpsi.stderr nscratch = 1 scratch = ['/scratch/evaleev/'])
</code></pre>
<pre>
mpqc: (
  checkpoint = no
  savestate = no
  restart = no
  coor&lt;SymmMolecularCoor&gt;: (
    molecule = $:molecule
    generator&lt;IntCoorGen&gt;: (
      molecule = $:molecule
    )
  )
  % molecular coordinates for optimization  do_energy = yes
  do_gradient = no
  % method for computing the molecule's energy
  mole&lt;PsiCCSD&gt;: (
    molecule = $:molecule
    basis = $:basis
    coor = $..:coor
    psienv = $:psienv
    memory = 32000000
    reference&lt;PsiCLHF&gt;: (
      psienv = $:psienv
      molecule = $:molecule
      total_charge = 0
      multiplicity = 1
      basis = $:basis
      memory = 32000000
    )
    hessian&lt;FinDispMolecularHessian&gt;: (
      point_group&lt;PointGroup&gt;: symmetry = C2V
      checkpoint = no
      restart = no
    )
  )
  optimize = yes
  % optimizer object for the molecular geometry
  opt&lt;QNewtonOpt&gt;: (
    max_iterations = 20
    function = $..:mole
    update&lt;BFGSUpdate&gt;: ()
    convergence&lt;MolEnergyConvergence&gt;: (
      cartesian = yes
      energy = $..:..:mole
    )
  )
% vibrational frequency input
  freq&lt;MolecularFrequencies&gt;: (
    point_group&lt;PointGroup&gt;: symmetry = C2V
    molecule = $:molecule
  )
)
</pre>
<p>&nbsp;<wbr> </p>
<h2>CCA Components</h2>
<p> Common Component Architecture (CCA) component wrappers, conforming to interfaces developed for the CCA Chemistry Component Toolkit, have been created to encapsulate some MPQC functionality. The following components are provided by MPQC: </p>
<dl>
<dt>o</p>
<dd> <code>MPQC.Chemistry_QC_ModelFactory</code></p>
<dt>o</p>
<dd> <code>MPQC.ChemistryOpt_CoordinateModel</code></p>
<dt>o</p>
<dd> <code>MPQC.IntegralEvaluatorFactory</code></dl>
<h3>MPQC.Chemistry_QC_ModelFactory</h3>
<p> This is an implementation of the Chemistry.QC.ModelFactory interface. This factory produces model objects (implementing the Chemistry.QC.Model interface) based on the MPQC package. The MPQC model allows calculation of molecular energies and energy derivatives using a variety of methods.</p>
<h3>Provides Ports</h3>
<dl>
<dt>o</p>
<dd> Chemistry.QC.ModelFactory <i>ModelFactory</i></dl>
<h3>Uses Ports</h3>
<dl>
<dt>o</p>
<dd> Chemistry.QC.MoleculeFactory <i>MoleculeFactory</i> (required)</dl>
<h3>Parameters</h3>
<dl>
<dt>o</p>
<dd> <code>theory</code> The method for determining the electronic structure. Defaults to HF. </p>
<dt> o</p>
<dd> <i>HF</i> Hartree-Fock method.</p>
<dt> o</p>
<dd> <i>B3LYP</i> Density Functional Theory (DFT) with B3LYP functional.</p>
<dt> o</p>
<dd> Use keyval input for other options.</dl>
<dl>
<dt>o</p>
<dd> <code>basis</code> The atomic orbital basis set. Defaults to <i>STO-3G</i>. </p>
<dt> o</p>
<dd> Any basis set defined in the MPQC package.</p>
<dt> o</p>
<dd> Use keyval input for mixed basis sets.</dl>
<dl>
<dt>o</p>
<dd> <code>molecule_filename</code> Path to the molecule file (see cca-chem-generic documentation for format). No default &#8212; required.</p>
<dt>o</p>
<dd> <code>keyval_filename</code> Path to the keyval input file (see below). No default &#8212; optional.</dl>
<h3>Keyval Input</h3>
<p> The <code>theory</code> and <code>basis</code> parameters allow very basic calculations to be performed. More complex calculations will require the use of a keyval input file. The keyval file format is the same as that used to run MPQC stand-alone, and any valid MPQC options may be used. The molecular energy object must be named model. The user-supplied keyval cannot contain a molecule section; the molecule section will be automatically inserted by the ModelFactory using the required <code>molecule_filename</code>. This molecule section should be referred to as $:molecule. </p>
<p> Example keyval input: </p>
<pre>
  model&lt;CLHF&gt;:(
    molecule=$:molecule
    basis&lt;GaussianBasisSet&gt;:(
      name = '6-31G'
      molecule = $:molecule
    )
  )
</pre>
<h3>MPQC.ChemistryOpt_CoordinateModel</h3>
<p> This is an implementation of the ChemistryOpt.CoordinateModel interface based on the MPQC package. It supports molecular structure optimization in cartesian, symmetrized internal, and redundant internal coordinates. Hessian approximation is supported.</p>
<h3>Provides Ports</h3>
<dl>
<dt>o</p>
<dd> ChemistryOpt.CoordinateModel <i>CoordinateModel</i></dl>
<h3>Uses Ports</h3>
<dl>
<dt>o</p>
<dd> Chemistry.QC.ModelFactory <i>ModelFactory</i> (required)</p>
<dt>o</p>
<dd> Chemistry.QC.ModelFactory <i>BackupModelFactory</i> (optional)</p>
<dt>o</p>
<dd> Chemistry.MoleculeViewer <i>MoleculeViewer</i> (optional)</dl>
<p> A backup model factory may be supplied. If an error is detected in the primary model, then a model obtained from the backup factory will be used. The molecule viewer is currently only used to communicate with the python viewer, in which case component instantiation and connection is handled automatically.</p>
<h3>Parameters</h3>
<dl>
<dt>o</p>
<dd> <code>grad_rms</code> RMS gradient convergence criteria. Defaults to 0.00030.</p>
<dt>o</p>
<dd> <code>grad_max</code> Max gradient convergence criteria. Defaults to 0.00045.</p>
<dt>o</p>
<dd> <code>disp_rms</code> RMS displacement convergence criteria. Defaults to 0.00120.</p>
<dt>o</p>
<dd> <code>disp_max</code> Max displacement convergence criteria. Defaults to 0.00180.</p>
<dt>o</p>
<dd> <code>coordinate_type</code> Optimization coordinate type. Defaults to <i>symmetrized</i>. </p>
<dt> o</p>
<dd> <i>cartesian</i> Cartesian coordinates.</p>
<dt> o</p>
<dd> <i>symmetrized</i> Symmetrized internal coordinates.</p>
<dt> o</p>
<dd> <i>redundant</i> Redundant internal coordinates.</dl>
<dl>
<dt>o</p>
<dd> <code>multiple_guess_h</code> Compute new guess Hessian at each call to guess_hessian_solve() (<i>true</i>) or use guess from first iteration only (<i>false</i>). Only meaningful in conjunction with solvers supporting use of dense guess Hessians with limited-memory methods. Defaults to <i>true</i>.</p>
<dt>o</p>
<dd> <code>use_current_geom</code> If <code>multiple_guess_h</code> is <i>true</i>, either use the current geometry (<i>true</i>) or the geometry at which the earliest correction pair used by the solver was determined (<i>false</i>) when computing the guess Hessian. Defaults to <i>false</i>.</dl>
<h3>MPQC.IntegralEvaluatorFactory</h3>
<p> This is an implementation of the Chemistry.QC.GaussianBasis.IntegralEvaluatorFactory interface. This factory produces molecular integral evaluator objects based on the MPQC package. This code is experimental and does not currently support derivative integrals.</p>
<h3>Provides Ports</h3>
<dl>
<dt>o</p>
<dd> Chemistry.QC.GaussianBasis.IntegralEvaluatorFactory <i>IntegralEvaluatorFactory</i></dl>
<h3>Parameters</h3>
<dl>
<dt>o</p>
<dd> <code>package</code> Integral package, either intv3 or cints. Defaults to intv3.</p>
<dt>o</p>
<dd> <code>integral_buffer</code> Integral buffer type, either opaque or array. The opaque option uses pointers and is therefore higher performance. The array option may be used by components implemented in languages which are not pointer-aware.</dl>
<p>&nbsp;<wbr></p>
<h2>MPQC License</h2>
<p> MPQC is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p>&nbsp;<wbr></p>
<h2>MPQC Warranty</h2>
<p> MPQC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
