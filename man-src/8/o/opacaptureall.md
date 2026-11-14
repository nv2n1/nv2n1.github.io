---
title: "opacaptureall(8)"
name: "opacaptureall"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opacaptureall/"
description: "opacaptureall"
---

<p>opacaptureall </p>
<p> <code>(Chassis and Host)</code> Captures supporting information for a problem report from all hosts or Intel(R) Omni-Path Chassis and uploads to this system. </p>
<p> <code>For Hosts :</code> When a host opacaptureall is performed, opacapture is run to create the specified capture file within ~root on each host (with the .tgz suffix added as needed). The files are uploaded and unpacked into a matching directory name within upload_dir/<i>hostname</i>/ on the local system. The default file name is hostcapture. </p>
<p> <code>For Chassis:</code> When a chassis opacaptureall is performed, opacapture is run on each chassis and its output is saved to upload_dir/<i>chassisname</i>/<i>file</i> on the local system. The default file name is chassiscapture. </p>
<p> For both host and chassis capture, the uploaded captures are combined into a .tgz file with the file name specified and the suffix .all.tgz added.</p>
<h2>Syntax</h2>
<p>opacaptureall [-C] [-p] [-f <i>hostfile</i>] [-F <i>chassisfile</i>]<br />
 [-h &#8216;<i>hosts</i>&#8216;]<br />
 [-H &#8216;<i>chassis</i>&#8216;] [-t <i>portsfile</i>] [-d <i>upload_dir</i>] [-S] [-D <i>detail_level</i>] [ <i>file</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-C</p>
<dd>Performs capture against chassis. Default is hosts. </p>
<dt>-p</p>
<dd>Performs capture upload in parallel on all host/chassis. For a host capture, this only affects the upload phase. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts file. </p>
<dt>-F <i>chassisfile</i></p>
<dd>File containing a list of chassis in the cluster. Default is /etc/sysconfig/opa/chassis file. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts on which to perform a capture. </p>
<dt>-H <i>chassis</i></p>
<dd>List of chassis on which to perform a capture. </p>
<dt>-t <i>portsfile</i></p>
<dd>File with list of local HFI ports used to access fabric(s) for switch access, default is /etc/sysconfig/opa/ports file. </p>
<dt>-d <i>upload_dir</i></p>
<dd>Directory to upload to, default is uploads. If not specified, the environment variable <code>UPLOADS_DIR</code> is used. If that is not exported, the default (./uploads) is used. </p>
<dt>-S</p>
<dd>Securely prompts for password for administrator on a chassis. </p>
<dt>-D <i>detail_level</i></p>
<dd>Level of detail of the capture passed to host opacapture. (Only used for host captures; ignored for chassis captures.)</p>
<dl>
<dd>
<dl>
<dd>1 Local. Obtains local information from each host.</dl>
</dl>
<dl>
<dd>
<dl>
<dd>2 Fabric. In addition to <i>Local</i>, also obtains basic fabric information by queries to the SM and fabric error analysis using opareport. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>3 Fabric+FDB. In addition to <i>Fabric</i>, also obtains the Forwarding Database (FDB), which includes the switch forwarding tables from the SM. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>4 Analysis. In addition to <i>Fabric+FDB</i>, also obtains opaallanalysis results. If opaallanalysis has not yet been run, it is run as part of the capture. </p>
</dl>
</dl>
<dd></dl>
<p> <code>NOTE:</code> Detail levels 2-4 can be used when fabric operational problems occur. If the problem is node-specific, detail level 1 should be sufficient. Detail levels 2-4 require an operational Intel(R) Omni-Path Fabric Suite Fabric Manager. Typically your support representative requests a given detail level. If a given detail level takes excessively long or fails to be gathered, try a lower detail level. </p>
<p> For detail levels 2-4, the additional information is only gathered on the node running the opacaptureall command. The information is gathered for every fabric specified in the /etc/sysconfig/opa/ports file. </p>
<dl>
<dt>
&nbsp;<wbr><i>file</i>&nbsp;<wbr></p>
<dd>Name for capture file. The suffix .tgz is appended if it is not specified in the name. </p>
</dl>
<h2>Examples</h2>
<h2>Host Capture Examples</h2>
<p>opacaptureall<br />
 # Creates a hostcapture directory in upload_dir/hostname/ for each host in<br />
 /etc/sysconfig/opa/hosts file, then creates hostcapture.all.tgz. </p>
<p> opacaptureall mycapture<br />
 # Creates a mycapture directory in upload_dir/hostname/ for each host in<br />
 /etc/sysconfig/opa/hosts file, then creates mycapture.all.tgz. </p>
<p> opacaptureall -h #8217#180;arwen elrond&acute; 030127capture<br />
 # Gets the list of hosts from arwen elrond file and creates 030127cap#8217#8208;<br />
 ture.tgz file.</p>
<h2>Chassis Capture Examples</h2>
<p>opacaptureall -C<br />
 # Creates a chassiscapture file in upload_dir/chassisname/ for each chassis<br />
 in /etc/sysconfig/opa/chassis file, then creates chassiscapture.all.tgz. </p>
<p> opacaptureall -C mycapture<br />
 # Creates a mycapture.tgz file in upload_dir/chassisname/ for each chassis<br />
 in /etc/sysconfig/opa/chassis file, then creates mycapture.all.tgz. </p>
<p> opacaptureall -C -H #8217#180;chassis1 chassis2&acute; 030127capture<br />
 # Captures from chassis1 and chassis2, and creates 030127capture.tgz file.</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -C is used and -h option is not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing a list of hosts, used in the absence of -f and -h. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing a list of chassis, used in the absence of -F and -H. </p>
<dt><code>UPLOADS_DIR</code></p>
<dd>Directory to upload to, used in the absence of -d. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When -p option is used, maximum concurrent operations are performed. </p>
<dt><code>FF_CHASSIS_LOGIN_METHOD</code></p>
<dd>How to log into chassis. Can be Telnet or SSH. </p>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></p>
<dd>Password for administrator on all chassis. Used in absence of -S option. </p>
</dl>
<h2>More Information</h2>
<p>When performing opacaptureall against hosts, internally SSH is used. The command opacaptureall requires that password-less SSH be set up between the host running Intel(R) Omni-Path Fabric Suite FastFabric Toolset and the hosts opacaptureall is operating against. The opasetupssh command can aid in setting up password-less SSH. </p>
<p> When performing operations against chassis, set up of SSH keys is recommended (see <i>opasetupssh</i> ). If SSH keys are not set up, all chassis must be configured with the same admin password and use of the -S option is recommended. The -S option avoids the need to keep the password in configuration files. </p>
<p> <code>NOTE:</code> The resulting host capture files can require significant amounts of space on the Intel(R) Omni-Path Fabric Suite FastFabric Toolset host. Actual size varies, but sizes can be multiple megabytes per host. Intel recommends that you ensure adequate space is available on the Intel(R) Omni-Path Fabric Suite FastFabric Toolset system. In many cases, it may not be necessary to run opacaptureall against all hosts or chassis; instead, a representative subset may be sufficient. Consult with your support representative for further information.</p>
