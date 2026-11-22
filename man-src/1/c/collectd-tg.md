---

title: "collectd-tg(1)"
name: "collectd-tg"
section: "1"
letter: "c"
url: "/docs/linux/man/1-collectd-tg/"
description: "collectd-tg – Traffic generator for collectd."
---

<p> collectd-tg &#8211; Traffic generator for collectd. </p>
<h2>SYNOPSIS</h2>
<p> collectd-tg <code>-n</code> <i>num_vl</i> <code>-H</code> <i>num_hosts</i> <code>-p</code> <i>num_plugins</i> <code>-i</code> <i>interval</i> <code>-d</code> <i>dest</i> <code>-D</code> <i>dport</i></p>
<h2>DESCRIPTION</h2>
<p> <code>collectd-tg</code> generates bogus <i>collectd</i> network traffic. While host, plugin and values are generated randomly, the generated traffic tries to mimic &#8220;real&#8221; traffic as closely as possible.</p>
<h2>ARGUMENTS AND OPTIONS</h2>
<p> The following options are understood by <i>collectd-tg</i>. The order of the arguments generally doesn&#8217;t matter, as long as no argument is passed more than once.</p>
<dl>
<dt><code>-n</code> <i>num_vl</i></dt>
<dd> Sets the number of unique <i>value lists</i> (VL) to generate. Defaults to 10000.</dd>
<dt><code>-H</code> <i>num_hosts</i></dt>
<dd> Sets the number of unique hosts to simulate. Defaults to 1000.</dd>
<dt><code>-p</code> <i>num_plugins</i></dt>
<dd> Sets the number of unique plugins to simulate. Defaults to 20.</dd>
<dt><code>-i</code> <i>interval</i></dt>
<dd> Sets the interval in which each <i>value list</i> is dispatched. Defaults to 10.0 seconds.</dd>
<dt><code>-d</code> <i>dest</i></dt>
<dd> Sets the destination to which to send the generated network traffic. Defaults to the IPv6 multicast address, <tt>&quot;ff18::efc0:4a42&quot;</tt>.</dd>
<dt><code>-D</code> <i>dport</i></dt>
<dd> Sets the destination port or service to which to send the generated network traffic. Defaults to <i>collectd&#8217;s</i> default port, <tt>25826</tt>.</dd>
<dt><code>-h</code></dt>
<dd> Print usage summary.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> Florian Forster &lt;octo at collectd.org&gt; </p>
