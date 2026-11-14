---
title: "mrtg(1)"
name: "mrtg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg/"
description: "mrtg – What is MRTG ?"
---

<h2 class="name">NAME</h2>
<p> mrtg &#8211; What is MRTG ? </p>
<h2>DESCRIPTION</h2>
<p> The Multi Router Traffic Grapher (<font SIZE="-1">MRTG</font>) is a tool to monitor the traffic load on network links. <font SIZE="-1">MRTG</font> generates <font SIZE="-1">HTML</font> pages containing <font SIZE="-1">PNG</font> images which provide a <font SIZE="-1">LIVE</font> visual representation of this traffic. Check <a rel="nofollow" href="http://www.stat.ee.ethz.ch/mrtg/">http://www.stat.ee.ethz.ch/mrtg/</a> to see what it does. </p>
<p> Go to<br />
&nbsp;<wbr><a rel="nofollow" href="http://oss.oetiker.ch/mrtg">http://oss.oetiker.ch/mrtg</a>&nbsp;<wbr> for all the details about mrtg.</p>
<h2>HIGHLIGHTS</h2>
<dl>
<dt>Portable</p>
<dd> <font SIZE="-1">MRTG</font> works on most <font SIZE="-1">UNIX</font> platforms and Windows <font SIZE="-1">NT</font>.</p>
<dt>Perl</p>
<dd> <font SIZE="-1">MRTG</font> is written in Perl and comes with full source.</p>
<dt>Portable <font SIZE="-1">SNMP</font></p>
<dd> <font SIZE="-1">MRTG</font> Uses a highly portable <font SIZE="-1">SNMP</font> implementation written entirely in Perl (thanks to Simon Leinen). There is no need to install any external <font SIZE="-1">SNMP</font> package.</p>
<dt>SNMPv2c support</p>
<dd> <font SIZE="-1">MRTG</font> can read the new SNMPv2c 64bit counters. No more counter wrapping.</p>
<dt>Reliable Interface Identification</p>
<dd> Router interfaces can be identified by <font SIZE="-1">IP</font> address, description and ethernet address in addition to the normal interface number.</p>
<dt>Constant size Logfiles</p>
<dd> <font SIZE="-1">MRTG</font>&#8216;s logfiles do <font SIZE="-1">NOT</font> grow thanks to the use of a unique data consolidation algorithm.</p>
<dt>Automatic Configuration</p>
<dd> <font SIZE="-1">MRTG</font> comes with a set of configuration tools which make configuration and setup very simple.</p>
<dt>Performance</p>
<dd> Time critical routines are written in C (thanks to the initiative of Dave Rand my Co-Author).</p>
<dt><font SIZE="-1">GIF</font> free Graphics</p>
<dd> Graphics are generated directly in <font SIZE="-1">PNG</font> format using the <font SIZE="-1">GD</font> library by Thomas Boutell.</p>
<dt>Customizability</p>
<dd> The look of the webpages produced by <font SIZE="-1">MRTG</font> is highly configurable.</p>
<dt>RRDtool</p>
<dd> <font SIZE="-1">MRTG</font> has built-in hooks for using RRDtool. If you are strapped for performance this may help.</dl>
<h2>DETAILS</h2>
<p> <font SIZE="-1">MRTG</font> consists of a Perl script which uses <font SIZE="-1">SNMP</font> to read the traffic counters of your routers and a fast C program which logs the traffic data and creates beautiful graphs representing the traffic on the monitored network connection. These graphs are embedded into webpages which can be viewed from any modern Web-browser. </p>
<p> In addition to a detailed daily view, <font SIZE="-1">MRTG</font> also creates visual representations of the traffic seen during the last seven days, the last five weeks and the last twelve months. This is possible because <font SIZE="-1">MRTG</font> keeps a log of all the data it has pulled from the router. This log is automatically consolidated so that it does not grow over time, but still contains all the relevant data for all the traffic seen over the last two years. This is all performed in an efficient manner. Therefore you can monitor 200 or more network links from any halfway decent <font SIZE="-1">UNIX</font> box. </p>
<p> <font SIZE="-1">MRTG</font> is not limited to monitoring traffic, though. It is possible to monitor any <font SIZE="-1">SNMP</font> variable you choose. You can even use an external program to gather the data which should be monitored via <font SIZE="-1">MRTG</font>. People are using <font SIZE="-1">MRTG</font>, to monitor things such as System Load, Login Sessions, Modem availability and more. <font SIZE="-1">MRTG</font> even allows you to accumulate two or more data sources into a single graph.</p>
<h2>HISTORY</h2>
<p> In 1994 I was working at a site where we had one 64kbit line to the outside world. Obviously, everybody was interested in knowing how the link was performing. So I wrote a quick hack which created a constantly updated graph on the web that showed the traffic load on our Internet link. This eventually evolved into a rather configurable Perl script called <font SIZE="-1">MRTG-1</font>.0 which I released in spring 1995. After a few updates, I left my job at <font SIZE="-1">DMU</font> to start work at the Swiss Federal Institute of Technology. Due to lack of time I had to put <font SIZE="-1">MRTG</font> aside. One day in January of 1996, I received email from Dave Rand asking if I had any ideas why <font SIZE="-1">MRTG</font> was so slow. Actually, I did. <font SIZE="-1">MRTG</font>&#8216;s programming was not very efficient and it was written entirely in Perl. After a week or so, Dave wrote back to me and said he had tried what I had suggested for improving <font SIZE="-1">MRTG</font>&#8216;s speed. Since the changes did not help much, he had decided to rewrite the time-critical sections of <font SIZE="-1">MRTG</font> in C. The code was attached to his email. His tool increased the speed of <font SIZE="-1">MRTG</font> by a factor of 40! This got me out of my &#8216;<font SIZE="-1">MRTG</font> ignorance&#8217; and I started to spend my spare time developing of <font SIZE="-1">MRTG-2</font>. </p>
<p> Soon after <font SIZE="-1">MRTG-2</font> development had begun I started to give beta copies to interested parties. In return I got many feature patches, a lot of user feedback and bug fixes. The product you are getting now wouldn&#8217;t be in this state if it hadn&#8217;t been for the great contributions and support I received from of many people. I would like to take this opportunity to thank them all. (See the files <font SIZE="-1">CHANGES</font> for a long list of folk people who helped to make <font SIZE="-1">MRTG</font> what it is today.)</p>
<h2>Command-line</h2>
<p> Mrtg is also the name of the script you have to run to poll data and generate the graphs. Most configuration is set through the configuration file; some command-line options exist all the same.</p>
<dl>
<dt><code>&#8211;user</code> <i>username</i> and <code>&#8211;group</code> <i>groupname</i></p>
<dd> Run as the given user and/or group. (Unix Only)</p>
<dt><code>&#8211;lock-file</code> <i>filename</i></p>
<dd> Use an alternate lock-file (the default is to use the configuration-file appended with <tt>&quot;_l&quot;</tt>).</p>
<dt><code>&#8211;confcache-file</code> <i>filename</i></p>
<dd> Use an alternate confcache-file (the default is to use the configuration-file appended with <tt>&quot;.ok&quot;</tt>)</p>
<dt><code>&#8211;logging</code> <i>filename</i>|<code>eventlog</code></p>
<dd> If this is set to writable filename, all output from mrtg (warnings, debug messages, errors) will go to <i>filename</i>. If you are running on Win32 you can specify <code>eventlog</code> instead of a filename which will send all error to the windows event log. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font>Note, there is no Message <font SIZE="-1">DLL</font> for mrtg. This has the side effect that the windows event logger will display a nice message with every entry in the event log, complaing about the fact that mrtg has no message dll. If any of the Windows folks want to contribute one, they are welcome.</p>
<dt><code>&#8211;daemon</code></p>
<dd> Put <font SIZE="-1">MRTG</font> into the background, running as a daemon. This works the same way as the config file option, but the switch is required for proper <font SIZE="-1">FHS</font> operation (because /var/run is writable only by root)</p>
<dt><code>&#8211;fhs</code></p>
<dd> Configure all mrtg paths to conform to the <font SIZE="-1">FHS</font> specification; <a rel="nofollow" href="http://www.pathname.com/fhs/">http://www.pathname.com/fhs/</a></p>
<dt><code>&#8211;check</code></p>
<dd> Only check the cfg file for errors. Do not do anything.</p>
<dt><code>&#8211;pid-file=s</code></p>
<dd> Define the name and path of the pid file for mrtg running as a daemon</p>
<dt><code>&#8211;log-only</code></p>
<dd> Only update the logfile, do not produce graphics or html pages</p>
<dt><code>&#8211;debug=s</code></p>
<dd> Enable debug options. The argument of the debug option is a comma separated list of debug values: </p>
<pre>
 cfg  - watch the config file reading
 dir  - directory mangeling
 base - basic program flow 
 tarp - target parser
 snpo - snmp polling 
 fork - forking view 
 time - some timing info
 log  - logging of data via rateup or rrdtool
</pre>
<p> Example: </p>
<pre>
 --debug=&quot;cfg,snpo&quot;
</pre>
</dl>
<h2>READ ON</h2>
<p> Learn more about <font SIZE="-1">MRTG</font> by going to the mrtg home page on: <a rel="nofollow" href="http://oss.oetiker.ch/mrtg">http://oss.oetiker.ch/mrtg</a></p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; and many contributors </p>
<h2>Index</h2>
