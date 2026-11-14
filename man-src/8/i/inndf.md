---
title: "inndf(8)"
name: "inndf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-inndf/"
description: "inndf – Report free disk, inodes, and overview information"
---

<p>inndf &#8211; Report free disk, inodes, and overview information</p>
<h2>Synopsis</h2>
<p><code>inndf</code> [<code>-Fhi</code>] [<code>-f</code> <i>filename</i>] <i>directory</i> [<i>directory</i> &#8230;] </p>
<p> <code>inndf</code> <code>-n</code> </p>
<p> <code>inndf</code> <code>-o</code></p>
<h2>Description</h2>
<p><code>inndf</code> was originally a replacement for <tt>&quot;df | awk&quot;</tt> in <i><a href="/docs/linux/man/5-innwatch-ctl/">innwatch.ctl</a></i>(5) and <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8), and now also reports various other usage information about <font SIZE="-1">INN</font>&#8216;s storage that <i><a href="/docs/linux/man/1-df/">df</a></i>(1) doesn&#8217;t understand. <code>inndf</code> doesn&#8217;t sync, forks less, and is generally less complicated than <i><a href="/docs/linux/man/1-df/">df</a></i>(1). </p>
<p> Its default behavior is to report free kilobytes (not disk blocks), or free inodes if <code>-i</code> is used, in the file systems holding the directories given on the command line. (A kilobyte in this case is 1024 bytes.) If only one directory is given, the output will be a simple number; if more than one directory is given, the output will be formatted for human readability. </p>
<p> If <i>enableoverview</i> is set to true in <i>inn.conf</i>, <code>inndf</code> can also be used to get information about the overview database. With the <code>-n</code> option, it reports a count of the total number of overview records stored. With <code>-o</code>, it reports the percentage of space used in the overview database (for those overview methods where this is meaningful data).</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>filename</i></p>
<dd><i>filename</i> should contain a list of directories to use in addition to those given by the arguments, one per line. Blank lines and anything after <tt>&quot;#&quot;</tt> on any line are ignored.</p>
<dt><code>-F</code></p>
<dd>Like <code>-f</code> except that the filename is <i>pathetc</i>/filesystems and it is not an error if this file doesn&#8217;t exist. (This option is used primarily by such things as <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8), so that the news administrator can add additional file systems to check to <i>pathetc</i>/filesystems without having to modify the script.)</p>
<dt><code>-h</code></p>
<dd>Print a usage message and exit.</p>
<dt><code>-i</code></p>
<dd>Report the number of free inodes rather than the amount of free disk space.</p>
<dt><code>-n</code></p>
<dd>Report the total number of records in the overview database. Note that crossposted articles will have one overview record for each newsgroup they&#8217;re posted to.</p>
<dt><code>-o</code></p>
<dd>Report the percentage usage of the overview database space. This is only meaningful for overview methods that pre-allocate a certain amount of space rather than grow to accomodate more records. Currently, this flag is only useful for the buffindexed overview method.</dl>
<h2>Examples</h2>
<p>Print the free kilobytes in <i>pathspool</i> as a simple number: </p>
<pre> inndf &lt;pathspool in inn.conf&gt;</pre>
<p>Report the free inodes in <i>pathnews</i> and <i>pathspool</i> in a format designed for human readability: </p>
<pre> inndf -i &lt;pathnews&gt; &lt;pathspool&gt;</pre>
<p>The same, but also add in all file systems in <i>pathetc</i>/filesystems: </p>
<pre> inndf -i -F &lt;pathnews&gt; &lt;pathspool&gt;</pre>
<p>Print out the number of overview records and the percentage space used by a buffindexed overview database: </p>
<pre> inndf -no</pre>
<h2>History</h2>
<p><code>inndf</code> was written by Ian Dickinson &lt;idickins [at] fore.com&gt;. This manual page was written by Swa Frantzen &lt;Swa.Frantzen [at] belgium.eu.net&gt;. Thanks also to the following folks for ports, patches, and comments: </p>
<pre> Mahesh Ramachandran &lt;rr [at] eel.ufl.edu&gt;
 Chuck Swiger &lt;chuck [at] its.com&gt;
 Sang-yong Suh &lt;sysuh [at] kigam.re.kr&gt;
 Brad Dickey &lt;bdickey [at] haverford.edu&gt;
 Taso N. Devetzis &lt;devetzis [at] snet.net&gt;
 Wei-Yeh Lee &lt;weiyeh [at] columbia.edu&gt;
 Jeff Garzik &lt;jeff.garzik [at] spinne.com&gt;</pre>
<p>and to all the other folks I met and worked with during my 10 years as a newsadmin. </p>
<p> Katsuhiro Kondou added the <code>-n</code> and <code>-o</code> options. Russ Allbery added reporting of percentage free disk space. Support for <code>-f</code> and <code>-F</code> was added by Fabien Tassin &lt;fta [at] sofaraway.org&gt;. </p>
<p> <tt>$Id:</tt> inndf.pod 8232 2008-12-14 17:05:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-df/">df</a></i>(1), <i><a href="/docs/linux/man/5-innwatch-ctl/">innwatch.ctl</a></i>(5), <i><a href="/docs/linux/man/8-innstat/">innstat</a></i>(8). </p>
