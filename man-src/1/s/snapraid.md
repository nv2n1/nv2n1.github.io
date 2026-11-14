---
title: "snapraid(1)"
name: "snapraid"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snapraid/"
description: "snapraid – SnapRAID Backup For Disk Arrays"
---

<h2>NAME</h2>
<p> snapraid &#8211; SnapRAID Backup For Disk Arrays</p>
<h2>SYNOPSIS</h2>
<p> snapraid [-c, &#8211;conf CONFIG] </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-f, &#8211;filter PATTERN] [-d, &#8211;filter-disk NAME]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-m, &#8211;filter-missing] [-e, &#8211;filter-error]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-a, &#8211;audit-only] [-h, &#8211;pre-hash] [-i, &#8211;import DIR]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-p, &#8211;plan PERC|bad|new|full]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-o, &#8211;older-than DAYS] [-l, &#8211;log FILE]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-Z, &#8211;force-zero] [-E, &#8211;force-empty]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-U, &#8211;force-uuid] [-D, &#8211;force-device]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-N, &#8211;force-nocopy] [-F, &#8211;force-full]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-S, &#8211;start BLKSTART] [-B, &#8211;count BLKCOUNT]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-L, &#8211;error-limit NUMBER]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[-v, &#8211;verbose] [-q, &#8211;quiet]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>status|smart|up|down|diff|sync|scrub|fix|check|list|dup</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>|up|down|pool|devices|touch|rehash</p>
<p> snapraid [-V, &#8211;version] [-H, &#8211;help] [-C, &#8211;gen-conf CONTENT] </p>
<h2>DESCRIPTION</h2>
<p> SnapRAID is a backup program for disk arrays. It stores parity information of your data and it recovers from up to six disk failures. </p>
<p> SnapRAID is mainly targeted for a home media center, with a lot of big files that rarely change. </p>
<p> Beside the ability to recover from disk failures, other features of SnapRAID are:</p>
<dl>
<dt>&bull;</p>
<dd> All your data is hashed to ensure data integrity and to avoid silent corruption.</p>
<dt>&bull;</p>
<dd> If the failed disks are too many to allow a recovery, you lose the data only on the failed disks. All the data in the other disks is safe.</p>
<dt>&bull;</p>
<dd> If you accidentally delete some files in a disk, you can recover them.</p>
<dt>&bull;</p>
<dd> You can start with already filled disks.</p>
<dt>&bull;</p>
<dd> The disks can have different sizes.</p>
<dt>&bull;</p>
<dd> You can add disks at any time.</p>
<dt>&bull;</p>
<dd> It doesn&#8217;t lock-in your data. You can stop using SnapRAID at any time without the need to reformat or move data.</p>
<dt>&bull;</p>
<dd> To access a file, a single disk needs to spin, saving power and producing less noise.</dl>
<p> The official site of SnapRAID is: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.snapraid.it/">http://www.snapraid.it/</a> </p>
</dl>
<h2>LIMITATIONS</h2>
<p> SnapRAID is in between a RAID and a Backup program trying to get the best benefits of them. Although it also has some limitations that you should consider before using it. </p>
<p> The main one is that if a disk fails, and you haven&#8217;t recently synced, you may be unable to do a complete recover. More specifically, you may be unable to recover up to the size of the amount of the changed or deleted files from the last sync operation. This happens even if the files changed or deleted are not in the failed disk. This is the reason because SnapRAID is better suited for data that rarely change. </p>
<p> Instead the new added files don&#8217;t prevent the recovering of the already existing files. You may only lose the just added files, if they are on the failed disk. </p>
<p> Other limitations are:</p>
<dl>
<dt>&bull;</p>
<dd> You have different file-systems for each disk. Using a RAID you have only a big file-system.</p>
<dt>&bull;</p>
<dd> It doesn&#8217;t stripe data. With RAID you get a speed boost with striping.</p>
<dt>&bull;</p>
<dd> It doesn&#8217;t support real-time recovery. With RAID you do not have to stop working when a disk fails.</p>
<dt>&bull;</p>
<dd> It&#8217;s able to recover damages only from a limited number of disks. With a Backup you are able to recover from a complete failure of the whole disk array.</p>
<dt>&bull;</p>
<dd> Only file, time-stamps, symlinks and hardlinks are saved. Permissions, ownership and extended attributes are not saved.</dl>
<h2>GETTING STARTED</h2>
<p> To use SnapRAID you need to first select one disk of your disk array to dedicate at the &quot;parity&quot; information. With one disk for parity you will be able to recover from a single disk failure, like RAID5. </p>
<p> If you want to be able to recover from more disk failures, like RAID6, you must reserve additional disks for parity. Any additional parity disk allow to recover from one more disk failure. </p>
<p> As parity disks, you have to pick the biggest disks in the array, as the parity information may grow in size as the biggest data disk in the array. </p>
<p> These disks will be dedicated to store the &quot;parity&quot; files. You should not store your data in them. </p>
<p> Then you have to define the &quot;data&quot; disks that you want to protect with SnapRAID. The protection is more effective if these disks contain data that rarely change. For this reason it&#8217;s better to DO NOT include the Windows C:\ disk, or the Unix /home, /var and /tmp disks. </p>
<p> The list of files is saved in the &quot;content&quot; files, usually stored in the data, parity or boot disks. These files contain the details of your backup, with all the check-sums to verify its integrity. The &quot;content&quot; file is stored in multiple copies, and each one must be in a different disk, to ensure that in even in case of multiple disk failures at least one copy is available. </p>
<p> For example, suppose that you are interested only at one parity level of protection, and that your disks are present in: </p>
<dl>
<dt>
<dd> /mnt/diskp &lt;- selected disk for parity </p>
<p> /mnt/disk1 &lt;- first disk to protect </p>
<p> /mnt/disk2 &lt;- second disk to protect </p>
<p> /mnt/disk3 &lt;- third disk to protect </p>
</dl>
<p> you have to create the configuration file /etc/snapraid.conf with the following options: </p>
<dl>
<dt>
<dd> parity /mnt/diskp/snapraid.parity </p>
<p> content /var/snapraid/snapraid.content </p>
<p> content /mnt/disk1/snapraid.content </p>
<p> content /mnt/disk2/snapraid.content </p>
<p> data d1 /mnt/disk1/ </p>
<p> data d2 /mnt/disk2/ </p>
<p> data d3 /mnt/disk3/ </p>
</dl>
<p> If you are in Windows, you should use the Windows path format, with drive letters and backslashes instead of slashes. </p>
<dl>
<dt>
<dd> parity E:\snapraid.parity </p>
<p> content C:\snapraid\snapraid.content </p>
<p> content F:rray\snapraid.content </p>
<p> content G:rray\snapraid.content </p>
<p> data d1 F:rray\ </p>
<p> data d2 G:rray\ </p>
<p> data d3 H:rray\ </p>
</dl>
<p> If you have many disks, and you run out of drive letters, you can mount disks directly in sub folders. See: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.google.com/search?q=Windows+mount+point">https://www.google.com/search?q=Windows+mount+point</a> </p>
</dl>
<p> At this point you are ready to start the &quot;sync&quot; command to build the parity information. </p>
<dl>
<dt>
<dd> snapraid sync </p>
</dl>
<p> This process may take some hours the first time, depending on the size of the data already present in the disks. If the disks are empty the process is immediate. </p>
<p> You can stop it at any time pressing Ctrl+C, and at the next run it will start where interrupted. </p>
<p> When this command completes, your data is SAFE. </p>
<p> Now you can start using your array as you like, and periodically update the parity information running the &quot;sync&quot; command.</p>
<h3>Scrubbing</h3>
<p> To periodically check the data and parity for errors, you can run the &quot;scrub&quot; command. </p>
<dl>
<dt>
<dd> snapraid scrub </p>
</dl>
<p> This command verifies the data in your array comparing it with the hash computed in the &quot;sync&quot; command. </p>
<p> Every run of the command checks about the 8% of the array, but not data already scrubbed in the previous 10 days. You can use the -p, &#8211;plan option to specify a different amount, and the -o, &#8211;older-than option to specify a different age in days. For example, to check 5% of the array older than 20 days use: </p>
<dl>
<dt>
<dd> snapraid -p 5 -o 20 scrub </p>
</dl>
<p> If during the process, silent or input/output errors are found, the corresponding blocks are marked as bad in the &quot;content&quot; file, and listed in the &quot;status&quot; command. </p>
<dl>
<dt>
<dd> snapraid status </p>
</dl>
<p> To fix them, you can use the &quot;fix&quot; command filtering for bad blocks with the -e, &#8211;filter-error options: </p>
<dl>
<dt>
<dd> snapraid -e fix </p>
</dl>
<p> At the next &quot;scrub&quot; the errors will disappear from the &quot;status&quot; report if really fixed. To make it fast, you can use -p bad to scrub only blocks marked as bad. </p>
<dl>
<dt>
<dd> snapraid -p bad scrub </p>
</dl>
<p> Take care that running &quot;scrub&quot; on a not synced array may result in errors caused by removed or modified files. These errors are reported in the &quot;scrub&quot; result, but related blocks are not marked as bad.</p>
<h3>Pooling</h3>
<p> To have all the files in your array shown in the same directory tree, you can enable the &quot;pooling&quot; feature. It consists in creating a read-only virtual view of all the files in your array using symbolic links. </p>
<p> You can configure the &quot;pooling&quot; directory in the configuration file with: </p>
<dl>
<dt>
<dd> pool /pool </p>
</dl>
<p> or, if you are in Windows, with: </p>
<dl>
<dt>
<dd> pool C:\pool </p>
</dl>
<p> and then run the &quot;pool&quot; command to create or update the virtual view. </p>
<dl>
<dt>
<dd> snapraid pool </p>
</dl>
<p> If you are using a Unix platform and you want to share such directory in the network to either Windows or Unix machines, you should add to your /etc/samba/smb.conf the following options: </p>
<dl>
<dt>
<dd> # In the global section of smb.conf </p>
<p> unix extensions = no </p>
</dl>
<dl>
<dt>
<dd> # In the share section of smb.conf </p>
<p> [pool] </p>
<p> comment = Pool </p>
<p> path = /pool </p>
<p> read only = yes </p>
<p> guest ok = yes </p>
<p> wide links = yes </p>
<p> follow symlinks = yes </p>
</dl>
<p> In Windows the same sharing operation is not so straightforward, because Windows shares the symbolic links as they are, and that requires the network clients to resolve them remotely. </p>
<p> To make it working, besides sharing in the network the pool directory, you must also share all the disks independently, using as share points the disk names as defined in the configuration file. You must also specify in the &quot;share&quot; option of the configure file, the Windows UNC path that remote clients needs to use to access such shared disks. </p>
<p> For example, operating from a server named &quot;darkstar&quot;, you can use the options: </p>
<dl>
<dt>
<dd> data d1 F:rray\ </p>
<p> data d2 G:rray\ </p>
<p> data d3 H:rray\ </p>
<p> pool C:\pool </p>
<p> share \darkstar </p>
</dl>
<p> and share the following dirs in the network: </p>
<dl>
<dt>
<dd> \darkstar\pool -&gt; C:\pool </p>
<p> \darkstar\d1 -&gt; F:rray </p>
<p> \darkstar\d2 -&gt; G:rray </p>
<p> \darkstar\d3 -&gt; H:rray </p>
</dl>
<p> to allow remote clients to access all the files at \darkstar\pool. </p>
<p> You may also need to configure remote clients enablinh access at remote symlinks with the command: </p>
<dl>
<dt>
<dd> fsutil behavior set SymlinkEvaluation L2L:1 R2R:1 L2R:1 R2L:1 </p>
</dl>
<h3>Undeleting</h3>
<p> SnapRAID is more like a backup program than a RAID system, and it can be used to restore or undelete files to their previous state using the -f, &#8211;filter option : </p>
<dl>
<dt>
<dd> snapraid fix -f FILE </p>
</dl>
<p> or for a directory: </p>
<dl>
<dt>
<dd> snapraid fix -f DIR/ </p>
</dl>
<p> You can also use it to recover only accidentally deleted files inside a directory using the -m, &#8211;filter-missing option, that restores only missing files, leaving untouched all the others. </p>
<dl>
<dt>
<dd> snapraid fix -m -f DIR/ </p>
</dl>
<p> Or to recover all the deleted files in all the drives with: </p>
<dl>
<dt>
<dd> snapraid fix -m </p>
</dl>
<h3>Recovering</h3>
<p> The worst happened, and you lost a disk! </p>
<p> DO NOT PANIC! You will be able to recover it! </p>
<p> The first thing you have to do is to avoid further changes at you disk array. Disable any remote connection to it, any scheduled process, including any scheduled SnapRAID nightly sync or scrub. </p>
<p> Then proceed with the following steps.</p>
<h3>STEP 1 -&gt; Reconfigure</h3>
<p> You need some space to recover, even better if you already have an additional disk, but in case, also an external USB or remote disk is enough. </p>
<p> Change the SnapRAID configuration file to make the &quot;disk&quot; option of the failed disk to point to the place where you have enough empty space to recover the files. </p>
<p> For example, if you have that disk &quot;d1&quot; failed, you can change from: </p>
<dl>
<dt>
<dd> data d1 /mnt/disk1/ </p>
</dl>
<p> to: </p>
<dl>
<dt>
<dd> data d1 /mnt/new_spare_disk/ </p>
</dl>
<h3>STEP 2 -&gt; Fix</h3>
<p> Run the fix command, storing the log in an external file with: </p>
<dl>
<dt>
<dd> snapraid -d NAME -l fix.log fix </p>
</dl>
<p> Where NAME is the name of the disk, like &quot;d1&quot; as in our previous example. </p>
<p> This command will take a long time. </p>
<p> Take care that you need also few gigabytes free to store the fix.log file. Run it from a disk with some free space. </p>
<p> Now you have recovered all the recoverable. If some file is partially or totally unrecoverable, it will be renamed adding the &quot;.unrecoverable&quot; extension. </p>
<p> You can get a detailed list of all the unrecoverable blocks in the fix.log file checking all the lines starting with &quot;unrecoverable:&quot; </p>
<p> If you are not satisfied of the recovering, you can retry it as many time you wish. </p>
<p> For example, if you have removed files from the array after the last &quot;sync&quot;, this may result in some other files not recovered. In this case, you can retry the &quot;fix&quot; using the -i, &#8211;import option, specifying where these files are now, to include them again in the recovering process. </p>
<p> If you are satisfied of the recovering, you can now proceed further, but take care that after syncing you cannot retry the &quot;fix&quot; command anymore!</p>
<h3>STEP 3 -&gt; Check</h3>
<p> As paranoid check, you can now run a &quot;check&quot; command to ensure that everything is OK on the recovered disk. </p>
<dl>
<dt>
<dd> snapraid -d NAME -a check </p>
</dl>
<p> Where NAME is the name of the disk, like &quot;d1&quot; as in our previous example. </p>
<p> The options -d and -a tell SnapRAID to check only the specified disk, and ignore all the parity data. </p>
<p> This command will take a long time, but if you are not paranoid, you can skip it.</p>
<h3>STEP 4 -&gt; Sync</h3>
<p> Run the &quot;sync&quot; command to resynchronize the array with the new disk. </p>
<dl>
<dt>
<dd> snapraid sync </p>
</dl>
<p> If everything is recovered, this command is immediate.</p>
<h2>COMMANDS</h2>
<p> SnapRAID provides a few simple commands that allow to:</p>
<dl>
<dt>&bull;</p>
<dd> Prints the status of the array -&gt; &quot;status&quot;</p>
<dt>&bull;</p>
<dd> Controls the disks -&gt; &quot;smart&quot;, &quot;up&quot;, &quot;down&quot;</p>
<dt>&bull;</p>
<dd> Makes a backup/snapshot -&gt; &quot;sync&quot;</p>
<dt>&bull;</p>
<dd> Periodically checks data -&gt; &quot;scrub&quot;</p>
<dt>&bull;</p>
<dd> Restore the last backup/snapshot -&gt; &quot;fix&quot;.</dl>
<p> Take care that the commands have to be written in lower case.</p>
<h3>status</h3>
<p> Prints a summary of the state of the disk array. </p>
<p> It includes information about the parity fragmentation, how old are the blocks without checking, and all the recorded silent errors encountered while scrubbing. </p>
<p> Note that the information presented refers at the latest time you run &quot;sync&quot;. Later modifications are not taken into account. </p>
<p> If bad blocks were detected, their block numbers are listed. To fix them, you can use the &quot;fix -e&quot; command. </p>
<p> It also shows a graph representing the the last time each block was scrubbed or synced. Scrubbed blocks are shown with &#8216;*&#8217;, blocks synced but not yet scrubbed with &#8216;o&#8217;. </p>
<p> Nothing is modified.</p>
<h3>smart</h3>
<p> Prints a SMART report of all the disks of the array. </p>
<p> It includes an estimation of the probability of failure in the next year allowing to plan maintenance replacements of the disks that show suspicious attributes. </p>
<p> This probability estimation obtained correlating the SMART attributes of the disks, with the Backblaze data available at: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.backblaze.com/hard-drive-test-data.html">https://www.backblaze.com/hard-drive-test-data.html</a> </p>
</dl>
<p> If SMART reports that a disk is failing, &quot;FAIL&quot; or &quot;PREFAIL&quot; is printed for that disk, and SnapRAID returns with an error. In this case an immediate replacement of the disk is highly recommended. </p>
<p> Other possible strings are:</p>
<dl>
<dt>
<dd>
<dl>
<dt> <i>logfail</i></p>
<dd>In the past some attributes were lower than the threshold.</p>
<dt> <i>logerr</i></p>
<dd>The device error log contains errors.</p>
<dt> <i>selferr</i></p>
<dd>The device self-test log contains errors.</dl>
</dl>
<p> If the -v, &#8211;verbose option is specified a deeper statistical analysis is provided. This analysis can help you to decide if you need more or less parity. </p>
<p> This command uses the &quot;smartctl&quot; tool, and it&#8217;s equivalent to run &quot;smartctl -a&quot; on all the devices. </p>
<p> If your devices are not auto-detected correctly, you can configure a custom command using the &quot;smartctl&quot; option in the configuration file. </p>
<p> Nothing is modified.</p>
<h3>up</h3>
<p> Spins up all the disks of the array. </p>
<p> You can spin-up only some specific disks using the -d, &#8211;filter-disk option. </p>
<p> Nothing is modified.</p>
<h3>down</h3>
<p> Spins down all the disks of the array. </p>
<p> This command uses the &quot;smartctl&quot; tool, and it&#8217;s equivalent to run &quot;smartctl -s standby,now&quot; on all the devices. </p>
<p> You can spin-down only some specific disks using the -d, &#8211;filter-disk option. </p>
<p> Nothing is modified.</p>
<h3>diff</h3>
<p> Lists all the files modified from the last &quot;sync&quot; that need to have their parity data recomputed. </p>
<p> This command doesn&#8217;t check the file data, but only the file time-stamp size and inode. </p>
<p> At the end of the command, you&#8217;ll get a summary of the file changes grouped by:</p>
<dl>
<dt>
<dd>
<dl>
<dt> <i>equal</i></p>
<dd>Files equal at before.</p>
<dt> <i>added</i></p>
<dd>Files added that were not present before.</p>
<dt> <i>removed</i></p>
<dd>Files removed.</p>
<dt> <i>updated</i></p>
<dd>Files with a different size or time-stamp, meaning that they were modified.</p>
<dt> <i>moved</i></p>
<dd>Files moved to a different directory of the same disk. They are identified by having the same name, size, time-stamp and inode, but different directory.</p>
<dt> <i>copied</i></p>
<dd>Files copied in the same or different disk. Note that if in true they are moved to a different disk, you&#8217;ll also have them counted in &quot;removed&quot;. They are identified by having the same name, size, and time-stamp. But if the sub-second time-stamp is zero, then the full path should match, and not only the name.</p>
<dt> <i>restored</i></p>
<dd>Files with a different inode but with name, size and time-stamp matching. These are usually files restored after being deleted.</dl>
</dl>
<p> If a &quot;sync&quot; is required, the process return code is 2, instead of the default 0. The return code 1 is instead for a generic error condition. </p>
<p> Nothing is modified.</p>
<h3>sync</h3>
<p> Updates the parity information. All the modified files in the disk array are read, and the corresponding parity data is updated. </p>
<p> You can stop this process at any time pressing Ctrl+C, without losing the work already done. At the next run the &quot;sync&quot; process will start where interrupted. </p>
<p> If during the process, silent or input/output errors are found, the corresponding blocks are marked as bad. </p>
<p> Files are identified by path and/or inode and checked by size and time-stamp. If the file size or time-stamp are different, the parity data is recomputed for the whole file. If the file is moved or renamed in the same disk, keeping the same inode, the parity is not recomputed. If the file is moved to another disk, the parity is recomputed, but the previously computed hash information is kept. </p>
<p> The &quot;content&quot; and &quot;parity&quot; files are modified if necessary. The files in the array are NOT modified.</p>
<h3>scrub</h3>
<p> Scrubs the array, checking for silent or input/output errors in data and parity disks. </p>
<p> For each command invocation, about the 8% of the array is checked, but nothing that was already scrubbed in the last 10 days. This means that scrubbing once a week, every bit of data is checked at least one time every three months. </p>
<p> You can define a different scrub plan or amount using the -p, &#8211;plan option that takes as argument: bad &#8211; Scrub blocks marked bad. new &#8211; Scrub just synced blocks not yet scrubbed. full &#8211; Scrub everything. 0-100 &#8211; Scrub the exact percentage of blocks. </p>
<p> If you specify a percentage amount, you can also use the -o, &#8211;older-than option to define how old the block should be. The oldest blocks are scrubbed first ensuring an optimal check. If instead you want to scrub the just synced blocks, not yet scrubbed, you should use the &quot;-p new&quot; option. </p>
<p> To get the details of the scrub status use the &quot;status&quot; command. </p>
<p> For any silent or input/output error found the corresponding blocks are marked as bad in the &quot;content&quot; file. These bad blocks are listed in &quot;status&quot;, and can be fixed with &quot;fix -e&quot;. After the fix, at the next scrub they will be rechecked, and if found corrected, the bad mark will be removed. To scrub only the bad blocks, you can use the &quot;scrub -p bad&quot; command. </p>
<p> It&#8217;s recommended to run &quot;scrub&quot; only on a synced array, to avoid to have reported error caused by unsynced data. These errors are recognized as not being silent errors, and the blocks are not marked as bad, but such errors are reported in the output of the command. </p>
<p> Files are identified only by path, and not by inode. </p>
<p> The &quot;content&quot; file is modified to update the time of the last check of each block, and to mark bad blocks. The &quot;parity&quot; files are NOT modified. The files in the array are NOT modified.</p>
<h3>fix</h3>
<p> Fix all the files and the parity data. </p>
<p> All the files and the parity data are compared with the snapshot state saved in the last &quot;sync&quot;. If a difference is found, it&#8217;s reverted to the stored snapshot. </p>
<p> The &quot;fix&quot; command doesn&#8217;t differentiate between errors and intentional modifications. It unconditionally reverts the file state at the last &quot;sync&quot;. </p>
<p> If no other option is specified the full array is processed. Use the filter options to select a subset of files or disks to operate on. </p>
<p> To only fix the blocks marked bad during &quot;sync&quot; and &quot;scrub&quot;, use the -e, &#8211;filter-error option. As difference from other filter options, with this one the fixes are applied only to files that are not modified from the the latest &quot;sync&quot;. </p>
<p> All the files that cannot be fixed are renamed adding the &quot;.unrecoverable&quot; extension. </p>
<p> Before fixing, the full array is scanned to find any moved file, after the last &quot;sync&quot; operation. These files are identified by their time-stamp, ignoring their name and directory, and are used in the recovering process if necessary. If you moved some of them outside the array, you can use the -i, &#8211;import option to specify additional directories to scan. </p>
<p> Files are identified only by path, and not by inode. </p>
<p> The &quot;content&quot; file is NOT modified. The &quot;parity&quot; files are modified if necessary. The files in the array are modified if necessary.</p>
<h3>check</h3>
<p> Verify all the files and the parity data. </p>
<p> It works like &quot;fix&quot;, but it only simulates a recovery and no change is written in the array. </p>
<p> This command is mostly intended for manual verifications, like after a recovery process or in other special conditions. For periodic and scheduled checks uses &quot;scrub&quot;. </p>
<p> If you use the -a, &#8211;audit-only option, only the file data is checked, and the parity data is ignored for a faster run. </p>
<p> Files are identified only by path, and not by inode. </p>
<p> Nothing is modified.</p>
<h3>list</h3>
<p> Lists all the files contained in the array at the time of the last &quot;sync&quot;. </p>
<p> Nothing is modified.</p>
<h3>dup</h3>
<p> Lists all the duplicate files. Two files are assumed equal if their hashes are matching. The file data is not read, but only the precomputed hashes are used. </p>
<p> Nothing is modified.</p>
<h3>up</h3>
<p> Spins up all the disks of the array. </p>
<p> Nothing is modified.</p>
<h3>down</h3>
<p> Spins down all the disks of the array. </p>
<p> Nothing is modified.</p>
<h3>pool</h3>
<p> Creates or updates in the &quot;pooling&quot; directory a virtual view of all the files of your disk array. </p>
<p> The files are not really copied here, but just linked using symbolic links. </p>
<p> When updating, all the present symbolic links and empty subdirectories are deleted and replaced with the new view of the array. Any other regular file is left in place. </p>
<p> Nothing is modified outside the pool directory.</p>
<h3>devices</h3>
<p> Prints the low level devices used by the array. </p>
<p> This command prints the devices associations in place in the array, and it&#8217;s mainly intended as a script interface. </p>
<p> The first two columns are the low level device id and path. The next two columns are the high level device id and path. The latest column if the disk name in the array. </p>
<p> In most cases you have one low level device for each disk in the array, but in some more complex configurations, you may have multiple low level devices used by a single disk in the array. </p>
<p> Nothing is modified.</p>
<h3>touch</h3>
<p> Sets arbitrarely the sub-second timestamp of all the files that have it at zero. </p>
<p> This improves the SnapRAID capability to recognize moved and copied files as it makes the timestamp almost unique, removing possible duplicates. </p>
<p> More specifically, if the sub-second timestamp is not zero, a moved or copied file is identified as such if it matches the name, size and timestamp. If instead the sub-second timestamp is zero, it&#8217;s cosidered a copy only if it matches the full path, size and timestamp. </p>
<p> Note that the second precision timestamp is not modified, and all the dates and times of your files will be maintained.</p>
<h3>rehash</h3>
<p> Schedules a rehash of the whole array. </p>
<p> This command changes the hash kind used, typically when upgrading from a 32 bits system to a 64 bits one, to switch from MurmurHash3 to the faster SpookyHash. </p>
<p> If you are already using the optimal hash, this command does nothing and tells you that nothing has to be done. </p>
<p> The rehash isn&#8217;t done immediately, but it takes place progressively during &quot;sync&quot; and &quot;scrub&quot;. </p>
<p> You can get the rehash state using &quot;status&quot;. </p>
<p> During the rehash, SnapRAID maintains full functionality, with the only exception of &quot;dup&quot; not able to detect duplicated files using a different hash.</p>
<h2>OPTIONS</h2>
<p> SnapRAID provides the following options:</p>
<dl>
<dt><code>-c, &#8211;conf CONFIG</code></p>
<dd> Selects the configuration file. If not specified it&#8217;s assumed the file &quot;/etc/snapraid.conf&quot; in Unix, and &quot;snapraid.conf&quot; in the current directory in Windows.</p>
<dt><code>-f, &#8211;filter PATTERN</code></p>
<dd> Filters the files to process in &quot;check&quot; and &quot;fix&quot;. Only the files matching the entered pattern are processed. This option can be used many times. See the PATTERN section for more details in the pattern specifications. In Unix, ensure to quote globbing chars if used. This option can be used only with &quot;check&quot; and &quot;fix&quot;. Note that it cannot be used with &quot;sync&quot; and &quot;scrub&quot;, because they always process the whole array.</p>
<dt><code>-d, &#8211;filter-disk NAME</code></p>
<dd> Filters the disks to process in &quot;check&quot;, &quot;fix&quot;, &quot;up&quot; and &quot;down&quot;. You must specify a disk name as named in the configuration file. You can also specify parity disks with the names: &quot;parity&quot;, &quot;2-parity&quot;, &quot;3-parity&quot;, &#8230; to limit the operations a specific parity disk. If you combine more &#8211;filter, &#8211;filter-disk and &#8211;filter-missing options, only files matching all the set of filters are selected. This option can be used many times. This option can be used only with &quot;check&quot;, &quot;fix&quot;, &quot;up&quot; and &quot;down&quot;. Note that it cannot be used with &quot;sync&quot; and &quot;scrub&quot;, because they always process the whole array.</p>
<dt><code>-m, &#8211;filter-missing</code></p>
<dd> Filters the files to process in &quot;check&quot; and &quot;fix&quot;. Only the files missing/deleted from the array are processed. When used with &quot;fix&quot;, this is a kind of &quot;undelete&quot; command. If you combine more &#8211;filter, &#8211;filter-disk and &#8211;filter-missing options, only files matching all the set of filters are selected. This option can be used only with &quot;check&quot; and &quot;fix&quot;. Note that it cannot be used with &quot;sync&quot; and &quot;scrub&quot;, because they always process the whole array.</p>
<dt><code>-e, &#8211;filter-error</code></p>
<dd> Filters the blocks to process in &quot;check&quot; and &quot;fix&quot;. It processes only the blocks marked with silent or input/output errors during &quot;sync&quot; and &quot;scrub&quot;, and listed in &quot;status&quot;. This option can be used only with &quot;check&quot; and &quot;fix&quot;.</p>
<dt><code>-p, &#8211;plan PERC|bad|new|full</code></p>
<dd> Selects the scrub plan. If PERC is a numeric value from 0 to 100, it&#8217;s interpreted as the percentage of blocks to scrub. Instead of a percentage, you can also specify a plan: &quot;bad&quot; scrubs bad blocks, &quot;new&quot; the blocks not yet scrubbed, and &quot;full&quot; for everything. This option can be used only with &quot;scrub&quot;.</p>
<dt><code>-o, &#8211;older-than DAYS</code></p>
<dd> Selects the older the part of the array to process in &quot;scrub&quot;. DAYS is the minimum age in days for a block to be scrubbed, default is 10. Blocks marked as bad are always scrubbed despite this option. This option can be used only with &quot;scrub&quot;.</p>
<dt><code>-a, &#8211;audit-only</code></p>
<dd> In &quot;check&quot; verifies the hash of the files without doing any kind of check on the parity data. If you are interested in checking only the file data this option can speedup a lot the checking process. This option can be used only with &quot;check&quot;.</p>
<dt><code>-h, &#8211;pre-hash</code></p>
<dd> In &quot;sync&quot; runs a preliminary hashing phase of all the new data to have an additional verification before the parity computation. Usually in &quot;sync&quot; no preliminary hashing is done, and the new data is hashed just before the parity computation when it&#8217;s read for the first time. Unfortunately, this process happens when the system is under heavy load, with all disks spinning and with a busy CPU. This is an extreme condition for the machine, and if it has a latent hardware problem, it&#8217;s possible to encounter silent errors what cannot be detected because the data is not yet hashed. To avoid this risk, you can enable the &quot;pre-hash&quot; mode and have all the data read two times to ensure its integrity. This option also verifies the files moved inside the array, to ensure that the move operation went successfully, and in case to block the sync and to allow to run a fix operation. This option can be used only with &quot;sync&quot;.</p>
<dt><code>-i, &#8211;import DIR</code></p>
<dd> Imports from the specified directory any file that you deleted from the array after the last &quot;sync&quot;. If you still have such files, they could be used by &quot;check&quot; and &quot;fix&quot; to improve the recover process. The files are read also in subdirectories and they are identified regardless of their name. This option can be used only with &quot;check&quot; and &quot;fix&quot;.</p>
<dt><code>-Z, &#8211;force-zero</code></p>
<dd> Forces the insecure operation of syncing a file with zero size that before was not. If SnapRAID detects a such condition, it stops proceeding unless you specify this option. This allows to easily detect when after a system crash, some accessed files were truncated. This is a possible condition in Linux with the ext3/ext4 file-systems. This option can be used only with &quot;sync&quot;.</p>
<dt><code>-E, &#8211;force-empty</code></p>
<dd> Forces the insecure operation of syncing a disk with all the original files missing. If SnapRAID detects that all the files originally present in the disk are missing or rewritten, it stops proceeding unless you specify this option. This allows to easily detect when a data file-system is not mounted. This option can be used only with &quot;sync&quot;.</p>
<dt><code>-U, &#8211;force-uuid</code></p>
<dd> Forces the insecure operation of syncing, checking and fixing with disks that have changed their UUID. If SnapRAID detects that some disks have changed UUID, it stops proceeding unless you specify this option. This allows to detect when your disks are mounted in the wrong mount points. It&#8217;s anyway allowed to have a single UUID change with single parity, and more with multiple parity, because it&#8217;s the normal case of replacing disks after a recovery. This option can be used only with &quot;sync&quot;, &quot;check&quot; or &quot;fix&quot;.</p>
<dt><code>-D, &#8211;force-device</code></p>
<dd> Forces the insecure operation of fixing with inaccessible disks, or with disks on the same physical device. Like if you lost two data disks, and you have a spare disk to recover only the first one, and you want to ignore the second inaccessible disk. Or if you want to recover a disk in the free space left in an already used disk, sharing the same physical device. This option can be used only with &quot;fix&quot;.</p>
<dt><code>-N, &#8211;force-nocopy</code></p>
<dd> In &quot;sync&quot;, &quot;check and &quot;fix&quot;, disables the copy detection heuristic. Without this option SnapRAID assumes that files with same attributes, like name, size and time-stamp are copies with the same data. This allows to identify copied or moved files from one disk to another, and to reuse the already computed hash information to detect silent errors or to recover missing files. This behavior, in some rare cases, may result in false positives, or in a slow process due the many hash verifications, and this option allows to resolve them. This option can be used only with &quot;sync&quot;, &quot;check&quot; and &quot;fix&quot;.</p>
<dt><code>-F, &#8211;force-full</code></p>
<dd> In &quot;sync&quot; forces a full rebuild of the parity. This option can be used when you reverted back to an old content file, but using a more recent parity data. Instead of recomputing the parity from scratch, this allows to reuse the hashes present in the content file to validate data, and to maintain data protection during the &quot;sync&quot; process using the old content file and the parity data you have. This option can be used only with &quot;sync&quot;.</p>
<dt><code>-l, &#8211;log FILE</code></p>
<dd> Write a detailed log in the specified file. If this option is not specified, unexpected errors are printed on the screen, likely resulting in too much output in case of many errors. When -l, &#8211;log is specified, on the screen, go only fatal errors that makes SnapRAID to stop progress. If the path starts with &#8216;&gt;&gt;&#8217; the file is opened in append mode. Occurrences of &#8216;%D&#8217; and &#8216;%T&#8217; in the name are replaced with the date and time in the format YYYYMMDD and HHMMSS. Note that in Windows batch files, you&#8217;ll have to double the &#8216;%&#8217; char, like result-%%D.log. And to use &#8216;&gt;&gt;&#8217; you&#8217;ll have to enclose the name in &quot;, like &quot;&gt;&gt;result.log&quot;. To output the log to standard output or standard error, you can use respectively &quot;&gt;&amp;1&quot; and &quot;&gt;&amp;2&quot;.</p>
<dt><code>-L, &#8211;error-limit</code></p>
<dd> Sets a new error limit before stopping execution. By default SnapRAID stops if it encounters more than 100 Input/Output errors, meaning that likely a disk is going to die. This options affects &quot;sync&quot; and &quot;scrub&quot;, that are allowed to continue after the first bunch of disk errors, to try to complete at most their operations. Instead, &quot;check&quot; and &quot;fix&quot; always stop at the first error.</p>
<dt><code>-S, &#8211;start BLKSTART</code></p>
<dd> Starts the processing from the specified block number. It could be useful to retry to check or fix some specific block, in case of a damaged disk. It&#8217;s present mainly for advanced manual recovering.</p>
<dt><code>-B, &#8211;count BLKCOUNT</code></p>
<dd> Processes only the specified number of blocks. It&#8217;s present mainly for advanced manual recovering.</p>
<dt><code>-C, &#8211;gen-conf CONTENT_FILE</code></p>
<dd> Generates a dummy configuration file from an existing content file. The configuration file is written in the standard output, and it doesn&#8217;t overwrite an existing one. This configuration file also contains the information needed to reconstruct the disk mount points, in case you lose the entire system.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Prints more information on the screen. If specified one time, it prints excluded files and more stats. This option has no effect on the log files.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Prints less information on the screen. If specified one time, removes the progress bar, if two times, the running operations, three times, the info messages, four times the status messages. Fatal errors are always printed on the screen. This option has no effect on the log files.</p>
<dt><code>-H, &#8211;help</code></p>
<dd> Prints a short help screen.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Prints the program version.</dl>
<h2>CONFIGURATION</h2>
<p> SnapRAID requires a configuration file to know where your disk array is located, and where storing the parity information. </p>
<p> This configuration file is located in /etc/snapraid.conf in Unix or in the execution directory in Windows. </p>
<p> It should contain the following options (case sensitive):</p>
<h3>parity FILE</h3>
<p> Defines the file to use to store the parity information. The parity enables the protection from a single disk failure, like RAID5. </p>
<p> It must be placed in a disk dedicated for this purpose with as much free space as the biggest disk in the array. Leaving the parity disk reserved for only this file ensures that it doesn&#8217;t get fragmented, improving the performance. </p>
<p> This option is mandatory and it can be used only one time.</p>
<h3>[2,3,4,5,6]-parity FILE</h3>
<p> Defines the files to use to store extra parity information. For each parity file specified, one additional level of protection is enabled:</p>
<dl>
<dt>&bull;</p>
<dd> 2-parity enables RAID6 double parity.</p>
<dt>&bull;</p>
<dd> 3-parity enables triple parity</p>
<dt>&bull;</p>
<dd> 4-parity enables quad parity</p>
<dt>&bull;</p>
<dd> 5-parity enables penta (five) parity</p>
<dt>&bull;</p>
<dd> 6-parity enables hexa (six) parity</dl>
<p> Each parity level requires also all the files of the previous levels. </p>
<p> Each file must be placed in a disk dedicated for this purpose with as much free space as the biggest disk in the array. Leaving the parity disks reserved for only these files ensures that they doesn&#8217;t get fragmented, improving the performance. </p>
<p> These options are optional and they can be used only one time.</p>
<h3>z-parity FILE</h3>
<p> Defines an alternate file and format to store the triple parity. </p>
<p> This option is an alternative at &#8216;3-parity&#8217; mainly intended for low-end CPUs like ARM or AMD Phenom, Athlon and Opteron that don&#8217;t support the SSSE3 instructions set, and in such case it provides a better performance. </p>
<p> This format is similar, but faster, at the one used by the ZFS RAIDZ3, but it doesn&#8217;t work beyond triple parity. </p>
<p> When using &#8216;3-parity&#8217; you will be warned if it&#8217;s recommended to use the &#8216;z-parity&#8217; format for a performance improvement. </p>
<p> It&#8217;s possible to convert from one format to another, adjusting the configuration file with the wanted z-parity or 3-parity file, and using &#8216;fix&#8217; to recreate it.</p>
<h3>content FILE</h3>
<p> Defines the file to use to store the list and check-sums of all the files present in your disk array. </p>
<p> It can be placed in the disk used to store data, parity, or any other disk available. If you use a data disk, this file is automatically excluded from the &quot;sync&quot; process. </p>
<p> This option is mandatory and it can be used more times to save more copies of the same files. </p>
<p> You have to store at least one copy for each parity disk used plus one. Using some more doesn&#8217;t hurt.</p>
<h3>data NAME DIR</h3>
<p> Defines the name and the mount point of the data disks of the array. NAME is used to identify the disk, and it must be unique. DIR is the mount point of the disk in the file-system. </p>
<p> You can change the mount point as you like, as long you keep the NAME fixed. </p>
<p> You should use one option for each data disk of the array. </p>
<p> You can rename later a disk, changing the NAME directly in the configuration file, and then run a &#8216;sync&#8217; command. In the rename case, the association is done using the stored UUID of the disks.</p>
<h3>nohidden</h3>
<p> Excludes all the hidden files and directory. In Unix hidden files are the ones starting with &quot;.&quot;. In Windows they are the ones with the hidden attribute.</p>
<h3>exclude/include PATTERN</h3>
<p> Defines the file or directory patterns to exclude and include in the sync process. All the patterns are processed in the specified order. </p>
<p> If the first pattern that matches is an &quot;exclude&quot; one, the file is excluded. If it&#8217;s an &quot;include&quot; one, the file is included. If no pattern matches, the file is excluded if the last pattern specified is an &quot;include&quot;, or included if the last pattern specified is an &quot;exclude&quot;. </p>
<p> See the PATTERN section for more details in the pattern specifications. </p>
<p> This option can be used many times.</p>
<h3>blocksize SIZE_IN_KIBIBYTES</h3>
<p> Defines the basic block size in kibi bytes of the parity. One kibi bytes is 1024 bytes. The default blocksize is 256 and it should work for most cases. </p>
<p> A reason to use a different blocksize is if your system has less than 4 GiB of memory. As a rule of thumb, with 4 GiB or more memory use the default 256, with 2 GiB use 512, and with 1 GiB use 1024. </p>
<p> In more details SnapRAID requires about TS*17/BS bytes of RAM memory. Where TS is the total size in bytes of your disk array, and BS is the block size in bytes. </p>
<p> For example with 8 disks of 4 TB and a block size of 256 KiB (1 KiB = 1024 bytes) you have: </p>
<p> RAM = (8 * 4 * 10^12) * 17 / (256 * 2^10) = 1.9 GiB </p>
<p> Another reason to use a different blocksize is if you have a lot of small files. In the order of many millions. </p>
<p> For each file, even of few bytes, a whole block of parity is allocated, and with many files this may result in a lot of unused parity space. And when you completely fill the parity disk, you are not allowed to add more files in the data disks. Anyway, the wasted parity doesn&#8217;t sum between data disks. Wasted space resulting from a high number of files in a data disk, limits only the amount of data in such data disk and not in others. </p>
<p> As approximation, you can assume that half of the block size is wasted for each file. For example, with 100000 files and a 256 KiB block size, you are going to waste 13 GB of parity, that may result in 13 GB less space available in the data disk. </p>
<p> You can get the amount of wasted space in each disk using &quot;status&quot;. This is the amount of space that you must leave free in the data disks, or use for files not included in the array. If this value is negative, it means that your are near to fill the parity, and it represents the space you can still waste. </p>
<p> To avoid the problem, you can use a bigger partition for parity. For example, if you have the parity partition bigger than 13 GB than data disks, you have enough extra space to handle up to 100000 files in each data disk. </p>
<p> A trick to get a bigger parity partition in Linux, is to format it with the command: </p>
<dl>
<dt>
<dd> mkfs.ext4 -m 0 -T largefile4 DEVICE </p>
</dl>
<p> This results in about 1.5% of extra space. Meaning about 60 GB for a 4 TB disk, that allows about 460000 files in each data disk without any wasted space.</p>
<h3>autosave SIZE_IN_GIGABYTES</h3>
<p> Automatically save the state when syncing or scrubbing after the specified amount of GB processed. This option is useful to avoid to restart from scratch long &quot;sync&quot; commands interrupted by a machine crash, or any other event that may interrupt SnapRAID.</p>
<h3>pool DIR</h3>
<p> Defines the pooling directory where the virtual view of the disk array is created using the &quot;pool&quot; command. </p>
<p> The directory must already exist.</p>
<h3>share UNC_DIR</h3>
<p> Defines the Windows UNC path required to access the disks remotely. </p>
<p> If this option is specified, the symbolic links created in the pool directory use this UNC path to access the disks. Without this option the symbolic links generated use only local paths, not allowing to share the pool directory in the network. </p>
<p> The symbolic links are formed using the specified UNC path, adding the disk name as specified in the &quot;disk&quot; option, and finally adding the file dir and name. </p>
<p> This option is only required for Windows.</p>
<h3>smartctl DISK/PARITY OPTIONS&#8230;</h3>
<p> Defines a custom smartctl command to obtain the SMART attributes for each disk. This may be required for RAID controllers and for some USB disk that cannot be auto-detected. </p>
<p> DISK is the same disk name specified in the &quot;disk&quot; option. PARITY is one of the parity name as &quot;parity,[1,2,3,4,5,6,z]-parity&quot;. </p>
<p> In the specified OPTIONS, the &quot;%s&quot; string is replaced by the device name. Note that in case of RAID controllers the device is likely fixed, and you don&#8217;t have to use &quot;%s&quot;. </p>
<p> Refers at the smartmontools documentation about the possible options: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.smartmontools.org/wiki/Supported_RAID-Controllers">https://www.smartmontools.org/wiki/Supported_RAID-Controllers</a> </p>
<p> <a rel="nofollow" href="https://www.smartmontools.org/wiki/Supported_USB-Devices">https://www.smartmontools.org/wiki/Supported_USB-Devices</a> </p>
</dl>
<h3>Examples</h3>
<p> An example of a typical configuration for Unix is: </p>
<dl>
<dt>
<dd> parity /mnt/diskp/snapraid.parity </p>
<p> content /mnt/diskp/snapraid.content </p>
<p> content /var/snapraid/snapraid.content </p>
<p> data d1 /mnt/disk1/ </p>
<p> data d2 /mnt/disk2/ </p>
<p> data d3 /mnt/disk3/ </p>
<p> exclude /lost+found/ </p>
<p> exclude /tmp/ </p>
<p> smartctl d1 -d sat %s </p>
<p> smartctl d2 -d usbjmicron %s </p>
<p> smartctl parity -d areca,1/1 /dev/sg0 </p>
<p> smartctl 2-parity -d areca,2/1 /dev/sg0 </p>
</dl>
<p> An example of a typical configuration for Windows is: </p>
<dl>
<dt>
<dd> parity E:\snapraid.parity </p>
<p> content E:\snapraid.content </p>
<p> content C:\snapraid\snapraid.content </p>
<p> data d1 G:rray\ </p>
<p> data d2 H:rray\ </p>
<p> data d3 I:rray\ </p>
<p> exclude Thumbs.db </p>
<p> exclude \$RECYCLE.BIN </p>
<p> exclude \System Volume Information </p>
<p> smartctl d1 -d sat %s </p>
<p> smartctl d2 -d usbjmicron %s </p>
<p> smartctl parity -d areca,1/1 /dev/arcmsr0 </p>
<p> smartctl 2-parity -d areca,2/1 /dev/arcmsr0 </p>
</dl>
<h2>PATTERN</h2>
<p> Patterns are used to select a subset of files to exclude or include in the process. </p>
<p> There are four different types of patterns:</p>
<dl>
<dt><code>FILE</code></p>
<dd> Selects any file named as FILE. You can use any globbing character like * and ?. This pattern is applied only to files and not to directories.</p>
<dt><code>DIR/</code></p>
<dd> Selects any directory named DIR and everything inside. You can use any globbing character like * and ?. This pattern is applied only to directories and not to files.</p>
<dt><code>/PATH/FILE</code></p>
<dd> Selects the exact specified file path. You can use any globbing character like * and ? but they never match a directory slash. This pattern is applied only to files and not to directories.</p>
<dt><code>/PATH/DIR/</code></p>
<dd> Selects the exact specified directory path and everything inside. You can use any globbing character like * and ? but they never match a directory slash. This pattern is applied only to directories and not to files.</dl>
<p> Note that when you specify an absolute path starting with /, it&#8217;s applied at the array root dir and not at the local file-system root dir. </p>
<p> In Windows you can use the backslash \ instead of the forward slash /. Note that Windows system directories, junctions, mount points, and any other Windows special directory are treated just as files, meaning that to exclude them you must use a file rule, and not a directory one. </p>
<p> In the configuration file, you can use different strategies to filter the files to process. The simplest one is to use only &quot;exclude&quot; rules to remove all the files and directories you do not want to process. For example: </p>
<dl>
<dt>
<dd> # Excludes any file named &quot;*.unrecoverable&quot; </p>
<p> exclude *.unrecoverable </p>
<p> # Excludes the root directory &quot;/lost+found&quot; </p>
<p> exclude /lost+found/ </p>
<p> # Excludes any sub-directory named &quot;tmp&quot; </p>
<p> exclude tmp/ </p>
</dl>
<p> The opposite way is to define only the file you want to process, using only &quot;include&quot; rules. For example: </p>
<dl>
<dt>
<dd> # Includes only some directories </p>
<p> include /movies/ </p>
<p> include /musics/ </p>
<p> include /pictures/ </p>
</dl>
<p> The final way, is to mix &quot;exclude&quot; and &quot;include&quot; rules. In this case take care that the order of rules is important. Previous rules have the precedence over the later ones. To get things simpler you can first have all the &quot;exclude&quot; rules and then all the &quot;include&quot; ones. For example: </p>
<dl>
<dt>
<dd> # Excludes any file named &quot;*.unrecoverable&quot; </p>
<p> exclude *.unrecoverable </p>
<p> # Excludes any sub-directory named &quot;tmp&quot; </p>
<p> exclude tmp/ </p>
<p> # Includes only some directories </p>
<p> include /movies/ </p>
<p> include /musics/ </p>
<p> include /pictures/ </p>
</dl>
<p> On the command line, using the -f option, you can only use &quot;include&quot; patterns. For example: </p>
<dl>
<dt>
<dd> # Checks only the .mp3 files. </p>
<p> # Note the &quot;&quot; use to avoid globbing expansion by the shell in Unix. </p>
<p> snapraid -f &quot;*.mp3&quot; check </p>
</dl>
<p> In Unix, when using globbing chars in the command line, you have to quote them. Otherwise the shell will try to expand them.</p>
<h2>CONTENT</h2>
<p> SnapRAID stores the list and check-sums of your files in the content file. </p>
<p> It&#8217;s a binary file, listing all the files present in your disk array, with all the check-sums to verify their integrity. </p>
<p> This file is read and written by the &quot;sync&quot; and &quot;scrub&quot; commands, and read by &quot;fix&quot;, &quot;check&quot; and &quot;status&quot;.</p>
<h2>PARITY</h2>
<p> SnapRAID stores the parity information of your array in the parity files. </p>
<p> They are binary files, containing the computed parity of all the blocks defined in the &quot;content&quot; file. </p>
<p> These files are read and written by the &quot;sync&quot; and &quot;fix&quot; commands, and only read by &quot;scrub&quot; and &quot;check&quot;.</p>
<h2>ENCODING</h2>
<p> SnapRAID in Unix ignores any encoding. It reads and stores the file names with the same encoding used by the file-system. </p>
<p> In Windows all the names read from the file-system are converted and processed in the UTF-8 format. </p>
<p> To have the file names printed correctly you have to set the Windows console in the UTF-8 mode, with the command &quot;chcp 65001&quot;, and use a TrueType font like &quot;Lucida Console&quot; as console font. Note that it has effect only on the printed file names, if you redirect the console output to a file, the resulting file is always in the UTF-8 format.</p>
<h2>COPYRIGHT</h2>
<p> This file is Copyright (C) 2011 Andrea Mazzoleni</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rsync/">rsync</a>(1) </p>
<h2>Index</h2>
