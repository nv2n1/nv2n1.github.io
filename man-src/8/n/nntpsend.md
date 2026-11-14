---
title: "nntpsend(8)"
name: "nntpsend"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nntpsend/"
description: "nntpsend – Send Usenet articles to remote sites"
---

<p>nntpsend &#8211; Send Usenet articles to remote sites</p>
<h2>Synopsis</h2>
<p><code>nntpsend</code> [<code>-acDdlNnpr</code>] [<code>-P</code> <i>portnum</i>] [<code>-s</code> <i>size</i>] [<code>-T</code> <i>timelimit</i>] [<code>-t</code> <i>timeout</i>] [<code>-w</code> <i>delay</i>] [<i>sitename</i> <i>fqdn</i>] &#8230;</p>
<h2>Description</h2>
<p><code>nntpsend</code> is a front-end that invokes <code>innxmit</code> to send Usenet articles to a remote <font SIZE="-1">NNTP</font> site. The sites to be fed may be specified by giving <i>sitename</i> <i>fqdn</i> pairs on the command line. If no such pairs are given, <code>nntpsend</code> defaults to the information given in the <i>nntpsend.ctl</i> config file. The <i>sitename</i> should be the name of the site as specified in the <i>newsfeeds</i> file. The <i>fqdn</i> should be the hostname or <font SIZE="-1">IP</font> address of the remote site. An <code>innxmit</code> is launched for sites with queued news. All <code>innxmit</code> processes are spawned in the background and the script waits for them all to finish before returning. Output is sent to the file <i>nntpsend.log</i> in <i>pathlog</i>. In order to keep from overwhelming the local system, <code>nntpsend</code> waits five seconds before spawning each child. </p>
<p> <code>nntpsend</code> expects that the batch file for a site is named <i>sitename</i> in <i>pathoutgoing</i>. To prevent batch files corruption, <code>shlock</code> is used to &#8220;lock&#8221; these files. When <i>sitename</i> <i>fqdn</i> pairs are given on the command line, any flags given on the command completely describe how <code>innxmit</code> and <code>shrinkfile</code> operate. When no such pairs are given on the command line, then the information found in <i>nntpsend.ctl</i> becomes the default flags for that site. Any flags given on the command line override the default flags for the site. </p>
<p> An alternative to <code>nntpsend</code> can be <code>innduct</code>, mentioned in the <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) man page.</p>
<h2>Options</h2>
<dl>
<dt><code>-D</code>, <code>-d</code></p>
<dd>The <code>-D</code> flag causes <code>nntpsend</code> to send output to stdout rather than the log file <i>nntpsend.log</i> in <i>pathlog</i>. The <code>-d</code> flag does the same and it passes <code>-d</code> to all <code>innxmit</code> invocations, which in turn causes <code>innxmit</code> to go into debug mode.</p>
<dt><code>-n</code></p>
<dd>If the <code>-n</code> flag is used, then <code>nntpsend</code> does not use <code>shlock</code> to lock the use of <code>nntpsend</code>. Batch files will still be locked.</p>
<dt><code>-s</code> <i>size</i></p>
<dd>If the <code>-s</code> flag is used, then <code>shrinkfile</code> will be invoked to perform a head truncation of <i>size</i> bytes on the batch file and the flag will be passed to it.</p>
<dt><code>-w</code> <i>delay</i></p>
<dd>If the <code>-w</code> flag is used, then <code>nntpsend</code> waits for <i>delay</i> seconds after flushing the site before launching <code>innxmit</code>.</p>
<dt><code>-a</code>, <code>-c</code>, <code>-l</code>, <code>-N</code>, <code>-P</code> <i>portnum</i>, <code>-p</code>, <code>-r</code>, <code>-T</code> <i>timelimit</i>, <code>-t</code> <i>timeout</i></p>
<dd>The <code>-a</code>, <code>-c</code>, <code>-l</code>, <code>-P</code> <i>portnum</i>, <code>-p</code>, <code>-r</code>, <code>-T</code> <i>timelimit</i> and <code>-t</code> <i>timeout</i> flags are passed on to the child <code>innxmit</code> program. The <code>-N</code> flag is passed as <code>-s</code> flag to the child <code>innxmit</code> program. See <i><a href="/docs/linux/man/8-innxmit/">innxmit</a></i>(8) for more details. </p>
<p> Note that if the <code>-p</code> flag is used, then no connection is made and no articles are fed to the remote site. It is useful to have <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8) invoke <code>nntpsend</code> with this flag in case a site cannot be reached for an extended period of time.</dl>
<h2>Examples</h2>
<p>With the following <i>nntpsend.ctl</i> config file: </p>
<pre> nsavax:erehwon.nsavax.gov::-t60
 group70:group70.org::
 walldrug:walldrug.com:4m-1m:-T1800 -t300
 kremvax:kremvax.cis:2m:</pre>
<p>the command <tt>&quot;nntpsend&quot;</tt> will result in the following: </p>
<pre> Sitename Truncation innxmit flags
 nsavax (none) -a -t60
 group70 (none) -a -t180
 walldrug 1m if &gt;4m -T1800 -t300
 kremvax 2m -t180</pre>
<p>The command <tt>&quot;nntpsend -d -T1200&quot;</tt> will result in the following: </p>
<pre> Sitename Truncation innxmit flags
 nsavax (none) -a -d -T1200 -t60
 group70 (none) -a -d -T1200 -t180
 walldrug 1m if &gt;4m -d -T1200 -t300
 kremvax 2m -d -T1200 -t180</pre>
<p>The command <tt>&quot;nntpsend -s 5m -T1200 nsavax erehwon.nsavax.gov group70 group70.org&quot;</tt> will result in the following: </p>
<pre> Sitename Truncation innxmit flags
 nsavax 5m -T1200 -t180
 group70 5m -T1200 -t180</pre>
<p>Remember that <code>-a</code> is always given when there is no size limit, and <code>-t</code> defaults to <tt>180</tt>.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> nntpsend.pod 9590 2013-12-19 17:48:22Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/1-innxmit/">innxmit</a></i>(1), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/5-nntpsend-ctl/">nntpsend.ctl</a></i>(5), <i><a href="/docs/linux/man/1-shlock/">shlock</a></i>(1), <i><a href="/docs/linux/man/1-shrinkfile/">shrinkfile</a></i>(1). </p>
