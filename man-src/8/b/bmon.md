---
title: "bmon(8)"
name: "bmon"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bmon/"
description: "bmon – bandwidth monitor and rate estimator"
---

<p>bmon &#8211; bandwidth monitor and rate estimator</p>
<h2>Synopsis</h2>
<p><code>bmon</code> [<code>&#8211;show-all</code>] [<code>&#8211;use-si</code>] [<code>&#8211;input</code>=<i>MODULE</i>] [<code>&#8211;output</code>=<i>MODULE</i>] [OPTIONS&#8230;] </p>
<h2>Description</h2>
<p>bmon is a monitoring and debugging tool to capture networking related statistics and prepare them visually in a human friendly way. It features various output methods including an interactive curses user interface and a programmable text output for scripting. </p>
<h2>Options</h2>
<p><code> -h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Prints a short help text and exits.</dl>
<p> <code> -V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Prints the versioning identifier and exits.</dl>
<p> <code> -i</code>, <code>&#8211;input=</code>MODULE[:OPTIONS][,MODULE&#8230;]</p>
<dl>
<dd>Set list of input modules to load and use. Multiple modules can be used in parallel. bmon automatically loads a useful and working input module by default. See INPUT MODULES for more details.</dl>
<p> <code> -o</code>, <code>&#8211;ouptut</code>MODULE[:OPTIONS][,MODULE&#8230;]</p>
<dl>
<dd>Set list of output modules to load and use. Multiple modules can be used in parallel. By default, bmon will use the curses output mode, if that is not available due to an incompatible console it will fall back to a simple text mode. See OUTPUT MODULES for more details.</dl>
<p> <code> -U</code>, <code>&#8211;use-si</code></p>
<dl>
<dd>Use SI unit system instead of 1KB = 1&#8217;024 bytes.</dl>
<p> <code> -f</code>, <code>&#8211;configfile=</code>FILE</p>
<dl>
<dd>Set alternative path to configuration file.</dl>
<p> <code> -p</code>, <code>&#8211;policy=</code>POLICY</p>
<dl>
<dd>Set policy defining which network interfaces to display. See INTERFACE SELECTION for more details.</dl>
<p> <code> -a</code>, <code>&#8211;show-all=</code></p>
<dl>
<dd>Display all interfaces, even interface that are administratively down.</dl>
<p> <code> -r</code>, <code>&#8211;read-interval=</code>FLOAT</p>
<dl>
<dd>Set interval in seconds in which input modules read statistics from their source. The default is 1.0 seconds.</dl>
<p> <code> -R</code>, <code>&#8211;rate-interval=</code>FLOAT</p>
<dl>
<dd>Set interval in seconds in which the rate per counter is calculated. The default is 1.0 seconds.</dl>
<p> <code> -L</code>, <code>&#8211;lifetime=</code>FLOAT</p>
<dl>
<dd>Set lifetime of an element in seconds before it is no longer displayed without receiving any statistical updates. The default is 30 seconds.</dl>
<h2>Input Modules</h2>
<p>Input modules provide statistical data about elements. Each element consists of attributes which represents a counter, a rate, or a percentage. Elements may carry additional child elements to represent a hierarchy. Each element is assigned to a group defined by the input module. Input modules are polled in the frequence of the configured read interval. </p>
<p> The following input modules are available:</p>
<dl>
<dt><code>netlink</code></p>
<dd>Uses the Netlink protocol to collect interface and traffic control statistics from the kernel. This is the default input module. </p>
<dt><code>proc</code></p>
<dd>Reads interface statistics from the /proc/net/dev file. This is considered a legacy interface and provided for backwards compatibily reasons. This is a fallback module if the Netlink interface is not available. </p>
<dt><code>dummy</code></p>
<dd>Programmable input module for debugging and testing purposes. </p>
<dt><code>null</code></p>
<dd>No data collected. </p>
</dl>
<p> To receive additional information about a module, run the module with the &quot;help&quot; option set like this: </p>
<dl>
<dd>bmon -i netlink:help</dl>
<p> See MODULE CONFIGURATION for more details.</p>
<h2>Output Modules</h2>
<p>Output modules display or export the statistical data collected by input modules. Multiple output modules can be run at the same time. bmon will not prevent possible conflicts such as multiple output modules writing to the console. </p>
<p> The following output modules exist: </p>
<dl>
<dt><code>curses</code></p>
<dd>Interactive curses based text user interface providing real time rate estimations and a graphical representatio nof each attribute. Press &#8216;?&#8217; to display the quick reference guide. This is the default output mode. </p>
<dt><code>ascii</code></p>
<dd>Simple programmable text output intended for human consumption. Capable of printing list of interfaces, detailed counters and graphs to the console. This is the default fallback output mode if curses is not available. </p>
<dt><code>format</code></p>
<dd>Fully scriptable output mode inteded for consumption by other programs. See the module help text for additional information. </p>
<dt><code>null</code></p>
<dd>Disable output. </p>
</dl>
<p> To receive additional information about a module, run the module with the &quot;help&quot; option set like this: </p>
<dl>
<dd>bmon -o curses:help</dl>
<p> See MODULE CONFIGURATION for more details.</p>
<h2>Module Configuration</h2>
<p>The syntax to configure modules is as follows: </p>
<dl>
<dd>ARGUMENT ::= mod1[:OPTS][,mod2[:OPTS]&#8230;]<br />
 OPTS ::= OPTION[;OPTION&#8230;]<br />
 OPTION ::= option[=value]</dl>
<p> Run the module with option &quot;help&quot; to receive the list of options for each module: </p>
<dl>
<dd>bmon -i module:help</dl>
<h2>Interface Selection</h2>
<p>The following syntax is used to define the interface selection policy: </p>
<dl>
<dd>SELECTION ::= NAME[,NAME[,&#8230;]]<br />
 NAME ::= [!]interface</dl>
<p> The interface name may contain the character &#8216;*&#8217; which will act as a wildcard and represents any number of any character type, e.g. eth*, h*0, &#8230; </p>
<p> Examples: </p>
<dl>
<dd>lo,eth0,eth1<br />
 eth*,!eth0</dl>
<h2>Examples</h2>
<p>To run bmon in curses mode monitoring the interfaces eth0 and eth1:</p>
<dl>
<dd><code>bmon -p eth0,eth1 -o curses</code></dl>
<h2>Files</h2>
<p>/etc/bmon.conf<br />
 $HOME/.bmonrc</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-netstat/">netstat</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), </p>
<h2>Author</h2>
<p>Thomas Graf &lt;tgraf [at] suug.ch&gt; among others</p>
