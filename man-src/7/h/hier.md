---
title: "hier(7)"
name: "hier"
section: "7"
letter: "h"
url: "/docs/linux/man/7-hier/"
description: "hier – description of the filesystem hierarchy"
---

<p>hier &#8211; description of the filesystem hierarchy</p>
<h2>Description</h2>
<p>A typical Linux system has, among others, the following directories:</p>
<dl>
<dt><i>/</i></p>
<dd>This is the root directory. This is where the whole tree starts.</p>
<dt><i>/bin</i></p>
<dd>This directory contains executable programs which are needed in single user mode and to bring the system up or repair it.</p>
<dt><i>/boot</i></p>
<dd>Contains static files for the boot loader. This directory holds only the files which are needed during the boot process. The map installer and configuration files should go to <i>/sbin</i> and <i>/etc</i>. The operating system kernel (initrd for example) must be located in either <i>/</i> or <i>/boot</i>.</p>
<dt><i>/dev</i></p>
<dd>Special or device files, which refer to physical devices. See <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1).</p>
<dt><i>/etc</i></p>
<dd>Contains configuration files which are local to the machine. Some larger software packages, like X11, can have their own subdirectories below <i>/etc</i>. Site-wide configuration files may be placed here or in <i>/usr/etc</i>. Nevertheless, programs should always look for these files in <i>/etc</i> and you may have links for these files to <i>/usr/etc</i>.</p>
<dt><i>/etc/opt</i></p>
<dd>Host-specific configuration files for add-on applications installed in <i>/opt</i>.</p>
<dt><i>/etc/sgml</i></p>
<dd>This directory contains the configuration files for SGML (optional).</p>
<dt><i>/etc/skel</i></p>
<dd>When a new user account is created, files from this directory are usually copied into the user&#8217;s home directory.</p>
<dt><i>/etc/X11</i></p>
<dd>Configuration files for the X11 window system (optional).</p>
<dt><i>/etc/xml</i></p>
<dd>This directory contains the configuration files for XML (optional).</p>
<dt><i>/home</i></p>
<dd>On machines with home directories for users, these are usually beneath this directory, directly or not. The structure of this directory depends on local administration decisions (optional).</p>
<dt><i>/lib</i></p>
<dd>This directory should hold those shared libraries that are necessary to boot the system and to run the commands in the root filesystem.</p>
<dt><i>/lib&lt;qual&gt;</i></p>
<dd>These directories are variants of <i>/lib</i> on system which support more than one binary format requiring separate libraries (optional).</p>
<dt><i>/lib/modules</i></p>
<dd>Loadable kernel modules (optional).</p>
<dt><i>/lost+found</i></p>
<dd>This directory contains items lost in the filesystem. These items are usually chunks of files mangled as a consequence of a faulty disk or a system crash.</p>
<dt><i>/media</i></p>
<dd>This directory contains mount points for removable media such as CD and DVD disks or USB sticks. On systems where more than one device exists for mounting a certain type of media, mount directories can be created by appending a digit to the name of those available above starting with &#8216;0&#8217;, but the unqualified name must also exist.</p>
<dt><i>/media/floppy[1-9]</i></p>
<dd>Floppy drive (optional).</p>
<dt><i>/media/cdrom[1-9]</i></p>
<dd>CD-ROM drive (optional).</p>
<dt><i>/media/cdrecorder[1-9]</i></p>
<dd>CD writer (optional).</p>
<dt><i>/media/zip[1-9]</i></p>
<dd>Zip drive (optional).</p>
<dt><i>/media/usb[1-9]</i></p>
<dd>USB drive (optional).</p>
<dt><i>/mnt</i></p>
<dd>This directory is a mount point for a temporarily mounted filesystem. In some distributions, <i>/mnt</i> contains subdirectories intended to be used as mount points for several temporary filesystems.</p>
<dt><i>/opt</i></p>
<dd>This directory should contain add-on packages that contain static files.</p>
<dt><i>/proc</i></p>
<dd>This is a mount point for the <i>proc</i> filesystem, which provides information about running processes and the kernel. This pseudo-filesystem is described in more detail in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><i>/root</i></p>
<dd>This directory is usually the home directory for the root user (optional).</p>
<dt><i>/run</i></p>
<dd>This directory contains information which describes the system since it was booted. Once this purpose was served by <i>/var/run</i> and programs may continue to use it.</p>
<dt><i>/sbin</i></p>
<dd>Like <i>/bin</i>, this directory holds commands needed to boot the system, but which are usually not executed by normal users.</p>
<dt><i>/srv</i></p>
<dd>This directory contains site-specific data that is served by this system.</p>
<dt><i>/sys</i></p>
<dd>This is a mount point for the sysfs filesystem, which provides information about the kernel like <i>/proc</i>, but better structured, following the formalism of kobject infrastructure.</p>
<dt><i>/tmp</i></p>
<dd>This directory contains temporary files which may be deleted with no notice, such as by a regular job or at system boot up.</p>
<dt><i>/usr</i></p>
<dd>This directory is usually mounted from a separate partition. It should hold only shareable, read-only data, so that it can be mounted by various machines running Linux.</p>
<dt><i>/usr/X11R6</i></p>
<dd>The X-Window system, version 11 release 6 (present in FHS 2.3, removed in FHS 3.0).</p>
<dt><i>/usr/X11R6/bin</i></p>
<dd>Binaries which belong to the X-Window system; often, there is a symbolic link from the more traditional <i>/usr/bin/X11</i> to here.</p>
<dt><i>/usr/X11R6/lib</i></p>
<dd>Data files associated with the X-Window system.</p>
<dt><i>/usr/X11R6/lib/X11</i></p>
<dd>These contain miscellaneous files needed to run X; Often, there is a symbolic link from <i>/usr/lib/X11</i> to this directory.</p>
<dt><i>/usr/X11R6/include/X11</i></p>
<dd>Contains include files needed for compiling programs using the X11 window system. Often, there is a symbolic link from <i>/usr/include/X11</i> to this directory.</p>
<dt><i>/usr/bin</i></p>
<dd>This is the primary directory for executable programs. Most programs executed by normal users which are not needed for booting or for repairing the system and which are not installed locally should be placed in this directory.</p>
<dt><i>/usr/bin/mh</i></p>
<dd>Commands for the MH mail handling system (optional).</p>
<dt><i>/usr/bin/X11</i></p>
<dd>is the traditional place to look for X11 executables; on Linux, it usually is a symbolic link to <i>/usr/X11R6/bin</i>.</p>
<dt><i>/usr/dict</i></p>
<dd>Replaced by <i>/usr/share/dict</i>.</p>
<dt><i>/usr/doc</i></p>
<dd>Replaced by <i>/usr/share/doc</i>.</p>
<dt><i>/usr/etc</i></p>
<dd>Site-wide configuration files to be shared between several machines may be stored in this directory. However, commands should always reference those files using the <i>/etc</i> directory. Links from files in <i>/etc</i> should point to the appropriate files in <i>/usr/etc</i>.</p>
<dt><i>/usr/games</i></p>
<dd>Binaries for games and educational programs (optional).</p>
<dt><i>/usr/include</i></p>
<dd>Include files for the C compiler.</p>
<dt><i>/usr/include/bsd</i></p>
<dd>BSD compatibility include files (optional).</p>
<dt><i>/usr/include/X11</i></p>
<dd>Include files for the C compiler and the X-Window system. This is usually a symbolic link to <i>/usr/X11R6/include/X11</i>.</p>
<dt><i>/usr/include/asm</i></p>
<dd>Include files which declare some assembler functions. This used to be a symbolic link to <i>/usr/src/linux/include/asm</i>.</p>
<dt><i>/usr/include/linux</i></p>
<dd>This contains information which may change from system release to system release and used to be a symbolic link to <i>/usr/src/linux/include/linux</i> to get at operating-system-specific information.</p>
<dd>(Note that one should have include files there that work correctly with the current libc and in user space. However, Linux kernel source is not designed to be used with user programs and does not know anything about the libc you are using. It is very likely that things will break if you let <i>/usr/include/asm</i> and <i>/usr/include/linux</i> point at a random kernel tree. Debian systems don&#8217;t do this and use headers from a known good kernel version, provided in the libc*-dev package.)</p>
<dt><i>/usr/include/g++</i></p>
<dd>Include files to use with the GNU C++ compiler.</p>
<dt><i>/usr/lib</i></p>
<dd>Object libraries, including dynamic libraries, plus some executables which usually are not invoked directly. More complicated programs may have whole subdirectories there.</p>
<dt><i>/usr/libexec</i></p>
<dd>Directory contains binaries for internal use only and they are not meant to be executed directly by users shell or scripts.</p>
<dt><i>/usr/lib&lt;qual&gt;</i></p>
<dd>These directories are variants of <i>/usr/lib</i> on system which support more than one binary format requiring separate libraries, except that the symbolic link <i>/usr/lib&lt;qual&gt;/X11</i> is not required (optional).</p>
<dt><i>/usr/lib/X11</i></p>
<dd>The usual place for data files associated with X programs, and configuration files for the X system itself. On Linux, it usually is a symbolic link to <i>/usr/X11R6/lib/X11</i>.</p>
<dt><i>/usr/lib/gcc-lib</i></p>
<dd>contains executables and include files for the GNU C compiler, <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1).</p>
<dt><i>/usr/lib/groff</i></p>
<dd>Files for the GNU groff document formatting system.</p>
<dt><i>/usr/lib/uucp</i></p>
<dd>Files for <code><a href="/docs/linux/man/1-uucp/">uucp</a></code>(1).</p>
<dt><i>/usr/local</i></p>
<dd>This is where programs which are local to the site typically go.</p>
<dt><i>/usr/local/bin</i></p>
<dd>Binaries for programs local to the site.</p>
<dt><i>/usr/local/doc</i></p>
<dd>Local documentation.</p>
<dt><i>/usr/local/etc</i></p>
<dd>Configuration files associated with locally installed programs.</p>
<dt><i>/usr/local/games</i></p>
<dd>Binaries for locally installed games.</p>
<dt><i>/usr/local/lib</i></p>
<dd>Files associated with locally installed programs.</p>
<dt><i>/usr/local/lib&lt;qual&gt;</i></p>
<dd>These directories are variants of <i>/usr/local/lib</i> on system which support more than one binary format requiring separate libraries (optional).</p>
<dt><i>/usr/local/include</i></p>
<dd>Header files for the local C compiler.</p>
<dt><i>/usr/local/info</i></p>
<dd>Info pages associated with locally installed programs.</p>
<dt><i>/usr/local/man</i></p>
<dd>Man pages associated with locally installed programs.</p>
<dt><i>/usr/local/sbin</i></p>
<dd>Locally installed programs for system administration.</p>
<dt><i>/usr/local/share</i></p>
<dd>Local application data that can be shared among different architectures of the same OS.</p>
<dt><i>/usr/local/src</i></p>
<dd>Source code for locally installed software.</p>
<dt><i>/usr/man</i></p>
<dd>Replaced by <i>/usr/share/man</i>.</p>
<dt><i>/usr/sbin</i></p>
<dd>This directory contains program binaries for system administration which are not essential for the boot process, for mounting <i>/usr</i>, or for system repair.</p>
<dt><i>/usr/share</i></p>
<dd>This directory contains subdirectories with specific application data, that can be shared among different architectures of the same OS. Often one finds stuff here that used to live in <i>/usr/doc</i> or <i>/usr/lib</i> or <i>/usr/man</i>.</p>
<dt><i>/usr/share/color</i></p>
<dd>Contains color management information, like International Color Consortium (ICC) Color profiles (optional).</p>
<dt><i>/usr/share/dict</i></p>
<dd>Contains the word lists used by spell checkers (optional).</p>
<dt><i>/usr/share/dict/words</i></p>
<dd>List of English words (optional).</p>
<dt><i>/usr/share/doc</i></p>
<dd>Documentation about installed programs (optional).</p>
<dt><i>/usr/share/games</i></p>
<dd>Static data files for games in <i>/usr/games</i> (optional).</p>
<dt><i>/usr/share/info</i></p>
<dd>Info pages go here (optional).</p>
<dt><i>/usr/share/locale</i></p>
<dd>Locale information goes here (optional).</p>
<dt><i>/usr/share/man</i></p>
<dd>Manual pages go here in subdirectories according to the man page sections.</p>
<dt><i>/usr/share/man/&lt;locale&gt;/man[1-9]</i></p>
<dd>These directories contain manual pages for the specific locale in source code form. Systems which use a unique language and code set for all manual pages may omit the &lt;locale&gt; substring.</p>
<dt><i>/usr/share/misc</i></p>
<dd>Miscellaneous data that can be shared among different architectures of the same OS.</p>
<dt><i>/usr/share/nls</i></p>
<dd>The message catalogs for native language support go here (optional).</p>
<dt><i>/usr/share/ppd</i></p>
<dd>Postscript Printer Definition (PPD) files (optional).</p>
<dt><i>/usr/share/sgml</i></p>
<dd>Files for SGML (optional).</p>
<dt><i>/usr/share/sgml/docbook</i></p>
<dd>DocBook DTD (optional).</p>
<dt><i>/usr/share/sgml/tei</i></p>
<dd>TEI DTD (optional).</p>
<dt><i>/usr/share/sgml/html</i></p>
<dd>HTML DTD (optional).</p>
<dt><i>/usr/share/sgml/mathtml</i></p>
<dd>MathML DTD (optional).</p>
<dt><i>/usr/share/terminfo</i></p>
<dd>The database for terminfo (optional).</p>
<dt><i>/usr/share/tmac</i></p>
<dd>Troff macros that are not distributed with groff (optional).</p>
<dt><i>/usr/share/xml</i></p>
<dd>Files for XML (optional).</p>
<dt><i>/usr/share/xml/docbook</i></p>
<dd>DocBook DTD (optional).</p>
<dt><i>/usr/share/xml/xhtml</i></p>
<dd>XHTML DTD (optional).</p>
<dt><i>/usr/share/xml/mathml</i></p>
<dd>MathML DTD (optional).</p>
<dt><i>/usr/share/zoneinfo</i></p>
<dd>Files for timezone information (optional).</p>
<dt><i>/usr/src</i></p>
<dd>Source files for different parts of the system, included with some packages for reference purposes. Don&#8217;t work here with your own projects, as files below /usr should be read-only except when installing software (optional).</p>
<dt><i>/usr/src/linux</i></p>
<dd>This was the traditional place for the kernel source. Some distributions put here the source for the default kernel they ship. You should probably use another directory when building your own kernel.</p>
<dt><i>/usr/tmp</i></p>
<dd>Obsolete. This should be a link to <i>/var/tmp</i>. This link is present only for compatibility reasons and shouldn&#8217;t be used.</p>
<dt><i>/var</i></p>
<dd>This directory contains files which may change in size, such as spool and log files.</p>
<dt><i>/var/account</i></p>
<dd>Process accounting logs (optional).</p>
<dt><i>/var/adm</i></p>
<dd>This directory is superseded by <i>/var/log</i> and should be a symbolic link to <i>/var/log</i>.</p>
<dt><i>/var/backups</i></p>
<dd>Reserved for historical reasons.</p>
<dt><i>/var/cache</i></p>
<dd>Data cached for programs.</p>
<dt><i>/var/cache/fonts</i></p>
<dd>Locally generated fonts (optional).</p>
<dt><i>/var/cache/man</i></p>
<dd>Locally formatted man pages (optional).</p>
<dt><i>/var/cache/www</i></p>
<dd>WWW proxy or cache data (optional).</p>
<dt><i>/var/cache/&lt;package&gt;</i></p>
<dd>Package specific cache data (optional).</p>
<dt><i>/var/catman/cat[1-9]</i> or <i>/var/cache/man/cat[1-9]</i></p>
<dd>These directories contain preformatted manual pages according to their man page section. (The use of preformatted manual pages is deprecated.)</p>
<dt><i>/var/crash</i></p>
<dd>System crash dumps (optional).</p>
<dt><i>/var/cron</i></p>
<dd>Reserved for historical reasons.</p>
<dt><i>/var/games</i></p>
<dd>Variable game data (optional).</p>
<dt><i>/var/lib</i></p>
<dd>Variable state information for programs.</p>
<dt><i>/var/lib/color</i></p>
<dd>Variable files containing color management information (optional).</p>
<dt><i>/var/lib/hwclock</i></p>
<dd>State directory for hwclock (optional).</p>
<dt><i>/var/lib/misc</i></p>
<dd>Miscellaneous state data.</p>
<dt><i>/var/lib/xdm</i></p>
<dd>X display manager variable data (optional).</p>
<dt><i>/var/lib/&lt;editor&gt;</i></p>
<dd>Editor backup files and state (optional).</p>
<dt><i>/var/lib/&lt;name&gt;</i></p>
<dd>These directories must be used for all distribution packaging support.</p>
<dt><i>/var/lib/&lt;package&gt;</i></p>
<dd>State data for packages and subsystems (optional).</p>
<dt><i>/var/lib/&lt;pkgtool&gt;</i></p>
<dd>Packaging support files (optional).</p>
<dt><i>/var/local</i></p>
<dd>Variable data for <i>/usr/local</i>.</p>
<dt><i>/var/lock</i></p>
<dd>Lock files are placed in this directory. The naming convention for device lock files is <i>LCK..&lt;device&gt;</i> where <i>&lt;device&gt;</i> is the device&#8217;s name in the filesystem. The format used is that of HDU UUCP lock files, that is, lock files contain a PID as a 10-byte ASCII decimal number, followed by a newline character.</p>
<dt><i>/var/log</i></p>
<dd>Miscellaneous log files.</p>
<dt><i>/var/opt</i></p>
<dd>Variable data for <i>/opt</i>.</p>
<dt><i>/var/mail</i></p>
<dd>Users&#8217; mailboxes. Replaces <i>/var/spool/mail</i>.</p>
<dt><i>/var/msgs</i></p>
<dd>Reserved for historical reasons.</p>
<dt><i>/var/preserve</i></p>
<dd>Reserved for historical reasons.</p>
<dt><i>/var/run</i></p>
<dd>Run-time variable files, like files holding process identifiers (PIDs) and logged user information <i>(utmp)</i>. Files in this directory are usually cleared when the system boots.</p>
<dt><i>/var/spool</i></p>
<dd>Spooled (or queued) files for various programs.</p>
<dt><i>/var/spool/at</i></p>
<dd>Spooled jobs for <code><a href="/docs/linux/man/1-at/">at</a></code>(1).</p>
<dt><i>/var/spool/cron</i></p>
<dd>Spooled jobs for <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8).</p>
<dt><i>/var/spool/lpd</i></p>
<dd>Spooled files for printing (optional).</p>
<dt><i>/var/spool/lpd/printer</i></p>
<dd>Spools for a specific printer (optional).</p>
<dt><i>/var/spool/mail</i></p>
<dd>Replaced by <i>/var/mail</i>.</p>
<dt><i>/var/spool/mqueue</i></p>
<dd>Queued outgoing mail (optional).</p>
<dt><i>/var/spool/news</i></p>
<dd>Spool directory for news (optional).</p>
<dt><i>/var/spool/rwho</i></p>
<dd>Spooled files for <code><a href="/docs/linux/man/8-rwhod/">rwhod</a></code>(8) (optional).</p>
<dt><i>/var/spool/smail</i></p>
<dd>Spooled files for the <code><a href="/docs/linux/man/1-smail/">smail</a></code>(1) mail delivery program.</p>
<dt><i>/var/spool/uucp</i></p>
<dd>Spooled files for <code><a href="/docs/linux/man/1-uucp/">uucp</a></code>(1) (optional).</p>
<dt><i>/var/tmp</i></p>
<dd>Like <i>/tmp</i>, this directory holds temporary files stored for an unspecified duration.</p>
<dt><i>/var/yp</i></p>
<dd>Database files for NIS, formerly known as the Sun Yellow Pages (YP).</dl>
<h2>Conforming To</h2>
<p>The Filesystem Hierarchy Standard (FHS), Version 3.0, published March 19, 2015</p>
<h2>Bugs</h2>
<p>This list is not exhaustive; different distributions and systems may be configured differently.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-ln/">ln</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-file-hierarchy/">file-hierarchy</a></code>(7), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
<p> The Filesystem Hierarchy Standard</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
