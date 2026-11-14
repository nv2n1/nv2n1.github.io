---
title: "storage-conf(5)"
name: "storage-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-storage-conf/"
description: "storage.conf – Configuration file for storage manager"
---

<p>storage.conf &#8211; Configuration file for storage manager</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/storage.conf contains the rules to be used in assigning articles to different storage methods. These rules determine where incoming articles will be stored. </p>
<p> The storage manager is a unified interface between <font SIZE="-1">INN</font> and a variety of different storage methods, allowing the news administrator to choose between different storage methods with different trade-offs (or even use several at the same time for different newsgroups, or articles of different sizes). The rest of <font SIZE="-1">INN</font> need not care what type of storage method was used for a given article; the storage manager will figure this out automatically when that article is retrieved via the storage <font SIZE="-1">API</font>. Note that you may also want to see the options provided in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) regarding article storage. </p>
<p> The <i>storage.conf</i> file consists of a series of storage method entries. Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. The maximum number of characters in each line is 255. The order of entries in this file is important, see below. </p>
<p> Each entry specifies a storage method and a set of rules. Articles which match all of the rules of a storage method entry will be stored using that storage method; if an article matches multiple storage method entries, the first one will be used. Each entry is formatted as follows: </p>
<pre> method &lt;methodname&gt; {
 class: &lt;storage_class&gt;
 newsgroups: &lt;wildmat&gt;
 size: &lt;minsize&gt;[,&lt;maxsize&gt;]
 expires: &lt;mintime&gt;[,&lt;maxtime&gt;]
 options: &lt;options&gt;
 exactmatch: &lt;bool&gt;
 }</pre>
<p>If spaces or tabs are included in a value, that value must be enclosed in double quotes (&quot;&quot;). If either a number sign (<tt>&quot;#&quot;</tt>) or a double quote are meant to be included verbatim in a value, they should be escaped with <tt>&quot;\&quot;</tt>. </p>
<p> &lt;methodname&gt; is the name of a storage method to use for articles which match the rules of this entry. The currently available storage methods are: </p>
<pre> cnfs
 timecaf
 timehash
 tradspool
 trash</pre>
<p>See the &#8220;<font SIZE="-1">STORAGE</font> <font SIZE="-1">METHODS</font>&#8221; section below for more details. </p>
<p> The meanings of the keys in each storage method entry are as follows:</p>
<dl>
<dt><i>class</i>: &lt;storage_class&gt;</p>
<dd>An identifier for this storage method entry. &lt;storage_class&gt; should be a number between 0 and 255. It should be unique across all of the entries in this file. It is mainly used for specifying expiration times by storage class as described in <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5); <tt>&quot;timehash&quot;</tt> and <tt>&quot;timecaf&quot;</tt> will also set the top-level directory in which articles accepted by this storage class are stored. The assignment of a particular number to a storage class is arbitrary but permanent (since it is used in storage tokens). Storage classes can be for instance numbered sequentially in <i>storage.conf</i>.</p>
<dt><i>newsgroups</i>: &lt;wildmat&gt;</p>
<dd>What newsgroups are stored using this storage method. &lt;wildmat&gt; is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern which is matched against the newsgroups an article is posted to. If <i>storeonxref</i> in <i>inn.conf</i> is true, this pattern will be matched against the newsgroup names in the Xref: header; otherwise, it will be matched against the newsgroup names in the Newsgroups: header (see <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for discussion of the differences between these possibilities). Poison wildmat expressions (expressions starting with <tt>&quot;@&quot;</tt>) are allowed and can be used to exclude certain group patterns: articles crossposted to poisoned newsgroups will not be stored using this storage method. The &lt;wildmat&gt; pattern is matched in order. </p>
<p> There is no default newsgroups pattern; if an entry should match all newsgroups, use an explicit <tt>&quot;newsgroups: *&quot;</tt>.</p>
<dt><i>size</i>: &lt;minsize&gt;[,&lt;maxsize&gt;]</p>
<dd>A range of article sizes (in bytes) which should be stored using this storage method. If &lt;maxsize&gt; is <tt>0</tt> or not given, the upper size of articles is limited only by <i>maxartsize</i> in <i>inn.conf</i>. The size: field is optional and may be omitted entirely if you want articles of any size to be stored in this storage method (if, of course, these articles fulfill all the other requirements of this storage method entry). By default, &lt;minsize&gt; is set to <tt>0</tt>.</p>
<dt><i>expires</i>: &lt;mintime&gt;[,&lt;maxtime&gt;]</p>
<dd>A range of article expiration times which should be stored using this storage method. Be careful; this is less useful than it may appear at first. This is based <code>only</code> on the Expires: header of the article, not on any local expiration policies or anything in <i>expire.ctl</i>! If &lt;mintime&gt; is non-zero, then this entry <code>will not match</code> any article without an Expires: header. This key is therefore only really useful for assigning articles with requested longer expire times to a separate storage method. Articles only match if the time until expiration (that is to say, the amount of time into the future that the Expires: header of the article requests that it remain around) falls in the interval specified by &lt;mintime&gt; and &lt;maxtime&gt;. </p>
<p> The format of these parameters is <tt>&quot;0d0h0m0s&quot;</tt> (days, hours, minutes, and seconds into the future). If &lt;maxtime&gt; is <tt>&quot;0s&quot;</tt> or is not specified, there is no upper bound on expire times falling into this entry (note that this key has no effect on when the article will actually be expired, but only on whether or not the article will be stored using this storage method). This field is also optional and may be omitted entirely if you do not want to store articles according to their Expires: header, if any. </p>
<p> A &lt;mintime&gt; value greater than <tt>&quot;0s&quot;</tt> implies that this storage method won&#8217;t match any article without an Expires: header.</p>
<dt><i>options</i>: &lt;options&gt;</p>
<dd>This key is for passing special options to storage methods that require them (currently only <tt>&quot;cnfs&quot;</tt>). See the &#8220;<font SIZE="-1">STORAGE</font> <font SIZE="-1">METHODS</font>&#8221; section below for a description of its use.</p>
<dt><i>exactmatch</i>: &lt;bool&gt;</p>
<dd>If this key is set to true, all the newsgroups in the Newsgroups: header of incoming articles will be examined to see if they match newsgroups patterns. (Normally, any non-zero number of matching newsgroups is sufficient, provided no newsgroup matches a poison wildmat as described above.) This is a boolean value; <tt>&quot;true&quot;</tt>, <tt>&quot;yes&quot;</tt> and <tt>&quot;on&quot;</tt> are usable to enable this key. The case of these values is not significant. The default is false.</dl>
<p> If an article matches all of the constraints of an entry, it is stored via that storage method and is associated with that &lt;storage_class&gt;. This file is scanned in order and the first matching entry is used to store the article. </p>
<p> If an article does not match any entry, either by being posted to a newsgroup which does not match any of the &lt;wildmat&gt; patterns or by being outside the size and expires ranges of all entries whose newsgroups pattern it does match, the article is not stored and is rejected by <code>innd</code>. When this happens, the error message: </p>
<pre> cant store article: no matching entry in storage.conf</pre>
<p>is logged to syslog. If you want to silently drop articles matching certain newsgroup patterns or size or expires ranges, assign them to the <tt>&quot;trash&quot;</tt> storage method rather than having them not match any storage method entry.</p>
<h2>Storage Methods</h2>
<p>Currently, there are five storage methods available. Each method has its pros and cons; you can choose any mixture of them as is suitable for your environment. Note that each method has an attribute <font SIZE="-1">EXPENSIVESTAT</font> which indicates whether checking the existence of an article is expensive or not. This is used to run <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8).</p>
<dl>
<dt><code>cnfs</code></p>
<dd>The <tt>&quot;cnfs&quot;</tt> storage method stores articles in large cyclic buffers (<font SIZE="-1">CNFS</font> stands for Cyclic News File System). Articles are stored in <font SIZE="-1">CNFS</font> buffers in arrival order, and when the buffer fills, it wraps around to the beginning and stores new articles over the top of the oldest articles in the buffer. The expire time of articles stored in <font SIZE="-1">CNFS</font> buffers is therefore entirely determined by how long it takes the buffer to wrap around, which depends on how quickly data is being stored in it. (This method is therefore said to have self-expire functionality.) <font SIZE="-1">EXPENSIVESTAT</font> is false for this method. </p>
<p> <font SIZE="-1">CNFS</font> has its own configuration file, <i>cycbuff.conf</i>, which describes some subtleties to the basic description given above. Storage method entries for the <tt>&quot;cnfs&quot;</tt> storage method must have an options: field specifying the metacycbuff into which articles matching that entry should be stored; see <i><a href="/docs/linux/man/5-cycbuff-conf/">cycbuff.conf</a></i>(5) for details on metacycbuffs. </p>
<p> Advantages: By far the fastest of all storage methods (except for <tt>&quot;trash&quot;</tt>), since it eliminates the overhead of dealing with a file system and creating new files. Unlike all other storage methods, it does not require manual article expiration. With <font SIZE="-1">CNFS</font>, the server will never throttle itself due to a full spool disk, and groups are restricted to just the buffer files given so that they can never use more than the amount of disk space allocated to them. </p>
<p> Disadvantages: Article retention times are more difficult to control because old articles are overwritten automatically. Attacks on Usenet, such as flooding or massive amounts of spam, can result in wanted articles expiring much faster than intended (with no warning).</p>
<dt><code>timecaf</code></p>
<dd>This method stores multiple articles in one file, whose name is based on the article&#8217;s arrival time and the storage class. The file name will be: </p>
<pre> &lt;patharticles&gt;/timecaf-nn/bb/aacc.CF</pre>
<p>where <tt>&quot;nn&quot;</tt> is the hexadecimal value of &lt;storage_class&gt;, <tt>&quot;bb&quot;</tt> and <tt>&quot;aacc&quot;</tt> are the hexadecimal components of the arrival time, and <tt>&quot;CF&quot;</tt> is a hardcoded extension. (The arrival time, in seconds since the epoch, is converted to hexadecimal and interpreted as <tt>0xaabbccdd</tt>, with <tt>&quot;aa&quot;</tt>, <tt>&quot;bb&quot;</tt>, and <tt>&quot;cc&quot;</tt> used to build the path.) This method does not have self-expire functionality (meaning <code>expire</code> has to run periodically to delete old articles). <font SIZE="-1">EXPENSIVESTAT</font> is false for this method. </p>
<p> Advantages: It is roughly four times faster than <tt>&quot;timehash&quot;</tt> for article writes, since much of the file system overhead is bypassed, while still retaining the same fine control over article retention time. </p>
<p> Disadvantages: Using this method means giving up all but the most careful manually fiddling with the article spool; in this aspect, it looks like <tt>&quot;cnfs&quot;</tt>. As one of the newer and least widely used storage types, <tt>&quot;timecaf&quot;</tt> has not been as thoroughly tested as the other methods.</p>
<dt><code>timehash</code></p>
<dd>This method is very similar to <tt>&quot;timecaf&quot;</tt> except that each article is stored in a separate file. The name of the file for a given article will be: </p>
<pre> &lt;patharticles&gt;/time-nn/bb/cc/yyyy-aadd</pre>
<p>where <tt>&quot;nn&quot;</tt> is the hexadecimal value of &lt;storage_class&gt;, <tt>&quot;yyyy&quot;</tt> is a hexadecimal sequence number, and <tt>&quot;bb&quot;</tt>, <tt>&quot;cc&quot;</tt>, and <tt>&quot;aadd&quot;</tt> are components of the arrival time in hexadecimal (the arrival time is interpreted as documented above under <tt>&quot;timecaf&quot;</tt>). This method does not have self-expire functionality. <font SIZE="-1">EXPENSIVESTAT</font> is true for this method. </p>
<p> Advantages: Heavy traffic groups do not cause bottlenecks, and a fine control of article retention time is still possible. </p>
<p> Disadvantages: The ability to easily find all articles in a given newsgroup and manually fiddle with the article spool is lost, and <font SIZE="-1">INN</font> still suffers from speed degradation due to file system overhead (creating and deleting individual files is a slow operation).</p>
<dt><code>tradspool</code></p>
<dd>Traditional spool, or <tt>&quot;tradspool&quot;</tt>, is the traditional news article storage format. Each article is stored in an individual text file named: </p>
<pre> &lt;patharticles&gt;/news/group/name/nnnnn</pre>
<p>where <tt>&quot;news/group/name&quot;</tt> is the name of the newsgroup to which the article was posted with each period changed to a slash, and <tt>&quot;nnnnn&quot;</tt> is the sequence number of the article in that newsgroup. For crossposted articles, the article is linked into each newsgroup to which it is crossposted (using either hard or symbolic links). This is the way versions of <font SIZE="-1">INN</font> prior to 2.0 stored all articles, as well as being the article storage format used by C News and earlier news systems. This method does not have self-expire functionality. <font SIZE="-1">EXPENSIVESTAT</font> is true for this method. </p>
<p> Advantages: It is widely used and well-understood; it can read article spools written by older versions of <font SIZE="-1">INN</font> and it is compatible with all third-party <font SIZE="-1">INN</font> add-ons. This storage mechanism provides easy and direct access to the articles stored on the server and makes writing programs that fiddle with the news spool very easy, and gives fine control over article retention times. </p>
<p> Disadvantages: It takes a very fast file system and I/O system to keep up with current Usenet traffic volumes due to file system overhead. Groups with heavy traffic tend to create a bottleneck because of inefficiencies in storing large numbers of article files in a single directory. It requires a nightly expire program to delete old articles out of the news spool, a process that can slow down the server for several hours or more.</p>
<dt><code>trash</code></p>
<dd>This method silently discards all articles stored in it. Its only real uses are for testing and for silently discarding articles matching a particular storage method entry (for whatever reason). Articles stored in this method take up no disk space and can never be retrieved, so this method has self-expire functionality of a sort. <font SIZE="-1">EXPENSIVESTAT</font> is false for this method.</dl>
<h2>Examples</h2>
<p>The following sample <i>storage.conf</i> file would store all articles posted to alt.binaries.* in the <tt>&quot;BINARIES&quot;</tt> <font SIZE="-1">CNFS</font> metacycbuff, all articles over roughly 50&nbsp;<wbr><font SIZE="-1">KB</font> in any other hierarchy in the <tt>&quot;LARGE&quot;</tt> <font SIZE="-1">CNFS</font> metacycbuff, all other articles in alt.* in one timehash class, and all other articles in any newsgroups in a second timehash class, except for the internal.* hierarchy which is stored in traditional spool format. </p>
<pre> method tradspool {
 class: 1
 newsgroups: internal.*
 }
 method cnfs {
 class: 2
 newsgroups: alt.binaries.*
 options: BINARIES
 }
 method cnfs {
 class: 3
 newsgroups: *
 size: 50000
 options: LARGE
 }
 method timehash {
 class: 4
 newsgroups: alt.*
 }
 method timehash {
 class: 5
 newsgroups: *
 }</pre>
<p>Notice that the last storage method entry will catch everything. This is a good habit to get into; make sure that you have at least one catch-all entry just in case something you did not expect falls through the cracks. Notice also that the special rule for the internal.* hierarchy is first, so it will catch even articles crossposted to alt.binaries.* or over 50&nbsp;<wbr><font SIZE="-1">KB</font> in size. </p>
<p> As for poison wildmat expressions, if you have for instance an article crossposted between misc.foo and misc.bar, the pattern: </p>
<pre> misc.*,!misc.bar</pre>
<p>will match that article whereas the pattern: </p>
<pre> misc.*,@misc.bar</pre>
<p>will not match that article. An article posted only to misc.bar will fail to match either pattern. </p>
<p> Usually, high-volume groups and groups whose articles do not need to be kept around very long (binaries groups, *.jobs*, news.lists.filters, etc.) are stored in <font SIZE="-1">CNFS</font> buffers. Use the other methods (or <font SIZE="-1">CNFS</font> buffers again) for everything else. However, it is as often as not most convenient to keep in <tt>&quot;tradspool&quot;</tt> special hierarchies like local hierarchies and hierarchies that should never expire or through the spool of which you need to go manually.</p>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Rewritten into <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> storage.conf.pod 8357 2009-02-27 17:56:00Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-cycbuff-conf/">cycbuff.conf</a></i>(5), <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5), <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
