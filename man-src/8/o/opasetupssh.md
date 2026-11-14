---
title: "opasetupssh(8)"
name: "opasetupssh"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opasetupssh/"
description: "opasetupssh"
---

<p>opasetupssh </p>
<p> <code>(Linux or Switch)</code> Creates SSH keys and configures them on all hosts or chassis so the system can use SSH and SCP into all other hosts or chassis without a password prompt. Typically, during cluster setup this tool enables the root user on the Management Node to log into the other hosts (as root) or chassis (as admin) using password-less SSH.</p>
<h2>Syntax</h2>
<p>opasetupssh [-C|p|U] [-f <i>hostfile</i>] [-F <i>chassisfile</i>] [-h &#8216;<i>hosts</i>&#8216;] [-H &#8216;<i>chassis</i>&#8216;] [-i <i>ipoib_suffix</i>] [-u <i>user</i>] [-S] [-R|P]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-C</p>
<dd>Performs operation against chassis. Default is hosts. </p>
<dt>-p</p>
<dd>Performs operation against all chassis or hosts in parallel. </p>
<dt>-U</p>
<dd>Performs connect only (to enter in local hosts, known hosts). When run in this mode, the -S option is ignored. </p>
<dt>-f <i>hostfile</i></p>
<dd>File with hosts in cluster. Default is /etc/sysconfig/opa/hosts file. </p>
<dt>-F <i>chassisfile</i></p>
<dd>File with chassis in cluster. Default is /etc/sysconfig/opa/chassis file. </p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts to set up. </p>
<dt>-H <i>chassis</i></p>
<dd>List of chassis to set up. </p>
<dt>-i <i>ipoib_suffix</i></p>
<dd>Suffix to apply to host names to create IPoIB host names. Default is -ib. </p>
<dt>-u <i>user</i></p>
<dd>User on remote system to allow this user to SSH to. Default is current user code for host(s) and admin for chassis. </p>
<dt>-S</p>
<dd>Securely prompts for password for user on remote system. </p>
<dt>-R</p>
<dd>Skips setup of SSH to local host. </p>
<dt>-P</p>
<dd>Skips ping of host (for SSH to devices on Internet with ping firewalled). </p>
</dl>
<h2>Examples</h2>
<h2>Operations on Hosts</h2>
<p>opasetupssh -S -i&#8221;<br />
 opasetupssh -U<br />
 opasetupssh -h &#8216;arwen elrond&#8217; -U<br />
 HOSTS=&#8217;arwen elrond&#8217; opasetupssh -U</p>
<h2>Operations on Chassis</h2>
<p>opasetupssh -C<br />
 opasetupssh -C -H &#8216;chassis1 chassis2&#8242;<br />
 CHASSIS=&#8217;chassis1 chassis2&#8217; opasetupssh -C</p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used in absence of -F and -H. </p>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -C is used and -H and -F options not supplied. </p>
<dt><code>FF_MAX_PARALLEL</code></p>
<dd>When -p option is used, maximum concurrent operations. </p>
<dt><code>FF_IPOIB_SUFFIX</code></p>
<dd>Suffix to append to hostname to create IPoIB hostname. Used in absence of -i. </p>
<dt><code>FF_CHASSIS_LOGIN_METHOD</code></p>
<dd>How to log into chassis. Can be Telnet or SSH. </p>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></p>
<dd>Password for admin on all chassis. Used in absence of -S option. </p>
</dl>
<h2>Description</h2>
<p>The Intel(R) Omni-Path Fabric Suite FastFabric Toolset provides additional flexibility in the translation between IPoIB and management network hostnames. Refer to &quot;Configuration of IPoIB Name Mapping&quot; section in the <i>Intel(R) Omni-Path Fabric Suite FastFabric User Guide</i> </p>
<p> for more information. </p>
<p> opasetupssh provides an easy way to create SSH keys and distribute them to the hosts or chassis in the cluster. Many of the FastFabric tools (as well as many versions of MPI) require that SSH is set up for password-less operation. Therefore, opasetupssh is an important setup step. </p>
<p> This tool also sets up SSH to the local host and the local host&#8217;s IPoIB name. This capability is required by selected FastFabric Toolset commands and may be used by some applications (such as MPI). </p>
<p> opasetupssh has two modes of operation. The mode is selected by the presence or absence of the -U option. Typically, opasetupssh is first run without the -U option, then it may later be run with the -U option.</p>
<h2>Host Initial Key Exchange</h2>
<p>When run without the -U option, opasetupssh performs the initial key exchange and enables password-less SSH and SCP. The preferred way to use opasetupssh for initial key exchange is with the -S option. This requires that all hosts are configured with the same password for the specified #8217#8220;user&#8221; (typically root). In this mode, the password is prompted for once and then SSH and SCP are used in conjunction with that password to complete the setup for the hosts. This mode also avoids the need to set up rsh/rcp/rlogin (which can be a security risk). </p>
<p> opasetupssh configures password-less SSH/SCP for both the management network and IPoIB. Typically, the management network is used for FastFabric Toolset operations while IPoIB is used for MPI and other applications. </p>
<p> During initial cluster installation, where the Intel(R) Omni-Path Fabric software is not yet installed on all the hosts, IPoIB is not yet running. In this situation, use the -i option with an empty string as follows:opasetupssh -i &#8221; </p>
<p> This causes the last part of the setup of SSH for IPoIB to be skipped.</p>
<h2>Refreshing Local Systems Known Hosts</h2>
<p>If aspects of the host have changed, such as IP addresses, MAC addresses, software installation, or server OS reinstallation, you can refresh the local host&#8217;s SSH known_hosts file by running opasetupssh with the -U option. This option does not transfer the keys, but instead connects to each host (management network and IPoIB) to refresh the SSH keys. Existing entries for the specified hosts are replaced within the local known_hosts file. When run in this mode, the -S option is ignored. This mode assumes SSH has previously been set up for the hosts, as such no files are transferred to the specified hosts and no passwords should be required. </p>
<p> Typically after completing the installation and booting of Intel(R) Omni-Path Fabric software, opasetupssh must be rerun with the -U option to update the known_hosts file.</p>
<h2>Chassis Initial Key Exchange</h2>
<p>When run without the -U option, opasetupssh performs the initial key exchange and enables password-less SSH and SCP. For chassis, the key exchange uses SCP and the chassis CLI. During this command you log into the chassis using the configured mechanism for chassis login. </p>
<p> The preferred way to use opasetupssh for initial key exchange is with the -S option. This requires that all chassis are configured with the same password for admin. In this mode, you are prompted for the password once and then the <code>FF_CHASSIS_LOGIN_METHOD</code> and SCP are used in conjunction with that password to complete the setup for the chassis. This method also avoids the need to setup the chassis password in /etc/sysconfig/opa/opafastfabric.conf (which can be a security risk). </p>
<p> For chassis, the -i option is ignored.</p>
<h2>Chassis Refreshing Local Systems Known Hosts</h2>
<p>If aspects of the chassis have changed, such as IP addresses or MAC addresses, you can refresh the local host&#8217;s SSH known_hosts file by running opasetupssh with the -U option. This option does not transfer the keys, but instead connects to each chassis to refresh the SSH keys. Existing entries for the specified chassis are replaced within the local known_hosts file. When run in this mode, the -S option is ignored. This mode assumes SSH has previously been set up for the chassis, because no files are transferred to the specified hosts and no passwords are required.</p>
