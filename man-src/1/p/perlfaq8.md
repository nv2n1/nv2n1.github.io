---
title: "perlfaq8(1)"
name: "perlfaq8"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq8/"
description: "perlfaq8 – System Interaction"
---

<h2 class="name">NAME</h2>
<p> perlfaq8 &#8211; System Interaction </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section of the Perl <font SIZE="-1">FAQ</font> covers questions involving operating system interaction. Topics include interprocess communication (<font SIZE="-1">IPC</font>), control over the user-interface (keyboard, screen and pointing devices), and most anything else not related to data manipulation. </p>
<p> Read the FAQs and documentation specific to the port of perl to your operating system (eg, perlvms, perlplan9, &#8230;). These should contain more detailed information on the vagaries of your perl.</p>
<h3>How do I find out which operating system I&#8217;m running under?</h3>
<p> The <tt>$^O</tt> variable (<tt>$OSNAME</tt> if you use <tt>&quot;English&quot;</tt>) contains an indication of the name of the operating system (not its release number) that your perl binary was built for.</p>
<h3>How come <code>exec()</code> doesn&#8217;t return?</h3>
<p> (contributed by brian d foy) </p>
<p> The <tt>&quot;exec&quot;</tt> function&#8217;s job is to turn your process into another command and never to return. If that&#8217;s not what you want to do, don&#8217;t use <tt>&quot;exec&quot;</tt>. :) </p>
<p> If you want to run an external command and still keep your Perl process going, look at a piped <tt>&quot;open&quot;</tt>, <tt>&quot;fork&quot;</tt>, or <tt>&quot;system&quot;</tt>.</p>
<h3>How do I do fancy stuff with the keyboard/screen/mouse?</h3>
<p> How you access/control keyboards, screens, and pointing devices (&#8220;mice&#8221;) is system-dependent. Try the following modules:</p>
<dl>
<dt>Keyboard</p>
<dd>
<pre>
    Term::Cap               Standard perl distribution
    Term::ReadKey           CPAN
    Term::ReadLine::Gnu     CPAN
    Term::ReadLine::Perl    CPAN
    Term::Screen            CPAN
</pre>
<dt>Screen</p>
<dd>
<pre>
    Term::Cap               Standard perl distribution
    Curses                  CPAN
    Term::ANSIColor         CPAN
</pre>
<dt>Mouse</p>
<dd>
<pre>
    Tk                      CPAN
    Wx                      CPAN
    Gtk2                    CPAN
    Qt4                     kdebindings4 package
</pre>
</dl>
<p> Some of these specific cases are shown as examples in other answers in this section of the perlfaq.</p>
<h3>How do I print something out in color?</h3>
<p> In general, you don&#8217;t, because you don&#8217;t know whether the recipient has a color-aware display device. If you know that they have an <font SIZE="-1">ANSI</font> terminal that understands color, you can use the Term::ANSIColor module from <font SIZE="-1">CPAN:</font> </p>
<pre><code>
use Term::ANSIColor;
print color("red"), "Stop!
", color("reset");
print color("green"), "Go!
", color("reset");
</code></pre>
<p> Or like this: </p>
<p>use Term::ANSIColor qw(<br />
    : constants);<br />
print RED, &#8220;Stop!
&#8221;, RESET;<br />
print GREEN, &#8220;Go!
&#8221;, RESET;</p>
<h3>How do I read just one key without waiting for a return key?</h3>
<p> Controlling input buffering is a remarkably system-dependent matter. On many systems, you can just use the <code>stty</code> command as shown in &#8220;getc&#8221; in perlfunc, but as you see, that&#8217;s already getting you into portability snags. </p>
<p>open(TTY, &#8220;+&lt;/dev/tty&#8221;) or die &#8220;no tty: $!&#8221;;<br />
system &#8220;stty  cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&#8221;;<br />
$key = getc(TTY);<br />
#perhaps this works<br />
#OR ELSE<br />
    sysread(TTY, $key, 1);<br />
#probably this does<br />
    system &#8220;stty -cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&#8221;;</p>
<p> The Term::ReadKey module from <font SIZE="-1">CPAN</font> offers an easy-to-use interface that should be more efficient than shelling out to <code>stty</code> for each key. It even includes limited support for Windows. </p>
<p>use Term::ReadKey;<br />
ReadMode(&#8216;cbreak&#8217;);<br />
$key = ReadKey(0);<br />
ReadMode(&#8216;normal&#8217;);</p>
<p> However, using the code requires that you have a working C compiler and can use it to build and install a <font SIZE="-1">CPAN</font> module. Here&#8217;s a solution using the standard <font SIZE="-1">POSIX</font> module, which is already on your system (assuming your system supports <font SIZE="-1">POSIX</font>). </p>
<p>use HotKey;<br />
$key = readkey();</p>
<p> And here&#8217;s the <tt>&quot;HotKey&quot;</tt> module, which hides the somewhat mystifying calls to manipulate the <font SIZE="-1">POSIX</font> termios structures. </p>
<p>#HotKey.pm<br />
package HotKey;<br />
use strict;<br />
use warnings;<br />
use parent &#8216;Exporter&#8217;;<br />
our @EXPORT = qw(cbreak cooked readkey);<br />
use POSIX qw(<br />
    : termios_h);<br />
my($term, $oterm, $echo, $noecho, $fd_stdin);<br />
$fd_stdin = fileno(STDIN);<br />
$term = POSIX::Termios-&gt;new ();<br />
$term-&gt;getattr($fd_stdin);<br />
$oterm = $term-&gt;getlflag();<br />
$echo = ECHO | ECHOK | ICANON;<br />
$noecho = $oterm &amp; ~$echo;<br />
sub cbreak<br />
{<br />
    $term-&gt;setlflag($noecho);<br />
#ok, so i don&#8217;t want echo either $term-&gt;setcc(VTIME, 1);<br />
    $term-&gt;setattr($fd_stdin, TCSANOW);<br />
}<br />
sub cooked<br />
{<br />
    $term-&gt;setlflag($oterm);<br />
    $term-&gt;setcc(VTIME, 0);<br />
    $term-&gt;setattr($fd_stdin, TCSANOW);<br />
}<br />
sub readkey<br />
{<br />
    my $key = &#8221;;<br />
    cbreak();<br />
    sysread(STDIN, $key, 1);<br />
    cooked();<br />
    return $key;<br />
}<br />
END<br />
{<br />
    cooked()<br />
}<br />
1;</p>
<h3>How do I check whether input is ready on the keyboard?</h3>
<p> The easiest way to do this is to read a key in nonblocking mode with the Term::ReadKey module from <font SIZE="-1">CPAN,</font> passing it an argument of -1 to indicate not to block: </p>
<p>use Term::ReadKey;<br />
ReadMode(&#8216;cbreak&#8217;);<br />
if (defined(my $char = ReadKey(-1))) {<br />
#input was waiting and it was $char<br />
} else {<br />
#no input was waiting<br />
}<br />
ReadMode(&#8216;normal&#8217;);<br />
#restore normal tty settings</p>
<h3>How do I clear the screen?</h3>
<p> (contributed by brian d foy) </p>
<p> To clear the screen, you just have to print the special sequence that tells the terminal to clear the screen. Once you have that sequence, output it when you want to clear the screen. </p>
<p> You can use the Term::ANSIScreen module to get the special sequence. Import the <tt>&quot;cls&quot;</tt> function (or the <tt>&quot;:screen&quot;</tt> tag): </p>
<p>use Term::ANSIScreen qw(cls);<br />
my $clear_screen = cls();<br />
print $clear_screen;</p>
<p> The Term::Cap module can also get the special sequence if you want to deal with the low-level details of terminal control. The <tt>&quot;Tputs&quot;</tt> method returns the string for the given capability: </p>
<p>use Term::Cap;<br />
my $terminal = Term::Cap-&gt;Tgetent({OSPEED = &gt; 9600});<br />
my $clear_screen = $terminal-&gt;Tputs(&#8216;cl&#8217;);<br />
print $clear_screen;</p>
<p> On Windows, you can use the Win32::Console module. After creating an object for the output filehandle you want to affect, call the <tt>&quot;Cls&quot;</tt> method: </p>
<p>Win32::Console;<br />
my $OUT = Win32::Console-&gt;new (STD_OUTPUT_HANDLE);<br />
my $clear_string = $OUT-&gt;Cls;<br />
print $clear_screen;</p>
<p> If you have a command-line program that does the job, you can call it in backticks to capture whatever it outputs so you can use it later: </p>
<pre>
    my $clear_string = `clear`;
    print $clear_string;
</pre>
<h3>How do I get the screen size?</h3>
<p> If you have Term::ReadKey module installed from <font SIZE="-1">CPAN,</font> you can use it to fetch the width and height in characters and in pixels: </p>
<p>use Term::ReadKey;<br />
my($wchar, $hchar, $wpixels, $hpixels) = GetTerminalSize();</p>
<p> This is more portable than the raw <tt>&quot;ioctl&quot;</tt>, but not as illustrative: </p>
<p>require &#8216;./sys/ioctl.ph&#8217;;<br />
die &#8220;no TIOCGWINSZ &#8221; unless defined &amp;TIOCGWINSZ;<br />
open(my $tty_fh, &#8220;+&lt;/dev/tty&#8221;) or die &#8220;No tty: $!&#8221;;<br />
unless(ioctl($tty_fh, &amp;TIOCGWINSZ, $winsize =&#8221;))<br />
{<br />
    die sprintf &#8220;$0: ioctl TIOCGWINSZ (%08x: $!)
&#8221;, &amp;TIOCGWINSZ;<br />
}<br />
my($row, $col, $xpixel, $ypixel) = unpack(&#8216;S4&#8217;, $winsize);<br />
print &#8220;(row,col) = ($row,$col)&#8221;;<br />
print &#8221;  (xpixel,ypixel) = ($xpixel,$ypixel)&#8221; if $xpixel || $ypixel;<br />
print &#8220;
&#8221;;</p>
<h3>How do I ask the user for a password?</h3>
<p> (This question has nothing to do with the web. See a different <font SIZE="-1">FAQ</font> for that.) </p>
<p> There&#8217;s an example of this in &#8220;crypt&#8221; in perlfunc. First, you put the terminal into &#8220;no echo&#8221; mode, then just read the password normally. You may do this with an old-style <tt>&quot;ioctl()&quot;</tt> function, <font SIZE="-1">POSIX</font> terminal control (see <font SIZE="-1">POSIX</font> or its documentation the Camel Book), or a call to the <code>stty</code> program, with varying degrees of portability. </p>
<p> You can also do this for most systems using the Term::ReadKey module from <font SIZE="-1">CPAN,</font> which is easier to use and in theory more portable. </p>
<p>use Term::ReadKey;<br />
ReadMode(&#8216;noecho&#8217;);<br />
my $password = ReadLine(0);</p>
<h3>How do I read and write the serial port?</h3>
<p> This depends on which operating system your program is running on. In the case of Unix, the serial ports will be accessible through files in <tt>&quot;/dev&quot;</tt>; on other systems, device names will doubtless differ. Several problem areas common to all device interaction are the following:</p>
<dl>
<dt>lockfiles</p>
<dd> Your system may use lockfiles to control multiple access. Make sure you follow the correct protocol. Unpredictable behavior can result from multiple processes reading from one device.</p>
<dt>open mode</p>
<dd> If you expect to use both read and write operations on the device, you&#8217;ll have to open it for update (see &#8220;open&#8221; in perlfunc for details). You may wish to open it without running the risk of blocking by using <tt>&quot;sysopen()&quot;</tt> and <tt>&quot;O_RDWR|O_NDELAY|O_NOCTTY&quot;</tt> from the Fcntl module (part of the standard perl distribution). See &#8220;sysopen&#8221; in perlfunc for more on this approach.</p>
<dt>end of line</p>
<dd> Some devices will be expecting a &#8220;&#8221; at the end of each line rather than a &#8220;
&#8221;. In some ports of perl, &#8220;&#8221; and &#8220;
&#8221; are different from their usual (Unix) <font SIZE="-1">ASCII</font> values of &#8220;&#8221; and &#8220;
&#8221;. You may have to give the numeric values you want directly, using octal (&#8220;&#8221;), hex (&#8220;0x0D&#8221;), or as a control-character specification (&#8220;
