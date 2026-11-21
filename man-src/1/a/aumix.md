---

title: "aumix(1)"
name: "aumix"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aumix/"
description: "aumix – adjust audio mixer"
---

<p> <code>aumix</code> &#8211; adjust audio mixer </p>
<p> [-&lt;channel option&gt;[[+|-][&lt;amount&gt;]]|&lt;level&gt;|R[ecord]|P[lay]|q[uery]] [-dhILqS] [-f &lt;rc file&gt;][-C &lt;color scheme file&gt;]</p>
<p> This program adjusts the settings of an audio mixing device. It can be used from the command line, in scripts, or interactively with the keyboard or mouse.</p>
<h2>OPTIONS</h2>
<h3>CHANNEL OPTIONS</h3>
<dl>
<dt><code>-v</code></dt>
<dd> main volume</dd>
<dt><code>-b</code></dt>
<dd> bass</dd>
<dt><code>-c</code></dt>
<dd> CD</dd>
<dt><code>-i</code></dt>
<dd> line in</dd>
<dt><code>-l</code></dt>
<dd> line</dd>
<dt><code>-m</code></dt>
<dd> microphone</dd>
<dt><code>-o</code></dt>
<dd> line out</dd>
<dt><code>-p</code></dt>
<dd> PC speaker</dd>
<dt><code>-s</code></dt>
<dd> synthesizer</dd>
<dt><code>-t</code></dt>
<dd> treble</dd>
<dt><code>-w</code></dt>
<dd> PCM</dd>
<dt><code>-x</code></dt>
<dd> imix</dd>
<dt><code>-1</code></dt>
<dd> line 1</dd>
<dt><code>-2</code></dt>
<dd> line 2</dd>
<dt><code>-3</code></dt>
<dd> line 3</dd></dl>
<p> For each channel, <code>q</code> queries, <code>+</code> and <code>&#8211;</code> increment and decrement by one, or an amount if one is specified. If no <code>+</code> or <code>&#8211;</code> is given after the channel option, a number sets a specific level (monophonically).</p>
<h3>OTHER OPTIONS</h3>
<dl>
<dt><code>-C </code><i>color_scheme_file</i></dt>
<dd> specify the name of a file containing a color scheme. This implies &#8211;<code>I</code></dd>
<dt><code>-d </code><i>device_file</i></dt>
<dd> specify the name of the mixer device (default is /dev/mixer</dd>
<dt><code>-f </code><i>rc_file</i></dt>
<dd> specify file for saving and loading settings</dd>
<dt><code>-h</code></dt>
<dd> display information on usage</dd>
<dt><code>-I</code></dt>
<dd> run interactively, using the full-screen ncurses-based interface. This is the default if no options are given, but must be specified in order to have go into interactive mode after doing things non-interactively.</dd>
<dt><code>-L</code></dt>
<dd> load settings from $HOME/.aumixrc or /etc/aumixrc if the former is inaccessible</dd>
<dt><code>-q</code></dt>
<dd> query all devices and print their settings</dd>
<dt><code>-S</code></dt>
<dd> save settings to $HOME/.aumixrc</dd></dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<blockquote>
<pre>
aumix -q -v75 -m 0 -c R -c+10 -m q
</pre>
</blockquote>
<p> prints all settings, sets volume to 75%, sets microphone to 0, sets CD to record, increases the CD level by ten (both left and right), and prints the new settings for the microphone. </p>
<p> The .aumixrc file containing: </p>
<blockquote>
<pre>
vol:60:60
wait:5000
vol:50:50
</pre>
</blockquote>
<p> sets the volume to 60%, waits five seconds, then reduces the volume to 50%. Note that &quot;wait&quot; lines will not be saved by aumix. They must be added by hand.</p>
<h2>INTERACTIVE USE</h2>
<p> If no options are given on the command line, and is compiled with ncurses, it will run interactively.</p>
<h3>LAYOUT</h3>
<p> The left bank of controls is used for adjusting levels; the right bank is for adjusting balance. Mixing channels not supported by your hardware will not be shown. Mixing channels which are stereo-capable will have balance controls.</p>
<h3>KEYS</h3>
<p> The following keys control in interactive mode:</p>
<dl>
<dt><code>page up, page down, up and down cursor</code></dt>
<dd> select a new control.</dd>
<dt><code>Tab, Enter, &lt;, &gt;, comma and period</code></dt>
<dd> toggle between level and balance controls</dd>
<dt><code>+ , &#8211; , [ , ] , left and right cursor and digits</code></dt>
<dd> adjust the setting of the current device. The <code>+</code> and right cursor keys increase the level by 3%; the <code>&#8211;</code> and left cursor keys decrease it by the same amount. The <code>[</code> key sets it to 0% and <code>]</code> sets it to 100%. The digits <code>1</code> to <code>9</code> set it to 10% through 90%. The same keys work analogously on the balance controls.</dd>
<dt><code>Space</code></dt>
<dd> toggles between record and play for controls which are capable of this.</dd>
<dt><code>|</code></dt>
<dd> centers the balance of the current device.</dd>
<dt><code>K or k</code></dt>
<dd> show a description of the functions of keys</dd>
<dt><code>L or l</code></dt>
<dd> load settings from $HOME/.aumixrc falling back to /etc/aumixrc</dd>
<dt><code>M or m</code></dt>
<dd> mute or unmute</dd>
<dt><code>O or o</code></dt>
<dd> &#8220;only&#8221; mute all channels but the current one</dd>
<dt><code>S or s</code></dt>
<dd> save settings to the rc file</dd>
<dt><code>U or u</code></dt>
<dd> undo any muting</dd>
<dt><code>Q or q</code></dt>
<dd> end the program</dd>
<dt><code>^L</code></dt>
<dd> refresh screen</dd></dl>
<p> ^Z, ^D and ^C also have their normal function (the screen is refreshed when is brought to the foreground).</p>
<h3>MOUSE</h3>
<p> In interactive mode, can accept input from the mouse if <a href="/docs/linux/man/8-gpm/">gpm</a>(8) is running and is compiled with <a href="/docs/linux/man/8-gpm/">gpm</a>(8) support. If gpm is not running but gpm support is included, the message `mouse&#8217; off will appear at the top of the screen, and only keyboard input will be accepted. With <a href="/docs/linux/man/8-gpm/">gpm</a>(8) running, most functions can be performed through the mouse. The mouse is active whenever one of its buttons is held down. While active, it works in the following ways: </p>
<ul>
<li> over a control track, it sets the control to match the position of the mouse cursor.
<li> over a record/play indicator, it toggles the record/play state.
<li> over the `Quit&#8217; , `Load&#8217; , `Save&#8217; , `Keys&#8217; , `Mute&#8217; , `Only&#8217; , or `Undo&#8217; labels at the top of the screen, it causes those actions to take place. </ul>
<h2>ENVIRONMENT</h2>
<p> The <code>HOME</code> variable is used. When is compiled with GTK+ support, <code>DISPLAY</code> is checked, and if set is used. <code>LANG</code> is used when the ncurses screen is displayed.</p>
<h2>FILES</h2>
<p> Saved settings for the mixer are kept in the /etc/aumixrc and $HOME/.aumixrc files, but can be kept anywhere if specified explicitly. Color schemes are normally kept in the directory given by <code>DATADIR</code> at compilation time, but are preferentially loaded from the current directory and can be kept anywhere so long as the path to them is specified. The format of these files is: </p>
<blockquote><p> <i>item</i> <i>foreground</i> <i>background</i> </p></blockquote>
<p> where <i>item</i> is one of `active&#8217; , `axis&#8217; , `handle&#8217; , `hotkey&#8217; , `menu&#8217; , `play&#8217; , `record&#8217; , or `track&#8217; and <i>foreground</i> and <i>background</i> are one of `black&#8217; , `red&#8217; , `green&#8217; , `yellow&#8217; , `blue&#8217; , `magenta&#8217; , `cyan&#8217; , or `white&#8217; The words should be separated by whitespace and can be upper-, lower-, or mixed-case. Lines not matching all these conditions are ignored. Some samples of color schemes are provided, named after the sort of terminal where they should be most suitable. </p>
<p> If either foreground or background is given as `-&#8216; , then the default color for that is used. The defaults are a white foreground and black background. </p>
<p> An xpm icon is provided.</p>
<h2>VERSION</h2>
<p> This page corresponds to version 2.7.</p>
<h2>BUGS</h2>
<p> Suspending with ^Z may make the terminal difficult to use. </p>
<p> Please send bug reports and other correspondence to the mailing list. Past messages may be read at </p>
<pre>
&lt;URL:<a rel="nofollow" href="http://lilax.org/wws/arc/aumix-l">http://lilax.org/wws/arc/aumix-l</a>&gt;
</pre>
<p> and you may wish to join the list via </p>
<pre>
&lt;URL:<a rel="nofollow" href="http://lilax.org/wws/info/aumix-l">http://lilax.org/wws/info/aumix-l</a>&gt;
</pre>
<p> or by sending a message with just `subscribe&#8217; in the subject to Aq aumix-l-request [at] lilax.org . To post without subscribing, omit &quot;-request&quot; from the address. </p>
<p> Information such as the version of aumix, the architecture and operating system, and the model of sound hardware is sometimes needed to diagnose problems, so it is best if you include such details in any bug reports.</p>
<h2>SEE ALSO</h2>
<p> gpm(1), moused(8), sb(4), <a href="/docs/linux/man/1-xaumix/">xaumix</a>(1) </p>
