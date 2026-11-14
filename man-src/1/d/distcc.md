---
title: "distcc(1)"
name: "distcc"
section: "1"
letter: "d"
url: "/docs/linux/man/1-distcc/"
description: "distcc – distributed C/C++/ObjC compiler with distcc-pump extensions"
---

<h2>NAME</h2>
<p> distcc &#8211; distributed C/C++/ObjC compiler with distcc-pump extensions</p>
<h2>SYNOPSIS</h2>
<p> <code>distcc </code> <i>&lt;compiler&gt; [COMPILER OPTIONS] </i> </p>
<p> <code>distcc</code> <i>[COMPILER OPTIONS]</i> </p>
<p> <code>&lt;compiler&gt;</code> <i>[COMPILER OPTIONS]</i> </p>
<p> <code>distcc</code> <i>[DISTCC OPTIONS]</i></p>
<h2>DESCRIPTION</h2>
<p> distcc distributes compilation of C code across several machines on a network. distcc should always generate the same results as a local compile, it is simple to install and use, and it is often much faster than a local compile. </p>
<p> This version incorporates plain distcc as well as an enhancement called pump mode or distcc-pump. </p>
<p> For each job, distcc in plain mode sends the complete preprocessed source code and compiler arguments across the network from the client to a compilation server. In pump mode, distcc sends the source code and recursively included header files (excluding those from the default system header directories), so that both preprocessing and compilation can take place on the compilation servers. This speeds up the delivery of compilations by up to an order of magnitude over plain distcc. </p>
<p> Compilation is driven by a client machine, which is typically the developer&#8217;s workstation or laptop. The distcc client runs on this machine, as does make, the preprocessor (if distcc&#8217;s pump mode is not used), the linker, and other stages of the build process. Any number of volunteer machines act as compilation servers and help the client to build the program, by running the <code><a href="/docs/linux/man/1-distccd/">distccd</a>(1) </code> daemon, C compiler and assembler as required. </p>
<p> distcc can run across either TCP sockets (on port 3632 by default), or through a tunnel command such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1). For TCP connections the volunteers must run the <a href="/docs/linux/man/1-distccd/">distccd</a>(1) daemon either directly or from inetd. For SSH connections distccd must be installed but should <code>not</code> be listening for connections. </p>
<p> TCP connections should only be used on secure networks because there is no user authentication or protection of source or object code. SSH connections are typically 25% slower because of processor overhead for encryption, although this can vary greatly depending on CPUs, network and the program being built. </p>
<p> distcc is intended to be used with GNU Make&#8217;s <code>-j </code> option, which runs several compiler processes concurrently. distcc spreads the jobs across both local and remote CPUs. Because distcc is able to distribute most of the work across the network, a higher concurrency level can be used than for local builds. As a rule of thumb, the <code>-j </code> value should be set to about twice the total number of available server CPUs but subject to client limitations. This setting allows for maximal interleaving of tasks being blocked waiting for disk or network IO. Note that distcc can also work with other build control tools, such as SCons, where similar concurrency settings must be adjusted. </p>
<p> The <code>-j</code> setting, especially for large values of <code>-j,</code> must take into account the CPU load on the client. Additional measures may be needed to curtail the client load. For example, concurrent linking should be severely curtailed using auxiliary locks. The effect of other build activity, such as Java compilation when building mixed code, should be considered. The <code>&#8211;localslots_cpp</code> parameter is by default set to 16. This limits the number of concurrent processes that do preprocessing in plain distcc (non-pump) mode. Therefore, larger <code>-j </code> values than 16 may be used without overloading a single-CPU client due to preprocessing. Such large values may speed up parts of the build that do not involve C compilations, but they may not be useful to distcc efficiency in plain mode. </p>
<p> In contrast, using pump mode and say 40 servers, a setting of <code>-j80</code> or larger may be appropriate even for single-CPU clients. </p>
<p> It is strongly recommended that you install the same compiler version on all machines participating in a build. Incompatible compilers may cause mysterious compile or link failures.</p>
<h2>QUICKSTART</h2>
<dl>
<dt>1</p>
<dd> For each machine, download distcc, unpack, and install.</p>
<dt>2</p>
<dd> On each of the servers, run <code>distccd &#8211;daemon</code> with <code>&#8211;allow</code> options to restrict access.</p>
<dt>3</p>
<dd> Put the names of the servers in your environment:</p>
<dl>
<dt>
<dd> $ export DISTCC_HOSTS=&#8217;localhost red green blue&#8217;</dl>
<dt>4</p>
<dd> Build!</p>
<dl>
<dt>
<dd> $ make -j8 CC=distcc</dl>
</dl>
<h2>QUICKSTART FOR DISTCC-PUMP MODE</h2>
<p> Proceed as above, but in Step 3, specify that the remote hosts are to carry the burden of preprocessing and that the files sent over the network should be compressed: </p>
<dl>
<dt>
<dd> $ export DISTCC_HOSTS=&#8217;&#8211;randomize localhost red,cpp,lzo green,cpp,lzo blue,cpp,lzo&#8217;</dl>
<p> The <code>&#8211;randomize</code> option enforces a uniform usage of compile servers. While you will get some benefit from distcc&#8217;s pump mode with only a few servers, you get increasing benefit with more server CPUs (up to the hundreds!). Wrap your build inside the pump command, here assuming 10 servers: </p>
<dl>
<dt>
<dd> $ pump make -j20 CC=distcc</dl>
<h2>QUICKSTART FOR DISTCC-GSSAPI MODE</h2>
<p> Proceed as per the <code>QUICKSTART</code> but in Step 3, specify that the remote hosts are to mutually authenticate with the client: </p>
<dl>
<dt>
<dd> $ export DISTCC_HOSTS=&#8217;&#8211;randomize localhost red,auth green,auth blue,auth&#8217;</dl>
<p> If distccd runs under a specific principal name then execute the following command prior to step 4: </p>
<dl>
<dt>
<dd> export DISTCC_PRINICIPAL=&lt;name&gt;</dl>
<h2>HOW PLAIN (NON-PUMP) DISTCC WORKS</h2>
<p> distcc only ever runs the compiler and assembler remotely. With plain distcc, the preprocessor must always run locally because it needs to access various header files on the local machine which may not be present, or may not be the same, on the volunteer. The linker similarly needs to examine libraries and object files, and so must run locally. </p>
<p> The compiler and assembler take only a single input file (the preprocessed source) and produce a single output (the object file). distcc ships these two files across the network and can therefore run the compiler/assembler remotely. </p>
<p> Fortunately, for most programs running the preprocessor is relatively cheap, and the linker is called relatively infrequent, so most of the work can be distributed. </p>
<p> distcc examines its command line to determine which of these phases are being invoked, and whether the job can be distributed. </p>
<h2>HOW DISTCC-PUMP MODE WORKS</h2>
<p> In pump mode, distcc runs the preprocessor remotely too. To do so, the preprocessor must have access to all the files that it would have accessed if had been running locally. In pump mode, therefore, distcc gathers all of the recursively included headers, except the ones that are default system headers, and sends them along with the source file to the compilation server. </p>
<p> In distcc-pump mode, the server unpacks the set of all source files in a temporary directory, which contains a directory tree that mirrors the part of the file system that is relevant to preprocessing, including symbolic links. </p>
<p> The compiler is then run from the path in the temporary directory that corresponds to the current working directory on the client. To find and transmit the many hundreds of files that are often part of a single compilation, pump mode uses an incremental include analysis algorithm. The include server is a Python program that implements this algorithm. The pump command starts the include server so that throughout the build it can answer include queries by distcc commands. </p>
<p> The include server uses static analysis of the macro language to deal with conditional compilation and computed includes. It uses the property that when a given header file has already been analyzed for includes, it is not necessary to do so again if all the include options (-I&#8217;s) are unchanged (along with other conditions). </p>
<p> For large builds, header files are included, on average, hundreds of times each. With distcc-pump mode each such file is analyzed only a few times, perhaps just once, instead of being preprocessed hundreds of times. Also, each source or header file is now compressed only once, because the include server memoizes the compressed files. As a result, the time used for preparing compilations may drop by up to an order of magnitude over the preprocessing of plain distcc. </p>
<p> Because distcc in pump mode is able to push out files up to about ten times faster, build speed may increase 3X or more for large builds compared to plain distcc mode. </p>
<h2>RESTRICTIONS FOR PUMP MODE</h2>
<p> Using pump mode requires both client and servers to use release 3.0 or later of distcc and distccd (respectively). </p>
<p> The incremental include analysis of distc-pump mode rests on the fundamental assumption that source and header files do not change during the build process. A few complex build systems, such as that for Linux kernel 2.6, do not quite satisfy this requirement. To overcome such issues, and other corner cases such as absolute filepaths in includes, see the <code><a href="/docs/linux/man/1-include_server/">include_server</a>(1)</code> man page. </p>
<p> Another important assumption is that the include configuration of all machines must be identical. Thus the headers under the default system path must be the same on all servers and all clients. If a standard GNU compiler installation is used, then this requirement applies to all libraries whose header files are installed under /usr/include or /usr/local/include/. Note that installing software packages often lead to additional headers files being placed in subdirectories of either. </p>
<p> If this assumption does not hold, then it is possible to break builds with distcc-pump mode, or worse, to get wrong results without warning. Presently this condition is not verified, and it is on our TODO list to address this issue. </p>
<p> An easy way to guarantee that the include configurations are identical is to use a cross-compiler that defines a default system search path restricted to directories of the compiler installation. </p>
<p> See the <code><a href="/docs/linux/man/1-include_server/">include_server</a></code>(1) manual for more information on symptoms and causes of violations of distcc-pump mode assumptions. </p>
<h2>HOW DISTCC-GSSAPI MODE WORKS</h2>
<p> In this mode distcc will use the GSS-API framework to access the currently configured security mechanism and perform mutual authentication with the daemon. </p>
<h2>OPTION SUMMARY</h2>
<p> Most options passed to distcc are interpreted as compiler options. The following options are understood by distcc itself. If any of these options are specified, distcc will not invoke the compiler. </p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Displays summary instructions.</dl>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Displays the distcc client version.</dl>
<dl>
<dt><code>&#8211;show-hosts</code></p>
<dd> Displays the host list that distcc would use. See the Host Specifications section.</dl>
<dl>
<dt><code>&#8211;scan-includes</code></p>
<dd> Displays the list of files that distcc would send to the remote machine, as computed by the include server. This is a conservative (over-)approximation of the files that would be read by the C compiler. This option only works in pump mode. See the &quot;How Distcc-pump Mode Works&quot; section for details on how this is computed.</p>
<dl>
<dt>
<dd>
<p> The list output by <code>distcc &#8211;scan-includes</code> will contain one entry per line. Each line contains a category followed by a path. The category is one of FILE, SYMLINK, DIRECTORY, or SYSTEMDIR:</p>
<dl>
<dt>
<dd> <code>FILE</code> indicates a source file or header file that would be sent to the distcc server host.</p>
<dt>
<dd> <code>SYMLINK</code> indicates a symbolic link that would be sent to the distcc server host.</p>
<dt>
<dd> <code>DIRECTORY</code> indicates a directory that may be needed in order to compile the source file. For example, a directory &quot;foo&quot; may be needed because of an include of the form #include &quot;foo/../bar.h&quot;. Such directories would be created on the distcc server host.</p>
<dt>
<dd> <code>SYSTEMDIR</code> indicates a system include directory, i.e. a directory which is on the compiler&#8217;s default include path, such as &quot;/usr/include&quot;; such directories are assumed to be present on the distcc server host, and so would not be sent to the distcc server host.</dl>
</dl>
<dt><code>-j</code></p>
<dd> Displays distcc&#8217;s concurrency level, as calculated from the host list; it is the maximum number of outstanding jobs issued by this client to all servers. By default this will be four times the number of hosts in the host list, unless the /LIMIT option was used in the host list. See the Host Specifications section.</dl>
<dl>
<dt><code>&#8211;show-principal</code></p>
<dd> Displays the name of the distccd security principal extracted from the environment. <code>This option is only available if distcc was compiled with</code> <code>the &#8211;with-auth configure option.</code> </p>
</dl>
<h2>INSTALLING DISTCC</h2>
<p> There are three different ways to call distcc, to suit different circumstances:</p>
<dl>
<dt>
<dd>
<p> distcc can be installed under the name of the real compiler, to intercept calls to it and run them remotely. This &quot;masqueraded&quot; compiler has the widest compatibility with existing source trees, and is convenient when you want to use distcc for all compilation. The fact that distcc is being used is transparent to the makefiles. </p>
<p> distcc can be prepended to compiler command lines, such as &quot;distcc cc -c hello.c&quot; or CC=&quot;distcc gcc&quot;. This is convenient when you want to use distcc for only some compilations or to try it out, but can cause trouble with some makefiles or versions of libtool that assume $CC does not contain a space. </p>
<p> Finally, distcc can be used directly as a compiler. &quot;cc&quot; is always used as the name of the real compiler in this &quot;implicit&quot; mode. This can be convenient for interactive use when &quot;explicit&quot; mode does not work but is not really recommended for new use.</dl>
<p> Remember that you should not use two methods for calling distcc at the same time. If you are using a masquerade directory, don&#8217;t change CC and/or CXX, just put the directory early on your PATH. If you&#8217;re not using a masquerade directory, you&#8217;ll need to either change CC and/or CXX, or modify the makefile(s) to call distcc explicitly.</p>
<h2>MASQUERADING</h2>
<p> The basic idea is to create a &quot;masquerade directory&quot; which contains links from the name of the real compiler to the distcc binary. This directory is inserted early on the PATH, so that calls to the compiler are intercepted and distcc is run instead. distcc then removes itself from the PATH to find the real compiler. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
# mkdir /usr/lib/distcc/bin
# cd /usr/lib/distcc/bin
# ln -s ../../../bin/distcc gcc
# ln -s ../../../bin/distcc cc
# ln -s ../../../bin/distcc g++
# ln -s ../../../bin/distcc c++
</pre>
</dl>
<p> Then, to use distcc, a user just needs to put the directory /usr/lib/distcc/bin early in the PATH, and have set a host list in DISTCC_HOSTS or a file. distcc will handle the rest. </p>
<p> Note that this masquerade directory must occur on the PATH earlier than the directory that contains the actual compilers of the same names, and that any auxiliary programs that these compilers call (such as as or ld) must also be found on the PATH in a directory after the masquerade directory since distcc calls out to the real compiler with a PATH value that has all directory up to and including the masquerade directory trimmed off. </p>
<p> It is possible to get a &quot;recursion error&quot; in masquerade mode, which means that distcc is somehow finding itself again, not the real compiler. This can indicate that you have two masquerade directories on the PATH, possibly because of having two distcc installations in different locations. It can also indicate that you&#8217;re trying to mix &quot;masqueraded&quot; and &quot;explicit&quot; operation. </p>
<p> Recursion errors can be avoided by using shell scripts instead of links. For example, in /usr/lib/distcc/bin create a file cc which contains: </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh 
distcc /usr/bin/gcc &quot;$@&quot;
</pre>
</dl>
<p> In this way, we are not dependent on distcc having to locate the real gcc by investigating the PATH variable. Instead, the compiler location is explicitly provided. </p>
<h2>USING DISTCC WITH CCACHE</h2>
<p> ccache is a program that speeds software builds by caching the results of compilations. ccache is normally called before distcc, so that results are retrieved from a normal cache. Some experimentation may be required for idiosyncratic makefiles to make everything work together. </p>
<p> The most reliable method is to set</p>
<dl>
<dt>
<dd> <code>CCACHE_PREFIX=distcc</code></dl>
<p> This tells ccache to run distcc as a wrapper around the real compiler. ccache still uses the real compiler to detect compiler upgrades. </p>
<p> ccache can then be run using either a masquerade directory <i>or </i> by setting</p>
<dl>
<dt>
<dd> <code>CC=ccache gcc</code></dl>
<p> As of version 2.2, ccache does not cache compilation from preprocessed source and so will never get a cache hit if it is run from distccd or distcc. It must be run only on the client side and before distcc to be any use. </p>
<p> distcc&#8217;s pump mode is not compatible with ccache.</p>
<h2>HOST SPECIFICATIONS</h2>
<p> A &quot;host list&quot; tells distcc which machines to use for compilation. In order, distcc looks in the <code>$DISTCC_HOSTS</code> environment variable, the user&#8217;s <code>$DISTCC_DIR/hosts</code> file, and the system-wide host file. If no host list can be found, distcc emits a warning and compiles locally. </p>
<p> The host list is a simple whitespace separated list of host specifications. The simplest and most common form is a host names, such as </p>
<dl>
<dt>
<dd> <code>localhost red green blue</code></dl>
<p> distcc prefers hosts towards the start of the list, so machines should be listed in descending order of speed. In particular, when only a single compilation can be run (such as from a configure script), the first machine listed is used (but see <i>&#8211;randomize</i> below). </p>
<p> Placing <i>localhost</i> at the right point in the list is important to getting good performance. Because overhead for running jobs locally is low, localhost should normally be first. However, it is important that the client have enough cycles free to run the local jobs and the distcc client. If the client is slower than the volunteers, or if there are many volunteers, then the client should be put later in the list or not at all. As a general rule, if the aggregate CPU speed of the client is less than one fifth of the total, then the client should be left out of the list. </p>
<p> If you have a large shared build cluster and a single shared hosts file, the above rules would cause the first few machines in the hosts file to be tried first even though they are likely to be busier than machines later in the list. To avoid this, place the keyword <i>&#8211;randomize</i> into the host list. This will cause the host list to be randomized, which should improve performance slightly for large build clusters. </p>
<p> There are two special host names <code>&#8211;localslots</code> and <code>&#8211;localslots_cpp</code> which are useful for adjusting load on the local machine. The <code>&#8211;localslots</code> host specifies how many jobs that cannot be run remotely that can be run concurrently on the local machine, while <code>&#8211;localslots_cpp</code> controls how many preprocessors will run in parallel on the local machine. Tuning these values can improve performance. Linking on large projects can take large amounts of memory. Running parallel linkers, which cannot be executed remotely, may force the machine to swap, which reduces performance over just running the jobs in sequence without swapping. Getting the number of parallel preprocessors just right allows you to use larger parallel factors with make, since the local machine now has some machanism for measuring local resource usage. </p>
<p> Finally there is the host entry </p>
<p> Performance depends on the details of the source and makefiles used for the project, and the machine and network speeds. Experimenting with different settings for the host list and <code>-j</code> factor may improve performance. </p>
<p> The syntax is </p>
<pre><code>
DISTCC_HOSTS = HOSTSPEC... HOSTSPEC = LOCAL_HOST | SSH_HOST | TCP_HOST | OLDSTYLE_TCP_HOST | GLOBAL_OPTION | ZEROCONF LOCAL_HOST = localhost[/ LIMIT] | --localslots = &lt;int&gt; | --localslots_cpp = &lt;int&gt;
                                                                                                                                                                           SSH_HOST = [USER] @HOSTID[/ LIMIT][:COMMAND][OPTIONS] TCP_HOST = HOSTID
[:PORT][/ LIMIT][OPTIONS] OLDSTYLE_TCP_HOST = HOSTID[/ LIMIT]
[:PORT][OPTIONS] HOSTID = HOSTNAME | IPV4 | IPV6 OPTIONS =, OPTION[OPTIONS] OPTION = lzo | cpp | auth GLOBAL_OPTION = --randomize
                                                                                                                          ZEROCONF = +zeroconf
</code></pre>
<p> Here are some individual examples of the syntax:</p>
<dl>
<dt><code>localhost</code></p>
<dd> The literal word &quot;localhost&quot; is interpreted specially to cause compilations to be directly executed, rather than passed to a daemon on the local machine. If you do want to connect to a daemon on the local machine for testing, then give the machine&#8217;s IP address or real hostname. (This will be slower.)</p>
<dt><code>IPV6</code></p>
<dd> A literal IPv6 address enclosed in square brackets, such as <code>[::1]</code></p>
<dt><code>IPV4</code></p>
<dd> A literal IPv4 address, such as <code>10.0.0.1</code></p>
<dt><code>HOSTNAME</code></p>
<dd> A hostname to be looked up using the resolver.</p>
<dt><code>:PORT</code></p>
<dd> Connect to a specified decimal port number, rather than the default of 3632.</p>
<dt><code>@HOSTID</code></p>
<dd> Connect to the host over SSH, rather than TCP. Options for the SSH connection can be set in <code>~/.ssh/config</code></p>
<dt><code>USER@</code></p>
<dd> Connect to the host over SSH as a specified username.</p>
<dt><code>:COMMAND </code></p>
<dd> Connect over SSH, and use a specified path to find the distccd server. This is normally only needed if for some reason you can&#8217;t install distccd into a directory on the default PATH for SSH connections. Use this if you get errors like &quot;distccd: command not found&quot; in SSH mode.</p>
<dt><code>/LIMIT</code></p>
<dd> A decimal limit can be added to any host specification to restrict the number of jobs that this client will send to the machine. The limit defaults to four per host (two for localhost), but may be further restricted by the server. You should only need to increase this for servers with more than two processors.</p>
<dt><code>,lzo</code></p>
<dd> Enables LZO compression for this TCP or SSH host.</p>
<dt><code>,cpp</code></p>
<dd> Enables distcc-pump mode for this host. Note: the build command must be wrapped in the pump script in order to start the include server.</p>
<dt><code>,auth</code></p>
<dd> Enables GSSAPI-based mutual authentication for this host.</p>
<dt><code>&#8211;randomize</code></p>
<dd> Randomize the order of the host list before execution.</p>
<dt><code>+zeroconf</code></p>
<dd> <code>This option is only available if distcc was compiled with Avahi support enabled at configure time.</code> When this special entry is present in the hosts list, distcc will use Avahi Zeroconf DNS Service Discovery (DNS-SD) to locate any available distccd servers on the local network. This avoids the need to explicitly list the host names or IP addresses of the distcc server machines. The distccd servers must have been started with the &quot;&#8211;zeroconf&quot; option to distccd. An important caveat is that in the current implementation, pump mode (&quot;,cpp&quot;) and compression (&quot;,lzo&quot;) will never be used for hosts located via zeroconf.</dl>
<p> Here is an example demonstrating some possibilities: </p>
<dl>
<dt>
<dd>
<pre>
<code>localhost/2 @bigman/16:/opt/bin/distccd oldmachine:4200/1</code>
<code># cartman is down</code>
<code>distant/3,lzo</code>
</pre>
</dl>
<p> Comments are allowed in host specifications. Comments start with a hash/pound sign (<code>#</code>) and run to the end of the line. </p>
<p> If a host in the list is not reachable distcc will emit a warning and ignore that host for about one minute.</p>
<h2>COMPRESSION</h2>
<p> The <code>lzo </code> host option specifies that LZO compression should be used for data transfer, including preprocessed source, object code and error messages. Compression is usually economical on networks slower than 100Mbps, but results may vary depending on the network, processors and source tree. </p>
<p> Enabling compression makes the distcc client and server use more CPU time, but less network traffic. The added CPU time is insignificant for pump mode. The compression ratio is typically 4:1 for source and 2:1 for object code. </p>
<p> Using compression requires both client and server to use at least release 2.9 of distcc. No server configuration is required: the server always responds with compressed replies to compressed requests. </p>
<p> Pump mode requires the servers to have the lzo host option on.</p>
<h2>SEARCH PATHS</h2>
<p> If the compiler name is an absolute path, it is passed verbatim to the server and the compiler is run from that directory. For example: </p>
<dl>
<dt>
<dd> <code>distcc /usr/local/bin/gcc-3.1415 -c hello.c</code></dl>
<p> If the compiler name is not absolute, or not fully qualified, distccd&#8217;s PATH is searched. When distcc is run from a masquerade directory, only the base name of the compiler is used. The client&#8217;s PATH is used only to run the preprocessor and has no effect on the server&#8217;s path.</p>
<h2>TIMEOUTS</h2>
<p> Both the distcc client and server impose timeouts on transfer of data across the network. This is intended to detect hosts which are down or unreachable, and to prevent compiles hanging indefinitely if a server is disconnected while in use. If a client-side timeout expires, the job will be re-run locally. </p>
<p> The timeouts are not configurable at present.</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages or warnings from local or remote compilers are passed through to diagnostic output on the client. </p>
<p> distcc can supply extensive debugging information when the verbose option is used. This is controlled by the <code>DISTCC_VERBOSE</code> environment variable on the client, and the <code>&#8211;verbose</code> option on the server. For troubleshooting, examine both the client and server error messages.</p>
<h2>EXIT CODES</h2>
<p> The exit code of distcc is normally that of the compiler: zero for successful compilation and non-zero otherwise. </p>
<p> distcc distinguishes between &quot;genuine&quot; errors such as a syntax error in the source, and &quot;accidental&quot; errors such as a networking problem connecting to a volunteer. In the case of accidental errors, distcc will retry the compilation locally unless the DISTCC_FALLBACK option has been disabled. </p>
<p> If the compiler exits with a signal, distcc returns an exit code of 128 plus the signal number. </p>
<p> distcc internal errors cause an exit code between 100 and 127. In particular</p>
<dl>
<dt>100</p>
<dd> General distcc failure.</p>
<dt>101</p>
<dd> Bad arguments.</p>
<dt>102</p>
<dd> Bind failed.</p>
<dt>103</p>
<dd> Connect failed.</p>
<dt>104</p>
<dd> Compiler crashed.</p>
<dt>105</p>
<dd> Out of memory.</p>
<dt>106</p>
<dd> Bad Host SPEC</p>
<dt>107</p>
<dd> I/O Error</p>
<dt>108</p>
<dd> Truncated.</p>
<dt>109</p>
<dd> Protocol Error.</p>
<dt>110</p>
<dd> The given compiler was not found on the remote host. Check that $CC is set appropriately and that it&#8217;s installed in a directory on the search path for distccd.</p>
<dt>111</p>
<dd> Recursive call to distcc.</p>
<dt>112</p>
<dd> Failed to discard privileges.</p>
<dt>113</p>
<dd> Network access denied.</p>
<dt>114</p>
<dd> In use by another process.</p>
<dt>115</p>
<dd> No such file.</p>
<dt>116</p>
<dd> No hosts defined and fallbacks disabled.</p>
<dt>118</p>
<dd> Timeout.</p>
<dt>119</p>
<dd> GSS-API &#8211; Catchall error code for GSS-API related errors. </p>
</dl>
<h2>FILES</h2>
<p> If $DISTCC_HOSTS is not set, distcc reads a host list from either <code>$DISTCC_DIR/hosts</code> or a system-wide configuration file set at compile time. The file locations are shown in the output from <code>distcc &#8211;help</code> </p>
<p> distcc creates a number of temporary and lock files underneath the temporary directory.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> distcc&#8217;s behaviour is controlled by a number of environment variables. For most cases nothing need be set if the host list is stored in a file.</p>
<dl>
<dt><code>DISTCC_HOSTS</code></p>
<dd> Space-separated list of volunteer host specifications.</p>
<dt><code>DISTCC_VERBOSE</code></p>
<dd> If set to 1, distcc produces explanatory messages on the standard error stream or in the log file. This can be helpful in debugging problems. Bug reports should include verbose output.</p>
<dt><code>DISTCC_LOG</code></p>
<dd> Log file to receive messages from distcc itself, rather than stderr.</p>
<dt><code>DISTCC_FALLBACK</code></p>
<dd> By default distcc will compile locally if it fails to distribute a job to the intended machine, or if no host list can be found. If this variable is set to 0 then fallbacks are disabled and those compilations will simply fail. Note that this does not affect jobs which must always be local such as linking.</p>
<dt><code>DISTCC_IO_TIMEOUT</code></p>
<dd> Specifies how long (in seconds) distcc will wait before deciding a distributed job has timed out. If a distributed job is expected to takes a long time, consider increasing this value so the job does not time out and fallback to a local compile. By default set to 300 seconds.</p>
<dt><code>DISTCC_SAVE_TEMPS</code></p>
<dd> If set to 1, temporary files are not deleted after use. Good for debugging, or if your disks are too empty.</p>
<dt><code>DISTCC_TCP_CORK</code></p>
<dd> If set to 0, disable use of &quot;TCP corks&quot;, even if they&#8217;re present on this system. Using corks normally helps pack requests into fewer packets and aids performance. This should normally be left enabled.</p>
<dt><code>DISTCC_SSH</code></p>
<dd> Specifies the command used for opening SSH connections. Defaults to &quot;ssh&quot; but may be set to a different connection command such as &quot;lsh&quot; or &quot;tsocks-ssh&quot; that accepts a similar command line. The command is not split into words and is not executed through the shell.</p>
<dt><code>DISTCC_SKIP_LOCAL_RETRY</code></p>
<dd> If set, when a remote compile fails, distcc will no longer try to recompile that file locally.</p>
<dt><code>DISTCC_DIR</code></p>
<dd> Per-user configuration directory to store lock files and state files. By default <code>~/.distcc/ </code> is used.</p>
<dt><code>TMPDIR</code></p>
<dd> Directory for temporary files such as preprocessor output. By default /tmp/ is used.</p>
<dt><code>UNCACHED_ERR_FD</code></p>
<dd> If set and if DISTCC_LOG is not set, distcc errors are written to the file descriptor identified by this variable. This variable is intended mainly for automatic use by ccache, which sets it to avoid caching transient errors such as network problems.</p>
<dt><code>DISTCC_ENABLE_DISCREPANCY_EMAIL</code></p>
<dd> If set, distcc sends an email when a compilation failed remotely, but succeeded locally. Built-in heuristics prevent some such discrepancy email from being sent if the problem is that a local file changed between the failing remote compilation and the succeeding local compilation.</p>
<dt><code>DISTCC_MAX_DISCREPANCY</code></p>
<dd> The maximum number of remote compilation failures allowed in pump mode before distcc switches to plain distcc mode. By default set to 1.</p>
<dt><code>DCC_EMAILLOG_WHOM_TO_BLAME</code></p>
<dd> The email address for discrepancy email; the default is &quot;distcc-pump-errors&quot;.</p>
<dt><code>DISTCC_PRINCIPAL</code></p>
<dd> If set, specifies the name of the principal that distccd runs under, and is used to authenticate the server to the client. <code>This environment variable is only used if distcc was compiled with</code> <code>the &#8211;with-auth configure option and the ,auth per host option is specified.</code></dl>
<h2>CROSS COMPILING</h2>
<p> Cross compilation means building programs to run on a machine with a different processor, architecture, or operating system to where they were compiled. distcc supports cross compilation, including teams of mixed-architecture machines, although some changes to the compilation commands may be required. </p>
<p> The compilation command passed to distcc must be one that will execute properly on every volunteer machine to produce an object file of the appropriate type. If the machines have different processors, then simply using <code>distcc cc</code> will probably not work, because that will normally invoke the volunteer&#8217;s native compiler. </p>
<p> Machines with the same CPU but different operating systems may not necessarily generate compatible .o files. </p>
<p> Several different gcc configurations can be installed side-by-side on any machine. If you build gcc from source, you should use the <code>&#8211;program-suffix configuration</code> options to cause it to be installed with a name that encodes the gcc version and the target platform. </p>
<p> The recommended convention for the gcc name is <i>TARGET-gcc-VERSION</i> such as <code>i686-linux-gcc-3.2</code> . GCC 3.3 will install itself under this name, in addition to <i>TARGET-gcc</i> and, if it&#8217;s native, <i>gcc-VERSION </i> and <i>gcc</i> . </p>
<p> The compiler must be installed under the same name on the client and on every volunteer machine.</p>
<h2>BUGS</h2>
<p> If you think you have found a distcc bug, please see the file <i>reporting-bugs.txt</i> in the documentation directory for information on how to report it. </p>
<p> Some makefiles have missing or extra dependencies that cause incorrect or slow parallel builds. Recursive make is inefficient and can leave processors unnecessarily idle for long periods. (See <i>Recursive Make Considered Harmful</i> by Peter Miller.) Makefile bugs are the most common cause of trees failing to build under distcc. Alternatives to Make such as <i>SCons</i> can give much faster builds for some projects. </p>
<p> Using different versions of gcc can cause confusing build problems because the header files and binary interfaces have changed over time, and some distributors have included incompatible patches without changing the version number. distcc does not protect against using incompatible versions. Compiler errors about link problems or declarations in system header files are usually due to mismatched or incorrectly installed compilers. </p>
<p> gcc&#8217;s <code>-MD </code> option can produce output in the wrong directory if the source and object files are in different directories and the <code>-MF </code> option is not used. There is no perfect solution because of incompatible changes between gcc versions. Explicitly specifying the dependency output file with <code>-MF</code> will fix the problem. </p>
<p> TCP mode connections should only be used on trusted networks. </p>
<p> Including slow machines in the list of volunteer hosts can slow the build down. </p>
<p> When distcc or ccache is used on NFS, the filesystem must be exported with the <code>no_subtree_check </code> option to allow reliable renames between directories. </p>
<p> The compiler can be invoked with a command line <code>gcc hello.c</code> to both compile and link. distcc doesn&#8217;t split this into separate parts, but rather runs the whole thing locally. </p>
<p> distcc-pump mode reverts to plain distcc mode for source files that contain includes with absolute paths (either directly or in an included file). </p>
<p> Due to limitations in gcc, gdb may not be able to automatically find the source files for programs built using distcc in some circumstances. The gdb <code>directory</code> command can be used. For distcc&#8217;s plain (non-pump) mode, this is fixed in gcc 3.4 and later. For pump mode, the fix in gcc 3.4 does not suffice; we&#8217;ve worked around the gcc limitation by rewriting the object files that gcc produces, but this is only done for ELF object files, but not for other object file formats. </p>
<p> The .o files produced by discc in pump mode will be different from those produced locally: for non-ELF files, the debug information will specify compile directories of the server. The code itself should be identical. </p>
<p> For the ELF-format, distcc rewrites the .o files to correct compile directory path information. While the resulting .o files are not bytewise identical to what would have been produced by compiling on the local client (due to different padding, etc), they should be functionally identical. </p>
<p> In distcc-pump mode, the include server is unable to handle certain very complicated computed includes as found in parts of the Boost library. The include server will time out and distcc will revert to plain mode. </p>
<p> In distcc-pump mode, certain assumptions are made that source and header files do not change during the build. See discussion in section DISTCC DISCREPANCY SYMPTOMS of <code>include_server</code>(1(). </p>
<p> Other known bugs may be documented on <i><a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a></i></p>
<h2>AUTHOR</h2>
<p> distcc was written by Martin Pool &lt;mbp [at] sourcefrog.net&gt;, with the co-operation of many scholars including Wayne Davison, Frerich Raabe, Dimitri Papadopoulos and others noted in the NEWS file. Please report bugs to &lt;distcc [at] lists.samba.org&gt;. See <code><a href="/docs/linux/man/1-pump/">pump</a></code>(1) for the authors of pump mode.</p>
<h2>LICENCE</h2>
<p> You are free to use distcc. distcc (including this manual) may be copied, modified or distributed only under the terms of the GNU General Public Licence version 2 or later. distcc comes with absolutely no warrany. A copy of the GPL is included in the file COPYING.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-distccd/">distccd</a></code>(1), <code><a href="/docs/linux/man/1-pump/">pump</a></code>(1), <code><a href="/docs/linux/man/1-include_server/">include_server</a></code>(1), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1), and <code><a href="/docs/linux/man/1-ccache/">ccache</a></code>(1). <i><a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a></i> <i><a rel="nofollow" href="http://ccache.samba.org/">http://ccache.samba.org/</a></i> </p>
<h2>Index</h2>
