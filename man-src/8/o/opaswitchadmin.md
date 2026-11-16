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
<dt>-help</dt>
<dd>Produces full help text. </dd>
<dt>-c</dt>
<dd>Clobbers result files from any previous run before starting this run. </dd>
<dt>-N <i>nodes</i></dt>
<dd>List of nodes to execute the operation against. </dd>
<dt>-L <i>nodefile</i></dt>
<dd>File with nodes in the cluster. Default is /etc/sysconfig/opa/switches file. </dd>
<dt>-P <i>packages</i></dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dd>For upgrades File name or directory where the firmware image is to install. For the directory specified, .emfw file in the directory tree is used. shell wild cards may also be used within quotes. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>For capture File name to upload to. Default is switchcapture file. </dd>
</dl>
</dl>
<dt>-t <i>portsfile</i></dt>
<dd>File with list of local HFI ports used to access fabrics for switch access. Default is /etc/sysconfig/opa/ports file. </dd>
<dt>-p <i>ports</i></dt>
<dd>List of local HFI ports used to access fabrics for switch access. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. </dd>
<dd>Uses the format hfi:port, for example:</dd>
<dl>
<dd>
</dd><dl>
<dd>0:0 First active port in system. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>0:y Port <i>y</i> within system. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>x:0 First active port on HFI <i>x</i>. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>x:y HFI <i>x</i>, port <i>y</i>. </dd>
</dl>
</dl>
<dt>-a <i>action</i></dt>
<dd>Action for firmware file for switch upgrade. The action argument can be one or more of the following: </dd>
<dl>
<dd>
</dd><dl>
<dd>select Ensures firmware is in primary (default). </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>run Ensures firmware is in primary and running. </dd>
</dl>
</dl>
<dt>-O</dt>
<dd>Override for firmware upgrades, bypasses the previous firmware version checks, and forces the update unconditionally. </dd>
<dt>
&nbsp;<wbr><i>operation</i>&nbsp;<wbr></dt>
<dd>Performs the specified <i>operation</i>, which can be one or more of the following: </dd>
<dl>
<dd>
</dd><dl>
<dd>reboot Reboots switches, ensures they go down and come back. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>configure Runs wizard to set up switch configuration. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>upgrade Upgrades installation of all switches. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>info Reports firmware and hardware version, part number, and data rate capability of all nodes. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>hwvpd Completes hardware Vital Product Data (VPD) report of all nodes. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>ping Pings all nodes and tests for presence. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>fwverify Reports integrity of failsafe firmware of all nodes. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>getconfig Gets port configurations of an externally managed switch. </dd>
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
<dt><code>OPASWITCHES</code></dt>
<dd>List of nodes, used in absence of -N and -L options. </dd>
<dt><code>OPASWITCHES_FILE</code></dt>
<dd>File containing list of nodes, used in absence of -N and -L options. </dd>
<dt><code>FF_MAX_PARALLEL</code></dt>
<dd>Maximum concurrent operations. </dd>
<dt><code>FF_SERIALIZE_OUTPUT</code></dt>
<dd>Serialize output of parallel operations (yes or no). </dd>
</dl>
<h2>Details</h2>
<p>opaswitchadmin provides detailed logging of its results. During each run, the following files are produced:</p>
<dl>
<dt>&bull;</dt>
<dd>test.res : Appended with summary results of run.</dd>
<dt>&bull;</dt>
<dd>test.log : Appended with detailed results of run.</dd>
<dt>&bull;</dt>
<dd>save_tmp/ : Contains a directory per failed test with detailed logs.</dd>
<dt>&bull;</dt>
<dd>test_tmp*/ : Intermediate result files while test is running.</dd></dl>
<p> The -c option removes all log files. </p>
<p> Results from opaswitchadmin are grouped into test suites, test cases, and test items. A given run of opaswitchadmin represents a single test suite. Within a test suite, multiple test cases occur; typically one test case per chassis being operated on. Some of the more complex operations may have multiple test items per test case. Each test item represents a major step in the overall test case. </p>
<p> Each opaswitchadmin run appends to test.res and test.log and creates temporary files in test_tmp$PID in the current directory. the test.res file provides an overall summary of operations performed and their results. The same information is also displayed while opaswitchadmin is executing. test.log contains detailed information about what was performed, including the specific commands executed and the resulting output. The test_tmp directories contain temporary files that reflect tests in progress (or killed). The logs for any failures are logged in the save_temp directory with a directory per failed test case. If the same test case fails more than once, save_temp retains the information from the first failure. Subsequent runs of opaswitchadmin are appended to test.log. Intel recommends reviewing failures and using the -c option to remove old logs before subsequent runs of opaswitchadmin. opaswitchadmin also appends to punchlist.csv for failing switches. </p>
<p> opaswitchadmin implicitly performs its operations in parallel. However, as for the other tools, <code>FF_MAX_PARALLEL</code> can be exported to change the degree of parallelism. Twenty (20) parallel operations is the default.</p>
<h2>opaswitchadmin Operation Details</h2>
<p><code>(Switch)</code> All operations against Intel(R) Omni-Path Fabric externally-managed switches (except ping) securely access the selected switches. If a password has been set, the -S option must be used to securely prompt for a password. In this case, the same password is used for all switches.</p>
<dl>
<dt>reboot</dt>
<dd>Reboots the given switches. </dd>
<dd>Use the <code>FF_MAX_PARALLEL</code> value to select either a rolling reboot or a parallel reboot. In most cases, a parallel reboot is recommended for expediency.</dd>
<dt>upgrade</dt>
<dd>Upgrades the firmware on each specified switch. The -P option selects a directory containing a .emfw file or provides an explicit .emfw file for the switches. If more than one .emfw file is specified, the operation is undefined. The -a option selects the desired minimal state for the new firmware. Only the select and run options are valid for this operation. </dd>
<dd>When the -a option specifies run, switches are rebooted. Use the <code>FF_MAX_PARALLEL</code> value to select a rolling upgrade or a parallel upgrade. In most cases, a parallel upgrade is recommended for expediency.</dd>
<dd>The upgrade process also sets the switch name.</dd>
<dd>The upgrade process is used to set, clear, or change the password of the switches using the -s option. When this option is specified, you are prompted for a new password to be set on the switches. To reset (clear) the password, press Enter when prompted. This option can be used to configure the switches to not require a password for subsequent operations. A change to the password does not take effect until the next reboot of the switch.</dd>
<dd>For more information about switch firmware, refer to the <i>Intel(R) Omni-Path Fabric Switches GUI User Guide</i> </dd>
<p> and <i>Intel(R) Omni-Path Fabric Externally-Managed Switches Release Notes</i> </p>
<dt>configure</dt>
<dd>Runs the switch setup wizard, which asks a series of questions. Once the wizard has finished prompting for configuration information, all the selected switches are configured according to the entered responses. The following items are configurable for all Intel(R) Omni-Path Switch 100 Series : </dd>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>MTU</dd>
<dt>&bull;</dt>
<dd>VL Capability</dd>
<dt>&bull;</dt>
<dd>VL credit distribution</dd>
<dt>&bull;</dt>
<dd>Link Width Supported</dd>
<dt>&bull;</dt>
<dd>OPA Node Description </dd>
</dl>
</dl>
<dd></dd></dl>
<p> <code>NOTE:</code> Typically, the Node Description is updated automatically during a firmware upgrade, if it is configured properly in the switches file. Updating the node description is also available using the configure option without performing a firmware upgrade. </p>
<dl>
<dt>info</dt>
<dd>Queries the switches and displays the following information: </dd>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>Firmware version</dd>
<dt>&bull;</dt>
<dd>Hardware version</dd>
<dt>&bull;</dt>
<dd>Hardware part number, including revision information</dd>
<dt>&bull;</dt>
<dd>Speed capability</dd>
<dt>&bull;</dt>
<dd>Fan status</dd>
<dt>&bull;</dt>
<dd>Power supply status </dd>
</dl>
</dl>
<dd>This operation also outputs a summary of various configuration settings for each switch within a fabric.</dd>
<dt>hwvpd</dt>
<dd>Queries the switches and displays the Vital Product Data (VPD) including: </dd>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>Serial number</dd>
<dt>&bull;</dt>
<dd>Part number</dd>
<dt>&bull;</dt>
<dd>Model name</dd>
<dt>&bull;</dt>
<dd>Hardware version</dd>
<dt>&bull;</dt>
<dd>Manufacturer</dd>
<dt>&bull;</dt>
<dd>Product description</dd>
<dt>&bull;</dt>
<dd>Manufacturer ID</dd>
<dt>&bull;</dt>
<dd>Manufacture date</dd>
<dt>&bull;</dt>
<dd>Manufacture time </dd>
</dl>
</dl>
<dt>ping</dt>
<dd>Issues an inband packet to the switches to test for presence and reports on presence/non-presence of each selected switch. </dd>
<dd></dd></dl>
<p> <code>NOTE:</code> It is not necessary to supply a password (using -S) for this operation. </p>
<dl>
<dt>fwverify</dt>
<dd>Verifies the integrity of the firmware images in the EEPROMs of the selected switches. </dd>
<dt>capture</dt>
<dd>Gets switch hardware and firmware state capture of all nodes. </dd>
<dt>getconfig</dt>
<dd>Gets port configurations of an externally managed switch. This operation also outputs a summary of various configuration settings for each switch within a fabric. For example, in a fabric with seven switches, a report similar to the following is displayed. </dd>
<dd>This summary helps determine if all switches have the same configuration, and if not, indicates how many have each value. If some of the values are not as expected, view the test.res file to identify which switches have the undesirable values. </dd>
</dl>
