---
title: "beep(1)"
name: "beep"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beep/"
description: "beep – beep the pc speaker any number of ways"
---

<h2>NAME</h2>
<p> beep &#8211; beep the pc speaker any number of ways</p>
<h2>SYNOPSIS</h2>
<p> <code>beep</code> [-f N] [-l N] [-r N] [-d N] [-D N] [-s] [-c]</p>
<dl>
<dt> <code>beep</code> [ OPTIONS ] [-n] [&#8211;new] [ OPTIONS ]</p>
<dt> <code>beep</code> [-h] [&#8211;help]</p>
<dt> <code>beep</code> [-v] [-V] [&#8211;version]</dl>
<h2>DESCRIPTION</h2>
<p> <code>beep</code> allows the user to control the pc-speaker with precision, allowing different sounds to indicate different events. While it can be run quite happily on the command line, it&#8217;s intended place of residence is within shell/perl scripts, notifying the user when something interesting occurs. Of course, it has no notion of what&#8217;s interesting, but it&#8217;s real good at that notifying part. </p>
<dd>All options have default values, meaning that just typing &#8216;<code>beep</code>&#8216; will work. If an option is specified more than once on the command line, subsequent options override their predecessors. So &#8216;<code>beep</code> -f 200 -f 300&#8242; will beep at 300Hz.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> N</p>
<dd> beep at N Hz, where 0 &lt; N &lt; 20000. As a general ballpark, the regular terminal beep is around 750Hz. N is not, incidentally, restricted to whole numbers.</p>
<dt><code>-l</code> N</p>
<dd> beep for N milliseconds.</p>
<dt><code>-r</code> N</p>
<dd> specify the number of repetitions (defaults to 1).</p>
<dt><code>-d</code> N, <code>-D</code> N</p>
<dd> specify a delay of N milliseconds between repetitions. Use of -d specifies that this delay should only occur <i>between</i> beeps, that is, it should not occur after the last repetition. -D indicates that the delay should occur after every repetition, including the last. Normally, -d is what you want, but if, for example, you are stringing several <code>beep</code> commands together to play the star wars anthem, you may want control over every delay.</p>
<dt><code>-n</code>, <code>&#8211;new</code></p>
<dd> this option allows you to break the command line up into specifying multiple beeps. Each time this option is used, beep starts treating all further arguments as though they were for a new beep. So for example: </p>
<p> <code>beep</code> -f 1000 -n -f 2000 -n -f 1500 </p>
<p> would produce a sequence of three beeps, the first with a frequency of 1000Hz (and otherwise default values), then a second beep with a frequency of 2000Hz (again, with things like delay and reps being set to their defaults), then a third beep, at 1500Hz. This is different from specifying a -r value, since -r repeats the same beep multiple times, whereas -n allows you to specify different beeps. After a -n, the new beep is created with all the default values, and any of these can be specified without altering values for preceeding (or later) beeps. See the <code>EXAMPLES</code> section if this managed to confuse you.</p>
<dt><code>-s</code>, <code>-c</code></p>
<dd> these options put <code>beep</code> into input-processing mode. -s tells <code>beep</code> to read from stdin, and beep after each newline, and -c tells it to do so after every character. In both cases, the program will also echo the input back out to stdout, which makes it easy to slip <code>beep</code> into a text-processing pipeline, see the <code>EXAMPLES</code> section.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display usage info and exit</p>
<dt><code>-v</code>, <code>-V</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>At its simplest (yet still effective)</p>
<dd>
<p> <code>beep</code></p>
<dt>A more interesting standalone setup</p>
<dd>
<p> <code>beep</code> -f 300.7 -r 2 -d 100 -l 400</p>
<dt>As part of a log-watching pipeline</p>
<dd>
<p> tail -f /var/log/xferlog | grep &#8216;passwd&#8217; | <code>beep</code> -f 1000 -r 5 -s</p>
<dt>When using -c mode, I recommend using a short -D, and a shorter -l, so that the beeps don&#8217;t blur together. Something like this will get you a cheesy 1970&#8217;s style beep-as-you-type-each-letter effect</p>
<dd>
<p> cat file | <code>beep</code> -c -f 400 -D 50 -l 10 </p>
<dt>A highly contrived example of -n/&#8211;new usage</p>
<dd>
<p> <code>beep</code> -f 1000 -r 2 -n -r 5 -l 10 &#8211;new </p>
<p> will produce first two 1000Hz beeps, then 5 beeps at the default tone, but only 10ms long each, followed by a third beep using all the default settings (since none are specified).</dl>
<h2>IOCTL WACKINESS</h2>
<p> Some users will encounter a situation where beep dies with a complaint from ioctl(). The reason for this, as Peter Tirsek was nice enough to point out to me, stems from how the kernel handles beep&#8217;s attempt to poke at (for non-programmers: ioctl is a sort of catch-all function that lets you poke at things that have no other predefined poking-at mechanism) the tty, which is how it beeps. The short story is, the kernel checks that either: </p>
<p> &#8211; you are the superuser </p>
<p> &#8211; you own the current tty </p>
<p> What this means is that root can always make beep work (to the best of my knowledge!), and that any local user can make beep work, BUT a non-root remote user cannot use beep in it&#8217;s natural state. What&#8217;s worse, an xterm, or other x-session counts, as far as the kernel is concerned, as &#8216;remote&#8217;, so beep won&#8217;t work from a non-priviledged xterm either. I had originally chalked this up to a bug, but there&#8217;s actually nothing I can do about it, and it really is a Good Thing that the kernel does things this way. There is also a solution. </p>
<p> By default beep is not installed with the suid bit set, because that would just be zany. On the other hand, if you do make it suid root, all your problems with beep bailing on ioctl calls will magically vanish, which is pleasant, and the only reason not to is that any suid program is a potential security hole. Conveniently, beep is very short, so auditing it is pretty straightforward. </p>
<p> Decide for yourself, of course, but it looks safe to me &#8211; there&#8217;s only one buffer and fgets doesn&#8217;t let it overflow, there&#8217;s only one file opening, and while there is a potential race condition there, it&#8217;s with /dev/console. If someone can exploit this race by replacing /dev/console, you&#8217;ve got bigger problems. :) </p>
<p> So the quick, only, and likely safe solution if beep is not beeping when you want it to is (as root): </p>
<p> # chmod 4755 /usr/bin/beep </p>
<p> (or wherever you put it) </p>
<p> The one snag is that this will give any little nitwit the ability to run beep successfully &#8211; make sure this is what you want. If it isn&#8217;t, a slightly more complex fix would be something like: </p>
<p> # chgrp beep /usr/bin/beep </p>
<p> # chmod 4750 /usr/bin/beep </p>
<p> and then add only beep-worthy users to the &#8216;beep&#8217; group.</p>
<h2>FREQUENCY TABLE</h2>
<p> Several people have asked for some basic help translating music notes to frequencies. There are a lot of music notes, and several tables online will give you translations, but here are <i>approximate</i> numbers for the octave of middle C, to get you started. </p>
<p> Note<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Frequency</p>
<pre>
C               261.6
C#              277.2
D               293.7
D#              311.1
E               329.6
F               349.2
F#              370.0
G               392.0
G#              415.3
A               440.0
A#              466.2
B               493.9
C               523.2
</pre>
<h2>BUGS</h2>
<p> None that I&#8217;m aware of, though see the <code>IOCTL WACKINESS</code> section.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;johnath [at] johnath.com&gt;</p>
<h2>AUTHOR</h2>
<p> This program was written by Johnathan Nightingale (johnath [at] johnath.com) and is distributed under the GNU General Public License. For more contributing information, check the source, and past contributors can be found in CREDITS. </p>
<h2>Index</h2>
