---
title: "opacmdall(8)"
name: "opacmdall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opacmdall/"
description: "opacmdall (Linux and Switch) Executes a command on all hosts or Intel(R) Omni-Path Chassis. This powerful command can be used for configuring servers or chassis, verifying that they are running, st..."
---

<p>opacmdall <code>(Linux and Switch)</code> Executes a command on all hosts or Intel(R) Omni-Path Chassis. This powerful command can be used for configuring servers or chassis, verifying that they are running, starting and stopping host processes, and other tasks. <code>NOTE:</code> opacmdall depends on the Linux* convention that utilities return 0 for success and #8217gt;0 for failure. If opacmdall is used to execute a non-standard utility like diff or a program that uses custom exit codes, then opacmdall may erroneously report &quot;Command execution FAILED&quot; when it encounters a non-zero exit code. However, command output is still returned normally and the error may be safely ignored. </p>
<h2>Syntax</h2>
<p>opacmdall [-Cpq] [-f <i>hostfile</i>] [-F <i>chassisfile</i>] [-h <i>hosts</i>] [-H <i>chassis</i>] [-u <i>user</i>] [-S] [-m <i>marker</i>] [-T <i>timelimit</i>] [-P] <i>cmd</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-C</p>
<dd>Performs command against chassis. Default is hosts. </p>
<dt>-p</p>
<dd>Runs command in parallel on all hosts/chassis. </p>
<dt>-q</p>
<dd>Quiet mode, do not show command to execute. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts file. </p>
<dt>-F <i>chassisfile</i></p>
<dd>File with chassis in cluster. Default is /etc/sysconfig/opa/chassis file. </p>
<dt>-h <i>host</i></p>
<dd>List of hosts to execute command on. </p>
<dt>-H <i>chassis</i></p>
<dd>List of chassis to execute command on. </p>
<dt>-u <i>user</i></p>
<dd>The user to perform the command as:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>For hosts, the default is current user code.</p>
<dt>&bull;</p>
<dd>For chassis, the default is admin. </p>
</dl>
</dl>
<dt>-S</p>
<dd>Securely prompts for password for user on chassis. </p>
<dt>-m <i>marker</i></p>
<dd>Marker for end of chassis command output. If omitted, defaults to chassis command prompt. This may be a regular expression. </p>
<dt>-T <i>timelimit</i></p>
<dd>Time limit in seconds when running host commands. Default is -1 (infinite). </p>
<dt>-P</p>
<dd>Outputs the hostname/chassis name as prefix to each output line. This can make script processing of output easier. </p>
</dl>
<h2>Examples</h2>
<h2>Operations on Host</h2>
<p>opacmdall date<br />
 opacmdall &#8216;uname -a&#8217;<br />
 opacmdall -h &#8216;elrond arwen&#8217; date<br />
 HOSTS=&#8217;elrond arwen&#8217; opacmdall date</p>
<h2>Operations on Chassis</h2>
<p>opacmdall -C &#8216;ismPortStats -noprompt&#8217;<br />
 opacmdall -C -H &#8216;chassis1 chassis2&#8242; ismPortStats -noprompt#8217#8217;<br />
 CHASSIS=&#8217;chassis1 chassis2&#8217; opacmdall ismPortStats -noprompt#8217#8217;</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -C is used and -H and -F options not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used in absence of -F and -H. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When -p option is used, maximum concurrent operations are performed. </p>
<dt><code>FF_SERIALIZE_OUTPUT</code></p>
<dd>Serialize output of parallel operations (yes or no). </p>
<dt><code>FF_CHASSIS_LOGIN_METHOD</code></p>
<dd>How to log into chassis. Can be Telnet or SSH. </p>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></p>
<dd>Password for admin on all chassis. Used in absence of -S option. </p>
</dl>
<h2>Notes</h2>
<p>All commands performed with opacmdall must be non-interactive in nature. opacmdall waits for the command to complete before proceeding. For example, when running host commands such as rm, the -i option (interactively prompt before removal) should not be used. (Note that this option is sometimes part of a standard bash alias list.) Similarly, when running chassis commands such as fwUpdateChassis, the -reboot option should not be used beccause this option causes an immediate reboot and therefore the command never returns. Also, the chassis command reboot should not be executed using opacmdall. Instead, use the opachassisadmin reboot command to reboot one or more chassis. For further information about individual chassis CLI commands, consult the <i>Intel(R) Omni-Path Fabric Switches Command Line Interface Reference Guide</i> When performing opacmdall against hosts, internally SSH is used. The command opacmdall requires that password-less SSH be set up between the host running the Intel(R) Omni-Path Fabric Suite FastFabric Toolset and the hosts opacmdall is operating against. The opasetupssh FastFabric tool can aid in setting up password-less SSH. When performing opacmdall against a set of chassis, all chassis must be configured with the same admin password. Alternatively, the opasetupssh FastFabric tool can be used to set up password-less SSH to the chassis. When performing operations against chassis, Intel recommends that you set up SSH keys (see <i>opasetupssh</i> ). If SSH keys are not set up, Intel recommends that you use the -S option, to avoid keeping the password in configuration files. </p>
