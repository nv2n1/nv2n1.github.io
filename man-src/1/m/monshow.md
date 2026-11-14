---
title: "monshow(1)"
name: "monshow"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monshow/"
description: "monshow – show operational status of mon server."
---

<h2>NAME</h2>
<p> monshow &#8211; show operational status of mon server.</p>
<h2>SYNOPSIS</h2>
<p> <code>monshow</code> [<code>&#8211;help</code>] [<code>&#8211;showall</code>] [<code>&#8211;full</code>] [<code>&#8211;disabled</code>] [<code>&#8211;detail</code> <i>group,service</i>] [<code>&#8211;view</code> <i>name</i>] [<code>&#8211;auth</code>] [<code>&#8211;login</code> <i>user</i>] [<code>&#8211;old</code>] [<code>&#8211;server</code> <i>hostname</i>] [<code>&#8211;port</code> <i>portnum</i>] [<code>&#8211;prot</code> <i>protocol</i>] [<code>&#8211;rcfile</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>monshow</code> show the operational status of the <code>mon</code> server. Both command-line and CGI interfaces are available.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show help</p>
<dt><code>&#8211;showall</code></p>
<dd> Do not read configuration file, and show operational status of all groups and services.</p>
<dt><code>&#8211;full</code></p>
<dd> Instead of showing only failed services, show all services no matter the state.</p>
<dt><code>&#8211;detail&nbsp;<wbr></code><i>group,service</i></p>
<dd> Display detailed information for <i>group</i> and <i>service</i>. This includes description, detailed output of the monitor, dependency information, and more. When invoked via CGI, append &quot;detail=group,service&quot; to get detail for a service.</p>
<dt><code>&#8211;view </code><i>name</i></p>
<dd> Display a pre-configured view. When invoked via CGI, supply the arguments &quot;view=name&quot; in the URL, or by using this technique: &quot;<a rel="nofollow" href="http://monhost/monshow.cgi/name">http://monhost/monshow.cgi/name</a>&quot;. For security reasons, leading forward slashes and imbedded &quot;..&quot;s are removed from the view name.</p>
<dt><code>&#8211;auth</code></p>
<dd> Authenticate client to the mon server.</p>
<dt><code>&#8211;disabled</code></p>
<dd> Show disabled groups, services, and hosts. The default is to not show anything which is disabled, but this may be overridden by the config file.</p>
<dt><code>&#8211;server </code><i>hostname</i></p>
<dd> Connect to the mon server on host <i>hostname</i>. <i>hostname</i> can be either the name of a host or an IP address. If this name is not supplied by this argument, then the environment variable <i>MONHOST</i> is used, if it exists. Otherwise, <i>monshow</i> will fail.</p>
<dt><code>&#8211;login</code><i>&nbsp;<wbr>username</i></p>
<dd> When authenticating, use <i>username</i>.</p>
<dt><code>&#8211;port</code><i>&nbsp;<wbr>portnum</i></p>
<dd> Connect to the server on <code>portnum</code>.</p>
<dt><code>&#8211;prot</code><i>&nbsp;<wbr>protocol</i></p>
<dd> Sets the protocol to <i>protocol</i>. The protocol must match the format &quot;1.2.3&quot;. If unset, the default supplied by the Mon::Client module is used. Do not use this parameter unless you really know what you are doing.</p>
<dt><code>&#8211;old</code></p>
<dd> Use the old 0.37 protocol and port number (32777).</p>
<dt><code>&#8211;rcfile</code><i>&nbsp;<wbr>file</i></p>
<dd> Use configuration file <i>file</i> instead of ~/.monshowrc. </p>
</dl>
<h2>CGI INVOCATION</h2>
<p> If <code>monshow</code> is invoked with the &quot;REQUEST_METHOD&quot; environment variable set, then CGI invocation is assumed. In that case, <code>monshow</code> gathers variables and commands submitted via the POST method and QUERY_STRING. Command-line options are ignored for security reasons. </p>
<p> All reports which are produced via the web interface have a text mode equivalent. </p>
<h2>VIEWS</h2>
<p> A view is a pre-defined configuration supplied to <code>monshow</code>. Views can be used to generate different reports of the status of certain services for different audiences. They are especially useful if you are monitoring hundreds of things with mon, and you need to see only a subset of the overall operational status. For example, the web server admins can see a report which has only the web server statuses, and the file server admins can have their own report which shows only the servers. Users can customize their own views by editing their own configurations. </p>
<p> Views are stored as files in a system-wide directory, typically <i>/etc/mon/monshow</i>, where each file specifies one view. If this path is not suitable for any reason, it can be changed by modifying the <code>$VIEWPATH</code> variable in the <code>monshow</code> script. </p>
<p> When invoking <code>monshow</code> from the command line, the view to display is specified by the <code>&#8211;view=</code><i>name</i> argument. </p>
<p> In the case of CGI invocation, views can be specified by appending either <i>?view=name</i> or <i>/name</i> to the URL. For example, the following are equivalent: </p>
<p> <i><a rel="nofollow" href="http://monhost/monshow.cgi?view=test">http://monhost/monshow.cgi?view=test</a></i><br />
 <i><a rel="nofollow" href="http://monhost/monshow.cgi/test">http://monhost/monshow.cgi/test</a></i> </p>
<p> If a view is not specified, then a default configuration will be loaded from <i>$HOME/.monshowrc</i> (command-line invocation) or <i>cgi-path/.monshowrc</i> (CGI invocation). </p>
<h2>VIEW CONFIGURATION FILE</h2>
<p> The view file contains a list of which services to display, how to display them, and a number of other parameters. Blank lines and lines beginning with a # (pound) are ignored. </p>
<dl>
<dt><code>watch</code><i> group</i></p>
<dd> Include the status of all the services for &quot;group&quot;.</p>
<dt><code>service</code><i> group service</i></p>
<dd> Include the status of the service specified by <i>group</i> and <i>service</i>. If no <code>watch</code> or <code>service</code> configuration lines are present, then the status of all groups and services are displayed.</p>
<dt><code>set show-disabled</code></p>
<dd> This has the same effect as using the <code>&#8211;disabled</code> option.</p>
<dt><code>set host</code><i> hostname</i></p>
<dd> Query the mon server <i>hostname</i>.</p>
<dt><code>set port</code><i> number</i></p>
<dd> The TCP port which the mon server is listening on.</p>
<dt><code>set prot</code><i> protocol</i></p>
<dd> Set the protocol. This probably should not be used unless you really know what you&#8217;re doing.</p>
<dt><code>set full</code></p>
<dd> Show everything disabled, all failures, all successes, and all untested services.</p>
<dt><code>set bg</code><i> color</i></p>
<dd> Background color for the CGI report. The value of this parameter should resemble &quot;d5d5d5&quot; (without the quotes).</p>
<dt><code>set bg-ok</code><i> color</i></p>
<dd> Background color for services which are in an &quot;ok&quot; state.</p>
<dt><code>set bg-fail</code><i> color</i></p>
<dd> Background color for services which are failing.</p>
<dt><code>set bg-untested</code><i> color</i></p>
<dd> Background color for services which have yet to be tested.</p>
<dt><code>set refresh</code><i> seconds</i></p>
<dd> For CGI output, set the frequency that the report reloads. The default is to not reload.</p>
<dt><code>summary-len</code><i> len</i></p>
<dd> For CGI output, set the maximum length of the summary output to display. Summary text which exceeds <i>len</i> will be truncated and replaced with ellipses.</p>
<dt><code>link</code><i> group service URL</i></p>
<dd> For the CGI report, make a link to <i>URL</i> at the bottom of the detail report for <i>group/service</i> for more information.</p>
<dt><code>link-text</code><i> group service</i></p>
<dd> Insert all HTML up until a line beginning with &quot;END&quot; after the link specified with the <code>link</code> setting.</p>
<dt><code>set html-header</code></p>
<dd> Lines after this statement, continuing up until a line beginning with the word &quot;END&quot; will be displayed after the &quot;&lt;/head&gt;&quot; tag in the CGI output. Use this to display custom headers, including images and other fancy things. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>MONHOST</p>
<dd> The hostname of the server which runs the <code>mon</code> process. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-mon/">mon</a>(8)</p>
<h2>BUGS</h2>
<p> Report bugs to the email address below.</p>
<h2>AUTHOR</h2>
<p> Jim Trocki &lt;trockij [at] arctic.org&gt; </p>
<h2>Index</h2>
