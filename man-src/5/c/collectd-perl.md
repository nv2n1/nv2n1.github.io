---
title: "collectd-perl(5)"
name: "collectd-perl"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-perl/"
description: "collectd-perl – Documentation of collectd’s \"perl plugin\""
---

<p>collectd-perl &#8211; Documentation of collectd&#8217;s &quot;perl plugin&quot;</p>
<h2>Synopsis</h2>
<pre> LoadPlugin perl
 # ...
 &lt;Plugin perl&gt;
 IncludeDir &quot;/path/to/perl/plugins&quot;
 BaseName &quot;Collectd::Plugins&quot;
 EnableDebugger &quot;&quot;
 LoadPlugin &quot;FooBar&quot;
 &lt;Plugin FooBar&gt;
 Foo &quot;Bar&quot;
 &lt;/Plugin&gt;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;perl plugin&quot;</tt> embeds a Perl-interpreter into collectd and provides an interface to collectd&#8217;s plugin system. This makes it possible to write plugins for collectd in Perl. This is a lot more efficient than executing a Perl-script every time you want to read a value with the <tt>&quot;exec plugin&quot;</tt> (see <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5)) and provides a lot more functionality, too.</p>
<h2>Configuration</h2>
<dl>
<dt><code>LoadPlugin</code> <i>Plugin</i></p>
<dd>Loads the Perl plugin <i>Plugin</i>. This does basically the same as <code>use</code> would do in a Perl program. As a side effect, the first occurrence of this option causes the Perl-interpreter to be initialized.</p>
<dt><code>BaseName</code> <i>Name</i></p>
<dd>Prepends <i>Name</i><code>::</code> to all plugin names loaded after this option. This is provided for convenience to keep plugin names short. All Perl-based plugins provided with the <i>collectd</i> distributions reside in the <tt>&quot;Collectd::Plugins&quot;</tt> namespace.</p>
<dt>&lt;<code>Plugin</code> <i>Name</i>&gt; block</p>
<dd>This block may be used to pass on configuration settings to a Perl plugin. The configuration is converted into a config-item data type which is passed to the registered configuration callback. See below for details about the config-item data type and how to register callbacks. </p>
<p> The <i>name</i> identifies the callback. It is used literally and independent of the <code>BaseName</code> setting.</p>
<dt><code>EnableDebugger</code> <i>Package</i>[=<i>option</i>,&#8230;]</p>
<dd>Run collectd under the control of the Perl source debugger. If <i>Package</i> is not the empty string, control is passed to the debugging, profiling, or tracing module installed as Devel::<i>Package</i>. A comma-separated list of options may be specified after the &#8220;=&#8221; character. Please note that you may not leave out the <i>Package</i> option even if you specify <code>&quot;&quot;</code>. This is the same as using the <code>-d:Package</code> command line option. </p>
<p> See perldebug for detailed documentation about debugging Perl. </p>
<p> This option does not prevent collectd from daemonizing, so you should start collectd with the <code>-f</code> command line option. Else you will not be able to use the command line driven interface of the debugger.</p>
<dt><code>IncludeDir</code> <i>Dir</i></p>
<dd>Adds <i>Dir</i> to the @INC array. This is the same as using the <code>-IDir</code> command line option or <code>use lib Dir</code> in the source code. Please note that it only has effect on plugins loaded after this option.</p>
<dt><code>RegisterLegacyFlush</code> <i>true|false</i></p>
<dd>The <tt>&quot;Perl plugin&quot;</tt> used to register one flush callback (called <code>&#8220;perl&#8221;</code>) and call all Perl-based flush handlers when this callback was called. Newer versions of the plugin wrap the Perl flush handlers and register them directly with the daemon <i>in addition</i> to the legacy <code>&#8220;perl&#8221;</code> callback. This allows to call specific Perl flush handlers, but has the downside that flushing <i>all</i> plugins now calls the Perl flush handlers twice (once directly and once via the legacy callback). Unfortunately, removing the <code>&#8220;perl&#8221;</code> callback would break backwards compatibility. </p>
<p> This option allows you to disable the legacy <code>&#8220;perl&#8221;</code> flush callback if you care about the double call and don&#8217;t call the <code>&#8220;perl&#8221;</code> callback in your setup.</dl>
<h2>Writing Your Own Plugins</h2>
<p>Writing your own plugins is quite simple. collectd manages plugins by means of <code>dispatch functions</code> which call the appropriate <code>callback functions</code> registered by the plugins. Any plugin basically consists of the implementation of these callback functions and initializing code which registers the functions with collectd. See the section &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> below for a really basic example. The following types of <code>callback functions</code> are known to collectd (all of them are optional):</p>
<dl>
<dt>configuration functions</p>
<dd>This type of functions is called during configuration if an appropriate <code>Plugin</code> block has been encountered. It is called once for each <code>Plugin</code> block which matches the name of the callback as provided with the <code>plugin_register</code> method &#8211; see below.</p>
<dt>init functions</p>
<dd>This type of functions is called once after loading the module and before any calls to the read and write functions. It should be used to initialize the internal state of the plugin (e. g. open sockets, &#8230;). If the return value evaluates to <code>false</code>, the plugin will be disabled.</p>
<dt>read functions</p>
<dd>This type of function is used to collect the actual data. It is called once per interval (see the <code>Interval</code> configuration option of collectd). Usually it will call <code>plugin_dispatch_values</code> to dispatch the values to collectd which will pass them on to all registered <code>write functions</code>. If the return value evaluates to <code>false</code> the plugin will be skipped for an increasing amount of time until it returns <code>true</code> again.</p>
<dt>write functions</p>
<dd>This type of function is used to write the dispatched values. It is called once for each call to <code>plugin_dispatch_values</code>.</p>
<dt>flush functions</p>
<dd>This type of function is used to flush internal caches of plugins. It is usually triggered by the user only. Any plugin which caches data before writing it to disk should provide this kind of callback function.</p>
<dt>log functions</p>
<dd>This type of function is used to pass messages of plugins or the daemon itself to the user.</p>
<dt>notification function</p>
<dd>This type of function is used to act upon notifications. In general, a notification is a status message that may be associated with a data instance. Usually, a notification is generated by the daemon if a configured threshold has been exceeded (see the section &#8220;<font SIZE="-1">THRESHOLD CONFIGURATION&#8221;</font> in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for more details), but any plugin may dispatch notifications as well.</p>
<dt>shutdown functions</p>
<dd>This type of function is called once before the daemon shuts down. It should be used to clean up the plugin (e.g. close sockets, &#8230;).</dl>
<p> Any function (except log functions) may set the <code>$@</code> variable to describe errors in more detail. The message will be passed on to the user using collectd&#8217;s logging mechanism. </p>
<p> See the documentation of the <code>plugin_register</code> method in the section &#8220;<font SIZE="-1">METHODS&#8221;</font> below for the number and types of arguments passed to each <code>callback function</code>. This section also explains how to register <code>callback functions</code> with collectd. </p>
<p> To enable a plugin, copy it to a place where Perl can find it (i. e. a directory listed in the @INC array) just as any other Perl plugin and add an appropriate <code>LoadPlugin</code> option to the configuration file. After restarting collectd you&#8217;re done.</p>
<h2>Data Types</h2>
<p>The following complex types are used to pass values between the Perl plugin and collectd:</p>
<dl>
<dt>Config-Item</p>
<dd>A config-item is one structure which keeps the information provided in the configuration file. The array of children keeps one entry for each configuration option. Each such entry is another config-item structure, which may nest further if nested blocks are used. </p>
<pre> {
 key =&gt; key,
 values =&gt; [ val1, val2, ... ],
 children =&gt; [ { ... }, { ... }, ... ]
 }</pre>
<dt>Data-Set</p>
<dd>A data-set is a list of one or more data-sources. Each data-source defines a name, type, min- and max-value and the data-set wraps them up into one structure. The general layout looks like this: </p>
<pre> [{
 name =&gt; 'data_source_name',
 type =&gt; DS_TYPE_COUNTER || DS_TYPE_GAUGE || DS_TYPE_DERIVE || DS_TYPE_ABSOLUTE,
 min =&gt; value || undef,
 max =&gt; value || undef
 }, ...]</pre>
<dt>Value-List</p>
<dd>A value-list is one structure which features an array of values and fields to identify the values, i. e. time and host, plugin name and plugin-instance as well as a type and type-instance. Since the &#8220;type&#8221; is not included in the value-list but is passed as an extra argument, the general layout looks like this: </p>
<pre> {
 values =&gt; [123, 0.5],
 time =&gt; time (),
 interval =&gt; plugin_get_interval (),
 host =&gt; $hostname_g,
 plugin =&gt; 'myplugin',
 type =&gt; 'myplugin',
 plugin_instance =&gt; '',
 type_instance =&gt; ''
 }</pre>
<dt>Notification</p>
<dd>A notification is one structure defining the severity, time and message of the status message as well as an identification of a data instance. Also, it includes an optional list of user-defined meta information represented as (name, value) pairs: </p>
<pre> {
 severity =&gt; NOTIF_FAILURE || NOTIF_WARNING || NOTIF_OKAY,
 time =&gt; time (),
 message =&gt; 'status message',
 host =&gt; $hostname_g,
 plugin =&gt; 'myplugin',
 type =&gt; 'mytype',
 plugin_instance =&gt; '',
 type_instance =&gt; '',
 meta =&gt; [ { name =&gt; &lt;name&gt;, value =&gt; &lt;value&gt; }, ... ]
 }</pre>
<dt>Match-Proc</p>
<dd>A match-proc is one structure storing the callbacks of a &#8220;match&#8221; of the filter chain infrastructure. The general layout looks like this: </p>
<pre> {
 create =&gt; 'my_create',
 destroy =&gt; 'my_destroy',
 match =&gt; 'my_match'
 }</pre>
<dt>Target-Proc</p>
<dd>A target-proc is one structure storing the callbacks of a &#8220;target&#8221; of the filter chain infrastructure. The general layout looks like this: </p>
<pre> {
 create =&gt; 'my_create',
 destroy =&gt; 'my_destroy',
 invoke =&gt; 'my_invoke'
 }</pre>
</dl>
<h2>Methods</h2>
<p>The following functions provide the C-interface to Perl-modules. They are exported by the &#8220;:plugin&#8221; export tag (see the section &#8220;<font SIZE="-1">EXPORTS&#8221;</font> below).</p>
<dl>
<dt><code>plugin_register</code> (<i>type</i>, <i>name</i>, <i>data</i>)</p>
<dd>Registers a callback-function or data-set. </p>
<p> <i>type</i> can be one of:</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">TYPE_CONFIG</font></p>
<dd>
<dt><font SIZE="-1">TYPE_INIT</font></p>
<dd>
<dt><font SIZE="-1">TYPE_READ</font></p>
<dd>
<dt><font SIZE="-1">TYPE_WRITE</font></p>
<dd>
<dt><font SIZE="-1">TYPE_FLUSH</font></p>
<dd>
<dt><font SIZE="-1">TYPE_LOG</font></p>
<dd>
<dt><font SIZE="-1">TYPE_NOTIF</font></p>
<dd>
<dt><font SIZE="-1">TYPE_SHUTDOWN</font></p>
<dd>
<dt><font SIZE="-1">TYPE_DATASET</font></p>
<dd></dl>
</dl>
<dl>
<dd><i>name</i> is the name of the callback-function or the type of the data-set, depending on the value of <i>type</i>. (Please note that the type of the data-set is the value passed as <i>name</i> here and has nothing to do with the <i>type</i> argument which simply tells <code>plugin_register</code> what is being registered.) </p>
<p> The last argument, <i>data</i>, is either a function name or an array-reference. If <i>type</i> is <font SIZE="-1"><code>TYPE_DATASET</code></font>, then the <i>data</i> argument must be an array-reference which points to an array of hashes. Each hash describes one data-set. For the exact layout see <code>Data-Set</code> above. Please note that there is a large number of predefined data-sets available in the <code>types.db</code> file which are automatically registered with collectd &#8211; see <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for a description of the format of this file. </p>
<p> <code>Note</code>: Using <code>plugin_register</code> to register a data-set is deprecated. Add the new type to a custom <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) file instead. This functionality might be removed in a future version of collectd. </p>
<p> If the <i>type</i> argument is any of the other types (<font SIZE="-1"><code>TYPE_INIT</code></font>, <font SIZE="-1"><code>TYPE_READ</code></font>, &#8230;) then <i>data</i> is expected to be a function name. If the name is not prefixed with the plugin&#8217;s package name collectd will add it automatically. The interface slightly differs from the C interface (which expects a function pointer instead) because Perl does not support to share references to subroutines between threads. </p>
<p> These functions are called in the various stages of the daemon (see the section &#8220;<font SIZE="-1">WRITING YOUR OWN PLUGINS&#8221;</font> above) and are passed the following arguments:</p>
<dl>
<dt><font SIZE="-1">TYPE_CONFIG</font></p>
<dd>The only argument passed is <i>config-item</i>. See above for the layout of this data type.</p>
<dt><font SIZE="-1">TYPE_INIT</font></p>
<dd>
<dt><font SIZE="-1">TYPE_READ</font></p>
<dd>
<dt><font SIZE="-1">TYPE_SHUTDOWN</font></p>
<dd>No arguments are passed.</p>
<dt><font SIZE="-1">TYPE_WRITE</font></p>
<dd>The arguments passed are <i>type</i>, <i>data-set</i>, and <i>value-list</i>. <i>type</i> is a string. For the layout of <i>data-set</i> and <i>value-list</i> see above.</p>
<dt><font SIZE="-1">TYPE_FLUSH</font></p>
<dd>The arguments passed are <i>timeout</i> and <i>identifier</i>. <i>timeout</i> indicates that only data older than <i>timeout</i> seconds is to be flushed. <i>identifier</i> specifies which values are to be flushed.</p>
<dt><font SIZE="-1">TYPE_LOG</font></p>
<dd>The arguments are <i>log-level</i> and <i>message</i>. The log level is small for important messages and high for less important messages. The least important level is <font SIZE="-1"><code>LOG_DEBUG</code></font>, the most important level is <font SIZE="-1"><code>LOG_ERR</code></font>. In between there are (from least to most important): <font SIZE="-1"><code>LOG_INFO</code></font>, <font SIZE="-1"><code>LOG_NOTICE</code></font>, and <font SIZE="-1"><code>LOG_WARNING</code></font>. <i>message</i> is simply a string <code>without</code> a newline at the end.</p>
<dt><font SIZE="-1">TYPE_NOTIF</font></p>
<dd>The only argument passed is <i>notification</i>. See above for the layout of this data type.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>plugin_unregister</code> (<i>type</i>, <i>plugin</i>)</p>
<dd>Removes a callback or data-set from collectd&#8217;s internal list of functions&nbsp;<wbr>/ datasets.</p>
<dt><code>plugin_dispatch_values</code> (<i>value-list</i>)</p>
<dd>Submits a <i>value-list</i> to the daemon. If the data-set identified by <i>value-list</i>-&gt;{<i>type</i>} is found (and the number of values matches the number of data-sources) then the type, data-set and value-list is passed to all write-callbacks that are registered with the daemon.</p>
<dt><code>plugin_write</code> ([<code>plugins</code> =&gt; <i>&#8230;</i>][, <code>datasets</code> =&gt; <i>&#8230;</i>], <code>valuelists</code> =&gt; <i>&#8230;</i>)</p>
<dd>Calls the write function of the given <i>plugins</i> with the provided <i>data sets</i> and <i>value lists</i>. In contrast to <code>plugin_dispatch_values</code>, it does not update collectd&#8217;s internal cache and bypasses the filter mechanism (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details). If the <code>plugins</code> argument has been omitted, the values will be dispatched to all registered write plugins. If the <code>datasets</code> argument has been omitted, the required data sets are looked up according to the <tt>&quot;type&quot;</tt> member in the appropriate value list. The value of all three arguments may either be a single scalar or a reference to an array. If the <code>datasets</code> argument has been specified, the number of data sets has to equal the number of specified value lists.</p>
<dt><code>plugin_flush</code> ([<code>timeout</code> =&gt; <i>timeout</i>][, <code>plugins</code> =&gt; <i>&#8230;</i>][, <code>identifiers</code> =&gt; <i>&#8230;</i>])</p>
<dd>Flush one or more plugins. <i>timeout</i> and the specified <i>identifiers</i> are passed on to the registered flush-callbacks. If omitted, the timeout defaults to <tt>&quot;-1&quot;</tt>. The identifier defaults to the undefined value. If the <code>plugins</code> argument has been specified, only named plugins will be flushed. The value of the <code>plugins</code> and <code>identifiers</code> arguments may either be a string or a reference to an array of strings.</p>
<dt><code>plugin_dispatch_notification</code> (<i>notification</i>)</p>
<dd>Submits a <i>notification</i> to the daemon which will then pass it to all notification-callbacks that are registered.</p>
<dt><code>plugin_log</code> (<i>log-level</i>, <i>message</i>)</p>
<dd>Submits a <i>message</i> of level <i>log-level</i> to collectd&#8217;s logging mechanism. The message is passed to all log-callbacks that are registered with collectd.</p>
<dt><font SIZE="-1"><code>ERROR</code></font>, <font SIZE="-1"><code>WARNING</code></font>, <font SIZE="-1"><code>NOTICE</code></font>, <font SIZE="-1"><code>INFO</code></font>, <font SIZE="-1"><code>DEBUG</code></font> (<i>message</i>)</p>
<dd>Wrappers around <code>plugin_log</code>, using <font SIZE="-1"><code>LOG_ERR</code></font>, <font SIZE="-1"><code>LOG_WARNING</code></font>, <font SIZE="-1"><code>LOG_NOTICE</code></font>, <font SIZE="-1"><code>LOG_INFO</code></font> and <font SIZE="-1"><code>LOG_DEBUG</code></font> respectively as <i>log-level</i>.</p>
<dt><code>plugin_get_interval</code> ()</p>
<dd>Returns the interval of the current plugin as a floating point number in seconds. This value depends on the interval configured within the <tt>&quot;LoadPlugin perl&quot;</tt> block or the global interval (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details).</dl>
<p> The following function provides the filter chain C-interface to Perl-modules. It is exported by the &#8220;:filter_chain&#8221; export tag (see the section &#8220;<font SIZE="-1">EXPORTS&#8221;</font> below).</p>
<dl>
<dt><code>fc_register</code> (<i>type</i>, <i>name</i>, <i>proc</i>)</p>
<dd>Registers filter chain callbacks with collectd. </p>
<p> <i>type</i> may be any of:</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">FC_MATCH</font></p>
<dd>
<dt><font SIZE="-1">FC_TARGET</font></p>
<dd></dl>
</dl>
<dl>
<dd><i>name</i> is the name of the match or target. By this name, the callbacks are identified in the configuration file when specifying a <code>Match</code> or <code>Target</code> block (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details). </p>
<p> <i>proc</i> is a hash reference. The hash includes up to three callbacks: an optional constructor (<code>create</code>) and destructor (<code>destroy</code>) and a mandatory <code>match</code> or <code>invoke</code> callback. <code>match</code> is called whenever processing an appropriate match, while <code>invoke</code> is called whenever processing an appropriate target (see the section &#8220;<font SIZE="-1">FILTER CONFIGURATION&#8221;</font> in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details). Just like any other callbacks, filter chain callbacks are identified by the function name rather than a function pointer because Perl does not support to share references to subroutines between threads. The following arguments are passed to the callbacks:</p>
<dl>
<dt>create</p>
<dd>The arguments passed are <i>config-item</i> and <i>user-data</i>. See above for the layout of the config-item data-type. <i>user-data</i> is a reference to a scalar value that may be used to store any information specific to this particular instance. The daemon does not care about this information at all. It&#8217;s for the plugin&#8217;s use only.</p>
<dt>destroy</p>
<dd>The only argument passed is <i>user-data</i> which is a reference to the user data initialized in the <code>create</code> callback. This callback may be used to cleanup instance-specific information and settings.</p>
<dt>match, invoke</p>
<dd>The arguments passed are <i>data-set</i>, <i>value-list</i>, <i>meta</i> and <i>user-data</i>. See above for the layout of the data-set and value-list data-types. <i>meta</i> is a pointer to an array of meta information, just like the <code>meta</code> member of the notification data-type (see above). <i>user-data</i> is a reference to the user data initialized in the <code>create</code> callback.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Global Variables</h2>
<dl>
<dt><code>$hostname_g</code></p>
<dd>As the name suggests this variable keeps the hostname of the system collectd is running on. The value might be influenced by the <code>Hostname</code> or <code>FQDNLookup</code> configuration options (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details).</p>
<dt><code>$interval_g</code></p>
<dd>This variable keeps the interval in seconds in which the read functions are queried (see the <code>Interval</code> configuration option). </p>
<p> <code>Note:</code> This variable should no longer be used in favor of <tt>&quot;plugin_get_interval()&quot;</tt> (see above). This function takes any plugin-specific interval settings into account (see the <tt>&quot;Interval&quot;</tt> option of <tt>&quot;LoadPlugin&quot;</tt> in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for details).</dl>
<p> Any changes to these variables will be globally visible in collectd.</p>
<h2>Exports</h2>
<p>By default no symbols are exported. However, the following export tags are available (<code>:all</code> will export all of them):</p>
<dl>
<dt><code>:plugin</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>plugin_register</code> ()</p>
<dd>
<dt><code>plugin_unregister</code> ()</p>
<dd>
<dt><code>plugin_dispatch_values</code> ()</p>
<dd>
<dt><code>plugin_flush</code> ()</p>
<dd>
<dt><code>plugin_flush_one</code> ()</p>
<dd>
<dt><code>plugin_flush_all</code> ()</p>
<dd>
<dt><code>plugin_dispatch_notification</code> ()</p>
<dd>
<dt><code>plugin_log</code> ()</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:types</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>TYPE_CONFIG</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_INIT</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_READ</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_WRITE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_FLUSH</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_SHUTDOWN</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_LOG</code></font></p>
<dd>
<dt><font SIZE="-1"><code>TYPE_DATASET</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:ds_types</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>DS_TYPE_COUNTER</code></font></p>
<dd>
<dt><font SIZE="-1"><code>DS_TYPE_GAUGE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>DS_TYPE_DERIVE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>DS_TYPE_ABSOLUTE</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:log</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>ERROR</code></font> ()</p>
<dd>
<dt><font SIZE="-1"><code>WARNING</code></font> ()</p>
<dd>
<dt><font SIZE="-1"><code>NOTICE</code></font> ()</p>
<dd>
<dt><font SIZE="-1"><code>INFO</code></font> ()</p>
<dd>
<dt><font SIZE="-1"><code>DEBUG</code></font> ()</p>
<dd>
<dt><font SIZE="-1"><code>LOG_ERR</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LOG_WARNING</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LOG_NOTICE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LOG_INFO</code></font></p>
<dd>
<dt><font SIZE="-1"><code>LOG_DEBUG</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:filter_chain</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>fc_register</code></p>
<dd>
<dt><font SIZE="-1"><code>FC_MATCH_NO_MATCH</code></font></p>
<dd>
<dt><font SIZE="-1"><code>FC_MATCH_MATCHES</code></font></p>
<dd>
<dt><font SIZE="-1"><code>FC_TARGET_CONTINUE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>FC_TARGET_STOP</code></font></p>
<dd>
<dt><font SIZE="-1"><code>FC_TARGET_RETURN</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:fc_types</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>FC_MATCH</code></font></p>
<dd>
<dt><font SIZE="-1"><code>FC_TARGET</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:notif</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><font SIZE="-1"><code>NOTIF_FAILURE</code></font></p>
<dd>
<dt><font SIZE="-1"><code>NOTIF_WARNING</code></font></p>
<dd>
<dt><font SIZE="-1"><code>NOTIF_OKAY</code></font></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt><code>:globals</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>$hostname_g</code></p>
<dd>
<dt><code>$interval_g</code></p>
<dd></dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>Examples</h2>
<p>Any Perl plugin will start similar to: </p>
<pre> package Collectd::Plugins::FooBar;
 use strict;
 use warnings;
 use Collectd qw( :all );</pre>
<p>A very simple read function might look like: </p>
<pre><code>sub foobar_read
{
    my $vl = {plugin = &gt; 'foobar', type = &gt; 'gauge'};
    $vl-&gt;{'values'} = [rand(42)];
    plugin_dispatch_values($vl);
    return 1;
}</code></pre>
<p> A very simple write function might look like: sub foobar_write<br />
{<br />
    my($type, $ds, $vl) = @_;<br />
    for (my $i = 0; $i &lt; scalar(@$ds); ++$i) {<br />
        print &quot;$vl-&gt;{&#8216;plugin&#8217;} ($vl-&gt;{&#8216;type&#8217;}): $vl-&gt;{&#8216;values&#8217;}-&gt;[$i]
&quot;;<br />
    }<br />
    return 1;<br />
} A very simple match callback might look like: </p>
<pre><code>sub foobar_match
{
    my($ds, $vl, $meta, $user_data) = @_;
    if (matches($ds, $vl)) {
        return FC_MATCH_MATCHES;
    } else {
        return FC_MATCH_NO_MATCH;
    }
}</code></pre>
<p> To register those functions with collectd: </p>
<pre> plugin_register (TYPE_READ, &quot;foobar&quot;, &quot;foobar_read&quot;);
 plugin_register (TYPE_WRITE, &quot;foobar&quot;, &quot;foobar_write&quot;);
 fc_register (FC_MATCH, &quot;foobar&quot;, &quot;foobar_match&quot;);</pre>
<p>See the section &#8220;<font SIZE="-1">DATA TYPES&#8221;</font> above for a complete documentation of the data types used by the read, write and match functions.</p>
<h2>Notes</h2>
<dl>
<dt>&bull;</p>
<dd>Please feel free to send in new plugins to collectd&#8217;s mailing list at &lt;collectd at collectd.org&gt; for review and, possibly, inclusion in the main distribution. In the latter case, we will take care of keeping the plugin up to date and adapting it to new versions of collectd. </p>
<p> Before submitting your plugin, please take a look at &lt;<a rel="nofollow" href="http://collectd.org/dev-info.shtml">http://collectd.org/dev-info.shtml</a>&gt;.</dl>
<h2>Caveats</h2>
<dl>
<dt>&bull;</p>
<dd>collectd is heavily multi-threaded. Each collectd thread accessing the perl plugin will be mapped to a Perl interpreter thread (see <i><a href="//www.systutorials.com/docs/linux/man/3perl-threads/">threads</a></i>(3perl)). Any such thread will be created and destroyed transparently and on-the-fly. </p>
<p> Hence, any plugin has to be thread-safe if it provides several entry points from collectd (i. e. if it registers more than one callback or if a registered callback may be called more than once in parallel). Please note that no data is shared between threads by default. You have to use the <code>threads::shared</code> module to do so.</p>
<dt>&bull;</p>
<dd>Each function name registered with collectd has to be available before the first thread has been created (i. e. basically at compile time). This basically means that hacks (yes, I really consider this to be a hack) like <tt>&quot;*foo = \&amp;bar; plugin_register (TYPE_READ, &quot;plugin&quot;, &quot;foo&quot;);&quot;</tt> most likely will not work. This is due to the fact that the symbol table is not shared across different threads.</p>
<dt>&bull;</p>
<dd>Each plugin is usually only loaded once and kept in memory for performance reasons. Therefore, <font SIZE="-1">END</font> blocks are only executed once when collectd shuts down. You should not rely on <font SIZE="-1">END</font> blocks anyway &#8211; use <code>shutdown functions</code> instead.</p>
<dt>&bull;</p>
<dd>The perl plugin exports the internal <font SIZE="-1">API</font> of collectd which is considered unstable and subject to change at any time. We try hard to not break backwards compatibility in the Perl <font SIZE="-1">API</font> during the life cycle of one major release. However, this cannot be guaranteed at all times. Watch out for warnings dispatched by the perl plugin after upgrades.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="//www.systutorials.com/docs/linux/man/3perl-threads/">threads</a></i>(3perl), <i><a href="//www.systutorials.com/docs/linux/man/3perl-threads::shared/">threads::shared</a></i>(3perl), <i><a href="/docs/linux/man/1-perldebug/">perldebug</a></i>(1)</p>
<h2>Author</h2>
<p>The <tt>&quot;perl plugin&quot;</tt> has been written by Sebastian Harl &lt;sh at tokkee.org&gt;. </p>
<p> This manpage has been written by Florian Forster &lt;octo at collectd.org&gt; and Sebastian Harl &lt;sh at tokkee.org&gt;.</p>
