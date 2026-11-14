---
title: "mpqcrun(1)"
name: "mpqcrun"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpqcrun/"
description: "mpqcrun – The mpqcrun program simplifies running MPQC."
---

<h2 class="name">NAME</h2>
<p> mpqcrun &#8211; The mpqcrun program simplifies running MPQC.</p>
<h2>Synopsis</h2>
<pre><code>
mpqcrun[options][file1.in][file2.in]...
</code></pre>
<h2>Description</h2>
<p> The mpqcrun program simplifies the task of running MPQC on multiple input files. Although it was primarily designed to run the validation suite, mpqcrun, is general enough to be useful in other situations. If multiple nodes or processors are present, it can be used to manage multiple invocations of MPQC. </p>
<h2>Running mpqcrun</h2>
<p> mpqcrun takes the following command line options: </p>
<dl>
<dt>&#8211;mpqc path</p>
<dd> The mpqc executable to use.</p>
<dt>&#8211;objdir</p>
<dd> Run the mpqc executable in the compile directory, rather than the install directory.</p>
<dt>&#8211;small</p>
<dd> Skip big runs in verification suite.</p>
<dt>&#8211;nnodeperjob n</p>
<dd> Run with n nodes per job. If this is nnode, use all available nodes.</p>
<dt>&#8211;nprocpernode n</p>
<dd> Run with n processes per node.</p>
<dt>&#8211;nprocperjob n</p>
<dd> Run with n processes per job. The default is to use all available processors.</p>
<dt>&#8211;nthreadperproc n</p>
<dd> Use n threads per process.</p>
<dt>&#8211;threadgrp grp</p>
<dd> Use the given threading layer.</p>
<dt><code>grp=</code>none</p>
<dd> Use MPQC&#8217;s default.</p>
<dt><code>grp=</code>proc</p>
<dd> Do a single threaded run.</p>
<dt><code>grp=</code>posix</p>
<dd> Use POSIX threads.</dl>
<dl>
<dt>&#8211;messagegrp grp</p>
<dd> Use the given communication layer.</p>
<dt><code>grp=</code>none</p>
<dd> Use MPQC&#8217;s default.</p>
<dt><code>grp=</code>proc</p>
<dd> Does a single processor run.</p>
<dt><code>grp=</code>mpi</p>
<dd> Use MPI.</dl>
<dl>
<dt>&#8211;memorygrp grp</p>
<dd> Use the given remote memory communication layer.</p>
<dt><code>grp=</code>none</p>
<dd> Use MPQC&#8217;s default.</p>
<dt><code>grp=</code>proc</p>
<dd> Does a single processor run.</p>
<dt><code>grp=</code>mtmpi</p>
<dd> Use multi-threaded MPI.</p>
<dt><code>grp=</code>armci</p>
<dd> Use ARMCI.</dl>
<dl>
<dt>&#8211;launch cmd</p>
<dd> Use the given command to launch jobs. See below.</p>
<dt>&#8211;nodefile file</p>
<dd> Specifies a file listing nodes to use. Duplicated nodes are removed.</p>
<dt>&#8211;nodes nodes</p>
<dd> Specifies list of machines to use. A range of nodes can be given with two integers separated by a dash. Groups of nodes can be separated by a comma.</p>
<dt>&#8211;nodename fmt</p>
<dd> This is a format string that converts the node number to its name.</p>
<dt>&#8211;seq regex</p>
<dd> Run inputs matching reqex sequentially. This is useful when one input requires that another be run first, and more than one job is run at a time.</p>
<dt>&#8211;exclude regex</p>
<dd> Exclude files matching regex.</p>
<dt>&#8211;readdir dir</p>
<dd> Run mpqc on all files matching dir/*.in.</p>
<dt>&#8211;inputprefix prefix</p>
<dd> Prepend prefix to all input file names.</p>
<dt>&#8211;outputprefix prefix</p>
<dd> Prepend prefix to all output file names.</p>
<dt>&#8211;count</p>
<dd> Print the number of input files that would be run.</p>
<dt>&#8211;printfiles</p>
<dd> Print the list of input files that would be run.</p>
<dt>&#8211;rerun</p>
<dd> Overwrite output file, even if up-to-date.</p>
<dt>&#8211;onlynew</p>
<dd> Do not overwrite output file, even if not up-to-date.</p>
<dt>&#8211;simpout</p>
<dd> Do not append extra info like nnode to filename.</p>
<dt>&#8211;uniqout</p>
<dd> Generate unique output filenames.</p>
<dt>&#8211;autoout</p>
<dd> Generate output filenames by replacing the suffix with &#8216;out&#8217;.</p>
<dt>&#8211;verbose</p>
<dd> Print out what action is to be taken on each file.</p>
<dt>&#8211;debug</p>
<dd> Don&#8217;t actually run mpqc.</p>
<dt>&#8211;help</p>
<dd> Print the documentation.</dl>
<p> The cmd given with the &#8211;launch option can contain special strings that will be substituted:</p>
<dl>
<dt>%MPQC%</p>
<dd> The MPQC program to run.</p>
<dt>%INPUT%</p>
<dd> The input filename.</p>
<dt>%OUTPUT%</p>
<dd> The output filename.</p>
<dt>%NPROC%</p>
<dd> The number of processes to start.</p>
<dt>%NODEFILE%</p>
<dd> The name of a file containing the node names.</p>
<dt>%NODELIST%</p>
<dd> A comma separated list of node names.</dl>
<p> For these last two, if they are contained within square brackets and a substitution is not available, then everything within the the brackets is removed. </p>
<p> This argument will launch MPI jobs giving mpirun a nodefile. </p>
<pre>
  --launch 'mpirun [-hf %NODEFILE%] -n %NPROC% %MPQC% -o %OUTPUT% %INPUT%'
</pre>
<p> This argument will launch MPI jobs giving mpirun list of hosts on the command line. </p>
<pre>
  --launch 'mpirun [-H %NODELIST%] -n %NPROC% %MPQC% -o %OUTPUT% %INPUT%'
</pre>
<h2>License</h2>
<p> mpqcrun is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Warranty</h2>
<p> mpqcrun is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
