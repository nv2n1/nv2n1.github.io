---
title: "newsfeeds(5)"
name: "newsfeeds"
section: "5"
letter: "n"
url: "/docs/linux/man/5-newsfeeds/"
description: "newsfeeds – Determine where Usenet articles are sent"
---

<p>newsfeeds &#8211; Determine where Usenet articles are sent</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/newsfeeds specifies how incoming articles should be distributed to other programs and files on the server. It is parsed by the InterNetNews server <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) when it starts up, or when directed to by <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8). <code>innd</code> doesn&#8217;t send articles to remote sites itself, so <i>newsfeeds</i> doesn&#8217;t directly determine which remote news servers articles are sent to. Instead, it specifies what batch files should be created or which programs should be run (and what information should be sent to them), and then this information is used by programs like <i><a href="/docs/linux/man/8-innxmit/">innxmit</a></i>(8) and <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) to feed articles to remote sites. </p>
<p> The <i>newsfeeds</i> file isn&#8217;t used solely to set up feeding accepted articles to remote sites but also to pass them (or bits of information about them) to any local programs or files that want that data. For example, <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8), a daemon that processes incoming control messages, runs out of <i>newsfeeds</i>, as could a news to mail gateway. </p>
<p> The file is interpreted as a set of lines, parsed according to the following rules: If a line ends with a backslash, the backslash, the newline, and any whitespace at the start of the next line is deleted. This is repeated until the entire &#8220;logical&#8221; line is collected. If the logical line is blank or starts with a number sign (<tt>&quot;#&quot;</tt>), it is ignored. </p>
<p> All other lines are interpreted as feed entries. An entry should consist of four colon-separated fields; two of the fields may have optional sub-fields, marked off by a slash. Fields or sub-fields that take multiple parameters should be separated by a comma. Extra whitespace can cause problems and should be avoided. Except for the site names, case is significant. The format of an entry is: </p>
<pre> sitename[/exclude,exclude,...]\
 :pattern,pattern...[/distribution,distribution...]\
 :flag,flag...\
 :parameter</pre>
<p>Each field is described below. </p>
<p> The <i>sitename</i> is the name of the site to which a news article can be sent. It is used for writing log entries and for determining if an article should be forwarded to a site. (A &#8220;site&#8221; is the generic term for some destination of newsfeed data; it often corresponds to a remote news peer, but doesn&#8217;t have to. For example, a local archiving program run from <i>newsfeeds</i> is also a &#8220;site.&#8221;) If <i>sitename</i> already appears in the article&#8217;s Path: header, then the article will not be sent to the site. The name is usually whatever the remote site uses to identify itself in the Path: header, but can be almost any word. </p>
<p> Be careful, though, to avoid having the <i>sitename</i> accidentally match a Path: header entry unintentionally. For this reason, special local entries (such as archivers or gateways) should probably end with an exclamation point to make sure that they do not have the same name as any real site. For example, <tt>&quot;gateway&quot;</tt> is an obvious name for the local entry that forwards articles out to a mailing list. If a site with the name <tt>&quot;gateway&quot;</tt> posts an article, when the local site receives the article it will see the name in the Path and not send the article to its own <tt>&quot;gateway&quot;</tt> entry. Since <tt>&quot;gateway!&quot;</tt> can&#8217;t appear as an individual Path: entry since <tt>&quot;!&quot;</tt> is a delimiter in the Path: header, that would be a better thing to use for <i>sitename</i>. </p>
<p> (Another way to avoid this problem is with the <tt>&quot;Ap&quot;</tt> flag; see the description below.) </p>
<p> If an entry has an exclusion sub-field, the article will not be sent to that site if any of <i>exclude</i> appear in the Path: header. (It&#8217;s sometimes convenient to have the <i>sitename</i> be an abbreviated form of the name of the remote site, since all the <i>sitename</i>s to which an article is sent are written to the log and using shorter <i>sitename</i>s can therefore improve performance for large servers. In this case, the Path: header entries of those sites should be given as <i>exclude</i> entries and the <tt>&quot;Ap&quot;</tt> flag used so that the abbreviated <i>sitename</i> doesn&#8217;t accidentally match some other Path: header entry.) </p>
<p> The same <i>sitename</i> can be used more than once and the appropriate action will be taken for each entry that should receive the article, but this is recommended only for program feeds to avoid confusion. Case is not significant in site names. </p>
<p> The comma-separated <i>pattern</i> specifies which groups to send to the site; it is interpreted to build a &#8220;subscription list&#8221; for the site. The default subscription is to get all groups carried by the server. It is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern supporting poison (<tt>&quot;@&quot;</tt>) wildcards; see the <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) man page for full details on the pattern matching language. <i>pattern</i> will be matched against every newsgroup carried by the server and all newsgroups that match will be added to the subscription list for the site. </p>
<p> Normally, a given article (or information about it) is sent to a site if any of the newsgroups to which the article was posted are in that site&#8217;s subscription list. If a newsgroup matches a <tt>&quot;@&quot;</tt> pattern in <i>pattern</i>, then not only is it not added to the subscription list, but any articles crossposted to that newsgroup also will not be sent to that site even if other newsgroups to which it was crossposted are in that site&#8217;s subscription list. This is called a poison pattern (because matching groups are &#8220;poisoned&#8221;). </p>
<p> For example, to receive all comp.* groups, but only comp.sources.unix within the sources newsgroups, the following <i>pattern</i> can be used: </p>
<pre> comp.*,!comp.sources.*,comp.sources.unix</pre>
<p>Note that the trailing <tt>&quot;.*&quot;</tt> is required; the pattern has to match the whole newsgroup name. <tt>&quot;comp.sources.*&quot;</tt> could be written <tt>&quot;comp.sources*&quot;</tt> and would exclude the newsgroup comp.sources (if it exists) as well as the groups in the comp.sources.* hierarchy, but note that this would also exclude a newsgroup named comp.sources-only (whereas the above pattern would add that group to the site subscription list since it matches <tt>&quot;comp.*&quot;</tt> and none of the other patterns). </p>
<p> For another example, to feed alt.* and misc.* to a given site but not any articles posted to alt.binaries.warez (even if they&#8217;re also crossposted to other alt.* or misc.* groups), the following pattern can be used: </p>
<pre> alt.*,@alt.binaries.warez,misc.*</pre>
<p>Note, however, that if you reversed the <tt>&quot;alt.*&quot;</tt> and <tt>&quot;@alt.binaries.warez&quot;</tt> entries, this pattern would be equivalent to <tt>&quot;alt.*,misc.*&quot;</tt>, since the last matching pattern determines whether a given newsgroup matches and the poison logic only applies if the poison entry is the last matching entry. </p>
<p> Control messages follow slightly different propagation rules than normal articles; see <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) for the details. Note that most subscriptions should have <tt>&quot;!junk,!control,!control.*&quot;</tt> in their pattern list due to those propagation rules (and since <tt>&quot;junk&quot;</tt> is a special internal newsgroup; see <i>wanttrash</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) for more details on what it&#8217;s used for) and that the best way to keep control messages local to a site is with a distribution. </p>
<p> A subscription can be further modified by specifying distributions that the site should or should not receive. The default is to send all articles to all sites that subscribe to any of the groups where it has been posted, but if an article has a Distribution: header and any <i>distribution</i>s are specified, then they are checked according to the following rules:</p>
<dl>
<dt>1.</p>
<dd>If the Distribution: header matches any of the values in the sub-field, the article is sent.</p>
<dt>2.</p>
<dd>If a <i>distribution</i> starts with an exclamation point, and it matches the Distribution: header, the article is not sent.</p>
<dt>3.</p>
<dd>If the Distribution: header does not match any <i>distribution</i> in the site&#8217;s entry and no negations were used, the article is not sent.</p>
<dt>4.</p>
<dd>If the Distribution: header does not match any <i>distribution</i> in the site&#8217;s entry and any <i>distribution</i> started with an exclamation point, the article is sent.</dl>
<p> If an article has more than one distribution specified, then each one is handled according according to the above rules. If any of the specified distributions indicate that the article should be sent, it is; if none do, it is not sent. In other words, the rules are used as a logical or. </p>
<p> It is almost definitely a mistake to have a single feed that specifies distributions that start with an exclamation point along with some that don&#8217;t. </p>
<p> Distributions are text words, not patterns; entries like <tt>&quot;*&quot;</tt> or <tt>&quot;all&quot;</tt> have no special meaning. </p>
<p> The <i>flag</i> field is described in &#8220;<font SIZE="-1">FLAG</font> <font SIZE="-1">VALUES</font>&#8221;. The interpretation of the <i>parameter</i> field depends on the type of feed and is explained in more detail in &#8220;<font SIZE="-1">FEED</font> <font SIZE="-1">TYPES</font>&#8221;. It can be omitted for some types of feeds. </p>
<p> The site named <tt>&quot;ME&quot;</tt> is special. There must be exactly one such entry, and it should be the first entry in the file. If the <tt>&quot;ME&quot;</tt> entry has an exclusion sub-field, incoming articles are rejected completely if any of the names specified in that exclusion sub-field appear in their Path: headers. If the <tt>&quot;ME&quot;</tt> entry has a subscription list, that list is prepended to the subscription list of all other entries. For example, <tt>&quot;*,!control,!control.*,!junk,!foo.*&quot;</tt> could be used to set the default subscription list for all other feeds so that local postings are not propagated unless <tt>&quot;foo.*&quot;</tt> explicitly appears in the site&#8217;s subscription list. This feature tends to be somewhat confusing since the default subscription is prepended and can be overridden by other patterns. </p>
<p> If the <tt>&quot;ME&quot;</tt> entry has a distribution sub-field, only articles that match that distribution list are accepted and all other articles with a distribution are rejected. A common use for this is to put something like <tt>&quot;/!local&quot;</tt> in the <tt>&quot;ME&quot;</tt> entry to reject local postings from other misconfigured sites. The distribution sub-field of <tt>&quot;ME&quot;</tt> has no effect on the acceptance or rejection of articles that do not have a Distribution header field. </p>
<p> An empty <tt>&quot;ME&quot;</tt> entry is possible, in which case no exclusion patterns will be defined. </p>
<p> Finally, it is also possible to set variables in <i>newsfeeds</i> and use them later in the file. A line starting with <tt>&quot;$&quot;</tt> sets a variable. For example: </p>
<pre> $LOCALGROUPS=local.*,example.*</pre>
<p>This sets the variable <tt>&quot;LOCALGROUPS&quot;</tt> to <tt>&quot;local.*,example.*&quot;</tt>. This variable can later be used elsewhere in the file, such as in a site entry like: </p>
<pre> news.example.com:$LOCALGROUPS:Tf,Wnm:</pre>
<p>which is then completely equivalent to: </p>
<pre> news.example.com:local.*,example.*:Tf,Wnm:</pre>
<p>Variables aren&#8217;t solely simple substitution. If either <tt>&quot;!&quot;</tt> or <tt>&quot;@&quot;</tt> immediately preceds the variable and the value of the variable contains commas, that character will be duplicated before each comma. This somewhat odd-sounding behavior is designed to make it easier to use variables to construct feed patterns. The utility becomes more obvious when you observe that the line: </p>
<pre> news.example.net:*,@$LOCALGROUPS:Tf,Wnm:</pre>
<p>is therefore equivalent to: </p>
<pre> news.example.net:*,@local.*,@example.*:Tf,Wnm:</pre>
<p>which (as explained below) excludes all of the groups in <tt>$LOCALGROUPS</tt> from the feed to that site.</p>
<h2>Flag Values</h2>
<p>The <i>flags</i> parameter specifies miscellaneous parameters, including the type of feed, what information should be sent to it, and various limitations on what articles should be sent to a site. They may be specified in any order and should be separated by commas. Flags that take values should have the value immediately after the flag letter with no whitespace. The valid flags are:</p>
<dl>
<dt><code>&lt;</code> <i>size</i></p>
<dd>An article will only be sent to this site if it is less than <i>size</i> bytes long. The default is no limit.</p>
<dt><code>&gt;</code> <i>size</i></p>
<dd>An article will only be sent to this site if it is greater than <i>size</i> bytes long. The default is no limit.</p>
<dt><code>A</code> <i>checks</i></p>
<dd>An article will only be sent to this site if it meets the requirements specified in <i>checks</i>, which should be chosen from the following set. <i>checks</i> can be multiple letters if appropriate. Note that this flag is not effective on funnel targets; it has to be used on every funnel entry (for instance, <code>Af</code> is not effective on the <i>innfeed!</i> funnel target and therefore has to be specified on every funnelled news site).</p>
<dl>
<dd>
<dl>
<dt>c</p>
<dd>Exclude all kinds of control messages.</p>
<dt>C</p>
<dd>Only send control messages, not regular articles.</p>
<dt>d</p>
<dd>Only send articles with a Distribution: header. Combined with a particular distribution value in the <i>distribution</i> part of the site entry, this can be used to limit articles sent to a site to just those with a particuliar distribution.</p>
<dt>e</p>
<dd>Only send articles where every newsgroup listed in the Newsgroups: header exists in the <i>active</i> file.</p>
<dt>f</p>
<dd>Don&#8217;t send articles rejected by filters. This is only useful when <i>dontrejectfiltered</i> is set to true in <i>inn.conf</i>. With that variable set, this lets one accept all articles but not propagate filtered ones to some sites.</p>
<dt>j</p>
<dd>Propagate articles according to their Newsgroups: header. This is only useful when <i>wanttrash</i> is set to true in <i>inn.conf</i>. With that variable set, articles accepted and filed in <tt>&quot;junk&quot;</tt> (due to <i>wanttrash</i>) are fed to peers based on their subscription pattern applied to the Newsgroups: header as though they were accepted and all those groups were locally carried. Otherwise, they are propagated to sites that receive the <tt>&quot;junk&quot;</tt> newsgroup. </p>
<p> This variable is useful if you want to run <font SIZE="-1">INN</font> with a minimal <i>active</i> file and propagate all posts.</p>
<dt>o</p>
<dd>Only send articles for which overview data was stored.</p>
<dt>O</p>
<dd>Send articles to this site that don&#8217;t have an Injection-Info: or X-Trace: header, even if the <tt>&quot;O&quot;</tt> flag is also given.</p>
<dt>p</p>
<dd>Only check the exclusions against the Path: header of articles; don&#8217;t check the site name. This is useful if your site names aren&#8217;t the same as the Path: entries added by those remote sites, or for program feeds where the site name is arbitrary and unrelated to the Path: header.</dl>
</dl>
<dl>
<dd>If both <tt>&quot;c&quot;</tt> and <tt>&quot;C&quot;</tt> are given, the last specified one takes precedence.</dl>
<dt><code>B</code> <i>high</i>/<i>low</i></p>
<dd>If a site is being fed by a file, channel, or exploder (see below), the server will normally start trying to write the information as soon as possible. Providing a buffer may give better system performance and help smooth out overall load if a large batch of news comes in. The value of the this flag should be two numbers separated by a slash. <i>high</i> specifies the point at which the server can start draining the feed&#8217;s I/O buffer, and <i>low</i> specifies when to stop writing and begin buffering again; the units are bytes. The default is to do no buffering, sending output as soon as it is possible to do so.</p>
<dt><code>C</code> <i>count</i></p>
<dd>If this flag is specified, an article will only be sent to this site if the number of groups it is posted to, plus the square of the number of groups followups would appear in, is no more than <i>count</i>. <tt>30</tt> is a good value for this flag, allowing crossposts to up to 29 groups when followups are set to a single group or poster and only allowing crossposts to 5 groups when followups aren&#8217;t set.</p>
<dt><code>F</code> <i>name</i></p>
<dd>Specifies the name of the file that should be used if it&#8217;s necessary to begin spooling for the site (see below). If <i>name</i> is not an absolute path, it is taken to be relative to <i>pathoutgoing</i> in <i>inn.conf</i>. If <i>name</i> is a directory, the file <i>togo</i> in that directory will be used as the file name.</p>
<dt><code>G</code> <i>count</i></p>
<dd>If this flag is specified, an article will only be sent to this site if it is posted to no more than <i>count</i> newsgroups. This has the problem of filtering out many FAQs, as well as newsgroup creation postings and similar administrative announcements. Either the <code>C</code> flag or the <code>U</code> flag is a better solution.</p>
<dt><code>H</code> <i>count</i></p>
<dd>If this flag is specified, an article will only be sent to this site if it has <i>count</i> or fewer sites in its Path: line. This flag should only be used as a rough guide because of the loose interpretation of the Path: header; some sites put the poster&#8217;s name in the header, and some sites that might logically be considered to be one hop become two because they put the posting workstation&#8217;s name in the header. The default value for <i>count</i> if not specified is one. (Also see the <code>O</code> flag, which is sometimes more appropriate for some uses of this flag.)</p>
<dt><code>I</code> <i>size</i></p>
<dd>The flag specifies the size of the internal buffer for a file feed. If there are more file feeds than allowed by the system, they will be buffered internally in least-recently-used order. If the internal buffer grows bigger then <i>size</i> bytes, however, the data will be written out to the appropriate file. The default value is <tt>16</tt>&nbsp;<wbr><font SIZE="-1">KB</font>.</p>
<dt><code>N</code> <i>status</i></p>
<dd>Restricts the articles sent to this site to those in newsgroups with the moderation status given by <i>status</i>. If <i>status</i> is <tt>&quot;m&quot;</tt>, only articles in moderated groups are sent; if <i>status</i> is <tt>&quot;u&quot;</tt>, only articles in unmoderated groups are sent.</p>
<dt><code>O</code> <i>originator</i></p>
<dd>If this flag is specified, an article will only be sent to this site if it contains an Injection-Info: header (or an X-Trace: header if no Injection-Info: header is found) and the first field of this header matches <i>originator</i>. <i>originator</i> is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) expression without commas or a list of such expressions, separated by <tt>&quot;/&quot;</tt>. The article is never sent if the first character of the pattern begins with <tt>&quot;@&quot;</tt> and the rest of the pattern matches. One use of this flag is to restrict the feed to locally generated posts by using an <i>originator</i> pattern that matches the Injection-Info: header added by the local server.</p>
<dt><code>P</code> <i>priority</i></p>
<dd>The nice priority that this channel or program feed should receive. This should be a positive number between 0 and 20 and is the priority that the new process will run with. This flag can be used to raise the priority to normal if you&#8217;re using the <i>nicekids</i> parameter in <i>inn.conf</i>.</p>
<dt><code>Q</code> <i>hashfeed</i></p>
<dd>Specifies the <i>hashfeed</i> match expression for this site. It must be in the form <tt>&quot;value/mod&quot;</tt> or <tt>&quot;start-end/mod&quot;</tt>. The Message-ID of the article is hashed using <font SIZE="-1">MD5</font>, which results in a 128-bit hash. The lowest 32 bits are then taken by default as the hashfeed value (which is an integer). If the hashfeed value modulus <tt>&quot;mod&quot;</tt> plus one equals <tt>&quot;value&quot;</tt> or is between <tt>&quot;start&quot;</tt> and <tt>&quot;end&quot;</tt>, the article will be fed to this site. All these numbers must be integers. </p>
<p> It is a deterministic way to control the flow of articles and to split a feed. For instance: </p>
<pre> Q1/2 Feeds about 50% of all articles to this site.
 Q2/2 Feeds the other 50% of all articles.</pre>
<p>Another example with three sites: </p>
<pre> Q1-3/10 Feeds about 30% of all articles.
 Q4-5/10 Feeds about 20% of all articles.
 Q6-10/10 Feeds about 50% of all articles.</pre>
<p>If this flag is specified multiple times, the contents will be logically <tt>&quot;OR&quot;</tt>ed together (just one match is needed). </p>
<p> You can use an extended syntax of the form <tt>&quot;value/mod_offset&quot;</tt> or <tt>&quot;start-end/mod_offset&quot;</tt>. As <font SIZE="-1">MD5</font> generates a 128-bit return value, it is possible to specify from which byte-offset the 32-bit integer used by hashfeed starts. The default value for <tt>&quot;offset&quot;</tt> is <tt>&quot;_0&quot;</tt> and thirteen overlapping values from <tt>&quot;_0&quot;</tt> to <tt>&quot;_12&quot;</tt> can be used. Only up to four totally independent values exist: <tt>&quot;_0&quot;</tt>, <tt>&quot;_4&quot;</tt>, <tt>&quot;_8&quot;</tt> and <tt>&quot;_12&quot;</tt>. </p>
<p> Therefore, it allows to a generate a second level of deterministic distribution. Indeed, if a news server is fed <tt>&quot;Q1/2&quot;</tt>, it can go on splitting thanks to <tt>&quot;Q1-3/9_4&quot;</tt> for instance. Up to four levels of deterministic distribution can be used. </p>
<p> The algorithm is compatible with the one used by Diablo 5.1 and up. If you want to use the legacy quickhashing method used by Diablo before 5.1, you can put an <tt>&quot;@&quot;</tt> sign just after the <code>Q</code> flag (for instance <tt>&quot;Q@1-3/10&quot;</tt>, but the distribution of the messages is not perfect with this legacy method whose use is discouraged and for which offsets cannot be used).</p>
<dt><code>S</code> <i>size</i></p>
<dd>If the amount of data queued for the site gets to be larger than <i>size</i> bytes, the server will switch to spooling, appending to a file specified by the <code>F</code> flag, or <i>pathoutgoing</i>/<i>sitename</i> if <code>F</code> is not specified. Spooling usually happens only for channel or exploder feeds, when the spawned program isn&#8217;t keeping up with its input.</p>
<dt><code>T</code> <i>type</i></p>
<dd>This flag specifies the type of feed for this site. <i>type</i> should be a letter chosen from the following set: </p>
<pre> c Channel
 f File
 l Log entry only
 m Funnel (multiple entries feed into one)
 p Program
 x Exploder</pre>
<p>Each feed is described below in &#8220;<font SIZE="-1">FEED</font> <font SIZE="-1">TYPES</font>&#8221;. The default is <code>Tf</code>, for a file feed.</p>
<dt><code>U</code> <i>count</i></p>
<dd>If this flag is specified, an article will only be sent to this site if followups to this article would be posted to no more than <i>count</i> newsgroups. (Also see <code>C</code> for a more complex way of handling this.)</p>
<dt><code>W</code> <i>items</i></p>
<dd>For a file, channel, or exploder feed, this flag controls what information will be sent to this site. For a program feed, only the asterisk (<tt>&quot;*&quot;</tt>) has any effect. <i>items</i> should be chosen from the following set:</p>
<dl>
<dd>
<dl>
<dt>b</p>
<dd>Size of the article (in wire format, meaning with <font SIZE="-1">CRLF</font> at the end of each line, periods doubled at the beginning of lines, and ending in a line with a single period) in bytes.</p>
<dt>e</p>
<dd>The time the article will expire as seconds since epoch if it has an Expires: header, <tt>0</tt> otherwise.</p>
<dt>f</p>
<dd>The storage <font SIZE="-1">API</font> token of the article (the same as <tt>&quot;n&quot;</tt>). The article can be retrieved given the storage <font SIZE="-1">API</font> token by using <i><a href="/docs/linux/man/8-sm/">sm</a></i>(8).</p>
<dt>g</p>
<dd>The newsgroup the article is in; if cross-posted, then the first of the groups to which the article was posted that this site gets. (The difference from <tt>&quot;G&quot;</tt> is that this sends the newsgroup to which the article was posted even if it is a control message.)</p>
<dt>h</p>
<dd>The history hash key of the article (derived from the message <font SIZE="-1">ID</font>).</p>
<dt>m</p>
<dd>The message <font SIZE="-1">ID</font> of the article.</p>
<dt>n</p>
<dd>The storage <font SIZE="-1">API</font> token of the article. The article can be retrieved given the storage <font SIZE="-1">API</font> token by using <i><a href="/docs/linux/man/8-sm/">sm</a></i>(8).</p>
<dt>p</p>
<dd>The time the article was posted a seconds since epoch.</p>
<dt>s</p>
<dd>The site that fed the article to the server. This is taken from either the Path: header or the <font SIZE="-1">IP</font> address of the sending site depending on the value of <i>logipaddr</i> in <i>inn.conf</i>. If <i>logipaddr</i> is true and the <font SIZE="-1">IP</font> address is <tt>0.0.0.0</tt> (meaning that the article was fed from localhost by a program like <i><a href="/docs/linux/man/8-rnews/">rnews</a></i>(8)), the Path: header value will be sent instead.</p>
<dt>t</p>
<dd>The time the article was received as seconds since epoch.</p>
<dt>*</p>
<dd>The names of the appropriate funnel entries, or all sites that get the article (see below for more details).</p>
<dt>D</p>
<dd>The value of the Distribution: header of the article, or <tt>&quot;?&quot;</tt> if there is no such header in the article.</p>
<dt>G</p>
<dd>Where the article is stored. If the newsgroup is crossposted, this is generally the first of the groups to which it was posted that this site receives; however, control messages are filed in control or control.* (which is the difference between this item and <tt>&quot;g&quot;</tt>).</p>
<dt>H</p>
<dd>All of the headers, followed by a blank line. The Xref header will already be present, and a Bytes header containing the article&#8217;s size in bytes as in the <tt>&quot;b&quot;</tt> item will be added to the headers. If used, this should be the only item in the list.</p>
<dt>N</p>
<dd>The value of the Newsgroups: header.</p>
<dt>P</p>
<dd>The value of the Path: header.</p>
<dt>O</p>
<dd>Overview data for the article.</p>
<dt>R</p>
<dd>Information needed for replication (the Xref header without the site name).</dl>
</dl>
<dl>
<dd>More than one letter can be given. If multiple items are specified, they will be written in the order specified separated by spaces. (<tt>&quot;H&quot;</tt> should be the only item if given, but if it&#8217;s not a newline will be sent before the beginning of the headers.) The default is <code>Wn</code>. </p>
<p> The <tt>&quot;H&quot;</tt> and <tt>&quot;O&quot;</tt> items are intended for use by programs that create news overview databases or require similar information. <code>WnteO</code> is the flag to generate input needed by the <i><a href="/docs/linux/man/8-overchan/">overchan</a></i>(8) program. </p>
<p> The asterisk (<tt>&quot;*&quot;</tt>) has special meaning. Normally it expands to a space-separated list of all sites that received the current article. If, however, this site is a target of a funnel feed (in other words, if it is named by other sites which have the <code>Tm</code> flag), then the asterisk expands to the names of the funnel feeds that received the article. Similarly, if the site is a program feed, an asterisk in the <i>parameter</i> field will be expanded into the list of funnel feeds that received the article. A program feed cannot get the site list unless it is the target of other <code>Tm</code> feeds.</dl>
</dl>
<h2>Feed Types</h2>
<p><code>innd</code> provides four basic types of feeds: log, file, program, and channel. An exploder is a special type of channel. In addition, several entries can feed into the same feed; these are funnel feeds, which refer to an entry that is one of the other types. Funnel feeds are partially described above with the description of the <code>W*</code> flag. A funnel feed gets every article that would be sent to any of the feeds that funnel into it and normally include the <code>W*</code> flag in their flags so that the program processing that feed knows which sites received which articles. The most common funnel feed is <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8). </p>
<p> Note that the term &#8220;feed&#8221; is technically a misnomer, since the server doesn&#8217;t transfer articles itself and only writes data to a file, program, or log telling another program to transfer the articles. </p>
<p> The simplest feed is a log feed (<code>Tl</code>). Other than a mention in the news log file, <i>pathlog</i>/news, no data is written out. This is equivalent to a <code>Tf</code> entry writing to <i>/dev/null</i>, except that no file is ever opened. Flushing a log feed does nothing. </p>
<p> A file feed (<code>Tf</code>) is the next simplest type of feed. When the site should receive an article, the specified data is written out to the file named by the <i>parameter</i> field. If <i>parameter</i> is not an absolute path, it is taken to be relative to <i>pathoutgoing</i> in <i>inn.conf</i>. If <i>parameter</i> is not given, it defaults to <i>pathoutgoing</i>/<i>sitename</i>. The file name should be unique (two file feeds should not ever point to the same file). </p>
<p> File feeds are designed for use by external programs that periodically process the written data. To cooperate with <code>innd</code> properly, such external programs should first rename the batch file and then send a flush command for that site to <code>innd</code> using <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8). <code>innd</code> will then write out any buffered data, close the file, and reopen it (under the original name), and the program can process the data in the renamed file at its leisure. File feeds are most frequently used in combination with <i><a href="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8). </p>
<p> A program feed (<code>Tp</code>) spawns a given program for every article that the site receives. The <i>parameter</i> field must be the command line to execute, and should contain one instance of <tt>%s</tt>, which will be replaced by the storage <font SIZE="-1">API</font> token of the article (the actual article can be retrieved by the program using <i><a href="/docs/linux/man/8-sm/">sm</a></i>(8)). The program will not receive anything on standard input (unlike earlier versions of <font SIZE="-1">INN</font>, where the article is sent to the program on stdin), and standard output and error from the program will be set to the error log (<i>pathlog</i>/errlog). <code>innd</code> will try to avoid spawning a shell if the command has no shell meta-characters; this feature can be defeated if necessary for some reason by appending a semi-colon to the end of the command. The full path name of the program to be run must be specified unless the command will be run by the shell (and it is strongly recommended that the full path name always be specified regardless). </p>
<p> If a program feed is the target of a funnel, and if <code>W*</code> appears in the flags of the site, a single asterisk may be present in the <i>parameter</i> and will be replaced by a space-separated list of names of the sites feeding into the funnel which received the relevant article. If the site is not the target of a funnel, or if the <code>W*</code> flag is not used, the asterisk has no special meaning. </p>
<p> Flushing a program feed does nothing. </p>
<p> For a channel (<code>Tc</code>) or exploder (<code>Tx</code>) feed, the <i>parameter</i> field again names the process to start. As with program feeds, the full path to the program must be specified. However, rather than spawning the program for every article, it is spawned once and then whenever the site receives an article, the data specified by the site flags is written to the standard input of the spawned program. Standard output and error are set as with program feeds. If the process exits, it will be restarted automatically. If the process cannot be started, the server will spool input to a file named <i>pathoutgoing</i>/<i>sitename</i> and will try to start the process again later. </p>
<p> When a channel or exploder feed is flushed, the server closes its end of the pipe to the program&#8217;s standard input. Any pending data that has not been written will be spooled; see the description of the <code>S</code> flag above. The server will then spawn a new instance of the program. No signal is sent to the program; it is up to the program handling a channel or exploder feed to notice end of file on its standard input and exit appropriately. </p>
<p> Exploders are a special type of channel feed. In addition to the channel feed behavior described above, exploders can also be sent command lines. These lines start with an exclamation point and their interpretation is up to the exploder. The following commands are generated automatically by the server: </p>
<pre> !newgroup group
 !rmgroup group
 !flush
 !flush site</pre>
<p>These commands are sent whenever the <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) command of the same name is received by the server. In addition, the <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) <tt>&quot;send&quot;</tt> command can be used to send an arbitrary command line to an exploder. The primary exploder is <i><a href="/docs/linux/man/8-buffchan/">buffchan</a></i>(8). </p>
<p> Finally, <code>Tm</code> feeds are the input to a funnel. The <i>parameter</i> field of the site should name the site handling articles for all of the funnel inputs.</p>
<h2>Examples</h2>
<p>The syntax of the <i>newsfeeds</i> file is so complex because you can specify a staggering variety of feeds. <font SIZE="-1">INN</font> is capable of interacting with a wide variety of programs that do various things with news articles. Far and away the most common two entries in <i>newsfeeds</i>, however, are file feeds for <i><a href="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8) and funnel feeds for <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8). </p>
<p> The former look like this: </p>
<pre> feed.example.com:*,!control,!control.*,!junk:Tf,Wnm:</pre>
<p>which generates a file named <i>pathoutgoing</i>/feed.example.com containing one line per article consisting of the storage <font SIZE="-1">API</font> token, a space, and the message <font SIZE="-1">ID</font>. </p>
<p> The latter look like this: </p>
<pre> feed.example.com:*,!control,!control.*,!junk:Tm:innfeed!</pre>
<p>Very similar, except that this is the input to a funnel feed named <tt>&quot;innfeed!&quot;</tt>. One could also write this as: </p>
<pre> example/feed.example.com:*,!control,!control.*,!junk:Ap,Tm:innfeed!</pre>
<p>(note the <code>Ap</code> so that articles that contain just <tt>&quot;example&quot;</tt> in the Path: header will still be sent), which is completely equivalent except that this will be logged in <i>pathlog</i>/news as going to the site <tt>&quot;example&quot;</tt> rather than <tt>&quot;feed.example.com&quot;</tt>. </p>
<p> The typical feed entry for <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) is a good example of a channel feed that&#8217;s the target of various funnel feeds (make sure the path to <code>innfeed</code> is properly set): </p>
<pre> innfeed!:!*:Tc,Wnm*:&lt;pathbin in inn.conf&gt;/innfeed -y</pre>
<p>Note that the <i>pattern</i> for this feed is just <tt>&quot;!*&quot;</tt> so that it won&#8217;t receive any articles directly. The feed should only receive those articles that would go to one of the funnel feeds that are feeding into it. <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) will receive one line per article on its standard input containing the storage <font SIZE="-1">API</font> token, the message <font SIZE="-1">ID</font>, and a space-separated list of sites that should receive that article. </p>
<p> Here&#8217;s a more esoteric example of a channel feed: </p>
<pre> watcher!:*:Tc,Wbnm\
 :exec awk '$1 &gt; 1000000 { print &quot;BIG&quot;, $2, $3 }' &gt; /dev/console</pre>
<p>This receives the byte size of each article along with the storage <font SIZE="-1">API</font> token and message <font SIZE="-1">ID</font>, and prints to the console a line for every article that&#8217;s over a million bytes. This is actually rather a strange way to write this since <font SIZE="-1">INN</font> can do the size check itself; the following is equivalent: </p>
<pre> watcher!:*:Tc,&gt;1000000,Wbnm\
 :exec awk '{ print &quot;BIG&quot;, $2, $3}' &gt; /dev/console</pre>
<p>Here&#8217;s a cute, really simple news to mail gateway that also serves as an example of a fairly fancy program feed: </p>
<pre> mailer!:!*:W*,Tp\
 :sm %s | innmail -s &quot;News article&quot; *</pre>
<p>Remember that <tt>%s</tt> is replaced by the storage <font SIZE="-1">API</font> token, so this retrieves the article and pipes it into <code>innmail</code> (which is safer than programs like <i><a href="/docs/linux/man/1-mail/">Mail</a></i>(1) because it doesn&#8217;t parse the body for tilde commands) with a given subject line. Note the use of <tt>&quot;*&quot;</tt> in the command line and <code>W*</code> in the flags; this entry is designed to be used as the target of funnel feeds such as: </p>
<pre> peter [at] example.com:news.software.nntp:Tm:mailer!
 sue [at] example.com:news.admin.misc:Tm:mailer!</pre>
<p>Suppose that the server receives an article crossposted between news.admin.misc and news.software.nntp. The server will notice that the article should be sent to the site <tt>&quot;peter [at] example.com&quot;</tt> and the site <tt>&quot;bob [at] example.com&quot;</tt>, both of which funnel into <tt>&quot;mailer!&quot;</tt>, so it will look at the <tt>&quot;mailer!&quot;</tt> site and end up executing the command line: </p>
<pre> sm @...@ | innmail -s &quot;News article&quot; peter [at] example.com sue [at] example.com</pre>
<p>which will mail the article to both Peter and Sue. </p>
<p> Finally, another very useful example of a channel feed: the standard entry for <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8). Make sure its path is properly set. </p>
<pre> controlchan!\
 :!*,control,control.*,!control.cancel/!collabra-internal\
 :AC,Tc,Wnsm:&lt;pathbin in inn.conf&gt;/controlchan</pre>
<p>This program only wants information about articles posted to a control newsgroup other than control.cancel, which due to the sorting of control messages described in <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) will send it all control messages except for cancel messages. In this case, we also exclude any article with a distribution of <tt>&quot;collabra-internal&quot;</tt>. <code>controlchan</code> gets the storage <font SIZE="-1">API</font> token, the name of the sending site (for processing old-style ihave and sendme control messages, be sure to read about <i>logipaddr</i> in <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8)), and the message <font SIZE="-1">ID</font> for each article. </p>
<p> For many other examples, including examples of the special <tt>&quot;ME&quot;</tt> site entry, see the example <i>newsfeeds</i> file distributed with <font SIZE="-1">INN</font>. Also see the install documentation that comes with <font SIZE="-1">INN</font> for information about setting up the standard newsfeeds entries used by most sites.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Reformatted and rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> newsfeeds.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-buffchan/">buffchan</a></i>(8), <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8), <i><a href="/docs/linux/man/8-innxmit/">innxmit</a></i>(8), <i><a href="/docs/linux/man/8-nntpsend/">nntpsend</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
