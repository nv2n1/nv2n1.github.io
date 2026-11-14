---
title: "greylist(1)"
name: "greylist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-greylist/"
description: "greylist – command line interface to greylistd(8)"
---

<h2>NAME</h2>
<p> greylist &#8211; command line interface to <code><a href="/docs/linux/man/8-greylistd/">greylistd</a>(8)</code></p>
<h2>SYNOPSIS</h2>
<p> <code>greylist </code>{<code> -h </code>|<code> &#8211;help </code>|<code> help </code>}<br />
 <code>greylist </code> <i>operation &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> This program provides a command line interface to <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8); please refer to that manual page for more information on the purpose and functionality of this program. </p>
<h2>USAGE</h2>
<p> In the following discussion, <i>data&#8230;</i> typically refers to the following <i>triplet</i> of information: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>&lt;sending host&#8217;s IP address&gt;&nbsp;<wbr>&lt;sender [at] address&gt;&nbsp;<wbr>&lt;recipient [at] address&gt;</i> </p>
<p> The following operations are available:</p>
<dl>
<dt><code>add</code> [<code>&#8211;white</code>|<code>&#8211;grey</code>|<code>&#8211;black</code>] <i>data&#8230;</i></p>
<dd> Add <i>data</i> to the corresponding list (<code>white</code> if unspecified). If the <i>triplet</i> of a future mail deliveriy (subject to timeouts) matches this data, the idea is that the message would be accepted, temporarily rejected, or permanently rejected, respectively.</p>
<dt><code>delete</code> <i>data&#8230;</i></p>
<dd> Remove <i>data</i> from all lists. If the data exists in any list, the command returns an exit status of 0, otherwise -1. A message is printed on standard output indicating the action taken.</p>
<dt><code>check</code> [<code>&#8211;white</code>|<code>&#8211;grey</code>|<code>&#8211;black</code>] <i>data&#8230;</i></p>
<dd> Check the current status of <i>data</i>, i.e. if a message delivery would succeed if its <i>triplet</i> matched this data. If a list is specified, the word &quot;true&quot; or &quot;false&quot; is printed, indicating whether the data was in the corresponding list; the exit status is also set accordingly. Otherwise, one of the words &quot;white&quot;, &quot;grey&quot;, and &quot;black&quot; is written on standard output, and the exit status is 0, 1, or 2, respectively. </p>
<p> NOTE: This operation is non-intrusive, and thus does not update any of the greylist data. So, for instance, if the <i>data</i> is currently in the &quot;grey&quot; list, but its minimum retry time (<code>retryMin</code>) has elapsed, the text &quot;white&quot; would be printed. However, unless an <code>update</code> takes place prior to the <code>retryMax</code> timeout, the <i>data</i> would still expire from the &quot;grey&quot; list.</p>
<dt><code>update</code> [<code>&#8211;white</code>|<code>&#8211;grey</code>|<code>&#8211;black</code>] <i>data&#8230;</i></p>
<dd> Same, but also update the greylist data accordingly. So if <i>data</i> is currently greylisted, but the minimum retry time <code>retryMin</code> has elapsed since it was first seen, <i>data</i> is moved to the &quot;white&quot; list. </p>
<p> This operation would normally be used by mail transport agents (MTAs).</p>
<dt><code>stats</code></p>
<dd> Print some statistics on greylist utilization and hits.</p>
<dt><code>mrtg</code></p>
<dd> Print statistics on greylist and whitelist hits in a format that MRTG can use as an External Monitoring Script.</p>
<dt><code>list</code> [<code>&#8211;white</code>] [<code>&#8211;grey</code>] [<code>&#8211;black</code>]</p>
<dd> Print available (original/unhashed) data items from the corresponding list(s). </p>
<p> NOTE: Internally, <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8) hashes the provided data into a single 32-bit value for efficiency. Prior to version 0.6, the original data was not retained; as of version 0.6, data is saved if the &quot;savetriplets&quot; setting in the [data] section of the configuration file is &quot;true&quot;. Only data items (i.e. triplets) that have been seen while this setting were enabled can be listed.</p>
<dt><code>save</code></p>
<dd> Force greylist data to be immediately saved (synchronized) to the filesystem. </p>
<p> Data is also saved after any operation if a certain <i>update interval</i> (default is 300 seconds/5 minutes) has elapsed since the last save, and there are no pending requests to <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8). </p>
<dt><code>reload</code></p>
<dd> Save greylist data to files, then reload configuration and data. </p>
<dt><code>clear</code> [<code>&#8211;white</code>] [<code>&#8211;grey</code>] [<code>&#8211;black</code>]</p>
<dd> Clear all items in the specified list(s), or all lists if none is specified. </p>
<p> If the whitelist is cleared, <i>all</i> new data trilplets will initially be in a &quot;grey&quot; state. </p>
<p> Use with caution!</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>greylist add &#8211;white 1.2.3.4 mailinglist [at] somewhere subscriber [at] yourhost</p>
<dd> Whitelists messages received from the IP address 1.2.3.4 on behalf of &lt;mailinglist [at] somewhere&gt; to &lt;subscriber [at] yourhost&gt;.</p>
<dt>greylist check &#8211;grey 1.2.3.4 mailinglist [at] somewhere subscriber [at] yourhost</p>
<dd> Prints &quot;true&quot; or &quot;false&quot; on standard output, depending on whether mail received from the IP address 1.2.3.4 on behalf of &lt;mailinglist [at] somewhere&gt; to &lt;subscriber [at] yourhost&gt; should be deferred or not, respectively. The data is neither recorded nor changed to a &quot;white&quot; state.</dl>
<h2>FILES</h2>
<h3>/var/run/greylistd/socket</h3>
<p> The UNIX domain socket providing the main interface to &quot;greylistd&quot;. </p>
<h2>AUTHOR</h2>
<p> This python script and manual page is written by Tor Slettnes, originally for Debian GNU/Linux.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2005 Tor Slettnes.</p>
<dl>
<dt>
<dd> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</dl>
<p> On a Debian GNU/Linux system, the full text of the GPL is available in /usr/share/common-licenses/GPL. It is also available at: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8)</p>
<dd> Greylisting daemon.</p>
<dt><code><a href="/docs/linux/man/8-greylistd-setup-exim4/">greylistd-setup-exim4</a></code>(8)</p>
<dd> Utility to add/remove support for greylistd in Exim 4 configuration files. </p>
</dl>
<h2>Index</h2>
