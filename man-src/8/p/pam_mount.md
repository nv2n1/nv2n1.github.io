---
title: "pam_mount(8)"
name: "pam_mount"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_mount/"
description: "pam_mount – A PAM module that can mount volumes for a user session"
---

<p>pam_mount &#8211; A PAM module that can mount volumes for a user session</p>
<h2>Overview</h2>
<p>This module is aimed at environments with central file servers that a user wishes to mount on login and unmount on logout, such as (semi-)diskless stations where many users can logon and where statically mounting the entire /home from a server is a security risk, or listing all possible volumes in /etc/fstab is not feasible.</p>
<dl>
<dt>&bull;</p>
<dd>Users can define their own list of volumes without having to change (possibly non-writable) global config files.</p>
<dt>&bull;</p>
<dd>Single sign-on feature &#8211; the user needs to type the password just once (at login)</p>
<dt>&bull;</p>
<dd>Transparent mount process</p>
<dt>&bull;</p>
<dd>No stored passwords</p>
<dt>&bull;</p>
<dd>Volumes are unmounted on logout, freeing system resources and not leaving data exposed.</dl>
<p> The module also supports mounting local filesystems of any kind the normal mount utility supports, with extra code to make sure certain volumes are set up properly because often they need more than just a mount call, such as encrypted volumes. This includes SMB/CIFS, FUSE, dm-crypt and LUKS. </p>
<p> If you intend to use pam_mount to protect volumes on your computer using an encrypted filesystem system, please know that there are many other issues you need to consider in order to protect your data. For example, you probably want to disable or encrypt your swap partition (the cryptoswap can help you do this). Do not assume a system is secure without carefully considering potential threats.</p>
<h2>Configuration</h2>
<p>The primary configuration file for the pam_mount module is pam_mount.conf.xml. On most platforms this file is read from /etc/security/pam_mount.conf.xml. On OpenBSD pam_mount reads its configuration file from /etc/pam_mount.conf.xml. See <a href="/docs/linux/man/5-pam_mount-conf/">pam_mount.conf</a>(5) documenting its use. </p>
<p> Individual users may define additional volumes to mount if allowed by pam_mount.conf.xml (usually ~/.pam_mount.conf.xml). The volume keyword is the only valid keyword in these per-user configuration files. If the luserconf parameter is set in pam_mount.conf.xml, allowing user-defined volume, then users may mount and unmount any volume they own at any mount point they own. On some filesystem configurations this may be a security flaw so user-defined volumes are not allowed by the example pam_mount.conf.xml distributed with pam_mount.</p>
<h2>PAM configuration</h2>
<p>In addition, you must include two entries in the system&#8217;s applicable /etc/pam.d/<i>service</i> config files, as the following example shows:</p>
<dl>
<dd>
<pre> auth required pam_securetty.so
 auth required pam_pwdb.so shadow nullok
 auth required pam_nologin.so
+++ auth optional pam_mount.so
 account required pam_pwdb.so
 password required pam_cracklib.so
 password required pam_pwdb.so shadow nullok use_authtok
 session required pam_pwdb.so
 session optional pam_console.so
+++ session optional pam_mount.so</pre>
</dl>
<p> When &quot;sufficient&quot; is used in the second column, you must make sure that pam_mount is added before this entry. Otherwise pam_mount will not get executed should a previous PAM module succeed. Also be aware of the &quot;include&quot; statements. These make PAM look into the specified file. If there is a &quot;sufficient&quot; statement, then the pam_mount entry must either be in the included file before the &quot;sufficient&quot; statement or before the &quot;include&quot; statement. </p>
<p> If you use pam_ldap, pam_winbind, or any other authentication services that make use of PAM&#8217;s sufficient keyword, model your configuration on the following order:</p>
<dl>
<dd>
<pre>&bull;&bull;&bull;
account sufficient pam_ldap.so
auth required pam_mount.so
auth sufficient pam_ldap.so use_first_pass
auth required pam_unix.so use_first_pass
session optional pam_mount.so
&bull;&bull;&bull;</pre>
</dl>
<p> This allows for:</p>
<dl>
<dt>1.</p>
<dd>pam_mount, as the first &quot;auth&quot; module, will prompt for a password and export it to the PAM system.</p>
<dt>2.</p>
<dd>pam_ldap will use the password from the PAM system to try and authenticate the user. If this succedes, the user will be authenticated. If it fails, pam_unix will try to authenticate.</p>
<dt>3.</p>
<dd>pam_unix will try to authenticate the user if pam_ldap failed. If pam_unix fails, then the authentication will be refused (due to the &quot;required&quot;).</dl>
<p> Alternatively, the following is possible (thanks to Andrew Morgan for the hint!):</p>
<dl>
<dd>
<pre>auth [success=2 default=ignore] pam_unix2.so
auth [success=1 default=ignore] pam_ldap.so use_first_pass
auth requisite pam_deny.so
auth optional pam_mount.so</pre>
</dl>
<p> It may seem odd, but the first three lines will make it so that at least one of pam_unix2 or pam_ldap has to succeed. As you can see, pam_mount will be run <code>after</code> successful authentification with these subsystems.</p>
<h2>Encrypted disks</h2>
<p>pam_mount supports a few types of crypto. The most common are encfs, dm-crypt and dm-crypt+LUKS. </p>
<p> The first one uses the FUSE layer; files within the encfs container are stored as single encrypted files on the host in a previously-existing directory. If you store lots of files, it is recommended to have a lower filesystem that is strong in this area, such as xfs, but some software and/or your partitioning decisions may force you to use a different fs. The 1:1 mapping of files also allows encrypted files to be reasonably efficiently rsync&#8217;ed for example without having to open the encrypted container. Creation is done through the <a href="/docs/linux/man/1-encfs/">encfs</a>(1) tool. </p>
<p> dm-crypt provides whole-filesystem/entire-partition encryption. You can also create a container file, but the idea is that it is represented as a block device on which you still have to create a filesystem. In fact, this way you can select a filesystem of your choice. The downside is that shrinking is often not possible (there is no such issue in encfs because it uses the lower fs). Suitable dm-crypt containers (and auxiliary files), using block devices or plain files, can be created using the <a href="/docs/linux/man/8-pmt-ehd/">pmt-ehd</a>(8) tool. </p>
<p> pmt-ehd creates filesystem key material which is a bunch of random bytes that will be used to en-/decrypt the volume. This material itself is encrypted with your own password &#8211; this is done so that you can change the password without having to reencrypt all of your data. </p>
<p> LUKS is an extension for dm-crypt to support multi-password containers. Unless you specifically need it, the above two solutions are recommended. </p>
<p> NOTE: The key file that <a href="/docs/linux/man/8-pmt-ehd/">pmt-ehd</a>(8) will create represents the filesystem key material as encrypted with your password. It is thus safe to store this on an unsecured filesystem.</p>
<h2>Troubleshooting</h2>
<p>To ensure that your system and, possibly, the remote server are all properly configured, you should try to mount all or some of the volumes by hand, using the same commands and mount points provided in pam_mount.conf.xml. This will save you a lot of grief, since it is more difficult to debug the mounting process via pam_mount. </p>
<p> If you can mount the volumes by hand but it is not happening via pam_mount, you may want to enable the &quot;debug&quot; option in pam_mount.conf.xml to see what is happening. </p>
<p> Verify if the user owns the mount point and has sufficient permissions over that. pam_mount will verify this and will refuse to mount the remote volume if the user does not own that directory. </p>
<p> If pam_mount is having trouble unmounting volumes upon logging out, enable the debug variable. This causes pam_mount to run ofl on logout and write its output to the system&#8217;s log.</p>
<h2>Authors</h2>
<p>W. Michael Petullo </p>
<p> Jan Engelhardt (current maintainer)</p>
<h2>Community Support</h2>
<p>The following two forms of communication are available. The maintainer has no preference, though you will reach more users who could answer by means of the mailing list.</p>
<dl>
<dt>Mailing List:</p>
<dd><a rel="nofollow" href="http://sf.net/mail/?group_id=41452">http://sf.net/mail/?group_id=41452</a></p>
<dt>Bug Tracker (no registration needed):</p>
<dd><a rel="nofollow" href="http://sf.net/tracker/?group_id=41452">http://sf.net/tracker/?group_id=41452</a> </p>
</dl>
