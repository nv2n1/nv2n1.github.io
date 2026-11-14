---
title: "collectd-exec(5)"
name: "collectd-exec"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-exec/"
description: "collectd-exec – Documentation of collectd’s \"exec plugin\""
---

<p>collectd-exec &#8211; Documentation of collectd&#8217;s &quot;exec plugin&quot;</p>
<h2>Synopsis</h2>
<pre> # See <a href="//www.systutorials.com/docs/linux/man/5-collectd.conf/">collectd.conf</a>(5)
 LoadPlugin exec
 # ...
 &lt;Plugin exec&gt;
 Exec &quot;myuser:mygroup&quot; &quot;myprog&quot;
 Exec &quot;otheruser&quot; &quot;/path/to/another/binary&quot; &quot;arg0&quot; &quot;arg1&quot;
 NotificationExec &quot;user&quot; &quot;/usr/lib/collectd/exec/handle_notification&quot;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;exec plugin&quot;</tt> forks off an executable either to receive values or to dispatch notifications to the outside world. The syntax of the configuration is explained in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) but summarized in the above synopsis. </p>
<p> If you want/need better performance or more functionality you should take a long look at the <tt>&quot;perl plugin&quot;</tt>, <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5).</p>
<h2>Executable Types</h2>
<p>There are currently two types of executables that can be executed by the <tt>&quot;exec plugin&quot;</tt>:</p>
<dl>
<dt>&quot;Exec&quot;</p>
<dd>These programs are forked and values that it writes to <tt>&quot;STDOUT&quot;</tt> are read back. The executable is forked in a fashion similar to init: It is forked once and not again until it exits. If it exited, it will be forked again after at most <i>Interval</i> seconds. It is perfectly legal for the executable to run for a long time and continuously write values to <tt>&quot;STDOUT&quot;</tt>. </p>
<p> See &#8220;<font SIZE="-1">EXEC DATA FORMAT&#8221;</font> below for a description of the output format expected from these programs. </p>
<p> <code>Warning:</code> If the executable only writes one value and then exits it will be executed every <i>Interval</i> seconds. If <i>Interval</i> is short (the default is 10 seconds) this may result in serious system load.</p>
<dt>&quot;NotificationExec&quot;</p>
<dd>The program is forked once for each notification that is handled by the daemon. The notification is passed to the program on <tt>&quot;STDIN&quot;</tt> in a fashion similar to HTTP-headers. In contrast to programs specified with <tt>&quot;Exec&quot;</tt> the execution of this program is not serialized, so that several instances of this program may run at once if multiple notifications are received. </p>
<p> See &#8220;<font SIZE="-1">NOTIFICATION DATA FORMAT&#8221;</font> below for a description of the data passed to these programs.</dl>
<h2>Exec Data Format</h2>
<p>The forked executable is expected to print values to <tt>&quot;STDOUT&quot;</tt>. The expected format is as follows:</p>
<dl>
<dt>Comments</p>
<dd>Each line beginning with a <tt>&quot;#&quot;</tt> (hash mark) is ignored.</p>
<dt><font SIZE="-1"><code>PUTVAL</code></font> <i>Identifier</i> [<i>OptionList</i>] <i>Valuelist</i></p>
<dd>Submits one or more values (identified by <i>Identifier</i>, see below) to the daemon which will dispatch it to all it&#8217;s write-plugins. </p>
<p> An <i>Identifier</i> is of the form <tt>&quot;</tt>host<tt></tt>/<tt></tt>plugin<tt></tt>&#8211;<tt></tt>instance<tt></tt>/<tt></tt>type<tt></tt>&#8211;<tt></tt>instance<tt>&quot;</tt> with both <i>instance</i>-parts being optional. If they&#8217;re omitted the hyphen must be omitted, too. <i>plugin</i> and each <i>instance</i>-part may be chosen freely as long as the tuple (plugin, plugin instance, type instance) uniquely identifies the plugin within collectd. <i>type</i> identifies the type and number of values (i. e. data-set) passed to collectd. A large list of predefined data-sets is available in the <code>types.db</code> file. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for a description of the format of this file. </p>
<p> The <i>OptionList</i> is an optional list of <i>Options</i>, where each option is a key-value-pair. A list of currently understood options can be found below, all other options will be ignored. Values that contain spaces must be quoted with double quotes. </p>
<p> <i>Valuelist</i> is a colon-separated list of the time and the values, each either an integer if the data-source is a counter, or a double if the data-source is of type &#8220;gauge&#8221;. You can submit an undefined gauge-value by using <code>U</code>. When submitting <code>U</code> to a counter the behavior is undefined. The time is given as epoch (i. e. standard <font SIZE="-1">UNIX</font> time) or <code>N</code> to use the current time. </p>
<p> You can mix options and values, but the order is important: Options only effect following values, so specifying an option as last field is allowed, but useless. Also, an option applies to <code>all</code> following values, so you don&#8217;t need to re-set an option over and over again. </p>
<p> The currently defined <code>Options</code> are:</p>
<dl>
<dd>
<dl>
<dt><code>interval=</code><i>seconds</i></p>
<dd>Gives the interval in which the data identified by <i>Identifier</i> is being collected.</dl>
</dl>
<dl>
<dd>Please note that this is the same format as used in the <code>unixsock plugin</code>, see <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5). There&#8217;s also a bit more information on identifiers in case you&#8217;re confused. </p>
<p> Since examples usually let one understand a lot better, here are some: </p>
<pre> PUTVAL leeloo/cpu-0/cpu-idle N:2299366
 PUTVAL alice/interface/if_octets-eth0 interval=10 1180647081:421465:479194</pre>
</dl>
<dt><font SIZE="-1"><code>PUTNOTIF</code></font> [<i>OptionList</i>] <code>message=</code><i>Message</i></p>
<dd>Submits a notification to the daemon which will then dispatch it to all plugins which have registered for receiving notifications. </p>
<p> The <font SIZE="-1"><code>PUTNOTIF</code></font> if followed by a list of options which further describe the notification. The <code>message</code> option is special in that it will consume the rest of the line as its value. The <code>message</code>, <code>severity</code>, and <code>time</code> options are mandatory. </p>
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
<dd></dl>
</dl>
<p> Please note that this is the same format as used in the <code>unixsock plugin</code>, see <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5). </p>
<p> When collectd exits it sends a <font SIZE="-1"><code>SIGTERM</code></font> to all still running child-processes upon which they have to quit.</p>
<h2>Notification Data Format</h2>
<p>The notification executables receive values rather than providing them. In fact, after the program is started <tt>&quot;STDOUT&quot;</tt> is connected to <tt>&quot;/dev/null&quot;</tt>. </p>
<p> The data is passed to the executables over <tt>&quot;STDIN&quot;</tt> in a format very similar to <font SIZE="-1">HTTP:</font> At first there is a &#8220;header&#8221; with one line per field. Every line consists of a field name, ended by a colon, and the associated value until end-of-line. The &#8220;header&#8221; is ended by two newlines immediately following another, i.e. an empty line. The rest, basically the &#8220;body&#8221;, is the message of the notification. </p>
<p> The following is an example notification passed to a program: </p>
<pre> Severity: FAILURE
 Time: 1200928930.515
 Host: myhost.mydomain.org
 

 This is a test notification to demonstrate the format</pre>
<p>The following header files are currently used. Please note, however, that you should ignore unknown header files to be as forward-compatible as possible.</p>
<dl>
<dt><code>Severity</code></p>
<dd>Severity of the notification. May either be <font SIZE="-1"><code>FAILURE</code></font>, <font SIZE="-1"><code>WARNING</code></font>, or <font SIZE="-1"><code>OKAY</code></font>.</p>
<dt><code>Time</code></p>
<dd>The time in epoch, i.e. as seconds since 1970-01-01 00:00:00 <font SIZE="-1">UTC.</font> The value currently has millisecond precision (i.e. three decimal places), but scripts should accept arbitrary numbers of decimal places, including no decimal places.</p>
<dt><code>Host</code></p>
<dd>
<dt><code>Plugin</code></p>
<dd>
<dt><code>PluginInstance</code></p>
<dd>
<dt><code>Type</code></p>
<dd>
<dt><code>TypeInstance</code></p>
<dd>Identification of the performance data this notification is associated with. All of these fields are optional because notifications do not <code>need</code> to be associated with a certain value.</dl>
<h2>Environment</h2>
<p>The following environment variables are set by the plugin before calling <i>exec</i>:</p>
<dl>
<dt><font SIZE="-1">COLLECTD_INTERVAL</font></p>
<dd>Value of the global interval setting.</p>
<dt><font SIZE="-1">COLLECTD_HOSTNAME</font></p>
<dd>Hostname used by <i>collectd</i> to dispatch local values.</dl>
<h2>Using Nagios Plugins</h2>
<p>Though the interface is far from perfect, there are tons of plugins for Nagios. You can use these plugins with collectd by using a simple transition layer, <tt>&quot;exec-nagios.px&quot;</tt>, which is shipped with the collectd distribution in the <tt>&quot;contrib/&quot;</tt> directory. It is a simple Perl script that comes with embedded documentation. To see it, run the following command: </p>
<pre> perldoc exec-nagios.px</pre>
<p>This script expects a configuration file, <tt>&quot;exec-nagios.conf&quot;</tt>. You can find an example in the <tt>&quot;contrib/&quot;</tt> directory, too. </p>
<p> Even a simple mechanism to submit &#8220;performance data&#8221; to collectd is implemented. If you need a more sophisticated setup, please rewrite the plugin to make use of collectd&#8217;s more powerful interface.</p>
<h2>Caveats</h2>
<dl>
<dt>&bull;</p>
<dd>The user, the binary is executed as, may not have root privileges, i. e. must have an <font SIZE="-1">UID</font> that is non-zero. This is for your own good.</p>
<dt>&bull;</p>
<dd>Early versions of the plugin did not use a command but treated all lines as if they were arguments to the <i></i><font SIZE="-1"><i>PUTVAL</i></font><i></i> command. When the <i></i><font SIZE="-1"><i>PUTNOTIF</i></font><i></i> command was implemented, this behavior was kept for lines which start with an unknown command for backwards compatibility. This compatibility code has been removed in <i>collectd 5</i>.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5), <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2), <i><a href="/docs/linux/man/3-exec/">exec</a></i>(3)</p>
<h2>Author</h2>
<p>Florian Forster &lt;octo [at] collectd.org&gt;</p>
