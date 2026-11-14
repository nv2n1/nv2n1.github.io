---
title: "in-tftpd(8)"
name: "in-tftpd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-tftpd/"
description: "tftpd – Trivial File Transfer Protocol server"
---

<p><code>tftpd</code> &#8211; Trivial File Transfer Protocol server</p>
<h2>Synopsis</h2>
<p><code>in.tftpd</code> [<i>options&#8230;</i>] <i>directory&#8230;</i></p>
<h2>Description</h2>
<p><code>tftpd</code> is a server for the Trivial File Transfer Protocol. The TFTP protocol is extensively used to support remote booting of diskless devices. The server is normally started by <code>inetd</code>, but can also run standalone. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;ipv4</code>, <code>-4</code></p>
<dd>Connect with IPv4 only, even if IPv6 support was compiled in.</p>
<dt><code>&#8211;ipv6</code>, <code>-6</code></p>
<dd>Connect with IPv6 only, if compiled in.</p>
<dt><code>-l</code>, <code>&#8211;listen</code></p>
<dd>Run the server in standalone (listen) mode, rather than run from <code>inetd</code>. In listen mode, the <code>&#8211;timeout</code> option is ignored, and the <code>&#8211;address</code> option can be used to specify a specific local address or port to listen to.</p>
<dt><code>&#8211;foreground</code>, <code>-L</code></p>
<dd>Similar to <code>&#8211;listen</code> but do not detach from the foreground process. Implies <code>&#8211;listen</code>.</p>
<dt><code>&#8211;address</code> <i>[address][:port]</i>, <code>-a</code> <i>[address][:port]</i></p>
<dd>Specify a specific <i>address</i> and <i>port</i> to listen to when called with the <code>&#8211;listen</code> or <code>&#8211;foreground</code> option. The default is to listen to the <i>tftp</i> port specified in <i>/etc/services</i> on all local addresses. </p>
<p> <code>Please note:</code> Numeric IPv6 adresses must be enclosed in square brackets to avoid ambiguity with the optional port information.</p>
<dt><code>&#8211;create</code>, <code>-c</code></p>
<dd>Allow new files to be created. By default, <code>tftpd</code> will only allow upload of files that already exist. Files are created with default permissions allowing anyone to read or write them, unless the <code>&#8211;permissive</code> or <code>&#8211;umask</code> options are specified.</p>
<dt><code>&#8211;secure</code>, <code>-s</code></p>
<dd>Change root directory on startup. This means the remote host does not need to pass along the directory as part of the transfer, and may add security. When <code>&#8211;secure</code> is specified, exactly one <i>directory</i> should be specified on the command line. The use of this option is recommended for security as well as compatibility with some boot ROMs which cannot be easily made to include a directory name in its request.</p>
<dt><code>&#8211;user</code> <i>username</i>, <code>-u</code> <i>username</i></p>
<dd>Specify the username which <code>tftpd</code> will run as; the default is &quot;nobody&quot;. The user ID, group ID, and (if possible on the platform) the supplementary group IDs will be set to the ones specified in the system permission database for this username.</p>
<dt><code>&#8211;umask</code> <i>umask</i>, <code>-U</code> <i>umask</i></p>
<dd>Sets the <i>umask</i> for newly created files to the specified value. The default is zero (anyone can read or write) if the <code>&#8211;permissive</code> option is not specified, or inherited from the invoking process if <code>&#8211;permissive</code> is specified.</p>
<dt><code>&#8211;permissive</code>, <code>-p</code></p>
<dd>Perform no additional permissions checks above the normal system-provided access controls for the user specified via the <code>&#8211;user</code> option.</p>
<dt><code>&#8211;pidfile</code> <i>pidfile</i>, <code>-P</code> <i>pidfile</i></p>
<dd>When run in standalone mode, write the process ID of the listening server into <i>pidfile</i>. On normal termination (SIGTERM or SIGINT) the pid file is automatically removed.</p>
<dt><code>&#8211;timeout</code> <i>timeout</i>, <code>-t</code> <i>timeout</i></p>
<dd>When run from <code>inetd</code> this specifies how long, in seconds, to wait for a second connection before terminating the server. <code>inetd</code> will then respawn the server when another request comes in. The default is 900 (15 minutes.)</p>
<dt><code>&#8211;retransmit</code> <i>timeout, </i><code>-T</code> <i>timeout</i></p>
<dd>Determine the default timeout, in microseconds, before the first packet is retransmitted. This can be modified by the client if the <code>timeout</code> or <code>utimeout</code> option is negotiated. The default is 1000000 (1 second.)</p>
<dt><code>&#8211;map-file</code> <i>remap-file</i>, <code>-m</code> <i>remap-file</i></p>
<dd>Specify the use of filename remapping. The <i>remap-file</i> is a file containing the remapping rules. See the section on filename remapping below. This option may not be compiled in, see the output of <code>in.tftpd -V</code> to verify whether or not it is available.</p>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd>Increase the logging verbosity of <code>tftpd</code>. This flag can be specified multiple times for even higher verbosity.</p>
<dt><code>&#8211;verbosity</code> <i>value</i></p>
<dd>Set the verbosity value to <i>value</i>.</p>
<dt><code>&#8211;refuse</code> <i>tftp-option</i>, <code>-r</code> <i>tftp-option</i></p>
<dd>Indicate that a specific RFC 2347 TFTP option should never be accepted.</p>
<dt><code>&#8211;blocksize</code> <i>max-block-size</i>, <code>-B</code> <i>max-block-size</i></p>
<dd>Specifies the maximum permitted block size. The permitted range for this parameter is from 512 to 65464. Some embedded clients request large block sizes and yet do not handle fragmented packets correctly; for these clients, it is recommended to set this value to the smallest MTU on your network minus 32 bytes (20 bytes for IP, 8 for UDP, and 4 for TFTP; less if you use IP options on your network.) For example, on a standard Ethernet (MTU 1500) a value of 1468 is reasonable.</p>
<dt><code>&#8211;port-range</code> <i>port:port</i>, <code>-R</code> <i>port:port</i></p>
<dd>Force the server port number (the Transaction ID) to be in the specified range of port numbers.</p>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd>Print the version number and configuration to standard output, then exit gracefully.</dl>
<h2>Rfc 2347 Option Negotiation</h2>
<p>This version of <code>tftpd</code> supports RFC 2347 option negotation. Currently implemented options are:</p>
<dl>
<dt><code>blksize</code> (RFC 2348)</p>
<dd>Set the transfer block size to anything less than or equal to the specified option. This version of <code>tftpd</code> can support any block size up to the theoretical maximum of 65464 bytes.</p>
<dt><code>blksize2</code> (nonstandard)</p>
<dd>Set the transfer block size to anything less than or equal to the specified option, but restrict the possible responses to powers of 2. The maximum is 32768 bytes (the largest power of 2 less than or equal to 65464.)</p>
<dt><code>tsize</code> (RFC 2349)</p>
<dd>Report the size of the file that is about to be transferred. This version of <code>tftpd</code> only supports the <code>tsize</code> option for binary (octet) mode transfers.</p>
<dt><code>timeout</code> (RFC 2349)</p>
<dd>Set the time before the server retransmits a packet, in seconds.</p>
<dt><code>utimeout</code> (nonstandard)</p>
<dd>Set the time before the server retransmits a packet, in microseconds.</p>
<dt><code>rollover</code> (nonstandard)</p>
<dd>Set the block number to resume at after a block number rollover. The default and recommended value is zero.</dl>
<p> The <code>&#8211;refuse</code> option can be used to disable specific options; this may be necessary to work around bugs in specific TFTP client implementations. For example, some TFTP clients have been found to request the <code>blksize</code> option, but crash with an error if they actually get the option accepted by the server.</p>
<h2>Filename Remapping</h2>
<p>The <code>&#8211;mapfile</code> option specifies a file which contains filename remapping rules. Each non-comment line (comments begin with hash marks, <code>#</code>) contains an <i>operation</i>, specified below; a <i>regex</i>, a regular expression in the style of <code>egrep</code>; and optionally a <i>replacement pattern</i>. The operation indicated by <i>operation</i> is performed if the <i>regex</i> matches all or part of the filename. Rules are processed from the top down, and by default, all rules are processed even if there is a match. </p>
<p> The <i>operation</i> can be any combination of the following letters:</p>
<dl>
<dt><code>r</code></p>
<dd>Replace the substring matched by <i>regex</i> by the <i>replacement pattern</i>. The replacement pattern may contain escape sequences; see below.</p>
<dt><code>g</code></p>
<dd>Repeat this rule until it no longer matches. This is always used with <code>r</code>.</p>
<dt><code>i</code></p>
<dd>Match the <i>regex</i> case-insensitively. By default it is case sensitive.</p>
<dt><code>e</code></p>
<dd>If this rule matches, end rule processing after executing the rule.</p>
<dt><code>s</code></p>
<dd>If this rule matches, start rule processing over from the very first rule after executing this rule.</p>
<dt><code>a</code></p>
<dd>If this rule matches, refuse the request and send an access denied error to the client.</p>
<dt><code>G</code></p>
<dd>This rule applies to GET (RRQ) requests only.</p>
<dt><code>P</code></p>
<dd>This rule applies to PUT (WRQ) requests only.</p>
<dt><code>~</code></p>
<dd>Inverse the sense of this rule, i.e. execute the <i>operation</i> only if the <i>regex</i> <i>doesn&#8217;t</i> match. Cannot used together with <code>r</code>.</dl>
<p> The following escape sequences are recognized as part of the <i>replacement pattern</i>:</p>
<dl>
<dt><code>
