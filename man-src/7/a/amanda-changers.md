---
title: "amanda-changers(7)"
name: "amanda-changers"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-changers/"
description: "amanda-changers – Configuring and Using Amanda Changers"
---

<p>amanda-changers &#8211; Configuring and Using Amanda Changers</p>
<h2>Description</h2>
<p>Amanda uses changers to arbitrate access to devices (<code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)) and data volumes. Changers provide an abstraction of tape robots, but are used to manage non-tape media, too. Amanda communicates with changers through the Changer API. This manpage contains a <i>user-level</i> overview of the API, and does not address details that are only of concern to developers. For that purpose, consult the Amanda source code and <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a></p>
<h2>Transition</h2>
<p>The Amanda Changer API is in transition from version 1.0 &#8211; driven by shell scripts invoked for each changer operation &#8211; to version 2.0, composed of perl objects that can manage parallel access to multiple devices and other complexity. At this point, all Amanda programs use the new Changer API directly, although 1.0 changer scripts are still fully supported via chg-compat. </p>
<p> The Changer API strives to treat all changers identically, so that Amanda&#8217;s behavior is independent of the changer in use. However, some parts of Amanda operate differently depending on whether a changer can efficiently search for a volume with a given label. This distinction is really only apparent with tape libraries: those with barcode readers can quickly find a desired tape, while those without may fall back to an inefficient scan of each volume. The capability to perform quick searches is called &quot;fast-search&quot;, and each changer is annotated below to indicate its support.</p>
<h2>Specifying Changers</h2>
<p>Changer specifications are strings like chg-disk:/my/vtapes. The chg- prefix serves to differentiate changers from devices (see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)). The next portion (disk, in this case) identifies the particular changer driver to use, and everything that follows the : is interpreted by the driver. Note that the : character is required, even when nothing follows it. This is an easy way to distinguish new changer specifications from old. </p>
<p> A name which does not match this pattern, but which matches an old changer script (e.g., chg-zd-mtx), invokes the backward-compatibility changer driver as e.g., chg-compat:chg-zd-mtx. If the name does not match an old changer, then it is treated as an Amanda device, and is wrapped by the single-device changer, e.g., chg-single:tape:/dev/rmt/0. </p>
<p> Changers which require additional parameters can also be described in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) with &quot;changer&quot; sections. Such a changer defininition creates a changer &quot;alias&quot;, in this case named <i>hp-robot</i>, which can then be named where an application expects a changer &#8211; for example, the target of the <code>amvault</code> command or in a global <code>tpchanger</code> parameter.</p>
<h3>Configuration</h3>
<p>The preferred method of specifying configuration for a changer is as a &quot;changer&quot; section in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5). The <i>tapedev</i> parameter then indicates, by name, the changer that will be used by default by most Amanda programs. For example: </p>
<pre>define changer hp-robot {
 tapedev &quot;chg-robot:/dev/sg1&quot;
 property &quot;tape-device&quot; &quot;0=tape:/dev/nst0&quot;
 property append &quot;tape-device&quot; &quot;1=tape:/dev/nst1&quot;
 device-property &quot;BLOCK_SIZE&quot; &quot;512k&quot;
}
# ...
tapedev &quot;hp-robot&quot;</pre>
<p>Several changer drivers accept <i>changer properties</i> which control the behavior of the changer. These properties must be specified in a changer definition, as in the <i>hp-robot</i> example, above. </p>
<p> Devices, too, can take properties to control their behavior (see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)). Device properties can come from four places: implicit device properties (from tapetype parameters), global device properties (from global <i>device-property</i> parameters), properties in device definitions, and properties in changer definitions. Properties are applied in this order, with later properties taking priority. </p>
<p> There are only three implicit properties: <i>MAX_VOLUME_USAGE</i> is set based on the tapetype <i>length</i> parameter, <i>READ_BLOCK_SIZE</i> is set if <i>readblocksize</i> is set, and <i>BLOCK_SIZE</i> is set based on the <i>blocksize</i> parameter. </p>
<p> Global device properties always apply. If the changer specifies a device by alias, then device properties from the definition apply. If the changer is specified by an alias, then properties from that definition applied.</p>
<h2>Changer Drivers</h2>
<p>This section lists the changer drivers included with Amanda, and basic instructions for using them. For complete How-To information, consult the Amanda wiki at <a rel="nofollow" href="http://wiki.zmanda.com.">http://wiki.zmanda.com.</a></p>
<h3>chg-aggregate:changer (new)</h3>
<pre>define changer robot0 {
 tpchanger &quot;chg-robot:/dev/sg0&quot;
 property &quot;tape-device&quot; &quot;0=tape:/dev/rmt/0&quot; &quot;1=tape:/dev/rmt/1&quot;
}
define changer robot1 {
 tpchanger &quot;chg-robot:/dev/sg1&quot;
 property &quot;tape-device&quot; &quot;0=tape:/dev/rmt/2&quot; &quot;1=tape:/dev/rmt/3&quot;
}
define changer single {
 tpchanger &quot;chg-single:/dev/rmt/4&quot;
}
define changer aggregate {
 tpchanger &quot;chg-aggregate:{robot0,robot1,single}&quot;
 property &quot;state-filename&quot; &quot;/etc/amanda/CONF/aggregate.state&quot;
}
tpchanger &quot;aggregate&quot;</pre>
<p>This changer driver allow to use two or more changers or standalone drive in sequence.</p>
<h3>Properties</h3>
<p>LOCK-TIMEOUT</p>
<dl>
<dd>The time in seconds amanda wait to lock the statefile (default:1000)</dl>
<p> STATE_FILENAME</p>
<dl>
<dd>The name of the state file (default: &quot;$CONFIG_DIR/$changer_name.state&quot;.</dl>
<h3>chg-disk:VTAPEROOT (new)</h3>
<pre>tpchanger &quot;chg-disk:/var/mnt/vtapes&quot;
property &quot;num-slot&quot; &quot;10&quot;
property &quot;auto-create-slot&quot; &quot;yes&quot;
property &quot;removable&quot; &quot;yes&quot;
property &quot;mount&quot; &quot;yes&quot;
property &quot;umount&quot; &quot;yes&quot;
property &quot;umount-lockfile&quot; &quot;/etc/amanda/conf/vtapes-lock&quot;
property &quot;umount-idle&quot; &quot;1&quot;</pre>
<p>This changer driver replaces the old <code>chg-disk</code>, supporting parallel access to vtapes stored in directories named slotN in the directory specified after chg-disk:. It does so by creating numbered &quot;drives&quot; so that simultaneous processes can access distinct slots. This changer is fast-search capable. </p>
<p> The current slot can be accessed using the device name file:VTAPEROOT. This is useful for the <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8) command line.</p>
<h3>Properties</h3>
<p>AUTO-CREATE-SLOT</p>
<dl>
<dd>If a slotN directory in the range 1 to NUM-SLOT does not already exist, and this property is true, then the changer will create the directory.</dl>
<p> LOCK-TIMEOUT</p>
<dl>
<dd>The time in seconds amanda wait to lock the statefile (default:1000)</dl>
<p> MOUNT</p>
<dl>
<dd>If this property is true, the changer try to mount the removable disk if nothing is mounted. The system must be configured to allow the amanda user to mount it.</dl>
<p> NUM-SLOT</p>
<dl>
<dd>The minimum number of slots in the changer, where the first slot is slot1. If additional slot directories exist, they will also be used.</dl>
<p> REMOVABLE</p>
<dl>
<dd>If this property is true, then the changer will verify that the changer directory (e.g., /var/mnt/vtapes) is on a different filesystem from its parent directory (e.g., /var/mnt). This is useful for removable disks, as it will prevent Amanda from creating slot directories when the removable disk is not mounted.</dl>
<p> UMOUNT</p>
<dl>
<dd>If this property is true, the changer try to umount the removable disk when it exit. The system must be configured to allow the amanda user to umount it.</dl>
<p> UMOUNT-LOCKFILE</p>
<dl>
<dd>If UMOUNT is set, it require a lockfile outside of the mount point to prevent race.</dl>
<p> UMOUNT-IDLE</p>
<dl>
<dd>If set, the changer try to umount the removable disk when it is not in use. The umount-idle value is a delay in second to wait before doing the umount. A value &gt;= 1 is required to prevent useless mount/umount.</dl>
<h3>chg-disk (old)</h3>
<pre>tapedev &quot;file:/u01/vtapes&quot;
tpchanger &quot;chg-disk&quot;
changerfile &quot;chg-disk.conf&quot; # optional file</pre>
<p>This changer script supports sequential access to vtapes stored in directories named slotN in the directory specified by the <i>tapedev</i> parameter. The configuration file parameter is: </p>
<pre>LASTSLOT=number # The number of slots, default to tapecycle setting.</pre>
<p>This changer is not fast-search capable.</p>
<h3>chg-multi:DEVICE-LIST</h3>
<pre>tpchanger &quot;chg-multi:{/dev/nst0,/dev/nst1,/dev/nst2}&quot;
changerfile &quot;chg-multi-state&quot;</pre>
<p>This script simply round-robins a number of distinct device names, as specified in the <i>tpchanger</i> setting. It is useful when all volumes for a configuration have different device names &#8212; for example, if you have many standalone drive. The <i>changerfile</i> must exist; it is used to save the state file. </p>
<p> The child devices are specified using the same syntax as for the RAIT device (see <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7)). The range specification can be especially useful here: </p>
<pre>tpchanger &quot;chg-multi:s3:mycompany-backups/tape-{001..100}&quot;</pre>
<p>This changer is not fast-search capable.</p>
<h3>Properties</h3>
<p>FIRST-SLOT</p>
<dl>
<dd>This property gives the number of the first slot. The default value is &quot;1&quot;.</dl>
<p> LOCK-TIMEOUT</p>
<dl>
<dd>The time in seconds amanda wait to lock the statefile (default:1000)</dl>
<h3>Special Operations</h3>
<p>A number of special operations are available for <code>chg-multi</code> via <code><a href="/docs/linux/man/8-amtape/">amtape</a></code>(8) subcommands. </p>
<p> The <code>reset</code> subcommand will change the current slot to the first available slot, but does not erase any stored state maintained by the changer. </p>
<p> The <code>eject</code> subcommand will eject the volume in the given drive </p>
<p> The <code>clean</code> subcommand is not yet implemented. </p>
<p> The <code>update</code> subcommand instructs the changer to update its state database. Given no arguments, the changer will scan all available slots, loading each tape and reading its label. Especially for large libraries, this can take a long time. If only a few slots have changed, they can be listed on the command line: </p>
<pre>amtape CONFIG update 1-3,9</pre>
<p>In this case, the changer will only scan the stated slots. Finally, the changer will not scan at all if it is given the tape label for the slot: </p>
<pre>amtape CONFIG update 2=DailySet-028</pre>
<p>In this case, the changer updates its state to indicate that DailySet-028 is in slot 2, without trying to load the tape. </p>
<pre>amtape CONFIG update 1-3,9=</pre>
<p>In this case, the changer marks the stated slots as an unknown state.</p>
<h3>chg-multi (old)</h3>
<pre>tpchanger &quot;chg-multi&quot;
changerfile &quot;chg-multi-state&quot;</pre>
<p>This script simply round-robins a number of distinct device names, as specified in its configuration file. It is useful when all volumes for a configuration have different device names &#8212; for example, with S3 devices. The <i>changerfile</i> need not exist; it is used as a prefix for filenames of state files. </p>
<p> The configuration file has simple lines with a parameter and its value separated by a space. The # character introduces a comment. The configuration parameters are: </p>
<p> multieject</p>
<dl>
<dd>If this is 1, use an &#8216;mt offline&#8217; command to change to the next tape, or multiple such commands for skipping several tapes at a time.</dl>
<p> needeject</p>
<dl>
<dd>This option is incompatible with &#8216;multieject&#8217;. This should be 1 for changers accessed through several virtual tape devices, when the changer needs the current tape to be ejected before changing to another device.</dl>
<p> gravity</p>
<dl>
<dd>Set this to 1 if the changer/stacker is unable to loop back to the first tape after unloading the last one, or if you don&#8217;t want amanda to go through the tape stack looking for the exact tape it wants instead of using the first acceptable one.</dl>
<p> slot X</p>
<dl>
<dd>The configuration file should list as many &#8216;slot X&#8217; statements as the number of slots supported by the changer or the number of separate tape drives used.</dl>
<p> This changer is not fast-search capable.</p>
<h3>chg-manual</h3>
<pre>tpchanger &quot;chg-manual&quot;
changerfile &quot;chg-manual.conf&quot;</pre>
<p>This script simply provides distinct device names in a round-robin fashion, as specified in its configuration file. It is useful when all volumes for a configuration have different device names &#8212; for example, with S3 devices. The configuration file parameters are (as listed in the script): </p>
<pre>resend_mail=900 # resend mail every __ seconds
timeout_mail=604800 # time out after this many seconds (default 7 days)
request=&quot;[type]&quot; # How to request a new tape (default &quot;tty_email&quot;)
 request=&quot;tty&quot; # Use the tty to ask the user to change tape.
 # Can't be use by cron
 request=&quot;email&quot; # Send an email to ask the user to change tape.
 request=&quot;tty_email&quot; # Use the tty if it exist or send an email.</pre>
<p>This changer is not fast-search capable.</p>
<h3>chg-zd-mtx (old)</h3>
<pre>tpchanger &quot;chg-zd-mtx&quot;
changerdev &quot;/dev/sg0&quot; # used with 'mtx -f'
changerfile &quot;chg-zd-mtx.conf&quot;
tapedev &quot;tape:/dev/nst0&quot;</pre>
<p>This script interfaces with a tape drive using the Zubkoff/Dandelion version of mtx. That&#8217;s the version that takes a device specifier with the <code>-f</code> option and has subcommands like <code>status</code>. The configuration file parameters are (as listed in the script itself): </p>
<pre>firstslot=? #### First storage slot (element)
lastslot=? #### Last storage slot (element)
cleanslot=-1 #### Slot with cleaner tape -- default is &quot;-1&quot;
 #### Set negative to indicate no cleaner available
driveslot=0 #### Drive slot number. Defaults to 0
 #### Use the 'Data Transfer Element' you want
autoclean=0 #### Set to '1' or greater to enable
autocleancount=99 #### Number of access before a clean.
havereader=0 #### If you have a barcode reader, set to 1.
offline_before_unload=0 #### Does your robot require an
 #### 'mt offline' before mtx unload?
poll_drive_ready=NN #### Time (seconds) between tests to see if
 #### the tape drive has gone ready (default: 3).
max_drive_wait=NN #### Maximum time (seconds) to wait for the
 #### tape drive to become ready (default: 120).
initial_poll_delay=NN #### initial delay after load before polling for
 #### readiness
slotinfofile=FILENAME #### record slot information to this file, in
 #### the line-based format &quot;SLOT LABEL
&quot;</pre>
<p>This changer is fast-search capable if and only if <code>havereader</code> is true.</p>
<h3>chg-rait:{CHILD1,CHILD2,..}</h3>
<pre>define changer vtape {
 tpchanger &quot;chg-disk:/path/to/vtape&quot;
}
define changer robot {
 tpchanger &quot;chg-robot:/dev/sg0&quot;
 tapedev &quot;tape:/dev/nst0&quot;
}
tpchanger &quot;chg-rait:{vtape,robot}&quot;</pre>
<p>This changer script constructs RAIT devices out of the devices provided by several &quot;sub-changers&quot;. The sub-changers are specified using the same shell-like syntax as the RAIT device (see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)). </p>
<p> Chg-rait does not require that all of the child changers have the same slot names: compound slot names are created by combining the slot names supplied by the child changers using the same shell-like syntax. For example, if the child changers return slots &quot;top&quot;, &quot;strange&quot;, and &quot;3&quot;, then the RAIT changer will return &quot;{top,strange,3}&quot;. This makes it possible to, for example, mirror data on tapes in slots 1-10 to tapes in slots 11-20 of the same robot, using two <code>chg-zd-mtx</code> child changers (and, naturally, two tape drives). In this arrangement, the first slot would be named {1,11}. </p>
<p> As a convenience to the user, the RAIT changer will also accept un-braced slot names, and supply the same name to each child changer. Thus with a 4-device RAIT changer, &quot;17&quot; is equivalent to &quot;{17,17,17,17}&quot;. </p>
<p> Drive names are parsed in a similar fashion, for operations that take drive names (clean and eject). </p>
<p> This changer is fast-search capable only if all of its child changers are fast-search capable. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The old chg-rait script is no longer supported nor shipped with Amanda, although the old script will continue to function via <code>chg-compat</code>, giving users time to upgrade their configuration. </p>
</dl>
<h3>chg-null:</h3>
<pre>tpchanger &quot;chg-null:&quot;</pre>
<p>This changer always provides the device &quot;null:&quot;. It is sometimes useful in conjunction with <code>chg-rait:</code>.</p>
<h3>chg-robot:DEVICE</h3>
<pre>define changer robot {
 tpchanger &quot;chg-robot:/dev/sg0&quot;
 property &quot;tape-device&quot; &quot;0=tape:/dev/rmt/0&quot; &quot;1=tape:/dev/rmt/1&quot;
 property &quot;eject-before-unload&quot; &quot;yes&quot;
 property &quot;use-slots&quot; &quot;1-5,11-20&quot;
}
tpchanger &quot;robot&quot;</pre>
<p>This changer drives a robotic tape library using the operating system&#8217;s <code>mtx</code> command. It replaces the ancient <code>chg-zd-mtx</code> script. The changer uses all of the information available to operate as efficiently as possible. Even without a barcode reader, the changer can usually load a tape immediately, without resorting to a sequential scan of many tapes. It is capable of sharing state across multiple Amanda configurations, avoiding conflicts and optimally tracking the contents of the library. </p>
<p> This changer does not accept a <code>changerdev</code> parameter, but the <code>changerfile</code> parameter can be used to specify a filename at which it should store its state. Ordinarily, this state is stored in a file named after the changer device under <i>$localstatedir/amanda</i>, e.g., <code>/var/amanda/chg-robot-dev-sg0</code>. There should be a single such statefile for each distinct tape library attached to the Amanda server, even if multiple Amanda configurations reference that library. </p>
<p> With a barcode reader present, it is possible for <code>chg-robot</code> to track the state of the library reliably, even recognizing tapes that are removed and later re-inserted (by remembering their barcodes). Without barcodes, the changer can still remember the slot in which it last saw the tape with a particular label, although this information can become stale if the tapes are rearranged by an operator. In any case, the changer will never &quot;hunt&quot; for a tape by repeatedly loading slots and checking labels. If the changer&#8217;s state is inaccurate, use the <code><a href="/docs/linux/man/8-amtape/">amtape</a></code>(8) subcommand <code>update</code>. </p>
<p> This changer is fast-search capable even without a barcode reader. For such libraries, it is the responsibility of the operator to <code>update</code> the changer when tapes are added to or removed from the library. </p>
<p> There is a shell script in the contrib/ directory of Amanda&#8217;s source distribution which can help you convert a <code>chg-zd-mtx</code> configuration into a <code>chg-robot</code> configuration. Just give it your Amanda configuration name: </p>
<pre> sh contrib/convert-zd-mtx-to-robot.sh $config</pre>
<p>The script can be downloaded at <a rel="nofollow" href="http://github.com/zmanda/amanda/raw/master/contrib/convert-zd-mtx-to-robot.sh">http://github.com/zmanda/amanda/raw/master/contrib/convert-zd-mtx-to-robot.sh</a></p>
<h3>Special Operations</h3>
<p>A number of special operations are available for <code>chg-robot</code> via <code><a href="/docs/linux/man/8-amtape/">amtape</a></code>(8) subcommands. </p>
<p> The <code>reset</code> subcommand will change the current slot to the first available slot, but does not erase any stored state maintained by the changer. </p>
<p> The <code>eject</code> subcommand will unload the volume in the given drive, ejecting first if the changer properties dictate. Note that, despite the subcommand name, the changer attempts to avoid the state where a volume has been ejected from the drive but not unloaded back to a storage slot. </p>
<p> The <code>clean</code> subcommand is not yet implemented. </p>
<p> The <code>update</code> subcommand instructs the changer to update its state database. Given no arguments, the changer will scan all available slots, loading each tape and reading its label. Especially for large libraries, this can take a long time. If only a few slots have changed, they can be listed on the command line: </p>
<pre>amtape CONFIG update 1-3,9</pre>
<p>In this case, the changer will only scan the stated slots. Finally, the changer will not scan at all if it is given the tape label for the slot: </p>
<pre>amtape CONFIG update 2=DailySet-028</pre>
<p>In this case, the changer updates its state to indicate that DailySet-028 is in slot 2, without trying to load the tape. </p>
<pre>amtape CONFIG update 1-3,9=</pre>
<p>In this case, the changer marks the stated slots as an unknown state.</p>
<h3>Properties</h3>
<p>DRIVE-CHOICE</p>
<dl>
<dd>This property controls the algorithm used to select a drive in which to load a tape. If set to the default (&quot;lru&quot;), the changer attempts to use the least recently used drive, resulting in a round-robin behavior. The &quot;firstavail&quot; algorithm selects the first available drive, thus preferring the first drive specified via the TAPE-DEVICE property.</dl>
<p> EJECT-BEFORE-UNLOAD</p>
<dl>
<dd>Set this boolean property to true if the library requires an <code>offline</code> operation be performed on the tape drive before it can be unloaded. If set, then <code>mt</code> will be invoked to perform this operation. Most libraries do not require this workaround.</dl>
<p> EJECT-DELAY</p>
<dl>
<dd>This is the time between ejecting a tape and unloading the volume to a storage slot, and defaults to 0 seconds. It is only used if EJECT-BEFORE-UNLOAD is true. See &quot;Timing&quot;, below.</dl>
<p> FAST-SEARCH</p>
<dl>
<dd>This boolean property indicates whether the changer advertises the ability to find volumes without sequential scanning. The traditional taperscan algorithm alters its behavior based on this flag, so it is sometimes necessary to adjust it, although the changer will always search for a desired tape using the most efficient means available. The default value is true.</dl>
<p> IGNORE-BARCODES</p>
<dl>
<dd>If this boolean property is true, then chg-robot will ignore any barcode information that the library provides. This property is probably only useful when the library returns incorrect barcodes, for example due to a malfunction in the barcode reader.</dl>
<p> LOAD-POLL</p>
<dl>
<dd>This property specifies the timing of Amanda&#8217;s polling for the tape drive to be ready after loading a new tape. See &quot;Timing&quot;, below. </p>
<p> The script &quot;polls&quot; by trying to open the tape device repeatedly until no error is encountered. The property specifies the time to wait before the first poll (D), the frequency at which to poll and retry on errors (P); and the time after which it should give up (U). The format is </p>
<pre>&quot;D [poll P [until U]]&quot;</pre>
<p>For a simple delay with no polling, use e.g., </p>
<pre>property &quot;load-poll&quot; &quot;13s&quot;</pre>
<p>To delay and then poll, use e.g., </p>
<pre>property &quot;load-poll&quot; &quot;13s poll 5s&quot;</pre>
<p>and to add a maximum total time, use e.g., </p>
<pre>property &quot;load-poll&quot; &quot;0s poll 5s until 2m&quot;</pre>
<p>The default value is <code>&quot;0s poll 3s until 2m&quot;</code>.</dl>
<p> LOCK-TIMEOUT</p>
<dl>
<dd>The time in seconds amanda wait to lock the statefile (default:1000)</dl>
<p> MTX</p>
<dl>
<dd>The path to the &#8216;mtx&#8217; binary. The default value is defined at compile time.</dl>
<p> STATUS-INTERVAL</p>
<dl>
<dd>This is the minimum time between invocations of <code>mtx status</code> to determine the state of the changer library. The default value, 2 seconds, avoids back-to-back status invocations but ensures that the metadata is up to date. For operating systems or libraries where the <code>mtx status</code> takes a considerable time to complete, this value should be increased. See &quot;Timing&quot;, below.</dl>
<p> TAPE-DEVICE</p>
<dl>
<dd>This property describes the correspondance of drive numbers in the library to Amanda devices, in the format <i>DRIVE=DEVICE</i>. The property can be specified multiple times to describe multiple devices. The device will usually be a tape device name starting with <code>tape:</code>, but may also refer to a device alias (see <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7)). As a shortcut, if the <code>tapedev</code> parameter is specified in the changer definition, then it is assumed to be the device name for drive 0.</dl>
<p> UNLOAD-DELAY</p>
<dl>
<dd>This specifies the minimum time between an unload operation any any subsequent operation. The default value is 0 seconds. See &quot;Timing&quot;, below.</dl>
<p> USE-SLOTS</p>
<dl>
<dd>This property, if specifies, enumerates the slots to which this changer should limit itself. The slots are specified as a comma-separated list of ranges, e.g., &quot;1-5,11-15,19,22&quot;. The property can be specified more than once, and the resulting sets will be combined. The changer will refuse to load tapes not found in these slots, except for import/export purposes.</dl>
<h3>Timing</h3>
<p>Tape libraries are fickle, and in many cases will report that an operation is complete when it is still in progress. Chg-robot takes several timing-related properties to accomodate such behavior. </p>
<p> A typical sequence of operations performed during a load are: get library status, eject a tape, unload the tape back to a storage slot, load a new tape, and read the label on that tape to ensure the drive is ready. </p>
<p> On most systems, the library status check is nearly instantaneous &#8212; the changer library provides its cached state to the host without initiating any robot motion. In order to keep its metadata up-to-date, chg-robot runs this command very frequently, but this frequency can be reduced (at the cost of potentially stale metadata) by setting the STATUS-INTERVAL property to a larger value. </p>
<p> Some tape libraries do not integrate the eject operation (performed by the embedded tape drive) with the unload operation (performed by the library robot), and can actually cause physical damage by attempting to remove the tape before the ejection is complete. For such changers, set the EJECT-DELAY property to allow enough time for the eject to complete. </p>
<p> Once a tape is unloaded, if the library needs time to &quot;quiesce&quot; before processing another command, add that time to the UNLOAD-DELAY parameter. No other operations will be performed on the library until this delay has elapsed. </p>
<p> Once a tape has been loaded, chg-robot waits until the drive is ready before allowing Amanda to use the volume, as described for LOAD-POLL, above. </p>
<p> Each of the times specified in these properties may be given as integers with the optional suffix <code>s</code> for seconds (the default) or <code>m</code> for minutes.</p>
<h3>chg-ndmp:HOST[:PORT]@SCSIDEV</h3>
<pre> tpchanger &quot;chg-ndmp:filer.company.com@/dev/sg0&quot;
 property &quot;tape-device&quot; &quot;0=ndmp:filer.company.com@/dev/rtape0&quot;
 property append &quot;tape-device&quot; &quot;1=ndmp:filer.company.com@/dev/rtape1&quot;
 property &quot;use-slots&quot; &quot;1-12&quot;
 property &quot;ndmp-auth&quot; &quot;text&quot;
 property &quot;ndmp-username&quot; &quot;luke&quot;
 property &quot;ndmp-password&quot; &quot;leia&quot;</pre>
<p>This changer is very similar to <code>chg-robot</code>, but controls a tape changer on an NDMP server instead of a local device. The <code>HOST</code> in the <code>tpchanger</code> should be the hostname of the NDMP server. The <code>PORT</code> is optional. The <code>SCSIDEV</code> should specify the SCSI device on the NDMP server which controls the changer. The format of this parameter is implementation-specific. </p>
<p> The appropriate authentication properties will be automatically set on any devices created by this changer.</p>
<h3>Properties</h3>
<p>This changer supports all of the properties supported by <code>chg-robot</code>, although the value of <code>MTX</code> is ignored. The following properties are also recognized: </p>
<p> NDMP_AUTH</p>
<dl>
<dd>Authentication method to use to connect to the NDMP server. One of &quot;md5&quot; (default), &quot;text&quot;, &quot;none&quot; (for an empty authentication attempt) or &quot;void&quot; (for no authentication attempt at all).</dl>
<p> NDMP-PASSWORD</p>
<dl>
<dd>The password for the NDMP server.</dl>
<p> NDMP-USERNAME</p>
<dl>
<dd>The username for the NDMP server.</dl>
<p> VERBOSE</p>
<dl>
<dd>If true, enables the NDMJOB library&#8217;s verbose (packet-level) debugging.</dl>
<h3>chg-single:DEVICE</h3>
<pre>tpchanger &quot;chg-single:tape:/dev/nst0&quot;</pre>
<p>This changer is for use with standalone drive, it can work with any device. The device (<code>tape:/dev/nst0</code>) must be set in the tpchanger definition. </p>
<p> The <code>chg-single</code> changer has no property.</p>
<h3>Unmaintained Changers</h3>
<p>Amanda has many other changer scripts and programs beyond those described here (see the changer-src/ in the source directory), but most of these scripts are unmaintained and undocumented, and will be removed when the new changer API is fully implemented.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-devices/">amanda-devices</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
