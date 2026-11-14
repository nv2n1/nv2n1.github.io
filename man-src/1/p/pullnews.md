---
title: "pullnews(1)"
name: "pullnews"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pullnews/"
description: "pullnews – Pull news from multiple news servers and feed it to another"
---

<h2 class="name">NAME</h2>
<p> pullnews &#8211; Pull news from multiple news servers and feed it to another </p>
<h2>SYNOPSIS</h2>
<p> <code>pullnews</code> [<code>-BhnOqRx</code>] [<code>-a</code> <i>hashfeed</i>] [<code>-b</code> <i>fraction</i>] [<code>-c</code> <i>config</i>] [<code>-C</code> <i>width</i>] [<code>-d</code> <i>level</i>] [<code>-f</code> <i>fraction</i>] [<code>-F</code> <i>fakehop</i>] [<code>-g</code> <i>groups</i>] [<code>-G</code> <i>newsgroups</i>] [<code>-H</code> <i>headers</i>] [<code>-k</code> <i>checkpt</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>header_pats</i>] [<code>-M</code> <i>num</i>] [<code>-N</code> <i>timeout</i>] [<code>-p</code> <i>port</i>] [<code>-P</code> <i>hop_limit</i>] [<code>-Q</code> <i>level</i>] [<code>-r</code> <i>file</i>] [<code>-s</code> <i>to-server</i>[:<i>port</i>]] [<code>-S</code> <i>max-run</i>] [<code>-t</code> <i>retries</i>] [<code>-T</code> <i>connect-pause</i>] [<code>-w</code> <i>num</i>] [<code>-z</code> <i>article-pause</i>] [<code>-Z</code> <i>group-pause</i>] [<i>from-server</i> &#8230;]</p>
<h2>REQUIREMENTS</h2>
<p> The <tt>&quot;Net::NNTP&quot;</tt> module must be installed. This module is available as part of the libnet distribution and comes with recent versions of Perl. For older versions of Perl, you can download it from &lt;<a rel="nofollow" href="http://www.cpan.org/">http://www.cpan.org/</a>&gt;.</p>
<h2>DESCRIPTION</h2>
<p> <code>pullnews</code> reads a config file in the running user&#8217;s home directory (normally called <i>~/.pullnews</i>) and connects to the upstream servers given there as a reader client. By default, it connects to all servers listed in the configuration file, but you can limit <code>pullnews</code> to specific servers by listing them on the command line: a whitespace-separated list of server names can be specified, like <i>from-server</i> for one of them. For each server it connects to, it pulls over articles and feeds them to the destination server via the <font SIZE="-1">IHAVE</font> or <font SIZE="-1">POST</font> commands. This means that the system <code>pullnews</code> is run on must have feeding access to the destination news server. </p>
<p> <code>pullnews</code> is designed for very small sites that do not want to bother setting up traditional peering and is not meant for handling large feeds.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>hashfeed</i></p>
<dd> This option is a deterministic way to control the flow of articles and to split a feed. The <i>hashfeed</i> parameter must be in the form <tt>&quot;value/mod&quot;</tt> or <tt>&quot;start-end/mod&quot;</tt>. The Message-ID of each article is hashed using <font SIZE="-1">MD5</font>, which results in a 128-bit hash. The lowest 32 bits are then taken by default as the hashfeed value (which is an integer). If the hashfeed value modulus <tt>&quot;mod&quot;</tt> plus one equals <tt>&quot;value&quot;</tt> or is between <tt>&quot;start&quot;</tt> and <tt>&quot;end&quot;</tt>, <code>pullnews</code> will feed the article. All these numbers must be integers. </p>
<p> For instance: </p>
<pre>
    pullnews -a 1/2      Feeds about 50% of all articles.
    pullnews -a 2/2      Feeds the other 50% of all articles.
</pre>
<p> Another example: </p>
<pre>
    pullnews -a 1-3/10   Feeds about 30% of all articles.
    pullnews -a 4-5/10   Feeds about 20% of all articles.
    pullnews -a 6-10/10  Feeds about 50% of all articles.
</pre>
<p> You can use an extended syntax of the form <tt>&quot;value/mod:offset&quot;</tt> or <tt>&quot;start-end/mod:offset&quot;</tt> (using an underscore <tt>&quot;_&quot;</tt> instead of a colon <tt>&quot;:&quot;</tt> is also recognized). As <font SIZE="-1">MD5</font> generates a 128-bit return value, it is possible to specify from which byte-offset the 32-bit integer used by hashfeed starts. The default value for <tt>&quot;offset&quot;</tt> is <tt>&quot;:0&quot;</tt> and thirteen overlapping values from <tt>&quot;:0&quot;</tt> to <tt>&quot;:12&quot;</tt> can be used. Only up to four totally independent values exist: <tt>&quot;:0&quot;</tt>, <tt>&quot;:4&quot;</tt>, <tt>&quot;:8&quot;</tt> and <tt>&quot;:12&quot;</tt>. </p>
<p> Therefore, it allows to a generate a second level of deterministic distribution. Indeed, if <code>pullnews</code> feeds <tt>&quot;1/2&quot;</tt>, it can go on splitting thanks to <tt>&quot;1-3/9:4&quot;</tt> for instance. Up to four levels of deterministic distribution can be used. </p>
<p> The algorithm is compatible with the one used by Diablo 5.1 and up.</p>
<dt><code>-b</code> <i>fraction</i></p>
<dd> Backtrack on server numbering reset. Specify the proportion (<tt>0.0</tt> to <tt>1.0</tt>) of a group&#8217;s articles to pull when the server&#8217;s article number is less than our high for that group. When <i>fraction</i> is <tt>1.0</tt>, pull all the articles on a renumbered server. The default is to do nothing.</p>
<dt><code>-B</code></p>
<dd> Feed is header-only, that is to say <code>pullnews</code> only feeds the headers of the articles, plus one blank line. It adds the Bytes: header field if the article does not already have one, and keeps the body only if the article is a control article.</p>
<dt><code>-c</code> <i>config</i></p>
<dd> Normally, the config file is stored in <i>~/.pullnews</i> for the user running <code>pullnews</code>. If <code>-c</code> is given, <i>config</i> will be used as the config file instead. This is useful if you&#8217;re running <code>pullnews</code> as a system user on an automated basis out of cron rather than as an individual user. </p>
<p> See &#8220;<font SIZE="-1">CONFIG</font> <font SIZE="-1">FILE</font>&#8221; below for the format of this file.</p>
<dt><code>-C</code> <i>width</i></p>
<dd> Use <i>width</i> characters per line for the progress table. The default value is <tt>50</tt>.</p>
<dt><code>-d</code> <i>level</i></p>
<dd> Set the debugging level to the integer <i>level</i>; more debugging output will be logged as this increases. The default value is <tt>0</tt>.</p>
<dt><code>-f</code> <i>fraction</i></p>
<dd> This changes the proportion of articles to get from each group to <i>fraction</i> and should be in the range <tt>0.0</tt> to <tt>1.0</tt> (<tt>1.0</tt> being the default).</p>
<dt><code>-F</code> <i>fakehop</i></p>
<dd> Prepend <i>fakehop</i> as a host to the Path: header of articles fed.</p>
<dt><code>-g</code> <i>groups</i></p>
<dd> Specify a collection of groups to get. <i>groups</i> is a list of newsgroups separated by commas (only commas, no spaces). Each group must be defined in the config file, and only the remote hosts that carry those groups will be contacted. Note that this is a simple list of groups, not a wildmat expression, and wildcards are not supported.</p>
<dt><code>-G</code> <i>newsgroups</i></p>
<dd> Add the comma-separated list of groups <i>newsgroups</i> to each server in the configuration file (see also <code>-g</code> and <code>-w</code>).</p>
<dt><code>-h</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>-H</code> <i>headers</i></p>
<dd> Remove these named headers (colon-separated list) from fed articles.</p>
<dt><code>-k</code> <i>checkpt</i></p>
<dd> Checkpoint (save) the config file every <i>checkpt</i> articles (default is <tt>0</tt>, that is to say at the end of the session).</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd> Log progress/stats to <i>logfile</i> (default is <tt>&quot;stdout&quot;</tt>).</p>
<dt><code>-m</code> <i>header_pats</i></p>
<dd> Feed an article based on header matching. The argument is a number of whitespace-separated tuples (each tuple being a colon-separated header and regular expression). For instance: </p>
<pre>
    -m &quot;Hdr1:regexp1 !Hdr2:regexp2 #Hdr3:regexp3 !#Hdr4:regexp4&quot;
</pre>
<p> specifies that the article will be passed only if the <tt>&quot;Hdr1:&quot;</tt> header matches <tt>&quot;regexp1&quot;</tt> and the <tt>&quot;Hdr2:&quot;</tt> header does not match <tt>&quot;regexp2&quot;</tt>. Besides, if the <tt>&quot;Hdr3:&quot;</tt> header matches <tt>&quot;regexp3&quot;</tt>, that header is removed; and if the <tt>&quot;Hdr4:&quot;</tt> header does not match <tt>&quot;regexp4&quot;</tt>, that header is removed.</p>
<dt><code>-M</code> <i>num</i></p>
<dd> Specify the maximum number of articles (per group) to process. The default is to process all new articles. See also <code>-f</code>.</p>
<dt><code>-n</code></p>
<dd> Do nothing but read articles &#8212; does not feed articles downstream, writes no <code>rnews</code> file, does not update the config file.</p>
<dt><code>-N</code> <i>timeout</i></p>
<dd> Specify the timeout length, as <i>timeout</i> seconds, when establishing an <font SIZE="-1">NNTP</font> connection.</p>
<dt><code>-O</code></p>
<dd> Use an optimized mode: <code>pullnews</code> checks whether the article already exists on the downstream server, before downloading it. It may help for huge articles or a slow link to upstream hosts.</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Connect to the destination news server on a port other than the default of <tt>119</tt>. This option does not change the port used to connect to the source news servers.</p>
<dt><code>-P</code> <i>hop_limit</i></p>
<dd> Restrict feeding an article based on the number of hops it has already made. Count the hops in the Path: header (<i>hop_count</i>), feeding the article only when <i>hop_limit</i> is <tt>&quot;+num&quot;</tt> and <i>hop_count</i> is more than <i>num</i>; or <i>hop_limit</i> is <tt>&quot;-num&quot;</tt> and <i>hop_count</i> is less than <i>num</i>.</p>
<dt><code>-q</code></p>
<dd> Print out less status information while running.</p>
<dt><code>-Q</code> <i>level</i></p>
<dd> Set the quietness level (<tt>&quot;-Q 2&quot;</tt> is equivalent to <tt>&quot;-q&quot;</tt>). The higher this value, the less gets logged. The default is <tt>0</tt>.</p>
<dt><code>-r</code> <i>file</i></p>
<dd> Rather than feeding the downloaded articles to a destination server, instead create a batch file that can later be fed to a server using <code>rnews</code>. See <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1) for more information about the batch file format.</p>
<dt><code>-R</code></p>
<dd> Be a reader (use <font SIZE="-1">MODE</font> <font SIZE="-1">READER</font> and <font SIZE="-1">POST</font> commands) to the downstream server. The default is to use the <font SIZE="-1">IHAVE</font> command.</p>
<dt><code>-s</code> <i>to-server</i>[:<i>port</i>]</p>
<dd> Normally, <code>pullnews</code> will feed the articles it retrieves to the news server running on localhost. To connect to a different host, specify a server with the <code>-s</code> flag. You can also specify the port with this same flag or use <code>-p</code>.</p>
<dt><code>-S</code> <i>max-run</i></p>
<dd> Specify the maximum time <i>max-run</i> in seconds for <code>pullnews</code> to run.</p>
<dt><code>-t</code> <i>retries</i></p>
<dd> The maximum number (<i>retries</i>) of attempts to connect to a server (see also <code>-T</code>). The default is <tt>0</tt>.</p>
<dt><code>-T</code> <i>connect-pause</i></p>
<dd> Pause <i>connect-pause</i> seconds between connection retries (see also <code>-t</code>). The default is <tt>1</tt>.</p>
<dt><code>-w</code> <i>num</i></p>
<dd> Set each group&#8217;s high water mark (last received article number) to <i>num</i>. If <i>num</i> is negative, calculate <i>Current</i>+<i>num</i> instead (i.e. get the last <i>num</i> articles). Therefore, a <i>num</i> of <tt>0</tt> will re-get all articles on the server; whereas a <i>num</i> of <tt>&quot;-0&quot;</tt> will get no old articles, setting the water mark to <i>Current</i> (the most recent article on the server).</p>
<dt><code>-x</code></p>
<dd> If the <code>-x</code> flag is used, an Xref: header is added to any article that lacks one. It can be useful for instance if articles are fed to a news server which has <i>xrefslave</i> set in <i>inn.conf</i>.</p>
<dt><code>-z</code> <i>article-pause</i></p>
<dd> Sleep <i>article-pause</i> seconds between articles. The default is <tt>0</tt>.</p>
<dt><code>-Z</code> <i>group-pause</i></p>
<dd> Sleep <i>group-pause</i> seconds between groups. The default is <tt>0</tt>.</dl>
<h2>CONFIG FILE</h2>
<p> The config file for <code>pullnews</code> is divided into blocks, one block for each remote server to connect to. A block begins with the host line (which must have no leading whitespace) and contains just the hostname of the remote server, optionally followed by authentication details (username and password for that server). Note that authentication details can also be provided for the downstream server (a host line could be added for it in the configuration file, with no newsgroup to fetch). </p>
<p> Following the host line should be one or more newsgroup lines which start with whitespace followed by the name of a newsgroup to retrieve. Only one newsgroup should be listed on each line. </p>
<p> <code>pullnews</code> will update the config file to include the time the group was last checked and the highest numbered article successfully retrieved and transferred to the destination server. It uses this data to avoid doing duplicate work the next time it runs. </p>
<p> The full syntax is: </p>
<pre><code>
    &lt;host&gt; [&lt;username&gt; &lt;password&gt;]
            &lt;group&gt; [&lt;time&gt; &lt;high&gt;]
            &lt;group&gt; [&lt;time&gt; &lt;high&gt;]
</code></pre>
<p> where the &lt;host&gt; line must not have leading whitespace and the &lt;group&gt; lines must. </p>
<p> A typical configuration file would be: </p>
<pre>
    # Format group date high
    data.pa.vix.com
            rec.bicycles.racing 908086612 783
            rec.humor.funny 908086613 18
            comp.programming.threads
    nnrp.vix.com pull sekret
            comp.std.lisp
</pre>
<p> Note that an earlier run of <code>pullnews</code> has filled in details about the last article downloads from the two rec.* groups. The two comp.* groups were just added by the user and have not yet been checked. </p>
<p> The nnrp.vix.com server requires authentication, and <code>pullnews</code> will use the username <tt>&quot;pull&quot;</tt> and the password <tt>&quot;sekret&quot;</tt>.</p>
<h2>FILES</h2>
<dl>
<dt><i>pathbin</i>/pullnews</p>
<dd> The Perl script itself used to pull news from upstream servers and feed it to another news server.</p>
<dt>~/.pullnews</p>
<dd> The default config file. It is in the running user&#8217;s home directory.</dl>
<h2>HISTORY</h2>
<p> <code>pullnews</code> was written by James Brister for <font SIZE="-1">INN</font>. The documentation was rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> Geraint A. Edwards greatly improved <code>pullnews</code>, adding no more than 16 new recognized flags, fixing some bugs and integrating the <code>backupfeed</code> contrib script by Kai Henningsen, adding again 6 other flags. </p>
<p> <tt>$Id:</tt> pullnews.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-incoming-conf/">incoming.conf</a></i>(5), <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1). </p>
<h2>Index</h2>
