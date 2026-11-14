---
title: "innfeed-conf(5)"
name: "innfeed-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-innfeed-conf/"
description: "innfeed.conf – Configuration file for innfeed"
---

<p>innfeed.conf &#8211; Configuration file for innfeed</p>
<h2>Description</h2>
<p>The configuration file <i>innfeed.conf</i> in <i>pathetc</i> is used to control the <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8) program. It is a fairly free-format file that consists of three types of entries: <i>key</i>:<i>value</i>, <i>peer</i> and <i>group</i>. Comments are from the hash character <tt>&quot;#&quot;</tt> to the end of the line. </p>
<p> <i>key</i>:<i>value</i> entries are a keyword and a value separated by a colon (which can itself be surrounded by whitespace). For example: </p>
<pre> max-connections: 10</pre>
<p>A legal <i>key</i> starts with a letter and contains only letters, digits, and the <tt>&quot;_&quot;</tt> and <tt>&quot;-&quot;</tt> characters. There are 5 different types of values: integers, floating-point numbers, characters, booleans, and strings. </p>
<p> Integer and floating-point numbers are as to be expected, except that exponents in floating-point numbers are not supported.<tt>&nbsp;<wbr>&nbsp;<wbr></tt>A boolean value<br />
 is either <tt>&quot;true&quot;</tt> or <tt>&quot;false&quot;</tt> (case is not significant). A character value is a single-quoted character as defined by the C-language. A string value is any other sequence of characters. If the string needs to contain whitespace, then it must be quoted with double quotes, and uses the same format for embedding non-printing characters as normal C-language string. </p>
<p> Peer entries look like: </p>
<pre> peer &lt;name&gt; {
 # body ...
 }</pre>
<p>The word <tt>&quot;peer&quot;</tt> is required. The <i>&lt;name&gt;</i> is the same as the site name in <font SIZE="-1">INN</font>&#8216;s <i>newsfeeds</i> configuration file. The body of a peer entry contains some number (possibly zero) of <i>key</i>:<i>value</i> entries. </p>
<p> Group entries look like: </p>
<pre> group &lt;name&gt; {
 # body ...
 }</pre>
<p>The word <tt>&quot;group&quot;</tt> is required. The <i>&lt;name&gt;</i> is any string valid as a key. The body of a group entry contains any number of the three types of entries. So <i>key</i>:<i>value</i> pairs can be defined inside a group, and peers can be nested inside a group, and other groups can be nested inside a group. </p>
<p> <i>key</i>:<i>value</i> entries that are defined outside of all <i>peer</i> and <i>group</i> entries are said to be at &#8220;global scope&#8221;. There are global <i>key</i>:<i>value</i> entries that apply to the process as a whole (for example the location of the backlog file directory), and there are global <i>key</i>:<i>value</i> entries that act as defaults for peers. When <code>innfeed</code> looks for a specific value in a peer entry (for example, the maximum number of connections to set up), if the value is not defined in the peer entry, then the enclosing groups are examined for the entry (starting at the closest enclosing group). If there are no enclosing groups, or the enclosing groups do not define the <i>key</i>:<i>value</i>, then the value at global scope is used. </p>
<p> A small example could be: </p>
<pre> # Global value applied to all peers that have
 # no value of their own.
 max-connections: 5
 # A peer definition. &quot;uunet&quot; is the name used by innd
 # in the newsfeeds configuration file.
 peer uunet {
 ip-name: usenet1.uu.net
 }
 peer vixie {
 ip-name: gw.home.vix.com
 max-connections: 10 # Override global value.
 }
 # A group of two peers which can handle more connections
 # than normal.
 group fast-sites {
 max-connections: 15
 # Another peer. The &quot;max-connections&quot; value from the
 # &quot;fast-sites&quot; group scope is used. The &quot;ip-name&quot; value
 # defaults to the peer's name.
 peer data.ramona.vix.com {
 }
 peer bb.home.vix.com {
 max-connections: 20 # He can really cook.
 }
 }</pre>
<p>Given the above configuration file, the defined peers would have the following values for the <i>max-connections</i> key: </p>
<pre> uunet 5
 vixie 10
 data.ramona.vix.com 15
 bb.home.vix.com 20</pre>
<p><code>innfeed</code> ignores <i>key</i>:<i>value</i> pairs it is not interested in. Some configuration file values can be set via a command-line option, in which case that setting overrides the settings in the file. </p>
<p> Configuration files can be included in other configuration files via the syntax: </p>
<pre> $INCLUDE filename</pre>
<p>There is a maximum nesting depth of 10. </p>
<p> For a fuller example configuration file, see the supplied <i>innfeed.conf</i>.</p>
<h2>Global Values</h2>
<p>The following listing show all the keys that apply to the process as whole. These are not required (compiled-in defaults are used where needed).</p>
<dl>
<dt><i>news-spool</i></p>
<dd>This key requires a pathname value and defaults to <i>patharticles</i> in <i>inn.conf</i>. It specifies where the top of the article spool is. This corresponds to the <code>-a</code> command-line option.</p>
<dt><i>input-file</i></p>
<dd>This key requires a pathname value. It specifies the pathname (relative to the <i>backlog-directory</i> value) that should be read in funnel-file mode. This corresponds to giving a filename as an argument on the command-line (i.e. its presence also implies that funnel-file mode should be used). </p>
<p> The default is unset; <code>innfeed</code> then runs in channel or batch mode.</p>
<dt><i>pid-file</i></p>
<dd>This key requires a pathname value and defaults to <i>innfeed.pid</i>. It specifies the pathname (relative to <i>pathrun</i> in <i>inn.conf</i>) where the pid of the <code>innfeed</code> process should be stored. This corresponds to the <code>-p</code> command-line option.</p>
<dt><i>debug-level</i></p>
<dd>This key defines the debug level for the process. Default is <tt>0</tt>. A non-zero number generates a lot of messages to stderr, or to the config-defined <i>log-file</i>. This corresponds to the <code>-d</code> command-line option. </p>
<p> If a file named <i>innfeed.debug</i> exists in the <i>pathlog</i> directory (as set in <i>inn.conf</i>), then <i>debug-level</i> is automatically set to <tt>1</tt>. This is a cheap way of avoiding continual reloading of the <i>newsfeeds</i> file when debugging. Note that debug messages still go to <i>log-file</i>.</p>
<dt><i>debug-shrinking</i></p>
<dd>This key requires a boolean value and defaults to false (the debug file is allowed to grow without bound). If set to true, this file is truncated when its size reaches a certain limit. See <i>backlog-limit</i> for more details.</p>
<dt><i>initial-sleep</i></p>
<dd>This key requires a positive integer. The default value is <tt>2</tt>. It defines the number of seconds to wait when <code>innfeed</code> (or a fork) starts, before beginning to open connections to remote hosts.</p>
<dt><i>fast-exit</i></p>
<dd>This key requires a boolean value and defaults to false. If set to true, when <code>innfeed</code> receives a <font SIZE="-1">SIGTERM</font> or <font SIZE="-1">SIGQUIT</font> signal, it will close its listeners as soon as it can, even if it means dropping articles.</p>
<dt><i>use-mmap</i></p>
<dd>This key requires a boolean value. It specifies whether mmaping should be used if <code>innfeed</code> has been built with <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) support. If article data on disk is not in NNTP-ready format (<font SIZE="-1">CR/LF</font> at the end of each line), then after mmaping, the article is read into memory and fixed up, so mmaping has no positive effect (and possibly some negative effect depending on your system), and so in such a case this value should be <tt>&quot;false&quot;</tt>, which is the default value. This corresponds to the <code>-M</code> command-line option.</p>
<dt><i>log-file</i></p>
<dd>This key requires a pathname value and defaults to <i>innfeed.log</i>. It specifies where any logging messages that could not be sent via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) should go (such as those generated when a positive value for <i>debug-value</i> is used). This corresponds to the <code>-l</code> command-line option. </p>
<p> This pathname is relative to <i>pathlog</i> in <i>inn.conf</i>.</p>
<dt><i>log-time-format</i></p>
<dd>This key requires a format string suitable for <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3). It is used for messages sent via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) and to the <i>status-file</i>. Default value is <tt>&quot;%a %b %d %H:%M:%S %Y&quot;</tt>.</p>
<dt><i>backlog-directory</i></p>
<dd>This key requires a pathname value and defaults to <i>innfeed</i>. It specifies where the current <code>innfeed</code> process should store backlog files. This corresponds to the <code>-b</code> command-line option. </p>
<p> This pathname is relative to <i>pathspool</i> in <i>inn.conf</i>.</p>
<dt><i>backlog-highwater</i></p>
<dd>This key requires a positive integer value and defaults to <tt>5</tt>. It specifies how many articles should be kept on the backlog file queue before starting to write new entries to disk.</p>
<dt><i>backlog-ckpt-period</i></p>
<dd>This key requires a positive integer value and defaults to <tt>30</tt>. It specifies how many seconds elapse between checkpoints of the input backlog file. Too small a number will mean frequent disk accesses; too large a number will mean after a crash, <code>innfeed</code> will re-offer more already-processed articles than necessary.</p>
<dt><i>backlog-newfile-period</i></p>
<dd>This key requires a positive integer value and defaults to <tt>600</tt>. It specifies how many seconds elapse before each check for externally generated backlog files that are to be picked up and processed.</p>
<dt><i>backlog-rotate-period</i></p>
<dd>This key requires a positive integer value and defaults to <tt>60</tt>. It specifies how many seconds elapse before <code>innfeed</code> checks for a manually created backlog file and moves the output backlog file to the input backlog file.</p>
<dt><i>dns-retry</i></p>
<dd>This key requires a positive integer value and defaults to <tt>900</tt>. It defines the number of seconds between attempts to re-lookup host information that previously failed to be resolved.</p>
<dt><i>dns-expire</i></p>
<dd>This key requires a positive integer value and defaults to <tt>86400</tt>. It defines the number of seconds between refreshes of name to address <font SIZE="-1">DNS</font> translation. This is so long-running processes do not get stuck with stale data, should peer <font SIZE="-1">IP</font> addresses change.</p>
<dt><i>gen-html</i></p>
<dd>This key requires a boolean value and defaults to false. It specifies whether the <i>status-file</i> should be HTML-ified.</p>
<dt><i>status-file</i></p>
<dd>This key requires a pathname value and defaults to <i>innfeed.status</i>. An absolute pathname can be used. It specifies the pathname (relative to <i>pathhttp</i> when <i>gen-html</i> is true; otherwise, <i>pathlog</i> as set in <i>inn.conf</i>) where the periodic status of the <code>innfeed</code> process should be stored. This corresponds to the <code>-S</code> command-line option.</p>
<dt><i>connection-stats</i></p>
<dd>This key requires a boolean value and defaults to false. If the value is true, then whenever the transmission statistics for a peer are logged, each active connection logs its own statistics. This corresponds to the <code>-z</code> command-line option.</p>
<dt><i>host-queue-highwater</i></p>
<dd>This key requires a positive integer value and defaults to <tt>10</tt>. It defines how many articles will be held internally for a peer before new arrivals cause article information to be spooled to the backlog file.</p>
<dt><i>stats-period</i></p>
<dd>This key requires a positive integer value and defaults to <tt>600</tt>. It defines how many seconds <code>innfeed</code> waits between generating statistics on transfer rates.</p>
<dt><i>stats-reset</i></p>
<dd>This key requires a positive integer value and defaults to <tt>43200</tt>. It defines how many seconds <code>innfeed</code> waits before resetting all internal transfer counters back to zero (after logging one final time). This is so a <code>innfeed</code> process running more than a day will generate &#8220;final&#8221; stats that will be picked up by logfile processing scripts.</p>
<dt><i>initial-reconnect-time</i></p>
<dd>This key requires a positive integer value and defaults to <tt>30</tt>. It defines how many seconds to first wait before retrying to reconnect after a connection failure. If the next attempt fails too, then the reconnect time is approximately doubled until the connection succeeds, or <i>max-reconnect-time</i> is reached.</p>
<dt><i>max-reconnect-time</i></p>
<dd>This key requires an integer value and defaults to <tt>3600</tt>. It defines the maximum number of seconds to wait between attempt to reconnect to a peer. The initial value for reconnection attempts is defined by <i>initial-reconnect-time</i>, and it is doubled after each failure, up to this value.</p>
<dt><i>stdio-fdmax</i></p>
<dd>This key requires a non-negative integer value and defaults to <tt>0</tt>. If the value is greater than zero, then whenever a network socket file descriptor is created and it has a value <i>less than</i> this, the file descriptor will be dup&#8217;ed to bring the value up greater than this. This is to leave lower numbered file descriptors free for stdio. Certain systems, Sun&#8217;s in particular, require this. SunOS 4.1.x usually requires a value of 128 and Solaris requires a value of 256. The default if this is not specified, is <tt>0</tt>.</dl>
<h3>Special keys for <code>imapfeed</code></h3>
<p>The following keys are used with <code>imapfeed</code> to authenticate to a remote host. Several parameters may be included at global scope:</p>
<dl>
<dt><i>deliver-authname</i></p>
<dd>The authname is who you want to authenticate as.</p>
<dt><i>deliver-password</i></p>
<dd>This is the appropriate password for authname.</p>
<dt><i>deliver-username</i></p>
<dd>The username is who you want to &#8220;act&#8221; as, that is, who is actually going to be using the server.</p>
<dt><i>deliver-realm</i></p>
<dd>In this case, the &#8220;realm&#8221; is the realm in which the specified authname is valid. Currently this is only needed by the <font SIZE="-1">DIGEST-MD5</font> <font SIZE="-1">SASL</font> mechanism.</p>
<dt><i>deliver-rcpt-to</i></p>
<dd>A <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format string for creating the envelope recipient address. The pattern <font SIZE="-1">MUST</font> include a single string specifier which will be replaced with the newgroup (e.g. <tt>&quot;bb+%s&quot;</tt>). The default is <tt>&quot;+%s&quot;</tt>.</p>
<dt><i>deliver-to-header</i></p>
<dd>An optional <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3)-style format string for creating a To: header field to be prepended to the article. The pattern <font SIZE="-1">MUST</font> include a single string specifier which will be replaced with the newgroup (e.g. <tt>&quot;post+%s [at] domain&quot;</tt>). If not specified, the To: header field will not be prepended.</dl>
<h2>Global Peer Defaults</h2>
<p>All the <i>key</i>:<i>value</i> pairs mentioned in this section can be specified at global scope. They may also be specified inside a group or peer definition. Note that when peers are added dynamically (i.e. when <code>innfeed</code> receives an article for an unspecified peer), it will add the peer site using the parameters specified at global scope.</p>
<h3>Required keys</h3>
<p>No keys are currently required. They all have a default value, if not present in the configuration file.</p>
<h3>Optional keys</h3>
<p>The following keys are optional:</p>
<dl>
<dt><i>article-timeout</i></p>
<dd>This key requires a non-negative integer value. The default value is <tt>600</tt>. If no articles need to be sent to the peer for this many seconds, then the peer is considered idle and all its active connections are torn down.</p>
<dt><i>response-timeout</i></p>
<dd>This key requires a non-negative integer value. The default value is <tt>300</tt>. It defines the maximum amount of time to wait for a response from the peer after issuing a command.</p>
<dt><i>initial-connections</i></p>
<dd>This key requires a non-negative integer value. The default value is <tt>1</tt>. It defines the number of connections to be opened immediately when setting up a peer binding. A value of <tt>0</tt> means no connections will be created until an article needs to be sent.</p>
<dt><i>max-connections</i></p>
<dd>This key requires a positive integer value. The default value is <tt>2</tt> but may be increased if needed or for large feeds. It defines the maximum number of connections to run in parallel to the peer. A value of <tt>0</tt> specifies an unlimited number of maximum connections. In general, use of an unlimited number of maximum connections is not recommended. Do not ever set <i>max-connections</i> to zero with <i>dynamic-method</i> 0 set, as this will saturate peer hosts with connections.</p>
<dt><i>close-period</i></p>
<dd>This key requires a positive integer value and defaults to <tt>86400</tt>. It is the maximum number of seconds a connection should be kept open. Some <font SIZE="-1">NNTP</font> servers do not deal well with connections being held open for long periods.</p>
<dt><i>dynamic-method</i></p>
<dd>This key requires an integer value between 0 and 3. The default value is <tt>3</tt>. It controls how connections are opened, up to the maximum specified by <i>max-connections</i>. In general (and specifically, with <i>dynamic-method</i> 0), a new connection is opened when the current number of connections is below <i>max-connections</i>, and an article is to be sent while no current connections are idle. Without further restraint (i.e. using <i>dynamic-method</i> 0), in practice this means that <i>max-connections</i> connections are established while articles are being sent. Use of other <i>dynamic-method</i> settings imposes a further limit on the amount of connections opened below that specified by <i>max-connections</i>. This limit is calculated in different ways, depending of the value of <i>dynamic-method</i>. </p>
<p> Users should note that adding additional connections is not always productive &#8212; just because opening twice as many connections results in a small percentage increase of articles accepted by the remote peer, this may be at considerable resource cost both locally and at the remote site, whereas the remote site might well have received the extra articles sent from another peer a fraction of a second later. Opening large numbers of connections is considered antisocial. </p>
<p> The meanings of the various settings are:</p>
<dl>
<dd>
<dl>
<dt><code>0</code> (no method)</p>
<dd>Increase of connections up to <i>max-connections</i> is unrestrained.</p>
<dt><code>1</code> (maximize articles per second)</p>
<dd>Connections are increased (up to <i>max-connections</i>) and decreased so as to maximize the number of articles per second sent, while using the fewest connections to do this.</p>
<dt><code>2</code> (set target queue length)</p>
<dd>Connections are increased (up to <i>max-connections</i>) and decreased so as to keep the queue of articles to be sent within the bounds set by <i>dynamic-backlog-low</i> and <i>dynamic-backlog-high</i>, while using the minimum resources possible. As the queue will tend to fill if the site is not keeping up, this method ensures that the maximum number of articles are offered to the peer while using the minimum number of connections to achieve this.</p>
<dt><code>3</code> (combination)</p>
<dd>This method uses a combination of methods 1 and 2 above. For sites accepting a large percentage of articles, method 2 will be used to ensure these sites are offered as complete a feed as possible. For sites accepting a small percentage of articles, method 1 is used, to minimize remote resource usage. For intermediate sites, an appropriate combination is used.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>dynamic-backlog-low</i></p>
<dd>This key requires a floating-point value between 0 and 100. It represents (as a percentage) the low water mark for the host queue. If the host queue falls below this level while using <i>dynamic-method</i> 2 or 3, and if 2 or more connections are open, <code>innfeed</code> will attempt to drop connections to the host. An Infinite Impulse Response (<font SIZE="-1">IIR</font>) filter is applied to the value to prevent connection flap (see <i>dynamic-filter</i>). The default value is <tt>20.0</tt>. This value must be smaller than <i>dynamic-backlog-high</i>.</p>
<dt><i>dynamic-backlog-high</i></p>
<dd>This key requires a floating-point value between 0 and 100. It represents (as a percentage) the high water mark for the host queue. If the host queue rises above this level while using <i>dynamic-method</i> 2 or 3, and if less than <i>max-connections</i> are open to the host, <code>innfeed</code> will attempt to open further connections to the host. An Infinite Impulse Response (<font SIZE="-1">IIR</font>) filter is applied to the value to prevent connection flap (see <i>dynamic-filter</i>). The default value is <tt>50.0</tt>. This value must be larger than <i>dynamic-backlog-low</i>.</p>
<dt><i>dynamic-backlog-filter</i></p>
<dd>This key requires a floating-point value between 0 and 1. It represents the filter coefficient used by the Infinite Impulse Response (<font SIZE="-1">IIR</font>) filter used to implement <i>dynamic-method</i> 2 and 3. The default value of this filter is <tt>0.7</tt>, giving a time constant of 1/(1-0.7) articles. Higher values will result in slower response to queue fullness changes; lower values in faster response.</p>
<dt><i>max-queue-size</i></p>
<dd>This key requires a positive integer value. The default value is <tt>5</tt>. It defines the maximum number of articles to process at one time when using streaming to transmit to a peer. Larger numbers mean more memory consumed as articles usually get pulled into memory (see the description of <i>use-mmap</i>).</p>
<dt><i>streaming</i></p>
<dd>This key requires a boolean value. Its default value is true. It defines whether streaming commands are used to transmit articles to the peers.</p>
<dt><i>no-check-high</i></p>
<dd>This key requires a floating-point number which must be in the range [0.0, 100.0]. When running transmitting with the streaming commands, <code>innfeed</code> attempts an optimization called &#8220;no-CHECK mode&#8221;. This involves <i>not</i> asking the peer if it wants the article, but just sending it. This optimization occurs when the percentage of the articles the peer has accepted gets larger than this number. If this value is set to <tt>100.0</tt>, then this effectively turns off no-CHECK mode, as the percentage can never get above 100.0. If this value is too small, then the number of articles the peer rejects will get bigger (and your bandwidth will be wasted). The default value of <tt>95.0</tt> usually works pretty well.</p>
<dt><i>no-check-low</i></p>
<dd>This key requires a floating-point number which must be in the range [0.0, 100.0], and it must be smaller that the value for <i>no-check-high</i>. When running in no-CHECK mode, as described above, if the percentage of articles the remote server accepts drops below this number, then the no-CHECK optimization is turned off until the percentage gets above the <i>no-check-high</i> value again. If there is small difference between this and the <i>no-check-high</i> value (less than about 5.0), then <code>innfeed</code> may frequently go in and out of no-CHECK mode. If the difference is too big, then it will make it harder to get out of no-CHECK mode when necessary (wasting bandwidth). Keeping this to between 5.0 and 10.0 less than <code>no-check-high</code> usually works pretty well. The default value is <tt>90.0</tt>.</p>
<dt><i>no-check-filter</i></p>
<dd>This is a floating-point value representing the time constant, in articles, over which the CHECK/no-CHECK calculations are done. The default value is <tt>50.0</tt>, which will implement an Infinite Impulse Response (<font SIZE="-1">IIR</font>) filter of time constant 50. This roughly equates to making a decision about the mode over the previous 50 articles. A higher number will result in a slower response to changing percentages of articles accepted; a lower number will result in a faster response.</p>
<dt><i>port-number</i></p>
<dd>This key requires a positive integer value. It defines the <font SIZE="-1">TCP/IP</font> port number to use when connecting to the remote. Usually, port number 119 is used, which is the default value.</p>
<dt><i>force-ipv4</i></p>
<dd>This key requires a boolean value. By default, it is set to false. Setting it to true is the same as setting <i>bindaddress6</i> to <tt>&quot;none&quot;</tt> and removing <i>bindaddress</i> from <tt>&quot;none&quot;</tt> if it was set.</p>
<dt><i>drop-deferred</i></p>
<dd>This key requires a boolean value. By default, it is set to false. When set to true, and a peer replies with code 431 or 436 (try again later), <code>innfeed</code> just drops the article and does not try to re-send it. This is useful for some peers that keep on deferring articles for a long time to prevent <code>innfeed</code> from trying to offer the same article over and over again.</p>
<dt><i>min-queue-connection</i></p>
<dd>This key requires a boolean value. By default, it is set to false. When set to true, <code>innfeed</code> will attempt to use a connection with the least queue size (or the first empty connection). If this key is set to true, it is recommended that <i>dynamic-method</i> be set to <tt>0</tt>. This allows for article propagation with the least delay.</p>
<dt><i>no-backlog</i></p>
<dd>This key requires a boolean value. It specifies whether spooling should be enabled (false, the default) or disabled (true). Note that when <i>no-backlog</i> is set, articles reported as spooled are actually silently discarded.</p>
<dt><i>backlog-limit</i></p>
<dd>This key requires a non-negative integer value. If the number is <tt>0</tt> (the default), then backlog files are allowed to grow without bound when the peer is unable to keep up with the article flow. If this number is greater than 0, then it specifies the size (in bytes) the backlog file should get truncated to when the backlog file reaches a certain limit. The limit depends on whether <i>backlog-factor</i> or <i>backlog-limit-highwater</i> is used. </p>
<p> This parameter also applies to the debug file when <i>debug-shrinking</i> is set to true, and has the same effect on this file as the one has on backlog files.</p>
<dt><i>backlog-factor</i></p>
<dd>This key requires a floating-point value, which must be larger than 1.0. It is used in conjunction with the peer key <i>backlog-limit</i>. If <i>backlog-limit</i> has a value greater than zero, then when the backlog file gets larger than the value <i>backlog-limit</i> * <i>backlog-factor</i>, then the backlog file will be truncated to the size <i>backlog-limit</i>. </p>
<p> For example, if <i>backlog-limit</i> has a value of <tt>1000000</tt>, and <i>backlog-factor</i> has a value of <tt>2.0</tt>, then when the backlog file gets to be larger than 2000000 bytes in size, it will be truncated to 1000000 bytes. The front portion of the file is removed, and the trimming happens on line boundaries, so the final size may be a bit less than this number. If <i>backlog-limit-highwater</i> is defined too, then <i>backlog-factor</i> takes precedence. The default value of <i>backlog-factor</i> is <tt>1.1</tt>. </p>
<p> This parameter also applies to the debug file when <i>debug-shrinking</i> is set to true, and has the same effect on this file as the one has on backlog files.</p>
<dt><i>backlog-limit-highwater</i></p>
<dd>This key requires a positive integer value that must be larger than the value for <i>backlog-limit</i>. The default value is <tt>0</tt>. </p>
<p> If the size of the backlog file gets larger than this value (in bytes), then the backlog file will be shrunk down to the size of <i>backlog-limit</i>. If both <i>backlog-factor</i> and <i>backlog-limit-highwater</i> are defined, then the value of <i>backlog-factor</i> is used. </p>
<p> This parameter also applies to the debug file when <i>debug-shrinking</i> is set to true, and has the same effect on this file as the one has on backlog files.</p>
<dt><i>backlog-feed-first</i></p>
<dd>This key requires a boolean value. By default it is set to false. When set to true, the backlog is fed before new files. This is intended to enforce in-order delivery, so setting this to true when <i>initial-connections</i> or <i>max-connections</i> is more than 1 is inconsistent.</p>
<dt><i>bindaddress</i></p>
<dd>This key requires a string value. It specifies which outgoing IPv4 address <code>innfeed</code> should bind the local end of its connection to. It must be an IPv4 address in dotted-quad format (nnn.nnn.nnn.nnn), <tt>&quot;any&quot;</tt>, or <tt>&quot;none&quot;</tt>. If not set or set to <tt>&quot;any&quot;</tt>, <code>innfeed</code> defaults to letting the kernel choose this address. If set to <tt>&quot;none&quot;</tt>, <code>innfeed</code> will not use IPv4 for outgoing connections to peers in this scope (i.e. it forces IPv6). </p>
<p> If not set in <i>innfeed.conf</i>, <code>innfeed</code> defaults to the value of <i>sourceaddress</i> from <i>inn.conf</i> (which by default is unset).</p>
<dt><i>bindaddress6</i></p>
<dd>This key requires a string value. It behaves like <i>bindaddress</i> except for outgoing IPv6 connections. It must be in numeric IPv6 format (note that a value containing colons must be enclosed in double quotes), <tt>&quot;any&quot;</tt>, or <tt>&quot;none&quot;</tt>. If set to <tt>&quot;none&quot;</tt>, <code>innfeed</code> will not use IPv6 for outgoing connections to peers in this scope. </p>
<p> If not set in <i>innfeed.conf</i>, <code>innfeed</code> defaults to the value of <i>sourceaddress6</i> from <i>inn.conf</i> (which by default is unset).</p>
<dt><i>username</i></p>
<dd>This key requires a string value. If the value is defined, then <code>innfeed</code> tries to authenticate by <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">USER</font> and this value used for user name. <i>password</i> must also be defined, if this key is defined.</p>
<dt><i>password</i></p>
<dd>This key requires a string value. The value is the password used for <font SIZE="-1">AUTHINFO</font> <font SIZE="-1">PASS</font>. <i>username</i> must also be defined, if this key is defined.</dl>
<h2>Peer Values</h2>
<p>As previously explained, the peer definitions can contain redefinitions of any of the <i>key</i>:<i>value</i> pairs described in the section about global peer defaults above. There is one <i>key</i>:<i>value</i> pair that is specific to a peer definition.</p>
<dl>
<dt><i>ip-name</i></p>
<dd>This key requires a word value. The word is the host&#8217;s <font SIZE="-1">FQDN</font>, or the dotted quad IP-address. If this value is not specified, then the name of the peer in the enclosing <i>peer</i> block is taken to also be its <i>ip-name</i>.</dl>
<h2>Reloading</h2>
<p>If <code>innfeed</code> gets a <font SIZE="-1">SIGHUP</font> signal, then it will reread the configuration file. All values at global scope except for <i>backlog-directory</i> can be changed (although note that <i>bindaddress</i> and <i>bindaddress6</i> changes will only affect new connections). </p>
<p> Any new peers are added and any missing peers have their connections closed. </p>
<p> The log file is also reopened.</p>
<h2>Example</h2>
<p>For a comprehensive example, see the sample <i>innfeed.conf</i> distributed with <font SIZE="-1">INN</font> and installed as a starting point. </p>
<p> Here are examples of how to format values: </p>
<pre> eg-string: &quot;New	config	file
&quot;
 eg-long-string: &quot;A long string that goes
 over multiple lines. The
 newline is kept in the
 string except when quoted
 with a backslash \
 as here.&quot;
 eg-simple-string: A-no-quote-string
 eg-integer: 10
 eg-boolean: true
 eg-char: 'a'
 eg-ctrl-g: ''</pre>
<h2>History</h2>
<p>Written by James Brister &lt;brister [at] vix.com&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> Earlier versions of <code>innfeed</code> (up to 0.10.1) were shipped separately; <code>innfeed</code> is now part of <font SIZE="-1">INN</font> and shares the same version number. Please note that the <i>innfeed.conf</i> format has changed dramatically since version 0.9.3. </p>
<p> <tt>$Id:</tt> innfeed.conf.pod 9479 2013-06-03 18:12:39Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innfeed/">innfeed</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). </p>
