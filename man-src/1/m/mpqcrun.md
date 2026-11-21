---
title: "mpqcrun(1)"
name: "mpqcrun"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpqcrun/"
description: "mpqcrun – The mpqcrun program simplifies running MPQC."
---

<h2>Synopsis</h2>
<pre><code>
mpqcrun[options][file1.in][file2.in]...
</code></pre>
<h2>Description</h2>
<p> The mpqcrun program simplifies the task of running MPQC on multiple input files. Although it was primarily designed to run the validation suite, mpqcrun, is general enough to be useful in other situations. If multiple nodes or processors are present, it can be used to manage multiple invocations of MPQC. </p>
<h2>Running mpqcrun</h2>
<p> mpqcrun takes the following command line options: </p>
<dl>
<dt>&#8211;mpqc path</dt>
<dd> The mpqc executable to use.</dd>
<dt>&#8211;objdir</dt>
<dd> Run the mpqc executable in the compile directory, rather than the install directory.</dd>
<dt>&#8211;small</dt>
<dd> Skip big runs in verification suite.</dd>
<dt>&#8211;nnodeperjob n</dt>
<dd> Run with n nodes per job. If this is nnode, use all available nodes.</dd>
<dt>&#8211;nprocpernode n</dt>
<dd> Run with n processes per node.</dd>
<dt>&#8211;nprocperjob n</dt>
<dd> Run with n processes per job. The default is to use all available processors.</dd>
<dt>&#8211;nthreadperproc n</dt>
<dd> Use n threads per process.</dd>
<dt>&#8211;threadgrp grp</dt>
<dd> Use the given threading layer.</dd>
<dt><code>grp=</code>none</dt>
<dd> Use MPQC&#8217;s default.</dd>
<dt><code>grp=</code>proc</dt>
<dd> Do a single threaded run.</dd>
<dt><code>grp=</code>posix</dt>
<dd> Use POSIX threads.</dd></dl>
<dl>
<dt>&#8211;messagegrp grp</dt>
<dd> Use the given communication layer.</dd>
<dt><code>grp=</code>none</dt>
<dd> Use MPQC&#8217;s default.</dd>
<dt><code>grp=</code>proc</dt>
<dd> Does a single processor run.</dd>
<dt><code>grp=</code>mpi</dt>
<dd> Use MPI.</dd></dl>
<dl>
<dt>&#8211;memorygrp grp</dt>
<dd> Use the given remote memory communication layer.</dd>
<dt><code>grp=</code>none</dt>
<dd> Use MPQC&#8217;s default.</dd>
<dt><code>grp=</code>proc</dt>
<dd> Does a single processor run.</dd>
<dt><code>grp=</code>mtmpi</dt>
<dd> Use multi-threaded MPI.</dd>
<dt><code>grp=</code>armci</dt>
<dd> Use ARMCI.</dd></dl>
<dl>
<dt>&#8211;launch cmd</dt>
<dd> Use the given command to launch jobs. See below.</dd>
<dt>&#8211;nodefile file</dt>
<dd> Specifies a file listing nodes to use. Duplicated nodes are removed.</dd>
<dt>&#8211;nodes nodes</dt>
<dd> Specifies list of machines to use. A range of nodes can be given with two integers separated by a dash. Groups of nodes can be separated by a comma.</dd>
<dt>&#8211;nodename fmt</dt>
<dd> This is a format string that converts the node number to its name.</dd>
<dt>&#8211;seq regex</dt>
<dd> Run inputs matching reqex sequentially. This is useful when one input requires that another be run first, and more than one job is run at a time.</dd>
<dt>&#8211;exclude regex</dt>
<dd> Exclude files matching regex.</dd>
<dt>&#8211;readdir dir</dt>
<dd> Run mpqc on all files matching dir/*.in.</dd>
<dt>&#8211;inputprefix prefix</dt>
<dd> Prepend prefix to all input file names.</dd>
<dt>&#8211;outputprefix prefix</dt>
<dd> Prepend prefix to all output file names.</dd>
<dt>&#8211;count</dt>
<dd> Print the number of input files that would be run.</dd>
<dt>&#8211;printfiles</dt>
<dd> Print the list of input files that would be run.</dd>
<dt>&#8211;rerun</dt>
<dd> Overwrite output file, even if up-to-date.</dd>
<dt>&#8211;onlynew</dt>
<dd> Do not overwrite output file, even if not up-to-date.</dd>
<dt>&#8211;simpout</dt>
<dd> Do not append extra info like nnode to filename.</dd>
<dt>&#8211;uniqout</dt>
<dd> Generate unique output filenames.</dd>
<dt>&#8211;autoout</dt>
<dd> Generate output filenames by replacing the suffix with &#8216;out&#8217;.</dd>
<dt>&#8211;verbose</dt>
<dd> Print out what action is to be taken on each file.</dd>
<dt>&#8211;debug</dt>
<dd> Don&#8217;t actually run mpqc.</dd>
<dt>&#8211;help</dt>
<dd> Print the documentation.</dd></dl>
<p> The cmd given with the &#8211;launch option can contain special strings that will be substituted:</p>
<dl>
<dt>%MPQC%</dt>
<dd> The MPQC program to run.</dd>
<dt>%INPUT%</dt>
<dd> The input filename.</dd>
<dt>%OUTPUT%</dt>
<dd> The output filename.</dd>
<dt>%NPROC%</dt>
<dd> The number of processes to start.</dd>
<dt>%NODEFILE%</dt>
<dd> The name of a file containing the node names.</dd>
<dt>%NODELIST%</dt>
<dd> A comma separated list of node names.</dd></dl>
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
