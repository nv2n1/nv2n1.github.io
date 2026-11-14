---
title: "perlport(1)"
name: "perlport"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlport/"
---

<h2 class="name">NAME</h2>
 

 perlport - Writing portable Perl 

<h2>DESCRIPTION</h2>

 Perl runs on numerous operating systems. While most of them share much in common, they also have their own unique features. 

 This document is meant to help you to find out what constitutes portable Perl code. That way once you make a decision to write portably, you know where the lines are drawn, and you can stay within them. 

 There is a tradeoff between taking full advantage of one particular type of computer and taking advantage of a full range of them. Naturally, as you broaden your range and become more diverse, the common factors drop, and you are left with an increasingly smaller area of common ground in which you can operate to accomplish a particular task. Thus, when you begin attacking a problem, it is important to consider under which part of the tradeoff curve you want to operate. Specifically, you must decide whether it is important that the task that you are coding has the full generality of being portable, or whether to just get the job done right now. This is the hardest choice to be made. The rest is easy, because Perl provides many choices, whichever way you want to approach your problem. 

 Looking at it another way, writing portable code is usually about willfully limiting your available choices. Naturally, it takes discipline and sacrifice to do that. The product of portability and convenience may be a constant. You have been warned. 

 Be aware of two important points:
<dl>
<dt>Not all Perl programs have to be portable
<dd> There is no reason you should not use Perl as a language to glue Unix tools together, or to prototype a Macintosh application, or to manage the Windows registry. If it makes no sense to aim for portability for one reason or another in a given program, then don't bother.
<dt>Nearly all of Perl already <i>is</i> portable
<dd> Don't be fooled into thinking that it is hard to create portable Perl code. It isn't. Perl tries its level-best to bridge the gaps between what's available on different platforms, and all the means available to use those features. Thus almost all Perl code runs on any machine without modification. But there are some significant issues in writing portable code, and this document is entirely about those issues.</dl>
 

 Here's the general rule: When you approach a task commonly done using a whole range of platforms, think about writing portable code. That way, you don't sacrifice much by way of the implementation choices you can avail yourself of, and at the same time you can give your users lots of platform choices. On the other hand, when you have to take advantage of some unique feature of a particular platform, as is often the case with systems programming (whether for Unix, Windows, <font SIZE="-1">VMS,</font> etc.), consider writing platform-specific code. 

 When the code will run on only two or three operating systems, you may need to consider only the differences of those particular systems. The important thing is to decide where the code will run and to be deliberate in your decision. 

 The material below is separated into three main sections: main issues of portability (``<font SIZE="-1">ISSUES''</font>), platform-specific issues (``<font SIZE="-1">PLATFORMS''</font>), and built-in Perl functions that behave differently on various ports (``<font SIZE="-1">FUNCTION IMPLEMENTATIONS''</font>). 

 This information should not be considered complete; it includes possibly transient information about idiosyncrasies of some of the ports, almost all of which are in a state of constant evolution. Thus, this material should be considered a perpetual work in progress (<tt>&quot;&lt;IMG SRC=&quot;yellow_sign.gif&quot; ALT=&quot;Under Construction&quot;&gt;&quot;</tt>).

<h2>ISSUES</h2>

<h3>Newlines</h3>

 In most operating systems, lines in files are terminated by newlines. Just what is used as a newline may vary from <font SIZE="-1">OS</font> to <font SIZE="-1">OS.</font> Unix traditionally uses <tt>&quot;\012&quot;</tt>, one type of DOSish I/O uses <tt>&quot;\015\012&quot;</tt>, Mac OS uses <tt>&quot;\015&quot;</tt>, and z/OS uses <tt>&quot;\025&quot;</tt>. 

 Perl uses <tt>&quot;\n&quot;</tt> to represent the ``logical'' newline, where what is logical may depend on the platform in use. In MacPerl, <tt>&quot;\n&quot;</tt> always means <tt>&quot;\015&quot;</tt>. On <font SIZE="-1">EBCDIC</font> platforms, <tt>&quot;\n&quot;</tt> could be <tt>&quot;\025&quot;</tt> or <tt>&quot;\045&quot;</tt>. In DOSish perls, <tt>&quot;\n&quot;</tt> usually means <tt>&quot;\012&quot;</tt>, but when accessing a file in ``text'' mode, perl uses the <tt>&quot;:crlf&quot;</tt> layer that translates it to (or from) <tt>&quot;\015\012&quot;</tt>, depending on whether you're reading or writing. Unix does the same thing on ttys in canonical mode. <tt>&quot;\015\012&quot;</tt> is commonly referred to as <font SIZE="-1">CRLF.</font> 

 To trim trailing newlines from text lines use <tt>&quot;chomp&quot;</tt>. With default settings that function looks for a trailing <tt>&quot;\n&quot;</tt> character and thus trims in a portable way. 

 When dealing with binary files (or text files in binary mode) be sure to explicitly set <tt>$/</tt> to the appropriate value for your file format before using <tt>&quot;chomp&quot;</tt>. 

 Because of the ``text'' mode translation, DOSish perls have limitations in using <tt>&quot;seek&quot;</tt> and <tt>&quot;tell&quot;</tt> on a file accessed in ``text'' mode. Stick to <tt>&quot;seek&quot;</tt>-ing to locations you got from <tt>&quot;tell&quot;</tt> (and no others), and you are usually free to use <tt>&quot;seek&quot;</tt> and <tt>&quot;tell&quot;</tt> even in ``text'' mode. Using <tt>&quot;seek&quot;</tt> or <tt>&quot;tell&quot;</tt> or other file operations may be non-portable. If you use <tt>&quot;binmode&quot;</tt> on a file, however, you can usually <tt>&quot;seek&quot;</tt> and <tt>&quot;tell&quot;</tt> with arbitrary values safely. 

 A common misconception in socket programming is that <tt>&quot;\n eq \012&quot;</tt> everywhere. When using protocols such as common Internet protocols, <tt>&quot;\012&quot;</tt> and <tt>&quot;\015&quot;</tt> are called for specifically, and the values of the logical <tt>&quot;\n&quot;</tt> and <tt>&quot;\r&quot;</tt> (carriage return) are not reliable. 

 <pre>
    print $socket &quot;Hi there, client!\r\n&quot;;      # WRONG
    print $socket &quot;Hi there, client!\015\012&quot;;  # RIGHT
</pre> 

 However, using <tt>&quot;\015\012&quot;</tt> (or <tt>&quot;\cM\cJ&quot;</tt>, or <tt>&quot;\x0D\x0A&quot;</tt>) can be tedious and unsightly, as well as confusing to those maintaining the code. As such, the <tt>&quot;Socket&quot;</tt> module supplies the Right Thing for those who want it. 

 <pre>
    use Socket qw(:DEFAULT :crlf);
    print $socket &quot;Hi there, client!$CRLF&quot;      # RIGHT
</pre> 

 When reading from a socket, remember that the default input record separator <tt>$/</tt> is <tt>&quot;\n&quot;</tt>, but robust socket code will recognize as either <tt>&quot;\012&quot;</tt> or <tt>&quot;\015\012&quot;</tt> as end of line: 

 <pre>
    while (&lt;$socket&gt;) {  # NOT ADVISABLE!
        # ...
    }
</pre> 

 Because both <font SIZE="-1">CRLF</font> and <font SIZE="-1">LF</font> end in <font SIZE="-1">LF,</font> the input record separator can be set to <font SIZE="-1">LF</font> and any <font SIZE="-1">CR</font> stripped later. Better to write: 

 <pre><code>
use Socket qw(
    : DEFAULT
    : crlf);
local($ /) = LF;
#not needed if $ / is already \012 while (&lt;$socket&gt;)
{
    s / $CR ? $LF /\n / ;
#not sure if socket uses LF or CRLF, OK
#s /\015 ?\012 /\n / ; #same thing
}
</code></pre> 

 This example is preferred over the previous one---even for Unix platforms---because now any <tt>&quot;\015&quot;</tt>'s (<tt>&quot;\cM&quot;</tt>'s) are stripped out (and there was much rejoicing). 

 Similarly, functions that return text data---such as a function that fetches a web page---should sometimes translate newlines before returning the data, if they've not yet been translated to the local newline representation. A single line of code will often suffice: 

 <pre>
    $data =~ s/\015?\012/\n/g;
    return $data;
</pre> 

 Some of this may be confusing. Here's a handy reference to the <font SIZE="-1">ASCII CR</font> and <font SIZE="-1">LF</font> characters. You can print it out and stick it in your wallet. 

 
LF eq  \012 eq  \x0A eq  \cJ eq chr(10) eq ASCII 10 CR eq  \015 eq  \x0D eq  \cM eq chr(13) eq ASCII 13 | Unix | DOS | Mac |
    -- -- -- -- -- -- -- -- -- -- -- -- -- -
        \n | LF | LF | CR |
        \r | CR | CR | LF |
        \n * | LF | CRLF | CR |
        \r * | CR | CR | LF |
    -- -- -- -- -- -- -- -- -- -- -- -- -- -*text - mode STDIO
 

 The Unix column assumes that you are not accessing a serial line (like a tty) in canonical mode. If you are, then <font SIZE="-1">CR</font> on input becomes ``\n'', and ``\n'' on output becomes <font SIZE="-1">CRLF.</font> 

 These are just the most common definitions of <tt>&quot;\n&quot;</tt> and <tt>&quot;\r&quot;</tt> in Perl. There may well be others. For example, on an <font SIZE="-1">EBCDIC</font> implementation such as z/OS (<font SIZE="-1">OS/390</font>) or <font SIZE="-1">OS/400</font> (using the <font SIZE="-1">ILE,</font> the <font SIZE="-1">PASE</font> is ASCII-based) the above material is similar to ``Unix'' but the code numbers change: 

 
LF eq  \025 eq  \x15 eq  \cU eq chr(21) eq CP - 1047 21 LF eq  \045 eq  \x25 eq chr(37) eq CP - 0037 37 CR eq  \015 eq  \x0D eq  \cM eq chr(13) eq CP - 1047 13 CR eq  \015 eq  \x0D eq  \cM eq chr(13) eq CP - 0037 13 | z / OS | OS / 400 |
    -- -- -- -- -- -- -- -- -- -- --
        \n | LF | LF |
        \r | CR | CR |
        \n * | LF | LF |
        \r * | CR | CR |
    -- -- -- -- -- -- -- -- -- -- --*text - mode STDIO


<h3>Numbers endianness and Width</h3>

 Different CPUs store integers and floating point numbers in different orders (called <i>endianness</i>) and widths (32-bit and 64-bit being the most common today). This affects your programs when they attempt to transfer numbers in binary format from one <font SIZE="-1">CPU</font> architecture to another, usually either ``live'' via network connection, or by storing the numbers to secondary storage such as a disk file or tape. 

 Conflicting storage orders make an utter mess out of the numbers. If a little-endian host (Intel, <font SIZE="-1">VAX</font>) stores 0x12345678 (305419896 in decimal), a big-endian host (Motorola, Sparc, <font SIZE="-1">PA</font>) reads it as 0x78563412 (2018915346 in decimal). Alpha and <font SIZE="-1">MIPS</font> can be either: Digital/Compaq used/uses them in little-endian mode; SGI/Cray uses them in big-endian mode. To avoid this problem in network (socket) connections use the <tt>&quot;pack&quot;</tt> and <tt>&quot;unpack&quot;</tt> formats <tt>&quot;n&quot;</tt> and <tt>&quot;N&quot;</tt>, the ``network'' orders. These are guaranteed to be portable. 

 As of Perl 5.10.0, you can also use the <tt>&quot;&gt;&quot;</tt> and <tt>&quot;&lt;&quot;</tt> modifiers to force big- or little-endian byte-order. This is useful if you want to store signed integers or 64-bit integers, for example. 

 You can explore the endianness of your platform by unpacking a data structure packed in native format such as: 

 <pre>
    print unpack(&quot;h*&quot;, pack(&quot;s2&quot;, 1, 2)), &quot;\n&quot;;
    # '10002000' on e.g. Intel x86 or Alpha 21064 in little-endian mode
    # '00100020' on e.g. Motorola 68040
</pre> 

 If you need to distinguish between endian architectures you could use either of the variables set like so: 

 
$is_big_endian = unpack("h*", pack("s", 1)) = ~ / 01 / ;
$is_little_endian = unpack("h*", pack("s", 1)) = ~ / ^1 / ;
 

 Differing widths can cause truncation even between platforms of equal endianness. The platform of shorter width loses the upper parts of the number. There is no good solution for this problem except to avoid transferring or storing raw binary numbers. 

 One can circumnavigate both these problems in two ways. Either transfer and store numbers always in text format, instead of raw binary, or else consider using modules like <tt>&quot;Data::Dumper&quot;</tt> and <tt>&quot;Storable&quot;</tt> (included as of Perl 5.8). Keeping all data as text significantly simplifies matters.

<h3>Files and Filesystems</h3>

 Most platforms these days structure files in a hierarchical fashion. So, it is reasonably safe to assume that all platforms support the notion of a ``path'' to uniquely identify a file on the system. How that path is really written, though, differs considerably. 

 Although similar, file path specifications differ between Unix, Windows, Mac OS, <font SIZE="-1">OS/2, VMS, VOS,</font> RISC OS, and probably others. Unix, for example, is one of the few OSes that has the elegant idea of a single root directory. 

 <font SIZE="-1">DOS, OS/2, VMS, VOS,</font> and Windows can work similarly to Unix with <tt>&quot;/&quot;</tt> as path separator, or in their own idiosyncratic ways (such as having several root directories and various ``unrooted'' device files such <font SIZE="-1">NIL:</font> and <font SIZE="-1">LPT:</font>). 

 Mac OS 9 and earlier used <tt>&quot;:&quot;</tt> as a path separator instead of <tt>&quot;/&quot;</tt>. 

 The filesystem may support neither hard links (<tt>&quot;link&quot;</tt>) nor symbolic links (<tt>&quot;symlink&quot;</tt>, <tt>&quot;readlink&quot;</tt>, <tt>&quot;lstat&quot;</tt>). 

 The filesystem may support neither access timestamp nor change timestamp (meaning that about the only portable timestamp is the modification timestamp), or one second granularity of any timestamps (e.g. the <font SIZE="-1">FAT</font> filesystem limits the time granularity to two seconds). 

 The ``inode change timestamp'' (the <tt>&quot;-C&quot;</tt> filetest) may really be the ``creation timestamp'' (which it is not in Unix). 

 <font SIZE="-1">VOS</font> perl can emulate Unix filenames with <tt>&quot;/&quot;</tt> as path separator. The native pathname characters greater-than, less-than, number-sign, and percent-sign are always accepted. 

 RISC OS perl can emulate Unix filenames with <tt>&quot;/&quot;</tt> as path separator, or go native and use <tt>&quot;.&quot;</tt> for path separator and <tt>&quot;:&quot;</tt> to signal filesystems and disk names. 

 Don't assume Unix filesystem access semantics: that read, write, and execute are all the permissions there are, and even if they exist, that their semantics (for example what do <tt>&quot;r&quot;</tt>, <tt>&quot;w&quot;</tt>, and <tt>&quot;x&quot;</tt> mean on a directory) are the Unix ones. The various Unix/POSIX compatibility layers usually try to make interfaces like <tt>&quot;chmod&quot;</tt> work, but sometimes there simply is no good mapping. 

 The <tt>&quot;File::Spec&quot;</tt> modules provide methods to manipulate path specifications and return the results in native format for each platform. This is often unnecessary as Unix-style paths are understood by Perl on every supported platform, but if you need to produce native paths for a native utility that does not understand Unix syntax, or if you are operating on paths or path components in unknown (and thus possibly native) syntax, <tt>&quot;File::Spec&quot;</tt> is your friend. Here are two brief examples: 

 
use File::Spec::Functions;
chdir(updir());
#go up one directory
#Concatenate a path from its components
    my $file = catfile(updir(), 'temp', 'file.txt');
#on Unix : '../temp/file.txt'
#on Win32 : '..\temp\file.txt'
#on VMS : '[-.temp]file.txt'
 

 In general, production code should not have file paths hardcoded. Making them user-supplied or read from a configuration file is better, keeping in mind that file path syntax varies on different machines. 

 This is especially noticeable in scripts like Makefiles and test suites, which often assume <tt>&quot;/&quot;</tt> as a path separator for subdirectories. 

 Also of use is <tt>&quot;File::Basename&quot;</tt> from the standard distribution, which splits a pathname into pieces (base filename, full path to directory, and file suffix). 

 Even when on a single platform (if you can call Unix a single platform), remember not to count on the existence or the contents of particular system-specific files or directories, like <i>/etc/passwd</i>, <i>/etc/sendmail.conf</i>, <i>/etc/resolv.conf</i>, or even <i>/tmp/</i>. For example, <i>/etc/passwd</i> may exist but not contain the encrypted passwords, because the system is using some form of enhanced security. Or it may not contain all the accounts, because the system is using <font SIZE="-1">NIS.</font> If code does need to rely on such a file, include a description of the file and its format in the code's documentation, then make it easy for the user to override the default location of the file. 

 Don't assume a text file will end with a newline. They should, but people forget. 

 Do not have two files or directories of the same name with different case, like <i>test.pl</i> and <i>Test.pl</i>, as many platforms have case-insensitive (or at least case-forgiving) filenames. Also, try not to have non-word characters (except for <tt>&quot;.&quot;</tt>) in the names, and keep them to the 8.3 convention, for maximum portability, onerous a burden though this may appear. 

 Likewise, when using the <tt>&quot;AutoSplit&quot;</tt> module, try to keep your functions to 8.3 naming and case-insensitive conventions; or, at the least, make it so the resulting files have a unique (case-insensitively) first 8 characters. 

 Whitespace in filenames is tolerated on most systems, but not all, and even on systems where it might be tolerated, some utilities might become confused by such whitespace. 

 Many systems (<font SIZE="-1">DOS, VMS ODS-2</font>) cannot have more than one <tt>&quot;.&quot;</tt> in their filenames. 

 Don't assume <tt>&quot;&gt;&quot;</tt> won't be the first character of a filename. Always use the three-arg version of <tt>&quot;open&quot;</tt>: 

 <pre>
    open my $fh, '&lt;', $existing_file) or die $!;
</pre> 

 Two-arg <tt>&quot;open&quot;</tt> is magic and can translate characters like <tt>&quot;&gt;&quot;</tt>, <tt>&quot;&lt;&quot;</tt>, and <tt>&quot;|&quot;</tt> in filenames, which is usually the wrong thing to do. <tt>&quot;sysopen&quot;</tt> and three-arg <tt>&quot;open&quot;</tt> don't have this problem. 

 Don't use <tt>&quot;:&quot;</tt> as a part of a filename since many systems use that for their own semantics (Mac <font SIZE="-1">OS</font> Classic for separating pathname components, many networking schemes and utilities for separating the nodename and the pathname, and so on). For the same reasons, avoid <tt>&quot;@&quot;</tt>, <tt>&quot;;&quot;</tt> and <tt>&quot;|&quot;</tt>. 

 Don't assume that in pathnames you can collapse two leading slashes <tt>&quot;//&quot;</tt> into one: some networking and clustering filesystems have special semantics for that. Let the operating system sort it out. 

 The <i>portable filename characters</i> as defined by <font SIZE="-1">ANSI C</font> are 

 <pre>
 a b c d e f g h i j k l m n o p q r s t u v w x y z
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
 0 1 2 3 4 5 6 7 8 9
 . _ -
</pre> 

 and <tt>&quot;-&quot;</tt> shouldn't be the first character. If you want to be hypercorrect, stay case-insensitive and within the 8.3 naming convention (all the files and directories have to be unique within one directory if their names are lowercased and truncated to eight characters before the <tt>&quot;.&quot;</tt>, if any, and to three characters after the <tt>&quot;.&quot;</tt>, if any). (And do not use <tt>&quot;.&quot;</tt>s in directory names.)

<h3>System Interaction</h3>

 Not all platforms provide a command line. These are usually platforms that rely primarily on a Graphical User Interface (<font SIZE="-1">GUI</font>) for user interaction. A program requiring a command line interface might not work everywhere. This is probably for the user of the program to deal with, so don't stay up late worrying about it. 

 Some platforms can't delete or rename files held open by the system, this limitation may also apply to changing filesystem metainformation like file permissions or owners. Remember to <tt>&quot;close&quot;</tt> files when you are done with them. Don't <tt>&quot;unlink&quot;</tt> or <tt>&quot;rename&quot;</tt> an open file. Don't <tt>&quot;tie&quot;</tt> or <tt>&quot;open&quot;</tt> a file already tied or opened; <tt>&quot;untie&quot;</tt> or <tt>&quot;close&quot;</tt> it first. 

 Don't open the same file more than once at a time for writing, as some operating systems put mandatory locks on such files. 

 Don't assume that write/modify permission on a directory gives the right to add or delete files/directories in that directory. That is filesystem specific: in some filesystems you need write/modify permission also (or even just) in the file/directory itself. In some filesystems (<font SIZE="-1">AFS, DFS</font>) the permission to add/delete directory entries is a completely separate permission. 

 Don't assume that a single <tt>&quot;unlink&quot;</tt> completely gets rid of the file: some filesystems (most notably the ones in <font SIZE="-1">VMS</font>) have versioned filesystems, and <tt>&quot;unlink&quot;</tt> removes only the most recent one (it doesn't remove all the versions because by default the native tools on those platforms remove just the most recent version, too). The portable idiom to remove all the versions of a file is 

 <pre>
    1 while unlink &quot;file&quot;;
</pre> 

 This will terminate if the file is undeletable for some reason (protected, not there, and so on). 

 Don't count on a specific environment variable existing in <tt>%ENV</tt>. Don't count on <tt>%ENV</tt> entries being case-sensitive, or even case-preserving. Don't try to clear <tt>%ENV</tt> by saying <tt>&quot;%ENV = ();&quot;</tt>, or, if you really have to, make it conditional on <tt>&quot;$^O ne 'VMS'&quot;</tt> since in <font SIZE="-1">VMS</font> the <tt>%ENV</tt> table is much more than a per-process key-value string table. 

 On <font SIZE="-1">VMS,</font> some entries in the <tt>%ENV</tt> hash are dynamically created when their key is used on a read if they did not previously exist. The values for <tt>$ENV{HOME}</tt>, <tt>$ENV{TERM}</tt>, <tt>$ENV{PATH}</tt>, and <tt>$ENV{USER}</tt>, are known to be dynamically generated. The specific names that are dynamically generated may vary with the version of the C library on <font SIZE="-1">VMS,</font> and more may exist than are documented. 

 On <font SIZE="-1">VMS</font> by default, changes to the <tt>%ENV</tt> hash persist after perl exits. Subsequent invocations of perl in the same process can inadvertently inherit environment settings that were meant to be temporary. 

 Don't count on signals or <tt>%SIG</tt> for anything. 

 Don't count on filename globbing. Use <tt>&quot;opendir&quot;</tt>, <tt>&quot;readdir&quot;</tt>, and <tt>&quot;closedir&quot;</tt> instead. 

 Don't count on per-program environment variables, or per-program current directories. 

 Don't count on specific values of <tt>$!</tt>, neither numeric nor especially the string values. Users may switch their locales causing error messages to be translated into their languages. If you can trust a POSIXish environment, you can portably use the symbols defined by the <tt>&quot;Errno&quot;</tt> module, like <tt>&quot;ENOENT&quot;</tt>. And don't trust on the values of <tt>$!</tt> at all except immediately after a failed system call.

<h3>Command names versus file pathnames</h3>

 Don't assume that the name used to invoke a command or program with <tt>&quot;system&quot;</tt> or <tt>&quot;exec&quot;</tt> can also be used to test for the existence of the file that holds the executable code for that command or program. First, many systems have ``internal'' commands that are built-in to the shell or <font SIZE="-1">OS</font> and while these commands can be invoked, there is no corresponding file. Second, some operating systems (e.g., Cygwin, <font SIZE="-1">DJGPP, OS/2,</font> and <font SIZE="-1">VOS</font>) have required suffixes for executable files; these suffixes are generally permitted on the command name but are not required. Thus, a command like <tt>&quot;perl&quot;</tt> might exist in a file named <i>perl</i>, <i>perl.exe</i>, or <i>perl.pm</i>, depending on the operating system. The variable <tt>$Config{_exe}</tt> in the <tt>&quot;Config&quot;</tt> module holds the executable suffix, if any. Third, the <font SIZE="-1">VMS</font> port carefully sets up <tt>$^X</tt> and <tt>$Config{perlpath}</tt> so that no further processing is required. This is just as well, because the matching regular expression used below would then have to deal with a possible trailing version number in the <font SIZE="-1">VMS</font> file name. 

 To convert <tt>$^X</tt> to a file pathname, taking account of the requirements of the various operating system possibilities, say: 

 
use Config;
my $thisperl = $ ^ X;
if ($ ^ O ne 'VMS') {
    $thisperl.= $Config{_exe} unless $thisperl = ~m /\Q$Config
    {
        _exe
    }
    \E$ / i;
}
 

 To convert <tt>$Config{perlpath}</tt> to a file pathname, say: 

 
use Config;
my $thisperl = $Config{perlpath};
if ($ ^ O ne 'VMS') {
    $thisperl.= $Config{_exe} unless $thisperl = ~m /\Q$Config
    {
        _exe
    }
    \E$ / i;
}


<h3>Networking</h3>

 Don't assume that you can reach the public Internet. 

 Don't assume that there is only one way to get through firewalls to the public Internet. 

 Don't assume that you can reach outside world through any other port than 80, or some web proxy. ftp is blocked by many firewalls. 

 Don't assume that you can send email by connecting to the local <font SIZE="-1">SMTP</font> port. 

 Don't assume that you can reach yourself or any node by the name 'localhost'. The same goes for '127.0.0.1'. You will have to try both. 

 Don't assume that the host has only one network card, or that it can't bind to many virtual <font SIZE="-1">IP</font> addresses. 

 Don't assume a particular network device name. 

 Don't assume a particular set of <tt>&quot;ioctl&quot;</tt>s will work. 

 Don't assume that you can ping hosts and get replies. 

 Don't assume that any particular port (service) will respond. 

 Don't assume that <tt>&quot;Sys::Hostname&quot;</tt> (or any other <font SIZE="-1">API</font> or command) returns either a fully qualified hostname or a non-qualified hostname: it all depends on how the system had been configured. Also remember that for things such as <font SIZE="-1">DHCP</font> and <font SIZE="-1">NAT,</font> the hostname you get back might not be very useful. 

 All the above <i>don't</i>s may look daunting, and they are, but the key is to degrade gracefully if one cannot reach the particular network service one wants. Croaking or hanging do not look very professional.

<h3>Interprocess Communication (<font SIZE="-1">IPC</font>)</h3>

 In general, don't directly access the system in code meant to be portable. That means, no <tt>&quot;system&quot;</tt>, <tt>&quot;exec&quot;</tt>, <tt>&quot;fork&quot;</tt>, <tt>&quot;pipe&quot;</tt>, <tt>&quot;``&quot;</tt> or <tt>&quot;qx//&quot;</tt>, <tt>&quot;open&quot;</tt> with a <tt>&quot;|&quot;</tt>, nor any of the other things that makes being a Perl hacker worth being. 

 Commands that launch external processes are generally supported on most platforms (though many of them do not support any type of forking). The problem with using them arises from what you invoke them on. External tools are often named differently on different platforms, may not be available in the same location, might accept different arguments, can behave differently, and often present their results in a platform-dependent way. Thus, you should seldom depend on them to produce consistent results. (Then again, if you're calling <tt>&quot;netstat -a&quot;</tt>, you probably don't expect it to run on both Unix and <font SIZE="-1">CP/M.</font>) 

 One especially common bit of Perl code is opening a pipe to <b>sendmail</b>: 

 <pre>
    open(my $mail, '|-', '/usr/lib/sendmail -t')
        or die &quot;cannot fork sendmail: $!&quot;;
</pre> 

 This is fine for systems programming when sendmail is known to be available. But it is not fine for many non-Unix systems, and even some Unix systems that may not have sendmail installed. If a portable solution is needed, see the various distributions on <font SIZE="-1">CPAN</font> that deal with it. <tt>&quot;Mail::Mailer&quot;</tt> and <tt>&quot;Mail::Send&quot;</tt> in the <tt>&quot;MailTools&quot;</tt> distribution are commonly used, and provide several mailing methods, including <tt>&quot;mail&quot;</tt>, <tt>&quot;sendmail&quot;</tt>, and direct <font SIZE="-1">SMTP</font> (via <tt>&quot;Net::SMTP&quot;</tt>) if a mail transfer agent is not available. <tt>&quot;Mail::Sendmail&quot;</tt> is a standalone module that provides simple, platform-independent mailing. 

 The Unix System V <font SIZE="-1">IPC</font> (<tt>&quot;msg*(), sem*(), shm*()&quot;</tt>) is not available even on all Unix platforms. 

 Do not use either the bare result of <tt>&quot;pack(&quot;N&quot;, 10, 20, 30, 40)&quot;</tt> or bare v-strings (such as <tt>&quot;v10.20.30.40&quot;</tt>) to represent IPv4 addresses: both forms just pack the four bytes into network order. That this would be equal to the C language <tt>&quot;in_addr&quot;</tt> struct (which is what the socket code internally uses) is not guaranteed. To be portable use the routines of the <tt>&quot;Socket&quot;</tt> module, such as <tt>&quot;inet_aton&quot;</tt>, <tt>&quot;inet_ntoa&quot;</tt>, and <tt>&quot;sockaddr_in&quot;</tt>. 

 The rule of thumb for portable code is: Do it all in portable Perl, or use a module (that may internally implement it with platform-specific code, but exposes a common interface).

<h3>External Subroutines (<font SIZE="-1">XS</font>)</h3>

 <font SIZE="-1">XS</font> code can usually be made to work with any platform, but dependent libraries, header files, etc., might not be readily available or portable, or the <font SIZE="-1">XS</font> code itself might be platform-specific, just as Perl code might be. If the libraries and headers are portable, then it is normally reasonable to make sure the <font SIZE="-1">XS</font> code is portable, too. 

 A different type of portability issue arises when writing <font SIZE="-1">XS</font> code: availability of a C compiler on the end-user's system. C brings with it its own portability issues, and writing <font SIZE="-1">XS</font> code will expose you to some of those. Writing purely in Perl is an easier way to achieve portability.

<h3>Standard Modules</h3>

 In general, the standard modules work across platforms. Notable exceptions are the <tt>&quot;CPAN&quot;</tt> module (which currently makes connections to external programs that may not be available), platform-specific modules (like <tt>&quot;ExtUtils::MM_VMS&quot;</tt>), and <font SIZE="-1">DBM</font> modules. 

 There is no one <font SIZE="-1">DBM</font> module available on all platforms. <tt>&quot;SDBM_File&quot;</tt> and the others are generally available on all Unix and DOSish ports, but not in MacPerl, where only <tt>&quot;NDBM_File&quot;</tt> and <tt>&quot;DB_File&quot;</tt> are available. 

 The good news is that at least some <font SIZE="-1">DBM</font> module should be available, and <tt>&quot;AnyDBM_File&quot;</tt> will use whichever module it can find. Of course, then the code needs to be fairly strict, dropping to the greatest common factor (e.g., not exceeding 1K for each record), so that it will work with any <font SIZE="-1">DBM</font> module. See AnyDBM_File for more details.

<h3>Time and Date</h3>

 The system's notion of time of day and calendar date is controlled in widely different ways. Don't assume the timezone is stored in <tt>$ENV{TZ}</tt>, and even if it is, don't assume that you can control the timezone through that variable. Don't assume anything about the three-letter timezone abbreviations (for example that <font SIZE="-1">MST</font> would be the Mountain Standard Time, it's been known to stand for Moscow Standard Time). If you need to use timezones, express them in some unambiguous format like the exact number of minutes offset from <font SIZE="-1">UTC,</font> or the <font SIZE="-1">POSIX</font> timezone format. 

 Don't assume that the epoch starts at 00:00:00, January 1, 1970, because that is <font SIZE="-1">OS-</font> and implementation-specific. It is better to store a date in an unambiguous representation. The <font SIZE="-1">ISO 8601</font> standard defines YYYY-MM-DD as the date format, or <font SIZE="-1">YYYY-MM-DDTHH:MM:SS</font> (that's a literal ``T'' separating the date from the time). Please do use the <font SIZE="-1">ISO 8601</font> instead of making us guess what date 02/03/04 might be. <font SIZE="-1">ISO 8601</font> even sorts nicely as-is. A text representation (like ``1987-12-18'') can be easily converted into an OS-specific value using a module like <tt>&quot;Time::Piece&quot;</tt> (see ``Date Parsing'' in Time::Piece) or <tt>&quot;Date::Parse&quot;</tt>. An array of values, such as those returned by <tt>&quot;localtime&quot;</tt>, can be converted to an OS-specific representation using <tt>&quot;Time::Local&quot;</tt>. 

 When calculating specific times, such as for tests in time or date modules, it may be appropriate to calculate an offset for the epoch. 

 
use Time::Local qw(timegm);
my $offset = timegm(0, 0, 0, 1, 0, 70);
 

 The value for <tt>$offset</tt> in Unix will be <tt>0</tt>, but in Mac <font SIZE="-1">OS</font> Classic will be some large number. <tt>$offset</tt> can then be added to a Unix time value to get what should be the proper value on any system.

<h3>Character sets and character encoding</h3>

 Assume very little about character sets. 

 Assume nothing about numerical values (<tt>&quot;ord&quot;</tt>, <tt>&quot;chr&quot;</tt>) of characters. Do not use explicit code point ranges (like <tt>&quot;\xHH-\xHH)&quot;</tt>. However, starting in Perl v5.22, regular expression pattern bracketed character class ranges specified like <tt>&quot;qr/[\N{U+HH}-\N{U+HH}]/&quot;</tt> are portable, and starting in Perl v5.24, the same ranges are portable in <tt>&quot;tr///&quot;</tt>. You can portably use symbolic character classes like <tt>&quot;[:print:]&quot;</tt>. 

 Do not assume that the alphabetic characters are encoded contiguously (in the numeric sense). There may be gaps. Special coding in Perl, however, guarantees that all subsets of <tt>&quot;qr/[A-Z]/&quot;</tt>, <tt>&quot;qr/[a-z]/&quot;</tt>, and <tt>&quot;qr/[0-9]/&quot;</tt> behave as expected. <tt>&quot;tr///&quot;</tt> behaves the same for these ranges. In patterns, any ranges specified with end points using the <tt>&quot;\N{...}&quot;</tt> notations ensures character set portability, but it is a bug in Perl v5.22 that this isn't true of <tt>&quot;tr///&quot;</tt>, fixed in v5.24. 

 Do not assume anything about the ordering of the characters. The lowercase letters may come before or after the uppercase letters; the lowercase and uppercase may be interlaced so that both ``a'' and ``A'' come before ``b''; the accented and other international characters may be interlaced so that ä comes before ``b''. Unicode::Collate can be used to sort this all out.

<h3>Internationalisation</h3>

 If you may assume <font SIZE="-1">POSIX</font> (a rather large assumption), you may read more about the <font SIZE="-1">POSIX</font> locale system from perllocale. The locale system at least attempts to make things a little bit more portable, or at least more convenient and native-friendly for non-English users. The system affects character sets and encoding, and date and time formatting---amongst other things. 

 If you really want to be international, you should consider Unicode. See perluniintro and perlunicode for more information. 

 By default Perl assumes your source code is written in an 8-bit <font SIZE="-1">ASCII</font> superset. To embed Unicode characters in your strings and regexes, you can use the <tt>&quot;\x{HH}&quot;</tt> or (more portably) <tt>&quot;\N{U+HH}&quot;</tt> notations. You can also use the <tt>&quot;utf8&quot;</tt> pragma and write your code in <font SIZE="-1">UTF-8,</font> which lets you use Unicode characters directly (not just in quoted constructs but also in identifiers).

<h3>System Resources</h3>

 If your code is destined for systems with severely constrained (or missing!) virtual memory systems then you want to be <i>especially</i> mindful of avoiding wasteful constructs such as: 

 
my @lines = &lt;$very_large_file&gt;;
#bad while (&lt;$fh&gt;){$file.= $_ } #sometimes bad
                       my $file = join('', &lt;$fh&gt;);
#better
 

 The last two constructs may appear unintuitive to most people. The first repeatedly grows a string, whereas the second allocates a large chunk of memory in one go. On some systems, the second is more efficient than the first.

<h3>Security</h3>

 Most multi-user platforms provide basic levels of security, usually implemented at the filesystem level. Some, however, unfortunately do not. Thus the notion of user id, or ``home'' directory, or even the state of being logged-in, may be unrecognizable on many platforms. If you write programs that are security-conscious, it is usually best to know what type of system you will be running under so that you can write code explicitly for that platform (or class of platforms). 

 Don't assume the Unix filesystem access semantics: the operating system or the filesystem may be using some <font SIZE="-1">ACL</font> systems, which are richer languages than the usual <tt>&quot;rwx&quot;</tt>. Even if the <tt>&quot;rwx&quot;</tt> exist, their semantics might be different. 

 (From the security viewpoint, testing for permissions before attempting to do something is silly anyway: if one tries this, there is potential for race conditions. Someone or something might change the permissions between the permissions check and the actual operation. Just try the operation.) 

 Don't assume the Unix user and group semantics: especially, don't expect <tt>$&lt;</tt> and <tt>$&gt;</tt> (or <tt>$(</tt> and <tt>$)</tt>) to work for switching identities (or memberships). 

 Don't assume set-uid and set-gid semantics. (And even if you do, think twice: set-uid and set-gid are a known can of security worms.)

<h3>Style</h3>

 For those times when it is necessary to have platform-specific code, consider keeping the platform-specific code in one place, making porting to other platforms easier. Use the <tt>&quot;Config&quot;</tt> module and the special variable <tt>$^O</tt> to differentiate platforms, as described in ``<font SIZE="-1">PLATFORMS''</font>. 

 Beware of the ``else syndrome'': 

 
if ($ ^ O eq 'MSWin32') {
#code that assumes Windows
} else {
#code that assumes Linux
}
 

 The <tt>&quot;else&quot;</tt> branch should be used for the really ultimate fallback, not for code specific to some platform. 

 Be careful in the tests you supply with your module or programs. Module code may be fully portable, but its tests might not be. This often happens when tests spawn off other processes or call external programs to aid in the testing, or when (as noted above) the tests assume certain things about the filesystem and paths. Be careful not to depend on a specific output style for errors, such as when checking <tt>$!</tt> after a failed system call. Using <tt>$!</tt> for anything else than displaying it as output is doubtful (though see the <tt>&quot;Errno&quot;</tt> module for testing reasonably portably for error value). Some platforms expect a certain output format, and Perl on those platforms may have been adjusted accordingly. Most specifically, don't anchor a regex when testing an error value.

<h2>CPAN Testers</h2>

 Modules uploaded to <font SIZE="-1">CPAN</font> are tested by a variety of volunteers on different platforms. These <font SIZE="-1">CPAN</font> testers are notified by mail of each new upload, and reply to the list with <font SIZE="-1">PASS, FAIL, NA</font> (not applicable to this platform), or <font SIZE="-1">UNKNOWN</font> (unknown), along with any relevant notations. 

 The purpose of the testing is twofold: one, to help developers fix any problems in their code that crop up because of lack of testing on other platforms; two, to provide users with information about whether a given module works on a given platform. 

 Also see:
<dl>
<dt>&bull;
<dd> Mailing list: cpan-testers-discuss [at] perl.org
<dt>&bull;
<dd> Testing results: &lt;<a rel="nofollow" HREF="http://www.cpantesters.org/">http://www.cpantesters.org/</a>&gt;</dl>

<h2>PLATFORMS</h2>

 Perl is built with a <tt>$^O</tt> variable that indicates the operating system it was built on. This was implemented to help speed up code that would otherwise have to <tt>&quot;use Config&quot;</tt> and use the value of <tt>$Config{osname}</tt>. Of course, to get more detailed information about the system, looking into <tt>%Config</tt> is certainly recommended. 

 <tt>%Config</tt> cannot always be trusted, however, because it was built at compile time. If perl was built in one place, then transferred elsewhere, some values may be wrong. The values may even have been edited after the fact.

<h3>Unix</h3>

 Perl works on a bewildering variety of Unix and Unix-like platforms (see e.g. most of the files in the <i>hints/</i> directory in the source code kit). On most of these systems, the value of <tt>$^O</tt> (hence <tt>$Config{osname}</tt>, too) is determined either by lowercasing and stripping punctuation from the first field of the string returned by typing <tt>&quot;uname -a&quot;</tt> (or a similar command) at the shell prompt or by testing the file system for the presence of uniquely named files such as a kernel or header file. Here, for example, are a few of the more popular Unix flavors: 

 
uname $ ^ O $Config
{
    archname
}
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --AIX aix aix
                                                                   BSD /
        OS bsdos i386 -
    bsdos
            Darwin darwin darwin
                DYNIX /
        ptx dynixptx i386 -
    dynixptx
        FreeBSD freebsd freebsd -
    i386
        Haiku haiku BePC -
    haiku
        Linux linux arm -
    linux
        Linux linux armv5tel -
    linux
        Linux linux i386 -
    linux
        Linux linux i586 -
    linux
        Linux linux ppc -
    linux
        HP -
    UX hpux PA - RISC1 .1 IRIX irix irix Mac OS X darwin darwin NeXT 3 next next - fat NeXT 4 next OPENSTEP - Mach openbsd openbsd i386 - openbsd OSF1 dec_osf alpha - dec_osf reliantunix - n svr4 RM400 - svr4 SCO_SV sco_sv i386 - sco_sv SINIX - N svr4 RM400 - svr4 sn4609 unicos CRAY_C90 - unicos sn6521 unicosmk t3e - unicosmk sn9617 unicos CRAY_J90 - unicos SunOS solaris sun4 - solaris SunOS solaris i86pc - solaris SunOS4 sunos sun4 - sunos
 

 Because the value of <tt>$Config{archname}</tt> may depend on the hardware architecture, it can vary more than the value of <tt>$^O</tt>.

<h3><font SIZE="-1">DOS</font> and Derivatives</h3>

 Perl has long been ported to Intel-style microcomputers running under systems like PC-DOS, MS-DOS, <font SIZE="-1">OS/2,</font> and most Windows platforms you can bring yourself to mention (except for Windows <font SIZE="-1">CE,</font> if you count that). Users familiar with <i></i><font SIZE="-1"><i>COMMAND.COM</i></font><i></i> or <i></i><font SIZE="-1"><i>CMD.EXE</i></font><i></i> style shells should be aware that each of these file specifications may have subtle differences: 

 
my $filespec0 = "c:/foo/bar/file.txt";
my $filespec1 = "c:\\foo\\bar\\file.txt";
my $filespec2 = 'c:\foo\bar\file.txt';
my $filespec3 = 'c:\\foo\\bar\\file.txt';
 

 System calls accept either <tt>&quot;/&quot;</tt> or <tt>&quot;\&quot;</tt> as the path separator. However, many command-line utilities of <font SIZE="-1">DOS</font> vintage treat <tt>&quot;/&quot;</tt> as the option prefix, so may get confused by filenames containing <tt>&quot;/&quot;</tt>. Aside from calling any external programs, <tt>&quot;/&quot;</tt> will work just fine, and probably better, as it is more consistent with popular usage, and avoids the problem of remembering what to backwhack and what not to. 

 The <font SIZE="-1">DOS FAT</font> filesystem can accommodate only ``8.3'' style filenames. Under the ``case-insensitive, but case-preserving'' <font SIZE="-1">HPFS</font> (<font SIZE="-1">OS/2</font>) and <font SIZE="-1">NTFS</font> (<font SIZE="-1">NT</font>) filesystems you may have to be careful about case returned with functions like <tt>&quot;readdir&quot;</tt> or used with functions like <tt>&quot;open&quot;</tt> or <tt>&quot;opendir&quot;</tt>. 

 <font SIZE="-1">DOS</font> also treats several filenames as special, such as <i></i><font SIZE="-1"><i>AUX</i></font><i></i>, <i></i><font SIZE="-1"><i>PRN</i></font><i></i>, <i></i><font SIZE="-1"><i>NUL</i></font><i></i>, <i></i><font SIZE="-1"><i>CON</i></font><i></i>, <i></i><font SIZE="-1"><i>COM1</i></font><i></i>, <i></i><font SIZE="-1"><i>LPT1</i></font><i></i>, <i></i><font SIZE="-1"><i>LPT2</i></font><i></i>, etc. Unfortunately, sometimes these filenames won't even work if you include an explicit directory prefix. It is best to avoid such filenames, if you want your code to be portable to <font SIZE="-1">DOS</font> and its derivatives. It's hard to know what these all are, unfortunately. 

 Users of these operating systems may also wish to make use of scripts such as <i>pl2bat.bat</i> to put wrappers around your scripts. 

 Newline (<tt>&quot;\n&quot;</tt>) is translated as <tt>&quot;\015\012&quot;</tt> by the I/O system when reading from and writing to files (see ``Newlines''). <tt>&quot;binmode($filehandle)&quot;</tt> will keep <tt>&quot;\n&quot;</tt> translated as <tt>&quot;\012&quot;</tt> for that filehandle. <tt>&quot;binmode&quot;</tt> should always be used for code that deals with binary data. That's assuming you realize in advance that your data is in binary. General-purpose programs should often assume nothing about their data. 

 The <tt>$^O</tt> variable and the <tt>$Config{archname}</tt> values for various DOSish perls are as follows: 

 
OS $ ^ O $Config{archname} ID Version-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -MS - DOS dos ? PC - DOS dos ? OS / 2 os2 ? Windows 3.1 ? ? 0 3 01 Windows 95 MSWin32 MSWin32 - x86 1 4 00 Windows 98 MSWin32 MSWin32 - x86 1 4 10 Windows ME MSWin32 MSWin32 - x86 1 ? Windows NT MSWin32 MSWin32 - x86 2 4 xx Windows NT MSWin32 MSWin32 - ALPHA 2 4 xx Windows NT MSWin32 MSWin32 - ppc 2 4 xx Windows 2000 MSWin32 MSWin32 - x86 2 5 00 Windows XP MSWin32 MSWin32 - x86 2 5 01 Windows 2003 MSWin32 MSWin32 - x86 2 5 02 Windows Vista MSWin32 MSWin32 - x86 2 6 00 Windows 7 MSWin32 MSWin32 - x86 2 6 01 Windows 7 MSWin32 MSWin32 - x64 2 6 01 Windows 2008 MSWin32 MSWin32 - x86 2 6 01 Windows 2008 MSWin32 MSWin32 - x64 2 6 01 Windows CE MSWin32 ? 3 Cygwin cygwin cygwin
 

 The various MSWin32 Perl's can distinguish the <font SIZE="-1">OS</font> they are running on via the value of the fifth element of the list returned from <tt>&quot;Win32::GetOSVersion()&quot;</tt>. For example: 

 
if ($ ^ O eq 'MSWin32') {
    my @os_version_info = Win32::GetOSVersion();
    print + ('3.1', '95', 'NT')[$os_version_info[4]], "\n";
}
 

 There are also <tt>&quot;Win32::IsWinNT()|Win32/Win32::IsWinNT()&quot;</tt>, <tt>&quot;Win32::IsWin95()|Win32/Win32::IsWin95()&quot;</tt>, and <tt>&quot;Win32::GetOSName()&quot;</tt>; try <tt>&quot;perldoc Win32&quot;</tt>. The very portable <tt>&quot;POSIX::uname()&quot;</tt> will work too: 

 <pre>
    c:\&gt; perl -MPOSIX -we &quot;print join '|', uname&quot;
    Windows NT|moonru|5.0|Build 2195 (Service Pack 2)|x86
</pre> 

 Errors set by Winsock functions are now put directly into <tt>$^E</tt>, and the relevant <tt>&quot;WSAE*&quot;</tt> error codes are now exported from the Errno and <font SIZE="-1">POSIX</font> modules for testing this against. 

 The previous behavior of putting the errors (converted to POSIX-style <tt>&quot;E*&quot;</tt> error codes since Perl 5.20.0) into <tt>$!</tt> was buggy due to the non-equivalence of like-named Winsock and <font SIZE="-1">POSIX</font> error constants, a relationship between which has unfortunately been established in one way or another since Perl 5.8.0. 

 The new behavior provides a much more robust solution for checking Winsock errors in portable software without accidentally matching <font SIZE="-1">POSIX</font> tests that were intended for other OSes and may have different meanings for Winsock. 

 The old behavior is currently retained, warts and all, for backwards compatibility, but users are encouraged to change any code that tests <tt>$!</tt> against <tt>&quot;E*&quot;</tt> constants for Winsock errors to instead test <tt>$^E</tt> against <tt>&quot;WSAE*&quot;</tt> constants. After a suitable deprecation period, which started with Perl 5.24, the old behavior may be removed, leaving <tt>$!</tt> unchanged after Winsock function calls, to avoid any possible confusion over which error variable to check. 

 Also see:
<dl>
<dt>&bull;
<dd> The djgpp environment for <font SIZE="-1">DOS,</font> &lt;<a rel="nofollow" HREF="http://www.delorie.com/djgpp/">http://www.delorie.com/djgpp/</a>&gt; and perldos.
<dt>&bull;
<dd> The <font SIZE="-1">EMX</font> environment for <font SIZE="-1">DOS, OS/2,</font> etc. emx [at] iaehv.nl, &lt;<a HREF="ftp://hobbes.nmsu.edu/pub/os2/dev/emx/">ftp://hobbes.nmsu.edu/pub/os2/dev/emx/</a>&gt; Also perlos2.
<dt>&bull;
<dd> Build instructions for Win32 in perlwin32, or under the Cygnus environment in perlcygwin.
<dt>&bull;
<dd> The <tt>&quot;Win32::*&quot;</tt> modules in Win32.
<dt>&bull;
<dd> The ActiveState Pages, &lt;<a rel="nofollow" HREF="http://www.activestate.com/">http://www.activestate.com/</a>&gt;
<dt>&bull;
<dd> The Cygwin environment for Win32; <i></i><font SIZE="-1"><i>README</i></font><i>.cygwin</i> (installed as perlcygwin), &lt;<a rel="nofollow" HREF="http://www.cygwin.com/">http://www.cygwin.com/</a>&gt;
<dt>&bull;
<dd> The U/WIN environment for Win32, &lt;<a rel="nofollow" HREF="http://www.research.att.com/sw/tools/uwin/">http://www.research.att.com/sw/tools/uwin/</a>&gt;
<dt>&bull;
<dd> Build instructions for <font SIZE="-1">OS/2,</font> perlos2</dl>

<h3><font SIZE="-1">VMS</font></h3>

 Perl on <font SIZE="-1">VMS</font> is discussed in perlvms in the Perl distribution. 

 The official name of <font SIZE="-1">VMS</font> as of this writing is OpenVMS. 

 Interacting with Perl from the Digital Command Language (<font SIZE="-1">DCL</font>) shell often requires a different set of quotation marks than Unix shells do. For example: 

 <pre>
    $ perl -e &quot;print &quot;&quot;Hello, world.\n&quot;&quot;&quot;
    Hello, world.
</pre> 

 There are several ways to wrap your Perl scripts in <font SIZE="-1">DCL</font> <i>.COM</i> files, if you are so inclined. For example: 

 
$ write sys$output "Hello from DCL!" $ if p1.eqs."" $ then perl - x 'f$environment("PROCEDURE") $ else perl - x - 'p1 ' p2 'p3 ' p4 'p5 ' p6 'p7 ' p8 $ deck / dollars = "__END__"
#!/ usr / bin / perl
    print "Hello from Perl!\n";
__END__
$ endif
 

 Do take care with <tt>&quot;$ ASSIGN/nolog/user SYS$COMMAND: SYS$INPUT&quot;</tt> if your Perl-in-DCL script expects to do things like <tt>&quot;$read = &lt;STDIN&gt;;&quot;</tt>. 

 The <font SIZE="-1">VMS</font> operating system has two filesystems, designated by their on-disk structure (<font SIZE="-1">ODS</font>) level: <font SIZE="-1">ODS-2</font> and its successor <font SIZE="-1">ODS-5.</font> The initial port of Perl to <font SIZE="-1">VMS</font> pre-dates <font SIZE="-1">ODS-5,</font> but all current testing and development assumes <font SIZE="-1">ODS-5</font> and its capabilities, including case preservation, extended characters in filespecs, and names up to 8192 bytes long. 

 Perl on <font SIZE="-1">VMS</font> can accept either <font SIZE="-1">VMS-</font> or Unix-style file specifications as in either of the following: 

 <pre>
    $ perl -ne &quot;print if /perl_setup/i&quot; SYS$LOGIN:LOGIN.COM
    $ perl -ne &quot;print if /perl_setup/i&quot; /sys$login/login.com
</pre> 

 but not a mixture of both as in: 

 <pre>
    $ perl -ne &quot;print if /perl_setup/i&quot; sys$login:/login.com
    Can't open sys$login:/login.com: file specification syntax error
</pre> 

 In general, the easiest path to portability is always to specify filenames in Unix format unless they will need to be processed by native commands or utilities. Because of this latter consideration, the File::Spec module by default returns native format specifications regardless of input format. This default may be reversed so that filenames are always reported in Unix format by specifying the <tt>&quot;DECC$FILENAME_UNIX_REPORT&quot;</tt> feature logical in the environment. 

 The file type, or extension, is always present in a VMS-format file specification even if it's zero-length. This means that, by default, <tt>&quot;readdir&quot;</tt> will return a trailing dot on a file with no extension, so where you would see <tt>&quot;a&quot;</tt> on Unix you'll see <tt>&quot;a.&quot;</tt> on <font SIZE="-1">VMS.</font> However, the trailing dot may be suppressed by enabling the <tt>&quot;DECC$READDIR_DROPDOTNOTYPE&quot;</tt> feature in the environment (see the <font SIZE="-1">CRTL</font> documentation on feature logical names). 

 What <tt>&quot;\n&quot;</tt> represents depends on the type of file opened. It usually represents <tt>&quot;\012&quot;</tt> but it could also be <tt>&quot;\015&quot;</tt>, <tt>&quot;\012&quot;</tt>, <tt>&quot;\015\012&quot;</tt>, <tt>&quot;\000&quot;</tt>, <tt>&quot;\040&quot;</tt>, or nothing depending on the file organization and record format. The <tt>&quot;VMS::Stdio&quot;</tt> module provides access to the special <tt>&quot;fopen()&quot;</tt> requirements of files with unusual attributes on <font SIZE="-1">VMS.</font> 

 The value of <tt>$^O</tt> on OpenVMS is ``<font SIZE="-1">VMS''.</font> To determine the architecture that you are running on refer to <tt>$Config{archname}</tt>. 

 On <font SIZE="-1">VMS,</font> perl determines the <font SIZE="-1">UTC</font> offset from the <tt>&quot;SYS$TIMEZONE_DIFFERENTIAL&quot;</tt> logical name. Although the <font SIZE="-1">VMS</font> epoch began at 17-NOV-1858 00:00:00.00, calls to <tt>&quot;localtime&quot;</tt> are adjusted to count offsets from 01-JAN-1970 00:00:00.00, just like Unix. 

 Also see:
<dl>
<dt>&bull;
<dd> <i></i><font SIZE="-1"><i>README</i></font><i>.vms</i> (installed as <i>README_vms</i>), perlvms
<dt>&bull;
<dd> vmsperl list, vmsperl-subscribe [at] perl.org
<dt>&bull;
<dd> vmsperl on the web, &lt;<a rel="nofollow" HREF="http://www.sidhe.org/vmsperl/index.html">http://www.sidhe.org/vmsperl/index.html</a>&gt;
<dt>&bull;
<dd> <font SIZE="-1">VMS</font> Software Inc. web site, &lt;<a rel="nofollow" HREF="http://www.vmssoftware.com">http://www.vmssoftware.com</a>&gt;</dl>

<h3><font SIZE="-1">VOS</font></h3>

 Perl on <font SIZE="-1">VOS</font> (also known as OpenVOS) is discussed in <i></i><font SIZE="-1"><i>README</i></font><i>.vos</i> in the Perl distribution (installed as perlvos). Perl on <font SIZE="-1">VOS</font> can accept either <font SIZE="-1">VOS-</font> or Unix-style file specifications as in either of the following: 

 <pre>
    $ perl -ne &quot;print if /perl_setup/i&quot; &gt;system&gt;notices
    $ perl -ne &quot;print if /perl_setup/i&quot; /system/notices
</pre> 

 or even a mixture of both as in: 

 <pre>
    $ perl -ne &quot;print if /perl_setup/i&quot; &gt;system/notices
</pre> 

 Even though <font SIZE="-1">VOS</font> allows the slash character to appear in object names, because the <font SIZE="-1">VOS</font> port of Perl interprets it as a pathname delimiting character, <font SIZE="-1">VOS</font> files, directories, or links whose names contain a slash character cannot be processed. Such files must be renamed before they can be processed by Perl. 

 Older releases of <font SIZE="-1">VOS</font> (prior to OpenVOS Release 17.0) limit file names to 32 or fewer characters, prohibit file names from starting with a <tt>&quot;-&quot;</tt> character, and prohibit file names from containing <tt>&quot; &quot;</tt> (space) or any character from the set <tt>&quot;!#%&amp;'()*;&lt;=&gt;?&quot;</tt>. 

 Newer releases of <font SIZE="-1">VOS</font> (OpenVOS Release 17.0 or later) support a feature known as extended names. On these releases, file names can contain up to 255 characters, are prohibited from starting with a <tt>&quot;-&quot;</tt> character, and the set of prohibited characters is reduced to <tt>&quot;#%*&lt;&gt;?&quot;</tt>. There are restrictions involving spaces and apostrophes: these characters must not begin or end a name, nor can they immediately precede or follow a period. Additionally, a space must not immediately precede another space or hyphen. Specifically, the following character combinations are prohibited: space-space, space-hyphen, period-space, space-period, period-apostrophe, apostrophe-period, leading or trailing space, and leading or trailing apostrophe. Although an extended file name is limited to 255 characters, a path name is still limited to 256 characters. 

 The value of <tt>$^O</tt> on <font SIZE="-1">VOS</font> is ``vos''. To determine the architecture that you are running on refer to <tt>$Config{archname}</tt>. 

 Also see:
<dl>
<dt>&bull;
<dd> <i></i><font SIZE="-1"><i>README</i></font><i>.vos</i> (installed as perlvos)
<dt>&bull;
<dd> The <font SIZE="-1">VOS</font> mailing list. 

 There is no specific mailing list for Perl on <font SIZE="-1">VOS.</font> You can contact the Stratus Technologies Customer Assistance Center (<font SIZE="-1">CAC</font>) for your region, or you can use the contact information located in the distribution files on the Stratus Anonymous <font SIZE="-1">FTP</font> site.
<dt>&bull;
<dd> Stratus Technologies on the web at &lt;<a rel="nofollow" HREF="http://www.stratus.com">http://www.stratus.com</a>&gt;
<dt>&bull;
<dd> <font SIZE="-1">VOS</font> Open-Source Software on the web at &lt;<a rel="nofollow" HREF="http://ftp.stratus.com/pub/vos/vos.html">http://ftp.stratus.com/pub/vos/vos.html</a>&gt;</dl>

<h3><font SIZE="-1">EBCDIC</font> Platforms</h3>

 v5.22 core Perl runs on z/OS (formerly <font SIZE="-1">OS/390</font>). Theoretically it could run on the successors of <font SIZE="-1">OS/400</font> on <font SIZE="-1">AS/400</font> minicomputers as well as <font SIZE="-1">VM/ESA,</font> and <font SIZE="-1">BS2000</font> for S/390 Mainframes. Such computers use <font SIZE="-1">EBCDIC</font> character sets internally (usually Character Code Set <font SIZE="-1">ID 0037</font> for <font SIZE="-1">OS/400</font> and either 1047 or POSIX-BC for S/390 systems). 

 The rest of this section may need updating, but we don't know what it should say. Please email comments to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. 

 On the mainframe Perl currently works under the ``Unix system services for <font SIZE="-1">OS/390''</font> (formerly known as OpenEdition), <font SIZE="-1">VM/ESA</font> OpenEdition, or the <font SIZE="-1">BS200</font> POSIX-BC system (<font SIZE="-1">BS2000</font> is supported in Perl 5.6 and greater). See perlos390 for details. Note that for <font SIZE="-1">OS/400</font> there is also a port of Perl 5.8.1/5.10.0 or later to the <font SIZE="-1">PASE</font> which is ASCII-based (as opposed to <font SIZE="-1">ILE</font> which is EBCDIC-based), see perlos400. 

 As of R2.5 of <font SIZE="-1">USS</font> for <font SIZE="-1">OS/390</font> and Version 2.3 of <font SIZE="-1">VM/ESA</font> these Unix sub-systems do not support the <tt>&quot;#!&quot;</tt> shebang trick for script invocation. Hence, on <font SIZE="-1">OS/390</font> and <font SIZE="-1">VM/ESA</font> Perl scripts can be executed with a header similar to the following simple script: 

 
    : # use perl
        eval 'exec /usr/local/bin/perl -S $0 ${1+"$@"}'
            if 0;
#!/ usr / local / bin / perl #just a comment really
    print "Hello from perl!\n";
 

 <font SIZE="-1">OS/390</font> will support the <tt>&quot;#!&quot;</tt> shebang trick in release 2.8 and beyond. Calls to <tt>&quot;system&quot;</tt> and backticks can use <font SIZE="-1">POSIX</font> shell syntax on all S/390 systems. 

 On the <font SIZE="-1">AS/400,</font> if <font SIZE="-1">PERL5</font> is in your library list, you may need to wrap your Perl scripts in a <font SIZE="-1">CL</font> procedure to invoke them like so: 

 <pre>
    BEGIN
      CALL PGM(PERL5/PERL) PARM('/QOpenSys/hello.pl')
    ENDPGM
</pre> 

 This will invoke the Perl script <i>hello.pl</i> in the root of the QOpenSys file system. On the <font SIZE="-1">AS/400</font> calls to <tt>&quot;system&quot;</tt> or backticks must use <font SIZE="-1">CL</font> syntax. 

 On these platforms, bear in mind that the <font SIZE="-1">EBCDIC</font> character set may have an effect on what happens with some Perl functions (such as <tt>&quot;chr&quot;</tt>, <tt>&quot;pack&quot;</tt>, <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, <tt>&quot;ord&quot;</tt>, <tt>&quot;sort&quot;</tt>, <tt>&quot;sprintf&quot;</tt>, <tt>&quot;unpack&quot;</tt>), as well as bit-fiddling with <font SIZE="-1">ASCII</font> constants using operators like <tt>&quot;^&quot;</tt>, <tt>&quot;&amp;&quot;</tt> and <tt>&quot;|&quot;</tt>, not to mention dealing with socket interfaces to <font SIZE="-1">ASCII</font> computers (see ``Newlines''). 

 Fortunately, most web servers for the mainframe will correctly translate the <tt>&quot;\n&quot;</tt> in the following statement to its <font SIZE="-1">ASCII</font> equivalent (<tt>&quot;\r&quot;</tt> is the same under both Unix and z/OS): 

 <pre>
    print &quot;Content-type: text/html\r\n\r\n&quot;;
</pre> 

 The values of <tt>$^O</tt> on some of these platforms include: 

 
uname $ ^ O $Config
{
    archname
}
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --OS / 390 os390 os390
                                                                          OS400 os400 os400
                                                                              POSIX -
    BC posix - bc BS2000 - posix - bc
 

 Some simple tricks for determining if you are running on an <font SIZE="-1">EBCDIC</font> platform could include any of the following (perhaps all): 

 
if ("\t" eq "\005") {
    print "EBCDIC may be spoken here!\n";
}
if (ord('A') == 193) {
    print "EBCDIC may be spoken here!\n";
}
if (chr(169) eq 'z') {
    print "EBCDIC may be spoken here!\n";
}
 

 One thing you may not want to rely on is the <font SIZE="-1">EBCDIC</font> encoding of punctuation characters since these may differ from code page to code page (and once your module or script is rumoured to work with <font SIZE="-1">EBCDIC,</font> folks will want it to work with all <font SIZE="-1">EBCDIC</font> character sets). 

 Also see:
<dl>
<dt>&bull;
<dd> perlos390, perlos400, perlbs2000, perlebcdic.
<dt>&bull;
<dd> The perl-mvs [at] perl.org list is for discussion of porting issues as well as general usage issues for all <font SIZE="-1">EBCDIC</font> Perls. Send a message body of ``subscribe perl-mvs'' to majordomo [at] perl.org.
<dt>&bull;
<dd> <font SIZE="-1">AS/400</font> Perl information at &lt;<a rel="nofollow" HREF="http://as400.rochester.ibm.com/">http://as400.rochester.ibm.com/</a>&gt; as well as on <font SIZE="-1">CPAN</font> in the <i>ports/</i> directory.</dl>

<h3>Acorn <font SIZE="-1">RISC OS</font></h3>

 Because Acorns use <font SIZE="-1">ASCII</font> with newlines (<tt>&quot;\n&quot;</tt>) in text files as <tt>&quot;\012&quot;</tt> like Unix, and because Unix filename emulation is turned on by default, most simple scripts will probably work ``out of the box''. The native filesystem is modular, and individual filesystems are free to be case-sensitive or insensitive, and are usually case-preserving. Some native filesystems have name length limits, which file and directory names are silently truncated to fit. Scripts should be aware that the standard filesystem currently has a name length limit of <b>10</b> characters, with up to 77 items in a directory, but other filesystems may not impose such limitations. 

 Native filenames are of the form 

 <pre>
    Filesystem#Special_Field::DiskName.$.Directory.Directory.File
</pre> 

 where 

 
    Special_Field is not usually present, but may contain . and $ .
    Filesystem =~ m|[A-Za-z0-9_]|
    DsicName   =~ m|[A-Za-z0-9_/]|
    $ represents the root directory
    . is the path separator
    @ is the current directory (per filesystem but machine global)
    ^ is the parent directory
    Directory and File =~ m|[^\0- "\.\$\%\&amp;:\@\\^\|\177]+|
 

 The default filename translation is roughly <tt>&quot;tr|/.|./|&quot;</tt>, swapping dots and slashes. 

 Note that <tt>&quot;&quot;ADFS::HardDisk.$.File&quot; ne 'ADFS::HardDisk.$.File'&quot;</tt> and that the second stage of <tt>&quot;$&quot;</tt> interpolation in regular expressions will fall foul of the <tt>$.</tt> variable if scripts are not careful. 

 Logical paths specified by system variables containing comma-separated search lists are also allowed; hence <tt>&quot;System:Modules&quot;</tt> is a valid filename, and the filesystem will prefix <tt>&quot;Modules&quot;</tt> with each section of <tt>&quot;System$Path&quot;</tt> until a name is made that points to an object on disk. Writing to a new file <tt>&quot;System:Modules&quot;</tt> would be allowed only if <tt>&quot;System$Path&quot;</tt> contains a single item list. The filesystem will also expand system variables in filenames if enclosed in angle brackets, so <tt>&quot;&lt;System$Dir&gt;.Modules&quot;</tt> would look for the file <tt>&quot;$ENV{'System$Dir'} . 'Modules'&quot;</tt>. The obvious implication of this is that <b>fully qualified filenames can start with </b>&quot;&lt;&gt;&quot; and the three-argument form of <tt>&quot;open&quot;</tt> should always be used. 

 Because <tt>&quot;.&quot;</tt> was in use as a directory separator and filenames could not be assumed to be unique after 10 characters, Acorn implemented the C compiler to strip the trailing <tt>&quot;.c&quot;</tt> <tt>&quot;.h&quot;</tt> <tt>&quot;.s&quot;</tt> and <tt>&quot;.o&quot;</tt> suffix from filenames specified in source code and store the respective files in subdirectories named after the suffix. Hence files are translated: 

 <pre>
    foo.h           h.foo
    C:foo.h         C:h.foo        (logical path variable)
    sys/os.h        sys.h.os       (C compiler groks Unix-speak)
    10charname.c    c.10charname
    10charname.o    o.10charname
    11charname_.c   c.11charname   (assuming filesystem truncates at 10)
</pre> 

 The Unix emulation library's translation of filenames to native assumes that this sort of translation is required, and it allows a user-defined list of known suffixes that it will transpose in this fashion. This may seem transparent, but consider that with these rules <i>foo/bar/baz.h</i> and <i>foo/bar/h/baz</i> both map to <i>foo.bar.h.baz</i>, and that <tt>&quot;readdir&quot;</tt> and <tt>&quot;glob&quot;</tt> cannot and do not attempt to emulate the reverse mapping. Other <tt>&quot;.&quot;</tt>'s in filenames are translated to <tt>&quot;/&quot;</tt>. 

 As implied above, the environment accessed through <tt>%ENV</tt> is global, and the convention is that program specific environment variables are of the form <tt>&quot;Program$Name&quot;</tt>. Each filesystem maintains a current directory, and the current filesystem's current directory is the <b>global</b> current directory. Consequently, sociable programs don't change the current directory but rely on full pathnames, and programs (and Makefiles) cannot assume that they can spawn a child process which can change the current directory without affecting its parent (and everyone else for that matter). 

 Because native operating system filehandles are global and are currently allocated down from 255, with 0 being a reserved value, the Unix emulation library emulates Unix filehandles. Consequently, you can't rely on passing <tt>&quot;STDIN&quot;</tt>, <tt>&quot;STDOUT&quot;</tt>, or <tt>&quot;STDERR&quot;</tt> to your children. 

 The desire of users to express filenames of the form <tt>&quot;&lt;Foo$Dir&gt;.Bar&quot;</tt> on the command line unquoted causes problems, too: <tt>&quot;``&quot;</tt> command output capture has to perform a guessing game. It assumes that a string <tt>&quot;&lt;[^&lt;&gt;]+\$[^&lt;&gt;]&gt;&quot;</tt> is a reference to an environment variable, whereas anything else involving <tt>&quot;&lt;&quot;</tt> or <tt>&quot;&gt;&quot;</tt> is redirection, and generally manages to be 99% right. Of course, the problem remains that scripts cannot rely on any Unix tools being available, or that any tools found have Unix-like command line arguments. 

 Extensions and <font SIZE="-1">XS</font> are, in theory, buildable by anyone using free tools. In practice, many don't, as users of the Acorn platform are used to binary distributions. MakeMaker does run, but no available make currently copes with MakeMaker's makefiles; even if and when this should be fixed, the lack of a Unix-like shell will cause problems with makefile rules, especially lines of the form <tt>&quot;cd sdbm &amp;&amp; make all&quot;</tt>, and anything using quoting. 

 ``RISC OS'' is the proper name for the operating system, but the value in <tt>$^O</tt> is ``riscos'' (because we don't like shouting).

<h3>Other perls</h3>

 Perl has been ported to many platforms that do not fit into any of the categories listed above. Some, such as AmigaOS, <font SIZE="-1">QNX,</font> Plan 9, and <font SIZE="-1">VOS,</font> have been well-integrated into the standard Perl source code kit. You may need to see the <i>ports/</i> directory on <font SIZE="-1">CPAN</font> for information, and possibly binaries, for the likes of: aos, Atari <font SIZE="-1">ST,</font> lynxos, riscos, Novell Netware, Tandem Guardian, <i>etc.</i> (Yes, we know that some of these OSes may fall under the Unix category, but we are not a standards body.) 

 Some approximate operating system names and their <tt>$^O</tt> values in the ``<font SIZE="-1">OTHER''</font> category include: 

 
OS $ ^ O $Config
{
    archname
}
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --Amiga DOS amigaos m68k - amigos
 

 See also:
<dl>
<dt>&bull;
<dd> Amiga, <i></i><font SIZE="-1"><i>README</i></font><i>.amiga</i> (installed as perlamiga).
<dt>&bull;
<dd> A free perl5-based <font SIZE="-1">PERL.NLM</font> for Novell Netware is available in precompiled binary and source code form from &lt;<a rel="nofollow" HREF="http://www.novell.com/">http://www.novell.com/</a>&gt; as well as from <font SIZE="-1">CPAN.</font>
<dt>&bull;
<dd> Plan 9, <i></i><font SIZE="-1"><i>README</i></font><i>.plan9</i></dl>

<h2>FUNCTION IMPLEMENTATIONS</h2>

 Listed below are functions that are either completely unimplemented or else have been implemented differently on various platforms. Preceding each description will be, in parentheses, a list of platforms that the description applies to. 

 The list may well be incomplete, or even wrong in some places. When in doubt, consult the platform-specific <font SIZE="-1">README</font> files in the Perl source distribution, and any other documentation resources accompanying a given port. 

 Be aware, moreover, that even among Unix-ish systems there are variations. 

 For many functions, you can also query <tt>%Config</tt>, exported by default from the <tt>&quot;Config&quot;</tt> module. For example, to check whether the platform has the <tt>&quot;lstat&quot;</tt> call, check <tt>$Config{d_lstat}</tt>. See Config for a full description of available variables.

<h3>Alphabetical Listing of Perl Functions</h3>

<dl>
<dt>-X
<dd> (Win32) <tt>&quot;-w&quot;</tt> only inspects the read-only file attribute (<font SIZE="-1">FILE_ATTRIBUTE_READONLY</font>), which determines whether the directory can be deleted, not whether it can be written to. Directories always have read and write access unless denied by discretionary access control lists (DACLs). 

 (<font SIZE="-1">VMS</font>) <tt>&quot;-r&quot;</tt>, <tt>&quot;-w&quot;</tt>, <tt>&quot;-x&quot;</tt>, and <tt>&quot;-o&quot;</tt> tell whether the file is accessible, which may not reflect UIC-based file protections. 

 (RISC OS) <tt>&quot;-s&quot;</tt> by name on an open file will return the space reserved on disk, rather than the current extent. <tt>&quot;-s&quot;</tt> on an open filehandle returns the current size. 

 (Win32, <font SIZE="-1">VMS,</font> RISC OS) <tt>&quot;-R&quot;</tt>, <tt>&quot;-W&quot;</tt>, <tt>&quot;-X&quot;</tt>, <tt>&quot;-O&quot;</tt> are indistinguishable from <tt>&quot;-r&quot;</tt>, <tt>&quot;-w&quot;</tt>, <tt>&quot;-x&quot;</tt>, <tt>&quot;-o&quot;</tt>. 

 (Win32, <font SIZE="-1">VMS,</font> RISC OS) <tt>&quot;-g&quot;</tt>, <tt>&quot;-k&quot;</tt>, <tt>&quot;-l&quot;</tt>, <tt>&quot;-u&quot;</tt>, <tt>&quot;-A&quot;</tt> are not particularly meaningful. 

 (<font SIZE="-1">VMS,</font> RISC OS) <tt>&quot;-p&quot;</tt> is not particularly meaningful. 

 (<font SIZE="-1">VMS</font>) <tt>&quot;-d&quot;</tt> is true if passed a device spec without an explicit directory. 

 (Win32) <tt>&quot;-x&quot;</tt> (or <tt>&quot;-X&quot;</tt>) determine if a file ends in one of the executable suffixes. <tt>&quot;-S&quot;</tt> is meaningless. 

 (RISC OS) <tt>&quot;-x&quot;</tt> (or <tt>&quot;-X&quot;</tt>) determine if a file has an executable file type.
<dt>alarm
<dd> (Win32) Emulated using timers that must be explicitly polled whenever Perl wants to dispatch ``safe signals'' and therefore cannot interrupt blocking system calls.
<dt>atan2
<dd> (Tru64, HP-UX 10.20) Due to issues with various CPUs, math libraries, compilers, and standards, results for <tt>&quot;atan2&quot;</tt> may vary depending on any combination of the above. Perl attempts to conform to the Open Group/IEEE standards for the results returned from <tt>&quot;atan2&quot;</tt>, but cannot force the issue if the system Perl is run on does not allow it. 

 The current version of the standards for <tt>&quot;atan2&quot;</tt> is available at &lt;<a rel="nofollow" HREF="http://www.opengroup.org/onlinepubs/009695399/functions/atan2.html">http://www.opengroup.org/onlinepubs/009695399/functions/atan2.html</a>&gt;.
<dt>binmode
<dd> (RISC OS) Meaningless. 

 (<font SIZE="-1">VMS</font>) Reopens file and restores pointer; if function fails, underlying filehandle may be closed, or pointer may be in a different position. 

 (Win32) The value returned by <tt>&quot;tell&quot;</tt> may be affected after the call, and the filehandle may be flushed.
<dt>chmod
<dd> (Win32) Only good for changing ``owner'' read-write access; ``group'' and ``other'' bits are meaningless. 

 (RISC OS) Only good for changing ``owner'' and ``other'' read-write access. 

 (<font SIZE="-1">VOS</font>) Access permissions are mapped onto <font SIZE="-1">VOS</font> access-control list changes. 

 (Cygwin) The actual permissions set depend on the value of the <tt>&quot;CYGWIN&quot;</tt> variable in the <font SIZE="-1">SYSTEM</font> environment settings. 

 (Android) Setting the exec bit on some locations (generally <i>/sdcard</i>) will return true but not actually set the bit. 

 (<font SIZE="-1">VMS</font>) A mode argument of zero sets permissions to the user's default permission mask rather than disabling all permissions.
<dt>chown
<dd> (Plan 9, RISC OS) Not implemented. 

 (Win32) Does nothing, but won't fail. 

 (<font SIZE="-1">VOS</font>) A little funky, because <font SIZE="-1">VOS</font>'s notion of ownership is a little funky.
<dt>chroot
<dd> (Win32, <font SIZE="-1">VMS,</font> Plan 9, RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>crypt
<dd> (Win32) May not be available if library or source was not provided when building perl. 

 (Android) Not implemented.
<dt>dbmclose
<dd> (<font SIZE="-1">VMS,</font> Plan 9, <font SIZE="-1">VOS</font>) Not implemented.
<dt>dbmopen
<dd> (<font SIZE="-1">VMS,</font> Plan 9, <font SIZE="-1">VOS</font>) Not implemented.
<dt>dump
<dd> (RISC OS) Not useful. 

 (Cygwin, Win32) Not supported. 

 (<font SIZE="-1">VMS</font>) Invokes <font SIZE="-1">VMS</font> debugger.
<dt>exec
<dd> (Win32) <tt>&quot;exec LIST&quot;</tt> without the use of indirect object syntax (<tt>&quot;exec PROGRAM LIST&quot;</tt>) may fall back to trying the shell if the first <tt>&quot;spawn()&quot;</tt> fails. 

 Note that the list form of <b>exec()</b> is emulated since the Win32 <font SIZE="-1">API</font> <b>CreateProcess()</b> accepts a simple string rather than an array of command-line arguments. This may have security implications for your code. 

 (SunOS, Solaris, HP-UX) Does not automatically flush output handles on some platforms. 

 (Symbian <font SIZE="-1">OS</font>) Not supported.
<dt>exit
<dd> (<font SIZE="-1">VMS</font>) Emulates Unix <tt>&quot;exit&quot;</tt> (which considers <tt>&quot;exit 1&quot;</tt> to indicate an error) by mapping the <tt>1</tt> to <tt>&quot;SS$_ABORT&quot;</tt> (<tt>44</tt>). This behavior may be overridden with the pragma <tt>&quot;use vmsish 'exit'&quot;</tt>. As with the <font SIZE="-1">CRTL</font>'s <tt>&quot;exit()&quot;</tt> function, <tt>&quot;exit 0&quot;</tt> is also mapped to an exit status of <tt>&quot;SS$_NORMAL&quot;</tt> (<tt>1</tt>); this mapping cannot be overridden. Any other argument to <tt>&quot;exit&quot;</tt> is used directly as Perl's exit status. On <font SIZE="-1">VMS,</font> unless the future <font SIZE="-1">POSIX_EXIT</font> mode is enabled, the exit code should always be a valid <font SIZE="-1">VMS</font> exit code and not a generic number. When the <font SIZE="-1">POSIX_EXIT</font> mode is enabled, a generic number will be encoded in a method compatible with the C library _POSIX_EXIT macro so that it can be decoded by other programs, particularly ones written in C, like the <font SIZE="-1">GNV</font> package. 

 (Solaris) <tt>&quot;exit&quot;</tt> resets file pointers, which is a problem when called from a child process (created by <tt>&quot;fork&quot;</tt>) in <tt>&quot;BEGIN&quot;</tt>. A workaround is to use <tt>&quot;POSIX::_exit&quot;</tt>. 

 <pre><code>
exit unless $Config{archname} = ~ /\bsolaris\b / ;
require POSIX;
POSIX::_exit(0);
</code></pre>
<dt>fcntl
<dd> (Win32) Not implemented. 

 (<font SIZE="-1">VMS</font>) Some functions available based on the version of <font SIZE="-1">VMS.</font>
<dt>flock
<dd> (<font SIZE="-1">VMS,</font> RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>fork
<dd> (AmigaOS, RISC OS, <font SIZE="-1">VMS</font>) Not implemented. 

 (Win32) Emulated using multiple interpreters. See perlfork. 

 (SunOS, Solaris, HP-UX) Does not automatically flush output handles on some platforms.
<dt>getlogin
<dd> (RISC OS) Not implemented.
<dt>getpgrp
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>getppid
<dd> (Win32, RISC OS) Not implemented.
<dt>getpriority
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>getpwnam
<dd> (Win32) Not implemented. 

 (RISC OS) Not useful.
<dt>getgrnam
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>getnetbyname
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>getpwuid
<dd> (Win32) Not implemented. 

 (RISC OS) Not useful.
<dt>getgrgid
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>getnetbyaddr
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>getprotobynumber
<dd> (Android) Not implemented.
<dt>getpwent
<dd> (Android, Win32) Not implemented.
<dt>getgrent
<dd> (Android, Win32, <font SIZE="-1">VMS</font>) Not implemented.
<dt>gethostbyname
<dd> (Irix 5) <tt>&quot;gethostbyname('localhost')&quot;</tt> does not work everywhere: you may have to use <tt>&quot;gethostbyname('127.0.0.1')&quot;</tt>.
<dt>gethostent
<dd> (Win32) Not implemented.
<dt>getnetent
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>getprotoent
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>getservent
<dd> (Win32, Plan 9) Not implemented.
<dt>seekdir
<dd> (Android) Not implemented.
<dt>sethostent
<dd> (Android, Win32, Plan 9, RISC OS) Not implemented.
<dt>setnetent
<dd> (Win32, Plan 9, RISC OS) Not implemented.
<dt>setprotoent
<dd> (Android, Win32, Plan 9, RISC OS) Not implemented.
<dt>setservent
<dd> (Plan 9, Win32, RISC OS) Not implemented.
<dt>endpwent
<dd> (Win32) Not implemented. 

 (Android) Either not implemented or a no-op.
<dt>endgrent
<dd> (Android, RISC OS, <font SIZE="-1">VMS,</font> Win32) Not implemented.
<dt>endhostent
<dd> (Android, Win32) Not implemented.
<dt>endnetent
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>endprotoent
<dd> (Android, Win32, Plan 9) Not implemented.
<dt>endservent
<dd> (Plan 9, Win32) Not implemented.
<dt>getsockopt
<dd> (Plan 9) Not implemented.
<dt>glob
<dd> This operator is implemented via the <tt>&quot;File::Glob&quot;</tt> extension on most platforms. See File::Glob for portability information.
<dt>gmtime
<dd> In theory, <tt>&quot;gmtime&quot;</tt> is reliable from -2**63 to 2**63-1. However, because work-arounds in the implementation use floating point numbers, it will become inaccurate as the time gets larger. This is a bug and will be fixed in the future. 

 (<font SIZE="-1">VOS</font>) Time values are 32-bit quantities.
<dt>ioctl
<dd> (<font SIZE="-1">VMS</font>) Not implemented. 

 (Win32) Available only for socket handles, and it does what the <tt>&quot;ioctlsocket()&quot;</tt> call in the Winsock <font SIZE="-1">API</font> does. 

 (RISC OS) Available only for socket handles.
<dt>kill
<dd> (RISC OS) Not implemented, hence not useful for taint checking. 

 (Win32) <tt>&quot;kill&quot;</tt> doesn't send a signal to the identified process like it does on Unix platforms. Instead <tt>&quot;kill($sig, $pid)&quot;</tt> terminates the process identified by <tt>$pid</tt>, and makes it exit immediately with exit status <tt>$sig</tt>. As in Unix, if <tt>$sig</tt> is 0 and the specified process exists, it returns true without actually terminating it. 

 (Win32) <tt>&quot;kill(-9, $pid)&quot;</tt> will terminate the process specified by <tt>$pid</tt> and recursively all child processes owned by it. This is different from the Unix semantics, where the signal will be delivered to all processes in the same process group as the process specified by <tt>$pid</tt>. 

 (<font SIZE="-1">VMS</font>) A pid of -1 indicating all processes on the system is not currently supported.
<dt>link
<dd> (RISC OS, <font SIZE="-1">VOS</font>) Not implemented. 

 (AmigaOS) Link count not updated because hard links are not quite that hard (They are sort of half-way between hard and soft links). 

 (Win32) Hard links are implemented on Win32 under <font SIZE="-1">NTFS</font> only. They are natively supported on Windows 2000 and later. On Windows <font SIZE="-1">NT</font> they are implemented using the Windows <font SIZE="-1">POSIX</font> subsystem support and the Perl process will need Administrator or Backup Operator privileges to create hard links. 

 (<font SIZE="-1">VMS</font>) Available on 64 bit OpenVMS 8.2 and later.
<dt>localtime
<dd> <tt>&quot;localtime&quot;</tt> has the same range as ``gmtime'', but because time zone rules change, its accuracy for historical and future times may degrade but usually by no more than an hour.
<dt>lstat
<dd> (RISC OS) Not implemented. 

 (Win32) Return values (especially for device and inode) may be bogus.
<dt>msgctl
<dd>
<dt>msgget
<dd>
<dt>msgsnd
<dd>
<dt>msgrcv
<dd> (Android, Win32, <font SIZE="-1">VMS,</font> Plan 9, RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>open
<dd> (RISC OS) Open modes <tt>&quot;|-&quot;</tt> and <tt>&quot;-|&quot;</tt> are unsupported. 

 (SunOS, Solaris, HP-UX) Opening a process does not automatically flush output handles on some platforms. 

 (Win32) Both of modes <tt>&quot;|-&quot;</tt> and <tt>&quot;-|&quot;</tt> are supported, but the list form is emulated since the Win32 <font SIZE="-1">API</font> <b>CreateProcess()</b> accepts a simple string rather than an array of arguments. This may have security implications for your code.
<dt>readlink
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>rename
<dd> (Win32) Can't move directories between directories on different logical volumes.
<dt>rewinddir
<dd> (Win32) Will not cause <tt>&quot;readdir&quot;</tt> to re-read the directory stream. The entries already read before the <tt>&quot;rewinddir&quot;</tt> call will just be returned again from a cache buffer.
<dt>select
<dd> (Win32, <font SIZE="-1">VMS</font>) Only implemented on sockets. 

 (RISC OS) Only reliable on sockets. 

 Note that the <tt>&quot;select FILEHANDLE&quot;</tt> form is generally portable.
<dt>semctl
<dd>
<dt>semget
<dd>
<dt>semop
<dd> (Android, Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>setgrent
<dd> (Android, <font SIZE="-1">VMS,</font> Win32, RISC OS) Not implemented.
<dt>setpgrp
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>setpriority
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>setpwent
<dd> (Android, Win32, RISC OS) Not implemented.
<dt>setsockopt
<dd> (Plan 9) Not implemented.
<dt>shmctl
<dd>
<dt>shmget
<dd>
<dt>shmread
<dd>
<dt>shmwrite
<dd> (Android, Win32, <font SIZE="-1">VMS,</font> RISC OS) Not implemented.
<dt>sleep
<dd> (Win32) Emulated using synchronization functions such that it can be interrupted by <tt>&quot;alarm&quot;</tt>, and limited to a maximum of 4294967 seconds, approximately 49 days.
<dt>socketpair
<dd> (RISC OS) Not implemented. 

 (<font SIZE="-1">VMS</font>) Available on 64 bit OpenVMS 8.2 and later.
<dt>stat
<dd> Platforms that do not have <tt>&quot;rdev&quot;</tt>, <tt>&quot;blksize&quot;</tt>, or <tt>&quot;blocks&quot;</tt> will return these as <tt>''</tt>, so numeric comparison or manipulation of these fields may cause 'not numeric' warnings. 

 (Mac OS X) <tt>&quot;ctime&quot;</tt> not supported on <font SIZE="-1">UFS.</font> 

 (Win32) <tt>&quot;ctime&quot;</tt> is creation time instead of inode change time. 

 (Win32) <tt>&quot;dev&quot;</tt> and <tt>&quot;ino&quot;</tt> are not meaningful. 

 (<font SIZE="-1">VMS</font>) <tt>&quot;dev&quot;</tt> and <tt>&quot;ino&quot;</tt> are not necessarily reliable. 

 (RISC OS) <tt>&quot;mtime&quot;</tt>, <tt>&quot;atime&quot;</tt> and <tt>&quot;ctime&quot;</tt> all return the last modification time. <tt>&quot;dev&quot;</tt> and <tt>&quot;ino&quot;</tt> are not necessarily reliable. 

 (<font SIZE="-1">OS/2</font>) <tt>&quot;dev&quot;</tt>, <tt>&quot;rdev&quot;</tt>, <tt>&quot;blksize&quot;</tt>, and <tt>&quot;blocks&quot;</tt> are not available. <tt>&quot;ino&quot;</tt> is not meaningful and will differ between stat calls on the same file. 

 (Cygwin) Some versions of cygwin when doing a <tt>&quot;stat(&quot;foo&quot;)&quot;</tt> and not finding it may then attempt to <tt>&quot;stat(&quot;foo.exe&quot;)&quot;</tt>. 

 (Win32) <tt>&quot;stat&quot;</tt> needs to open the file to determine the link count and update attributes that may have been changed through hard links. Setting <tt>&quot;${^WIN32_SLOPPY_STAT}&quot;</tt> to a true value speeds up <tt>&quot;stat&quot;</tt> by not performing this operation.
<dt>symlink
<dd> (Win32, RISC OS) Not implemented. 

 (<font SIZE="-1">VMS</font>) Implemented on 64 bit <font SIZE="-1">VMS 8.3.</font> <font SIZE="-1">VMS</font> requires the symbolic link to be in Unix syntax if it is intended to resolve to a valid path.
<dt>syscall
<dd> (Win32, <font SIZE="-1">VMS,</font> RISC OS, <font SIZE="-1">VOS</font>) Not implemented.
<dt>sysopen
<dd> (Mac OS, <font SIZE="-1">OS/390</font>) The traditional <tt>0</tt>, <tt>1</tt>, and <tt>2</tt> MODEs are implemented with different numeric values on some systems. The flags exported by <tt>&quot;Fcntl&quot;</tt> (<tt>&quot;O_RDONLY&quot;</tt>, <tt>&quot;O_WRONLY&quot;</tt>, <tt>&quot;O_RDWR&quot;</tt>) should work everywhere though.
<dt>system
<dd> (Win32) As an optimization, may not call the command shell specified in <tt>$ENV{PERL5SHELL}</tt>. <tt>&quot;system(1, @args)&quot;</tt> spawns an external process and immediately returns its process designator, without waiting for it to terminate. Return value may be used subsequently in <tt>&quot;wait&quot;</tt> or <tt>&quot;waitpid&quot;</tt>. Failure to <tt>&quot;spawn()&quot;</tt> a subprocess is indicated by setting <tt>$?</tt> to <tt>&quot;255 &lt;&lt; 8&quot;</tt>. <tt>$?</tt> is set in a way compatible with Unix (i.e. the exit status of the subprocess is obtained by <tt>&quot;$? &gt;&gt; 8&quot;</tt>, as described in the documentation). 

 Note that the list form of <b>system()</b> is emulated since the Win32 <font SIZE="-1">API</font> <b>CreateProcess()</b> accepts a simple string rather than an array of command-line arguments. This may have security implications for your code. 

 (RISC OS) There is no shell to process metacharacters, and the native standard is to pass a command line terminated by ``\n'' ``\r'' or ``\0'' to the spawned program. Redirection such as <tt>&quot;&gt; foo&quot;</tt> is performed (if at all) by the run time library of the spawned program. <tt>&quot;system LIST&quot;</tt> will call the Unix emulation library's <tt>&quot;exec&quot;</tt> emulation, which attempts to provide emulation of the stdin, stdout, stderr in force in the parent, provided the child program uses a compatible version of the emulation library. <tt>&quot;system SCALAR&quot;</tt> will call the native command line directly and no such emulation of a child Unix program will occur. Mileage <b>will</b> vary. 

 (Win32) <tt>&quot;system LIST&quot;</tt> without the use of indirect object syntax (<tt>&quot;system PROGRAM LIST&quot;</tt>) may fall back to trying the shell if the first <tt>&quot;spawn()&quot;</tt> fails. 

 (SunOS, Solaris, HP-UX) Does not automatically flush output handles on some platforms. 

 (<font SIZE="-1">VMS</font>) As with Win32, <tt>&quot;system(1, @args)&quot;</tt> spawns an external process and immediately returns its process designator without waiting for the process to terminate. In this case the return value may be used subsequently in <tt>&quot;wait&quot;</tt> or <tt>&quot;waitpid&quot;</tt>. Otherwise the return value is POSIX-like (shifted up by 8 bits), which only allows room for a made-up value derived from the severity bits of the native 32-bit condition code (unless overridden by <tt>&quot;use vmsish 'status'&quot;</tt>). If the native condition code is one that has a <font SIZE="-1">POSIX</font> value encoded, the <font SIZE="-1">POSIX</font> value will be decoded to extract the expected exit value. For more details see ``$?'' in perlvms.
<dt>telldir
<dd> (Android) Not implemented.
<dt>times
<dd> (Win32) ``Cumulative'' times will be bogus. On anything other than Windows <font SIZE="-1">NT</font> or Windows 2000, ``system'' time will be bogus, and ``user'' time is actually the time returned by the <tt>&quot;clock()&quot;</tt> function in the C runtime library. 

 (RISC OS) Not useful.
<dt>truncate
<dd> (Older versions of <font SIZE="-1">VMS</font>) Not implemented. 

 (<font SIZE="-1">VOS</font>) Truncation to same-or-shorter lengths only. 

 (Win32) If a <font SIZE="-1">FILEHANDLE</font> is supplied, it must be writable and opened in append mode (i.e., use <tt>&quot;open(my $fh, '&gt;&gt;', 'filename')&quot;</tt> or <tt>&quot;sysopen(my $fh, ..., O_APPEND|O_RDWR)&quot;</tt>. If a filename is supplied, it should not be held open elsewhere.
<dt>umask
<dd> Returns <tt>&quot;undef&quot;</tt> where unavailable. 

 (AmigaOS) <tt>&quot;umask&quot;</tt> works but the correct permissions are set only when the file is finally closed.
<dt>utime
<dd> (<font SIZE="-1">VMS,</font> RISC OS) Only the modification time is updated. 

 (Win32) May not behave as expected. Behavior depends on the C runtime library's implementation of <tt>&quot;utime()&quot;</tt>, and the filesystem being used. The <font SIZE="-1">FAT</font> filesystem typically does not support an ``access time'' field, and it may limit timestamps to a granularity of two seconds.
<dt>wait
<dd>
<dt>waitpid
<dd> (Win32) Can only be applied to process handles returned for processes spawned using <tt>&quot;system(1, ...)&quot;</tt> or pseudo processes created with <tt>&quot;fork&quot;</tt>. 

 (RISC OS) Not useful.</dl>

<h2>Supported Platforms</h2>

 The following platforms are known to build Perl 5.12 (as of April 2010, its release date) from the standard source code distribution available at &lt;<a rel="nofollow" HREF="http://www.cpan.org/src">http://www.cpan.org/src</a>&gt;
<dl>
<dt>Linux (x86, <font SIZE="-1">ARM, IA64</font>)
<dd>
<dt>HP-UX
<dd>
<dt><font SIZE="-1">AIX</font>
<dd>
<dt>Win32
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Windows 2000
<dd>
<dt>Windows <font SIZE="-1">XP</font>
<dd>
<dt>Windows Server 2003
<dd>
<dt>Windows Vista
<dd>
<dt>Windows Server 2008
<dd>
<dt>Windows 7
<dd></dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Cygwin
<dd> Some tests are known to fail:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> <i>ext/XS-APItest/t/call_checker.t</i> - see &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=78502">https://rt.perl.org/Ticket/Display.html?id=78502</a>&gt;
<dt>&bull;
<dd> <i>dist/I18N-Collate/t/I18N-Collate.t</i>
<dt>&bull;
<dd> <i>ext/Win32CORE/t/win32core.t</i> - may fail on recent cygwin installs.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Solaris (x86, <font SIZE="-1">SPARC</font>)
<dd>
<dt>OpenVMS
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Alpha (7.2 and later)
<dd>
<dt>I64 (8.2 and later)
<dd></dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Symbian
<dd>
<dt>NetBSD
<dd>
<dt>FreeBSD
<dd>
<dt>Debian GNU/kFreeBSD
<dd>
<dt>Haiku
<dd>
<dt>Irix (6.5. What else?)
<dd>
<dt>OpenBSD
<dd>
<dt>Dragonfly <font SIZE="-1">BSD</font>
<dd>
<dt>Midnight <font SIZE="-1">BSD</font>
<dd>
<dt><font SIZE="-1">QNX</font> Neutrino <font SIZE="-1">RTOS</font> (6.5.0)
<dd>
<dt>MirOS <font SIZE="-1">BSD</font>
<dd>
<dt>Stratus OpenVOS (17.0 or later)
<dd> Caveats:
<dl>
<dt>
<dd>
<dl>
<dt>time_t issues that may or may not be fixed
<dd></dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Symbian (Series 60 v3, 3.2 and 5 - what else?)
<dd>
<dt>Stratus <font SIZE="-1">VOS /</font> OpenVOS
<dd>
<dt><font SIZE="-1">AIX</font>
<dd>
<dt>Android
<dd>
<dt>FreeMINT
<dd> Perl now builds with FreeMiNT/Atari. It fails a few tests, that needs some investigation. 

 The FreeMiNT port uses <font SIZE="-1">GNU</font> dld for loadable module capabilities. So ensure you have that library installed when building perl.</dl>

<h2>EOL Platforms</h2>

<h3>(Perl 5.20)</h3>

 The following platforms were supported by a previous version of Perl but have been officially removed from Perl's source code as of 5.20:
<dl>
<dt><font SIZE="-1">AT&amp;T</font> 3b1
<dd></dl>

<h3>(Perl 5.14)</h3>

 The following platforms were supported up to 5.10. They may still have worked in 5.12, but supporting code has been removed for 5.14:
<dl>
<dt>Windows 95
<dd>
<dt>Windows 98
<dd>
<dt>Windows <font SIZE="-1">ME</font>
<dd>
<dt>Windows <font SIZE="-1">NT4</font>
<dd></dl>

<h3>(Perl 5.12)</h3>

 The following platforms were supported by a previous version of Perl but have been officially removed from Perl's source code as of 5.12:
<dl>
<dt>Atari MiNT
<dd>
<dt>Apollo Domain/OS
<dd>
<dt>Apple Mac <font SIZE="-1">OS 8/9</font>
<dd>
<dt>Tenon Machten
<dd></dl>

<h2>Supported Platforms (Perl 5.8)</h2>

 As of July 2002 (the Perl release 5.8.0), the following platforms were able to build Perl from the standard source code distribution available at &lt;<a rel="nofollow" HREF="http://www.cpan.org/src/">http://www.cpan.org/src/</a>&gt; 

 <pre>
        AIX
        BeOS
        BSD/OS          (BSDi)
        Cygwin
        DG/UX
        DOS DJGPP       1)
        DYNIX/ptx
        EPOC R5
        FreeBSD
        HI-UXMPP        (Hitachi) (5.8.0 worked but we didn't know it)
        HP-UX
        IRIX
        Linux
        Mac OS Classic
        Mac OS X        (Darwin)
        MPE/iX
        NetBSD
        NetWare
        NonStop-UX
        ReliantUNIX     (formerly SINIX)
        OpenBSD
        OpenVMS         (formerly VMS)
        Open UNIX       (Unixware) (since Perl 5.8.1/5.9.0)
        OS/2
        OS/400          (using the PASE) (since Perl 5.8.1/5.9.0)
        POSIX-BC        (formerly BS2000)
        QNX
        Solaris
        SunOS 4
        SUPER-UX        (NEC)
        Tru64 UNIX      (formerly DEC OSF/1, Digital UNIX)
        UNICOS
        UNICOS/mk
        UTS
        VOS / OpenVOS
        Win95/98/ME/2K/XP 2)
        WinCE
        z/OS            (formerly OS/390)
        VM/ESA
        1) in DOS mode either the DOS or OS/2 ports can be used
        2) compilers: Borland, MinGW (GCC), VC6
</pre> 

 The following platforms worked with the previous releases (5.6 and 5.7), but we did not manage either to fix or to test these in time for the 5.8.0 release. There is a very good chance that many of these will work fine with the 5.8.0. 

 <pre>
        BSD/OS
        DomainOS
        Hurd
        LynxOS
        MachTen
        PowerMAX
        SCO SV
        SVR4
        Unixware
        Windows 3.1
</pre> 

 Known to be broken for 5.8.0 (but 5.6.1 and 5.7.2 can be used): 

 <pre>
        AmigaOS 3
</pre> 

 The following platforms have been known to build Perl from source in the past (5.005_03 and earlier), but we haven't been able to verify their status for the current release, either because the hardware/software platforms are rare or because we don't have an active champion on these platforms---or both. They used to work, though, so go ahead and try compiling them, and let perlbug [at] perl.org of any trouble. 

 <pre>
        3b1
        A/UX
        ConvexOS
        CX/UX
        DC/OSx
        DDE SMES
        DOS EMX
        Dynix
        EP/IX
        ESIX
        FPS
        GENIX
        Greenhills
        ISC
        MachTen 68k
        MPC
        NEWS-OS
        NextSTEP
        OpenSTEP
        Opus
        Plan 9
        RISC/os
        SCO ODT/OSR
        Stellar
        SVR2
        TI1500
        TitanOS
        Ultrix
        Unisys Dynix
</pre> 

 The following platforms have their own source code distributions and binaries available via &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/">http://www.cpan.org/ports/</a>&gt; 

 <pre>
                                Perl release
        OS/400 (ILE)            5.005_02
        Tandem Guardian         5.004
</pre> 

 The following platforms have only binaries available via &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/index.html">http://www.cpan.org/ports/index.html</a>&gt; : 

 <pre>
                                Perl release
        Acorn RISCOS            5.005_02
        AOS                     5.002
        LynxOS                  5.004_02
</pre> 

 Although we do suggest that you always build your own Perl from the source code, both for maximal configurability and for security, in case you are in a hurry you can check &lt;<a rel="nofollow" HREF="http://www.cpan.org/ports/index.html">http://www.cpan.org/ports/index.html</a>&gt; for binary distributions.

<h2>SEE ALSO</h2>

 perlaix, perlamiga, perlbs2000, perlce, perlcygwin, perldos, perlebcdic, perlfreebsd, perlhurd, perlhpux, perlirix, perlmacos, perlmacosx, perlnetware, perlos2, perlos390, perlos400, perlplan9, perlqnx, perlsolaris, perltru64, perlunicode, perlvms, perlvos, perlwin32, and Win32.

<h2>AUTHORS / CONTRIBUTORS</h2>

 Abigail &lt;abigail [at] abigail.be&gt;, Charles Bailey &lt;bailey [at] newman.upenn.edu&gt;, Graham Barr &lt;gbarr [at] pobox.com&gt;, Tom Christiansen &lt;tchrist [at] perl.com&gt;, Nicholas Clark &lt;nick [at] ccl4.org&gt;, Thomas Dorner &lt;Thomas.Dorner [at] start.de&gt;, Andy Dougherty &lt;doughera [at] lafayette.edu&gt;, Dominic Dunlop &lt;domo [at] computer.org&gt;, Neale Ferguson &lt;neale [at] vma.tabnsw.com.au&gt;, David J. Fiander &lt;davidf [at] mks.com&gt;, Paul Green &lt;Paul.Green [at] stratus.com&gt;, M.J.T. Guy &lt;mjtg [at] cam.ac.uk&gt;, Jarkko Hietaniemi &lt;jhi [at] iki.fi&gt;, Luther Huffman &lt;lutherh [at] stratcom.com&gt;, Nick Ing-Simmons &lt;nick [at] ing-simmons.net&gt;, Andreas J. König &lt;a.koenig [at] mind.de&gt;, Markus Laker &lt;mlaker [at] contax.co.uk&gt;, Andrew M. Langmead &lt;aml [at] world.std.com&gt;, Lukas Mai &lt;l.mai [at] web.de&gt;, Larry Moore &lt;ljmoore [at] freespace.net&gt;, Paul Moore &lt;Paul.Moore [at] uk.origin-it.com&gt;, Chris Nandor &lt;pudge [at] pobox.com&gt;, Matthias Neeracher &lt;neeracher [at] mac.com&gt;, Philip Newton &lt;pne [at] cpan.org&gt;, Gary Ng &lt;71564.1743 [at] CompuServe.COM&gt;, Tom Phoenix &lt;rootbeer [at] teleport.com&gt;, André Pirard &lt;A.Pirard [at] ulg.ac.be&gt;, Peter Prymmer &lt;pvhp [at] forte.com&gt;, Hugo van der Sanden &lt;hv [at] crypt0.demon.co.uk&gt;, Gurusamy Sarathy &lt;gsar [at] activestate.com&gt;, Paul J. Schinder &lt;schinder [at] pobox.com&gt;, Michael G Schwern &lt;schwern [at] pobox.com&gt;, Dan Sugalski &lt;dan [at] sidhe.org&gt;, Nathan Torkington &lt;gnat [at] frii.com&gt;, John Malmberg &lt;wb8tyw [at] qsl.net&gt; 

<h2>Index</h2>



<dt><a HREF="#lbAT">CPAN Testers</a>
<dd>
<dt><a HREF="#lbAU">PLATFORMS</a>
<dd>


<dt><a HREF="#lbBC">FUNCTION IMPLEMENTATIONS</a>
<dd>


<dt><a HREF="#lbBE">Supported Platforms</a>
<dd>
<dt><a HREF="#lbBF">EOL Platforms</a>
<dd>


<dt><a HREF="#lbBJ">Supported Platforms (Perl 5.8)</a>
<dd>
<dt><a HREF="#lbBK">SEE ALSO</a>
<dd>
<dt><a HREF="#lbBL">AUTHORS / CONTRIBUTORS</a>
<dd></dl>
