---
title: "ntfs-3g(8)"
name: "ntfs-3g"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfs-3g/"
description: "ntfs-3g – Third Generation Read/Write NTFS Driver"
---

<p>ntfs-3g &#8211; Third Generation Read/Write NTFS Driver</p>
<h2>Synopsis</h2>
<p><code>ntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br/>
 <code>mount -t ntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br/>
 <code>lowntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i><br/>
 <code>mount -t lowntfs-3g</code> <code>[-o </code><i>option</i><code>[,&#8230;]]</code> <i>volume mount_point</i></p>
<h2>Description</h2>
<p><code>ntfs-3g</code> is an NTFS driver, which can create, remove, rename, move files, directories, hard links, and streams; it can read and write files, including streams, sparse files and transparently compressed files; it can handle special files like symbolic links, devices, and FIFOs; moreover it provides standard management of file ownership and permissions, including POSIX ACLs. </p>
<p> It comes in two variants <code>ntfs-3g</code> and <code>lowntfs-3g</code> with a few differences mentioned below in relevant options descriptions. </p>
<p> The <i>volume</i> to be mounted can be either a block device or an image file, either by using the mount command or starting the drive.</p>
<h3>Windows hibernation and fast restarting</h3>
<p>On computers which can be dual-booted into Windows or Linux, Windows has to be fully shut down before booting into Linux, otherwise the NTFS file systems on internal disks may be left in an inconsistent state and changes made by Linux may be ignored by Windows. </p>
<p> So, Windows may not be left in hibernation when starting Linux, in order to avoid inconsistencies. Moreover, the fast restart feature available on recent Windows systems has to be disabled. This can be achieved by issuing as an Administrator the Windows command which disables both hibernation and fast restarting :</p>
<dl>
<dd>powercfg /h off </dd>
</dl>
<p> If either Windows is hibernated or its fast restart is enabled, partitions on internal disks are forced to be mounted in read-only mode.</p>
<h3>Access Handling and Security</h3>
<p>By default, files and directories are owned by the effective user and group of the mounting process, and everybody has full read, write, execution and directory browsing permissions. You can also assign permissions to a single user by using the <code>uid</code> and/or the <code>gid </code> options together with the <code>umask,</code> or <code>fmask</code> and <code>dmask</code> options. </p>
<p> Doing so, all Windows users have full access to the files created by <code>ntfs-3g.</code> </p>
<p> But, by setting the <code>permissions</code> option, you can benefit from the full ownership and permissions features as defined by POSIX. Moreover, by defining a Windows-to-Linux user mapping, the ownerships and permissions are even applied to Windows users and conversely. </p>
<p> If <code>ntfs-3g </code> is set setuid-root then non-root users will be also able to mount volumes.</p>
<h3>Windows Filename Compatibility</h3>
<p>NTFS supports several filename namespaces: DOS, Win32 and POSIX. While the <code>ntfs-3g</code> driver handles all of them, it always creates new files in the POSIX namespace for maximum portability and interoperability reasons. This means that filenames are case sensitive and all characters are allowed except &#8216;/&#8217; and &#8216;\0&#8217;. This is perfectly legal on Windows, though some application may get confused. The option <code>windows_names</code> may be used to apply Windows restrictions to new file names.  </p>
<h3>Alternate Data Streams (ADS)</h3>
<p> NTFS stores all data in streams. Every file has exactly one unnamed data stream and can have many named data streams. The size of a file is the size of its unnamed data stream. By default, <code>ntfs-3g</code> will only read the unnamed data stream. </p>
<p> By using the option <code>streams_interface=windows</code>, with the ntfs-3g driver (not possible with lowntfs-3g), you will be able to read any named data streams, simply by specifying the stream name after a colon. For example: </p>
<dl>
<dd> <p> cat some.mp3:artist </p>
 </dd></dl>
<p> Named data streams act like normal files, so you can read from them, write to them and even delete them (using rm). You can list all the named data streams a file has by getting the <code>ntfs.streams.list</code> extended attribute.  </p>
<h2>OPTIONS</h2>
<p> Below is a summary of the options that <code>ntfs-3g</code> accepts. </p>
<dl>
<dt><code>acl</code></dt>
<dd> <p> Enable setting Posix ACLs on created files and use them for access control. This option is only available on specific builds. It is set by default when a user mapping file is present and the <code>permissions</code> mount option is not set. </p>
 </dd>
<dt><code>allow_other</code></dt>
<dd> <p> This option overrides the security measure restricting file access to the user mounting the filesystem. This option is only allowed to root, but this restriction can be overridden by the <code>user_allow_other</code> option in the /etc/fuse.conf file. </p>
 </dd>
<dt><code>atime, noatime, relatime</code></dt>
<dd> <p> The <code>atime </code> option updates inode access time for each access. </p>
<p> The <code>noatime </code> option disables inode access time updates, which can speed up file operations and prevent sleeping (notebook) disks spinning up too often thus saving energy and disk lifetime. </p>
<p> The <code>relatime </code> option is very similar to <code>noatime. </code> It updates inode access times relative to modify or change time. The access time is only updated if the previous access time was earlier than the current modify or change time. Unlike <code>noatime</code> this option doesn&#8217;t break applications that need to know if a file has been read since the last time it was modified. This is the default behaviour. </p>
 </dd>
<dt><code>big_writes</code></dt>
<dd> <p> This option prevents fuse from splitting write buffers into 4K chunks, enabling big write buffers to be transferred from the application in a single step (up to some system limit, generally 128K bytes). </p>
 </dd>
<dt><code>compression</code></dt>
<dd> <p> This option enables creating new transparently compressed files in directories marked for compression. A directory is marked for compression by setting the bit 11 (value 0x00000800) in its Windows attribute. In such a directory, new files are created compressed and new subdirectories are themselves marked for compression. The option and the flag have no effect on existing files. Currently this is the default option. </p>
 </dd>
<dt><code>debug</code></dt>
<dd> <p> Makes ntfs-3g (or lowntfs-3g) to print a lot of debug output from libntfs-3g and FUSE. </p>
 </dd>
<dt><code>delay_mtime[= value]</code></dt>
<dd> <p> Only update the file modification time and the file change time of a file when it is closed or when the indicated delay since the previous update has elapsed. The argument is a number of seconds, with a default value of 60. This is mainly useful for big files which are kept open for a long time and written to without changing their size, such as databases or file system images mounted as loop. </p>
 </dd>
<dt><code>dmask=</code><i>value</i></dt>
<dd> <p> Set the bitmask of the directory permissions that are not present. The value is given in octal. The default value is 0 which means full access to everybody. </p>
 </dd>
<dt><code>efs_raw</code></dt>
<dd> <p> This option should only be used in backup or restore situation. It changes the apparent size of files and the behavior of read and write operation so that encrypted files can be saved and restored without being decrypted. The <code>user.ntfs.efsinfo</code> extended attribute has also to be saved and restored for the file to be decrypted. </p>
 </dd>
<dt><code>fmask=</code><i>value</i></dt>
<dd> <p> Set the bitmask of the file permissions that are not present. The value is given in octal. The default value is 0 which means full access to everybody. </p>
 </dd>
<dt><code>force</code></dt>
<dd> <p> This option is obsolete. It has been superseded by the <code>recover</code> and <code>norecover</code> options. </p>
 </dd>
<dt><code>hide_dot_files</code></dt>
<dd> <p> Set the hidden flag in the NTFS attribute for created files and directories whose first character of the name is a dot. Such files and directories normally do not appear in directory listings, and when the flag is set they do not appear in Windows directory displays either. When a file is renamed or linked with a new name, the hidden flag is adjusted to the latest name. </p>
 </dd>
<dt><code>hide_hid_files</code></dt>
<dd> <p> Hide the hidden files and directories in directory listings, the hidden files and directories being the ones whose NTFS attribute have the hidden flag set. The hidden files will not be selected when using wildcards in commands, but all files and directories remain accessible by full name, for example you can always display the Windows trash bin directory by : &quot;ls -ld &#8216;$RECYCLE.BIN&#8217;&quot;. </p>
 </dd>
<dt><code>ignore_case </code>(only with lowntfs-3g) </dt>
<dd> <p> Ignore character case when accessing a file (<code>FOO</code>, <code>Foo</code>, <code>foo</code>, etc. designate the same file). All files are displayed with lower case in directory listings. </p>
 </dd>
<dt><code>inherit</code></dt>
<dd> <p> When creating a new file, set its initial protections according to inheritance rules defined in parent directory. These rules deviate from Posix specifications, but yield a better Windows compatibility. The <code>permissions</code> (or **acl**) option or a valid user mapping file is required for this option to be effective. </p>
 </dd>
<dt><code>locale=</code><i>value</i></dt>
<dd> <p> This option can be useful when wanting a language specific locale environment. It is however discouraged as it leads to files with untranslatable characters to not be visible. </p>
 </dd>
<dt><code>max_read=</code><i>value</i></dt>
<dd> <p> With this option the maximum size of read operations can be set. The default is infinite. Note that the size of read requests is limited anyway by the system (usually to 128kbyte). </p>
 </dd>
<dt><code>no_def_opts</code></dt>
<dd> <p> By default ntfs-3g acts as if <code>silent</code> (ignore permission errors when permissions are not enabled), <code>allow_other</code> (allow any user to access files) and <code>nonempty</code> (allow mounting on non-empty directories) were set, and <code>no_def_opts</code> cancels these default options. </p>
 </dd>
<dt><code>no_detach</code></dt>
<dd> <p> Makes ntfs-3g to not detach from terminal and print some debug output. </p>
 </dd>
<dt><code>nocompression</code></dt>
<dd> <p> This option disables creating new transparently compressed files in directories marked for compression. Existing compressed files can still be read and updated. </p>
 </dd>
<dt><code>norecover</code></dt>
<dd> <p> Do not try to mount a partition which was not unmounted properly by Windows. </p>
 </dd>
<dt><code>permissions</code></dt>
<dd> <p> Set standard permissions on created files and use standard access control. This option is set by default when a user mapping file is present. </p>
 </dd>
<dt><code>posix_nlink</code></dt>
<dd> <p> Compute the count of hard links of a file or directory according to the POSIX specifications. When this option is not set, a count of 1 is set for directories, and the short name of files is accounted for. Using the option entails some penalty as the count is not stored and has to be computed. </p>
 </dd>
<dt><code>recover</code></dt>
<dd> <p> Recover and try to mount a partition which was not unmounted properly by Windows. The Windows logfile is cleared, which may cause inconsistencies. Currently this is the default option. </p>
 </dd>
<dt><code>remove_hiberfile</code></dt>
<dd> <p> When the NTFS volume is hibernated, a read-write mount is denied and a read-only mount is forced. One needs either to resume Windows and shutdown it properly, or use this option which will remove the Windows hibernation file. Please note, this means that the saved Windows session will be completely lost. Use this option under your own responsibility. </p>
 </dd>
<dt><code>ro</code></dt>
<dd> <p> Mount the filesystem read-only. Useful if Windows is hibernated or the NTFS journal file is unclean. </p>
 </dd>
<dt><code>show_sys_files</code></dt>
<dd> <p> Show the metafiles in directory listings. Otherwise the default behaviour is to hide the metafiles, which are special files used to store the NTFS structure. Please note that even when this option is specified, &quot;$MFT&quot; may not be visible due to a glibc bug. Furthermore, irrespectively of <code>show_sys_files</code>, all files are accessible by name, for example you can always do &quot;ls -l &#8216;$UpCase&#8217;&quot;. </p>
 </dd>
<dt><code>silent</code></dt>
<dd> <p> Do nothing, without returning any error, on chmod and chown operations and on permission checking errors, when the <code>permissions</code> option is not set and no user mapping file is defined. This option is on by default, and when set off (through option <code>no_def_opts</code>) ownership and permissions parameters have to be set. </p>
 </dd>
<dt><code>special_files=</code><i>mode</i></dt>
<dd> <p> This option selects a mode for representing a special file to be created (symbolic link, socket, fifo, character or block device). The <i>mode</i> can be <code>interix</code> or <code>wsl</code>, and existing files in either mode are recognized irrespective of the selected mode. Interix is the traditional mode, used by default, and wsl is interoperable with Windows WSL, but it is not compatible with Windows versions earlier than Windows 10. Neither mode are interoperable with Windows. </p>
 </dd>
<dt><code>streams_interface=</code><i>mode</i></dt>
<dd> <p> This option controls how the user can access Alternate Data Streams (ADS) or in other words, named data streams. The <i>mode</i> can be set to one of <code>none</code>, <code>windows</code> or <code>xattr</code>. If the option is set to <code>none</code>, the user will have no access to the named data streams. If it is set to <code>windows</code> (not possible with lowntfs-3g), then the user can access them just like in Windows (eg. cat file:stream). If it&#8217;s set to <code>xattr</code>, then the named data streams are mapped to extended attributes and a user can manipulate them using <code>{get,set}fattr</code> utilities. The default is <code>xattr</code>. </p>
 </dd>
<dt><code>uid=</code><i>value</i> and <code>gid=</code><i>value</i></dt>
<dd> <p> Set the owner and the group of files and directories. The values are numerical. The defaults are the uid and gid of the current process. </p>
 </dd>
<dt><code>umask=</code><i>value</i></dt>
<dd> <p> Set the bitmask of the file and directory permissions that are not present. The value is given in octal. The default value is 0 which means full access to everybody. </p>
 </dd>
<dt><code>usermapping=</code><i>file-name</i></dt>
<dd> <p> Use file <i>file-name</i> as the user mapping file instead of the default <code>.NTFS-3G/UserMapping</code>. If <i>file-name</i> defines a full path, the file must be located on a partition previously mounted. If it defines a relative path, it is interpreted relative to the root of NTFS partition being mounted. </p>
 </dd></dl>
<dl>
<dd> <p> When a user mapping file is defined, the options <code>uid=</code>, <code>gid=</code>, <code>umask=</code>, <code>fmask=</code>, <code>dmask=</code> and <code>silent</code> are ignored. </p>
 </dd></dl>
<dl>
<dt><code>user_xattr</code></dt>
<dd> <p> Same as <code>streams_interface=</code><i>xattr</i>. </p>
 </dd>
<dt><code>windows_names</code></dt>
<dd> <p> This option prevents files, directories and extended attributes to be created with a name not allowed by windows, because </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> &#8211; it contains some not allowed character, <br/>
 &#8211; or the last character is a space or a dot, <br/>
 &#8211; or the name is reserved. </p>
 </dd></dl>
<p> The forbidden characters are the nine characters &quot; * / : &lt; &gt; ? \ | and those whose code is less than 0x20, and the reserved names are CON, PRN, AUX, NUL, COM1..COM9, LPT1..LPT9, with no suffix or followed by a dot. </p>
<p> Existing such files can still be read (and renamed). </dl>
 </dl>
  </p>
<h2>USER MAPPING</h2>
<p> NTFS uses specific ids to record the ownership of files instead of the <code>uid</code> (user id) and <code>gid</code> (group id) used by Linux. As a consequence a mapping between the ids has to be defined for ownerships to be recorded into NTFS files and recognized. </p>
<p> By default, this mapping is fetched from the file <code>.NTFS-3G/UserMapping</code> located in the NTFS partition. The option <code>usermapping=</code> may be used to define another location. When the option **permissions** is set and no mapping file is found, a default mapping is used. </p>
<p> Each line in the user mapping file defines a mapping. It is organized in three fields separated by colons. The first field identifies a <code>uid</code>, the second field identifies a <code>gid</code> and the third one identifies the corresponding NTFS id, known as a <code>SID</code>. The <code>uid</code> and the <code>gid</code> are optional and defining both of them for the same <code>SID</code> is not recommended. </p>
<p> If no interoperation with Windows is needed, you can use the option <code>permissions</code> to define a standard mapping. Alternately, you may define your own mapping by setting a single default mapping with no uid and gid. In both cases, files created on Linux will appear to Windows as owned by a foreign user, and files created on Windows will appear to Linux as owned by root. Just copy the example below and replace the 9 and 10-digit numbers by any number not greater than 4294967295. The resulting behavior is the same as the one with the option <code>permission</code> set with no ownership option and no user mapping file available. </p>
<dl>
<dd> <p> <code>::S-1-5-21-3141592653-589793238-462643383-10000</code> </p>
 </dd></dl>
<p> If a strong interoperation with Windows is needed, the mapping has to be defined for each user and group known to both system, and the <code>SID</code>s used by Windows has to be collected. This will lead to a user mapping file like : </p>
<dl>
<dd> <p> <code>john::S-1-5-21-3141592653-589793238-462643383-1008</code> <code>mary::S-1-5-21-3141592653-589793238-462643383-1009</code> <code>:smith:S-1-5-21-3141592653-589793238-462643383-513</code> <code>::S-1-5-21-3141592653-589793238-462643383-10000</code> </p>
 </dd></dl>
<p> The utility <code>ntfsusermap</code> may be used to create such a user mapping file.  </p>
<h2>EXAMPLES</h2>
<p> Mount /dev/sda1 to /mnt/windows: </p>
<dl>
<dd> <p> <code>ntfs-3g /dev/sda1 /mnt/windows</code> </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> <code>mount -t ntfs-3g /dev/sda1 /mnt/windows</code> </p>
 </dd></dl>
<p> Mount the ntfs data partition /dev/sda3 to /mnt/data with standard Linux permissions applied : </p>
<dl>
<dd> <p> <code>ntfs-3g -o permissions /dev/sda3 /mnt/data</code> </p>
 </dd></dl>
<p> or </p>
<dl>
<dd> <p> <code>mount -t ntfs-3g -o permissions /dev/sda3 /mnt/data</code> </p>
 </dd></dl>
<p> Read-only mount /dev/sda5 to /home/user/mnt and make user with uid 1000 to be the owner of all files: </p>
<dl>
<dd> <p> <code>ntfs-3g /dev/sda5 /home/user/mnt -o ro,uid=1000</code> </p>
 </dd></dl>
<p> /etc/fstab entry for the above (the sixth and last field has to be zero to avoid a file system check at boot time) : </p>
<dl>
<dd> <p> <code>/dev/sda5 /home/user/mnt ntfs-3g ro,uid=1000 0 0</code> </p>
 </dd></dl>
<p> Unmount /mnt/windows: </p>
<dl>
<dd> <p> <code>umount /mnt/windows</code> </p>
 </dd></dl>
<h2>EXIT CODES</h2>
<p> To facilitate the use of the <code>ntfs-3g</code> driver in scripts, an exit code is returned to give an indication of the mountability status of a volume. Value 0 means success, and all other ones mean an error. The unique error codes are documented in the <code><a href="/docs/linux/man/8-ntfs-3g.probe/">ntfs-3g.probe</a></code>(8) manual page.  </p>
<h2>KNOWN ISSUES</h2>
<p> Please see </p>
<dl>
<dd> <p> <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ">https://github.com/tuxera/ntfs-3g/wiki/NTFS-3G-FAQ</a> </p>
 </dd></dl>
<p> for common questions and known issues. If you would find a new one in the latest release of the software then please post an ntfs-3g issue describing it in detail so that the development team can be aware of the issue and take care of it: </p>
<dl>
<dd> <p> <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/issues">https://github.com/tuxera/ntfs-3g/issues</a> </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> <code>ntfs-3g </code> was based on and a major improvement to ntfsmount and libntfs which were written by Yura Pakhuchiy and the Linux-NTFS team. The improvements were made, the ntfs-3g project was initiated and currently led by long time Linux-NTFS team developer Szabolcs Szakacsits (szaka [at] tuxera.com).  </p>
<h2>THANKS</h2>
<p> Several people made heroic efforts, often over five or more years which resulted the ntfs-3g driver. Most importantly they are Anton Altaparmakov, Jean-Pierre André, Erik Larsson, Richard Russon, Szabolcs Szakacsits, Yura Pakhuchiy, Yuval Fledel, and the author of the groundbreaking FUSE filesystem development framework, Miklos Szeredi.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ntfs-3g.probe/">ntfs-3g.probe</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8), <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5), <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1) </p>
