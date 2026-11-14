---
title: "pam_mount-conf(5)"
name: "pam_mount-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_mount-conf/"
description: "pam_mount.conf – Description of the pam_mount configuration file"
---

<p>pam_mount.conf &#8211; Description of the pam_mount configuration file</p>
<h2>Overview</h2>
<p>The pam_mount configuration file defines soft defaults for commands pam_mount will be executing, the messages it will show, and which volumes to mount on login. Since pam_mount 0.18, the configuration file is written in XML so as to simplify the pam_mount code base while giving formatting freedom to the end-user. Special characters like <code>&lt;</code>, <code>&gt;</code> and <code>&amp;</code> that are used by XML itself must be encoded as <code>&amp;lt;</code>, <code>&amp;gt;</code> and <code>&amp;amp;</code>, respectively; additionally, <code>&quot;</code> must be encoded as <code>&amp;quot;</code> within a &quot;&quot; area, but these three/four symbols are unlikely to be seen often anyway. </p>
<p> Do not use comments inside elements taking verbatim text, like &lt;fusermount&gt;&lt;/fusermount&gt; &#8211; this is not handled by the pam_mount XML tree parser.</p>
<h2>Volume definitions</h2>
<p>Volumes are defined with the <code>&lt;volume&gt;</code> element, which primarily takes the parameters as attributes, such as </p>
<p> &lt;volume user=&quot;joe&quot; fstype=&quot;nfs&quot; server=&quot;fsbox&quot; path=&quot;/home/%(USER)&quot; mountpoint=&quot;/bigdisk/%(USER)&quot; /&gt; </p>
<p> and define to mount what for whom and how. There are a lot of tunables, which are described in this section.</p>
<h3>Simple user control</h3>
<p>The following attributes control whether the volume is going to get mounted once the user logs in. By default, volumes apply to all users, and specifying attributes limits it to the given conditions, i.e. they are logically ANDed. There is a more powerful and verbose mechanism for specifying complex conditions, described further below in the section &quot;Extended user control&quot;.</p>
<dl>
<dt><code>user=&quot;</code><i>username</i><code>&quot;</code></p>
<dd>Limit the volume to the specified user, identified by name</p>
<dt><code>uid=&quot;</code><i>number</i><code>&quot;</code> or <code>uid=&quot;</code><i>number</i><code>&#8211;</code><i>number</i><code>&quot;</code></p>
<dd>Limit the volume to the specified user(s), identified by UID or UID range.</p>
<dt><code>pgrp=&quot;</code><i>groupname</i><code>&quot;</code></p>
<dd>Limit the volume to users which have the group identified by name as their primary group.</p>
<dt><code>gid=&quot;</code><i>number</i><code>&quot;</code> or <code>gid=&quot;</code><i>number</i><code>&#8211;</code><i>number</i><code>&quot;</code></p>
<dd>Limit the volume to users which have the group(s) given by GID or GID range as a primary group.</p>
<dt><code>sgrp=&quot;</code><i>groupname</i><code>&quot;</code></p>
<dd>Limit the volume to users which are a member of the group identified by name (either as primary or secondary group).</dl>
<h3>Volume configuration</h3>
<p>The following attributes select volume source, destination, options and so on.</p>
<dl>
<dt><code>fstype=&quot;</code><i>type</i><code>&quot;</code></p>
<dd>The filesystem type, which can be anything your kernel, userspace and pam_mount understand. If the fstype specifies a pam_mount-special type, pam_mount will handle it. Otherwise, the fstype is passed to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) which then in turn looks for a userspace helper /sbin/mount.<i>fstype</i> and runs that if it exists, and in any other case, <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) would call <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2) to cause the kernel to directly mount it. <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) knows of an <code>auto</code> fstype, which might be helpful in some cases. Not specifying the fstype attribute implies <code>fstype=&quot;auto&quot;</code>. Note that mounting with <code>auto</code> may fail if the filesystem kernel module is not loaded yet, since <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) will check /proc/partitions.</p>
<dd>The fstypes <code>cifs</code>, <code>smbfs</code>, <code>ncpfs</code>, <code>fuse</code>, <code>nfs</code> and <code>nfs</code> are overriden by pam_mount and we run the respective helper programs directly instead of invoking <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) with the basic default set of arguments which are often insufficient for networked filesystems. See this manpage&#8217;s section &quot;Examples&quot; below for more details.</p>
<dt><code>noroot=&quot;1&quot;</code></p>
<dd>Call the mount program without root privileges. It defaults to yes for the <code>fuse</code> fstype, because FUSE volumes must be mounted as the user that logs in to get access to the files by default.</p>
<dt><code>server=&quot;</code><i>name</i><code>&quot;</code></p>
<dd>Defines the server to which to connect in case of <code>cifs</code>, <code>smbfs</code> and <code>ncpfs</code> and <code>nfs</code> fstypes. For all other fs types, this attribute is ignored. You can also specify the server in the <code>path</code> attribute instead, but need to adhere to the specific syntax that is a particular fstype requires. (E.g. CIFS uses &quot;//server/path&quot;, whereas NFS uses &quot;server:path&quot;, etc.)</p>
<dt><code>path=&quot;</code><i>path</i><code>&quot;</code></p>
<dd>This mandatory attribute specifies the location of the volume, relative to the server (if specified).</p>
<dt><code>mountpoint=&quot;</code><i>directory</i><code>&quot;</code></p>
<dd>This specifies the destination directory onto which the volume is mounted. &quot;<code>~</code>&quot; expands to the user&#8217;s home directory as present in the passwd database, according to sh semantics. &quot;<code>~name</code>&quot; is <i>not</i> supported. If this attribute is omitted, the location is read from /etc/fstab, which also requires <code>path</code> to be a device or a source directory of an fstab entry.</p>
<dt><code>options=&quot;</code><i>&#8230;</i><code>&quot;</code></p>
<dd>Specifies the mount options. If omitted and /etc/fstab is used (see <code>mountpoint</code>), the options will also be sources from fstab.</p>
<dt><code>ssh=&quot;0&quot;</code> or <code>ssh=&quot;1&quot;</code></p>
<dd>The <code>ssh</code> option enables an input hack wrapper (zerossh, see <code><a href="/docs/linux/man/1-pmt-fd0ssh/">pmt-fd0ssh</a></code>(1)) for this volume to hand the password to ssh over an ssh-specific mechanism. Enable this option for any mount involving the SSH binary, e.g. ccgfs or sshfs. Do <i>not</i> enable it for anything else or the login will most likely hang.</p>
<dt><code>cipher=&quot;</code><i>cipher</i><code>&quot;</code></p>
<dd>Cryptsetup cipher name for the volume. To be used with the <code>crypt</code> fstype.</p>
<dt><code>fskeycipher=&quot;</code><i>ciphertype</i><code>&quot;</code></p>
<dd>OpenSSL cipher name for the fskey. Use with the <code>crypt</code> fstype (dm-crypt and LUKS). The special cipher keyword &quot;<code>none</code>&quot; may be used to directly pass the file&#8217;s contents to cryptsetup without decryption by OpenSSL.</p>
<dt><code>fskeyhash=&quot;</code><i>hash</i><code>&quot;</code></p>
<dd>OpenSSL hash name for the fskey.</p>
<dt><code>fskeypath=&quot;</code><i>path</i><code>&quot;</code></p>
<dd>Path to the filesystem key.</dl>
<h2>Variables</h2>
<p>Within attributes and commands (see later section), specific placeholders or variables, identified by <code>%(</code><i>name</i><code>)</code> may be used. These are substituted at command invocation time.</p>
<dl>
<dt><code>%(USER)</code></p>
<dd>Expands to the username of the user logging in.</p>
<dt><code>%(DOMAIN_NAME)</code>, <code>%(DOMAIN_USER)</code></p>
<dd>Winbind has special UNIX usernames in the form of &quot;<i>domain</i><code>\</code><i>username</i>&quot;, and %(DOMAIN_NAME) and %(DOMAIN_USER) provide the split parts of it. This is useful when a sharename on an MSAD server is the same as the username, e.g. &lt;volume fstype=&quot;cifs&quot; server=&quot;fsbox&quot; path=&quot;%(DOMAIN_USER)&quot; /&gt;.</p>
<dt><code>%(USERUID)</code>, <code>%(USERGID)</code></p>
<dd>The numeric UID and GID of the primary group of the user logging in. This is obtained via getpw*(), not getuid(). It is useful in conjunction with the uid= or gid= mount options, e.g. &lt;volume options=&quot;uid=%(USERUID)&quot; /&gt;. Note that you <code>do not</code> need to specify uid=%(USERUID) for smbfs or cifs mounts because this is already done automatically by pam_mount.</p>
<dt><code>%(GROUP)</code></p>
<dd>The name of the group for %(USERGID).</dl>
<p> All other variables you might find in the source code are internal to pam_mount, and are likely not to be expanded when you would expect it.</p>
<h2>pam_mount parameters</h2>
<p>Besides volumes, there are other elements allowed in pam_mount.conf.xml that control pam_mount&#8217;s own behavior.</p>
<h3>General tunables</h3>
<dl>
<dt><code>&lt;debug enable=&quot;1&quot; /&gt;</code></p>
<dd>Enables verbose output during login to stderr and syslog. Some programs do not cope with output sent on stderr, see doc/bugs.txt for a list. <code>0</code> disables debugging, <code>1</code> enables pam_mount tracing, and <code>2</code> additionally enables tracing in mount.crypt. The default is <code>0</code>. As the config file is parsed linearly, the &lt;debug&gt; directive takes effect once it is seen &#8211; it it thus advised to put it near the start of the file, before any &lt;volume&gt; definitions.</p>
<dt><code>&lt;logout wait=&quot;</code><i>microseconds</i><code>&quot; hup=&quot;</code><i>yes/no</i><code>&quot; term=&quot;</code><i>yes/no</i><code>&quot; kill=&quot;</code><i>yes/no</i><code>&quot; /&gt;</code></p>
<dd>Programs exist that do not terminate when the session is closed. (This applies to the &quot;final&quot; close, i.e. when the last user session ends.) Examples are processes still running in the background; or a broken X session manager that did not clean up its children, or other X programs that did not react to the X server termination notification. pam_mount can be configured to kill these processes and optionally wait before sending signals.</p>
<dt><code>&lt;luserconf name=&quot;</code><i>.pam_mount.conf.xml</i><code>&quot; /&gt;</code></p>
<dd>Individual users may define additional volumes in a file by the specified <i>name</i> relative to their home directory. The presence of <code>&lt;luserconf&gt;</code> in the master config file enables this feature. If turned on, users may mount and unmount any volumes they specify and that they have ownership of (in case of local mounts). The mount process is executed <code>as superuser</code>. This may have security implications, so this feature is disabled by default. Luserconfigs are parsed after any volumes from the global configuration file have been mounted, so that first mounting home directories with a global config and then mounting further volumes from luserconfigs is possible.</p>
<dt><code>&lt;mntoptions allow=&quot;</code><i>options,&#8230;</i><code>&quot; /&gt;</code></p>
<dd>The &lt;mntoptions&gt; elements determine which options may be specified in &lt;volumes&gt; in per-user configuration files (see &lt;luserconf&gt;). It does not apply to the master file. Specifying &lt;mntoptions&gt; is forbidden and ignored in per-user configs. The default allowed list consists of &quot;<i>nosuid,nodev</i>&quot;, and this default is cleared when the first allow=&quot;&#8230;&quot; attribute is seen by the config parser. All further allow=&quot;&#8230;&quot; are additive, though.</p>
<dt><code>&lt;mntoptions deny=&quot;</code><i>options,&#8230;</i><code>&quot; /&gt;</code></p>
<dd>Any options listed in deny may not appear in the option list of per-user mounts. The default deny list is empty.</p>
<dt><code>&lt;mntoptions require=&quot;</code><i>options,&#8230;</i><code>&quot; /&gt;</code></p>
<dd>All options listed in require must appear in the option list of per-user mounts. The default require list consists of &quot;<i>nosuid,nodev</i>&quot;, and like allow=&quot;&quot;, is cleared when first encountered by the parser, and is otherwise additive.</p>
<dt><code>&lt;path&gt;</code><i>directories&#8230;</i><code>&lt;/path&gt;</code></p>
<dd>The default for the PATH environmental variable is not consistent across distributions, and so, pam_mount provides its own set of sane defaults which you may change at will.</dl>
<h3>Volume-related</h3>
<dl>
<dt><code>&lt;mkmountpoint enable=&quot;1&quot; remove=&quot;true&quot; /&gt;</code></p>
<dd>Controls automatic creation and removal of mountpoints. If a mountpoint does not exist when the volume is about to be mounted, pam_mount can be instructed to create one using the <code>enable</code> attribute. Normally, directories created this way are retained after logout, but <code>remove</code> may be set to <code>true</code> to remove the mountpoint again, <i>but only</i> if it was automatically created by pam_mount in the same session before.</dl>
<h3>Auxiliary programs</h3>
<p>Some mount programs need special default parameters to properly function. It is good practice to specify uid= for CIFS for example, because it is mounted as root and would otherwise show files belonging to root instead of the user logging in.</p>
<dl>
<dt><code>&lt;fd0ssh&gt;</code><i>program&#8230;</i><code>&lt;/fd0ssh&gt;</code></p>
<dd>fd0ssh is a hack around OpenSSH that essentially makes it read passwords from stdin even though OpenSSH normally does not do that.</p>
<dt><code>&lt;fsck&gt;</code><i>fsck -p %(FSCKTARGET)</i><code>&lt;/fsck&gt;</code></p>
<dd>Local volumes will be checked before mounting if this program is set.</p>
<dt><code>&lt;ofl&gt;</code><i>ofl -k%(SIGNAL) %(MNTPT)</i><code>&lt;/ofl&gt;</code></p>
<dd>The Open File Lister is used to identify processes using files within the given subdirectory, and optionally send a signal to those processes.</p>
<dt><code>&lt;pmvarrun&gt;</code><i>pmvarrun &#8230;</i><code>&lt;/pmvarrun&gt;</code></p>
<dd><code><a href="/docs/linux/man/8-pmvarrun/">pmvarrun</a></code>(8) is a separate program to manage the reference count tracking user sessions.</dl>
<h3>Mount programs</h3>
<p>Commands to mount/unmount volumes. They can take parameters, as shown. You can specify either absolute paths, or relative ones, in which case $PATH will be searched. Since login programs have differing default PATHs, pam_mount has its own path definition (see above).</p>
<dl>
<dt><code>&lt;lclmount&gt;</code><i>mount -p0 -t %(FSTYPE) &#8230;</i><code>&lt;/lclmount&gt;</code></p>
<dd>The regular mount program.</p>
<dt><code>&lt;umount&gt;</code><i>umount %(MNTPT)</i><code>&lt;/umount&gt;</code></p>
<dd>Unless there is a dedicated umount program for a given filesystem type, the regular umount program will be used.</p>
<dd>Linux supports lazy unmounting using `/sbin/umount -l`. This may be dangerous for encrypted volumes because the underlying device is not unmapped. Loopback devices are also affected by this (not being unmapped when files are still open). Also, unmount on SMB volumes needs to be called on %(MNTPT) and not %(VOLUME).</dl>
<p> Commands for various mount programs. Not all have a dedicated umount helper because some do not need one.</p>
<dl>
<dt><code>&lt;cifsmount&gt;</code><i>mount.cifs &#8230;</i><code>&lt;/cifsmount&gt;</code></p>
<dd>
<dt><code>&lt;cryptmount&gt;</code><i>mount.crypt &#8230;</i><code>&lt;/cryptmount&gt;</code></p>
<dd>
<dt><code>&lt;cryptumount&gt;</code><i>umount.crypt %(MNTPT)</i><code>&lt;/cryptumount&gt;</code></p>
<dd>Mount helpers for dm-crypt and LUKS volumes.</p>
<dt><code>&lt;fusemount&gt;</code><i>mount.fuse &#8230;</i><code>&lt;/fusemount&gt;</code></p>
<dd>
<dt><code>&lt;fuseumount&gt;</code><i>fuserumount &#8230;</i><code>&lt;/fuseumount&gt;</code></p>
<dd>
<dt><code>&lt;ncpmount&gt;</code><i>ncpmount &#8230;</i><code>&lt;/ncpmount&gt;</code></p>
<dd>
<dt><code>&lt;ncpumount&gt;</code><i>ncpumount &#8230;</i><code>&lt;/ncpumount&gt;</code></p>
<dd>
<dt><code>&lt;nfsmount&gt;</code><i>mount %(SERVER):%(VOLUME) &#8230;</i><code>&lt;/nfsmount&gt;</code></p>
<dd>
<dt><code>&lt;smbmount&gt;</code><i>smbmount &#8230;</i><code>&lt;/smbmount&gt;</code></p>
<dd>
<dt><code>&lt;smbumount&gt;</code><i>smbumount &#8230;</i><code>&lt;/smbumount&gt;</code></p>
<dd></dl>
<h3>Messages</h3>
<dl>
<dt><code>&lt;msg-authpw&gt;</code><i>pam_mount password:</i><code>&lt;/msg-authpw&gt;</code></p>
<dd>When pam_mount cannot obtain a password through PAM, or is configured to not do so in the first place, and is configured to ask for a password interactively as a replacement, this prompt will be shown.</p>
<dt><code>&lt;msg-sessionpw&gt;</code><i>reenter&#8230;:</i><code>&lt;/msg-sessionpw&gt;</code></p>
<dd>In case the &#8216;session&#8217; PAM block does not have the password (e.g. on su from root to user), it will ask again. This prompt can also be customized.</dl>
<h2>Extended user control</h2>
<p>Sometimes, the simple user control attributes for the &lt;volume&gt; element are not sufficient where one may want to build more complex expressions as to whom a volume applies. Instead of attributes, extended user control is set up using additional elements within &lt;volume&gt;, for example </p>
<p> &lt;volume path=&quot;/dev/shm&quot; mountpoint=&quot;~&quot;&gt; &lt;and&gt; &lt;sgrp&gt;students&lt;/sgrp&gt; &lt;not&gt; &lt;sgrp&gt;profs&lt;/sgrp&gt; &lt;/not&gt; &lt;/and&gt; &lt;/volume&gt; </p>
<p> Which translates to (students &amp;&amp; !profs).</p>
<h3>Logical operators</h3>
<dl>
<dt><code>&lt;and&gt;</code><i>&lt;elements&gt;*</i><code>&lt;/and&gt;</code></p>
<dd>All elements within this one are logically ANDed. Any number of elements may appear.</p>
<dt><code>&lt;or&gt;</code><i>&lt;elements&gt;*</i><code>&lt;/or&gt;</code></p>
<dd>All elements within this one are logically ORed. Any number of elements may appear.</p>
<dt><code>&lt;xor&gt;</code><i>&lt;elements&gt;{2}</i><code>&lt;/xor&gt;</code></p>
<dd>The two elements within the &lt;xor&gt; are logically XORed.</p>
<dt><code>&lt;not&gt;</code><i>&lt;element&gt;</i><code>&lt;/not&gt;</code></p>
<dd>The single element within the &lt;not&gt; is logically negated.</dl>
<h3>User selection</h3>
<dl>
<dt><code>&lt;user&gt;</code><i>username</i><code>&lt;/user&gt;</code></p>
<dd>Match against the given username.</p>
<dt><code>&lt;uid&gt;</code><i>number</i><code>&lt;/uid&gt;</code> or <code>&lt;uid&gt;</code><i>number</i><code>&#8211;</code><i>number</i><code>&lt;/uid&gt;</code></p>
<dd>Match the UID of the user logging in against a UID or UID range.</p>
<dt><code>&lt;gid&gt;</code><i>number</i><code>&lt;/gid&gt;</code> or <code>&lt;gid&gt;</code><i>number</i><code>&#8211;</code><i>number</i><code>&lt;/gid&gt;</code></p>
<dd>Match the primary group of the user logging in against a GID or GID range.</p>
<dt><code>&lt;pgrp&gt;</code><i>groupname</i><code>&lt;/pgrp&gt;</code></p>
<dd>Check if the user logging in has <i>groupname</i> as the primary group.</p>
<dt><code>&lt;sgrp&gt;</code><i>groupname</i><code>&lt;/sgrp&gt;</code></p>
<dd>Check if the user logging in is a member of the group given by <i>name</i> (i.e. it is either a primary or secondary group).</dl>
<h3>Attributes</h3>
<dl>
<dt><code>icase=&quot;yes&quot;</code> or <code>icase=&quot;no&quot;</code></p>
<dd>The <code>icase</code> attribute may be used on <code>&lt;user&gt;</code>, <code>&lt;pgrp&gt;</code> and <code>&lt;sgrp&gt;</code> to enable case-insensitive matching (or not). It defaults to &quot;no&quot;.</p>
<dt><code>regex=&quot;yes&quot;</code> (or no)</p>
<dd>The <code>regex</code> attribute may be used on <code>&lt;user&gt;</code>, <code>&lt;pgrp&gt;</code> and <code>&lt;sgrp&gt;</code> to enable interpreting the text content of the tag as a Perl-compatible regular expression pattern. This attribute may be combined with &quot;icase&quot; (see above). Example: &lt;user regex=&quot;yes&quot;&gt;joe&lt;/user&gt; matches any user who has the letter sequence &quot;joe&quot; anywhere in their username. Therefor, use the regex feature cautiously and consider adding ^ and $ anchors to limit security surprises. Example: &lt;user regex=&quot;yes&quot;&gt;^.*joe.*$&lt;/user&gt; if you really wanted to match the sequence at any position.</dl>
<h2>Examples</h2>
<p>Remember that <code>~</code> can be used in the mountpoint attribute to denote the home directory as retrievable through <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3).</p>
<h3>sshfs and ccgfs</h3>
<p>Not specifying any path after the colon (:) uses the path whereever ssh will put you in, usually the home directory. </p>
<pre><code>&lt;volume fstype=&quot;fuse&quot; path=&quot;sshfs#%(USER)@fileserver:&quot; mountpoint=&quot;~&quot; /&gt;</code></pre>
<p> &lt;volume fstype=&quot;fuse&quot; path=&quot;ccgfs-ssh-pull#%(USER)@host:directory&quot; mountpoint=&quot;~&quot; /&gt;</p>
<h3>encfs 1.4.x and up</h3>
<p>&lt;volume fstype=&quot;fuse&quot; path=&quot;encfs#/crypto/%(USER)&quot; mountpoint=&quot;~&quot;<br />
options=&quot;nonempty&quot; /&gt; (encfs 1.3 is no longer supported.)</p>
<h3>NFS mounts</h3>
<p>&lt;volume fstype=&quot;nfs&quot; server=&quot;fileserver&quot; path=&quot;/home/%(USER)&quot; mountpoint=&quot;~&quot; /&gt;</p>
<h3>CIFS/SMB mounts</h3>
<p>&lt;volume user=&quot;user&quot; fstype=&quot;smbfs&quot; server=&quot;krueger&quot; path=&quot;public&quot; mountpoint=&quot;/home/user/krueger&quot; /&gt;</p>
<h3>NCP mounts</h3>
<p>&lt;volume user=&quot;user&quot; fstype=&quot;ncpfs&quot; server=&quot;krueger&quot; path=&quot;public&quot; mountpoint=&quot;/home/user/krueger&quot; options=&quot;username=user.context&quot; /&gt;</p>
<h3>Bind mounts</h3>
<p>This may come useful in conjunction with pam_chroot: &lt;volume path=&quot;/bin&quot; mountpoint=&quot;~/bin&quot; options=&quot;bind&quot; /&gt;</p>
<h3>tmpfs mounts</h3>
<p>Volatile tmpfs mount with restricted size (thanks to Mike Hommey for this example): &lt;volume user=&quot;test&quot; fstype=&quot;tmpfs&quot; mountpoint=&quot;/home/test&quot; options=&quot;size=10M,uid=%(USER),mode=0700&quot; /&gt;</p>
<h3>dm-crypt volumes</h3>
<p>Crypt mounts require a kernel with CONFIG_BLK_DEV_DM and CONFIG_DM_CRYPT enabled, as well as all the ciphers that are going to be used, e.g. CONFIG_CRYPTO_AES, CONFIG_CRYPTO_BLOWFISH, CONFIG_CRYPTO_TWOFISH. &lt;volume path=&quot;/home/%(USER).img&quot; mountpoint=&quot;~&quot; cipher=&quot;aes-cbc-essiv:sha256&quot; fskeycipher=&quot;aes-256-cbc&quot; fskeyhash=&quot;sha1&quot; fskeypath=&quot;/home/%(USER).key&quot; /&gt;</p>
<h3>LUKS volumes</h3>
<p>&lt;volume path=&quot;/home/%(USER).img&quot; mountpoint=&quot;~&quot; cipher=&quot;aes-cbc-essiv:sha256&quot; /&gt;</p>
<h3>cryptoloop volumes</h3>
<p>cryptoloop is not explicitly supported by pam_mount. Citing the Linux kernel config help text: &quot;WARNING: This device [cryptoloop] is not safe for journal[l]ed filesystems[&#8230;]. Please use the Device Mapper [dm-crypt] module instead.&quot;</p>
<h3>OpenBSD encrypted home</h3>
<p>OpenBSD encrypted home directory example: </p>
<pre><code>&lt;volume path=&quot;/home/user.img&quot; mountpoint=&quot;/home/user&quot; options=&quot;svnd0&quot; /&gt;
</code></pre>
