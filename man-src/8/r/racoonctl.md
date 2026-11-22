---
title: "racoonctl(8)"
name: "racoonctl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoonctl/"
description: "racoonctl – racoon administrative control tool"
---

<p><code>racoonctl</code> &#8211; racoon administrative control tool</p>
<h2>Synopsis</h2>
<p>[opts] reload-config<br/>
 [opts] show-schedule<br/>
 [opts] show-sa [isakmp|esp|ah|ipsec]<br/>
 [opts] get-sa-cert [inet|inet6] <i>src dst</i><br/>
 [opts] flush-sa [isakmp|esp|ah|ipsec]<br/>
 [opts] delete-sa <i>saopts</i><br/>
 [opts] establish-sa [-<code>w</code> ] [-<code>n </code><i>remoteconf</i> ] [-<code>u </code><i>identity</i> ] <i>saopts</i><br/>
 [opts] vpn-connect [-<code>u </code><i>identity</i> ] <i>vpn_gateway</i><br/>
 [opts] vpn-disconnect <i>vpn_gateway</i><br/>
 [opts] show-event<br/>
 [opts] logout-user <i>login</i></p>
<h2>Description</h2>
<p>is used to control <a href="/docs/linux/man/8-racoon/">racoon</a>(8) operation, if ipsec-tools was configured with adminport support. Communication between and <a href="/docs/linux/man/8-racoon/">racoon</a>(8) is done through a UNIX socket. By changing the default mode and ownership of the socket, you can allow non-root users to alter <a href="/docs/linux/man/8-racoon/">racoon</a>(8) behavior, so do that with caution. The following general options are available:</p>
<dl>
<dt><code>-d</code></dt>
<dd>Debug mode. Hexdump sent admin port commands.</dd>
<dt><code>-l</code></dt>
<dd>Increase verbosity. Mainly for show-sa command.</dd>
<dt><code>-s </code><i>socket</i></dt>
<dd>Specify unix socket name used to connecting racoon.</dd></dl>
<p> The following commands are available:</p>
<dl>
<dt><code>reload-config</code></dt>
<dd>This should cause <a href="/docs/linux/man/8-racoon/">racoon</a>(8) to reload its configuration file.</dd>
<dt><code>show-schedule</code></dt>
<dd>Unknown command.</dd>
<dt><code>show-sa </code>[isakmp|esp|ah|ipsec]</dt>
<dd>Dump the SA: All the SAs if no SA class is provided, or either ISAKMP SAs, IPsec ESP SAs, IPsec AH SAs, or all IPsec SAs. Use &#8211;<code>l</code> to increase verbosity.</dd>
<dt><code>get-sa-cert </code>[inet|inet6 <i>src dst</i> ]</dt>
<dd>Output the raw certificate that was used to authenticate the phase 1 matching <i>src</i> and <i>dst</i></dd>
<dt><code>flush-sa </code>[isakmp|esp|ah|ipsec]</dt>
<dd>is used to flush all SAs if no SA class is provided, or a class of SAs, either ISAKMP SAs, IPsec ESP SAs, IPsec AH SAs, or all IPsec SAs.</dd>
<dt><code>establish-sa </code>[-<code>w </code>[-<code>n </code><i>remoteconf </i>[-<code>u </code><i>username</i> ] ]</dt>
<dd>Oc Ar saopts Establish an SA, either an ISAKMP SA, IPsec ESP SA, or IPsec AH SA. The optional &#8211;<code>u </code><i>username</i> can be used when establishing an ISAKMP SA while hybrid auth is in use. The exact remote block to use can be specified with &#8211;<code>n </code><i>remoteconf</i> will prompt you for the password associated with <i>username</i> and these credentials will be used in the Xauth exchange. Specifying &#8211;<code>w</code> will make racoonctl wait until the SA is actually established or an error occurs. <i>saopts</i> has the following format:</dd>
<dl>
<dt><code>isakmp {inet|inet6} </code><i>src dst</i></dt>
<dd>
</dd><dt><code>{esp|ah} {inet|inet6} </code><i>src/prefixlen/port dst/prefixlen/port</i></dt>
<dd>{icmp|tcp|udp|gre|any}</dd></dl>
<dt><code>vpn-connect </code>[-<code>u </code><i>username vpn_gateway</i> ]</dt>
<dd>This is a particular case of the previous command. It will establish an ISAKMP SA with <i>vpn_gateway</i></dd>
<dt><code>delete-sa </code><i>saopts</i></dt>
<dd>Delete an SA, either an ISAKMP SA, IPsec ESP SA, or IPsec AH SA.</dd>
<dt><code>vpn-disconnect </code><i>vpn_gateway</i></dt>
<dd>This is a particular case of the previous command. It will kill all SAs associated with <i>vpn_gateway</i></dd>
<dt><code>show-event</code></dt>
<dd>Listen for all events reported by <a href="/docs/linux/man/8-racoon/">racoon</a>(8).</dd>
<dt><code>logout-user </code><i>login</i></dt>
<dd>Delete all SA established on behalf of the Xauth user <i>login</i></dd></dl>
<p> Command shortcuts are available:</p>
<dl>
<dt><code>rc</code></dt>
<dd>reload-config</dd>
<dt><code>ss</code></dt>
<dd>show-sa</dd>
<dt><code>sc</code></dt>
<dd>show-schedule</dd>
<dt><code>fs</code></dt>
<dd>flush-sa</dd>
<dt><code>ds</code></dt>
<dd>delete-sa</dd>
<dt><code>es</code></dt>
<dd>establish-sa</dd>
<dt><code>vc</code></dt>
<dd>vpn-connect</dd>
<dt><code>vd</code></dt>
<dd>vpn-disconnect</dd>
<dt><code>se</code></dt>
<dd>show-event</dd>
<dt><code>lu</code></dt>
<dd>logout-user</dd></dl>
<h2>Return Values</h2>
<p>The command should exit with 0 on success, and non-zero on errors.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/racoon/racoon.sock or</code></dt>
<dd>
</dd><dt><code>/var/run/racoon.sock </code></dt>
<dd><a href="/docs/linux/man/8-racoon/">racoon</a>(8) control socket.</dd></dl>
<h2>See Also</h2>
<p>ipsec(4), <a href="/docs/linux/man/8-racoon/">racoon</a>(8)</p>
<h2>History</h2>
<p>Once was <code>kmpstat</code> in the KAME project. It turned into but remained undocumented for a while. An Emmanuel Dreyfus Aq manu [at] NetBSD.org wrote this man page.</p>
