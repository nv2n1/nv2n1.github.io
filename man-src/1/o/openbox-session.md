---
title: "openbox-session(1)"
name: "openbox-session"
section: "1"
letter: "o"
url: "/docs/linux/man/1-openbox-session/"
description: "openbox-session — Runs an Openbox session without any session manager."
---

<h2>NAME</h2>
<p> openbox-session &#8212; Runs an Openbox session without any session manager.<br />
&nbsp;<wbr></p>
<h2>DESCRIPTION</h2>
<p> <code>openbox-session</code> runs an openbox session without any session manager. Without a session manager, you will not be able to save your state from one log in to the next. </p>
<p> <code>openbox-session</code> does not take any command line arguments. </p>
<p> On log in, <code>openbox-session</code> will run the ~/.config/openbox/autostart.sh script if it exists, and will run the system-wide script /etc/xdg/openbox/autostart.sh otherwise. You may place anything you want to run automatically in those files, for example:<br />
&nbsp;<wbr> </p>
<dl>
<dt>
<dd>
<pre>
xsetroot -solid grey &amp; 
gnome-settings-daemon &amp; 
</pre>
</dl>
<p> Make sure that each line is followed by a &quot;&amp;&quot; or else the script will stop there and further commands will not be executed. You can use the /etc/xdg/openbox/autostart.sh file as an example for creating your own.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-openbox/">openbox</a>(1), <a href="/docs/linux/man/1-openbox-session/">openbox-session</a>(1), <a href="/docs/linux/man/1-openbox-gnome-session/">openbox-gnome-session</a>(1).<br />
&nbsp;<wbr> </p>
<p> The program&#8217;s full documentation is available on the website: <code><a rel="nofollow" href="http://openbox.org/">http://openbox.org/</a></code> </p>
<p> Please report bugs to: <code><a rel="nofollow" href="http://bugzilla.icculus.org/">http://bugzilla.icculus.org/</a> </code> </p>
<h2>Index</h2>
