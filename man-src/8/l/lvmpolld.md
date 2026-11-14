---
title: "lvmpolld(8)"
name: "lvmpolld"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmpolld/"
description: "lvmpolld — LVM poll daemon"
---

<p>lvmpolld &#8212; LVM poll daemon</p>
<h2>Synopsis</h2>
<p><code>lvmpolld</code> [<code>-l</code>|<code>&#8211;log</code> {<i>all</i>|<i>wire</i>|<i>debug</i>}] [<code>-p</code>|<code>&#8211;pidfile</code> <i>pidfile_path</i>] [<code>-s</code>|<code>&#8211;socket</code> <i>socket_path</i>] [<code>-B</code>|<code>&#8211;binary</code> <i>lvm_binary_path</i>] [<code>-t</code>|<code>&#8211;timeout</code> <i>timeout_value</i>] [<code>-f</code>|<code>&#8211;foreground</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-V</code>|<code>&#8211;version</code>] </p>
<p> <code>lvmpolld</code> [<code>&#8211;dump</code>]</p>
<h2>Description</h2>
<p>lvmpolld is polling daemon for LVM. The daemon receives requests for polling of already initialised operations originating in LVM2 command line tool. The requests for polling originate in the <code>lvconvert</code>, <code>pvmove</code>, <code>lvchange</code> or <code>vgchange</code> LVM2 commands. </p>
<p> The purpose of lvmpolld is to reduce the number of spawned background processes per otherwise unique polling operation. There should be only one. It also eliminates the possibility of unsolicited termination of background process by external factors. </p>
<p> lvmpolld is used by LVM only if it is enabled in <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) by specifying the <code>global/use_lvmpolld</code> setting. If this is not defined in the LVM configuration explicitly then default setting is used instead (see the output of <code>lvmconfig &#8211;type default global/use_lvmpolld</code> command).</p>
<h2>Options</h2>
<p>To run the daemon in a test environment both the pidfile_path and the socket_path should be changed from the defaults.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>Don&#8217;t fork, but run in the foreground.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show help information.</p>
<dt><i></i><code>-l</code>, <i></i><code>&#8211;log</code> {<i>all</i>|<i>wire</i>|<i>debug</i>}</p>
<dd>Select the type of log messages to generate. Messages are logged by syslog. Additionally, when -f is given they are also sent to standard error. There are two classes of messages: wire and debug. Selecting &#8216;all&#8217; supplies both and is equivalent to a comma-separated list -l wire,debug.</p>
<dt><code>-p</code>, <code>&#8211;pidfile</code> <i>pidfile_path</i></p>
<dd>Path to the pidfile. This overrides both the built-in default (/run/lvmpolld.pid) and the environment variable <code>LVM_LVMPOLLD_PIDFILE</code>. This file is used to prevent more than one instance of the daemon running simultaneously.</p>
<dt><code>-s</code>, <code>&#8211;socket</code> <i>socket_path</i></p>
<dd>Path to the socket file. This overrides both the built-in default (/run/lvm/lvmpolld.socket) and the environment variable <code>LVM_LVMPOLLD_SOCKET</code>.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code> <i>timeout_value</i></p>
<dd>The daemon may shutdown after being idle for the given time (in seconds). When the option is omitted or the value given is zero the daemon never shutdowns on idle.</p>
<dt><code>-B</code>, <code>&#8211;binary</code> <i>lvm_binary_path</i></p>
<dd>Optional path to alternative LVM binary (default: /lvm). Use for testing purposes only.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display the version of lvmpolld daemon.</p>
<dt><code>&#8211;dump</code></p>
<dd>Contact the running lvmpolld daemon to obtain the complete state and print it out in a raw format.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>LVM_LVMPOLLD_PIDFILE</code></p>
<dd>Path for the pid file.</p>
<dt><code>LVM_LVMPOLLD_SOCKET</code></p>
<dd>Path for the socket file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) </p>
