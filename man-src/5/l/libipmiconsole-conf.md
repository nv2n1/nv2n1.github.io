---
title: "libipmiconsole-conf(5)"
name: "libipmiconsole-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libipmiconsole-conf/"
description: "libipmiconsole.conf – specify default values for libipmiconsole"
---

<p>libipmiconsole.conf &#8211; specify default values for libipmiconsole</p>
<h2>Description</h2>
<p>The <code>Libipmiconsole</code> configuration file can be used to set alternate default values for the <code>Libipmiconsole</code> library. The configuration of these defaults may be useful for environments in which programs link to libipmiconsole but do not support configuration of libipmiconsole parameters. Users should be ware that setting alternate default values into <code>Libipmiconsole</code> will affect all tools that link to the library, such as the <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> tool. For users wishing to set alternate defaults to <code><a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8)</code> please use the <code><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5)</code> file instead. </p>
<p> The configuration file is stored at /etc/freeipmi//libipmiconsole.conf.</p>
<h2>Format</h2>
<p>The configuration options that can be specified in the configuration file are listed below. Each configuration option must be listed on a separate line. Arguments for an option are separated by any amount of whitespace. Multiple arguments are also separated by whitespace. Comments can be marked by using the pound sign (&quot;#&quot;) character, and lines can be continued on the next using backslash (&quot;\&quot;).</p>
<h2>Context Ipmi Config Options</h2>
<p>Every SOL session is housed within an libipmiconsole context. The following defines IPMI config default values for each context created.</p>
<dl>
<dt><code>libipmiconsole-context-username</code> <i>USERNAME</i></p>
<dd>Specify the default username to use.</p>
<dt><code>libipmiconsole-context-password</code> <i>PASSWORD</i></p>
<dd>Specify the default password to use.</p>
<dt><code>libipmiconsole-context-k_g</code> <i>str</i></p>
<dd>Specify the default BMC key (K_g) to use. Prefix with &#8216;0x&#8217; to enter the key in hex.</p>
<dt><code>libipmiconsole-context-privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the default privilege type to use. The following privilege levels are supported: USER, OPERATOR, ADMIN.</p>
<dt><code>libipmiconsole-context-cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the default cipher suite id to use. The following cipher suite ids are supported: 0, 1, 2, 3, 6, 7, 8, 11, 12.</p>
<dt><code>libipmiconsole-context-workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify default workaround flags to use. Multiple workarounds can be specified separated by whitespace. The following workarounds are supported: authcap, intel20, supermicro20, sun20, opensesspriv, integritycheckvalue, solpayloadsize, solport, solstatus.</dl>
<h2>Context Protocol Config Options</h2>
<p>Every SOL session is housed within an libipmiconsole context. The following defines protocol config default values for each context created.</p>
<dl>
<dt><code>libipmiconsole-context-session-timeout-len</code> <i>MILLISECONDS</i></p>
<dd>Specify the default session timeout length to use in milliseconds.</p>
<dt><code>libipmiconsole-context-retransmission-timeout-len</code> <i>MILLISECONDS</i></p>
<dd>Specify the default retransmission timeout length to use in milliseconds.</p>
<dt><code>libipmiconsole-context-retransmission-backoff-count</code> <i>NUM</i></p>
<dd>Specify the default retransmission backoff count to use.</p>
<dt><code>libipmiconsole-context-keepalive-timeout-len</code> <i>MILLISECONDS</i></p>
<dd>Specify the default keepalive timeout length to use in milliseconds.</p>
<dt><code>libipmiconsole-context-retransmission-keepalive-timeout-len</code> <i>MILLISECONDS</i></p>
<dd>Specify the default retransmission timeout length to use for keepalive packets in milliseconds.</p>
<dt><code>libipmiconsole-context-acceptable-packet-errors-count</code> <i>NUM</i></p>
<dd>Specify the default packet errors count to use.</p>
<dt><code>libipmiconsole-context-maximum-retransmission-count</code> <i>NUM</i></p>
<dd>Specify the default maximum retransmission count to use.</dl>
<h2>Context Engine Config Options</h2>
<p>Every SOL session is housed within an libipmiconsole context. The following defines engine config default values for each context created. Knowledge of the libipmiconsole library may be necessary to understand the meaning of these settings. Please see the <code>ipmiconsole.h</code> header file for additional information on the library.</p>
<dl>
<dt><code>libipmiconsole-context-engine-flags</code> <i>FLAGS</i></p>
<dd>Specify default engine flags to use. Multiple flags can be specified separated by whitespace. The following flags are supported: closefd, outputonsolestablished, lockmemory, serialkeepalive.</p>
<dt><code>libipmiconsole-context-behavior-flags</code> <i>FLAGS</i></p>
<dd>Specify default behavior flags to use. Multiple flags can be specified separated by whitespace. The following flags are supported: erroronsolinuse, deactivateonly, deactivateallinstances.</p>
<dt><code>libipmiconsole-context-debug-flags</code> <i>FLAGS</i></p>
<dd>Specify default debug flags to use. Multiple flags can be specified separated by whitespace. The following flags are supported: stdout, stderr, syslog, file, ipmipackets.</p>
<dt><code>libipmiconsole-context-sol-payload-instance</code> <i>NUM</i></p>
<dd>Specify default SOL payload instance. Has range of 1 to 15.</dl>
<h2>Files</h2>
<p>/etc/freeipmi//libipmiconsole.conf</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2006-2007 The Regents of the University of California. </p>
<p> FreeIPMI is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5), <a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/3-libipmiconsole/">libipmiconsole</a>(3), <a href="/docs/linux/man/8-ipmiconsole/">ipmiconsole</a>(8), <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
