---
title: "ccze(1)"
name: "ccze"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccze/"
description: "ccze – A robust log colorizer"
---

<h2>NAME</h2>
<p> ccze &#8211; A robust log colorizer</p>
<h2>SYNOPSIS</h2>
<p> <code>ccze</code> [<i>options</i>] &lt;<i>logfile</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ccze</code> utility, which is a drop-in replacement for <code>colorize</code>, but written in C, to be faster and less resource-hungry. The goal was to be fully backwards compatible, yet superior with respect to speed and features.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-a, &#8211;argument </code><i>PLUGIN=ARGUMENTS</i></p>
<dd> Use this option to pass <i>ARGUMENTS</i> to the specified <i>PLUGIN</i>. The argument list is whitespace separated.</p>
<dt><code>-A, &#8211;raw-ansi</code></p>
<dd> If one wants to enable raw ANSI color sequences instead of using curses, this option does just that.</p>
<dt><code>-c, &#8211;color </code><i>KEY=COLOR</i></p>
<dd> Set the color of the keyword <i>KEY</i> to <i>COLOR</i>, like one would do in one of the configuration files.</p>
<dt><code>-C, &#8211;convert-date</code></p>
<dd> Convert unix timestamp to readable date format (in oops and squid logs, for example).</p>
<dt><code>-F, &#8211;rcfile </code><i>rcfile</i></p>
<dd> Read <i>rcfile</i> as a configuration file upon startup, instead of the default ones.</p>
<dt><code>-h, &#8211;html</code></p>
<dd> Instead of colorising the input onto the console, output it in HTML format instead.</p>
<dt><code>-l, &#8211;list-plugins</code></p>
<dd> List all available (loaded) plugins, along with their type and a short description.</p>
<dt><code>-m, &#8211;mode </code><i>mode</i></p>
<dd> Change the output mode. Available modes are <i>curses</i>, <i>ansi</i> and <i>html</i>.</p>
<dt><code>-o, &#8211;options </code><i>OPTIONS&#8230;</i></p>
<dd> <code>CCZE</code> is able to toggle some of its features with this option. You can toggle the <i>scroll</i>, <i>wordcolor</i>, <i>lookups</i>, and <i>transparent</i> features, or you can fiddle with <i>cssfile</i>. All of these are enabled by default, except <i>cssfile</i>. One can turn them off by prefixing the option with a &quot;no&quot;. </p>
<p> With <i>scroll</i>, one can enable or disable scrolling. If the output is not redirected, it is wise to leave it enabled. </p>
<p> The <i>wordcolor</i> option makes <code>ccze</code> search for different keywords in unparsed input, and color those too. Since it is quite fast, and makes the output look better, it is recommended to leave this enabled. </p>
<p> However, <i>lookups</i> is an option that might be better to disable. When on, <code>ccze</code> will try to look up usernames, service names, and lots of other stuff, which will slow down coloring a great deal. If one is piping a long log through <code>ccze</code>, this option might be turned off to speed up the process. </p>
<p> With the <i>transparent</i> option, one can make CCZE treat black background colors as transparent &#8211; that means, a black background will appear transparent in a similar X terminal. If turned off, it will appear as black. </p>
<p> If <i>cssfile</i> is set, then CCZE will not inline the Cascading Style Sheet information into the outputted HTML, but include a link to the external stylesheet given in this paramater.</p>
<dt><code>-p, &#8211;plugin </code><i>PLUGIN</i></p>
<dd> While the default action is to load all plugins (see the <code>Plugins</code> section below), when this option is present, only the specified plugins will be loaded. If one knows what kind of log will be piped through <code>ccze</code>, using this option may result in a slight speedup.</p>
<dt><code>-r, &#8211;remove-facilty</code></p>
<dd> Syslog-ng puts the facility level before log messages. With this switch, these can be cut off.</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program.</dl>
<h2>PLUGINS</h2>
<p> Different programs have different kind of logs, and every kind of log <code>ccze</code> supports is implemented via a plug-in. They are by default located under <i>/usr/lib64/ccze</i> and <i>$HOME/.ccze</i> (so they can be overridden by the user easily). </p>
<p> At the moment, the following modules are bundled with the official release:</p>
<dl>
<dt><i>apm</i></p>
<dd> For coloring apmd&#8217;s logs.</p>
<dt><i>distcc</i></p>
<dd> For coloring distccd&#8217;s logs. (See <i><a href="/docs/linux/man/1-distccd/">distccd</a></i>(1))</p>
<dt><i>exim</i></p>
<dd> For coloring exim&#8217;s <i>main.log</i>. (See <i><a href="/docs/linux/man/8-exim/">exim</a></i>(8))</p>
<dt><i>fetchmail</i></p>
<dd> For coloring fetchmail&#8217;s log files. (See <i><a href="/docs/linux/man/1-fetchmail/">fetchmail</a></i>(1))</p>
<dt><i>ftpstats</i></p>
<dd> For coloring ftpStats compatible log files, such as Pure-FTPD&#8217;s <i>Stats</i> log format.</p>
<dt><i>httpd</i></p>
<dd> For coloring apache-style <i>access.log</i> and <i>error.log</i> files. (See <i><a href="/docs/linux/man/8-apache/">apache</a></i>(8)) </p>
<p> As a side-effect, all compatible formats, like <i><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a></i>(8)&#8217;s common-log format is also supported by this plugin.</p>
<dt><i>icecast</i></p>
<dd> For coloring <i>icecast/icecast.log</i> and <i>icecast/usage.log</i> files. (See <i><a href="/docs/linux/man/8-icecast/">icecast</a></i>(8))</p>
<dt><i>oops</i></p>
<dd> For coloring <i>oops/oops.log</i> files.</p>
<dt><i>php</i></p>
<dd> For coloring <i>php.log</i> files.</p>
<dt><i>postfix</i></p>
<dd> For coloring postfix logs. (See <i><a href="/docs/linux/man/1-postfix/">postfix</a></i>(1))</p>
<dt><i>procmail</i></p>
<dd> For coloring procmail&#8217;s log file. (See <i><a href="/docs/linux/man/1-procmail/">procmail</a></i>(1))</p>
<dt><i>proftpd</i></p>
<dd> For coloring proftpd&#8217;s <i>access.log</i> and <i>auth.log</i> files. (See <i><a href="/docs/linux/man/8-proftpd/">proftpd</a></i>(8))</p>
<dt><i>squid</i></p>
<dd> For coloring squid&#8217;s <i>access.log</i>, <i>store.log</i> and <i>cache.log</i> files. (See <i><a href="/docs/linux/man/8-squid/">squid</a></i>(8))</p>
<dt><i>sulog</i></p>
<dd> For coloring <i>sulog</i> files. (See <i><a href="/docs/linux/man/1-su/">su</a></i>(1))</p>
<dt><i>super</i></p>
<dd> For coloring <i>super.log</i> files. (See <i><a href="/docs/linux/man/1-super/">super</a></i>(1))</p>
<dt><i>syslog</i></p>
<dd> For coloring generic syslog messages. (See <i><a href="/docs/linux/man/8-syslogd/">syslogd</a></i>(8))</p>
<dt><i>ulogd</i></p>
<dd> For coloring ulogd logs.</p>
<dt><i>vsftpd</i></p>
<dd> For coloring <i>vsftpd.log</i> files. (See <i><a href="/docs/linux/man/8-vsftpd/">vsftpd</a></i>(8))</p>
<dt><i>xferlog</i></p>
<dd> For coloring <i>xferlog</i> files. (See <i><a href="/docs/linux/man/5-xferlog/">xferlog</a></i>(5))</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/colorizerc</i>, <i>$HOME/.colorizerc</i></p>
<dd>
<dl>
<dt>
<dd> These files are the default configuration files for <code>colorize</code>, and are parsed by <code>ccze</code> for the sake of full compatibility.</dl>
<p> <i>/etc/cczerc</i>, <i>$HOME/.cczerc</i></p>
<dl>
<dt>
<dd> This two are the main configuration files, in which one can change the colors used by the program to his liking. See the comments in the beginning of <i>/etc/cczerc</i> for a description on the files&#8217; structure. </p>
<p> If neither of these files exist on your system, consider using the <code>ccze-dump</code> utility in the source tree, which dumps the default color set to standard output.</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-colorize/">colorize</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> ccze was written by Gergely Nagy &lt;algernon [at] bonehunter.rulez.org&gt;, based on colorize by Istvan Karaszi &lt;colorize [at] spam.raszi.hu&gt;. </p>
<h2>Index</h2>
