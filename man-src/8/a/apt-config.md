---
title: "apt-config(8)"
name: "apt-config"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apt-config/"
description: "apt-config – APT Configuration Query program"
---

<p>apt-config &#8211; APT Configuration Query program</p>
<h2>Synopsis</h2>
<pre><code>apt-config [--empty] [--format '%f &quot;%v&quot;;%n'] [-o=config_string] [-c=config_file] {shell | dump | {-v | --version} | {-h | --help}}</code></pre>
<h2>Description</h2>
<p><code>apt-config</code></p>
<dd>is an internal program used by various portions of the APT suite to provide consistent configurability. It accesses the main configuration file /etc/apt/apt.conf in a manner that is easy to use for scripted applications. </p>
<p> Unless the <code>-h</code>, or <code>&#8211;help</code> option is given, one of the commands below must be present. </p>
<p> <code>shell</code></p>
<dl>
<dd>shell is used to access the configuration information from a shell script. It is given pairs of arguments, the first being a shell variable and the second the configuration value to query. As output it lists shell assignment commands for each value present. In a shell script it should be used as follows: </p>
<dl>
<dd>
<pre>OPTS=&quot;-f&quot;
RES=`apt-config shell OPTS MyApp::options`
eval $RES</pre>
</dl>
<p> This will set the shell environment variable $OPTS to the value of MyApp::options with a default of <code>-f</code>. </p>
<p> The configuration item may be postfixed with a /[fdbi]. f returns file names, d returns directories, b returns true or false and i returns an integer. Each of the returns is normalized and verified internally.</dl>
<p> <code>dump</code></p>
<dl>
<dd>Just show the contents of the configuration space.</dl>
<h2>Options</h2>
<p>All command line options may be set using the configuration file, the descriptions indicate the configuration option to set. For boolean options you can override the config file by using something like <code>-f-</code>,<code>&#8211;no-f</code>, <code>-f=no</code> or several other variations. </p>
<p> <code>&#8211;empty</code></p>
<dl>
<dd>Include options which have an empty value. This is the default, so use &#8211;no-empty to remove them from the output.</dl>
<p> <code>&#8211;format &#8216;</code><i>%f &quot;%v&quot;;%n</i><code>&#8216;</code></p>
<dl>
<dd>Defines the output of each config option. %t will be replaced with its individual name, %f with its full hierarchical name and %v with its value. Use uppercase letters and special characters in the value will be encoded to ensure that it can e.g. be safely used in a quoted-string as defined by RFC822. Additionally %n will be replaced by a newline, and %N by a tab. A % can be printed by using %%.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show a short usage summary.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show the program version.</dl>
<p> <code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dd>Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <code>APT_CONFIG</code> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information.</dl>
<p> <code>-o</code>, <code>&#8211;option</code></p>
<dl>
<dd>Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o Foo::Bar=bar</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5)</p>
<h2>Diagnostics</h2>
<p><code>apt-config</code> returns zero on normal operation, decimal 100 on error.</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Authors</h2>
<p><code>Jason Gunthorpe</code></p>
<dl>
<dd></dl>
<p> <code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
