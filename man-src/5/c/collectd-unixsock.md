---
title: "collectd-unixsock(5)"
name: "collectd-unixsock"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-unixsock/"
description: "collectd-unixsock – Documentation of collectd’s \"unixsock plugin\""
---

<p>collectd-unixsock &#8211; Documentation of collectd&#8217;s &quot;unixsock plugin&quot;</p>
<h2>Synopsis</h2>
<pre> # See <a href="//www.systutorials.com/docs/linux/man/5-collectd.conf/">collectd.conf</a>(5)
 LoadPlugin unixsock
 # ...
 &lt;Plugin unixsock&gt;
 SocketFile &quot;/path/to/socket&quot;
 SocketGroup &quot;collectd&quot;
 SocketPerms &quot;0770&quot;
 DeleteSocket false
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;unixsock plugin&quot;</tt> opens an UNIX-socket over which one can interact with the daemon. This can be used to use the values collected by collectd in other applications, such as monitoring solutions, or submit externally collected values to collectd. </p>
<p> For example, this plugin is used by <i><a href="/docs/linux/man/1-collectd-nagios/">collectd-nagios</a></i>(1) to check if some value is in a certain range and exit with a Nagios-compatible exit code.</p>
<h2>Commands</h2>
<p>Upon start the <tt>&quot;unixsock plugin&quot;</tt> opens a UNIX-socket and waits for connections. Once a connection is established the client can send commands to the daemon which it will answer, if it understand them. </p>
<p> In general the plugin answers with a status line of the following form: </p>
<p> <i>Status</i> <i>Message</i> </p>
<p> If <i>Status</i> is greater than or equal to zero the message indicates success, if <i>Status</i> is less than zero the message indicates failure. <i>Message</i> is a human-readable string that further describes the return value. </p>
<p> On success, <i>Status</i> furthermore indicates the number of subsequent lines of output (not including the status line). Each such lines usually contains a single return value. See the description of each command for details. </p>
<p> The following commands are implemented:</p>
<dl>
<dt><font SIZE="-1"><code>GETVAL</code></font> <i>Identifier</i></p>
<dd>If the value identified by <i>Identifier</i> (see below) is found the complete value-list is returned. The response is a list of name-value-pairs, each pair on its own line (the number of lines is indicated by the status line &#8211; see above). Each name-value-pair is of the form <i>name</i><code>=</code><i>value</i>. Counter-values are converted to a rate, e. g. bytes per second. Undefined values are returned as <code>NaN</code>. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>|&nbsp;<wbr><font SIZE="-1">GETVAL</font>&nbsp;<wbr>myhost/cpu-0/cpu-user<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 1 Value found<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | value=1.260000e+00</p>
<dt><font SIZE="-1"><code>LISTVAL</code></font></p>
<dd>Returns a list of the values available in the value cache together with the time of the last update, so that querying applications can issue a <font SIZE="-1"><code>GETVAL</code></font> command for the values that have changed. Each return value consists of the update time as an epoch value and the identifier, separated by a space. The update time is the time of the last value, as provided by the collecting instance and may be very different from the time the server considers to be &#8220;now&#8221;. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>|&nbsp;<wbr><font SIZE="-1">LISTVAL<br />
&nbsp;<wbr></font>&nbsp;<wbr>&lt;- | 69 Values found<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 1182204284 myhost/cpu-0/cpu-idle<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 1182204284 myhost/cpu-0/cpu-nice<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 1182204284 myhost/cpu-0/cpu-system<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 1182204284 myhost/cpu-0/cpu-user<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;</p>
<dt><font SIZE="-1"><code>PUTVAL</code></font> <i>Identifier</i> [<i>OptionList</i>] <i>Valuelist</i></p>
<dd>Submits one or more values (identified by <i>Identifier</i>, see below) to the daemon which will dispatch it to all it&#8217;s write-plugins. </p>
<p> An <i>Identifier</i> is of the form <tt>&quot;</tt>host<tt></tt>/<tt></tt>plugin<tt></tt>&#8211;<tt></tt>instance<tt></tt>/<tt></tt>type<tt></tt>&#8211;<tt></tt>instance<tt>&quot;</tt> with both <i>instance</i>-parts being optional. If they&#8217;re omitted the hyphen must be omitted, too. <i>plugin</i> and each <i>instance</i>-part may be chosen freely as long as the tuple (plugin, plugin instance, type instance) uniquely identifies the plugin within collectd. <i>type</i> identifies the type and number of values (i. e. data-set) passed to collectd. A large list of predefined data-sets is available in the <code>types.db</code> file. </p>
<p> The <i>OptionList</i> is an optional list of <i>Options</i>, where each option is a key-value-pair. A list of currently understood options can be found below, all other options will be ignored. Values that contain spaces must be quoted with double quotes. </p>
<p> <i>Valuelist</i> is a colon-separated list of the time and the values, each either an integer if the data-source is a counter, or a double if the data-source is of type &#8220;gauge&#8221;. You can submit an undefined gauge-value by using <code>U</code>. When submitting <code>U</code> to a counter the behavior is undefined. The time is given as epoch (i. e. standard <font SIZE="-1">UNIX</font> time). </p>
<p> You can mix options and values, but the order is important: Options only effect following values, so specifying an option as last field is allowed, but useless. Also, an option applies to <code>all</code> following values, so you don&#8217;t need to re-set an option over and over again. </p>
<p> The currently defined <code>Options</code> are:</p>
<dl>
<dd>
<dl>
<dt><code>interval=</code><i>seconds</i></p>
<dd>Gives the interval in which the data identified by <i>Identifier</i> is being collected.</dl>
</dl>
<dl>
<dd>Please note that this is the same format as used in the <code>exec plugin</code>, see <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5). </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>|&nbsp;<wbr><font SIZE="-1">PUTVAL</font>&nbsp;<wbr>testhost/interface/if_octets-test0 interval=10 1179574444:123:456<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 0 Success</dl>
<dt><font SIZE="-1"><code>PUTNOTIF</code></font> [<i>OptionList</i>] <code>message=</code><i>Message</i></p>
<dd>Submits a notification to the daemon which will then dispatch it to all plugins which have registered for receiving notifications. </p>
<p> The <font SIZE="-1"><code>PUTNOTIF</code></font> command is followed by a list of options which further describe the notification. The <code>message</code> option is special in that it will consume the rest of the line as its value. The <code>message</code>, <code>severity</code>, and <code>time</code> options are mandatory. </p>
<p> Valid options are:</p>
<dl>
<dd>
<dl>
<dt><code>message=</code><i>Message</i> (<font SIZE="-1"><code>REQUIRED</code></font>)</p>
<dd>Sets the message of the notification. This is the message that will be made accessible to the user, so it should contain some useful information. As with all options: If the message includes spaces, it must be quoted with double quotes. This option is mandatory.</p>
<dt><code>severity=failure</code>|<code>warning</code>|<code>okay</code> (<font SIZE="-1"><code>REQUIRED</code></font>)</p>
<dd>Sets the severity of the notification. This option is mandatory.</p>
<dt><code>time=</code><i>Time</i> (<font SIZE="-1"><code>REQUIRED</code></font>)</p>
<dd>Sets the time of the notification. The time is given as &#8220;epoch&#8221;, i. e. as seconds since January 1st, 1970, 00:00:00. This option is mandatory.</p>
<dt><code>host=</code><i>Hostname</i></p>
<dd>
<dt><code>plugin=</code><i>Plugin</i></p>
<dd>
<dt><code>plugin_instance=</code><i>Plugin-Instance</i></p>
<dd>
<dt><code>type=</code><i>Type</i></p>
<dd>
<dt><code>type_instance=</code><i>Type-Instance</i></p>
<dd>These &#8220;associative&#8221; options establish a relation between this notification and collected performance data. This connection is purely informal, i. e. the daemon itself doesn&#8217;t do anything with this information. However, websites or GUIs may use this information to place notifications near the affected graph or table. All the options are optional, but <code>plugin_instance</code> without <code>plugin</code> or <code>type_instance</code> without <code>type</code> doesn&#8217;t make much sense and should be avoided.</p>
<dt><code>type:key=</code><i>value</i></p>
<dd>Sets user defined meta information. The <code>type</code> key is a single character defining the type of the meta information. </p>
<p> The current supported types are:</p>
<dl>
<dd>
<dl>
<dt><code>s</code> A string passed as-is.</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
</dl>
</dl>
<dl>
<dd>Please note that this is the same format as used in the <code>exec plugin</code>, see <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5). </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>|&nbsp;<wbr><font SIZE="-1">PUTNOTIF</font>&nbsp;<wbr>type=temperature severity=warning time=1201094702 message=The roof is on fire!<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 0 Success</dl>
<dt><font SIZE="-1"><code>FLUSH</code></font> [<code>timeout=</code><i>Timeout</i>] [<code>plugin=</code><i>Plugin</i> [&#8230;]] [<code>identifier=</code><i>Ident</i> [&#8230;]]</p>
<dd>Flushes all cached data older than <i>Timeout</i> seconds. If no timeout has been specified, it defaults to -1 which causes all data to be flushed. </p>
<p> If the <code>plugin</code> option has been specified, only the <i>Plugin</i> plugin will be flushed. You can have multiple <code>plugin</code> options to flush multiple plugins in one go. If the <code>plugin</code> option is not given all plugins providing a flush callback will be flushed. </p>
<p> If the <code>identifier</code> option is given only the specified values will be flushed. This is meant to be used by graphing or displaying frontends which want to have the latest values for a specific graph. Again, you can specify the <code>identifier</code> option multiple times to flush several values. If this option is not specified at all, all values will be flushed. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>-&gt;&nbsp;<wbr>|&nbsp;<wbr><font SIZE="-1">FLUSH</font>&nbsp;<wbr>plugin=rrdtool identifier=localhost/df/df-root identifier=localhost/df/df-var<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;- | 0 Done: 2 successful, 0 errors</dl>
<h3>Identifiers</h3>
<p>Value or value-lists are identified in a uniform fashion: </p>
<p> <i>Hostname</i>/<i>Plugin</i>/<i>Type</i> </p>
<p> Where <i>Plugin</i> and <i>Type</i> are both either of type &quot;<i>Name</i>&#8220; or &#8221;<i>Name</i>&#8211;<i>Instance</i>&quot;. If the identifier includes spaces, it must be quoted using double quotes. This sounds more complicated than it is, so here are some examples: </p>
<pre> myhost/cpu-0/cpu-user
 myhost/load/load
 myhost/memory/memory-used
 myhost/disk-sda/disk_octets
 &quot;myups/snmp/temperature-Outlet 1&quot;</pre>
<h2>Abstraction Layer</h2>
<p><code>collectd</code> ships the Perl-Module Collectd::Unixsock which provides an abstraction layer over the actual socket connection. It can be found in the directory <i>bindings/perl/</i> in the source distribution or (usually) somewhere near <i>/usr/share/perl5/</i> if you&#8217;re using a package. If you want to use Perl to communicate with the daemon, you&#8217;re encouraged to use and expand this module.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/1-collectd-nagios/">collectd-nagios</a></i>(1), <i><a href="/docs/linux/man/7-unix/">unix</a></i>(7)</p>
<h2>Author</h2>
<p>Florian Forster &lt;octo [at] collectd.org&gt;</p>
