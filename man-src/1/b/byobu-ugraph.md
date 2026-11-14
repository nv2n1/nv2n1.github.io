---
title: "byobu-ugraph(1)"
name: "byobu-ugraph"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byobu-ugraph/"
description: "byobu-ugraph – helper script for notification history graphs"
---

<h2>NAME</h2>
<p> <code>byobu-ugraph</code> &#8211; helper script for notification history graphs </p>
<h2>DESCRIPTION</h2>
<p> <code>byobu-ugraph</code> is a helper script that can be used to create history graphs </p>
<h2>USAGE</h2>
<p> <code>byobu-ugraph</code> [options] [command [args&#8230;]] </p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>-f&nbsp;<wbr>&lt;file&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: File to read data points from.&nbsp;<wbr>&nbsp;<wbr>(only required if no command specified).<br />
&nbsp;<wbr>&nbsp;<wbr>-h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Show this help.<br />
&nbsp;<wbr>&nbsp;<wbr>-m&nbsp;<wbr>&lt;num&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Minimum value&nbsp;<wbr>(default=$min_default).<br />
&nbsp;<wbr>&nbsp;<wbr>-n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Supress output of newline character.<br />
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&lt;points&gt;&nbsp;<wbr>: Specify number of data points in graph&nbsp;<wbr>(default=$points_default).<br />
&nbsp;<wbr>&nbsp;<wbr>-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Do not rotate file&nbsp;<wbr>&lt;file&gt;&nbsp;<wbr>(default is to rotate).&nbsp;<wbr>&nbsp;<wbr>Option implies file&nbsp;<wbr>&lt;file&gt;&nbsp;<wbr>should not be written to so a command cannot follow script options in this case.<br />
&nbsp;<wbr>&nbsp;<wbr>-t&nbsp;<wbr>&lt;theme&gt;&nbsp;<wbr>&nbsp;<wbr>:&nbsp;<wbr>&#8216;byobu-ulevel&#8217;&nbsp;<wbr>theme to use&nbsp;<wbr>(default=$theme_default).<br />
&nbsp;<wbr>&nbsp;<wbr>-x&nbsp;<wbr>&lt;num&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Maximum value&nbsp;<wbr>(default=$max_default). </p>
<h2>EXAMPLES</h2>
<p> Using byobu-ugraph to run a command, rotate log and display graph. </p>
<p> Here we specify a command to display available memory. Trailing echo adds a required newline Note no filename specified. </p>
<p>&nbsp;<wbr>byobu-ugraph&nbsp;<wbr>&quot;(/usr/lib/byobu/mem_used | sed -e&nbsp;<wbr>&#8216;s/%&nbsp;<wbr>//g&#8217;;echo)&quot; </p>
<p> Using byobu-ugraph just to rotate log and display the graph </p>
<p>&nbsp;<wbr>file=/tmp/load.dat<br />
&nbsp;<wbr>awk&nbsp;<wbr>&#8216;{&nbsp;<wbr>print&nbsp;<wbr>$1}&#8217;&nbsp;<wbr>/proc/loadavg&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$file<br />
&nbsp;<wbr>#&nbsp;<wbr>Note: we need to specify what we consider to be a&nbsp;<wbr>&quot;reasonable&quot;&nbsp;<wbr>maximum load<br />
&nbsp;<wbr>byobu-ugraph -m 3.0 -f&nbsp;<wbr>$file </p>
<h2>NOTES</h2>
<p> If you specify &#8216;command&#8217;, care must be taken with shell quoting to avoid expansion prior to this script running the command. </p>
<p> If &#8216;-r&#8217; is not specified, the file &lt;file&gt; will be rotated such that at most &lt;points&gt; lines are retained on each invocation of this script. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-byobu/">byobu</a></code>(1) </p>
<dl>
<dt><i><a rel="nofollow" href="http://byobu.co">http://byobu.co</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This utility was written by James Hunt &lt;james.hunt [at] canonical.com&gt;, and this manpage was written by Dustin Kirkland &lt;kirkland [at] byobu.co&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document and the utility under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> The complete text of the GNU General Public License can be found in <i>/usr/share/common-licenses/GPL</i> on Debian/Ubuntu systems, or in <i>/usr/share/doc/fedora-release-*/GPL</i> on Fedora systems, or on the web at <i><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.txt">http://www.gnu.org/licenses/gpl.txt</a></i>. </p>
<h2>Index</h2>
