---
title: "innfeed(5)"
name: "innfeed"
section: "5"
letter: "i"
url: "/docs/linux/man/5-innfeed/"
description: "innfeed.conf – configuration file for innfeed"
---

<p>innfeed.conf &#8211; configuration file for innfeed</p>
<h2>Description</h2>
<p>This man page describes the configuration file for version 1.0 of innfeed. This format has changed dramatically since version 0.9.3. </p>
<p> The file <code>innfeed.conf</code> is used to control the <a href="/docs/linux/man/1-innfeed/">innfeed</a>(1) program. It is a fairly free-format file that consists of three types of entries: <i>key/value</i>, <i>peer</i> and <i>group</i>. Comments are from the hash character &#8220;#&#8221; to the end of the line. </p>
<p> <i>Key/value</i> entries are a keyword and a value separated by a colon (which can itself be surrounded by whitespace). For example: </p>
<dl>
<dd>
<pre>max-connections: 10</pre>
</dl>
<p> A legal key starts with a letter and contains only letters, digits, and &#8220;_&#8221;, &#8220;-&#8221;. </p>
<p> There are 5 different type of values: integers, floating-point numbers, characters, booleans, and strings. Integer and floating point numbers are as to be expected except that exponents in floating point numbers are not supported. A boolean value is either &#8220;true&#8221; or &#8220;false&#8221; (case is not significant). A character value is a single-quoted character as defined by the C-language. A string value is any other sequence of characters. If the string needs to contain whitespace, then it must be quoted with double quotes, and uses the same format for embedding non-printing characters as normal C-language string. </p>
<p> Peer entries look like: </p>
<dl>
<dd>
<pre>peer &lt;name&gt; {
 # body ...
}</pre>
</dl>
<p> The word &#8220;peer&#8221; is required. The &#8220;&lt;name&gt;&#8221; is the same as the site name in INN&#8217;s newsfeeds file. The body of a peer entry contains some number (possibly zero) of key/value entries. </p>
<p> Group entries look like: </p>
<dl>
<dd>
<pre>group &lt;name&gt; {
 # body 
}</pre>
</dl>
<p> The word &#8220;group&#8221; is required. The &#8220;&lt;name&gt;&#8221; is any string valid as a key. The body of a group entry contains any number of the three types of entries. So key/value pairs can be defined inside a group, and peers can be nested inside a group, and other groups can be nested inside a group. </p>
<p> Key/value entries that are defined outside of all peer and group entries are said to be at &#8220;global scope&#8221;. There are global key/value entries that apply to the process as a whole (for example the location of the backlog file directory), and there are global key/value entries that act as defaults for peers. When innfeed looks for a specific value in a peer entry (for example, the maximum number of connections to set up), if the value is not defined in the peer entry, then the enclosing groups are examined for the entry (starting at the closest enclosing group). If there are no enclosing groups, or the enclosing groups don&#8217;t define the key/value, then the value at global scope is used. </p>
<p> A small example could be: </p>
<dl>
<dd>
<pre># Global value applied to all peers that have 
# no value of their own.
max-connections: 5
# A peer definition. ``uunet'' is the name used by innd in 
# the newsfeeds file.
peer uunet {
 ip-name: usenet1.uu.net
}
peer vixie {
 ip-name: gw.home.vix.com
 max-connections: 10 # override global value.
}
# A group of two peers who can handle more connections 
# than normal
group fast-sites {
 max-connections: 15
 # Another peer. The ``max-connections'' value from the
 # ``fast-sites'' group scope is used. The ``ip-name'' value
 # defaults to the peer's name.
 peer data.ramona.vix.com { 
 }
 peer bb.home.vix.com {
 max-connections: 20 # he can really cook.
 }
}</pre>
</dl>
<p> Given the above configuration file, the defined peers would have the following values for the &#8220;max-connections&#8221; key. </p>
<dl>
<dd>
<pre>uunet 5
vixie 10
data.ramona.vix.com 15
bb.home.vix.com 20</pre>
</dl>
<p> Innfeed ignores key/value pairs it is not interested in. Some config file values can be set via a command line option, in which case that setting overrides the settings in the file. </p>
<p> Config files can be included in other config files via the syntax: </p>
<pre><dl><dt><dd>$INCLUDE filename
</dl></pre>
<p>There is a maximum nesting depth of 10. </p>
<p> For a fuller example config file, see the supplied <i>innfeed.conf</i>.</p>
<h2>Global Values</h2>
<p>The following listing show all the keys that apply to the process as whole. These are not required (compiled-in defaults are used where needed).</p>
<dl>
<dt><code>news-spool</code></p>
<dd>This key requires a pathname value. It specifies where the top of the article spool is. This corresponds to the &#8220;<i>-a</i>&#8221; command-line option.</p>
<dt><code>input-file</code></p>
<dd>This key requires a pathname value. It specifies the pathname (relative to the <code>backlog-directory</code>) that should be read in funnel-file mode. This corresponds to giving a filename as an argument on the command-line (i.e. its presence also implies that funnel-file mode should be used).</p>
<dt><code>pid-file</code></p>
<dd>This key requires a pathname value. It specifies the pathname (relative to the <code>backlog-directory</code>) where the pid of the innfeed process should be stored. This corresponds to the &#8220;<i>-p</i>&#8221; command-line option.</p>
<dt><code>debug-level</code></p>
<dd>This key defines the debug level for the process. A non-zero number generates a lot of messages to stderr, or to the config-defined &#8220;log-file&#8221;. This corresponds to the &#8220;<i>-d</i>&#8221; command-line option.</p>
<dt><code>use-mmap</code></p>
<dd>This key requires a boolean value. It specifies whether mmaping should be used if innfeed has been built with mmap support. If article data on disk is not in NNTP-ready format (CR/LF at the end of each line), then after mmaping the article is read into memory and fixed up, so mmaping has no positive effect (and possibly some negative effect depending on your system), and so in such a case this value should be <i>false</i>. This corresponds to the &#8220;<i>-M</i>&#8221; command-line option.</p>
<dt><code>log-file</code></p>
<dd>This key requires a pathname value. It specifies where any logging messages that couldn&#8217;t be sent via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) should go (such as those generated when a positive value for &#8220;<code>debug-value</code>&#8221;, is used). This corresponds to the &#8220;<i>-l</i>&#8221; command-line option. A relative pathname is relative to the &#8220;<code>backlog-directory</code>&#8221; value.</p>
<dt><code>log-time-format</code></p>
<dd>This key requires a format string suitable for <a href="/docs/linux/man/3-strftime/">strftime</a>(3). It is used for messages sent via <a href="/docs/linux/man/3-syslog/">syslog</a>(3) and to the <code>status-file</code>. Default value is &quot;%a %b %d %H:%M:%S %Y&quot;.</p>
<dt><code>backlog-directory</code></p>
<dd>This key requires a pathname value. It specifies where the current innfeed process should store backlog files. This corresponds to the &#8220;<i>-b</i>&#8221; command-line option.</p>
<dt><code>backlog-highwater</code></p>
<dd>This key requires a positive integer value. It specifies how many articles should be kept on the backlog file queue before starting to write new entries to disk.</p>
<dt><code>backlog-ckpt-period</code></p>
<dd>This key requires a positive integer value. It specifies how many seconds between checkpoints of the input backlog file. Too small a number will mean frequent disk accesses, too large a number will mean after a crash innfeed will re-offer more already-processed articles than necessary.</p>
<dt><code>backlog-newfile-period</code></p>
<dd>This key requires a positive integer value. It specifies how many seconds before each checks for externally generated backlog files that are to be picked up and processed.</p>
<dt><code>backlog-rotate-period</code></p>
<dd>This key requires a positive integer value. It specifies how many seconds elapse before <code>innfeed</code> checks for a manually created backlog file and moves the output backlog file to the input backlog file.</p>
<dt><code>dns-retry</code></p>
<dd>This key requires a positive integer value. It defines the number of seconds between attempts to re-lookup host information that previous failed to be resolved.</p>
<dt><code>dns-expire</code></p>
<dd>This key requires a positive integer value. It defines the number of seconds between refreshes of name to address DNS translation. This is so long-running processes don&#8217;t get stuck with stale data, should peer ip addresses change.</p>
<dt><code>close-period</code></p>
<dd>This key requires a positive integer value. It is the maximum number of seconds a connection should be kept open. Some NNTP servers don&#8217;t deal well with connections being held open for long periods.</p>
<dt><code>gen-html</code></p>
<dd>This key requires a boolean value. It specifies whether the <code>status-file</code> should be HTML-ified.</p>
<dt><code>status-file</code></p>
<dd>This key requires a pathname value. It specifies the pathname (relative to the <code>backlog-directory</code>) where the periodic status of the innfeed process should be stored. This corresponds to the &#8220;<i>-S</i>&#8221; command-line option.</p>
<dt><code>connection-stats</code></p>
<dd>This key requires a boolean value. If the value is true, then whenever the transmission statistics for a peer are logged, then each active connection logs its own statistics. This corresponds to the &#8220;<i>-z</i>&#8221; command-line option.</p>
<dt><code>host-queue-highwater</code></p>
<dd>This key requires a positive integer value. It defines how many articles will be held internally for a peer before new arrivals cause article information to be spooled to the backlog file.</p>
<dt><code>stats-period</code></p>
<dd>This key requires a positive integer value. It defines how many seconds innfeed waits between generating statistics on transfer rates.</p>
<dt><code>stats-reset</code></p>
<dd>This key requires a positive integer value. It defines how many seconds innfeed waits before resetting all internal transfer counters back to zero (after logging one final time). This is so a innfeed-process running more than a day will generate &#8220;final&#8221; stats that will be picked up by logfile processing scripts.</p>
<dt><code>initial-reconnect-time</code></p>
<dd>This key requires a positive integer value. It defines how many seconds to first wait before retrying to reconnect after a connection failure. If the next attempt fails too, then the reconnect time is approximately doubled until the connection succeeds, or <code>max-reconnection-time</code> is reached.</p>
<dt><code>max-reconnect-time</code></p>
<dd>This key requires an integer value. It defines the maximum number of seconds to wait between attempt to reconnect to a peer. The initial value for reconnection attempts is defined by <code>initial-reconnect-time</code>, and it is doubled after each failure, up to this value.</p>
<dt><code>stdio-fdmax</code></p>
<dd>This key requires a non-negative integer value. If the value is greater than zero, then whenever a network socket file descriptor is created and it has a value <i>less than</i> this, the file descriptor will be dup&#8217;ed to bring the value up greater than this. This is to leave lower numbered file descriptors free for stdio. Certain systems, Sun&#8217;s in particular, require this. SunOS 4.1.x usually requires a value of 128 and Solaris requires a value of 256. The default if this is not specified, is 0.</dl>
<h2>Global Peer Defaults</h2>
<p>All the key/value pairs mentioned in this section must be specified at global scope. They may also be specified inside a group or peer definition. Note that when peers are added dynamically (i.e. when innfeed receives an article for an unspecified peer), it will add the peer site using the parameters specified at global scope.</p>
<dl>
<dt><code>article-timeout</code></p>
<dd>This key requires a non-negative integer value. If no articles need to be sent to the peer for this many seconds, then the peer is considered idle and all its active connections are torn down.</p>
<dt><code>response-timeout</code></p>
<dd>This key requires a non-negative integer value. It defines the maximum amount of time to wait for a response from the peer after issuing a command.</p>
<dt><code>initial-connections</code></p>
<dd>This key requires a non-negative integer value. It defines the number of connections to be opened immediately when setting up a peer binding. A value of 0 means no connections will be created until an article needs to be sent.</p>
<dt><code>max-connections</code></p>
<dd>This key requires positive integer value. It defines the maximum number of connections to run in parallel to the peer. A value of zero specifies an unlimited number of maximum connections. In general use of an unlimited number of maximum connections is not recommended. Do not ever set <code>max-connections</code> to zero with <code>dynamic-method</code> 0 set, as this will saturate peer hosts with connections. [ Note that in previous versions of innfeed, a value of 1 had a special meaning. This is no longer the case, 1 means a maximum of 1 connection ].</p>
<dt><code>dynamic-method</code></p>
<dd>This key requires an integer value between 0 and 3. It controls how connections (up to max-connections) are opened, up to the maximum specified by <code>max-connections</code>. In general (and specifically, with <code>dynamic-method</code> 0), a new connection is opened when the current number of connections is below <code>max-connections</code>, and an article is to be sent while no current connections are idle. Without further restraint (i.e. using <code>dynamic-method</code> 0), in practice this means that <code>max-connections</code> connections are established while articles are being sent. Use of other <code>dynamic-method</code> settings imposes a further limit on the amount of connections opened below that specified by <code>max-connections</code>. This limit is calculated in different ways, depending of the value of <code>dynamic-method</code>. Users should note that adding additional connections is not always productive &#8211; just because opening twice as many connections results in a small percentage increase of articles accepted by the remote peer, this may be at considerable resource cost both locally and at the remote site, whereas the remote site might well have received the extra articles sent from another peer a fraction of a second later. Opening large numbers of connections is considered antisocial. The meanings of the various settings are:</p>
<dl>
<dd>
<dl>
<dt><code>0 no method</code></p>
<dd>Increase of connections up to <code>max-connections</code> is unrestrained.</p>
<dt><code>1 maximize articles per second</code></p>
<dd>Connections are increased (up to <code>max-connections</code>) and decreased so as to maximize the number of articles per second sent, while using the fewest connections to do this.</p>
<dt><code>2 set target queue length</code></p>
<dd>Connections are increased (up to <code>max-connections</code>) and decreased so as to keep the queue of articles to be sent within the bounds set by <code>dynamic-backlog-low</code> and <code>dynamic-backlog-high</code>, while using the minimum resources possible. As the queue will tend to fill if the site is not keeping up, this method ensures that the maximum number of articles are offered to the peer while using the minimum number of connections to achieve this.</p>
<dt><code>3 combination</code></p>
<dd>This method uses a combination of methods 1 and 2 above. For sites accepting a large percentage of articles, method 2 will be used to ensure these sites are offered as complete a feed as possible. For sites accepting a small percentage of articles, method 1 is used, to minimize remote resource usage. For intermediate sites, an appropriate combination is used.</dl>
</dl>
<dt><code>dynamic-backlog-low</code></p>
<dd>This key requires an integer value between 0 and 100. It represents (as a percentage) the low water mark for the host queue. If the host queue falls below this level while using <code>dynamic-method</code> 2 or 3, and if 2 or more connections are open, innfeed will attempt to drop connections to the host. An IIR filter is applied to the value to prevent connection flap (see <code>dynamic-filter</code>). A value of 25.0 is recommended. This value must be smaller than <code>dynamic-backlog-high</code>.</p>
<dt><code>dynamic-backlog-high</code></p>
<dd>This key requries an integer value between 0 and 100. It represents (as a percentage) the high water mark for the host queue. If the host queue rises above this level while using <code>dynamic-method</code> 2 or 3, and if less than <code>max-connections</code> are open to the host, innfeed will attempt to open further connections to the host. An IIR filter is applied to the value to prevent connection flap (see <code>dynamic-filter</code>). A value of 50.0 is recommended. This value must be larger than <code>dynamic-backlog-low</code>.</p>
<dt><code>dynamic-backlog-filter</code></p>
<dd>This key requires a floating-point value between 0 and 1. It represents the filter coefficient used by the IIR filter used to implement <code>dynamic-method</code> 2 and 3. The recommended value of this filter is 0.7, giving a time constant of 1/(1-0.7) articles. Higher values will result in slower response to queue fullness changes, lower values in faster response.</p>
<dt><code>max-queue-size</code></p>
<dd>This key requires a positive integer value. It defines the maximum number of articles to process at one time when using streaming to transmit to a peer. Larger numbers mean more memory consumed as articles usually get pulled into memory (see the description of <code>use-mmap</code>).</p>
<dt><code>streaming</code></p>
<dd>This key requires a boolean value. It defines whether streaming commands are used to transmit articles to the peers.</p>
<dt><code>no-check-high</code></p>
<dd>This key requires a floating-point number which must be in the range [0.0, 100.0]. When running transmitting with the streaming commands, innfeed attempts an optimization called &#8220;no-CHECK&#8221; mode. This involves <i>not</i> asking the peer if it wants the article, but just sending it. This optimization occurs when the percentage of the articles the peer has accepted gets larger than this number. If this value is set to 100.0, then this effectively turns off no-CHECK mode, as the percentage can never get above 100.0. If this value is too small, then the number of articles the peer rejects will get bigger (and your bandwidth will be wasted). A value of 95.0 usually works pretty well. NOTE: In innfeed 0.9.3 and earlier this value was in the range [0.0, 9.0].</p>
<dt><code>no-check-low:</code></p>
<dd>This key requires a floating-point number which must be in the range [0.0, 100.0), and it must be smaller that the value for <code>no-check-high</code>. When running in no-CHECK mode, as described above, if the percentage of articles the remote accepts drops below this number, then the no-CHECK optimization is turned off until the percentage gets above the <code>no-check-high</code> value again. If there is small difference between this and the <code>no-check-high</code> value (less than about 5.0), then innfeed may frequently go in and out of no-CHECK mode. If the difference is too big, then it will make it harder to get out of no-CHECK mode when necessary (wasting bandwidth). Keeping this to between 5.0 and 10.0 less than <code>no-check-high</code> usually works pretty well.</p>
<dt><code>no-check-filter</code></p>
<dd>This is a floating point value representing the time constant, in articles, over which the CHECK / no-CHECK calculations are done. The recommended value is 50.0 which will implement an IIR filter of time constant 50. This roughly equates to making a decision about the mode over the previous 50 articles. A higher number will result in a slower response to changing percentages of articles accepted; a lower number will result in a faster response.</p>
<dt><code>bindaddress</code></p>
<dd>This key requires a string value. It specifies which outgoing IPv4 address innfeed should bind the local end of its connection to. Must be an IPv4 address in dotted-quad format (nnn.nnn.nnn.nnn), &quot;any&quot;, or &quot;none&quot;. If not set or set to &quot;any&quot;, innfeed defaults to letting the kernel choose this address. If set to &quot;none&quot;, innfeed will not use IPv4 for outgoing connections to peers in this scope (i.e. it forces IPv6). If not set in innfeed.conf, innfeed defaults to the value of <code>sourceaddress</code> from <a href="/docs/linux/man/5-inn-conf/">inn.conf</a>(5) (which by default is unset).</p>
<dt><code>bindaddress6</code></p>
<dd>This key requires a string value. It behaves like <code>bindaddress</code> except for outgoing IPv6 connections. Must be in numeric IPv6 format (note that a value containing colons must be enclosed in double quotes), &quot;any&quot;, or &quot;none&quot;. If set to &quot;none&quot;, innfeed will not use IPv6 for outgoing connections to peers in this scope. If not set in innfeed.conf, innfeed defaults to the value of <code>sourceaddress6</code> from <a href="/docs/linux/man/5-inn-conf/">inn.conf</a>(5) (which by default is unset).</p>
<dt><code>port-number</code></p>
<dd>This key requires a positive integer value. It defines the tcp/ip port number to use when connecting to the remote.</p>
<dt><code>force-ipv4</code></p>
<dd>This key requires a boolean value. By default it is set to false. Setting it to true is the same as setting &quot;bindaddress6: none&quot; and removing &quot;bindaddress: none&quot; if it was set.</p>
<dt><code>drop-deferred</code></p>
<dd>This key requires a boolean value. By default it is set to false. When set to true, and a peer replies with code 431 or 436 (try again later) just drop the article and don&#8217;t try to re-send it. This is useful for some peers that keep on deferring articles for a long time to prevent innfeed from trying to offer the same article over and over again.</p>
<dt><code>min-queue-connection</code></p>
<dd>This key requires a boolean value. By default it is set to false. When set to true, innfeed will attempt to use a connection with the least queue size (or the first empty connection). If this key is set to true, it is recommended that <code>dynamic-method</code> be set to 0. This allows for article propagation with the least delay.</p>
<dt><code>no-backlog</code></p>
<dd>This key requires a boolean value. It specifies whether spooling should be enabled (false, the default) or disabled (true). Note that when no-backlog is set, articles reported as &quot;spooled&quot; are actually silently discarded.</p>
<dt><code>backlog-limit</code></p>
<dd>This key requires a non-negative integer value. If the number is 0 then backlog files are allowed to grown without bound when the peer is unable to keep up with the article flow. If this number is greater than 0 then it specifies the size (in bytes) the backlog file should get truncated to when the backlog file reaches a certain limit. The limit depends on whether <code>backlog-factor</code> or <code>backlog-limit-highwater</code> is used.</p>
<dt><code>backlog-factor</code></p>
<dd>This key requires a floating point value, which must be larger than 1.0. It is used in conjunction with the peer key <code>backlog-limit</code>. If <code>backlog-limit</code> has a value greater than zero, then when the backlog file gets larger than the value <code>backlog-limit * backlog-factor</code>, then the backlog file will be truncated to the size <code>backlog-limit</code>. For example if <code>backlog-limit</code> has a value of 1000000, and <code>backlog-factor</code> has a value of 2.0, then when the backlogfile gets to be larger than 2000000 bytes in size, it will be truncated to 1000000 bytes. The front portion of the file is removed, and the trimming happens on line boundaries, so the final size may be a bit less than this number. If <code>backlog-limit-highwater</code> is defined too, then <code>backlog-factor</code> takes precedence.</p>
<dt><code>backlog-limit-highwater</code></p>
<dd>This key requires a positive integer value that must be larger than the value for <code>backlog-limit</code>. If the size of the backlog file gets larger than this value (in bytes), then the backlog file will be shrunk down to the size of <code>backlog-limit</code>. If both <code>backlog-factor</code> and <code>backlog-limit-highwater</code> are defined, then the value of <code>backlog-factor</code> is used.</p>
<dt><code>backlog-feed-first</code></p>
<dd>This key requires a boolean value. By default it is set to false. When set to true, the backlog is fed before new files. This is intended to enforce in-order delivery, so setting this to true when initial-connections or max-connections is more than 1 is inconsistent.</p>
<dt><code>username</code></p>
<dd>This key requires a string value. If the value is defined, then innfeed tries to authenticate by &#8220;AUTHINFO USER&#8221; and this value used for user name. <code>password</code> must also be defined, if this key is defined.</p>
<dt><code>password</code></p>
<dd>This key requires a string value. The value is the password used for &#8220;AUTHINFO PASS&#8221;. <code>username</code> must also be defined, if this key is defined.</p>
<dt><code>deliver</code></p>
<dd>This key is used with imapfeed to authenticate to a remote host. It is optional. There are several parameters that must be included with deliver:</p>
<dl>
<dd>
<dl>
<dt><code>deliver-authname</code></p>
<dd>The authname is who you want to authenticate as.</p>
<dt><code>deliver-password</code></p>
<dd>This is the appropriate password for authname.</p>
<dt><code>deliver-username</code></p>
<dd>The username is who you want to &quot;act&quot; as, that is, who is actually going to be using the server.</p>
<dt><code>deliver-realm</code></p>
<dd>In this case, the &quot;realm&quot; is the realm in which the specified authname is valid. Currently this is only needed by the DIGEST-MD5 SASL mechanism.</p>
<dt><code>deliver-rcpt-to</code></p>
<dd>A printf-style format string for creating the envelope recipient address. The pattern MUST include a single string specifier which will be replaced with the newgroup (e.g &quot;bb+%s&quot;). The default is &quot;+%s&quot;.</p>
<dt><code>deliver-to-header</code></p>
<dd>An optional printf-style format string for creating a To: header to be prepended to the article. The pattern MUST include a single string specifier which will be replaced with the newgroup (e.g &quot;post+%s [at] domain&quot;). If not specified, the To: header will not be prepended.</dl>
</dl>
</dl>
<h2>Peer Values</h2>
<p>As previously explained, the peer definitions can contain redefinitions of any of the key/value pairs described in the <code>GLOBAL PEER DEFAULTS</code> section above. There is one key/value pair that is specific to a peer definition.</p>
<dl>
<dt><code>ip-name</code></p>
<dd>This key requires a word value. The word is the host&#8217;s FQDN, or the dotted quad ip-address. If this value is not specified then the name of the peer is taken to also be its ip-name. See the entry for data.ramona.vix.com in the example below.</dl>
<h2>Reloading</h2>
<p>If innfeed gets a SIGHUP signal, then it will reread the config file. All values at global scope except for &#8220;<code>backlog-directory</code>&#8221; can be changed (although note that &#8220;<code>bindaddress</code>&#8221; and &#8220;<code>bindaddress6</code>&#8221; changes will only affect new connections). Any new peers are added and any missing peers have their connections closed.</p>
<h2>Example</h2>
<p>Below is the sample innfeed.conf file.</p>
<dl>
<dd>
<pre>#
# innfeed.conf file. See the comment block at the
# end for a fuller description.
#
##
## Global values. Not specific to any peer. These
## are optional, but if used will override the
## compiled in values. Command-line options used
## will override these values.
##
pid-file: innfeed.pid
debug-level: 0
use-mmap: false
log-file: innfeed.log
stdio-fdmax: 0
backlog-directory: innfeed
backlog-rotate-period: 60
backlog-ckpt-period: 30
backlog-newfile-period: 600
dns-retry: 900
dns-expire: 86400
close-period: 3600
gen-html: false
status-file: innfeed.status
connection-stats: false
host-queue-highwater: 200
stats-period: 600
stats-reset: 43200
max-reconnect-time: 3600
initial-reconnect-time: 30
##
## Defaults for all peers. These must all exist at
## global scope. Any of them can be redefined
## inside a peer or group definition.
##
article-timeout: 600
response-timeout: 300
initial-connections: 1
max-connections: 5
max-queue-size: 25
streaming: true
no-check-high: 95.0
no-check-low: 90.0
no-check-filter: 50.0
port-number: 119
backlog-limit: 0
backlog-factor: 1.10
backlog-limit-highwater:0
dynamic-method: 3
dynamic-backlog-filter: 0.7
dynamic-backlog-low: 25.0
dynamic-backlog-high: 50.0
no-backlog: false
##
## Peers. 
##
peer decwrl {
 ip-name: news1.pa.dec.com
}
peer uunet {
 ip-name: news.uunet.uu.net
 max-connections: 10
}
peer data.ramona.vix.com {
 # ip-name defaults to data.ramona.vix.com
 streaming: false
}
peer bb.home.vix.com {
 ip-name: 192.5.5.33
}
# Blank lines are ignored. Everything after a '#'
# is ignored too.
#
# Format is:
# key : value
#
# See <a href="//www.systutorials.com/docs/linux/man/5-innfeed.conf/">innfeed.conf</a>(5) for a description of
# necessary &amp; useful keys. Unknown keys and their
# values are ignored.
#
# Values may be a integer, floating-point, c-style
# single-quoted characters, boolean, and strings.
#
# If a string value contains whitespace, or
# embedded quotes, or the comment character
# (``#''), then the whole string must be quoted
# with double quotes. Inside the quotes, you may
# use the standard c-escape sequence
# (	,
,,,,\&quot;,\').
#
# Examples:
# eg-string: &quot;New	Config	file
&quot;
# eg-long-string: &quot;A long string that goes
# over multiple lines. The
# newline is kept in the
# string except when quoted 
# with a backslash \
# as here.&quot;
# eg-simple-string: A-no-quote-string
# eg-integer: 10
# eg-boolean: true
# eg-char: 'a'
# eg-ctrl-g: ''</pre>
</dl>
<h2>History</h2>
<p>Written by James Brister &lt;brister [at] vix.com&gt; for InterNetNews. This is revision 8243, dated 2008-12-21.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-innfeed/">innfeed</a>(1), <a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a>(5) </p>
