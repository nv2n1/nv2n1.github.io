---
title: "clatd(8)"
name: "clatd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clatd/"
description: "clatd – a CLAT / SIIT-DC Edge Relay implementation for Linux"
---

<p>clatd &#8211; a CLAT / SIIT-DC Edge Relay implementation for Linux</p>
<h2>Description</h2>
<p><code>clatd</code> implements the <font SIZE="-1">CLAT</font> component of the 464XLAT network architecture specified in <i></i><font SIZE="-1"><i>RFC 6877</i></font><i></i>. It allows an IPv6-only host to have IPv4 connectivity that is translated to IPv6 before being routed to an upstream <font SIZE="-1">PLAT </font>(which is typically a Stateful <font SIZE="-1">NAT64</font> operated by the <font SIZE="-1">ISP</font>) and there translated back to IPv4 before being routed to the IPv4 internet. This is especially useful when local applications on the host requires actual IPv4 connectivity or cannot make use of <font SIZE="-1">DNS64 </font>(for example because they use legacy <font SIZE="-1">AF_INET</font> socket calls, or if they are simply not using <font SIZE="-1">DNS64</font>). </p>
<p> <code>clatd</code> may also be used to implement an SIIT-DC Edge Relay as described in <i></i><font SIZE="-1"><i>RFC 7756</i></font><i></i>. In this scenario, the <font SIZE="-1">PLAT</font> is in reality a SIIT-DC Border Relay (see <i></i><font SIZE="-1"><i>RFC 7755</i></font><i></i>) instead of a Stateful <font SIZE="-1">NAT64 </font>(see <i></i><font SIZE="-1"><i>RFC6146</i></font><i></i>). When used as a SIIT-DC Edge Relay, you will probably want to manually configure the settings <i>clat-v4-addr</i>, <i>clat-v6-addr</i>, and <i>plat-prefix</i> to mirror the SIIT-DC Border Relay&#8217;s configuration. </p>
<p> It relies on the software package <font SIZE="-1">TAYGA</font> by Nathan Lutchansky for the actual translation of packets between IPv4 and IPv6 (<i></i><font SIZE="-1"><i>RFC 6145</i></font><i></i>) <font SIZE="-1">TAYGA</font> may be downloaded from its home page at &lt;<a rel="nofollow" href="http://www.litech.org/tayga/">http://www.litech.org/tayga/</a>&gt;.</p>
<h2>Synopsis</h2>
<p><code>clatd</code> [options]</p>
<h2>Options</h2>
<dl>
<dt>-q</p>
<dd>Quiet mode; suppress normal output. This is the same as setting <code>quiet=1</code>. Warnings and errors are still outputted, to silence those too, repeat <i>-q</i>.</p>
<dt>-d</p>
<dd>Enable debugging output. This is the same as setting <code>debug=1</code>. Repeat for even more debugging output, which is the equivalent of setting <code>debug=2</code>.</p>
<dt>-c conf-file</p>
<dd>Read configuration settings from <code>conf-file</code>. See section <font SIZE="-1"><code>CONFIGURATION</code></font> below for more info.</p>
<dt>-h, &#8211;help</p>
<dd>Print a brief usage help and exit.</p>
<dt>key=value</p>
<dd>Set configuration <code>key</code> to <i>value</i>, overriding any setting found in the configuration file. Refer to the section <font SIZE="-1"><code>CONFIGURATION</code></font> below for more info.</dl>
<h2>Invocation</h2>
<p><code>clatd</code> is meant to be run under a daemonising control process such as systemd, upstart, or similar. It is further meant to be (re)started whenever a network interface goes up/down as this might mean a change in the <font SIZE="-1">PLAT</font> availability or which prefixes/addresses needs to be used for the <font SIZE="-1">CLAT</font> to work. It may also be run directly from the command line. It will run until killed with <font SIZE="-1">SIGINT </font>(^C) or <font SIZE="-1">SIGTERM,</font> at which point it will clean up after itself and exit gracefully. </p>
<p> See the <i>scripts/</i> directory in the source distribution for some examples on how to invoke it it.</p>
<h2>Installation</h2>
<p>The following commands will quickly download and install the latest version of <code>clatd</code> and its dependencies:</p>
<dl>
<dt>git clone <a rel="nofollow" href="https://github.com/toreanderson/clatd">https://github.com/toreanderson/clatd</a></p>
<dd>
<dt>sudo make -C clatd install installdeps</p>
<dd></dl>
<p> This will install <code>clatd</code> to /usr/sbin, plus install systemd, upstart, and/or NetworkManager scripts if your distribution appears to be using them, and install all the dependencies. Note that <font SIZE="-1">TAYGA</font> isn&#8217;t available in <font SIZE="-1">RPM</font> format, so on RedHat/Fedora the installdeps target will install gcc and attempt to compile <font SIZE="-1">TAYGA</font> from source.</p>
<h2>Configuration</h2>
<p><code>clatd</code> is designed to be able to run without any user-supplied configuration in most cases. However, user-specified onfiguration settings may be added to the configuration file, the path to which may be given on the command line using the <i>-c</i> option, or if it is not, the default location <i>/etc/clatd.conf</i> is used. Configuration settings may also be given directly on the command line when starting <code>clatd</code>, which takes precedence over settings in the configuration file. </p>
<p> Settings are of the form <code>key=value</code>. A list of recogniced keys and their possible values follow below:</p>
<dl>
<dt><code>quiet=integer</code> (default: <i>0</i>)</p>
<dd>Set this to 1 to suppress normal output from <code>clatd</code>. This is the same as providing the command line option <i>-q</i>. Set it to 2 to additionally suppress warnings and errors. Note that this does not suppress debugging output.</p>
<dt><code>debug=integer</code> (default: <i>0</i>)</p>
<dd>Set this to 1 to get debugging output from <code>clatd</code>, or 2 to get even more of the stuff. These are the equivalent of providing the command line option <i>-d</i> the specified number of times.</p>
<dt><code>script-up=string</code> (no default)</p>
<dd>Specify a custom script to be run when <code>clatd</code> is starting up. The invocation of this script is the last thing that happens before <font SIZE="-1">TAYGA</font> starts up, so all the preparations have been completed at that point (i.e., the <code>clat-dev</code> exists and has routing/addressing configured, forwarding has been enabled, and so on). </p>
<p> The script is run by the system shell, so you can do everything you could in an interactive shell: run multiple commands by separating them by semi-colon or double ampersands, use standard if/else statements, use variable substitutions, redirect output to files, set up command pipelines, and so on. However it must all be on one line, so if you want to do complex things or use some other programming language it&#8217;s probably better to put the script itself in a separate executable file and just make <code>script-up</code> invoke that file instead. </p>
<p> If the script returns a nonzero exit status, this is considered a fatal error, and <code>clatd</code> will abort. This can be prevented by appending <i>|| true</i> at the end of the script. </p>
<p> All of <code>clatd</code>&#8216;s configuration settings are available as standard variables in the script&#8217;s environment (hyphens are replaced with underscores). </p>
<p> Logging or debug messages from the script may simply be sent to stdout, where it will be picked up by the init system along with <code>clatd</code>&#8216;s own output. The script may of course consult the <i></i>$quiet<i></i> and <i></i>$debug<i></i> environment variables in order to determine how much output is appropriate. </p>
<p> The script should not be enclosed in quotes in the configuration file (even though it contains whitespace). For example: </p>
<p> <code>script-up=echo `date -Ins`: clatd started on </code>$clat_dev<code> | tee -a ~/clatd.log</code> </p>
<p> If on the other hand you want to supply a <code>script-up</code> containing whitespace directly <code>clatd</code>&#8216;s command line, quoting is required in order to prevent the shell from splitting it up and into multiple command line arguments. For example: </p>
<p> <code>clatd &#8216;script-up=ip route add 192.0.2.0/24 dev </code>$clat_dev<code> || true&#8217;</code></p>
<dt><code>script-down=string</code> (no default)</p>
<dd>This works exactly the same as <code>script-up</code>, only that this script is run right after <font SIZE="-1">TAYGA</font> has exited, before the clean-up process of restoring any settings that were changed. </p>
<p> An unsuccessful exit code from <code>script-down</code> will cause <code>clatd</code> to exit unsuccessfully too. Beyond that an unsuccessful exit won&#8217;t change anything, because <code>script-down</code> is invoked at a point in time where the only thing left for <code>clatd</code> to do is to clean up after itself and exit anyway.</p>
<dt><code>clat-dev=string</code> (default: <i>clat</i>)</p>
<dd>The name of the network device used by the <font SIZE="-1">CLAT.</font> There should be no reason to change the default, unless you plan on running multiple instances of <code>clatd</code> simultaneously.</p>
<dt><code>clat-v4-addr=ipv4-address</code> (default: <i>192.0.0.1</i>)</p>
<dd>The IPv4 address that will be assigned to the <font SIZE="-1">CLAT</font> device. Local applications will bind to this address when communicating with external IPv4 destinations. In a standard 464XLAT environment with a stateful <font SIZE="-1">NAT64</font> serving as the <font SIZE="-1">PLAT,</font> there should be no need to change the default. </p>
<p> When using <code>clatd</code> as an SIIT-DC Edge Relay (<i></i><font SIZE="-1"><i>RFC 7756</i></font><i></i>), you will want to set this to the IPv4 Service Address configured in the SIIT-DC Border Relay. This way, local applications can correctly identify which public address they&#8217;ll be using on the IPv4 internet, and will be able to provide fully functional references to it in application-level payload, and so on. </p>
<p> The default address is one from <i></i><font SIZE="-1"><i>RFC 7335</i></font><i></i>.</p>
<dt><code>clat-v6-addr=ipv6-address</code> (default: auto-generated)</p>
<dd>The IPv6 address of the <font SIZE="-1">CLAT.</font> Traffic to/from the <code>clat-v4-addr</code> will be translated into this address. When using <code>clatd</code> as an SIIT-DC Edge Relay, you will want to set this to the same IPv6 address in the Explicit Address Mapping configured in the SIIT-DC Border Relay. </p>
<p> By default, <code>clatd</code> will attempt to figure out which network device will be used for traffic towards the <font SIZE="-1">PLAT,</font> see if there is any SLAAC-based globally scoped addresses on it (i.e., a /64 with &#8216;0xfffe&#8217; in the middle of the Interface <font SIZE="-1">ID</font>), and will if so substitute that &#8216;0xfffe&#8217; value with &#8216;0xc1a7&#8217; (&#8220;clat&#8221;) to generate a <font SIZE="-1">CLAT</font> IPv6 address. </p>
<p> If only a non-SLAAC global address is found on the PLAT-facing device, <code>clatd</code> will substitute its Interface <font SIZE="-1">ID</font> with a random integer and use the result as the <font SIZE="-1">CLAT</font> IPv6 address. It will only do so if the prefix length is /120 or smaller, as otherwise the risk of <font SIZE="-1">IID</font> collisions is considered to be too high. Note that on most Perl platforms, the <i>rand()</i> function is limited to 48 bits, which means that for longer IIDs, the least significant bits will be all 0. </p>
<p> If multiple addresses are found in either category, the one that shares the longest common prefix with the <font SIZE="-1">PLAT</font> prefix will be preferred when deriving the <font SIZE="-1">CLAT</font> IPv6 address according to the algorithm described above.</p>
<dt><code>dns64-servers=srv1,[srv2,..]</code> (default: use system resolver)</p>
<dd>Comma-separated list of <font SIZE="-1">DNS64</font> servers to use when discovering the <font SIZE="-1">PLAT</font> prefix using the method described in <font SIZE="-1">RFC 7050.</font> By default, the system resolver is used, but it might be useful to override this in case your <font SIZE="-1">ISP</font> doesn&#8217;t provide you with a DNS64-enabled name server, and you want to test <code>clatd</code> using any of the public <font SIZE="-1">DNS64/NAT64</font> instances on the internet. The first <font SIZE="-1">PLAT</font> prefix encountered will be used.</p>
<dt><code>cmd-ip=path</code> (default: assume in $PATH)</p>
<dd>Path to the <code>ip</code> binary from the iproute2 package available at &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/net/iproute2">https://www.kernel.org/pub/linux/utils/net/iproute2</a>&gt;. Required.</p>
<dt><code>cmd-ip6tables=path</code> (default: assume in $PATH)</p>
<dd>Path to the <code>ip6tables</code> binary from the netfilter package available at &lt;<a rel="nofollow" href="http://netfilter.org">http://netfilter.org</a>&gt;. Only required for adding ip6tables rules (see the <code>ip6tables-enable</code> configuration setting).</p>
<dt><code>cmd-tayga=path</code> (default: assume in $PATH)</p>
<dd>Path to the <code>tayga</code> binary from the <font SIZE="-1">TAYGA</font> package available at &lt;<a rel="nofollow" href="http://www.litech.org/tayga">http://www.litech.org/tayga</a>&gt;. Required.</p>
<dt><code>forwarding-enable=bool</code> (default: <i>yes</i>)</p>
<dd>Controls whether or not <code>clatd</code> should enable IPv6 forwarding if necessary. IPv6 forwarding is necessary for <code>clatd</code> to work correctly. It will also ensure that the <i>accept_ra</i> sysctl is to &#8216;2&#8217; for all devices have it set to &#8216;1&#8217;, in order to prevent any connectivity loss as a result of enabling forwarding. </p>
<p> All sysctls that are modified will be restored to their original values when <code>clatd</code> is shutting down.</p>
<dt><code>ip6tables-enable=bool</code> (default: see below)</p>
<dd>Controls whether or not <code>clatd</code> should insert ip6tables rules that permit the forwarding of IPv6 traffic between the <font SIZE="-1">CLAT</font> and <font SIZE="-1">PLAT</font> devices. Such forwarding must be permitted for <code>clatd</code> to work correctly. Any rules added will be removed when <code>clatd</code> is shutting down. </p>
<p> The default is <i>yes</i> if the ip6tables_filter kernel module is loaded, <i>no</i> if it is not.</p>
<dt><code>plat-dev</code> (default: auto-detect)</p>
<dd>Which network device is facing the <font SIZE="-1">PLAT </font>(<font SIZE="-1">NAT64</font>). By default, this is auto-detected by performing a route table lookup towards the <font SIZE="-1">PLAT</font> prefix. This setting is used when setting up generating the <font SIZE="-1">CLAT</font> IPv6 address, and when setting up ip6tables rules and Proxy-ND entries.</p>
<dt><code>plat-prefix</code> (default: auto-detect)</p>
<dd>The IPv6 translation prefix into which the <font SIZE="-1">PLAT</font> maps the IPv4 internet. See <i></i><font SIZE="-1"><i>RFC 6052</i></font><i></i> for a closer description. By default, this is auto-detected from <font SIZE="-1">DNS64</font> answers using the method in <i></i><font SIZE="-1"><i>RFC 7050</i></font><i></i>.</p>
<dt><code>proxynd-enable</code> (default: <i>yes</i>)</p>
<dd>Controls whether or not <code>clatd</code> should add a Proxy-ND entry for the <font SIZE="-1">CLAT</font> IPv6 address on the network device facing the <font SIZE="-1">PLAT.</font> This is probably necessary on Ethernet networks (otherwise the upstream IPv6 router won&#8217;t know where to send packets to the <font SIZE="-1">CLAT</font>&#8216;s IPv6 adderss), but likely not necessary on point-to-point links like <font SIZE="-1">PPP</font> or 3GPP mobile broadband, as in those cases IPv6 <font SIZE="-1">ND</font> isn&#8217;t used. However it doesn&#8217;t hurt to add Proxy-ND entries in that case, either. </p>
<p> Any entries added wil be removed when <code>clatd</code> is shutting down.</p>
<dt><code>tayga-conffile</code> (default: use a temporary file)</p>
<dd>Where to write the <font SIZE="-1">TAYGA</font> configuration file. By default, a temporary file will be created (and also deleted when <code>clatd</code> is shutting down), but you may also specify an explicit configuration file here, which will not be deleted on shutdown.</p>
<dt><code>tayga-v4-addr</code> (default: <i>192.0.0.2</i>)</p>
<dd>The IPv4 address assigned to the <font SIZE="-1">TAYGA</font> process. This is used for emitting ICMPv4 errors back to the host (i.e., it will show up as the first hop when tracerouting to IPv4 destinations), and you may also ping it to verify that the <font SIZE="-1">TAYGA</font> process is still alive and well. </p>
<p> The default address is one from <i></i><font SIZE="-1"><i>RFC 7335</i></font><i></i>.</p>
<dt><code>v4-conncheck-enable=bool</code> (default: <i>yes</i>)</p>
<dd>Whether or not to check if the system has IPv4 connectivity before starting the <font SIZE="-1">CLAT.</font> If it does, then <code>clatd</code> will simply exit without doing anything. This is meant so that you can always enable <code>clatd</code> to the system startup scripts or network-up event scripts (such as NetworkManager&#8217;s dispatcher scripts), but not have <code>clatd</code> interfering with native IPv4 connectivity when this is present. </p>
<p> If you want to always start the <font SIZE="-1">CLAT</font> whenever possible, even though the system has IPv4 connectivity, disable this setting. You may instead use the <code>v4-defaultroute-enable</code> and <code>v4-defaultroute-metric</code> settings to prevent <code>clatd</code> from interfering with native IPv4 connectivity. </p>
<p> Note that enabling <code>v4-defaultroute-replace</code> will override <code>v4-conncheck-enable</code> and unconditionally disable IPv4 connectivity checking.</p>
<dt><code>v4-conncheck-delay=seconds</code> (default: <i>10</i>)</p>
<dd>When performing an IPv4 connectivity check, wait this number of seconds before actually doing anything. This is to avoid a race condition where for example IPv6 <font SIZE="-1">SLAAC</font> finshes and triggers a network-up event script to start <code>clatd</code>, while IPv4 DHCPv4 is still running in the background. This is at least a likely scenario when using NetworkManager, as it will start the dispatcher scripts as soon as either IPv4 or IPv6 has completed, and IPv6 <font SIZE="-1">SLAAC</font> is typically faster than IPv4 DHCPv4. </p>
<p> Set it to 0 to perform the check immediately.</p>
<dt><code>v4-defaultroute-enable=bool</code> (default: <i>yes</i>)</p>
<dd>Whether or not to add an IPv4 default route pointing to the <font SIZE="-1">CLAT.</font> In a typical 464XLAT environment, you want this. However when using <code>clatd</code> in an environment where native IPv4 connectivity is also present, you might want to disable this and instead control manually which IPv4 destinations is reached through the <font SIZE="-1">CLAT</font> and which are not.</p>
<dt><code>v4-defaultroute-replace=bool</code> (default: <i>no</i>)</p>
<dd>Instructs <code>clatd</code> to remove any pre-existing IPv4 default routes, replacing it with one pointing to the <font SIZE="-1">CLAT </font>(assuming <code>v4-defaultroute-enable</code> is <i>yes</i>). The replacement is temporary, any pre-existing routes that were removed will be restored when <code>clatd</code> is shutting down. </p>
<p> Note that nothing prevents software like a connection manager or a DHCPv4 client daemon from re-adding any replaced routes while <code>clatd</code> is running. </p>
<p> If you enable <code>v4-defaultroute-replace</code> while at the same time disabling <code>v4-defaultroute-enable</code>, <code>clatd</code> will remove any pre-existing IPv4 default routes but not add any of its own. </p>
<p> Setting <code>v4-defaultroute-replace</code> to <i>yes</i> will disable the IPv4 connectivity check.</p>
<dt><code>v4-defaultroute-metric=integer</code> (default: <i>2048</i>)</p>
<dd>The metric of the IPv4 default route pointing to the <font SIZE="-1">CLAT.</font> The default is chosen because it is higher than that of a native IPv4 default route added by NetworkManager, which makes it so that the native IPv4 connectivity is preferred if present.</p>
<dt><code>v4-defaultroute-mtu=integer</code> (default: <i>1260</i>)</p>
<dd>The <font SIZE="-1">MTU</font> of the default route pointing to the <font SIZE="-1">CLAT.</font> The default is the default IPv6 <font SIZE="-1">MTU</font> used by <font SIZE="-1">TAYGA </font>(1280, which in turn comes from <i></i><font SIZE="-1"><i>RFC 6145</i></font><i></i>) minus 20 to compensate for the difference in header size between IPv4 and IPv6. This prevents outbound packets from having to be fragmented by <font SIZE="-1">TAYGA,</font> and also makes local applications advertise a <font SIZE="-1">TCP MSS</font> to their remote peers that prevent them from sending packets beck to us that would require fragmentation. </p>
<p> If you know that the IPv6 Path <font SIZE="-1">MTU</font> between the host and the <font SIZE="-1">PLAT</font> is larger than 1280, you may increase this, but then you should also recompile <font SIZE="-1">TAYGA</font> with a larger <code>ipv6_offlink_mtu</code> setting in <i>conffile.c</i>.</p>
<dt><code>v4-defaultroute-advmss=integer</code> (default: <code>v4-defaultroute-mtu</code> &#8211; 40)</p>
<dd>The &#8220;advmss&#8221; value assigned to the the default route potining to the <font SIZE="-1">CLAT.</font> This controls the advertised <font SIZE="-1">TCP MSS</font> value for <font SIZE="-1">TCP</font> connections made through the <font SIZE="-1">CLAT.</font> </p>
<p> You should normally not need to set this. By default the value is calculated by taking the value of <code>v4-defaultroute-mtu</code> and substracting 40 (20 bytes for the IPv4 header + 20 bytes for the <font SIZE="-1">TCP</font> header). If <code>v4-defaultroute-mtu</code> is unset or 0, there is no default.</dl>
<h2>Limitations</h2>
<p><code>clatd</code> will not be able to acquire an IPv6 address for the <font SIZE="-1">CLAT</font> if <font SIZE="-1">SLAAC</font> isn&#8217;t used. <i></i><font SIZE="-1"><i>RFC 6877</i></font><i></i> suggests DHCPv6 <font SIZE="-1">IA_PD</font> should be attempted in this case, but this isn&#8217;t currently implemented. </p>
<p> <code>clatd</code> will not attempt to perform Duplicate Address Detection for the IPv6 address it generates. This is a violation of <i></i><font SIZE="-1"><i>RFC 6877</i></font><i></i>. </p>
<p> <code>clatd</code> will not attempt to perform a connectivity check to a discovered <font SIZE="-1">PLAT</font> prefix before setting up the <font SIZE="-1">CLAT,</font> as <i></i><font SIZE="-1"><i>RFC 7050</i></font><i></i> suggest it should.</p>
<h2>Bugs</h2>
<p>If you are experiencing any bugs or have any feature requests, head over to &lt;<a rel="nofollow" href="https://github.com/toreanderson/clatd/issues">https://github.com/toreanderson/clatd/issues</a>&gt; and submit a new issue (if someone else hasn&#8217;t already done so). Please make sure to include logs with full debugging output (using <i>-d -d</i> on the command line or <code>debug=2</code> in the configuration file) when reporting a bug.</p>
<h2>Licence</h2>
<p>Copyright (c) 2014-2016 Tore Anderson &lt;tore [at] fud.no&gt; </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &#8220;Software&#8221;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> <font SIZE="-1">THE SOFTWARE IS PROVIDED &#8220;AS IS&#8221;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</font></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ip/">ip</a></i>(8), <i><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></i>(8), <i><a href="/docs/linux/man/8-tayga/">tayga</a></i>(8), <i><a href="/docs/linux/man/5-tayga-conf/">tayga.conf</a></i>(5) <font SIZE="-1">RFC 6052, RFC 6145, RFC 6146, RFC 6877, RFC 7050, RFC 7335 RFC 7755, RFC 7756, RFC 7757</font> </p>
