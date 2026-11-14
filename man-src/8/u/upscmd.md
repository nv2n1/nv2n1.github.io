---
title: "upscmd(8)"
name: "upscmd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upscmd/"
description: "upscmd – UPS administration program for instant commands"
---

<p>upscmd &#8211; UPS administration program for instant commands</p>
<h2>Synopsis</h2>
<p><code>upscmd</code> -h </p>
<p> <code>upscmd</code> -l <i>ups</i> </p>
<p> <code>upscmd</code> [-u <i>username</i>] [-p <i>password</i>] <i>ups</i> <i>command</i></p>
<h2>Description</h2>
<p><code>upscmd</code> allows you to invoke &quot;instant commands&quot; in your UPS hardware. Not all hardware supports this, so check the list with -l to see if anything will work on your equipment. </p>
<p> On hardware that supports it, you can use this program to start and stop battery tests, invoke a front panel test (beep!), turn the load on or off, and more.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help message.</dl>
<p> <code>-l</code> <i>ups</i></p>
<dl>
<dd>Show the list of supported instant commands on that UPS. Some hardware may not support any of them.</dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dd>Set the username for the connection to the server. This is optional, and you will be prompted for this when invoking a command if -u is not used.</dl>
<p> <code>-p</code> <i>password</i></p>
<dl>
<dd>Set the password to authenticate to the server. This is also optional like -u, and you will be prompted for it if necessary.</dl>
<p> <i>ups</i></p>
<dl>
<dd>Connect to this UPS. The format is upsname[@hostname[:port]]. The default hostname is &quot;localhost&quot;.</dl>
<h2>Unattended Mode</h2>
<p>If you run this program inside a shell script or similar to invoke a command, you will need to specify all of the information on the command line. This means using -u and -p. Otherwise it will put up a prompt and your program will hang. </p>
<p> This is not necessary when displaying the list, as the username and password are not required for read-only mode. </p>
<p> Moreover, if you run this program inside a shell script or similar, you should only consider using output from stdout, not stderr.</p>
<h2>Dangerous Commands</h2>
<p>Some drivers like <code><a href="/docs/linux/man/8-apcsmart/">apcsmart</a></code>(8) have built-in paranoia for the dangerous commands like load.off. To make them actually turn off the load, you will have to send the command twice within a short window. That is, you will have to send it once, then send it again after 3 seconds elapse but before 15 seconds pass. </p>
<p> This paranoia is entirely defined within the driver. upsd and upscmd have no control over the timing.</p>
<h2>Diagnostics</h2>
<p>upscmd won&#8217;t work unless you provide a valid username and password. If you get &quot;access denied&quot; errors, make sure that your <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5) has an entry for you, and that the username you are using has permissions to SET variables.</p>
<h2>Bugs</h2>
<p>There is currently no way to tell the user when the driver requires confirmation to invoke a command such as load.off. Similarly, there is not yet a way to tell the user if a command succeeds or fails. </p>
<p> This is on the list of things to fix in the future, so don&#8217;t despair. It involves magic cookies.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
