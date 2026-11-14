---
title: "disklist(5)"
name: "disklist"
section: "5"
letter: "d"
url: "/docs/linux/man/5-disklist/"
description: "disklist – List of partitions to back up for Amanda"
---

<p>disklist &#8211; List of partitions to back up for Amanda</p>
<h2>Description</h2>
<p>The <i>disklist</i> file determines which disks will be backed up by Amanda. The file contains <code>includefile</code> directive or disklist entry (<code>DLE</code>). </p>
<p> <code>includefile</code> <i>string</i></p>
<dl>
<dd>Default: <i>no default</i>. The name of a disklist file to include within the current file. Useful for sharing disklist among several configurations. Relative pathnames are relative to the configuration directory.</dl>
<p> A <code>DLE</code> usually contains one line per disk: </p>
<pre><i>hostname diskname</i> [<i>diskdevice</i>] <i>dumptype</i> [<i>spindle</i> [<i>interface</i>] ]</pre>
<p>All pairs [ <i>hostname diskname</i> ] must be unique. </p>
<p> Lines starting with # are ignored, as are blank lines. The fields have the following meanings: </p>
<p> <i>hostname</i></p>
<dl>
<dd>The name of the host to be backed up. If <code>diskdevice</code> refers to a PC share, this is the host Amanda will run the Samba <code>smbclient</code> program on to back up the share.</dl>
<p> <i>diskname</i></p>
<dl>
<dd>The name of the disk (a label). In most case, you set your <code>diskname</code> to the <code>diskdevice</code> and you don&#8217;t set the <code>diskdevice.</code> If you want multiple entries with the same <code>diskdevice</code>, you must set a different <code>diskname</code> for each entry. It&#8217;s the <code>diskname</code> that you use on the commandline for any Amanda command. Look at the example/disklist file for example.</dl>
<p> <i>diskdevice</i></p>
<dl>
<dd>Default: same as diskname. The name of the disk device to be backed up. It may be a full device name, a device name without the /dev/ prefix, e.g. <i>sd0a</i>, or a mount point such as /usr. </p>
<p> It may also refer to a PC share by starting the name with two (forward) slashes, e.g. //some-pc/home. In this case, the <code>program</code> option in the associated <code>dumptype</code> must be entered as <code>GNUTAR</code>. It is the combination of the double slash disk name and <code>program GNUTAR</code> in the <code>dumptype</code> that triggers the use of Samba.</dl>
<p> <i>dumptype</i></p>
<dl>
<dd>Refers to a <code>dumptype</code> defined in the <code>amanda.conf</code> file. <i>Dumptype</i>s specify backup related parameters, such as whether to compress the backups, whether to record backup results in /etc/dumpdates, the disk&#8217;s relative priority, etc.</dl>
<p> <i>spindle</i></p>
<dl>
<dd>Default: <code>-1</code>. A number used to balance backup load on a host. Amanda will not run multiple backups at the same time on the same spindle, unless the spindle number is -1, which means there is no spindle restriction.</dl>
<p> <i>interface</i></p>
<dl>
<dd>Default: <i>local</i>. The name of a network interface definition in the <code>amanda.conf</code> file, used to balance network load.</dl>
<p> Instead of naming a <code>dumptype</code>, it is possible to define one in-line, enclosing <code>dumptype</code> options within curly braces, one per line, just like a <code>dumptype</code> definition in <code>amanda.conf</code>. Since pre-existing <code>dumptype</code>s are valid option names, this syntax may be used to customize <code>dumptype</code>s for particular disks. </p>
<p> A line break <code>must</code> follow the left curly bracket. </p>
<p> For instance, if a <code>dumptype</code> named <i>normal</i> is used for most disks, but use of the holding disk needs to be disabled for the file system that holds it, this would work instead of defining a new dumptype: </p>
<pre><i>hostname diskname</i> [ <i>diskdevice</i> ] {
 normal
 holdingdisk never
} [ <i>spindle</i> [ <i>interface</i> ] ]</pre>
<p>The { must appear at the end of a line, and the } on its own line possibly followed by the spindle and interface.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt; </p>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
