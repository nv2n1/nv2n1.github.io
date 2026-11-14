---
title: "expire(8)"
name: "expire"
section: "8"
letter: "e"
url: "/docs/linux/man/8-expire/"
description: "expire – Usenet article and history expiration program"
---

<p>expire &#8211; Usenet article and history expiration program</p>
<h2>Synopsis</h2>
<p><code>expire</code> [<code>-iNnptx</code>] [<code>-d</code> <i>dir</i>] [<code>-f</code> <i>file</i>] [<code>-g</code> <i>file</i>] [<code>-h</code> <i>file</i>] [<code>-r</code> <i>reason</i>] [<code>-s</code> <i>size</i>] [<code>-v</code> <i>level</i>] [<code>-w</code> <i>number</i>] [<code>-z</code> <i>file</i>] [<i>expire.ctl</i>]</p>
<h2>Description</h2>
<p><code>expire</code> scans the <i><a href="/docs/linux/man/5-history/">history</a></i>(5)-format text file <i>pathdb</i>/history and uses the information recorded in it to purge itself of old news articles. Articles stored using a storage method that has self-expire functionality are by default not affected by <code>expire</code>&#8216;s primary behavior (but see the <code>-N</code> flag to disable this). In this case, <i>expire.ctl</i> is ignored except the <tt>&quot;/remember/&quot;</tt> line for that article; <code>expire</code> does still probe to see if the article still exists and purges the relevant history and overview entries if appropriate. However, if <i>groupbaseexpiry</i> in <i>inn.conf</i> is true, <code>expire</code> acts on all articles as specified by <i>expire.ctl</i> regardless of whether their storage methods have self-expire functionality. </p>
<p> Note that <code>expire</code> never purges articles which do not match any entry in <i>expire.ctl</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> <i>dir</i></p>
<dd>If the <code>-d</code> flag is used, then the new <i>history</i> file and database is created in the specified directory <i>dir</i>. This is useful when the filesystem does not have sufficient space to hold both the old and new history files. When this flag is used, <code>expire</code> leaves the server paused and creates a zero-length file named after the new history file, with an extension of <tt>&quot;.done&quot;</tt> to indicate that it has successfully completed the expiration. The calling script should install the new history file and unpause the server. The <code>-r</code> flag should be used with this flag.</p>
<dt><code>-f</code> <i>file</i></p>
<dd>To specify an alternate history file, use the <code>-f</code> flag. This flag is valid when used with the <code>-d</code> flag, and the output will be written to the specified file. The default without <code>-f</code> is <tt>&quot;history&quot;</tt>.</p>
<dt><code>-g</code> <i>file</i></p>
<dd>If the <code>-g</code> flag is given, then a one-line summary equivalent to the output of <code>-v 1</code>, except preceded by the current time, will be appended to the specified <i>file</i>.</p>
<dt><code>-h</code> <i>file</i></p>
<dd>To specify an alternate input text history file, use the <code>-h</code> flag. <code>expire</code> uses the old <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3) database to determine the size of the new one. (If the <code>-d</code> flag is not used, the output filename will be the same as the input filename with an extension of <tt>&quot;.n&quot;</tt>.) </p>
<p> The default without the <code>-h</code> flag is <i>pathdb</i>/history.</p>
<dt><code>-i</code></p>
<dd>To ignore the old database, use the <code>-i</code> flag.</p>
<dt><code>-N</code></p>
<dd>The control file is normally ignored for articles in storage methods which have self-expire functionality. If the <code>-N</code> flag is used, <code>expire</code> still uses the control file for these articles.</p>
<dt><code>-n</code></p>
<dd>If <code>innd</code> is not running, use the <code>-n</code> flag and <code>expire</code> will not send the <tt>&quot;pause&quot;</tt> or <tt>&quot;go&quot;</tt> commands. (For more details on the commands, see <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8)). Note that <code>expire</code> only needs exclusive access for a very short time &#8212; long enough to see if any new articles arrived since it first hit the end of the file, and to rename the new files to the working files.</p>
<dt><code>-p</code></p>
<dd><code>expire</code> makes its decisions on the time the article arrived, as found in the <i>history</i> file. This means articles are often kept a little longer than with other expiration programs that base their decisions on the article&#8217;s posting date. To use the article&#8217;s posting date, use the <code>-p</code> flag.</p>
<dt><code>-r</code> <i>reason</i></p>
<dd><code>expire</code> normally sends a <tt>&quot;pause&quot;</tt> command to the local <code>innd</code> daemon when it needs exclusive access to the <i>history</i> file, using the string <tt>&quot;Expiring&quot;</tt> as the reason. To give a different reason, use the <code>-r</code> flag. The process <font SIZE="-1">ID</font> will be appended to the reason. When <code>expire</code> is finished and the new <i>history</i> file is ready, it sends a <tt>&quot;go&quot;</tt> command. See also the <code>-n</code> flag.</p>
<dt><code>-s</code> <i>size</i></p>
<dd>Optimize the new history database for approximately <i>size</i> pairs (lines in <i>history</i>). Accurately specifying the size will create a more efficient database. (The size should be the estimated eventual size of the file, typically the size of the old file.)</p>
<dt><code>-t</code></p>
<dd>If the <code>-t</code> flag is used, then <code>expire</code> will generate a list of the tokens that should be removed on its standard output, and the new <i>history</i> file will be left in <i>history.n</i>, <i>history.n.dir</i>, <i>history.n.index</i> and <i>history.n.hash</i>. This flag is useful for debugging when used with the <code>-n</code> flag. Note that if the <code>-f</code> flag is used, then the name specified with that flag will be used instead of <i>history</i>.</p>
<dt><code>-v</code> <i>level</i></p>
<dd>The <code>-v</code> flag is used to increase the verbosity of the program, generating messages to standard output. The <i>level</i> should be a number, where higher numbers result in more output. Level one will print totals of the various actions done (not valid if a new <i>history</i> file is not written), level two will print a report on each individual file, while level five results in multiple lines of output for every history line processed.</p>
<dt><code>-w</code> <i>number</i></p>
<dd>Use the <code>-w</code> flag to &#8220;warp&#8221; time so that <code>expire</code> thinks it is running at some time other then the current time. The value should be a signed floating point number indicating the number of days to use as the offset.</p>
<dt><code>-x</code></p>
<dd>If the <code>-x</code> flag is used, then <code>expire</code> will not create any new history files. This is most useful when combined with the <code>-n</code> and <code>-t</code> flags to see how different expiration policies would change the amount of disk space used.</p>
<dt><code>-z</code> <i>file</i></p>
<dd>If the <code>-z</code> flag is used, then articles are not removed, but their names are appended to the specified <i>file</i>. See the description of <code>delayrm</code> in <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8). If a filename is specified, it is taken as the control file and parsed according to the rules in <i>expire.ctl</i>. A single dash (<tt>&quot;-&quot;</tt>) may be used to read the file from standard input. If no file is specified, the file <i>pathetc</i>/expire.ctl is read.</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> expire.pod 8577 2009-08-18 14:02:02Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3), <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/3-inndcomm/">inndcomm</a></i>(3), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8). </p>
