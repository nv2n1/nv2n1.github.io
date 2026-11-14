---
title: "opachassisadmin(8)"
name: "opachassisadmin"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opachassisadmin/"
description: "opachassisadmin"
---

<p>opachassisadmin </p>
<p> <code>(Switch)</code> Performs a number of multi-step chassis initialization and verification operations, including initial chassis setup, firmware upgrades, chassis reboot, and others.</p>
<h2>Syntax</h2>
<p>opachassisadmin [-c] [-F <i>chassisfile</i>] [-H &#8216;<i>chassis</i>&#8216;] [-P <i>packages</i>] [-a <i>action</i>] [-I <i>fm_bootstate</i>] [-S] [-d <i>upload_dir</i>] [-s <i>securityfiles</i>] <i>operation</i>&#8230;</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-c</p>
<dd>Clobbers result files from any previous run before starting this run. </p>
<dt>-F <i>chassisfile</i></p>
<dd>File with chassis in cluster. The default is /etc/sysconfig/opa/chassis. </p>
<dt>-H <i>chassis</i></p>
<dd>List of chassis to execute the operation against. </p>
<dt>-P <i>packages</i></p>
<dd>Filenames and directories of firmware images to install. For directories specified, all .pkg files in directory tree are used. shell wild cards may also be used within quotes, or for fmconfig, filename of FM config file to use, or for fmgetconfig, filename to upload to (default opafm.xml). </p>
<dt>-a <i>action</i></p>
<dd>Action for supplied file. The default is push.</p>
<dl>
<dd>
<dl>
<dd>For chassis upgrade: </p>
<dl>
<dd>
<dl>
<dd>push Ensures firmware is in primary or alternate. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>select Ensures firmware is in primary. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>run Ensures firmware is in primary and running. </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>For chassis fmconfig : </p>
<dl>
<dd>
<dl>
<dd>push Ensures the configuration file is in chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>run After push, restarts FM on master, stops on secondary. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>runall After push, restarts FM on all management modules. </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>For chassis fmcontrol : </p>
<dl>
<dd>
<dl>
<dd>stop Stops FM on all management modules. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>run Ensures FM running on master, stopped on secondary. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>runall Ensures FM running on all management modules. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>restart Restarts FM on master, stops on secondary. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>restartall Restarts FM on all MM. </p>
</dl>
</dl>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>For chassis fmsecurityfiles : </p>
<dl>
<dd>
<dl>
<dd>push Ensures FM security files are in chassis. </p>
</dl>
</dl>
</dl>
</dl>
<dt>-I <i>fm_bootstate</i></p>
<dd>fmconfig and fmcontrol install options.</p>
<dl>
<dd>
<dl>
<dd>disable Disables FM start at chassis boot. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>enable Enables FM start on master at chassis boot. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>enableall Enables FM start on all MM at chassis boot. </p>
</dl>
</dl>
<dt>-d <i>upload_dir</i></p>
<dd>Directory to upload FM configuration files to; default is uploads. </p>
<dt>-S</p>
<dd>Securely prompts for password for user on chassis. </p>
<dt>-s <i>securityFiles</i></p>
<dd>Security files to install. Default is *.pem. For Chassis <i>fmsecurityfiles</i>, filenames/directories of security files to install. For directories specified, all security files in directory tree are used. Shell wildcards may also be used within quotes. </p>
<dd>For Chassis <i>fmgetsecurityfiles</i>, filename to upload to. Default is *.pem</p>
<dt>
&nbsp;<wbr><i>operation</i>&nbsp;<wbr></p>
<dd>Operation to perform. Can be one or more of:</p>
<dl>
<dd>
<dl>
<dd>reboot Reboots chassis, ensures they go down and come back. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>configure Runs wizard to perform chassis configuration. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>upgrade Upgrades install of all chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>getconfig Gets basic configuration of chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fmconfig FM configuration operation on all chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fmgetconfig Fetches FM configuration from all chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fmcontrol Controls FM on all chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fmsecurityfiles FM security files operation on all chassis. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>fmgetsecurityfiles Fetches FM security files from all chassis. </p>
</dl>
</dl>
<p> For more information on the operations that can be performed, see <i>Operation Details</i> </p>
</dl>
<h2>Example</h2>
<p>opachassisadmin -c reboot<br />
 opachassisadmin -P /root/ChassisFw4.2.0.0.1 upgrade<br />
 opachassisadmin -H &#8216;chassis1 chassis2&#8242; reboot<br />
 CHASSIS=&#8217;chassis1 chassis2&#8217; opachassis_admin reboot<br />
 opachassisadmin -a run -P &#8216;*.pkg&#8217; upgrade</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -H and -F option not supplied. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used in absence of -F and -H. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>Maximum concurrent operations. </p>
<dt><code>FF_SERIALIZE_OUTPUT</code></p>
<dd>Serializes output of parallel operations (yes or no). </p>
<dt><code>UPLOADS_DIR</code></p>
<dd>Directory to upload to, used in absence of -d. </p>
</dl>
<h2>Operation Details</h2>
<p><code>(Switch)</code> All chassis operations log into the chassis as chassis user admin. Intel recommends using the -S option to securely prompt for a password, in which case the same password is used for all chassis. Alternately, the password may be put in the environment or the opafastfabric.conf file using <code>FF_CHASSIS_ADMIN_PASSWORD</code>. </p>
<p> All versions of Intel(R) Omni-Path Switch 100 Series firmware permit SSH keys to be configured within the chassis for secure password-less login. In this case, there is no need to configure a <code>FF_CHASSIS_ADMIN_PASSWORD</code> and <code>FF_CHASSIS_LOGIN_METHOD</code> can be SSH. Refer to the <i>Intel(R) Omni-Path Fabric Switches Command Line Interface Reference Guide</i> </p>
<p> for more information.</p>
<dl>
<dt>upgrade</p>
<dd>Upgrades the firmware on each chassis or slot specified. The -P option selects a directory containing .pkg files or provides an explicit list of .pkg files for the chassis and/or slots. The -a option selects the desired minimal state for the new firmware. For each chassis and/or slot selected for upgrade, the .pkg file applicable to that slot is selected and used. If more than one .pkg file is specified of a given card type, the operation is undefined. </p>
<dd>The upgrade is intelligent and does not upgrade chassis that already have the desired firmware in the desired state (as specified by -a).</p>
<dd>When the -a option specifies run, chassis that are not already running the desired firmware are rebooted. By selecting the proper <code>FF_MAX_PARALLEL</code> value, a rolling upgrade or a parallel upgrade may be accomplished. In most cases, a parallel upgrade is recommended for expediency.</p>
<dd>For more information about chassis firmware, refer to the <i>Intel(R) Omni-Path Fabric Switches GUI User Guide</i> </p>
<p> and <i>Intel(R) Omni-Path Fabric Externally-Managed Switches Release Notes</i> </p>
<dt>configure</p>
<dd>Runs the chassis setup wizard, which asks a series of questions. Once the wizard has finished prompting for configuration information, all the selected chassis are configured through the CLI interface according to the responses. The following options may be configured for all chassis: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>syslog server IP address, TCP/UDP port number, syslog facility code, and the chassis LogMode. </p>
<dt>&bull;</p>
<dd>NTP server </p>
<dt>&bull;</p>
<dd>local time zone </p>
<dt>&bull;</p>
<dd>maximum packet MTU </p>
<dt>&bull;</p>
<dd>VL capability </p>
<dt>&bull;</p>
<dd>VL credit distribution </p>
<dt>&bull;</p>
<dd>link width supported </p>
<dt>&bull;</p>
<dd>IB node description </p>
<dt>&bull;</p>
<dd>IB node description format </p>
<dt>&bull;</p>
<dd>disable chassis auto clear of port counters </p>
</dl>
</dl>
<dt>reboot</p>
<dd>Reboots the given chassis and ensures they go down and come back up by pinging them during the reboot process. </p>
<dd>By selecting the proper <code>FF_MAX_PARALLEL</code> value, a rolling reboot or a parallel reboot may be accomplished. In most cases, a parallel upgrade is recommended for expediency.</p>
<dt>getconfig</p>
<dd>Retrieves basic information from a chassis such as syslog, NTP configuration, timezone info, MTU Capability, VL Capability, VL Credit Distribution, Link Width, and node description. </p>
<dt>fmconfig</p>
<dd>Updates the Fabric Manager configuration file on each chassis specified. The -P option selects a file to transfer to the chassis. The -a option selects the desired minimal state for the new configuration and controls whether the FM is started/restarted after the file is updated. The -I option can be used to configure the FM start at boot for the selected chassis. </p>
<dt>fmgetconfig</p>
<dd>Uploads the FM configuration file from all selected chassis. The file is uploaded to the selected uploads directory. The -P option specifies the desired destination filename within the uploads directory. </p>
<dt>fmcontrol</p>
<dd>Allows the FM to be controlled on each chassis specified. The -a option selects the desired state for the FM. </p>
<dd>The -I option configures the FM start at boot for the selected chassis.</p>
<dt>fmsecurityfiles</p>
<dd>Updates the FM security files on each chassis specified. The -s option selects file(s) to transfer to the chassis. The -a option selects the desired minimal state for the new security files. In this release, push is the only supported action. </p>
<dt>fmgetsecurityfiles</p>
<dd>Uploads the FM security files from all selected chassis. The files are uploaded to the selected uploads directory. The -s option specifies the desired destination filename within the uploads directory. </p>
</dl>
<h2>Logging</h2>
<p>opachassisadmin provides detailed logging of its results. During each run, the following files are produced:</p>
<dl>
<dt>test.res</p>
<dd>Appended with summary results of run. </p>
<dt>test.log</p>
<dd>Appended with detailed results of run. </p>
<dt>save_tmp/</p>
<dd>Contains a directory per failed test with detailed logs. </p>
<dt>test_tmp*/</p>
<dd>Intermediate result files while test is running. </p>
</dl>
<p> The -c option removes all log files.</p>
<h2>ssh Keys</h2>
<p>When performing operations against chassis, Intel recommends setting up SSH keys. If SSH keys are not set up, all chassis must be configured with the same admin password. In this case, Intel recommends using the -S option. The -S option avoids the need to keep the password in configuration files.</p>
<h2>Results</h2>
<p>Results from opachassisadmin are grouped into test suites, test cases, and test items. A given run of opachassisadmin represents a single test suite. Within a test suite, multiple test cases occur; typically one test case per chassis being operated on. Some of the more complex operations may have multiple test items per test case. Each test item represents a major step in the overall test case. </p>
<p> Each opachassisadmin run appends to test.res and test.log, and creates temporary files in test_tmp$PID in the current directory. The test.res file provides an overall summary of operations performed and their results. The same information is also displayed while opachassisadmin is executing. test.log contains detailed information about what was performed, including the specific commands executed and the resulting output. The test_tmp directories contain temporary files that reflect tests in progress (or killed). The logs for any failures are logged in the save_temp directory with a directory per failed test case. If the same test case fails more than once, save_temp retains the information from the first failure. Subsequent runs of opachassisadmin are appended to test.log. Intel recommends reviewing failures and using the -c option to remove old logs before subsequent runs of opachassisadmin. </p>
<p> opachassisadmin implicitly performs its operations in parallel. However, as for the other tools, <code>FF_MAX_PARALLEL</code> can be exported to change the degree of parallelism. Twenty (20) parallel operations is the default.</p>
