---
title: "mdadm(5)"
name: "mdadm"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mdadm/"
description: "mdadm.conf – configuration for management of Software RAID with mdadm"
---

<p>mdadm.conf &#8211; configuration for management of Software RAID with mdadm</p>
<h2>Synopsis</h2>
<p>/etc/mdadm.conf</p>
<h2>Description</h2>
<p><i>mdadm</i> is a tool for creating, managing, and monitoring RAID devices using the <code>md</code> driver in Linux. Some common tasks, such as assembling all arrays, can be simplified by describing the devices and arrays in this configuration file.</p>
<h3>Syntax</h3>
<p>The file should be seen as a collection of words separated by white space (space, tab, or newline). Any word that beings with a hash sign (#) starts a comment and that word together with the remainder of the line is ignored. Spaces can be included in a word using quotation characters. Either single quotes (<code>&#8216;</code>) or double quotes (<code>&quot;</code>) may be used. All the characters from one quotation character to next identical character are protected and will not be used to separate words to start new quoted strings. To include a single quote it must be between double quotes. To include a double quote it must be between single quotes. Any line that starts with white space (space or tab) is treated as though it were a continuation of the previous line. Empty lines are ignored, but otherwise each (non continuation) line must start with a keyword as listed below. The keywords are case insensitive and can be abbreviated to 3 characters. The keywords are:</p>
<dl>
<dt><code>DEVICE</code></p>
<dd>A <code>device</code> line lists the devices (whole devices or partitions) that might contain a component of an MD array. When looking for the components of an array, <i>mdadm</i> will scan these devices (or any devices listed on the command line). The <code>device</code> line may contain a number of different devices (separated by spaces) and each device name can contain wild cards as defined by <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7). Also, there may be several device lines present in the file. Alternatively, a <code>device</code> line can contain either or both of the words <code>containers</code> and <code>partitions</code>. The word <code>containers</code> will cause <i>mdadm</i> to look for assembled CONTAINER arrays and included them as a source for assembling further arrays. The word <i>partitions</i> will cause <i>mdadm</i> to read <i>/proc/partitions</i> and include all devices and partitions found therein. <i>mdadm</i> does not use the names from <i>/proc/partitions</i> but only the major and minor device numbers. It scans <i>/dev</i> to find the name that matches the numbers. If no DEVICE line is present, then &quot;DEVICE partitions containers&quot; is assumed. For example:</p>
<dd>DEVICE /dev/hda* /dev/hdc*<br />
 DEV /dev/sd*<br />
 DEVICE /dev/disk/by-path/pci*<br />
 DEVICE partitions</p>
<dt><code>ARRAY</code></p>
<dd>The ARRAY lines identify actual arrays. The second word on the line may be the name of the device where the array is normally assembled, such as <code>/dev/md1</code> or <code>/dev/md/backup</code>. If the name does not start with a slash (&#8216;<code>/</code>&#8216;), it is treated as being in <code>/dev/md/</code>. Alternately the word <code>&lt;ignore&gt;</code> (complete with angle brackets) can be given in which case any array which matches the rest of the line will never be automatically assembled. If no device name is given, <i>mdadm</i> will use various heuristics to determine an appropriate name. Subsequent words identify the array, or identify the array as a member of a group. If multiple identities are given, then a component device must match ALL identities to be considered a match. Each identity word has a tag, and equals sign, and some value. The tags are:</p>
<dl>
<dd>
<dl>
<dt><code>uuid=</code></p>
<dd>The value should be a 128 bit uuid in hexadecimal, with punctuation interspersed if desired. This must match the uuid stored in the superblock.</p>
<dt><code>name=</code></p>
<dd>The value should be a simple textual name as was given to <i>mdadm</i> when the array was created. This must match the name stored in the superblock on a device for that device to be included in the array. Not all superblock formats support names.</p>
<dt><code>super-minor=</code></p>
<dd>The value is an integer which indicates the minor number that was stored in the superblock when the array was created. When an array is created as /dev/mdX, then the minor number X is stored.</p>
<dt><code>devices=</code></p>
<dd>The value is a comma separated list of device names or device name patterns. Only devices with names which match one entry in the list will be used to assemble the array. Note that the devices listed there must also be listed on a DEVICE line.</p>
<dt><code>level=</code></p>
<dd>The value is a RAID level. This is not normally used to identify an array, but is supported so that the output of <code>mdadm &#8211;examine &#8211;scan</code> can be use directly in the configuration file.</p>
<dt><code>num-devices=</code></p>
<dd>The value is the number of devices in a complete active array. As with <code>level=</code> this is mainly for compatibility with the output of <code>mdadm &#8211;examine &#8211;scan</code>.</p>
<dt><code>spares=</code></p>
<dd>The value is a number of spare devices to expect the array to have. The sole use of this keyword and value is as follows: <code>mdadm &#8211;monitor</code> will report an array if it is found to have fewer than this number of spares when <code>&#8211;monitor</code> starts or when <code>&#8211;oneshot</code> is used.</p>
<dt><code>spare-group=</code></p>
<dd>The value is a textual name for a group of arrays. All arrays with the same <code>spare-group</code> name are considered to be part of the same group. The significance of a group of arrays is that <i>mdadm</i> will, when monitoring the arrays, move a spare drive from one array in a group to another array in that group if the first array had a failed or missing drive but no spare.</p>
<dt><code>auto=</code></p>
<dd>This option is rarely needed with mdadm-3.0, particularly if use with the Linux kernel v2.6.28 or later. It tells <i>mdadm</i> whether to use partitionable array or non-partitionable arrays and, in the absence of <i>udev</i>, how many partition devices to create. From 2.6.28 all md array devices are partitionable, hence this option is not needed. The value of this option can be &quot;yes&quot; or &quot;md&quot; to indicate that a traditional, non-partitionable md array should be created, or &quot;mdp&quot;, &quot;part&quot; or &quot;partition&quot; to indicate that a partitionable md array (only available in linux 2.6 and later) should be used. This later set can also have a number appended to indicate how many partitions to create device files for, e.g. <code>auto=mdp5</code>. The default is 4.</p>
<dt><code>bitmap=</code></p>
<dd>The option specifies a file in which a write-intent bitmap should be found. When assembling the array, <i>mdadm</i> will provide this file to the <code>md</code> driver as the bitmap file. This has the same function as the <code>&#8211;bitmap-file</code> option to <code>&#8211;assemble</code>.</p>
<dt><code>metadata=</code></p>
<dd>Specify the metadata format that the array has. This is mainly recognised for comparability with the output of <code>mdadm -Es</code>.</p>
<dt><code>container=</code></p>
<dd>Specify that this array is a member array of some container. The value given can be either a path name in /dev, or a UUID of the container array.</p>
<dt><code>member=</code></p>
<dd>Specify that this array is a member array of some container. Each type of container has some way to enumerate member arrays, often a simple sequence number. The value identifies which member of a container the array is. It will usually accompany a &quot;container=&quot; word.</dl>
</dl>
<dt><code>MAILADDR</code></p>
<dd>The <code>mailaddr</code> line gives an E-mail address that alerts should be sent to when <i>mdadm</i> is running in <code>&#8211;monitor</code> mode (and was given the <code>&#8211;scan</code> option). There should only be one <code>MAILADDR</code> line and it should have only one address. Any subsequent addresses are silently ignored.</p>
<dt><code>MAILFROM</code></p>
<dd>The <code>mailfrom</code> line (which can only be abbreviated to at least 5 characters) gives an address to appear in the &quot;From&quot; address for alert mails. This can be useful if you want to explicitly set a domain, as the default from address is &quot;root&quot; with no domain. All words on this line are catenated with spaces to form the address. Note that this value cannot be set via the <i>mdadm</i> commandline. It is only settable via the config file.</p>
<dt><code>PROGRAM</code></p>
<dd>The <code>program</code> line gives the name of a program to be run when <code>mdadm &#8211;monitor</code> detects potentially interesting events on any of the arrays that it is monitoring. This program gets run with two or three arguments, they being the Event, the md device, and possibly the related component device. There should only be one <code>program</code> line and it should be give only one program.</p>
<dt><code>CREATE</code></p>
<dd>The <code>create</code> line gives default values to be used when creating arrays, new members of arrays, and device entries for arrays. These include:</p>
<dl>
<dd>
<dl>
<dt><code>owner=</code></p>
<dd>
<dt><code>group=</code></p>
<dd>These can give user/group ids or names to use instead of system defaults (root/wheel or root/disk).</p>
<dt><code>mode=</code></p>
<dd>An octal file mode such as 0660 can be given to override the default of 0600.</p>
<dt><code>auto=</code></p>
<dd>This corresponds to the <code>&#8211;auto</code> flag to mdadm. Give <code>yes</code>, <code>md</code>, <code>mdp</code>, <code>part</code> &#8212; possibly followed by a number of partitions &#8212; to indicate how missing device entries should be created.</p>
<dt><code>metadata=</code></p>
<dd>The name of the metadata format to use if none is explicitly given. This can be useful to impose a system-wide default of version-1 superblocks.</p>
<dt><code>symlinks=no</code></p>
<dd>Normally when creating devices in <code>/dev/md/</code> <i>mdadm</i> will create a matching symlink from <code>/dev/</code> with a name starting <code>md</code> or <code>md_</code>. Give <code>symlinks=no</code> to suppress this symlink creation.</p>
<dt><code>names=yes</code></p>
<dd>Since Linux 2.6.29 it has been possible to create <code>md</code> devices with a name like <code>md_home</code> rather than just a number, like <code>md3</code>. <i>mdadm</i> will use the numeric alternative by default as other tools that interact with md arrays may expect only numbers. If <code>names=yes</code> is given in <i>mdadm.conf</i> then <i>mdadm</i> will use a name when appropriate. If <code>names=no</code> is given, then non-numeric <i>md</i> device names will not be used even if the default changes in a future release of <i>mdadm</i>.</p>
<dt><code>bbl=no</code></p>
<dd>By default, <i>mdadm</i> will reserve space for a bad block list (bbl) on all devices included in or added to any array that supports them. Setting <code>bbl=no</code> will prevent this, so newly added devices will not have a bad block log.</dl>
</dl>
<dt><code>HOMEHOST</code></p>
<dd>The <code>homehost</code> line gives a default value for the <code>&#8211;homehost=</code> option to mdadm. There should normally be only one other word on the line. It should either be a host name, or one of the special words <code>&lt;system&gt;,</code> <code>&lt;none&gt;</code> and <code>&lt;ignore&gt;</code>. If <code>&lt;system&gt;</code> is given, then the <code>gethostname</code>(<code>2</code>) systemcall is used to get the host name. This is the default. If <code>&lt;ignore&gt;</code> is given, then a flag is set so that when arrays are being auto-assembled the checking of the recorded <i>homehost</i> is disabled. If <code>&lt;ignore&gt;</code> is given it is also possible to give an explicit name which will be used when creating arrays. This is the only case when there can be more that one other word on the <code>HOMEHOST</code> line. If there are other words, or other <code>HOMEHOST</code> lines, they are silently ignored. If <code>&lt;none&gt;</code> is given, then the default of using <code>gethostname</code>(<code>2</code>) is over-ridden and no homehost name is assumed. When arrays are created, this host name will be stored in the metadata. When arrays are assembled using auto-assembly, arrays which do not record the correct homehost name in their metadata will be assembled using a &quot;foreign&quot; name. A &quot;foreign&quot; name alway ends with a digit string preceded by an underscore to differentiate it from any possible local name. e.g. <code>/dev/md/1_1</code> or <code>/dev/md/home_0</code>.</p>
<dt><code>AUTO</code></p>
<dd>A list of names of metadata format can be given, each preceded by a plus or minus sign. Also the word <i>homehost</i> is allowed as is <i>all</i> preceded by plus or minus sign. <i>all</i> is usually last. When <i>mdadm</i> is auto-assembling an array, either via <i>&#8211;assemble</i> or <i>&#8211;incremental</i> and it finds metadata of a given type, it checks that metadata type against those listed in this line. The first match wins, where <i>all</i> matches anything. If a match is found that was preceded by a plus sign, the auto assembly is allowed. If the match was preceded by a minus sign, the auto assembly is disallowed. If no match is found, the auto assembly is allowed. If the metadata indicates that the array was created for <i>this</i> host, and the word <i>homehost</i> appears before any other match, then the array is treated as a valid candidate for auto-assembly. This can be used to disable all auto-assembly (so that only arrays explicitly listed in mdadm.conf or on the command line are assembled), or to disable assembly of certain metadata types which might be handled by other software. It can also be used to disable assembly of all foreign arrays &#8211; normally such arrays are assembled but given a non-deterministic name in <code>/dev/md/</code>. The known metadata types are <code>0.90</code>, <code>1.x</code>, <code>ddf</code>, <code>imsm</code>. <code>AUTO</code> should be given at most once. Subsequent lines are silently ignored. Thus an earlier config file in a config directory will over-ride the setting in a later config file.</p>
<dt><code>POLICY</code></p>
<dd>This is used to specify what automatic behavior is allowed on devices newly appearing in the system and provides a way of marking spares that can be moved to other arrays as well as the migration domains. <i>Domain</i> can be defined through <i>policy</i> line by specifying a domain name for a number of paths from <code>/dev/disk/by-path/</code>. A device may belong to several domains. The domain of an array is a union of domains of all devices in that array. A spare can be automatically moved from one array to another if the set of the destination array&#8217;s <i>domains</i> contains all the <i>domains</i> of the new disk or if both arrays have the same <i>spare-group</i>. To update hot plug configuration it is necessary to execute <code>mdadm &#8211;udev-rules</code> command after changing the config file Key words used in the <i>POLICY</i> line and supported values are:</p>
<dl>
<dd>
<dl>
<dt><code>domain=</code></p>
<dd>any arbitrary string</p>
<dt><code>metadata=</code></p>
<dd>0.9 1.x ddf or imsm</p>
<dt><code>path=</code></p>
<dd>file glob matching anything from <code>/dev/disk/by-path</code></p>
<dt><code>type=</code></p>
<dd>either <code>disk</code> or <code>part</code>.</p>
<dt><code>action=</code></p>
<dd>include, re-add, spare, spare-same-slot, or force-spare</p>
<dt><code>auto=</code></p>
<dd>yes, no, or homehost.  The <i>action</i> item determines the automatic behavior allowed for devices matching the <i>path</i> and <i>type</i> in the same line. If a device matches several lines with different <i>actions</i> then the most permissive will apply. The ordering of policy lines is irrelevant to the end result.</p>
<dl>
<dt><code>include</code></p>
<dd>allows adding a disk to an array if metadata on that disk matches that array</p>
<dt><code>re-add</code></p>
<dd>will include the device in the array if it appears to be a current member or a member that was recently removed and the array has a write-intent-bitmap to allow the <code>re-add</code> functionality.</p>
<dt><code>spare</code></p>
<dd>as above and additionally: if the device is bare it can become a spare if there is any array that it is a candidate for based on domains and metadata.</p>
<dt><code>spare-same-slot</code></p>
<dd>as above and additionally if given slot was used by an array that went degraded recently and the device plugged in has no metadata then it will be automatically added to that array (or it&#8217;s container)</p>
<dt><code>force-spare</code></p>
<dd>as above and the disk will become a spare in remaining cases</dl>
</dl>
<h2>Example</h2>
<p>DEVICE /dev/sd[bcdjkl]1<br />
 DEVICE /dev/hda1 /dev/hdb1 # /dev/md0 is known by its UUID.<br />
 ARRAY /dev/md0 UUID=3aaa0122:29827cfa:5331ad66:ca767371<br />
 # /dev/md1 contains all devices with a minor number of<br />
 # 1 in the superblock.<br />
 ARRAY /dev/md1 superminor=1<br />
 # /dev/md2 is made from precisely these two devices<br />
 ARRAY /dev/md2 devices=/dev/hda1,/dev/hdb1 # /dev/md4 and /dev/md5 are a spare-group and spares<br />
 # can be moved between them<br />
 ARRAY /dev/md4 uuid=b23f3c6d:aec43a9f:fd65db85:369432df </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>spare-group=group1<br />
 ARRAY /dev/md5 uuid=19464854:03f71b1b:e0df2edd:246cc977 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>spare-group=group1<br />
 # /dev/md/home is created if need to be a partitionable md array<br />
 # any spare device number is allocated.<br />
 ARRAY /dev/md/home UUID=9187a482:5dde19d9:eea3cc4a:d646ab8b </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>auto=part<br />
 # The name of this array contains a space.<br />
 ARRAY /dev/md9 name=&#8217;Data Storage&#8217; POLICY domain=domain1 metadata=imsm path=pci-0000:00:1f.2-scsi-* </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>action=spare<br />
 POLICY domain=domain1 metadata=imsm path=pci-0000:04:00.0-scsi-[01]* </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>action=include<br />
 # One domain comprising of devices attached to specified paths is defined.<br />
 # Bare device matching first path will be made an imsm spare on hot plug.<br />
 # If more than one array is created on devices belonging to domain1 and<br />
 # one of them becomes degraded, then any imsm spare matching any path for<br />
 # given domain name can be migrated.<br />
 MAILADDR root [at] mydomain.tld<br />
 PROGRAM /usr/sbin/handle-mdadm-events<br />
 CREATE group=system mode=0640 auto=part-8<br />
 HOMEHOST &lt;system&gt;<br />
 AUTO +1.x homehost -all </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mdadm/">mdadm</a></code>(8), <code><a href="/docs/linux/man/4-md/">md</a></code>(4). </p>
