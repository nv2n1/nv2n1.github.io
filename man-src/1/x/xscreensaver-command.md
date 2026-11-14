---
title: "xscreensaver-command(1)"
name: "xscreensaver-command"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-command/"
description: "xscreensaver-command – control a running xscreensaver process"
---

<h2 class="name">NAME</h2>
<p> xscreensaver-command &#8211; control a running xscreensaver process </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-command</code> [-display <i>host:display.screen</i>] [-help | -demo | -prefs | -activate | -deactivate | -cycle | -next | -prev | -select <i>n</i> | -exit | -restart | -lock | -version | -time | -watch]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-command</i> program controls a running <i>xscreensaver</i> process by sending it client-messages. </p>
<p> <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) has a client-server model: the xscreensaver process is a daemon that runs in the background; it is controlled by other foreground programs such as <i>xscreensaver-command</i> and <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1). </p>
<p> This program, <i>xscreensaver-command</i>, is a command-line-oriented tool; the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1). program is a graphical tool.</p>
<h2>OPTIONS</h2>
<p> <i>xscreensaver-command</i> accepts the following command-line options:</p>
<dl>
<dt><code>-help</code></p>
<dd> Prints a brief summary of command-line options.</p>
<dt><code>-demo</code></p>
<dd> This just launches the <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) program, in which one can experiment with the various graphics hacks available, and edit parameters.</p>
<dt><code>-demo </code><i>number</i></p>
<dd> When the <i>-demo</i> option is followed by an integer, it instructs the <i>xscreensaver</i> daemon to run that hack, and wait for the user to click the mouse before deactivating (i.e., mouse motion does not deactivate.) This is the mechanism by which <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) communicates with the <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) daemon. (The first hack in the list is numbered 1, not 0.)</p>
<dt><code>-prefs</code></p>
<dd> Like the no-argument form of <i>-demo</i>, but brings up that program&#8217;s Preferences panel by default.</p>
<dt><code>-activate</code></p>
<dd> Tell xscreensaver to turn on immediately (that is, blank the screen, as if the user had been idle for long enough.) The screensaver will deactivate as soon as there is any user activity, as usual. </p>
<p> It is useful to run this from a menu; you may wish to run it as </p>
<pre>
sleep 5 ; xscreensaver-command -activate
</pre>
<p> to be sure that you have time to take your hand off the mouse before the screensaver comes on. (Because if you jiggle the mouse, xscreensaver will notice, and deactivate.)</p>
<dt><code>-deactivate</code></p>
<dd> This tells xscreensaver to pretend that there has just been user activity. This means that if the screensaver is active (the screen is blanked), then this command will cause the screen to un-blank as if there had been keyboard or mouse activity. If the screen is locked, then the password dialog will pop up first, as usual. If the screen is not blanked, then this simulated user activity will re-start the countdown (so, issuing the <i>-deactivate</i> command periodically is <i>one</i> way to prevent the screen from blanking.)</p>
<dt><code>-cycle</code></p>
<dd> If the screensaver is active (the screen is blanked), then stop the current graphics demo and run a new one (chosen randomly.)</p>
<dt><code>-next</code></p>
<dd> This is like either <i>-activate</i> or <i>-cycle</i>, depending on which is more appropriate, except that the graphics hack that will be run is the next one in the list, instead of a randomly-chosen one. In other words, repeatedly executing -next will cause the xscreensaver process to invoke each graphics demo sequentially. (Though using the <i>-demo</i> option is probably an easier way to accomplish that.)</p>
<dt><code>-prev</code></p>
<dd> This is like <i>-next</i>, but cycles in the other direction.</p>
<dt><code>-select </code><i>number</i></p>
<dd> Like <i>-activate</i>, but runs the <i>N</i>th element in the list of hacks. By knowing what is in the <i>programs</i> list, and in what order, you can use this to activate the screensaver with a particular graphics demo. (The first element in the list is numbered 1, not 0.)</p>
<dt><code>-exit</code></p>
<dd> Causes the xscreensaver process to exit gracefully. This does nothing if the display is currently locked. </p>
<p> <code>Warning:</code> never use <i>kill -9</i> with <i>xscreensaver</i> while the screensaver is active. If you are using a virtual root window manager, that can leave things in an inconsistent state, and you may need to restart your window manager to repair the damage.</p>
<dt><code>-lock</code></p>
<dd> Tells the running xscreensaver process to lock the screen immediately. This is like <i>-activate</i>, but forces locking as well, even if locking is not the default (that is, even if xscreensaver&#8217;s <i>lock</i> resource is false, and even if the <i>lockTimeout</i> resource is non-zero.) </p>
<p> Note that locking doesn&#8217;t work unless the <i>xscreensaver</i> process is running as you. See <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) for details.</p>
<dt><code>-version</code></p>
<dd> Prints the version of xscreensaver that is currently running on the display: that is, the actual version number of the running xscreensaver background process, rather than the version number of xscreensaver-command. (To see the version number of <i>xscreensaver-command</i> itself, use the <i>-help</i> option.)</p>
<dt><code>-time</code></p>
<dd> Prints the time at which the screensaver last activated or deactivated (roughly, how long the user has been idle or non-idle: but not quite, since it only tells you when the screen became blanked or un-blanked.)</p>
<dt><code>-restart</code></p>
<dd> Causes the screensaver process to exit and then restart with the same command line arguments as last time. You shouldn&#8217;t really need to do this, since xscreensaver notices when the <i>.xscreensaver</i> file has changed and re-reads it as needed.</p>
<dt><code>-watch</code></p>
<dd> Prints a line each time the screensaver changes state: when the screen blanks, locks, unblanks, or when the running hack is changed. This option never returns; it is intended for use by shell scripts that want to react to the screensaver in some way. An example of its output would be: </p>
<pre>
BLANK Fri Nov  5 01:57:22 1999
RUN 34
RUN 79
RUN 16
LOCK Fri Nov  5 01:57:22 1999
RUN 76
RUN 12
UNBLANK Fri Nov  5 02:05:59 1999
</pre>
<p> The above shows the screensaver activating, running three different hacks, then locking (perhaps because the lock-timeout went off) then unblanking (because the user became active, and typed the correct password.) The hack numbers are their index in the `programs&#8217; list (starting with 1, not 0, as for the <i>-select</i> command.) </p>
<p> For example, suppose you want to run a program that turns down the volume on your machine when the screen blanks, and turns it back up when the screen un-blanks. You could do that by running a Perl program like the following in the background. The following program tracks the output of the <i>-watch</i> command and reacts accordingly: </p>
<pre><code>
#!/ usr / bin / perl
my $blanked = 0;
open(IN, "xscreensaver-command -watch |");
while (&lt;IN&gt;) {
    if (m / ^(BLANK | LOCK) /) {
        if (!$blanked) {
            system "sound-off";
            $blanked = 1;
        }
    }
    elsif(m / ^UNBLANK /)
    {
        system "sound-on";
        $blanked = 0;
    }
}
</code></pre>
<p> Note that LOCK might come either with or without a preceding BLANK (depending on whether the lock-timeout is non-zero), so the above program keeps track of both of them.</dl>
<h2>STOPPING GRAPHICS</h2>
<p> If xscreensaver is running, but you want it to stop running screen hacks (e.g., if you are logged in remotely, and you want the console to remain locked but just be black, with no graphics processes running) you can accomplish that by simply powering down the monitor remotely. In a minute or so, xscreensaver will notice that the monitor is off, and will stop running screen hacks. You can power off the monitor like so: </p>
<pre>
xset dpms force off
</pre>
<p> See the <code><a href="/docs/linux/man/1-xset/">xset</a></code>(1) manual for more info. </p>
<p> You can also use <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1) to make the monitor power down after a few hours, meaning that xscreensaver will run graphics until it has been idle for the length of time you specified; and after that, the monitor will power off, and screen hacks will stop being run.</p>
<h2>DIAGNOSTICS</h2>
<p> If an error occurs while communicating with the <i>xscreensaver</i> daemon, or if the daemon reports an error, a diagnostic message will be printed to stderr, and <i>xscreensaver-command</i> will exit with a non-zero value. If the command is accepted, an indication of this will be printed to stdout, and the exit value will be zero.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the host and display number of the screen whose saver is to be manipulated.</p>
<dt><code>PATH</code></p>
<dd> to find the executable to restart (for the <i>-restart</i> command). Note that this variable is consulted in the environment of the <i>xscreensaver</i> process, not the <i>xscreensaver-command</i> process.</dl>
<h2>UPGRADES</h2>
<p> The latest version of <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) and related tools can always be found at <a rel="nofollow" href="https://www.jwz.org/xscreensaver/">https://www.jwz.org/xscreensaver/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), <code><a href="/docs/linux/man/1-xset/">xset</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1992-2013 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 13-aug-1992. </p>
<p> Please let me know if you find any bugs or make any improvements. </p>
<h2>Index</h2>
