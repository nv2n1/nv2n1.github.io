---
title: "tcsd-conf(5)"
name: "tcsd-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tcsd-conf/"
description: "tcsd.conf – configuration file for the trousers TCS daemon."
---

<p>TCG Software Stack<br />
 </center></p>
<h2>Name</h2>
<p>tcsd.conf &#8211; configuration file for the trousers TCS daemon.</p>
<h2>Description</h2>
<p>This file, by default <i>/etc/tcsd.conf</i> is read by the trousers TCSD daemon, tcsd (see <a href="/docs/linux/man/8-tcsd/">tcsd</a>(8)). The tcsd.conf file that is installed by trousers contains all the default options, commented out.</p>
<h2>Options</h2>
<p><code>port</code> The port that TCSD will listen on for connections, local and remote, from applications. </p>
<p> <code>num_threads</code> The maximum number of threads that the TCSD will spawn simultaneously to service applications. After <code>num_threads</code> threads have been spawned, any application that attempts to connect to the TCSD will receive an error. </p>
<p> <code>system_ps_file</code> The location of the system persistent storage file. The system persistent storage file holds keys and data across restarts of the TCSD and system reboots. </p>
<p> <code>firmware_log_file</code> Path to the file containing the current firmware PCR event log data. The interface to this log is usually provided by the TPM device driver. </p>
<p> <code>kernel_log_file</code> Path to the file containing the current kernel PCR event log data. By default, this data will be parsed in the format provided by the Integrity Measurement Architecture LSM. </p>
<p> <code>firmware_pcrs</code> A list of PCR indices that are manipulated only by the system firmware and therefore are not extended or logged by the TCSD. Applications that call Tcsi_PcrExtend on PCRs listed here will receive an error. </p>
<p> <code>kernel_pcrs</code> A list of PCR indices that are manipulated only by the kernel and therefore are not extended or logged by the TCSD. Applications that call Tcsi_PcrExtend on PCRs listed here will receive an error. </p>
<p> <code>platform_cred</code> Path to the platform credential for your TPM. Your TPM manufacturer may have provided you with a set of credentials (certificates) that should be used when creating identities using your TPM. When a user of your TPM makes an identity, this credential will be encrypted as part of that process. See the 1.1b TPM Main specification section 9.3 for information on this process. </p>
<p> <code>conformance_cred</code> Path to the conformance credential for your TPM. Your TPM manufacturer may have provided you with a set of credentials (certificates) that should be used when creating identities using your TPM. When a user of your TPM makes an identity, this credential will be encrypted as part of that process. See the 1.1b TPM Main specification section 9.3 for information on this process. </p>
<p> <code>endorsement_cred</code> Path to the endorsement credential for your TPM. Your TPM manufacturer may have provided you with a set of credentials (certificates) that should be used when creating identities using your TPM. When a user of your TPM makes an identity, this credential will be encrypted as part of that process. See the 1.1b TPM Main specification section 9.3 for information on this process. </p>
<p> <code>remote_ops</code> A list of TCS commands which will be allowed to be executed on this machine&#8217;s TCSD by TSP&#8217;s on non-local hosts (over the internet). By default, access to all operations is denied. </p>
<p> <code>host_platform_class</code> Determines the TCG specification of the host&#8217;s platform class. This refers to one of the specifications contained in the TCG web site. The default is PC specification version 1.2 . </p>
<p> <code>all_platform_classes</code> Specifies all the TCG defined platforms associated with the host platform. The host_platform_class must not be defined here. By default, all platforms but the host platform are associated.</p>
<h2>Example</h2>
<dl>
<dd>
<pre>port = 30003
num_threads = 10
system_ps_file = /var/lib/tpm/system.data
firmware_log_file = /proc/tpm/firmware_events
kernel_log_file = /proc/tcg/measurement_events
firmware_pcrs = 0,1,2,3,4,5,6,7
kernel_pcrs = 10,11
platform_cred = /var/lib/tpm/platform.cert
conformance_cred = /var/lib/tpm/conformance.cert
endorsement_cred = /var/lib/tpm/endorsement.cert
remote_ops = create_key,random
host_platform_class = server_12
all_platform_classes = pc_11,pc_12,mobile_12</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tcsd/">tcsd</a></code>(8)</p>
<h2>Author</h2>
<p>Kent Yoder</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-tech [at] lists.sf.net&gt;</p>
