---
title: "encfs(1)"
name: "encfs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-encfs/"
description: "encfs – mounts or creates an encrypted virtual filesystem"
---

<h2 class="name">NAME</h2>
<p> encfs &#8211; mounts or creates an encrypted virtual filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>encfs</code> [<code>&#8211;version</code>] [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-c</code>|<code>&#8211;config</code>] [<code>-t</code>|<code>&#8211;syslogtag</code>] [<code>-s</code>] [<code>-f</code>] [<code>&#8211;annotate</code>] [<code>&#8211;standard</code>] [<code>&#8211;paranoia</code>] [<code>&#8211;insecure</code>] [<code>&#8211;reverse</code>] [<code>&#8211;reversewrite</code>] [<code>&#8211;extpass=program</code>] [<code>-S</code>|<code>&#8211;stdinpass</code>] [<code>&#8211;anykey</code>] [<code>&#8211;forcedecode</code>] [<code>-require-macs</code>] [<code>-i </code><font SIZE="-1"><code>MINUTES</code></font>|<code>&#8211;idle=MINUTES</code>] [<code>-m</code>|<code>&#8211;ondemand</code>] [<code>&#8211;delaymount</code>] [<code>-u</code>|<code>&#8211;unmount</code>] [<code>&#8211;public</code>] [<code>&#8211;nocache</code>] [<code>&#8211;noattrcache</code>] [<code>&#8211;nodatacache</code>] [<code>&#8211;no-default-flags</code>] [<code>-o </code><font SIZE="-1"><code>FUSE_OPTION</code></font>] [<code>-d</code>|<code>&#8211;fuse-debug</code>] [<code>-H</code>|<code>&#8211;fuse-help</code>] <i>rootdir</i> <i>mountPoint</i> [<code>&#8212;</code> [<i>Fuse Mount Options</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>EncFS</code> creates a virtual encrypted filesystem which stores encrypted data in the <i>rootdir</i> directory and makes the unencrypted data visible at the <i>mountPoint</i> directory. The user must supply a password which is used to (indirectly) encrypt both filenames and file contents. </p>
<p> If <code>EncFS</code> is unable to find a supported filesystem at the specified <i>rootdir</i>, then the user will be asked if they wish to create a new encrypted filesystem at the specified location. Options will be presented to the user allowing some control over the algorithms to use. As <code>EncFS</code> matures, there may be an increasing number of choices.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Shows <code>EncFS</code> version. Using <code>&#8211;verbose</code> before <code>&#8211;version</code> may display additional information.</p>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd> Causes <code>EncFS</code> to use the supplied file as the configuration file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Causes <code>EncFS</code> to enable logging of various debug channels within <code>EncFS</code>. Normally these logging messages are disabled and have no effect. It is recommended that you run in foreground (<code>-f</code>) mode when running with verbose enabled.</p>
<dt><code>-t</code>, <code>&#8211;syslogtag</code></p>
<dd> This option allows to set the syslog tag which will be used when messages are logged via syslog. By default the syslog tag is set to <code>encfs</code>.</p>
<dt><code>-s</code></p>
<dd> The <code>-s</code> (<i>single threaded</i>) option causes <code>EncFS</code> to run in single threaded mode. By default, <code>EncFS</code> runs in multi-threaded mode. This option is used during <code>EncFS</code> development in order to simplify debugging and allow it to run under memory checking tools.</p>
<dt><code>-f</code></p>
<dd> The <code>-f</code> (<i>foreground</i>) option causes <code>EncFS</code> to run in the foreground. Normally <code>EncFS</code> spawns off as a daemon and runs in the background, returning control to the spawning shell. With the <code>-f</code> option, it will run in the foreground and any warning/debug log messages will be displayed on standard error. In the default (background) mode, all log messages are logged via syslog.</p>
<dt><code>&#8211;annotate</code></p>
<dd> Print annotation lines to stderr during configuration.</p>
<dt><code>&#8211;standard</code></p>
<dd> If creating a new filesystem, this automatically selects standard configuration options, to help with automatic filesystem creation. This is the set of options that should be used unless you know what you&#8217;re doing and have read the documentation. </p>
<p> When not creating a filesystem, this flag does nothing.</p>
<dt><code>&#8211;paranoia</code></p>
<dd> Same as <code>&#8211;standard</code>, but for <code>paranoia</code> mode.</p>
<dt><code>&#8211;insecure</code></p>
<dd> Allows you to disable data encoding, thus to pass plain data as is. Fully discouraged of course!</p>
<dt><code>&#8211;reverse</code></p>
<dd> Normally <code>EncFS</code> provides a plaintext view of data on demand: it stores enciphered data and displays plaintext data. With <code>&#8211;reverse</code> it takes as source plaintext data and produces enciphered data on-demand. This can be useful for creating remote encrypted backups, where you do not wish to keep the local files unencrypted. </p>
<p> For example, the following would create an encrypted view in /tmp/crypt-view. </p>
<pre>
    encfs --reverse /home/me /tmp/crypt-view
</pre>
<p> You could then copy the /tmp/crypt-view directory in order to have a copy of the encrypted data. You must also keep a copy of the file /home/me/.encfs6.xml which contains the filesystem information. Together, the two can be used to reproduce the unencrypted data: </p>
<pre>
    ENCFS6_CONFIG=/home/me/.encfs6.xml encfs /tmp/crypt-view /tmp/plain-view
</pre>
<p> Now /tmp/plain-view contains the same data as /home/me </p>
<p> Note that <code>&#8211;reverse</code> mode only works with limited configuration options, so many settings may be disabled when used. Incompatible options as for now : Filename Initialization Vector Chaining and External <font SIZE="-1">IV</font> Chaining.</p>
<dt><code>&#8211;reversewrite</code></p>
<dd> Same as <code>&#8211;reverse</code> but will allow writes, if possible (configuration must have UniqueIV disabled). Incompatible option : Per-File Initialization Vectors.</p>
<dt><code>&#8211;extpass=program</code></p>
<dd> Specify an external program to use for getting the user password. When the external program is spawned, the environment variable &#8220;RootDir&#8221; will be set to contain the path to the root directory. The program should print the password to standard output. </p>
<p> <code>EncFS</code> takes everything returned from the program to be the password, except for a trailing newline (
) which will be removed. </p>
<p> For example, specifying <code>&#8211;extpass</code>=<i>/usr/lib/ssh/ssh-askpass</i> will cause <code>EncFS</code> to use ssh&#8217;s password prompt program. </p>
<p> <code>Note</code>: <code>EncFS</code> reads at most 2k of data from the password program, and it removes any trailing newline. Versions before 1.4.x accepted only 64 bytes of text.</p>
<dt><code>-S</code>, <code>&#8211;stdinpass</code></p>
<dd> Read password from standard input, without prompting. This may be useful for scripting encfs mounts. </p>
<p> Note that you should make sure the filesystem and mount points exist first. Otherwise encfs will prompt for the filesystem creation options, which may interfere with your script.</p>
<dt><code>&#8211;anykey</code></p>
<dd> Turn off key validation checking. This allows <code>EncFS</code> to be used with secondary passwords. This could be used to store a separate set of files in an encrypted filesystem. <code>EncFS</code> ignores files which do not decode properly, so files created with separate passwords will only be visible when the filesystem is mounted with their associated password. </p>
<p> Note that if the primary password is changed (using <code>encfsctl</code>), the other passwords will not be usable unless the primary password is set back to what it was, as the other passwords rely on an invalid decoding of the volume key, which will not remain the same if the primary password is changed. </p>
<p> <code>Warning</code>: Use this option at your own risk.</p>
<dt><code>&#8211;forcedecode</code></p>
<dd> This option only has an effect on filesystems which use <font SIZE="-1">MAC</font> block headers. By default, if a block is decoded and the stored <font SIZE="-1">MAC</font> doesn&#8217;t match what is calculated, then an <font SIZE="-1">IO</font> error is returned to the application and the block is not returned. However, by specifying <code>&#8211;forcedecode</code>, only an error will be logged and the data will still be returned to the application. This may be useful for attempting to read corrupted files.</p>
<dt><code>&#8211;require-macs</code></p>
<dd> If creating a new filesystem, this forces block authentication code headers to be enabled. When mounting an existing filesystem, this causes encfs to exit if block authentication code headers are not enabled. </p>
<p> This can be used to improve security in case the ciphertext is vulnerable to tampering, by preventing an attacker from disabling MACs in the config file.</p>
<dt><code>-i</code>, <code>&#8211;idle=MINUTES</code></p>
<dd> Enable automatic unmount of the filesystem after a period of inactivity. The period is specified in minutes, so the shortest timeout period that can be requested is one minute. <code>EncFS</code> will not automatically unmount if there are files open within the filesystem, even if they are open in read-only mode. However simply having files open does not count as activity.</p>
<dt><code>-m</code>, <code>&#8211;ondemand</code></p>
<dd> Mount the filesystem on-demand. This currently only makes sense in combination with <code>&#8211;idle</code> and <code>&#8211;extpass</code> options. When the filesystem becomes idle, instead of exiting, <code>EncFS</code> stops allowing access to the filesystem by internally dropping its reference to it. If someone attempts to access the filesystem again, the extpass program is used to prompt the user for the password. If this succeeds, then the filesystem becomes available again.</p>
<dt><code>&#8211;delaymount</code></p>
<dd> Do not mount the filesystem when encfs starts; instead, delay mounting until first use. This option only makes sense with <code>&#8211;ondemand</code>.</p>
<dt><code>-u</code>, <code>&#8211;unmount</code></p>
<dd> Unmounts the specified <i>mountPoint</i>.</p>
<dt><code>&#8211;public</code></p>
<dd> Attempt to make encfs behave as a typical multi-user filesystem. By default, all <font SIZE="-1">FUSE</font> based filesystems are visible only to the user who mounted them. No other users (including root) can view the filesystem contents. The <code>&#8211;public</code> option does two things. It adds the <font SIZE="-1">FUSE</font> flags &#8220;allow_other&#8221; and &#8220;default_permission&#8221; when mounting the filesystem, which tells <font SIZE="-1">FUSE</font> to allow other users to access the filesystem, and to use the ownership permissions provided by the filesystem. Secondly, the <code>&#8211;public</code> flag changes how encfs&#8217;s node creation functions work &#8211; as they will try and set ownership of new nodes based on the caller identification. </p>
<p> <code>Warning</code>: In order for this to work, encfs must be run as root &#8212; otherwise it will not have the ability to change ownership of files. I recommend that you instead investigate if the fuse allow_other option can be used to do what you want before considering the use of <code>&#8211;public</code>.</p>
<dt><code>&#8211;nocache</code></p>
<dd> Disable the kernel&#8217;s cache of file attributes. Setting this option makes EncFS pass &#8220;attr_timeout=0&#8221; and &#8220;entry_timeout=0&#8221; to <font SIZE="-1">FUSE.</font> This makes sure that modifications to the backing file attributes that occour outside EncFS show up immediately in the EncFS mount. The internal EncFS data cache is also disabled. The main use case for <code>&#8211;nocache</code> is reverse mode.</p>
<dt><code>&#8211;noattrcache</code></p>
<dd> Same as <code>&#8211;nocache</code> but for attributes only.</p>
<dt><code>&#8211;nodatacache</code></p>
<dd> Same as <code>&#8211;nocache</code> but for data only.</p>
<dt><code>&#8211;no-default-flags</code></p>
<dd> <code>Encfs</code> adds the <font SIZE="-1">FUSE</font> flags &#8220;use_ino&#8221; and &#8220;default_permissions&#8221; by default, as of version 1.2.2, because that improves compatibility with some programs. If for some reason you need to disable one or both of these flags, use the option <code>&#8211;no-default-flags</code>. </p>
<p> The following command lines produce the same result: </p>
<pre>
    encfs raw crypt
    encfs --no-default-flags raw crypt -- -o use_ino,default_permissions
</pre>
<dt><code>-o </code><font SIZE="-1"><code>FUSE_ARG</code></font></p>
<dd> Pass through <font SIZE="-1"><code>FUSE</code></font> args to the underlying library. This makes it easy to pass <font SIZE="-1">FUSE</font> options when mounting <code>EncFS</code> via mount (and /etc/fstab). Eg: </p>
<pre>
    mount encfs#/home/me-crypt /home/me -t fuse -o kernel_cache
</pre>
<p> Note that encfs arguments cannot be set this way. If you need to set encfs arguments, create a wrapper, such as encfs-reverse; </p>
<pre>
    #!/bin/sh
    encfs --reverse &quot;$@&quot;
</pre>
<p> Then mount using the script path </p>
<pre>
    mount encfs-reverse#/home/me /home/me-crypt -t fuse
</pre>
<dt><code>-d</code>, <code>&#8211;fuse-debug</code></p>
<dd> Enables debugging within the <font SIZE="-1"><code>FUSE</code></font> library. This should only be used if you suspect a problem within <font SIZE="-1"><code>FUSE</code></font> itself (not <code>EncFS</code>), as it generates a lot of low-level data and is not likely to be very helpful in general problem tracking. Try <i>verbose</i> mode (<code>-v</code>) first, which gives a higher level view of what is happening within <code>EncFS</code>.</p>
<dt><code>-H</code>, <code>&#8211;fuse-help</code></p>
<dd> Shows <font SIZE="-1"><code>FUSE</code></font> help.</p>
<dt><code>&#8212;</code></p>
<dd> The <code>&#8212;</code> option tells <code>EncFS</code> to send any remaining arguments directly to <font SIZE="-1"><code>FUSE</code></font>. In turn, <font SIZE="-1"><code>FUSE</code></font> passes the arguments to <code>fusermount</code>. See the <code>fusermount</code> help page for information on available commands.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><font SIZE="-1"><code>ENCFS6_CONFIG</code></font></p>
<dd> Which config file (typically named .encfs6.xml) to use. By default, the config file is read from the encrypted directory. Using this option allows to store the config file separated from the encrypted files. </p>
<p> Warning: If you lose the config file, the encrypted file contents are irrecoverably lost. It contains the master key encrypted with your password. Without the master key, recovery is impossible, even if you know the password.</dl>
<h2>EXAMPLES</h2>
<p> Create a new encrypted filesystem. Store the raw (encrypted) data in &#8220;~/.crypt&#8221; , and make the unencrypted data visible in &#8220;~/crypt&#8221;. Both directories are in the home directory in this example. This example shows the full output of encfs as it asks the user if they wish to create the filesystem: </p>
<pre>
    % encfs ~/.crypt ~/crypt
    Directory &quot;/home/me/.crypt&quot; does not exist, create (y,n)?y
    Directory &quot;/home/me/crypt&quot; does not exist, create (y,n)?y
    Creating new encrypted volume.
    Please choose from one of the following options:
     enter &quot;x&quot; for expert configuration mode,
     enter &quot;p&quot; for pre-configured paranoia mode,
     anything else, or an empty line will select standard mode.
    ?&gt; 
    Standard configuration selected.
    Using cipher Blowfish, key size 160, block size 512
    New Password: &lt;password entered here&gt;
    Verify: &lt;password entered here&gt;
</pre>
<p> The filesystem is now mounted and visible in <i>~/crypt</i>. If files are created there, they can be seen in encrypted form in <i>~/.crypt</i>. To unmount the filesystem, use <i>fusermount</i> with the <code>-u</code> (unmount) option: </p>
<pre>
    % fusermount -u ~/crypt
</pre>
<p> Another example. To mount the same filesystem, but have fusermount name the mount point &#8216;/dev/foo&#8217; (as shown in <i>df</i> and other tools which read /etc/mtab), and also request kernel-level caching of file data (which are both special arguments to fusermount): </p>
<pre>
    % encfs ~/.crypt ~/crypt -- -n /dev/foo -c
</pre>
<p> Or, if you find strange behavior under some particular program when working in an encrypted filesystem, it may be helpful to run in verbose mode while reproducing the problem and send along the output with the problem report: </p>
<pre>
    % encfs -v -f ~/.crypt ~/crypt 2&gt; encfs-report.txt
</pre>
<p> In order to avoid leaking sensitive information through the debugging channels, all warnings and debug messages (as output in verbose mode) contain only encrypted filenames. You can use the <i>encfsctl</i> program&#8217;s <i>decode</i> function to decode filenames if desired.</p>
<h2>CAVEATS</h2>
<p> <code>EncFS</code> is not a true filesystem. It does not deal with any of the actual storage or maintenance of files. It simply translates requests (encrypting or decrypting as necessary) and passes the requests through to the underlying host filesystem. Therefore any limitations of the host filesystem will be inherited by <code>EncFS</code> (or possibly be further limited). </p>
<p> One such limitation is filename length. If your underlying filesystem limits you to N characters in a filename, then <code>EncFS</code> will limit you to approximately 3*(N-2)/4. For example if the host filesystem limits to 255 characters, then <code>EncFS</code> will be limited to 189 character filenames. This is because encrypted filenames are always longer than plaintext filenames.</p>
<h2>FILESYSTEM OPTIONS</h2>
<p> When <code>EncFS</code> is given a root directory which does not contain an existing <code>EncFS</code> filesystem, it will give the option to create one. Note that options can only be set at filesystem creation time. There is no support for modifying a filesystem&#8217;s options in-place. </p>
<p> If you want to upgrade a filesystem to use newer features, then you need to create a new filesystem and mount both the old filesystem and new filesystem at the same time and copy the old to the new. </p>
<p> Multiple instances of encfs can be run at the same time, including different versions of encfs, as long as they are compatible with the current <font SIZE="-1">FUSE</font> module on your system. </p>
<p> A choice is provided for two pre-configured settings (&#8216;standard&#8217; and &#8216;paranoia&#8217;), along with an expert configuration mode. </p>
<p> <i>Standard</i> mode uses the following settings:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Cipher:&nbsp;<font SIZE="-1">AES</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Key Size: 192 bits<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<font SIZE="-1">PBKDF2</font>&nbsp;with 1/2 second runtime, 160 bit salt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Filesystem Block Size: 1024 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Filename Encoding: Block encoding with&nbsp;<font SIZE="-1">IV</font>&nbsp;chaining<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Unique initialization vector file headers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File holes passed through </p>
<p> <i>Paranoia</i> mode uses the following settings:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Cipher:&nbsp;<font SIZE="-1">AES</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Key Size: 256 bits<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<font SIZE="-1">PBKDF2</font>&nbsp;with 3 second runtime, 160 bit salt<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Filesystem Block Size: 1024 bytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Filename Encoding: Block encoding with&nbsp;<font SIZE="-1">IV</font>&nbsp;chaining<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Unique initialization vector file headers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Message Authentication Code block headers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;External&nbsp;<font SIZE="-1">IV</font>&nbsp;Chaining<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File holes passed through </p>
<p> In the expert / manual configuration mode, each of the above options is configurable. Here is a list of current options with some notes about what they mean:</p>
<h2>Key Derivation Function</h2>
<p> As of version 1.5, <code>EncFS</code> now uses <font SIZE="-1">PBKDF2</font> as the default key derivation function. The number of iterations in the keying function is selected based on wall clock time to generate the key. In standard mode, a target time of 0.5 seconds is used, and in paranoia mode a target of 3.0 seconds is used. </p>
<p> On a 1.6Ghz <font SIZE="-1">AMD 64</font> system, roughly 64k iterations of the key derivation function can be handled in half a second. The exact number of iterations to use is stored in the configuration file, as it is needed to remount the filesystem. </p>
<p> If an <code>EncFS</code> filesystem configuration from 1.4.x is modified with version 1.5 (such as when using encfsctl to change the password), then the new <font SIZE="-1">PBKDF2</font> function will be used and the filesystem will no longer be readable by older versions.</p>
<dl>
<dt><i>Cipher</i></p>
<dd> Which encryption algorithm to use. The list is generated automatically based on what supported algorithms <code>EncFS</code> found in the encryption libraries. When using a recent version of <code>OpenSSL</code>, Blowfish and <font SIZE="-1">AES</font> are the typical options. </p>
<p> Blowfish is an 8 byte cipher &#8211; encoding 8 bytes at a time. <font SIZE="-1">AES</font> is a 16 byte cipher.</p>
<dt><i>Cipher Key Size</i></p>
<dd> Many, if not all, of the supported ciphers support multiple key lengths. There is not really much need to have enormous key lengths. Even 160 bits (the default) is probably overkill.</p>
<dt><i>Filesystem Block Size</i></p>
<dd> This is the size (in bytes) that <code>EncFS</code> deals with at one time. Each block gets its own initialization vector and is encoded in the cipher&#8217;s cipher-block-chaining mode. A partial block at the end of a file is encoded using a stream mode to avoid having to store the filesize somewhere. </p>
<p> Having larger block sizes reduces the overhead of <code>EncFS</code> a little, but it can also add overhead if your programs read small parts of files. In order to read a single byte from a file, the entire block that contains that byte must be read and decoded, so a large block size adds overhead to small requests. With write calls it is even worse, as a block must be read and decoded, the change applied and the block encoded and written back out. </p>
<p> The default is 512 bytes as of version 1.0. It was hard coded to 64 bytes in version 0.x, which was not as efficient as the current setting for general usage.</p>
<dt><i>Filename Encoding</i></p>
<dd> <code>New in 1.1</code>. A choice is given between stream encoding of filename and block encoding. The advantage of stream encoding is that the encoded filenames will be as short as possible. If you have a filename with a single letter, it will be very short in the encoded form, where as block encoded filenames are always rounded up to the block size of the encryption cipher (8 bytes for Blowfish and 16 bytes for <font SIZE="-1">AES</font>). </p>
<p> The advantage of block encoding mode is that filename lengths all come out as a multiple of the cipher block size. This means that someone looking at your encrypted data can&#8217;t tell as much about the length of your filenames. It is on by default, as it takes a similar amount of time to using the stream cipher. However stream cipher mode may be useful if you want shorter encrypted filenames for some reason. </p>
<p> Based on an underlying filesystem supporting a maximum of 255 characters in filenames, here is the maximum possible filename length depending on the choosen encoding scheme : stream (189), block (176), block32 (143). Note that we should rather talk about bytes, when filenames contain special (multi-bytes) characters. </p>
<p> Prior to version 1.1, only stream encoding was supported.</p>
<dt><i>Filename Initialization Vector Chaining</i></p>
<dd> <code>New in 1.1</code>. In previous versions of <code>EncFS</code>, each filename element in a path was encoded separately. So if &#8220;foo&#8221; encoded to &#8220;<font SIZE="-1">XXX&#8221;,</font> then it would always encode that way (given the same encryption key), no matter if the path was &#8220;a/b/foo&#8221;, or &#8220;aa/foo/cc&#8221;, etc. That meant it was possible for someone looking at the encrypted data to see if two files in different directories had the same name, even though they wouldn&#8217;t know what that name decoded to. </p>
<p> With initialization vector chaining, each directory gets its own initialization vector. So &#8220;a/foo&#8221; and &#8220;b/foo&#8221; will have completely different encoded names for &#8220;foo&#8221;. This features has almost no performance impact (for most operations), and so is the default in all modes. </p>
<p> <code>Note:</code> One significant performance exception is directory renames. Since the initialization vector for filename encoding depends on the directory path, any rename requires re-encoding every filename in the tree of the directory being changed. If there are thousands of files, then EncFS will have to do thousands of renames. It may also be possible that EncFS will come across a file that it can&#8217;t decode or doesn&#8217;t have permission to move during the rename operation, in which case it will attempt to undo any changes it made up to that point and the rename will fail.</p>
<dt><i>Per-File Initialization Vectors</i></p>
<dd> <code>New in 1.1</code>. In previous versions of <code>EncFS</code>, each file was encoded in the same way. Each block in a file has always had its own initialization vector, but in a deterministic way, so that block N in one file was encoded in the same way as block N in another file. That made it possible for someone to tell if two files were identical (or parts of the file were identical) by comparing the encoded data. </p>
<p> With per-file initialization vectors, each file gets its own 64-bit random initialization vector, so that each file is encrypted in a different way. </p>
<p> This option is enabled by default. </p>
<p> Reverse mode derivates <font SIZE="-1">IV</font> from inode number, it may then change for example when source files are copied from one <font SIZE="-1">FS</font> to another.</p>
<dt><i>External </i><font SIZE="-1"><i>IV</i></font><i> Chaining</i></p>
<dd> <code>New in 1.1.3</code>. This option is closely related to Per-File Initialization Vectors and Filename Initialization Vector Chaining. Basically it extends the initialization vector chaining from filenames to the per-file initialization vector. </p>
<p> When this option is enabled, the per-file initialization vector is encoded using the initialization vector derived from the filename initialization vector chaining code. This means that the data in a file becomes tied to the filename. If an encrypted file is renamed outside of encfs, it will no longer be decodable within encfs. Note that unless Block <font SIZE="-1">MAC</font> headers are enabled, the decoding error will not be detected and will result in reading random looking data. </p>
<p> There is a cost associated with this. When External <font SIZE="-1">IV</font> Chaining is enabled, hard links will not be allowed within the filesystem, as there would be no way to properly decode two different filenames pointing to the same data. </p>
<p> Also, renaming a file requires modifying the file header. So renames will only be allowed when the user has write access to the file. </p>
<p> Because of these limits, this option is disabled by default for standard mode (and enabled by default for paranoia mode). </p>
<p> This option may be incompatible with some cloud providers, as during a rename, file&#8217;s content changes, but not its timestamp. Due to this, file&#8217;s changes may no be correctly seen by cloud providers&#8217; sync programs. It is then not recommended for cloud usage.</p>
<dt><i>Block </i><font SIZE="-1"><i>MAC</i></font><i> headers</i></p>
<dd> <code>New to 1.1</code>. If this is enabled, every block in every file is stored along with a cryptographic checksum (Message Authentication Code). This makes it virtually impossible to modify a file without the change being detected by <code>EncFS</code>. <code>EncFS</code> will refuse to read data which does not pass the checksum, and will log the error and return an <font SIZE="-1">IO</font> error to the application. </p>
<p> This adds substantial overhead (default being 8 bytes per filesystem block), plus computational overhead, and is not enabled by default except in paranoia mode. </p>
<p> When this is not enabled and if <code>EncFS</code> is asked to read modified or corrupted data, it will have no way to verify that the decoded data is what was originally encoded.</p>
<dt><i>File-hole pass-through</i></p>
<dd> Make encfs leave holes in files. If a block is read as all zeros, it will be assumed to be a hole and will be left as 0&#8217;s when read (not deciphered). This is required if accessing encfs using the <font SIZE="-1">SMB</font> protocol. </p>
<p> Enabled by default. Can be disabled in expert mode.</dl>
<h2>Attacks</h2>
<p> The primary goal of <code>EncFS</code> is to protect data off-line. That is, provide a convenient way of storing files in a way that will frustrate any attempt to read them if the files are later intercepted. </p>
<p> Some algorithms in <code>EncFS</code> are also meant to frustrate on-line attacks where an attacker is assumed to be able to modify the files. </p>
<p> The most intrusive attacks, where an attacker has complete control of the user&#8217;s machine (and can therefore modify <code>EncFS</code>, or <font SIZE="-1"><code>FUSE</code></font>, or the kernel itself) are not guarded against. Do not assume that encrypted files will protect your sensitive data if you enter your password into a compromised computer. How you determine that the computer is safe to use is beyond the scope of this documentation. </p>
<p> That said, here are some example attacks and data gathering techniques on the filesystem contents along with the algorithms <code>EncFS</code> supports to thwart them:</p>
<dl>
<dt><code>Attack</code>: modifying a few bytes of an encrypted file (without knowing what they will decode to).</p>
<dd> <code>EncFS</code> does not use any form of <font SIZE="-1">XOR</font> encryption which would allow single bytes to be modified without affecting others. Most modifications would affect dozens or more bytes. Additionally, <font SIZE="-1">MAC</font> Block headers can be used to identify any changes to files.</p>
<dt><code>Attack</code>: copying a random block of one file to a random block of another file.</p>
<dd> Each block has its own [deterministic] initialization vector.</p>
<dt><code>Attack</code>: copying block N to block N of another file.</p>
<dd> When the Per-File Initialization Vector support is enabled (default in 1.1.x filesystems), a copied block will not decode properly when copied to another file.</p>
<dt><code>Attack</code>: copying an entire file to another file.</p>
<dd> Can be prevented by enabling External <font SIZE="-1">IV</font> Chaining mode.</p>
<dt><code>Attack</code>: determine if two filenames are the same by looking at encrypted names.</p>
<dd> Filename Initialization Vector chaining prevents this by giving each file a 64-bit initialization vector derived from its full path name.</p>
<dt><code>Attack</code>: compare if two files contain the same data.</p>
<dd> Per-File Initialization Vector support prevents this.</dl>
<h2>DISCLAIMER</h2>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> Please refer to the &#8220;<font SIZE="-1">COPYING&#8221;</font> file distributed with <code>EncFS</code> for complete details.</p>
<h2>AUTHORS</h2>
<p> <code>EncFS</code> was written by <code>Valient Gough &lt;vgough [at] pobox.com&gt;</code>. </p>
<p> Site : <code><a rel="nofollow" href="https://vgough.github.io/encfs/">https://vgough.github.io/encfs/</a></code>. </p>
<p> Support, bug reports&#8230; : <code><a rel="nofollow" href="https://github.com/vgough/encfs">https://github.com/vgough/encfs</a></code>. </p>
<p> Mailing list : none. </p>
<p> Cygwin, Windows ports : <code><a rel="nofollow" href="https://github.com/vgough/encfs/wiki">https://github.com/vgough/encfs/wiki</a></code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-encfsctl/">encfsctl</a></code>(1) </p>
<h2>Index</h2>
