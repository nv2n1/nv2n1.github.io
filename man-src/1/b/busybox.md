---

title: "busybox(1)"
name: "busybox"
section: "1"
letter: "b"
url: "/docs/linux/man/1-busybox/"
description: "BusyBox – The Swiss Army Knife of Embedded Linux"
---

<p> BusyBox &#8211; The Swiss Army Knife of Embedded Linux </p>
<h2>SYNTAX</h2>
<pre><code>
busybox&lt;applet&gt;[arguments...] # or
    &lt;applet&gt;[arguments...] #if symlinked
</code></pre>
<h2>DESCRIPTION</h2>
<p> BusyBox combines tiny versions of many common UNIX utilities into a single small executable. It provides minimalist replacements for most of the utilities you usually find in GNU coreutils, util-linux, etc. The utilities in BusyBox generally have fewer options than their full-featured GNU cousins; however, the options that are included provide the expected functionality and behave very much like their GNU counterparts. </p>
<p> BusyBox has been written with size-optimization and limited resources in mind. It is also extremely modular so you can easily include or exclude commands (or features) at compile time. This makes it easy to customize your embedded systems. To create a working system, just add /dev, /etc, and a Linux kernel. BusyBox provides a fairly complete POSIX environment for any small or embedded system. </p>
<p> BusyBox is extremely configurable. This allows you to include only the components you need, thereby reducing binary size. Run &#8216;make config&#8217; or &#8216;make menuconfig&#8217; to select the functionality that you wish to enable. Then run &#8216;make&#8217; to compile BusyBox using your configuration. </p>
<p> After the compile has finished, you should use &#8216;make install&#8217; to install BusyBox. This will install the &#8216;bin/busybox&#8217; binary, in the target directory specified by CONFIG_PREFIX. CONFIG_PREFIX can be set when configuring BusyBox, or you can specify an alternative location at install time (i.e., with a command line like &#8216;make CONFIG_PREFIX=/tmp/foo install&#8217;). If you enabled any applet installation scheme (either as symlinks or hardlinks), these will also be installed in the location pointed to by CONFIG_PREFIX.</p>
<h2>USAGE</h2>
<p> BusyBox is a multi-call binary. A multi-call binary is an executable program that performs the same job as more than one utility program. That means there is just a single BusyBox binary, but that single binary acts like a large number of utilities. This allows BusyBox to be smaller since all the built-in utility programs (we call them applets) can share code for many common operations. </p>
<p> You can also invoke BusyBox by issuing a command as an argument on the command line. For example, entering </p>
<pre>
        /bin/busybox ls
</pre>
<p> will also cause BusyBox to behave as &#8216;ls&#8217;. </p>
<p> Of course, adding &#8216;/bin/busybox&#8217; into every command would be painful. So most people will invoke BusyBox using links to the BusyBox binary. </p>
<p> For example, entering </p>
<pre>
        ln -s /bin/busybox ls
        ./ls
</pre>
<p> will cause BusyBox to behave as &#8216;ls&#8217; (if the &#8216;ls&#8217; command has been compiled into BusyBox). Generally speaking, you should never need to make all these links yourself, as the BusyBox build system will do this for you when you run the &#8216;make install&#8217; command. </p>
<p> If you invoke BusyBox with no arguments, it will provide you with a list of the applets that have been compiled into your BusyBox binary.</p>
<h2>COMMON OPTIONS</h2>
<p> Most BusyBox applets support the <code>&#8211;help</code> argument to provide a terse runtime description of their behavior. If the CONFIG_FEATURE_VERBOSE_USAGE option has been enabled, more detailed usage information will also be available.</p>
<h2>COMMANDS</h2>
<p> Currently available applets include: </p>
<p>        [, [[, acpid, adjtimex, ar, arch, arp, arping, ash, awk, basename,<br/>
        bc, blkdiscard, blockdev, brctl, bunzip2, busybox, bzcat, bzip2,<br/>
        cal, cat, chgrp, chmod, chown, chpasswd, chroot, chvt, clear, cmp,<br/>
        cp, cpio, crond, crontab, cttyhack, cut, date, dc, dd, deallocvt,<br/>
        depmod, devmem, df, diff, dirname, dmesg, dnsdomainname, dos2unix,<br/>
        dpkg, dpkg-deb, du, dumpkmap, dumpleases, echo, ed, egrep, env,<br/>
        expand, expr, factor, fallocate, false, fatattr, fdisk, fgrep, find,<br/>
        fold, free, freeramdisk, fsfreeze, fstrim, ftpget, ftpput, getopt,<br/>
        getty, grep, groups, gunzip, gzip, halt, head, hexdump, hostid,<br/>
        hostname, httpd, hwclock, i2cdetect, i2cdump, i2cget, i2cset, id,<br/>
        ifconfig, ifdown, ifup, init, insmod, ionice, ip, ipcalc, ipneigh,<br/>
        kill, killall, klogd, last, less, link, linux32, linux64, linuxrc,<br/>
        ln, loadfont, loadkmap, logger, login, logname, logread, losetup,<br/>
        ls, lsmod, lsscsi, lzcat, lzma, lzop, md5sum, mdev, microcom, mkdir,<br/>
        mkdosfs, mke2fs, mkfifo, mknod, mkpasswd, mkswap, mktemp, modinfo,<br/>
        modprobe, more, mount, mt, mv, nameif, nc, netstat, nl, nologin,<br/>
        nproc, nsenter, nslookup, nuke, od, openvt, partprobe, passwd,<br/>
        paste, patch, pidof, ping, ping6, pivot_root, poweroff, printf, ps,<br/>
        pwd, rdate, readlink, realpath, reboot, renice, reset, resume, rev,<br/>
        rm, rmdir, rmmod, route, rpm, rpm2cpio, run-init, run-parts, sed,<br/>
        seq, setkeycodes, setpriv, setsid, sh, sha1sum, sha256sum,<br/>
        sha512sum, shred, shuf, sleep, sort, ssl_client, start-stop-daemon,<br/>
        stat, static-sh, strings, stty, su, sulogin, svc, svok, swapoff,<br/>
        swapon, switch_root, sync, sysctl, syslogd, tac, tail, tar, taskset,<br/>
        tc, tee, telnet, telnetd, test, tftp, time, timeout, top, touch, tr,<br/>
        traceroute, traceroute6, true, truncate, tty, tunctl, ubirename,<br/>
        udhcpc, udhcpd, uevent, umount, uname, uncompress, unexpand, uniq,<br/>
        unix2dos, unlink, unlzma, unshare, unxz, unzip, uptime, usleep,<br/>
        uudecode, uuencode, vconfig, vi, w, watch, watchdog, wc, wget,<br/>
        which, who, whoami, xargs, xxd, xz, xzcat, yes, zcat</p>
<h2>COMMAND DESCRIPTIONS</h2>
<dl>
<dt><code>acpid</code></dt>
<dd> acpid [-df] [-c CONFDIR] [-l LOGFILE] [-a ACTIONFILE] [-M MAPFILE] [-e PROC_EVENT_FILE] [-p PIDFILE] </dd>
<p> Listen to ACPI events and spawn specific helpers on event arrival </p>
<p>&#8211; d Log to stderr, not log file(implies &#8211; f) &#8211; f Run in foreground &#8211; c DIR Config directory[/ etc / acpi] &#8211; e FILE / proc event file[/ proc / acpi / event] &#8211; l FILE Log file[/ var / log / acpid.log] &#8211; p FILE Pid file[/ var / run / acpid.pid] &#8211; a FILE Action file[/ etc / acpid.conf] &#8211; M FILE Map file[/ etc / acpi.map]</p>
<p> Accept and ignore compatibility options -g -m -s -S -v</p>
<dt><code>adjtimex</code></dt>
<dd> adjtimex [-q] [-o OFF] [-f FREQ] [-p TCONST] [-t TICK] </dd>
<p> Read or set kernel time variables. See <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2) </p>
<pre>
        -q      Quiet
        -o OFF  Time offset, microseconds
        -f FREQ Frequency adjust, integer kernel units (65536 is 1ppm)
        -t TICK Microseconds per tick, usually 10000
                (positive -t or -f values make clock run faster)
        -p TCONST
</pre>
<dt><code>ar</code></dt>
<dd> ar [-o] [-v] [-p] [-t] [-x] ARCHIVE FILES </dd>
<p> Extract or list FILES from an ar archive </p>
<pre>
        -o      Preserve original dates
        -p      Extract to stdout
        -t      List
        -x      Extract
        -v      Verbose
</pre>
<dt><code>arch</code></dt>
<dd> arch </dd>
<p> Print system architecture</p>
<dt><code>arp</code></dt>
<dd> arp [-vn]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-H HWTYPE] [-i IF] -a [HOSTNAME]<br/>
 [-v]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> [-i IF] -d HOSTNAME [pub]<br/>
 [-v]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-H HWTYPE] [-i IF] -s HOSTNAME HWADDR [temp]<br/>
 [-v]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-H HWTYPE] [-i IF] -s HOSTNAME HWADDR [netmask MASK] pub<br/>
 [-v]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-H HWTYPE] [-i IF] -Ds HOSTNAME IFACE [netmask MASK] pub</dd>
<p> Manipulate ARP cache </p>
<pre>
        -a              Display (all) hosts
        -d              Delete ARP entry
        -s              Set new entry
        -v              Verbose
        -n              Don't resolve names
        -i IF           Network interface
        -D              Read HWADDR from IFACE
        -A,-p AF        Protocol family
        -H HWTYPE       Hardware address type
</pre>
<dt><code>arping</code></dt>
<dd> arping [-fqbDUA] [-c CNT] [-w TIMEOUT] [-I IFACE] [-s SRC_IP] DST_IP </dd>
<p> Send ARP requests/replies </p>
<pre>
        -f              Quit on first ARP reply
        -q              Quiet
        -b              Keep broadcasting, don't go unicast
        -D              Exit with 1 if DST_IP replies
        -U              Unsolicited ARP mode, update your neighbors
        -A              ARP answer mode, update your neighbors
        -c N            Stop after sending N ARP requests
        -w TIMEOUT      Seconds to wait for ARP reply
        -I IFACE        Interface to use (default eth0)
        -s SRC_IP       Sender IP address
        DST_IP          Target IP address
</pre>
<dt><code>ash</code></dt>
<dd> ash [-/+OPTIONS] [-/+o OPT]&#8230; [-c &#8216;SCRIPT&#8216; [ARG0 [ARGS]] / FILE [ARGS] / -s [ARGS]] </dd>
<p> Unix shell interpreter</p>
<dt><code>awk</code></dt>
<dd> awk [OPTIONS] [AWK_PROGRAM] [FILE]&#8230; </dd>
<pre>
        -v VAR=VAL      Set variable
        -F SEP          Use SEP as field separator
        -f FILE         Read program from FILE
        -e AWK_PROGRAM
</pre>
<dt><code>basename</code></dt>
<dd> basename FILE [SUFFIX] </dd>
<p> Strip directory path and .SUFFIX from FILE</p>
<dt><code>bc</code></dt>
<dd> bc [-sqlw] FILE&#8230; </dd>
<p> Arbitrary precision calculator </p>
<pre>
        -q      Quiet
        -l      Load standard math library
        -s      Be POSIX compatible
        -w      Warn if extensions are used
</pre>
<p> <tt>$BC_LINE_LENGTH</tt> changes output width</p>
<dt><code>blkdiscard</code></dt>
<dd> blkdiscard [-o OFS] [-l LEN] [-s] DEVICE </dd>
<p> Discard sectors on DEVICE </p>
<pre>
        -o OFS  Byte offset into device
        -l LEN  Number of bytes to discard
        -s      Perform a secure discard
</pre>
<dt><code>blockdev</code></dt>
<dd> blockdev OPTION BLOCKDEV </dd>
<p>&#8211;setro Set ro&#8211; setrw Set rw&#8211; getro Get ro&#8211; getss Get sector size&#8211; getbsz Get block size&#8211; setbsz BYTES Set block size&#8211; getsz Get device size in 512 &#8211; byte sectors&#8211; getsize64 Get device size in bytes&#8211; flushbufs Flush buffers&#8211; rereadpt Reread partition table</p>
<dt><code>brctl</code></dt>
<dd> brctl COMMAND [BRIDGE [INTERFACE]] </dd>
<p> Manage ethernet bridges </p>
<p> Commands: </p>
<pre>
        addbr BRIDGE            Create BRIDGE
        delbr BRIDGE            Delete BRIDGE
        addif BRIDGE IFACE      Add IFACE to BRIDGE
        delif BRIDGE IFACE      Delete IFACE from BRIDGE
</pre>
<dt><code>bunzip2</code></dt>
<dd> bunzip2 [-cfk] [FILE]&#8230; </dd>
<p> Decompress FILEs (or stdin) </p>
<pre>
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>bzcat</code></dt>
<dd> bzcat [FILE]&#8230; </dd>
<p> Decompress to stdout</p>
<dt><code>bzip2</code></dt>
<dd> bzip2 [OPTIONS] [FILE]&#8230; </dd>
<p> Compress FILEs (or stdin) with bzip2 algorithm </p>
<pre>
        -1..9   Compression level
        -d      Decompress
        -t      Test file integrity
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>cal</code></dt>
<dd> cal [-jy] [[MONTH] YEAR] </dd>
<p> Display a calendar </p>
<pre>
        -j      Use julian dates
        -y      Display the entire year
</pre>
<dt><code>cat</code></dt>
<dd> cat [-nbvteA] [FILE]&#8230; </dd>
<p> Print FILEs to stdout </p>
<pre>
        -n      Number output lines
        -b      Number nonempty lines
        -v      Show nonprinting characters as ^x or M-x
        -t      ...and tabs as ^I
        -e      ...and end lines with $
        -A      Same as -vte
</pre>
<dt><code>chgrp</code></dt>
<dd> chgrp [-RhLHPcvf]&#8230; GROUP FILE&#8230; </dd>
<p> Change the group membership of each FILE to GROUP </p>
<pre>
        -R      Recurse
        -h      Affect symlinks instead of symlink targets
        -L      Traverse all symlinks to directories
        -H      Traverse symlinks on command line only
        -P      Don't traverse symlinks (default)
        -c      List changed files
        -v      Verbose
        -f      Hide errors
</pre>
<dt><code>chmod</code></dt>
<dd> chmod [-Rcvf] MODE[,MODE]&#8230; FILE&#8230; </dd>
<p> Each MODE is one or more of the letters ugoa, one of the symbols +-= and one or more of the letters rwxst </p>
<pre>
        -R      Recurse
        -c      List changed files
        -v      List all files
        -f      Hide errors
</pre>
<dt><code>chown</code></dt>
<dd> chown [-RhLHPcvf]&#8230; USER[:[GRP]] FILE&#8230; </dd>
<p> Change the owner and/or group of each FILE to USER and/or GRP </p>
<pre>
        -R      Recurse
        -h      Affect symlinks instead of symlink targets
        -L      Traverse all symlinks to directories
        -H      Traverse symlinks on command line only
        -P      Don't traverse symlinks (default)
        -c      List changed files
        -v      List all files
        -f      Hide errors
</pre>
<dt><code>chpasswd</code></dt>
<dd> chpasswd [&#8211;md5|&#8211;encrypted|&#8211;crypt-method|&#8211;root] </dd>
<p> Read user:password from stdin and update /etc/passwd </p>
<p>&#8211; e, &#8211;encrypted Supplied passwords are in encrypted form &#8211; m, &#8211;md5 Encrypt using md5, not des &#8211; c, &#8211;crypt &#8211; method ALG des, md5, sha256 / 512(default sha256) &#8211; R, &#8211;root DIR Directory to chroot into</p>
<dt><code>chroot</code></dt>
<dd> chroot NEWROOT [PROG ARGS] </dd>
<p> Run PROG with root directory set to NEWROOT</p>
<dt><code>chvt</code></dt>
<dd> chvt N </dd>
<p> Change the foreground virtual terminal to /dev/ttyN</p>
<dt><code>clear</code></dt>
<dd> clear </dd>
<p> Clear screen</p>
<dt><code>cmp</code></dt>
<dd> cmp [-l] [-s] FILE1 [FILE2 [SKIP1 [SKIP2]]] </dd>
<p> Compare FILE1 with FILE2 (or stdin) </p>
<pre>
        -l      Write the byte numbers (decimal) and values (octal)
                for all differing bytes
        -s      Quiet
</pre>
<dt><code>cp</code></dt>
<dd> cp [OPTIONS] SOURCE&#8230; DEST </dd>
<p> Copy SOURCE(s) to DEST </p>
<pre>
        -a      Same as -dpR
        -R,-r   Recurse
        -d,-P   Preserve symlinks (default if -R)
        -L      Follow all symlinks
        -H      Follow symlinks on command line
        -p      Preserve file attributes if possible
        -f      Overwrite
        -i      Prompt before overwrite
        -l,-s   Create (sym)links
        -T      Treat DEST as a normal file
        -u      Copy only newer files
</pre>
<dt><code>cpio</code></dt>
<dd> cpio [-dmvu] [-F FILE] [-R USER[:GRP]] [-H newc] [-tio] [EXTR_FILE]&#8230; </dd>
<p> Extract (-i) or list (-t) files from a cpio archive, or take file list from stdin and create an archive (-o) </p>
<p> Main operation mode: </p>
<pre>
        -t      List
        -i      Extract EXTR_FILEs (or all)
        -o      Create (requires -H newc)
Options:
        -H newc Archive format
        -d      Make leading directories
        -m      Preserve mtime
        -v      Verbose
        -u      Overwrite
        -F FILE Input (-t,-i,-p) or output (-o) file
        -R USER[:GRP]   Set owner of created files
        -L      Dereference symlinks
        -0      Input is separated by NULs
</pre>
<dt><code>crond</code></dt>
<dd> crond -fbS -l N -L LOGFILE -c DIR </dd>
<pre>
        -f      Foreground
        -b      Background (default)
        -S      Log to syslog (default)
        -l N    Set log level. Most verbose 0, default 8
        -L FILE Log to FILE
        -c DIR  Cron dir. Default:/var/spool/cron/crontabs
</pre>
<dt><code>crontab</code></dt>
<dd> crontab [-c DIR] [-u USER] [-ler]|[FILE] </dd>
<pre>
        -c      Crontab directory
        -u      User
        -l      List crontab
        -e      Edit crontab
        -r      Delete crontab
        FILE    Replace crontab by FILE ('-': stdin)
</pre>
<dt><code>cttyhack</code></dt>
<dd> cttyhack [PROG ARGS] </dd>
<p> Give PROG a controlling tty if possible. Example for /etc/inittab (for busybox init): <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>::respawn:/bin/cttyhack /bin/sh<br/>
 Giving controlling tty to shell running with PID 1: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>$ exec cttyhack sh<br/>
 Starting interactive shell from boot shell script: </p>
<pre>
        setsid cttyhack sh
</pre>
<dt><code>cut</code></dt>
<dd> cut [OPTIONS] [FILE]&#8230; </dd>
<p> Print selected fields from each input FILE to stdout </p>
<pre>
        -b LIST Output only bytes from LIST
        -c LIST Output only characters from LIST
        -d CHAR Use CHAR instead of tab as the field delimiter
        -s      Output only the lines containing delimiter
        -f N    Print only these fields
        -n      Ignored
</pre>
<dt><code>date</code></dt>
<dd> date [OPTIONS] [+FMT] [TIME] </dd>
<p> Display time (using +FMT), or set time </p>
<p>        [-s,&#8211;set] TIME Set time to TIME<br/>
        -u,&#8211;utc        Work in UTC (don&#8217;t convert to local time)<br/>
        -R,&#8211;rfc-2822   Output RFC-2822 compliant date string<br/>
        -I[SPEC]        Output ISO-8601 compliant date string<br/>
                        SPEC=&#8217;date&#8217; (default) for date only,<br/>
                        &#8216;hours&#8217;, &#8216;minutes&#8217;, or &#8216;seconds&#8217; for date and<br/>
                        time to the indicated precision<br/>
        -r,&#8211;reference FILE     Display last modification time of FILE<br/>
        -d,&#8211;date TIME  Display TIME, not &#8216;now&#8217;<br/>
        -D FMT          Use FMT for -d TIME conversion</p>
<p> Recognized TIME formats: </p>
<p>hh : mm[:ss]<br/>
         [YYYY.] MM.DD &#8211; hh : mm<br/>
     [:ss] YYYY &#8211; MM &#8211; DD hh : mm<br/>
     [:ss]<br/>
         [[[[[YY] YY] MM] DD] hh] mm[.ss] &#8216;date TIME&#8217; form accepts MMDDhhmm[[YY] YY][.ss] instead</p>
<dt><code>dc</code></dt>
<dd> dc [-x] [-eSCRIPT]&#8230; [-fFILE]&#8230; [FILE]&#8230; </dd>
<p> Tiny RPN calculator. Operations: +, -, *, /, %, ~, ^, |, p &#8211; print top of the stack without popping f &#8211; print entire stack k &#8211; pop the value and set the precision i &#8211; pop the value and set input radix o &#8211; pop the value and set output radix Examples: dc -e&#8217;2 2 + p&#8217; -&gt; 4, dc -e&#8217;8 8 * 2 2 + / p&#8217; -&gt; 16</p>
<dt><code>dd</code></dt>
<dd> dd [if=FILE] [of=FILE] [ibs=N obs=N/bs=N] [count=N] [skip=N] [seek=N] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[conv=notrunc|noerror|sync|fsync]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[iflag=skip_bytes|fullblock] [oflag=seek_bytes]</dd>
<p> Copy a file with converting and formatting </p>
<pre>
        if=FILE         Read from FILE instead of stdin
        of=FILE         Write to FILE instead of stdout
        bs=N            Read and write N bytes at a time
        ibs=N           Read N bytes at a time
        obs=N           Write N bytes at a time
        count=N         Copy only N input blocks
        skip=N          Skip N input blocks
        seek=N          Skip N output blocks
        conv=notrunc    Don't truncate output file
        conv=noerror    Continue after read errors
        conv=sync       Pad blocks with zeros
        conv=fsync      Physically write data out before finishing
        conv=swab       Swap every pair of bytes
        iflag=skip_bytes        skip=N is in bytes
        iflag=fullblock Read full blocks
        oflag=seek_bytes        seek=N is in bytes
        status=noxfer   Suppress rate output
        status=none     Suppress all output
</pre>
<p> N may be suffixed by c (1), w (2), b (512), kB (1000), k (1024), MB, M, GB, G</p>
<dt><code>deallocvt</code></dt>
<dd> deallocvt [N] </dd>
<p> Deallocate unused virtual terminal /dev/ttyN</p>
<dt><code>depmod</code></dt>
<dd> depmod [-n] [-b BASE] [VERSION] [MODFILES]&#8230; </dd>
<p> Generate modules.dep, alias, and symbols files </p>
<pre>
        -b BASE Use BASE/lib/modules/VERSION
        -n      Dry run: print files to stdout
</pre>
<dt><code>devmem</code></dt>
<dd> devmem ADDRESS [WIDTH [VALUE]] </dd>
<p> Read/write from physical address </p>
<pre>
        ADDRESS Address to act upon
        WIDTH   Width (8/16/...)
        VALUE   Data to be written
</pre>
<dt><code>df</code></dt>
<dd> df [-PkmhTai] [-B SIZE] [FILESYSTEM]&#8230; </dd>
<p> Print filesystem usage statistics </p>
<pre>
        -P      POSIX output format
        -k      1024-byte blocks (default)
        -m      1M-byte blocks
        -h      Human readable (e.g. 1K 243M 2G)
        -T      Print filesystem type
        -a      Show all filesystems
        -i      Inodes
        -B SIZE Blocksize
</pre>
<dt><code>diff</code></dt>
<dd> diff [-abBdiNqrTstw] [-L LABEL] [-S FILE] [-U LINES] FILE1 FILE2 </dd>
<p> Compare files line by line and output the differences between them. This implementation supports unified diffs only. </p>
<pre>
        -a      Treat all files as text
        -b      Ignore changes in the amount of whitespace
        -B      Ignore changes whose lines are all blank
        -d      Try hard to find a smaller set of changes
        -i      Ignore case differences
        -L      Use LABEL instead of the filename in the unified header
        -N      Treat absent files as empty
        -q      Output only whether files differ
        -r      Recurse
        -S      Start with FILE when comparing directories
        -T      Make tabs line up by prefixing a tab when necessary
        -s      Report when two files are the same
        -t      Expand tabs to spaces in output
        -U      Output LINES lines of context
        -w      Ignore all whitespace
</pre>
<dt><code>dirname</code></dt>
<dd> dirname FILENAME </dd>
<p> Strip non-directory suffix from FILENAME</p>
<dt><code>dmesg</code></dt>
<dd> dmesg [-c] [-n LEVEL] [-s SIZE] </dd>
<p> Print or control the kernel ring buffer </p>
<pre>
        -c              Clear ring buffer after printing
        -n LEVEL        Set console logging level
        -s SIZE         Buffer size
        -r              Print raw message buffer
</pre>
<dt><code>dos2unix</code></dt>
<dd> dos2unix [-ud] [FILE] </dd>
<p> Convert FILE in-place from DOS to Unix format. When no file is given, use stdin/stdout. </p>
<pre>
        -u      dos2unix
        -d      unix2dos
</pre>
<dt><code>dpkg</code></dt>
<dd> dpkg [-ilCPru] [-F OPT] PACKAGE </dd>
<p> Install, remove and manage Debian packages </p>
<p>        -i,&#8211;install    Install the package<br/>
        -l,&#8211;list       List of installed packages<br/>
        &#8211;configure     Configure an unpackaged package<br/>
        -P,&#8211;purge      Purge all files of a package<br/>
        -r,&#8211;remove     Remove all but the configuration files for a package<br/>
        &#8211;unpack        Unpack a package, but don&#8217;t configure it<br/>
        &#8211;force-depends Ignore dependency problems<br/>
        &#8211;force-confnew Overwrite existing config files when installing<br/>
        &#8211;force-confold Keep old config files when installing</p>
<dt><code>dpkg-deb</code></dt>
<dd> dpkg-deb [-cefxX] FILE [DIR] </dd>
<p> Perform actions on Debian packages (.deb) </p>
<pre>
        -c      List files
        -f      Print control fields
        -e      Extract control files to DIR (default: ./DEBIAN)
        -x      Extract files to DIR (no default)
        -X      Verbose -x
</pre>
<dt><code>du</code></dt>
<dd> du [-aHLdclsxhmk] [FILE]&#8230; </dd>
<p> Summarize disk space used for each FILE and/or directory </p>
<pre>
        -a      Show file sizes too
        -L      Follow all symlinks
        -H      Follow symlinks on command line
        -d N    Limit output to directories (and files with -a) of depth &lt; N
        -c      Show grand total
        -l      Count sizes many times if hard linked
        -s      Display only a total for each argument
        -x      Skip directories on different filesystems
        -h      Sizes in human readable format (e.g., 1K 243M 2G)
        -m      Sizes in megabytes
        -k      Sizes in kilobytes (default)
</pre>
<dt><code>dumpkmap</code></dt>
<dd> dumpkmap &gt; keymap </dd>
<p> Print a binary keyboard translation table to stdout</p>
<dt><code>dumpleases</code></dt>
<dd> dumpleases [-r|-a] [-d] [-f LEASEFILE] </dd>
<p> Display DHCP leases granted by udhcpd </p>
<p>&#8211; f, &#8211;file FILE Lease file &#8211; r, &#8211;remaining Show remaining time &#8211; a, &#8211;absolute Show expiration time &#8211; d, &#8211;decimal Show time in seconds</p>
<dt><code>echo</code></dt>
<dd> echo [-neE] [ARG]&#8230; </dd>
<p> Print the specified ARGs to stdout </p>
<pre>
        -n      Suppress trailing newline
        -e      Interpret backslash escapes (i.e., 	=tab)
        -E      Don't interpret backslash escapes (default)
</pre>
<dt><code>ed</code></dt>
<dd> ed [FILE]</dd>
<dt><code>env</code></dt>
<dd> env [-iu] [-] [name=value]&#8230; [PROG ARGS] </dd>
<p> Print the current environment or run PROG after setting up the specified environment </p>
<pre>
        -, -i   Start with an empty environment
        -u      Remove variable from the environment
</pre>
<dt><code>expand</code></dt>
<dd> expand [-i] [-t N] [FILE]&#8230; </dd>
<p> Convert tabs to spaces, writing to stdout </p>
<pre>
        -i      Don't convert tabs after non blanks
        -t      Tabstops every N chars
</pre>
<dt><code>expr</code></dt>
<dd> expr EXPRESSION </dd>
<p> Print the value of EXPRESSION to stdout </p>
<p> EXPRESSION may be: </p>
<p>ARG1 | ARG2 ARG1 if it is neither null nor 0, otherwise ARG2 ARG1 &amp;ARG2 ARG1 if neither argument is null or 0, otherwise 0 ARG1&lt;ARG2 1 if ARG1 is less than ARG2, else 0. Similarly : ARG1 &lt;= ARG2 ARG1 = ARG2 ARG1 != ARG2 ARG1 &gt;= ARG2 ARG1&gt; ARG2 ARG1 + ARG2 Sum of ARG1 and ARG2.Similarly : ARG1 &#8211; ARG2 ARG1 *ARG2 ARG1 / ARG2 ARG1 % ARG2 STRING : REGEXP Anchored pattern match of REGEXP in STRING match STRING REGEXP Same as STRING : REGEXP substr STRING POS LENGTH Substring of STRING, POS counted from 1 index STRING CHARS Index in STRING where any CHARS is found, or 0 length STRING Length of STRING<br/>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             quote TOKEN Interpret TOKEN as a string,<br/>
    even if it is a keyword like &#8216;match&#8217; or an<br/>
                                            operator like &#8216;/'(EXPRESSION)Value of EXPRESSION</p>
<p> Beware that many operators need to be escaped or quoted for shells. Comparisons are arithmetic if both ARGs are numbers, else lexicographical. Pattern matches return the string matched between \( and \) or null; if \( and \) are not used, they return the number of characters matched or 0.</p>
<dt><code>factor</code></dt>
<dd> factor [NUMBER]&#8230; </dd>
<p> Print prime factors</p>
<dt><code>fallocate</code></dt>
<dd> fallocate [-o OFS] -l LEN FILE </dd>
<p> Preallocate space for FILE </p>
<pre>
        -o OFS  Offset of range
        -l LEN  Length of range
</pre>
<dt><code>fatattr</code></dt>
<dd> fatattr [-+rhsvda] FILE&#8230; </dd>
<p> Change file attributes on FAT filesystem </p>
<pre>
        -       Clear attributes
        +       Set attributes
        r       Read only
        h       Hidden
        s       System
        v       Volume label
        d       Directory
        a       Archive
</pre>
<dt><code>fdisk</code></dt>
<dd> fdisk [-ul] [-C CYLINDERS] [-H HEADS] [-S SECTORS] [-b SSZ] DISK </dd>
<p> Change partition table </p>
<pre>
        -u              Start and End are in sectors (instead of cylinders)
        -l              Show partition table for each DISK, then exit
        -b 2048         (for certain MO disks) use 2048-byte sectors
        -C CYLINDERS    Set number of cylinders/heads/sectors
        -H HEADS        Typically 255
        -S SECTORS      Typically 63
</pre>
<dt><code>find</code></dt>
<dd> find [-HL] [PATH]&#8230; [OPTIONS] [ACTIONS] </dd>
<p> Search for files and perform actions on them. First failed action stops processing of current file. Defaults: PATH is current directory, action is &#8216;-print&#8217; </p>
<pre>
        -L,-follow      Follow symlinks
        -H              ...on command line only
        -xdev           Don't descend directories on other filesystems
        -maxdepth N     Descend at most N levels. -maxdepth 0 applies
                        actions to command line arguments only
        -mindepth N     Don't act on first N levels
        -depth          Act on directory *after* traversing it
</pre>
<p> Actions: </p>
<p>        ( ACTIONS )     Group actions for -o / -a<br/>
        ! ACT           Invert ACT&#8217;s success/failure<br/>
        ACT1 [-a] ACT2  If ACT1 fails, stop, else do ACT2<br/>
        ACT1 -o ACT2    If ACT1 succeeds, stop, else do ACT2<br/>
                        Note: -a has higher priority than -o<br/>
        -name PATTERN   Match file name (w/o directory name) to PATTERN<br/>
        -iname PATTERN  Case insensitive -name<br/>
        -path PATTERN   Match path to PATTERN<br/>
        -ipath PATTERN  Case insensitive -path<br/>
        -regex PATTERN  Match path to regex PATTERN<br/>
        -type X         File type is X (one of: f,d,l,b,c,s,p)<br/>
        -executable     File is executable<br/>
        -perm MASK      At least one mask bit (+MASK), all bits (-MASK),<br/>
                        or exactly MASK bits are set in file&#8217;s mode<br/>
        -mtime DAYS     mtime is greater than (+N), less than (-N),<br/>
                        or exactly N days in the past<br/>
        -mmin MINS      mtime is greater than (+N), less than (-N),<br/>
                        or exactly N minutes in the past<br/>
        -newer FILE     mtime is more recent than FILE&#8217;s<br/>
        -inum N         File has inode number N<br/>
        -user NAME/ID   File is owned by given user<br/>
        -group NAME/ID  File is owned by given group<br/>
        -size N[bck]    File size is N (c:bytes,k:kbytes,b:512 bytes(def.))<br/>
                        +/-N: file size is bigger/smaller than N<br/>
        -links N        Number of links is greater than (+N), less than (-N),<br/>
                        or exactly N<br/>
        -prune          If current file is directory, don&#8217;t descend into it<br/>
If none of the following actions is specified, -print is assumed<br/>
        -print          Print file name<br/>
        -print0         Print file name, NUL terminated<br/>
        -exec CMD ARG ;<br/>
        Run CMD with all instances of<br/>
        {<br/>
        }<br/>
        replaced by<br/>
                file name.Fails if CMD exits with nonzero &#8211;<br/>
            exec CMD ARG + Run CMD with<br/>
        {<br/>
        }<br/>
        replaced by list of file names &#8211; quit Exit</p>
<dt><code>fold</code></dt>
<dd> fold [-bs] [-w WIDTH] [FILE]&#8230; </dd>
<p> Wrap input lines in each FILE (or stdin), writing to stdout </p>
<pre>
        -b      Count bytes rather than columns
        -s      Break at spaces
        -w      Use WIDTH columns instead of 80
</pre>
<dt><code>free</code></dt>
<dd> free [-b/k/m/g] </dd>
<p> Display the amount of free and used system memory</p>
<dt><code>freeramdisk</code></dt>
<dd> freeramdisk DEVICE </dd>
<p> Free all memory used by the specified ramdisk</p>
<dt><code>fsfreeze</code></dt>
<dd> fsfreeze &#8211;[un]freeze MOUNTPOINT </dd>
<p> Flush and halt writes to MOUNTPOINT</p>
<dt><code>fstrim</code></dt>
<dd> fstrim [OPTIONS] MOUNTPOINT </dd>
<p>&#8211; o, &#8211;offset OFFSET Offset in bytes to discard from &#8211; l, &#8211;length LEN Bytes to discard &#8211; m, &#8211;minimum MIN Minimum extent length &#8211; v, &#8211;verbose Print number of discarded bytes</p>
<dt><code>ftpget</code></dt>
<dd> ftpget [OPTIONS] HOST [LOCAL_FILE] REMOTE_FILE </dd>
<p> Download a file via FTP </p>
<pre>
        -c      Continue previous transfer
        -v      Verbose
        -u USER Username
        -p PASS Password
        -P NUM  Port
</pre>
<dt><code>ftpput</code></dt>
<dd> ftpput [OPTIONS] HOST [REMOTE_FILE] LOCAL_FILE </dd>
<p> Upload a file to a FTP server </p>
<pre>
        -v      Verbose
        -u USER Username
        -p PASS Password
        -P NUM  Port number
</pre>
<dt><code>getopt</code></dt>
<dd> getopt [OPTIONS] [&#8211;] OPTSTRING PARAMS </dd>
<pre>
        -a              Allow long options starting with single -
        -l LOPT[,...]   Long options to recognize
        -n PROGNAME     The name under which errors are reported
        -o OPTSTRING    Short options to recognize
        -q              No error messages on unrecognized options
        -Q              No normal output
        -s SHELL        Set shell quoting conventions
        -T              Version test (exits with 4)
        -u              Don't quote output
</pre>
<p> Example: </p>
<p> O=`getopt -l bb: &#8212; ab:c:: &#8220;$@&#8221;` || exit 1 eval set &#8212; &#8220;$O&#8221; while true; do <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>case &#8220;$1&#8221; in<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-a)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo A; shift;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-b|&#8211;bb) echo &#8220;B:&#8217;$2&#8221;&#8217;; shift 2;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-c)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>case &#8220;$2&#8221; in<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&quot;&#8220;)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo C; shift 2;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>*)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo &#8221;C:&#8217;$2&#8217;&quot;; shift 2;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>esac;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&#8211;)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>shift; break;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>*)<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo Error; exit 1;;<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>esac<br/>
 done</p>
<dt><code>getty</code></dt>
<dd> getty [OPTIONS] BAUD_RATE[,BAUD_RATE]&#8230; TTY [TERMTYPE] </dd>
<p> Open TTY, prompt for login name, then invoke /bin/login </p>
<p>        -h              Enable hardware RTS/CTS flow control<br/>
        -L              Set CLOCAL (ignore Carrier Detect state)<br/>
        -m              Get baud rate from modem&#8217;s CONNECT status message<br/>
        -n              Don&#8217;t prompt for login name<br/>
        -w              Wait for CR or LF before sending /etc/issue<br/>
        -i              Don&#8217;t display /etc/issue<br/>
        -f ISSUE_FILE   Display ISSUE_FILE instead of /etc/issue<br/>
        -l LOGIN        Invoke LOGIN instead of /bin/login<br/>
        -t SEC          Terminate after SEC if no login name is read<br/>
        -I INITSTR      Send INITSTR before anything else<br/>
        -H HOST         Log HOST into the utmp file as the hostname</p>
<p> BAUD_RATE of 0 leaves it unchanged</p>
<dt><code>grep</code></dt>
<dd> grep [-HhnlLoqvsriwFEz] [-m N] [-A/B/C N] PATTERN/-e PATTERN.../-f FILE [FILE]&#8230; </dd>
<p> Search for PATTERN in FILEs (or stdin) </p>
<pre>
        -H      Add 'filename:' prefix
        -h      Do not add 'filename:' prefix
        -n      Add 'line_no:' prefix
        -l      Show only names of files that match
        -L      Show only names of files that don't match
        -c      Show only count of matching lines
        -o      Show only the matching part of line
        -q      Quiet. Return 0 if PATTERN is found, 1 otherwise
        -v      Select non-matching lines
        -s      Suppress open and read errors
        -r      Recurse
        -i      Ignore case
        -w      Match whole words only
        -x      Match whole lines only
        -F      PATTERN is a literal (not regexp)
        -E      PATTERN is an extended regexp
        -z      Input is NUL terminated
        -m N    Match up to N times per file
        -A N    Print N lines of trailing context
        -B N    Print N lines of leading context
        -C N    Same as '-A N -B N'
        -e PTRN Pattern to match
        -f FILE Read pattern from file
</pre>
<dt><code>groups</code></dt>
<dd> groups [USER] </dd>
<p> Print the group memberships of USER or for the current process</p>
<dt><code>gunzip</code></dt>
<dd> gunzip [-cfkt] [FILE]&#8230; </dd>
<p> Decompress FILEs (or stdin) </p>
<pre>
        -c      Write to stdout
        -f      Force
        -k      Keep input files
        -t      Test file integrity
</pre>
<dt><code>gzip</code></dt>
<dd> gzip [-cfkdt] [FILE]&#8230; </dd>
<p> Compress FILEs (or stdin) </p>
<pre>
        -d      Decompress
        -t      Test file integrity
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>halt</code></dt>
<dd> halt [-d DELAY] [-n] [-f] [-w] </dd>
<p> Halt the system </p>
<pre>
        -d SEC  Delay interval
        -n      Do not sync
        -f      Force (don't go through init)
        -w      Only write a wtmp record
</pre>
<dt><code>head</code></dt>
<dd> head [OPTIONS] [FILE]&#8230; </dd>
<p> Print first 10 lines of each FILE (or stdin) to stdout. With more than one FILE, precede each with a filename header. </p>
<p>&#8211; n N[kbm] Print first N lines &#8211; n &#8211; N[kbm] Print all except N last lines &#8211; c[-] N[kbm] Print first N bytes &#8211; q Never print headers &#8211; v Always print headers</p>
<p> N may be suffixed by k (x1024), b (x512), or m (x1024^2).</p>
<dt><code>hexdump</code></dt>
<dd> hexdump [-bcCdefnosvx] [FILE]&#8230; </dd>
<p> Display FILEs (or stdin) in a user specified format </p>
<pre>
        -b              1-byte octal display
        -c              1-byte character display
        -d              2-byte decimal display
        -o              2-byte octal display
        -x              2-byte hex display
        -C              hex+ASCII 16 bytes per line
        -v              Show all (no dup folding)
        -e FORMAT_STR   Example: '16/1 &quot;%02x|&quot;&quot;
&quot;'
        -f FORMAT_FILE
        -n LENGTH       Show only first LENGTH bytes
        -s OFFSET       Skip OFFSET bytes
</pre>
<dt><code>hostid</code></dt>
<dd> hostid </dd>
<p> Print out a unique 32-bit identifier for the machine</p>
<dt><code>hostname</code></dt>
<dd> hostname [OPTIONS] [HOSTNAME | -F FILE] </dd>
<p> Get or set hostname or DNS domain name </p>
<pre>
        -s      Short
        -i      Addresses for the hostname
        -d      DNS domain name
        -f      Fully qualified domain name
        -F FILE Use FILE's content as hostname
</pre>
<dt><code>httpd</code></dt>
<dd> httpd [-ifv[v]] [-c CONFFILE] [-p [IP:]PORT] [-u USER[:GRP]] [-r REALM] [-h HOME] or httpd -d/-e/-m STRING </dd>
<p> Listen for incoming HTTP requests </p>
<p>        -i              Inetd mode<br/>
        -f              Don&#8217;t daemonize<br/>
        -v[v]           Verbose<br/>
        -p [IP:]PORT    Bind to IP:PORT (default *:80)<br/>
        -u USER[:GRP]   Set uid/gid after binding to port<br/>
        -r REALM        Authentication Realm for Basic Authentication<br/>
        -h HOME         Home directory (default .)<br/>
        -c FILE         Configuration file (default {/etc,HOME}/httpd.conf)<br/>
        -m STRING       MD5 crypt STRING<br/>
        -e STRING       HTML encode STRING<br/>
        -d STRING       URL decode STRING</p>
<dt><code>hwclock</code></dt>
<dd> hwclock [-r|&#8211;show] [-s|&#8211;hctosys] [-w|&#8211;systohc] [&#8211;systz] [&#8211;localtime] [-u|&#8211;utc] [-f|&#8211;rtc FILE] </dd>
<p> Query and set hardware clock (RTC) </p>
<pre>
        -r      Show hardware clock time
        -s      Set system time from hardware clock
        -w      Set hardware clock from system time
        --systz Set in-kernel timezone, correct system time
                if hardware clock is in local time
        -u      Assume hardware clock is kept in UTC
        --localtime     Assume hardware clock is kept in local time
        -f FILE Use specified device (e.g. /dev/rtc2)
</pre>
<dt><code>i2cdetect</code></dt>
<dd> i2cdetect -l | -F I2CBUS | [-ya] [-q|-r] I2CBUS [FIRST LAST] </dd>
<p> Detect I2C chips </p>
<pre>
        -l      List installed buses
        -F BUS# List functionalities on this bus
        -y      Disable interactive mode
        -a      Force scanning of non-regular addresses
        -q      Use smbus quick write commands for probing (default)
        -r      Use smbus read byte commands for probing
        FIRST and LAST limit probing range
</pre>
<dt><code>i2cdump</code></dt>
<dd> i2cdump [-fy] [-r FIRST-LAST] BUS ADDR [MODE] </dd>
<p> Examine I2C registers </p>
<pre>
        I2CBUS  I2C bus number
        ADDRESS 0x03-0x77
MODE is:
        b       Byte (default)
        w       Word
        W       Word on even register addresses
        i       I2C block
        s       SMBus block
        c       Consecutive byte
        Append p for SMBus PEC
        -f      Force access
        -y      Disable interactive mode
        -r      Limit the number of registers being accessed
</pre>
<dt><code>i2cget</code></dt>
<dd> i2cget [-fy] BUS CHIP-ADDRESS [DATA-ADDRESS [MODE]] </dd>
<p> Read from I2C/SMBus chip registers </p>
<pre>
        I2CBUS  I2C bus number
        ADDRESS 0x03-0x77
MODE is:
        b       Read byte data (default)
        w       Read word data
        c       Write byte/read byte
        Append p for SMBus PEC
        -f      Force access
        -y      Disable interactive mode
</pre>
<dt><code>i2cset</code></dt>
<dd> i2cset [-fy] [-m MASK] BUS CHIP-ADDRESS DATA-ADDRESS [VALUE] &#8230; [MODE] </dd>
<p> Set I2C registers </p>
<pre>
        I2CBUS  I2C bus number
        ADDRESS 0x03-0x77
MODE is:
        c       Byte, no value
        b       Byte data (default)
        w       Word data
        i       I2C block data
        s       SMBus block data
        Append p for SMBus PEC
        -f      Force access
        -y      Disable interactive mode
        -r      Read back and compare the result
        -m MASK Mask specifying which bits to write
</pre>
<dt><code>id</code></dt>
<dd> id [OPTIONS] [USER] </dd>
<p> Print information about USER or the current user </p>
<pre>
        -u      User ID
        -g      Group ID
        -G      Supplementary group IDs
        -n      Print names instead of numbers
        -r      Print real ID instead of effective ID
</pre>
<dt><code>ifconfig</code></dt>
<dd> ifconfig [-a] interface [address] </dd>
<p> Configure a network interface </p>
<p>[add ADDRESS[/ PREFIXLEN]]<br/>
    [del ADDRESS[/ PREFIXLEN]]<br/>
    [[-] broadcast[ADDRESS]][[-] pointopoint[ADDRESS]]<br/>
    [netmask ADDRESS][dstaddr ADDRESS]<br/>
    [outfill NN][keepalive NN]<br/>
    [hw ether | infiniband ADDRESS][metric NN][mtu NN]<br/>
    [[-] trailers][[-] arp][[-] allmulti]<br/>
    [multicast][[-] promisc][txqueuelen NN][[-] dynamic]<br/>
    [mem_start NN][io_addr NN][irq NN]<br/>
    [up | down]&#8230;</p>
<dt><code>ifdown</code></dt>
<dd> ifdown [-anmvf] [-i FILE] IFACE&#8230; </dd>
<pre>
        -a      Deconfigure all interfaces
        -i FILE Use FILE for interface definitions
        -n      Print out what would happen, but don't do it
                (note: doesn't disable mappings)
        -m      Don't run any mappings
        -v      Print out what would happen before doing it
        -f      Force deconfiguration
</pre>
<dt><code>ifup</code></dt>
<dd> ifup [-anmvf] [-i FILE] IFACE&#8230; </dd>
<pre>
        -a      Configure all interfaces
        -i FILE Use FILE instead of /etc/network/interfaces
        -n      Print out what would happen, but don't do it
                (note: doesn't disable mappings)
        -m      Don't run any mappings
        -v      Print out what would happen before doing it
        -f      Force configuration
</pre>
<dt><code>init</code></dt>
<dd> init </dd>
<p> Init is the first process started during boot. It never exits. It (re)spawns children according to /etc/inittab.</p>
<dt><code>insmod</code></dt>
<dd> insmod FILE [SYMBOL=VALUE]&#8230; </dd>
<p> Load kernel module</p>
<dt><code>ionice</code></dt>
<dd> ionice [-c 1-3] [-n 0-7] [-p PID] [PROG] </dd>
<p> Change I/O priority and class </p>
<pre>
        -c      Class. 1:realtime 2:best-effort 3:idle
        -n      Priority
</pre>
<dt><code>ip</code></dt>
<dd> ip [OPTIONS] address|route|link|tunnel|neigh|rule [ARGS] </dd>
<p> OPTIONS := -f[amily] inet|inet6|link | -o[neline] </p>
<p> ip addr add|del IFADDR dev IFACE | show|flush [dev IFACE] [to PREFIX] ip route list|flush|add|del|change|append|replace|test ROUTE ip link set IFACE [up|down] [arp on|off] [multicast on|off] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[promisc on|off] [mtu NUM] [name NAME] [qlen NUM] [address MAC]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[master IFACE | nomaster]<br/>
 ip tunnel add|change|del|show [NAME] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[mode ipip|gre|sit] [remote ADDR] [local ADDR] [ttl TTL]<br/>
 ip neigh show|flush [to PREFIX] [dev DEV] [nud STATE] ip rule [list] | add|del SELECTOR ACTION</p>
<dt><code>ipcalc</code></dt>
<dd> ipcalc [OPTIONS] ADDRESS[/PREFIX] [NETMASK] </dd>
<p> Calculate and display network settings from IP address </p>
<pre>
        -b      Broadcast address
        -n      Network address
        -m      Default netmask for IP
        -p      Prefix for IP/NETMASK
        -h      Resolved host name
        -s      No error messages
</pre>
<dt><code>ipneigh</code></dt>
<dd> ipneigh show|flush [to PREFIX] [dev DEV] [nud STATE]</dd>
<dt><code>kill</code></dt>
<dd> kill [-l] [-SIG] PID&#8230; </dd>
<p> Send a signal (default: TERM) to given PIDs </p>
<pre>
        -l      List all signal names and numbers
</pre>
<dt><code>killall</code></dt>
<dd> killall [-l] [-q] [-SIG] PROCESS_NAME&#8230; </dd>
<p> Send a signal (default: TERM) to given processes </p>
<pre>
        -l      List all signal names and numbers
        -q      Don't complain if no processes were killed
</pre>
<dt><code>klogd</code></dt>
<dd> klogd [-c N] [-n] </dd>
<p> Log kernel messages to syslog </p>
<pre>
        -c N    Print to console messages more urgent than prio N (1-8)
        -n      Run in foreground
</pre>
<dt><code>last</code></dt>
<dd> last </dd>
<p> Show listing of the last users that logged into the system</p>
<dt><code>less</code></dt>
<dd> less [-EFIMmNSRh~] [FILE]&#8230; </dd>
<p> View FILE (or stdin) one screenful at a time </p>
<pre>
        -E      Quit once the end of a file is reached
        -F      Quit if entire file fits on first screen
        -I      Ignore case in all searches
        -M,-m   Display status line with line numbers
                and percentage through the file
        -N      Prefix line number to each line
        -S      Truncate long lines
        -R      Remove color escape codes in input
        -~      Suppress ~s displayed past EOF
</pre>
<dt><code>link</code></dt>
<dd> link FILE LINK </dd>
<p> Create hard LINK to FILE</p>
<dt><code>ln</code></dt>
<dd> ln [OPTIONS] TARGET&#8230; LINK|DIR </dd>
<p> Create a link LINK or DIR/TARGET to the specified TARGET(s) </p>
<pre>
        -s      Make symlinks instead of hardlinks
        -f      Remove existing destinations
        -n      Don't dereference symlinks - treat like normal file
        -b      Make a backup of the target (if exists) before link operation
        -S suf  Use suffix instead of ~ when making backup files
        -T      2nd arg must be a DIR
        -v      Verbose
</pre>
<dt><code>loadfont</code></dt>
<dd> loadfont &lt; font </dd>
<p> Load a console font from stdin</p>
<dt><code>loadkmap</code></dt>
<dd> loadkmap &lt; keymap </dd>
<p> Load a binary keyboard translation table from stdin</p>
<dt><code>logger</code></dt>
<dd> logger [OPTIONS] [MESSAGE] </dd>
<p> Write MESSAGE (or stdin) to syslog </p>
<pre>
        -s      Log to stderr as well as the system log
        -t TAG  Log using the specified tag (defaults to user name)
        -p PRIO Priority (numeric or facility.level pair)
</pre>
<dt><code>login</code></dt>
<dd> login [-p] [-h HOST] [[-f] USER] </dd>
<p> Begin a new session on the system </p>
<pre>
        -f      Don't authenticate (user already authenticated)
        -h HOST Host user came from (for network logins)
        -p      Preserve environment
</pre>
<dt><code>logname</code></dt>
<dd> logname </dd>
<p> Print the name of the current user</p>
<dt><code>logread</code></dt>
<dd> logread [-fF] </dd>
<p> Show messages in syslogd&#8217;s circular buffer </p>
<pre>
        -f      Output data as log grows
        -F      Same as -f, but dump buffer first
</pre>
<dt><code>losetup</code></dt>
<dd> losetup [-r] [-o OFS] {-f|LOOPDEV} FILE &#8211; associate loop devices <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>losetup -d LOOPDEV &#8211; disassociate<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>losetup -a &#8211; show status<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>losetup -f &#8211; show next free loop device</dd>
<pre>
        -o OFS  Start OFS bytes into FILE
        -r      Read-only
        -f      Show/use next free loop device
</pre>
<dt><code>ls</code></dt>
<dd> ls [-1AaCxdLHRFplinshrSXvctu] [-w WIDTH] [FILE]&#8230; </dd>
<p> List directory contents </p>
<p>&#8211; 1 One column output &#8211; a Include entries which start with.- A Like &#8211; a, but exclude.and..- x List by lines &#8211; d List directory entries instead of contents &#8211; L Follow symlinks &#8211; H Follow symlinks on command line &#8211; R Recurse &#8211; p Append / to dir entries &#8211; F Append indicator(one of * /= @ |)to entries<br/>
                                                                             &#8211; l Long listing format<br/>
                                                                             &#8211; i List inode numbers<br/>
                                                                             &#8211; n List numeric UIDs and GIDs instead of names<br/>
                                                                             &#8211; s List allocated blocks<br/>
                                                                             &#8211; lc List ctime<br/>
                                                                             &#8211; lu List atime&#8211; full &#8211; time List full date and time<br/>
                                                                             &#8211; h Human readable sizes(1K 243M 2G)&#8211; group &#8211; directories &#8211; first<br/>
                                                                             &#8211; S Sort by size<br/>
                                                                             &#8211; X Sort by extension<br/>
                                                                             &#8211; v Sort by version<br/>
                                                                             &#8211; t Sort by mtime<br/>
                                                                             &#8211; tc Sort by ctime<br/>
                                                                             &#8211; tu Sort by atime<br/>
                                                                             &#8211; r Reverse sort order<br/>
                                                                             &#8211; w N Format N columns wide&#8211; color[= {always, never, auto}] Control coloring</p>
<dt><code>lsmod</code></dt>
<dd> lsmod </dd>
<p> List loaded kernel modules</p>
<dt><code>lzcat</code></dt>
<dd> lzcat [FILE]&#8230; </dd>
<p> Decompress to stdout</p>
<dt><code>lzma</code></dt>
<dd> lzma -d [-cfk] [FILE]&#8230; </dd>
<p> Decompress FILE (or stdin) </p>
<pre>
        -d      Decompress
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>lzop</code></dt>
<dd> lzop [-cfUvd123456789CF] [FILE]&#8230; </dd>
<pre>
        -1..9   Compression level
        -d      Decompress
        -c      Write to stdout
        -f      Force
        -U      Delete input files
        -v      Verbose
        -F      Don't store or verify checksum
        -C      Also write checksum of compressed block
</pre>
<dt><code>md5sum</code></dt>
<dd> md5sum [-c[sw]] [FILE]&#8230; </dd>
<p> Print or check MD5 checksums </p>
<pre>
        -c      Check sums against list in FILEs
        -s      Don't output anything, status code shows success
        -w      Warn about improperly formatted checksum lines
</pre>
<dt><code>mdev</code></dt>
<dd> mdev [-s] </dd>
<p> mdev -s is to be run during boot to scan /sys and populate /dev. </p>
<p> Bare mdev is a kernel hotplug helper. To activate it: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>echo /sbin/mdev &gt;/proc/sys/kernel/hotplug</p>
<p> It uses /etc/mdev.conf with lines <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-][ENV=regex;]&#8230;DEVNAME UID:GID PERM [&gt;|=PATH]|[!] [@|$|*PROG]<br/>
 where DEVNAME is device name regex, <tt>@major</tt>,minor[-minor2], or environment variable regex. A common use of the latter is to load modules for hotplugged devices: </p>
<pre>
        $MODALIAS=.* 0:0 660 @modprobe &quot;$MODALIAS&quot;
</pre>
<p> If /dev/mdev.seq file exists, mdev will wait for its value to match <tt>$SEQNUM</tt> variable. This prevents plug/unplug races. To activate this feature, create empty /dev/mdev.seq at boot. </p>
<p> If /dev/mdev.log file exists, debug log will be appended to it.</p>
<dt><code>microcom</code></dt>
<dd> microcom [-d DELAY] [-t TIMEOUT] [-s SPEED] [-X] TTY </dd>
<p> Copy bytes for stdin to TTY and from TTY to stdout </p>
<pre>
        -d      Wait up to DELAY ms for TTY output before sending every
                next byte to it
        -t      Exit if both stdin and TTY are silent for TIMEOUT ms
        -s      Set serial line to SPEED
        -X      Disable special meaning of NUL and Ctrl-X from stdin
</pre>
<dt><code>mkdir</code></dt>
<dd> mkdir [OPTIONS] DIRECTORY&#8230; </dd>
<p> Create DIRECTORY </p>
<pre>
        -m MODE Mode
        -p      No error if exists; make parent directories as needed
</pre>
<dt><code>mkdosfs</code></dt>
<dd> mkdosfs [-v] [-n LABEL] BLOCKDEV [KBYTES] </dd>
<p> Make a FAT32 filesystem </p>
<pre>
        -v      Verbose
        -n LBL  Volume label
</pre>
<dt><code>mke2fs</code></dt>
<dd> mke2fs [-Fn] [-b BLK_SIZE] [-i INODE_RATIO] [-I INODE_SIZE] [-m RESERVED_PERCENT] [-L LABEL] BLOCKDEV [KBYTES] </dd>
<pre>
        -b BLK_SIZE     Block size, bytes
        -F              Force
        -i RATIO        Max number of files is filesystem_size / RATIO
        -I BYTES        Inode size (min 128)
        -L LBL          Volume label
        -m PERCENT      Percent of blocks to reserve for admin
        -n              Dry run
</pre>
<dt><code>mkfifo</code></dt>
<dd> mkfifo [-m MODE] NAME </dd>
<p> Create named pipe </p>
<pre>
        -m MODE Mode (default a=rw)
</pre>
<dt><code>mknod</code></dt>
<dd> mknod [-m MODE] NAME TYPE [MAJOR MINOR] </dd>
<p> Create a special file (block, character, or pipe) </p>
<pre>
        -m MODE Creation mode (default a=rw)
TYPE:
        b       Block device
        c or u  Character device
        p       Named pipe (MAJOR MINOR must be omitted)
</pre>
<dt><code>mkpasswd</code></dt>
<dd> mkpasswd [OPTIONS] [PASSWORD] [SALT] </dd>
<p> Print <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) hashed PASSWORD </p>
<pre>
        -P,--password-fd N      Read password from fd N
        -m,--method TYPE        des,md5,sha256/512 (default sha256)
        -S,--salt SALT
</pre>
<dt><code>mkswap</code></dt>
<dd> mkswap [-L LBL] BLOCKDEV [KBYTES] </dd>
<p> Prepare BLOCKDEV to be used as swap partition </p>
<pre>
        -L LBL  Label
</pre>
<dt><code>mktemp</code></dt>
<dd> mktemp [-dt] [-p DIR] [TEMPLATE] </dd>
<p> Create a temporary file with name based on TEMPLATE and print its name. TEMPLATE must end with XXXXXX (e.g. [/dir/]nameXXXXXX). Without TEMPLATE, -t tmp.XXXXXX is assumed. </p>
<pre>
        -d      Make directory, not file
        -q      Fail silently on errors
        -t      Prepend base directory name to TEMPLATE
        -p DIR  Use DIR as a base directory (implies -t)
        -u      Do not create anything; print a name
</pre>
<p> Base directory is: -p DIR, else <tt>$TMPDIR</tt>, else /tmp</p>
<dt><code>modinfo</code></dt>
<dd> modinfo [-adlpn0] [-F keyword] MODULE </dd>
<p>        -a              Shortcut for &#8216;-F author&#8217;<br/>
        -d              Shortcut for &#8216;-F description&#8217;<br/>
        -l              Shortcut for &#8216;-F license&#8217;<br/>
        -p              Shortcut for &#8216;-F parm&#8217;<br/>
        -F keyword      Keyword to look for<br/>
        -0              Separate output with NULs</p>
<dt><code>modprobe</code></dt>
<dd> modprobe [-alrqvsDb] MODULE [SYMBOL=VALUE]&#8230; </dd>
<pre>
        -a      Load multiple MODULEs
        -l      List (MODULE is a pattern)
        -r      Remove MODULE (stacks) or do autoclean
        -q      Quiet
        -v      Verbose
        -s      Log to syslog
        -D      Show dependencies
        -b      Apply blacklist to module names too
</pre>
<dt><code>more</code></dt>
<dd> more [FILE]&#8230; </dd>
<p> View FILE (or stdin) one screenful at a time</p>
<dt><code>mount</code></dt>
<dd> mount [OPTIONS] [-o OPT] DEVICE NODE </dd>
<p> Mount a filesystem. Filesystem autodetection requires /proc. </p>
<p>&#8211; a Mount all filesystems in fstab &#8211; f Dry run &#8211; i Don&#8217;t run mount helper &#8211; r Read &#8211; only mount &#8211; t FSTYPE[, &#8230;] Filesystem type(s) &#8211; T FILE Read FILE instead of / etc / fstab<br/>
    &#8211; O OPT Mount only filesystems with option OPT(-a only) &#8211; o OPT:<br/>
    loop Ignored(loop devices are autodetected)<br/>
                    [a] sync Writes are[a] synchronous<br/>
                        [no] atime Disable<br/>
                / enable updates to inode access times[no] diratime Disable / enable atime updates to directories[no] relatime Disable / enable atime updates relative to modification time[no] dev(Dis)allow use of special device files[no] exec(Dis)allow use of executable files[no] suid(Dis)allow set<br/>
            &#8211; user &#8211; id &#8211; root programs[r] shared Convert[recursively] to a shared subtree[r] slave Convert[recursively] to a slave subtree[r] private Convert[recursively] to a private subtree[un] bindable Make mount point[un] able to be bind mounted[r] bind Bind a file<br/>
        or directory[recursively] to another location<br/>
        move Relocate an existing mount point<br/>
        remount Remount a mounted filesystem,<br/>
    changing flags<br/>
        ro Same as<br/>
        &#8211; r</p>
<p> There are filesystem-specific -o flags.</p>
<dt><code>mt</code></dt>
<dd> mt [-f device] opcode value </dd>
<p> Control magnetic tape drive operation </p>
<p> Available Opcodes: </p>
<p> bsf bsfm bsr bss datacompression drvbuffer eof eom erase fsf fsfm fsr fss load lock mkpart nop offline ras1 ras2 ras3 reset retension rewind rewoffline seek setblk setdensity setpart tell unload unlock weof wset</p>
<dt><code>mv</code></dt>
<dd> mv [-fin] SOURCE DEST or: mv [-fin] SOURCE&#8230; DIRECTORY </dd>
<p> Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY </p>
<pre>
        -f      Don't prompt before overwriting
        -i      Interactive, prompt before overwrite
        -n      Don't overwrite an existing file
</pre>
<dt><code>nameif</code></dt>
<dd> nameif [-s] [-c FILE] [IFNAME HWADDR]&#8230; </dd>
<p> Rename network interface while it in the down state. The device with address HWADDR is renamed to IFACE. </p>
<pre>
        -c FILE Configuration file (default: /etc/mactab)
        -s      Log to syslog
</pre>
<dt><code>nc</code></dt>
<dd> nc [-iN] [-wN] [-l] [-p PORT] [-f FILE|IPADDR PORT] [-e PROG] </dd>
<p> Open a pipe to IP:PORT or FILE </p>
<pre>
        -l      Listen mode, for inbound connects
                (use -ll with -e for persistent server)
        -p PORT Local port
        -w SEC  Connect timeout
        -i SEC  Delay interval for lines sent
        -f FILE Use file (ala /dev/ttyS0) instead of network
        -e PROG Run PROG after connect
</pre>
<dt><code>netstat</code></dt>
<dd> netstat [-ral] [-tuwx] [-en] </dd>
<p> Display networking information </p>
<pre>
        -r      Routing table
        -a      All sockets
        -l      Listening sockets
                Else: connected sockets
        -t      TCP sockets
        -u      UDP sockets
        -w      Raw sockets
        -x      Unix sockets
                Else: all socket types
        -e      Other/more information
        -n      Don't resolve names
</pre>
<dt><code>nl</code></dt>
<dd> nl [OPTIONS] [FILE]&#8230; </dd>
<p> Write FILEs to standard output with line numbers added </p>
<pre>
        -b STYLE        Which lines to number - a: all, t: nonempty, n: none
        -i N            Line number increment
        -s STRING       Use STRING as line number separator
        -v N            Start from N
        -w N            Width of line numbers
</pre>
<dt><code>nologin</code></dt>
<dd> nologin </dd>
<p> Politely refuse a login</p>
<dt><code>nproc</code></dt>
<dd> nproc &#8211;all &#8211;ignore=N </dd>
<p> Print number of available CPUs </p>
<pre>
        --all           Number of installed CPUs
        --ignore=N      Exclude N CPUs
</pre>
<dt><code>nsenter</code></dt>
<dd> nsenter [OPTIONS] [PROG [ARGS]] </dd>
<p>&#8211; t PID Target process to get namespaces from &#8211; m[FILE] Enter mount namespace &#8211; u[FILE] Enter UTS namespace(hostname etc) &#8211; i[FILE] Enter System V IPC namespace &#8211; n[FILE] Enter network namespace &#8211; p[FILE] Enter pid namespace &#8211; U[FILE] Enter user namespace &#8211; S UID Set uid in entered namespace &#8211; G GID Set gid in entered namespace &#8211;preserve &#8211; credentials Don&#8217;t touch uids or gids &#8211; r[DIR] Set root directory<br/>
    &#8211; w[DIR] Set working directory<br/>
    &#8211; F Don &#8216;t fork before exec&#8217; ing PROG</p>
<dt><code>nslookup</code></dt>
<dd> nslookup [-type=QUERY_TYPE] [-debug] HOST [DNS_SERVER] </dd>
<p> Query DNS about HOST </p>
<p> QUERY_TYPE: soa,ns,a,aaaa,cname,mx,txt,ptr,any</p>
<dt><code>nuke</code></dt>
<dd> nuke DIR&#8230; </dd>
<p> Remove DIRs</p>
<dt><code>od</code></dt>
<dd> od [-abcdfhilovxs] [-t TYPE] [-A RADIX] [-N SIZE] [-j SKIP] [-S MINSTR] [-w WIDTH] [FILE]&#8230; </dd>
<p> Print FILEs (or stdin) unambiguously, as octal bytes by default</p>
<dt><code>openvt</code></dt>
<dd> openvt [-c N] [-sw] [PROG ARGS] </dd>
<p> Start PROG on a new virtual terminal </p>
<pre>
        -c N    Use specified VT
        -s      Switch to the VT
        -w      Wait for PROG to exit
</pre>
<dt><code>partprobe</code></dt>
<dd> partprobe DEVICE&#8230; </dd>
<p> Ask kernel to rescan partition table</p>
<dt><code>passwd</code></dt>
<dd> passwd [OPTIONS] [USER] </dd>
<p> Change USER&#8216;s password (default: current user) </p>
<pre>
        -a ALG  des,md5,sha256/512 (default sha256)
        -d      Set password to ''
        -l      Lock (disable) account
        -u      Unlock (enable) account
</pre>
<dt><code>paste</code></dt>
<dd> paste [OPTIONS] [FILE]&#8230; </dd>
<p> Paste lines from each input file, separated with tab </p>
<pre>
        -d LIST Use delimiters from LIST, not tab
        -s      Serial: one file at a time
</pre>
<dt><code>patch</code></dt>
<dd> patch [OPTIONS] [ORIGFILE [PATCHFILE]] </dd>
<pre>
        -p N    Strip N leading components from file names
        -i DIFF Read DIFF instead of stdin
        -R      Reverse patch
        -N      Ignore already applied patches
        -E      Remove output files if they become empty
        --dry-run       Don't actually change files
</pre>
<dt><code>pidof</code></dt>
<dd> pidof [NAME]&#8230; </dd>
<p> List PIDs of all processes with names that match NAMEs</p>
<dt><code>ping</code></dt>
<dd> ping [OPTIONS] HOST </dd>
<p> Send ICMP ECHO_REQUEST packets to network hosts </p>
<pre>
        -4,-6           Force IP or IPv6 name resolution
        -c CNT          Send only CNT pings
        -s SIZE         Send SIZE data bytes in packets (default 56)
        -i SECS         Interval
        -A              Ping as soon as reply is recevied
        -t TTL          Set TTL
        -I IFACE/IP     Source interface or IP address
        -W SEC          Seconds to wait for the first response (default 10)
                        (after all -c CNT packets are sent)
        -w SEC          Seconds until ping exits (default:infinite)
                        (can exit earlier with -c CNT)
        -q              Quiet, only display output at start
                        and when finished
        -p HEXBYTE      Pattern to use for payload
</pre>
<dt><code>ping6</code></dt>
<dd> ping6 [OPTIONS] HOST </dd>
<p> Send ICMP ECHO_REQUEST packets to network hosts </p>
<pre>
        -c CNT          Send only CNT pings
        -s SIZE         Send SIZE data bytes in packets (default 56)
        -i SECS         Interval
        -A              Ping as soon as reply is recevied
        -I IFACE/IP     Source interface or IP address
        -q              Quiet, only display output at start
                        and when finished
        -p HEXBYTE      Pattern to use for payload
</pre>
<dt><code>pivot_root</code></dt>
<dd> pivot_root NEW_ROOT PUT_OLD </dd>
<p> Move the current root file system to PUT_OLD and make NEW_ROOT the new root file system</p>
<dt><code>poweroff</code></dt>
<dd> poweroff [-d DELAY] [-n] [-f] </dd>
<p> Halt and shut off power </p>
<pre>
        -d SEC  Delay interval
        -n      Do not sync
        -f      Force (don't go through init)
</pre>
<dt><code>printf</code></dt>
<dd> printf FORMAT [ARG]&#8230; </dd>
<p> Format and print ARG(s) according to FORMAT (a-la C printf)</p>
<dt><code>ps</code></dt>
<dd> ps [-o COL1,COL2=HEADER] [-T] </dd>
<p> Show list of processes </p>
<pre>
        -o COL1,COL2=HEADER     Select columns for display
        -T                      Show threads
</pre>
<dt><code>pwd</code></dt>
<dd> pwd </dd>
<p> Print the full filename of the current working directory</p>
<dt><code>rdate</code></dt>
<dd> rdate [-s/-p] HOST </dd>
<p> Set and print time from HOST using RFC 868 </p>
<pre>
        -s      Only set system time
        -p      Only print time
</pre>
<dt><code>readlink</code></dt>
<dd> readlink [-fnv] FILE </dd>
<p> Display the value of a symlink </p>
<pre>
        -f      Canonicalize by following all symlinks
        -n      Don't add newline
        -v      Verbose
</pre>
<dt><code>realpath</code></dt>
<dd> realpath FILE&#8230; </dd>
<p> Return the absolute pathnames of given FILE</p>
<dt><code>reboot</code></dt>
<dd> reboot [-d DELAY] [-n] [-f] </dd>
<p> Reboot the system </p>
<pre>
        -d SEC  Delay interval
        -n      Do not sync
        -f      Force (don't go through init)
</pre>
<dt><code>renice</code></dt>
<dd> renice [-n] PRIORITY [[-p | -g | -u] ID&#8230;]&#8230; </dd>
<p> Change scheduling priority of a running process </p>
<pre>
        -n      Add PRIORITY to current nice value
                Without -n, nice value is set to PRIORITY
        -p      Process ids (default)
        -g      Process group ids
        -u      Process user names
</pre>
<dt><code>reset</code></dt>
<dd> reset </dd>
<p> Reset the screen</p>
<dt><code>resume</code></dt>
<dd> resume BLOCKDEV [OFFSET] </dd>
<p> Restore system state from &#8216;suspend-to-disk&#8217; data in BLOCKDEV</p>
<dt><code>rev</code></dt>
<dd> rev [FILE]&#8230; </dd>
<p> Reverse lines of FILE</p>
<dt><code>rm</code></dt>
<dd> rm [-irf] FILE&#8230; </dd>
<p> Remove (unlink) FILEs </p>
<pre>
        -i      Always prompt before removing
        -f      Never prompt
        -R,-r   Recurse
</pre>
<dt><code>rmdir</code></dt>
<dd> rmdir [OPTIONS] DIRECTORY&#8230; </dd>
<p> Remove DIRECTORY if it is empty </p>
<pre>
        -p      Include parents
        --ignore-fail-on-non-empty
</pre>
<dt><code>rmmod</code></dt>
<dd> rmmod [-wfa] [MODULE]&#8230; </dd>
<p> Unload kernel modules </p>
<pre>
        -w      Wait until the module is no longer used
        -f      Force unload
        -a      Remove all unused modules (recursively)
</pre>
<dt><code>route</code></dt>
<dd> route [{add|del|delete}] </dd>
<p> Edit kernel routing tables </p>
<pre>
        -n      Don't resolve names
        -e      Display other/more information
        -A inet{6}      Select address family
</pre>
<dt><code>rpm</code></dt>
<dd> rpm -i PACKAGE.rpm; rpm -qp[ildc] PACKAGE.rpm </dd>
<p> Manipulate RPM packages </p>
<p> Commands: </p>
<pre>
        -i      Install package
        -qp     Query package
        -qpi    Show information
        -qpl    List contents
        -qpd    List documents
        -qpc    List config files
</pre>
<dt><code>rpm2cpio</code></dt>
<dd> rpm2cpio PACKAGE.rpm </dd>
<p> Output a cpio archive of the rpm file</p>
<dt><code>run-init</code></dt>
<dd> run-init [-d CAP,CAP&#8230;] [-n] [-c CONSOLE_DEV] NEW_ROOT NEW_INIT [ARGS] </dd>
<p> Free initramfs and switch to another root fs: </p>
<p> chroot to NEW_ROOT, delete all in /, move NEW_ROOT to /, execute NEW_INIT. PID must be 1. NEW_ROOT must be a mountpoint. </p>
<pre>
        -c DEV  Reopen stdio to DEV after switch
        -d CAPS Drop capabilities
        -n      Dry run
</pre>
<dt><code>run-parts</code></dt>
<dd> run-parts [-a ARG]&#8230; [-u UMASK] [&#8211;reverse] [&#8211;test] [&#8211;exit-on-error] DIRECTORY </dd>
<p> Run a bunch of scripts in DIRECTORY </p>
<p>&#8211; a ARG Pass ARG as argument to scripts &#8211; u UMASK Set UMASK before running scripts&#8211; reverse Reverse execution order&#8211; test Dry run&#8211; exit &#8211; on &#8211; error Exit if a script exits with non &#8211; zero</p>
<dt><code>sed</code></dt>
<dd> sed [-i[SFX]] [-nrE] [-f FILE]&#8230; [-e CMD]&#8230; [FILE]&#8230; or: sed [-i[SFX]] [-nrE] CMD [FILE]&#8230; </dd>
<pre>
        -e CMD  Add CMD to sed commands to be executed
        -f FILE Add FILE contents to sed commands to be executed
        -i[SFX] Edit files in-place (otherwise sends to stdout)
                Optionally back files up, appending SFX
        -n      Suppress automatic printing of pattern space
        -r,-E   Use extended regex syntax
</pre>
<p> If no -e or -f, the first non-option argument is the sed command string. Remaining arguments are input files (stdin if none).</p>
<dt><code>seq</code></dt>
<dd> seq [-w] [-s SEP] [FIRST [INC]] LAST </dd>
<p> Print numbers from FIRST to LAST, in steps of INC. FIRST, INC default to 1. </p>
<pre>
        -w      Pad to last with leading zeros
        -s SEP  String separator
</pre>
<dt><code>setkeycodes</code></dt>
<dd> setkeycodes { SCANCODE KEYCODE }&#8230; </dd>
<p> Modify kernel&#8217;s scancode-to-keycode map, allowing unusual keyboards to generate usable keycodes. </p>
<p> SCANCODE is either xx or e0xx (hexadecimal), KEYCODE is decimal.</p>
<dt><code>setpriv</code></dt>
<dd> setpriv [OPTIONS] PROG [ARGS] </dd>
<p> Run PROG with different privilege settings </p>
<p> -d,&#8211;dump<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show current capabilities<br/>
 &#8211;nnp,&#8211;no-new-privs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Ignore setuid/setgid bits and file capabilities<br/>
 &#8211;inh-caps CAP,CAP<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Set inheritable capabilities<br/>
 &#8211;ambient-caps CAP,CAP<tt>&nbsp;<wbr>&nbsp;</tt>Set ambient capabilities</p>
<dt><code>setsid</code></dt>
<dd> setsid [-c] PROG ARGS </dd>
<p> Run PROG in a new session. PROG will have no controlling terminal and will not be affected by keyboard signals (^C etc). </p>
<pre>
        -c      Set controlling terminal to stdin
</pre>
<dt><code>sh</code></dt>
<dd> sh [-/+OPTIONS] [-/+o OPT]&#8230; [-c &#8216;SCRIPT&#8216; [ARG0 [ARGS]] / FILE [ARGS] / -s [ARGS]] </dd>
<p> Unix shell interpreter</p>
<dt><code>sha1sum</code></dt>
<dd> sha1sum [-c[sw]] [FILE]&#8230; </dd>
<p> Print or check SHA1 checksums </p>
<pre>
        -c      Check sums against list in FILEs
        -s      Don't output anything, status code shows success
        -w      Warn about improperly formatted checksum lines
</pre>
<dt><code>sha256sum</code></dt>
<dd> sha256sum [-c[sw]] [FILE]&#8230; </dd>
<p> Print or check SHA256 checksums </p>
<pre>
        -c      Check sums against list in FILEs
        -s      Don't output anything, status code shows success
        -w      Warn about improperly formatted checksum lines
</pre>
<dt><code>sha512sum</code></dt>
<dd> sha512sum [-c[sw]] [FILE]&#8230; </dd>
<p> Print or check SHA512 checksums </p>
<pre>
        -c      Check sums against list in FILEs
        -s      Don't output anything, status code shows success
        -w      Warn about improperly formatted checksum lines
</pre>
<dt><code>shred</code></dt>
<dd> shred FILE&#8230; </dd>
<p> Overwrite/delete FILEs </p>
<pre>
        -f      Chmod to ensure writability
        -n N    Overwrite N times (default 3)
        -z      Final overwrite with zeros
        -u      Remove file
</pre>
<dt><code>shuf</code></dt>
<dd> shuf [-e|-i L-H] [-n NUM] [-o FILE] [-z] [FILE|ARG&#8230;] </dd>
<p> Randomly permute lines </p>
<pre>
        -e      Treat ARGs as lines
        -i L-H  Treat numbers L-H as lines
        -n NUM  Output at most NUM lines
        -o FILE Write to FILE, not standard output
        -z      End lines with zero byte, not newline
</pre>
<dt><code>sleep</code></dt>
<dd> sleep [N]&#8230; </dd>
<p> Pause for a time equal to the total of the args given, where each arg can have an optional suffix of (s)econds, (m)inutes, (h)ours, or (d)ays</p>
<dt><code>sort</code></dt>
<dd> sort [-nrugMcszbdfiokt] [-o FILE] [-k start[.offset][opts][,end[.offset][opts]] [-t CHAR] [FILE]&#8230; </dd>
<p> Sort lines of text </p>
<pre>
        -o FILE Output to FILE
        -c      Check whether input is sorted
        -b      Ignore leading blanks
        -f      Ignore case
        -i      Ignore unprintable characters
        -d      Dictionary order (blank or alphanumeric only)
        -n      Sort numbers
        -g      General numerical sort
        -M      Sort month
        -V      Sort version
        -t CHAR Field separator
        -k N[,M] Sort by Nth field
        -r      Reverse sort order
        -s      Stable (don't sort ties alphabetically)
        -u      Suppress duplicate lines
        -z      Lines are terminated by NUL, not newline
</pre>
<dt><code>ssl_client</code></dt>
<dd> ssl_client [-e] -s FD [-r FD] [-n SNI]</dd>
<dt><code>start-stop-daemon</code></dt>
<dd> start-stop-daemon [OPTIONS] [-S|-K] &#8230; [&#8211; ARGS&#8230;] </dd>
<p> Search for matching processes, and then -K: stop all matching processes -S: start a process unless a matching process is found </p>
<p> Process matching: </p>
<p>&#8211; u USERNAME | UID Match only this user&#8217;s processes &#8211; n NAME Match processes with NAME in comm field in / proc / PID / stat &#8211; x EXECUTABLE Match processes with this command command in / proc / PID / cmdline &#8211; p FILE Match a process with PID from FILE All specified conditions must match &#8211; S only:<br/>
                                                                                                                                                                                                                                                                                                       -x EXECUTABLE Program to run &#8211; a NAME Zeroth argument &#8211; b Background &#8211; N N Change nice level &#8211; c USER<br/>
                                                                                                                                                                                                                                                                                                      [:[GRP]<br/>
] Change user / group &#8211; m Write PID to pidfile specified by &#8211; p &#8211; K<br/>
                                                                                                                                                                                                                                                                                                   only:<br/>
                                                                                                                                                                                                                                                                                                       -s SIG Signal to send &#8211; t Match only, exit with 0 if found<br/>
                                                                                                                                                                                                                                                                                                  Other:<br/>
                                                                                                                                                                                                                                                                                                      -o Exit with status 0 if nothing is done &#8211; v Verbose &#8211; q Quiet</p>
<dt><code>stat</code></dt>
<dd> stat [OPTIONS] FILE&#8230; </dd>
<p> Display file (default) or filesystem status </p>
<pre>
        -c FMT  Use the specified format
        -f      Display filesystem status
        -L      Follow links
        -t      Terse display
</pre>
<p> FMT sequences for files: </p>
<pre>
 %a     Access rights in octal
 %A     Access rights in human readable form
 %b     Number of blocks allocated (see %B)
 %B     Size in bytes of each block reported by %b
 %d     Device number in decimal
 %D     Device number in hex
 %f     Raw mode in hex
 %F     File type
 %g     Group ID
 %G     Group name
 %h     Number of hard links
 %i     Inode number
 %n     File name
 %N     File name, with -&gt; TARGET if symlink
 %o     I/O block size
 %s     Total size in bytes
 %t     Major device type in hex
 %T     Minor device type in hex
 %u     User ID
 %U     User name
 %x     Time of last access
 %X     Time of last access as seconds since Epoch
 %y     Time of last modification
 %Y     Time of last modification as seconds since Epoch
 %z     Time of last change
 %Z     Time of last change as seconds since Epoch
</pre>
<p> FMT sequences for file systems: </p>
<pre>
 %a     Free blocks available to non-superuser
 %b     Total data blocks
 %c     Total file nodes
 %d     Free file nodes
 %f     Free blocks
 %i     File System ID in hex
 %l     Maximum length of filenames
 %n     File name
 %s     Block size (for faster transfer)
 %S     Fundamental block size (for block counts)
 %t     Type in hex
 %T     Type in human readable form
</pre>
<dt><code>strings</code></dt>
<dd> strings [-fo] [-t o/d/x] [-n LEN] [FILE]&#8230; </dd>
<p> Display printable strings in a binary file </p>
<pre>
        -f              Precede strings with filenames
        -o              Precede strings with octal offsets
        -t o/d/x        Precede strings with offsets in base 8/10/16
        -n LEN          At least LEN characters form a string (default 4)
</pre>
<dt><code>stty</code></dt>
<dd> stty [-a|g] [-F DEVICE] [SETTING]&#8230; </dd>
<p> Without arguments, prints baud rate, line discipline, and deviations from stty sane </p>
<pre>
        -F DEVICE       Open device instead of stdin
        -a              Print all current settings in human-readable form
        -g              Print in stty-readable form
        [SETTING]       See manpage
</pre>
<dt><code>su</code></dt>
<dd> su [-lmp] [-] [-s SH] [USER [SCRIPT ARGS / -c &#8216;CMD&#8216; ARG0 ARGS]] </dd>
<p> Run shell under USER (by default, root) </p>
<pre>
        -,-l    Clear environment, go to home dir, run shell as login shell
        -p,-m   Do not set new $HOME, $SHELL, $USER, $LOGNAME
        -c CMD  Command to pass to 'sh -c'
        -s SH   Shell to use instead of user's default
</pre>
<dt><code>sulogin</code></dt>
<dd> sulogin [-t N] [TTY] </dd>
<p> Single user login </p>
<pre>
        -t N    Timeout
</pre>
<dt><code>svc</code></dt>
<dd> svc [-udopchaitkx] SERVICE_DIR&#8230; </dd>
<p> Control services monitored by runsv supervisor </p>
<p>&#8211; u If service is not running, start it;<br/>
restart if it stops &#8211; d If service is running, send TERM + CONT signals;<br/>
do<br/>
    not restart it &#8211; o Once : if service is not running, start it;<br/>
do<br/>
not restart it &#8211; pchaitk Send STOP, CONT, HUP, ALRM, INT, TERM, KILL signal to service &#8211; x Exit : runsv will exit as soon as the service is down</p>
<dt><code>svok</code></dt>
<dd> svok SERVICE_DIR </dd>
<p> Check whether runsv supervisor is running. Exit code is 0 if it does, 100 if it does not, 111 (with error message) if SERVICE_DIR does not exist.</p>
<dt><code>swapoff</code></dt>
<dd> swapoff [-a] [DEVICE] </dd>
<p> Stop swapping on DEVICE </p>
<pre>
        -a      Stop swapping on all swap devices
</pre>
<dt><code>swapon</code></dt>
<dd> swapon [-a] [-e] [-d[POL]] [DEVICE] </dd>
<p> Start swapping on DEVICE </p>
<pre>
        -a      Start swapping on all swap devices
        -d[POL] Discard blocks at swapon (POL=once),
                as freed (POL=pages), or both (POL omitted)
        -e      Silently skip devices that do not exist
</pre>
<dt><code>switch_root</code></dt>
<dd> switch_root [-c CONSOLE_DEV] NEW_ROOT NEW_INIT [ARGS] </dd>
<p> Free initramfs and switch to another root fs: </p>
<p> chroot to NEW_ROOT, delete all in /, move NEW_ROOT to /, execute NEW_INIT. PID must be 1. NEW_ROOT must be a mountpoint. </p>
<pre>
        -c DEV  Reopen stdio to DEV after switch
</pre>
<dt><code>sync</code></dt>
<dd> sync [-df] [FILE]&#8230; </dd>
<p> Write all buffered blocks (in FILEs) to disk <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Avoid syncing metadata<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>-f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Sync filesystems underlying FILEs</p>
<dt><code>sysctl</code></dt>
<dd> sysctl -p [-enq] [FILE&#8230;] / [-enqaw] [KEY[=VALUE]]&#8230; </dd>
<p> Show/set kernel parameters </p>
<pre>
        -p      Set values from FILEs (default /etc/sysctl.conf)
        -e      Don't warn about unknown keys
        -n      Don't show key names
        -q      Quiet
        -a      Show all values
        -w      Set values
</pre>
<dt><code>syslogd</code></dt>
<dd> syslogd [OPTIONS] </dd>
<p> System logging utility (this version of syslogd ignores /etc/syslog.conf) </p>
<p>&#8211; n Run in foreground &#8211; R HOST[:PORT<br/>
] Log to<br/>
HOST:PORT(default PORT:514) &#8211; L Log locally and via network(default is network only if &#8211; R) &#8211; C[size_kb] Log to shared mem buffer(use logread to read it) &#8211; O FILE Log to FILE(default: / var / log / messages, stdout if -) &#8211; l N Log only messages more urgent than prio N(1 &#8211; 8) &#8211; S Smaller output<br/>
     &#8211; t Strip client &#8211; generated timestamps</p>
<dt><code>tac</code></dt>
<dd> tac [FILE]&#8230; </dd>
<p> Concatenate FILEs and print them in reverse</p>
<dt><code>tail</code></dt>
<dd> tail [OPTIONS] [FILE]&#8230; </dd>
<p> Print last 10 lines of each FILE (or stdin) to stdout. With more than one FILE, precede each with a filename header. </p>
<p>&#8211; f Print data as file grows &#8211; c[+] N[kbm] Print last N bytes &#8211; n N[kbm] Print last N lines &#8211; n + N[kbm] Start on Nth line and print the rest &#8211; q Never print headers &#8211; s SECONDS Wait SECONDS between reads with &#8211; f &#8211; v Always print headers &#8211; F Same as &#8211; f, but keep retrying</p>
<p> N may be suffixed by k (x1024), b (x512), or m (x1024^2).</p>
<dt><code>tar</code></dt>
<dd> tar c|x|t [-ZzJjahmvokO] [-f TARFILE] [-C DIR] [FILE]&#8230; </dd>
<p> Create, extract, or list files from a tar file </p>
<pre>
        c       Create
        x       Extract
        t       List
        -f FILE Name of TARFILE ('-' for stdin/out)
        -C DIR  Change to DIR before operation
        -v      Verbose
        -O      Extract to stdout
        -m      Don't restore mtime
        -o      Don't restore user:group
        -k      Don't replace existing files
        -Z      (De)compress using compress
        -z      (De)compress using gzip
        -J      (De)compress using xz
        -j      (De)compress using bzip2
        -a      (De)compress using lzma
        -h      Follow symlinks
</pre>
<dt><code>taskset</code></dt>
<dd> taskset [-p] [HEXMASK] PID | PROG ARGS </dd>
<p> Set or get CPU affinity </p>
<pre>
        -p      Operate on an existing PID
</pre>
<dt><code>tc</code></dt>
<dd> tc OBJECT CMD [dev STRING] </dd>
<p> OBJECT: qdisc|class|filter CMD: add|del|change|replace|show </p>
<p> qdisc [handle QHANDLE] [root|ingress|parent CLASSID] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[[QDISC_KIND] [help|OPTIONS]]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>QDISC_KIND := [p|b]fifo|tbf|prio|cbq|red|etc.<br/>
 qdisc show [dev STRING] [ingress] class [classid CLASSID] [root|parent CLASSID] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[[QDISC_KIND] [help|OPTIONS] ]<br/>
 class show [ dev STRING ] [root|parent CLASSID] filter [pref PRIO] [protocol PROTO] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[root|classid CLASSID] [handle FILTERID]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[[FILTER_TYPE] [help|OPTIONS]]<br/>
 filter show [dev STRING] [root|parent CLASSID]</p>
<dt><code>tee</code></dt>
<dd> tee [-ai] [FILE]&#8230; </dd>
<p> Copy stdin to each FILE, and also to stdout </p>
<pre>
        -a      Append to the given FILEs, don't overwrite
        -i      Ignore interrupt signals (SIGINT)
</pre>
<dt><code>telnet</code></dt>
<dd> telnet [-a] [-l USER] HOST [PORT] </dd>
<p> Connect to telnet server </p>
<pre>
        -a      Automatic login with $USER variable
        -l USER Automatic login as USER
</pre>
<dt><code>telnetd</code></dt>
<dd> telnetd [OPTIONS] </dd>
<p> Handle incoming telnet connections </p>
<pre>
        -l LOGIN        Exec LOGIN on connect
        -f ISSUE_FILE   Display ISSUE_FILE instead of /etc/issue
        -K              Close connection as soon as login exits
                        (normally wait until all programs close slave pty)
        -p PORT         Port to listen on
        -b ADDR[:PORT]  Address to bind to
        -F              Run in foreground
        -i              Inetd mode
</pre>
<dt><code>tftp</code></dt>
<dd> tftp [OPTIONS] HOST [PORT] </dd>
<p> Transfer a file from/to tftp server </p>
<pre>
        -l FILE Local FILE
        -r FILE Remote FILE
        -g      Get file
        -p      Put file
        -b SIZE Transfer blocks of SIZE octets
</pre>
<dt><code>time</code></dt>
<dd> time [-vpa] [-o FILE] PROG ARGS </dd>
<p> Run PROG, display resource usage when it exits </p>
<pre>
        -v      Verbose
        -p      POSIX output format
        -f FMT  Custom format
        -o FILE Write result to FILE
        -a      Append (else overwrite)
</pre>
<dt><code>timeout</code></dt>
<dd> timeout [-s SIG] SECS PROG ARGS </dd>
<p> Runs PROG. Sends SIG to it if it is not gone in SECS seconds. Default SIG: TERM.</p>
<dt><code>top</code></dt>
<dd> top [-b] [-nCOUNT] [-dSECONDS] </dd>
<p> Provide a view of process activity in real time. Read the status of all processes from /proc each SECONDS and display a screenful of them. Keys: </p>
<pre>
        N/M/P/T: sort by pid/mem/cpu/time
        R: reverse sort
        H: toggle threads
        Q,^C: exit
</pre>
<p> Options: </p>
<pre>
        -b      Batch mode
        -n N    Exit after N iterations
        -d N    Delay between updates
</pre>
<dt><code>touch</code></dt>
<dd> touch [-c] [-d DATE] [-t DATE] [-r FILE] FILE&#8230; </dd>
<p> Update the last-modified date on the given FILE[s] </p>
<pre>
        -c      Don't create files
        -h      Don't follow links
        -d DT   Date/time to use
        -t DT   Date/time to use
        -r FILE Use FILE's date/time
</pre>
<dt><code>tr</code></dt>
<dd> tr [-cds] STRING1 [STRING2] </dd>
<p> Translate, squeeze, or delete characters from stdin, writing to stdout </p>
<pre>
        -c      Take complement of STRING1
        -d      Delete input characters coded STRING1
        -s      Squeeze multiple output characters of STRING2 into one character
</pre>
<dt><code>traceroute</code></dt>
<dd> traceroute [-46FIlnrv] [-f 1ST_TTL] [-m MAXTTL] [-q PROBES] [-p PORT] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-t TOS] [-w WAIT_SEC] [-s SRC_IP] [-i IFACE]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-z PAUSE_MSEC] HOST [BYTES]</dd>
<p> Trace the route to HOST </p>
<pre>
        -4,-6   Force IP or IPv6 name resolution
        -F      Set don't fragment bit
        -l      Display TTL value of the returned packet
        -n      Print numeric addresses
        -r      Bypass routing tables, send directly to HOST
        -v      Verbose
        -f N    First number of hops (default 1)
        -m N    Max number of hops
        -q N    Number of probes per hop (default 3)
        -p N    Base UDP port number used in probes
                (default 33434)
        -s IP   Source address
        -i IFACE Source interface
        -t N    Type-of-service in probe packets (default 0)
        -w SEC  Time to wait for a response (default 3)
        -g IP   Loose source route gateway (8 max)
</pre>
<dt><code>traceroute6</code></dt>
<dd> traceroute6 [-nrv] [-m MAXTTL] [-q PROBES] [-p PORT] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-t TOS] [-w WAIT_SEC] [-s SRC_IP] [-i IFACE]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>HOST [BYTES]</dd>
<p> Trace the route to HOST </p>
<pre>
        -n      Print numeric addresses
        -r      Bypass routing tables, send directly to HOST
        -v      Verbose
        -m N    Max number of hops
        -q N    Number of probes per hop (default 3)
        -p N    Base UDP port number used in probes
                (default 33434)
        -s IP   Source address
        -i IFACE Source interface
        -t N    Type-of-service in probe packets (default 0)
        -w SEC  Time wait for a response (default 3)
</pre>
<dt><code>truncate</code></dt>
<dd> truncate [-c] -s SIZE FILE&#8230; </dd>
<p> Truncate FILEs to the given size </p>
<pre>
        -c      Do not create files
        -s SIZE Truncate to SIZE
</pre>
<dt><code>tty</code></dt>
<dd> tty </dd>
<p> Print file name of stdin&#8217;s terminal </p>
<pre>
        -s      Print nothing, only return exit status
</pre>
<dt><code>tunctl</code></dt>
<dd> tunctl [-f device] ([-t name] | -d name) </dd>
<p> Create or delete tun interfaces </p>
<pre>
        -f name         tun device (/dev/net/tun)
        -t name         Create iface 'name'
        -d name         Delete iface 'name'
</pre>
<dt><code>ubirename</code></dt>
<dd> ubirename UBI_DEVICE OLD_VOLNAME NEW_VOLNAME [OLD2 NEW2]&#8230; </dd>
<p> Rename UBI volumes on UBI_DEVICE</p>
<dt><code>udhcpc</code></dt>
<dd> udhcpc [-fbqRB] [-a[MSEC]] [-t N] [-T SEC] [-A SEC/-n] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-i IFACE] [-s PROG] [-p PIDFILE]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-oC] [-r IP] [-V VENDOR] [-F NAME] [-x OPT:VAL]&#8230; [-O OPT]&#8230;</dd>
<p>&#8211; i IFACE Interface to use(default eth0) &#8211; s PROG Run PROG at DHCP events(default / etc / udhcpc / default.script) &#8211; p FILE Create pidfile<br/>
    &#8211; B Request broadcast replies<br/>
    &#8211; t N Send up to N discover packets(default 3) &#8211; T SEC Pause between packets(default 3) &#8211; A SEC Wait if lease is not obtained(default 20) &#8211; n Exit if lease is not obtained<br/>
    &#8211; q Exit after obtaining lease<br/>
    &#8211; R Release IP on exit<br/>
    &#8211; f Run in foreground<br/>
    &#8211; b Background if lease is not obtained<br/>
    &#8211; S Log to syslog too<br/>
    &#8211; a[MSEC] Validate offered address with ARP ping<br/>
    &#8211; r IP Request this IP address<br/>
    &#8211; o Don&#8217;t request any options (unless -O is given) &#8211; O OPT Request option OPT from server(cumulative) &#8211; x OPT:VAL Include option OPT in sent packets(cumulative)<br/>
                        Examples of string, numeric, and hex byte opts:<br/>
                        -x hostname:bbox &#8211; option 12<br/>
                        -x lease:3600 &#8211; option 51 (lease time)<br/>
                        -x 0x3d:0100BEEFC0FFEE &#8211; option 61 (client id)<br/>
                        -x 14:'&#8221;dumpfile&#8221;&#8216; &#8211; option 14 (shell-quoted)<br/>
        -F NAME         Ask server to update DNS mapping for NAME<br/>
        -V VENDOR       Vendor identifier (default &#8216;udhcp VERSION&#8217;)<br/>
        -C              Don&#8217;t send MAC as client identifier<br/>
Signals:<br/>
        USR1    Renew lease<br/>
        USR2    Release lease</p>
<dt><code>udhcpd</code></dt>
<dd> udhcpd [-fS] [-I ADDR] [CONFFILE] </dd>
<p> DHCP server </p>
<pre>
        -f      Run in foreground
        -S      Log to syslog too
        -I ADDR Local address
        -a MSEC Timeout for ARP ping (default 2000)
</pre>
<dt><code>uevent</code></dt>
<dd> uevent [PROG [ARGS]] </dd>
<p> uevent runs PROG for every netlink notification. PROG&#8216;s environment contains data passed from the kernel. Typical usage (daemon for dynamic device node creation): <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># uevent mdev &amp; mdev -s</p>
<dt><code>umount</code></dt>
<dd> umount [OPTIONS] FILESYSTEM|DIRECTORY </dd>
<p> Unmount file systems </p>
<p>&#8211; a Unmount all file systems &#8211; r Try to remount devices as read &#8211; only if mount is busy &#8211; l Lazy umount(detach filesystem) &#8211; f Force umount(i.e., unreachable NFS server) &#8211; d Free loop device if it has been used<br/>
    &#8211; t FSTYPE[, &#8230;] Unmount only these filesystem type(s)</p>
<dt><code>uname</code></dt>
<dd> uname [-amnrspvio] </dd>
<p> Print system information </p>
<pre>
        -a      Print all
        -m      The machine (hardware) type
        -n      Hostname
        -r      Kernel release
        -s      Kernel name (default)
        -p      Processor type
        -v      Kernel version
        -i      The hardware platform
        -o      OS name
</pre>
<dt><code>uncompress</code></dt>
<dd> uncompress [-cf] [FILE]&#8230; </dd>
<p> Decompress .Z file[s] </p>
<pre>
        -c      Write to stdout
        -f      Overwrite
</pre>
<dt><code>unexpand</code></dt>
<dd> unexpand [-fa][-t N] [FILE]&#8230; </dd>
<p> Convert spaces to tabs, writing to stdout </p>
<pre>
        -a      Convert all blanks
        -f      Convert only leading blanks
        -t N    Tabstops every N chars
</pre>
<dt><code>uniq</code></dt>
<dd> uniq [-cdu][-f,s,w N] [INPUT [OUTPUT]] </dd>
<p> Discard duplicate lines </p>
<pre>
        -c      Prefix lines by the number of occurrences
        -d      Only print duplicate lines
        -u      Only print unique lines
        -i      Ignore case
        -f N    Skip first N fields
        -s N    Skip first N chars (after any skipped fields)
        -w N    Compare N characters in line
</pre>
<dt><code>unix2dos</code></dt>
<dd> unix2dos [-ud] [FILE] </dd>
<p> Convert FILE in-place from Unix to DOS format. When no file is given, use stdin/stdout. </p>
<pre>
        -u      dos2unix
        -d      unix2dos
</pre>
<dt><code>unlink</code></dt>
<dd> unlink FILE </dd>
<p> Delete FILE by calling <code>unlink()</code></p>
<dt><code>unlzma</code></dt>
<dd> unlzma [-cfk] [FILE]&#8230; </dd>
<p> Decompress FILE (or stdin) </p>
<pre>
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>unshare</code></dt>
<dd> unshare [OPTIONS] [PROG [ARGS]] </dd>
<p>&#8211; m, &#8211;mount[= FILE] Unshare mount namespace &#8211; u, &#8211;uts[= FILE] Unshare UTS namespace(hostname etc.) &#8211; i, &#8211;ipc[= FILE] Unshare System V IPC namespace &#8211; n, &#8211;net[= FILE] Unshare network namespace &#8211; p, &#8211;pid[= FILE] Unshare PID namespace &#8211; U, &#8211;user[= FILE] Unshare user namespace &#8211; f, &#8211;fork Fork before execing PROG &#8211; r, &#8211;map &#8211; root &#8211; user Map current user to root(implies &#8211; U)&#8211; mount &#8211; proc[= DIR] Mount / proc filesystem first(implies &#8211; m)&#8211; propagation slave | shared | private | unchanged Modify mount propagation in mount namespace &#8211;setgroups allow | deny Control the setgroups syscall in user namespaces</p>
<dt><code>unxz</code></dt>
<dd> unxz [-cfk] [FILE]&#8230; </dd>
<p> Decompress FILE (or stdin) </p>
<pre>
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>unzip</code></dt>
<dd> unzip [-lnojpq] FILE[.zip] [FILE]&#8230; [-x FILE&#8230;] [-d DIR] </dd>
<p> Extract FILEs from ZIP archive </p>
<pre>
        -l      List contents (with -q for short form)
        -n      Never overwrite files (default: ask)
        -o      Overwrite
        -j      Do not restore paths
        -p      Print to stdout
        -q      Quiet
        -x FILE Exclude FILEs
        -d DIR  Extract into DIR
</pre>
<dt><code>uptime</code></dt>
<dd> uptime </dd>
<p> Display the time since the last boot</p>
<dt><code>usleep</code></dt>
<dd> usleep N </dd>
<p> Pause for N microseconds</p>
<dt><code>uudecode</code></dt>
<dd> uudecode [-o OUTFILE] [INFILE] </dd>
<p> Uudecode a file Finds OUTFILE in uuencoded source unless -o is given</p>
<dt><code>uuencode</code></dt>
<dd> uuencode [-m] [FILE] STORED_FILENAME </dd>
<p> Uuencode FILE (or stdin) to stdout </p>
<pre>
        -m      Use base64 encoding per RFC1521
</pre>
<dt><code>vconfig</code></dt>
<dd> vconfig COMMAND [OPTIONS] </dd>
<p> Create and remove virtual ethernet devices </p>
<pre>
        add             IFACE VLAN_ID
        rem             VLAN_NAME
        set_flag        IFACE 0|1 VLAN_QOS
        set_egress_map  VLAN_NAME SKB_PRIO VLAN_QOS
        set_ingress_map VLAN_NAME SKB_PRIO VLAN_QOS
        set_name_type   NAME_TYPE
</pre>
<dt><code>vi</code></dt>
<dd> vi [OPTIONS] [FILE]&#8230; </dd>
<p> Edit FILE </p>
<pre>
        -c CMD  Initial command to run ($EXINIT also available)
        -R      Read-only
        -H      List available features
</pre>
<dt><code>w</code></dt>
<dd> w </dd>
<p> Show who is logged on</p>
<dt><code>watch</code></dt>
<dd> watch [-n SEC] [-t] PROG ARGS </dd>
<p> Run PROG periodically </p>
<pre>
        -n      Loop period in seconds (default 2)
        -t      Don't print header
</pre>
<dt><code>watchdog</code></dt>
<dd> watchdog [-t N[ms]] [-T N[ms]] [-F] DEV </dd>
<p> Periodically write to watchdog device DEV </p>
<pre>
        -T N    Reboot after N seconds if not reset (default 60)
        -t N    Reset every N seconds (default 30)
        -F      Run in foreground
</pre>
<p> Use 500ms to specify period in milliseconds</p>
<dt><code>wc</code></dt>
<dd> wc [-cmlwL] [FILE]&#8230; </dd>
<p> Count lines, words, and bytes for each FILE (or stdin) </p>
<pre>
        -c      Count bytes
        -m      Count characters
        -l      Count newlines
        -w      Count words
        -L      Print longest line length
</pre>
<dt><code>wget</code></dt>
<dd> wget [-c|&#8211;continue] [&#8211;spider] [-q|&#8211;quiet] [-O|&#8211;output-document FILE] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[&#8211;header &#8216;header: value&#8217;] [-Y|&#8211;proxy on/off] [-P DIR]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[&#8211;no-check-certificate]<br/>
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[-S|&#8211;server-response] [-U|&#8211;user-agent AGENT] URL&#8230;</dd>
<p> Retrieve files via HTTP or FTP </p>
<p>&#8211;spider Only check URL existence : $ ? is 0 if exists&#8211; no &#8211; check &#8211; certificate Don &#8216;t validate the server&#8217; s certificate &#8211; c Continue retrieval of aborted transfer &#8211; q Quiet &#8211; P DIR Save to DIR(default.) &#8211; S Show server response<br/>
                                            &#8211; O FILE Save to FILE(&#8216;-&#8216; for stdout) &#8211; U STR Use STR for User &#8211; Agent header &#8211; Y on / off Use proxy</p>
<dt><code>which</code></dt>
<dd> which [COMMAND]&#8230; </dd>
<p> Locate a COMMAND</p>
<dt><code>who</code></dt>
<dd> who [-a] </dd>
<p> Show who is logged on </p>
<pre>
        -a      Show all
        -H      Print column headers
</pre>
<dt><code>whoami</code></dt>
<dd> whoami </dd>
<p> Print the user name associated with the current effective user id</p>
<dt><code>xargs</code></dt>
<dd> xargs [OPTIONS] [PROG ARGS] </dd>
<p> Run PROG on every item given by stdin </p>
<p>&#8211; p Ask user whether to run each command &#8211; r Don&#8217;t run command if input is empty &#8211; 0 Input is separated by NULs &#8211; a FILE Read from FILE instead of stdin &#8211; t Print the command on stderr before execution &#8211; e[STR] STR stops input processing &#8211; n N Pass no more than N args to PROG &#8211; s N Pass command line of no more than N bytes &#8211; I STR Replace STR within PROG ARGS with input line &#8211; P N Run up to N PROGs in parallel &#8211; x Exit if size is exceeded</p>
<dt><code>xxd</code></dt>
<dd> xxd [OPTIONS] [FILE] </dd>
<p> Hex dump FILE (or stdin) </p>
<pre>
        -g N            Bytes per group
        -c N            Bytes per line
        -p              Show only hex bytes, assumes -c30
        -l LENGTH       Show only first LENGTH bytes
        -s OFFSET       Skip OFFSET bytes
</pre>
<dt><code>xz</code></dt>
<dd> xz -d [-cfk] [FILE]&#8230; </dd>
<p> Decompress FILE (or stdin) </p>
<pre>
        -d      Decompress
        -c      Write to stdout
        -f      Force
        -k      Keep input files
</pre>
<dt><code>xzcat</code></dt>
<dd> xzcat [FILE]&#8230; </dd>
<p> Decompress to stdout</p>
<dt><code>yes</code></dt>
<dd> yes [STRING] </dd>
<p> Repeatedly output a line with STRING, or &#8216;y&#8217;</p>
<dt><code>zcat</code></dt>
<dd> zcat [FILE]&#8230; </dd>
<p> Decompress to stdout</dl>
<h2>LIBC NSS</h2>
<p> GNU Libc (glibc) uses the Name Service Switch (NSS) to configure the behavior of the C library for the local environment, and to configure how it reads system data, such as passwords and group information. This is implemented using an /etc/nsswitch.conf configuration file, and using one or more of the /lib/libnss_* libraries. BusyBox tries to avoid using any libc calls that make use of NSS. Some applets however, such as login and su, will use libc functions that require NSS. </p>
<p> If you enable CONFIG_USE_BB_PWD_GRP, BusyBox will use internal functions to directly access the /etc/passwd, /etc/group, and /etc/shadow files without using NSS. This may allow you to run your system without the need for installing any of the NSS configuration files and libraries. </p>
<p> When used with glibc, the BusyBox &#8216;networking&#8217; applets will similarly require that you install at least some of the glibc NSS stuff (in particular, /etc/nsswitch.conf, /lib/libnss_dns*, /lib/libnss_files*, and /lib/libresolv*). </p>
<p> Shameless Plug: As an alternative, one could use a C library such as uClibc. In addition to making your system significantly smaller, uClibc does not require the use of any NSS support files or libraries.</p>
<h2>MAINTAINER</h2>
<p> Denis Vlasenko &lt;vda.linux [at] googlemail.com&gt;</p>
<h2>AUTHORS</h2>
<p> The following people have contributed code to BusyBox whether they know it or not. If you have written code included in BusyBox, you should probably be listed here so you can obtain your bit of eternal glory. If you should be listed here, or the description of what you have done needs more detail, or is incorrect, please send in an update. </p>
<p> Emanuele Aina &lt;emanuele.aina [at] tiscali.it&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;run-parts </p>
<p> Erik Andersen &lt;andersen [at] codepoet.org&gt; </p>
<pre>
    Tons of new stuff, major rewrite of most of the
    core apps, tons of new apps as noted in header files.
    Lots of tedious effort writing these boring docs that
    nobody is going to actually read.
</pre>
<p> Laurence Anderson &lt;l.d.anderson [at] warwick.ac.uk&gt; </p>
<pre>
    rpm2cpio, unzip, get_header_cpio, read_gz interface, rpm
</pre>
<p> Jeff Angielski &lt;jeff [at] theptrgroup.com&gt; </p>
<pre>
    ftpput, ftpget
</pre>
<p> Edward Betts &lt;edward [at] debian.org&gt; </p>
<pre>
    expr, hostid, logname, whoami
</pre>
<p> John Beppu &lt;beppu [at] codepoet.org&gt; </p>
<pre>
    du, nslookup, sort
</pre>
<p> Brian Candler &lt;B.Candler [at] pobox.com&gt; </p>
<pre>
    tiny-ls(ls)
</pre>
<p> Randolph Chung &lt;tausq [at] debian.org&gt; </p>
<pre>
    fbset, ping, hostname
</pre>
<p> Dave Cinege &lt;dcinege [at] psychosis.com&gt; </p>
<pre>
    more(v2), makedevs, dutmp, modularization, auto links file,
    various fixes, Linux Router Project maintenance
</pre>
<p> Jordan Crouse &lt;jordan [at] cosmicpenguin.net&gt; </p>
<pre>
    ipcalc
</pre>
<p> Magnus Damm &lt;damm [at] opensource.se&gt; </p>
<pre>
    tftp client insmod powerpc support
</pre>
<p> Larry Doolittle &lt;ldoolitt [at] recycle.lbl.gov&gt; </p>
<pre>
    pristine source directory compilation, lots of patches and fixes.
</pre>
<p> Glenn Engel &lt;glenne [at] engel.org&gt; </p>
<pre>
    httpd
</pre>
<p> Gennady Feldman &lt;gfeldman [at] gena01.com&gt; </p>
<pre>
    Sysklogd (single threaded syslogd, IPC Circular buffer support,
    logread), various fixes.
</pre>
<p> Karl M. Hegbloom &lt;karlheg [at] debian.org&gt; </p>
<pre>
    cp_mv.c, the test suite, various fixes to utility.c, &amp;c.
</pre>
<p> Daniel Jacobowitz &lt;dan [at] debian.org&gt; </p>
<pre>
    mktemp.c
</pre>
<p> Matt Kraai &lt;kraai [at] alumni.cmu.edu&gt; </p>
<pre>
    documentation, bugfixes, test suite
</pre>
<p> Stephan Linz &lt;linz [at] li-pro.net&gt; </p>
<pre>
    ipcalc, Red Hat equivalence
</pre>
<p> John Lombardo &lt;john [at] deltanet.com&gt; </p>
<pre>
    tr
</pre>
<p> Glenn McGrath &lt;bug1 [at] iinet.net.au&gt; </p>
<pre>
    Common unarchiving code and unarchiving applets, ifupdown, ftpgetput,
    nameif, sed, patch, fold, install, uudecode.
    Various bugfixes, review and apply numerous patches.
</pre>
<p> Manuel Novoa III &lt;mjn3 [at] codepoet.org&gt; </p>
<pre>
    cat, head, mkfifo, mknod, rmdir, sleep, tee, tty, uniq, usleep, wc, yes,
    mesg, vconfig, make_directory, parse_mode, dirname, mode_string,
    get_last_path_component, simplify_path, and a number trivial libbb routines
    also bug fixes, partial rewrites, and size optimizations in
    ash, basename, cal, cmp, cp, df, du, echo, env, ln, logname, md5sum, mkdir,
    mv, realpath, rm, sort, tail, touch, uname, watch, arith, human_readable,
    interface, dutmp, ifconfig, route
</pre>
<p> Vladimir Oleynik &lt;dzo [at] simtreas.ru&gt; </p>
<pre><code>
cmdedit;
xargs(current), httpd(current);
ports : ash, crond, fdisk, inetd, stty, traceroute, top;
locale, various fixes
            and irreconcilable critic of everything not perfect.
</code></pre>
<p> Bruce Perens &lt;bruce [at] pixar.com&gt; </p>
<pre>
    Original author of BusyBox in 1995, 1996. Some of his code can
    still be found hiding here and there...
</pre>
<p> Tim Riker &lt;Tim [at] Rikers.org&gt; </p>
<pre>
    bug fixes, member of fan club
</pre>
<p> Kent Robotti &lt;robotti [at] metconnect.com&gt; </p>
<pre>
    reset, tons and tons of bug reports and patches.
</pre>
<p> Chip Rosenthal &lt;chip [at] unicom.com&gt;, &lt;crosenth [at] covad.com&gt; </p>
<pre>
    wget - Contributed by permission of Covad Communications
</pre>
<p> Pavel Roskin &lt;proski [at] gnu.org&gt; </p>
<pre>
    Lots of bugs fixes and patches.
</pre>
<p> Gyepi Sam &lt;gyepi [at] praxis-sw.com&gt; </p>
<pre>
    Remote logging feature for syslogd
</pre>
<p> Linus Torvalds &lt;torvalds [at] transmeta.com&gt; </p>
<pre>
    mkswap, fsck.minix, mkfs.minix
</pre>
<p> Mark Whitley &lt;markw [at] codepoet.org&gt; </p>
<pre>
    grep, sed, cut, xargs(previous),
    style-guide, new-applet-HOWTO, bug fixes, etc.
</pre>
<p> Charles P. Wright &lt;cpwright [at] villagenet.com&gt; </p>
<pre>
    gzip, mini-netcat(nc)
</pre>
<p> Enrique Zanardi &lt;ezanardi [at] ull.es&gt; </p>
<pre>
    tarcat (since removed), loadkmap, various fixes, Debian maintenance
</pre>
<p> Tito Ragusa &lt;farmatito [at] tiscali.it&gt; </p>
<pre>
    devfsd and size optimizations in strings, openvt and deallocvt.
</pre>
<p> Paul Fox &lt;pgf [at] foxharp.boston.ma.us&gt; </p>
<pre>
    vi editing mode for ash, various other patches/fixes
</pre>
<p> Roberto A. Foglietta &lt;me [at] roberto.foglietta.name&gt; </p>
<pre>
    port: dnsd
</pre>
<p> Bernhard Reutner-Fischer &lt;rep.dot.nop [at] gmail.com&gt; </p>
<pre>
    misc
</pre>
<p> Mike Frysinger &lt;vapier [at] gentoo.org&gt; </p>
<pre>
    initial e2fsprogs, printenv, setarch, sum, misc
</pre>
<p> Jie Zhang &lt;jie.zhang [at] analog.com&gt; </p>
<pre>
    fixed two bugs in msh and hush (exitcode of killed processes)
</pre>
