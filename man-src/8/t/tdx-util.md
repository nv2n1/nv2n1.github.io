---
title: "tdx-util(8)"
name: "tdx-util"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tdx-util/"
description: "tdx-util – Tradindexed overview manipulation utility"
---

<p>tdx-util &#8211; Tradindexed overview manipulation utility</p>
<h2>Synopsis</h2>
<p><code>tdx-util</code> [<code>-AFcgiOo</code>] [<code>-a</code> <i>article</i>] [<code>-f</code> <i>status</i>] [<code>-n</code> <i>newsgroup</i>] [<code>-p</code> <i>path</i>] [<code>-R</code> <i>path</i>]</p>
<h2>Description</h2>
<p><code>tdx-util</code> is an administrative interface to the tradindexed overview method for <font SIZE="-1">INN</font>. It only works on tradindexed overview databases, not on any other type of <font SIZE="-1">INN</font> overview. It allows the administrator to dump various information about the internal state of the overview, audit it for errors, and rebuild portions of the overview database. </p>
<p> The tradindexed overview method should lock properly and therefore it should be safe to run this utility and perform any operation it performs, including full repairs or per-group overview rebuilds, while the server is running. However, note that some of the operations performed by this utility can take an extended period of time and will hold locks in the overview database during that period, which depending on what the server is doing may cause the server to stall until <code>tdx-util</code> completes its operation. </p>
<p> The dump operations are <code>-i</code>, which dumps the master index for the overview database, <code>-g</code>, which dumps the index for an individual group, and <code>-o</code> and <code>-O</code>, which dump the overview information for a particular group (including the additional metadata stored in the index) in two different formats. For <code>-g</code>, <code>-o</code>, and <code>-O</code>, the <code>-n</code> option must also be given to specify a newsgroup to operate on. </p>
<p> To add a new newsgroup to the overview database, use <code>-c</code>. A group must be specified with <code>-n</code>. If the group status is something other than <tt>&quot;y&quot;</tt>, it should be specified with <code>-f</code>, and the low and high article numbers may be specified with <code>-a</code>. If only one number is given rather than a range, it will be taken to be the high water mark and the low mark will be set to 1. </p>
<p> To audit the entire overview database for problems, use <code>-A</code>. Any problems found will be reported to standard error. Use <code>-F</code> to correct the errors found. </p>
<p> To rebuild the database for a particular newsgroup, use <code>-R</code>. The <code>-R</code> option takes a path to a directory which contains all of the articles for that newsgroup, one per file. The names of the files must be the numbers of the articles in that group. (In other words, this directory must be a traditional spool directory for that group.) The <code>-n</code> option must also be given to specify the newsgroup for which the overview is being rebuilt. </p>
<p> For all operations performed by <code>tdx-util</code>, a different overview database than the one specified in <i>inn.conf</i> may be specified using the <code>-p</code> option.</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Audit the entire overview database for problems. This runs the internal consistency checks built into the tradindexed overview implementation, checking such things as the validity and reachability of all group index entries, the format of the individual overview entries, the correspondence of index entries to overview data, and similar such things. No changes will be made to the database, but problems will be reported to standard error.</p>
<dt><code>-a</code> <i>article</i></p>
<dd>The article number or numbers to act on. <i>article</i> is a valid <font SIZE="-1">NNTP</font> range, meaning that it can be either a single article number or a range of article numbers (like <tt>&quot;1-5&quot;</tt>). Either the start or the end (or both) of the range may be omitted, in which case they will be set to the first or last article number in the group. Passing <tt>&quot;-&quot;</tt> for <i>article</i> is therefore equivalent to not using the <code>-a</code> option at all. </p>
<p> Only useful in combination with the <code>-o</code> option to dump overview information or with <code>-c</code> to specify the low and high article numbers when creating a group.</p>
<dt><code>-c</code></p>
<dd>Create a new group in the overview database. The group must be specified with <code>-n</code>. The newsgroup status defaults to <tt>&quot;y&quot;</tt> but may be set with <code>-f</code>. The low and high article numbers default to 1 and 0 respectively, but may be set with <code>-a</code>. If only one number is given to <code>-a</code>, it is taken as the high article number.</p>
<dt><code>-F</code></p>
<dd>Audit the entire overview database for problems, fixing them as they&#8217;re detected where possible. This runs the internal consistency checks built into the tradindexed overview implementation, checking such things as the validity and reachability of all group index entries, the format of the individual overview entries, the correspondence of index entries to overview data, and similar such things. The strategy used when fixing problems is to throw away data that&#8217;s unrecoverable, so be warned that using this option may result in inaccessible articles if their overview data has been corrupted. </p>
<p> To see what would be changed by <code>-F</code>, run <code>tdx-util</code> with <code>-A</code> first.</p>
<dt><code>-f</code> <i>status</i></p>
<dd>When creating a newsgroup with <code>-c</code>, set the status of the newly created group to <i>status</i> instead of <tt>&quot;y&quot;</tt>. Only useful with <code>-c</code>.</p>
<dt><code>-g</code></p>
<dd>Dump the index of a particular group. The fields are, in order, the article number, the offset of the data for that article in the overview data file for that group, the length of the overview data, the time (in seconds since epoch) when the article arrived on the server, the time (in seconds since epoch) when the article should expire based on its Expires: header (or 0 if there is no Expires: header), and the storage <font SIZE="-1">API</font> token of the article. </p>
<p> If this option is given, the <code>-n</code> option must also be given to specify the newsgroup on which to act.</p>
<dt><code>-i</code></p>
<dd>Dump the master index of the overview database. This contains similar information to the server <i>active</i> file, such as high and low water marks and moderation status, and is the information that <code>nnrpd</code> hands out to clients. </p>
<p> The fields are, in order, the newsgroup name, the high water mark, the low water mark, the base article number (the point at which the group index begins), the count of articles in the group, the group status, the time (in seconds since epoch) when that newsgroup was deleted or 0 if it hasn&#8217;t been, and the inode of the index file for that group. </p>
<p> A particular newsgroup can be specified with the <code>-n</code> option. If <code>-n</code> is not given, the entire master index will be dumped.</p>
<dt><code>-n</code> <i>newsgroup</i></p>
<dd>Specify the newsgroup on which to act, required for the <code>-i</code>, <code>-o</code>, and <code>-R</code> options.</p>
<dt><code>-O</code></p>
<dd>Dump the overview information for a newsgroup in the format used by <code>overchan</code> as input. Each line will start with the storage <font SIZE="-1">API</font> token, the arrival timestamp in seconds since epoch, the expires timestamp in the same format (or 0 if there is no Expires: header), and then the overview data. </p>
<p> If this option is given, the <code>-n</code> option must also be given to specify the newsgroup on which to act. By default, all of the overview information for that newsgroup is dumped, but the <code>-a</code> option may be given to restrict the dump to the information for a single article.</p>
<dt><code>-o</code></p>
<dd>Dump the overview information for a newsgroup, in the same format as it would be returned to clients but with one modification. Appended to the end of each entry will be four additional pieces of data: the article number according to the index file for that group labelled with <tt>&quot;Article:&quot;</tt>, the storage <font SIZE="-1">API</font> token for that article labelled with <tt>&quot;Token:&quot;</tt>, the arrival date for that article on the server in <font SIZE="-1">RFC</font>&nbsp;<wbr>5322 date format labelled with <tt>&quot;Arrived:&quot;</tt>, and the expiration date for that article (from the Expires: header) in <font SIZE="-1">RFC</font>&nbsp;<wbr>5322 date format if there is any, labelled with <tt>&quot;Expires:&quot;</tt>. </p>
<p> If this option is given, the <code>-n</code> option must also be given to specify the newsgroup on which to act. By default, all of the overview information for that newsgroup is dumped, but the <code>-a</code> option may be given to restrict the dump to the information for a single article.</p>
<dt><code>-p</code> <i>path</i></p>
<dd>Act on the overview database rooted in <i>path</i>, overriding the overview path specified in <i>inn.conf</i>.</p>
<dt><code>-R</code> <i>path</i></p>
<dd>Rebuild the overview for a given group from the articles stored in <i>path</i>. The articles must be in the form of a traditional spool directory; in other words, each article must be in a separate file and the name of the file must match the article number of the article. </p>
<p> If this option is given, the <code>-n</code> option must also be given to specify the newsgroup on which to act.</dl>
<h2>Examples</h2>
<p>Dump the master index for the overview database in <i>/news/overview</i>, regardless of the overview path specified in <i>inn.conf</i>: </p>
<pre> tdx-util -i -p /news/overview</pre>
<p>Dump the group index for example.test: </p>
<pre> tdx-util -g -n example.test</pre>
<p>Dump the complete overview information for example.test: </p>
<pre> tdx-util -o -n example.test</pre>
<p>Dump the overview information for articles 45 and higher in example.test: </p>
<pre> tdx-util -o -n example.test -a 45-</pre>
<p>Create an entry for example.test with mode m and low and high article numbers of 4 and 23, respectively. </p>
<pre> tdx-util -c -n example.test -f m -a 4-23</pre>
<p>Audit the entire overview database for any problems: </p>
<pre> tdx-util -A</pre>
<p>Rebuild the overview information for example.test from a traditional spool directory: </p>
<pre> tdx-util -R &lt;patharticles in inn.conf&gt;/example/test -n example.test</pre>
<p>The last command may be useful for recovering from a bad crash or corrupted overview information for a particular group, if you are also using the tradspool article storage method.</p>
<h2>History</h2>
<p>Written by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> tdx-util.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
