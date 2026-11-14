---
title: "zulucrypt-cli(1)"
name: "zulucrypt-cli"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zulucrypt-cli/"
description: "zuluCrypt-cli – command line interface frontend to cryptsetup and tcplay"
---

<p>zuluCrypt-cli &#8211; command line interface frontend to cryptsetup and tcplay</p>
<h2>Synopsis</h2>
<p>meaning of symbols:<br />
 &lt;&gt; = required option<br />
 [] = optional argument<br />
 * = default option<br />
 | = alternatives for the same option<br />
 {} = not allowed option<br />
 zuluCrypt-cli &#8211;test<br />
 zuluCrypt-cli -E &lt;d&gt; &lt;e&gt; &lt;p|f|h&gt;<br />
 zuluCrypt-cli -D &lt;d&gt; &lt;e&gt; &lt;p|f|h&gt;<br />
 zuluCrypt-cli -o &lt;d&gt; &lt;m&gt; [e] &lt;p|f|h&gt;<br />
 zuluCrypt-cli -O &lt;d&gt; {m} [e] &lt;p|f|h&gt;<br />
 zuluCrypt-cli -q &lt;d&gt;<br />
 zuluCrypt-cli -i &lt;d&gt;<br />
 zuluCrypt-cli -c &lt;d&gt; &lt;p|f|h&gt; [ktzg]<br />
 zuluCrypt-cli -r &lt;-d&gt; &lt;p|f|h&gt;<br />
 zuluCrypt-cli -a &lt;d&gt; &lt;&lt;y|u&gt; &lt;l|n&gt;&gt;|&lt;h&gt;<br />
 zuluCrypt-cli -b &lt;d&gt;<br />
 zuluCrypt-cli -w &lt;d&gt; d argument must be something like: UUID=<br />
 zuluCrypt-cli -P &lt;d&gt; d device must be mapper path at /dev/mapper/<br />
 zuluCrypt-cli -X &lt;d&gt;<br />
 zuluCrypt-cli -J &lt;d&gt;<br />
 zuluCrypt-cli -R &lt;d&gt; &lt;f&gt;<br />
 zuluCrypt-cli -B &lt;d&gt; &lt;f&gt;<br />
 zuluCrypt-cli -A<br />
 zuluCrypt-cli -S<br />
 zuluCrypt-cli -N </p>
<p> examples:<br />
 create volume: zuluCrypt-cli -c -d /dev/sdc1 -z ext4 -t luks -p xxx<br />
 open volume : zuluCrypt-cli -o -d /dev/sdc1 -m sdc1 -e ro -p xxx<br />
 close volume ; zuluCrypt-cli -q -d /dev/sdc1<br />
 remove key ; zuluCrypt-cli -r -d /dev/sdc1 -p xxx<br />
 add key : zuluCrypt-cli -a -d /dev/sdc1 -y xxx -l yyy<br />
 get device path from mapper : zuluCrypt-cli -P -d /dev/mapper/zuluCrypt-sdc1<br />
 check if partition with UUID is present : zuluCrypt-cli -w -d UUID=</p>
<h2>Description</h2>
<p>zuluCrypt is a front end to cryptsetup. It aims to simplify using cryptsetup volumes by creating a simple to use command line interface and a Qt based GUI front end to the command line. </p>
<p> The command line program is called &quot;zuluCrypt-cli&quot;, the Qt based GUI is called &quot;zuluCrypt-gui&quot;. The cli part of the program is an suid program to allow management of the volumes without setting up sudo with appropriate permissions first or requiring root&#8217;s password. </p>
<p> The GUI part of the program calls the cli part for its operations. </p>
<p> This tool will create volumes only in non system partitions. </p>
<p> System partition is a partition with an active entry in /etc/fstab and /etc/crypttab </p>
<h2>Usage</h2>
<p>usage: zuluCrypt-cli &lt;operation&gt; &lt;options specific to the operation&gt;<br />
 operation list:<br />
 -c create an encrypted volume<br />
 -o open and encrypted volume<br />
 -O open an encrypted volume but do not mount it( -m therefore not needed )<br />
 -q close an opened encrypted volume<br />
 -r remove a key from luks volume<br />
 -a add a key to luks volume<br />
 -i check if a device contain a luks volume<br />
 -s check if a device is opened and print its properties if it is<br />
 -b show status of each slot of luks volume.&quot;0&quot;=empty,&quot;1&quot;=occupied,&quot;2&quot;=invalid slot,&quot;3&quot;=last occupied<br />
 -A print the list of all partitions on the system<br />
 -N print a list of non system partitions on the system( partitions with no active entries in /etc/fstab and /etc/crypttab<br />
 -T print a detailed list of mounted partitions.Must be used with -A or -S or -N<br />
 -Z print a detailed list of unmounted partitions.Must be used with -A or -S or -N<br />
 -S print a list of system partitions on the system( partitions with active entries in /etc/fstab and /etc/crypttab<br />
 -w check if UUID matches UUID of any partition<br />
 -P get device path from mapper( located at /dev/mapper )<br />
 -L print a list of all opened volumes and their mount point.The list is not formatted<br />
 -X open a device pointed by argument -d and write random data to it hiding data previously written to device<br />
 -W check if a device is a truecrypt device or not,required argument are -p or -f<br />
 -U print UUID of a given device,required argument: -d<br />
 -H compare a header on a luks device to a backup header,required arg: -d and -f<br />
 -M create a publicly accessible &quot;mirror&quot; of the mount point in &quot;/run/media/public/&quot; from the original created in &quot;/run/media/private/$USER/&quot;<br />
 -J create a plain mapper owned by the user who run the command on a device pointed by argument -d<br />
 -B create a luks or truecrypt header backup<br />
 -R restore a luks or truecrypt header on a device from backup </p>
<p> <code>NOTE</code><br />
 A system partition is defined as a partition with an active entry in /etc/fstab and/or /etc/crypttab.<br />
 An active entry is an entry that is not commented out. </p>
<p> options that goes with above operations:<br />
 -G module name to use to get a passphrase to open a volume<br />
 -e mode for opening volumes(ro*/rw) when used with -o/-O. path to destination file when used with -E/-D<br />
 -e mode for managing a truecrypt header when used with -B/-R.Options can be &quot;fde&quot; for volumes that use whole disk </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>encryption,&quot;sys&quot;&nbsp;<wbr>for a windows system volume.The volume is assumed to be a normal one when the option is not set.<br />
 -k do not ask for confirmation when doing dangerous operations<br />
 -d path to a file or partition with encrypted volume<br />
 -m path component to be added to mount point prefix(/run/media/private/$USER or /home/$USER)<br />
 -z file system type installed(ext2,ext3,ext4* etc) or or luks/tcrypt header backup path<br />
 -t type of volume (vera,plain/luks*). &quot;vera&quot; is a necessary argument when opening a VeraCrypt volume<br />
 -g options to be used when creating a volume. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>default for luks are:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;/dev/urandom.aes.xts-plain64.256.sha1&quot; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>default for tcrypt are:&nbsp;<wbr>&quot;/dev/urandom.aes.xts-plain64.256.ripemd160&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>possible combination for tcrypt:&nbsp;<wbr>&quot;/dev/urandom.serpent:twofish:aes.xts-plain64.256.whirlpool&quot;<br />
 -h get passphrase interactively<br />
 -p passphrase<br />
 -f path to keyfile<br />
 -F path to normal truecrypt multiple keyfiles.Multiple keyfiles are added by setting the option multiple times.<br />
 -V path to hidden truecrypt multiple keyfiles.Multiple keyfiles are added by setting the option multiple times.<br />
 -y passphrase already in the volume(required by -a if -u is absent and -h is also absent)<br />
 -u path to keyfile with passphrase already in the volume(required by -a if -y is absent and -h is also absent)<br />
 -l passphrase to be added(required by -a if -n is absent and -h is also absent)<br />
 -n path to keyfile with a passphrase to be added (required by -a if -l is absent and -h is also absent) </p>
<h2>Copyright</h2>
<p>Copyright (c) 2011-2013<br />
 name : Francis Banyikwa<br />
 email: mhogomchungu [at] gmail.com </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>Last Edit</h2>
<p>Last change: Fri Jan 9 14:43:08 EAT 2015</p>
