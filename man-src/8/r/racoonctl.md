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
<p>[opts] reload-config<br />
 [opts] show-schedule<br />
 [opts] show-sa [isakmp|esp|ah|ipsec]<br />
 [opts] get-sa-cert [inet|inet6] <i>src dst</i><br />
 [opts] flush-sa [isakmp|esp|ah|ipsec]<br />
 [opts] delete-sa <i>saopts</i><br />
 [opts] establish-sa [-<code>w</code> ] [-<code>n </code><i>remoteconf</i> ] [-<code>u </code><i>identity</i> ] <i>saopts</i><br />
 [opts] vpn-connect [-<code>u </code><i>identity</i> ] <i>vpn_gateway</i><br />
 [opts] vpn-disconnect <i>vpn_gateway</i><br />
 [opts] show-event<br />
 [opts] logout-user <i>login</i></p>
<h2>Description</h2>
<p>is used to control <a href="/docs/linux/man/8-racoon/">racoon</a>(8) operation, if ipsec-tools was configured with adminport support. Communication between and <a href="/docs/linux/man/8-racoon/">racoon</a>(8) is done through a UNIX socket. By changing the default mode and ownership of the socket, you can allow non-root users to alter <a href="/docs/linux/man/8-racoon/">racoon</a>(8) behavior, so do that with caution. The following general options are available:</p>
<dl>
<dt><code>-d</code></p>
<dd>Debug mode. Hexdump sent admin port commands.</p>
<dt><code>-l</code></p>
<dd>Increase verbosity. Mainly for show-sa command.</p>
<dt><code>-s </code><i>socket</i></p>
<dd>Specify unix socket name used to connecting racoon.</dl>
<p> The following commands are available:</p>
<dl>
<dt><code>reload-config</code></p>
<dd>This should cause <a href="/docs/linux/man/8-racoon/">racoon</a>(8) to reload its configuration file.</p>
<dt><code>show-schedule</code></p>
<dd>Unknown command.</p>
<dt><code>show-sa </code>[isakmp|esp|ah|ipsec]</p>
<dd>Dump the SA: All the SAs if no SA class is provided, or either ISAKMP SAs, IPsec ESP SAs, IPsec AH SAs, or all IPsec SAs. Use &#8211;<code>l</code> to increase verbosity.</p>
<dt><code>get-sa-cert </code>[inet|inet6 <i>src dst</i> ]</p>
<dd>Output the raw certificate that was used to authenticate the phase 1 matching <i>src</i> and <i>dst</i></p>
<dt><code>flush-sa </code>[isakmp|esp|ah|ipsec]</p>
<dd>is used to flush all SAs if no SA class is provided, or a class of SAs, either ISAKMP SAs, IPsec ESP SAs, IPsec AH SAs, or all IPsec SAs.</p>
<dt><code>establish-sa </code>[-<code>w </code>[-<code>n </code><i>remoteconf </i>[-<code>u </code><i>username</i> ] ]</p>
<dd>Oc Ar saopts Establish an SA, either an ISAKMP SA, IPsec ESP SA, or IPsec AH SA. The optional &#8211;<code>u </code><i>username</i> can be used when establishing an ISAKMP SA while hybrid auth is in use. The exact remote block to use can be specified with &#8211;<code>n </code><i>remoteconf</i> will prompt you for the password associated with <i>username</i> and these credentials will be used in the Xauth exchange. Specifying &#8211;<code>w</code> will make racoonctl wait until the SA is actually established or an error occurs. <i>saopts</i> has the following format:</p>
<dl>
<dt><code>isakmp {inet|inet6} </code><i>src dst</i></p>
<dd>
<dt><code>{esp|ah} {inet|inet6} </code><i>src/prefixlen/port dst/prefixlen/port</i></p>
<dd>{icmp|tcp|udp|gre|any}</dl>
<dt><code>vpn-connect </code>[-<code>u </code><i>username vpn_gateway</i> ]</p>
<dd>This is a particular case of the previous command. It will establish an ISAKMP SA with <i>vpn_gateway</i></p>
<dt><code>delete-sa </code><i>saopts</i></p>
<dd>Delete an SA, either an ISAKMP SA, IPsec ESP SA, or IPsec AH SA.</p>
<dt><code>vpn-disconnect </code><i>vpn_gateway</i></p>
<dd>This is a particular case of the previous command. It will kill all SAs associated with <i>vpn_gateway</i></p>
<dt><code>show-event</code></p>
<dd>Listen for all events reported by <a href="/docs/linux/man/8-racoon/">racoon</a>(8).</p>
<dt><code>logout-user </code><i>login</i></p>
<dd>Delete all SA established on behalf of the Xauth user <i>login</i></dl>
<p> Command shortcuts are available:</p>
<dl>
<dt><code>rc</code></p>
<dd>reload-config</p>
<dt><code>ss</code></p>
<dd>show-sa</p>
<dt><code>sc</code></p>
<dd>show-schedule</p>
<dt><code>fs</code></p>
<dd>flush-sa</p>
<dt><code>ds</code></p>
<dd>delete-sa</p>
<dt><code>es</code></p>
<dd>establish-sa</p>
<dt><code>vc</code></p>
<dd>vpn-connect</p>
<dt><code>vd</code></p>
<dd>vpn-disconnect</p>
<dt><code>se</code></p>
<dd>show-event</p>
<dt><code>lu</code></p>
<dd>logout-user</dl>
<h2>Return Values</h2>
<p>The command should exit with 0 on success, and non-zero on errors.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/racoon/racoon.sock or</code></p>
<dd>
<dt><code>/var/run/racoon.sock </code></p>
<dd><a href="/docs/linux/man/8-racoon/">racoon</a>(8) control socket.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/4-ipsec/">ipsec</a>(4), <a href="/docs/linux/man/8-racoon/">racoon</a>(8)</p>
<h2>History</h2>
<p>Once was <code>kmpstat</code> in the KAME project. It turned into but remained undocumented for a while. An Emmanuel Dreyfus Aq manu [at] NetBSD.org wrote this man page.</p>
