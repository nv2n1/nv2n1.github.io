---
title: "collectdctl(1)"
name: "collectdctl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectdctl/"
description: "collectdctl – Control interface for collectd"
---

<h2 class="name">NAME</h2>
<p> collectdctl &#8211; Control interface for collectd </p>
<h2>SYNOPSIS</h2>
<p> collectdctl <i>[options]</i> <i>&lt;command&gt;</i> <i>[command options]</i></p>
<h2>DESCRIPTION</h2>
<p> collectdctl provides a control interface for collectd, which may be used to interact with the daemon using the <tt>&quot;unixsock plugin&quot;</tt>.</p>
<h2>OPTIONS</h2>
<p> collectdctl supports the following options:</p>
<dl>
<dt><code>-s</code> <i>socket</i></p>
<dd> Path to the <font SIZE="-1">UNIX</font> socket opened by collectd&#8217;s <tt>&quot;unixsock plugin&quot;</tt>. Default: /var/run/collectd-unixsock</p>
<dt><code>-h</code></p>
<dd> Display usage information and exit.</dl>
<h2>AVAILABLE COMMANDS</h2>
<p> The following commands are supported:</p>
<dl>
<dt><code>getval</code> <i>&lt;identifier&gt;</i></p>
<dd> Query the latest collected value identified by the specified <i>&lt;identifier&gt;</i> (see below). The value-list associated with that data-set is returned as a list of key-value-pairs, each on its own line. Keys and values are separated by the equal sign (<tt>&quot;=&quot;</tt>).</p>
<dt><code>flush</code> [<code>timeout=</code><i>&lt;seconds&gt;</i>] [<code>plugin=</code><i>&lt;name&gt;</i>] [<code>identifier=</code><i>&lt;id&gt;</i>]</p>
<dd> Flush the daemon. This is useful, e. g., to make sure that the latest values have been written to the respective <font SIZE="-1">RRD</font> file before graphing them or copying them to somewhere else. </p>
<p> The following options are supported by the flush command:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>timeout=</code><i>&lt;seconds&gt;</i></p>
<dd> Flush values older than the specified timeout (in seconds) only.</p>
<dt><code>plugin=</code><i>&lt;name&gt;</i></p>
<dd> Flush the specified plugin only. I. e., data cached by the specified plugin is written to disk (or network or whatever), if the plugin supports that operation. </p>
<p> Example: <code>rrdtool</code>.</p>
<dt><code>identifier=</code><i>&lt;id&gt;</i></p>
<dd> If this option is present, only the data specified by the specified identifier (see below) will be flushed. Note that this option is not supported by all plugins (e. g., the <tt>&quot;network&quot;</tt> plugin does not support this).</dl>
</dl>
<dl>
<dt>
<dd>
<p> The <code>plugin</code> and <code>identifier</code> options may be specified more than once. In that case, all combinations of specified plugins and identifiers will be flushed only.</dl>
<dt><code>listval</code></p>
<dd> Returns a list of all values (by their identifier) available to the <tt>&quot;unixsock&quot;</tt> plugin. Each value is printed on its own line. I. e., this command returns a list of valid identifiers that may be used with the other commands.</p>
<dt><code>putval</code> <i>&lt;identifier&gt;</i> [<code>interval=</code><i>&lt;seconds&gt;</i>] <i>&lt;value-list(s)&gt;</i></p>
<dd> Submit one or more values (identified by <i>&lt;identifier&gt;</i>, see below) to the daemon which will then dispatch them to the write plugins. <code>interval</code> specifies the interval (in seconds) used to collect the values following that option. It defaults to the default of the running collectd instance receiving the data. Multiple <i>&lt;value-list(s)&gt;</i> (see below) may be specified. Each of them will be submitted to the daemon. The values have to match the data-set definition specified by the type as given in the identifier (see <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for details).</dl>
<h2>IDENTIFIERS</h2>
<p> An identifier has the following format: </p>
<p> [<i>hostname</i>/]<i>plugin</i>[-<i>plugin_instance</i>]/<i>type</i>[-<i>type_instance</i>] </p>
<p> Examples:<br />
&nbsp;<wbr>somehost/cpu-0/cpu-idle<br />
&nbsp;<wbr>uptime/uptime<br />
&nbsp;<wbr>otherhost/memory/memory-used </p>
<p> Hostname defaults to the local (non-fully qualified) hostname if omitted. No error is returned if the specified identifier does not exist (this is a limitation in the <tt>&quot;libcollectdclient&quot;</tt> library).</p>
<h2>VALUE-LIST</h2>
<p> A value list describes one data-set as handled by collectd. It is a colon (<tt>&quot;:&quot;</tt>) separated list of the time and the values. Each value is either given as an integer if the data-type is a counter, or as a double if the data-type is a gauge value. A literal <tt>&quot;U&quot;</tt> is interpreted as an undefined gauge value. The number of values and the data-types have to match the type specified in the identifier (see <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for details). The time is specified as epoch (i. e., standard <font SIZE="-1">UNIX</font> time) or as a literal <tt>&quot;N&quot;</tt> which will be interpreted as now.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>&quot;collectdctl flush plugin=rrdtool identifier=somehost/cpu-0/cpu-wait&quot;</p>
<dd> Flushes all <font SIZE="-1">CPU</font> wait <font SIZE="-1">RRD</font> values of the first <font SIZE="-1">CPU</font> of the local host. I. e., writes all pending <font SIZE="-1">RRD</font> updates of that data-source to disk.</p>
<dt>&quot;for ident in `collectdctl listval | grep users/users`; do collectdctl getval $ident; done&quot;</p>
<dd> Query the latest number of logged in users on all hosts known to the local collectd instance.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/5-collectd-unixsock/">collectd-unixsock</a></i>(5), <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> collectd has been written by Florian Forster &lt;octo at collectd.org&gt; and many contributors (see `<font SIZE="-1">AUTHORS</font>&#8216;). </p>
<p> collectdctl has been written by HXkon J Dugstad Johnsen &lt;hakon-dugstad.johnsen at telenor.com&gt; and Sebastian Harl &lt;sh at tokkee.org&gt;. </p>
<h2>Index</h2>
