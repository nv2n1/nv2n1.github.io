---
title: "newscache(8)"
name: "newscache"
section: "8"
letter: "n"
url: "/docs/linux/man/8-newscache/"
description: "newscache – Cache for Network News Transport Protocol (NNTP)"
---

<p>newscache &#8211; Cache for Network News Transport Protocol (NNTP)</p>
<h2>Synopsis</h2>
<p><code>newscache</code> [&#8211;version] [-h] [-v] [-f] [-c config-file] [-i] [-d] [-p] [-o]</p>
<h2>Description</h2>
<p>NewsCache is a free cache server for USENET News. NewsCache acts to news reading clients like a news server, except that it stores only those articles that have been requested by at least one client. NewsCache targets problems of the current News System like network bandwidth consumption or the IO load caused by news clients. NewsCache acts to the upstream news server like a news reader programm.</p>
<dl>
<dt>It supports principles the following modes (for a detailed description read ServerSpec Configuration Options below):</p>
<dd>
<dt><i>cached</i></p>
<dd>NewsCache store every retrieved article in his internal cache. If this article is retrieved by another news reader client, then NewsCache can get the article from his cache instead of retrieving this article again from the upstream newsserver.</p>
<dt><i>not-cached</i></p>
<dd>NewsCache act as a &quot;proxy&quot; and does&#8217;nt store retrieved article in his local cache. This is usefull for combined multiple local newsserver configuration.</p>
<dt><i>offline</i></p>
<dd>NewsCache does&#8217;nt connect to the upstream newsserver. Only the specified newsgroups are retrieved by <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and stored in the cache. This is usefull in dialup configurations. The news reader clients can only access this newsgroups.</p>
<dt><i>semi-offline, cached</i></p>
<dd>The overview informations are loaded with <code><a href="/docs/linux/man/8-updatenews/">updatenews</a>(8)</code> and the articles retrieved by NewsCache, if a news reader client request it. The article is stored in the internal cache. </p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. For a complete description, see the Info files.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Show version of program.</p>
<dt><code>-f &#8211;fqdn</code></p>
<dd>Print what newscache thinks is the fully qualified domain name.</p>
<dt><code>-c &#8211;configuration config-file</code></p>
<dd>
<dt><code>-i &#8211;inetd</code></p>
<dd>newscache is used with inetd and read from stdin.</p>
<dt><code>-d &#8211;debug</code></p>
<dd>Do not detach.</p>
<dt><code>-p &#8211;print-parameter</code></p>
<dd>Print current parameter settings.</p>
<dt><code>-o &#8211;configuration-options</code></p>
<dd>Print all options specified in the configure phase. </p>
</dl>
<h2>Signals</h2>
<dl>
<dt><code>SIGTERM, SIGQUIT, SIGINT, SIGPIPE</code></p>
<dd>These signals instruct NewsCache to abort any existing transfers, close all connections and terminate the process. If the target of the signal is the daemon, all current child processes wil also be terminated. </p>
<dt><code>SIGHUP</code></p>
<dd>This signal instruct NewsCache to reread its configuration file <i>/etc/newscache.conf</i> . </p>
</dl>
<h2>Notes</h2>
<p>Running NewsCache in <code>inetd</code> mode requires a correct inetd configuration. An example configuration line looks like: <code>news stream tcp nowait news /usr/sbin/newscache -i</code> </p>
<h2>Diagnostics</h2>
<p>NewsCache logs diagnostics messages with the syslog priority debug. If NewsCache is configured with the <code>&#8211;enabe-debug</code> option, he produce much more messages (for details see the INSTALL file). <code>newscache -o </code> prints out the actual configuration parameter. In some error situation you can try to create a core dump file or debug a client process with gdb (for details see the documentation directory).</p>
<h2>Files</h2>
<p>/etc/newscache.conf<br />
 /usr/sbin/newscache<br />
 /usr/sbin/newscacheclean<br />
 /usr/sbin/newscacheclean<br />
 /usr/sbin/updatenews</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-newscache-conf/">newscache.conf</a></code>(5), <code><a href="/docs/linux/man/8-newscacheclean/">newscacheclean</a></code>(8), <code><a href="/docs/linux/man/8-updatenews/">updatenews</a></code>(8). </p>
<h2>Authors</h2>
<p>1997-2000 Thomas Gschwind &lt;tom [at] infosys.tuwien.ac.at&gt;<br />
 2001-2004 Herbert Straub &lt;h.straub [at] aon.at&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;newscache [at] linuxhacker.org&gt;.</p>
<h2>Copyright</h2>
<p><code>NewsCache</code> is released under the <code>GNU General Public License (GPL).</code> There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
