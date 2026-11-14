---
title: "ntfs-3g-usermap(8)"
name: "ntfs-3g-usermap"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfs-3g-usermap/"
description: "ntfs-3g.usermap – NTFS Building a User Mapping File"
---

<p>ntfs-3g.usermap &#8211; NTFS Building a User Mapping File</p>
<h2>Synopsis</h2>
<p><code>ntfs-3g.usermap</code> <i>windows-system-device</i> <code>[</code><i>other-ntfs-device</i>&#8230;<code>]</code> </p>
<p> Where <i>windows-system-device</i> is the device containing the Windows system whose users are to be mapped to current Linux system. </p>
<p> And <i>other-ntfs-device</i> is another device containing files which are to be accessed both by the Windows mentioned above and current Linux system. </p>
<p> the ntfs-3g.usermap command must be started as root, and the designated devices must not be mounted. </p>
<p> Typing ntfs-3g.usermap with no args will display a summary of command arguments.</p>
<h2>Description</h2>
<p><code>ntfs-3g.usermap</code> creates the file defining the mapping of Windows accounts to Linux logins for users who owns files which should be visible from both Windows and Linux. </p>
<p> It relies on existing files which were created on Windows, trying to locate significant files and asking which Linux user or group should own them. When a Linux owner or group is requested, the reply may be : </p>
<p> &#8211; the uid or gid (numeric or symbolic) of Linux owner or group of the file.</p>
<dl>
<dd>In that situation, no more file with the same Windows owner will be selected.</dl>
<p> &#8211; or no answer, when not able to define the owner or group.</p>
<dl>
<dd>In that situation another file owned by the same Windows user or group may be selected later so that a mapping can be defined.</dl>
<p> The mappings for standard Windows users, such as &quot;Administrator&quot; or &quot;All Users&quot; are defined implicitly. As a consequence a user mapping should never be defined as Linux root. </p>
<p> When there are no more significant files, ntfs-3g.usermap create the mapping file into the file UserMapping in the current directory. This file has to be moved to the hidden directory .NTFS-3G in the root of all the NTFS file systems to be shared between Windows and Linux. This requires the file system to be mounted, but the created file will not be taken into account if not present at mount time, which means the file system has to be unmounted and mounted again for the new mapping file to be taken into account.</p>
<h2>Options</h2>
<p>No option is defined for ntfs-3g.usermap.</p>
<h2>Examples</h2>
<p>Map the users defined on the Windows system present on /dev/sda1 :</p>
<dl>
<dd><code>ntfs-3g.usermap /dev/sda1</code>  A detailed example, with screen displays is available on <a rel="nofollow" href="http://pagesperso-orange.fr/b.andre/usermap.html">http://pagesperso-orange.fr/b.andre/usermap.html</a></p>
<h2>Exit Codes</h2>
<p><code>ntfs-3g.usermap</code> exits with a value of 0 when no error was detected, and with a value of 1 when an error was detected.</p>
<h2>Known Issues</h2>
<p>Please see</p>
<dl>
<dd><a rel="nofollow" href="http://www.tuxera.com/community/ntfs-3g-faq/">http://www.tuxera.com/community/ntfs-3g-faq/</a> </p>
</dl>
<p> for common questions and known issues. If you would find a new one in the latest release of the software then please send an email describing it in detail. You can contact the development team on the ntfs-3g-devel [at] lists.sf.net address.</p>
<h2>Authors</h2>
<p><code>ntfs-3g.secaudit</code> has been developed by Jean-Pierre André.</p>
<h2>Thanks</h2>
<p>Several people made heroic efforts, often over five or more years which resulted the ntfs-3g driver. Most importantly they are Anton Altaparmakov, Richard Russon, Szabolcs Szakacsits, Yura Pakhuchiy, Yuval Fledel, and the author of the groundbreaking FUSE filesystem development framework, Miklos Szeredi.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8), <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5), <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1) </p>
