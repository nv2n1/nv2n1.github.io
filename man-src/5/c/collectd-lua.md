---
title: "collectd-lua(5)"
name: "collectd-lua"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-lua/"
description: "collectd-lua – Documentation of collectd’s \"Lua plugin\""
---

<p>collectd-lua &#8211; Documentation of collectd&#8217;s &quot;Lua plugin&quot;</p>
<h2>Synopsis</h2>
<pre> LoadPlugin lua
 # ...
 &lt;Plugin lua&gt;
 BasePath &quot;/path/to/your/lua/scripts&quot;
 Script &quot;script1.lua&quot;
 Script &quot;script2.lua&quot;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;Lua plugin&quot;</tt> embeds a Lua interpreter into collectd and provides an interface to collectd&#8217;s plugin system. This makes it possible to write plugins for collectd in Lua. This is a lot more efficient than executing a Lua script every time you want to read a value with the <tt>&quot;exec plugin&quot;</tt> (see <i><a href="/docs/linux/man/5-collectd-exec/">collectd-exec</a></i>(5)) and provides a lot more functionality, too. </p>
<p> The minimum required Lua version is <i>5.1</i>.</p>
<h2>Configuration</h2>
<dl>
<dt><code>LoadPlugin</code> <i>Lua</i></p>
<dd>Loads the Lua plugin.</p>
<dt><code>BasePath</code> <i>Name</i></p>
<dd>The directory the <tt>&quot;Lua plugin&quot;</tt> looks in to find script <code>Script</code>. If set, this is also prepended to <code>package.path</code>.</p>
<dt><code>Script</code> <i>Name</i></p>
<dd>The script the <tt>&quot;Lua plugin&quot;</tt> is going to run. If <code>BasePath</code> is not specified, this needs to be an absolute path.</dl>
<h2>Writing Your Own Plugins</h2>
<p>Writing your own plugins is quite simple. collectd manages plugins by means of <code>dispatch functions</code> which call the appropriate <code>callback functions</code> registered by the plugins. Any plugin basically consists of the implementation of these callback functions and initializing code which registers the functions with collectd. See the section &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> below for a really basic example. The following types of <code>callback functions</code> are implemented in the Lua plugin (all of them are optional):</p>
<dl>
<dt>read functions</p>
<dd>These are used to collect the actual data. It is called once per interval (see the <code>Interval</code> configuration option of collectd). Usually it will call <code>collectd.dispatch_values</code> to dispatch the values to collectd which will pass them on to all registered <code>write functions</code>. If this function does not return 0 the plugin will be skipped for an increasing amount of time until it returns normally again.</p>
<dt>write functions</p>
<dd>These are used to write the dispatched values. They are called once for every value that was dispatched by any plugin.</dl>
<h2>Functions</h2>
<p>The following functions are provided to Lua modules:</p>
<dl>
<dt>register_read(callback)</p>
<dd>The callback will be called without arguments. If this callback function does not return 0 the next call will be delayed by an increasing interval.</p>
<dt>register_write</p>
<dd>The callback function will be called with one argument passed, which will be a table of values. If this callback function does not return 0 next call will be delayed by an increasing interval.</p>
<dt>log_error, log_warning, log_notice, log_info, log_debug(<i>message</i>)</p>
<dd>Log a message with the specified severity.</dl>
<h2>Examples</h2>
<dl>
<dd>A very simple read function might look like: </p>
<pre><code>function read()
    collectd.log_info(&quot;read function called&quot;)
        t = {
    host = 'localhost',
    plugin = 'myplugin',
    type = 'counter',
    values = {42},
} collectd.dispatch_values(t) return 0 end</code></pre>
<p> A very simple write function might look like: </p>
<pre><code>function write(vl)
for i = 1, #vl.values do
collectd.log_info(vl.host .. '.' .. vl.plugin .. '.' .. vl.type .. ' ' .. vl.values[i])
end
return 0
end</code></pre>
<p> To register those functions with collectd: </p>
<pre> collectd.register_read(read)
 collectd.register_write(write)</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/1-lua/">lua</a></i>(1),</p>
<h2>Author</h2>
<p>The <tt>&quot;Lua plugin&quot;</tt> has been written by Julien Ammous &lt;j.ammous&lt;nbsp&gt;at gmail.com&gt;, Florian Forster &lt;octo at collectd.org&gt; and Ruben Kerkhof &lt;ruben&lt;nbsp&gt;at rubenkerkhof.com&lt;gt&gt; and </p>
<p> This manpage has been written by Ruben Kerkhof &lt;ruben&lt;nbsp&gt;at rubenkerkhof.com&lt;gt&gt;. It is based on the <i><a href="/docs/linux/man/5-collectd-perl/">collectd-perl</a></i>(5) manual page by Florian Forster &lt;octo at collectd.org&gt; and Sebastian Harl &lt;sh at tokkee.org&gt;.</p>
