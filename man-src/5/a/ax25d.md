---
title: "ax25d(5)"
name: "ax25d"
section: "5"
letter: "a"
url: "/docs/linux/man/5-ax25d/"
description: "ax25d.conf – ax25d configuration file."
---

<p>ax25d.conf &#8211; ax25d configuration file.</p>
<h2>Description</h2>
<p><code>Ax25d.conf</code> controls the functioning of <code>ax25d.</code> Its purpose is to specify on which ports to listen on, which applications are available, and to whom they are available to. The configuration file is common to both AX.25, NET/ROM and Rose and their is similarity between the two parts of the file. The general layout for an entry for a given port is as follows:</p>
<dl>
<dd>interface control<br />
 callsign entry 1 </p>
<p>&nbsp;<wbr>. </p>
<p>&nbsp;<wbr>.<br />
 callsign entry n</dl>
<p> The <code>interface control</code> line determines which port and callsigns apply to the following <code>callsign entry</code> lines, until the next <code>interface control</code> is read. There are four different variants of the <code>interface control</code> line:</p>
<dl>
<dd>1. [AX.25 Port Name]<br />
 2. [Callsign VIA AX.25 Port Name]<br />
 3. &lt;NET/ROM Port Name&gt;<br />
 4. {Callsign VIA Rose Port Name}</dl>
<p> Version 1 allows the following <code>callsign entry</code> lines to listen on the AX.25 port specified by the AX.25 port name using the default callsign of that AX.25 port. Version 2 allows the following <code>callsign entry</code> lines to listen on the AX.25 port specified by the AX.25 port name using the callsign specified instead of the default callsign of that AX.25 port. Specifying a * for the AX.25 port name allows the following <code>callsign entries</code> to be valid for all the operating AX.25 ports using the callsign specified. VIA can be abbreviated to just V. If the callsign has an asterisk appended to it then the system will be listening on the port with the callsign, but as a pseudo-digipeater instead of being the normal destination callsign. Version 3 allows the following <code>callsign entry</code> lines to listen on the NET/ROM port specified by the NET/ROM port name using the default callsign of that NET/ROM port. Version 4 allows the following <code>callsign entry</code> lines to listen on the Rose port using the specified Rose port name using the callsign specified as the service access point (SAP). A * may be specified for a callsign to allow matching to any incoming Call Requests with any SAP. The <code>callsign entry</code> lines have a similar layout for both AX.25, NET/ROM and Rose, the layout is:</p>
<dl>
<dd>peer window t1 t2 t3 idle n2 mode uid exec args&#8230;</dl>
<p> All values must be entered for all entries even when they are not used (ie window for NET/ROM, just enter a * instead), The meanings of each of the fields is given below. All timings apart from the idle value are given in seconds, the idle values is given in minutes.</p>
<dl>
<dd>
<dl>
<dt><code>peer</code></p>
<dd>This specifies the callsign of the remote end of the connection that should have the following parameters and executable set up for them. The syntax of the peer argument is explained below.</p>
<dt><code>window</code></p>
<dd>This sets the the value of the window size, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used. This entry is used by AX.25 but not by NET/ROM or Rose.</p>
<dt><code>t1</code></p>
<dd>This sets the the value of the T1 timer, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used. This entry is used by both AX.25 and NET/ROM but not by Rose.</p>
<dt><code>t2</code></p>
<dd>This sets the the value of the T2 timer, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used. This entry is used by both AX.25 and NET/ROM but not by Rose.</p>
<dt><code>t3</code></p>
<dd>This sets the the value of the T3 timer, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used. This entry is used by AX.25 but not by NET/ROM or Rose.</p>
<dt><code>idle</code></p>
<dd>This sets the the value of the idle timer, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used.</p>
<dt><code>n2</code></p>
<dd>This sets the the value of the N2 counter, if a value of * is entered in this field then the default value for the port is taken from the lqparametersrq entry (see below) or lacking such an entry, the kernel default value is used. This entry is used by both AX.25 and NET/ROM but not by Rose.</p>
<dt><code>mode</code></p>
<dd>This is a set of flags that control the various properties associated with the incoming connection. The flags are single letters, may be in either upper or lower case, and there may not be any spaces between them. If no flags are to be specified either a 0, &#8211; or a * must be entered instead. The valid mode flag letters are:</p>
<dl>
<dd>
<dl>
<dt><code>D</code></p>
<dd>Do not allow connections that have passed via any digi-peaters. AX.25 only.</p>
<dt><code>L</code></p>
<dd>Do not allow this station to connect, they are Locked out.</p>
<dt><code>N</code></p>
<dd>Check that the NET/ROM neighbour is allowed, currently unused.</p>
<dt><code>Q</code></p>
<dd>Do not make an entry into the log file for this connection.</p>
<dt><code>V</code></p>
<dd>Validate the callsign of the incoming connection, currently unused.</dl>
</dl>
<dt><code>uid</code></p>
<dd>This is the userid that the following command should run under when executing.</p>
<dt><code>exec</code></p>
<dd>This is the executable that should be executed when an incoming connection matches the criteria of both the <code>interface control</code> and the <code>callsign entry.</code></p>
<dt><code>args&#8230;</code></p>
<dd>These are the optional arguments that are passed to the executable. All of the arguments are passed literally apart from the following:</p>
<dl>
<dd>
<dl>
<dt><code>%d</code></p>
<dd>The name of the port that the connection is on.</p>
<dt><code>%U</code></p>
<dd>The username (callsign) of the remote station in upper case without the SSID.</p>
<dt><code>%u</code></p>
<dd>The username (callsign) of the remote station in lower case without the SSID.</p>
<dt><code>%S</code></p>
<dd>The username (callsign) of the remote station in upper case with the SSID.</p>
<dt><code>%s</code></p>
<dd>The username (callsign) of the remote station in lower case with the SSID.</p>
<dt><code>%P</code></p>
<dd>The nodename of the remote station in upper case without the SSID. This is only valid under NET/ROM and Rose, under AX.25 a % is substituted instead.</p>
<dt><code>%p</code></p>
<dd>The nodename of the remote station in lower case without the SSID. This is only valid under NET/ROM and Rose, under AX.25 a % is substituted instead.</p>
<dt><code>%R</code></p>
<dd>The nodename of the remote station in upper case with the SSID. This is only valid under NET/ROM and Rose, under AX.25 a % is substituted instead.</p>
<dt><code>%r</code></p>
<dd>The nodename of the remote station in lower case with the SSID. This is only valid under NET/ROM and Rose, under AX.25 a % is substituted instead.</p>
<dt><code>%%</code></p>
<dd>A %.</dl>
</dl>
</dl>
</dl>
<p> The <code>peer</code> argument is dependant upon whether AX.25, NET/ROM or Rose is being used. There are five formats of this argument:</p>
<dl>
<dd>1. default<br />
 2. parameters<br />
 3. callsign<br />
 4. callsign [at] node<br />
 5. @node</dl>
<p> The first version is used by AX.25, NET/ROM and Rose to specify that all callsigns on a given port are to be matched. The default line is usually the last of the <code>callsign entry</code> lines, so that more specific entries may have the chance to be matched first. The second version is not a <code>callsign entry</code> that is used by any incoming connections. It is a means to specify default values for parameters such as Window, T1, T2, T3, Idle and N2. It is used for both AX.25, NET/ROM and Rose. The third version is used by both AX.25, NET/ROM and Rose to specify the callsign of the remote station to match the <code>callsign entry</code> line. If no SSID is specified then the callsign will be matched with any that has the same callsign and any SSID. Specifying an SSID causes the callsign to be matched exactly. In the case of NET/ROM and Rose this entry does not specify which node the originating callsign comes from. The fourth version is used by NET/ROM and Rose to specify the callsign of the remote station and the remote node to match the <code>callsign entry</code> line. If no SSID is specified in the callsign section then the callsign will be matched with any that has the same callsign and any SSID. Specifying an SSID causes the callsign to be matched exactly. The fifth version is used by NET/ROM and Rose to specify only the address of the remote node to match the <code>callsign entry</code> line. This entry will mean that all remote users at the given node will match the entry. Comments may be embedded in the configuration file by placing a # in the first column. ax25d can now honour AX.25 TCP/IP mode-VC connections in a special way. Therefore, a new port specific option &quot;parameters_extAX25&quot; is available, with the following options, which are seperated by space.</p>
<dl>
<dt>parameters_extAX25</p>
<dd>VC-debug<br />
 VC-reject-login|VC-wait-login|VC-login-ok<br />
 VC-disc-on-linkfailure-msg, VC-send-failure-msg, VC-log-connections<br />
 Recommended settings in ax25d.conf: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>parameters_extAX25 VC-wait-login VC-disc-on-linkfailure-msg VC-log-connections<br />
 or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>parameters_extAX25 VC-reject-login VC-send-failure-msg VC-log-connections </p>
<h2>Files</h2>
<p>/etc/ax25/ax25d.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/5-nrports/">nrports</a></code>(5), <code><a href="/docs/linux/man/5-rsports/">rsports</a></code>(5), <code><a href="/docs/linux/man/8-ax25d/">ax25d</a></code>(8). </p>
