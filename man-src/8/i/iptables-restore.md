---
title: "iptables-restore(8)"
name: "iptables-restore"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptables-restore/"
description: "iptables-restore — Restore IP Tables"
---

<p>iptables-restore &#8212; Restore IP Tables </p>
<p> ip6tables-restore &#8212; Restore IPv6 Tables</p>
<h2>Synopsis</h2>
<p><code>iptables-restore</code> [<code>-chntvV</code>] [<code>-w</code> <i>secs</i>] [<code>-W</code> <i>usecs</i>] [<code>-M</code> <i>modprobe</i>] [<code>-T</code> <i>name</i>] [<code>file</code>] </p>
<p> <code>ip6tables-restore</code> [<code>-chntvV</code>] [<code>-w</code> <i>secs</i>] [<code>-W</code> <i>usecs</i>] [<code>-M</code> <i>modprobe</i>] [<code>-T</code> <i>name</i>] [<code>file</code>]</p>
<h2>Description</h2>
<p><code>iptables-restore</code> and <code>ip6tables-restore</code> are used to restore IP and IPv6 Tables from data specified on STDIN or in <i>file</i>. Use I/O redirection provided by your shell to read from a file or specify <i>file</i> as an argument.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;counters</code></dt>
<dd>restore the values of all packet and byte counters</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print a short option summary.</dd>
<dt><code>-n</code>, <code>&#8211;noflush</code></dt>
<dd>don&#8217;t flush the previous contents of the table. If not specified, both commands flush (delete) all previous contents of the respective table.</dd>
<dt><code>-t</code>, <code>&#8211;test</code></dt>
<dd>Only parse and construct the ruleset, but do not commit it.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Print additional debug info during ruleset processing.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Print the program version number.</dd>
<dt><code>-w</code>, <code>&#8211;wait</code> [<i>seconds</i>]</dt>
<dd>Wait for the xtables lock. To prevent multiple instances of the program from running concurrently, an attempt will be made to obtain an exclusive lock at launch. By default, the program will exit if the lock cannot be obtained. This option will make the program wait (indefinitely or for optional <i>seconds</i>) until the exclusive lock can be obtained.</dd>
<dt><code>-W</code>, <code>&#8211;wait-interval</code> <i>microseconds</i></dt>
<dd>Interval to wait per each iteration. When running latency sensitive applications, waiting for the xtables lock for extended durations may not be acceptable. This option will make each iteration take the amount of time specified. The default interval is 1 second. This option only works with <code>-w</code>.</dd>
<dt><code>-M</code>, <code>&#8211;modprobe</code> <i>modprobe_program</i></dt>
<dd>Specify the path to the modprobe program. By default, iptables-restore will inspect /proc/sys/kernel/modprobe to determine the executable&#8217;s path.</dd>
<dt><code>-T</code>, <code>&#8211;table</code> <i>name</i></dt>
<dd>Restore only the named table even if the input stream contains other ones.</dd></dl>
<h2>Bugs</h2>
<p>None known as of iptables-1.2.1 release</p>
<h2>Authors</h2>
<p>Harald Welte &lt;laforge [at] gnumonks.org&gt; wrote iptables-restore based on code from Rusty Russell.<br />
 Andras Kis-Szabo &lt;kisza [at] sch.bme.hu&gt; contributed ip6tables-restore.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables-apply/">iptables-apply</a></code>(8),<code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) The iptables-HOWTO, which details more iptables usage, the NAT-HOWTO, which details NAT, and the netfilter-hacking-HOWTO which details the internals. </p>
