---
title: "collectd-python(5)"
name: "collectd-python"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-python/"
description: "collectd-python – Documentation of collectd’s \"python plugin\""
---

<p>collectd-python &#8211; Documentation of collectd&#8217;s &quot;python plugin&quot;</p>
<h2>Synopsis</h2>
<pre> LoadPlugin python
 # ...
 &lt;Plugin python&gt;
 ModulePath &quot;/path/to/your/python/modules&quot;
 LogTraces true
 Interactive false
 Import &quot;spam&quot;
 &lt;Module spam&gt;
 spam &quot;wonderful&quot; &quot;lovely&quot;
 &lt;/Module&gt;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;python plugin&quot;</tt> embeds a Python-interpreter into collectd and provides an interface to collectd&#8217;s plugin system. This makes it possible to write plugins for collectd in Python. This is a lot more efficient than executing a Python-script every time you want to read a value with the <tt>&quot;exec plugin&quot;</tt> (see <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5)) and provides a lot more functionality, too. </p>
<p> The minimum required Python version is <i>2.6</i>.</p>
<h2>Configuration</h2>
<dl>
<dt><code>LoadPlugin</code> <i>Plugin</i></p>
<dd>Loads the Python plugin <i>Plugin</i>.</p>
<dt><code>Encoding</code> <i>Name</i></p>
<dd>The default encoding for Unicode objects you pass to collectd. If you omit this option it will default to <code>ascii</code> on <i>Python 2</i>. On <i>Python 3</i> it will always be <code>utf-8</code>, as this function was removed, so this will be silently ignored. These defaults are hardcoded in Python and will ignore everything else, including your locale.</p>
<dt><code>ModulePath</code> <i>Name</i></p>
<dd>Prepends <i>Name</i> to <code>sys.path</code>. You won&#8217;t be able to import any scripts you wrote unless they are located in one of the directories in this list. Please note that it only has effect on plugins loaded after this option. You can use multiple <code>ModulePath</code> lines to add more than one directory.</p>
<dt><code>LogTraces</code> <i>bool</i></p>
<dd>If a Python script throws an exception it will be logged by collectd with the name of the exception and the message. If you set this option to true it will also log the full stacktrace just like the default output of an interactive Python interpreter. This should probably be set to false most of the time but is very useful for development and debugging of new modules.</p>
<dt><code>Interactive</code> <i>bool</i></p>
<dd>This option will cause the module to launch an interactive Python interpreter that reads from and writes to the terminal. Note that collectd will terminate right after starting up if you try to run it as a daemon while this option is enabled so make sure to start collectd with the <code>-f</code> option. </p>
<p> The <code>collectd</code> module is <i>not</i> imported into the interpreter&#8217;s globals. You have to do it manually. Be sure to read the help text of the module, it can be used as a reference guide during coding. </p>
<p> This interactive session will behave slightly differently from a daemonized collectd script as well as from a normal Python interpreter:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>1.</code> collectd will try to import the <code>readline</code> module to give you a decent way of entering your commands. The daemonized collectd won&#8217;t do that.</p>
<dt>&bull;</p>
<dd><code>2.</code> Python will be handling <i></i><font SIZE="-1"><i>SIGINT</i></font><i></i>. Pressing <i>Ctrl+C</i> will usually cause collectd to shut down. This would be problematic in an interactive session, therefore Python will be handling it in interactive sessions. This allows you to use <i>Ctrl+C</i> to interrupt Python code without killing collectd. This also means you can catch <i>KeyboardInterrupt</i> exceptions which does not work during normal operation. </p>
<p> To quit collectd send <i></i><font SIZE="-1"><i>EOF</i></font><i></i> (press <i>Ctrl+D</i> at the beginning of a new line).</p>
<dt>&bull;</p>
<dd><code>3.</code> collectd handles <i></i><font SIZE="-1"><i>SIGCHLD</i></font><i></i>. This means that Python won&#8217;t be able to determine the return code of spawned processes with <i>system()</i>, <i>popen()</i> and subprocess. This will result in Python not using external programs like less to display help texts. You can override this behavior with the <font SIZE="-1"><code>PAGER</code></font> environment variable, e.g. <i>export PAGER=less</i> before starting collectd. Depending on your version of Python this might or might not result in an <code>OSError</code> exception which can be ignored. </p>
<p> If you really need to spawn new processes from Python you can register an init callback and reset the action for <font SIZE="-1">SIGCHLD</font> to the default behavior. Please note that this <i>will</i> break the exec plugin. Do not even load the exec plugin if you intend to do this! </p>
<p> There is an example script located in <code>contrib/python/getsigchld.py</code> to do this. If you import this from <i>collectd.conf</i> <font SIZE="-1">SIGCHLD</font> will be handled normally and spawning processes from Python will work as intended.</dl>
</dl>
<dl>
<dd></dl>
<dt>&lt;<code>Module</code> <i>Name</i>&gt; block</p>
<dd>This block may be used to pass on configuration settings to a Python module. The configuration is converted into an instance of the <code>Config</code> class which is passed to the registered configuration callback. See below for details about the <code>Config</code> class and how to register callbacks. </p>
<p> The <i>name</i> identifies the callback.</dl>
<h2>Strings</h2>
<p>There are a lot of places where strings are sent from collectd to Python and from Python to collectd. How exactly this works depends on whether byte or unicode strings or Python2 or Python3 are used. </p>
<p> Python2 has <i>str</i>, which is just bytes, and <i>unicode</i>. Python3 has <i>str</i>, which is a unicode object, and <i>bytes</i>. </p>
<p> When passing strings from Python to collectd all of these object are supported in all places, however <i>str</i> should be used if possible. These strings must not contain a <font SIZE="-1">NUL</font> byte. Ignoring this will result in a <i>TypeError</i> exception. If a byte string was used it will be used as is by collectd. If a unicode object was used it will be encoded using the default encoding (see above). If this is not possible Python will raise a <i>UnicodeEncodeError</i> exception. </p>
<p> When passing strings from collectd to Python the behavior depends on the Python version used. Python2 will always receive a <i>str</i> object. Python3 will usually receive a <i>str</i> object as well, however the original string will be decoded to unicode using the default encoding. If this fails because the string is not a valid sequence for this encoding a <i>bytes</i> object will be returned instead.</p>
<h2>Writing Your Own Plugins</h2>
<p>Writing your own plugins is quite simple. collectd manages plugins by means of <code>dispatch functions</code> which call the appropriate <code>callback functions</code> registered by the plugins. Any plugin basically consists of the implementation of these callback functions and initializing code which registers the functions with collectd. See the section &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> below for a really basic example. The following types of <code>callback functions</code> are known to collectd (all of them are optional):</p>
<dl>
<dt>configuration functions</p>
<dd>These are called during configuration if an appropriate <code>Module</code> block has been encountered. It is called once for each <code>Module</code> block which matches the name of the callback as provided with the <code>register_config</code> method &#8211; see below. </p>
<p> Python thread support has not been initialized at this point so do not use any threading functions here!</p>
<dt>init functions</p>
<dd>These are called once after loading the module and before any calls to the read and write functions. It should be used to initialize the internal state of the plugin (e. g. open sockets, &#8230;). This is the earliest point where you may use threads.</p>
<dt>read functions</p>
<dd>These are used to collect the actual data. It is called once per interval (see the <code>Interval</code> configuration option of collectd). Usually it will call <code>plugin_dispatch_values</code> to dispatch the values to collectd which will pass them on to all registered <code>write functions</code>. If this function throws any kind of exception the plugin will be skipped for an increasing amount of time until it returns normally again.</p>
<dt>write functions</p>
<dd>These are used to write the dispatched values. It is called once for every value that was dispatched by any plugin.</p>
<dt>flush functions</p>
<dd>These are used to flush internal caches of plugins. It is usually triggered by the user only. Any plugin which caches data before writing it to disk should provide this kind of callback function.</p>
<dt>log functions</p>
<dd>These are used to pass messages of plugins or the daemon itself to the user.</p>
<dt>notification function</p>
<dd>These are used to act upon notifications. In general, a notification is a status message that may be associated with a data instance. Usually, a notification is generated by the daemon if a configured threshold has been exceeded (see the section &#8220;<font SIZE="-1">THRESHOLD CONFIGURATION&#8221;</font> in <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5) for more details), but any plugin may dispatch notifications as well.</p>
<dt>shutdown functions</p>
<dd>These are called once before the daemon shuts down. It should be used to clean up the plugin (e.g. close sockets, &#8230;).</dl>
<p> Any function (except log functions) may throw an exception in case of errors. The exception will be passed on to the user using collectd&#8217;s logging mechanism. If a log callback throws an exception it will be printed to standard error instead. </p>
<p> See the documentation of the various <code>register_</code> methods in the section &#8220;<font SIZE="-1">FUNCTIONS&#8221;</font> below for the number and types of arguments passed to each <code>callback function</code>. This section also explains how to register <code>callback functions</code> with collectd. </p>
<p> To enable a module, copy it to a place where Python can find it (i. e. a directory listed in <code>sys.path</code>) just as any other Python plugin and add an appropriate <code>Import</code> option to the configuration file. After restarting collectd you&#8217;re done.</p>
<h2>Classes</h2>
<p>The following complex types are used to pass values between the Python plugin and collectd:</p>
<h3>Signed</h3>
<p>The Signed class is just a long. It has all its methods and behaves exactly like any other long object. It is used to indicate if an integer was or should be stored as a signed or unsigned integer object. </p>
<pre> class Signed(long)</pre>
<p>This is a long by another name. Use it in meta data dicts to choose the way it is stored in the meta data.</p>
<h3>Unsigned</h3>
<p>The Unsigned class is just a long. It has all its methods and behaves exactly like any other long object. It is used to indicate if an integer was or should be stored as a signed or unsigned integer object. </p>
<pre> class Unsigned(long)</pre>
<p>This is a long by another name. Use it in meta data dicts to choose the way it is stored in the meta data.</p>
<h3>Config</h3>
<p>The Config class is an object which keeps the information provided in the configuration file. The sequence of children keeps one entry for each configuration option. Each such entry is another Config instance, which may nest further if nested blocks are used. </p>
<pre> class Config(object)</pre>
<p>This represents a piece of collectd&#8217;s config file. It is passed to scripts with config callbacks (see <code>register_config</code>) and is of little use if created somewhere else. </p>
<p> It has no methods beyond the bare minimum and only exists for its data members. </p>
<p> Data descriptors defined here:</p>
<dl>
<dt>parent</p>
<dd>This represents the parent of this node. On the root node of the config tree it will be None.</p>
<dt>key</p>
<dd>This is the keyword of this item, i.e. the first word of any given line in the config file. It will always be a string.</p>
<dt>values</p>
<dd>This is a tuple (which might be empty) of all value, i.e. words following the keyword in any given line in the config file. </p>
<p> Every item in this tuple will be either a string, a float or a boolean, depending on the contents of the configuration file.</p>
<dt>children</p>
<dd>This is a tuple of child nodes. For most nodes this will be empty. If this node represents a block instead of a single line of the config file it will contain all nodes in this block.</dl>
<h3>PluginData</h3>
<p>This should not be used directly but it is the base class for both Values and Notification. It is used to identify the source of a value or notification. </p>
<pre> class PluginData(object)</pre>
<p>This is an internal class that is the base for Values and Notification. It is pretty useless by itself and was therefore not exported to the collectd module. </p>
<p> Data descriptors defined here:</p>
<dl>
<dt>host</p>
<dd>The hostname of the host this value was read from. For dispatching this can be set to an empty string which means the local hostname as defined in collectd.conf.</p>
<dt>plugin</p>
<dd>The name of the plugin that read the data. Setting this member to an empty string will insert &#8220;python&#8221; upon dispatching.</p>
<dt>plugin_instance</p>
<dd>Plugin instance string. May be empty.</p>
<dt>time</p>
<dd>This is the Unix timestamp of the time this value was read. For dispatching values this can be set to zero which means &#8220;now&#8221;. This means the time the value is actually dispatched, not the time it was set to 0.</p>
<dt>type</p>
<dd>The type of this value. This type has to be defined in your <i>types.db</i>. Attempting to set it to any other value will raise a <i>TypeError</i> exception. Assigning a type is mandatory, calling dispatch without doing so will raise a <i>RuntimeError</i> exception.</p>
<dt>type_instance</p>
<dd>Type instance string. May be empty.</dl>
<h3>Values</h3>
<p>A Value is an object which features a sequence of values. It is based on the <i>PluginData</i> type and uses its members to identify the values. </p>
<pre> class Values(PluginData)</pre>
<p>A Values object used for dispatching values to collectd and receiving values from write callbacks. </p>
<p> Method resolution order:</p>
<dl>
<dt>Values</p>
<dd>
<dt>PluginData</p>
<dd>
<dt>object</p>
<dd></dl>
<p> Methods defined here:</p>
<dl>
<dt><code>dispatch</code>([type][, values][, plugin_instance][, type_instance][, plugin][, host][, time][, interval]) -&gt; None.</p>
<dd>Dispatch this instance to the collectd process. The object has members for each of the possible arguments for this method. For a detailed explanation of these parameters see the member of the same same. </p>
<p> If you do not submit a parameter the value saved in its member will be submitted. If you do provide a parameter it will be used instead, without altering the member.</p>
<dt><code>write</code>([destination][, type][, values][, plugin_instance][, type_instance][, plugin][, host][, time][, interval]) -&gt; None.</p>
<dd>Write this instance to a single plugin or all plugins if &#8220;destination&#8221; is omitted. This will bypass the main collectd process and all filtering and caching. Other than that it works similar to &#8220;dispatch&#8221;. In most cases &#8220;dispatch&#8221; should be used instead of &#8220;write&#8221;.</dl>
<p> Data descriptors defined here:</p>
<dl>
<dt>interval</p>
<dd>The interval is the timespan in seconds between two submits for the same data source. This value has to be a positive integer, so you can&#8217;t submit more than one value per second. If this member is set to a non-positive value, the default value as specified in the config file will be used (default: 10). </p>
<p> If you submit values more often than the specified interval, the average will be used. If you submit less values, your graphs will have gaps.</p>
<dt>values</p>
<dd>These are the actual values that get dispatched to collectd. It has to be a sequence (a tuple or list) of numbers. The size of the sequence and the type of its content depend on the type member your <i>types.db</i> file. For more information on this read the <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) manual page. </p>
<p> If the sequence does not have the correct size upon dispatch a <i>RuntimeError</i> exception will be raised. If the content of the sequence is not a number, a <i>TypeError</i> exception will be raised.</p>
<dt>meta</p>
<dd>These are the meta data for this Value object. It has to be a dictionary of numbers, strings or bools. All keys must be strings. <i>int</i> and &lt;long&gt; objects will be dispatched as signed integers unless they are between 2**63 and 2**64-1, which will result in a unsigned integer. You can force one of these storage classes by using the classes <code>collectd.Signed</code> and <code>collectd.Unsigned</code>. A meta object received by a write callback will always contain <code>Signed</code> or <code>Unsigned</code> objects.</dl>
<h3>Notification</h3>
<p>A notification is an object defining the severity and message of the status message as well as an identification of a data instance by means of the members of <i>PluginData</i> on which it is based. </p>
<p> class Notification(PluginData) The Notification class is a wrapper around the collectd notification. It can be used to notify other plugins about bad stuff happening. It works similar to Values but has a severity and a message instead of interval and time. Notifications can be dispatched at any time and can be received with register_notification. </p>
<p> Method resolution order:</p>
<dl>
<dt>Notification</p>
<dd>
<dt>PluginData</p>
<dd>
<dt>object</p>
<dd></dl>
<p> Methods defined here:</p>
<dl>
<dt><code>dispatch</code>([type][, values][, plugin_instance][, type_instance][, plugin][, host][, time][, interval]) -&gt; None. Dispatch a value list.</p>
<dd>Dispatch this instance to the collectd process. The object has members for each of the possible arguments for this method. For a detailed explanation of these parameters see the member of the same same. </p>
<p> If you do not submit a parameter the value saved in its member will be submitted. If you do provide a parameter it will be used instead, without altering the member.</dl>
<p> Data descriptors defined here:</p>
<dl>
<dt>message</p>
<dd>Some kind of description of what&#8217;s going on and why this Notification was generated.</p>
<dt>severity</p>
<dd>The severity of this notification. Assign or compare to <i></i><font SIZE="-1"><i>NOTIF_FAILURE</i></font><i></i>, <i></i><font SIZE="-1"><i>NOTIF_WARNING</i></font><i></i> or <i></i><font SIZE="-1"><i>NOTIF_OKAY</i></font><i></i>.</dl>
<h2>Functions</h2>
<p>The following functions provide the C-interface to Python-modules.</p>
<dl>
<dt><code>register_*</code>(<i>callback</i>[, <i>data</i>][, <i>name</i>]) -&gt; identifier</p>
<dd>There are eight different register functions to get callback for eight different events. With one exception all of them are called as shown above.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><i>callback</i> is a callable object that will be called every time the event is triggered.</p>
<dt>&bull;</p>
<dd><i>data</i> is an optional object that will be passed back to the callback function every time it is called. If you omit this parameter no object is passed back to your callback, not even None.</p>
<dt>&bull;</p>
<dd><i>name</i> is an optional identifier for this callback. The default name is <code>python</code>.<i>module</i>. <i>module</i> is taken from the <code>__module__</code> attribute of your callback function. Every callback needs a unique identifier, so if you want to register the same callback multiple times in the same module you need to specify a name here. Otherwise it&#8217;s safe to ignore this parameter.</p>
<dt>&bull;</p>
<dd><i>identifier</i> is the full identifier assigned to this callback.</dl>
</dl>
<dl>
<dd>These functions are called in the various stages of the daemon (see the section &#8220;<font SIZE="-1">WRITING YOUR OWN PLUGINS&#8221;</font> above) and are passed the following arguments:</p>
<dl>
<dt>register_config</p>
<dd>The only argument passed is a <i>Config</i> object. See above for the layout of this data type. Note that you cannot receive the whole config files this way, only <code>Module</code> blocks inside the Python configuration block. Additionally you will only receive blocks where your callback identifier matches <code>python.</code><i>blockname</i>.</p>
<dt>register_init</p>
<dd>The callback will be called without arguments.</p>
<dt>register_read(callback[, interval][, data][, name]) -&gt; <i>identifier</i></p>
<dd>This function takes an additional parameter: <i>interval</i>. It specifies the time between calls to the callback function. </p>
<p> The callback will be called without arguments.</p>
<dt>register_shutdown</p>
<dd>The callback will be called without arguments.</p>
<dt>register_write</p>
<dd>The callback function will be called with one argument passed, which will be a <i>Values</i> object. For the layout of <i>Values</i> see above. If this callback function throws an exception the next call will be delayed by an increasing interval.</p>
<dt>register_flush</p>
<dd>Like <code>register_config</code> is important for this callback because it determines what flush requests the plugin will receive. </p>
<p> The arguments passed are <i>timeout</i> and <i>identifier</i>. <i>timeout</i> indicates that only data older than <i>timeout</i> seconds is to be flushed. <i>identifier</i> specifies which values are to be flushed.</p>
<dt>register_log</p>
<dd>The arguments are <i>severity</i> and <i>message</i>. The severity is an integer and small for important messages and high for less important messages. The least important level is <font SIZE="-1"><code>LOG_DEBUG</code></font>, the most important level is <font SIZE="-1"><code>LOG_ERR</code></font>. In between there are (from least to most important): <font SIZE="-1"><code>LOG_INFO</code></font>, <font SIZE="-1"><code>LOG_NOTICE</code></font>, and <font SIZE="-1"><code>LOG_WARNING</code></font>. <i>message</i> is simply a string <code>without</code> a newline at the end. </p>
<p> If this callback throws an exception it will <code>not</code> be logged. It will just be printed to <code>sys.stderr</code> which usually means silently ignored.</p>
<dt>register_notification</p>
<dd>The only argument passed is a <i>Notification</i> object. See above for the layout of this data type.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>unregister_*</code>(<i>identifier</i>) -&gt; None</p>
<dd>Removes a callback or data-set from collectd&#8217;s internal list of callback functions. Every <i>register_*</i> function has an <i>unregister_*</i> function. <i>identifier</i> is either the string that was returned by the register function or a callback function. The identifier will be constructed in the same way as for the register functions.</p>
<dt><code>get_dataset</code>(<i>name</i>) -&gt; <i>definition</i></p>
<dd>Returns the definition of a dataset specified by <i>name</i>. <i>definition</i> is a list of tuples, each representing one data source. Each tuple has 4 values:</p>
<dl>
<dd>
<dl>
<dt>name</p>
<dd>A string, the name of the data source.</p>
<dt>type</p>
<dd>A string that is equal to either of the variables <font SIZE="-1"><code>DS_TYPE_COUNTER</code></font>, <font SIZE="-1"><code>DS_TYPE_GAUGE</code></font>, <font SIZE="-1"><code>DS_TYPE_DERIVE</code></font> or <font SIZE="-1"><code>DS_TYPE_ABSOLUTE</code></font>.</p>
<dt>min</p>
<dd>A float or None, the minimum value.</p>
<dt>max</p>
<dd>A float or None, the maximum value.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>flush</code>(<i>plugin[, timeout][, identifier]) &#8211;</i> None</p>
<dd>Flush one or all plugins. <i>timeout</i> and the specified <i>identifiers</i> are passed on to the registered flush-callbacks. If omitted, the timeout defaults to <tt>&quot;-1&quot;</tt>. The identifier defaults to None. If the <code>plugin</code> argument has been specified, only named plugin will be flushed.</p>
<dt><code>error</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>(<i>message</i>)</p>
<dd>Log a message with the specified severity.</dl>
<h2>Examples</h2>
<p>Any Python module will start similar to: </p>
<pre> import collectd</pre>
<p>A very simple read function might look like: </p>
<pre> import random
 def read(data=None):
 vl = collectd.Values(type='gauge')
 vl.plugin='python.spam'
 vl.dispatch(values=[random.random() * 100])</pre>
<p>A very simple write function might look like: </p>
<pre> def write(vl, data=None):
 for i in vl.values:
 print &quot;%s (%s): %f&quot; % (vl.plugin, vl.type, i)</pre>
<p>To register those functions with collectd: </p>
<pre> collectd.register_read(read)
 collectd.register_write(write)</pre>
<p>See the section &#8220;<font SIZE="-1">CLASSES&#8221;</font> above for a complete documentation of the data types used by the read, write and match functions.</p>
<h2>Caveats</h2>
<dl>
<dt>&bull;</p>
<dd>collectd is heavily multi-threaded. Each collectd thread accessing the Python plugin will be mapped to a Python interpreter thread. Any such thread will be created and destroyed transparently and on-the-fly. </p>
<p> Hence, any plugin has to be thread-safe if it provides several entry points from collectd (i. e. if it registers more than one callback or if a registered callback may be called more than once in parallel).</p>
<dt>&bull;</p>
<dd>The Python thread module is initialized just before calling the init callbacks. This means you must not use Python&#8217;s threading module prior to this point. This includes all config and possibly other callback as well.</p>
<dt>&bull;</p>
<dd>The python plugin exports the internal <font SIZE="-1">API</font> of collectd which is considered unstable and subject to change at any time. We try hard to not break backwards compatibility in the Python <font SIZE="-1">API</font> during the life cycle of one major release. However, this cannot be guaranteed at all times. Watch out for warnings dispatched by the python plugin after upgrades.</dl>
<h2>Known Bugs</h2>
<dl>
<dt>&bull;</p>
<dd>Not all aspects of the collectd <font SIZE="-1">API</font> are accessible from Python. This includes but is not limited to filters and data sets.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5), <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5), <i><a href="/docs/linux/man/1-python/">python</a></i>(1),</p>
<h2>Author</h2>
<p>The <tt>&quot;python plugin&quot;</tt> has been written by Sven Trenkel &lt;collectd at semidefinite.de&gt;. </p>
<p> This manpage has been written by Sven Trenkel &lt;collectd at semidefinite.de&gt;. It is based on the <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5) manual page by Florian Forster &lt;octo at collectd.org&gt; and Sebastian Harl &lt;sh at tokkee.org&gt;.</p>
