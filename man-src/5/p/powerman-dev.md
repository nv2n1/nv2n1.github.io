---
title: "powerman-dev(5)"
name: "powerman-dev"
section: "5"
letter: "p"
url: "/docs/linux/man/5-powerman-dev/"
description: "powerman.dev – PowerMan device specification files"
---

<p>powerman.dev &#8211; PowerMan device specification files</p>
<h2>Description</h2>
<p>PowerMan device specifications are rather wierd. For this reason, we suggest that you leave the writing of these scripts to the PowerMan authors. However, if you insist, here is how they work. Note: the authors do not guarantee that the PowerMan specification language will not change, however we are open to taking on maintenance of scripts submitted by PowerMan users. We can&#8217;t guarantee that we&#8217;ll be able to test new releases against all devices but we&#8217;ll do our best not to break anything. NOTE: the best way to help us in this endeavor is to provide a &#8220;simulator&#8221; for your power controller and associated tests in the <i>test</i> subdirectory of the powerman source code. See the examples in that directory. By convention, device scripts are one device per file and are included as needed from a powerman.conf file, like this:</p>
<dl>
<dd>
<pre>include &quot;/etc/powerman/icebox3.dev&quot;</pre>
</dl>
<p> A device script is surrounded by an outer block:</p>
<dl>
<dd>
<pre>specification &quot;my_device_name&quot; {
 # configuration settings 
 # script blocks
}</pre>
</dl>
<p> The possible configuration settings are:</p>
<dl>
<dt><i>timeout &lt;float&gt;</i></p>
<dd>(optional) device script timeout in seconds &#8211; applies to each script, the whole thing, not just a particular &quot;expect&quot;.</p>
<dt><i>plug name { &lt;string list&gt; }</i></p>
<dd>(optional) if plug names are static, they should be defined. Any reference to a plug name in the powerman.conf must match one of the defined plug names.</p>
<dt><i>pingperiod &lt;float&gt;</i></p>
<dd>(optional) if a ping script is defined, and pingperiod is nonzero, the ping script will be executed periodically, every &lt;float&gt; seconds.</dl>
<p> Script blocks have the form:</p>
<dl>
<dd>
<pre>script &lt;script_name&gt; {
 # statements
}</pre>
</dl>
<p> Script blocks should all be grouped together with no config lines in between. Scripts are for performing particular operations such as power on, get power status, etc. The various script names are listed below. Those marked with [%s] are called with a plug name &quot;argument&quot;, which can be included in a send statements by including a %s (printf style). Warning: all the send strings are processed with printf and you can cause powermand to segfault if you include any printf tokens other than the appropriate zero or one %s.</p>
<dl>
<dt><i>login</i></p>
<dd>Executed immediately on (re-)connect. If you need to login to the box, do it here. This is also a good place to descend through a first layer of menus. Caveat: % occurring in passwords must be escaped as %%. Caveat: occurs outside of client session so cannot be debugged with -T. A trick when debugging is to move this code into the status script temporarily so you can see what is going on.</p>
<dt><i>logout</i></p>
<dd>Executed prior to disconnect. Get device in a state so login script will work (though hopefully disconnecting will do that too).</p>
<dt><i>status_all, status[%s]</i></p>
<dd>Obtain plug state for all plugs or only the specified plug. When all plugs of a device are involved in a plug status query, the status_all script, if defined, will be called in preference to the status script; otherwise the status script is called for each plug.</p>
<dt><i>on_all, on_range[%s], on[%s] </i></p>
<dd>Power on all plugs, a range of plugs, or the specified plug.</p>
<dt><i>off_all, off_range[%s], off[%s]</i></p>
<dd>Power off all plugs, a range of plugs, or the specified plug.</p>
<dt><i>cycle_all, cycle_range[%s], cycle[%s]</i></p>
<dd>Power cycle all plugs, a range of plugs, or the specified plug. The intent of this command was to map to the RPC&#8217;s cycle command; however, device script are increasingly implementing this in terms of a power off/delay/power so the off time can be controlled by the script.</p>
<dt><i>status_soft_all, status_soft[%s]</i></p>
<dd>Obtain soft power state for all plugs or only the specified plug. Soft Power refers to the &quot;standby state&quot; of the node. On means the node is powered up. Off means either the node is powered off at the plug or is powered on at the plug and in standby mode. This is really only useful on devices that include both a plug relay and a probe into the node attached to a non-standby power source.</p>
<dt><i>status_temp_all, status_temp[%s]</i></p>
<dd>Obtain temperature reading for all plugs or only the specified plug. Temperature is obtained by sampling a thermocouple in the node. Results are reported as a text string &#8211; not interpreted by Powerman beyond any regex chopping done by the script.</p>
<dt><i>status_beacon_all, status_beacon[%s]</i></p>
<dd>Obtain beacon state for all plugs or only the specified plug. Some RPC&#8217;s include a way to flash a light on a node.</p>
<dt><i>beacon_on[%s]</i></p>
<dd>Flash beacon on the specified plug.</p>
<dt><i>beacon_off[%s]</i></p>
<dd>Clear beacon on the specified plug.</p>
<dt><i>reset_all, reset_range[%s], reset[%s]</i></p>
<dd>Reset all plugs, a range of plugs, or only the specified plug. Reset refers to signaling a motherboard reset butten header, not a plug cycle.</dl>
<p> Within a script, the following statements can be used:</p>
<dl>
<dt><i>send &lt;string&gt;</i></p>
<dd>Send &lt;string&gt; to the device.</p>
<dt><i>delay &lt;float&gt;</i></p>
<dd>Pause script for &lt;float&gt; seconds.</p>
<dt><i>expect &lt;string&gt;</i></p>
<dd>&lt;string&gt; is compiled as a regular expression with <a href="/docs/linux/man/3-regcomp/">regcomp</a>(3). The regular expression is matched against device input. The script blocks until the regex is matched or the device timeout occurs (in which case the script is aborted). Upon matching, any parenthesized expressiones are assigned to variables: $1 for the first match, $2 for the second match, and so on. Warning: some implementations of <a href="/docs/linux/man/3-regex/">regex</a>(3) silently fail if the regular expression exceeds available static storage.</p>
<dt><i>setplugstate [&lt;string&gt;|&lt;regmatch&gt;] &lt;regmatch&gt; [off=&lt;string&gt;] [on=&lt;string&gt;]</i></p>
<dd>Set the plug state. The first argument, if present, is the literal plug name or a &lt;regmatch&gt; from the previous expect which contains the plug name. If omitted, the plug name is presumed to be the script argument. The off and on strings are compiled regexes, which if matched by the second argument, result in the plug state being set to off or on. Yes we are applying regexes to regmatches! If no off or on strings are provided, state will be unknown.</p>
<dt><i>ifoff, ifon</i></p>
<dd>Script statements enclosed in an ifon/ifoff block are conditional executed based on the state of the plug passed in as an argument. Ifon/ifoff blocks can only be used in single plug scripts that take an argument.</p>
<dt><i>foreachplug</i></p>
<dd>Script statements enclosed in a foreachplug block are executed iteratively with a %s argument defined for each target plug. Foreachplug blocks can only be used in all plug scripts that take no argument.</dl>
<p> Script terminals are defined as follows:</p>
<dl>
<dt><i>&lt;float&gt;</i></p>
<dd>decimal number &#8211; exponent forms not supported</p>
<dt><i>&lt;string&gt;</i></p>
<dd>Text surrounded by double quotes. May contain C style backslash-escaped characters, including three digit octal values, and most common backslash-escaped single character values.</p>
<dt><i>&lt;string list&gt;</i></p>
<dd>Multiple &lt;string&gt; values separated by white space.</p>
<dt><i>&lt;script_name&gt;</i></p>
<dd>Name of script (see above).</p>
<dt><i>&lt;regmatch&gt;</i></p>
<dd>Results of a parenthesized regular expression match are assigned to $1, $2, &#8230; $N. </p>
<h2>Files</h2>
<p>/etc/powerman/*.dev</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
