---
title: "send-uucp(8)"
name: "send-uucp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-send-uucp/"
description: "send-uucp – Send Usenet articles via UUCP"
---

<p>send-uucp &#8211; Send Usenet articles via UUCP</p>
<h2>Synopsis</h2>
<p><code>send-uucp</code> [<i>site</i> &#8230;]</p>
<h2>Description</h2>
<p>The <code>send-uucp</code> program processes batch files written by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) to send Usenet articles to <font SIZE="-1">UUCP</font> sites. It reads a configuration file to control how it behaves with various sites. Normally, it is run periodically out of cron to put together batches and send them to remote <font SIZE="-1">UUCP</font> sites. </p>
<p> It makes it possible to reduce bandwidth usage and to send news to remote <font SIZE="-1">UUCP</font> sites which cannot receive a real-time feed (for instance if they are over dial-up connections).</p>
<h2>Options</h2>
<p>Any arguments provided to the program are interpreted as a list of sites specified in <i>send-uucp.cf</i> for which batches should be generated. If no arguments are supplied then batches will be generated for all sites listed in that configuration file.</p>
<h2>Configuration</h2>
<p>The sites to which articles are to be sent must be configured in the configuration file <i>send-uucp.cf</i> in <i>pathetc</i> as set in <i>inn.conf</i>. Each site is specified with a line of the form: </p>
<pre> site[:host[:funnel]] [compressor [maxsize [batchtime]]]</pre>
<dl>
<dt><i>site</i></p>
<dd>The news site name being configured. This must match a site name from <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5).</p>
<dt><i>host</i></p>
<dd>The <font SIZE="-1">UUCP</font> host name to which batches should be sent for this site. If omitted, the news site name will be used as the <font SIZE="-1">UUCP</font> host name.</p>
<dt><i>funnel</i></p>
<dd>In the case of a site configured as a funnel, <code>send-uucp</code> needs to flush the channel (or exploder) being used as the target of the funnel instead of flushing the site. This is the way to tell <code>send-uucp</code> the name of the channel or exploder to flush for this site. If not specified, default to flushing the site.</p>
<dt><i>compressor</i></p>
<dd>The compression method to use for batches. This should be one of <tt>&quot;bzip2&quot;</tt>, <tt>&quot;compress&quot;</tt>, <tt>&quot;gzip&quot;</tt> or <tt>&quot;none&quot;</tt>. Arguments for the compression command may be specified by using <tt>&quot;_&quot;</tt> instead of spaces. For example, <tt>&quot;gzip_-9&quot;</tt>. The default value is <tt>&quot;gzip&quot;</tt>.</p>
<dt><i>maxsize</i></p>
<dd>The maximum size in bytes of a single batch <i>before</i> compression. The default value is <tt>500000</tt> bytes.</p>
<dt><i>batchtime</i></p>
<dd>A comma separated list of hours during which batches should be generated for a given site. When <code>send-uucp</code> runs, a site will only be processed if the current hour matches one of the hours in <i>batchtime</i>. The default is no limitation on when to generate batches.</dl>
<p> Fields are separated by spaces and only the site name needs to be specified, with defaults being used for unspecified values. If the first character on a line is a hash sign (<tt>&quot;#&quot;</tt>) then the rest of the line is ignored.</p>
<h2>Example</h2>
<p>Here is an example for the <i>send-uucp.cf</i> configuration file: </p>
<pre> zoetermeer gzip 1048576 5,18,22
 hoofddorp gzip 1048576 5,18,22
 pa3ebv gzip 1048576 5,18,22
 drinkel bzip2 1048576 5,6,18,20,22,0,2
 manhole compress 1048576 5,18,22
 owl compress 1048576
 able
 pern::MYFUNNEL!</pre>
<p>This defines eight <font SIZE="-1">UUCP</font> sites. The first three and the last two use <tt>&quot;gzip&quot;</tt> compression, the fourth site (<tt>&quot;drinkel&quot;</tt>) uses <tt>&quot;bzip2&quot;</tt> and the remaining sites (<tt>&quot;manhole&quot;</tt> and <tt>&quot;owl&quot;</tt>) use <tt>&quot;compress&quot;</tt>. The first six use a batch size of 1&nbsp;<wbr><font SIZE="-1">MB,</font> and the two last sites (<tt>&quot;able&quot;</tt> and <tt>&quot;pern&quot;</tt>) use the default of 500,000 bytes. The <tt>&quot;zoetermeer&quot;</tt>, <tt>&quot;hoofddorp&quot;</tt>, <tt>&quot;pa3ebv&quot;</tt>, and <tt>&quot;manhole&quot;</tt> sites will only have batches generated for them during the hours of 05:00, 18:00, and 22:00, and the <tt>&quot;drinkel&quot;</tt> site will only have batches generated during those hours and 06:00, 20:00, 00:00, and 02:00. There are no restrictions on when batches will be generated for <tt>&quot;owl&quot;</tt>, <tt>&quot;able&quot;</tt> and <tt>&quot;pern&quot;</tt>. </p>
<p> The <tt>&quot;pern&quot;</tt> site is configured as a funnel into <tt>&quot;MYFUNNEL!&quot;</tt>. <code>send-uucp</code> will issue <tt>&quot;ctlinnd flush MYFUNNEL!&quot;</tt> instead of <tt>&quot;ctlinnd flush pern&quot;</tt>. </p>
<p> As for the <i>newsfeeds</i> file, the usual flags used for a <font SIZE="-1">UUCP</font> feed are <tt>&quot;Tf,Wnb&quot;</tt>. Here is a typical entry for <tt>&quot;zoetermeer&quot;</tt>, where the batching is kept between 4&nbsp;<wbr><font SIZE="-1">KB</font> and 1&nbsp;<wbr><font SIZE="-1">KB:</font> </p>
<pre> zoetermeer\
 :*,!junk,!control,!control.*/!foo\
 :Tf,Wnb,B4096/1024:</pre>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/send-uucp</p>
<dd>The Perl script itself used to create news batches from the outgoing files.</p>
<dt><i>pathetc</i>/send-uucp.cf</p>
<dd>The configuration file which specifies a list of sites to be processed.</dl>
<h2>History</h2>
<p>This program was originally written by Edvard Tuinder &lt;ed [at] elm.net&gt; and then maintained and extended by Miquel van Smoorenburg &lt;miquels [at] cistron.nl&gt;. Marco d&#8217;Itri &lt;md [at] linux.it&gt; cleaned up the code for inclusion in <font SIZE="-1">INN. </font> This manual page was written by Mark Brown &lt;broonie [at] sirena.org.uk&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/8-uucp/">uucp</a></i>(8). </p>
