---
title: "opahostadmin(8)"
name: "opahostadmin"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opahostadmin/"
description: "opahostadmin"
---

<p>opahostadmin </p>
<p> <code>(Host)</code> Performs a number of multi-step host initialization and verification operations, including upgrading software or firmware, rebooting hosts, and other operations. In general, operations performed by opahostadmin involve a login to one or more host systems.</p>
<h2>Syntax</h2>
<p>opahostadmin [-c] [-i <i>ipoib_suffix</i>] [-f <i>hostfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-r <i>release</i>] [-I <i>install_options</i>] [-U <i>upgrade_options</i>] [-d <i>dir</i>] [-T <i>product</i>] [-P <i>packages</i>] [-m <i>netmask</i>] [-S] <i>operation</i>&#8230;</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-c</p>
<dd>Clobbers result files from any previous run before starting this run. </p>
<dt>-i <i>ipoib_suffix</i></p>
<dd>Suffix to apply to host names to create ipoib host names. Default is -opa. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with the names of hosts in a cluster. Default is /etc/sysconfig/opa/hosts file. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to execute the operation against. </p>
<dt>-r <i>release</i></p>
<dd>Software version to load/upgrade to. Default is the version of Intel(R) Omni-Path Software presently being run on the server. </p>
<dt>-d <i>dir</i></p>
<dd>Directory to retrieve <i>product</i>. <i>release</i>.tgz for load or upgrade. </p>
<dt>-I <i>install_options</i></p>
<dd>Software install options. </p>
<dt>-U <i>upgrade_options</i></p>
<dd>Software upgrade options. </p>
<dt>-T <i>product</i></p>
<dd>Product type to install. Default = IntelOPA-Basic.RHEL7-x86_64 </p>
<dd>Other options include: IntelOPA-Basic. <i>#8217lt;distro&gt;</i>, IntelOPA-IFS. <i>&lt;distro&gt;</i> where <i>&lt;distro&gt;</i> is the distribution and CPU.</p>
<dt>-P <i>packages</i></p>
<dd>Packages to install. Default = oftools ipoib mpi </p>
<dt>-m <i>netmask</i></p>
<dd>IPoIB netmask to use for configipoib operation. </p>
<dt>-S</p>
<dd>Securely prompts for user password on remote system. </p>
<dt>
&nbsp;<wbr><i>operation</i>&nbsp;<wbr></p>
<dd>Performs the specified <i>operation</i>, which can be one or more of the following: </p>
<dl>
<dd>
<dl>
<dd>load Starts initial installation of all hosts. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>upgrade Upgrades installation of all hosts. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>configipoib Creates ifcfg-ib1 using host IP address from /etc/hosts file. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>reboot Reboots hosts, ensures they go down and come back. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>sacache Confirms sacache has all hosts in it. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>ipoibping Verifies this host can ping each host through IPoIB. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>mpiperf Verifies latency and bandwidth for each host. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>mpiperfdeviation Verifies latency and bandwidth for each host against a defined threshold (or relative to average host performance). </p>
</dl>
</dl>
</dl>
<h2>Example</h2>
<p>opahostadmin -c reboot<br />
 opahostadmin upgrade<br />
 opahostadmin -h &#8216;elrond arwen&#8217; reboot<br />
 HOSTS=&#8217;elrond arwen&#8217; opahostadmin reboot</p>
<h2>Details</h2>
<p>opahostadmin provides detailed logging of its results. During each run, the following files are produced:</p>
<dl>
<dt>&bull;</p>
<dd>test.res : Appended with summary results of run.</p>
<dt>&bull;</p>
<dd>test.log : Appended with detailed results of run.</p>
<dt>&bull;</p>
<dd>save_tmp/ : Contains a directory per failed test with detailed logs.</p>
<dt>&bull;</p>
<dd>test_tmp*/ : Intermediate result files while test is running.</dl>
<p> The -c option removes all log files. </p>
<p> Results from opahostadmin are grouped into test suites, test cases, and test items. A given run of opahostadmin represents a single test suite. Within a test suite, multiple test cases occur; typically one test case per host being operated on. Some of the more complex operations may have multiple test items per test case. Each test item represents a major step in the overall test case. </p>
<p> Each opahostadmin run appends to test.res and test.log, and creates temporary files in test_tmp$PID in the current directory. test.res provides an overall summary of operations performed and their results. The same information is also displayed while opahostadmin is executing. test.log contains detailed information about what was performed, including the specific commands executed and the resulting output. The test_tmp directories contain temporary files which reflect tests in progress (or killed). The logs for any failures are logged in the save_temp directory with a directory per failed test case. If the same test case fails more than once, save_temp retains the information from the first failure. Subsequent runs of opahostadmin are appended to test.log. Intel recommends reviewing failures and using the -c option to remove old logs before subsequent runs of opahostadmin. </p>
<p> opahostadmin implicitly performs its operations in parallel. However, as for the other tools, <code>FF_MAX_PARALLEL</code> can be exported to change the degree of parallelism. Twenty (20) parallel operations is the default.</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations are performed. </p>
<dt><code>FF_SERIALIZE_OUTPUT</code></p>
<dd>Serialize output of parallel operations (yes or no). </p>
</dl>
<h2>opahostadmin Operation Details</h2>
<p><code>(Host)</code> Intel recommends that you set up password SSH or SCP for use during this operation. Alternatively, the -S option can be used to securely prompt for a password, in which case the same password is used for all hosts. Alternately, the password may be put in the environment or the opafastfabric.conf file using <code>FF_PASSWORD</code> and <code>FF_ROOTPASS</code>.</p>
<dl>
<dt>load</p>
<dd>Performs an initial installation of Intel(R) Omni-Path Software on a group of hosts. Any existing installation is uninstalled and existing configuration files are removed. Subsequently, the hosts are installed with a default Intel(R) Omni-Path Software configuration. The -I option can be used to select different install packages. Default = oftools ipoib mpi The -r option can be used to specify a release to install other than the one that this host is presently running. The <i>FF_PRODUCT</i>. <i>FF_PRODUCT_VERSION</i>.tgz file (for example, IntelOPA-Basic. <i>version</i>.tgz) is expected to exist in the directory specified by -d. Default is the current working directory. The specified software is copied to all the selected hosts and installed. </p>
<dt>upgrade</p>
<dd>Upgrades all selected hosts without modifying existing configurations. This operation is comparable to the -U option when running ./INSTALL manually. The -r option can be used to upgrade to a release different from this host. The default is to upgrade to the same release as this host. The <i>FF_PRODUCT</i>. <i>FF_PRODUCT_VERSION</i>.tgz file (for example, IntelOPA-Basic. <i>version</i>.tgz) is expected to exist in the directory specified by -d. (The default is the current working directory.) The specified software is copied to all the end nodes and installed.</p>
<dd></dl>
<p> <code>NOTE:</code> Only components that are currently installed are upgraded. This operation fails for hosts that do not have Intel(R) Omni-Path Software installed. </p>
<dl>
<dt>configipoib</p>
<dd>Creates a ifcfg-ib1 configuration file for each node using the IP address found using the resolver on the node. The standard Linux* resolver is used through the host command. (If running OFA Delta, this option configures ifcfg-ib0 .) </p>
<dd>If the host is not found, /etc/hosts on the node is checked. The -i option specifies an IPoIB suffix to apply to the host name to create the IPoIB host name for the node. The default suffix is -ib. The -m option specifies a netmask other than the default for the given class of IP address, such as when dividing a class A or B address into smaller IP subnets. IPoIB is configured for a static IP address and is autostarted at boot. For the Intel(R) OP Software Stack, the default /etc/sysconfig/ipoib.cfg file is used, which provides a redundant IPoIB configuration using both ports of the first HFI in the system.</p>
<dd></dl>
<p> <code>NOTE:</code> opahostadmin configipoib now supports DHCP (auto or static options) for configuring the IPoIB interface. You must specify these options in /etc/sysconfig/opa/opafastfabric.conf against the <code>FF_IPOIB_CONFIG</code> variable. If no options are found, the static IP configuration is used by default. If auto is specified, then one IP address from either static or dhcp is chosen. Static is used if the IP address can be obtained out of /etc/hosts or the resolver, otherwise DHCP is used. </p>
<dl>
<dt>reboot</p>
<dd>Reboots the given hosts and ensures they go down and come back up by pinging them during the reboot process. The ping rate is slow (5 seconds), so if the servers boot faster than this, false failures may be seen. </p>
<dt>sacache</p>
<dd>Verifies the given hosts can properly communicate with the SA and any cached SA data that is up to date. To run this command, Intel(R) Omni-Path Fabric software must be installed and running on the given hosts. The subnet manager and switches must be up. If this test fails: opacmdall &#8216;opasaquery -o desc&#8217; can be run against any problem hosts. </p>
<dd></dl>
<p> <code>NOTE:</code> This operation requires that the hosts being queried are specified by a resolvable TCP/IP host name. This operation FAILS if the selected hosts are specified by IP address. </p>
<dl>
<dt>ipoibping</p>
<dd>Verifies IPoIB basic operation by ensuring that the host can ping all other nodes through IPoIB. To run this command, Intel(R) Omni-Path Fabric software must be installed, IPoIB must be configured and running on the host, and the given hosts, the SM, and switches must be up. The -i option can specify an alternate IPoIB hostname suffix. </p>
<dt>mpiperf</p>
<dd>Verifies that MPI is operational and checks MPI end-to-end latency and bandwidth between pairs of nodes (for example, 1-2, 3-4, 5-6). Use this to verify switch latency/hops, PCI bandwidth, and overall MPI performance. The test.res file contains the results of each pair of nodes tested. </p>
<dd></dl>
<p> <code>NOTE:</code> This option is available for the Intel(R) Omni-Path Fabric Host Software OFA Delta packaging, but is not presently available for other packagings of OFED. </p>
<dl>
<dd>To obtain accurate results, this test should be run at a time when no other stressful applications (for example, MPI jobs or high stress file system operations) are running on the given hosts.</p>
<dd>Bandwidth issues typically indicate server configuration issues (for example, incorrect slot used, incorrect BIOS settings, or incorrect HFI model), or fabric issues (for example, symbol errors, incorrect link width, or speed). Assuming opareport has previously been used to check for link errors and link speed issues, the server configuration should be verified.</p>
<dd>Note that BIOS settings and differences between server models can account for 10-20% differences in bandwidth. For more details about BIOS settings, consult the documentation from the server supplier and/or the server PCI chipset manufacturer.</p>
<dt>mpiperfdeviation</p>
<dd>Enhanced version of mpiperf that verifies MPI performance. Can be used to verify switch latency/hops, PCI bandwidth, and overall MPI performance. It performs assorted pair-wise bandwidth and latency tests, and reports pairs outside an acceptable tolerance range. The tool identifies specific nodes that have problems and provides a concise summary of results. The test.res file contains the results of each pair of nodes tested. </p>
<dd>By default, concurrent mode is used to quickly analyze the fabric and host performance. Pairs that have 20% less bandwidth or 50% more latency than the average pair are reported as failures.</p>
<dd>The tool can be run in a sequential or a concurrent mode. Sequential mode runs each host against a reference host. By default, the reference host is selected based on the best performance from a quick test of the first 40 hosts. In concurrent mode, hosts are paired up and all pairs are run concurrently. Since there may be fabric contention during such a run, any poor performing pairs are then rerun sequentially against the reference host.</p>
<dd>Concurrent mode runs the tests in the shortest amount of time, however, the results could be slightly less accurate due to switch contention. In heavily oversubscribed fabric designs, if concurrent mode is producing unexpectedly low performance, try sequential mode.</p>
<dd></dl>
<p> <code>NOTE:</code> This option is available for the Intel(R) Omni-Path Fabric Host Software OFA Delta packaging, but is not presently available for other packagings of OFED. </p>
<dl>
<dd>To obtain accurate results, this test should be run at a time when no other stressful applications (for example, MPI jobs, high stress file system operations) are running on the given hosts.</p>
<dd>Bandwidth issues typically indicate server configuration issues (for example, incorrect slot used, incorrect BIOS settings, or incorrect HFI model), or fabric issues (for example, symbol errors, incorrect link width, or speed). Assuming opareport has previously been used to check for link errors and link speed issues, the server configuration should be verified.</p>
<dd>Note that BIOS settings and differences between server models can account for 10-20% differences in bandwidth. A result 5-10% below the average is typically not cause for serious alarm, but may reflect limitations in the server design or the chosen BIOS settings.</p>
<dd>For more details about BIOS settings, consult the documentation from the server supplier and/or the server PCI chipset manufacturer.</p>
<dd>The deviation application supports a number of parameters which allow for more precise control over the mode, benchmark and pass/fail criteria. The parameters to use can be selected using the <code>FF_DEVIATION_ARGS</code> configuration parameter in opafastfabric.conf</p>
<dd>Available parameters for deviation application:</p>
<dd>[-bwtol bwtol] [-bwdelta MBs] [-bwthres MBs]<br />
 [-bwloop count] [-bwsize size] [-lattol latol]<br />
 [-latdelta usec] [-latthres usec] [-latloop count]<br />
 [-latsize size][-c] [-b] [-v] [-vv]<br />
 [-h reference_host] </p>
<dl>
<dd>
<dl>
<dd>-bwtol Percent of bandwidth degradation allowed below average value. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwbidir Performs a bidirectional bandwidth test. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwunidir Performs a unidirectional bandwidth test (default). </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwdelta Limit in MB/s of bandwidth degradation allowed below average value. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwthres Lower limit in MB/s of bandwidth allowed. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwloop Number of loops to execute each bandwidth test. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-bwsize Size of message to use for bandwidth test. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-lattol Percent of latency degradation allowed above average value. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-latdelta Limit in usec of latency degradation allowed above average value. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-latthres Lower limit in usec of latency allowed. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-latloop Number of loops to execute each latency test. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-latsize Size of message to use for latency test. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-c Runs test pairs concurrently instead of the default of sequential. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-b When comparing results against tolerance and delta, uses best instead of average. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-v Verbose output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-vv Very verbose output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>-h Reference host to use for sequential pairing. </p>
</dl>
</dl>
<dd>Both bwtol and bwdelta must be exceeded to fail bandwidth test.</p>
<dd>When bwthres is supplied, bwtol and bwdelta are ignored.</p>
<dd>Both lattol and latdelta must be exceeded to fail latency test.</p>
<dd>When latthres is supplied, lattol and latdelta are ignored.</p>
<dd>For consistency with OSU benchmarks, MB/s is defined as 1000000 bytes/s. </p>
</dl>
