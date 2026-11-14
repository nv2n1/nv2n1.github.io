---
title: "rear(8)"
name: "rear"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rear/"
description: "rear – bare metal disaster recovery and system migration tool"
---

<p>rear &#8211; bare metal disaster recovery and system migration tool</p>
<h2>Synopsis</h2>
<p><code>rear</code> [<code>-dDsSvV</code>] [<code>-r</code> <i>KERNEL</i>] <i>COMMAND</i> [&#8211; <i>ARGS</i>&#8230;]</p>
<h2>Description</h2>
<p>Relax-and-Recover is the leading Open Source disaster recovery solution. It is a modular framework with many ready-to-go workflows for common situations. </p>
<p> Relax-and-Recover produces a bootable image. This image can repartition the system. Once that is done it initiates a restore from backup. Restores to different hardware are possible. Relax-and-Recover can therefore be used as a migration tool as well. </p>
<p> Currently Relax-and-Recover supports various boot media (incl. ISO, PXE, OBDR tape, USB or eSATA storage), a variety of network protocols (incl. sftp, ftp, http, nfs, cifs) for storage and backup as well as a multitude of backup strategies (incl. IBM Tivoli Storage Manager, HP DataProtector, Symantec NetBackup, EMC NetWorker, Bareos, Bacula, rsync, rbme). This results in a bootable image that os capable of booting via PXE, DVD/CD, bootable tape or virtual provisioning. </p>
<p> Relax-and-Recover was designed to be easy to set up, requires no maintenance and is there to assist when disaster strikes. Its setup-and-forget nature removes any excuses for not having a disaster recovery solution implemented. </p>
<p> Recovering from disaster is made very straight-forward by a 2-step recovery process so that it can be executed by operational teams when required. When used interactively (e.g. when used for migrating systems), menus help make decisions to restore to a new (hardware) environment. </p>
<p> Extending Relax-and-Recover is made possible by its modular framework. Consistent logging and optionally extended output help understand the concepts behind Relax-and-Recover and help debug during development. </p>
<p> Relax-and-Recover comes with ABSOLUTELY NO WARRANTY; for details see the GNU General Public License at: m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></code>m[]</p>
<h2>Options</h2>
<h3>Global Options</h3>
<p>-d</p>
<dl>
<dd><code>debug mode</code> (log debug messages to log file)</dl>
<p> -D</p>
<dl>
<dd><code>debugscript mode</code> (log every function call)</dl>
<p> -r KERNEL</p>
<dl>
<dd>kernel version to use (by default use running kernel)</dl>
<p> -s</p>
<dl>
<dd><code>simulation mode</code> (show what scripts rear would include)</dl>
<p> -S</p>
<dl>
<dd><code>step-by-step mode</code> (acknowledge each script individually)</dl>
<p> -v</p>
<dl>
<dd><code>verbose mode</code> (show progress output)</dl>
<p> -V</p>
<dl>
<dd>version information</dl>
<h3>Commands</h3>
<p><code>checklayout</code></p>
<dl>
<dd>check if the disk layout has changed since the last run of mkbackup/mkrescue</dl>
<p> <code>dump</code></p>
<dl>
<dd>dump configuration and system information; please run this to verify your setup</dl>
<p> <code>format</code></p>
<dl>
<dd>format and label USB or tape media to be used with rear; </p>
<p> first argument is the USB or tape device to use, eg. <i>/dev/sdX</i> or <i>/dev/stX</i></dl>
<p> <code>help</code></p>
<dl>
<dd>print full list of commands and options</dl>
<p> <code>mkbackup</code></p>
<dl>
<dd>create rescue media and backup the system (only for internal backup methods)</dl>
<p> <code>mkbackuponly</code></p>
<dl>
<dd>backup the system (only for internal backup methods) without creating rescue media</dl>
<p> <code>mkrescue</code></p>
<dl>
<dd>create rescue media only</dl>
<p> <code>recover</code></p>
<dl>
<dd>recover the system; can be used only when running from the rescue media</dl>
<p> <code>validate</code></p>
<dl>
<dd>submit validation information</dl>
<p> Use <i>rear -v help</i> for more advanced commands.</p>
<h2>Background Information</h2>
<p>The process of bare metal disaster recovery consists of two parts: </p>
<dl>
<dd>&bull; Recreate the system layout</dl>
<dl>
<dd>&bull; Restore the data to the system</dl>
<p> Most backup software solutions are very good at restoring data but do not support recreating the system layout. Relax-and-Recover is very good at recreating the system layout but works best when used together with supported backup software. </p>
<p> In this combination Relax-and-Recover recreates the system layout and calls the backup software to restore the actual data. Thus there is no unnessecary duplicate data storage and the Relax-and-Recover rescue media can be very small. </p>
<p> For demonstration and special use purposes Relax-and-Recover also includes an internal backup method, NETFS, which can be used to create a simple tar.gz archive of the system. For all permanent setups we recommend using something more professional for backup, either a traditional backup software (open source or commercial) or rsync with hardlink based solutions, e.g. RSYNC BACKUP MADE EASY.</p>
<h2>Rescue Image Configuration</h2>
<p>The OUTPUT variable defines how from where our rescue image will be booted and the OUTPUT_URL variable defines where the rescue image should be send to. Possible OUTPUT setting are: </p>
<p> OUTPUT=<code>RAMDISK</code></p>
<dl>
<dd>Create only the Relax-and-Recover initramfs.</dl>
<p> OUTPUT=<code>ISO</code></p>
<dl>
<dd><code>(Default)</code> Create a bootable ISO9660 image on disk as <i>rear-$(hostname).iso</i></dl>
<p> OUTPUT=<code>PXE</code></p>
<dl>
<dd>Create on a remote PXE/NFS server the required files (such as configuration file, kernel and initrd image</dl>
<p> OUTPUT=<code>OBDR</code></p>
<dl>
<dd>Create a bootable OBDR tape (optionally including the backup archive). Specify the OBDR tape device by using TAPE_DEVICE.</dl>
<p> OUTPUT=<code>USB</code></p>
<dl>
<dd>Create a bootable USB disk (using extlinux). Specify the USB storage device by using USB_DEVICE.</dl>
<p> When using OUTPUT=ISO, RAMDISK, OBDR or USB you should provide the backup target location through the OUTPUT_URL variable. Possible OUTPUT_URL settings are: </p>
<p> OUTPUT_URL=<code>file://</code></p>
<dl>
<dd>Write the image to disk. The default is in <i>/var/lib/rear/output/</i>.</dl>
<p> OUTPUT_URL=<code>fish://</code></p>
<dl>
<dd>Write the image using lftp and the FISH protocol.</dl>
<p> OUTPUT_URL=<code>ftp://</code></p>
<dl>
<dd>Write the image using lftp and the FTP protocol.</dl>
<p> OUTPUT_URL=<code>ftps://</code></p>
<dl>
<dd>Write the image using lftp and the FTPS protocol.</dl>
<p> OUTPUT_URL=<code>hftp://</code></p>
<dl>
<dd>Write the image using lftp and the HFTP protocol.</dl>
<p> OUTPUT_URL=<code>http://</code></p>
<dl>
<dd>Write the image using lftp and the HTTP (PUT) procotol.</dl>
<p> OUTPUT_URL=<code>https://</code></p>
<dl>
<dd>Write the image using lftp and the HTTPS (PUT) protocol.</dl>
<p> OUTPUT_URL=<code>sftp://</code></p>
<dl>
<dd>Write the image using lftp and the secure FTP (SFTP) protocol.</dl>
<p> OUTPUT_URL=<code>rsync://</code></p>
<dl>
<dd>Write the image using rsync and the RSYNC protocol (SSH only).</dl>
<p> OUTPUT_URL=<code>sshfs://</code></p>
<dl>
<dd>Write the image using sshfs and the SSH protocol.</dl>
<p> OUTPUT_URL=<code>null</code></p>
<dl>
<dd>Do not copy the ISO image from <i>/var/lib/rear/output/</i> to an external destination. Useful in combination with an <i>external</i> backup program, or when BACKUP_URL=<a href="iso://backup">iso://backup</a></dl>
<h2>Backup Software Integration</h2>
<p>Currently Relax-and-Recover supports the following backup methods. Please distinguish carefully between Relax-and-Recover support for 3rd party backup software and Relax-and-Recover internal backup methods. The latter also creates a backup of your data while the former will only integrate Relax-and-Recover with the backup software to restore the data with the help of the backup software without actually creating backups. This means that for all non-internal backup software you <code>must</code> take care of creating backups yourself. </p>
<p> Especially the rear mkbackup command can be confusing as it is only useful for the internal backup methods and has no function at all with the other (external) backup methods. </p>
<p> The following backup methods need to be set in Relax-and-Recover with the BACKUP option. As mentioned we have two types of BACKUP methods &#8211; <i>internal</i> and <i>external</i>. </p>
<p> The following BACKUP methods are <i>external</i> of Relax-and-Recover meaning that you are responsible of backups being made: </p>
<p> BACKUP=<code>REQUESTRESTORE</code></p>
<dl>
<dd><code>(default)</code> Not really a backup method at all, Relax-and-Recover simply halts the recovery and requests that somebody will restore the data to the appropriate location (e.g. via SSH). This method works especially well with an rsync bases backup that is pushed back to the backup client.</dl>
<p> BACKUP=<code>EXTERNAL</code></p>
<dl>
<dd>Internal backup method that uses an arbitrary external command to create a backup and restore the data.</dl>
<p> BACKUP=<code>DP</code></p>
<dl>
<dd>Use HP Data Protector to restore the data.</dl>
<p> BACKUP=<code>GALAXY</code></p>
<dl>
<dd>Use CommVault Galaxy 5 to restore the data.</dl>
<p> BACKUP=<code>GALAXY7</code></p>
<dl>
<dd>Use CommVault Galaxy 7 to restore the data.</dl>
<p> BACKUP=<code>GALAXY10</code></p>
<dl>
<dd>Use CommVault Galaxy 10 (or Simpana 10) to restore the data.</dl>
<p> BACKUP=<code>NBU</code></p>
<dl>
<dd>Use Symantec NetBackup to restore the data.</dl>
<p> BACKUP=<code>TSM</code></p>
<dl>
<dd>Use IBM Tivoli Storage Manager to restore the data. The Relax-and-Recover result files (e.g. ISO image) are also saved into TSM.</dl>
<p> BACKUP=<code>NSR</code></p>
<dl>
<dd>Using EMC NetWorker (Legato) to restore the data.</dl>
<p> BACKUP=<code>SESAM</code></p>
<dl>
<dd>Using SEP Sesam to restore the data.</dl>
<p> BACKUP=<code>RBME</code></p>
<dl>
<dd>Use Rsync Backup Made Easy (rbme) to restore the data.</dl>
<p> BACKUP=<code>BAREOS</code></p>
<dl>
<dd>Use Open Source backup solution BAREOS (a fork a BUCULA) to restore the data.</dl>
<p> BACKUP=<code>BACULA</code></p>
<dl>
<dd>Use Open Source backup solution BACULA to restore the data.</dl>
<p> BACKUP=<code>DUPLICITY</code></p>
<dl>
<dd>Use encrypted bandwidth-efficient backup solution using the rsync algorithm to restore the data.</dl>
<p> The following BACKUP methods are <i>internal</i> of Relax-and-Recover: </p>
<p> BACKUP=<code>NETFS</code></p>
<dl>
<dd>Internal backup method which can be used to create a simple backup (tar archive).</dl>
<p> BACKUP=<code>RSYNC</code></p>
<dl>
<dd>Use rsync to restore data.</dl>
<p> If your favourite backup software is missing from this list, please submit a patch or ask us to implement it for you. </p>
<p> When using BACKUP=NETFS you should provide the backup target location through the BACKUP_URL variable. Possible BACKUP_URL settings are: </p>
<p> BACKUP_URL=<code>file://</code></p>
<dl>
<dd>To backup to local disk, use BACKUP_URL=file:///directory/path/</dl>
<p> BACKUP_URL=<code>nfs://</code></p>
<dl>
<dd>To backup to NFS disk, use BACKUP_URL=<a href="nfs://nfs-server-name/share/path">nfs://nfs-server-name/share/path</a></dl>
<p> BACKUP_URL=<code>tape://</code></p>
<dl>
<dd>To backup to tape device, use BACKUP_URL=<a href="tape:///dev/nst0">tape:///dev/nst0</a> or alternatively, simply define TAPE_DEVICE=/dev/nst0</dl>
<p> BACKUP_URL=<code>cifs://</code></p>
<dl>
<dd>To backup to a Samba share (CIFS), use BACKUP_URL=<a href="cifs://cifs-server-name/share/path.">cifs://cifs-server-name/share/path.</a> To provide credentials for CIFS mounting use a <i>/etc/rear/.cifs</i> credentials file and define BACKUP_OPTIONS=&quot;cred=/etc/rear/.cifs&quot; and pass along: </p>
<dl>
<dd>
<pre>username=_username_
password=_secret password_
domain=_domain_</pre>
</dl>
</dl>
<p> BACKUP_URL=<code>usb://</code></p>
<dl>
<dd>To backup to USB storage device, use BACKUP_URL=<a href="usb:///dev/disk/by-path/REAR-000">usb:///dev/disk/by-path/REAR-000</a> or use a real device node or a specific filesystem label. Alternatively, you can specify the device using USB_DEVICE=/dev/disk/by-path/REAR-000. </p>
<p> If you combine this with OUTPUT=USB you will end up with a bootable USB device.</dl>
<p> BACKUP_URL=<code>sshfs://</code></p>
<dl>
<dd>To backup to a remote server via sshfs (SSH protocol), use BACKUP_URL=<a href="sshfs://user@remote-system.domain.org/home/user/backup-dir/">sshfs://user@remote-system.domain.org/home/user/backup-dir/</a> </p>
<p> It is advisable to add <code>ServerAliveInterval 15</code> in the /root/.ssh/config file for the remote system (remote-system.domain.org).</dl>
<p> BACKUP_URL=<code>iso://</code></p>
<dl>
<dd>To include the backup within the ISO image. It is important that the BACKUP_URL and OUTPUT_URL variables are different. E.g. </p>
<dl>
<dd>
<pre>BACKUP_URL=<a href="iso:///backup/">iso:///backup/</a>
OUTPUT_URL=<a href="nfs://server/path/">nfs://server/path/</a></pre>
</dl>
</dl>
<p> When using BACKUP=NETFS there is an option to select a BACKUP_TYPE=incremental to have rear make incrementals until the next FULLBACKUPDAY=&quot;Mon&quot; has reached.</p>
<h2>Configuration</h2>
<p>To configure Relax-and-Recover you have to edit the configuration files in <i>/etc/rear/</i>. All <i>*.conf</i> files there are part of the configuration, but only <i>site.conf</i> and <i>local.conf</i> are intended for the user configuration. All other configuration files hold defaults for various distributions and should not be changed. </p>
<p> In <i>/etc/rear/templates/</i> there are also some template files which are used by Relax-and-Recover to create configuration files (mostly for the boot environment). Modify the templates to adjust the information contained in the emails produced by Relax-and-Recover. You can use these templates to prepend your own configurations to the configuration files created by Relax-and-recover, for example you can edit <i>PXE_pxelinux.cfg</i> to add some general pxelinux configuration you use. </p>
<p> In almost all circumstances you have to configure two main settings and their parameters: The backup method and the output method. </p>
<p> The backup method defines, how your data was saved and wether Relax-and-Recover should backup your data as part of the mkrescue process or wether you use an external application, e.g. backup software to archive your data. </p>
<p> The output method defines how the rescue system is written to disk and how you plan to boot the failed computer from the rescue system. </p>
<p> See the default configuration file <i>/usr/share/rear/conf/default.conf</i> for an overview of the possible methods and their options. </p>
<p> An example to use TSM for backup and ISO for output would be to add these lines to <i>/etc/rear/local.conf</i> (no need to define a BACKUP_URL when using an external backup solution): </p>
<dl>
<dd>
<pre>BACKUP=TSM
OUTPUT=ISO</pre>
</dl>
<p> And if all your systems use NTP for time synchronisation, you can also add these lines to <i>/etc/rear/site.conf</i> </p>
<dl>
<dd>
<pre>TIMESYNC=NTP</pre>
</dl>
<p> Do not forget to distribute the <i>site.conf</i> to all your systems. </p>
<p> The resulting ISO image will be created in <i>/var/lib/rear/output/</i>. You can now modify the behaviour by copying the appropriate configuration variables from <i>default.conf</i> to <i>local.conf</i> and changing them to suit your environment.</p>
<h2>Exit Status</h2>
<p>0</p>
<dl>
<dd>Successful program execution.</dl>
<p> &gt;0</p>
<dl>
<dd>Usage, syntax or execution errors. Check the log file in <i>/var/log/rear/</i> for more information.</dl>
<h2>Examples</h2>
<p>To print out the current settings for BACKUP and OUTPUT methods and some system information. This command can be used to see the supported features for the given release and platform. </p>
<dl>
<dd>
<pre># rear dump</pre>
</dl>
<p> To create a new rescue environment. Do not forget to copy the resulting rescue system away so that you can use it in the case of a system failure. </p>
<dl>
<dd>
<pre># rear -v mkrescue</pre>
</dl>
<p> To create a new rescue image together with a complete archive of your local system run the command: </p>
<dl>
<dd>
<pre># rear -v mkbackup</pre>
</dl>
<h2>Files</h2>
<p>/usr/sbin/rear</p>
<dl>
<dd>The program itself.</dl>
<p> /etc/rear/local.conf</p>
<dl>
<dd>System specific configuration can be set here.</dl>
<p> /etc/rear/site.conf</p>
<dl>
<dd>Site specific configuration can be set here (not created by default).</dl>
<p> /var/log/rear/</p>
<dl>
<dd>Directory holding the log files.</dl>
<p> /tmp/rear.####</p>
<dl>
<dd>Relax-and-Recover working directory. If Relax-and-Recover exits with an error, you must remove this directory manually.</dl>
<p> /usr/share/rear</p>
<dl>
<dd>Relax-and-Recover script components.</dl>
<p> /usr/share/rear/conf/default.conf</p>
<dl>
<dd>Relax-and-Recover default values. Contains a complete set of parameters and its explanation. Please do not edit or modify. Copy values to <i>local.conf</i> or <i>site.conf</i> instead.</dl>
<h2>Bugs</h2>
<p>Feedback is welcome, please report any issues or improvements to our issue-tracker at: m[blue]<code><a rel="nofollow" href="http://github.com/rear/issues/">http://github.com/rear/issues/</a></code>m[] </p>
<p> Furthermore, we welcome pull requests via GitHub.</p>
<h2>See Also</h2>
<p>Relax-and-Recover comes with extensive documentation located in <i>/usr/share/doc</i>.</p>
<h2>Authors</h2>
<p>Gratien Dhaese, Schlomo Schapiro, Jeroen Hoekx and Dag Wieers. </p>
<p> Lars Pinne (original man page). </p>
<p> Relax-and-Recover is a collaborative process using Github at: m[blue]<code><a rel="nofollow" href="http://github.com/rear/">http://github.com/rear/</a></code>m[] </p>
<p> The Relax-and-Recover website is located at: m[blue]<code><a rel="nofollow" href="http://relax-and-recover.org/">http://relax-and-recover.org/</a></code>m[]</p>
<h2>Copyright</h2>
<p>(c) 2006-2015 </p>
<p> Schlomo Schapiro </p>
<p> Gratien Dhaese, IT3 Consultants </p>
<p> Jeroen Hoekx </p>
<p> Dag Wieers, Dagit Linux Solutions </p>
<p> Relax-and-Recover comes with ABSOLUTELY NO WARRANTY; for details see the GNU General Public License at m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></code>m[]</p>
