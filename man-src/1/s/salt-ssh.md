---
title: "salt-ssh(1)"
name: "salt-ssh"
section: "1"
letter: "s"
url: "/docs/linux/man/1-salt-ssh/"
description: "salt-ssh – salt-ssh Documentation"
---

<h2>NAME</h2>
<p> salt-ssh &#8211; salt-ssh Documentation</p>
<h2>SYNOPSIS</h2>
<pre><code>
salt - ssh '*'[options] sys.doc salt - ssh - E '.*'[options] sys.doc cmd
</code></pre>
<h2>DESCRIPTION</h2>
<p> Salt SSH allows for salt routines to be executed using only SSH for transport</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r, &#8211;raw, &#8211;raw-shell</code></p>
<dd> Execute a raw shell command.</p>
<dt><code>&#8211;priv</code></p>
<dd> Specify the SSH private key file to be used for authentication.</p>
<dt><code>&#8211;roster</code></p>
<dd> Define which roster system to use, this defines if a database backend, scanner, or custom roster system is used. Default is the flat file roster.</p>
<dt><code>&#8211;roster-file</code></p>
<dd> Define an alternative location for the default roster file location. The default roster file is called <code>roster</code> and is found in the same directory as the master config file. </p>
<p> New in version 2014.1.0. </p>
<dt><code>&#8211;refresh, &#8211;refresh-cache</code></p>
<dd> Force a refresh of the master side data cache of the target&#8217;s data. This is needed if a target&#8217;s grains have been changed and the auto refresh timeframe has not been reached.</p>
<dt><code>&#8211;max-procs</code></p>
<dd> Set the number of concurrent minions to communicate with. This value defines how many processes are opened up at a time to manage connections, the more running process the faster communication should be, default is 25.</p>
<dt><code>-i, &#8211;ignore-host-keys</code></p>
<dd> Ignore the ssh host keys which by default are honored and connections would ask for approval.</p>
<dt><code>&#8211;passwd</code></p>
<dd> Set the default password to attempt to use when authenticating.</p>
<dt><code>&#8211;key-deploy</code></p>
<dd> Set this flag to attempt to deploy the authorized ssh key with all minions. This combined with &#8211;passwd can make initial deployment of keys very fast and easy.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version of Salt that is running.</p>
<dt><code>&#8211;versions-report</code></p>
<dd> Show program&#8217;s dependencies and version number, and then exit</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>-c CONFIG_DIR, &#8211;config-dir=CONFIG_dir</code></p>
<dd> The location of the Salt configuration directory. This directory contains the configuration files for Salt master and minions. The default location on most systems is <code>/etc/salt</code>.</dl>
<h3>Target Selection</h3>
<dl>
<dt><code>-E, &#8211;pcre</code></p>
<dd> The target expression will be interpreted as a PCRE regular expression rather than a shell glob.</p>
<dt><code>-L, &#8211;list</code></p>
<dd> The target expression will be interpreted as a comma-delimited list; example: server1.foo.bar,server2.foo.bar,example7.quo.qux</p>
<dt><code>-G, &#8211;grain</code></p>
<dd> The target expression matches values returned by the Salt grains system on the minions. The target expression is in the format of &#8216;&lt;grain value&gt;:&lt;glob expression&gt;&#8217;; example: &#8216;os:Arch*&#8217; </p>
<p> This was changed in version 0.9.8 to accept glob expressions instead of regular expression. To use regular expression matching with grains, use the &#8211;grain-pcre option.</p>
<dt><code>&#8211;grain-pcre</code></p>
<dd> The target expression matches values returned by the Salt grains system on the minions. The target expression is in the format of &#8216;&lt;grain value&gt;:&lt; regular expression&gt;&#8217;; example: &#8216;os:Arch.*&#8217;</p>
<dt><code>-N, &#8211;nodegroup</code></p>
<dd> Use a predefined compound target defined in the Salt master configuration file.</p>
<dt><code>-R, &#8211;range</code></p>
<dd> Instead of using shell globs to evaluate the target, use a range expression to identify targets. Range expressions look like %cluster. </p>
<p> Using the Range option requires that a range server is set up and the location of the range server is referenced in the master configuration file.</dl>
<h3>Logging Options</h3>
<p> Logging options which override any settings defined on the configuration files.</p>
<dl>
<dt><code>-l LOG_LEVEL, &#8211;log-level=LOG_LEVEL</code></p>
<dd> Console logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</p>
<dt><code>&#8211;log-file=LOG_FILE</code></p>
<dd> Log file path. Default: /var/log/salt/ssh.</p>
<dt><code>&#8211;log-file-level=LOG_LEVEL_LOGFILE</code></p>
<dd> Logfile logging log level. One of <code>all</code>, <code>garbage</code>, <code>trace</code>, <code>debug</code>, <code>info</code>, <code>warning</code>, <code>error</code>, <code>quiet</code>. Default: <code>warning</code>.</dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;out</code></p>
<dd> Pass in an alternative outputter to display the return of data. This outputter can be any of the available outputters: <code>grains</code>, <code>highstate</code>, <code>json</code>, <code>key</code>, <code>overstatestage</code>, <code>pprint</code>, <code>raw</code>, <code>txt</code>, <code>yaml</code> </p>
<p> Some outputters are formatted only for data returned from specific functions; for instance, the <code>grains</code> outputter will not work for non-grains data. </p>
<p> If an outputter is used that does not support the data passed into it, then Salt will fall back on the <code>pprint</code> outputter and display the return data using the Python <code>pprint</code> standard library module. </p>
<p> <code>NOTE:</code> If using <code>&#8211;out=json</code>, you will probably want <code>&#8211;static</code> as well. Without the static option, you will get a separate JSON string per minion which makes JSON output invalid as a whole. This is due to using an iterative outputter. So if you want to feed it to a JSON parser, use <code>&#8211;static</code> as well.</p>
<dt><code>&#8211;out-indent OUTPUT_INDENT, &#8211;output-indent OUTPUT_INDENT</code></p>
<dd> Print the output indented by the provided value in spaces. Negative values disable indentation. Only applicable in outputters that support indentation.</p>
<dt><code>&#8211;out-file=OUTPUT_FILE, &#8211;output-file=OUTPUT_FILE</code></p>
<dd> Write the output to the specified file.</p>
<dt><code>&#8211;no-color</code></p>
<dd> Disable all colored output</p>
<dt><code>&#8211;force-color</code></p>
<dd> Force colored output </p>
<p> <code>NOTE:</code> When using colored output the color codes are as follows: </p>
<p> <code>green</code> denotes success, <code>red</code> denotes failure, <code>blue</code> denotes changes and success and <code>yellow</code> denotes a expected future change in configuration.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-salt/">salt</a>(7)</i> <i><a href="/docs/linux/man/1-salt-master/">salt-master</a>(1)</i> <i><a href="/docs/linux/man/1-salt-minion/">salt-minion</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Thomas S. Hatch &lt;thatch45 [at] gmail.com&gt; and many others, please see the Authors file</p>
<h2>COPYRIGHT</h2>
<p> 2016 SaltStack, Inc. </p>
<h2>Index</h2>
