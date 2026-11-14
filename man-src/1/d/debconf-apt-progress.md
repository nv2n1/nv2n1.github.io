---
title: "debconf-apt-progress(1)"
name: "debconf-apt-progress"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-apt-progress/"
description: "debconf-apt-progress – install packages using debconf to display a progress bar"
---

<h2 class="name">NAME</h2>
<p> debconf-apt-progress &#8211; install packages using debconf to display a progress bar </p>
<h2>SYNOPSIS</h2>
<pre><code>
debconf - apt - progress[--] command[args...] debconf - apt - progress-- config debconf - apt - progress-- start debconf - apt - progress-- from waypoint-- to waypoint[--] command[args...] debconf - apt - progress-- stop
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>debconf-apt-progress</code> installs packages using debconf to display a progress bar. The given <i>command</i> should be any command-line apt frontend; specifically, it must send progress information to the file descriptor selected by the <tt>&quot;APT::Status-Fd&quot;</tt> configuration option, and must keep the file descriptors nominated by the <tt>&quot;APT::Keep-Fds&quot;</tt> configuration option open when invoking debconf (directly or indirectly), as those file descriptors will be used for the debconf passthrough protocol. </p>
<p> The arguments to the command you supply should generally include <code>-y</code> (for <code>apt-get</code> or <code>aptitude</code>) or similar to avoid the apt frontend prompting for input. <code>debconf-apt-progress</code> cannot do this itself because the appropriate argument may differ between apt frontends. </p>
<p> The <code>&#8211;start</code>, <code>&#8211;stop</code>, <code>&#8211;from</code>, and <code>&#8211;to</code> options may be used to create a progress bar with multiple segments for different stages of installation, provided that the caller is a debconf confmodule. The caller may also interact with the progress bar itself using the debconf protocol if it so desires. </p>
<p> debconf locks its config database when it starts up, which makes it unfortunately inconvenient to have one instance of debconf displaying the progress bar and another passing through questions from packages being installed. If you&#8217;re using a multiple-segment progress bar, you&#8217;ll need to eval the output of the <code>&#8211;config</code> option before starting the debconf frontend to work around this. See &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> in the <font SIZE="-1">EXAMPLES</font> section below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config</code></p>
<dd> Print environment variables necessary to start up a progress bar frontend.</p>
<dt><code>&#8211;start</code></p>
<dd> Start up a progress bar, running from 0 to 100 by default. Use <code>&#8211;from</code> and <code>&#8211;to</code> to use other endpoints.</p>
<dt><code>&#8211;from</code> <i>waypoint</i></p>
<dd> If used with <code>&#8211;start</code>, make the progress bar begin at <i>waypoint</i> rather than 0. </p>
<p> Otherwise, install packages with their progress bar beginning at this &#8220;waypoint&#8221;. Must be used with <code>&#8211;to</code>.</p>
<dt><code>&#8211;to</code> <i>waypoint</i></p>
<dd> If used with <code>&#8211;start</code>, make the progress bar end at <i>waypoint</i> rather than 100. </p>
<p> Otherwise, install packages with their progress bar ending at this &#8220;waypoint&#8221;. Must be used with <code>&#8211;from</code>.</p>
<dt><code>&#8211;stop</code></p>
<dd> Stop a running progress bar.</p>
<dt><code>&#8211;no-progress</code></p>
<dd> Avoid starting, stopping, or stepping the progress bar. Progress messages from apt, media change events, and debconf questions will still be passed through to debconf.</p>
<dt><code>&#8211;dlwaypoint</code> <i>percentage</i></p>
<dd> Specify what percent of the progress bar to use for downloading packages. The remainder will be used for installing packages. The default is to use 15% for downloading and the remaining 85% for installing.</p>
<dt><code>&#8211;logfile</code> <i>file</i></p>
<dd> Send the normal output from apt to the given file.</p>
<dt><code>&#8211;logstderr</code></p>
<dd> Send the normal output from apt to stderr. If you supply neither <code>&#8211;logfile</code> nor <code>&#8211;logstderr</code>, the normal output from apt will be discarded.</p>
<dt><code>&#8212;</code></p>
<dd> Terminate options. Since you will normally need to give at least the <code>-y</code> argument to the command being run, you will usually need to use <code>&#8212;</code> to prevent that being interpreted as an option to <code>debconf-apt-progress</code> itself.</dl>
<h2>EXAMPLES</h2>
<p> Install the <font SIZE="-1">GNOME</font> desktop and an X window system development environment within a progress bar: </p>
<pre>
 debconf-apt-progress -- aptitude -y install gnome x-window-system-dev
</pre>
<p> Install the <font SIZE="-1">GNOME, KDE,</font> and <font SIZE="-1">XFCE</font> desktops within a single progress bar, allocating 45% of the progress bar for each of <font SIZE="-1">GNOME</font> and <font SIZE="-1">KDE</font> and the remaining 10% for <font SIZE="-1">XFCE:</font> </p>
<pre><code>
#!/ bin / sh
 set -e
 case $1 in
   '')
     eval "$(debconf-apt-progress --config)"
     "$0" debconf
     ;
 ;
   debconf)
     . /usr/share/debconf/confmodule
     debconf-apt-progress --start
     debconf-apt-progress --from 0 --to 45 -- apt-get -y install gnome
     debconf-apt-progress --from 45 --to 90 -- apt-get -y install kde
     debconf-apt-progress --from 90 --to 100 -- apt-get -y install xfce4
     debconf-apt-progress --stop
     ;
   ;
   esac
</code></pre>
<h2>RETURN CODE</h2>
<p> The exit code of the specified command is returned, unless the user hit the cancel button on the progress bar. If the cancel button was hit, a value of 30 is returned. To avoid ambiguity, if the command returned 30, a value of 3 will be returned.</p>
<h2>AUTHORS</h2>
<p> Colin Watson &lt;cjwatson [at] debian.org&gt; </p>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
