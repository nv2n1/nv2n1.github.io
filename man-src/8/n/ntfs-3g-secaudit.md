---
title: "ntfs-3g-secaudit(8)"
name: "ntfs-3g-secaudit"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfs-3g-secaudit/"
description: "ntfs-3g.secaudit – NTFS Security Data Auditing"
---

<p>ntfs-3g.secaudit &#8211; NTFS Security Data Auditing</p>
<h2>Synopsis</h2>
<p><code>ntfs-3g.secaudit</code> <code>[</code><i>options</i><code>]</code> <i>args</i> </p>
<p> Where <i>options</i> is a combination of :</p>
<dl>
<dd>-a full auditing of security data (Linux only)</dl>
<dl>
<dd>-b backup ACLs</dl>
<dl>
<dd>-e setting extra backed-up parameters (in conjunction with -s)</dl>
<dl>
<dd>-h displaying hexadecimal security descriptors saved in a file</dl>
<dl>
<dd>-r recursing in a directory</dl>
<dl>
<dd>-s setting backed-up ACLs</dl>
<dl>
<dd>-u getting a user mapping proposal</dl>
<dl>
<dd>-v verbose (very verbose if set twice)</dl>
<p> and args define the parameters and the set of files acted upon. </p>
<p> Typing secaudit with no args will display a summary of available options.</p>
<h2>Description</h2>
<p><code>ntfs-3g.secaudit</code> displays the ownership and permissions of a set of files on an NTFS file system, and checks their consistency. It can be started in terminal mode only (no graphical user interface is available.) </p>
<p> When a <i>volume</i> is required, it has to be unmounted, and the command has to be issued as <code>root</code>. The <i>volume</i> can be either a block device (i.e. a disk partition) or an image file. </p>
<p> When acting on a directory or volume, the command may produce a lot of information. It is therefore advisable to redirect the output to a file or pipe it to a text editor for examination.</p>
<h2>Options</h2>
<p>Below are the valid combinations of options and arguments that <code>ntfs-3g.secaudit</code> accepts. All the indicated arguments are mandatory and must be unique (if wildcards are used, they must resolve to a single name.)</p>
<dl>
<dt><code>-h</code> <i>file</i></p>
<dd>Displays in an human readable form the hexadecimal security descriptors saved in <i>file</i>. This can be used to turn a verbose output into a very verbose output.</p>
<dt><code>-a[rv]</code> <i>volume</i></p>
<dd>Audits the volume : all the global security data on <i>volume</i> are scanned and errors are displayed. If option <code>-r</code> is present, all files and directories are also scanned and their relations to global security data are checked. This can produce a lot of data. </p>
<p> This option is not effective on volumes formatted for old NTFS versions (pre NTFS 3.0). Such volumes have no global security data. </p>
<p> When errors are signalled, it is advisable to repair the volume with an appropriate tool (such as <code>chkdsk</code> on Windows.)</p>
<dt><code>[-v]</code> <i>volume</i> <i>file</i></p>
<dd>Displays the security parameters of <i>file</i> : its interpreted Linux mode (rwx flags in octal) and Posix ACL[1], its security key if any, and its security descriptor if verbose output.</p>
<dt><code>-r[v]</code> <i>volume</i> <i>directory</i></p>
<dd>displays the security parameters of all files and subdirectories in <i>directory</i> : their interpreted Linux mode (rwx flags in octal) and Posix ACL[1], their security key if any, and their security descriptor if verbose output.</p>
<dt><code>-b[v] </code><i>volume</i> <i>[directory]</i></p>
<dd>Recursively extracts to standard output the NTFS ACLs of files in <i>volume</i> and <i>directory</i>.</p>
<dt><code>-s[ev]</code> <i>volume</i> <i>[backup-file]</i></p>
<dd>Sets the NTFS ACLS as indicated in <i>backup-file</i> or standard input. The input data must have been created on Linux. With option <code>-e</code>, also sets extra parameters (currently Windows attrib).</p>
<dt><i>volume</i> <i>perms</i> <i>file</i></p>
<dd>Sets the security parameters of file to perms. Perms is the Linux requested mode (rwx flags, expressed in octal form as in chmod) or a Posix ACL[1] (expressed like in setfacl -m). This sets a new ACL which is effective for Linux and Windows.</p>
<dt><code>-r[v]</code> <i>volume</i> <i>perms</i> <i>directory</i></p>
<dd>Sets the security parameters of all files and subdirectories in <i>directory</i> to <i>perms</i>. Perms is the Linux requested mode (rwx flags, expressed in octal form as in <code>chmod</code>), or a Posix ACL[1] (expressed like in <code>setfacl -m</code>.) This sets new ACLs which are effective for Linux and Windows.</p>
<dt><code>[-v]</code> <i>mounted-file</i></p>
<dd>Displays the security parameters of <i>mounted-file</i> : its interpreted Linux mode (rwx flags in octal) and Posix ACL[1], its security key if any, and its security descriptor if verbose output. This is a special case which acts on a mounted file (or directory) and does not require being root. The Posix ACL interpretation can only be displayed if the full path to <i>mounted-file</i> from the root of the global file tree is provided.</p>
<dt><code>-u[v]</code> <i>mounted-file</i></p>
<dd>Displays a proposed contents for a user mapping file, based on the ownership parameters set by Windows on <i>mounted-file</i>, assuming this file was created on Windows by the user who should be mapped to the current Linux user. The displayed information has to be copied to the file <code>.NTFS-3G/UserMapping</code> where <code>.NTFS-3G</code> is a hidden subdirectory of the root of the partition for which the mapping is to be defined. This will cause the ownership of files created on that partition to be the same as the original <i>mounted-file</i>.</dl>
<h2>Note</h2>
<p>[1] provided the POSIX ACL option was selected at compile time. A Posix ACL specification looks like &quot;<code>[d:]{ugmo}:[id]:[perms],&#8230;</code>&quot; where id is a numeric user or group id, and perms an octal digit or a set from the letters r, w and x.</p>
<dl>
<dd>Example : &quot;<code>u::7,g::5,o:0,u:510:rwx,g:500:5,d:u:510:7</code>&quot;</dl>
<h2>Examples</h2>
<p>Audit the global security data on /dev/sda1</p>
<dl>
<dd><code>ntfs-3g.secaudit -ar /dev/sda1</code></dl>
<p> Display the ownership and permissions parameters for files in directory /audio/music on device /dev/sda5, excluding sub-directories :</p>
<dl>
<dd><code>ntfs-3g.secaudit /dev/sda5 /audio/music</code></dl>
<p> Set all files in directory /audio/music on device /dev/sda5 as writeable by owner and read-only for everybody :</p>
<dl>
<dd><code>ntfs-3g.secaudit -r /dev/sda5 644 /audio/music</code> </p>
<h2>Exit Codes</h2>
<p><code>ntfs-3g.secaudit</code> exits with a value of 0 when no error was detected, and with a value of 1 when an error was detected.</p>
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
