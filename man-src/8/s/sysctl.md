---
title: "sysctl(8)"
name: "sysctl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sysctl/"
description: "sysctl – configure kernel parameters at runtime"
---

<p>sysctl &#8211; configure kernel parameters at runtime</p>
<h2>Synopsis</h2>
<p><code>sysctl</code> [<i>options</i>] [<i>variable</i>[<code>=</code><i>value</i>]] [&#8230;]<br />
 <code>sysctl -p</code> [<i>file</i> or <i>regexp</i>] [&#8230;]</p>
<h2>Description</h2>
<p><code>sysctl</code> is used to modify kernel parameters at runtime. The parameters available are those listed under /proc/sys/. Procfs is required for <code>sysctl</code> support in Linux. You can use <code>sysctl</code> to both read and write sysctl data.</p>
<h2>Parameters</h2>
<dl>
<dt><i>variable</i></p>
<dd>The name of a key to read from. An example is kernel.ostype. The &#8216;/&#8217; separator is also accepted in place of a &#8216;.&#8217;.</p>
<dt><i>variable</i>=<i>value</i></p>
<dd>To set a key, use the form <i>variable</i>=<i>value</i> where <i>variable</i> is the key and <i>value</i> is the value to set it to. If the value contains quotes or characters which are parsed by the shell, you may need to enclose the value in double quotes.</p>
<dt><code>-n</code>, <code>&#8211;values</code></p>
<dd>Use this option to disable printing of the key name when printing values.</p>
<dt><code>-e</code>, <code>&#8211;ignore</code></p>
<dd>Use this option to ignore errors about unknown keys.</p>
<dt><code>-N</code>, <code>&#8211;names</code></p>
<dd>Use this option to only print the names. It may be useful with shells that have programmable completion.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Use this option to not display the values set to stdout.</p>
<dt><code>-w</code>, <code>&#8211;write</code></p>
<dd>Use this option when all arguments prescribe a key to be set.</p>
<dt><code>-p</code>[<i>FILE</i>], <code>&#8211;load</code>[=<i>FILE</i>]</p>
<dd>Load in sysctl settings from the file specified or /etc/sysctl.conf if none given. Specifying &#8211; as filename means reading data from standard input. Using this option will mean arguments to <code>sysctl</code> are files, which are read in the order they are specified. The file argument may be specified as regular expression.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>Display all values currently available.</p>
<dt><code>&#8211;deprecated</code></p>
<dd>Include deprecated parameters to <code>&#8211;all</code> values listing.</p>
<dt><code>-b</code>, <code>&#8211;binary</code></p>
<dd>Print value without new line.</p>
<dt><code>&#8211;system</code></p>
<dd>Load settings from all system configuration files. Files are read from directories in the following list in given order from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.<br />
 /etc/sysctl.d/*.conf<br />
 /run/sysctl.d/*.conf<br />
 /usr/local/lib/sysctl.d/*.conf<br />
 /usr/lib/sysctl.d/*.conf<br />
 /lib/sysctl.d/*.conf<br />
 /etc/sysctl.conf</p>
<dt><code>-r</code>, <code>&#8211;pattern</code> <i>pattern</i></p>
<dd>Only apply settings that match <i>pattern</i>. The <i>pattern</i> uses extended regular expression syntax.</p>
<dt><code>-A</code></p>
<dd>Alias of <code>-a</code></p>
<dt><code>-d</code></p>
<dd>Alias of <code>-h</code></p>
<dt><code>-f</code></p>
<dd>Alias of <code>-p</code></p>
<dt><code>-X</code></p>
<dd>Alias of <code>-a</code></p>
<dt><code>-o</code></p>
<dd>Does nothing, exists for BSD compatibility.</p>
<dt><code>-x</code></p>
<dd>Does nothing, exists for BSD compatibility.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help text and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information and exit.</dl>
<h2>Examples</h2>
<p>/sbin/sysctl -a<br />
 /sbin/sysctl -n kernel.hostname<br />
 /sbin/sysctl -w kernel.domainname=&quot;example.com&quot;<br />
 /sbin/sysctl -p/etc/sysctl.conf<br />
 /sbin/sysctl -a &#8211;pattern forward<br />
 /sbin/sysctl -a &#8211;pattern forward$<br />
 /sbin/sysctl -a &#8211;pattern &#8216;net.ipv4.conf.(eth|wlan)0.arp&#8217;<br />
 /sbin/sysctl &#8211;system &#8211;pattern &#8216;^net.ipv6&#8217;</p>
<h2>Deprecated Parameters</h2>
<p>The <code>base_reachable_time</code> and <code>retrans_time</code> are deprecated. The <code>sysctl</code> command does not allow changing values of these parameters. Users who insist to use deprecated kernel interfaces should push values to /proc file system by other means. For example: </p>
<p> echo 256 &gt; /proc/sys/net/ipv6/neigh/eth0/base_reachable_time</p>
<h2>Files</h2>
<p><i>/proc/sys</i><br />
 <i>/etc/sysctl.d/*.conf</i><br />
 <i>/run/sysctl.d/*.conf</i><br />
 <i>/usr/local/lib/sysctl.d/*.conf</i><br />
 <i>/usr/lib/sysctl.d/*.conf</i><br />
 <i>/lib/sysctl.d/*.conf</i><br />
 <i>/etc/sysctl.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-sysctl-conf/">sysctl.conf</a></code>(5) <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)</p>
<h2>Author</h2>
<p>George Staikos</p>
<h2>Reporting Bugs</h2>
<p>Please send bug reports to</p>
