---
title: "slrnpull(1)"
name: "slrnpull"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slrnpull/"
description: "slrnpull – Pull a small newsfeed for offline reading."
---

<h2 class="name">NAME</h2>
<p> slrnpull &#8211; Pull a small newsfeed for offline reading. </p>
<h2>SYNOPSIS</h2>
<p> <code>slrnpull</code> [-d&nbsp;<wbr><i>spooldir</i>] [-h&nbsp;<wbr><i>server</i>] [&#8211;debug&nbsp;<wbr><i>file</i>] [&#8211;expire] [&#8211;fetch-score <i>n</i>] [&#8211;help] [&#8211;kill-log&nbsp;<wbr><i>file</i>] [&#8211;kill-score <i>n</i>] [&#8211;logfile&nbsp;<wbr><i>file</i>] [&#8211;marked-bodies] [&#8211;new-groups] [&#8211;no-post] [&#8211;post] [&#8211;post-only] [&#8211;rebuild] [&#8211;version] </p>
<h2>DESCRIPTION</h2>
<p> <i>slrnpull</i> pulls a small newsfeed from an NNTP server. It puts the articles into a spool directory from which <i>slrn</i> can later read them, even if the server is unreachable at that time. Typically, this is useful if you do not have a permanent network connection.</p>
<h2>OPTIONS</h2>
<p> The following options can be used when calling <i>slrnpull</i> from the command line.</p>
<dl>
<dt>-d <i>spooldir</i></p>
<dd> Set slrnpull&#8217;s root directory for this run to <i>spooldir</i>, overriding the <i>$SLRNPULL_ROOT</i> environment variable.</p>
<dt>-h <i>host[:port]</i></p>
<dd> Connect to the NNTP server on <i>host</i>, overriding the <i>$NNTPSERVER</i> environment variable. If no <i>port</i> is given, the default NNTP port (119) will be used.</p>
<dt>&#8211;debug <i>file</i></p>
<dd> Write dialogue with the server and some additional debugging output to <i>file</i>.</p>
<dt>&#8211;expire</p>
<dd> Expire (remove) old messages from the spool, but do not fetch news.</p>
<dt>&#8211;fetch-score <i>n</i></p>
<dd> Fetch article bodies with a score of at least <i>n</i> automatically (in true offline mode, the default is to fetch only bodies that were explicitly marked by the user).</p>
<dt>&#8211;help</p>
<dd> Show help for command line switches.</p>
<dt>&#8211;kill-log <i>file</i></p>
<dd> Keep a log of all articles that were killed by the scorefile in <i>file</i>. By default, no such logfile is created.</p>
<dt>&#8211;kill-score <i>n</i></p>
<dd> Kill all articles with a score below <i>n</i>. The default value for this is 0.</p>
<dt>&#8211;logfile <i>file</i></p>
<dd> Log the messages and errors that slrnpull prints to the screen to <i>file</i>. By default, they get written to the file log in slrnpull&#8217;s root directory.</p>
<dt>&#8211;marked-bodies</p>
<dd> Only fetch bodies that were marked for download within slrn.</p>
<dt>&#8211;new-groups</p>
<dd> Check for new groups, appending them to the file new.groups in the data directory.</p>
<dt>&#8211;no-post</p>
<dd> Do not post any articles to the server.</p>
<dt>&#8211;post</p>
<dd> Obsolete version of <i>&#8211;post-only</i>.</p>
<dt>&#8211;post-only</p>
<dd> Post outgoing articles, but do not fetch news.</p>
<dt>&#8211;rebuild</p>
<dd> Like &#8211;expire, but also rebuild the overview information. To be used when the overview information is damaged.</p>
<dt>&#8211;version</p>
<dd> Print the version number. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> <i>slrnpull</i> reads the following environment variables. Note that they can be overridden by command line switches.</p>
<dl>
<dt><code>NNTPSERVER</code></p>
<dd> You can use this variable to tell <i>slrnpull</i> which NNTP server to connect to. It can be overridden by the command line option -h.</p>
<dt><code>SLRNPULL_ROOT</code></p>
<dd> Defines the directory where <i>slrnpull</i> will look for its configuration files and spool the articles. An absolute filename is needed here. This can be overriden by the option -d.</dl>
<h2>FILES</h2>
<dl>
<dt>$SLRNPULL_ROOT/authinfo</p>
<dd> If the server requires authentication, this file needs to contain the data (username in the first line, password in the second). Be careful not to make this file world-readable!</p>
<dt>$SLRNPULL_ROOT/log</p>
<dd> The default file to log status and error messages to.</p>
<dt>$SLRNPULL_ROOT/score</p>
<dd> If you want <i>slrnpull</i> to apply scoring rules to decide which articles to download, put them into this file.</p>
<dt>$SLRNPULL_ROOT/slrnpull.conf</p>
<dd> The main configuration file. It tells <i>slrnpull</i> how many articles to get from which groups and when to expire them. </p>
</dl>
<h2>SEE ALSO</h2>
<p> The documentation that comes with <i>slrnpull</i>, especially README and SETUP. The FAQ of slrn also answers some questions about slrnpull. </p>
<p> You might also want to look at slrn&#8217;s official home page, <i><a rel="nofollow" href="http://slrn.sourceforge.net/">http://slrn.sourceforge.net/</a></i> or post to <i>news.software.readers</i> if you have a question not covered by existing documentation. </p>
<p> The latest version of <i>slrnpull</i> is part of the slrn package available from <i><a rel="nofollow" href="http://prdownloads.sourceforge.net/slrn/">http://prdownloads.sourceforge.net/slrn/</a></i></p>
<h2>AUTHOR</h2>
<p> John E. Davis &lt;davis [at] space.mit.edu&gt; </p>
<p> Please send any bug reports to the current maintainer, Thomas Schultz &lt;tststs [at] gmx.de&gt; </p>
<h2>Index</h2>
