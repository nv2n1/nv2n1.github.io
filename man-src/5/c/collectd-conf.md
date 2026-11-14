---
title: "collectd-conf(5)"
name: "collectd-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-conf/"
description: "collectd.conf – Configuration for the system statistics collection daemon collectd"
---

<p>collectd.conf &#8211; Configuration for the system statistics collection daemon collectd</p>
<h2>Synopsis</h2>
<pre> BaseDir &quot;/var/lib/collectd&quot;
 PIDFile &quot;/run/collectd.pid&quot;
 Interval 10.0
 LoadPlugin cpu
 LoadPlugin load
 &lt;LoadPlugin df&gt;
 Interval 3600
 &lt;/LoadPlugin&gt;
 &lt;Plugin df&gt;
 ValuesPercentage true
 &lt;/Plugin&gt;
 LoadPlugin ping
 &lt;Plugin ping&gt;
 Host &quot;example.org&quot;
 Host &quot;provider.net&quot;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>This config file controls how the system statistics collection daemon <code>collectd</code> behaves. The most significant option is <code>LoadPlugin</code>, which controls which plugins to load. These plugins ultimately define collectd&#8217;s behavior. If the <code>AutoLoadPlugin</code> option has been enabled, the explicit <code>LoadPlugin</code> lines may be omitted for all plugins with a configuration block, i.e. a <tt>&quot;&lt;Plugin ...&gt;&quot;</tt> block. </p>
<p> The syntax of this config file is similar to the config file of the famous <i>Apache</i> webserver. Each line contains either an option (a key and a list of one or more values) or a section-start or -end. Empty lines and everything after a non-quoted hash-symbol (<tt>&quot;#&quot;</tt>) are ignored. <i>Keys</i> are unquoted strings, consisting only of alphanumeric characters and the underscore (<tt>&quot;_&quot;</tt>) character. Keys are handled case insensitive by <i>collectd</i> itself and all plugins included with it. <i>Values</i> can either be an <i>unquoted string</i>, a <i>quoted string</i> (enclosed in double-quotes) a <i>number</i> or a <i>boolean</i> expression. <i>Unquoted strings</i> consist of only alphanumeric characters and underscores (<tt>&quot;_&quot;</tt>) and do not need to be quoted. <i>Quoted strings</i> are enclosed in double quotes (<tt>&quot;&quot;&quot;</tt>). You can use the backslash character (<tt>&quot;\&quot;</tt>) to include double quotes as part of the string. <i>Numbers</i> can be specified in decimal and floating point format (using a dot <tt>&quot;.&quot;</tt> as decimal separator), hexadecimal when using the <tt>&quot;0x&quot;</tt> prefix and octal with a leading zero (<tt>0</tt>). <i>Boolean</i> values are either <code>true</code> or <code>false</code>. </p>
<p> Lines may be wrapped by using <tt>&quot;\&quot;</tt> as the last character before the newline. This allows long lines to be split into multiple lines. Quoted strings may be wrapped as well. However, those are treated special in that whitespace at the beginning of the following lines will be ignored, which allows for nicely indenting the wrapped lines. </p>
<p> The configuration is read and processed in order, i.e. from top to bottom. So the plugins are loaded in the order listed in this config file. It is a good idea to load any logging plugins first in order to catch messages from plugins during configuration. Also, unless <code>AutoLoadPlugin</code> is enabled, the <code>LoadPlugin</code> option <i>must</i> occur <i>before</i> the appropriate <tt>&quot;&lt;</tt>Plugin<tt> ...&gt;&quot;</tt> block.</p>
<h2>Global Options</h2>
<dl>
<dt><code>BaseDir</code> <i>Directory</i></p>
<dd>Sets the base directory. This is the directory beneath which all RRD-files are created. Possibly more subdirectories are created. This is also the working directory for the daemon.</p>
<dt><code>LoadPlugin</code> <i>Plugin</i></p>
<dd>Loads the plugin <i>Plugin</i>. This is required to load plugins, unless the <code>AutoLoadPlugin</code> option is enabled (see below). Without any loaded plugins, <i>collectd</i> will be mostly useless. </p>
<p> Only the first <code>LoadPlugin</code> statement or block for a given plugin name has any effect. This is useful when you want to split up the configuration into smaller files and want each file to be &#8220;self contained&#8221;, i.e. it contains a <code>Plugin</code> block <i>and</i> the appropriate <code>LoadPlugin</code> statement. The downside is that if you have multiple conflicting <code>LoadPlugin</code> blocks, e.g. when they specify different intervals, only one of them (the first one encountered) will take effect and all others will be silently ignored. </p>
<p> <code>LoadPlugin</code> may either be a simple configuration <i>statement</i> or a <i>block</i> with additional options, affecting the behavior of <code>LoadPlugin</code>. A simple statement looks like this: </p>
<pre> LoadPlugin &quot;cpu&quot;</pre>
<p>Options inside a <code>LoadPlugin</code> block can override default settings and influence the way plugins are loaded, e.g.: </p>
<pre> &lt;LoadPlugin perl&gt;
 Interval 60
 &lt;/LoadPlugin&gt;</pre>
<p>The following options are valid inside <code>LoadPlugin</code> blocks:</p>
<dl>
<dd>
<dl>
<dt><code>Globals</code> <code>true|false</code></p>
<dd>If enabled, collectd will export all global symbols of the plugin (and of all libraries loaded as dependencies of the plugin) and, thus, makes those symbols available for resolving unresolved symbols in subsequently loaded plugins if that is supported by your system. </p>
<p> This is useful (or possibly even required), e.g., when loading a plugin that embeds some scripting language into the daemon (e.g. the <i>Perl</i> and <i>Python plugins</i>). Scripting languages usually provide means to load extensions written in C. Those extensions require symbols provided by the interpreter, which is loaded as a dependency of the respective collectd plugin. See the documentation of those plugins (e.g., <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5) or <i><a href="/docs/linux/man/5-collectd-python/">collectd-python</a></i>(5)) for details. </p>
<p> By default, this is disabled. As a special exception, if the plugin name is either <tt>&quot;perl&quot;</tt> or <tt>&quot;python&quot;</tt>, the default is changed to enabled in order to keep the average user from ever having to deal with this low level linking stuff.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Sets a plugin-specific interval for collecting metrics. This overrides the global <code>Interval</code> setting. If a plugin provides its own support for specifying an interval, that setting will take precedence.</p>
<dt><code>FlushInterval</code> <i>Seconds</i></p>
<dd>Specifies the interval, in seconds, to call the flush callback if it&#8217;s defined in this plugin. By default, this is disabled.</p>
<dt><code>FlushTimeout</code> <i>Seconds</i></p>
<dd>Specifies the value of the timeout argument of the flush callback.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>AutoLoadPlugin</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>false</code> (the default), each plugin needs to be loaded explicitly, using the <code>LoadPlugin</code> statement documented above. If a <code>&lt;Plugin &#8230;&gt;</code> block is encountered and no configuration handling callback for this plugin has been registered, a warning is logged and the block is ignored. </p>
<p> When set to <code>true</code>, explicit <code>LoadPlugin</code> statements are not required. Each <code>&lt;Plugin &#8230;&gt;</code> block acts as if it was immediately preceded by a <code>LoadPlugin</code> statement. <code>LoadPlugin</code> statements are still required for plugins that don&#8217;t provide any configuration, e.g. the <i>Load plugin</i>.</p>
<dt><code>CollectInternalStats</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>true</code>, various statistics about the <i>collectd</i> daemon will be collected, with &#8220;collectd&#8221; as the <i>plugin name</i>. Defaults to <code>false</code>. </p>
<p> The following metrics are reported:</p>
<dl>
<dd>
<dl>
<dt>&quot;collectd-write_queue/queue_length&quot;</p>
<dd>The number of metrics currently in the write queue. You can limit the queue length with the <code>WriteQueueLimitLow</code> and <code>WriteQueueLimitHigh</code> options.</p>
<dt>&quot;collectd-write_queue/derive-dropped&quot;</p>
<dd>The number of metrics dropped due to a queue length limitation. If this value is non-zero, your system can&#8217;t handle all incoming metrics and protects itself against overload by dropping metrics.</p>
<dt>&quot;collectd-cache/cache_size&quot;</p>
<dd>The number of elements in the metric cache (the cache you can interact with using <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5)).</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Include</code> <i>Path</i> [<i>pattern</i>]</p>
<dd>If <i>Path</i> points to a file, includes that file. If <i>Path</i> points to a directory, recursively includes all files within that directory and its subdirectories. If the <tt>&quot;wordexp&quot;</tt> function is available on your system, shell-like wildcards are expanded before files are included. This means you can use statements like the following: </p>
<pre> Include &quot;/etc/collectd.d/*.conf&quot;</pre>
<p>Starting with version 5.3, this may also be a block in which further options affecting the behavior of <code>Include</code> may be specified. The following option is currently allowed: </p>
<pre> &lt;Include &quot;/etc/collectd.d&quot;&gt;
 Filter &quot;*.conf&quot;
 &lt;/Include&gt;</pre>
<dl>
<dd>
<dl>
<dt><code>Filter</code> <i>pattern</i></p>
<dd>If the <tt>&quot;fnmatch&quot;</tt> function is available on your system, a shell-like wildcard <i>pattern</i> may be specified to filter which files to include. This may be used in combination with recursively including a directory to easily be able to arbitrarily mix configuration files and other documents (e.g. <font SIZE="-1">README</font> files). The given example is similar to the first example above but includes all files matching <tt>&quot;*.conf&quot;</tt> in any subdirectory of <tt>&quot;/etc/collectd.d&quot;</tt>.</dl>
</dl>
<dl>
<dd>If more than one file is included by a single <code>Include</code> option, the files will be included in lexicographical order (as defined by the <tt>&quot;strcmp&quot;</tt> function). Thus, you can e. g. use numbered prefixes to specify the order in which the files are loaded. </p>
<p> To prevent loops and shooting yourself in the foot in interesting ways the nesting is limited to a depth of 8 levels, which should be sufficient for most uses. Since symlinks are followed it is still possible to crash the daemon by looping symlinks. In our opinion significant stupidity should result in an appropriate amount of pain. </p>
<p> It is no problem to have a block like <tt>&quot;&lt;Plugin foo&gt;&quot;</tt> in more than one file, but you cannot include files from within blocks.</dl>
<dt><code>PIDFile</code> <i>File</i></p>
<dd>Sets where to write the <font SIZE="-1">PID</font> file to. This file is overwritten when it exists and deleted when the program is stopped. Some init-scripts might override this setting using the <code>-P</code> command-line option.</p>
<dt><code>PluginDir</code> <i>Directory</i></p>
<dd>Path to the plugins (shared objects) of collectd.</p>
<dt><code>TypesDB</code> <i>File</i> [<i>File</i> &#8230;]</p>
<dd>Set one or more files that contain the data-set descriptions. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for a description of the format of this file. </p>
<p> If this option is not specified, a default file is read. If you need to define custom types in addition to the types defined in the default file, you need to explicitly load both. In other words, if the <code>TypesDB</code> option is encountered the default behavior is disabled and if you need the default types you have to also explicitly load them.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Configures the interval in which to query the read plugins. Obviously smaller values lead to a higher system load produced by collectd, while higher values lead to more coarse statistics. </p>
<p> <code>Warning:</code> You should set this once and then never touch it again. If you do, <i>you will have to delete all your </i><font SIZE="-1"><i>RRD</i></font><i> files</i> or know some serious RRDtool magic! (Assuming you&#8217;re using the <i>RRDtool</i> or <i>RRDCacheD</i> plugin.)</p>
<dt><code>MaxReadInterval</code> <i>Seconds</i></p>
<dd>A read plugin doubles the interval between queries after each failed attempt to get data. </p>
<p> This options limits the maximum value of the interval. The default value is <code>86400</code>.</p>
<dt><code>Timeout</code> <i>Iterations</i></p>
<dd>Consider a value list &#8220;missing&#8221; when no update has been read or received for <i>Iterations</i> iterations. By default, <i>collectd</i> considers a value list missing when no update has been received for twice the update interval. Since this setting uses iterations, the maximum allowed time without update depends on the <i>Interval</i> information contained in each value list. This is used in the <i>Threshold</i> configuration to dispatch notifications about missing values, see <i><a href="/docs/linux/man/5-collectd-threshold/">collectd-threshold</a></i>(5) for details.</p>
<dt><code>ReadThreads</code> <i>Num</i></p>
<dd>Number of threads to start for reading plugins. The default value is <code>5</code>, but you may want to increase this if you have more than five plugins that take a long time to read. Mostly those are plugins that do network-IO. Setting this to a value higher than the number of registered read callbacks is not recommended.</p>
<dt><code>WriteThreads</code> <i>Num</i></p>
<dd>Number of threads to start for dispatching value lists to write plugins. The default value is <code>5</code>, but you may want to increase this if you have more than five plugins that may take relatively long to write to.</p>
<dt><code>WriteQueueLimitHigh</code> <i>HighNum</i></p>
<dd>
<dt><code>WriteQueueLimitLow</code> <i>LowNum</i></p>
<dd>Metrics are read by the <i>read threads</i> and then put into a queue to be handled by the <i>write threads</i>. If one of the <i>write plugins</i> is slow (e.g. network timeouts, I/O saturation of the disk) this queue will grow. In order to avoid running into memory issues in such a case, you can limit the size of this queue. </p>
<p> By default, there is no limit and memory may grow indefinitely. This is most likely not an issue for clients, i.e. instances that only handle the local metrics. For servers it is recommended to set this to a non-zero value, though. </p>
<p> You can set the limits using <code>WriteQueueLimitHigh</code> and <code>WriteQueueLimitLow</code>. Each of them takes a numerical argument which is the number of metrics in the queue. If there are <i>HighNum</i> metrics in the queue, any new metrics <i>will</i> be dropped. If there are less than <i>LowNum</i> metrics in the queue, all new metrics <i>will</i> be enqueued. If the number of metrics currently in the queue is between <i>LowNum</i> and <i>HighNum</i>, the metric is dropped with a probability that is proportional to the number of metrics in the queue (i.e. it increases linearly until it reaches 100%.) </p>
<p> If <code>WriteQueueLimitHigh</code> is set to non-zero and <code>WriteQueueLimitLow</code> is unset, the latter will default to half of <code>WriteQueueLimitHigh</code>. </p>
<p> If you do not want to randomly drop values when the queue size is between <i>LowNum</i> and <i>HighNum</i>, set <code>WriteQueueLimitHigh</code> and <code>WriteQueueLimitLow</code> to the same value. </p>
<p> Enabling the <code>CollectInternalStats</code> option is of great help to figure out the values to set <code>WriteQueueLimitHigh</code> and <code>WriteQueueLimitLow</code> to.</p>
<dt><code>Hostname</code> <i>Name</i></p>
<dd>Sets the hostname that identifies a host. If you omit this setting, the hostname will be determined using the <i><a href="/docs/linux/man/2-gethostname/">gethostname</a></i>(2) system call.</p>
<dt><code>FQDNLookup</code> <code>true|false</code></p>
<dd>If <code>Hostname</code> is determined automatically this setting controls whether or not the daemon should try to figure out the &#8220;fully qualified domain name&#8221;, <font SIZE="-1">FQDN.</font> This is done using a lookup of the name returned by <tt>&quot;gethostname&quot;</tt>. This option is enabled by default.</p>
<dt><code>PreCacheChain</code> <i>ChainName</i></p>
<dd>
<dt><code>PostCacheChain</code> <i>ChainName</i></p>
<dd>Configure the name of the &#8220;pre-cache chain&#8221; and the &#8220;post-cache chain&#8221;. Please see &#8220;<font SIZE="-1">FILTER CONFIGURATION&#8221;</font> below on information on chains and how these setting change the daemon&#8217;s behavior.</dl>
<h2>Plugin Options</h2>
<p>Some plugins may register own options. These options must be enclosed in a <tt>&quot;Plugin&quot;</tt>-Section. Which options exist depends on the plugin used. Some plugins require external configuration, too. The <tt>&quot;apache plugin&quot;</tt>, for example, required <tt>&quot;mod_status&quot;</tt> to be configured in the webserver you&#8217;re going to collect data from. These plugins are listed below as well, even if they don&#8217;t require any configuration within collectd&#8217;s configuration file. </p>
<p> A list of all plugins and a short summary for each plugin can be found in the <i></i><font SIZE="-1"><i>README</i></font><i></i> file shipped with the sourcecode and hopefully binary packets as well.</p>
<h3>Plugin aggregation</h3>
<p>The <i>Aggregation plugin</i> makes it possible to aggregate several values into one using aggregation functions such as <i>sum</i>, <i>average</i>, <i>min</i> and <i>max</i>. This can be put to a wide variety of uses, e.g. average and total <font SIZE="-1">CPU</font> statistics for your entire fleet. </p>
<p> The grouping is powerful but, as with many powerful tools, may be a bit difficult to wrap your head around. The grouping will therefore be demonstrated using an example: The average and sum of the <font SIZE="-1">CPU</font> usage across all CPUs of each host is to be calculated. </p>
<p> To select all the affected values for our example, set <tt>&quot;Plugin cpu&quot;</tt> and <tt>&quot;Type cpu&quot;</tt>. The other values are left unspecified, meaning &#8220;all values&#8221;. The <i>Host</i>, <i>Plugin</i>, <i>PluginInstance</i>, <i>Type</i> and <i>TypeInstance</i> options work as if they were specified in the <tt>&quot;WHERE&quot;</tt> clause of an <tt>&quot;SELECT&quot;</tt> <font SIZE="-1">SQL</font> statement. </p>
<pre> Plugin &quot;cpu&quot;
 Type &quot;cpu&quot;</pre>
<p>Although the <i>Host</i>, <i>PluginInstance</i> (<font SIZE="-1">CPU</font> number, i.e. 0, 1, 2, &#8230;) and <i>TypeInstance</i> (idle, user, system, &#8230;) fields are left unspecified in the example, the intention is to have a new value for each host / type instance pair. This is achieved by &#8220;grouping&#8221; the values using the <tt>&quot;GroupBy&quot;</tt> option. It can be specified multiple times to group by more than one field. </p>
<pre> GroupBy &quot;Host&quot;
 GroupBy &quot;TypeInstance&quot;</pre>
<p>We do neither specify nor group by <i>plugin instance</i> (the <font SIZE="-1">CPU</font> number), so all metrics that differ in the <font SIZE="-1">CPU</font> number only will be aggregated. Each aggregation needs <i>at least one</i> such field, otherwise no aggregation would take place. </p>
<p> The full example configuration looks like this: </p>
<pre> &lt;Plugin &quot;aggregation&quot;&gt;
 &lt;Aggregation&gt;
 Plugin &quot;cpu&quot;
 Type &quot;cpu&quot;
 GroupBy &quot;Host&quot;
 GroupBy &quot;TypeInstance&quot;
 CalculateSum true
 CalculateAverage true
 &lt;/Aggregation&gt;
 &lt;/Plugin&gt;</pre>
<p>There are a couple of limitations you should be aware of:</p>
<dl>
<dt>&bull;</p>
<dd>The <i>Type</i> cannot be left unspecified, because it is not reasonable to add apples to oranges. Also, the internal lookup structure won&#8217;t work if you try to group by type.</p>
<dt>&bull;</p>
<dd>There must be at least one unspecified, ungrouped field. Otherwise nothing will be aggregated.</dl>
<p> As you can see in the example above, each aggregation has its own <code>Aggregation</code> block. You can have multiple aggregation blocks and aggregation blocks may match the same values, i.e. one value list can update multiple aggregations. The following options are valid inside <code>Aggregation</code> blocks:</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>
<dt><code>Plugin</code> <i>Plugin</i></p>
<dd>
<dt><code>PluginInstance</code> <i>PluginInstance</i></p>
<dd>
<dt><code>Type</code> <i>Type</i></p>
<dd>
<dt><code>TypeInstance</code> <i>TypeInstance</i></p>
<dd>Selects the value lists to be added to this aggregation. <code>Type</code> must be a valid data set name, see <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for details. </p>
<p> If the string starts with and ends with a slash (<tt>&quot;/&quot;</tt>), the string is interpreted as a <i>regular expression</i>. The regex flavor used are <font SIZE="-1">POSIX</font> extended regular expressions as described in <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7). Example usage: </p>
<pre> Host &quot;/^db[0-9]\.example\.com$/&quot;</pre>
<dt><code>GroupBy</code> <code>Host</code>|<code>Plugin</code>|<code>PluginInstance</code>|<code>TypeInstance</code></p>
<dd>Group valued by the specified field. The <code>GroupBy</code> option may be repeated to group by multiple fields.</p>
<dt><code>SetHost</code> <i>Host</i></p>
<dd>
<dt><code>SetPlugin</code> <i>Plugin</i></p>
<dd>
<dt><code>SetPluginInstance</code> <i>PluginInstance</i></p>
<dd>
<dt><code>SetTypeInstance</code> <i>TypeInstance</i></p>
<dd>Sets the appropriate part of the identifier to the provided string. </p>
<p> The <i>PluginInstance</i> should include the placeholder <tt>&quot;%{aggregation}&quot;</tt> which will be replaced with the aggregation function, e.g. &#8220;average&#8221;. Not including the placeholder will result in duplication warnings and/or messed up values if more than one aggregation function are enabled. </p>
<p> The following example calculates the average usage of all &#8220;even&#8221; CPUs: </p>
<pre> &lt;Plugin &quot;aggregation&quot;&gt;
 &lt;Aggregation&gt;
 Plugin &quot;cpu&quot;
 PluginInstance &quot;/[0,2,4,6,8]$/&quot;
 Type &quot;cpu&quot;
 SetPlugin &quot;cpu&quot;
 SetPluginInstance &quot;even-%{aggregation}&quot;
 GroupBy &quot;Host&quot;
 GroupBy &quot;TypeInstance&quot;
 CalculateAverage true
 &lt;/Aggregation&gt;
 &lt;/Plugin&gt;</pre>
<p>This will create the files:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>foo.example.com/cpu-even-average/cpu-idle</p>
<dt>&bull;</p>
<dd>foo.example.com/cpu-even-average/cpu-system</p>
<dt>&bull;</p>
<dd>foo.example.com/cpu-even-average/cpu-user</p>
<dt>&bull;</p>
<dd>&#8230;</dl>
</dl>
<dl>
<dd></dl>
<dt><code>CalculateNum</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CalculateSum</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CalculateAverage</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CalculateMinimum</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CalculateMaximum</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CalculateStddev</code> <code>true</code>|<code>false</code></p>
<dd>Boolean options for enabling calculation of the number of value lists, their sum, average, minimum, maximum and&nbsp;<wbr>/ or standard deviation. All options are disabled by default.</dl>
<h3>Plugin amqp</h3>
<p>The <i></i><font SIZE="-1"><i>AMQP</i></font><i> plugin</i> can be used to communicate with other instances of <i>collectd</i> or third party applications using an <font SIZE="-1">AMQP</font> message broker. Values are sent to or received from the broker, which handles routing, queueing and possibly filtering out messages. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;amqp&quot;&gt;
 # Send values to an AMQP broker
 &lt;Publish &quot;some_name&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;5672&quot;
 VHost &quot;/&quot;
 User &quot;guest&quot;
 Password &quot;guest&quot;
 Exchange &quot;amq.fanout&quot;
 # ExchangeType &quot;fanout&quot;
 # RoutingKey &quot;collectd&quot;
 # Persistent false
 # ConnectionRetryDelay 0
 # Format &quot;command&quot;
 # StoreRates false
 # GraphitePrefix &quot;collectd.&quot;
 # GraphiteEscapeChar &quot;_&quot;
 # GraphiteSeparateInstances false
 # GraphiteAlwaysAppendDS false
 # GraphitePreserveSeparator false
 &lt;/Publish&gt;
 # Receive values from an AMQP broker
 &lt;Subscribe &quot;some_name&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;5672&quot;
 VHost &quot;/&quot;
 User &quot;guest&quot;
 Password &quot;guest&quot;
 Exchange &quot;amq.fanout&quot;
 # ExchangeType &quot;fanout&quot;
 # Queue &quot;queue_name&quot;
 # QueueDurable false
 # QueueAutoDelete true
 # RoutingKey &quot;collectd.#&quot;
 # ConnectionRetryDelay 0
 &lt;/Subscribe&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin&#8217;s configuration consists of a number of <i>Publish</i> and <i>Subscribe</i> blocks, which configure sending and receiving of values respectively. The two blocks are very similar, so unless otherwise noted, an option can be used in either block. The name given in the blocks starting tag is only used for reporting messages, but may be used to support <i>flushing</i> of certain <i>Publish</i> blocks in the future.</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>Hostname or IP-address of the <font SIZE="-1">AMQP</font> broker. Defaults to the default behavior of the underlying communications library, <i>rabbitmq-c</i>, which is &#8220;localhost&#8221;.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>Service name or port number on which the <font SIZE="-1">AMQP</font> broker accepts connections. This argument must be a string, even if the numeric form is used. Defaults to &#8220;5672&#8221;.</p>
<dt><code>VHost</code> <i>VHost</i></p>
<dd>Name of the <i>virtual host</i> on the <font SIZE="-1">AMQP</font> broker to use. Defaults to &#8220;/&#8221;.</p>
<dt><code>User</code> <i>User</i></p>
<dd>
<dt><code>Password</code> <i>Password</i></p>
<dd>Credentials used to authenticate to the <font SIZE="-1">AMQP</font> broker. By default &#8220;guest&#8221;/&#8220;guest&#8221; is used.</p>
<dt><code>Exchange</code> <i>Exchange</i></p>
<dd>In <i>Publish</i> blocks, this option specifies the <i>exchange</i> to send values to. By default, &#8220;amq.fanout&#8221; will be used. </p>
<p> In <i>Subscribe</i> blocks this option is optional. If given, a <i>binding</i> between the given exchange and the <i>queue</i> is created, using the <i>routing key</i> if configured. See the <code>Queue</code> and <code>RoutingKey</code> options below.</p>
<dt><code>ExchangeType</code> <i>Type</i></p>
<dd>If given, the plugin will try to create the configured <i>exchange</i> with this <i>type</i> after connecting. When in a <i>Subscribe</i> block, the <i>queue</i> will then be bound to this exchange.</p>
<dt><code>Queue</code> <i>Queue</i> (Subscribe only)</p>
<dd>Configures the <i>queue</i> name to subscribe to. If no queue name was configured explicitly, a unique queue name will be created by the broker.</p>
<dt><code>QueueDurable</code> <code>true</code>|<code>false</code> (Subscribe only)</p>
<dd>Defines if the <i>queue</i> subscribed to is durable (saved to persistent storage) or transient (will disappear if the <font SIZE="-1">AMQP</font> broker is restarted). Defaults to &#8220;false&#8221;. </p>
<p> This option should be used in conjunction with the <i>Persistent</i> option on the publish side.</p>
<dt><code>QueueAutoDelete</code> <code>true</code>|<code>false</code> (Subscribe only)</p>
<dd>Defines if the <i>queue</i> subscribed to will be deleted once the last consumer unsubscribes. Defaults to &#8220;true&#8221;.</p>
<dt><code>RoutingKey</code> <i>Key</i></p>
<dd>In <i>Publish</i> blocks, this configures the routing key to set on all outgoing messages. If not given, the routing key will be computed from the <i>identifier</i> of the value. The host, plugin, type and the two instances are concatenated together using dots as the separator and all containing dots replaced with slashes. For example &#8220;collectd.host/example/com.cpu.0.cpu.user&#8221;. This makes it possible to receive only specific values using a &#8220;topic&#8221; exchange. </p>
<p> In <i>Subscribe</i> blocks, configures the <i>routing key</i> used when creating a <i>binding</i> between an <i>exchange</i> and the <i>queue</i>. The usual wildcards can be used to filter messages when using a &#8220;topic&#8221; exchange. If you&#8217;re only interested in <font SIZE="-1">CPU</font> statistics, you could use the routing key &#8220;collectd.*.cpu.#&#8221; for example.</p>
<dt><code>Persistent</code> <code>true</code>|<code>false</code> (Publish only)</p>
<dd>Selects the <i>delivery method</i> to use. If set to <code>true</code>, the <i>persistent</i> mode will be used, i.e. delivery is guaranteed. If set to <code>false</code> (the default), the <i>transient</i> delivery mode will be used, i.e. messages may be lost due to high load, overflowing queues or similar issues.</p>
<dt><code>ConnectionRetryDelay</code> <i>Delay</i></p>
<dd>When the connection to the <font SIZE="-1">AMQP</font> broker is lost, defines the time in seconds to wait before attempting to reconnect. Defaults to 0, which implies collectd will attempt to reconnect at each read interval (in Subscribe mode) or each time values are ready for submission (in Publish mode).</p>
<dt><code>Format</code> <code>Command</code>|<font SIZE="-1"><code>JSON</code></font>|<code>Graphite</code> (Publish only)</p>
<dd>Selects the format in which messages are sent to the broker. If set to <code>Command</code> (the default), values are sent as <tt>&quot;PUTVAL&quot;</tt> commands which are identical to the syntax used by the <i>Exec</i> and <i>UnixSock plugins</i>. In this case, the <tt>&quot;Content-Type&quot;</tt> header field will be set to <tt>&quot;text/collectd&quot;</tt>. </p>
<p> If set to <font SIZE="-1"><code>JSON</code></font>, the values are encoded in the <i>JavaScript Object Notation</i>, an easy and straight forward exchange format. The <tt>&quot;Content-Type&quot;</tt> header field will be set to <tt>&quot;application/json&quot;</tt>. </p>
<p> If set to <code>Graphite</code>, values are encoded in the <i>Graphite</i> format, which is &#8220;&lt;metric&gt; &lt;value&gt; &lt;timestamp&gt;
&#8221;. The <tt>&quot;Content-Type&quot;</tt> header field will be set to <tt>&quot;text/graphite&quot;</tt>. </p>
<p> A subscribing client <i>should</i> use the <tt>&quot;Content-Type&quot;</tt> header field to determine how to decode the values. Currently, the <i></i><font SIZE="-1"><i>AMQP</i></font><i> plugin</i> itself can only decode the <code>Command</code> format.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code> (Publish only)</p>
<dd>Determines whether or not <tt>&quot;COUNTER&quot;</tt>, <tt>&quot;DERIVE&quot;</tt> and <tt>&quot;ABSOLUTE&quot;</tt> data sources are converted to a <i>rate</i> (i.e. a <tt>&quot;GAUGE&quot;</tt> value). If set to <code>false</code> (the default), no conversion is performed. Otherwise the conversion is performed using the internal value cache. </p>
<p> Please note that currently this option is only used if the <code>Format</code> option has been set to <font SIZE="-1"><code>JSON</code></font>.</p>
<dt><code>GraphitePrefix</code> (Publish and <code>Format</code>=<i>Graphite</i> only)</p>
<dd>A prefix can be added in the metric name when outputting in the <i>Graphite</i> format. It&#8217;s added before the <i>Host</i> name. Metric name will be &#8220;&lt;prefix&gt;&lt;host&gt;&lt;postfix&gt;&lt;plugin&gt;&lt;type&gt;&lt;name&gt;&#8221;</p>
<dt><code>GraphitePostfix</code> (Publish and <code>Format</code>=<i>Graphite</i> only)</p>
<dd>A postfix can be added in the metric name when outputting in the <i>Graphite</i> format. It&#8217;s added after the <i>Host</i> name. Metric name will be &#8220;&lt;prefix&gt;&lt;host&gt;&lt;postfix&gt;&lt;plugin&gt;&lt;type&gt;&lt;name&gt;&#8221;</p>
<dt><code>GraphiteEscapeChar</code> (Publish and <code>Format</code>=<i>Graphite</i> only)</p>
<dd>Specify a character to replace dots (.) in the host part of the metric name. In <i>Graphite</i> metric name, dots are used as separators between different metric parts (host, plugin, type). Default is &#8220;_&#8221; (<i>Underscore</i>).</p>
<dt><code>GraphiteSeparateInstances</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, the plugin instance and type instance will be in their own path component, for example <tt>&quot;host.cpu.0.cpu.idle&quot;</tt>. If set to <code>false</code> (the default), the plugin and plugin instance (and likewise the type and type instance) are put into one component, for example <tt>&quot;host.cpu-0.cpu-idle&quot;</tt>.</p>
<dt><code>GraphiteAlwaysAppendDS</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;metric&#8221; identifier. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></p>
<dt><code>GraphitePreserveSeparator</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>false</code> (the default) the <tt>&quot;.&quot;</tt> (dot) character is replaced with <i>GraphiteEscapeChar</i>. Otherwise, if set to <code>true</code>, the <tt>&quot;.&quot;</tt> (dot) character is preserved, i.e. passed through.</dl>
<h3>Plugin apache</h3>
<p>To configure the <tt>&quot;apache&quot;</tt>-plugin you first need to configure the Apache webserver correctly. The Apache-plugin <tt>&quot;mod_status&quot;</tt> needs to be loaded and working and the <tt>&quot;ExtendedStatus&quot;</tt> directive needs to be <code>enabled</code>. You can use the following snipped to base your Apache config upon: </p>
<pre> ExtendedStatus on
 &lt;IfModule mod_status.c&gt;
 &lt;Location /mod_status&gt;
 SetHandler server-status
 &lt;/Location&gt;
 &lt;/IfModule&gt;</pre>
<p>Since its <tt>&quot;mod_status&quot;</tt> module is very similar to Apache&#8217;s, <code>lighttpd</code> is also supported. It introduces a new field, called <tt>&quot;BusyServers&quot;</tt>, to count the number of currently connected clients. This field is also supported. </p>
<p> The configuration of the <i>Apache</i> plugin consists of one or more <tt>&quot;&lt;Instance&nbsp;<wbr>/&gt;&quot;</tt> blocks. Each block requires one string argument as the instance name. For example: </p>
<pre> &lt;Plugin &quot;apache&quot;&gt;
 &lt;Instance &quot;www1&quot;&gt;
 URL &quot;<a rel="nofollow" href="http://www1.example.com/mod_status?auto">http://www1.example.com/mod_status?auto</a>&quot;
 &lt;/Instance&gt;
 &lt;Instance &quot;www2&quot;&gt;
 URL &quot;<a rel="nofollow" href="http://www2.example.com/mod_status?auto">http://www2.example.com/mod_status?auto</a>&quot;
 &lt;/Instance&gt;
 &lt;/Plugin&gt;</pre>
<p>The instance name will be used as the <i>plugin instance</i>. To emulate the old (version 4) behavior, you can use an empty string (&quot;&quot;). In order for the plugin to work correctly, each instance name must be unique. This is not enforced by the plugin and it is your responsibility to ensure it. </p>
<p> The following options are accepted within each <i>Instance</i> block:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i><a rel="nofollow" href="http://host/mod_status?auto">http://host/mod_status?auto</a></i></p>
<dd>Sets the <font SIZE="-1">URL</font> of the <tt>&quot;mod_status&quot;</tt> output. This needs to be the output generated by <tt>&quot;ExtendedStatus on&quot;</tt> and it needs to be the machine readable output generated by appending the <tt>&quot;?auto&quot;</tt> argument. This option is <i>mandatory</i>.</p>
<dt><code>User</code> <i>Username</i></p>
<dd>Optional user name needed for authentication.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Optional password needed for authentication.</p>
<dt><code>VerifyPeer</code> <code>true|false</code></p>
<dd>Enable or disable peer <font SIZE="-1">SSL</font> certificate verification. See &lt;<a rel="nofollow" href="http://curl.haxx.se/docs/sslcerts.html">http://curl.haxx.se/docs/sslcerts.html</a>&gt; for details. Enabled by default.</p>
<dt><code>VerifyHost</code> <code>true|false</code></p>
<dd>Enable or disable peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a <font SIZE="-1">SSL</font> enabled server. Enabled by default.</p>
<dt><code>CACert</code> <i>File</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">HTTPS</font> you will possibly need this option. What <font SIZE="-1">CA</font> certificates come bundled with <tt>&quot;libcurl&quot;</tt> and are checked by default depends on the distribution you use.</p>
<dt><code>SSLCiphers</code> <i>list of ciphers</i></p>
<dd>Specifies which ciphers to use in the connection. The list of ciphers must specify valid ciphers. See &lt;<a rel="nofollow" href="http://www.openssl.org/docs/apps/ciphers.html">http://www.openssl.org/docs/apps/ciphers.html</a>&gt; for details.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the overall timeout for <font SIZE="-1">HTTP</font> requests to <font SIZE="-1"><code>URL</code></font>, in milliseconds. By default, the configured <code>Interval</code> is used to set the timeout.</dl>
<h3>Plugin apcups</h3>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname of the host running <code>apcupsd</code>. Defaults to <code>localhost</code>. Please note that IPv6 support has been disabled unless someone can confirm or decline that <code>apcupsd</code> can handle it.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>TCP-Port to connect to. Defaults to <code>3551</code>.</p>
<dt><code>ReportSeconds</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, the time reported in the <tt>&quot;timeleft&quot;</tt> metric will be converted to seconds. This is the recommended setting. If set to <code>false</code>, the default for backwards compatibility, the time will be reported in minutes.</p>
<dt><code>PersistentConnection</code> <code>true</code>|<code>false</code></p>
<dd>The plugin is designed to keep the connection to <i>apcupsd</i> open between reads. If plugin poll interval is greater than 15 seconds (hardcoded socket close timeout in <i>apcupsd</i> <font SIZE="-1">NIS</font>), then this option is <code>false</code> by default. </p>
<p> You can instruct the plugin to close the connection after each read by setting this option to <code>false</code> or force keeping the connection by setting it to <code>true</code>. </p>
<p> If <i>apcupsd</i> appears to close the connection due to inactivity quite quickly, the plugin will try to detect this problem and switch to an open-read-close mode.</dl>
<h3>Plugin aquaero</h3>
<p>This plugin collects the value of the available sensors in an <i>Aquaero 5</i> board. Aquaero 5 is a water-cooling controller board, manufactured by Aqua Computer GmbH &lt;<a rel="nofollow" href="http://www.aquacomputer.de/">http://www.aquacomputer.de/</a>&gt;, with a <font SIZE="-1">USB2</font> connection for monitoring and configuration. The board can handle multiple temperature sensors, fans, water pumps and water level sensors and adjust the output settings such as fan voltage or power used by the water pump based on the available inputs using a configurable controller included in the board. This plugin collects all the available inputs as well as some of the output values chosen by this controller. The plugin is based on the <i>libaquaero5</i> library provided by <i>aquatools-ng</i>.</p>
<dl>
<dt><code>Device</code> <i>DevicePath</i></p>
<dd>Device path of the Aquaero 5&#8217;s <font SIZE="-1">USB HID </font>(human interface device), usually in the form <tt>&quot;/dev/usb/hiddevX&quot;</tt>. If this option is no set the plugin will try to auto-detect the Aquaero 5 <font SIZE="-1">USB</font> device based on vendor-ID and product-ID.</dl>
<h3>Plugin ascent</h3>
<p>This plugin collects information about an Ascent server, a free server for the &#8220;World of Warcraft&#8221; game. This plugin gathers the information by fetching the <font SIZE="-1">XML</font> status page using <tt>&quot;libcurl&quot;</tt> and parses it using <tt>&quot;libxml2&quot;</tt>. </p>
<p> The configuration options are the same as for the <tt>&quot;apache&quot;</tt> plugin above:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i><a rel="nofollow" href="http://localhost/ascent/status/">http://localhost/ascent/status/</a></i></p>
<dd>Sets the <font SIZE="-1">URL</font> of the <font SIZE="-1">XML</font> status output.</p>
<dt><code>User</code> <i>Username</i></p>
<dd>Optional user name needed for authentication.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Optional password needed for authentication.</p>
<dt><code>VerifyPeer</code> <code>true|false</code></p>
<dd>Enable or disable peer <font SIZE="-1">SSL</font> certificate verification. See &lt;<a rel="nofollow" href="http://curl.haxx.se/docs/sslcerts.html">http://curl.haxx.se/docs/sslcerts.html</a>&gt; for details. Enabled by default.</p>
<dt><code>VerifyHost</code> <code>true|false</code></p>
<dd>Enable or disable peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a <font SIZE="-1">SSL</font> enabled server. Enabled by default.</p>
<dt><code>CACert</code> <i>File</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">HTTPS</font> you will possibly need this option. What <font SIZE="-1">CA</font> certificates come bundled with <tt>&quot;libcurl&quot;</tt> and are checked by default depends on the distribution you use.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the overall timeout for <font SIZE="-1">HTTP</font> requests to <font SIZE="-1"><code>URL</code></font>, in milliseconds. By default, the configured <code>Interval</code> is used to set the timeout.</dl>
<h3>Plugin barometer</h3>
<p>This plugin reads absolute air pressure using digital barometer sensor on a I2C bus. Supported sensors are:</p>
<dl>
<dt><i></i><font SIZE="-1"><i>MPL115A2</i></font><i></i> from Freescale, see &lt;<a rel="nofollow" href="http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MPL115A">http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MPL115A</a>&gt;.</p>
<dd>
<dt><i></i><font SIZE="-1"><i>MPL3115</i></font><i></i> from Freescale see &lt;<a rel="nofollow" href="http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MPL3115A2">http://www.freescale.com/webapp/sps/site/prod_summary.jsp?code=MPL3115A2</a>&gt;.</p>
<dd>
<dt><i></i><font SIZE="-1"><i>BMP085</i></font><i></i> from Bosch Sensortec</p>
<dd></dl>
<p> The sensor type &#8211; one of the above &#8211; is detected automatically by the plugin and indicated in the plugin_instance (you will see subdirectory &#8220;barometer-mpl115&#8221; or &#8220;barometer-mpl3115&#8221;, or &#8220;barometer-bmp085&#8221;). The order of detection is <font SIZE="-1">BMP085 &#8211;</font>&gt; <font SIZE="-1">MPL3115 &#8211;</font>&gt; <font SIZE="-1">MPL115A2,</font> the first one found will be used (only one sensor can be used by the plugin). </p>
<p> The plugin provides absolute barometric pressure, air pressure reduced to sea level (several possible approximations) and as an auxiliary value also internal sensor temperature. It uses (expects/provides) typical metric units &#8211; pressure in [hPa], temperature in [C], altitude in [m]. </p>
<p> It was developed and tested under Linux only. The only platform dependency is the standard Linux i2c-dev interface (the particular bus driver has to support the <font SIZE="-1">SM</font> Bus command subset). </p>
<p> The reduction or normalization to mean sea level pressure requires (depending on selected method/approximation) also altitude and reference to temperature sensor(s). When multiple temperature sensors are configured the minimum of their values is always used (expecting that the warmer ones are affected by e.g. direct sun light at that moment). </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;barometer&quot;&gt;
 Device &quot;/dev/i2c-0&quot;;
 Oversampling 512
 PressureOffset 0.0
 TemperatureOffset 0.0
 Normalization 2
 Altitude 238.0
 TemperatureSensor &quot;myserver/onewire-F10FCA000800/temperature&quot;
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>Device</code> <i>device</i></p>
<dd>The only mandatory configuration parameter. </p>
<p> Device name of the I2C bus to which the sensor is connected. Note that typically you need to have loaded the i2c-dev module. Using i2c-tools you can check/list i2c buses available on your system by: </p>
<pre> i2cdetect -l</pre>
<p>Then you can scan for devices on given bus. E.g. to scan the whole bus 0 use: </p>
<pre> i2cdetect -y -a 0</pre>
<p>This way you should be able to verify that the pressure sensor (either type) is connected and detected on address 0x60.</p>
<dt><code>Oversampling</code> <i>value</i></p>
<dd>Optional parameter controlling the oversampling/accuracy. Default value is 1 providing fastest and least accurate reading. </p>
<p> For <i></i><font SIZE="-1"><i>MPL115</i></font><i></i> this is the size of the averaging window. To filter out sensor noise a simple averaging using floating window of this configurable size is used. The plugin will use average of the last <tt>&quot;value&quot;</tt> measurements (value of 1 means no averaging). Minimal size is 1, maximal 1024. </p>
<p> For <i></i><font SIZE="-1"><i>MPL3115</i></font><i></i> this is the oversampling value. The actual oversampling is performed by the sensor and the higher value the higher accuracy and longer conversion time (although nothing to worry about in the collectd context). Supported values are: 1, 2, 4, 8, 16, 32, 64 and 128. Any other value is adjusted by the plugin to the closest supported one. </p>
<p> For <i></i><font SIZE="-1"><i>BMP085</i></font><i></i> this is the oversampling value. The actual oversampling is performed by the sensor and the higher value the higher accuracy and longer conversion time (although nothing to worry about in the collectd context). Supported values are: 1, 2, 4, 8. Any other value is adjusted by the plugin to the closest supported one.</p>
<dt><code>PressureOffset</code> <i>offset</i></p>
<dd>Optional parameter for <font SIZE="-1">MPL3115</font> only. </p>
<p> You can further calibrate the sensor by supplying pressure and/or temperature offsets. This is added to the measured/caclulated value (i.e. if the measured value is too high then use negative offset). In hPa, default is 0.0.</p>
<dt><code>TemperatureOffset</code> <i>offset</i></p>
<dd>Optional parameter for <font SIZE="-1">MPL3115</font> only. </p>
<p> You can further calibrate the sensor by supplying pressure and/or temperature offsets. This is added to the measured/caclulated value (i.e. if the measured value is too high then use negative offset). In C, default is 0.0.</p>
<dt><code>Normalization</code> <i>method</i></p>
<dd>Optional parameter, default value is 0. </p>
<p> Normalization method &#8211; what approximation/model is used to compute the mean sea level pressure from the air absolute pressure. </p>
<p> Supported values of the <tt>&quot;method&quot;</tt> (integer between from 0 to 2) are:</p>
<dl>
<dd>
<dl>
<dt><code>0</code> &#8211; no conversion, absolute pressure is simply copied over. For this method you do not need to configure &quot;Altitude&quot; or &quot;TemperatureSensor&quot;.</p>
<dd>
<dt><code>1</code> &#8211; international formula for conversion , See &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_atmospheric_pressure_variation">http://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_atmospheric_pressure_variation</a>&gt;. For this method you have to configure &quot;Altitude&quot; but do not need &quot;TemperatureSensor&quot; (uses fixed global temperature average instead).</p>
<dd>
<dt><code>2</code> &#8211; formula as recommended by the Deutsche Wetterdienst (German Meteorological Service). See &lt;<a rel="nofollow" href="http://de.wikipedia.org/wiki/Barometrische_H%C3%B6henformel#Theorie">http://de.wikipedia.org/wiki/Barometrische_H%C3%B6henformel#Theorie</a>&gt; For this method you have to configure both &quot;Altitude&quot; and &quot;TemperatureSensor&quot;.</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>Altitude</code> <i>altitude</i></p>
<dd>The altitude (in meters) of the location where you meassure the pressure.</p>
<dt><code>TemperatureSensor</code> <i>reference</i></p>
<dd>Temperature sensor(s) which should be used as a reference when normalizing the pressure using <tt>&quot;Normalization&quot;</tt> method 2. When specified more sensors a minimum is found and used each time. The temperature reading directly from this pressure sensor/plugin is typically not suitable as the pressure sensor will be probably inside while we want outside temperature. The collectd reference name is something like &lt;hostname&gt;/&lt;plugin_name&gt;-&lt;plugin_instance&gt;/&lt;type&gt;-&lt;type_instance&gt; (&lt;type_instance&gt; is usually omitted when there is just single value type). Or you can figure it out from the path of the output data files.</dl>
<h3>Plugin battery</h3>
<p>The <i>battery plugin</i> reports the remaining capacity, power and voltage of laptop batteries.</p>
<dl>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, remaining capacity is reported as a percentage, e.g. &#8220;42% capacity remaining&#8221;. Otherwise the capacity is stored as reported by the battery, most likely in &#8220;Wh&#8221;. This option does not work with all input methods, in particular when only <tt>&quot;/proc/pmu&quot;</tt> is available on an old Linux system. Defaults to <code>false</code>.</p>
<dt><code>ReportDegraded</code> <code>false</code>|<code>true</code></p>
<dd>Typical laptop batteries degrade over time, meaning the capacity decreases with recharge cycles. The maximum charge of the previous charge cycle is tracked as &#8220;last full capacity&#8221; and used to determine that a battery is &#8220;fully charged&#8221;. </p>
<p> When this option is set to <code>false</code>, the default, the <i>battery plugin</i> will only report the remaining capacity. If the <code>ValuesPercentage</code> option is enabled, the relative remaining capacity is calculated as the ratio of the &#8220;remaining capacity&#8221; and the &#8220;last full capacity&#8221;. This is what most tools, such as the status bar of desktop environments, also do. </p>
<p> When set to <code>true</code>, the battery plugin will report three values: <code>charged</code> (remaining capacity), <code>discharged</code> (difference between &#8220;last full capacity&#8221; and &#8220;remaining capacity&#8221;) and <code>degraded</code> (difference between &#8220;design capacity&#8221; and &#8220;last full capacity&#8221;).</p>
<dt><code>QueryStateFS</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>true</code>, the battery plugin will only read statistics related to battery performance as exposed by StateFS at /run/state. StateFS is used in Mer-based Sailfish <font SIZE="-1">OS,</font> for example.</dl>
<h3>Plugin bind</h3>
<p>Starting with <font SIZE="-1">BIND 9.5.0,</font> the most widely used <font SIZE="-1">DNS</font> server software provides extensive statistics about queries, responses and lots of other information. The bind plugin retrieves this information that&#8217;s encoded in <font SIZE="-1">XML</font> and provided via <font SIZE="-1">HTTP</font> and submits the values to collectd. </p>
<p> To use this plugin, you first need to tell <font SIZE="-1">BIND</font> to make this information available. This is done with the <tt>&quot;statistics-channels&quot;</tt> configuration option: </p>
<pre> statistics-channels {
 inet localhost port 8053;
 };</pre>
<p>The configuration follows the grouping that can be seen when looking at the data with an <font SIZE="-1">XSLT</font> compatible viewer, such as a modern web browser. It&#8217;s probably a good idea to make yourself familiar with the provided values, so you can understand what the collected statistics actually mean. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;bind&quot;&gt;
 URL &quot;<a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a>&quot;
 ParseTime false
 OpCodes true
 QTypes true
 ServerStats true
 ZoneMaintStats true
 ResolverStats false
 MemoryStats true
 &lt;View &quot;_default&quot;&gt;
 QTypes true
 ResolverStats true
 CacheRRSets true
 Zone &quot;127.in-addr.arpa/IN&quot;
 &lt;/View&gt;
 &lt;/Plugin&gt;</pre>
<p>The bind plugin accepts the following configuration options:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd><font SIZE="-1">URL</font> from which to retrieve the <font SIZE="-1">XML</font> data. If not specified, <tt>&quot;<a rel="nofollow" href="http://localhost:8053/">http://localhost:8053/</a>&quot;</tt> will be used.</p>
<dt><code>ParseTime</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, the time provided by <font SIZE="-1">BIND</font> will be parsed and used to dispatch the values. When set to <code>false</code>, the local time source is queried. </p>
<p> This setting is set to <code>true</code> by default for backwards compatibility; setting this to <code>false</code> is <i>recommended</i> to avoid problems with timezones and localization.</p>
<dt><code>OpCodes</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, statistics about the <i>&#8220;OpCodes&#8221;</i>, for example the number of <tt>&quot;QUERY&quot;</tt> packets, are collected. </p>
<p> Default: Enabled.</p>
<dt><code>QTypes</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the number of <i>incoming</i> queries by query types (for example <tt>&quot;A&quot;</tt>, <tt>&quot;MX&quot;</tt>, <tt>&quot;AAAA&quot;</tt>) is collected. </p>
<p> Default: Enabled.</p>
<dt><code>ServerStats</code> <code>true</code>|<code>false</code></p>
<dd>Collect global server statistics, such as requests received over IPv4 and IPv6, successful queries, and failed updates. </p>
<p> Default: Enabled.</p>
<dt><code>ZoneMaintStats</code> <code>true</code>|<code>false</code></p>
<dd>Collect zone maintenance statistics, mostly information about notifications (zone updates) and zone transfers. </p>
<p> Default: Enabled.</p>
<dt><code>ResolverStats</code> <code>true</code>|<code>false</code></p>
<dd>Collect resolver statistics, i. e. statistics about outgoing requests (e. g. queries over IPv4, lame servers). Since the global resolver counters apparently were removed in <font SIZE="-1">BIND 9.5.1</font> and 9.6.0, this is disabled by default. Use the <code>ResolverStats</code> option within a <code>View &#8220;_default&#8221;</code> block instead for the same functionality. </p>
<p> Default: Disabled.</p>
<dt><code>MemoryStats</code></p>
<dd>Collect global memory statistics. </p>
<p> Default: Enabled.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the overall timeout for <font SIZE="-1">HTTP</font> requests to <font SIZE="-1"><code>URL</code></font>, in milliseconds. By default, the configured <code>Interval</code> is used to set the timeout.</p>
<dt><code>View</code> <i>Name</i></p>
<dd>Collect statistics about a specific <i>&#8220;view&#8221;</i>. <font SIZE="-1">BIND</font> can behave different, mostly depending on the source IP-address of the request. These different configurations are called &#8220;views&#8221;. If you don&#8217;t use this feature, you most likely are only interested in the <tt>&quot;_default&quot;</tt> view. </p>
<p> Within a &lt;<code>View</code>&nbsp;<wbr><i>name</i>&gt; block, you can specify which information you want to collect about a view. If no <code>View</code> block is configured, no detailed view statistics will be collected.</p>
<dl>
<dd>
<dl>
<dt><code>QTypes</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, the number of <i>outgoing</i> queries by query type (e. g. <tt>&quot;A&quot;</tt>, <tt>&quot;MX&quot;</tt>) is collected. </p>
<p> Default: Enabled.</p>
<dt><code>ResolverStats</code> <code>true</code>|<code>false</code></p>
<dd>Collect resolver statistics, i. e. statistics about outgoing requests (e. g. queries over IPv4, lame servers). </p>
<p> Default: Enabled.</p>
<dt><code>CacheRRSets</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, the number of entries (<i>&#8220;</i><font SIZE="-1"><i>RR</i></font><i> sets&#8221;</i>) in the view&#8217;s cache by query type is collected. Negative entries (queries which resulted in an error, for example names that do not exist) are reported with a leading exclamation mark, e. g. &#8220;!A&#8221;. </p>
<p> Default: Enabled.</p>
<dt><code>Zone</code> <i>Name</i></p>
<dd>When given, collect detailed information about the given zone in the view. The information collected if very similar to the global <code>ServerStats</code> information (see above). </p>
<p> You can repeat this option to collect detailed information about multiple zones. </p>
<p> By default no detailed zone information is collected.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin ceph</h3>
<p>The ceph plugin collects values from <font SIZE="-1">JSON</font> data to be parsed by <code>libyajl</code> (&lt;<a rel="nofollow" href="https://lloyd.github.io/yajl/">https://lloyd.github.io/yajl/</a>&gt;) retrieved from ceph daemon admin sockets. </p>
<p> A separate <code>Daemon</code> block must be configured for each ceph daemon to be monitored. The following example will read daemon statistics from four separate ceph daemons running on the same device (two OSDs, one <font SIZE="-1">MON,</font> one <font SIZE="-1">MDS</font>) : </p>
<pre> &lt;Plugin ceph&gt;
 LongRunAvgLatency false
 ConvertSpecialMetricTypes true
 &lt;Daemon &quot;osd.0&quot;&gt;
 SocketPath &quot;/var/run/ceph/ceph-osd.0.asok&quot;
 &lt;/Daemon&gt;
 &lt;Daemon &quot;osd.1&quot;&gt;
 SocketPath &quot;/var/run/ceph/ceph-osd.1.asok&quot;
 &lt;/Daemon&gt;
 &lt;Daemon &quot;mon.a&quot;&gt;
 SocketPath &quot;/var/run/ceph/ceph-mon.ceph1.asok&quot;
 &lt;/Daemon&gt;
 &lt;Daemon &quot;mds.a&quot;&gt;
 SocketPath &quot;/var/run/ceph/ceph-mds.ceph1.asok&quot;
 &lt;/Daemon&gt;
 &lt;/Plugin&gt;</pre>
<p>The ceph plugin accepts the following configuration options:</p>
<dl>
<dt><code>LongRunAvgLatency</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, latency values(sum,count pairs) are calculated as the long run average &#8211; average since the ceph daemon was started = (sum / count). When disabled, latency values are calculated as the average since the last collection = (sum_now &#8211; sum_last) / (count_now &#8211; count_last). </p>
<p> Default: Disabled</p>
<dt><code>ConvertSpecialMetricTypes</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, special metrics (metrics that differ in type from similar counters) are converted to the type of those similar counters. This currently only applies to filestore.journal_wr_bytes which is a counter for <font SIZE="-1">OSD</font> daemons. The ceph schema reports this metric type as a sum,count pair while similar counters are treated as derive types. When converted, the sum is used as the counter value and is treated as a derive type. When disabled, all metrics are treated as the types received from the ceph schema. </p>
<p> Default: Enabled</dl>
<p> Each <code>Daemon</code> block must have a string argument for the plugin instance name. A <code>SocketPath</code> is also required for each <code>Daemon</code> block:</p>
<dl>
<dt><code>Daemon</code> <i>DaemonName</i></p>
<dd>Name to be used as the instance name for this daemon.</p>
<dt><code>SocketPath</code> <i>SocketPath</i></p>
<dd>Specifies the path to the <font SIZE="-1">UNIX</font> admin socket of the ceph daemon.</dl>
<h3>Plugin cgroups</h3>
<p>This plugin collects the <font SIZE="-1">CPU</font> user/system time for each <i>cgroup</i> by reading the <i>cpuacct.stat</i> files in the first cpuacct-mountpoint (typically <i>/sys/fs/cgroup/cpu.cpuacct</i> on machines using systemd).</p>
<dl>
<dt><code>CGroup</code> <i>Directory</i></p>
<dd>Select <i>cgroup</i> based on the name. Whether only matching <i>cgroups</i> are collected or if they are ignored is controlled by the <code>IgnoreSelected</code> option; see below.</p>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Invert the selection: If set to true, all cgroups <i>except</i> the ones that match any one of the criteria are collected. By default only selected cgroups are collected if a selection is made. If no selection is configured at all, <code>all</code> cgroups are selected.</dl>
<h3>Plugin chrony</h3>
<p>The <tt>&quot;chrony&quot;</tt> plugin collects ntp data from a <code>chronyd</code> server, such as clock skew and per-peer stratum. </p>
<p> For talking to <code>chronyd</code>, it mimics what the <code>chronyc</code> control program does on the wire. </p>
<p> Available configuration options for the <tt>&quot;chrony&quot;</tt> plugin:</p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname of the host running <code>chronyd</code>. Defaults to <code>localhost</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>UDP-Port to connect to. Defaults to <code>323</code>.</p>
<dt><code>Timeout</code> <i>Timeout</i></p>
<dd>Connection timeout in seconds. Defaults to <code>2</code>.</dl>
<h3>Plugin conntrack</h3>
<p>This plugin collects <font SIZE="-1">IP</font> conntrack statistics.</p>
<dl>
<dt><code>OldFiles</code></p>
<dd>Assume the <code>conntrack_count</code> and <code>conntrack_max</code> files to be found in <i>/proc/sys/net/ipv4/netfilter</i> instead of <i>/proc/sys/net/netfilter/</i>.</dl>
<h3>Plugin cpu</h3>
<p>The <i></i><font SIZE="-1"><i>CPU</i></font><i> plugin</i> collects <font SIZE="-1">CPU</font> usage metrics. By default, <font SIZE="-1">CPU</font> usage is reported as Jiffies, using the <tt>&quot;cpu&quot;</tt> type. Two aggregations are available:</p>
<dl>
<dt>&bull;</p>
<dd>Sum, per-state, over all CPUs installed in the system; and</p>
<dt>&bull;</p>
<dd>Sum, per-CPU, over all non-idle states of a <font SIZE="-1">CPU,</font> creating an &#8220;active&#8221; state.</dl>
<p> The two aggregations can be combined, leading to <i>collectd</i> only emitting a single &#8220;active&#8221; metric for the entire system. As soon as one of these aggregations (or both) is enabled, the <i>cpu plugin</i> will report a percentage, rather than Jiffies. In addition, you can request individual, per-state, per-CPU metrics to be reported as percentage. </p>
<p> The following configuration options are available:</p>
<dl>
<dt><code>ReportByState</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, the default, reports per-state metrics, e.g. &#8220;system&#8221;, &#8220;user&#8221; and &#8220;idle&#8221;. When set to <code>false</code>, aggregates (sums) all <i>non-idle</i> states into one &#8220;active&#8221; metric.</p>
<dt><code>ReportByCpu</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, the default, reports per-CPU (per-core) metrics. When set to <code>false</code>, instead of reporting metrics for individual CPUs, only a global sum of <font SIZE="-1">CPU</font> states is emitted.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>This option is only considered when both, <code>ReportByCpu</code> and <code>ReportByState</code> are set to <code>true</code>. In this case, by default, metrics will be reported as Jiffies. By setting this option to <code>true</code>, you can request percentage values in the un-aggregated (per-CPU, per-state) mode as well.</p>
<dt><code>ReportNumCpu</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>true</code>, reports the number of available CPUs. Defaults to <code>false</code>.</dl>
<h3>Plugin cpufreq</h3>
<p>This plugin doesn&#8217;t have any options. It reads <i>/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq</i> (for the first <font SIZE="-1">CPU</font> installed) to get the current <font SIZE="-1">CPU</font> frequency. If this file does not exist make sure <code>cpufreqd</code> (&lt;<a rel="nofollow" href="http://cpufreqd.sourceforge.net/">http://cpufreqd.sourceforge.net/</a>&gt;) or a similar tool is installed and an &#8220;cpu governor&#8221; (that&#8217;s a kernel module) is loaded.</p>
<h3>Plugin cpusleep</h3>
<p>This plugin doesn&#8217;t have any options. It reads <font SIZE="-1">CLOCK_BOOTTIME</font> and <font SIZE="-1">CLOCK_MONOTONIC</font> and reports the difference between these clocks. Since <font SIZE="-1">BOOTTIME</font> clock increments while device is suspended and <font SIZE="-1">MONOTONIC</font> clock does not, the derivative of the difference between these clocks gives the relative amount of time the device has spent in suspend state. The recorded value is in milliseconds of sleep per seconds of wall clock.</p>
<h3>Plugin csv</h3>
<dl>
<dt><code>DataDir</code> <i>Directory</i></p>
<dd>Set the directory to store CSV-files under. Per default CSV-files are generated beneath the daemon&#8217;s working directory, i. e. the <code>BaseDir</code>. The special strings <code>stdout</code> and <code>stderr</code> can be used to write to the standard output and standard error channels, respectively. This, of course, only makes much sense when collectd is running in foreground- or non-daemon-mode.</p>
<dt><code>StoreRates</code> <code>true|false</code></p>
<dd>If set to <code>true</code>, convert counter values to rates. If set to <code>false</code> (the default) counter values are stored as is, i. e. as an increasing integer number.</dl>
<h3>cURL Statistics</h3>
<p>All cURL-based plugins support collection of generic, request-based statistics. These are disabled by default and can be enabled selectively for each page or <font SIZE="-1">URL</font> queried from the curl, curl_json, or curl_xml plugins. See the documentation of those plugins for specific information. This section describes the available metrics that can be configured for each plugin. All options are disabled by default. </p>
<p> See &lt;<a rel="nofollow" href="http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html">http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html</a>&gt; for more details.</p>
<dl>
<dt><code>TotalTime</code> <code>true|false</code></p>
<dd>Total time of the transfer, including name resolving, <font SIZE="-1">TCP</font> connect, etc.</p>
<dt><code>NamelookupTime</code> <code>true|false</code></p>
<dd>Time it took from the start until name resolving was completed.</p>
<dt><code>ConnectTime</code> <code>true|false</code></p>
<dd>Time it took from the start until the connect to the remote host (or proxy) was completed.</p>
<dt><code>AppconnectTime</code> <code>true|false</code></p>
<dd>Time it took from the start until the <font SIZE="-1">SSL/SSH</font> connect/handshake to the remote host was completed.</p>
<dt><code>PretransferTime</code> <code>true|false</code></p>
<dd>Time it took from the start until just before the transfer begins.</p>
<dt><code>StarttransferTime</code> <code>true|false</code></p>
<dd>Time it took from the start until the first byte was received.</p>
<dt><code>RedirectTime</code> <code>true|false</code></p>
<dd>Time it took for all redirection steps include name lookup, connect, pre-transfer and transfer before final transaction was started.</p>
<dt><code>RedirectCount</code> <code>true|false</code></p>
<dd>The total number of redirections that were actually followed.</p>
<dt><code>SizeUpload</code> <code>true|false</code></p>
<dd>The total amount of bytes that were uploaded.</p>
<dt><code>SizeDownload</code> <code>true|false</code></p>
<dd>The total amount of bytes that were downloaded.</p>
<dt><code>SpeedDownload</code> <code>true|false</code></p>
<dd>The average download speed that curl measured for the complete download.</p>
<dt><code>SpeedUpload</code> <code>true|false</code></p>
<dd>The average upload speed that curl measured for the complete upload.</p>
<dt><code>HeaderSize</code> <code>true|false</code></p>
<dd>The total size of all the headers received.</p>
<dt><code>RequestSize</code> <code>true|false</code></p>
<dd>The total size of the issued requests.</p>
<dt><code>ContentLengthDownload</code> <code>true|false</code></p>
<dd>The content-length of the download.</p>
<dt><code>ContentLengthUpload</code> <code>true|false</code></p>
<dd>The specified size of the upload.</p>
<dt><code>NumConnects</code> <code>true|false</code></p>
<dd>The number of new connections that were created to achieve the transfer.</dl>
<h3>Plugin curl</h3>
<p>The curl plugin uses the <code>libcurl</code> (&lt;<a rel="nofollow" href="http://curl.haxx.se/">http://curl.haxx.se/</a>&gt;) to read web pages and the match infrastructure (the same code used by the tail plugin) to use regular expressions with the received data. </p>
<p> The following example will read the current value of <font SIZE="-1">AMD</font> stock from Google&#8217;s finance page and dispatch the value to collectd. </p>
<pre> &lt;Plugin curl&gt;
 &lt;Page &quot;stock_quotes&quot;&gt;
 URL &quot;<a rel="nofollow" href="http://finance.google.com/finance?q=NYSE%3AAMD">http://finance.google.com/finance?q=NYSE%3AAMD</a>&quot;
 User &quot;foo&quot;
 Password &quot;bar&quot;
 Digest false
 VerifyPeer true
 VerifyHost true
 CACert &quot;/path/to/ca.crt&quot;
 Header &quot;X-Custom-Header: foobar&quot;
 Post &quot;foo=bar&quot;
 MeasureResponseTime false
 MeasureResponseCode false
 &lt;Match&gt;
 Regex &quot;&lt;span +class=\&quot;pr\&quot;[^&gt;]*&gt; *([0-9]*\.[0-9]+) *&lt;/span&gt;&quot;
 DSType &quot;GaugeAverage&quot;
 # Note: `stock_value' is not a standard type.
 Type &quot;stock_value&quot;
 Instance &quot;AMD&quot;
 &lt;/Match&gt;
 &lt;/Page&gt;
 &lt;/Plugin&gt;</pre>
<p>In the <code>Plugin</code> block, there may be one or more <code>Page</code> blocks, each defining a web page and one or more &#8220;matches&#8221; to be performed on the returned data. The string argument to the <code>Page</code> block is used as plugin instance. </p>
<p> The following options are valid within <code>Page</code> blocks:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd><font SIZE="-1">URL</font> of the web site to retrieve. Since a regular expression will be used to extract information from this data, non-binary data is a big plus here ;)</p>
<dt><code>User</code> <i>Name</i></p>
<dd>Username to use if authorization is required to read the page.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Password to use if authorization is required to read the page.</p>
<dt><code>Digest</code> <code>true</code>|<code>false</code></p>
<dd>Enable <font SIZE="-1">HTTP</font> digest authentication.</p>
<dt><code>VerifyPeer</code> <code>true</code>|<code>false</code></p>
<dd>Enable or disable peer <font SIZE="-1">SSL</font> certificate verification. See &lt;<a rel="nofollow" href="http://curl.haxx.se/docs/sslcerts.html">http://curl.haxx.se/docs/sslcerts.html</a>&gt; for details. Enabled by default.</p>
<dt><code>VerifyHost</code> <code>true</code>|<code>false</code></p>
<dd>Enable or disable peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a <font SIZE="-1">SSL</font> enabled server. Enabled by default.</p>
<dt><code>CACert</code> <i>file</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">HTTPS</font> you will possibly need this option. What <font SIZE="-1">CA</font> certificates come bundled with <tt>&quot;libcurl&quot;</tt> and are checked by default depends on the distribution you use.</p>
<dt><code>Header</code> <i>Header</i></p>
<dd>A <font SIZE="-1">HTTP</font> header to add to the request. Multiple headers are added if this option is specified more than once.</p>
<dt><code>Post</code> <i>Body</i></p>
<dd>Specifies that the <font SIZE="-1">HTTP</font> operation should be a <font SIZE="-1">POST</font> instead of a <font SIZE="-1">GET.</font> The complete data to be posted is given as the argument. This option will usually need to be accompanied by a <code>Header</code> option to set an appropriate <tt>&quot;Content-Type&quot;</tt> for the post body (e.g. to <tt>&quot;application/x-www-form-urlencoded&quot;</tt>).</p>
<dt><code>MeasureResponseTime</code> <code>true</code>|<code>false</code></p>
<dd>Measure response time for the request. If this setting is enabled, <code>Match</code> blocks (see below) are optional. Disabled by default. </p>
<p> Beware that requests will get aborted if they take too long to complete. Adjust <code>Timeout</code> accordingly if you expect <code>MeasureResponseTime</code> to report such slow requests. </p>
<p> This option is similar to enabling the <code>TotalTime</code> statistic but it&#8217;s measured by collectd instead of cURL.</p>
<dt><code>MeasureResponseCode</code> <code>true</code>|<code>false</code></p>
<dd>Measure response code for the request. If this setting is enabled, <code>Match</code> blocks (see below) are optional. Disabled by default.</p>
<dt><code>&lt;Statistics&gt;</code></p>
<dd>One <code>Statistics</code> block can be used to specify cURL statistics to be collected for each request to the remote web site. See the section &#8220;cURL Statistics&#8221; above for details. If this setting is enabled, <code>Match</code> blocks (see below) are optional.</p>
<dt><code>&lt;Match&gt;</code></p>
<dd>One or more <code>Match</code> blocks that define how to match information in the data returned by <tt>&quot;libcurl&quot;</tt>. The <tt>&quot;curl&quot;</tt> plugin uses the same infrastructure that&#8217;s used by the <tt>&quot;tail&quot;</tt> plugin, so please see the documentation of the <tt>&quot;tail&quot;</tt> plugin below on how matches are defined. If the <code>MeasureResponseTime</code> or <code>MeasureResponseCode</code> options are set to <code>true</code>, <code>Match</code> blocks are optional.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the overall timeout for <font SIZE="-1">HTTP</font> requests to <font SIZE="-1"><code>URL</code></font>, in milliseconds. By default, the configured <code>Interval</code> is used to set the timeout. Prior to version 5.5.0, there was no timeout and requests could hang indefinitely. This legacy behaviour can be achieved by setting the value of <code>Timeout</code> to 0. </p>
<p> If <code>Timeout</code> is 0 or bigger than the <code>Interval</code>, keep in mind that each slow network connection will stall one read thread. Adjust the <code>ReadThreads</code> global setting accordingly to prevent this from blocking other plugins.</dl>
<h3>Plugin curl_json</h3>
<p>The <code>curl_json plugin</code> collects values from <font SIZE="-1">JSON</font> data to be parsed by <code>libyajl</code> (&lt;<a rel="nofollow" href="https://lloyd.github.io/yajl/">https://lloyd.github.io/yajl/</a>&gt;) retrieved via either <code>libcurl</code> (&lt;<a rel="nofollow" href="http://curl.haxx.se/">http://curl.haxx.se/</a>&gt;) or read directly from a unix socket. The former can be used, for example, to collect values from CouchDB documents (which are stored <font SIZE="-1">JSON</font> notation), and the latter to collect values from a uWSGI stats socket. </p>
<p> The following example will collect several values from the built-in <tt>&quot;_stats&quot;</tt> runtime statistics module of <i>CouchDB</i> (&lt;<a rel="nofollow" href="http://wiki.apache.org/couchdb/Runtime_Statistics">http://wiki.apache.org/couchdb/Runtime_Statistics</a>&gt;). </p>
<pre> &lt;Plugin curl_json&gt;
 &lt;URL &quot;<a rel="nofollow" href="http://localhost:5984/_stats">http://localhost:5984/_stats</a>&quot;&gt;
 Instance &quot;httpd&quot;
 &lt;Key &quot;httpd/requests/count&quot;&gt;
 Type &quot;http_requests&quot;
 &lt;/Key&gt;
 &lt;Key &quot;httpd_request_methods/*/count&quot;&gt;
 Type &quot;http_request_methods&quot;
 &lt;/Key&gt;
 &lt;Key &quot;httpd_status_codes/*/count&quot;&gt;
 Type &quot;http_response_codes&quot;
 &lt;/Key&gt;
 &lt;/URL&gt;
 &lt;/Plugin&gt;</pre>
<p>This example will collect data directly from a <i>uWSGI</i> &#8220;Stats Server&#8221; socket. </p>
<pre> &lt;Plugin curl_json&gt;
 &lt;Sock &quot;/var/run/uwsgi.stats.sock&quot;&gt;
 Instance &quot;uwsgi&quot;
 &lt;Key &quot;workers/*/requests&quot;&gt;
 Type &quot;http_requests&quot;
 &lt;/Key&gt;
 &lt;Key &quot;workers/*/apps/*/requests&quot;&gt;
 Type &quot;http_requests&quot;
 &lt;/Key&gt;
 &lt;/Sock&gt;
 &lt;/Plugin&gt;</pre>
<p>In the <code>Plugin</code> block, there may be one or more <font SIZE="-1"><code>URL</code></font> blocks, each defining a <font SIZE="-1">URL</font> to be fetched via <font SIZE="-1">HTTP </font>(using libcurl) or <code>Sock</code> blocks defining a unix socket to read <font SIZE="-1">JSON</font> from directly. Each of these blocks may have one or more <code>Key</code> blocks. </p>
<p> The <code>Key</code> string argument must be in a path format. Each component is used to match the key from a <font SIZE="-1">JSON</font> map or the index of an <font SIZE="-1">JSON</font> array. If a path component of a <code>Key</code> is a <i>*</i>&nbsp;<wbr>wildcard, the values for all map keys or array indices will be collectd. </p>
<p> The following options are valid within <font SIZE="-1"><code>URL</code></font> blocks:</p>
<dl>
<dt><code>Host</code> <i>Name</i></p>
<dd>Use <i>Name</i> as the host name when submitting values. Defaults to the global host name setting.</p>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Sets the plugin instance to <i>Instance</i>.</p>
<dt><code>Interval</code> <i>Interval</i></p>
<dd>Sets the interval (in seconds) in which the values will be collected from this <font SIZE="-1">URL.</font> By default the global <code>Interval</code> setting will be used.</p>
<dt><code>User</code> <i>Name</i></p>
<dd>
<dt><code>Password</code> <i>Password</i></p>
<dd>
<dt><code>Digest</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>VerifyPeer</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>VerifyHost</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CACert</code> <i>file</i></p>
<dd>
<dt><code>Header</code> <i>Header</i></p>
<dd>
<dt><code>Post</code> <i>Body</i></p>
<dd>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>These options behave exactly equivalent to the appropriate options of the <i>cURL</i> plugin. Please see there for a detailed description.</p>
<dt><code>&lt;Statistics&gt;</code></p>
<dd>One <code>Statistics</code> block can be used to specify cURL statistics to be collected for each request to the remote <font SIZE="-1">URL.</font> See the section &#8220;cURL Statistics&#8221; above for details.</dl>
<p> The following options are valid within <code>Key</code> blocks:</p>
<dl>
<dt><code>Type</code> <i>Type</i></p>
<dd>Sets the type used to dispatch the values to the daemon. Detailed information about types and their configuration can be found in <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5). This option is mandatory.</p>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Type-instance to use. Defaults to the current map key or current string array element value.</dl>
<h3>Plugin curl_xml</h3>
<p>The <code>curl_xml plugin</code> uses <code>libcurl</code> (&lt;<a rel="nofollow" href="http://curl.haxx.se/">http://curl.haxx.se/</a>&gt;) and <code>libxml2</code> (&lt;<a rel="nofollow" href="http://xmlsoft.org/">http://xmlsoft.org/</a>&gt;) to retrieve <font SIZE="-1">XML</font> data via cURL. </p>
<pre> &lt;Plugin &quot;curl_xml&quot;&gt;
 &lt;URL &quot;<a rel="nofollow" href="http://localhost/stats.xml">http://localhost/stats.xml</a>&quot;&gt;
 Host &quot;my_host&quot;
 Instance &quot;some_instance&quot;
 User &quot;collectd&quot;
 Password &quot;thaiNg0I&quot;
 VerifyPeer true
 VerifyHost true
 CACert &quot;/path/to/ca.crt&quot;
 Header &quot;X-Custom-Header: foobar&quot;
 Post &quot;foo=bar&quot;
 &lt;XPath &quot;table[@id=\&quot;magic_level\&quot;]/tr&quot;&gt;
 Type &quot;magic_level&quot;
 #InstancePrefix &quot;prefix-&quot;
 InstanceFrom &quot;td[1]&quot;
 ValuesFrom &quot;td[2]/span[@class=\&quot;level\&quot;]&quot;
 &lt;/XPath&gt;
 &lt;/URL&gt;
 &lt;/Plugin&gt;</pre>
<p>In the <code>Plugin</code> block, there may be one or more <font SIZE="-1"><code>URL</code></font> blocks, each defining a <font SIZE="-1">URL</font> to be fetched using libcurl. Within each <font SIZE="-1"><code>URL</code></font> block there are options which specify the connection parameters, for example authentication information, and one or more <code>XPath</code> blocks. </p>
<p> Each <code>XPath</code> block specifies how to get one type of information. The string argument must be a valid XPath expression which returns a list of &#8220;base elements&#8221;. One value is dispatched for each &#8220;base element&#8221;. The <i>type instance</i> and values are looked up using further <i>XPath</i> expressions that should be relative to the base element. </p>
<p> Within the <font SIZE="-1"><code>URL</code></font> block the following options are accepted:</p>
<dl>
<dt><code>Host</code> <i>Name</i></p>
<dd>Use <i>Name</i> as the host name when submitting values. Defaults to the global host name setting.</p>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Use <i>Instance</i> as the plugin instance when submitting values. Defaults to an empty string (no plugin instance).</p>
<dt><code>Namespace</code> <i>Prefix</i> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd>If an XPath expression references namespaces, they must be specified with this option. <i>Prefix</i> is the &#8220;namespace prefix&#8221; used in the <font SIZE="-1">XML</font> document. <i></i><font SIZE="-1"><i>URL</i></font><i></i> is the &#8220;namespace name&#8221;, an <font SIZE="-1">URI</font> reference uniquely identifying the namespace. The option can be repeated to register multiple namespaces. </p>
<p> Examples: </p>
<pre> Namespace &quot;s&quot; &quot;<a rel="nofollow" href="http://schemas.xmlsoap.org/soap/envelope/">http://schemas.xmlsoap.org/soap/envelope/</a>&quot;
 Namespace &quot;m&quot; &quot;<a rel="nofollow" href="http://www.w3.org/1998/Math/MathML">http://www.w3.org/1998/Math/MathML</a>&quot;</pre>
<dt><code>User</code> <i>User</i></p>
<dd>
<dt><code>Password</code> <i>Password</i></p>
<dd>
<dt><code>Digest</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>VerifyPeer</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>VerifyHost</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>CACert</code> <i></i><font SIZE="-1"><i>CA</i></font><i> Cert File</i></p>
<dd>
<dt><code>Header</code> <i>Header</i></p>
<dd>
<dt><code>Post</code> <i>Body</i></p>
<dd>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>These options behave exactly equivalent to the appropriate options of the <i>cURL plugin</i>. Please see there for a detailed description.</p>
<dt><code>&lt;Statistics&gt;</code></p>
<dd>One <code>Statistics</code> block can be used to specify cURL statistics to be collected for each request to the remote <font SIZE="-1">URL.</font> See the section &#8220;cURL Statistics&#8221; above for details.</p>
<dt>&lt;<code>XPath</code> <i>XPath-expression</i>&gt;</p>
<dd>Within each <font SIZE="-1"><code>URL</code></font> block, there must be one or more <code>XPath</code> blocks. Each <code>XPath</code> block specifies how to get one type of information. The string argument must be a valid XPath expression which returns a list of &#8220;base elements&#8221;. One value is dispatched for each &#8220;base element&#8221;. </p>
<p> Within the <code>XPath</code> block the following options are accepted:</p>
<dl>
<dd>
<dl>
<dt><code>Type</code> <i>Type</i></p>
<dd>Specifies the <i>Type</i> used for submitting patches. This determines the number of values that are required / expected and whether the strings are parsed as signed or unsigned integer or as double values. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for details. This option is required.</p>
<dt><code>InstancePrefix</code> <i>InstancePrefix</i></p>
<dd>Prefix the <i>type instance</i> with <i>InstancePrefix</i>. The values are simply concatenated together without any separator. This option is optional.</p>
<dt><code>InstanceFrom</code> <i>InstanceFrom</i></p>
<dd>Specifies a XPath expression to use for determining the <i>type instance</i>. The XPath expression must return exactly one element. The element&#8217;s value is then used as <i>type instance</i>, possibly prefixed with <i>InstancePrefix</i> (see above). </p>
<p> This value is required. As a special exception, if the &#8220;base XPath expression&#8221; (the argument to the <code>XPath</code> block) returns exactly one argument, then this option may be omitted.</p>
<dt><code>ValuesFrom</code> <i>ValuesFrom</i> [<i>ValuesFrom</i> &#8230;]</p>
<dd>Specifies one or more XPath expression to use for reading the values. The number of XPath expressions must match the number of data sources in the <i>type</i> specified with <code>Type</code> (see above). Each XPath expression must return exactly one element. The element&#8217;s value is then parsed as a number and used as value for the appropriate value in the value list dispatched to the daemon.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin dbi</h3>
<p>This plugin uses the <code>dbi</code> library (&lt;<a rel="nofollow" href="http://libdbi.sourceforge.net/">http://libdbi.sourceforge.net/</a>&gt;) to connect to various databases, execute <i></i><font SIZE="-1"><i>SQL</i></font><i></i> statements and read back the results. <i>dbi</i> is an acronym for &#8220;database interface&#8221; in case you were wondering about the name. You can configure how each column is to be interpreted and the plugin will generate one or more data sets from each row returned according to these rules. </p>
<p> Because the plugin is very generic, the configuration is a little more complex than those of other plugins. It usually looks something like this: </p>
<pre> &lt;Plugin dbi&gt;
 &lt;Query &quot;out_of_stock&quot;&gt;
 Statement &quot;SELECT category, COUNT(*) AS value FROM products WHERE in_stock = 0 GROUP BY category&quot;
 # Use with MySQL 5.0.0 or later
 MinVersion 50000
 &lt;Result&gt;
 Type &quot;gauge&quot;
 InstancePrefix &quot;out_of_stock&quot;
 InstancesFrom &quot;category&quot;
 ValuesFrom &quot;value&quot;
 &lt;/Result&gt;
 &lt;/Query&gt;
 &lt;Database &quot;product_information&quot;&gt;
 Driver &quot;mysql&quot;
 Interval 120
 DriverOption &quot;host&quot; &quot;localhost&quot;
 DriverOption &quot;username&quot; &quot;collectd&quot;
 DriverOption &quot;password&quot; &quot;aZo6daiw&quot;
 DriverOption &quot;dbname&quot; &quot;prod_info&quot;
 SelectDB &quot;prod_info&quot;
 Query &quot;out_of_stock&quot;
 &lt;/Database&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration above defines one query with one result and one database. The query is then linked to the database with the <code>Query</code> option <i>within</i> the <code>&lt;Database&gt;</code> block. You can have any number of queries and databases and you can also use the <code>Include</code> statement to split up the configuration file in multiple, smaller files. However, the <code>&lt;Query&gt;</code> block <i>must</i> precede the <code>&lt;Database&gt;</code> blocks, because the file is interpreted from top to bottom! </p>
<p> The following is a complete list of options: </p>
<p> <i></i>Query<i> blocks</i> </p>
<p> Query blocks define <i></i><font SIZE="-1"><i>SQL</i></font><i></i> statements and how the returned data should be interpreted. They are identified by the name that is given in the opening line of the block. Thus the name needs to be unique. Other than that, the name is not used in collectd. </p>
<p> In each <code>Query</code> block, there is one or more <code>Result</code> blocks. <code>Result</code> blocks define which column holds which value or instance information. You can use multiple <code>Result</code> blocks to create multiple values from one returned row. This is especially useful, when queries take a long time and sending almost the same query again and again is not desirable. </p>
<p> Example: </p>
<pre> &lt;Query &quot;environment&quot;&gt;
 Statement &quot;select station, temperature, humidity from environment&quot;
 &lt;Result&gt;
 Type &quot;temperature&quot;
 # InstancePrefix &quot;foo&quot;
 InstancesFrom &quot;station&quot;
 ValuesFrom &quot;temperature&quot;
 &lt;/Result&gt;
 &lt;Result&gt;
 Type &quot;humidity&quot;
 InstancesFrom &quot;station&quot;
 ValuesFrom &quot;humidity&quot;
 &lt;/Result&gt;
 &lt;/Query&gt;</pre>
<p>The following options are accepted:</p>
<dl>
<dt><code>Statement</code> <i></i><font SIZE="-1"><i>SQL</i></font><i></i></p>
<dd>Sets the statement that should be executed on the server. This is <code>not</code> interpreted by collectd, but simply passed to the database server. Therefore, the <font SIZE="-1">SQL</font> dialect that&#8217;s used depends on the server collectd is connected to. </p>
<p> The query has to return at least two columns, one for the instance and one value. You cannot omit the instance, even if the statement is guaranteed to always return exactly one line. In that case, you can usually specify something like this: </p>
<pre> Statement &quot;SELECT \&quot;instance\&quot;, COUNT(*) AS value FROM table&quot;</pre>
<p>(That works with MySQL but may not be valid <font SIZE="-1">SQL</font> according to the spec. If you use a more strict database server, you may have to select from a dummy table or something.) </p>
<p> Please note that some databases, for example <code>Oracle</code>, will fail if you include a semicolon at the end of the statement.</p>
<dt><code>MinVersion</code> <i>Version</i></p>
<dd>
<dt><code>MaxVersion</code> <i>Value</i></p>
<dd>Only use this query for the specified database version. You can use these options to provide multiple queries with the same name but with a slightly different syntax. The plugin will use only those queries, where the specified minimum and maximum versions fit the version of the database in use. </p>
<p> The database version is determined by <tt>&quot;dbi_conn_get_engine_version&quot;</tt>, see the libdbi documentation &lt;<a rel="nofollow" href="http://libdbi.sourceforge.net/docs/programmers-guide/reference-conn.html#DBI-CONN-GET-ENGINE-VERSION">http://libdbi.sourceforge.net/docs/programmers-guide/reference-conn.html#DBI-CONN-GET-ENGINE-VERSION</a>&gt; for details. Basically, each part of the version is assumed to be in the range from <code>00</code> to <code>99</code> and all dots are removed. So version &#8220;4.1.2&#8221; becomes &#8220;40102&#8221;, version &#8220;5.0.42&#8221; becomes &#8220;50042&#8221;. </p>
<p> <code>Warning:</code> The plugin will use <code>all</code> matching queries, so if you specify multiple queries with the same name and <code>overlapping</code> ranges, weird stuff will happen. Don&#8217;t to it! A valid example would be something along these lines: </p>
<pre> MinVersion 40000
 MaxVersion 49999
 ...
 MinVersion 50000
 MaxVersion 50099
 ...
 MinVersion 50100
 # No maximum</pre>
<p>In the above example, there are three ranges that don&#8217;t overlap. The last one goes from version &#8220;5.1.0&#8221; to infinity, meaning &#8220;all later versions&#8221;. Versions before &#8220;4.0.0&#8221; are not specified.</p>
<dt><code>Type</code> <i>Type</i></p>
<dd>The <code>type</code> that&#8217;s used for each line returned. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for more details on how types are defined. In short: A type is a predefined layout of data and the number of values and type of values has to match the type definition. </p>
<p> If you specify &#8220;temperature&#8221; here, you need exactly one gauge column. If you specify &#8220;if_octets&#8221;, you will need two counter columns. See the <code>ValuesFrom</code> setting below. </p>
<p> There must be exactly one <code>Type</code> option inside each <code>Result</code> block.</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>Prepends <i>prefix</i> to the type instance. If <code>InstancesFrom</code> (see below) is not given, the string is simply copied. If <code>InstancesFrom</code> is given, <i>prefix</i> and all strings returned in the appropriate columns are concatenated together, separated by dashes <i>(&#8220;-&#8221;)</i>.</p>
<dt><code>InstancesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>Specifies the columns whose values will be used to create the &#8220;type-instance&#8221; for each row. If you specify more than one column, the value of all columns will be joined together with dashes <i>(&#8220;-&#8221;)</i> as separation characters. </p>
<p> The plugin itself does not check whether or not all built instances are different. It&#8217;s your responsibility to assure that each is unique. This is especially true, if you do not specify <code>InstancesFrom</code>: <code>You</code> have to make sure that only one row is returned in this case. </p>
<p> If neither <code>InstancePrefix</code> nor <code>InstancesFrom</code> is given, the type-instance will be empty.</p>
<dt><code>ValuesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>Names the columns whose content is used as the actual data for the data sets that are dispatched to the daemon. How many such columns you need is determined by the <code>Type</code> setting above. If you specify too many or not enough columns, the plugin will complain about that and no data will be submitted to the daemon. </p>
<p> The actual data type in the columns is not that important. The plugin will automatically cast the values to the right type if it know how to do that. So it should be able to handle integer an floating point types, as well as strings (if they include a number at the beginning). </p>
<p> There must be at least one <code>ValuesFrom</code> option inside each <code>Result</code> block.</p>
<dt><code>MetadataFrom</code> [<i>column0</i> <i>column1</i> &#8230;]</p>
<dd>Names the columns whose content is used as metadata for the data sets that are dispatched to the daemon. </p>
<p> The actual data type in the columns is not that important. The plugin will automatically cast the values to the right type if it know how to do that. So it should be able to handle integer an floating point types, as well as strings (if they include a number at the beginning).</dl>
<p> <i></i>Database<i> blocks</i> </p>
<p> Database blocks define a connection to a database and which queries should be sent to that database. Since the used &#8220;dbi&#8221; library can handle a wide variety of databases, the configuration is very generic. If in doubt, refer to libdbi&#8217;s documentation &#8211; we stick as close to the terminology used there. </p>
<p> Each database needs a &#8220;name&#8221; as string argument in the starting tag of the block. This name will be used as &#8220;PluginInstance&#8221; in the values submitted to the daemon. Other than that, that name is not used.</p>
<dl>
<dt><code>Interval</code> <i>Interval</i></p>
<dd>Sets the interval (in seconds) in which the values will be collected from this database. By default the global <code>Interval</code> setting will be used.</p>
<dt><code>Driver</code> <i>Driver</i></p>
<dd>Specifies the driver to use to connect to the database. In many cases those drivers are named after the database they can connect to, but this is not a technical necessity. These drivers are sometimes referred to as &#8220;<font SIZE="-1">DBD&#8221;, </font><code>D</code>ata<code>B</code>ase <code>D</code>river, and some distributions ship them in separate packages. Drivers for the &#8220;dbi&#8221; library are developed by the <code>libdbi-drivers</code> project at &lt;<a rel="nofollow" href="http://libdbi-drivers.sourceforge.net/">http://libdbi-drivers.sourceforge.net/</a>&gt;. </p>
<p> You need to give the driver name as expected by the &#8220;dbi&#8221; library here. You should be able to find that in the documentation for each driver. If you mistype the driver name, the plugin will dump a list of all known driver names to the log.</p>
<dt><code>DriverOption</code> <i>Key</i> <i>Value</i></p>
<dd>Sets driver-specific options. What option a driver supports can be found in the documentation for each driver, somewhere at &lt;<a rel="nofollow" href="http://libdbi-drivers.sourceforge.net/">http://libdbi-drivers.sourceforge.net/</a>&gt;. However, the options &#8220;host&#8221;, &#8220;username&#8221;, &#8220;password&#8221;, and &#8220;dbname&#8221; seem to be de facto standards. </p>
<p> DBDs can register two types of options: String options and numeric options. The plugin will use the <tt>&quot;dbi_conn_set_option&quot;</tt> function when the configuration provides a string and the <tt>&quot;dbi_conn_require_option_numeric&quot;</tt> function when the configuration provides a number. So these two lines will actually result in different calls being used: </p>
<pre> DriverOption &quot;Port&quot; 1234 # numeric
 DriverOption &quot;Port&quot; &quot;1234&quot; # string</pre>
<p>Unfortunately, drivers are not too keen to report errors when an unknown option is passed to them, so invalid settings here may go unnoticed. This is not the plugin&#8217;s fault, it will report errors if it gets them from the library&nbsp;<wbr>/ the driver. If a driver complains about an option, the plugin will dump a complete list of all options understood by that driver to the log. There is no way to programmatically find out if an option expects a string or a numeric argument, so you will have to refer to the appropriate <font SIZE="-1">DBD</font>&#8216;s documentation to find this out. Sorry.</p>
<dt><code>SelectDB</code> <i>Database</i></p>
<dd>In some cases, the database name you connect with is not the database name you want to use for querying data. If this option is set, the plugin will &#8220;select&#8221; (switch to) that database after the connection is established.</p>
<dt><code>Query</code> <i>QueryName</i></p>
<dd>Associates the query named <i>QueryName</i> with this database connection. The query needs to be defined <i>before</i> this statement, i. e. all query blocks you want to refer to must be placed above the database block you want to refer to them from.</p>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Sets the <code>host</code> field of <i>value lists</i> to <i>Hostname</i> when dispatching values. Defaults to the global hostname setting.</dl>
<h3>Plugin df</h3>
<dl>
<dt><code>Device</code> <i>Device</i></p>
<dd>Select partitions based on the devicename.</p>
<dt><code>MountPoint</code> <i>Directory</i></p>
<dd>Select partitions based on the mountpoint.</p>
<dt><code>FSType</code> <i>FSType</i></p>
<dd>Select partitions based on the filesystem type.</p>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Invert the selection: If set to true, all partitions <code>except</code> the ones that match any one of the criteria are collected. By default only selected partitions are collected if a selection is made. If no selection is configured at all, <code>all</code> partitions are selected.</p>
<dt><code>ReportByDevice</code> <code>true</code>|<code>false</code></p>
<dd>Report using the device name rather than the mountpoint. i.e. with this <i>false</i>, (the default), it will report a disk as &#8220;root&#8221;, but with it <i>true</i>, it will be &#8220;sda1&#8221; (or whichever).</p>
<dt><code>ReportInodes</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables reporting of free, reserved and used inodes. Defaults to inode collection being disabled. </p>
<p> Enable this option if inodes are a scarce resource for you, usually because many small files are stored on the disk. This is a usual scenario for mail transfer agents and web caches.</p>
<dt><code>ValuesAbsolute</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables reporting of free and used disk space in 1K-blocks. Defaults to <code>true</code>.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>Enables or disables reporting of free and used disk space in percentage. Defaults to <code>false</code>. </p>
<p> This is useful for deploying <i>collectd</i> on the cloud, where machines with different disk size may exist. Then it is more practical to configure thresholds based on relative disk size.</dl>
<h3>Plugin disk</h3>
<p>The <tt>&quot;disk&quot;</tt> plugin collects information about the usage of physical disks and logical disks (partitions). Values collected are the number of octets written to and read from a disk or partition, the number of read/write operations issued to the disk and a rather complex &#8220;time&#8221; it took for these commands to be issued. </p>
<p> Using the following two options you can ignore some disks or configure the collection only of specific disks.</p>
<dl>
<dt><code>Disk</code> <i>Name</i></p>
<dd>Select the disk <i>Name</i>. Whether it is collected or ignored depends on the <code>IgnoreSelected</code> setting, see below. As with other plugins that use the daemon&#8217;s ignorelist functionality, a string that starts and ends with a slash is interpreted as a regular expression. Examples: </p>
<pre> Disk &quot;sdd&quot;
 Disk &quot;/hda[34]/&quot;</pre>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Sets whether selected disks, i. e. the ones matches by any of the <code>Disk</code> statements, are ignored or if all other disks are ignored. The behavior (hopefully) is intuitive: If no <code>Disk</code> option is configured, all disks are collected. If at least one <code>Disk</code> option is given and no <code>IgnoreSelected</code> or set to <code>false</code>, <code>only</code> matching disks will be collected. If <code>IgnoreSelected</code> is set to <code>true</code>, all disks are collected <code>except</code> the ones matched.</p>
<dt><code>UseBSDName</code> <code>true</code>|<code>false</code></p>
<dd>Whether to use the device&#8217;s &#8220;<font SIZE="-1">BSD</font> Name&#8221;, on Mac&nbsp;<wbr><font SIZE="-1">OS</font>&nbsp;<wbr>X, instead of the default major/minor numbers. Requires collectd to be built with Apple&#8217;s IOKitLib support.</p>
<dt><code>UdevNameAttr</code> <i>Attribute</i></p>
<dd>Attempt to override disk instance name with the value of a specified udev attribute when built with <code>libudev</code>. If the attribute is not defined for the given device, the default name is used. Example: </p>
<pre> UdevNameAttr &quot;DM_NAME&quot;</pre>
</dl>
<h3>Plugin dns</h3>
<dl>
<dt><code>Interface</code> <i>Interface</i></p>
<dd>The dns plugin uses <code>libpcap</code> to capture dns traffic and analyzes it. This option sets the interface that should be used. If this option is not set, or set to &#8220;any&#8221;, the plugin will try to get packets from <code>all</code> interfaces. This may not work on certain platforms, such as Mac&nbsp;<wbr><font SIZE="-1">OS</font>&nbsp;<wbr>X.</p>
<dt><code>IgnoreSource</code> <i>IP-address</i></p>
<dd>Ignore packets that originate from this address.</p>
<dt><code>SelectNumericQueryTypes</code> <code>true</code>|<code>false</code></p>
<dd>Enabled by default, collects unknown (and thus presented as numeric only) query types.</dl>
<h3>Plugin dpdkstat</h3>
<p>The <i>dpdkstat plugin</i> collects information about <font SIZE="-1">DPDK</font> interfaces using the extended <font SIZE="-1">NIC</font> stats <font SIZE="-1">API</font> in <font SIZE="-1">DPDK.</font> </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;dpdkstat&quot;&gt;
 Coremask &quot;0x4&quot;
 MemoryChannels &quot;4&quot;
 ProcessType &quot;secondary&quot;
 FilePrefix &quot;rte&quot;
 EnabledPortMask 0xffff
 PortName &quot;interface1&quot;
 PortName &quot;interface2&quot;
 &lt;/Plugin&gt;</pre>
<p><code>Options:</code></p>
<dl>
<dt><code>Coremask</code> <i>Mask</i></p>
<dd>A string containing an hexadecimal bit mask of the cores to run on. Note that core numbering can change between platforms and should be determined beforehand.</p>
<dt><code>Memorychannels</code> <i>Channels</i></p>
<dd>A string containing a number of memory channels per processor socket.</p>
<dt><code>ProcessType</code> <i>type</i></p>
<dd>A string containing the type of <font SIZE="-1">DPDK</font> process instance.</p>
<dt><code>FilePrefix</code> <i>File</i></p>
<dd>The prefix text used for hugepage filenames. The filename will be set to /var/run/.&lt;prefix&gt;_config where prefix is what is passed in by the user.</p>
<dt><code>SocketMemory</code> <i></i><font SIZE="-1"><i>MB</i></font><i></i></p>
<dd>A string containing amount of Memory to allocate from hugepages on specific sockets in <font SIZE="-1">MB</font></p>
<dt><code>EnabledPortMask</code> <i>Mask</i></p>
<dd>A hexidecimal bit mask of the <font SIZE="-1">DPDK</font> ports which should be enabled. A mask of 0x0 means that all ports will be disabled. A bitmask of all Fs means that all ports will be enabled. This is an optional argument &#8211; default is all ports enabled.</p>
<dt><code>PortName</code> <i>Name</i></p>
<dd>A string containing an optional name for the enabled <font SIZE="-1">DPDK</font> ports. Each PortName option should contain only one port name; specify as many PortName options as desired. Default naming convention will be used if PortName is blank. If there are less PortName options than there are enabled ports, the default naming convention will be used for the additional ports.</dl>
<h3>Plugin email</h3>
<dl>
<dt><code>SocketFile</code> <i>Path</i></p>
<dd>Sets the socket-file which is to be created.</p>
<dt><code>SocketGroup</code> <i>Group</i></p>
<dd>If running as root change the group of the UNIX-socket after it has been created. Defaults to <code>collectd</code>.</p>
<dt><code>SocketPerms</code> <i>Permissions</i></p>
<dd>Change the file permissions of the UNIX-socket after it has been created. The permissions must be given as a numeric, octal value as you would pass to <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). Defaults to <code>0770</code>.</p>
<dt><code>MaxConns</code> <i>Number</i></p>
<dd>Sets the maximum number of connections that can be handled in parallel. Since this many threads will be started immediately setting this to a very high value will waste valuable resources. Defaults to <code>5</code> and will be forced to be at most <code>16384</code> to prevent typos and dumb mistakes.</dl>
<h3>Plugin ethstat</h3>
<p>The <i>ethstat plugin</i> collects information about network interface cards (NICs) by talking directly with the underlying kernel driver using <i><a href="/docs/linux/man/2-ioctl/">ioctl</a></i>(2). </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;ethstat&quot;&gt;
 Interface &quot;eth0&quot;
 Map &quot;rx_csum_offload_errors&quot; &quot;if_rx_errors&quot; &quot;checksum_offload&quot;
 Map &quot;multicast&quot; &quot;if_multicast&quot;
 &lt;/Plugin&gt;</pre>
<p><code>Options:</code></p>
<dl>
<dt><code>Interface</code> <i>Name</i></p>
<dd>Collect statistical information about interface <i>Name</i>.</p>
<dt><code>Map</code> <i>Name</i> <i>Type</i> [<i>TypeInstance</i>]</p>
<dd>By default, the plugin will submit values as type <tt>&quot;derive&quot;</tt> and <i>type instance</i> set to <i>Name</i>, the name of the metric as reported by the driver. If an appropriate <code>Map</code> option exists, the given <i>Type</i> and, optionally, <i>TypeInstance</i> will be used.</p>
<dt><code>MappedOnly</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, only metrics that can be mapped to a <i>type</i> will be collected, all other metrics will be ignored. Defaults to <code>false</code>.</dl>
<h3>Plugin exec</h3>
<p>Please make sure to read <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5) before using this plugin. It contains valuable information on when the executable is executed and the output that is expected from it.</p>
<dl>
<dt><code>Exec</code> <i>User</i>[:[<i>Group</i>]] <i>Executable</i> [<i>&lt;arg&gt;</i> [<i>&lt;arg&gt;</i> &#8230;]]</p>
<dd>
<dt><code>NotificationExec</code> <i>User</i>[:[<i>Group</i>]] <i>Executable</i> [<i>&lt;arg&gt;</i> [<i>&lt;arg&gt;</i> &#8230;]]</p>
<dd>Execute the executable <i>Executable</i> as user <i>User</i>. If the user name is followed by a colon and a group name, the effective group is set to that group. The real group and saved-set group will be set to the default group of that user. If no group is given the effective group <font SIZE="-1">ID</font> will be the same as the real group <font SIZE="-1">ID.</font> </p>
<p> Please note that in order to change the user and/or group the daemon needs superuser privileges. If the daemon is run as an unprivileged user you must specify the same user/group here. If the daemon is run with superuser privileges, you must supply a non-root user here. </p>
<p> The executable may be followed by optional arguments that are passed to the program. Please note that due to the configuration parsing numbers and boolean values may be changed. If you want to be absolutely sure that something is passed as-is please enclose it in quotes. </p>
<p> The <code>Exec</code> and <code>NotificationExec</code> statements change the semantics of the programs executed, i. e. the data passed to them and the response expected from them. This is documented in great detail in <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5).</dl>
<h3>Plugin fhcount</h3>
<p>The <tt>&quot;fhcount&quot;</tt> plugin provides statistics about used, unused and total number of file handles on Linux. </p>
<p> The <i>fhcount plugin</i> provides the following configuration options:</p>
<dl>
<dt><code>ValuesAbsolute</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables reporting of file handles usage in absolute numbers, e.g. file handles used. Defaults to <code>true</code>.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>Enables or disables reporting of file handles usage in percentages, e.g. percent of file handles used. Defaults to <code>false</code>.</dl>
<h3>Plugin filecount</h3>
<p>The <tt>&quot;filecount&quot;</tt> plugin counts the number of files in a certain directory (and its subdirectories) and their combined size. The configuration is very straight forward: </p>
<pre> &lt;Plugin &quot;filecount&quot;&gt;
 &lt;Directory &quot;/var/qmail/queue/mess&quot;&gt;
 Instance &quot;qmail-message&quot;
 &lt;/Directory&gt;
 &lt;Directory &quot;/var/qmail/queue/todo&quot;&gt;
 Instance &quot;qmail-todo&quot;
 &lt;/Directory&gt;
 &lt;Directory &quot;/var/lib/php5&quot;&gt;
 Instance &quot;php5-sessions&quot;
 Name &quot;sess_*&quot;
 &lt;/Directory&gt;
 &lt;/Plugin&gt;</pre>
<p>The example above counts the number of files in QMail&#8217;s queue directories and the number of <font SIZE="-1">PHP5</font> sessions. Jfiy: The &#8220;todo&#8221; queue holds the messages that QMail has not yet looked at, the &#8220;message&#8221; queue holds the messages that were classified into &#8220;local&#8221; and &#8220;remote&#8221;. </p>
<p> As you can see, the configuration consists of one or more <tt>&quot;Directory&quot;</tt> blocks, each of which specifies a directory in which to count the files. Within those blocks, the following options are recognized:</p>
<dl>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Sets the plugin instance to <i>Instance</i>. That instance name must be unique, but it&#8217;s your responsibility, the plugin doesn&#8217;t check for that. If not given, the instance is set to the directory name with all slashes replaced by underscores and all leading underscores removed.</p>
<dt><code>Name</code> <i>Pattern</i></p>
<dd>Only count files that match <i>Pattern</i>, where <i>Pattern</i> is a shell-like wildcard as understood by <i><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></i>(3). Only the <code>filename</code> is checked against the pattern, not the entire path. In case this makes it easier for you: This option has been named after the <code>-name</code> parameter to <i><a href="/docs/linux/man/1-find/">find</a></i>(1).</p>
<dt><code>MTime</code> <i>Age</i></p>
<dd>Count only files of a specific age: If <i>Age</i> is greater than zero, only files that haven&#8217;t been touched in the last <i>Age</i> seconds are counted. If <i>Age</i> is a negative number, this is inversed. For example, if <code>-60</code> is specified, only files that have been modified in the last minute will be counted. </p>
<p> The number can also be followed by a &#8220;multiplier&#8221; to easily specify a larger timespan. When given in this notation, the argument must in quoted, i. e. must be passed as string. So the <code>-60</code> could also be written as <code>&#8220;-1m&#8221;</code> (one minute). Valid multipliers are <tt>&quot;s&quot;</tt> (second), <tt>&quot;m&quot;</tt> (minute), <tt>&quot;h&quot;</tt> (hour), <tt>&quot;d&quot;</tt> (day), <tt>&quot;w&quot;</tt> (week), and <tt>&quot;y&quot;</tt> (year). There is no &#8220;month&#8221; multiplier. You can also specify fractional numbers, e. g. <code>&#8220;0.5d&#8221;</code> is identical to <code>&#8220;12h&#8221;</code>.</p>
<dt><code>Size</code> <i>Size</i></p>
<dd>Count only files of a specific size. When <i>Size</i> is a positive number, only files that are at least this big are counted. If <i>Size</i> is a negative number, this is inversed, i. e. only files smaller than the absolute value of <i>Size</i> are counted. </p>
<p> As with the <code>MTime</code> option, a &#8220;multiplier&#8221; may be added. For a detailed description see above. Valid multipliers here are <tt>&quot;b&quot;</tt> (byte), <tt>&quot;k&quot;</tt> (kilobyte), <tt>&quot;m&quot;</tt> (megabyte), <tt>&quot;g&quot;</tt> (gigabyte), <tt>&quot;t&quot;</tt> (terabyte), and <tt>&quot;p&quot;</tt> (petabyte). Please note that there are 1000 bytes in a kilobyte, not 1024.</p>
<dt><code>Recursive</code> <i>true</i>|<i>false</i></p>
<dd>Controls whether or not to recurse into subdirectories. Enabled by default.</p>
<dt><code>IncludeHidden</code> <i>true</i>|<i>false</i></p>
<dd>Controls whether or not to include &#8220;hidden&#8221; files and directories in the count. &#8220;Hidden&#8221; files and directories are those, whose name begins with a dot. Defaults to <i>false</i>, i.e. by default hidden files and directories are ignored.</dl>
<h3>Plugin GenericJMX</h3>
<p>The <i>GenericJMX plugin</i> is written in <i>Java</i> and therefore documented in <i><a href="/docs/linux/man/5-collectd-java/">collectd-java</a></i>(5).</p>
<h3>Plugin gmond</h3>
<p>The <i>gmond</i> plugin received the multicast traffic sent by <code>gmond</code>, the statistics collection daemon of Ganglia. Mappings for the standard &#8220;metrics&#8221; are built-in, custom mappings may be added via <code>Metric</code> blocks, see below. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;gmond&quot;&gt;
 MCReceiveFrom &quot;239.2.11.71&quot; &quot;8649&quot;
 &lt;Metric &quot;swap_total&quot;&gt;
 Type &quot;swap&quot;
 TypeInstance &quot;total&quot;
 DataSource &quot;value&quot;
 &lt;/Metric&gt;
 &lt;Metric &quot;swap_free&quot;&gt;
 Type &quot;swap&quot;
 TypeInstance &quot;free&quot;
 DataSource &quot;value&quot;
 &lt;/Metric&gt;
 &lt;/Plugin&gt;</pre>
<p>The following metrics are built-in:</p>
<dl>
<dt>&bull;</p>
<dd>load_one, load_five, load_fifteen</p>
<dt>&bull;</p>
<dd>cpu_user, cpu_system, cpu_idle, cpu_nice, cpu_wio</p>
<dt>&bull;</p>
<dd>mem_free, mem_shared, mem_buffers, mem_cached, mem_total</p>
<dt>&bull;</p>
<dd>bytes_in, bytes_out</p>
<dt>&bull;</p>
<dd>pkts_in, pkts_out</dl>
<p> Available configuration options:</p>
<dl>
<dt><code>MCReceiveFrom</code> <i>MCGroup</i> [<i>Port</i>]</p>
<dd>Sets sets the multicast group and <font SIZE="-1">UDP</font> port to which to subscribe. </p>
<p> Default: <code>239.2.11.71</code>&nbsp;<wbr>/&nbsp;<wbr><code>8649</code></p>
<dt>&lt;<code>Metric</code> <i>Name</i>&gt;</p>
<dd>These blocks add a new metric conversion to the internal table. <i>Name</i>, the string argument to the <code>Metric</code> block, is the metric name as used by Ganglia.</p>
<dl>
<dd>
<dl>
<dt><code>Type</code> <i>Type</i></p>
<dd>Type to map this metric to. Required.</p>
<dt><code>TypeInstance</code> <i>Instance</i></p>
<dd>Type-instance to use. Optional.</p>
<dt><code>DataSource</code> <i>Name</i></p>
<dd>Data source to map this metric to. If the configured type has exactly one data source, this is optional. Otherwise the option is required.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin gps</h3>
<p>The <tt>&quot;gps plugin&quot;</tt> connects to gpsd on the host machine. The host, port, timeout and pause are configurable. </p>
<p> This is useful if you run an <font SIZE="-1">NTP</font> server using a <font SIZE="-1">GPS</font> for source and you want to monitor it. </p>
<p> Mind your <font SIZE="-1">GPS</font> must send $&#8211;GSA for having the data reported! </p>
<p> The following elements are collected:</p>
<dl>
<dt><code>satellites</code></p>
<dd>Number of satellites used for fix (type instance &#8220;used&#8221;) and in view (type instance &#8220;visible&#8221;). 0 means no <font SIZE="-1">GPS</font> satellites are visible.</p>
<dt><code>dilution_of_precision</code></p>
<dd>Vertical and horizontal dilution (type instance &#8220;horizontal&#8221; or &#8220;vertical&#8221;). It should be between 0 and 3. Look at the documentation of your <font SIZE="-1">GPS</font> to know more.</dl>
<p> Synopsis: </p>
<pre> LoadPlugin gps
 &lt;Plugin &quot;gps&quot;&gt;
 # Connect to localhost on gpsd regular port:
 Host &quot;127.0.0.1&quot;
 Port &quot;2947&quot;
 # 15 ms timeout
 Timeout 0.015
 # PauseConnect of 5 sec. between connection attempts.
 PauseConnect 5
 &lt;/Plugin&gt;</pre>
<p>Available configuration options:</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>The host on which gpsd daemon runs. Defaults to <code>localhost</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>Port to connect to gpsd on the host machine. Defaults to <code>2947</code>.</p>
<dt><code>Timeout</code> <i>Seconds</i></p>
<dd>Timeout in seconds (default 0.015 sec). </p>
<p> The <font SIZE="-1">GPS</font> data stream is fetch by the plugin form the daemon. It waits for data to be available, if none arrives it times out and loop for another reading. Mind to put a low value gpsd expects value in the micro-seconds area (recommended is 500 us) since the waiting function is blocking. Value must be between 500 us and 5 sec., if outside that range the default value is applied. </p>
<p> This only applies from gpsd release-2.95.</p>
<dt><code>PauseConnect</code> <i>Seconds</i></p>
<dd>Pause to apply between attempts of connection to gpsd in seconds (default 5 sec).</dl>
<h3>Plugin grpc</h3>
<p>The <i>grpc</i> plugin provides an <font SIZE="-1">RPC</font> interface to submit values to or query values from collectd based on the open source gRPC framework. It exposes an end-point for dispatching values to the daemon. </p>
<p> The <code>gRPC</code> homepage can be found at &lt;<a rel="nofollow" href="https://grpc.io/">https://grpc.io/</a>&gt;.</p>
<dl>
<dt><code>Server</code> <i>Host</i> <i>Port</i></p>
<dd>The <code>Server</code> statement sets the address of a server to which to send metrics via the <tt>&quot;DispatchValues&quot;</tt> function. </p>
<p> The argument <i>Host</i> may be a hostname, an IPv4 address, or an IPv6 address. </p>
<p> Optionally, <code>Server</code> may be specified as a configuration block which supports the following options:</p>
<dl>
<dd>
<dl>
<dt><code>EnableSSL</code> <code>false</code>|<code>true</code></p>
<dd>Whether to require <font SIZE="-1">SSL</font> for outgoing connections. Default: false.</p>
<dt><code>SSLCACertificateFile</code> <i>Filename</i></p>
<dd>
<dt><code>SSLCertificateFile</code> <i>Filename</i></p>
<dd>
<dt><code>SSLCertificateKeyFile</code> <i>Filename</i></p>
<dd>Filenames specifying <font SIZE="-1">SSL</font> certificate and key material to be used with <font SIZE="-1">SSL</font> connections.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Listen</code> <i>Host</i> <i>Port</i></p>
<dd>The <code>Listen</code> statement sets the network address to bind to. When multiple statements are specified, the daemon will bind to all of them. If none are specified, it defaults to <code>0.0.0.0:50051</code>. </p>
<p> The argument <i>Host</i> may be a hostname, an IPv4 address, or an IPv6 address. </p>
<p> Optionally, <code>Listen</code> may be specified as a configuration block which supports the following options:</p>
<dl>
<dd>
<dl>
<dt><code>EnableSSL</code> <i>true</i>|<i>false</i></p>
<dd>Whether to enable <font SIZE="-1">SSL</font> for incoming connections. Default: false.</p>
<dt><code>SSLCACertificateFile</code> <i>Filename</i></p>
<dd>
<dt><code>SSLCertificateFile</code> <i>Filename</i></p>
<dd>
<dt><code>SSLCertificateKeyFile</code> <i>Filename</i></p>
<dd>Filenames specifying <font SIZE="-1">SSL</font> certificate and key material to be used with <font SIZE="-1">SSL</font> connections.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin hddtemp</h3>
<p>To get values from <code>hddtemp</code> collectd connects to <code>localhost</code> (127.0.0.1), port <code>7634/tcp</code>. The <code>Host</code> and <code>Port</code> options can be used to change these default values, see below. <tt>&quot;hddtemp&quot;</tt> has to be running to work correctly. If <tt>&quot;hddtemp&quot;</tt> is not running timeouts may appear which may interfere with other statistics.. </p>
<p> The <code>hddtemp</code> homepage can be found at &lt;<a rel="nofollow" href="http://www.guzu.net/linux/hddtemp.php">http://www.guzu.net/linux/hddtemp.php</a>&gt;.</p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname to connect to. Defaults to <code>127.0.0.1</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>TCP-Port to connect to. Defaults to <code>7634</code>.</dl>
<h3>Plugin hugepages</h3>
<p>To collect <code>hugepages</code> information, collectd reads directories &#8220;/sys/devices/system/node/*/hugepages&#8221; and &#8220;/sys/kernel/mm/hugepages&#8221;. Reading of these directories can be disabled by the following options (default is enabled).</p>
<dl>
<dt><code>ReportPerNodeHP</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, information will be collected from the hugepage counters in &#8220;/sys/devices/system/node/*/hugepages&#8221;. This is used to check the per-node hugepage statistics on a <font SIZE="-1">NUMA</font> system.</p>
<dt><code>ReportRootHP</code> <code>true</code>|<code>false</code></p>
<dd>If enabled, information will be collected from the hugepage counters in &#8220;/sys/kernel/mm/hugepages&#8221;. This can be used on both <font SIZE="-1">NUMA</font> and non-NUMA systems to check the overall hugepage statistics.</p>
<dt><code>ValuesPages</code> <code>true</code>|<code>false</code></p>
<dd>Whether to report hugepages metrics in number of pages. Defaults to <code>true</code>.</p>
<dt><code>ValuesBytes</code> <code>false</code>|<code>true</code></p>
<dd>Whether to report hugepages metrics in bytes. Defaults to <code>false</code>.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>Whether to report hugepages metrics as percentage. Defaults to <code>false</code>.</dl>
<h3>Plugin intel_rdt</h3>
<p>The <i>intel_rdt</i> plugin collects information provided by monitoring features of Intel Resource Director Technology (Intel(R) <font SIZE="-1">RDT</font>) like Cache Monitoring Technology (<font SIZE="-1">CMT</font>), Memory Bandwidth Monitoring (<font SIZE="-1">MBM</font>). These features provide information about utilization of shared resources. <font SIZE="-1">CMT</font> monitors last level cache occupancy (<font SIZE="-1">LLC</font>). <font SIZE="-1">MBM</font> supports two types of events reporting local and remote memory bandwidth. Local memory bandwidth (<font SIZE="-1">MBL</font>) reports the bandwidth of accessing memory associated with the local socket. Remote memory bandwidth (<font SIZE="-1">MBR</font>) reports the bandwidth of accessing the remote socket. Also this technology allows to monitor instructions per clock (<font SIZE="-1">IPC</font>). Monitor events are hardware dependant. Monitoring capabilities are detected on plugin initialization and only supported events are monitored. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;intel_rdt&quot;&gt;
 Cores &quot;0-2&quot; &quot;3,4,6&quot; &quot;8-10,15&quot;
 &lt;/Plugin&gt;</pre>
<p><code>Options:</code></p>
<dl>
<dt><code>Interval</code> <i>seconds</i></p>
<dd>The interval within which to retrieve statistics on monitored events in seconds. For milliseconds divide the time by 1000 for example if the desired interval is 50ms, set interval to 0.05. Due to limited capacity of counters it is not recommended to set interval higher than 1 sec.</p>
<dt><code>Cores</code> <i>cores groups</i></p>
<dd>All events are reported on a per core basis. Monitoring of the events can be configured for group of cores (aggregated statistics). This field defines groups of cores on which to monitor supported events. The field is represented as list of strings with core group values. Each string represents a list of cores in a group. Allowed formats are:<br />
&nbsp;<wbr>0,1,2,3<br />
&nbsp;<wbr>0-10,20-18<br />
&nbsp;<wbr>1,3,5-8,10,0&#215;10-12 </p>
<p> If an empty string is provided as value for this field default cores configuration is applied &#8211; a separate group is created for each core.</dl>
<p> <code>Note:</code> By default global interval is used to retrieve statistics on monitored events. To configure a plugin specific interval use <code>Interval</code> option of the intel_rdt &lt;LoadPlugin&gt; block. For milliseconds divide the time by 1000 for example if the desired interval is 50ms, set interval to 0.05. Due to limited capacity of counters it is not recommended to set interval higher than 1 sec.</p>
<h3>Plugin interface</h3>
<dl>
<dt><code>Interface</code> <i>Interface</i></p>
<dd>Select this interface. By default these interfaces will then be collected. For a more detailed description see <code>IgnoreSelected</code> below.</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>If no configuration if given, the <code>interface</code>-plugin will collect data from all interfaces. This may not be practical, especially for loopback- and similar interfaces. Thus, you can use the <code>Interface</code>-option to pick the interfaces you&#8217;re interested in. Sometimes, however, it&#8217;s easier/preferred to collect all interfaces <i>except</i> a few ones. This option enables you to do that: By setting <code>IgnoreSelected</code> to <i>true</i> the effect of <code>Interface</code> is inverted: All selected interfaces are ignored and all other interfaces are collected. </p>
<p> It is possible to use regular expressions to match interface names, if the name is surrounded by <i>/&#8230;/</i> and collectd was compiled with support for regexps. This is useful if there&#8217;s a need to collect (or ignore) data for a group of interfaces that are similarly named, without the need to explicitly list all of them (especially useful if the list is dynamic). Example: </p>
<pre> Interface &quot;lo&quot;
 Interface &quot;/^veth/&quot;
 Interface &quot;/^tun[0-9]+/&quot;
 IgnoreSelected &quot;true&quot;</pre>
<p>This will ignore the loopback interface, all interfaces with names starting with <i>veth</i> and all interfaces with names starting with <i>tun</i> followed by at least one digit.</p>
<dt><code>ReportInactive</code> <i>true</i>|<i>false</i></p>
<dd>When set to <i>false</i>, only interfaces with non-zero traffic will be reported. Note that the check is done by looking into whether a package was sent at any time from boot and the corresponding counter is non-zero. So, if the interface has been sending data in the past since boot, but not during the reported time-interval, it will still be reported. </p>
<p> The default value is <i>true</i> and results in collection of the data from all interfaces that are selected by <code>Interface</code> and <code>IgnoreSelected</code> options.</p>
<dt><code>UniqueName</code> <i>true</i>|<i>false</i></p>
<dd>Interface name is not unique on Solaris (<font SIZE="-1">KSTAT</font>), interface name is unique only within a module/instance. Following tuple is considered unique:<br />
(ks_module, ks_instance, ks_name) If this option is set to true, interface name contains above three fields separated by an underscore. For more info on <font SIZE="-1">KSTAT,</font> visit &lt;<a rel="nofollow" href="http://docs.oracle.com/cd/E23824_01/html/821-1468/kstat-3kstat.html#REFMAN3Ekstat-3kstat">http://docs.oracle.com/cd/E23824_01/html/821-1468/kstat-3kstat.html#REFMAN3Ekstat-3kstat</a>&gt; </p>
<p> This option is only available on Solaris.</dl>
<h3>Plugin ipmi</h3>
<dl>
<dt><code>Sensor</code> <i>Sensor</i></p>
<dd>Selects sensors to collect or to ignore, depending on <code>IgnoreSelected</code>.</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>If no configuration if given, the <code>ipmi</code> plugin will collect data from all sensors found of type &#8220;temperature&#8221;, &#8220;voltage&#8221;, &#8220;current&#8221; and &#8220;fanspeed&#8221;. This option enables you to do that: By setting <code>IgnoreSelected</code> to <i>true</i> the effect of <code>Sensor</code> is inverted: All selected sensors are ignored and all other sensors are collected.</p>
<dt><code>NotifySensorAdd</code> <i>true</i>|<i>false</i></p>
<dd>If a sensor appears after initialization time of a minute a notification is sent.</p>
<dt><code>NotifySensorRemove</code> <i>true</i>|<i>false</i></p>
<dd>If a sensor disappears a notification is sent.</p>
<dt><code>NotifySensorNotPresent</code> <i>true</i>|<i>false</i></p>
<dd>If you have for example dual power supply and one of them is (un)plugged then a notification is sent.</dl>
<h3>Plugin iptables</h3>
<dl>
<dt><code>Chain</code> <i>Table</i> <i>Chain</i> [<i>Comment|Number</i> [<i>Name</i>]]</p>
<dd>
<dt><code>Chain6</code> <i>Table</i> <i>Chain</i> [<i>Comment|Number</i> [<i>Name</i>]]</p>
<dd>Select the iptables/ip6tables filter rules to count packets and bytes from. </p>
<p> If only <i>Table</i> and <i>Chain</i> are given, this plugin will collect the counters of all rules which have a comment-match. The comment is then used as type-instance. </p>
<p> If <i>Comment</i> or <i>Number</i> is given, only the rule with the matching comment or the <i>n</i>th rule will be collected. Again, the comment (or the number) will be used as the type-instance. </p>
<p> If <i>Name</i> is supplied, it will be used as the type-instance instead of the comment or the number.</dl>
<h3>Plugin irq</h3>
<dl>
<dt><code>Irq</code> <i>Irq</i></p>
<dd>Select this irq. By default these irqs will then be collected. For a more detailed description see <code>IgnoreSelected</code> below.</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>If no configuration if given, the <code>irq</code>-plugin will collect data from all irqs. This may not be practical, especially if no interrupts happen. Thus, you can use the <code>Irq</code>-option to pick the interrupt you&#8217;re interested in. Sometimes, however, it&#8217;s easier/preferred to collect all interrupts <i>except</i> a few ones. This option enables you to do that: By setting <code>IgnoreSelected</code> to <i>true</i> the effect of <code>Irq</code> is inverted: All selected interrupts are ignored and all other interrupts are collected.</dl>
<h3>Plugin java</h3>
<p>The <i>Java</i> plugin makes it possible to write extensions for collectd in Java. This section only discusses the syntax and semantic of the configuration options. For more in-depth information on the <i>Java</i> plugin, please read <i><a href="/docs/linux/man/5-collectd-java/">collectd-java</a></i>(5). </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;java&quot;&gt;
 JVMArg &quot;-verbose:jni&quot;
 JVMArg &quot;-Djava.class.path=/opt/collectd/lib/collectd/bindings/java&quot;
 LoadPlugin &quot;org.collectd.java.Foobar&quot;
 &lt;Plugin &quot;org.collectd.java.Foobar&quot;&gt;
 # To be parsed by the plugin
 &lt;/Plugin&gt;
 &lt;/Plugin&gt;</pre>
<p>Available configuration options:</p>
<dl>
<dt><code>JVMArg</code> <i>Argument</i></p>
<dd>Argument that is to be passed to the <i>Java Virtual Machine</i> (<font SIZE="-1">JVM</font>). This works exactly the way the arguments to the <i>java</i> binary on the command line work. Execute <tt>&quot;java --help&quot;</tt> for details. </p>
<p> Please note that <code>all</code> these options must appear <code>before</code> (i. e. above) any other options! When another option is found, the <font SIZE="-1">JVM</font> will be started and later options will have to be ignored!</p>
<dt><code>LoadPlugin</code> <i>JavaClass</i></p>
<dd>Instantiates a new <i>JavaClass</i> object. The constructor of this object very likely then registers one or more callback methods with the server. </p>
<p> See <i><a href="/docs/linux/man/5-collectd-java/">collectd-java</a></i>(5) for details. </p>
<p> When the first such option is found, the virtual machine (<font SIZE="-1">JVM</font>) is created. This means that all <code>JVMArg</code> options must appear before (i. e. above) all <code>LoadPlugin</code> options!</p>
<dt><code>Plugin</code> <i>Name</i></p>
<dd>The entire block is passed to the Java plugin as an <i>org.collectd.api.OConfigItem</i> object. </p>
<p> For this to work, the plugin has to register a configuration callback first, see &#8220;config callback&#8221; in <i><a href="/docs/linux/man/5-collectd-java/">collectd-java</a></i>(5). This means, that the <code>Plugin</code> block must appear after the appropriate <code>LoadPlugin</code> block. Also note, that <i>Name</i> depends on the (Java) plugin registering the callback and is completely independent from the <i>JavaClass</i> argument passed to <code>LoadPlugin</code>.</dl>
<h3>Plugin load</h3>
<p>The <i>Load plugin</i> collects the system load. These numbers give a rough overview over the utilization of a machine. The system load is defined as the number of runnable tasks in the run-queue and is provided by many operating systems as a one, five or fifteen minute average. </p>
<p> The following configuration options are available:</p>
<dl>
<dt><code>ReportRelative</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, system load divided by number of available <font SIZE="-1">CPU</font> cores is reported for intervals 1 min, 5 min and 15 min. Defaults to false.</dl>
<h3>Plugin logfile</h3>
<dl>
<dt><code>LogLevel</code> <code>debug|info|notice|warning|err</code></p>
<dd>Sets the log-level. If, for example, set to <code>notice</code>, then all events with severity <code>notice</code>, <code>warning</code>, or <code>err</code> will be written to the logfile. </p>
<p> Please note that <code>debug</code> is only available if collectd has been compiled with debugging support.</p>
<dt><code>File</code> <i>File</i></p>
<dd>Sets the file to write log messages to. The special strings <code>stdout</code> and <code>stderr</code> can be used to write to the standard output and standard error channels, respectively. This, of course, only makes much sense when <i>collectd</i> is running in foreground- or non-daemon-mode.</p>
<dt><code>Timestamp</code> <code>true</code>|<code>false</code></p>
<dd>Prefix all lines printed by the current time. Defaults to <code>true</code>.</p>
<dt><code>PrintSeverity</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, all lines are prefixed by the severity of the log message, for example &#8220;warning&#8221;. Defaults to <code>false</code>.</dl>
<p> <code>Note</code>: There is no need to notify the daemon after moving or removing the log file (e. g. when rotating the logs). The plugin reopens the file for each line it writes.</p>
<h3>Plugin log_logstash</h3>
<p>The <i>log logstash plugin</i> behaves like the logfile plugin but formats messages as <font SIZE="-1">JSON</font> events for logstash to parse and input.</p>
<dl>
<dt><code>LogLevel</code> <code>debug|info|notice|warning|err</code></p>
<dd>Sets the log-level. If, for example, set to <code>notice</code>, then all events with severity <code>notice</code>, <code>warning</code>, or <code>err</code> will be written to the logfile. </p>
<p> Please note that <code>debug</code> is only available if collectd has been compiled with debugging support.</p>
<dt><code>File</code> <i>File</i></p>
<dd>Sets the file to write log messages to. The special strings <code>stdout</code> and <code>stderr</code> can be used to write to the standard output and standard error channels, respectively. This, of course, only makes much sense when <i>collectd</i> is running in foreground- or non-daemon-mode.</dl>
<p> <code>Note</code>: There is no need to notify the daemon after moving or removing the log file (e. g. when rotating the logs). The plugin reopens the file for each line it writes.</p>
<h3>Plugin lpar</h3>
<p>The <i></i><font SIZE="-1"><i>LPAR</i></font><i> plugin</i> reads <font SIZE="-1">CPU</font> statistics of <i>Logical Partitions</i>, a virtualization technique for <font SIZE="-1">IBM POWER</font> processors. It takes into account <font SIZE="-1">CPU</font> time stolen from or donated to a partition, in addition to the usual user, system, I/O statistics. </p>
<p> The following configuration options are available:</p>
<dl>
<dt><code>CpuPoolStats</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, statistics about the processor pool are read, too. The partition needs to have pool authority in order to be able to acquire this information. Defaults to false.</p>
<dt><code>ReportBySerial</code> <code>false</code>|<code>true</code></p>
<dd>If enabled, the serial of the physical machine the partition is currently running on is reported as <i>hostname</i> and the logical hostname of the machine is reported in the <i>plugin instance</i>. Otherwise, the logical hostname will be used (just like other plugins) and the <i>plugin instance</i> will be empty. Defaults to false.</dl>
<h3>Plugin lua</h3>
<p>This plugin embeds a Lua interpreter into collectd and provides an interface to collectd&#8217;s plugin system. See <i><a href="/docs/linux/man/5-collectd-lua/">collectd-lua</a></i>(5) for its documentation.</p>
<h3>Plugin mbmon</h3>
<p>The <tt>&quot;mbmon plugin&quot;</tt> uses mbmon to retrieve temperature, voltage, etc. </p>
<p> Be default collectd connects to <code>localhost</code> (127.0.0.1), port <code>411/tcp</code>. The <code>Host</code> and <code>Port</code> options can be used to change these values, see below. <tt>&quot;mbmon&quot;</tt> has to be running to work correctly. If <tt>&quot;mbmon&quot;</tt> is not running timeouts may appear which may interfere with other statistics.. </p>
<p> <tt>&quot;mbmon&quot;</tt> must be run with the -r option (&#8220;print <font SIZE="-1">TAG</font> and Value format&#8221;); Debian&#8217;s <i>/etc/init.d/mbmon</i> script already does this, other people will need to ensure that this is the case.</p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname to connect to. Defaults to <code>127.0.0.1</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>TCP-Port to connect to. Defaults to <code>411</code>.</dl>
<h3>Plugin md</h3>
<p>The <tt>&quot;md plugin&quot;</tt> collects information from Linux Software-RAID devices (md). </p>
<p> All reported values are of the type <tt>&quot;md_disks&quot;</tt>. Reported type instances are <i>active</i>, <i>failed</i> (present but not operational), <i>spare</i> (hot stand-by) and <i>missing</i> (physically absent) disks.</p>
<dl>
<dt><code>Device</code> <i>Device</i></p>
<dd>Select md devices based on device name. The <i>device name</i> is the basename of the device, i.e. the name of the block device without the leading <tt>&quot;/dev/&quot;</tt>. See <code>IgnoreSelected</code> for more details.</p>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Invert device selection: If set to <code>true</code>, all md devices <code>except</code> those listed using <code>Device</code> are collected. If <code>false</code> (the default), only those listed are collected. If no configuration is given, the <code>md</code> plugin will collect data from all md devices.</dl>
<h3>Plugin memcachec</h3>
<p>The <tt>&quot;memcachec plugin&quot;</tt> connects to a memcached server, queries one or more given <i>pages</i> and parses the returned data according to user specification. The <i>matches</i> used are the same as the matches used in the <tt>&quot;curl&quot;</tt> and <tt>&quot;tail&quot;</tt> plugins. </p>
<p> In order to talk to the memcached server, this plugin uses the <i>libmemcached</i> library. Please note that there is another library with a very similar name, libmemcache (notice the missing `d&#8217;), which is not applicable. </p>
<p> Synopsis of the configuration: </p>
<pre> &lt;Plugin &quot;memcachec&quot;&gt;
 &lt;Page &quot;plugin_instance&quot;&gt;
 Server &quot;localhost&quot;
 Key &quot;page_key&quot;
 &lt;Match&gt;
 Regex &quot;(\d+) bytes sent&quot;
 DSType CounterAdd
 Type &quot;ipt_octets&quot;
 Instance &quot;type_instance&quot;
 &lt;/Match&gt;
 &lt;/Page&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration options are:</p>
<dl>
<dt>&lt;<code>Page</code> <i>Name</i>&gt;</p>
<dd>Each <code>Page</code> block defines one <i>page</i> to be queried from the memcached server. The block requires one string argument which is used as <i>plugin instance</i>.</p>
<dt><code>Server</code> <i>Address</i></p>
<dd>Sets the server address to connect to when querying the page. Must be inside a <code>Page</code> block.</p>
<dt><code>Key</code> <i>Key</i></p>
<dd>When connected to the memcached server, asks for the page <i>Key</i>.</p>
<dt>&lt;<code>Match</code>&gt;</p>
<dd>Match blocks define which strings to look for and how matches substrings are interpreted. For a description of match blocks, please see &#8220;Plugin tail&#8221;.</dl>
<h3>Plugin memcached</h3>
<p>The <code>memcached plugin</code> connects to a memcached server and queries statistics about cache utilization, memory and bandwidth used. &lt;<a rel="nofollow" href="http://memcached.org/">http://memcached.org/</a>&gt; </p>
<pre> &lt;Plugin &quot;memcached&quot;&gt;
 &lt;Instance &quot;name&quot;&gt;
 #Host &quot;memcache.example.com&quot;
 Address &quot;127.0.0.1&quot;
 Port 11211
 &lt;/Instance&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin configuration consists of one or more <code>Instance</code> blocks which specify one <i>memcached</i> connection each. Within the <code>Instance</code> blocks, the following options are allowed:</p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Sets the <code>host</code> field of dispatched values. Defaults to the global hostname setting. For backwards compatibility, values are also dispatched with the global hostname when <code>Host</code> is set to <code>127.0.0.1</code> or <code>localhost</code> and <code>Address</code> is not set.</p>
<dt><code>Address</code> <i>Address</i></p>
<dd>Hostname or <font SIZE="-1">IP</font> to connect to. For backwards compatibility, defaults to the value of <code>Host</code> or <code>127.0.0.1</code> if <code>Host</code> is unset.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd><font SIZE="-1">TCP</font> port to connect to. Defaults to <code>11211</code>.</p>
<dt><code>Socket</code> <i>Path</i></p>
<dd>Connect to <i>memcached</i> using the <font SIZE="-1">UNIX</font> domain socket at <i>Path</i>. If this setting is given, the <code>Address</code> and <code>Port</code> settings are ignored.</dl>
<h3>Plugin mic</h3>
<p>The <code>mic plugin</code> gathers <font SIZE="-1">CPU</font> statistics, memory usage and temperatures from Intel&#8217;s Many Integrated Core (<font SIZE="-1">MIC</font>) systems. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin mic&gt;
 ShowCPU true
 ShowCPUCores true
 ShowMemory true
 ShowTemperatures true
 Temperature vddg
 Temperature vddq
 IgnoreSelectedTemperature true
 ShowPower true
 Power total0
 Power total1
 IgnoreSelectedPower true
 &lt;/Plugin&gt;</pre>
<p>The following options are valid inside the <code>Plugin mic</code> block:</p>
<dl>
<dt><code>ShowCPU</code> <code>true</code>|<code>false</code></p>
<dd>If enabled (the default) a sum of the <font SIZE="-1">CPU</font> usage across all cores is reported.</p>
<dt><code>ShowCPUCores</code> <code>true</code>|<code>false</code></p>
<dd>If enabled (the default) per-core <font SIZE="-1">CPU</font> usage is reported.</p>
<dt><code>ShowMemory</code> <code>true</code>|<code>false</code></p>
<dd>If enabled (the default) the physical memory usage of the <font SIZE="-1">MIC</font> system is reported.</p>
<dt><code>ShowTemperatures</code> <code>true</code>|<code>false</code></p>
<dd>If enabled (the default) various temperatures of the <font SIZE="-1">MIC</font> system are reported.</p>
<dt><code>Temperature</code> <i>Name</i></p>
<dd>This option controls which temperatures are being reported. Whether matching temperatures are being ignored or <i>only</i> matching temperatures are reported depends on the <code>IgnoreSelectedTemperature</code> setting below. By default <i>all</i> temperatures are reported.</p>
<dt><code>IgnoreSelectedTemperature</code> <code>false</code>|<code>true</code></p>
<dd>Controls the behavior of the <code>Temperature</code> setting above. If set to <code>false</code> (the default) only temperatures matching a <code>Temperature</code> option are reported or, if no <code>Temperature</code> option is specified, all temperatures are reported. If set to <code>true</code>, matching temperatures are <i>ignored</i> and all other temperatures are reported. </p>
<p> Known temperature names are:</p>
<dl>
<dd>
<dl>
<dt>die</p>
<dd>Die of the <font SIZE="-1">CPU</font></p>
<dt>devmem</p>
<dd>Device Memory</p>
<dt>fin</p>
<dd>Fan In</p>
<dt>fout</p>
<dd>Fan Out</p>
<dt>vccp</p>
<dd>Voltage ccp</p>
<dt>vddg</p>
<dd>Voltage ddg</p>
<dt>vddq</p>
<dd>Voltage ddq</dl>
</dl>
<dl>
<dd></dl>
<dt><code>ShowPower</code> <code>true</code>|<code>false</code></p>
<dd>If enabled (the default) various temperatures of the <font SIZE="-1">MIC</font> system are reported.</p>
<dt><code>Power</code> <i>Name</i></p>
<dd>This option controls which power readings are being reported. Whether matching power readings are being ignored or <i>only</i> matching power readings are reported depends on the <code>IgnoreSelectedPower</code> setting below. By default <i>all</i> power readings are reported.</p>
<dt><code>IgnoreSelectedPower</code> <code>false</code>|<code>true</code></p>
<dd>Controls the behavior of the <code>Power</code> setting above. If set to <code>false</code> (the default) only power readings matching a <code>Power</code> option are reported or, if no <code>Power</code> option is specified, all power readings are reported. If set to <code>true</code>, matching power readings are <i>ignored</i> and all other power readings are reported. </p>
<p> Known power names are:</p>
<dl>
<dd>
<dl>
<dt>total0</p>
<dd>Total power utilization averaged over Time Window 0 (uWatts).</p>
<dt>total1</p>
<dd>Total power utilization averaged over Time Window 0 (uWatts).</p>
<dt>inst</p>
<dd>Instantaneous power (uWatts).</p>
<dt>imax</p>
<dd>Max instantaneous power (uWatts).</p>
<dt>pcie</p>
<dd>PCI-E connector power (uWatts).</p>
<dt>c2x3</p>
<dd>2&#215;3 connector power (uWatts).</p>
<dt>c2x4</p>
<dd>2&#215;4 connector power (uWatts).</p>
<dt>vccp</p>
<dd>Core rail (uVolts).</p>
<dt>vddg</p>
<dd>Uncore rail (uVolts).</p>
<dt>vddq</p>
<dd>Memory subsystem rail (uVolts).</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin memory</h3>
<p>The <i>memory plugin</i> provides the following configuration options:</p>
<dl>
<dt><code>ValuesAbsolute</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables reporting of physical memory usage in absolute numbers, i.e. bytes. Defaults to <code>true</code>.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>Enables or disables reporting of physical memory usage in percentages, e.g. percent of physical memory used. Defaults to <code>false</code>. </p>
<p> This is useful for deploying <i>collectd</i> in a heterogeneous environment in which the sizes of physical memory vary.</dl>
<h3>Plugin modbus</h3>
<p>The <code>modbus plugin</code> connects to a Modbus &#8220;slave&#8221; via Modbus/TCP or Modbus/RTU and reads register values. It supports reading single registers (unsigned 16 bit values), large integer values (unsigned 32 bit values) and floating point values (two registers interpreted as <font SIZE="-1">IEEE</font> floats in big endian notation). </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Data &quot;voltage-input-1&quot;&gt;
 RegisterBase 0
 RegisterType float
 RegisterCmd ReadHolding
 Type voltage
 Instance &quot;input-1&quot;
 &lt;/Data&gt;
 &lt;Data &quot;voltage-input-2&quot;&gt;
 RegisterBase 2
 RegisterType float
 RegisterCmd ReadHolding
 Type voltage
 Instance &quot;input-2&quot;
 &lt;/Data&gt;
 &lt;Data &quot;supply-temperature-1&quot;&gt;
 RegisterBase 0
 RegisterType Int16
 RegisterCmd ReadHolding
 Type temperature
 Instance &quot;temp-1&quot;
 &lt;/Data&gt;
 &lt;Host &quot;modbus.example.com&quot;&gt;
 Address &quot;192.168.0.42&quot;
 Port &quot;502&quot;
 Interval 60
 &lt;Slave 1&gt;
 Instance &quot;power-supply&quot;
 Collect &quot;voltage-input-1&quot;
 Collect &quot;voltage-input-2&quot;
 &lt;/Slave&gt;
 &lt;/Host&gt;
 &lt;Host &quot;localhost&quot;&gt;
 Device &quot;/dev/ttyUSB0&quot;
 Baudrate 38400
 Interval 20
 &lt;Slave 1&gt;
 Instance &quot;temperature&quot;
 Collect &quot;supply-temperature-1&quot;
 &lt;/Slave&gt;
 &lt;/Host&gt;</pre>
<dl>
<dt>&lt;<code>Data</code> <i>Name</i>&gt; blocks</p>
<dd>Data blocks define a mapping between register numbers and the &#8220;types&#8221; used by <i>collectd</i>. </p>
<p> Within &lt;Data&nbsp;<wbr>/&gt; blocks, the following options are allowed:</p>
<dl>
<dd>
<dl>
<dt><code>RegisterBase</code> <i>Number</i></p>
<dd>Configures the base register to read from the device. If the option <code>RegisterType</code> has been set to <code>Uint32</code> or <code>Float</code>, this and the next register will be read (the register number is increased by one).</p>
<dt><code>RegisterType</code> <code>Int16</code>|<code>Int32</code>|<code>Uint16</code>|<code>Uint32</code>|<code>Float</code></p>
<dd>Specifies what kind of data is returned by the device. If the type is <code>Int32</code>, <code>Uint32</code> or <code>Float</code>, two 16 bit registers will be read and the data is combined into one value. Defaults to <code>Uint16</code>.</p>
<dt><code>RegisterCmd</code> <code>ReadHolding</code>|<code>ReadInput</code></p>
<dd>Specifies register type to be collected from device. Works only with libmodbus 2.9.2 or higher. Defaults to <code>ReadHolding</code>.</p>
<dt><code>Type</code> <i>Type</i></p>
<dd>Specifies the &#8220;type&#8221; (data set) to use when dispatching the value to <i>collectd</i>. Currently, only data sets with exactly one data source are supported.</p>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Sets the type instance to use when dispatching the value to <i>collectd</i>. If unset, an empty string (no type instance) is used.</dl>
</dl>
<dl>
<dd></dl>
<dt>&lt;<code>Host</code> <i>Name</i>&gt; blocks</p>
<dd>Host blocks are used to specify to which hosts to connect and what data to read from their &#8220;slaves&#8221;. The string argument <i>Name</i> is used as hostname when dispatching the values to <i>collectd</i>. </p>
<p> Within &lt;Host&nbsp;<wbr>/&gt; blocks, the following options are allowed:</p>
<dl>
<dd>
<dl>
<dt><code>Address</code> <i>Hostname</i></p>
<dd>For Modbus/TCP, specifies the node name (the actual network address) used to connect to the host. This may be an <font SIZE="-1">IP</font> address or a hostname. Please note that the used <i>libmodbus</i> library only supports IPv4 at the moment.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>for Modbus/TCP, specifies the port used to connect to the host. The port can either be given as a number or as a service name. Please note that the <i>Service</i> argument must be a string, even if ports are given in their numerical form. Defaults to &#8220;502&#8221;.</p>
<dt><code>Device</code> <i>Devicenode</i></p>
<dd>For Modbus/RTU, specifies the path to the serial device being used.</p>
<dt><code>Baudrate</code> <i>Baudrate</i></p>
<dd>For Modbus/RTU, specifies the baud rate of the serial device. Note, connections currently support only 8/N/1.</p>
<dt><code>Interval</code> <i>Interval</i></p>
<dd>Sets the interval (in seconds) in which the values will be collected from this host. By default the global <code>Interval</code> setting will be used.</p>
<dt>&lt;<code>Slave</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i>&gt;</p>
<dd>Over each connection, multiple Modbus devices may be reached. The slave <font SIZE="-1">ID</font> is used to specify which device should be addressed. For each device you want to query, one <code>Slave</code> block must be given. </p>
<p> Within &lt;Slave&nbsp;<wbr>/&gt; blocks, the following options are allowed:</p>
<dl>
<dd>
<dl>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Specify the plugin instance to use when dispatching the values to <i>collectd</i>. By default &quot;slave_<i></i><font SIZE="-1"><i>ID</i></font><i></i>&quot; is used.</p>
<dt><code>Collect</code> <i>DataName</i></p>
<dd>Specifies which data to retrieve from the device. <i>DataName</i> must be the same string as the <i>Name</i> argument passed to a <code>Data</code> block. You can specify this option multiple times to collect more than one value from a slave. At least one <code>Collect</code> option is mandatory.</dl>
</dl>
<dl>
<dd></dl>
</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin mqtt</h3>
<p>The <i></i><font SIZE="-1"><i>MQTT</i></font><i> plugin</i> can send metrics to <font SIZE="-1">MQTT </font>(<code>Publish</code> blocks) and receive values from <font SIZE="-1">MQTT </font>(<code>Subscribe</code> blocks). </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin mqtt&gt;
 &lt;Publish &quot;name&quot;&gt;
 Host &quot;mqtt.example.com&quot;
 Prefix &quot;collectd&quot;
 &lt;/Publish&gt;
 &lt;Subscribe &quot;name&quot;&gt;
 Host &quot;mqtt.example.com&quot;
 Topic &quot;collectd/#&quot;
 &lt;/Subscribe&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin&#8217;s configuration is in <code>Publish</code> and/or <code>Subscribe</code> blocks, configuring the sending and receiving direction respectively. The plugin will register a write callback named <tt>&quot;mqtt/</tt>name<tt>&quot;</tt> where <i>name</i> is the string argument given to the <code>Publish</code> block. Both types of blocks share many but not all of the following options. If an option is valid in only one of the blocks, it will be mentioned explicitly. </p>
<p> <code>Options:</code></p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname of the <font SIZE="-1">MQTT</font> broker to connect to.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Port number or service name of the <font SIZE="-1">MQTT</font> broker to connect to.</p>
<dt><code>User</code> <i>UserName</i></p>
<dd>Username used when authenticating to the <font SIZE="-1">MQTT</font> broker.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Password used when authenticating to the <font SIZE="-1">MQTT</font> broker.</p>
<dt><code>ClientId</code> <i>ClientId</i></p>
<dd><font SIZE="-1">MQTT</font> client <font SIZE="-1">ID</font> to use. Defaults to the hostname used by <i>collectd</i>.</p>
<dt><code>QoS</code> [<code>0</code>&#8211;<code>2</code>]</p>
<dd>Sets the <i>Quality of Service</i>, with the values <tt>0</tt>, <tt>1</tt> and <tt>2</tt> meaning:</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>At most once</p>
<dt><code>1</code></p>
<dd>At least once</p>
<dt><code>2</code></p>
<dd>Exactly once</dl>
</dl>
<dl>
<dd>In <code>Publish</code> blocks, this option determines the QoS flag set on outgoing messages and defaults to <code>0</code>. In <code>Subscribe</code> blocks, determines the maximum QoS setting the client is going to accept and defaults to <code>2</code>. If the QoS flag on a message is larger than the maximum accepted QoS of a subscriber, the message&#8217;s QoS will be downgraded.</dl>
<dt><code>Prefix</code> <i>Prefix</i> (Publish only)</p>
<dd>This plugin will use one topic per <i>value list</i> which will looks like a path. <i>Prefix</i> is used as the first path element and defaults to <code>collectd</code>. </p>
<p> An example topic name would be: </p>
<pre> collectd/cpu-0/cpu-user</pre>
<dt><code>Retain</code> <code>false</code>|<code>true</code> (Publish only)</p>
<dd>Controls whether the <font SIZE="-1">MQTT</font> broker will retain (keep a copy of) the last message sent to each topic and deliver it to new subscribers. Defaults to <code>false</code>.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code> (Publish only)</p>
<dd>Controls whether <tt>&quot;DERIVE&quot;</tt> and <tt>&quot;COUNTER&quot;</tt> metrics are converted to a <i>rate</i> before sending. Defaults to <code>true</code>.</p>
<dt><code>CleanSession</code> <code>true</code>|<code>false</code> (Subscribe only)</p>
<dd>Controls whether the <font SIZE="-1">MQTT </font>&#8220;cleans&#8221; the session up after the subscriber disconnects or if it maintains the subscriber&#8217;s subscriptions and all messages that arrive while the subscriber is disconnected. Defaults to <code>true</code>.</p>
<dt><code>Topic</code> <i>TopicName</i> (Subscribe only)</p>
<dd>Configures the topic(s) to subscribe to. You can use the single level <tt>&quot;+&quot;</tt> and multi level <tt>&quot;#&quot;</tt> wildcards. Defaults to <code>collectd/#</code>, i.e. all topics beneath the <code>collectd</code> branch.</p>
<dt><code>CACert</code> <i>file</i></p>
<dd>Path to the PEM-encoded <font SIZE="-1">CA</font> certificate file. Setting this option enables <font SIZE="-1">TLS</font> communication with the <font SIZE="-1">MQTT</font> broker, and as such, <code>Port</code> should be the TLS-enabled port of the <font SIZE="-1">MQTT</font> broker. A valid <font SIZE="-1">TLS</font> configuration requires <code>CACert</code>, <code>CertificateFile</code> and <code>CertificateKeyFile</code>.</p>
<dt><code>CertificateFile</code> <i>file</i></p>
<dd>Path to the PEM-encoded certificate file to use as client certificate when connecting to the <font SIZE="-1">MQTT</font> broker. A valid <font SIZE="-1">TLS</font> configuration requires <code>CACert</code>, <code>CertificateFile</code> and <code>CertificateKeyFile</code>.</p>
<dt><code>CertificateKeyFile</code> <i>file</i></p>
<dd>Path to the unencrypted PEM-encoded key file corresponding to <code>CertificateFile</code>. A valid <font SIZE="-1">TLS</font> configuration requires <code>CACert</code>, <code>CertificateFile</code> and <code>CertificateKeyFile</code>.</p>
<dt><code>TLSProtocol</code> <i>protocol</i></p>
<dd>If configured, this specifies the string protocol version (e.g. <tt>&quot;tlsv1&quot;</tt>, <tt>&quot;tlsv1.2&quot;</tt>) to use for the <font SIZE="-1">TLS</font> connection to the broker. If not set a default version is used which depends on the version of OpenSSL the Mosquitto library was linked against.</p>
<dt><code>CipherSuite</code> <i>ciphersuite</i></p>
<dd>A string describing the ciphers available for use. See <i><a href="/docs/linux/man/1-ciphers/">ciphers</a></i>(1) and the <tt>&quot;openssl ciphers&quot;</tt> utility for more information. If unset, the default ciphers will be used.</dl>
<h3>Plugin mysql</h3>
<p>The <tt>&quot;mysql plugin&quot;</tt> requires <code>mysqlclient</code> to be installed. It connects to one or more databases when started and keeps the connection up as long as possible. When the connection is interrupted for whatever reason it will try to re-connect. The plugin will complain loudly in case anything goes wrong. </p>
<p> This plugin issues the MySQL <tt>&quot;SHOW STATUS&quot;</tt> / <tt>&quot;SHOW GLOBAL STATUS&quot;</tt> command and collects information about MySQL network traffic, executed statements, requests, the query cache and threads by evaluating the <tt>&quot;Bytes_{received,sent}&quot;</tt>, <tt>&quot;Com_*&quot;</tt>, <tt>&quot;Handler_*&quot;</tt>, <tt>&quot;Qcache_*&quot;</tt> and <tt>&quot;Threads_*&quot;</tt> return values. Please refer to the <code>MySQL reference manual</code>, <i>5.1.6. Server Status Variables</i> for an explanation of these values. </p>
<p> Optionally, master and slave statistics may be collected in a MySQL replication setup. In that case, information about the synchronization state of the nodes are collected by evaluating the <tt>&quot;Position&quot;</tt> return value of the <tt>&quot;SHOW MASTER STATUS&quot;</tt> command and the <tt>&quot;Seconds_Behind_Master&quot;</tt>, <tt>&quot;Read_Master_Log_Pos&quot;</tt> and <tt>&quot;Exec_Master_Log_Pos&quot;</tt> return values of the <tt>&quot;SHOW SLAVE STATUS&quot;</tt> command. See the <code>MySQL reference manual</code>, <i>12.5.5.21 </i><font SIZE="-1"><i>SHOW MASTER STATUS</i></font><i> Syntax</i> and <i>12.5.5.31 </i><font SIZE="-1"><i>SHOW SLAVE STATUS</i></font><i> Syntax</i> for details. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin mysql&gt;
 &lt;Database foo&gt;
 Host &quot;hostname&quot;
 User &quot;username&quot;
 Password &quot;password&quot;
 Port &quot;3306&quot;
 MasterStats true
 ConnectTimeout 10
 SSLKey &quot;/path/to/key.pem&quot;
 SSLCert &quot;/path/to/cert.pem&quot;
 SSLCA &quot;/path/to/ca.pem&quot;
 SSLCAPath &quot;/path/to/cas/&quot;
 SSLCipher &quot;DHE-RSA-AES256-SHA&quot;
 &lt;/Database&gt;
 &lt;Database bar&gt;
 Alias &quot;squeeze&quot;
 Host &quot;localhost&quot;
 Socket &quot;/var/run/mysql/mysqld.sock&quot;
 SlaveStats true
 SlaveNotifications true
 &lt;/Database&gt;
 &lt;Database galera&gt;
 Alias &quot;galera&quot;
 Host &quot;localhost&quot;
 Socket &quot;/var/run/mysql/mysqld.sock&quot;
 WsrepStats true
 &lt;/Database&gt;
 &lt;/Plugin&gt;</pre>
<p>A <code>Database</code> block defines one connection to a MySQL database. It accepts a single argument which specifies the name of the database. None of the other options are required. MySQL will use default values as documented in the &#8220;<i>mysql_real_connect()</i>&#8221; and &#8220;<i>mysql_ssl_set()</i>&#8221; sections in the <code>MySQL reference manual</code>.</p>
<dl>
<dt><code>Alias</code> <i>Alias</i></p>
<dd>Alias to use as sender instead of hostname when reporting. This may be useful when having cryptic hostnames.</p>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname of the database server. Defaults to <code>localhost</code>.</p>
<dt><code>User</code> <i>Username</i></p>
<dd>Username to use when connecting to the database. The user does not have to be granted any privileges (which is synonym to granting the <tt>&quot;USAGE&quot;</tt> privilege), unless you want to collectd replication statistics (see <code>MasterStats</code> and <code>SlaveStats</code> below). In this case, the user needs the <tt>&quot;REPLICATION CLIENT&quot;</tt> (or <tt>&quot;SUPER&quot;</tt>) privileges. Else, any existing MySQL user will do.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Password needed to log into the database.</p>
<dt><code>Database</code> <i>Database</i></p>
<dd>Select this database. Defaults to <i>no database</i> which is a perfectly reasonable option for what this plugin does.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>TCP-port to connect to. The port must be specified in its numeric form, but it must be passed as a string nonetheless. For example: </p>
<pre> Port &quot;3306&quot;</pre>
<p>If <code>Host</code> is set to <code>localhost</code> (the default), this setting has no effect. See the documentation for the <tt>&quot;mysql_real_connect&quot;</tt> function for details.</p>
<dt><code>Socket</code> <i>Socket</i></p>
<dd>Specifies the path to the <font SIZE="-1">UNIX</font> domain socket of the MySQL server. This option only has any effect, if <code>Host</code> is set to <code>localhost</code> (the default). Otherwise, use the <code>Port</code> option above. See the documentation for the <tt>&quot;mysql_real_connect&quot;</tt> function for details.</p>
<dt><code>InnodbStats</code> <i>true|false</i></p>
<dd>If enabled, metrics about the InnoDB storage engine are collected. Disabled by default.</p>
<dt><code>MasterStats</code> <i>true|false</i></p>
<dd>
<dt><code>SlaveStats</code> <i>true|false</i></p>
<dd>Enable the collection of master / slave statistics in a replication setup. In order to be able to get access to these statistics, the user needs special privileges. See the <code>User</code> documentation above. Defaults to <code>false</code>.</p>
<dt><code>SlaveNotifications</code> <i>true|false</i></p>
<dd>If enabled, the plugin sends a notification if the replication slave I/O and / or <font SIZE="-1">SQL</font> threads are not running. Defaults to <code>false</code>.</p>
<dt><code>WsrepStats</code> <i>true|false</i></p>
<dd>
<pre> Enable the collection of wsrep plugin statistics, used in Master-Master
 replication setups like in MySQL Galera/Percona XtraDB Cluster.
 User needs only privileges to execute 'SHOW GLOBAL STATUS'</pre>
<dt><code>ConnectTimeout</code> <i>Seconds</i></p>
<dd>Sets the connect timeout for the MySQL client.</p>
<dt><code>SSLKey</code> <i>Path</i></p>
<dd>If provided, the X509 key in <font SIZE="-1">PEM</font> format.</p>
<dt><code>SSLCert</code> <i>Path</i></p>
<dd>If provided, the X509 cert in <font SIZE="-1">PEM</font> format.</p>
<dt><font SIZE="-1"><code>SSLCA</code></font> <i>Path</i></p>
<dd>If provided, the <font SIZE="-1">CA</font> file in <font SIZE="-1">PEM</font> format (check OpenSSL docs).</p>
<dt><code>SSLCAPath</code> <i>Path</i></p>
<dd>If provided, the <font SIZE="-1">CA</font> directory (check OpenSSL docs).</p>
<dt><code>SSLCipher</code> <i>String</i></p>
<dd>If provided, the <font SIZE="-1">SSL</font> cipher to use.</dl>
<h3>Plugin netapp</h3>
<p>The netapp plugin can collect various performance and capacity information from a NetApp filer using the NetApp <font SIZE="-1">API.</font> </p>
<p> Please note that NetApp has a wide line of products and a lot of different software versions for each of these products. This plugin was developed for a NetApp <font SIZE="-1">FAS3040</font> running OnTap 7.2.3P8 and tested on <font SIZE="-1">FAS2050 7.3.1.1L1, FAS3140 7.2.5.1</font> and <font SIZE="-1">FAS3020 7.2.4P9.</font> It <i>should</i> work for most combinations of model and software version but it is very hard to test this. If you have used this plugin with other models and/or software version, feel free to send us a mail to tell us about the results, even if it&#8217;s just a short &#8220;It works&#8221;. </p>
<p> To collect these data collectd will log in to the NetApp via <font SIZE="-1">HTTP</font>(S) and <font SIZE="-1">HTTP</font> basic authentication. </p>
<p> <code>Do not use a regular user for this!</code> Create a special collectd user with just the minimum of capabilities needed. The user only needs the &#8220;login-http-admin&#8221; capability as well as a few more depending on which data will be collected. Required capabilities are documented below. </p>
<p> <i>Synopsis</i> </p>
<pre> &lt;Plugin &quot;netapp&quot;&gt;
 &lt;Host &quot;netapp1.example.com&quot;&gt;
 Protocol &quot;https&quot;
 Address &quot;10.0.0.1&quot;
 Port 443
 User &quot;username&quot;
 Password &quot;aef4Aebe&quot;
 Interval 30
 &lt;WAFL&gt;
 Interval 30
 GetNameCache true
 GetDirCache true
 GetBufferCache true
 GetInodeCache true
 &lt;/WAFL&gt;
 &lt;Disks&gt;
 Interval 30
 GetBusy true
 &lt;/Disks&gt;
 &lt;VolumePerf&gt;
 Interval 30
 GetIO &quot;volume0&quot;
 IgnoreSelectedIO false
 GetOps &quot;volume0&quot;
 IgnoreSelectedOps false
 GetLatency &quot;volume0&quot;
 IgnoreSelectedLatency false
 &lt;/VolumePerf&gt;
 &lt;VolumeUsage&gt;
 Interval 30
 GetCapacity &quot;vol0&quot;
 GetCapacity &quot;vol1&quot;
 IgnoreSelectedCapacity false
 GetSnapshot &quot;vol1&quot;
 GetSnapshot &quot;vol3&quot;
 IgnoreSelectedSnapshot false
 &lt;/VolumeUsage&gt;
 &lt;Quota&gt;
 Interval 60
 &lt;/Quota&gt;
 &lt;Snapvault&gt;
 Interval 30
 &lt;/Snapvault&gt;
 &lt;System&gt;
 Interval 30
 GetCPULoad true
 GetInterfaces true
 GetDiskOps true
 GetDiskIO true
 &lt;/System&gt;
 &lt;VFiler vfilerA&gt;
 Interval 60
 SnapVault true
 # ...
 &lt;/VFiler&gt;
 &lt;/Host&gt;
 &lt;/Plugin&gt;</pre>
<p>The netapp plugin accepts the following configuration options:</p>
<dl>
<dt><code>Host</code> <i>Name</i></p>
<dd>A host block defines one NetApp filer. It will appear in collectd with the name you specify here which does not have to be its real name nor its hostname (see the <code>Address</code> option below).</p>
<dt><code>VFiler</code> <i>Name</i></p>
<dd>A <code>VFiler</code> block may only be used inside a host block. It accepts all the same options as the <code>Host</code> block (except for cascaded <code>VFiler</code> blocks) and will execute all NetApp <font SIZE="-1">API</font> commands in the context of the specified VFiler(R). It will appear in collectd with the name you specify here which does not have to be its real name. The VFiler name may be specified using the <code>VFilerName</code> option. If this is not specified, it will default to the name you specify here. </p>
<p> The VFiler block inherits all connection related settings from the surrounding <code>Host</code> block (which appear before the <code>VFiler</code> block) but they may be overwritten inside the <code>VFiler</code> block. </p>
<p> This feature is useful, for example, when using a VFiler as SnapVault target (supported since OnTap 8.1). In that case, the SnapVault statistics are not available in the host filer (vfiler0) but only in the respective VFiler context.</p>
<dt><code>Protocol</code> <code>httpd</code>|<code>http</code></p>
<dd>The protocol collectd will use to query this host. </p>
<p> Optional </p>
<p> Type: string </p>
<p> Default: https </p>
<p> Valid options: http, https</p>
<dt><code>Address</code> <i>Address</i></p>
<dd>The hostname or <font SIZE="-1">IP</font> address of the host. </p>
<p> Optional </p>
<p> Type: string </p>
<p> Default: The &#8220;host&#8221; block&#8217;s name.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>The <font SIZE="-1">TCP</font> port to connect to on the host. </p>
<p> Optional </p>
<p> Type: integer </p>
<p> Default: 80 for protocol &#8220;http&#8221;, 443 for protocol &#8220;https&#8221;</p>
<dt><code>User</code> <i>User</i></p>
<dd>
<dt><code>Password</code> <i>Password</i></p>
<dd>The username and password to use to login to the NetApp. </p>
<p> Mandatory </p>
<p> Type: string</p>
<dt><code>VFilerName</code> <i>Name</i></p>
<dd>The name of the VFiler in which context to execute <font SIZE="-1">API</font> commands. If not specified, the name provided to the <code>VFiler</code> block will be used instead. </p>
<p> Optional </p>
<p> Type: string </p>
<p> Default: name of the <code>VFiler</code> block </p>
<p> <code>Note:</code> This option may only be used inside <code>VFiler</code> blocks.</p>
<dt><code>Interval</code> <i>Interval</i></p>
<dd><font SIZE="-1"><code>TODO</code></font></dl>
<p> The following options decide what kind of data will be collected. You can either use them as a block and fine tune various parameters inside this block, use them as a single statement to just accept all default values, or omit it to not collect any data. </p>
<p> The following options are valid inside all blocks:</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect the respective statistics every <i>Seconds</i> seconds. Defaults to the host specific setting.</dl>
<p> <i>The System block</i> </p>
<p> This will collect various performance data about the whole system. </p>
<p> <code>Note:</code> To get this data the collectd user needs the &#8220;api-perf-object-get-instances&#8221; capability.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect disk statistics every <i>Seconds</i> seconds.</p>
<dt><code>GetCPULoad</code> <code>true</code>|<code>false</code></p>
<dd>If you set this option to true the current <font SIZE="-1">CPU</font> usage will be read. This will be the average usage between all CPUs in your NetApp without any information about individual CPUs. </p>
<p> <code>Note:</code> These are the same values that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;<font SIZE="-1">CPU&#8221;</font> field. </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: Two value lists of type &#8220;cpu&#8221;, and type instances &#8220;idle&#8221; and &#8220;system&#8221;.</p>
<dt><code>GetInterfaces</code> <code>true</code>|<code>false</code></p>
<dd>If you set this option to true the current traffic of the network interfaces will be read. This will be the total traffic over all interfaces of your NetApp without any information about individual interfaces. </p>
<p> <code>Note:</code> This is the same values that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;Net kB/s&#8221; field. </p>
<p> <code>Or is it?</code> </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;if_octects&#8221;.</p>
<dt><code>GetDiskIO</code> <code>true</code>|<code>false</code></p>
<dd>If you set this option to true the current <font SIZE="-1">IO</font> throughput will be read. This will be the total <font SIZE="-1">IO</font> of your NetApp without any information about individual disks, volumes or aggregates. </p>
<p> <code>Note:</code> This is the same values that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;Disk kB/s&#8221; field. </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;disk_octets&#8221;.</p>
<dt><code>GetDiskOps</code> <code>true</code>|<code>false</code></p>
<dd>If you set this option to true the current number of <font SIZE="-1">HTTP, NFS, CIFS, FCP,</font> iSCSI, etc. operations will be read. This will be the total number of operations on your NetApp without any information about individual volumes or aggregates. </p>
<p> <code>Note:</code> These are the same values that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;<font SIZE="-1">NFS&#8221;, &#8220;CIFS&#8221;, &#8220;HTTP&#8221;, &#8220;FCP&#8221;</font> and &#8220;iSCSI&#8221; fields. </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: A variable number of value lists of type &#8220;disk_ops_complex&#8221;. Each type of operation will result in one value list with the name of the operation as type instance.</dl>
<p> <i>The </i><font SIZE="-1"><i>WAFL</i></font><i> block</i> </p>
<p> This will collect various performance data about the <font SIZE="-1">WAFL</font> file system. At the moment this just means cache performance. </p>
<p> <code>Note:</code> To get this data the collectd user needs the &#8220;api-perf-object-get-instances&#8221; capability. </p>
<p> <code>Note:</code> The interface to get these values is classified as &#8220;Diagnostics&#8221; by NetApp. This means that it is not guaranteed to be stable even between minor releases.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect disk statistics every <i>Seconds</i> seconds.</p>
<dt><code>GetNameCache</code> <code>true</code>|<code>false</code></p>
<dd>Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;cache_ratio&#8221; and type instance &#8220;name_cache_hit&#8221;.</p>
<dt><code>GetDirCache</code> <code>true</code>|<code>false</code></p>
<dd>Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;cache_ratio&#8221; and type instance &#8220;find_dir_hit&#8221;.</p>
<dt><code>GetInodeCache</code> <code>true</code>|<code>false</code></p>
<dd>Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;cache_ratio&#8221; and type instance &#8220;inode_cache_hit&#8221;.</p>
<dt><code>GetBufferCache</code> <code>true</code>|<code>false</code></p>
<dd><code>Note:</code> This is the same value that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;Cache hit&#8221; field. </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;cache_ratio&#8221; and type instance &#8220;buf_hash_hit&#8221;.</dl>
<p> <i>The Disks block</i> </p>
<p> This will collect performance data about the individual disks in the NetApp. </p>
<p> <code>Note:</code> To get this data the collectd user needs the &#8220;api-perf-object-get-instances&#8221; capability.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect disk statistics every <i>Seconds</i> seconds.</p>
<dt><code>GetBusy</code> <code>true</code>|<code>false</code></p>
<dd>If you set this option to true the busy time of all disks will be calculated and the value of the busiest disk in the system will be written. </p>
<p> <code>Note:</code> This is the same values that the NetApp <font SIZE="-1">CLI</font> command &#8220;sysstat&#8221; returns in the &#8220;Disk util&#8221; field. Probably. </p>
<p> Optional </p>
<p> Type: boolean </p>
<p> Default: true </p>
<p> Result: One value list of type &#8220;percent&#8221; and type instance &#8220;disk_busy&#8221;.</dl>
<p> <i>The VolumePerf block</i> </p>
<p> This will collect various performance data about the individual volumes. </p>
<p> You can select which data to collect about which volume using the following options. They follow the standard ignorelist semantic. </p>
<p> <code>Note:</code> To get this data the collectd user needs the <i>api-perf-object-get-instances</i> capability.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect volume performance data every <i>Seconds</i> seconds.</p>
<dt><code>GetIO</code> <i>Volume</i></p>
<dd>
<dt><code>GetOps</code> <i>Volume</i></p>
<dd>
<dt><code>GetLatency</code> <i>Volume</i></p>
<dd>Select the given volume for <font SIZE="-1">IO,</font> operations or latency statistics collection. The argument is the name of the volume without the <tt>&quot;/vol/&quot;</tt> prefix. </p>
<p> Since the standard ignorelist functionality is used here, you can use a string starting and ending with a slash to specify regular expression matching: To match the volumes &#8220;vol0&#8221;, &#8220;vol2&#8221; and &#8220;vol7&#8221;, you can use this regular expression: </p>
<pre> GetIO &quot;/^vol[027]$/&quot;</pre>
<p>If no regular expression is specified, an exact match is required. Both, regular and exact matching are case sensitive. </p>
<p> If no volume was specified at all for either of the three options, that data will be collected for all available volumes.</p>
<dt><code>IgnoreSelectedIO</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>IgnoreSelectedOps</code> <code>true</code>|<code>false</code></p>
<dd>
<dt><code>IgnoreSelectedLatency</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, the volumes selected for <font SIZE="-1">IO,</font> operations or latency statistics collection will be ignored and the data will be collected for all other volumes. </p>
<p> When set to <code>false</code>, data will only be collected for the specified volumes and all other volumes will be ignored. </p>
<p> If no volumes have been specified with the above <code>Get*</code> options, all volumes will be collected regardless of the <code>IgnoreSelected*</code> option. </p>
<p> Defaults to <code>false</code></dl>
<p> <i>The VolumeUsage block</i> </p>
<p> This will collect capacity data about the individual volumes. </p>
<p> <code>Note:</code> To get this data the collectd user needs the <i>api-volume-list-info</i> capability.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect volume usage statistics every <i>Seconds</i> seconds.</p>
<dt><code>GetCapacity</code> <i>VolumeName</i></p>
<dd>The current capacity of the volume will be collected. This will result in two to four value lists, depending on the configuration of the volume. All data sources are of type &#8220;df_complex&#8221; with the name of the volume as plugin_instance. </p>
<p> There will be type_instances &#8220;used&#8221; and &#8220;free&#8221; for the number of used and available bytes on the volume. If the volume has some space reserved for snapshots, a type_instance &#8220;snap_reserved&#8221; will be available. If the volume has <font SIZE="-1">SIS</font> enabled, a type_instance &#8220;sis_saved&#8221; will be available. This is the number of bytes saved by the <font SIZE="-1">SIS</font> feature. </p>
<p> <code>Note:</code> The current NetApp <font SIZE="-1">API</font> has a bug that results in this value being reported as a 32 bit number. This plugin tries to guess the correct number which works most of the time. If you see strange values here, bug NetApp support to fix this. </p>
<p> Repeat this option to specify multiple volumes.</p>
<dt><code>IgnoreSelectedCapacity</code> <code>true</code>|<code>false</code></p>
<dd>Specify whether to collect only the volumes selected by the <code>GetCapacity</code> option or to ignore those volumes. <code>IgnoreSelectedCapacity</code> defaults to <code>false</code>. However, if no <code>GetCapacity</code> option is specified at all, all capacities will be selected anyway.</p>
<dt><code>GetSnapshot</code> <i>VolumeName</i></p>
<dd>Select volumes from which to collect snapshot information. </p>
<p> Usually, the space used for snapshots is included in the space reported as &#8220;used&#8221;. If snapshot information is collected as well, the space used for snapshots is subtracted from the used space. </p>
<p> To make things even more interesting, it is possible to reserve space to be used for snapshots. If the space required for snapshots is less than that reserved space, there is &#8220;reserved free&#8221; and &#8220;reserved used&#8221; space in addition to &#8220;free&#8221; and &#8220;used&#8221;. If the space required for snapshots exceeds the reserved space, that part allocated in the normal space is subtracted from the &#8220;used&#8221; space again. </p>
<p> Repeat this option to specify multiple volumes.</p>
<dt><code>IgnoreSelectedSnapshot</code></p>
<dd>Specify whether to collect only the volumes selected by the <code>GetSnapshot</code> option or to ignore those volumes. <code>IgnoreSelectedSnapshot</code> defaults to <code>false</code>. However, if no <code>GetSnapshot</code> option is specified at all, all capacities will be selected anyway.</dl>
<p> <i>The Quota block</i> </p>
<p> This will collect (tree) quota statistics (used disk space and number of used files). This mechanism is useful to get usage information for single qtrees. In case the quotas are not used for any other purpose, an entry similar to the following in <tt>&quot;/etc/quotas&quot;</tt> would be sufficient: </p>
<pre> /vol/volA/some_qtree tree - - - - -</pre>
<p>After adding the entry, issue <tt>&quot;quota on -w volA&quot;</tt> on the NetApp filer.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect SnapVault(R) statistics every <i>Seconds</i> seconds.</dl>
<p> <i>The SnapVault block</i> </p>
<p> This will collect statistics about the time and traffic of SnapVault(R) transfers.</p>
<dl>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect SnapVault(R) statistics every <i>Seconds</i> seconds.</dl>
<h3>Plugin netlink</h3>
<p>The <tt>&quot;netlink&quot;</tt> plugin uses a netlink socket to query the Linux kernel about statistics of various interface and routing aspects.</p>
<dl>
<dt><code>Interface</code> <i>Interface</i></p>
<dd>
<dt><code>VerboseInterface</code> <i>Interface</i></p>
<dd>Instruct the plugin to collect interface statistics. This is basically the same as the statistics provided by the <tt>&quot;interface&quot;</tt> plugin (see above) but potentially much more detailed. </p>
<p> When configuring with <code>Interface</code> only the basic statistics will be collected, namely octets, packets, and errors. These statistics are collected by the <tt>&quot;interface&quot;</tt> plugin, too, so using both at the same time is no benefit. </p>
<p> When configured with <code>VerboseInterface</code> all counters <code>except</code> the basic ones, so that no data needs to be collected twice if you use the <tt>&quot;interface&quot;</tt> plugin. This includes dropped packets, received multicast packets, collisions and a whole zoo of differentiated <font SIZE="-1">RX</font> and <font SIZE="-1">TX</font> errors. You can try the following command to get an idea of what awaits you: </p>
<pre> ip -s -s link list</pre>
<p>If <i>Interface</i> is <code>All</code>, all interfaces will be selected.</p>
<dt><code>QDisc</code> <i>Interface</i> [<i>QDisc</i>]</p>
<dd>
<dt><code>Class</code> <i>Interface</i> [<i>Class</i>]</p>
<dd>
<dt><code>Filter</code> <i>Interface</i> [<i>Filter</i>]</p>
<dd>Collect the octets and packets that pass a certain qdisc, class or filter. </p>
<p> QDiscs and classes are identified by their type and handle (or classid). Filters don&#8217;t necessarily have a handle, therefore the parent&#8217;s handle is used. The notation used in collectd differs from that used in <i><a href="/docs/linux/man/1-tc/">tc</a></i>(1) in that it doesn&#8217;t skip the major or minor number if it&#8217;s zero and doesn&#8217;t print special ids by their name. So, for example, a qdisc may be identified by <tt>&quot;pfifo_fast-1:0&quot;</tt> even though the minor number of <code>all</code> qdiscs is zero and thus not displayed by <i><a href="/docs/linux/man/1-tc/">tc</a></i>(1). </p>
<p> If <code>QDisc</code>, <code>Class</code>, or <code>Filter</code> is given without the second argument, i. .e. without an identifier, all qdiscs, classes, or filters that are associated with that interface will be collected. </p>
<p> Since a filter itself doesn&#8217;t necessarily have a handle, the parent&#8217;s handle is used. This may lead to problems when more than one filter is attached to a qdisc or class. This isn&#8217;t nice, but we don&#8217;t know how this could be done any better. If you have a idea, please don&#8217;t hesitate to tell us. </p>
<p> As with the <code>Interface</code> option you can specify <code>All</code> as the interface, meaning all interfaces. </p>
<p> Here are some examples to help you understand the above text more easily: </p>
<pre> &lt;Plugin netlink&gt;
 VerboseInterface &quot;All&quot;
 QDisc &quot;eth0&quot; &quot;pfifo_fast-1:0&quot;
 QDisc &quot;ppp0&quot;
 Class &quot;ppp0&quot; &quot;htb-1:10&quot;
 Filter &quot;ppp0&quot; &quot;u32-1:0&quot;
 &lt;/Plugin&gt;</pre>
<dt><code>IgnoreSelected</code></p>
<dd>The behavior is the same as with all other similar plugins: If nothing is selected at all, everything is collected. If some things are selected using the options described above, only these statistics are collected. If you set <code>IgnoreSelected</code> to <code>true</code>, this behavior is inverted, i. e. the specified statistics will not be collected.</dl>
<h3>Plugin network</h3>
<p>The Network plugin sends data to a remote instance of collectd, receives data from a remote instance, or both at the same time. Data which has been received from the network is usually not transmitted again, but this can be activated, see the <code>Forward</code> option below. </p>
<p> The default IPv6 multicast group is <tt>&quot;ff18::efc0:4a42&quot;</tt>. The default IPv4 multicast group is <tt>239.192.74.66</tt>. The default <i></i><font SIZE="-1"><i>UDP</i></font><i></i> port is <code>25826</code>. </p>
<p> Both, <code>Server</code> and <code>Listen</code> can be used as single option or as block. When used as block, given options are valid for this socket only. The following example will export the metrics twice: Once to an &#8220;internal&#8221; server (without encryption and signing) and one to an external server (with cryptographic signature): </p>
<pre> &lt;Plugin &quot;network&quot;&gt;
 # Export to an internal server
 # (demonstrates usage without additional options)
 Server &quot;collectd.internal.tld&quot;
 # Export to an external server
 # (demonstrates usage with signature options)
 &lt;Server &quot;collectd.external.tld&quot;&gt;
 SecurityLevel &quot;sign&quot;
 Username &quot;myhostname&quot;
 Password &quot;ohl0eQue&quot;
 &lt;/Server&gt;
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>&lt;Server</code> <i>Host</i> [<i>Port</i>]<code>&gt;</code></p>
<dd>The <code>Server</code> statement/block sets the server to send datagrams to. The statement may occur multiple times to send each datagram to multiple destinations. </p>
<p> The argument <i>Host</i> may be a hostname, an IPv4 address or an IPv6 address. The optional second argument specifies a port number or a service name. If not given, the default, <code>25826</code>, is used. </p>
<p> The following options are recognized within <code>Server</code> blocks:</p>
<dl>
<dd>
<dl>
<dt><code>SecurityLevel</code> <code>Encrypt</code>|<code>Sign</code>|<code>None</code></p>
<dd>Set the security you require for network communication. When the security level has been set to <code>Encrypt</code>, data sent over the network will be encrypted using <i></i><font SIZE="-1"><i>AES-256</i></font><i></i>. The integrity of encrypted packets is ensured using <i></i><font SIZE="-1"><i>SHA-1</i></font><i></i>. When set to <code>Sign</code>, transmitted data is signed using the <i></i><font SIZE="-1"><i>HMAC-SHA-256</i></font><i></i> message authentication code. When set to <code>None</code>, data is sent without any security. </p>
<p> This feature is only available if the <i>network</i> plugin was linked with <i>libgcrypt</i>.</p>
<dt><code>Username</code> <i>Username</i></p>
<dd>Sets the username to transmit. This is used by the server to lookup the password. See <code>AuthFile</code> below. All security levels except <code>None</code> require this setting. </p>
<p> This feature is only available if the <i>network</i> plugin was linked with <i>libgcrypt</i>.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Sets a password (shared secret) for this socket. All security levels except <code>None</code> require this setting. </p>
<p> This feature is only available if the <i>network</i> plugin was linked with <i>libgcrypt</i>.</p>
<dt><code>Interface</code> <i>Interface name</i></p>
<dd>Set the outgoing interface for <font SIZE="-1">IP</font> packets. This applies at least to IPv6 packets and if possible to IPv4. If this option is not applicable, undefined or a non-existent interface name is specified, the default behavior is to let the kernel choose the appropriate interface. Be warned that the manual selection of an interface for unicast traffic is only necessary in rare cases.</p>
<dt><code>ResolveInterval</code> <i>Seconds</i></p>
<dd>Sets the interval at which to re-resolve the <font SIZE="-1">DNS</font> for the <i>Host</i>. This is useful to force a regular <font SIZE="-1">DNS</font> lookup to support a high availability setup. If not specified, re-resolves are never attempted.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&lt;Listen</code> <i>Host</i> [<i>Port</i>]<code>&gt;</code></p>
<dd>The <code>Listen</code> statement sets the interfaces to bind to. When multiple statements are found the daemon will bind to multiple interfaces. </p>
<p> The argument <i>Host</i> may be a hostname, an IPv4 address or an IPv6 address. If the argument is a multicast address the daemon will join that multicast group. The optional second argument specifies a port number or a service name. If not given, the default, <code>25826</code>, is used. </p>
<p> The following options are recognized within <tt>&quot;&lt;Listen&gt;&quot;</tt> blocks:</p>
<dl>
<dd>
<dl>
<dt><code>SecurityLevel</code> <code>Encrypt</code>|<code>Sign</code>|<code>None</code></p>
<dd>Set the security you require for network communication. When the security level has been set to <code>Encrypt</code>, only encrypted data will be accepted. The integrity of encrypted packets is ensured using <i></i><font SIZE="-1"><i>SHA-1</i></font><i></i>. When set to <code>Sign</code>, only signed and encrypted data is accepted. When set to <code>None</code>, all data will be accepted. If an <code>AuthFile</code> option was given (see below), encrypted data is decrypted if possible. </p>
<p> This feature is only available if the <i>network</i> plugin was linked with <i>libgcrypt</i>.</p>
<dt><code>AuthFile</code> <i>Filename</i></p>
<dd>Sets a file in which usernames are mapped to passwords. These passwords are used to verify signatures and to decrypt encrypted network packets. If <code>SecurityLevel</code> is set to <code>None</code>, this is optional. If given, signed data is verified and encrypted packets are decrypted. Otherwise, signed data is accepted without checking the signature and encrypted data cannot be decrypted. For the other security levels this option is mandatory. </p>
<p> The file format is very simple: Each line consists of a username followed by a colon and any number of spaces followed by the password. To demonstrate, an example file could look like this: </p>
<pre> user0: foo
 user1: bar</pre>
<p>Each time a packet is received, the modification time of the file is checked using <i><a href="/docs/linux/man/2-stat/">stat</a></i>(2). If the file has been changed, the contents is re-read. While the file is being read, it is locked using <i><a href="/docs/linux/man/2-fcntl/">fcntl</a></i>(2).</p>
<dt><code>Interface</code> <i>Interface name</i></p>
<dd>Set the incoming interface for <font SIZE="-1">IP</font> packets explicitly. This applies at least to IPv6 packets and if possible to IPv4. If this option is not applicable, undefined or a non-existent interface name is specified, the default behavior is, to let the kernel choose the appropriate interface. Thus incoming traffic gets only accepted, if it arrives on the given interface.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>TimeToLive</code> <i>1-255</i></p>
<dd>Set the time-to-live of sent packets. This applies to all, unicast and multicast, and IPv4 and IPv6 packets. The default is to not change this value. That means that multicast packets will be sent with a <font SIZE="-1">TTL</font> of <tt>1</tt> (one) on most operating systems.</p>
<dt><code>MaxPacketSize</code> <i>1024-65535</i></p>
<dd>Set the maximum size for datagrams received over the network. Packets larger than this will be truncated. Defaults to 1452 bytes, which is the maximum payload size that can be transmitted in one Ethernet frame using IPv6&nbsp;<wbr>/ <font SIZE="-1">UDP.</font> </p>
<p> On the server side, this limit should be set to the largest value used on <i>any</i> client. Likewise, the value on the client must not be larger than the value on the server, or data will be lost. </p>
<p> <code>Compatibility:</code> Versions prior to <i>version 4.8</i> used a fixed sized buffer of 1024 bytes. Versions <i>4.8</i>, <i>4.9</i> and <i>4.10</i> used a default value of 1024 bytes to avoid problems when sending data to an older server.</p>
<dt><code>Forward</code> <i>true|false</i></p>
<dd>If set to <i>true</i>, write packets that were received via the network plugin to the sending sockets. This should only be activated when the <code>Listen</code>&#8211; and <code>Server</code>-statements differ. Otherwise packets may be send multiple times to the same multicast group. While this results in more network traffic than necessary it&#8217;s not a huge problem since the plugin has a duplicate detection, so the values will not loop.</p>
<dt><code>ReportStats</code> <code>true</code>|<code>false</code></p>
<dd>The network plugin cannot only receive and send statistics, it can also create statistics about itself. Collectd data included the number of received and sent octets and packets, the length of the receive queue and the number of values handled. When set to <code>true</code>, the <i>Network plugin</i> will make these statistics available. Defaults to <code>false</code>.</dl>
<h3>Plugin nginx</h3>
<p>This plugin collects the number of connections and requests handled by the <tt>&quot;nginx daemon&quot;</tt> (speak: engine X), a <font SIZE="-1">HTTP</font> and mail server/proxy. It queries the page provided by the <tt>&quot;ngx_http_stub_status_module&quot;</tt> module, which isn&#8217;t compiled by default. Please refer to &lt;<a rel="nofollow" href="http://wiki.codemongers.com/NginxStubStatusModule">http://wiki.codemongers.com/NginxStubStatusModule</a>&gt; for more information on how to compile and configure nginx and this module. </p>
<p> The following options are accepted by the <tt>&quot;nginx plugin&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i><a rel="nofollow" href="http://host/nginx_status">http://host/nginx_status</a></i></p>
<dd>Sets the <font SIZE="-1">URL</font> of the <tt>&quot;ngx_http_stub_status_module&quot;</tt> output.</p>
<dt><code>User</code> <i>Username</i></p>
<dd>Optional user name needed for authentication.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Optional password needed for authentication.</p>
<dt><code>VerifyPeer</code> <code>true|false</code></p>
<dd>Enable or disable peer <font SIZE="-1">SSL</font> certificate verification. See &lt;<a rel="nofollow" href="http://curl.haxx.se/docs/sslcerts.html">http://curl.haxx.se/docs/sslcerts.html</a>&gt; for details. Enabled by default.</p>
<dt><code>VerifyHost</code> <code>true|false</code></p>
<dd>Enable or disable peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a <font SIZE="-1">SSL</font> enabled server. Enabled by default.</p>
<dt><code>CACert</code> <i>File</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">HTTPS</font> you will possibly need this option. What <font SIZE="-1">CA</font> certificates come bundled with <tt>&quot;libcurl&quot;</tt> and are checked by default depends on the distribution you use.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the overall timeout for <font SIZE="-1">HTTP</font> requests to <font SIZE="-1"><code>URL</code></font>, in milliseconds. By default, the configured <code>Interval</code> is used to set the timeout.</dl>
<h3>Plugin notify_desktop</h3>
<p>This plugin sends a desktop notification to a notification daemon, as defined in the Desktop Notification Specification. To actually display the notifications, <code>notification-daemon</code> is required and <code>collectd</code> has to be able to access the X server (i. e., the <tt>&quot;DISPLAY&quot;</tt> and <tt>&quot;XAUTHORITY&quot;</tt> environment variables have to be set correctly) and the D-Bus message bus. </p>
<p> The Desktop Notification Specification can be found at &lt;<a rel="nofollow" href="http://www.galago-project.org/specs/notification/">http://www.galago-project.org/specs/notification/</a>&gt;.</p>
<dl>
<dt><code>OkayTimeout</code> <i>timeout</i></p>
<dd>
<dt><code>WarningTimeout</code> <i>timeout</i></p>
<dd>
<dt><code>FailureTimeout</code> <i>timeout</i></p>
<dd>Set the <i>timeout</i>, in milliseconds, after which to expire the notification for <tt>&quot;OKAY&quot;</tt>, <tt>&quot;WARNING&quot;</tt> and <tt>&quot;FAILURE&quot;</tt> severities respectively. If zero has been specified, the displayed notification will not be closed at all &#8211; the user has to do so herself. These options default to 5000. If a negative number has been specified, the default is used as well.</dl>
<h3>Plugin notify_email</h3>
<p>The <i>notify_email</i> plugin uses the <i></i><font SIZE="-1"><i>ESMTP</i></font><i></i> library to send notifications to a configured email address. </p>
<p> <i>libESMTP</i> is available from &lt;<a rel="nofollow" href="http://www.stafford.uklinux.net/libesmtp/">http://www.stafford.uklinux.net/libesmtp/</a>&gt;. </p>
<p> Available configuration options:</p>
<dl>
<dt><code>From</code> <i>Address</i></p>
<dd>Email address from which the emails should appear to come from. </p>
<p> Default: <tt>&quot;root [at] localhost&quot;</tt></p>
<dt><code>Recipient</code> <i>Address</i></p>
<dd>Configures the email address(es) to which the notifications should be mailed. May be repeated to send notifications to multiple addresses. </p>
<p> At least one <code>Recipient</code> must be present for the plugin to work correctly.</p>
<dt><code>SMTPServer</code> <i>Hostname</i></p>
<dd>Hostname of the <font SIZE="-1">SMTP</font> server to connect to. </p>
<p> Default: <tt>&quot;localhost&quot;</tt></p>
<dt><code>SMTPPort</code> <i>Port</i></p>
<dd><font SIZE="-1">TCP</font> port to connect to. </p>
<p> Default: <tt>25</tt></p>
<dt><code>SMTPUser</code> <i>Username</i></p>
<dd>Username for <font SIZE="-1">ASMTP</font> authentication. Optional.</p>
<dt><code>SMTPPassword</code> <i>Password</i></p>
<dd>Password for <font SIZE="-1">ASMTP</font> authentication. Optional.</p>
<dt><code>Subject</code> <i>Subject</i></p>
<dd>Subject-template to use when sending emails. There must be exactly two string-placeholders in the subject, given in the standard <i><a href="/docs/linux/man/3-printf/">printf</a>(3)</i> syntax, i. e. <tt>%s</tt>. The first will be replaced with the severity, the second with the hostname. </p>
<p> Default: <tt>&quot;Collectd notify: %s@%s&quot;</tt></dl>
<h3>Plugin notify_nagios</h3>
<p>The <i>notify_nagios</i> plugin writes notifications to Nagios&#8217; <i>command file</i> as a <i>passive service check result</i>. </p>
<p> Available configuration options:</p>
<dl>
<dt><code>CommandFile</code> <i>Path</i></p>
<dd>Sets the <i>command file</i> to write to. Defaults to <i>/usr/local/nagios/var/rw/nagios.cmd</i>.</dl>
<h3>Plugin ntpd</h3>
<p>The <tt>&quot;ntpd&quot;</tt> plugin collects per-peer ntp data such as time offset and time dispersion. </p>
<p> For talking to <code>ntpd</code>, it mimics what the <code>ntpdc</code> control program does on the wire &#8211; using <code>mode 7</code> specific requests. This mode is deprecated with newer <code>ntpd</code> releases (4.2.7p230 and later). For the <tt>&quot;ntpd&quot;</tt> plugin to work correctly with them, the ntp daemon must be explicitly configured to enable <code>mode 7</code> (which is disabled by default). Refer to the <i><a href="/docs/linux/man/5-ntp-conf/">ntp.conf</a>(5)</i> manual page for details. </p>
<p> Available configuration options for the <tt>&quot;ntpd&quot;</tt> plugin:</p>
<dl>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>Hostname of the host running <code>ntpd</code>. Defaults to <code>localhost</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>UDP-Port to connect to. Defaults to <code>123</code>.</p>
<dt><code>ReverseLookups</code> <code>true</code>|<code>false</code></p>
<dd>Sets whether or not to perform reverse lookups on peers. Since the name or IP-address may be used in a filename it is recommended to disable reverse lookups. The default is to do reverse lookups to preserve backwards compatibility, though.</p>
<dt><code>IncludeUnitID</code> <code>true</code>|<code>false</code></p>
<dd>When a peer is a refclock, include the unit <font SIZE="-1">ID</font> in the <i>type instance</i>. Defaults to <code>false</code> for backward compatibility. </p>
<p> If two refclock peers use the same driver and this is <code>false</code>, the plugin will try to write simultaneous measurements from both to the same type instance. This will result in error messages in the log and only one set of measurements making it through.</dl>
<h3>Plugin nut</h3>
<dl>
<dt><font SIZE="-1"><code>UPS</code></font> <i>upsname</i><code>@</code><i>hostname</i>[<code>:</code><i>port</i>]</p>
<dd>Add a <font SIZE="-1">UPS</font> to collect data from. The format is identical to the one accepted by <i><a href="/docs/linux/man/8-upsc/">upsc</a></i>(8).</dl>
<h3>Plugin olsrd</h3>
<p>The <i>olsrd</i> plugin connects to the <font SIZE="-1">TCP</font> port opened by the <i>txtinfo</i> plugin of the Optimized Link State Routing daemon and reads information about the current state of the meshed network. </p>
<p> The following configuration options are understood:</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>Connect to <i>Host</i>. Defaults to <code>&#8220;localhost&#8221;</code>.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>Specifies the port to connect to. This must be a string, even if you give the port as a number rather than a service name. Defaults to <code>&#8220;2006&#8221;</code>.</p>
<dt><code>CollectLinks</code> <code>No</code>|<code>Summary</code>|<code>Detail</code></p>
<dd>Specifies what information to collect about links, i. e. direct connections of the daemon queried. If set to <code>No</code>, no information is collected. If set to <code>Summary</code>, the number of links and the average of all <i>link quality</i> (<font SIZE="-1">LQ</font>) and <i>neighbor link quality</i> (<font SIZE="-1">NLQ</font>) values is calculated. If set to <code>Detail</code> <font SIZE="-1">LQ</font> and <font SIZE="-1">NLQ</font> are collected per link. </p>
<p> Defaults to <code>Detail</code>.</p>
<dt><code>CollectRoutes</code> <code>No</code>|<code>Summary</code>|<code>Detail</code></p>
<dd>Specifies what information to collect about routes of the daemon queried. If set to <code>No</code>, no information is collected. If set to <code>Summary</code>, the number of routes and the average <i>metric</i> and <i></i><font SIZE="-1"><i>ETX</i></font><i></i> is calculated. If set to <code>Detail</code> metric and <font SIZE="-1">ETX</font> are collected per route. </p>
<p> Defaults to <code>Summary</code>.</p>
<dt><code>CollectTopology</code> <code>No</code>|<code>Summary</code>|<code>Detail</code></p>
<dd>Specifies what information to collect about the global topology. If set to <code>No</code>, no information is collected. If set to <code>Summary</code>, the number of links in the entire topology and the average <i>link quality</i> (<font SIZE="-1">LQ</font>) is calculated. If set to <code>Detail</code> <font SIZE="-1">LQ</font> and <font SIZE="-1">NLQ</font> are collected for each link in the entire topology. </p>
<p> Defaults to <code>Summary</code>.</dl>
<h3>Plugin onewire</h3>
<p><font SIZE="-1"><code>EXPERIMENTAL</code></font><code>!</code> See notes below. </p>
<p> The <tt>&quot;onewire&quot;</tt> plugin uses the <code>owcapi</code> library from the <code>owfs</code> project &lt;<a rel="nofollow" href="http://owfs.org/">http://owfs.org/</a>&gt; to read sensors connected via the onewire bus. </p>
<p> It can be used in two possible modes &#8211; standard or advanced. </p>
<p> In the standard mode only temperature sensors (sensors with the family code <tt>10</tt>, <tt>22</tt> and <tt>28</tt> &#8211; e.g. <font SIZE="-1">DS1820, DS18S20, DS1920</font>) can be read. If you have other sensors you would like to have included, please send a sort request to the mailing list. You can select sensors to be read or to be ignored depending on the option <code>IgnoreSelected</code>). When no list is provided the whole bus is walked and all sensors are read. </p>
<p> Hubs (the <font SIZE="-1">DS2409</font> chips) are working, but read the note, why this plugin is experimental, below. </p>
<p> In the advanced mode you can configure any sensor to be read (only numerical value) using full <font SIZE="-1">OWFS</font> path (e.g. &#8220;/uncached/10.F10FCA000800/temperature&#8221;). In this mode you have to list all the sensors. Neither default bus walk nor <code>IgnoreSelected</code> are used here. Address and type (file) is extracted from the path automatically and should produce compatible structure with the &#8220;standard&#8221; mode (basically the path is expected as for example &#8220;/uncached/10.F10FCA000800/temperature&#8221; where it would extract address part &#8220;F10FCA000800&#8221; and the rest after the slash is considered the type &#8211; here &#8220;temperature&#8221;). There are two advantages to this mode &#8211; you can access virtually any sensor (not just temperature), select whether to use cached or directly read values and it is slighlty faster. The downside is more complex configuration. </p>
<p> The two modes are distinguished automatically by the format of the address. It is not possible to mix the two modes. Once a full path is detected in any <code>Sensor</code> then the whole addressing (all sensors) is considered to be this way (and as standard addresses will fail parsing they will be ignored).</p>
<dl>
<dt><code>Device</code> <i>Device</i></p>
<dd>Sets the device to read the values from. This can either be a &#8220;real&#8221; hardware device, such as a serial port or an <font SIZE="-1">USB</font> port, or the address of the <i><a href="/docs/linux/man/1-owserver/">owserver</a></i>(1) socket, usually <code>localhost:4304</code>. </p>
<p> Though the documentation claims to automatically recognize the given address format, with version 2.7p4 we had to specify the type explicitly. So with that version, the following configuration worked for us: </p>
<pre> &lt;Plugin onewire&gt;
 Device &quot;-s localhost:4304&quot;
 &lt;/Plugin&gt;</pre>
<p>This directive is <code>required</code> and does not have a default value.</p>
<dt><code>Sensor</code> <i>Sensor</i></p>
<dd>In the standard mode selects sensors to collect or to ignore (depending on <code>IgnoreSelected</code>, see below). Sensors are specified without the family byte at the beginning, so you have to use for example <tt>&quot;F10FCA000800&quot;</tt>, and <code>not</code> include the leading <tt>10.</tt> family byte and point. When no <code>Sensor</code> is configured the whole Onewire bus is walked and all supported sensors (see above) are read. </p>
<p> In the advanced mode the <code>Sensor</code> specifies full <font SIZE="-1">OWFS</font> path &#8211; e.g. <tt>&quot;/uncached/10.F10FCA000800/temperature&quot;</tt> (or when cached values are <font SIZE="-1">OK </font><tt>&quot;/10.F10FCA000800/temperature&quot;</tt>). <code>IgnoreSelected</code> is not used. </p>
<p> As there can be multiple devices on the bus you can list multiple sensor (use multiple <code>Sensor</code> elements).</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>If no configuration is given, the <code>onewire</code> plugin will collect data from all sensors found. This may not be practical, especially if sensors are added and removed regularly. Sometimes, however, it&#8217;s easier/preferred to collect only specific sensors or all sensors <i>except</i> a few specified ones. This option enables you to do that: By setting <code>IgnoreSelected</code> to <i>true</i> the effect of <code>Sensor</code> is inverted: All selected interfaces are ignored and all other interfaces are collected. </p>
<p> Used only in the standard mode &#8211; see above.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Sets the interval in which all sensors should be read. If not specified, the global <code>Interval</code> setting is used.</dl>
<p> <font SIZE="-1"><code>EXPERIMENTAL</code></font><code>!</code> The <tt>&quot;onewire&quot;</tt> plugin is experimental, because it doesn&#8217;t yet work with big setups. It works with one sensor being attached to one controller, but as soon as you throw in a couple more senors and maybe a hub or two, reading all values will take more than ten seconds (the default interval). We will probably add some separate thread for reading the sensors and some cache or something like that, but it&#8217;s not done yet. We will try to maintain backwards compatibility in the future, but we can&#8217;t promise. So in short: If it works for you: Great! But keep in mind that the config <i>might</i> change, though this is unlikely. Oh, and if you want to help improving this plugin, just send a short notice to the mailing list. Thanks :)</p>
<h3>Plugin openldap</h3>
<p>To use the <tt>&quot;openldap&quot;</tt> plugin you first need to configure the <i>OpenLDAP</i> server correctly. The backend database <tt>&quot;monitor&quot;</tt> needs to be loaded and working. See <i><a href="/docs/linux/man/5-slapd-monitor/">slapd-monitor</a></i>(5) for the details. </p>
<p> The configuration of the <tt>&quot;openldap&quot;</tt> plugin consists of one or more <code>Instance</code> blocks. Each block requires one string argument as the instance name. For example: </p>
<pre> &lt;Plugin &quot;openldap&quot;&gt;
 &lt;Instance &quot;foo&quot;&gt;
 URL &quot;<a href="ldap://localhost/">ldap://localhost/</a>&quot;
 &lt;/Instance&gt;
 &lt;Instance &quot;bar&quot;&gt;
 URL &quot;<a href="ldaps://localhost/">ldaps://localhost/</a>&quot;
 &lt;/Instance&gt;
 &lt;/Plugin&gt;</pre>
<p>The instance name will be used as the <i>plugin instance</i>. To emulate the old (version 4) behavior, you can use an empty string (&quot;&quot;). In order for the plugin to work correctly, each instance name must be unique. This is not enforced by the plugin and it is your responsibility to ensure it is. </p>
<p> The following options are accepted within each <code>Instance</code> block:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i><a href="ldap://host/binddn">ldap://host/binddn</a></i></p>
<dd>Sets the <font SIZE="-1">URL</font> to use to connect to the <i>OpenLDAP</i> server. This option is <i>mandatory</i>.</p>
<dt><code>BindDN</code> <i>BindDN</i></p>
<dd>Name in the form of an <font SIZE="-1">LDAP</font> distinguished name intended to be used for authentication. Defaults to empty string to establish an anonymous authorization.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Password for simple bind authentication. If this option is not set, unauthenticated bind operation is used.</p>
<dt><code>StartTLS</code> <code>true|false</code></p>
<dd>Defines whether <font SIZE="-1">TLS</font> must be used when connecting to the <i>OpenLDAP</i> server. Disabled by default.</p>
<dt><code>VerifyHost</code> <code>true|false</code></p>
<dd>Enables or disables peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Enabled by default.</p>
<dt><code>CACert</code> <i>File</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">TLS/SSL</font> you may possibly need this option. What <font SIZE="-1">CA</font> certificates are checked by default depends on the distribution you use and can be changed with the usual ldap client configuration mechanisms. See <i><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></i>(5) for the details.</p>
<dt><code>Timeout</code> <i>Seconds</i></p>
<dd>Sets the timeout value for ldap operations, in seconds. By default, the configured <code>Interval</code> is used to set the timeout. Use <code>-1</code> to disable (infinite timeout).</p>
<dt><code>Version</code> <i>Version</i></p>
<dd>An integer which sets the <font SIZE="-1">LDAP</font> protocol version number to use when connecting to the <i>OpenLDAP</i> server. Defaults to <code>3</code> for using <i>LDAPv3</i>.</dl>
<h3>Plugin openvpn</h3>
<p>The OpenVPN plugin reads a status file maintained by OpenVPN and gathers traffic statistics about connected clients. </p>
<p> To set up OpenVPN to write to the status file periodically, use the <code>&#8211;status</code> option of OpenVPN. Since OpenVPN can write two different formats, you need to set the required format, too. This is done by setting <code>&#8211;status-version</code> to <code>2</code>. </p>
<p> So, in a nutshell you need: </p>
<pre> openvpn $OTHER_OPTIONS \
 --status &quot;/var/run/openvpn-status&quot; 10 \
 --status-version 2</pre>
<p>Available options:</p>
<dl>
<dt><code>StatusFile</code> <i>File</i></p>
<dd>Specifies the location of the status file.</p>
<dt><code>ImprovedNamingSchema</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the filename of the status file will be used as plugin instance and the client&#8217;s &#8220;common name&#8221; will be used as type instance. This is required when reading multiple status files. Enabling this option is recommended, but to maintain backwards compatibility this option is disabled by default.</p>
<dt><code>CollectCompression</code> <code>true</code>|<code>false</code></p>
<dd>Sets whether or not statistics about the compression used by OpenVPN should be collected. This information is only available in <i>single</i> mode. Enabled by default.</p>
<dt><code>CollectIndividualUsers</code> <code>true</code>|<code>false</code></p>
<dd>Sets whether or not traffic information is collected for each connected client individually. If set to false, currently no traffic data is collected at all because aggregating this data in a save manner is tricky. Defaults to <code>true</code>.</p>
<dt><code>CollectUserCount</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the number of currently connected clients or users is collected. This is especially interesting when <code>CollectIndividualUsers</code> is disabled, but can be configured independently from that option. Defaults to <code>false</code>.</dl>
<h3>Plugin oracle</h3>
<p>The &#8220;oracle&#8221; plugin uses the OracleX Call Interface <i>(</i><font SIZE="-1"><i>OCI</i></font><i>)</i> to connect to an OracleX Database and lets you execute <font SIZE="-1">SQL</font> statements there. It is very similar to the &#8220;dbi&#8221; plugin, because it was written around the same time. See the &#8220;dbi&#8221; plugin&#8217;s documentation above for details. </p>
<pre> &lt;Plugin oracle&gt;
 &lt;Query &quot;out_of_stock&quot;&gt;
 Statement &quot;SELECT category, COUNT(*) AS value FROM products WHERE in_stock = 0 GROUP BY category&quot;
 &lt;Result&gt;
 Type &quot;gauge&quot;
 # InstancePrefix &quot;foo&quot;
 InstancesFrom &quot;category&quot;
 ValuesFrom &quot;value&quot;
 &lt;/Result&gt;
 &lt;/Query&gt;
 &lt;Database &quot;product_information&quot;&gt;
 ConnectID &quot;db01&quot;
 Username &quot;oracle&quot;
 Password &quot;secret&quot;
 Query &quot;out_of_stock&quot;
 &lt;/Database&gt;
 &lt;/Plugin&gt;</pre>
<p><i></i>Query<i> blocks</i> </p>
<p> The Query blocks are handled identically to the Query blocks of the &#8220;dbi&#8221; plugin. Please see its documentation above for details on how to specify queries. </p>
<p> <i></i>Database<i> blocks</i> </p>
<p> Database blocks define a connection to a database and which queries should be sent to that database. Each database needs a &#8220;name&#8221; as string argument in the starting tag of the block. This name will be used as &#8220;PluginInstance&#8221; in the values submitted to the daemon. Other than that, that name is not used.</p>
<dl>
<dt><code>ConnectID</code> <i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>Defines the &#8220;database alias&#8221; or &#8220;service name&#8221; to connect to. Usually, these names are defined in the file named <tt>&quot;$ORACLE_HOME/network/admin/tnsnames.ora&quot;</tt>.</p>
<dt><code>Host</code> <i>Host</i></p>
<dd>Hostname to use when dispatching values for this database. Defaults to using the global hostname of the <i>collectd</i> instance.</p>
<dt><code>Username</code> <i>Username</i></p>
<dd>Username used for authentication.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Password used for authentication.</p>
<dt><code>Query</code> <i>QueryName</i></p>
<dd>Associates the query named <i>QueryName</i> with this database connection. The query needs to be defined <i>before</i> this statement, i. e. all query blocks you want to refer to must be placed above the database block you want to refer to them from.</dl>
<h3>Plugin perl</h3>
<p>This plugin embeds a Perl-interpreter into collectd and provides an interface to collectd&#8217;s plugin system. See <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5) for its documentation.</p>
<h3>Plugin pinba</h3>
<p>The <i>Pinba plugin</i> receives profiling information from <i>Pinba</i>, an extension for the <i></i><font SIZE="-1"><i>PHP</i></font><i></i> interpreter. At the end of executing a script, i.e. after a PHP-based webpage has been delivered, the extension will send a <font SIZE="-1">UDP</font> packet containing timing information, peak memory usage and so on. The plugin will wait for such packets, parse them and account the provided information, which is then dispatched to the daemon once per interval. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin pinba&gt;
 Address &quot;::0&quot;
 Port &quot;30002&quot;
 # Overall statistics for the website.
 &lt;View &quot;www-total&quot;&gt;
 Server &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;
 &lt;/View&gt;
 # Statistics for www-a only
 &lt;View &quot;www-a&quot;&gt;
 Host &quot;www-a.example.com&quot;
 Server &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;
 &lt;/View&gt;
 # Statistics for www-b only
 &lt;View &quot;www-b&quot;&gt;
 Host &quot;www-b.example.com&quot;
 Server &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;
 &lt;/View&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin provides the following configuration options:</p>
<dl>
<dt><code>Address</code> <i>Node</i></p>
<dd>Configures the address used to open a listening socket. By default, plugin will bind to the <i>any</i> address <tt>&quot;::0&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Configures the port (service) to bind to. By default the default Pinba port &#8220;30002&#8221; will be used. The option accepts service names in addition to port numbers and thus requires a <i>string</i> argument.</p>
<dt>&lt;<code>View</code> <i>Name</i>&gt; block</p>
<dd>The packets sent by the Pinba extension include the hostname of the server, the server name (the name of the virtual host) and the script that was executed. Using <code>View</code> blocks it is possible to separate the data into multiple groups to get more meaningful statistics. Each packet is added to all matching groups, so that a packet may be accounted for more than once.</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>Matches the hostname of the system the webserver / script is running on. This will contain the result of the <i><a href="/docs/linux/man/2-gethostname/">gethostname</a></i>(2) system call. If not configured, all hostnames will be accepted.</p>
<dt><code>Server</code> <i>Server</i></p>
<dd>Matches the name of the <i>virtual host</i>, i.e. the contents of the <tt>$_SERVER[&quot;SERVER_NAME&quot;]</tt> variable when within <font SIZE="-1">PHP.</font> If not configured, all server names will be accepted.</p>
<dt><code>Script</code> <i>Script</i></p>
<dd>Matches the name of the <i>script name</i>, i.e. the contents of the <tt>$_SERVER[&quot;SCRIPT_NAME&quot;]</tt> variable when within <font SIZE="-1">PHP.</font> If not configured, all script names will be accepted.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin ping</h3>
<p>The <i>Ping</i> plugin starts a new thread which sends <font SIZE="-1">ICMP </font>&#8220;ping&#8221; packets to the configured hosts periodically and measures the network latency. Whenever the <tt>&quot;read&quot;</tt> function of the plugin is called, it submits the average latency, the standard deviation and the drop rate for each host. </p>
<p> Available configuration options:</p>
<dl>
<dt><code>Host</code> <i>IP-address</i></p>
<dd>Host to ping periodically. This option may be repeated several times to ping multiple hosts.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Sets the interval in which to send <font SIZE="-1">ICMP</font> echo packets to the configured hosts. This is <code>not</code> the interval in which statistics are queries from the plugin but the interval in which the hosts are &#8220;pinged&#8221;. Therefore, the setting here should be smaller than or equal to the global <code>Interval</code> setting. Fractional times, such as &#8220;1.24&#8221; are allowed. </p>
<p> Default: <code>1.0</code></p>
<dt><code>Timeout</code> <i>Seconds</i></p>
<dd>Time to wait for a response from the host to which an <font SIZE="-1">ICMP</font> packet had been sent. If a reply was not received after <i>Seconds</i> seconds, the host is assumed to be down or the packet to be dropped. This setting must be smaller than the <code>Interval</code> setting above for the plugin to work correctly. Fractional arguments are accepted. </p>
<p> Default: <code>0.9</code></p>
<dt><font SIZE="-1"><code>TTL</code></font> <i>0-255</i></p>
<dd>Sets the Time-To-Live of generated <font SIZE="-1">ICMP</font> packets.</p>
<dt><code>Size</code> <i>size</i></p>
<dd>Sets the size of the data payload in <font SIZE="-1">ICMP</font> packet to specified <i>size</i> (it will be filled with regular <font SIZE="-1">ASCII</font> pattern). If not set, default 56 byte long string is used so that the packet size of an ICMPv4 packet is exactly 64 bytes, similar to the behaviour of normal <i><a href="/docs/linux/man/1-ping/">ping</a></i>(1) command.</p>
<dt><code>SourceAddress</code> <i>host</i></p>
<dd>Sets the source address to use. <i>host</i> may either be a numerical network address or a network hostname.</p>
<dt><code>Device</code> <i>name</i></p>
<dd>Sets the outgoing network device to be used. <i>name</i> has to specify an interface name (e. g. <tt>&quot;eth0&quot;</tt>). This might not be supported by all operating systems.</p>
<dt><code>MaxMissed</code> <i>Packets</i></p>
<dd>Trigger a <font SIZE="-1">DNS</font> resolve after the host has not replied to <i>Packets</i> packets. This enables the use of dynamic <font SIZE="-1">DNS</font> services (like dyndns.org) with the ping plugin. </p>
<p> Default: <code>-1</code> (disabled)</dl>
<h3>Plugin postgresql</h3>
<p>The <tt>&quot;postgresql&quot;</tt> plugin queries statistics from PostgreSQL databases. It keeps a persistent connection to all configured databases and tries to reconnect if the connection has been interrupted. A database is configured by specifying a <code>Database</code> block as described below. The default statistics are collected from PostgreSQL&#8217;s <code>statistics collector</code> which thus has to be enabled for this plugin to work correctly. This should usually be the case by default. See the section &#8220;The Statistics Collector&#8221; of the <code>PostgreSQL Documentation</code> for details. </p>
<p> By specifying custom database queries using a <code>Query</code> block as described below, you may collect any data that is available from some PostgreSQL database. This way, you are able to access statistics of external daemons which are available in a PostgreSQL database or use future or special statistics provided by PostgreSQL without the need to upgrade your collectd installation. </p>
<p> Starting with version 5.2, the <tt>&quot;postgresql&quot;</tt> plugin supports writing data to PostgreSQL databases as well. This has been implemented in a generic way. You need to specify an <font SIZE="-1">SQL</font> statement which will then be executed by collectd in order to write the data (see below for details). The benefit of that approach is that there is no fixed database layout. Rather, the layout may be optimized for the current setup. </p>
<p> The <code>PostgreSQL Documentation</code> manual can be found at &lt;<a rel="nofollow" href="http://www.postgresql.org/docs/manuals/">http://www.postgresql.org/docs/manuals/</a>&gt;. </p>
<pre> &lt;Plugin postgresql&gt;
 &lt;Query magic&gt;
 Statement &quot;SELECT magic FROM wizard WHERE host = $1;&quot;
 Param hostname
 &lt;Result&gt;
 Type gauge
 InstancePrefix &quot;magic&quot;
 ValuesFrom magic
 &lt;/Result&gt;
 &lt;/Query&gt;
 &lt;Query rt36_tickets&gt;
 Statement &quot;SELECT COUNT(type) AS count, type \
 FROM (SELECT CASE \
 WHEN resolved = 'epoch' THEN 'open' \
 ELSE 'resolved' END AS type \
 FROM tickets) type \
 GROUP BY type;&quot;
 &lt;Result&gt;
 Type counter
 InstancePrefix &quot;rt36_tickets&quot;
 InstancesFrom &quot;type&quot;
 ValuesFrom &quot;count&quot;
 &lt;/Result&gt;
 &lt;/Query&gt;
 &lt;Writer sqlstore&gt;
 Statement &quot;SELECT collectd_insert($1, $2, $3, $4, $5, $6, $7, $8, $9);&quot;
 StoreRates true
 &lt;/Writer&gt;
 &lt;Database foo&gt;
 Host &quot;hostname&quot;
 Port &quot;5432&quot;
 User &quot;username&quot;
 Password &quot;secret&quot;
 SSLMode &quot;prefer&quot;
 KRBSrvName &quot;kerberos_service_name&quot;
 Query magic
 &lt;/Database&gt;
 &lt;Database bar&gt;
 Interval 300
 Service &quot;service_name&quot;
 Query backend # predefined
 Query rt36_tickets
 &lt;/Database&gt;
 &lt;Database qux&gt;
 # ...
 Writer sqlstore
 CommitInterval 10
 &lt;/Database&gt;
 &lt;/Plugin&gt;</pre>
<p>The <code>Query</code> block defines one database query which may later be used by a database definition. It accepts a single mandatory argument which specifies the name of the query. The names of all queries have to be unique (see the <code>MinVersion</code> and <code>MaxVersion</code> options below for an exception to this rule). </p>
<p> In each <code>Query</code> block, there is one or more <code>Result</code> blocks. Multiple <code>Result</code> blocks may be used to extract multiple values from a single query. </p>
<p> The following configuration options are available to define the query:</p>
<dl>
<dt><code>Statement</code> <i>sql query statement</i></p>
<dd>Specify the <i>sql query statement</i> which the plugin should execute. The string may contain the tokens $1, $2, etc. which are used to reference the first, second, etc. parameter. The value of the parameters is specified by the <code>Param</code> configuration option &#8211; see below for details. To include a literal <code>$</code> character followed by a number, surround it with single quotes (<code>&#8216;</code>). </p>
<p> Any <font SIZE="-1">SQL</font> command which may return data (such as <tt>&quot;SELECT&quot;</tt> or <tt>&quot;SHOW&quot;</tt>) is allowed. Note, however, that only a single command may be used. Semicolons are allowed as long as a single non-empty command has been specified only. </p>
<p> The returned lines will be handled separately one after another.</p>
<dt><code>Param</code> <i>hostname</i>|<i>database</i>|<i>instance</i>|<i>username</i>|<i>interval</i></p>
<dd>Specify the parameters which should be passed to the <font SIZE="-1">SQL</font> query. The parameters are referred to in the <font SIZE="-1">SQL</font> query as $1, $2, etc. in the same order as they appear in the configuration file. The value of the parameter is determined depending on the value of the <code>Param</code> option as follows:</p>
<dl>
<dd>
<dl>
<dt><i>hostname</i></p>
<dd>The configured hostname of the database connection. If a <font SIZE="-1">UNIX</font> domain socket is used, the parameter expands to &#8220;localhost&#8221;.</p>
<dt><i>database</i></p>
<dd>The name of the database of the current connection.</p>
<dt><i>instance</i></p>
<dd>The name of the database plugin instance. See the <code>Instance</code> option of the database specification below for details.</p>
<dt><i>username</i></p>
<dd>The username used to connect to the database.</p>
<dt><i>interval</i></p>
<dd>The interval with which this database is queried (as specified by the database specific or global <code>Interval</code> options).</dl>
</dl>
<dl>
<dd>Please note that parameters are only supported by PostgreSQL&#8217;s protocol version 3 and above which was introduced in version 7.4 of PostgreSQL.</dl>
<dt><code>PluginInstanceFrom</code> <i>column</i></p>
<dd>Specify how to create the &#8220;PluginInstance&#8221; for reporting this query results. Only one column is supported. You may concatenate fields and string values in the query statement to get the required results.</p>
<dt><code>MinVersion</code> <i>version</i></p>
<dd>
<dt><code>MaxVersion</code> <i>version</i></p>
<dd>Specify the minimum or maximum version of PostgreSQL that this query should be used with. Some statistics might only be available with certain versions of PostgreSQL. This allows you to specify multiple queries with the same name but which apply to different versions, thus allowing you to use the same configuration in a heterogeneous environment. </p>
<p> The <i>version</i> has to be specified as the concatenation of the major, minor and patch-level versions, each represented as two-decimal-digit numbers. For example, version 8.2.3 will become 80203.</dl>
<p> The <code>Result</code> block defines how to handle the values returned from the query. It defines which column holds which value and how to dispatch that value to the daemon.</p>
<dl>
<dt><code>Type</code> <i>type</i></p>
<dd>The <i>type</i> name to be used when dispatching the values. The type describes how to handle the data and where to store it. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for more details on types and their configuration. The number and type of values (as selected by the <code>ValuesFrom</code> option) has to match the type of the given name. </p>
<p> This option is mandatory.</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>
<dt><code>InstancesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>Specify how to create the &#8220;TypeInstance&#8221; for each data set (i. e. line). <code>InstancePrefix</code> defines a static prefix that will be prepended to all type instances. <code>InstancesFrom</code> defines the column names whose values will be used to create the type instance. Multiple values will be joined together using the hyphen (<tt>&quot;-&quot;</tt>) as separation character. </p>
<p> The plugin itself does not check whether or not all built instances are different. It is your responsibility to assure that each is unique. </p>
<p> Both options are optional. If none is specified, the type instance will be empty.</p>
<dt><code>ValuesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>Names the columns whose content is used as the actual data for the data sets that are dispatched to the daemon. How many such columns you need is determined by the <code>Type</code> setting as explained above. If you specify too many or not enough columns, the plugin will complain about that and no data will be submitted to the daemon. </p>
<p> The actual data type, as seen by PostgreSQL, is not that important as long as it represents numbers. The plugin will automatically cast the values to the right type if it know how to do that. For that, it uses the <i><a href="/docs/linux/man/3-strtoll/">strtoll</a></i>(3) and <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3) functions, so anything supported by those functions is supported by the plugin as well. </p>
<p> This option is required inside a <code>Result</code> block and may be specified multiple times. If multiple <code>ValuesFrom</code> options are specified, the columns are read in the given order.</dl>
<p> The following predefined queries are available (the definitions can be found in the <i>postgresql_default.conf</i> file which, by default, is available at <tt>&quot;</tt>prefix<tt>/share/collectd/&quot;</tt>):</p>
<dl>
<dt><code>backends</code></p>
<dd>This query collects the number of backends, i. e. the number of connected clients.</p>
<dt><code>transactions</code></p>
<dd>This query collects the numbers of committed and rolled-back transactions of the user tables.</p>
<dt><code>queries</code></p>
<dd>This query collects the numbers of various table modifications (i. e. insertions, updates, deletions) of the user tables.</p>
<dt><code>query_plans</code></p>
<dd>This query collects the numbers of various table scans and returned tuples of the user tables.</p>
<dt><code>table_states</code></p>
<dd>This query collects the numbers of live and dead rows in the user tables.</p>
<dt><code>disk_io</code></p>
<dd>This query collects disk block access counts for user tables.</p>
<dt><code>disk_usage</code></p>
<dd>This query collects the on-disk size of the database in bytes.</dl>
<p> In addition, the following detailed queries are available by default. Please note that each of those queries collects information <code>by table</code>, thus, potentially producing <code>a lot</code> of data. For details see the description of the non-by_table queries above.</p>
<dl>
<dt><code>queries_by_table</code></p>
<dd>
<dt><code>query_plans_by_table</code></p>
<dd>
<dt><code>table_states_by_table</code></p>
<dd>
<dt><code>disk_io_by_table</code></p>
<dd></dl>
<p> The <code>Writer</code> block defines a PostgreSQL writer backend. It accepts a single mandatory argument specifying the name of the writer. This will then be used in the <code>Database</code> specification in order to activate the writer instance. The names of all writers have to be unique. The following options may be specified:</p>
<dl>
<dt><code>Statement</code> <i>sql statement</i></p>
<dd>This mandatory option specifies the <font SIZE="-1">SQL</font> statement that will be executed for each submitted value. A single <font SIZE="-1">SQL</font> statement is allowed only. Anything after the first semicolon will be ignored. </p>
<p> Nine parameters will be passed to the statement and should be specified as tokens $1, $2, through $9 in the statement string. The following values are made available through those parameters:</p>
<dl>
<dd>
<dl>
<dt><code>$1</code></p>
<dd>The timestamp of the queried value as an <font SIZE="-1">RFC</font> 3339-formatted local time.</p>
<dt><code>$2</code></p>
<dd>The hostname of the queried value.</p>
<dt><code>$3</code></p>
<dd>The plugin name of the queried value.</p>
<dt><code>$4</code></p>
<dd>The plugin instance of the queried value. This value may be <font SIZE="-1"><code>NULL</code></font> if there is no plugin instance.</p>
<dt><code>$5</code></p>
<dd>The type of the queried value (cf. <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5)).</p>
<dt><code>$6</code></p>
<dd>The type instance of the queried value. This value may be <font SIZE="-1"><code>NULL</code></font> if there is no type instance.</p>
<dt><code>$7</code></p>
<dd>An array of names for the submitted values (i. e., the name of the data sources of the submitted value-list).</p>
<dt><code>$8</code></p>
<dd>An array of types for the submitted values (i. e., the type of the data sources of the submitted value-list; <tt>&quot;counter&quot;</tt>, <tt>&quot;gauge&quot;</tt>, &#8230;). Note, that if <code>StoreRates</code> is enabled (which is the default, see below), all types will be <tt>&quot;gauge&quot;</tt>.</p>
<dt><code>$9</code></p>
<dd>An array of the submitted values. The dimensions of the value name and value arrays match.</dl>
</dl>
<dl>
<dd>In general, it is advisable to create and call a custom function in the PostgreSQL database for this purpose. Any procedural language supported by PostgreSQL will do (see chapter &#8220;Server Programming&#8221; in the PostgreSQL manual for details).</dl>
<dt><code>StoreRates</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i. e. as an increasing integer number.</dl>
<p> The <code>Database</code> block defines one PostgreSQL database for which to collect statistics. It accepts a single mandatory argument which specifies the database name. None of the other options are required. PostgreSQL will use default values as documented in the section &#8220;<font SIZE="-1">CONNECTING TO A DATABASE&#8221;</font> in the <i><a href="/docs/linux/man/1-psql/">psql</a></i>(1) manpage. However, be aware that those defaults may be influenced by the user collectd is run as and special environment variables. See the manpage for details.</p>
<dl>
<dt><code>Interval</code> <i>seconds</i></p>
<dd>Specify the interval with which the database should be queried. The default is to use the global <code>Interval</code> setting.</p>
<dt><code>CommitInterval</code> <i>seconds</i></p>
<dd>This option may be used for database connections which have &#8220;writers&#8221; assigned (see above). If specified, it causes a writer to put several updates into a single transaction. This transaction will last for the specified amount of time. By default, each update will be executed in a separate transaction. Each transaction generates a fair amount of overhead which can, thus, be reduced by activating this option. The draw-back is, that data covering the specified amount of time will be lost, for example, if a single statement within the transaction fails or if the database server crashes.</p>
<dt><code>Instance</code> <i>name</i></p>
<dd>Specify the plugin instance name that should be used instead of the database name (which is the default, if this option has not been specified). This allows one to query multiple databases of the same name on the same host (e.g. when running multiple database server versions in parallel). The plugin instance name can also be set from the query result using the <code>PluginInstanceFrom</code> option in <code>Query</code> block.</p>
<dt><code>Host</code> <i>hostname</i></p>
<dd>Specify the hostname or <font SIZE="-1">IP</font> of the PostgreSQL server to connect to. If the value begins with a slash, it is interpreted as the directory name in which to look for the <font SIZE="-1">UNIX</font> domain socket. </p>
<p> This option is also used to determine the hostname that is associated with a collected data set. If it has been omitted or either begins with with a slash or equals <code>localhost</code> it will be replaced with the global hostname definition of collectd. Any other value will be passed literally to collectd when dispatching values. Also see the global <code>Hostname</code> and <code>FQDNLookup</code> options.</p>
<dt><code>Port</code> <i>port</i></p>
<dd>Specify the <font SIZE="-1">TCP</font> port or the local <font SIZE="-1">UNIX</font> domain socket file extension of the server.</p>
<dt><code>User</code> <i>username</i></p>
<dd>Specify the username to be used when connecting to the server.</p>
<dt><code>Password</code> <i>password</i></p>
<dd>Specify the password to be used when connecting to the server.</p>
<dt><code>ExpireDelay</code> <i>delay</i></p>
<dd>Skip expired values in query output.</p>
<dt><code>SSLMode</code> <i>disable</i>|<i>allow</i>|<i>prefer</i>|<i>require</i></p>
<dd>Specify whether to use an <font SIZE="-1">SSL</font> connection when contacting the server. The following modes are supported:</p>
<dl>
<dd>
<dl>
<dt><i>disable</i></p>
<dd>Do not use <font SIZE="-1">SSL</font> at all.</p>
<dt><i>allow</i></p>
<dd>First, try to connect without using <font SIZE="-1">SSL.</font> If that fails, try using <font SIZE="-1">SSL.</font></p>
<dt><i>prefer</i> (default)</p>
<dd>First, try to connect using <font SIZE="-1">SSL.</font> If that fails, try without using <font SIZE="-1">SSL.</font></p>
<dt><i>require</i></p>
<dd>Use <font SIZE="-1">SSL</font> only.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Instance</code> <i>name</i></p>
<dd>Specify the plugin instance name that should be used instead of the database name (which is the default, if this option has not been specified). This allows one to query multiple databases of the same name on the same host (e.g. when running multiple database server versions in parallel).</p>
<dt><code>KRBSrvName</code> <i>kerberos_service_name</i></p>
<dd>Specify the Kerberos service name to use when authenticating with Kerberos 5 or <font SIZE="-1">GSSAPI.</font> See the sections &#8220;Kerberos authentication&#8221; and &#8220;<font SIZE="-1">GSSAPI&#8221;</font> of the <code>PostgreSQL Documentation</code> for details.</p>
<dt><code>Service</code> <i>service_name</i></p>
<dd>Specify the PostgreSQL service name to use for additional parameters. That service has to be defined in <i>pg_service.conf</i> and holds additional connection parameters. See the section &#8220;The Connection Service File&#8221; in the <code>PostgreSQL Documentation</code> for details.</p>
<dt><code>Query</code> <i>query</i></p>
<dd>Specifies a <i>query</i> which should be executed in the context of the database connection. This may be any of the predefined or user-defined queries. If no such option is given, it defaults to &#8220;backends&#8221;, &#8220;transactions&#8221;, &#8220;queries&#8221;, &#8220;query_plans&#8221;, &#8220;table_states&#8221;, &#8220;disk_io&#8221; and &#8220;disk_usage&#8221; (unless a <code>Writer</code> has been specified). Else, the specified queries are used only.</p>
<dt><code>Writer</code> <i>writer</i></p>
<dd>Assigns the specified <i>writer</i> backend to the database connection. This causes all collected data to be send to the database using the settings defined in the writer configuration (see the section &#8220;<font SIZE="-1">FILTER CONFIGURATION&#8221;</font> below for details on how to selectively send data to certain plugins). </p>
<p> Each writer will register a flush callback which may be used when having long transactions enabled (see the <code>CommitInterval</code> option above). When issuing the <font SIZE="-1"><code>FLUSH</code></font> command (see <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5) for details) the current transaction will be committed right away. Two different kinds of flush callbacks are available with the <tt>&quot;postgresql&quot;</tt> plugin:</p>
<dl>
<dd>
<dl>
<dt><code>postgresql</code></p>
<dd>Flush all writer backends.</p>
<dt><code>postgresql-</code><i>database</i></p>
<dd>Flush all writers of the specified <i>database</i> only.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin powerdns</h3>
<p>The <tt>&quot;powerdns&quot;</tt> plugin queries statistics from an authoritative PowerDNS nameserver and/or a PowerDNS recursor. Since both offer a wide variety of values, many of which are probably meaningless to most users, but may be useful for some. So you may chose which values to collect, but if you don&#8217;t, some reasonable defaults will be collected. </p>
<pre> &lt;Plugin &quot;powerdns&quot;&gt;
 &lt;Server &quot;server_name&quot;&gt;
 Collect &quot;latency&quot;
 Collect &quot;udp-answers&quot; &quot;udp-queries&quot;
 Socket &quot;/var/run/pdns.controlsocket&quot;
 &lt;/Server&gt;
 &lt;Recursor &quot;recursor_name&quot;&gt;
 Collect &quot;questions&quot;
 Collect &quot;cache-hits&quot; &quot;cache-misses&quot;
 Socket &quot;/var/run/pdns_recursor.controlsocket&quot;
 &lt;/Recursor&gt;
 LocalSocket &quot;/opt/collectd/var/run/collectd-powerdns&quot;
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>Server</code> and <code>Recursor</code> block</p>
<dd>The <code>Server</code> block defines one authoritative server to query, the <code>Recursor</code> does the same for an recursing server. The possible options in both blocks are the same, though. The argument defines a name for the server&nbsp;<wbr>/ recursor and is required.</p>
<dl>
<dd>
<dl>
<dt><code>Collect</code> <i>Field</i></p>
<dd>Using the <code>Collect</code> statement you can select which values to collect. Here, you specify the name of the values as used by the PowerDNS servers, e. g. <tt>&quot;dlg-only-drops&quot;</tt>, <tt>&quot;answers10-100&quot;</tt>. </p>
<p> The method of getting the values differs for <code>Server</code> and <code>Recursor</code> blocks: When querying the server a <tt>&quot;SHOW *&quot;</tt> command is issued in any case, because that&#8217;s the only way of getting multiple values out of the server at once. collectd then picks out the values you have selected. When querying the recursor, a command is generated to query exactly these values. So if you specify invalid fields when querying the recursor, a syntax error may be returned by the daemon and collectd may not collect any values at all. </p>
<p> If no <code>Collect</code> statement is given, the following <code>Server</code> values will be collected:</p>
<dl>
<dd>
<dl>
<dt>latency</p>
<dd>
<dt>packetcache-hit</p>
<dd>
<dt>packetcache-miss</p>
<dd>
<dt>packetcache-size</p>
<dd>
<dt>query-cache-hit</p>
<dd>
<dt>query-cache-miss</p>
<dd>
<dt>recursing-answers</p>
<dd>
<dt>recursing-questions</p>
<dd>
<dt>tcp-answers</p>
<dd>
<dt>tcp-queries</p>
<dd>
<dt>udp-answers</p>
<dd>
<dt>udp-queries</p>
<dd></dl>
</dl>
<dl>
<dd>The following <code>Recursor</code> values will be collected by default:</p>
<dl>
<dt>noerror-answers</p>
<dd>
<dt>nxdomain-answers</p>
<dd>
<dt>servfail-answers</p>
<dd>
<dt>sys-msec</p>
<dd>
<dt>user-msec</p>
<dd>
<dt>qa-latency</p>
<dd>
<dt>cache-entries</p>
<dd>
<dt>cache-hits</p>
<dd>
<dt>cache-misses</p>
<dd>
<dt>questions</p>
<dd></dl>
</dl>
<dl>
<dd>Please note that up to that point collectd doesn&#8217;t know what values are available on the server and values that are added do not need a change of the mechanism so far. However, the values must be mapped to collectd&#8217;s naming scheme, which is done using a lookup table that lists all known values. If values are added in the future and collectd does not know about them, you will get an error much like this: </p>
<pre> powerdns plugin: submit: Not found in lookup table: foobar = 42</pre>
<p>In this case please file a bug report with the collectd team.</dl>
<dt><code>Socket</code> <i>Path</i></p>
<dd>Configures the path to the <font SIZE="-1">UNIX</font> domain socket to be used when connecting to the daemon. By default <tt>&quot;${localstatedir}/run/pdns.controlsocket&quot;</tt> will be used for an authoritative server and <tt>&quot;${localstatedir}/run/pdns_recursor.controlsocket&quot;</tt> will be used for the recursor.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>LocalSocket</code> <i>Path</i></p>
<dd>Querying the recursor is done using <font SIZE="-1">UDP.</font> When using <font SIZE="-1">UDP</font> over <font SIZE="-1">UNIX</font> domain sockets, the client socket needs a name in the file system, too. You can set this local name to <i>Path</i> using the <code>LocalSocket</code> option. The default is <tt>&quot;</tt>prefix<tt>/var/run/collectd-powerdns&quot;</tt>.</dl>
<h3>Plugin processes</h3>
<dl>
<dt><code>Process</code> <i>Name</i></p>
<dd>Select more detailed statistics of processes matching this name. The statistics collected for these selected processes are size of the resident segment size (<font SIZE="-1">RSS</font>), user- and system-time used, number of processes and number of threads, io data (where available) and minor and major pagefaults. </p>
<p> Some platforms have a limit on the length of process names. <i>Name</i> must stay below this limit.</p>
<dt><code>ProcessMatch</code> <i>name</i> <i>regex</i></p>
<dd>Similar to the <code>Process</code> option this allows one to select more detailed statistics of processes matching the specified <i>regex</i> (see <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7) for details). The statistics of all matching processes are summed up and dispatched to the daemon using the specified <i>name</i> as an identifier. This allows one to &#8220;group&#8221; several processes together. <i>name</i> must not contain slashes.</p>
<dt><code>CollectContextSwitch</code> <i>Boolean</i></p>
<dd>Collect context switch of the process.</dl>
<h3>Plugin protocols</h3>
<p>Collects a lot of information about various network protocols, such as <i></i><font SIZE="-1"><i>IP</i></font><i></i>, <i></i><font SIZE="-1"><i>TCP</i></font><i></i>, <i></i><font SIZE="-1"><i>UDP</i></font><i></i>, etc. </p>
<p> Available configuration options:</p>
<dl>
<dt><code>Value</code> <i>Selector</i></p>
<dd>Selects whether or not to select a specific value. The string being matched is of the form &quot;<i>Protocol</i>:<i>ValueName</i>&quot;, where <i>Protocol</i> will be used as the plugin instance and <i>ValueName</i> will be used as type instance. An example of the string being used would be <tt>&quot;Tcp:RetransSegs&quot;</tt>. </p>
<p> You can use regular expressions to match a large number of values with just one configuration option. To select all &#8220;extended&#8221; <i></i><font SIZE="-1"><i>TCP</i></font><i></i> values, you could use the following statement: </p>
<pre> Value &quot;/^TcpExt:/&quot;</pre>
<p>Whether only matched values are selected or all matched values are ignored depends on the <code>IgnoreSelected</code>. By default, only matched values are selected. If no value is configured at all, all values will be selected.</p>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, inverts the selection made by <code>Value</code>, i. e. all matching values will be ignored.</dl>
<h3>Plugin python</h3>
<p>This plugin embeds a Python-interpreter into collectd and provides an interface to collectd&#8217;s plugin system. See <i><a href="/docs/linux/man/5-collectd-python/">collectd-python</a></i>(5) for its documentation.</p>
<h3>Plugin routeros</h3>
<p>The <tt>&quot;routeros&quot;</tt> plugin connects to a device running <i>RouterOS</i>, the Linux-based operating system for routers by <i>MikroTik</i>. The plugin uses <i>librouteros</i> to connect and reads information about the interfaces and wireless connections of the device. The configuration supports querying multiple routers: </p>
<pre> &lt;Plugin &quot;routeros&quot;&gt;
 &lt;Router&gt;
 Host &quot;router0.example.com&quot;
 User &quot;collectd&quot;
 Password &quot;secr3t&quot;
 CollectInterface true
 CollectCPULoad true
 CollectMemory true
 &lt;/Router&gt;
 &lt;Router&gt;
 Host &quot;router1.example.com&quot;
 User &quot;collectd&quot;
 Password &quot;5ecret&quot;
 CollectInterface true
 CollectRegistrationTable true
 CollectDF true
 CollectDisk true
 &lt;/Router&gt;
 &lt;/Plugin&gt;</pre>
<p>As you can see above, the configuration of the <i>routeros</i> plugin consists of one or more <code>&lt;Router&gt;</code> blocks. Within each block, the following options are understood:</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>Hostname or IP-address of the router to connect to.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>Port name or port number used when connecting. If left unspecified, the default will be chosen by <i>librouteros</i>, currently &#8220;8728&#8221;. This option expects a string argument, even when a numeric port number is given.</p>
<dt><code>User</code> <i>User</i></p>
<dd>Use the user name <i>User</i> to authenticate. Defaults to &#8220;admin&#8221;.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Set the password used to authenticate.</p>
<dt><code>CollectInterface</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, interface statistics will be collected for all interfaces present on the device. Defaults to <code>false</code>.</p>
<dt><code>CollectRegistrationTable</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, information about wireless <font SIZE="-1">LAN</font> connections will be collected. Defaults to <code>false</code>.</p>
<dt><code>CollectCPULoad</code> <code>true</code>|<code>false</code></p>
<dd>When set to <code>true</code>, information about the <font SIZE="-1">CPU</font> usage will be collected. The number is a dimensionless value where zero indicates no <font SIZE="-1">CPU</font> usage at all. Defaults to <code>false</code>.</p>
<dt><code>CollectMemory</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the amount of used and free memory will be collected. How used memory is calculated is unknown, for example whether or not caches are counted as used space. Defaults to <code>false</code>.</p>
<dt><code>CollectDF</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the amount of used and free disk space will be collected. Defaults to <code>false</code>.</p>
<dt><code>CollectDisk</code> <code>true</code>|<code>false</code></p>
<dd>When enabled, the number of sectors written and bad blocks will be collected. Defaults to <code>false</code>.</dl>
<h3>Plugin redis</h3>
<p>The <i>Redis plugin</i> connects to one or more Redis servers and gathers information about each server&#8217;s state. For each server there is a <i>Node</i> block which configures the connection parameters for this node. </p>
<pre> &lt;Plugin redis&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;6379&quot;
 Timeout 2000
 &lt;Query &quot;LLEN myqueue&quot;&gt;
 Type &quot;queue_length&quot;
 Instance &quot;myqueue&quot;
 &lt;Query&gt;
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>The information shown in the synopsis above is the <i>default configuration</i> which is used by the plugin if no configuration is present.</p>
<dl>
<dt><code>Node</code> <i>Nodename</i></p>
<dd>The <code>Node</code> block identifies a new Redis node, that is a new Redis instance running in an specified host and port. The name for node is a canonical identifier which is used as <i>plugin instance</i>. It is limited to 64 characters in length.</p>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>The <code>Host</code> option is the hostname or IP-address where the Redis instance is running on.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>The <code>Port</code> option is the <font SIZE="-1">TCP</font> port on which the Redis instance accepts connections. Either a service name of a port number may be given. Please note that numerical port numbers must be given as a string, too.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Use <i>Password</i> to authenticate when connecting to <i>Redis</i>.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option set the socket timeout for node response. Since the Redis read function is blocking, you should keep this value as low as possible. Keep in mind that the sum of all <code>Timeout</code> values for all <code>Nodes</code> should be lower than <code>Interval</code> defined globally.</p>
<dt><code>Query</code> <i>Querystring</i></p>
<dd>The <code>Query</code> block identifies a query to execute against the redis server. There may be an arbitrary number of queries to execute.</p>
<dt><code>Type</code> <i>Collectd type</i></p>
<dd>Within a query definition, a valid collectd type to use as when submitting the result of the query. When not supplied, will default to <code>gauge</code>.</p>
<dt><code>Instance</code> <i>Type instance</i></p>
<dd>Within a query definition, an optional type instance to use when submitting the result of the query. When not supplied will default to the escaped command, up to 64 chars.</dl>
<h3>Plugin rrdcached</h3>
<p>The <tt>&quot;rrdcached&quot;</tt> plugin uses the RRDtool accelerator daemon, <i><a href="/docs/linux/man/1-rrdcached/">rrdcached</a></i>(1), to store values to <font SIZE="-1">RRD</font> files in an efficient manner. The combination of the <tt>&quot;rrdcached&quot;</tt> <code>plugin</code> and the <tt>&quot;rrdcached&quot;</tt> <code>daemon</code> is very similar to the way the <tt>&quot;rrdtool&quot;</tt> plugin works (see below). The added abstraction layer provides a number of benefits, though: Because the cache is not within <tt>&quot;collectd&quot;</tt> anymore, it does not need to be flushed when <tt>&quot;collectd&quot;</tt> is to be restarted. This results in much shorter (if any) gaps in graphs, especially under heavy load. Also, the <tt>&quot;rrdtool&quot;</tt> command line utility is aware of the daemon so that it can flush values to disk automatically when needed. This allows one to integrate automated flushing of values into graphing solutions much more easily. </p>
<p> There are disadvantages, though: The daemon may reside on a different host, so it may not be possible for <tt>&quot;collectd&quot;</tt> to create the appropriate <font SIZE="-1">RRD</font> files anymore. And even if <tt>&quot;rrdcached&quot;</tt> runs on the same host, it may run in a different base directory, so relative paths may do weird stuff if you&#8217;re not careful. </p>
<p> So the <code>recommended configuration</code> is to let <tt>&quot;collectd&quot;</tt> and <tt>&quot;rrdcached&quot;</tt> run on the same host, communicating via a <font SIZE="-1">UNIX</font> domain socket. The <code>DataDir</code> setting should be set to an absolute path, so that a changed base directory does not result in <font SIZE="-1">RRD</font> files being created&nbsp;<wbr>/ expected in the wrong place.</p>
<dl>
<dt><code>DaemonAddress</code> <i>Address</i></p>
<dd>Address of the daemon as understood by the <tt>&quot;rrdc_connect&quot;</tt> function of the <font SIZE="-1">RRD</font> library. See <i><a href="/docs/linux/man/1-rrdcached/">rrdcached</a></i>(1) for details. Example: </p>
<pre> &lt;Plugin &quot;rrdcached&quot;&gt;
 DaemonAddress &quot;unix:/var/run/rrdcached.sock&quot;
 &lt;/Plugin&gt;</pre>
<dt><code>DataDir</code> <i>Directory</i></p>
<dd>Set the base directory in which the <font SIZE="-1">RRD</font> files reside. If this is a relative path, it is relative to the working base directory of the <tt>&quot;rrdcached&quot;</tt> daemon! Use of an absolute path is recommended.</p>
<dt><code>CreateFiles</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables the creation of <font SIZE="-1">RRD</font> files. If the daemon is not running locally, or <code>DataDir</code> is set to a relative path, this will not work as expected. Default is <code>true</code>.</p>
<dt><code>CreateFilesAsync</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, new <font SIZE="-1">RRD</font> files are enabled asynchronously, using a separate thread that runs in the background. This prevents writes to block, which is a problem especially when many hundreds of files need to be created at once. However, since the purpose of creating the files asynchronously is <i>not</i> to block until the file is available, values before the file is available will be discarded. When disabled (the default) files are created synchronously, blocking for a short while, while the file is being written.</p>
<dt><code>StepSize</code> <i>Seconds</i></p>
<dd><code>Force</code> the stepsize of newly created RRD-files. Ideally (and per default) this setting is unset and the stepsize is set to the interval in which the data is collected. Do not use this option unless you absolutely have to for some reason. Setting this option may cause problems with the <tt>&quot;snmp plugin&quot;</tt>, the <tt>&quot;exec plugin&quot;</tt> or when the daemon is set up to receive data from other hosts.</p>
<dt><code>HeartBeat</code> <i>Seconds</i></p>
<dd><code>Force</code> the heartbeat of newly created RRD-files. This setting should be unset in which case the heartbeat is set to twice the <code>StepSize</code> which should equal the interval in which data is collected. Do not set this option unless you have a very good reason to do so.</p>
<dt><code>RRARows</code> <i>NumRows</i></p>
<dd>The <tt>&quot;rrdtool plugin&quot;</tt> calculates the number of PDPs per <font SIZE="-1">CDP</font> based on the <code>StepSize</code>, this setting and a timespan. This plugin creates RRD-files with three times five RRAs, i. e. five RRAs with the CFs <font SIZE="-1"><code>MIN</code></font>, <font SIZE="-1"><code>AVERAGE</code></font>, and <font SIZE="-1"><code>MAX</code></font>. The five RRAs are optimized for graphs covering one hour, one day, one week, one month, and one year. </p>
<p> So for each timespan, it calculates how many PDPs need to be consolidated into one <font SIZE="-1">CDP</font> by calculating:<br />
&nbsp;<wbr>&nbsp;<wbr>number of PDPs&nbsp;<wbr>=&nbsp;<wbr>timespan&nbsp;<wbr>/&nbsp;<wbr>(stepsize&nbsp;<wbr>*&nbsp;<wbr>rrarows) </p>
<p> Bottom line is, set this no smaller than the width of you graphs in pixels. The default is 1200.</p>
<dt><code>RRATimespan</code> <i>Seconds</i></p>
<dd>Adds an RRA-timespan, given in seconds. Use this option multiple times to have more then one <font SIZE="-1">RRA.</font> If this option is never used, the built-in default of (3600, 86400, 604800, 2678400, 31622400) is used. </p>
<p> For more information on how RRA-sizes are calculated see <code>RRARows</code> above.</p>
<dt><font SIZE="-1"><code>XFF</code></font> <i>Factor</i></p>
<dd>Set the &#8220;XFiles Factor&#8221;. The default is 0.1. If unsure, don&#8217;t set this option. <i>Factor</i> must be in the range <tt>&quot;[0.0-1.0)&quot;</tt>, i.e. between zero (inclusive) and one (exclusive).</p>
<dt><code>CollectStatistics</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>true</code>, various statistics about the <i>rrdcached</i> daemon will be collected, with &#8220;rrdcached&#8221; as the <i>plugin name</i>. Defaults to <code>false</code>. </p>
<p> Statistics are read via <i>rrdcached</i>s socket using the <font SIZE="-1">STATS</font> command. See <i><a href="/docs/linux/man/1-rrdcached/">rrdcached</a></i>(1) for details.</dl>
<h3>Plugin rrdtool</h3>
<p>You can use the settings <code>StepSize</code>, <code>HeartBeat</code>, <code>RRARows</code>, and <font SIZE="-1"><code>XFF</code></font> to fine-tune your RRD-files. Please read <i><a href="/docs/linux/man/1-rrdcreate/">rrdcreate</a></i>(1) if you encounter problems using these settings. If you don&#8217;t want to dive into the depths of RRDtool, you can safely ignore these settings.</p>
<dl>
<dt><code>DataDir</code> <i>Directory</i></p>
<dd>Set the directory to store <font SIZE="-1">RRD</font> files under. By default <font SIZE="-1">RRD</font> files are generated beneath the daemon&#8217;s working directory, i.e. the <code>BaseDir</code>.</p>
<dt><code>CreateFilesAsync</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, new <font SIZE="-1">RRD</font> files are enabled asynchronously, using a separate thread that runs in the background. This prevents writes to block, which is a problem especially when many hundreds of files need to be created at once. However, since the purpose of creating the files asynchronously is <i>not</i> to block until the file is available, values before the file is available will be discarded. When disabled (the default) files are created synchronously, blocking for a short while, while the file is being written.</p>
<dt><code>StepSize</code> <i>Seconds</i></p>
<dd><code>Force</code> the stepsize of newly created RRD-files. Ideally (and per default) this setting is unset and the stepsize is set to the interval in which the data is collected. Do not use this option unless you absolutely have to for some reason. Setting this option may cause problems with the <tt>&quot;snmp plugin&quot;</tt>, the <tt>&quot;exec plugin&quot;</tt> or when the daemon is set up to receive data from other hosts.</p>
<dt><code>HeartBeat</code> <i>Seconds</i></p>
<dd><code>Force</code> the heartbeat of newly created RRD-files. This setting should be unset in which case the heartbeat is set to twice the <code>StepSize</code> which should equal the interval in which data is collected. Do not set this option unless you have a very good reason to do so.</p>
<dt><code>RRARows</code> <i>NumRows</i></p>
<dd>The <tt>&quot;rrdtool plugin&quot;</tt> calculates the number of PDPs per <font SIZE="-1">CDP</font> based on the <code>StepSize</code>, this setting and a timespan. This plugin creates RRD-files with three times five RRAs, i.e. five RRAs with the CFs <font SIZE="-1"><code>MIN</code></font>, <font SIZE="-1"><code>AVERAGE</code></font>, and <font SIZE="-1"><code>MAX</code></font>. The five RRAs are optimized for graphs covering one hour, one day, one week, one month, and one year. </p>
<p> So for each timespan, it calculates how many PDPs need to be consolidated into one <font SIZE="-1">CDP</font> by calculating:<br />
&nbsp;<wbr>&nbsp;<wbr>number of PDPs&nbsp;<wbr>=&nbsp;<wbr>timespan&nbsp;<wbr>/&nbsp;<wbr>(stepsize&nbsp;<wbr>*&nbsp;<wbr>rrarows) </p>
<p> Bottom line is, set this no smaller than the width of you graphs in pixels. The default is 1200.</p>
<dt><code>RRATimespan</code> <i>Seconds</i></p>
<dd>Adds an RRA-timespan, given in seconds. Use this option multiple times to have more then one <font SIZE="-1">RRA.</font> If this option is never used, the built-in default of (3600, 86400, 604800, 2678400, 31622400) is used. </p>
<p> For more information on how RRA-sizes are calculated see <code>RRARows</code> above.</p>
<dt><font SIZE="-1"><code>XFF</code></font> <i>Factor</i></p>
<dd>Set the &#8220;XFiles Factor&#8221;. The default is 0.1. If unsure, don&#8217;t set this option. <i>Factor</i> must be in the range <tt>&quot;[0.0-1.0)&quot;</tt>, i.e. between zero (inclusive) and one (exclusive).</p>
<dt><code>CacheFlush</code> <i>Seconds</i></p>
<dd>When the <tt>&quot;rrdtool&quot;</tt> plugin uses a cache (by setting <code>CacheTimeout</code>, see below) it writes all values for a certain RRD-file if the oldest value is older than (or equal to) the number of seconds specified. If some RRD-file is not updated anymore for some reason (the computer was shut down, the network is broken, etc.) some values may still be in the cache. If <code>CacheFlush</code> is set, then the entire cache is searched for entries older than <code>CacheTimeout</code> seconds and written to disk every <i>Seconds</i> seconds. Since this is kind of expensive and does nothing under normal circumstances, this value should not be too small. 900 seconds might be a good value, though setting this to 7200 seconds doesn&#8217;t normally do much harm either.</p>
<dt><code>CacheTimeout</code> <i>Seconds</i></p>
<dd>If this option is set to a value greater than zero, the <tt>&quot;rrdtool plugin&quot;</tt> will save values in a cache, as described above. Writing multiple values at once reduces IO-operations and thus lessens the load produced by updating the files. The trade off is that the graphs kind of &#8220;drag behind&#8221; and that more memory is used.</p>
<dt><code>WritesPerSecond</code> <i>Updates</i></p>
<dd>When collecting many statistics with collectd and the <tt>&quot;rrdtool&quot;</tt> plugin, you will run serious performance problems. The <code>CacheFlush</code> setting and the internal update queue assert that collectd continues to work just fine even under heavy load, but the system may become very unresponsive and slow. This is a problem especially if you create graphs from the <font SIZE="-1">RRD</font> files on the same machine, for example using the <tt>&quot;graph.cgi&quot;</tt> script included in the <tt>&quot;contrib/collection3/&quot;</tt> directory. </p>
<p> This setting is designed for very large setups. Setting this option to a value between 25 and 80 updates per second, depending on your hardware, will leave the server responsive enough to draw graphs even while all the cached values are written to disk. Flushed values, i. e. values that are forced to disk by the <font SIZE="-1"><code>FLUSH</code></font> command, are <code>not</code> effected by this limit. They are still written as fast as possible, so that web frontends have up to date data when generating graphs. </p>
<p> For example: If you have 100,000 <font SIZE="-1">RRD</font> files and set <code>WritesPerSecond</code> to 30 updates per second, writing all values to disk will take approximately 56 minutes. Together with the flushing ability that&#8217;s integrated into &#8220;collection3&#8221; you&#8217;ll end up with a responsive and fast system, up to date graphs and basically a &#8220;backup&#8221; of your values every hour.</p>
<dt><code>RandomTimeout</code> <i>Seconds</i></p>
<dd>When set, the actual timeout for each value is chosen randomly between <i>CacheTimeout</i>&#8211;<i>RandomTimeout</i> and <i>CacheTimeout</i>+<i>RandomTimeout</i>. The intention is to avoid high load situations that appear when many values timeout at the same time. This is especially a problem shortly after the daemon starts, because all values were added to the internal cache at roughly the same time.</dl>
<h3>Plugin sensors</h3>
<p>The <i>Sensors plugin</i> uses <code>lm_sensors</code> to retrieve sensor-values. This means that all the needed modules have to be loaded and lm_sensors has to be configured (most likely by editing <i>/etc/sensors.conf</i>. Read <i><a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a></i>(5) for details. </p>
<p> The <code>lm_sensors</code> homepage can be found at &lt;<a rel="nofollow" href="http://secure.netroedge.com/~lm78/">http://secure.netroedge.com/~lm78/</a>&gt;.</p>
<dl>
<dt><code>SensorConfigFile</code> <i>File</i></p>
<dd>Read the <i>lm_sensors</i> configuration from <i>File</i>. When unset (recommended), the library&#8217;s default will be used.</p>
<dt><code>Sensor</code> <i>chip-bus-address/type-feature</i></p>
<dd>Selects the name of the sensor which you want to collect or ignore, depending on the <code>IgnoreSelected</code> below. For example, the option &quot;<code>Sensor</code> <i>it8712-isa-0290/voltage-in1</i>&quot; will cause collectd to gather data for the voltage sensor <i>in1</i> of the <i>it8712</i> on the isa bus at the address 0290.</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>If no configuration if given, the <code>sensors</code>-plugin will collect data from all sensors. This may not be practical, especially for uninteresting sensors. Thus, you can use the <code>Sensor</code>-option to pick the sensors you&#8217;re interested in. Sometimes, however, it&#8217;s easier/preferred to collect all sensors <i>except</i> a few ones. This option enables you to do that: By setting <code>IgnoreSelected</code> to <i>true</i> the effect of <code>Sensor</code> is inverted: All selected sensors are ignored and all other sensors are collected.</p>
<dt><code>UseLabels</code> <i>true</i>|<i>false</i></p>
<dd>Configures how sensor readings are reported. When set to <i>true</i>, sensor readings are reported using their descriptive label (e.g. &#8220;VCore&#8221;). When set to <i>false</i> (the default) the sensor name is used (&#8220;in0&#8221;).</dl>
<h3>Plugin sigrok</h3>
<p>The <i>sigrok plugin</i> uses <i>libsigrok</i> to retrieve measurements from any device supported by the sigrok &lt;<a rel="nofollow" href="http://sigrok.org/">http://sigrok.org/</a>&gt; project. </p>
<p> <code>Synopsis</code> </p>
<pre> &lt;Plugin sigrok&gt;
 LogLevel 3
 &lt;Device &quot;AC Voltage&quot;&gt;
 Driver &quot;fluke-dmm&quot;
 MinimumInterval 10
 Conn &quot;/dev/ttyUSB2&quot;
 &lt;/Device&gt;
 &lt;Device &quot;Sound Level&quot;&gt;
 Driver &quot;cem-dt-885x&quot;
 Conn &quot;/dev/ttyUSB1&quot;
 &lt;/Device&gt;
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>LogLevel</code> <code>0-5</code></p>
<dd>The <i>sigrok</i> logging level to pass on to the <i>collectd</i> log, as a number between <code>0</code> and <code>5</code> (inclusive). These levels correspond to <tt>&quot;None&quot;</tt>, <tt>&quot;Errors&quot;</tt>, <tt>&quot;Warnings&quot;</tt>, <tt>&quot;Informational&quot;</tt>, <tt>&quot;Debug &quot;</tt>and <tt>&quot;Spew&quot;</tt>, respectively. The default is <code>2</code> (<tt>&quot;Warnings&quot;</tt>). The <i>sigrok</i> log messages, regardless of their level, are always submitted to <i>collectd</i> at its <font SIZE="-1">INFO</font> log level.</p>
<dt>&lt;<code>Device</code> <i>Name</i>&gt;</p>
<dd>A sigrok-supported device, uniquely identified by this section&#8217;s options. The <i>Name</i> is passed to <i>collectd</i> as the <i>plugin instance</i>.</p>
<dt><code>Driver</code> <i>DriverName</i></p>
<dd>The sigrok driver to use for this device.</p>
<dt><code>Conn</code> <i>ConnectionSpec</i></p>
<dd>If the device cannot be auto-discovered, or more than one might be discovered by the driver, <i>ConnectionSpec</i> specifies the connection string to the device. It can be of the form of a device path (e.g.&nbsp;<wbr><tt>&quot;/dev/ttyUSB2&quot;</tt>), or, in case of a non-serial USB-connected device, the <font SIZE="-1">USB </font><i>VendorID</i><code>.</code><i>ProductID</i> separated by a period (e.g.&nbsp;<wbr><tt>0403.6001</tt>). A <font SIZE="-1">USB</font> device can also be specified as <i>Bus</i><code>.</code><i>Address</i> (e.g.&nbsp;<wbr><tt>1.41</tt>).</p>
<dt><code>SerialComm</code> <i>SerialSpec</i></p>
<dd>For serial devices with non-standard port settings, this option can be used to specify them in a form understood by <i>sigrok</i>, e.g.&nbsp;<wbr><tt>&quot;9600/8n1&quot;</tt>. This should not be necessary; drivers know how to communicate with devices they support.</p>
<dt><code>MinimumInterval</code> <i>Seconds</i></p>
<dd>Specifies the minimum time between measurement dispatches to <i>collectd</i>, in seconds. Since some <i>sigrok</i> supported devices can acquire measurements many times per second, it may be necessary to throttle these. For example, the <i></i><font SIZE="-1"><i>RRD</i></font><i> plugin</i> cannot process writes more than once per second. </p>
<p> The default <code>MinimumInterval</code> is <code>0</code>, meaning measurements received from the device are always dispatched to <i>collectd</i>. When throttled, unused measurements are discarded.</dl>
<h3>Plugin smart</h3>
<p>The <tt>&quot;smart&quot;</tt> plugin collects <font SIZE="-1">SMART</font> information from physical disks. Values collectd include temperature, power cycle count, poweron time and bad sectors. Also, all <font SIZE="-1">SMART</font> attributes are collected along with the normalized current value, the worst value, the threshold and a human readable value. </p>
<p> Using the following two options you can ignore some disks or configure the collection only of specific disks.</p>
<dl>
<dt><code>Disk</code> <i>Name</i></p>
<dd>Select the disk <i>Name</i>. Whether it is collected or ignored depends on the <code>IgnoreSelected</code> setting, see below. As with other plugins that use the daemon&#8217;s ignorelist functionality, a string that starts and ends with a slash is interpreted as a regular expression. Examples: </p>
<pre> Disk &quot;sdd&quot;
 Disk &quot;/hda[34]/&quot;</pre>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Sets whether selected disks, i. e. the ones matches by any of the <code>Disk</code> statements, are ignored or if all other disks are ignored. The behavior (hopefully) is intuitive: If no <code>Disk</code> option is configured, all disks are collected. If at least one <code>Disk</code> option is given and no <code>IgnoreSelected</code> or set to <code>false</code>, <code>only</code> matching disks will be collected. If <code>IgnoreSelected</code> is set to <code>true</code>, all disks are collected <code>except</code> the ones matched.</p>
<dt><code>IgnoreSleepMode</code> <code>true</code>|<code>false</code></p>
<dd>Normally, the <tt>&quot;smart&quot;</tt> plugin will ignore disks that are reported to be asleep. This option disables the sleep mode check and allows the plugin to collect data from these disks anyway. This is useful in cases where libatasmart mistakenly reports disks as asleep because it has not been updated to incorporate support for newer idle states in the <font SIZE="-1">ATA</font> spec.</p>
<dt><code>UseSerial</code> <code>true</code>|<code>false</code></p>
<dd>A disk&#8217;s kernel name (e.g., sda) can change from one boot to the next. If this option is enabled, the <tt>&quot;smart&quot;</tt> plugin will use the disk&#8217;s serial number (e.g., <font SIZE="-1">HGST_HUH728080ALE600_2EJ8VH8X</font>) instead of the kernel name as the key for storing data. This ensures that the data for a given disk will be kept together even if the kernel name changes.</dl>
<h3>Plugin snmp</h3>
<p>Since the configuration of the <tt>&quot;snmp plugin&quot;</tt> is a little more complicated than other plugins, its documentation has been moved to an own manpage, <i><a href="/docs/linux/man/5-collectd-snmp/">collectd-snmp</a></i>(5). Please see there for details.</p>
<h3>Plugin statsd</h3>
<p>The <i>statsd plugin</i> listens to a <font SIZE="-1">UDP</font> socket, reads &#8220;events&#8221; in the statsd protocol and dispatches rates or other aggregates of these numbers periodically. </p>
<p> The plugin implements the <i>Counter</i>, <i>Timer</i>, <i>Gauge</i> and <i>Set</i> types which are dispatched as the <i>collectd</i> types <tt>&quot;derive&quot;</tt>, <tt>&quot;latency&quot;</tt>, <tt>&quot;gauge&quot;</tt> and <tt>&quot;objects&quot;</tt> respectively. </p>
<p> The following configuration options are valid:</p>
<dl>
<dt><code>Host</code> <i>Host</i></p>
<dd>Bind to the hostname / address <i>Host</i>. By default, the plugin will bind to the &#8220;any&#8221; address, i.e. accept packets sent to any of the hosts addresses.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd><font SIZE="-1">UDP</font> port to listen to. This can be either a service name or a port number. Defaults to <tt>8125</tt>.</p>
<dt><code>DeleteCounters</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>DeleteTimers</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>DeleteGauges</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>DeleteSets</code> <code>false</code>|<code>true</code></p>
<dd>These options control what happens if metrics are not updated in an interval. If set to <code>False</code>, the default, metrics are dispatched unchanged, i.e. the rate of counters and size of sets will be zero, timers report <tt>&quot;NaN&quot;</tt> and gauges are unchanged. If set to <code>True</code>, the such metrics are not dispatched and removed from the internal cache.</p>
<dt><code>CounterSum</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, creates a <tt>&quot;count&quot;</tt> metric which reports the change since the last read. This option primarily exists for compatibility with the <i>statsd</i> implementation by Etsy.</p>
<dt><code>TimerPercentile</code> <i>Percent</i></p>
<dd>Calculate and dispatch the configured percentile, i.e. compute the latency, so that <i>Percent</i> of all reported timers are smaller than or equal to the computed latency. This is useful for cutting off the long tail latency, as it&#8217;s often done in <i>Service Level Agreements</i> (SLAs). </p>
<p> Different percentiles can be calculated by setting this option several times. If none are specified, no percentiles are calculated / dispatched.</p>
<dt><code>TimerLower</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>TimerUpper</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>TimerSum</code> <code>false</code>|<code>true</code></p>
<dd>
<dt><code>TimerCount</code> <code>false</code>|<code>true</code></p>
<dd>Calculate and dispatch various values out of <i>Timer</i> metrics received during an interval. If set to <code>False</code>, the default, these values aren&#8217;t calculated / dispatched.</dl>
<h3>Plugin swap</h3>
<p>The <i>Swap plugin</i> collects information about used and available swap space. On <i>Linux</i> and <i>Solaris</i>, the following options are available:</p>
<dl>
<dt><code>ReportByDevice</code> <code>false</code>|<code>true</code></p>
<dd>Configures how to report physical swap devices. If set to <code>false</code> (the default), the summary over all swap devices is reported only, i.e. the globally used and available space over all devices. If <code>true</code> is configured, the used and available space of each device will be reported separately. </p>
<p> This option is only available if the <i>Swap plugin</i> can read <tt>&quot;/proc/swaps&quot;</tt> (under Linux) or use the <i><a href="/docs/linux/man/2-swapctl/">swapctl</a></i>(2) mechanism (under <i>Solaris</i>).</p>
<dt><code>ReportBytes</code> <code>false</code>|<code>true</code></p>
<dd>When enabled, the <i>swap I/O</i> is reported in bytes. When disabled, the default, <i>swap I/O</i> is reported in pages. This option is available under Linux only.</p>
<dt><code>ValuesAbsolute</code> <code>true</code>|<code>false</code></p>
<dd>Enables or disables reporting of absolute swap metrics, i.e. number of <i>bytes</i> available and used. Defaults to <code>true</code>.</p>
<dt><code>ValuesPercentage</code> <code>false</code>|<code>true</code></p>
<dd>Enables or disables reporting of relative swap metrics, i.e. <i>percent</i> available and free. Defaults to <code>false</code>. </p>
<p> This is useful for deploying <i>collectd</i> in a heterogeneous environment, where swap sizes differ and you want to specify generic thresholds or similar.</dl>
<h3>Plugin syslog</h3>
<dl>
<dt><code>LogLevel</code> <code>debug|info|notice|warning|err</code></p>
<dd>Sets the log-level. If, for example, set to <code>notice</code>, then all events with severity <code>notice</code>, <code>warning</code>, or <code>err</code> will be submitted to the syslog-daemon. </p>
<p> Please note that <code>debug</code> is only available if collectd has been compiled with debugging support.</p>
<dt><code>NotifyLevel</code> <font SIZE="-1"><code>OKAY</code></font>|<font SIZE="-1"><code>WARNING</code></font>|<font SIZE="-1"><code>FAILURE</code></font></p>
<dd>Controls which notifications should be sent to syslog. The default behaviour is not to send any. Less severe notifications always imply logging more severe notifications: Setting this to <font SIZE="-1"><code>OKAY</code></font> means all notifications will be sent to syslog, setting this to <font SIZE="-1"><code>WARNING</code></font> will send <font SIZE="-1"><code>WARNING</code></font> and <font SIZE="-1"><code>FAILURE</code></font> notifications but will dismiss <font SIZE="-1"><code>OKAY</code></font> notifications. Setting this option to <font SIZE="-1"><code>FAILURE</code></font> will only send failures to syslog.</dl>
<h3>Plugin table</h3>
<p>The <tt>&quot;table plugin&quot;</tt> provides generic means to parse tabular data and dispatch user specified values. Values are selected based on column numbers. For example, this plugin may be used to get values from the Linux <i><a href="/docs/linux/man/5-proc/">proc</a></i>(5) filesystem or <font SIZE="-1">CSV </font>(comma separated values) files. </p>
<pre> &lt;Plugin table&gt;
 &lt;Table &quot;/proc/slabinfo&quot;&gt;
 Instance &quot;slabinfo&quot;
 Separator &quot; &quot;
 &lt;Result&gt;
 Type gauge
 InstancePrefix &quot;active_objs&quot;
 InstancesFrom 0
 ValuesFrom 1
 &lt;/Result&gt;
 &lt;Result&gt;
 Type gauge
 InstancePrefix &quot;objperslab&quot;
 InstancesFrom 0
 ValuesFrom 4
 &lt;/Result&gt;
 &lt;/Table&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration consists of one or more <code>Table</code> blocks, each of which configures one file to parse. Within each <code>Table</code> block, there are one or more <code>Result</code> blocks, which configure which data to select and how to interpret it. </p>
<p> The following options are available inside a <code>Table</code> block:</p>
<dl>
<dt><code>Instance</code> <i>instance</i></p>
<dd>If specified, <i>instance</i> is used as the plugin instance. So, in the above example, the plugin name <tt>&quot;table-slabinfo&quot;</tt> would be used. If omitted, the filename of the table is used instead, with all special characters replaced with an underscore (<tt>&quot;_&quot;</tt>).</p>
<dt><code>Separator</code> <i>string</i></p>
<dd>Any character of <i>string</i> is interpreted as a delimiter between the different columns of the table. A sequence of two or more contiguous delimiters in the table is considered to be a single delimiter, i. e. there cannot be any empty columns. The plugin uses the <i><a href="/docs/linux/man/3-strtok_r/">strtok_r</a></i>(3) function to parse the lines of a table &#8211; see its documentation for more details. This option is mandatory. </p>
<p> A horizontal tab, newline and carriage return may be specified by <tt>&quot;\t&quot;</tt>, <tt>&quot;\n&quot;</tt> and <tt>&quot;\r&quot;</tt> respectively. Please note that the double backslashes are required because of collectd&#8217;s config parsing.</dl>
<p> The following options are available inside a <code>Result</code> block:</p>
<dl>
<dt><code>Type</code> <i>type</i></p>
<dd>Sets the type used to dispatch the values to the daemon. Detailed information about types and their configuration can be found in <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5). This option is mandatory.</p>
<dt><code>InstancePrefix</code> <i>prefix</i></p>
<dd>If specified, prepend <i>prefix</i> to the type instance. If omitted, only the <code>InstancesFrom</code> option is considered for the type instance.</p>
<dt><code>InstancesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>If specified, the content of the given columns (identified by the column number starting at zero) will be used to create the type instance for each row. Multiple values (and the instance prefix) will be joined together with dashes (<i>&#8211;</i>) as separation character. If omitted, only the <code>InstancePrefix</code> option is considered for the type instance. </p>
<p> The plugin itself does not check whether or not all built instances are different. ItXs your responsibility to assure that each is unique. This is especially true, if you do not specify <code>InstancesFrom</code>: <code>You</code> have to make sure that the table only contains one row. </p>
<p> If neither <code>InstancePrefix</code> nor <code>InstancesFrom</code> is given, the type instance will be empty.</p>
<dt><code>ValuesFrom</code> <i>column0</i> [<i>column1</i> &#8230;]</p>
<dd>Specifies the columns (identified by the column numbers starting at zero) whose content is used as the actual data for the data sets that are dispatched to the daemon. How many such columns you need is determined by the <code>Type</code> setting above. If you specify too many or not enough columns, the plugin will complain about that and no data will be submitted to the daemon. The plugin uses <i><a href="/docs/linux/man/3-strtoll/">strtoll</a></i>(3) and <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3) to parse counter and gauge values respectively, so anything supported by those functions is supported by the plugin as well. This option is mandatory.</dl>
<h3>Plugin tail</h3>
<p>The <tt>&quot;tail plugin&quot;</tt> follows logfiles, just like <i><a href="/docs/linux/man/1-tail/">tail</a></i>(1) does, parses each line and dispatches found values. What is matched can be configured by the user using (extended) regular expressions, as described in <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7). </p>
<pre> &lt;Plugin &quot;tail&quot;&gt;
 &lt;File &quot;/var/log/exim4/mainlog&quot;&gt;
 Instance &quot;exim&quot;
 Interval 60
 &lt;Match&gt;
 Regex &quot;S=([1-9][0-9]*)&quot;
 DSType &quot;CounterAdd&quot;
 Type &quot;ipt_bytes&quot;
 Instance &quot;total&quot;
 &lt;/Match&gt;
 &lt;Match&gt;
 Regex &quot;\&lt;R=local_user\&gt;&quot;
 ExcludeRegex &quot;\&lt;R=local_user\&gt;.*mail_spool defer&quot;
 DSType &quot;CounterInc&quot;
 Type &quot;counter&quot;
 Instance &quot;local_user&quot;
 &lt;/Match&gt;
 &lt;Match&gt;
 Regex &quot;l=([0-9]*\.[0-9]*)&quot;
 &lt;DSType &quot;Distribution&quot;&gt;
 Percentile 99
 Bucket 0 100
 &lt;/DSType&gt;
 Type &quot;latency&quot;
 Instance &quot;foo&quot;
 &lt;/Match&gt;
 &lt;/File&gt;
 &lt;/Plugin&gt;</pre>
<p>The config consists of one or more <code>File</code> blocks, each of which configures one logfile to parse. Within each <code>File</code> block, there are one or more <code>Match</code> blocks, which configure a regular expression to search for. </p>
<p> The <code>Instance</code> option in the <code>File</code> block may be used to set the plugin instance. So in the above example the plugin name <tt>&quot;tail-foo&quot;</tt> would be used. This plugin instance is for all <code>Match</code> blocks that <code>follow</code> it, until the next <code>Instance</code> option. This way you can extract several plugin instances from one logfile, handy when parsing syslog and the like. </p>
<p> The <code>Interval</code> option allows you to define the length of time between reads. If this is not set, the default Interval will be used. </p>
<p> Each <code>Match</code> block has the following options to describe how the match should be performed:</p>
<dl>
<dt><code>Regex</code> <i>regex</i></p>
<dd>Sets the regular expression to use for matching against a line. The first subexpression has to match something that can be turned into a number by <i><a href="/docs/linux/man/3-strtoll/">strtoll</a></i>(3) or <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3), depending on the value of <tt>&quot;CounterAdd&quot;</tt>, see below. Because <code>extended</code> regular expressions are used, you do not need to use backslashes for subexpressions! If in doubt, please consult <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7). Due to collectd&#8217;s config parsing you need to escape backslashes, though. So if you want to match literal parentheses you need to do the following: </p>
<pre> Regex &quot;SPAM \(Score: (-?[0-9]+\.[0-9]+)\)&quot;</pre>
<dt><code>ExcludeRegex</code> <i>regex</i></p>
<dd>Sets an optional regular expression to use for excluding lines from the match. An example which excludes all connections from localhost from the match: </p>
<pre> ExcludeRegex &quot;127\.0\.0\.1&quot;</pre>
<dt><code>DSType</code> <i>Type</i></p>
<dd>Sets how the values are cumulated. <i>Type</i> is one of:</p>
<dl>
<dd>
<dl>
<dt><code>GaugeAverage</code></p>
<dd>Calculate the average.</p>
<dt><code>GaugeMin</code></p>
<dd>Use the smallest number only.</p>
<dt><code>GaugeMax</code></p>
<dd>Use the greatest number only.</p>
<dt><code>GaugeLast</code></p>
<dd>Use the last number found.</p>
<dt><code>GaugePersist</code></p>
<dd>Use the last number found. The number is not reset at the end of an interval. It is continously reported until another number is matched. This is intended for cases in which only state changes are reported, for example a thermometer that only reports the temperature when it changes.</p>
<dt><code>CounterSet</code></p>
<dd>
<dt><code>DeriveSet</code></p>
<dd>
<dt><code>AbsoluteSet</code></p>
<dd>The matched number is a counter. Simply <i>sets</i> the internal counter to this value. Variants exist for <tt>&quot;COUNTER&quot;</tt>, <tt>&quot;DERIVE&quot;</tt>, and <tt>&quot;ABSOLUTE&quot;</tt> data sources.</p>
<dt><code>GaugeAdd</code></p>
<dd>
<dt><code>CounterAdd</code></p>
<dd>
<dt><code>DeriveAdd</code></p>
<dd>Add the matched value to the internal counter. In case of <code>DeriveAdd</code>, the matched number may be negative, which will effectively subtract from the internal counter.</p>
<dt><code>GaugeInc</code></p>
<dd>
<dt><code>CounterInc</code></p>
<dd>
<dt><code>DeriveInc</code></p>
<dd>Increase the internal counter by one. These <code>DSType</code> are the only ones that do not use the matched subexpression, but simply count the number of matched lines. Thus, you may use a regular expression without submatch in this case.</p>
<dt><code>Distribution</code></p>
<dd>Type to do calculations based on the distribution of values, primarily calculating percentiles. This is primarily geared towards latency, but can be used for other metrics as well. The range of values tracked with this setting must be in the range (0X2^34) and can be fractional. Please note that neither zero nor 2^34 are inclusive bounds, i.e. zero <i>cannot</i> be handled by a distribution. </p>
<p> This option must be used together with the <code>Percentile</code> and/or <code>Bucket</code> options. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;DSType &quot;Distribution&quot;&gt;
 Percentile 99
 Bucket 0 100
 &lt;/DSType&gt;</pre>
<dl>
<dd>
<dl>
<dt><code>Percentile</code> <i>Percent</i></p>
<dd>Calculate and dispatch the configured percentile, i.e. compute the value, so that <i>Percent</i> of all matched values are smaller than or equal to the computed latency. </p>
<p> Metrics are reported with the <i>type</i> <code>Type</code> (the value of the above option) and the <i>type instance</i> <tt>&quot;[&lt;Instance&gt;-]&lt;Percent&gt;&quot;</tt>. </p>
<p> This option may be repeated to calculate more than one percentile.</p>
<dt><code>Bucket</code> <i>lower_bound</i> <i>upper_bound</i></p>
<dd>Export the number of values (a <tt>&quot;DERIVE&quot;</tt>) falling within the given range. Both, <i>lower_bound</i> and <i>upper_bound</i> may be a fractional number, such as <code>0.5</code>. Each <code>Bucket</code> option specifies an interval <tt>&quot;(</tt>lower_bound<tt>, </tt>upper_bound<tt>]&quot;</tt>, i.e. the range <i>excludes</i> the lower bound and <i>includes</i> the upper bound. <i>lower_bound</i> and <i>upper_bound</i> may be zero, meaning no lower/upper bound. </p>
<p> To export the entire (0Xinf) range without overlap, use the upper bound of the previous range as the lower bound of the following range. In other words, use the following schema: </p>
<pre> Bucket 0 1
 Bucket 1 2
 Bucket 2 5
 Bucket 5 10
 Bucket 10 20
 Bucket 20 50
 Bucket 50 0</pre>
<p>Metrics are reported with the <i>type</i> <tt>&quot;bucket&quot;</tt> and the <i>type instance</i> <tt>&quot;&lt;Type&gt;[-&lt;Instance&gt;]-&lt;lower_bound&gt;_&lt;upper_bound&gt;&quot;</tt>. </p>
<p> This option may be repeated to calculate more than one rate.</dl>
</dl>
<dl>
<dd></dl>
</dl>
</dl>
<dl>
<dd>The <code>Gauge*</code> and <code>Distribution</code> types interpret the submatch as a floating point number, using <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3). The <code>Counter*</code> and <code>AbsoluteSet</code> types interpret the submatch as an unsigned integer using <i><a href="/docs/linux/man/3-strtoull/">strtoull</a></i>(3). The <code>Derive*</code> types interpret the submatch as a signed integer using <i><a href="/docs/linux/man/3-strtoll/">strtoll</a></i>(3). <code>CounterInc</code> and <code>DeriveInc</code> do not use the submatch at all and it may be omitted in this case.</dl>
<dt><code>Type</code> <i>Type</i></p>
<dd>Sets the type used to dispatch this value. Detailed information about types and their configuration can be found in <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5).</p>
<dt><code>Instance</code> <i>TypeInstance</i></p>
<dd>This optional setting sets the type instance to use.</dl>
<h3>Plugin tail_csv</h3>
<p>The <i>tail_csv plugin</i> reads files in the <font SIZE="-1">CSV</font> format, e.g. the statistics file written by <i>Snort</i>. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;tail_csv&quot;&gt;
 &lt;Metric &quot;snort-dropped&quot;&gt;
 Type &quot;percent&quot;
 Instance &quot;dropped&quot;
 Index 1
 &lt;/Metric&gt;
 &lt;File &quot;/var/log/snort/snort.stats&quot;&gt;
 Instance &quot;snort-eth0&quot;
 Interval 600
 Collect &quot;snort-dropped&quot;
 &lt;/File&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration consists of one or more <code>Metric</code> blocks that define an index into the line of the <font SIZE="-1">CSV</font> file and how this value is mapped to <i>collectd&#8217;s</i> internal representation. These are followed by one or more <code>Instance</code> blocks which configure which file to read, in which interval and which metrics to extract.</p>
<dl>
<dt>&lt;<code>Metric</code> <i>Name</i>&gt;</p>
<dd>The <code>Metric</code> block configures a new metric to be extracted from the statistics file and how it is mapped on <i>collectd&#8217;s</i> data model. The string <i>Name</i> is only used inside the <code>Instance</code> blocks to refer to this block, so you can use one <code>Metric</code> block for multiple <font SIZE="-1">CSV</font> files.</p>
<dl>
<dd>
<dl>
<dt><code>Type</code> <i>Type</i></p>
<dd>Configures which <i>Type</i> to use when dispatching this metric. Types are defined in the <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) file, see the appropriate manual page for more information on specifying types. Only types with a single <i>data source</i> are supported by the <i>tail_csv plugin</i>. The information whether the value is an absolute value (i.e. a <tt>&quot;GAUGE&quot;</tt>) or a rate (i.e. a <tt>&quot;DERIVE&quot;</tt>) is taken from the <i>Type&#8217;s</i> definition.</p>
<dt><code>Instance</code> <i>TypeInstance</i></p>
<dd>If set, <i>TypeInstance</i> is used to populate the type instance field of the created value lists. Otherwise, no type instance is used.</p>
<dt><code>ValueFrom</code> <i>Index</i></p>
<dd>Configure to read the value from the field with the zero-based index <i>Index</i>. If the value is parsed as signed integer, unsigned integer or double depends on the <code>Type</code> setting, see above.</dl>
</dl>
<dl>
<dd></dl>
<dt>&lt;<code>File</code> <i>Path</i>&gt;</p>
<dd>Each <code>File</code> block represents one <font SIZE="-1">CSV</font> file to read. There must be at least one <i>File</i> block but there can be multiple if you have multiple <font SIZE="-1">CSV</font> files.</p>
<dl>
<dd>
<dl>
<dt><code>Instance</code> <i>PluginInstance</i></p>
<dd>Sets the <i>plugin instance</i> used when dispatching the values.</p>
<dt><code>Collect</code> <i>Metric</i></p>
<dd>Specifies which <i>Metric</i> to collect. This option must be specified at least once, and you can use this option multiple times to specify more than one metric to be extracted from this statistic file.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Configures the interval in which to read values from this instance / file. Defaults to the plugin&#8217;s default interval.</p>
<dt><code>TimeFrom</code> <i>Index</i></p>
<dd>Rather than using the local time when dispatching a value, read the timestamp from the field with the zero-based index <i>Index</i>. The value is interpreted as seconds since epoch. The value is parsed as a double and may be factional.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Plugin teamspeak2</h3>
<p>The <tt>&quot;teamspeak2 plugin&quot;</tt> connects to the query port of a teamspeak2 server and polls interesting global and virtual server data. The plugin can query only one physical server but unlimited virtual servers. You can use the following options to configure it:</p>
<dl>
<dt><code>Host</code> <i>hostname/ip</i></p>
<dd>The hostname or ip which identifies the physical server. Default: 127.0.0.1</p>
<dt><code>Port</code> <i>port</i></p>
<dd>The query port of the physical server. This needs to be a string. Default: &#8220;51234&#8221;</p>
<dt><code>Server</code> <i>port</i></p>
<dd>This option has to be added once for every virtual server the plugin should query. If you want to query the virtual server on port 8767 this is what the option would look like: </p>
<pre> Server &quot;8767&quot;</pre>
<p>This option, although numeric, needs to be a string, i. e. you <code>must</code> use quotes around it! If no such statement is given only global information will be collected.</dl>
<h3>Plugin ted</h3>
<p>The <i></i><font SIZE="-1"><i>TED</i></font><i></i> plugin connects to a device of &#8220;The Energy Detective&#8221;, a device to measure power consumption. These devices are usually connected to a serial (<font SIZE="-1">RS232</font>) or <font SIZE="-1">USB</font> port. The plugin opens a configured device and tries to read the current energy readings. For more information on <font SIZE="-1">TED,</font> visit &lt;<a rel="nofollow" href="http://www.theenergydetective.com/">http://www.theenergydetective.com/</a>&gt;. </p>
<p> Available configuration options:</p>
<dl>
<dt><code>Device</code> <i>Path</i></p>
<dd>Path to the device on which <font SIZE="-1">TED</font> is connected. collectd will need read and write permissions on that file. </p>
<p> Default: <code>/dev/ttyUSB0</code></p>
<dt><code>Retries</code> <i>Num</i></p>
<dd>Apparently reading from <font SIZE="-1">TED</font> is not that reliable. You can therefore configure a number of retries here. You only configure the <i>retries</i> here, to if you specify zero, one reading will be performed (but no retries if that fails); if you specify three, a maximum of four readings are performed. Negative values are illegal. </p>
<p> Default: <code>0</code></dl>
<h3>Plugin tcpconns</h3>
<p>The <tt>&quot;tcpconns plugin&quot;</tt> counts the number of currently established <font SIZE="-1">TCP</font> connections based on the local port and/or the remote port. Since there may be a lot of connections the default if to count all connections with a local port, for which a listening socket is opened. You can use the following options to fine-tune the ports you are interested in:</p>
<dl>
<dt><code>ListeningPorts</code> <i>true</i>|<i>false</i></p>
<dd>If this option is set to <i>true</i>, statistics for all local ports for which a listening socket exists are collected. The default depends on <code>LocalPort</code> and <code>RemotePort</code> (see below): If no port at all is specifically selected, the default is to collect listening ports. If specific ports (no matter if local or remote ports) are selected, this option defaults to <i>false</i>, i. e. only the selected ports will be collected unless this option is set to <i>true</i> specifically.</p>
<dt><code>LocalPort</code> <i>Port</i></p>
<dd>Count the connections to a specific local port. This can be used to see how many connections are handled by a specific daemon, e. g. the mailserver. You have to specify the port in numeric form, so for the mailserver example you&#8217;d need to set <code>25</code>.</p>
<dt><code>RemotePort</code> <i>Port</i></p>
<dd>Count the connections to a specific remote port. This is useful to see how much a remote service is used. This is most useful if you want to know how many connections a local service has opened to remote services, e. g. how many connections a mail server or news server has to other mail or news servers, or how many connections a web proxy holds to web servers. You have to give the port in numeric form.</p>
<dt><code>AllPortsSummary</code> <i>true</i>|<i>false</i></p>
<dd>If this option is set to <i>true</i> a summary of statistics from all connections are collected. This option defaults to <i>false</i>.</dl>
<h3>Plugin thermal</h3>
<dl>
<dt><code>ForceUseProcfs</code> <i>true</i>|<i>false</i></p>
<dd>By default, the <i>Thermal plugin</i> tries to read the statistics from the Linux <tt>&quot;sysfs&quot;</tt> interface. If that is not available, the plugin falls back to the <tt>&quot;procfs&quot;</tt> interface. By setting this option to <i>true</i>, you can force the plugin to use the latter. This option defaults to <i>false</i>.</p>
<dt><code>Device</code> <i>Device</i></p>
<dd>Selects the name of the thermal device that you want to collect or ignore, depending on the value of the <code>IgnoreSelected</code> option. This option may be used multiple times to specify a list of devices.</p>
<dt><code>IgnoreSelected</code> <i>true</i>|<i>false</i></p>
<dd>Invert the selection: If set to true, all devices <code>except</code> the ones that match the device names specified by the <code>Device</code> option are collected. By default only selected devices are collected if a selection is made. If no selection is configured at all, <code>all</code> devices are selected.</dl>
<h3>Plugin threshold</h3>
<p>The <i>Threshold plugin</i> checks values collected or received by <i>collectd</i> against a configurable <i>threshold</i> and issues <i>notifications</i> if values are out of bounds. </p>
<p> Documentation for this plugin is available in the <i><a href="/docs/linux/man/5-collectd-threshold/">collectd-threshold</a></i>(5) manual page.</p>
<h3>Plugin tokyotyrant</h3>
<p>The <i>TokyoTyrant plugin</i> connects to a TokyoTyrant server and collects a couple metrics: number of records, and database size on disk.</p>
<dl>
<dt><code>Host</code> <i>Hostname/IP</i></p>
<dd>The hostname or <font SIZE="-1">IP</font> which identifies the server. Default: <code>127.0.0.1</code></p>
<dt><code>Port</code> <i>Service/Port</i></p>
<dd>The query port of the server. This needs to be a string, even if the port is given in its numeric form. Default: <code>1978</code></dl>
<h3>Plugin turbostat</h3>
<p>The <i>Turbostat plugin</i> reads <font SIZE="-1">CPU</font> frequency and C-state residency on modern Intel processors by using <i>Model Specific Registers</i>.</p>
<dl>
<dt><code>CoreCstates</code> <i>Bitmask(Integer)</i></p>
<dd>Bit mask of the list of core C-states supported by the processor. This option should only be used if the automated detection fails. Default value extracted from the <font SIZE="-1">CPU</font> model and family. </p>
<p> Currently supported C-states (by this plugin): 3, 6, 7 </p>
<p> <code>Example:</code> </p>
<pre> All states (3, 6 and 7):
 (1&lt;&lt;3) + (1&lt;&lt;6) + (1&lt;&lt;7) = 392</pre>
<dt><code>PackageCstates</code> <i>Bitmask(Integer)</i></p>
<dd>Bit mask of the list of packages C-states supported by the processor. This option should only be used if the automated detection fails. Default value extracted from the <font SIZE="-1">CPU</font> model and family. </p>
<p> Currently supported C-states (by this plugin): 2, 3, 6, 7, 8, 9, 10 </p>
<p> <code>Example:</code> </p>
<pre> States 2, 3, 6 and 7:
 (1&lt;&lt;2) + (1&lt;&lt;3) + (1&lt;&lt;6) + (1&lt;&lt;7) = 396</pre>
<dt><code>SystemManagementInterrupt</code> <i>true</i>|<i>false</i></p>
<dd>Boolean enabling the collection of the I/O System-Management Interrupt counter. This option should only be used if the automated detection fails or if you want to disable this feature.</p>
<dt><code>DigitalTemperatureSensor</code> <i>true</i>|<i>false</i></p>
<dd>Boolean enabling the collection of the temperature of each core. This option should only be used if the automated detection fails or if you want to disable this feature.</p>
<dt><code>TCCActivationTemp</code> <i>Temperature</i></p>
<dd><i>Thermal Control Circuit Activation Temperature</i> of the installed <font SIZE="-1">CPU.</font> This temperature is used when collecting the temperature of cores or packages. This option should only be used if the automated detection fails. Default value extracted from <font SIZE="-1"><code>MSR_IA32_TEMPERATURE_TARGET</code></font>.</p>
<dt><code>RunningAveragePowerLimit</code> <i>Bitmask(Integer)</i></p>
<dd>Bit mask of the list of elements to be thermally monitored. This option should only be used if the automated detection fails or if you want to disable some collections. The different bits of this bit mask accepted by this plugin are:</p>
<dl>
<dd>
<dl>
<dt>0 (&#8216;1&#8217;): Package</p>
<dd>
<dt>1 (&#8216;2&#8217;): <font SIZE="-1">DRAM</font></p>
<dd>
<dt>2 (&#8216;4&#8217;): Cores</p>
<dd>
<dt>3 (&#8216;8&#8217;): Embedded graphic device</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>LogicalCoreNames</code> <i>true</i>|<i>false</i></p>
<dd>Boolean enabling the use of logical core numbering for per core statistics. When enabled, <tt>&quot;cpu&lt;n&gt;&quot;</tt> is used as plugin instance, where <i>n</i> is a sequential number assigned by the kernel. Otherwise, <tt>&quot;core&lt;n&gt;&quot;</tt> is used where <i>n</i> is the n-th core of the socket, causing name conflicts when there is more than one socket.</dl>
<h3>Plugin unixsock</h3>
<dl>
<dt><code>SocketFile</code> <i>Path</i></p>
<dd>Sets the socket-file which is to be created.</p>
<dt><code>SocketGroup</code> <i>Group</i></p>
<dd>If running as root change the group of the UNIX-socket after it has been created. Defaults to <code>collectd</code>.</p>
<dt><code>SocketPerms</code> <i>Permissions</i></p>
<dd>Change the file permissions of the UNIX-socket after it has been created. The permissions must be given as a numeric, octal value as you would pass to <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). Defaults to <code>0770</code>.</p>
<dt><code>DeleteSocket</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, delete the socket file before calling <i><a href="/docs/linux/man/2-bind/">bind</a></i>(2), if a file with the given name already exists. If <i>collectd</i> crashes a socket file may be left over, preventing the daemon from opening a new socket when restarted. Since this is potentially dangerous, this defaults to <code>false</code>.</dl>
<h3>Plugin uuid</h3>
<p>This plugin, if loaded, causes the Hostname to be taken from the machine&#8217;s <font SIZE="-1">UUID.</font> The <font SIZE="-1">UUID</font> is a universally unique designation for the machine, usually taken from the machine&#8217;s <font SIZE="-1">BIOS.</font> This is most useful if the machine is running in a virtual environment such as Xen, in which case the <font SIZE="-1">UUID</font> is preserved across shutdowns and migration. </p>
<p> The following methods are used to find the machine&#8217;s <font SIZE="-1">UUID,</font> in order:</p>
<dl>
<dt>&bull;</p>
<dd>Check <i>/etc/uuid</i> (or <i>UUIDFile</i>).</p>
<dt>&bull;</p>
<dd>Check for <font SIZE="-1">UUID</font> from <font SIZE="-1">HAL </font>(&lt;<a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/hal">http://www.freedesktop.org/wiki/Software/hal</a>&gt;) if present.</p>
<dt>&bull;</p>
<dd>Check for <font SIZE="-1">UUID</font> from <tt>&quot;dmidecode&quot;</tt> / <font SIZE="-1">SMBIOS.</font></p>
<dt>&bull;</p>
<dd>Check for <font SIZE="-1">UUID</font> from Xen hypervisor.</dl>
<p> If no <font SIZE="-1">UUID</font> can be found then the hostname is not modified.</p>
<dl>
<dt><code>UUIDFile</code> <i>Path</i></p>
<dd>Take the <font SIZE="-1">UUID</font> from the given file (default <i>/etc/uuid</i>).</dl>
<h3>Plugin varnish</h3>
<p>The <i>varnish plugin</i> collects information about Varnish, an <font SIZE="-1">HTTP</font> accelerator. It collects a subset of the values displayed by <i><a href="/docs/linux/man/1-varnishstat/">varnishstat</a></i>(1), and organizes them in categories which can be enabled or disabled. Currently only metrics shown in <i><a href="/docs/linux/man/1-varnishstat/">varnishstat</a></i>(1)&#8217;s <i></i><font SIZE="-1"><i>MAIN</i></font><i></i> section are collected. The exact meaning of each metric can be found in <i><a href="/docs/linux/man/7-varnish-counters/">varnish-counters</a></i>(7). </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;varnish&quot;&gt;
 &lt;Instance &quot;example&quot;&gt;
 CollectBackend true
 CollectBan false
 CollectCache true
 CollectConnections true
 CollectDirectorDNS false
 CollectESI false
 CollectFetch false
 CollectHCB false
 CollectObjects false
 CollectPurge false
 CollectSession false
 CollectSHM true
 CollectSMA false
 CollectSMS false
 CollectSM false
 CollectStruct false
 CollectTotals false
 CollectUptime false
 CollectVCL false
 CollectVSM false
 CollectWorkers false
 &lt;/Instance&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration consists of one or more &lt;<code>Instance</code>&nbsp;<wbr><i>Name</i>&gt; blocks. <i>Name</i> is the parameter passed to &#8220;varnishd -n&#8221;. If left empty, it will collectd statistics from the default &#8220;varnishd&#8221; instance (this should work fine in most cases). </p>
<p> Inside each &lt;<code>Instance</code>&gt; blocks, the following options are recognized:</p>
<dl>
<dt><code>CollectBackend</code> <code>true</code>|<code>false</code></p>
<dd>Back-end connection statistics, such as successful, reused, and closed connections. True by default.</p>
<dt><code>CollectBan</code> <code>true</code>|<code>false</code></p>
<dd>Statistics about ban operations, such as number of bans added, retired, and number of objects tested against ban operations. Only available with Varnish 3.x and above. False by default.</p>
<dt><code>CollectCache</code> <code>true</code>|<code>false</code></p>
<dd>Cache hits and misses. True by default.</p>
<dt><code>CollectConnections</code> <code>true</code>|<code>false</code></p>
<dd>Number of client connections received, accepted and dropped. True by default.</p>
<dt><code>CollectDirectorDNS</code> <code>true</code>|<code>false</code></p>
<dd><font SIZE="-1">DNS</font> director lookup cache statistics. Only available with Varnish 3.x. False by default.</p>
<dt><code>CollectESI</code> <code>true</code>|<code>false</code></p>
<dd>Edge Side Includes (<font SIZE="-1">ESI</font>) parse statistics. False by default.</p>
<dt><code>CollectFetch</code> <code>true</code>|<code>false</code></p>
<dd>Statistics about fetches (<font SIZE="-1">HTTP</font> requests sent to the backend). False by default.</p>
<dt><code>CollectHCB</code> <code>true</code>|<code>false</code></p>
<dd>Inserts and look-ups in the crit bit tree based hash. Look-ups are divided into locked and unlocked look-ups. False by default.</p>
<dt><code>CollectObjects</code> <code>true</code>|<code>false</code></p>
<dd>Statistics on cached objects: number of objects expired, nuked (prematurely expired), saved, moved, etc. False by default.</p>
<dt><code>CollectPurge</code> <code>true</code>|<code>false</code></p>
<dd>Statistics about purge operations, such as number of purges added, retired, and number of objects tested against purge operations. Only available with Varnish 2.x. False by default.</p>
<dt><code>CollectSession</code> <code>true</code>|<code>false</code></p>
<dd>Client session statistics. Number of past and current sessions, session herd and linger counters, etc. False by default. Note that if using Varnish 4.x, some metrics found in the Connections and Threads sections with previous versions of Varnish have been moved here.</p>
<dt><code>CollectSHM</code> <code>true</code>|<code>false</code></p>
<dd>Statistics about the shared memory log, a memory region to store log messages which is flushed to disk when full. True by default.</p>
<dt><code>CollectSMA</code> <code>true</code>|<code>false</code></p>
<dd>malloc or umem (umem_alloc(3MALLOC) based) storage statistics. The umem storage component is Solaris specific. Only available with Varnish 2.x. False by default.</p>
<dt><code>CollectSMS</code> <code>true</code>|<code>false</code></p>
<dd>synth (synthetic content) storage statistics. This storage component is used internally only. False by default.</p>
<dt><code>CollectSM</code> <code>true</code>|<code>false</code></p>
<dd>file (memory mapped file) storage statistics. Only available with Varnish 2.x. False by default.</p>
<dt><code>CollectStruct</code> <code>true</code>|<code>false</code></p>
<dd>Current varnish internal state statistics. Number of current sessions, objects in cache store, open connections to backends (with Varnish 2.x), etc. False by default.</p>
<dt><code>CollectTotals</code> <code>true</code>|<code>false</code></p>
<dd>Collects overview counters, such as the number of sessions created, the number of requests and bytes transferred. False by default.</p>
<dt><code>CollectUptime</code> <code>true</code>|<code>false</code></p>
<dd>Varnish uptime. Only available with Varnish 3.x and above. False by default.</p>
<dt><code>CollectVCL</code> <code>true</code>|<code>false</code></p>
<dd>Number of total (available + discarded) <font SIZE="-1">VCL </font>(config files). False by default.</p>
<dt><code>CollectVSM</code> <code>true</code>|<code>false</code></p>
<dd>Collect statistics about Varnish&#8217;s shared memory usage (used by the logging and statistics subsystems). Only available with Varnish 4.x. False by default.</p>
<dt><code>CollectWorkers</code> <code>true</code>|<code>false</code></p>
<dd>Collect statistics about worker threads. False by default.</dl>
<h3>Plugin virt</h3>
<p>This plugin allows <font SIZE="-1">CPU,</font> disk and network load to be collected for virtualized guests on the machine. This means that these metrics can be collected for guest systems without installing any software on them &#8211; <i>collectd</i> only runs on the host system. The statistics are collected through libvirt (&lt;<a rel="nofollow" href="http://libvirt.org/">http://libvirt.org/</a>&gt;). </p>
<p> Only <i>Connection</i> is required.</p>
<dl>
<dt><code>Connection</code> <i>uri</i></p>
<dd>Connect to the hypervisor given by <i>uri</i>. For example if using Xen use: </p>
<pre> Connection &quot;<a href="xen:///">xen:///</a>&quot;</pre>
<p>Details which URIs allowed are given at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt;.</p>
<dt><code>RefreshInterval</code> <i>seconds</i></p>
<dd>Refresh the list of domains and devices every <i>seconds</i>. The default is 60 seconds. Setting this to be the same or smaller than the <i>Interval</i> will cause the list of domains and devices to be refreshed on every iteration. </p>
<p> Refreshing the devices in particular is quite a costly operation, so if your virtualization setup is static you might consider increasing this. If this option is set to 0, refreshing is disabled completely.</p>
<dt><code>Domain</code> <i>name</i></p>
<dd>
<dt><code>BlockDevice</code> <i>name:dev</i></p>
<dd>
<dt><code>InterfaceDevice</code> <i>name:dev</i></p>
<dd>
<dt><code>IgnoreSelected</code> <code>true</code>|<code>false</code></p>
<dd>Select which domains and devices are collected. </p>
<p> If <i>IgnoreSelected</i> is not given or <code>false</code> then only the listed domains and disk/network devices are collected. </p>
<p> If <i>IgnoreSelected</i> is <code>true</code> then the test is reversed and the listed domains and disk/network devices are ignored, while the rest are collected. </p>
<p> The domain name and device names may use a regular expression, if the name is surrounded by <i>/&#8230;/</i> and collectd was compiled with support for regexps. </p>
<p> The default is to collect statistics for all domains and all their devices. </p>
<p> Example: </p>
<pre> BlockDevice &quot;/:hdb/&quot;
 IgnoreSelected &quot;true&quot;</pre>
<p>Ignore all <i>hdb</i> devices on any domain, but other block devices (eg. <i>hda</i>) will be collected.</p>
<dt><code>BlockDeviceFormat</code> <code>target</code>|<code>source</code></p>
<dd>If <i>BlockDeviceFormat</i> is set to <code>target</code>, the default, then the device name seen by the guest will be used for reporting metrics. This corresponds to the <tt>&quot;&lt;target&gt;&quot;</tt> node in the <font SIZE="-1">XML</font> definition of the domain. </p>
<p> If <i>BlockDeviceFormat</i> is set to <code>source</code>, then metrics will be reported using the path of the source, e.g. an image file. This corresponds to the <tt>&quot;&lt;source&gt;&quot;</tt> node in the <font SIZE="-1">XML</font> definition of the domain. </p>
<p> <code>Example:</code> </p>
<p> If the domain <font SIZE="-1">XML</font> have the following device defined: </p>
<pre> &lt;disk type='block' device='disk'&gt;
 &lt;driver name='qemu' type='raw' cache='none' io='native' discard='unmap'/&gt;
 &lt;source dev='/var/lib/libvirt/images/image1.qcow2'/&gt;
 &lt;target dev='sda' bus='scsi'/&gt;
 &lt;boot order='2'/&gt;
 &lt;address type='drive' controller='0' bus='0' target='0' unit='0'/&gt;
 &lt;/disk&gt;</pre>
<p>Setting <tt>&quot;BlockDeviceFormat target&quot;</tt> will cause the <i>type instance</i> to be set to <tt>&quot;sda&quot;</tt>. Setting <tt>&quot;BlockDeviceFormat source&quot;</tt> will cause the <i>type instance</i> to be set to <tt>&quot;var_lib_libvirt_images_image1.qcow2&quot;</tt>.</p>
<dt><code>BlockDeviceFormatBasename</code> <code>false</code>|<code>true</code></p>
<dd>The <code>BlockDeviceFormatBasename</code> controls whether the full path or the <i><a href="/docs/linux/man/1-basename/">basename</a></i>(1) of the source is being used as the <i>type instance</i> when <code>BlockDeviceFormat</code> is set to <code>source</code>. Defaults to <code>false</code>. </p>
<p> <code>Example:</code> </p>
<p> Assume the device path (source tag) is <tt>&quot;/var/lib/libvirt/images/image1.qcow2&quot;</tt>. Setting <tt>&quot;BlockDeviceFormatBasename false&quot;</tt> will cause the <i>type instance</i> to be set to <tt>&quot;var_lib_libvirt_images_image1.qcow2&quot;</tt>. Setting <tt>&quot;BlockDeviceFormatBasename true&quot;</tt> will cause the <i>type instance</i> to be set to <tt>&quot;image1.qcow2&quot;</tt>.</p>
<dt><code>HostnameFormat</code> <code>name|uuid|hostname|&#8230;</code></p>
<dd>When the virt plugin logs data, it sets the hostname of the collected data according to this setting. The default is to use the guest name as provided by the hypervisor, which is equal to setting <code>name</code>. </p>
<p> <code>uuid</code> means use the guest&#8217;s <font SIZE="-1">UUID.</font> This is useful if you want to track the same guest across migrations. </p>
<p> <code>hostname</code> means to use the global <code>Hostname</code> setting, which is probably not useful on its own because all guests will appear to have the same name. </p>
<p> You can also specify combinations of these fields. For example <code>name uuid</code> means to concatenate the guest name and <font SIZE="-1">UUID </font>(with a literal colon character between, thus <i>&#8220;foo:1234-1234-1234-1234&#8221;</i>). </p>
<p> At the moment of writing (collectd-5.5), hostname string is limited to 62 characters. In case when combination of fields exceeds 62 characters, hostname will be truncated without a warning.</p>
<dt><code>InterfaceFormat</code> <code>name</code>|<code>address</code></p>
<dd>When the virt plugin logs interface data, it sets the name of the collected data according to this setting. The default is to use the path as provided by the hypervisor (the &#8220;dev&#8221; property of the target node), which is equal to setting <code>name</code>. </p>
<p> <code>address</code> means use the interface&#8217;s mac address. This is useful since the interface path might change between reboots of a guest or across migrations.</p>
<dt><code>PluginInstanceFormat</code> <code>name|uuid|none</code></p>
<dd>When the virt plugin logs data, it sets the plugin_instance of the collected data according to this setting. The default is to not set the plugin_instance. </p>
<p> <code>name</code> means use the guest&#8217;s name as provided by the hypervisor. <code>uuid</code> means use the guest&#8217;s <font SIZE="-1">UUID.</font> </p>
<p> You can also specify combinations of the <code>name</code> and <code>uuid</code> fields. For example <code>name uuid</code> means to concatenate the guest name and <font SIZE="-1">UUID </font>(with a literal colon character between, thus <i>&#8220;foo:1234-1234-1234-1234&#8221;</i>).</dl>
<h3>Plugin vmem</h3>
<p>The <tt>&quot;vmem&quot;</tt> plugin collects information about the usage of virtual memory. Since the statistics provided by the Linux kernel are very detailed, they are collected very detailed. However, to get all the details, you have to switch them on manually. Most people just want an overview over, such as the number of pages read from swap space.</p>
<dl>
<dt><code>Verbose</code> <code>true</code>|<code>false</code></p>
<dd>Enables verbose collection of information. This will start collecting page &#8220;actions&#8221;, e. g. page allocations, (de)activations, steals and so on. Part of these statistics are collected on a &#8220;per zone&#8221; basis.</dl>
<h3>Plugin vserver</h3>
<p>This plugin doesn&#8217;t have any options. <code>VServer</code> support is only available for Linux. It cannot yet be found in a vanilla kernel, though. To make use of this plugin you need a kernel that has <code>VServer</code> support built in, i. e. you need to apply the patches and compile your own kernel, which will then provide the <i>/proc/virtual</i> filesystem that is required by this plugin. </p>
<p> The <code>VServer</code> homepage can be found at &lt;<a rel="nofollow" href="http://linux-vserver.org/">http://linux-vserver.org/</a>&gt;. </p>
<p> <code>Note</code>: The traffic collected by this plugin accounts for the amount of traffic passing a socket which might be a lot less than the actual on-wire traffic (e. g. due to headers and retransmission). If you want to collect on-wire traffic you could, for example, use the logging facilities of iptables to feed data for the guest IPs into the iptables plugin.</p>
<h3>Plugin write_graphite</h3>
<p>The <tt>&quot;write_graphite&quot;</tt> plugin writes data to <i>Graphite</i>, an open-source metrics storage and graphing project. The plugin connects to <i>Carbon</i>, the data layer of <i>Graphite</i>, via <i></i><font SIZE="-1"><i>TCP</i></font><i></i> or <i></i><font SIZE="-1"><i>UDP</i></font><i></i> and sends data via the &#8220;line based&#8221; protocol (per default using port 2003). The data will be sent in blocks of at most 1428 bytes to minimize the number of network packets. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin write_graphite&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;2003&quot;
 Protocol &quot;tcp&quot;
 LogSendErrors true
 Prefix &quot;collectd&quot;
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration consists of one or more &lt;<code>Node</code>&nbsp;<wbr><i>Name</i>&gt; blocks. Inside the <code>Node</code> blocks, the following options are recognized:</p>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>2003</tt>.</p>
<dt><code>Protocol</code> <i>String</i></p>
<dd>Protocol to use when connecting to <i>Graphite</i>. Defaults to <tt>&quot;tcp&quot;</tt>.</p>
<dt><code>ReconnectInterval</code> <i>Seconds</i></p>
<dd>When set to non-zero, forces the connection to the Graphite backend to be closed and re-opend periodically. This behavior is desirable in environments where the connection to the Graphite backend is done through load balancers, for example. When set to zero, the default, the connetion is kept open for as long as possible.</p>
<dt><code>LogSendErrors</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code> (the default), logs errors when sending data to <i>Graphite</i>. If set to <code>false</code>, it will not log the errors. This is especially useful when using Protocol <font SIZE="-1">UDP</font> since many times we want to use the &#8220;fire-and-forget&#8221; approach and logging errors fills syslog with unneeded messages.</p>
<dt><code>Prefix</code> <i>String</i></p>
<dd>When set, <i>String</i> is added in front of the host name. Dots and whitespace are <i>not</i> escaped in this string (see <code>EscapeCharacter</code> below).</p>
<dt><code>Postfix</code> <i>String</i></p>
<dd>When set, <i>String</i> is appended to the host name. Dots and whitespace are <i>not</i> escaped in this string (see <code>EscapeCharacter</code> below).</p>
<dt><code>EscapeCharacter</code> <i>Char</i></p>
<dd><i>Carbon</i> uses the dot (<tt>&quot;.&quot;</tt>) as escape character and doesn&#8217;t allow whitespace in the identifier. The <code>EscapeCharacter</code> option determines which character dots, whitespace and control characters are replaced with. Defaults to underscore (<tt>&quot;_&quot;</tt>).</p>
<dt><code>StoreRates</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i. e. as an increasing integer number.</p>
<dt><code>SeparateInstances</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, the plugin instance and type instance will be in their own path component, for example <tt>&quot;host.cpu.0.cpu.idle&quot;</tt>. If set to <code>false</code> (the default), the plugin and plugin instance (and likewise the type and type instance) are put into one component, for example <tt>&quot;host.cpu-0.cpu-idle&quot;</tt>.</p>
<dt><code>AlwaysAppendDS</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;metric&#8221; identifier. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></p>
<dt><code>PreserveSeparator</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>false</code> (the default) the <tt>&quot;.&quot;</tt> (dot) character is replaced with <i>EscapeCharacter</i>. Otherwise, if set to <code>true</code>, the <tt>&quot;.&quot;</tt> (dot) character is preserved, i.e. passed through.</p>
<dt><code>DropDuplicateFields</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, detect and remove duplicate components in Graphite metric names. For example, the metric name <tt>&quot;host.load.load.shortterm&quot;</tt> will be shortened to <tt>&quot;host.load.shortterm&quot;</tt>.</dl>
<h3>Plugin write_log</h3>
<p>The <tt>&quot;write_log&quot;</tt> plugin writes metrics as <font SIZE="-1">INFO</font> log messages. </p>
<p> This plugin supports two output formats: <i>Graphite</i> and <i></i><font SIZE="-1"><i>JSON</i></font><i></i>. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin write_log&gt;
 Format Graphite
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>Format</code> <i>Format</i></p>
<dd>The output format to use. Can be one of <tt>&quot;Graphite&quot;</tt> or <tt>&quot;JSON&quot;</tt>.</dl>
<h3>Plugin write_tsdb</h3>
<p>The <tt>&quot;write_tsdb&quot;</tt> plugin writes data to <i>OpenTSDB</i>, a scalable open-source time series database. The plugin connects to a <i></i><font SIZE="-1"><i>TSD</i></font><i></i>, a masterless, no shared state daemon that ingests metrics and stores them in HBase. The plugin uses <i></i><font SIZE="-1"><i>TCP</i></font><i></i> over the &#8220;line based&#8221; protocol with a default port 4242. The data will be sent in blocks of at most 1428 bytes to minimize the number of network packets. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin write_tsdb&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;tsd-1.my.domain&quot;
 Port &quot;4242&quot;
 HostTags &quot;status=production&quot;
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>The configuration consists of one or more &lt;<code>Node</code>&nbsp;<wbr><i>Name</i>&gt; blocks. Inside the <code>Node</code> blocks, the following options are recognized:</p>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>4242</tt>.</p>
<dt><code>HostTags</code> <i>String</i></p>
<dd>When set, <i>HostTags</i> is added to the end of the metric. It is intended to be used for name=value pairs that the <font SIZE="-1">TSD</font> will tag the metric with. Dots and whitespace are <i>not</i> escaped in this string.</p>
<dt><code>StoreRates</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, convert counter values to rates. If set to <code>false</code> (the default) counter values are stored as is, as an increasing integer number.</p>
<dt><code>AlwaysAppendDS</code> <code>false</code>|<code>true</code></p>
<dd>If set the <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;metric&#8221; identifier. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></dl>
<h3>Plugin write_mongodb</h3>
<p>The <i>write_mongodb plugin</i> will send values to <i>MongoDB</i>, a schema-less NoSQL database. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;write_mongodb&quot;&gt;
 &lt;Node &quot;default&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;27017&quot;
 Timeout 1000
 StoreRates true
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin can send values to multiple instances of <i>MongoDB</i> by specifying one <code>Node</code> block for each instance. Within the <code>Node</code> blocks, the following options are available:</p>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>27017</tt>.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>Set the timeout for each operation on <i>MongoDB</i> to <i>Timeout</i> milliseconds. Setting this option to zero means no timeout, which is the default.</p>
<dt><code>StoreRates</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i.e. as an increasing integer number.</p>
<dt><code>Database</code> <i>Database</i></p>
<dd>
<dt><code>User</code> <i>User</i></p>
<dd>
<dt><code>Password</code> <i>Password</i></p>
<dd>Sets the information used when authenticating to a <i>MongoDB</i> database. The fields are optional (in which case no authentication is attempted), but if you want to use authentication all three fields must be set.</dl>
<h3>Plugin write_prometheus</h3>
<p>The <i>write_prometheus plugin</i> implements a tiny webserver that can be scraped using <i>Prometheus</i>. </p>
<p> <code>Options:</code></p>
<dl>
<dt><code>Port</code> <i>Port</i></p>
<dd>Port the embedded webserver should listen on. Defaults to <code>9103</code>.</p>
<dt><code>StalenessDelta</code> <i>Seconds</i></p>
<dd>Time in seconds after which <i>Prometheus</i> considers a metric &#8220;stale&#8221; if it hasn&#8217;t seen any update for it. This value must match the setting in Prometheus. It defaults to <code>300</code> seconds (5 minutes), same as Prometheus. </p>
<p> <code>Background:</code> </p>
<p> <i>Prometheus</i> has a global setting, <tt>&quot;StalenessDelta&quot;</tt>, which controls after which time a metric without updates is considered &#8220;stale&#8221;. This setting effectively puts an upper limit on the interval in which metrics are reported. </p>
<p> When the <i>write_prometheus plugin</i> encounters a metric with an interval exceeding this limit, it will inform you, the user, and provide the metric to <i>Prometheus</i> <code>without</code> a timestamp. That causes <i>Prometheus</i> to consider the metric &#8220;fresh&#8221; each time it is scraped, with the time of the scrape being considered the time of the update. The result is that there appear more datapoints in <i>Prometheus</i> than were actually created, but at least the metric doesn&#8217;t disappear periodically.</dl>
<h3>Plugin write_http</h3>
<p>This output plugin submits values to an <font SIZE="-1">HTTP</font> server using <font SIZE="-1">POST</font> requests and encoding metrics with <font SIZE="-1">JSON</font> or using the <tt>&quot;PUTVAL&quot;</tt> command described in <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5). </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;write_http&quot;&gt;
 &lt;Node &quot;example&quot;&gt;
 URL &quot;<a rel="nofollow" href="http://example.com/post-collectd">http://example.com/post-collectd</a>&quot;
 User &quot;collectd&quot;
 Password &quot;weCh3ik0&quot;
 Format JSON
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>The plugin can send values to multiple <font SIZE="-1">HTTP</font> servers by specifying one &lt;<code>Node</code>&nbsp;<wbr><i>Name</i>&gt; block for each server. Within each <code>Node</code> block, the following options are available:</p>
<dl>
<dt><font SIZE="-1"><code>URL</code></font> <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<dd><font SIZE="-1">URL</font> to which the values are submitted to. Mandatory.</p>
<dt><code>User</code> <i>Username</i></p>
<dd>Optional user name needed for authentication.</p>
<dt><code>Password</code> <i>Password</i></p>
<dd>Optional password needed for authentication.</p>
<dt><code>VerifyPeer</code> <code>true</code>|<code>false</code></p>
<dd>Enable or disable peer <font SIZE="-1">SSL</font> certificate verification. See &lt;<a rel="nofollow" href="http://curl.haxx.se/docs/sslcerts.html">http://curl.haxx.se/docs/sslcerts.html</a>&gt; for details. Enabled by default.</p>
<dt><code>VerifyHost</code> <code>true|false</code></p>
<dd>Enable or disable peer host name verification. If enabled, the plugin checks if the <tt>&quot;Common Name&quot;</tt> or a <tt>&quot;Subject Alternate Name&quot;</tt> field of the <font SIZE="-1">SSL</font> certificate matches the host name provided by the <font SIZE="-1"><code>URL</code></font> option. If this identity check fails, the connection is aborted. Obviously, only works when connecting to a <font SIZE="-1">SSL</font> enabled server. Enabled by default.</p>
<dt><code>CACert</code> <i>File</i></p>
<dd>File that holds one or more <font SIZE="-1">SSL</font> certificates. If you want to use <font SIZE="-1">HTTPS</font> you will possibly need this option. What <font SIZE="-1">CA</font> certificates come bundled with <tt>&quot;libcurl&quot;</tt> and are checked by default depends on the distribution you use.</p>
<dt><code>CAPath</code> <i>Directory</i></p>
<dd>Directory holding one or more <font SIZE="-1">CA</font> certificate files. You can use this if for some reason all the needed <font SIZE="-1">CA</font> certificates aren&#8217;t in the same file and can&#8217;t be pointed to using the <code>CACert</code> option. Requires <tt>&quot;libcurl&quot;</tt> to be built against OpenSSL.</p>
<dt><code>ClientKey</code> <i>File</i></p>
<dd>File that holds the private key in <font SIZE="-1">PEM</font> format to be used for certificate-based authentication.</p>
<dt><code>ClientCert</code> <i>File</i></p>
<dd>File that holds the <font SIZE="-1">SSL</font> certificate to be used for certificate-based authentication.</p>
<dt><code>ClientKeyPass</code> <i>Password</i></p>
<dd>Password required to load the private key in <code>ClientKey</code>.</p>
<dt><code>Header</code> <i>Header</i></p>
<dd>A <font SIZE="-1">HTTP</font> header to add to the request. Multiple headers are added if this option is specified more than once. Example: </p>
<pre> Header &quot;X-Custom-Header: custom_value&quot;</pre>
<dt><code>SSLVersion</code> <code>SSLv2</code>|<code>SSLv3</code>|<code>TLSv1</code>|<code>TLSv1_0</code>|<code>TLSv1_1</code>|<code>TLSv1_2</code></p>
<dd>Define which <font SIZE="-1">SSL</font> protocol version must be used. By default <tt>&quot;libcurl&quot;</tt> will attempt to figure out the remote <font SIZE="-1">SSL</font> protocol version. See <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></i>(3) for more details.</p>
<dt><code>Format</code> <code>Command</code>|<font SIZE="-1"><code>JSON</code></font>|<font SIZE="-1"><code>KAIROSDB</code></font></p>
<dd>Format of the output to generate. If set to <code>Command</code>, will create output that is understood by the <i>Exec</i> and <i>UnixSock</i> plugins. When set to <font SIZE="-1"><code>JSON</code></font>, will create output in the <i>JavaScript Object Notation</i> (<font SIZE="-1">JSON</font>). When set to <font SIZE="-1">KAIROSDB ,</font> will create output in the KairosDB format. </p>
<p> Defaults to <code>Command</code>.</p>
<dt><code>Metrics</code> <code>true</code>|<code>false</code></p>
<dd>Controls whether <i>metrics</i> are POSTed to this location. Defaults to <code>true</code>.</p>
<dt><code>Notifications</code> <code>false</code>|<code>true</code></p>
<dd>Controls whether <i>notifications</i> are POSTed to this location. Defaults to <code>false</code>.</p>
<dt><code>StoreRates</code> <code>true|false</code></p>
<dd>If set to <code>true</code>, convert counter values to rates. If set to <code>false</code> (the default) counter values are stored as is, i.e. as an increasing integer number.</p>
<dt><code>BufferSize</code> <i>Bytes</i></p>
<dd>Sets the send buffer size to <i>Bytes</i>. By increasing this buffer, less <font SIZE="-1">HTTP</font> requests will be generated, but more metrics will be batched / metrics are cached for longer before being sent, introducing additional delay until they are available on the server side. <i>Bytes</i> must be at least 1024 and cannot exceed the size of an <tt>&quot;int&quot;</tt>, i.e. 2 GByte. Defaults to <tt>4096</tt>.</p>
<dt><code>LowSpeedLimit</code> <i>Bytes per Second</i></p>
<dd>Sets the minimal transfer rate in <i>Bytes per Second</i> below which the connection with the <font SIZE="-1">HTTP</font> server will be considered too slow and aborted. All the data submitted over this connection will probably be lost. Defaults to 0, which means no minimum transfer rate is enforced.</p>
<dt><code>Timeout</code> <i>Timeout</i></p>
<dd>Sets the maximum time in milliseconds given for <font SIZE="-1">HTTP POST</font> operations to complete. When this limit is reached, the <font SIZE="-1">POST</font> operation will be aborted, and all the data in the current send buffer will probably be lost. Defaults to 0, which means the connection never times out.</p>
<dt><code>LogHttpError</code> <code>false</code>|<code>true</code></p>
<dd>Enables printing of <font SIZE="-1">HTTP</font> error code to log. Turned off by default. </p>
<p> The <tt>&quot;write_http&quot;</tt> plugin regularly submits the collected values to the <font SIZE="-1">HTTP</font> server. How frequently this happens depends on how much data you are collecting and the size of <code>BufferSize</code>. The optimal value to set <code>Timeout</code> to is slightly below this interval, which you can estimate by monitoring the network traffic between collectd and the <font SIZE="-1">HTTP</font> server.</dl>
<h3>Plugin write_kafka</h3>
<p>The <i>write_kafka plugin</i> will send values to a <i>Kafka</i> topic, a distributed queue. Synopsis: </p>
<pre> &lt;Plugin &quot;write_kafka&quot;&gt;
 Property &quot;metadata.broker.list&quot; &quot;broker1:9092,broker2:9092&quot;
 &lt;Topic &quot;collectd&quot;&gt;
 Format JSON
 &lt;/Topic&gt;
 &lt;/Plugin&gt;</pre>
<p>The following options are understood by the <i>write_kafka plugin</i>:</p>
<dl>
<dt>&lt;<code>Topic</code> <i>Name</i>&gt;</p>
<dd>The plugin&#8217;s configuration consists of one or more <code>Topic</code> blocks. Each block is given a unique <i>Name</i> and specifies one kafka producer. Inside the <code>Topic</code> block, the following per-topic options are understood:</p>
<dl>
<dd>
<dl>
<dt><code>Property</code> <i>String</i> <i>String</i></p>
<dd>Configure the named property for the current topic. Properties are forwarded to the kafka producer library <code>librdkafka</code>.</p>
<dt><code>Key</code> <i>String</i></p>
<dd>Use the specified string as a partitioning key for the topic. Kafka breaks topic into partitions and guarantees that for a given topology, the same consumer will be used for a specific key. The special (case insensitive) string <code>Random</code> can be used to specify that an arbitrary partition should be used.</p>
<dt><code>Format</code> <code>Command</code>|<font SIZE="-1"><code>JSON</code></font>|<code>Graphite</code></p>
<dd>Selects the format in which messages are sent to the broker. If set to <code>Command</code> (the default), values are sent as <tt>&quot;PUTVAL&quot;</tt> commands which are identical to the syntax used by the <i>Exec</i> and <i>UnixSock plugins</i>. </p>
<p> If set to <font SIZE="-1"><code>JSON</code></font>, the values are encoded in the <i>JavaScript Object Notation</i>, an easy and straight forward exchange format. </p>
<p> If set to <code>Graphite</code>, values are encoded in the <i>Graphite</i> format, which is <tt>&quot;&lt;metric&gt; &lt;value&gt; &lt;timestamp&gt;
&quot;</tt>.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code></p>
<dd>Determines whether or not <tt>&quot;COUNTER&quot;</tt>, <tt>&quot;DERIVE&quot;</tt> and <tt>&quot;ABSOLUTE&quot;</tt> data sources are converted to a <i>rate</i> (i.e. a <tt>&quot;GAUGE&quot;</tt> value). If set to <code>false</code> (the default), no conversion is performed. Otherwise the conversion is performed using the internal value cache. </p>
<p> Please note that currently this option is only used if the <code>Format</code> option has been set to <font SIZE="-1"><code>JSON</code></font>.</p>
<dt><code>GraphitePrefix</code> (<code>Format</code>=<i>Graphite</i> only)</p>
<dd>A prefix can be added in the metric name when outputting in the <i>Graphite</i> format. It&#8217;s added before the <i>Host</i> name. Metric name will be <tt>&quot;&lt;prefix&gt;&lt;host&gt;&lt;postfix&gt;&lt;plugin&gt;&lt;type&gt;&lt;name&gt;&quot;</tt></p>
<dt><code>GraphitePostfix</code> (<code>Format</code>=<i>Graphite</i> only)</p>
<dd>A postfix can be added in the metric name when outputting in the <i>Graphite</i> format. It&#8217;s added after the <i>Host</i> name. Metric name will be <tt>&quot;&lt;prefix&gt;&lt;host&gt;&lt;postfix&gt;&lt;plugin&gt;&lt;type&gt;&lt;name&gt;&quot;</tt></p>
<dt><code>GraphiteEscapeChar</code> (<code>Format</code>=<i>Graphite</i> only)</p>
<dd>Specify a character to replace dots (.) in the host part of the metric name. In <i>Graphite</i> metric name, dots are used as separators between different metric parts (host, plugin, type). Default is <tt>&quot;_&quot;</tt> (<i>Underscore</i>).</p>
<dt><code>GraphiteSeparateInstances</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, the plugin instance and type instance will be in their own path component, for example <tt>&quot;host.cpu.0.cpu.idle&quot;</tt>. If set to <code>false</code> (the default), the plugin and plugin instance (and likewise the type and type instance) are put into one component, for example <tt>&quot;host.cpu-0.cpu-idle&quot;</tt>.</p>
<dt><code>GraphiteAlwaysAppendDS</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;metric&#8221; identifier. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></p>
<dt><code>GraphitePreserveSeparator</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>false</code> (the default) the <tt>&quot;.&quot;</tt> (dot) character is replaced with <i>GraphiteEscapeChar</i>. Otherwise, if set to <code>true</code>, the <tt>&quot;.&quot;</tt> (dot) character is preserved, i.e. passed through.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i.e. as an increasing integer number. </p>
<p> This will be reflected in the <tt>&quot;ds_type&quot;</tt> tag: If <code>StoreRates</code> is enabled, converted values will have &#8220;rate&#8221; appended to the data source type, e.g. <tt>&quot;ds_type:derive:rate&quot;</tt>.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Property</code> <i>String</i> <i>String</i></p>
<dd>Configure the kafka producer through properties, you almost always will want to set <code>metadata.broker.list</code> to your Kafka broker list.</dl>
<h3>Plugin write_redis</h3>
<p>The <i>write_redis plugin</i> submits values to <i>Redis</i>, a data structure server. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;write_redis&quot;&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;6379&quot;
 Timeout 1000
 Prefix &quot;collectd/&quot;
 Database 1
 MaxSetSize -1
 StoreRates true
 &lt;/Node&gt;
 &lt;/Plugin&gt;</pre>
<p>Values are submitted to <i>Sorted Sets</i>, using the metric name as the key, and the timestamp as the score. Retrieving a date range can then be done using the <tt>&quot;ZRANGEBYSCORE&quot;</tt> <i>Redis</i> command. Additionally, all the identifiers of these <i>Sorted Sets</i> are kept in a <i>Set</i> called <tt>&quot;collectd/values&quot;</tt> (or <tt>&quot;${prefix}/values&quot;</tt> if the <code>Prefix</code> option was specified) and can be retrieved using the <tt>&quot;SMEMBERS&quot;</tt> <i>Redis</i> command. You can specify the database to use with the <code>Database</code> parameter (default is <tt>0</tt>). See &lt;<a rel="nofollow" href="http://redis.io/commands#sorted_set">http://redis.io/commands#sorted_set</a>&gt; and &lt;<a href="http://redis.io/commands#set">http://redis.io/commands#set</a>&gt; for details. </p>
<p> The information shown in the synopsis above is the <i>default configuration</i> which is used by the plugin if no configuration is present. </p>
<p> The plugin can send values to multiple instances of <i>Redis</i> by specifying one <code>Node</code> block for each instance. Within the <code>Node</code> blocks, the following options are available:</p>
<dl>
<dt><code>Node</code> <i>Nodename</i></p>
<dd>The <code>Node</code> block identifies a new <i>Redis</i> node, that is a new <i>Redis</i> instance running on a specified host and port. The node name is a canonical identifier which is used as <i>plugin instance</i>. It is limited to 51 characters in length.</p>
<dt><code>Host</code> <i>Hostname</i></p>
<dd>The <code>Host</code> option is the hostname or IP-address where the <i>Redis</i> instance is running on.</p>
<dt><code>Port</code> <i>Port</i></p>
<dd>The <code>Port</code> option is the <font SIZE="-1">TCP</font> port on which the Redis instance accepts connections. Either a service name of a port number may be given. Please note that numerical port numbers must be given as a string, too.</p>
<dt><code>Timeout</code> <i>Milliseconds</i></p>
<dd>The <code>Timeout</code> option sets the socket connection timeout, in milliseconds.</p>
<dt><code>Prefix</code> <i>Prefix</i></p>
<dd>Prefix used when constructing the name of the <i>Sorted Sets</i> and the <i>Set</i> containing all metrics. Defaults to <tt>&quot;collectd/&quot;</tt>, so metrics will have names like <tt>&quot;collectd/cpu-0/cpu-user&quot;</tt>. When setting this to something different, it is recommended but not required to include a trailing slash in <i>Prefix</i>.</p>
<dt><code>Database</code> <i>Index</i></p>
<dd>This index selects the redis database to use for writing operations. Defaults to <tt>0</tt>.</p>
<dt><code>MaxSetSize</code> <i>Items</i></p>
<dd>The <code>MaxSetSize</code> option limits the number of items that the <i>Sorted Sets</i> can hold. Negative values for <i>Items</i> sets no limit, which is the default behavior.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i.e. as an increasing integer number.</dl>
<h3>Plugin write_riemann</h3>
<p>The <i>write_riemann plugin</i> will send values to <i>Riemann</i>, a powerful stream aggregation and monitoring system. The plugin sends <i>Protobuf</i> encoded data to <i>Riemann</i> using <font SIZE="-1">UDP</font> packets. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;write_riemann&quot;&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;5555&quot;
 Protocol UDP
 StoreRates true
 AlwaysAppendDS false
 TTLFactor 2.0
 &lt;/Node&gt;
 Tag &quot;foobar&quot;
 Attribute &quot;foo&quot; &quot;bar&quot;
 &lt;/Plugin&gt;</pre>
<p>The following options are understood by the <i>write_riemann plugin</i>:</p>
<dl>
<dt>&lt;<code>Node</code> <i>Name</i>&gt;</p>
<dd>The plugin&#8217;s configuration consists of one or more <code>Node</code> blocks. Each block is given a unique <i>Name</i> and specifies one connection to an instance of <i>Riemann</i>. Indise the <code>Node</code> block, the following per-connection options are understood:</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>5555</tt>.</p>
<dt><code>Protocol</code> <font SIZE="-1"><code>UDP</code></font>|<font SIZE="-1"><code>TCP</code></font>|<font SIZE="-1"><code>TLS</code></font></p>
<dd>Specify the protocol to use when communicating with <i>Riemann</i>. Defaults to <font SIZE="-1"><code>TCP</code></font>.</p>
<dt><code>TLSCertFile</code> <i>Path</i></p>
<dd>When using the <font SIZE="-1"><code>TLS</code></font> protocol, path to a <font SIZE="-1">PEM</font> certificate to present to remote host.</p>
<dt><code>TLSCAFile</code> <i>Path</i></p>
<dd>When using the <font SIZE="-1"><code>TLS</code></font> protocol, path to a <font SIZE="-1">PEM CA</font> certificate to use to validate the remote hosts&#8217;s identity.</p>
<dt><code>TLSKeyFile</code> <i>Path</i></p>
<dd>When using the <font SIZE="-1"><code>TLS</code></font> protocol, path to a <font SIZE="-1">PEM</font> private key associated with the certificate defined by <code>TLSCertFile</code>.</p>
<dt><code>Batch</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> and <code>Protocol</code> is set to <font SIZE="-1"><code>TCP</code></font>, events will be batched in memory and flushed at regular intervals or when <code>BatchMaxSize</code> is exceeded. </p>
<p> Notifications are not batched and sent as soon as possible. </p>
<p> When enabled, it can occur that events get processed by the Riemann server close to or after their expiration time. Tune the <code>TTLFactor</code> and <code>BatchMaxSize</code> settings according to the amount of values collected, if this is an issue. </p>
<p> Defaults to true</p>
<dt><code>BatchMaxSize</code> <i>size</i></p>
<dd>Maximum payload size for a riemann packet. Defaults to 8192</p>
<dt><code>BatchFlushTimeout</code> <i>seconds</i></p>
<dd>Maximum amount of seconds to wait in between to batch flushes. No timeout by default.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i.e. as an increasing integer number. </p>
<p> This will be reflected in the <tt>&quot;ds_type&quot;</tt> tag: If <code>StoreRates</code> is enabled, converted values will have &#8220;rate&#8221; appended to the data source type, e.g. <tt>&quot;ds_type:derive:rate&quot;</tt>.</p>
<dt><code>AlwaysAppendDS</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;service&#8221;, i.e. the field that, together with the &#8220;host&#8221; field, uniquely identifies a metric in <i>Riemann</i>. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></p>
<dt><code>TTLFactor</code> <i>Factor</i></p>
<dd><i>Riemann</i> events have a <i>Time to Live</i> (<font SIZE="-1">TTL</font>) which specifies how long each event is considered active. <i>collectd</i> populates this field based on the metrics interval setting. This setting controls the factor with which the interval is multiplied to set the <font SIZE="-1">TTL.</font> The default value is <code>2.0</code>. Unless you know exactly what you&#8217;re doing, you should only increase this setting from its default value.</p>
<dt><code>Notifications</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, create riemann events for notifications. This is <code>true</code> by default. When processing thresholds from write_riemann, it might prove useful to avoid getting notification events.</p>
<dt><code>CheckThresholds</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, attach state to events based on thresholds defined in the <code>Threshold</code> plugin. Defaults to <code>false</code>.</p>
<dt><code>EventServicePrefix</code> <i>String</i></p>
<dd>Add the given string as a prefix to the event service name. If <code>EventServicePrefix</code> not set or set to an empty string (&quot;&quot;), no prefix will be used.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Tag</code> <i>String</i></p>
<dd>Add the given string as an additional tag to the metric being sent to <i>Riemann</i>.</p>
<dt><code>Attribute</code> <i>String</i> <i>String</i></p>
<dd>Consider the two given strings to be the key and value of an additional attribute for each metric being sent out to <i>Riemann</i>.</dl>
<h3>Plugin write_sensu</h3>
<p>The <i>write_sensu plugin</i> will send values to <i>Sensu</i>, a powerful stream aggregation and monitoring system. The plugin sends <i></i><font SIZE="-1"><i>JSON</i></font><i></i> encoded data to a local <i>Sensu</i> client using a <font SIZE="-1">TCP</font> socket. </p>
<p> At the moment, the <i>write_sensu plugin</i> does not send over a collectd_host parameter so it is not possible to use one collectd instance as a gateway for others. Each collectd host must pair with one <i>Sensu</i> client. </p>
<p> Synopsis: </p>
<pre> &lt;Plugin &quot;write_sensu&quot;&gt;
 &lt;Node &quot;example&quot;&gt;
 Host &quot;localhost&quot;
 Port &quot;3030&quot;
 StoreRates true
 AlwaysAppendDS false
 MetricHandler &quot;influx&quot;
 MetricHandler &quot;default&quot;
 NotificationHandler &quot;flapjack&quot;
 NotificationHandler &quot;howling_monkey&quot;
 Notifications true
 &lt;/Node&gt;
 Tag &quot;foobar&quot;
 Attribute &quot;foo&quot; &quot;bar&quot;
 &lt;/Plugin&gt;</pre>
<p>The following options are understood by the <i>write_sensu plugin</i>:</p>
<dl>
<dt>&lt;<code>Node</code> <i>Name</i>&gt;</p>
<dd>The plugin&#8217;s configuration consists of one or more <code>Node</code> blocks. Each block is given a unique <i>Name</i> and specifies one connection to an instance of <i>Sensu</i>. Inside the <code>Node</code> block, the following per-connection options are understood:</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>3030</tt>.</p>
<dt><code>StoreRates</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> (the default), convert counter values to rates. If set to <code>false</code> counter values are stored as is, i.e. as an increasing integer number. </p>
<p> This will be reflected in the <tt>&quot;collectd_data_source_type&quot;</tt> tag: If <code>StoreRates</code> is enabled, converted values will have &#8220;rate&#8221; appended to the data source type, e.g. <tt>&quot;collectd_data_source_type:derive:rate&quot;</tt>.</p>
<dt><code>AlwaysAppendDS</code> <code>false</code>|<code>true</code></p>
<dd>If set the <code>true</code>, append the name of the <i>Data Source</i> (<font SIZE="-1">DS</font>) to the &#8220;service&#8221;, i.e. the field that, together with the &#8220;host&#8221; field, uniquely identifies a metric in <i>Sensu</i>. If set to <code>false</code> (the default), this is only done when there is more than one <font SIZE="-1">DS.</font></p>
<dt><code>Notifications</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, create <i>Sensu</i> events for notifications. This is <code>false</code> by default. At least one of <code>Notifications</code> or <code>Metrics</code> should be enabled.</p>
<dt><code>Metrics</code> <code>false</code>|<code>true</code></p>
<dd>If set to <code>true</code>, create <i>Sensu</i> events for metrics. This is <code>false</code> by default. At least one of <code>Notifications</code> or <code>Metrics</code> should be enabled.</p>
<dt><code>Separator</code> <i>String</i></p>
<dd>Sets the separator for <i>Sensu</i> metrics name or checks. Defaults to &#8220;/&#8221;.</p>
<dt><code>MetricHandler</code> <i>String</i></p>
<dd>Add a handler that will be set when metrics are sent to <i>Sensu</i>. You can add several of them, one per line. Defaults to no handler.</p>
<dt><code>NotificationHandler</code> <i>String</i></p>
<dd>Add a handler that will be set when notifications are sent to <i>Sensu</i>. You can add several of them, one per line. Defaults to no handler.</p>
<dt><code>EventServicePrefix</code> <i>String</i></p>
<dd>Add the given string as a prefix to the event service name. If <code>EventServicePrefix</code> not set or set to an empty string (&quot;&quot;), no prefix will be used.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>Tag</code> <i>String</i></p>
<dd>Add the given string as an additional tag to the metric being sent to <i>Sensu</i>.</p>
<dt><code>Attribute</code> <i>String</i> <i>String</i></p>
<dd>Consider the two given strings to be the key and value of an additional attribute for each metric being sent out to <i>Sensu</i>.</dl>
<h3>Plugin xencpu</h3>
<p>This plugin collects metrics of hardware <font SIZE="-1">CPU</font> load for machine running Xen hypervisor. Load is calculated from &#8216;idle time&#8217; value, provided by Xen. Result is reported using the <tt>&quot;percent&quot;</tt> type, for each <font SIZE="-1">CPU </font>(core). </p>
<p> This plugin doesn&#8217;t have any options (yet).</p>
<h3>Plugin zookeeper</h3>
<p>The <i>zookeeper plugin</i> will collect statistics from a <i>Zookeeper</i> server using the mntr command. It requires Zookeeper 3.4.0+ and access to the client port. </p>
<p> <code>Synopsis:</code> </p>
<pre> &lt;Plugin &quot;zookeeper&quot;&gt;
 Host &quot;127.0.0.1&quot;
 Port &quot;2181&quot;
 &lt;/Plugin&gt;</pre>
<dl>
<dt><code>Host</code> <i>Address</i></p>
<dd>Hostname or address to connect to. Defaults to <tt>&quot;localhost&quot;</tt>.</p>
<dt><code>Port</code> <i>Service</i></p>
<dd>Service name or port number to connect to. Defaults to <tt>2181</tt>.</dl>
<h2>Threshold Configuration</h2>
<p>Starting with version <tt>4.3.0</tt> collectd has support for <code>monitoring</code>. By that we mean that the values are not only stored or sent somewhere, but that they are judged and, if a problem is recognized, acted upon. The only action collectd takes itself is to generate and dispatch a &#8220;notification&#8221;. Plugins can register to receive notifications and perform appropriate further actions. </p>
<p> Since systems and what you expect them to do differ a lot, you can configure <code>thresholds</code> for your values freely. This gives you a lot of flexibility but also a lot of responsibility. </p>
<p> Every time a value is out of range a notification is dispatched. This means that the idle percentage of your <font SIZE="-1">CPU</font> needs to be less then the configured threshold only once for a notification to be generated. There&#8217;s no such thing as a moving average or similar &#8211; at least not now. </p>
<p> Also, all values that match a threshold are considered to be relevant or &#8220;interesting&#8221;. As a consequence collectd will issue a notification if they are not received for <code>Timeout</code> iterations. The <code>Timeout</code> configuration option is explained in section &#8220;<font SIZE="-1">GLOBAL OPTIONS&#8221;</font>. If, for example, <code>Timeout</code> is set to &#8220;2&#8221; (the default) and some hosts sends it&#8217;s <font SIZE="-1">CPU</font> statistics to the server every 60 seconds, a notification will be dispatched after about 120 seconds. It may take a little longer because the timeout is checked only once each <code>Interval</code> on the server. </p>
<p> When a value comes within range again or is received after it was missing, an &#8220;OKAY-notification&#8221; is dispatched. </p>
<p> Here is a configuration example to get you started. Read below for more information. </p>
<pre> &lt;Plugin threshold&gt;
 &lt;Type &quot;foo&quot;&gt;
 WarningMin 0.00
 WarningMax 1000.00
 FailureMin 0.00
 FailureMax 1200.00
 Invert false
 Instance &quot;bar&quot;
 &lt;/Type&gt;
 &lt;Plugin &quot;interface&quot;&gt;
 Instance &quot;eth0&quot;
 &lt;Type &quot;if_octets&quot;&gt;
 FailureMax 10000000
 DataSource &quot;rx&quot;
 &lt;/Type&gt;
 &lt;/Plugin&gt;
 &lt;Host &quot;hostname&quot;&gt;
 &lt;Type &quot;cpu&quot;&gt;
 Instance &quot;idle&quot;
 FailureMin 10
 &lt;/Type&gt;
 &lt;Plugin &quot;memory&quot;&gt;
 &lt;Type &quot;memory&quot;&gt;
 Instance &quot;cached&quot;
 WarningMin 100000000
 &lt;/Type&gt;
 &lt;/Plugin&gt;
 &lt;/Host&gt;
 &lt;/Plugin&gt;</pre>
<p>There are basically two types of configuration statements: The <tt>&quot;Host&quot;</tt>, <tt>&quot;Plugin&quot;</tt>, and <tt>&quot;Type&quot;</tt> blocks select the value for which a threshold should be configured. The <tt>&quot;Plugin&quot;</tt> and <tt>&quot;Type&quot;</tt> blocks may be specified further using the <tt>&quot;Instance&quot;</tt> option. You can combine the block by nesting the blocks, though they must be nested in the above order, i. e. <tt>&quot;Host&quot;</tt> may contain either <tt>&quot;Plugin&quot;</tt> and <tt>&quot;Type&quot;</tt> blocks, <tt>&quot;Plugin&quot;</tt> may only contain <tt>&quot;Type&quot;</tt> blocks and <tt>&quot;Type&quot;</tt> may not contain other blocks. If multiple blocks apply to the same value the most specific block is used. </p>
<p> The other statements specify the threshold to configure. They <code>must</code> be included in a <tt>&quot;Type&quot;</tt> block. Currently the following statements are recognized:</p>
<dl>
<dt><code>FailureMax</code> <i>Value</i></p>
<dd>
<dt><code>WarningMax</code> <i>Value</i></p>
<dd>Sets the upper bound of acceptable values. If unset defaults to positive infinity. If a value is greater than <code>FailureMax</code> a <font SIZE="-1"><code>FAILURE</code></font> notification will be created. If the value is greater than <code>WarningMax</code> but less than (or equal to) <code>FailureMax</code> a <font SIZE="-1"><code>WARNING</code></font> notification will be created.</p>
<dt><code>FailureMin</code> <i>Value</i></p>
<dd>
<dt><code>WarningMin</code> <i>Value</i></p>
<dd>Sets the lower bound of acceptable values. If unset defaults to negative infinity. If a value is less than <code>FailureMin</code> a <font SIZE="-1"><code>FAILURE</code></font> notification will be created. If the value is less than <code>WarningMin</code> but greater than (or equal to) <code>FailureMin</code> a <font SIZE="-1"><code>WARNING</code></font> notification will be created.</p>
<dt><code>DataSource</code> <i>DSName</i></p>
<dd>Some data sets have more than one &#8220;data source&#8221;. Interesting examples are the <tt>&quot;if_octets&quot;</tt> data set, which has received (<tt>&quot;rx&quot;</tt>) and sent (<tt>&quot;tx&quot;</tt>) bytes and the <tt>&quot;disk_ops&quot;</tt> data set, which holds <tt>&quot;read&quot;</tt> and <tt>&quot;write&quot;</tt> operations. The system load data set, <tt>&quot;load&quot;</tt>, even has three data sources: <tt>&quot;shortterm&quot;</tt>, <tt>&quot;midterm&quot;</tt>, and <tt>&quot;longterm&quot;</tt>. </p>
<p> Normally, all data sources are checked against a configured threshold. If this is undesirable, or if you want to specify different limits for each data source, you can use the <code>DataSource</code> option to have a threshold apply only to one data source.</p>
<dt><code>Invert</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code> the range of acceptable values is inverted, i. e. values between <code>FailureMin</code> and <code>FailureMax</code> (<code>WarningMin</code> and <code>WarningMax</code>) are not okay. Defaults to <code>false</code>.</p>
<dt><code>Persist</code> <code>true</code>|<code>false</code></p>
<dd>Sets how often notifications are generated. If set to <code>true</code> one notification will be generated for each value that is out of the acceptable range. If set to <code>false</code> (the default) then a notification is only generated if a value is out of range but the previous value was okay. </p>
<p> This applies to missing values, too: If set to <code>true</code> a notification about a missing value is generated once every <code>Interval</code> seconds. If set to <code>false</code> only one such notification is generated until the value appears again.</p>
<dt><code>Percentage</code> <code>true</code>|<code>false</code></p>
<dd>If set to <code>true</code>, the minimum and maximum values given are interpreted as percentage value, relative to the other data sources. This is helpful for example for the &#8220;df&#8221; type, where you may want to issue a warning when less than 5&nbsp;<wbr>% of the total space is available. Defaults to <code>false</code>.</p>
<dt><code>Hits</code> <i>Number</i></p>
<dd>Delay creating the notification until the threshold has been passed <i>Number</i> times. When a notification has been generated, or when a subsequent value is inside the threshold, the counter is reset. If, for example, a value is collected once every 10 seconds and <code>Hits</code> is set to 3, a notification will be dispatched at most once every 30 seconds. </p>
<p> This is useful when short bursts are not a problem. If, for example, 100% <font SIZE="-1">CPU</font> usage for up to a minute is normal (and data is collected every 10 seconds), you could set <code>Hits</code> to <code>6</code> to account for this.</p>
<dt><code>Hysteresis</code> <i>Number</i></p>
<dd>When set to non-zero, a hysteresis value is applied when checking minimum and maximum bounds. This is useful for values that increase slowly and fluctuate a bit while doing so. When these values come close to the threshold, they may &#8220;flap&#8221;, i.e. switch between failure / warning case and okay case repeatedly. </p>
<p> If, for example, the threshold is configures as </p>
<pre> WarningMax 100.0
 Hysteresis 1.0</pre>
<p>then a <i>Warning</i> notification is created when the value exceeds <i>101</i> and the corresponding <i>Okay</i> notification is only created once the value falls below <i>99</i>, thus avoiding the &#8220;flapping&#8221;.</dl>
<h2>Filter Configuration</h2>
<p>Starting with collectd 4.6 there is a powerful filtering infrastructure implemented in the daemon. The concept has mostly been copied from <i>ip_tables</i>, the packet filter infrastructure for Linux. We&#8217;ll use a similar terminology, so that users that are familiar with iptables feel right at home.</p>
<h3>Terminology</h3>
<p>The following are the terms used in the remainder of the filter configuration documentation. For an ASCII-art schema of the mechanism, see &#8220;General structure&#8221; below.</p>
<dl>
<dt><code>Match</code></p>
<dd>A <i>match</i> is a criteria to select specific values. Examples are, of course, the name of the value or it&#8217;s current value. </p>
<p> Matches are implemented in plugins which you have to load prior to using the match. The name of such plugins starts with the &#8220;match_&#8221; prefix.</p>
<dt><code>Target</code></p>
<dd>A <i>target</i> is some action that is to be performed with data. Such actions could, for example, be to change part of the value&#8217;s identifier or to ignore the value completely. </p>
<p> Some of these targets are built into the daemon, see &#8220;Built-in targets&#8221; below. Other targets are implemented in plugins which you have to load prior to using the target. The name of such plugins starts with the &#8220;target_&#8221; prefix.</p>
<dt><code>Rule</code></p>
<dd>The combination of any number of matches and at least one target is called a <i>rule</i>. The target actions will be performed for all values for which <code>all</code> matches apply. If the rule does not have any matches associated with it, the target action will be performed for all values.</p>
<dt><code>Chain</code></p>
<dd>A <i>chain</i> is a list of rules and possibly default targets. The rules are tried in order and if one matches, the associated target will be called. If a value is handled by a rule, it depends on the target whether or not any subsequent rules are considered or if traversal of the chain is aborted, see &#8220;Flow control&#8221; below. After all rules have been checked, the default targets will be executed.</dl>
<h3>General structure</h3>
<p>The following shows the resulting structure: </p>
<pre> +---------+
 ! Chain !
 +---------+
 !
 V
 +---------+ +---------+ +---------+ +---------+
 ! Rule !-&gt;! Match !-&gt;! Match !-&gt;! Target !
 +---------+ +---------+ +---------+ +---------+
 !
 V
 +---------+ +---------+ +---------+
 ! Rule !-&gt;! Target !-&gt;! Target !
 +---------+ +---------+ +---------+
 !
 V
 :
 :
 !
 V
 +---------+ +---------+ +---------+
 ! Rule !-&gt;! Match !-&gt;! Target !
 +---------+ +---------+ +---------+
 !
 V
 +---------+
 ! Default !
 ! Target !
 +---------+</pre>
<h3>Flow control</h3>
<p>There are four ways to control which way a value takes through the filter mechanism:</p>
<dl>
<dt><code>jump</code></p>
<dd>The built-in <code>jump</code> target can be used to &#8220;call&#8221; another chain, i. e. process the value with another chain. When the called chain finishes, usually the next target or rule after the jump is executed.</p>
<dt><code>stop</code></p>
<dd>The stop condition, signaled for example by the built-in target <code>stop</code>, causes all processing of the value to be stopped immediately.</p>
<dt><code>return</code></p>
<dd>Causes processing in the current chain to be aborted, but processing of the value generally will continue. This means that if the chain was called via <code>Jump</code>, the next target or rule after the jump will be executed. If the chain was not called by another chain, control will be returned to the daemon and it may pass the value to another chain.</p>
<dt><code>continue</code></p>
<dd>Most targets will signal the <code>continue</code> condition, meaning that processing should continue normally. There is no special built-in target for this condition.</dl>
<h3>Synopsis</h3>
<p>The configuration reflects this structure directly: </p>
<pre> PostCacheChain &quot;PostCache&quot;
 &lt;Chain &quot;PostCache&quot;&gt;
 &lt;Rule &quot;ignore_mysql_show&quot;&gt;
 &lt;Match &quot;regex&quot;&gt;
 Plugin &quot;^mysql$&quot;
 Type &quot;^mysql_command$&quot;
 TypeInstance &quot;^show_&quot;
 &lt;/Match&gt;
 &lt;Target &quot;stop&quot;&gt;
 &lt;/Target&gt;
 &lt;/Rule&gt;
 &lt;Target &quot;write&quot;&gt;
 Plugin &quot;rrdtool&quot;
 &lt;/Target&gt;
 &lt;/Chain&gt;</pre>
<p>The above configuration example will ignore all values where the plugin field is &#8220;mysql&#8221;, the type is &#8220;mysql_command&#8221; and the type instance begins with &#8220;show_&#8221;. All other values will be sent to the <tt>&quot;rrdtool&quot;</tt> write plugin via the default target of the chain. Since this chain is run after the value has been added to the cache, the MySQL <tt>&quot;show_*&quot;</tt> command statistics will be available via the <tt>&quot;unixsock&quot;</tt> plugin.</p>
<h3>List of configuration options</h3>
<dl>
<dt><code>PreCacheChain</code> <i>ChainName</i></p>
<dd>
<dt><code>PostCacheChain</code> <i>ChainName</i></p>
<dd>Configure the name of the &#8220;pre-cache chain&#8221; and the &#8220;post-cache chain&#8221;. The argument is the name of a <i>chain</i> that should be executed before and/or after the values have been added to the cache. </p>
<p> To understand the implications, it&#8217;s important you know what is going on inside <i>collectd</i>. The following diagram shows how values are passed from the read-plugins to the write-plugins: </p>
<pre> +---------------+
 ! Read-Plugin !
 +-------+-------+
 !
 + - - - - V - - - - +
 : +---------------+ :
 : ! Pre-Cache ! :
 : ! Chain ! :
 : +-------+-------+ :
 : ! :
 : V :
 : +-------+-------+ : +---------------+
 : ! Cache !---&gt;! Value Cache !
 : ! insert ! : +---+---+-------+
 : +-------+-------+ : ! !
 : ! ,------------' !
 : V V : V
 : +-------+---+---+ : +-------+-------+
 : ! Post-Cache +---&gt;! Write-Plugins !
 : ! Chain ! : +---------------+
 : +---------------+ :
 : :
 : dispatch values :
 + - - - - - - - - - +</pre>
<p>After the values are passed from the &#8220;read&#8221; plugins to the dispatch functions, the pre-cache chain is run first. The values are added to the internal cache afterwards. The post-cache chain is run after the values have been added to the cache. So why is it such a huge deal if chains are run before or after the values have been added to this cache? </p>
<p> Targets that change the identifier of a value list should be executed before the values are added to the cache, so that the name in the cache matches the name that is used in the &#8220;write&#8221; plugins. The <tt>&quot;unixsock&quot;</tt> plugin, too, uses this cache to receive a list of all available values. If you change the identifier after the value list has been added to the cache, this may easily lead to confusion, but it&#8217;s not forbidden of course. </p>
<p> The cache is also used to convert counter values to rates. These rates are, for example, used by the <tt>&quot;value&quot;</tt> match (see below). If you use the rate stored in the cache <code>before</code> the new value is added, you will use the old, <code>previous</code> rate. Write plugins may use this rate, too, see the <tt>&quot;csv&quot;</tt> plugin, for example. The <tt>&quot;unixsock&quot;</tt> plugin uses these rates too, to implement the <tt>&quot;GETVAL&quot;</tt> command. </p>
<p> Last but not last, the <code>stop</code> target makes a difference: If the pre-cache chain returns the stop condition, the value will not be added to the cache and the post-cache chain will not be run.</p>
<dt><code>Chain</code> <i>Name</i></p>
<dd>Adds a new chain with a certain name. This name can be used to refer to a specific chain, for example to jump to it. </p>
<p> Within the <code>Chain</code> block, there can be <code>Rule</code> blocks and <code>Target</code> blocks.</p>
<dt><code>Rule</code> [<i>Name</i>]</p>
<dd>Adds a new rule to the current chain. The name of the rule is optional and currently has no meaning for the daemon. </p>
<p> Within the <code>Rule</code> block, there may be any number of <code>Match</code> blocks and there must be at least one <code>Target</code> block.</p>
<dt><code>Match</code> <i>Name</i></p>
<dd>Adds a match to a <code>Rule</code> block. The name specifies what kind of match should be performed. Available matches depend on the plugins that have been loaded. </p>
<p> The arguments inside the <code>Match</code> block are passed to the plugin implementing the match, so which arguments are valid here depends on the plugin being used. If you do not need any to pass any arguments to a match, you can use the shorter syntax: </p>
<pre> Match &quot;foobar&quot;</pre>
<p>Which is equivalent to: </p>
<pre> &lt;Match &quot;foobar&quot;&gt;
 &lt;/Match&gt;</pre>
<dt><code>Target</code> <i>Name</i></p>
<dd>Add a target to a rule or a default target to a chain. The name specifies what kind of target is to be added. Which targets are available depends on the plugins being loaded. </p>
<p> The arguments inside the <code>Target</code> block are passed to the plugin implementing the target, so which arguments are valid here depends on the plugin being used. If you do not need any to pass any arguments to a target, you can use the shorter syntax: </p>
<pre> Target &quot;stop&quot;</pre>
<p>This is the same as writing: </p>
<pre> &lt;Target &quot;stop&quot;&gt;
 &lt;/Target&gt;</pre>
</dl>
<h3>Built-in targets</h3>
<p>The following targets are built into the core daemon and therefore need no plugins to be loaded:</p>
<dl>
<dt><code>return</code></p>
<dd>Signals the &#8220;return&#8221; condition, see the &#8220;Flow control&#8221; section above. This causes the current chain to stop processing the value and returns control to the calling chain. The calling chain will continue processing targets and rules just after the <code>jump</code> target (see below). This is very similar to the <font SIZE="-1"><code>RETURN</code></font> target of iptables, see <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8). </p>
<p> This target does not have any options. </p>
<p> Example: </p>
<pre> Target &quot;return&quot;</pre>
<dt><code>stop</code></p>
<dd>Signals the &#8220;stop&#8221; condition, see the &#8220;Flow control&#8221; section above. This causes processing of the value to be aborted immediately. This is similar to the <font SIZE="-1"><code>DROP</code></font> target of iptables, see <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8). </p>
<p> This target does not have any options. </p>
<p> Example: </p>
<pre> Target &quot;stop&quot;</pre>
<dt><code>write</code></p>
<dd>Sends the value to &#8220;write&#8221; plugins. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Plugin</code> <i>Name</i></p>
<dd>Name of the write plugin to which the data should be sent. This option may be given multiple times to send the data to more than one write plugin. If the plugin supports multiple instances, the plugin&#8217;s instance(s) must also be specified.</dl>
</dl>
<dl>
<dd>If no plugin is explicitly specified, the values will be sent to all available write plugins. </p>
<p> Single-instance plugin example: </p>
<pre> &lt;Target &quot;write&quot;&gt;
 Plugin &quot;rrdtool&quot;
 &lt;/Target&gt;</pre>
<p>Multi-instance plugin example: </p>
<pre> &lt;Plugin &quot;write_graphite&quot;&gt;
 &lt;Node &quot;foo&quot;&gt;
 ...
 &lt;/Node&gt;
 &lt;Node &quot;bar&quot;&gt;
 ...
 &lt;/Node&gt;
 &lt;/Plugin&gt;
 ...
 &lt;Target &quot;write&quot;&gt;
 Plugin &quot;write_graphite/foo&quot;
 &lt;/Target&gt;</pre>
</dl>
<dt><code>jump</code></p>
<dd>Starts processing the rules of another chain, see &#8220;Flow control&#8221; above. If the end of that chain is reached, or a stop condition is encountered, processing will continue right after the <code>jump</code> target, i. e. with the next target or the next rule. This is similar to the <code>-j</code> command line option of iptables, see <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8). </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Chain</code> <i>Name</i></p>
<dd>Jumps to the chain <i>Name</i>. This argument is required and may appear only once.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Target &quot;jump&quot;&gt;
 Chain &quot;foobar&quot;
 &lt;/Target&gt;</pre>
</dl>
</dl>
<h3>Available matches</h3>
<dl>
<dt><code>regex</code></p>
<dd>Matches a value using regular expressions. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>Regex</i></p>
<dd>
<dt><code>Plugin</code> <i>Regex</i></p>
<dd>
<dt><code>PluginInstance</code> <i>Regex</i></p>
<dd>
<dt><code>Type</code> <i>Regex</i></p>
<dd>
<dt><code>TypeInstance</code> <i>Regex</i></p>
<dd>
<dt><code>MetaData</code> <i>String</i> <i>Regex</i></p>
<dd>Match values where the given regular expressions match the various fields of the identifier of a value. If multiple regular expressions are given, <code>all</code> regexen must match for a value to match.</p>
<dt><code>Invert</code> <code>false</code>|<code>true</code></p>
<dd>When set to <code>true</code>, the result of the match is inverted, i.e. all value lists where all regular expressions apply are not matched, all other value lists are matched. Defaults to <code>false</code>.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Match &quot;regex&quot;&gt;
 Host &quot;customer[0-9]+&quot;
 Plugin &quot;^foobar$&quot;
 &lt;/Match&gt;</pre>
</dl>
<dt><code>timediff</code></p>
<dd>Matches values that have a time which differs from the time on the server. </p>
<p> This match is mainly intended for servers that receive values over the <tt>&quot;network&quot;</tt> plugin and write them to disk using the <tt>&quot;rrdtool&quot;</tt> plugin. RRDtool is very sensitive to the timestamp used when updating the <font SIZE="-1">RRD</font> files. In particular, the time must be ever increasing. If a misbehaving client sends one packet with a timestamp far in the future, all further packets with a correct time will be ignored because of that one packet. What&#8217;s worse, such corrupted <font SIZE="-1">RRD</font> files are hard to fix. </p>
<p> This match lets one match all values <code>outside</code> a specified time range (relative to the server&#8217;s time), so you can use the <code>stop</code> target (see below) to ignore the value, for example. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Future</code> <i>Seconds</i></p>
<dd>Matches all values that are <i>ahead</i> of the server&#8217;s time by <i>Seconds</i> or more seconds. Set to zero for no limit. Either <code>Future</code> or <code>Past</code> must be non-zero.</p>
<dt><code>Past</code> <i>Seconds</i></p>
<dd>Matches all values that are <i>behind</i> of the server&#8217;s time by <i>Seconds</i> or more seconds. Set to zero for no limit. Either <code>Future</code> or <code>Past</code> must be non-zero.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Match &quot;timediff&quot;&gt;
 Future 300
 Past 3600
 &lt;/Match&gt;</pre>
<p>This example matches all values that are five minutes or more ahead of the server or one hour (or more) lagging behind.</dl>
<dt><code>value</code></p>
<dd>Matches the actual value of data sources against given minimum&nbsp;<wbr>/ maximum values. If a data-set consists of more than one data-source, all data-sources must match the specified ranges for a positive match. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Min</code> <i>Value</i></p>
<dd>Sets the smallest value which still results in a match. If unset, behaves like negative infinity.</p>
<dt><code>Max</code> <i>Value</i></p>
<dd>Sets the largest value which still results in a match. If unset, behaves like positive infinity.</p>
<dt><code>Invert</code> <code>true</code>|<code>false</code></p>
<dd>Inverts the selection. If the <code>Min</code> and <code>Max</code> settings result in a match, no-match is returned and vice versa. Please note that the <code>Invert</code> setting only effects how <code>Min</code> and <code>Max</code> are applied to a specific value. Especially the <code>DataSource</code> and <code>Satisfy</code> settings (see below) are not inverted.</p>
<dt><code>DataSource</code> <i>DSName</i> [<i>DSName</i> &#8230;]</p>
<dd>Select one or more of the data sources. If no data source is configured, all data sources will be checked. If the type handled by the match does not have a data source of the specified name(s), this will always result in no match (independent of the <code>Invert</code> setting).</p>
<dt><code>Satisfy</code> <code>Any</code>|<code>All</code></p>
<dd>Specifies how checking with several data sources is performed. If set to <code>Any</code>, the match succeeds if one of the data sources is in the configured range. If set to <code>All</code> the match only succeeds if all data sources are within the configured range. Default is <code>All</code>. </p>
<p> Usually <code>All</code> is used for positive matches, <code>Any</code> is used for negative matches. This means that with <code>All</code> you usually check that all values are in a &#8220;good&#8221; range, while with <code>Any</code> you check if any value is within a &#8220;bad&#8221; range (or outside the &#8220;good&#8221; range).</dl>
</dl>
<dl>
<dd>Either <code>Min</code> or <code>Max</code>, but not both, may be unset. </p>
<p> Example: </p>
<pre> # Match all values smaller than or equal to 100. Matches only if all data
 # sources are below 100.
 &lt;Match &quot;value&quot;&gt;
 Max 100
 Satisfy &quot;All&quot;
 &lt;/Match&gt;
 # Match if the value of any data source is outside the range of 0 - 100.
 &lt;Match &quot;value&quot;&gt;
 Min 0
 Max 100
 Invert true
 Satisfy &quot;Any&quot;
 &lt;/Match&gt;</pre>
</dl>
<dt><code>empty_counter</code></p>
<dd>Matches all values with one or more data sources of type <font SIZE="-1"><code>COUNTER</code></font> and where all counter values are zero. These counters usually <i>never</i> increased since they started existing (and are therefore uninteresting), or got reset recently or overflowed and you had really, <i>really</i> bad luck. </p>
<p> Please keep in mind that ignoring such counters can result in confusing behavior: Counters which hardly ever increase will be zero for long periods of time. If the counter is reset for some reason (machine or service restarted, usually), the graph will be empty (<font SIZE="-1">NAN</font>) for a long time. People may not understand why.</p>
<dt><code>hashed</code></p>
<dd>Calculates a hash value of the host name and matches values according to that hash value. This makes it possible to divide all hosts into groups and match only values that are in a specific group. The intended use is in load balancing, where you want to handle only part of all data and leave the rest for other servers. </p>
<p> The hashing function used tries to distribute the hosts evenly. First, it calculates a 32 bit hash value using the characters of the hostname: </p>
<pre> hash_value = 0;
 for (i = 0; host[i] != 0; i++)
 hash_value = (hash_value * 251) + host[i];</pre>
<p>The constant 251 is a prime number which is supposed to make this hash value more random. The code then checks the group for this host according to the <i>Total</i> and <i>Match</i> arguments: </p>
<pre> if ((hash_value % Total) == Match)
 matches;
 else
 does not match;</pre>
<p>Please note that when you set <i>Total</i> to two (i. e. you have only two groups), then the least significant bit of the hash value will be the <font SIZE="-1">XOR</font> of all least significant bits in the host name. One consequence is that when you have two hosts, &#8220;server0.example.com&#8221; and &#8220;server1.example.com&#8221;, where the host name differs in one digit only and the digits differ by one, those hosts will never end up in the same group. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Match</code> <i>Match</i> <i>Total</i></p>
<dd>Divide the data into <i>Total</i> groups and match all hosts in group <i>Match</i> as described above. The groups are numbered from zero, i. e. <i>Match</i> must be smaller than <i>Total</i>. <i>Total</i> must be at least one, although only values greater than one really do make any sense. </p>
<p> You can repeat this option to match multiple groups, for example: </p>
<pre> Match 3 7
 Match 5 7</pre>
<p>The above config will divide the data into seven groups and match groups three and five. One use would be to keep every value on two hosts so that if one fails the missing data can later be reconstructed from the second host.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> # Operate on the pre-cache chain, so that ignored values are not even in the
 # global cache.
 &lt;Chain &quot;PreCache&quot;&gt;
 &lt;Rule&gt;
 &lt;Match &quot;hashed&quot;&gt;
 # Divide all received hosts in seven groups and accept all hosts in
 # group three.
 Match 3 7
 &lt;/Match&gt;
 # If matched: Return and continue.
 Target &quot;return&quot;
 &lt;/Rule&gt;
 # If not matched: Return and stop.
 Target &quot;stop&quot;
 &lt;/Chain&gt;</pre>
</dl>
</dl>
<h3>Available targets</h3>
<dl>
<dt><code>notification</code></p>
<dd>Creates and dispatches a notification. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Message</code> <i>String</i></p>
<dd>This required option sets the message of the notification. The following placeholders will be replaced by an appropriate value:</p>
<dl>
<dd>
<dl>
<dt><code>%{host}</code></p>
<dd>
<dt><code>%{plugin}</code></p>
<dd>
<dt><code>%{plugin_instance}</code></p>
<dd>
<dt><code>%{type}</code></p>
<dd>
<dt><code>%{type_instance}</code></p>
<dd>These placeholders are replaced by the identifier field of the same name.</p>
<dt><code>%{ds:</code><i>name</i><code>}</code></p>
<dd>These placeholders are replaced by a (hopefully) human readable representation of the current rate of this data source. If you changed the instance name (using the <code>set</code> or <code>replace</code> targets, see below), it may not be possible to convert counter values to rates.</dl>
</dl>
<dl>
<dd>Please note that these placeholders are <code>case sensitive</code>!</dl>
<dt><code>Severity</code> <code>&quot;</code><font SIZE="-1"><code>FAILURE&quot;</code></font>|<code>&quot;</code><font SIZE="-1"><code>WARNING&quot;</code></font>|<code>&quot;</code><font SIZE="-1"><code>OKAY&quot;</code></font></p>
<dd>Sets the severity of the message. If omitted, the severity <code>&#8220;</code><font SIZE="-1"><code>WARNING&#8221;</code></font> is used.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Target &quot;notification&quot;&gt;
 Message &quot;Oops, the %{type_instance} temperature is currently %{ds:value}!&quot;
 Severity &quot;WARNING&quot;
 &lt;/Target&gt;</pre>
</dl>
<dt><code>replace</code></p>
<dd>Replaces parts of the identifier using regular expressions. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>Regex</i> <i>Replacement</i></p>
<dd>
<dt><code>Plugin</code> <i>Regex</i> <i>Replacement</i></p>
<dd>
<dt><code>PluginInstance</code> <i>Regex</i> <i>Replacement</i></p>
<dd>
<dt><code>TypeInstance</code> <i>Regex</i> <i>Replacement</i></p>
<dd>
<dt><code>MetaData</code> <i>String</i> <i>Regex</i> <i>Replacement</i></p>
<dd>
<dt><code>DeleteMetaData</code> <i>String</i> <i>Regex</i></p>
<dd>Match the appropriate field with the given regular expression <i>Regex</i>. If the regular expression matches, that part that matches is replaced with <i>Replacement</i>. If multiple places of the input buffer match a given regular expression, only the first occurrence will be replaced. </p>
<p> You can specify each option multiple times to use multiple regular expressions one after another.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Target &quot;replace&quot;&gt;
 # Replace &quot;example.net&quot; with &quot;example.com&quot;
 Host &quot;\&lt;example.net\&gt;&quot; &quot;example.com&quot;
 # Strip &quot;www.&quot; from hostnames
 Host &quot;\&lt;www\.&quot; &quot;&quot;
 &lt;/Target&gt;</pre>
</dl>
<dt><code>set</code></p>
<dd>Sets part of the identifier of a value to a given string. </p>
<p> Available options:</p>
<dl>
<dd>
<dl>
<dt><code>Host</code> <i>String</i></p>
<dd>
<dt><code>Plugin</code> <i>String</i></p>
<dd>
<dt><code>PluginInstance</code> <i>String</i></p>
<dd>
<dt><code>TypeInstance</code> <i>String</i></p>
<dd>
<dt><code>MetaData</code> <i>String</i> <i>String</i></p>
<dd>Set the appropriate field to the given string. The strings for plugin instance, type instance, and meta data may be empty, the strings for host and plugin may not be empty. It&#8217;s currently not possible to set the type of a value this way. </p>
<p> The following placeholders will be replaced by an appropriate value:</p>
<dl>
<dd>
<dl>
<dt><code>%{host}</code></p>
<dd>
<dt><code>%{plugin}</code></p>
<dd>
<dt><code>%{plugin_instance}</code></p>
<dd>
<dt><code>%{type}</code></p>
<dd>
<dt><code>%{type_instance}</code></p>
<dd>These placeholders are replaced by the identifier field of the same name.</p>
<dt><code>%{meta:</code><i>name</i><code>}</code></p>
<dd>These placeholders are replaced by the meta data value with the given name.</dl>
</dl>
<dl>
<dd>Please note that these placeholders are <code>case sensitive</code>!</dl>
<dt><code>DeleteMetaData</code> <i>String</i></p>
<dd>Delete the named meta data field.</dl>
</dl>
<dl>
<dd>Example: </p>
<pre> &lt;Target &quot;set&quot;&gt;
 PluginInstance &quot;coretemp&quot;
 TypeInstance &quot;core3&quot;
 &lt;/Target&gt;</pre>
</dl>
</dl>
<h3>Backwards compatibility</h3>
<p>If you use collectd with an old configuration, i. e. one without a <code>Chain</code> block, it will behave as it used to. This is equivalent to the following configuration: </p>
<pre> &lt;Chain &quot;PostCache&quot;&gt;
 Target &quot;write&quot;
 &lt;/Chain&gt;</pre>
<p>If you specify a <code>PostCacheChain</code>, the <code>write</code> target will not be added anywhere and you will have to make sure that it is called where appropriate. We suggest to add the above snippet as default target to your &#8220;PostCache&#8221; chain.</p>
<h3>Examples</h3>
<p>Ignore all values, where the hostname does not contain a dot, i. e. can&#8217;t be an <font SIZE="-1">FQDN.</font> </p>
<pre> &lt;Chain &quot;PreCache&quot;&gt;
 &lt;Rule &quot;no_fqdn&quot;&gt;
 &lt;Match &quot;regex&quot;&gt;
 Host &quot;^[^\.]*$&quot;
 &lt;/Match&gt;
 Target &quot;stop&quot;
 &lt;/Rule&gt;
 Target &quot;write&quot;
 &lt;/Chain&gt;</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5), <i><a href="/docs/linux/man/8-hddtemp/">hddtemp</a></i>(8), <i><a href="/docs/linux/man/8-iptables/">iptables</a></i>(8), kstat(3KSTAT), <i><a href="/docs/linux/man/1-mbmon/">mbmon</a></i>(1), <i><a href="/docs/linux/man/1-psql/">psql</a></i>(1), <i><a href="/docs/linux/man/7-regex/">regex</a></i>(7), <i><a href="/docs/linux/man/1-rrdtool/">rrdtool</a></i>(1), <i><a href="/docs/linux/man/1-sensors/">sensors</a></i>(1)</p>
<h2>Author</h2>
<p>Florian Forster &lt;octo [at] collectd.org&gt;</p>
