---
title: "ipmi-console(8)"
name: "ipmi-console"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi-console/"
description: "ipmiconsole – IPMI console utility"
---

<p>ipmiconsole &#8211; IPMI console utility</p>
<h2>Synopsis</h2>
<p><code>ipmiconsole</code> [<i>OPTION</i>&#8230;]</p>
<h2>Description</h2>
<p><code>ipmiconsole</code> is a Serial-over-LAN (SOL) console utility. It can be used to establish console sessions to remote machines using the IPMI 2.0 SOL protocol. <code>Ipmiconsole</code> communicates with a remote machine&#8217;s Baseboard Management Controller (BMC) to establish a console session. Before any SOL communication can take place, the remote machine&#8217;s BMC must be configured properly. The FreeIPMI tool <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> may be used to do this configuration. </p>
<p> Often (although not always), console redirection must be also be configured properly in the BIOS and/or operating system. Both must be configured to redirect console traffic out the appropriate COM port. Please see your motherboard and OS documentation for instructions on proper setup. </p>
<p> Listed below are general IPMI options, tool specific options, trouble shooting information, workaround information, examples, and known issues. For a general introduction to FreeIPMI please see <code><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7).</code></p>
<h2>General Options</h2>
<p>The following options are general options for configuring IPMI communication and executing general tool commands.</p>
<dl>
<dt><code>-h</code> <i>IPMIHOSTFR, </i><code>&#8211;hostname</code>=<i>IPMIHOST[:PORT]</i></p>
<dd>Specify the remote host to communicate with. An optional port can be specified, which may be useful in port forwarding or similar situations.</p>
<dt><code>-u</code>, <code>&#8211;username</code>=<i>USERNAME</i></p>
<dd>Specify the username to use when authenticating with the remote host. If not specified, a null (i.e. anonymous) username is assumed. The user must a high enough privilege to establish a SOL session and have SOL session abilities.</p>
<dt><code>-p</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd>Specify the password to use when authenticationg with the remote host. If not specified, a null password is assumed. Maximum password length is 16 for IPMI 1.5 and 20 for IPMI 2.0.</p>
<dt><code>-P</code>, <code>&#8211;password-prompt</code></p>
<dd>Prompt for password to avoid possibility of listing it in process lists.</p>
<dt><code>-k</code> <i>K_G</i>, <code>&#8211;k-g</code>=<i>K_G</i></p>
<dd>Specify the K_g BMC key to use when authenticating with the remote host for IPMI 2.0. If not specified, a null key is assumed. To input the key in hexadecimal form, prefix the string with &#8216;0x&#8217;. E.g., the key &#8216;abc&#8217; can be entered with the either the string &#8216;abc&#8217; or the string &#8216;0x616263&#8217;</p>
<dt><code>-K</code>, <code>&#8211;k-g-prompt</code></p>
<dd>Prompt for k-g to avoid possibility of listing it in process lists.</p>
<dt><code>&#8211;session-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the session timeout in milliseconds. Defaults to 60000 milliseconds (60 seconds) if not specified.</p>
<dt><code>&#8211;retransmission-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the packet retransmission timeout in milliseconds. Defaults to 500 milliseconds (0.5 seconds) if not specified.</p>
<dt><code>-I</code>, <code>&#8211;cipher-suite-id</code>=<i>CIPHER-SUITE-ID</i></p>
<dd>Specify the IPMI 2.0 cipher suite ID to use. The Cipher Suite ID identifies a set of authentication, integrity, and confidentiality algorithms to use for IPMI 2.0 communication. The authentication algorithm identifies the algorithm to use for session setup, the integrity algorithm identifies the algorithm to use for session packet signatures, and the confidentiality algorithm identifies the algorithm to use for payload encryption. Defaults to cipher suite ID 3 if not specified. The user should be aware that only cipher suite ids 3, 8, and 12 encrypt console payloads. Console information will be sent in the clear if an alternate cipher suite id is selected. The following cipher suite ids are currently supported: </p>
<p> 0 &#8211; Authentication Algorithm = None; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 1 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 2 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = None </p>
<p> 3 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 6 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 7 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = None </p>
<p> 8 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 11 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = None </p>
<p> 12 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 15 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 16 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = None </p>
<p> 17 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = AES-CBC-128</p>
<dt><code>-l</code> <i>PRIVILEGE-LEVEL</i>, <code>&#8211;privilege-level</code>=<i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the privilege level to be used. The currently available privilege levels are USER, OPERATOR, and ADMIN. Defaults to ADMIN if not specified.</p>
<dt><code>&#8211;config-file</code>=<i>FILE</i></p>
<dd>Specify an alternate configuration file.</p>
<dt><code>-W</code> <i>WORKAROUNDS</i>, <code>&#8211;workaround-flags</code>=<i>WORKAROUNDS</i></p>
<dd>Specify workarounds to vendor compliance issues. Multiple workarounds can be specified separated by commas. A special command line flag of &quot;none&quot;, will indicate no workarounds (may be useful for overriding configured defaults). See WORKAROUNDS below for a list of available workarounds.</p>
<dt><code>&#8211;debug</code></p>
<dd>Turn on debugging.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Output a help list and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output the program version and exit.</dl>
<h2>Ipmiconsole Options</h2>
<p>The following options are specific to <code>Ipmiconsole.</code></p>
<dl>
<dt><code>-e</code> <i>CHAR</i>, <code>&#8211;escape-char</code>=<i>CHAR</i></p>
<dd>Specify an alternate escape character (default char &#8216;&amp;&#8217;).</p>
<dt><code>&#8211;dont-steal</code></p>
<dd>Do not steal an SOL session if one is already detected as being in use. Under most circumstances, if SOL is detected as being in use, <code>ipmiconsole</code> will attempt to steal the SOL session away from the previous session. This default behavior exists for several reasons, most notably that earlier SOL sessions may have not been able to be deactivate properly.</p>
<dt><code>&#8211;deactivate</code></p>
<dd>Deactivate SOL session if one is detected as being in use and exit.</p>
<dt><code>&#8211;serial-keepalive</code></p>
<dd>Occasionally send NUL characters to detect inactive serial connections. This option is particularly useful for those who intend to run <code>ipmiconsole</code> without much interaction, such as for logging purposes. While IPMI connections may still be alive, some motherboards have exhibited bugs in which underlying serial data can no longer be sent/received. From the viewpoint of <code>ipmiconsole,</code> data is simply not be sent out of the remote system and this problem is only detected once there is user interaction. By sending the occasional NUL character, the underlying loss of serial data transfer can be detected far more quickly. There is some risk with this option, as the NUL character byte may affect the remote system depending on what data it may or may not be expecting.</p>
<dt><code>&#8211;serial-keepalive-empty</code></p>
<dd>This option is identical to <code>&#8211;serial-keepalive</code> except that SOL packets will contain no NUL character data. On some motherboards, this may be sufficient to deal with a hanging IPMI session without the risk regularly sending a NUL character byte may have. However, some systems may not ACK a SOL packet without character data in it, meaning these keepalive packets do nothing.</p>
<dt><code>&#8211;sol-payload-instance</code>=<i>NUM</i></p>
<dd>Specify the SOL payload instance number. The default value is 1, valid values range from 1 to 15. Most systems only support a single instance, however a few allow users to access multiple.</p>
<dt><code>&#8211;deactivate-all-instances</code></p>
<dd>When used along with the <code>&#8211;deactivate</code> option, will deactivate all active SOL instances instead of just the currently configured payload instance.</p>
<dt><code>&#8211;lock-memory</code></p>
<dd>Lock sensitive information (such as usernames and passwords) in memory.</dl>
<h2>Escape Characters</h2>
<p>The following escape sequences are supported. The default supported escape character is &#8216;&amp;&#8217;, but can be changed with the <code>-e</code> option.</p>
<dl>
<dt><i>&amp;?</i></p>
<dd>Display a list of currently available escape sequences.</p>
<dt><i>&amp;.</i></p>
<dd>Terminate the connection.</p>
<dt><i>&amp;B</i></p>
<dd>Send a &quot;serial-break&quot; to the remote console.</p>
<dt><i>&amp;D</i></p>
<dd>Send a DEL character.</p>
<dt><i>&amp;&amp;</i></p>
<dd>Send a single escape character.</dl>
<h2>General Troubleshooting</h2>
<p>Most often, IPMI problems are due to configuration problems. </p>
<p> IPMI over LAN problems involve a misconfiguration of the remote machine&#8217;s BMC. Double check to make sure the following are configured properly in the remote machine&#8217;s BMC: IP address, MAC address, subnet mask, username, user enablement, user privilege, password, LAN privilege, LAN enablement, and allowed authentication type(s). For IPMI 2.0 connections, double check to make sure the cipher suite privilege(s) and K_g key are configured properly. The <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool can be used to check and/or change these configuration settings. </p>
<p> In addition to the troubleshooting tips below, please see WORKAROUNDS below to also if there are any vendor specific bugs that have been discovered and worked around. </p>
<p> Listed below are many of the common issues for error messages. For additional support, please e-mail the &lt;freeipmi-users [at] gnu.org&gt; mailing list. </p>
<p> &quot;username invalid&quot; &#8211; The username entered (or a NULL username if none was entered) is not available on the remote machine. It may also be possible the remote BMC&#8217;s username configuration is incorrect. </p>
<p> &quot;password invalid&quot; &#8211; The password entered (or a NULL password if none was entered) is not correct. It may also be possible the password for the user is not correctly configured on the remote BMC. </p>
<p> &quot;password verification timeout&quot; &#8211; Password verification has timed out. A &quot;password invalid&quot; error (described above) or a generic &quot;session timeout&quot; (described below) occurred. During this point in the protocol it cannot be differentiated which occurred. </p>
<p> &quot;k_g invalid&quot; &#8211; The K_g key entered (or a NULL K_g key if none was entered) is not correct. It may also be possible the K_g key is not correctly configured on the remote BMC. </p>
<p> &quot;privilege level insufficient&quot; &#8211; An IPMI command requires a higher user privilege than the one authenticated with. Please try to authenticate with a higher privilege. This may require authenticating to a different user which has a higher maximum privilege. </p>
<p> &quot;privilege level cannot be obtained for this user&quot; &#8211; The privilege level you are attempting to authenticate with is higher than the maximum allowed for this user. Please try again with a lower privilege. It may also be possible the maximum privilege level allowed for a user is not configured properly on the remote BMC. </p>
<p> &quot;authentication type unavailable for attempted privilege level&quot; &#8211; The authentication type you wish to authenticate with is not available for this privilege level. Please try again with an alternate authentication type or alternate privilege level. It may also be possible the available authentication types you can authenticate with are not correctly configured on the remote BMC. </p>
<p> &quot;cipher suite id unavailable&quot; &#8211; The cipher suite id you wish to authenticate with is not available on the remote BMC. Please try again with an alternate cipher suite id. It may also be possible the available cipher suite ids are not correctly configured on the remote BMC. </p>
<p> &quot;ipmi 2.0 unavailable&quot; &#8211; IPMI 2.0 was not discovered on the remote machine. Please try to use IPMI 1.5 instead. </p>
<p> &quot;connection timeout&quot; &#8211; Initial IPMI communication failed. A number of potential errors are possible, including an invalid hostname specified, an IPMI IP address cannot be resolved, IPMI is not enabled on the remote server, the network connection is bad, etc. Please verify configuration and connectivity. </p>
<p> &quot;session timeout&quot; &#8211; The IPMI session has timed out. Please reconnect. If this error occurs often, you may wish to increase the retransmission timeout. Some remote BMCs are considerably slower than others. </p>
<p> &quot;internal IPMI error&quot; &#8211; An IPMI error has occurred that FreeIPMI does not know how to handle. Please e-mail &lt;freeipmi-users [at] gnu.org&gt; to report the issue.</p>
<h2>Ipmiconsole Troubleshooting</h2>
<p>The following are common issues for error messages in <code>ipmiconsole.</code> </p>
<p> &quot;SOL unavailable&quot; &#8211; SOL is not configured for use on the remote BMC. It may be not configured in general or for the specific user specified. Authenticating with a different user may be sufficient, however the IPMI protocol does not reveal detail on what is not configured on the remote BMC. </p>
<p> &quot;SOL in use&quot; &#8211; SOL is already in use on the remote BMC. If you do not specify the <i>&#8211;dont-steal</i> option, <code>ipmiconsole</code> will attempt to steal the SOL session away from the other session. Not all BMCs support the ability to steal away a SOL session. </p>
<p> &quot;SOL session stolen&quot; &#8211; Your SOL session has been stolen by another session. You may wish to try and steal the session back by reconnecting. </p>
<p> &quot;SOL requires encryption&quot; &#8211; SOL requires a cipher suite id that includes encryption. Please try to use cipher suite id 3, 8, or 12. It may also be possible the encryption requirements are not configured correctly on the remote BMC. </p>
<p> &quot;SOL requires no encryption&quot; &#8211; SOL requires a cipher suite id that does not use encryption. Please try to use cipher suite id 0, 1, 2, 6, 7, or 11. It may also be possible the encryption requirements are not configured correctly on the remote BMC. </p>
<p> &quot;BMC Implementation&quot; &#8211; The BMC on the remote machine has a severe problem in its implementation. Please see the WORKAROUNDS section below for possible workarounds. If additional vendor workarounds are required, please contact the authors. </p>
<p> &quot;excess retransmissions sent&quot; &#8211; An excessive number of retransmissions of SOL packets has occurred and <code>ipmiconsole</code> has given up. This may be due to network issues or SOL issues. Some of the same issues involved with &quot;connection timeout&quot; or &quot;session timeout&quot; errors may be involved. Please try to reconnect. </p>
<p> &quot;excess errors received&quot; &#8211; An excessive number of SOL packet errors has occurred and <code>ipmiconsole</code> has given up. This may be due to network issues or SOL issues. Please try to reconnect. </p>
<p> &quot;BMC Error&quot; &#8211; This error usually means a vendor SOL implementation requires a combination of authentication, encryption, privilege, etc. that have not been met by the user&#8217;s choices. Please try a combination of different cipher suites, privileges, etc. to resolve the problem. Please see the WORKAROUNDS section below for possible workarounds too.</p>
<h2>Workarounds</h2>
<p>With so many different vendors implementing their own IPMI solutions, different vendors may implement their IPMI protocols incorrectly. The following describes a number of workarounds currently available to handle discovered compliance issues. When possible, workarounds have been implemented so they will be transparent to the user. However, some will require the user to specify a workaround be used via the -W option. </p>
<p> The hardware listed below may only indicate the hardware that a problem was discovered on. Newer versions of hardware may fix the problems indicated below. Similar machines from vendors may or may not exhibit the same problems. Different vendors may license their firmware from the same IPMI firmware developer, so it may be worthwhile to try workarounds listed below even if your motherboard is not listed. </p>
<p> If you believe your hardware has an additional compliance issue that needs a workaround to be implemented, please contact the FreeIPMI maintainers on &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;. </p>
<p> <i>authcap</i> &#8211; This workaround flag will skip early checks for username capabilities, authentication capabilities, and K_g support and allow IPMI authentication to succeed. It works around multiple issues in which the remote system does not properly report username capabilities, authentication capabilities, or K_g status. Those hitting this issue may see &quot;username invalid&quot;, &quot;authentication type unavailable for attempted privilege level&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Asus P5M2/P5MT-R/RS162-E4/RX4, Intel SR1520ML/X38ML, and Sun Fire 2200/4150/4450 with ELOM. </p>
<p> <i>nochecksumcheck</i> &#8211; This workaround flag will tell FreeIPMI to not check the checksums returned from IPMI command responses. It works around systems that return invalid checksums due to implementation errors, but the packet is otherwise valid. Users are cautioned on the use of this option, as it removes validation of packet integrity in a number of circumstances. However, it is unlikely to be an issue in most situations. Those hitting this issue may see &quot;connection timeout&quot;, &quot;session timeout&quot;, or &quot;password verification timeout&quot; errors. On IPMI 1.5 connections, the &quot;noauthcodecheck&quot; workaround may also needed too. Issue observed on Supermicro X9SCM-iiF, Supermicro X9DRi-F, and Supermicro X9DRFR. </p>
<p> <i>intel20</i> &#8211; This workaround flag will work around several Intel IPMI 2.0 authentication issues. The issues covered include padding of usernames, and password truncation if the authentication algorithm is HMAC-MD5-128. Those hitting this issue may see &quot;username invalid&quot;, &quot;password invalid&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Intel SE7520AF2 with Intel Server Management Module (Professional Edition). </p>
<p> <i>supermicro20</i> &#8211; This workaround flag will work around several Supermicro IPMI 2.0 authentication issues on motherboards w/ Peppercon IPMI firmware. The issues covered include handling invalid length authentication codes. Those hitting this issue may see &quot;password invalid&quot; errors. Issue observed on Supermicro H8QME with SIMSO daughter card. Confirmed fixed on newerver firmware. </p>
<p> <i>sun20</i> &#8211; This workaround flag will work work around several Sun IPMI 2.0 authentication issues. The issues covered include invalid lengthed hash keys, improperly hashed keys, and invalid cipher suite records. Those hitting this issue may see &quot;password invalid&quot; or &quot;bmc error&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM. This workaround automatically includes the &quot;opensesspriv&quot; workaround. </p>
<p> <i>opensesspriv</i> &#8211; This workaround flag will slightly alter FreeIPMI&#8217;s IPMI 2.0 connection protocol to workaround an invalid hashing algorithm used by the remote system. The privilege level sent during the Open Session stage of an IPMI 2.0 connection is used for hashing keys instead of the privilege level sent during the RAKP1 connection stage. Those hitting this issue may see &quot;password invalid&quot;, &quot;k_g invalid&quot;, or &quot;bad rmcpplus status code&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM, Inventec 5441/Dell Xanadu II, Supermicro X8DTH, Supermicro X8DTG, Intel S5500WBV/Penguin Relion 700, Intel S2600JF/Appro 512X, and Quanta QSSC-S4R/Appro GB812X-CN. This workaround is automatically triggered with the &quot;sun20&quot; workaround. </p>
<p> <i>integritycheckvalue</i> &#8211; This workaround flag will work around an invalid integrity check value during an IPMI 2.0 session establishment when using Cipher Suite ID 0. The integrity check value should be 0 length, however the remote motherboard responds with a non-empty field. Those hitting this issue may see &quot;k_g invalid&quot; errors. Issue observed on Supermicro X8DTG, Supermicro X8DTU, and Intel S5500WBV/Penguin Relion 700, and Intel S2600JF/Appro 512X. </p>
<p> <i>solpayloadsize</i> &#8211; This workaround flag will not check for valid SOL payload sizes and assume a proper set. It works around remote systems that report invalid IPMI 2.0 SOL payload sizes. Those hitting this issue may see &quot;BMC Implementation&quot; errors. Issue observed on Asus P5M2/RS162-E4/RX4, Intel SR1520ML/X38ML, Inventec 5441/Dell Xanadu II, Sun x4100, Supermicro X8DTH, Supermicro X8DTG, Supermicro X8DTU, and Quanta QSSC-S4R//Appro GB812X-CN. </p>
<p> <i>solport</i> &#8211; This workaround flag will ignore alternate SOL ports specified during the protocol. It works around remote systems that report invalid alternate SOL ports. Those hitting this issue may see &quot;connection timeout&quot; errors. Issue observed on Asus P5MT-R and Supermicro X8DTH-iF. </p>
<p> <i>solstatus</i> &#8211; This workaround flag will not check the current activation status of SOL during the protocol setup. It works around remote systems that do not properly support this command. Those hitting this issue may see &quot;BMC Error&quot; errors. Issue observed on Supermicro X8SIL-F.</p>
<h2>Known Issues</h2>
<p>On older operating systems, if you input your username, password, and other potentially security relevant information on the command line, this information may be discovered by other users when using tools like the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command or looking in the /proc file system. It is generally more secure to input password information with options like the -P or -K options. Configuring security relevant information in the FreeIPMI configuration file would also be an appropriate way to hide this information. </p>
<p> In order to prevent brute force attacks, some BMCs will temporarily &quot;lock up&quot; after a number of remote authentication errors. You may need to wait awhile in order to this temporary &quot;lock up&quot; to pass before you may authenticate again. </p>
<p> Some motherboards define an OEM SOL inactivity timeout for SOL sessions. If SOL sessions stay inactive for long periods of time, <code>ipmiconsole</code> sessions may be abruptly closed, most likely resulting in session timeout errors. Please see OEM notes for information on modifying this parameter if you wish for sessions to stay active longer.</p>
<h2>Specific Hardware Notes</h2>
<p>Intel SR1520ML/X38ML: After a reboot, the SOL session appears to &quot;disconnect&quot; from the motherboard but stay alive. Character data input from the <code>ipmiconsole</code> client is accepted by the remote machine, but no character data or console data is ever sent back from the remote machine. The SOL session is subsequently useless. There is currently no workaround in place to handle this. The session must be closed and restarted.</p>
<h2>Examples</h2>
<p><code># ipmiconsole -h ahost -u myusername -p mypassword</code> Establish a console sesssion with a remote host. </p>
<h2>Known Issues</h2>
<p>On older operating systems, if you input your username, password, and other potentially security relevant information on the command line, this information may be discovered by other users when using tools like the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command or looking in the /proc file system. It is generally more secure to input password information with options like the -P or -K options. Configuring security relevant information in the FreeIPMI configuration file would also be an appropriate way to hide this information. </p>
<p> In order to prevent brute force attacks, some BMCs will temporarily &quot;lock up&quot; after a number of remote authentication errors. You may need to wait awhile in order to this temporary &quot;lock up&quot; to pass before you may authenticate again.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2006-2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5), <a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
