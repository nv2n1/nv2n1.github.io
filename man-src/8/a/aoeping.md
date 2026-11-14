---
title: "aoeping(8)"
name: "aoeping"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aoeping/"
description: "aoeping – simple communication with AoE device"
---

<p>aoeping &#8211; simple communication with AoE device</p>
<h2>Synopsis</h2>
<p><code>aoeping [options] {shelf} {slot} {netif}</code></p>
<h2>Description</h2>
<p>The <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) program performs simple one or two-round-trip communication with an ATA over Ethernet (AoE) device. </p>
<p> Running <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) without command line arguments will result in a short usage summary being displayed. </p>
<p> The <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) program will wait forever if if doesn&#8217;t receive an expected response. The caller should use a time out to catch this situation.</p>
<h3>Arguments</h3>
<dl>
<dt><code>shelf</code></p>
<dd>This should be the shelf address (major AoE address) of the AoE device to communicate with.</p>
<dt><code>slot</code></p>
<dd>This should be the slot address (minor AoE address) of the AoE device to communicate with.</p>
<dt><code>netif</code></p>
<dd>The name of the ethernet network interface to use for AoE communications, e.g., eth1.</dl>
<h3>Options</h3>
<dl>
<dt><code>-i</code></p>
<dd>Issue an ATA &quot;identify device&quot; command after receiving the AoE device&#8217;s Config Query response. The &quot;ident&quot; response will be printed on standard output as a hexidecimal dump.</p>
<dt><code>-I</code></p>
<dd>Issue an ATA &quot;identify device&quot; command after receiving the AoE device&#8217;s Config Query response. The &quot;ident&quot; response will be pretty-printed on standard output as selected human-readable fields.</p>
<dt><code>-v</code></p>
<dd>Turn on more copious output, including a hexidecimal dump of the Config Query response from the AoE device (see AoE spec at URL below).</p>
<dt><code>-s</code></p>
<dd>This option takes an argument. The argument is a decimal integer that specifies the number of seconds that <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) will wait for a response before timing out and exiting with a non-zero status.</p>
<dt><code>-S</code></p>
<dd>This option takes an argument. The argument is the name of a SMART command to send to the disk. The SMART commands in the list below are supported. If the command requires data transfer, one sector (512 bytes) of data is always the amount transfered. If the command takes a parameter (for the Low LBA register), then the name of the SMART command is immediately followed by a colon and then a number, the value of the parameter, e.g., &quot;-S read_log:1&quot;.</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>read_data<br />
&nbsp;<wbr>&nbsp;<wbr>offline_immediate<br />
&nbsp;<wbr>&nbsp;<wbr>read_log<br />
&nbsp;<wbr>&nbsp;<wbr>write_log<br />
&nbsp;<wbr>&nbsp;<wbr>enable<br />
&nbsp;<wbr>&nbsp;<wbr>disable<br />
&nbsp;<wbr>&nbsp;<wbr>return_status </p>
<p> For <code>write_log</code>, <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) reads from standard input the one sector of data to be written to the specified log. </p>
<p> The <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) command just sends and receives SMART commands, without interpreting them. See the ATA specification for more information on using SMART.</dl>
<dl>
<dt><code>-t</code></p>
<dd>(This is an advanced feature.) This option has an argument. The argument is a decimal integer that is used as the initial tag, with the highest bit set, as the first tag in ATA commands. Tags for subsequent ATA commands will be incremented by one.</p>
<dt><code>-h</code></p>
<dd>Show a usage summary.</dl>
<h2>Example</h2>
<p>In this example, the root user uses <i><a href="/docs/linux/man/8-aoeping/">aoeping</a></i>(8) to check for the presence of aoe device e10.9 on network interface eth0.</p>
<dl>
<dd>
<pre>bash# aoeping -v 10 9 eth0 | head
tag: 80000000
eth: eth0
shelf: 10
slot: 9
config query response:
00 0d 87 aa c9 00 00 10 04 00 11 1f 88 a2 18 00 
00 0a 09 01 00 00 00 00 00 03 30 08 00 10 00 04 
66 6f 6f 0a 00 ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff </pre>
</dl>
<p> The next example shows root making sure the disk on the e10.9 is still responsive by issuing an ATA device identify command with a 20-second timeout.</p>
<dl>
<dd>
<pre>bash# aoeping -i -s 20 \
 10 9 eth0 &gt; /dev/null \
 &amp;&amp; echo ok
ok</pre>
</dl>
<p> The next example uses SMART to determine whether the disk on e10.9 thinks it has exceeded its error threshold. The ATA spec says that the LBA Mid register will be 0x4f when the disk has not exceeded its error threshold.</p>
<dl>
<dd>
<pre>bash# aoeping -S return_status \
 10 9 eth0 | grep 'LBA Mid: 0x4f' \
 &gt; /dev/null \
 &amp;&amp; echo ok
ok</pre>
</dl>
<p> Note that in a script, it would be prudent to specify and handle a timeout. Also, a good script would make sure the <code>Status</code> register does not have the error bit (bit zero) or the device fault bit (bit 5) set.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-aoe-discover/">aoe-discover</a></i>(8), <i><a href="/docs/linux/man/8-aoe-interfaces/">aoe-interfaces</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkdevs/">aoe-mkdevs</a></i>(8), <i><a href="/docs/linux/man/8-aoe-mkshelf/">aoe-mkshelf</a></i>(8), <i><a href="/docs/linux/man/8-aoe-stat/">aoe-stat</a></i>(8), </p>
<p> <i>AoE (ATA over Ethernet)</i>: <a rel="nofollow" href="http://www.coraid.com/documents/AoEr10.txt,">http://www.coraid.com/documents/AoEr10.txt,</a> </p>
<p> <i>ATA specification</i></p>
<h2>Author</h2>
<p>Ed L. Cashin (ecashin [at] coraid.com)</p>
