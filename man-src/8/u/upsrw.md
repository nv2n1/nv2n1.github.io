---
title: "upsrw(8)"
name: "upsrw"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsrw/"
description: "upsrw – UPS variable administration tool"
---

<p>upsrw &#8211; UPS variable administration tool</p>
<h2>Synopsis</h2>
<p><code>upsrw</code> <i>ups</i> </p>
<p> <code>upsrw</code> -h </p>
<p> <code>upsrw</code> -s <i>variable</i> [-u <i>username</i>] [-p <i>password</i>] <i>ups</i></p>
<h2>Description</h2>
<p><code>upsrw</code> allows you to view and change the read/write variables inside your UPS. It sends commands via the server <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) to your driver, which configures the hardware for you. </p>
<p> The list of variables that allow you to change their values is based on the capabilities of your UPS equipment. Not all models support this feature. Typically, cheaper hardware does not support any of them. Run upsrw with a UPS identifier to see what will work for you.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help message.</dl>
<p> <code>-s</code> <i>variable</i></p>
<dl>
<dd>Specify the variable to be changed inside the UPS. For unattended mode such as in shell scripts, use the format VAR=VALUE to specify both the variable and the value, for example: </p>
<dl>
<dd>
<pre>-s input.transfer.high=129</pre>
</dl>
<p> Without this argument, upsrw will just display the list of the variables and their possible values. </p>
<p> Some variables are strings, and can be set to any value within the length limit. Others are enumerated types and can only be set to one of those values. Others may be within an allowed range of values. Refer to the list to know what&#8217;s available in your hardware.</dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dd>Set the NUT username for the connection to the server. This is optional, and you will be prompted for this when using the -s option if you don&#8217;t specify -u on the command line. NUT usernames are defined in <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5), and are not linked to system usernames.</dl>
<p> <code>-p</code> <i>password</i></p>
<dl>
<dd>Set the password to authenticate to the server. This is also optional like -u, and you will be prompted for it if necessary.</dl>
<p> <i>ups</i></p>
<dl>
<dd>View or change the settings on this UPS. The format for this option is upsname[@hostname[:port]]. The default hostname is &quot;localhost&quot;.</dl>
<h2>Unattended Mode</h2>
<p>If you run this program inside a shell script or similar to set variables, you will need to specify all of the information on the command line. This means using -s VAR=VALUE, -u and -p. Otherwise it will put up a prompt and your program will hang. </p>
<p> This is not necessary when displaying the list, as the username and password are not required for read-only mode. </p>
<p> Moreover, if you run this program inside a shell script or similar, you should only consider using output from stdout, not stderr.</p>
<h2>Diagnostics</h2>
<p><code>upsrw</code> can&#8217;t set variables on your UPS unless you provide a valid username and password. If you get &quot;access denied&quot; errors, make sure that your <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5) has an entry for you, and that the username you are using has permissions to SET variables.</p>
<h2>History</h2>
<p>This program used to be called upsct2, which was ambiguous and confusing.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
