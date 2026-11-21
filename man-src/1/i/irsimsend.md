---

title: "irsimsend(1)"
name: "irsimsend"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irsimsend/"
description: "irsimsend- send simulated IR data."
---

<h2>NAME</h2>
<p> irsimsend- send simulated IR data.</p>
<p> <code>irsimsend [-v|-h|-c &lt;count&gt;|-U plugindir] irsimsend &lt;configfile&gt;</code> </p>
<p> irsimsend is a simple test tool which given a configuration file will send all keys defined in that file or the keys listed in another file. The program uses the file driver to log all sent data (pulses/spaces durations) into a file &#8216;simsend.out&#8217;. The symbols sent are printed on stdout. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c, &#8211;count &lt;count&gt;</code></dt>
<dd> Repeat each sent signal &lt;count&gt; times. </dd>
<dt><code>-U, &#8211;plugindir &lt;path&gt;</code></dt>
<dd> Load drivers from &lt;path&gt;, a &#8216;:&#8217; separated search path similar to $PATH. </dd>
<dt><code>-l,&#8211;listfile &lt;path&gt;</code></dt>
<dd> Send symbols listed in file instead of just the symbols in the config file. The file could either be listing a single key symbol per line, or have a complete code string like <i>000000000000a123 01 KEY_POWER brand</i> on each line. </dd>
<dt><code>-v , &#8211;version</code></dt>
<dd> Print version and exit. </dd>
<dt><code>-h , &#8211;help</code></dt>
<dd> Print help message.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.cache/irsimsend.log</code></dt>
<dd> Debug output. Setting the XDG_CACHE_HOME environment variable relocates this file to $XDG_CACHE_HOME/irsimsend.log </dd>
</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
