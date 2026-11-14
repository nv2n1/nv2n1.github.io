---
title: "upsset-cgi(8)"
name: "upsset-cgi"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsset-cgi/"
description: "upsset.cgi – Web-based UPS administration program"
---

<p>upsset.cgi &#8211; Web-based UPS administration program</p>
<h2>Synopsis</h2>
<p><code>upsset.cgi</code></p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 As a CGI program, this should be invoked through your web server. If you run it from the command line, it will sit there until you give it input resembling a POST request. </p>
<h2>Description</h2>
<p><code>upsset.cgi</code> lets you access many administrative functions within the UPS software from your web browser. You can change settings and invoke instant commands where available.</p>
<h2>Changing Settings</h2>
<p>Some UPS hardware allows you to change certain variables to other values. To see what&#8217;s available, pick a UPS from the chooser and select &quot;settings&quot;, then select &quot;View&quot; to update the page. </p>
<p> You should see a list of items with the descriptions on the left side and the possible options or input spaces on the right. After changing something, be sure to &quot;Save changes&quot; to update the values in your UPS. </p>
<p> If your UPS doesn&#8217;t support any read/write variables, there will be nothing to do on this page. </p>
<p> Setting values in read/write variables can also be done from the command line with <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8).</p>
<h2>Instant Commands</h2>
<p>Some UPS hardware also has provisions for performing certain actions at the user&#8217;s command. These include battery tests, battery calibration, front panel tests (beep!) and more. To access this section, do as above, but pick &quot;Commands&quot; as the function. </p>
<p> If your UPS supports any instant commands, they will be listed in a chooser widget. Pick the one you like and &quot;Issue command&quot; to make it happen. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> some dangerous commands like &quot;Turn off load&quot; may not happen right away. This is a feature, not a bug. </p>
</dl>
<p> The apcsmart driver and some others require that you send this command twice within a short window in order to make it happen. This is to keep you from accidentally killing your systems by picking the wrong one. </p>
<p> To actually turn off the load, you have to send the command once, then send it again after 3 seconds elapse but before 15 seconds pass. If you do it too quickly or slowly, you have to wait at least 3 seconds but not 15 seconds again. </p>
<p> You can also invoke instant commands from the command line with <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8).</p>
<h2>Access Control</h2>
<p>upsset will only talk to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) servers that have been defined in your <code><a href="/docs/linux/man/8-hosts-conf/">hosts.conf</a></code>(8). If it complains about &quot;Access to that host is not authorized&quot;, check your hosts.conf first.</p>
<h2>Security</h2>
<p>upsset will not run until you convince it that your CGI directory has been secured. This is due to the possibility of someone using upsset to try password combinations against your <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server. </p>
<p> See the example upsset.conf file for more information on how you do this. The short explanation is&#8212;if you can&#8217;t lock it down, don&#8217;t try to run it.</p>
<h2>Files</h2>
<p><code><a href="/docs/linux/man/5-hosts-conf/">hosts.conf</a></code>(5), <code><a href="/docs/linux/man/5-upsset-conf/">upsset.conf</a></code>(5)</p>
<h2>See Also</h2>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
