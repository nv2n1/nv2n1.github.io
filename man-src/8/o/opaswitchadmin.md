---
title: "opaswitchadmin(8)"
name: "opaswitchadmin"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaswitchadmin/"
description: "opaswitchadmin"
---

<p>opaswitchadmin </p>
<p> <code>(Switch)</code> Performs a number of multi-step initialization and verification operations against one or more externally managed Intel(R) Omni-Path switches. The operations include initial switch setup, firmware upgrades, chassis reboot, and others.</p>
<h2>Syntax</h2>
<p>opaswitchadmin [-c] [-N &#8216;<i>nodes</i>&#8216;] [-L <i>nodefile</i>] [-O] [-P <i>packages</i>] [-a <i>action</i>] [-t <i>portsfile</i>] [-p <i>ports</i>] <i>operation</i>&#8230;</p>
<h2>Options</h2>
<dl>
<dt>-help</p>
<dd>Produces full help text. </p>
<dt>-c</p>
<dd>Clobbers result files from any previous run before starting this run. </p>
<dt>-N <i>nodes</i></p>
<dd>List of nodes to execute the operation against. </p>
<dt>-L <i>nodefile</i></p>
<dd>File with nodes in the cluster. Default is /etc/sysconfig/opa/switches file. </p>
<dt>-P <i>packages</i></p>
<dd>
<dl>
<dd>
<dl>
<dd>For upgrades File name or directory where the firmware image is to install. For the directory specified, .emfw file in the directory tree is used. shell wild cards may also be used within quotes. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>For capture File name to upload to. Default is switchcapture file. </p>
</dl>
</dl>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabrics for switch access. Default is /etc/sysconfig/opa/ports file. </p>
<dt>-p <i>ports</i></p>
<dd>List of local HFI ports used to access fabrics for switch access. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </p>
<dd>Uses the format hfi:port, for example:</p>
<dl>
<dd>
<dl>
<dd>0:0 First active port in system. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>0:y Port <i>y</i> within system. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>x:0 First active port on HFI <i>x</i>. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>x:y HFI <i>x</i>, port <i>y</i>. </p>
</dl>
</dl>
<dt>-a <i>action</i></p>
<dd>Action for firmware file for switch upgrade. The action argument can be one or more of the following: </p>
<dl>
<dd>
<dl>
<dd>select Ensures firmware is in primary (default). </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>run Ensures firmware is in primary and running. </p>
</dl>
</dl>
<dt>-O</p>
<dd>Override for firmware upgrades, bypasses the previous firmware version checks, and forces the update unconditionally. </p>
<dt>
&nbsp;<wbr><i>operation</i>&nbsp;<wbr></p>
<dd>Performs the specified <i>operation</i>, which can be one or more of the following: </p>
<dl>
<dd>
<dl>
<dd>reboot Reboots switches, ensures they go down and come back. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>configure Runs wizard to set up switch configuration. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>upgrade Upgrades installation of all switches. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>info Reports firmware and hardware version, part number, and data rate capability of all nodes. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>hwvpd Completes hardware Vital Product Data (VPD) report of all nodes. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>ping Pings all nodes and tests for presence. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fwverify Reports integrity of failsafe firmware of all nodes. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>getconfig Gets port configurations of an externally managed switch. </p>
</dl>
</dl>
</dl>
<p> For more information on operations, see <i>opachassisadmin Operation Details</i></p>
<h2>Example</h2>
<p>opaswitchadmin -c reboot<br />
 opaswitchadmin -P /root/ChassisFw <i>X.X.X.X.X</i> upgrade<br />
 opaswitchadmin -a run -P &#8216;*.emfw&#8217; upgrade</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>OPASWITCHES</code></p>
<dd>List of nodes, used in absence of -N and -L options. </p>
<dt><code>OPASWITCHES_FILE</code></p>
<dd>File containing list of nodes, used in absence of -N and -L options. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations. </p>
<dt><code>FF_SERIALIZE_OUTPUT</code></p>
<dd>Serialize output of parallel operations (yes or no). </p>
</dl>
<h2>Details</h2>
<p>opaswitchadmin provides detailed logging of its results. During each run, the following files are produced:</p>
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
<p> Results from opaswitchadmin are grouped into test suites, test cases, and test items. A given run of opaswitchadmin represents a single test suite. Within a test suite, multiple test cases occur; typically one test case per chassis being operated on. Some of the more complex operations may have multiple test items per test case. Each test item represents a major step in the overall test case. </p>
<p> Each opaswitchadmin run appends to test.res and test.log and creates temporary files in test_tmp$PID in the current directory. the test.res file provides an overall summary of operations performed and their results. The same information is also displayed while opaswitchadmin is executing. test.log contains detailed information about what was performed, including the specific commands executed and the resulting output. The test_tmp directories contain temporary files that reflect tests in progress (or killed). The logs for any failures are logged in the save_temp directory with a directory per failed test case. If the same test case fails more than once, save_temp retains the information from the first failure. Subsequent runs of opaswitchadmin are appended to test.log. Intel recommends reviewing failures and using the -c option to remove old logs before subsequent runs of opaswitchadmin. opaswitchadmin also appends to punchlist.csv for failing switches. </p>
<p> opaswitchadmin implicitly performs its operations in parallel. However, as for the other tools, <code>FF_MAX_PARALLEL</code> can be exported to change the degree of parallelism. Twenty (20) parallel operations is the default.</p>
<h2>opaswitchadmin Operation Details</h2>
<p><code>(Switch)</code> All operations against Intel(R) Omni-Path Fabric externally-managed switches (except ping) securely access the selected switches. If a password has been set, the -S option must be used to securely prompt for a password. In this case, the same password is used for all switches.</p>
<dl>
<dt>reboot</p>
<dd>Reboots the given switches. </p>
<dd>Use the <code>FF_MAX_PARALLEL</code> value to select either a rolling reboot or a parallel reboot. In most cases, a parallel reboot is recommended for expediency.</p>
<dt>upgrade</p>
<dd>Upgrades the firmware on each specified switch. The -P option selects a directory containing a .emfw file or provides an explicit .emfw file for the switches. If more than one .emfw file is specified, the operation is undefined. The -a option selects the desired minimal state for the new firmware. Only the select and run options are valid for this operation. </p>
<dd>When the -a option specifies run, switches are rebooted. Use the <code>FF_MAX_PARALLEL</code> value to select a rolling upgrade or a parallel upgrade. In most cases, a parallel upgrade is recommended for expediency.</p>
<dd>The upgrade process also sets the switch name.</p>
<dd>The upgrade process is used to set, clear, or change the password of the switches using the -s option. When this option is specified, you are prompted for a new password to be set on the switches. To reset (clear) the password, press Enter when prompted. This option can be used to configure the switches to not require a password for subsequent operations. A change to the password does not take effect until the next reboot of the switch.</p>
<dd>For more information about switch firmware, refer to the <i>Intel(R) Omni-Path Fabric Switches GUI User Guide</i> </p>
<p> and <i>Intel(R) Omni-Path Fabric Externally-Managed Switches Release Notes</i> </p>
<dt>configure</p>
<dd>Runs the switch setup wizard, which asks a series of questions. Once the wizard has finished prompting for configuration information, all the selected switches are configured according to the entered responses. The following items are configurable for all Intel(R) Omni-Path Switch 100 Series : </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>MTU</p>
<dt>&bull;</p>
<dd>VL Capability</p>
<dt>&bull;</p>
<dd>VL credit distribution</p>
<dt>&bull;</p>
<dd>Link Width Supported</p>
<dt>&bull;</p>
<dd>OPA Node Description </p>
</dl>
</dl>
<dd></dl>
<p> <code>NOTE:</code> Typically, the Node Description is updated automatically during a firmware upgrade, if it is configured properly in the switches file. Updating the node description is also available using the configure option without performing a firmware upgrade. </p>
<dl>
<dt>info</p>
<dd>Queries the switches and displays the following information: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Firmware version</p>
<dt>&bull;</p>
<dd>Hardware version</p>
<dt>&bull;</p>
<dd>Hardware part number, including revision information</p>
<dt>&bull;</p>
<dd>Speed capability</p>
<dt>&bull;</p>
<dd>Fan status</p>
<dt>&bull;</p>
<dd>Power supply status </p>
</dl>
</dl>
<dd>This operation also outputs a summary of various configuration settings for each switch within a fabric.</p>
<dt>hwvpd</p>
<dd>Queries the switches and displays the Vital Product Data (VPD) including: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Serial number</p>
<dt>&bull;</p>
<dd>Part number</p>
<dt>&bull;</p>
<dd>Model name</p>
<dt>&bull;</p>
<dd>Hardware version</p>
<dt>&bull;</p>
<dd>Manufacturer</p>
<dt>&bull;</p>
<dd>Product description</p>
<dt>&bull;</p>
<dd>Manufacturer ID</p>
<dt>&bull;</p>
<dd>Manufacture date</p>
<dt>&bull;</p>
<dd>Manufacture time </p>
</dl>
</dl>
<dt>ping</p>
<dd>Issues an inband packet to the switches to test for presence and reports on presence/non-presence of each selected switch. </p>
<dd></dl>
<p> <code>NOTE:</code> It is not necessary to supply a password (using -S) for this operation. </p>
<dl>
<dt>fwverify</p>
<dd>Verifies the integrity of the firmware images in the EEPROMs of the selected switches. </p>
<dt>capture</p>
<dd>Gets switch hardware and firmware state capture of all nodes. </p>
<dt>getconfig</p>
<dd>Gets port configurations of an externally managed switch. This operation also outputs a summary of various configuration settings for each switch within a fabric. For example, in a fabric with seven switches, a report similar to the following is displayed. </p>
<dd>This summary helps determine if all switches have the same configuration, and if not, indicates how many have each value. If some of the values are not as expected, view the test.res file to identify which switches have the undesirable values. </p>
</dl>
