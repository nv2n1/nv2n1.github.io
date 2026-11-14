---
title: "makehistory(8)"
name: "makehistory"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makehistory/"
description: "makehistory – Initialize or rebuild INN history database"
---

<p>makehistory &#8211; Initialize or rebuild INN history database</p>
<h2>Synopsis</h2>
<p><code>makehistory</code> [<code>-abFIOSx</code>] [<code>-f</code> <i>filename</i>] [<code>-l</code> <i>count</i>] [<code>-L</code> <i>load-average</i>] [<code>-s</code> <i>size</i>] [<code>-T</code> <i>tmpdir</i>]</p>
<h2>Description</h2>
<p><code>makehistory</code> rebuilds the <i><a href="/docs/linux/man/5-history/">history</a></i>(5) text file, which contains a list of message-IDs of articles already seen by the server. It can also be used to rebuild the overview database. Note that even though the <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3) indices for the <i>history</i> file are also rebuilt by <code>makehistory</code>, it is useful to run <i><a href="/docs/linux/man/8-makedbz/">makedbz</a></i>(8) after <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8) in order to improve the efficiency of the indices (<code>makehistory</code> does not know how large to make the hash table at first run, unless the size is given by the <code>-s</code> flag). </p>
<p> The default location of the <i>history</i> text file is <i>pathdb</i>/history; to specify an alternate location, use the <code>-f</code> flag. </p>
<p> By default, <code>makehistory</code> will scan the entire spool, using the storage manager, and write a history line for every article. To also generate overview information, use the <code>-O</code> flag. </p>
<p> <font SIZE="-1">WARNING:</font> If you&#8217;re trying to rebuild the overview database, be sure to stop <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) and delete or zero out the existing database before you start for the best results. An overview rebuild should not be done while the server is running. Unless the existing overview is deleted, you may end up with problems like out-of-order overview entries, excessively large overview buffers, and the like. </p>
<p> If <i>ovmethod</i> in <i>inn.conf</i> is <tt>&quot;ovdb&quot;</tt>, you must have the ovdb processes running while rebuilding overview. ovdb needs them available while writing overview entries. You can start them by hand separate from the rest of the server by running <code>ovdb_init</code>; see <i><a href="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8) for more details.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Append to the <i>history</i> file rather than generating a new one. If you append to the main <i>history</i> file, make sure <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) is throttled or not running, or you can corrupt the history.</p>
<dt><code>-b</code></p>
<dd>Delete any messages found in the spool that do not have valid Message-ID: headers in them.</p>
<dt><code>-F</code></p>
<dd>Fork a separate process to flush overview data to disk rather than doing it directly. The advantage of this is that it allows <code>makehistory</code> to continue to collect more data from the spool while the first batch of data is being written to the overview database. The disadvantage is that up to twice as much temporary disk space will be used for the generated overview data. This option only makes sense in combination with <code>-O</code>. With buffindexed, the <code>overchan</code> program is invoked to write overview.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd>Rather than writing directly to <i>pathdb</i>/history, instead write to <i>filename</i>, also in <i>pathdb</i>.</p>
<dt><code>-I</code></p>
<dd>Don&#8217;t store overview data for articles numbered lower than the lowest article number in <i>active</i>. This is useful if there are for whatever reason old articles on disk that shouldn&#8217;t be available to readers or put into the overview database.</p>
<dt><code>-l</code> <i>count</i></p>
<dd>This option specifies how many articles to process before writing the accumulated overview information out to the overview database. The default is <tt>10000</tt>. Since overview write performance is faster with sorted data, each &#8220;batch&#8221; gets sorted. Increasing the batch size with this option may further improve write performance, at the cost of longer sort times. Also, temporary space will be needed to store the overview batches. At a rough estimate, about 300 * <i>count</i> bytes of temporary space will be required (not counting temp files created by <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1)). See the description of the <code>-T</code> option for how to specify the temporary storage location. This option has no effect with buffindexed, because buffindexed does not need sorted overview and no batching is done.</p>
<dt><code>-L</code> <i>load-average</i></p>
<dd>Temporarily pause activities if the system load average exceeds the specified level <i>load-average</i>. This allows <code>makehistory</code> to run on a system being used for other purposes without monopolizing system resources and thus making the response time for other applications unacceptably slow. Using <i><a href="/docs/linux/man/1-nice/">nice</a></i>(1) does not help much for that because the problem comes from disk I/O usage, and <i><a href="/docs/linux/man/1-ionice/">ionice</a></i>(1) is not always available or efficient.</p>
<dt><code>-O</code></p>
<dd>Create the overview database as well as the <i>history</i> file. Overview information is only required if the server supports readers; it is not needed for a transit-only server (see <i>enableoverview</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5)). If you are using the buffindexed overview storage method, erase all of your overview buffers before running <code>makehistory</code> with <code>-O</code>.</p>
<dt><code>-S</code></p>
<dd>Rather than storing the overview data into the overview database, just write it to standard output in a form suitable for feeding to <code>overchan</code> later if wished. When this option is used, <code>-F</code>, <code>-I</code>, <code>-l</code>, and <code>-T</code> are ignored. This option only makes sense in combination with <code>-O</code>.</p>
<dt><code>-s</code> <i>size</i></p>
<dd>Size the history database for approximately <i>size</i> pairs. Accurately specifying the size is an optimization that will create a more efficient database. (The size should be the estimated eventual size of the <i>history</i> file, typically the size of the old file, in lines.)</p>
<dt><code>-T</code> <i>tmpdir</i></p>
<dd>If <code>-O</code> is given, <code>makehistory</code> needs a location to write temporary overview data. By default, it uses <i>pathtmp</i>, set in <i>inn.conf</i>, but if this option is given, the provided <i>tmpdir</i> is used instead. This is also used for temporary files created by <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) (which is invoked in the process of writing overview information since sorted overview information writes faster). By default, <code>sort</code> usually uses your system temporary directory; see the <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) man page on your system to be sure.</p>
<dt><code>-x</code></p>
<dd>If this option is given, <code>makehistory</code> won&#8217;t write out <i>history</i> file entries. This is useful mostly for building overview without generating a new <i>history</i> file.</dl>
<h2>Examples</h2>
<p>Here&#8217;s a typical example of rebuilding the entire history and overview database, removing broken articles in the news spool. This uses the default temporary file locations and should be done while <code>innd</code> isn&#8217;t running (or is throttled). </p>
<pre> makehistory -b -f history.n -O -l 30000 -I</pre>
<p>This will rebuild the overview (if using buffindexed, erase the existing overview buffers before running this command) and leave a new <i>history</i> file as <tt>&quot;history.n&quot;</tt> in <i>pathdb</i>. To preserve all of the history entries from the old <i>history</i> file that correspond to rejected articles or expired articles, follow the above command with: </p>
<pre> cd &lt;pathdb&gt;
 awk 'NF == 2 { print }' &lt; history &gt;&gt; history.n</pre>
<p>(replacing the path with your <i>pathdb</i>, if it isn&#8217;t the default). Then look over the new <i>history</i> file for problems and run: </p>
<pre> makedbz -s `wc -l &lt; history.n` -f history.n</pre>
<p>Then rename all of the files matching <tt>&quot;history.n.*&quot;</tt> to <tt>&quot;history.*&quot;</tt>, replacing the current history database and indices. After that, it&#8217;s safe to unthrottle <code>innd</code>. </p>
<p> For a simpler example: </p>
<pre> makehistory -b -f history.n -I -O</pre>
<p>will scan the spool, removing broken articles and generating history and overview entries for articles missing from history. </p>
<p> To just rebuild overview: </p>
<pre> makehistory -O -x -F</pre>
<h2>Files</h2>
<dl>
<dt><i>pathdb</i>/history</p>
<dd>This is the default output file for <code>makehistory</code>.</p>
<dt><i>pathtmp</i></p>
<dd>Where temporary files are written unless <code>-T</code> is given.</dl>
<h2>History</h2>
<p>Originally written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews and updated by various other people since. </p>
<p> <tt>$Id:</tt> makehistory.pod 8535 2009-06-23 18:09:56Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-makedbz/">makedbz</a></i>(8), <i><a href="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8), <i><a href="/docs/linux/man/8-overchan/">overchan</a></i>(8). </p>
