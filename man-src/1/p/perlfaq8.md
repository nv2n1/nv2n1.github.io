---
title: "perlfaq8(1)"
name: "perlfaq8"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq8/"
description: "perlfaq8 – System Interaction"
---
<h2>VERSION</h2>
<p> version 5.20190126  </p>
<h2>DESCRIPTION</h2>
<p> This section of the Perl <font SIZE="-1">FAQ</font> covers questions involving operating system interaction. Topics include interprocess communication (<font SIZE="-1">IPC</font>), control over the user-interface (keyboard, screen and pointing devices), and most anything else not related to data manipulation. </p>
<p> Read the FAQs and documentation specific to the port of perl to your operating system (eg, perlvms, perlplan9, ...). These should contain more detailed information on the vagaries of your perl.  </p>
<h3>How do I find out which operating system I'm running under?</h3>
<p> The <code>$^O</code> variable (<code>$OSNAME</code> if you use <code>&quot;English&quot;</code>) contains an indication of the name of the operating system (not its release number) that your perl binary was built for.  </p>
<code></code><h3>How come exec() doesn't return?</h3>
<p> (contributed by brian d foy) </p>
<p> The <code>&quot;exec&quot;</code> function&#8217;s job is to turn your process into another command and never to return. If that&#8217;s not what you want to do, don&#8217;t use <code>&quot;exec&quot;</code>. :) </p>
<p> If you want to run an external command and still keep your Perl process going, look at a piped <code>&quot;open&quot;</code>, <code>&quot;fork&quot;</code>, or <code>&quot;system&quot;</code>.  </p>
<h3>How do I do fancy stuff with the keyboard/screen/mouse?</h3>
<p> How you access/control keyboards, screens, and pointing devices (``mice&#8217;&#8216;) is system-dependent. Try the following modules: </p>
<dl>
<dt>Keyboard</dt>
<dd> <pre><code>    Term::Cap Standard perl distribution
    Term::ReadKey CPAN
    Term::ReadLine::Gnu CPAN
    Term::ReadLine::Perl CPAN
    Term::Screen CPAN
</code></pre>
 </dd>
<dt>Screen</dt>
<dd> <pre><code>    Term::Cap Standard perl distribution
    Curses CPAN
    Term::ANSIColor CPAN
</code></pre>
 </dd>
<dt>Mouse</dt>
<dd> <pre><code>    Tk CPAN
    Wx CPAN
    Gtk2 CPAN
    Qt4 kdebindings4 package
</code></pre>
 </dd></dl>
<p> Some of these specific cases are shown as examples in other answers in this section of the perlfaq.  </p>
<h3>How do I print something out in color?</h3>
<p> In general, you don&#8217;t, because you don&#8217;t know whether the recipient has a color-aware display device. If you know that they have an <font SIZE="-1">ANSI</font> terminal that understands color, you can use the Term::ANSIColor module from <font SIZE="-1">CPAN:</font> </p>
<pre><code>    use Term::ANSIColor;
    print color(&quot;red&quot;), &quot;Stop!\n&quot;, color(&quot;reset&quot;);
    print color(&quot;green&quot;), &quot;Go!\n&quot;, color(&quot;reset&quot;);
</code></pre>
<p> Or like this: </p>
<pre><code>    use Term::ANSIColor qw(:constants);
    print RED, &quot;Stop!\n&quot;, RESET;
    print GREEN, &quot;Go!\n&quot;, RESET;
</code></pre>
<h3>How do I read just one key without waiting for a return key?</h3>
<p> Controlling input buffering is a remarkably system-dependent matter. On many systems, you can just use the <code>stty</code> command as shown in ``getc&#8217;&#8216; in perlfunc, but as you see, that&#8217;s already getting you into portability snags. </p>
<pre><code>    open(TTY, &quot;+&lt;/dev/tty&quot;) or die &quot;no tty: $!&quot;;
    system &quot;stty cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&quot;;
    $key = getc(TTY); # perhaps this works
    # OR ELSE
    sysread(TTY, $key, 1); # probably this does
    system &quot;stty -cbreak &lt;/dev/tty &gt;/dev/tty 2&gt;&amp;1&quot;;
</code></pre>
<p> The Term::ReadKey module from <font SIZE="-1">CPAN</font> offers an easy-to-use interface that should be more efficient than shelling out to <code>stty</code> for each key. It even includes limited support for Windows. </p>
<pre><code>    use Term::ReadKey;
    ReadMode('cbreak');
    $key = ReadKey(0);
    ReadMode('normal');
</code></pre>
<p> However, using the code requires that you have a working C compiler and can use it to build and install a <font SIZE="-1">CPAN</font> module. Here&#8217;s a solution using the standard <font SIZE="-1">POSIX</font> module, which is already on your system (assuming your system supports <font SIZE="-1">POSIX</font>). </p>
<pre><code>    use HotKey;
    $key = readkey();
</code></pre>
<p> And here&#8217;s the <code>&quot;HotKey&quot;</code> module, which hides the somewhat mystifying calls to manipulate the <font SIZE="-1">POSIX</font> termios structures. </p>
<pre><code>    # HotKey.pm
    package HotKey;
    use strict;
    use warnings;
    use parent 'Exporter';
    our @EXPORT = qw(cbreak cooked readkey);
    use POSIX qw(:termios_h);
    my ($term, $oterm, $echo, $noecho, $fd_stdin);
    $fd_stdin = fileno(STDIN);
    $term = POSIX::Termios-&gt;new();
    $term-&gt;getattr($fd_stdin);
    $oterm = $term-&gt;getlflag();
    $echo = ECHO | ECHOK | ICANON;
    $noecho = $oterm &amp; ~$echo;
    sub cbreak {
        $term-&gt;setlflag($noecho); # ok, so i don't want echo either
        $term-&gt;setcc(VTIME, 1);
        $term-&gt;setattr($fd_stdin, TCSANOW);
    }
    sub cooked {
        $term-&gt;setlflag($oterm);
        $term-&gt;setcc(VTIME, 0);
        $term-&gt;setattr($fd_stdin, TCSANOW);
    }
    sub readkey {
        my $key = '';
        cbreak();
        sysread(STDIN, $key, 1);
        cooked();
        return $key;
    }
    END { cooked() }
    1;
</code></pre>
<h3>How do I check whether input is ready on the keyboard?</h3>
<p> The easiest way to do this is to read a key in nonblocking mode with the Term::ReadKey module from <font SIZE="-1">CPAN,</font> passing it an argument of -1 to indicate not to block: </p>
<pre><code>    use Term::ReadKey;
    ReadMode('cbreak');
    if (defined (my $char = ReadKey(-1)) ) {
        # input was waiting and it was $char
    } else {
        # no input was waiting
    }
    ReadMode('normal'); # restore normal tty settings
</code></pre>
<h3>How do I clear the screen?</h3>
<p> (contributed by brian d foy) </p>
<p> To clear the screen, you just have to print the special sequence that tells the terminal to clear the screen. Once you have that sequence, output it when you want to clear the screen. </p>
<p> You can use the Term::ANSIScreen module to get the special sequence. Import the <code>&quot;cls&quot;</code> function (or the <code>&quot;:screen&quot;</code> tag): </p>
<pre><code>    use Term::ANSIScreen qw(cls);
    my $clear_screen = cls();
    print $clear_screen;
</code></pre>
<p> The Term::Cap module can also get the special sequence if you want to deal with the low-level details of terminal control. The <code>&quot;Tputs&quot;</code> method returns the string for the given capability: </p>
<pre><code>    use Term::Cap;
    my $terminal = Term::Cap-&gt;Tgetent( { OSPEED =&gt; 9600 } );
    my $clear_screen = $terminal-&gt;Tputs('cl');
    print $clear_screen;
</code></pre>
<p> On Windows, you can use the Win32::Console module. After creating an object for the output filehandle you want to affect, call the <code>&quot;Cls&quot;</code> method: </p>
<pre><code>    Win32::Console;
    my $OUT = Win32::Console-&gt;new(STD_OUTPUT_HANDLE);
    my $clear_string = $OUT-&gt;Cls;
    print $clear_screen;
</code></pre>
<p> If you have a command-line program that does the job, you can call it in backticks to capture whatever it outputs so you can use it later: </p>
<pre><code>    my $clear_string = `clear`;
    print $clear_string;
</code></pre>
<h3>How do I get the screen size?</h3>
<p> If you have Term::ReadKey module installed from <font SIZE="-1">CPAN,</font> you can use it to fetch the width and height in characters and in pixels: </p>
<pre><code>    use Term::ReadKey;
    my ($wchar, $hchar, $wpixels, $hpixels) = GetTerminalSize();
</code></pre>
<p> This is more portable than the raw <code>&quot;ioctl&quot;</code>, but not as illustrative: </p>
<pre><code>    require './sys/ioctl.ph';
    die &quot;no TIOCGWINSZ &quot; unless defined &amp;TIOCGWINSZ;
    open(my $tty_fh, &quot;+&lt;/dev/tty&quot;) or die &quot;No tty: $!&quot;;
    unless (ioctl($tty_fh, &amp;TIOCGWINSZ, $winsize='')) {
        die sprintf &quot;$0: ioctl TIOCGWINSZ (%08x: $!)\n&quot;, &amp;TIOCGWINSZ;
    }
    my ($row, $col, $xpixel, $ypixel) = unpack('S4', $winsize);
    print &quot;(row,col) = ($row,$col)&quot;;
    print &quot; (xpixel,ypixel) = ($xpixel,$ypixel)&quot; if $xpixel || $ypixel;
    print &quot;\n&quot;;
</code></pre>
<h3>How do I ask the user for a password?</h3>
<p> (This question has nothing to do with the web. See a different <font SIZE="-1">FAQ</font> for that.) </p>
<p> There&#8217;s an example of this in ``crypt&#8217;&#8216; in perlfunc. First, you put the terminal into ``no echo&#8217;&#8216; mode, then just read the password normally. You may do this with an old-style <code>&quot;ioctl()&quot;</code> function, <font SIZE="-1">POSIX</font> terminal control (see <font SIZE="-1">POSIX</font> or its documentation the Camel Book), or a call to the <code>stty</code> program, with varying degrees of portability. </p>
<p> You can also do this for most systems using the Term::ReadKey module from <font SIZE="-1">CPAN,</font> which is easier to use and in theory more portable. </p>
<pre><code>    use Term::ReadKey;
    ReadMode('noecho');
    my $password = ReadLine(0);
</code></pre>
<h3>How do I read and write the serial port?</h3>
<p> This depends on which operating system your program is running on. In the case of Unix, the serial ports will be accessible through files in <code>&quot;/dev&quot;</code>; on other systems, device names will doubtless differ. Several problem areas common to all device interaction are the following: </p>
<dl>
<dt>lockfiles</dt>
<dd> <p> Your system may use lockfiles to control multiple access. Make sure you follow the correct protocol. Unpredictable behavior can result from multiple processes reading from one device. </p>
 </dd>
<dt>open mode</dt>
<dd> <p> If you expect to use both read and write operations on the device, you&#8217;ll have to open it for update (see ``open&#8217;&#8216; in perlfunc for details). You may wish to open it without running the risk of blocking by using <code>&quot;sysopen()&quot;</code> and <code>&quot;O_RDWR|O_NDELAY|O_NOCTTY&quot;</code> from the Fcntl module (part of the standard perl distribution). See ``sysopen&#8217;&#8216; in perlfunc for more on this approach. </p>
 </dd>
<dt>end of line</dt>
<dd> <p> Some devices will be expecting a ``\r&#8217;&#8216; at the end of each line rather than a ``\n&#8217;&#8216;. In some ports of perl, ``\r&#8217;&#8216; and ``\n&#8217;&#8216; are different from their usual (Unix) <font SIZE="-1">ASCII</font> values of ``\015&#8217;&#8216; and ``\012&#8217;&#8216;. You may have to give the numeric values you want directly, using octal (``\015&#8217;&#8216;), hex (``0x0D&#8217;&#8216;), or as a control-character specification (``\cM&#8217;&#8216;). </p>
<pre><code>    print DEV &quot;atv1\012&quot;; # wrong, for some devices
    print DEV &quot;atv1\015&quot;; # right, for some devices
</code></pre>
<p> Even though with normal text files a ``\n&#8217;&#8216; will do the trick, there is still no unified scheme for terminating a line that is portable between Unix, DOS/Win, and Macintosh, except to terminate <i></i><font SIZE="-1"><i>ALL</i></font><i></i> line ends with ``\015\012&#8217;&#8216;, and strip what you don&#8217;t need from the output. This applies especially to socket I/O and autoflushing, discussed next. </p>
 </dd>
<dt>flushing output</dt>
<dd> <p> If you expect characters to get to your device when you <code>&quot;print()&quot;</code> them, you&#8217;ll want to autoflush that filehandle. You can use <code>&quot;select()&quot;</code> and the <code>$|</code> variable to control autoflushing (see ``$|&#8216;&#8216; in perlvar and ``select&#8217;&#8216; in perlfunc, or perlfaq5, ``How do I flush/unbuffer an output filehandle? Why must I do this?&#8216;&#8216;): </p>
<pre><code>    my $old_handle = select($dev_fh);
    $| = 1;
    select($old_handle);
</code></pre>
<p> You&#8217;ll also see code that does this without a temporary variable, as in </p>
<pre><code>    select((select($deb_handle), $| = 1)[0]);
</code></pre>
<p> Or if you don&#8217;t mind pulling in a few thousand lines of code just because you&#8217;re afraid of a little <code>$|</code> variable: </p>
<pre><code>    use IO::Handle;
    $dev_fh-&gt;autoflush(1);
</code></pre>
<p> As mentioned in the previous item, this still doesn&#8217;t work when using socket I/O between Unix and Macintosh. You&#8217;ll need to hard code your line terminators, in that case. </p>
 </dd>
<dt>non-blocking input</dt>
<dd> <p> If you are doing a blocking <code>&quot;read()&quot;</code> or <code>&quot;sysread()&quot;</code>, you&#8217;ll have to arrange for an alarm handler to provide a timeout (see ``alarm&#8217;&#8216; in perlfunc). If you have a non-blocking open, you&#8217;ll likely have a non-blocking read, which means you may have to use a 4-arg <code>&quot;select()&quot;</code> to determine whether I/O is ready on that device (see ``select&#8217;&#8216; in perlfunc. </p>
 </dd></dl>
<p> While trying to read from his caller-id box, the notorious Jamie Zawinski <code>&quot;&lt;jwz [at] netscape.com&gt;&quot;</code>, after much gnashing of teeth and fighting with <code>&quot;sysread&quot;</code>, <code>&quot;sysopen&quot;</code>, <font SIZE="-1">POSIX</font>&#8216;s <code>&quot;tcgetattr&quot;</code> business, and various other functions that go bump in the night, finally came up with this: </p>
<pre><code>    sub open_modem {
        use IPC::Open2;
        my $stty = `/bin/stty -g`;
        open2( \*MODEM_IN, \*MODEM_OUT, &quot;cu -l$modem_device -s2400 2&gt;&amp;1&quot;);
        # starting cu hoses /dev/tty's stty settings, even when it has
        # been opened on a pipe...
        system(&quot;/bin/stty $stty&quot;);
        $_ = &lt;MODEM_IN&gt;;
        chomp;
        if ( !m/^Connected/ ) {
            print STDERR &quot;$0: cu printed `$_' instead of `Connected'\n&quot;;
        }
    }
</code></pre>
<h3>How do I decode encrypted password files?</h3>
<p> You spend lots and lots of money on dedicated hardware, but this is bound to get you talked about. </p>
<p> Seriously, you can&#8217;t if they are Unix password files---the Unix password system employs one-way encryption. It&#8217;s more like hashing than encryption. The best you can do is check whether something else hashes to the same string. You can&#8217;t turn a hash back into the original string. Programs like Crack can forcibly (and intelligently) try to guess passwords, but don&#8217;t (can&#8217;t) guarantee quick success. </p>
<p> If you&#8217;re worried about users selecting bad passwords, you should proactively check when they try to change their password (by modifying <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), for example).  </p>
<h3>How do I start a process in the background?</h3>
<p> (contributed by brian d foy) </p>
<p> There&#8217;s not a single way to run code in the background so you don&#8217;t have to wait for it to finish before your program moves on to other tasks. Process management depends on your particular operating system, and many of the techniques are covered in perlipc. </p>
<p> Several <font SIZE="-1">CPAN</font> modules may be able to help, including IPC::Open2 or IPC::Open3, IPC::Run, Parallel::Jobs, Parallel::ForkManager, <font SIZE="-1">POE</font>, Proc::Background, and Win32::Process. There are many other modules you might use, so check those namespaces for other options too. </p>
<p> If you are on a Unix-like system, you might be able to get away with a system call where you put an <code>&quot;&amp;&quot;</code> on the end of the command: </p>
<pre><code>    system(&quot;cmd &amp;&quot;)
</code></pre>
<p> You can also try using <code>&quot;fork&quot;</code>, as described in perlfunc (although this is the same thing that many of the modules will do for you). </p>
<dl>
<dt><font SIZE="-1">STDIN, STDOUT,</font> and <font SIZE="-1">STDERR</font> are shared</dt>
<dd> <p> Both the main process and the backgrounded one (the ``child&#8217;&#8216; process) share the same <font SIZE="-1">STDIN, STDOUT</font> and <font SIZE="-1">STDERR</font> filehandles. If both try to access them at once, strange things can happen. You may want to close or reopen these for the child. You can get around this with <code>&quot;open&quot;</code>ing a pipe (see ``open&#8217;&#8216; in perlfunc) but on some systems this means that the child process cannot outlive the parent. </p>
 </dd>
<dt>Signals</dt>
<dd> <p> You&#8217;ll have to catch the <font SIZE="-1">SIGCHLD</font> signal, and possibly <font SIZE="-1">SIGPIPE</font> too. <font SIZE="-1">SIGCHLD</font> is sent when the backgrounded process finishes. <font SIZE="-1">SIGPIPE</font> is sent when you write to a filehandle whose child process has closed (an untrapped <font SIZE="-1">SIGPIPE</font> can cause your program to silently die). This is not an issue with <code>&quot;system(&quot;cmd&amp;&quot;)&quot;</code>. </p>
 </dd>
<dt>Zombies</dt>
<dd> <p> You have to be prepared to ``reap&#8217;&#8216; the child process when it finishes. </p>
<pre><code>    $SIG{CHLD} = sub { wait };
    $SIG{CHLD} = 'IGNORE';
</code></pre>
<p> You can also use a double fork. You immediately <code>&quot;wait()&quot;</code> for your first child, and the init daemon will <code>&quot;wait()&quot;</code> for your grandchild once it exits. </p>
<pre><code>    unless ($pid = fork) {
        unless (fork) {
            exec &quot;what you really wanna do&quot;;
            die &quot;exec failed!&quot;;
        }
        exit 0;
    }
    waitpid($pid, 0);
</code></pre>
<p> See ``Signals&#8217;&#8216; in perlipc for other examples of code to do this. Zombies are not an issue with <code>&quot;system(&quot;prog &amp;&quot;)&quot;</code>. </p>
 </dd></dl>
<h3>How do I trap control characters/signals?</h3>
<p> You don&#8217;t actually ``trap&#8217;&#8216; a control character. Instead, that character generates a signal which is sent to your terminal&#8217;s currently foregrounded process group, which you then trap in your process. Signals are documented in ``Signals&#8217;&#8216; in perlipc and the section on ``Signals&#8217;&#8216; in the Camel. </p>
<p> You can set the values of the <code>%SIG</code> hash to be the functions you want to handle the signal. After perl catches the signal, it looks in <code>%SIG</code> for a key with the same name as the signal, then calls the subroutine value for that key. </p>
<pre><code>    # as an anonymous subroutine
    $SIG{INT} = sub { syswrite(STDERR, &quot;ouch\n&quot;, 5 ) };
    # or a reference to a function
    $SIG{INT} = \&amp;ouch;
    # or the name of the function as a string
    $SIG{INT} = &quot;ouch&quot;;
</code></pre>
<p> Perl versions before 5.8 had in its C source code signal handlers which would catch the signal and possibly run a Perl function that you had set in <code>%SIG</code>. This violated the rules of signal handling at that level causing perl to dump core. Since version 5.8.0, perl looks at <code>%SIG</code> <code>after</code> the signal has been caught, rather than while it is being caught. Previous versions of this answer were incorrect.  </p>
<h3>How do I modify the shadow password file on a Unix system?</h3>
<p> If perl was installed correctly and your shadow library was written properly, the <code>&quot;getpw*()&quot;</code> functions described in perlfunc should in theory provide (read-only) access to entries in the shadow password file. To change the file, make a new shadow password file (the format varies from system to system---see <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1) for specifics) and use <code>pwd_mkdb(8)</code> to install it (see <code>pwd_mkdb</code>(8) for more details).  </p>
<h3>How do I set the time and date?</h3>
<p> Assuming you&#8217;re running under sufficient permissions, you should be able to set the system-wide date and time by running the <code><a href="/docs/linux/man/1-date/">date</a>(1)</code> program. (There is no way to set the time and date on a per-process basis.) This mechanism will work for Unix, MS-DOS, Windows, and <font SIZE="-1">NT</font>; the <font SIZE="-1">VMS</font> equivalent is <code>&quot;set time&quot;</code>. </p>
<p> However, if all you want to do is change your time zone, you can probably get away with setting an environment variable: </p>
<pre><code>    $ENV{TZ} = &quot;MST7MDT&quot;; # Unixish
    $ENV{'SYS$TIMEZONE_DIFFERENTIAL'}=&quot;-5&quot; # vms
    system('trn', 'comp.lang.perl.misc');
</code></pre>
<code></code><code></code><h3>How can I sleep() or alarm() for under a second?</h3>
<p> If you want finer granularity than the 1 second that the <code>&quot;sleep()&quot;</code> function provides, the easiest way is to use the <code>&quot;select()&quot;</code> function as documented in ``select&#8217;&#8216; in perlfunc. Try the Time::HiRes and the BSD::Itimer modules (available from <font SIZE="-1">CPAN,</font> and starting from Perl 5.8 Time::HiRes is part of the standard distribution).  </p>
<h3>How can I measure time under a second?</h3>
<p> (contributed by brian d foy) </p>
<p> The Time::HiRes module (part of the standard distribution as of Perl 5.8) measures time with the <code>&quot;gettimeofday()&quot;</code> system call, which returns the time in microseconds since the epoch. If you can&#8217;t install Time::HiRes for older Perls and you are on a Unixish system, you may be able to call <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a>(2)</code> directly. See ``syscall&#8217;&#8216; in perlfunc.  </p>
<code></code><code></code><code></code><h3>How can I do an atexit() or setjmp() / longjmp() ? (Exception handling)</h3>
<p> You can use the <code>&quot;END&quot;</code> block to simulate <code>&quot;atexit()&quot;</code>. Each package&#8217;s <code>&quot;END&quot;</code> block is called when the program or thread ends. See the perlmod manpage for more details about <code>&quot;END&quot;</code> blocks. </p>
<p> For example, you can use this to make sure your filter program managed to finish its output without filling up the disk: </p>
<pre><code>    END {
        close(STDOUT) || die &quot;stdout close failed: $!&quot;;
    }
</code></pre>
<p> The <code>&quot;END&quot;</code> block isn&#8217;t called when untrapped signals kill the program, though, so if you use <code>&quot;END&quot;</code> blocks you should also use </p>
<pre><code>    use sigtrap qw(die normal-signals);
</code></pre>
<p> Perl&#8217;s exception-handling mechanism is its <code>&quot;eval()&quot;</code> operator. You can use <code>&quot;eval()&quot;</code> as <code>&quot;setjmp&quot;</code> and <code>&quot;die()&quot;</code> as <code>&quot;longjmp&quot;</code>. For details of this, see the section on signals, especially the time-out handler for a blocking <code>&quot;flock()&quot;</code> in ``Signals&#8217;&#8216; in perlipc or the section on ``Signals&#8217;&#8216; in <i>Programming Perl</i>. </p>
<p> If exception handling is all you&#8217;re interested in, use one of the many <font SIZE="-1">CPAN</font> modules that handle exceptions, such as Try::Tiny. </p>
<p> If you want the <code>&quot;atexit()&quot;</code> syntax (and an <code>&quot;rmexit()&quot;</code> as well), try the <code>&quot;AtExit&quot;</code> module available from <font SIZE="-1">CPAN.</font>  </p>
<h3>Why doesn't my sockets program work under System V (Solaris)? What does the error message Protocol not supported mean?</h3>
<p> Some Sys-V based systems, notably Solaris 2.X, redefined some of the standard socket constants. Since these were constant across all architectures, they were often hardwired into perl code. The proper way to deal with this is to ``use Socket&#8217;&#8216; to get the correct values. </p>
<p> Note that even though SunOS and Solaris are binary compatible, these values are different. Go figure.  </p>
<h3>How can I call my system's unique C functions from Perl?</h3>
<p> In most cases, you write an external module to do it---see the answer to ``Where can I learn about linking C with Perl? [h2xs, xsubpp]&#8216;&#8216;. However, if the function is a system call, and your system supports <code>&quot;syscall()&quot;</code>, you can use the <code>&quot;syscall&quot;</code> function (documented in perlfunc). </p>
<p> Remember to check the modules that came with your distribution, and <font SIZE="-1">CPAN</font> as well---someone may already have written a module to do it. On Windows, try Win32::API. On Macs, try Mac::Carbon. If no module has an interface to the C function, you can inline a bit of C in your Perl source with Inline::C.  </p>
<code></code><code></code><h3>Where do I get the include files to do ioctl() or syscall() ?</h3>
<p> Historically, these would be generated by the h2ph tool, part of the standard perl distribution. This program converts <code><a href="/docs/linux/man/1-cpp/">cpp</a>(1)</code> directives in C header files to files containing subroutine definitions, like <code>&quot;SYS_getitimer()&quot;</code>, which you can use as arguments to your functions. It doesn&#8217;t work perfectly, but it usually gets most of the job done. Simple files like <i>errno.h</i>, <i>syscall.h</i>, and <i>socket.h</i> were fine, but the hard ones like <i>ioctl.h</i> nearly always need to be hand-edited. Here&#8217;s how to install the *.ph files: </p>
<pre><code>    1. Become the super-user
    2. cd /usr/include
    3. h2ph *.h */*.h
</code></pre>
<p> If your system supports dynamic loading, for reasons of portability and sanity you probably ought to use h2xs (also part of the standard perl distribution). This tool converts C header files to Perl extensions. See perlxstut for how to get started with h2xs. </p>
<p> If your system doesn&#8217;t support dynamic loading, you still probably ought to use h2xs. See perlxstut and ExtUtils::MakeMaker for more information (in brief, just use <code>make perl</code> instead of a plain <code>make</code> to rebuild perl with a new static extension).  </p>
<h3>Why do setuid perl scripts complain about kernel problems?</h3>
<p> Some operating systems have bugs in the kernel that make setuid scripts inherently insecure. Perl gives you a number of options (described in perlsec) to work around such systems.  </p>
<h3>How can I open a pipe both to and from a command?</h3>
<p> The IPC::Open2 module (part of the standard perl distribution) is an easy-to-use approach that internally uses <code>&quot;pipe()&quot;</code>, <code>&quot;fork()&quot;</code>, and <code>&quot;exec()&quot;</code> to do the job. Make sure you read the deadlock warnings in its documentation, though (see IPC::Open2). See ``Bidirectional Communication with Another Process&#8217;&#8216; in perlipc and ``Bidirectional Communication with Yourself&#8217;&#8216; in perlipc </p>
<p> You may also use the IPC::Open3 module (part of the standard perl distribution), but be warned that it has a different order of arguments from IPC::Open2 (see IPC::Open3).  </p>
<code></code><h3>Why can't I get the output of a command with system() ?</h3>
<p> You&#8217;re confusing the purpose of <code>&quot;system()&quot;</code> and backticks (``). <code>&quot;system()&quot;</code> runs a command and returns exit status information (as a 16 bit value: the low 7 bits are the signal the process died from, if any, and the high 8 bits are the actual exit value). Backticks (``) run a command and return what it sent to <font SIZE="-1">STDOUT.</font> </p>
<pre><code>    my $exit_status = system(&quot;mail-users&quot;);
    my $output_string = `ls`;
</code></pre>
<font SIZE="-1"></font><h3>How can I capture STDERR from an external command?</h3>
<p> There are three basic ways of running external commands: </p>
<pre><code>    system $cmd; # using system()
    my $output = `$cmd`; # using backticks (``)
    open (my $pipe_fh, &quot;$cmd |&quot;); # using open()
</code></pre>
<p> With <code>&quot;system()&quot;</code>, both <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR</font> will go the same place as the script&#8217;s <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR,</font> unless the <code>&quot;system()&quot;</code> command redirects them. Backticks and <code>&quot;open()&quot;</code> read <code>only</code> the <font SIZE="-1">STDOUT</font> of your command. </p>
<p> You can also use the <code>&quot;open3()&quot;</code> function from IPC::Open3. Benjamin Goldberg provides some sample code: </p>
<p> To capture a program&#8217;s <font SIZE="-1">STDOUT,</font> but discard its <font SIZE="-1">STDERR:</font> </p>
<pre><code>    use IPC::Open3;
    use File::Spec;
    my $in = '';
    open(NULL, &quot;&gt;&quot;, File::Spec-&gt;devnull);
    my $pid = open3($in, \*PH, &quot;&gt;&amp;NULL&quot;, &quot;cmd&quot;);
    while( &lt;PH&gt; ) { }
    waitpid($pid, 0);
</code></pre>
<p> To capture a program&#8217;s <font SIZE="-1">STDERR,</font> but discard its <font SIZE="-1">STDOUT:</font> </p>
<pre><code>    use IPC::Open3;
    use File::Spec;
    my $in = '';
    open(NULL, &quot;&gt;&quot;, File::Spec-&gt;devnull);
    my $pid = open3($in, &quot;&gt;&amp;NULL&quot;, \*PH, &quot;cmd&quot;);
    while( &lt;PH&gt; ) { }
    waitpid($pid, 0);
</code></pre>
<p> To capture a program&#8217;s <font SIZE="-1">STDERR,</font> and let its <font SIZE="-1">STDOUT</font> go to our own <font SIZE="-1">STDERR:</font> </p>
<pre><code>    use IPC::Open3;
    my $in = '';
    my $pid = open3($in, &quot;&gt;&amp;STDERR&quot;, \*PH, &quot;cmd&quot;);
    while( &lt;PH&gt; ) { }
    waitpid($pid, 0);
</code></pre>
<p> To read both a command&#8217;s <font SIZE="-1">STDOUT</font> and its <font SIZE="-1">STDERR</font> separately, you can redirect them to temp files, let the command run, then read the temp files: </p>
<pre><code>    use IPC::Open3;
    use IO::File;
    my $in = '';
    local *CATCHOUT = IO::File-&gt;new_tmpfile;
    local *CATCHERR = IO::File-&gt;new_tmpfile;
    my $pid = open3($in, &quot;&gt;&amp;CATCHOUT&quot;, &quot;&gt;&amp;CATCHERR&quot;, &quot;cmd&quot;);
    waitpid($pid, 0);
    seek $_, 0, 0 for \*CATCHOUT, \*CATCHERR;
    while( &lt;CATCHOUT&gt; ) {}
    while( &lt;CATCHERR&gt; ) {}
</code></pre>
<p> But there&#8217;s no real need for <code>both</code> to be tempfiles... the following should work just as well, without deadlocking: </p>
<pre><code>    use IPC::Open3;
    my $in = '';
    use IO::File;
    local *CATCHERR = IO::File-&gt;new_tmpfile;
    my $pid = open3($in, \*CATCHOUT, &quot;&gt;&amp;CATCHERR&quot;, &quot;cmd&quot;);
    while( &lt;CATCHOUT&gt; ) {}
    waitpid($pid, 0);
    seek CATCHERR, 0, 0;
    while( &lt;CATCHERR&gt; ) {}
</code></pre>
<p> And it&#8217;ll be faster, too, since we can begin processing the program&#8217;s stdout immediately, rather than waiting for the program to finish. </p>
<p> With any of these, you can change file descriptors before the call: </p>
<pre><code>    open(STDOUT, &quot;&gt;logfile&quot;);
    system(&quot;ls&quot;);
</code></pre>
<p> or you can use Bourne shell file-descriptor redirection: </p>
<pre><code>    $output = `$cmd 2&gt;some_file`;
    open (PIPE, &quot;cmd 2&gt;some_file |&quot;);
</code></pre>
<p> You can also use file-descriptor redirection to make <font SIZE="-1">STDERR</font> a duplicate of <font SIZE="-1">STDOUT:</font> </p>
<pre><code>    $output = `$cmd 2&gt;&amp;1`;
    open (PIPE, &quot;cmd 2&gt;&amp;1 |&quot;);
</code></pre>
<p> Note that you <i>cannot</i> simply open <font SIZE="-1">STDERR</font> to be a dup of <font SIZE="-1">STDOUT</font> in your Perl program and avoid calling the shell to do the redirection. This doesn&#8217;t work: </p>
<pre><code>    open(STDERR, &quot;&gt;&amp;STDOUT&quot;);
    $alloutput = `cmd args`; # stderr still escapes
</code></pre>
<p> This fails because the <code>&quot;open()&quot;</code> makes <font SIZE="-1">STDERR</font> go to where <font SIZE="-1">STDOUT</font> was going at the time of the <code>&quot;open()&quot;</code>. The backticks then make <font SIZE="-1">STDOUT</font> go to a string, but don&#8217;t change <font SIZE="-1">STDERR</font> (which still goes to the old <font SIZE="-1">STDOUT</font>). </p>
<p> Note that you <i>must</i> use Bourne shell (<code><a href="/docs/linux/man/1-sh/">sh</a>(1)</code>) redirection syntax in backticks, not <code><a href="/docs/linux/man/1-csh/">csh</a>(1)</code>! Details on why Perl&#8217;s <code>&quot;system()&quot;</code> and backtick and pipe opens all use the Bourne shell are in the <i>versus/csh.whynot</i> article in the ``Far More Than You Ever Wanted To Know&#8217;&#8216; collection in &lt;<a rel="nofollow" href="http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz">http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz</a>&gt; . To capture a command&#8217;s <font SIZE="-1">STDERR</font> and <font SIZE="-1">STDOUT</font> together: </p>
<pre><code>    $output = `cmd 2&gt;&amp;1`; # either with backticks
    $pid = open(PH, &quot;cmd 2&gt;&amp;1 |&quot;); # or with an open pipe
    while (&lt;PH&gt;) { } # plus a read
</code></pre>
<p> To capture a command&#8217;s <font SIZE="-1">STDOUT</font> but discard its <font SIZE="-1">STDERR:</font> </p>
<pre><code>    $output = `cmd 2&gt;/dev/null`; # either with backticks
    $pid = open(PH, &quot;cmd 2&gt;/dev/null |&quot;); # or with an open pipe
    while (&lt;PH&gt;) { } # plus a read
</code></pre>
<p> To capture a command&#8217;s <font SIZE="-1">STDERR</font> but discard its <font SIZE="-1">STDOUT:</font> </p>
<pre><code>    $output = `cmd 2&gt;&amp;1 1&gt;/dev/null`; # either with backticks
    $pid = open(PH, &quot;cmd 2&gt;&amp;1 1&gt;/dev/null |&quot;); # or with an open pipe
    while (&lt;PH&gt;) { } # plus a read
</code></pre>
<p> To exchange a command&#8217;s <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR</font> in order to capture the <font SIZE="-1">STDERR</font> but leave its <font SIZE="-1">STDOUT</font> to come out our old <font SIZE="-1">STDERR:</font> </p>
<pre><code>    $output = `cmd 3&gt;&amp;1 1&gt;&amp;2 2&gt;&amp;3 3&gt;&amp;-`; # either with backticks
    $pid = open(PH, &quot;cmd 3&gt;&amp;1 1&gt;&amp;2 2&gt;&amp;3 3&gt;&amp;-|&quot;);# or with an open pipe
    while (&lt;PH&gt;) { } # plus a read
</code></pre>
<p> To read both a command&#8217;s <font SIZE="-1">STDOUT</font> and its <font SIZE="-1">STDERR</font> separately, it&#8217;s easiest to redirect them separately to files, and then read from those files when the program is done: </p>
<pre><code>    system(&quot;program args 1&gt;program.stdout 2&gt;program.stderr&quot;);
</code></pre>
<p> Ordering is important in all these examples. That&#8217;s because the shell processes file descriptor redirections in strictly left to right order. </p>
<pre><code>    system(&quot;prog args 1&gt;tmpfile 2&gt;&amp;1&quot;);
    system(&quot;prog args 2&gt;&amp;1 1&gt;tmpfile&quot;);
</code></pre>
<p> The first command sends both standard out and standard error to the temporary file. The second command sends only the old standard output there, and the old standard error shows up on the old standard out.  </p>
<code></code><h3>Why doesn't open() return an error when a pipe open fails?</h3>
<p> If the second argument to a piped <code>&quot;open()&quot;</code> contains shell metacharacters, perl <code>&quot;fork()&quot;</code>s, then <code>&quot;exec()&quot;</code>s a shell to decode the metacharacters and eventually run the desired program. If the program couldn&#8217;t be run, it&#8217;s the shell that gets the message, not Perl. All your Perl program can find out is whether the shell itself could be successfully started. You can still capture the shell&#8217;s <font SIZE="-1">STDERR</font> and check it for error messages. See ``How can I capture <font SIZE="-1">STDERR</font> from an external command?&#8216;&#8216; elsewhere in this document, or use the IPC::Open3 module. </p>
<p> If there are no shell metacharacters in the argument of <code>&quot;open()&quot;</code>, Perl runs the command directly, without using the shell, and can correctly report whether the command started.  </p>
<h3>What's wrong with using backticks in a void context?</h3>
<p> Strictly speaking, nothing. Stylistically speaking, it&#8217;s not a good way to write maintainable code. Perl has several operators for running external commands. Backticks are one; they collect the output from the command for use in your program. The <code>&quot;system&quot;</code> function is another; it doesn&#8217;t do this. </p>
<p> Writing backticks in your program sends a clear message to the readers of your code that you wanted to collect the output of the command. Why send a clear message that isn&#8217;t true? </p>
<p> Consider this line: </p>
<pre><code>    `cat /etc/termcap`;
</code></pre>
<p> You forgot to check <code>$?</code> to see whether the program even ran correctly. Even if you wrote </p>
<pre><code>    print `cat /etc/termcap`;
</code></pre>
<p> this code could and probably should be written as </p>
<pre><code>    system(&quot;cat /etc/termcap&quot;) == 0
    or die &quot;cat program failed!&quot;;
</code></pre>
<p> which will echo the cat command&#8217;s output as it is generated, instead of waiting until the program has completed to print it out. It also checks the return value. </p>
<p> <code>&quot;system&quot;</code> also provides direct control over whether shell wildcard processing may take place, whereas backticks do not.  </p>
<h3>How can I call backticks without shell processing?</h3>
<p> This is a bit tricky. You can&#8217;t simply write the command like this: </p>
<pre><code>    @ok = `grep @opts '$search_string' @filenames`;
</code></pre>
<p> As of Perl 5.8.0, you can use <code>&quot;open()&quot;</code> with multiple arguments. Just like the list forms of <code>&quot;system()&quot;</code> and <code>&quot;exec()&quot;</code>, no shell escapes happen. </p>
<pre><code>    open( GREP, &quot;-|&quot;, 'grep', @opts, $search_string, @filenames );
    chomp(@ok = &lt;GREP&gt;);
    close GREP;
</code></pre>
<p> You can also: </p>
<pre><code>    my @ok = ();
    if (open(GREP, &quot;-|&quot;)) {
        while (&lt;GREP&gt;) {
            chomp;
            push(@ok, $_);
        }
        close GREP;
    } else {
        exec 'grep', @opts, $search_string, @filenames;
    }
</code></pre>
<p> Just as with <code>&quot;system()&quot;</code>, no shell escapes happen when you <code>&quot;exec()&quot;</code> a list. Further examples of this can be found in ``Safe Pipe Opens&#8217;&#8216; in perlipc. </p>
<p> Note that if you&#8217;re using Windows, no solution to this vexing issue is even possible. Even though Perl emulates <code>&quot;fork()&quot;</code>, you&#8217;ll still be stuck, because Windows does not have an argc/argv-style <font SIZE="-1">API.</font>  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>Why can't my script read from STDIN after I gave it EOF (^D on Unix, ^Z on MS-DOS)?</h3>
<p> This happens only if your perl is compiled to use stdio instead of perlio, which is the default. Some (maybe all?) stdios set error and eof flags that you may need to clear. The <font SIZE="-1">POSIX</font> module defines <code>&quot;clearerr()&quot;</code> that you can use. That is the technically correct way to do it. Here are some less reliable workarounds: </p>
<dl>
<dt>1.</dt>
<dd> <p> Try keeping around the seekpointer and go there, like this: </p>
<pre><code>    my $where = tell($log_fh);
    seek($log_fh, $where, 0);
</code></pre>
 </dd>
<dt>2.</dt>
<dd> <p> If that doesn&#8217;t work, try seeking to a different part of the file and then back. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If that doesn&#8217;t work, try seeking to a different part of the file, reading something, and then seeking back. </p>
 </dd>
<dt>4.</dt>
<dd> <p> If that doesn&#8217;t work, give up on your stdio package and use sysread. </p>
 </dd></dl>
<h3>How can I convert my shell script to perl?</h3>
<p> Learn Perl and rewrite it. Seriously, there&#8217;s no simple converter. Things that are awkward to do in the shell are easy to do in Perl, and this very awkwardness is what would make a shell-&gt;perl converter nigh-on impossible to write. By rewriting it, you&#8217;ll think about what you&#8217;re really trying to do, and hopefully will escape the shell&#8217;s pipeline datastream paradigm, which while convenient for some matters, causes many inefficiencies.  </p>
<h3>Can I use perl to run a telnet or ftp session?</h3>
<p> Try the Net::FTP, TCP::Client, and Net::Telnet modules (available from <font SIZE="-1">CPAN</font>). &lt;<a rel="nofollow" href="http://www.cpan.org/scripts/netstuff/telnet.emul.shar">http://www.cpan.org/scripts/netstuff/telnet.emul.shar</a>&gt; will also help for emulating the telnet protocol, but Net::Telnet is quite probably easier to use. </p>
<p> If all you want to do is pretend to be telnet but don&#8217;t need the initial telnet handshaking, then the standard dual-process approach will suffice: </p>
<pre><code>    use IO::Socket; # new in 5.004
    my $handle = IO::Socket::INET-&gt;new('www.perl.com:80')
        or die &quot;can't connect to port 80 onwww.perl.com $!&quot;;
    $handle-&gt;autoflush(1);
    if (fork()) { # XXX: undef means failure
        select($handle);
        print while &lt;STDIN&gt;; # everything from stdin to socket
    } else {
        print while &lt;$handle&gt;; # everything from socket to stdout
    }
    close $handle;
    exit;
</code></pre>
<h3>How can I write expect in Perl?</h3>
<p> Once upon a time, there was a library called <i>chat2.pl</i> (part of the standard perl distribution), which never really got finished. If you find it somewhere, <i>don&#8217;t use it</i>. These days, your best bet is to look at the Expect module available from <font SIZE="-1">CPAN,</font> which also requires two other modules from <font SIZE="-1">CPAN,</font> IO::Pty and IO::Stty.  </p>
<h3>Is there a way to hide perl's command line from programs such as ps?</h3>
<p> First of all note that if you&#8217;re doing this for security reasons (to avoid people seeing passwords, for example) then you should rewrite your program so that critical information is never given as an argument. Hiding the arguments won&#8217;t make your program completely secure. </p>
<p> To actually alter the visible command line, you can assign to the variable <code>$0</code> as documented in perlvar. This won&#8217;t work on all operating systems, though. Daemon programs like sendmail place their state there, as in: </p>
<pre><code>    $0 = &quot;orcus [accepting connections]&quot;;
</code></pre>
<h3>I {changed directory, modified my environment} in a perl script. How come the change disappeared when I exited the script? How do I get my changes to be visible?</h3>
<dl>
<dt>Unix</dt>
<dd> <p> In the strictest sense, it can&#8217;t be done---the script executes as a different process from the shell it was started from. Changes to a process are not reflected in its parent---only in any children created after the change. There is shell magic that may allow you to fake it by <code>&quot;eval()&quot;</code>ing the script&#8217;s output in your shell; check out the comp.unix.questions <font SIZE="-1">FAQ</font> for details. </p>
 </dd></dl>
<h3>How do I close a process's filehandle without waiting for it to complete?</h3>
<p> Assuming your system supports such things, just send an appropriate signal to the process (see ``kill&#8217;&#8216; in perlfunc). It&#8217;s common to first send a <font SIZE="-1">TERM</font> signal, wait a little bit, and then send a <font SIZE="-1">KILL</font> signal to finish it off.  </p>
<h3>How do I fork a daemon process?</h3>
<p> If by daemon process you mean one that&#8217;s detached (disassociated from its tty), then the following process is reported to work on most Unixish systems. Non-Unix users should check their Your_OS::Process module for other solutions. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Open /dev/tty and use the <font SIZE="-1">TIOCNOTTY</font> ioctl on it. See <code><a href="/docs/linux/man/1-tty/">tty</a></code>(1) for details. Or better yet, you can just use the <code>&quot;POSIX::setsid()&quot;</code> function, so you don&#8217;t have to worry about process groups. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Change directory to / </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reopen <font SIZE="-1">STDIN, STDOUT,</font> and <font SIZE="-1">STDERR</font> so they&#8217;re not connected to the old tty. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Background yourself like this: </p>
<pre><code>    fork &amp;&amp; exit;
</code></pre>
 </dd></dl>
<p> The Proc::Daemon module, available from <font SIZE="-1">CPAN,</font> provides a function to perform these actions for you.  </p>
<h3>How do I find out if I'm running interactively or not?</h3>
<p> (contributed by brian d foy) </p>
<p> This is a difficult question to answer, and the best answer is only a guess. </p>
<p> What do you really want to know? If you merely want to know if one of your filehandles is connected to a terminal, you can try the <code>&quot;-t&quot;</code> file test: </p>
<pre><code>    if( -t STDOUT ) {
        print &quot;I'm connected to a terminal!\n&quot;;
    }
</code></pre>
<p> However, you might be out of luck if you expect that means there is a real person on the other side. With the Expect module, another program can pretend to be a person. The program might even come close to passing the Turing test. </p>
<p> The IO::Interactive module does the best it can to give you an answer. Its <code>&quot;is_interactive&quot;</code> function returns an output filehandle; that filehandle points to standard output if the module thinks the session is interactive. Otherwise, the filehandle is a null handle that simply discards the output: </p>
<pre><code>    use IO::Interactive;
    print { is_interactive } &quot;I might go to standard output!\n&quot;;
</code></pre>
<p> This still doesn&#8217;t guarantee that a real person is answering your prompts or reading your output. </p>
<p> If you want to know how to handle automated testing for your distribution, you can check the environment. The <font SIZE="-1">CPAN</font> Testers, for instance, set the value of <code>&quot;AUTOMATED_TESTING&quot;</code>: </p>
<pre><code>    unless( $ENV{AUTOMATED_TESTING} ) {
        print &quot;Hello interactive tester!\n&quot;;
    }
</code></pre>
<h3>How do I timeout a slow event?</h3>
<p> Use the <code>&quot;alarm()&quot;</code> function, probably in conjunction with a signal handler, as documented in ``Signals&#8217;&#8216; in perlipc and the section on ``Signals&#8217;&#8216; in the Camel. You may instead use the more flexible Sys::AlarmCall module available from <font SIZE="-1">CPAN.</font> </p>
<p> The <code>&quot;alarm()&quot;</code> function is not implemented on all versions of Windows. Check the documentation for your specific version of Perl.  </p>
<font SIZE="-1"></font><h3>How do I set CPU limits?</h3>
<p> (contributed by Xho) </p>
<p> Use the BSD::Resource module from <font SIZE="-1">CPAN.</font> As an example: </p>
<pre><code>    use BSD::Resource;
    setrlimit(RLIMIT_CPU,10,20) or die $!;
</code></pre>
<p> This sets the soft and hard limits to 10 and 20 seconds, respectively. After 10 seconds of time spent running on the <font SIZE="-1">CPU</font> (not ``wall&#8217;&#8216; time), the process will be sent a signal (<font SIZE="-1">XCPU</font> on some systems) which, if not trapped, will cause the process to terminate. If that signal is trapped, then after 10 more seconds (20 seconds in total) the process will be killed with a non-trappable signal. </p>
<p> See the BSD::Resource and your systems documentation for the gory details.  </p>
<h3>How do I avoid zombies on a Unix system?</h3>
<p> Use the reaper code from ``Signals&#8217;&#8216; in perlipc to call <code>&quot;wait()&quot;</code> when a <font SIZE="-1">SIGCHLD</font> is received, or else use the double-fork technique described in ``How do I start a process in the background?&#8216;&#8216; in perlfaq8.  </p>
<font SIZE="-1"></font><h3>How do I use an SQL database?</h3>
<p> The <font SIZE="-1">DBI</font> module provides an abstract interface to most database servers and types, including Oracle, <font SIZE="-1">DB2,</font> Sybase, mysql, Postgresql, <font SIZE="-1">ODBC,</font> and flat files. The <font SIZE="-1">DBI</font> module accesses each database type through a database driver, or <font SIZE="-1">DBD.</font> You can see a complete list of available drivers on <font SIZE="-1">CPAN:</font> &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-module/DBD/">http://www.cpan.org/modules/by-module/DBD/</a>&gt; . You can read more about <font SIZE="-1">DBI</font> on &lt;<a rel="nofollow" href="http://dbi.perl.org/">http://dbi.perl.org/</a>&gt; . </p>
<p> Other modules provide more specific access: Win32::ODBC, Alzabo, <code>&quot;iodbc&quot;</code>, and others found on <font SIZE="-1">CPAN</font> Search: &lt;<a rel="nofollow" href="https://metacpan.org/">https://metacpan.org/</a>&gt; .  </p>
<code></code><h3>How do I make a system() exit on control-C?</h3>
<p> You can&#8217;t. You need to imitate the <code>&quot;system()&quot;</code> call (see perlipc for sample code) and then have a signal handler for the <font SIZE="-1">INT</font> signal that passes the signal on to the subprocess. Or you can check for it: </p>
<pre><code>    $rc = system($cmd);
    if ($rc &amp; 127) { die &quot;signal death&quot; }
</code></pre>
<h3>How do I open a file without blocking?</h3>
<p> If you&#8217;re lucky enough to be using a system that supports non-blocking reads (most Unixish systems do), you need only to use the <code>&quot;O_NDELAY&quot;</code> or <code>&quot;O_NONBLOCK&quot;</code> flag from the <code>&quot;Fcntl&quot;</code> module in conjunction with <code>&quot;sysopen()&quot;</code>: </p>
<pre><code>    use Fcntl;
    sysopen(my $fh, &quot;/foo/somefile&quot;, O_WRONLY|O_NDELAY|O_CREAT, 0644)
        or die &quot;can't open /foo/somefile: $!&quot;:
</code></pre>
<h3>How do I tell the difference between errors from the shell and perl?</h3>
<p> (answer contributed by brian d foy) </p>
<p> When you run a Perl script, something else is running the script for you, and that something else may output error messages. The script might emit its own warnings and error messages. Most of the time you cannot tell who said what. </p>
<p> You probably cannot fix the thing that runs perl, but you can change how perl outputs its warnings by defining a custom warning and die functions. </p>
<p> Consider this script, which has an error you may not notice immediately. </p>
<pre><code>    #!/usr/locl/bin/perl
    print &quot;Hello World\n&quot;;
</code></pre>
<p> I get an error when I run this from my shell (which happens to be bash). That may look like perl forgot it has a <code>&quot;print()&quot;</code> function, but my shebang line is not the path to perl, so the shell runs the script, and I get the error. </p>
<pre><code>    $ ./test
    ./test: line 3: print: command not found
</code></pre>
<p> A quick and dirty fix involves a little bit of code, but this may be all you need to figure out the problem. </p>
<pre><code>    #!/usr/bin/perl -w
    BEGIN {
        $SIG{__WARN__} = sub{ print STDERR &quot;Perl: &quot;, @_; };
        $SIG{__DIE__} = sub{ print STDERR &quot;Perl: &quot;, @_; exit 1};
    }
    $a = 1 + undef;
    $x / 0;
    __END__
</code></pre>
<p> The perl message comes out with ``Perl&#8217;&#8216; in front. The <code>&quot;BEGIN&quot;</code> block works at compile time so all of the compilation errors and warnings get the ``Perl:&#8216;&#8216; prefix too. </p>
<pre><code>    Perl: Useless use of division (/) in void context at ./test line 9.
    Perl: Name &quot;main::a&quot; used only once: possible typo at ./test line 8.
    Perl: Name &quot;main::x&quot; used only once: possible typo at ./test line 9.
    Perl: Use of uninitialized value in addition (+) at ./test line 8.
    Perl: Use of uninitialized value in division (/) at ./test line 9.
    Perl: Illegal division by zero at ./test line 9.
    Perl: Illegal division by zero at -e line 3.
</code></pre>
<p> If I don&#8217;t see that ``Perl:&#8216;&#8216;, it&#8217;s not from perl. </p>
<p> You could also just know all the perl errors, and although there are some people who may know all of them, you probably don&#8217;t. However, they all should be in the perldiag manpage. If you don&#8217;t find the error in there, it probably isn&#8217;t a perl error. </p>
<p> Looking up every message is not the easiest way, so let perl to do it for you. Use the diagnostics pragma with turns perl&#8217;s normal messages into longer discussions on the topic. </p>
<pre><code>    use diagnostics;
</code></pre>
<p> If you don&#8217;t get a paragraph or two of expanded discussion, it might not be perl&#8217;s message.  </p>
<font SIZE="-1"></font><h3>How do I install a module from CPAN ?</h3>
<p> (contributed by brian d foy) </p>
<p> The easiest way is to have a module also named <font SIZE="-1">CPAN</font> do it for you by using the <code>&quot;cpan&quot;</code> command that comes with Perl. You can give it a list of modules to install: </p>
<pre><code>    $ cpan IO::Interactive Getopt::Whatever
</code></pre>
<p> If you prefer <code>&quot;CPANPLUS&quot;</code>, it&#8217;s just as easy: </p>
<pre><code>    $ cpanp i IO::Interactive Getopt::Whatever
</code></pre>
<p> If you want to install a distribution from the current directory, you can tell <code>&quot;CPAN.pm&quot;</code> to install <code>&quot;.&quot;</code> (the full stop): </p>
<pre><code>    $ cpan .
</code></pre>
<p> See the documentation for either of those commands to see what else you can do. </p>
<p> If you want to try to install a distribution by yourself, resolving all dependencies on your own, you follow one of two possible build paths. </p>
<p> For distributions that use <i>Makefile.PL</i>: </p>
<pre><code>    $ perl Makefile.PL
    $ make test install
</code></pre>
<p> For distributions that use <i>Build.PL</i>: </p>
<pre><code>    $ perl Build.PL
    $ ./Build test
    $ ./Build install
</code></pre>
<p> Some distributions may need to link to libraries or other third-party code and their build and installation sequences may be more complicated. Check any <i></i><font SIZE="-1"><i>README</i></font><i></i> or <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> files that you may find.  </p>
<h3>What's the difference between require and use?</h3>
<p> (contributed by brian d foy) </p>
<p> Perl runs <code>&quot;require&quot;</code> statement at run-time. Once Perl loads, compiles, and runs the file, it doesn&#8217;t do anything else. The <code>&quot;use&quot;</code> statement is the same as a <code>&quot;require&quot;</code> run at compile-time, but Perl also calls the <code>&quot;import&quot;</code> method for the loaded package. These two are the same: </p>
<pre><code>    use MODULE qw(import list);
    BEGIN {
        require MODULE;
        MODULE-&gt;import(import list);
    }
</code></pre>
<p> However, you can suppress the <code>&quot;import&quot;</code> by using an explicit, empty import list. Both of these still happen at compile-time: </p>
<pre><code>    use MODULE ();
    BEGIN {
        require MODULE;
    }
</code></pre>
<p> Since <code>&quot;use&quot;</code> will also call the <code>&quot;import&quot;</code> method, the actual value for <code>&quot;MODULE&quot;</code> must be a bareword. That is, <code>&quot;use&quot;</code> cannot load files by name, although <code>&quot;require&quot;</code> can: </p>
<pre><code>    require &quot;$ENV{HOME}/lib/Foo.pm&quot;; # no @INC searching!
</code></pre>
<p> See the entry for <code>&quot;use&quot;</code> in perlfunc for more details.  </p>
<h3>How do I keep my own module/library directory?</h3>
<p> When you build modules, tell Perl where to install the modules. </p>
<p> If you want to install modules for your own use, the easiest way might be local::lib, which you can download from <font SIZE="-1">CPAN.</font> It sets various installation settings for you, and uses those same settings within your programs. </p>
<p> If you want more flexibility, you need to configure your <font SIZE="-1">CPAN</font> client for your particular situation. </p>
<p> For <code>&quot;Makefile.PL&quot;</code>-based distributions, use the <font SIZE="-1">INSTALL_BASE</font> option when generating Makefiles: </p>
<pre><code>    perl Makefile.PL INSTALL_BASE=/mydir/perl
</code></pre>
<p> You can set this in your <code>&quot;CPAN.pm&quot;</code> configuration so modules automatically install in your private library directory when you use the <font SIZE="-1">CPAN</font>.pm shell: </p>
<pre><code>    % cpan
    cpan&gt; o conf makepl_arg INSTALL_BASE=/mydir/perl
    cpan&gt; o conf commit
</code></pre>
<p> For <code>&quot;Build.PL&quot;</code>-based distributions, use the --install_base option: </p>
<pre><code>    perl Build.PL --install_base /mydir/perl
</code></pre>
<p> You can configure <code>&quot;CPAN.pm&quot;</code> to automatically use this option too: </p>
<pre><code>    % cpan
    cpan&gt; o conf mbuild_arg &quot;--install_base /mydir/perl&quot;
    cpan&gt; o conf commit
</code></pre>
<p> <font SIZE="-1">INSTALL_BASE</font> tells these tools to put your modules into <i>/mydir/perl/lib/perl5</i>. See ``How do I add a directory to my include path (@INC) at runtime?&#8216;&#8216; for details on how to run your newly installed modules. </p>
<p> There is one caveat with <font SIZE="-1">INSTALL_BASE,</font> though, since it acts differently from the <font SIZE="-1">PREFIX</font> and <font SIZE="-1">LIB</font> settings that older versions of ExtUtils::MakeMaker advocated. <font SIZE="-1">INSTALL_BASE</font> does not support installing modules for multiple versions of Perl or different architectures under the same directory. You should consider whether you really want that and, if you do, use the older <font SIZE="-1">PREFIX</font> and <font SIZE="-1">LIB</font> settings. See the ExtUtils::Makemaker documentation for more details.  </p>
<h3>How do I add the directory my program lives in to the module/library search path?</h3>
<p> (contributed by brian d foy) </p>
<p> If you know the directory already, you can add it to <code>@INC</code> as you would for any other directory. You might &lt;use lib&gt; if you know the directory at compile time: </p>
<pre><code>    use lib $directory;
</code></pre>
<p> The trick in this task is to find the directory. Before your script does anything else (such as a <code>&quot;chdir&quot;</code>), you can get the current working directory with the <code>&quot;Cwd&quot;</code> module, which comes with Perl: </p>
<pre><code>    BEGIN {
        use Cwd;
        our $directory = cwd;
    }
    use lib $directory;
</code></pre>
<p> You can do a similar thing with the value of <code>$0</code>, which holds the script name. That might hold a relative path, but <code>&quot;rel2abs&quot;</code> can turn it into an absolute path. Once you have the </p>
<pre><code>    BEGIN {
        use File::Spec::Functions qw(rel2abs);
        use File::Basename qw(dirname);
        my $path = rel2abs( $0 );
        our $directory = dirname( $path );
    }
    use lib $directory;
</code></pre>
<p> The FindBin module, which comes with Perl, might work. It finds the directory of the currently running script and puts it in <code>$Bin</code>, which you can then use to construct the right library path: </p>
<pre><code>    use FindBin qw($Bin);
</code></pre>
<p> You can also use local::lib to do much of the same thing. Install modules using local::lib&#8217;s settings then use the module in your program: </p>
<pre><code>     use local::lib; # sets up a local lib at ~/perl5
</code></pre>
<p> See the local::lib documentation for more details.  </p>
<h3>How do I add a directory to my include path (@INC) at runtime?</h3>
<p> Here are the suggested ways of modifying your include path, including environment variables, run-time switches, and in-code statements: </p>
<dl>
<dt>the &quot;PERLLIB&quot; environment variable</dt>
<dd> <pre><code>    $ export PERLLIB=/path/to/my/dir
    $ perl program.pl
</code></pre>
 </dd>
<dt>the &quot;PERL5LIB&quot; environment variable</dt>
<dd> <pre><code>    $ export PERL5LIB=/path/to/my/dir
    $ perl program.pl
</code></pre>
 </dd>
<dt>the &quot;perl -Idir&quot; command line flag</dt>
<dd> <pre><code>    $ perl -I/path/to/my/dir program.pl
</code></pre>
 </dd>
<dt>the &quot;lib&quot; pragma:</dt>
<dd> <pre><code>    use lib &quot;$ENV{HOME}/myown_perllib&quot;;
</code></pre>
 </dd>
<dt>the local::lib module:</dt>
<dd> <pre><code>    use local::lib;
    use local::lib &quot;~/myown_perllib&quot;;
</code></pre>
 </dd></dl>
<p> The last is particularly useful because it knows about machine-dependent architectures. The <code>&quot;lib.pm&quot;</code> pragmatic module was first included with the 5.002 release of Perl.  </p>
<h3>Where are modules installed?</h3>
<p> Modules are installed on a case-by-case basis (as provided by the methods described in the previous section), and in the operating system. All of these paths are stored in <code>@INC</code>, which you can display with the one-liner </p>
<pre><code>    perl -e 'print join(&quot;\n&quot;,@INC,&quot;&quot;)'
</code></pre>
<p> The same information is displayed at the end of the output from the command </p>
<pre><code>    perl -V
</code></pre>
<p> To find out where a module&#8217;s source code is located, use </p>
<pre><code>    perldoc -l Encode
</code></pre>
<p> to display the path to the module. In some cases (for example, the <code>&quot;AutoLoader&quot;</code> module), this command will show the path to a separate <code>&quot;pod&quot;</code> file; the module itself should be in the same directory, with a &#8216;pm&#8217; file extension.  </p>
<h3>What is socket.ph and where do I get it?</h3>
<p> It&#8217;s a Perl 4 style file defining values for system networking constants. Sometimes it is built using h2ph when Perl is installed, but other times it is not. Modern programs should use <code>&quot;use Socket;&quot;</code> instead.  </p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples in this file are hereby placed into the public domain. You are permitted and encouraged to use this code in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit would be courteous but is not required. </p>
