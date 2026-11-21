---

title: "fls(1)"
name: "fls"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fls/"
description: "fls – List file and directory names in a disk image."
---

<p> <code>fls [-adDFlpruvV] [-m</code> <i>mnt</i> <code>] [-z</code> <i>zone</i> <code>] [-f</code> <i>fstype</i> <code>] [-s</code> <i>seconds</i> <code>] [-i </code> <i>imgtype</i> <code>] [-o </code> <i>imgoffset</i> <code>] [-b dev_sector_size] </code> <i>image [images] </i> <code>[</code> <i>inode</i> <code>]</code></p>
<p> <code>fls</code> lists the files and directory names in the <i>image</i> and can display file names of recently deleted files for the directory using the given <i>inode.</i> If the inode argument is not given, the inode value for the root directory is used. For example, on an NTFS file system it would be 5 and on a Ext3 file system it would be 2. </p>
<p> The arguments are as follows:</p>
<dl>
<dt>-a</dt>
<dd> Display the &quot;.&quot; and &quot;..&quot; directory entries (by default it does not)</dd>
<dt>-d</dt>
<dd> Display deleted entries only</dd>
<dt>-D</dt>
<dd> Display directory entries only</dd>
<dt>-f fstype</dt>
<dd> The type of file system. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-F</dt>
<dd> Display file (all non-directory) entries only.</dd>
<dt>-l</dt>
<dd> Display file details in long format. The following contents are displayed: </dd>
<p> file_type inode file_name mod_time acc_time chg_time cre_time size uid gid</p>
<dt>-m mnt</dt>
<dd> Display files in time machine format so that a timeline can be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;created with&nbsp;<a href="/docs/linux/man/1-mactime/">mactime</a>(1).&nbsp;<wbr>&nbsp; The string given as <i>mnt</i> will be prepended to the file names as the mounting point (for example /usr).</dd>
<dt>-p</dt>
<dd> Display the full path for each entry. By default it denotes the directory depth on recursive runs with a &#8216;+&#8217; sign.</dd>
<dt>-r</dt>
<dd> Recursively display directories. This will not follow deleted directories, because it can&#8217;t.</dd>
<dt>-s seconds</dt>
<dd> The time skew of the original system in seconds. For example, if the original system was 100 seconds slow, this value would be -100. This is only used if -l or -m are given.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-u</dt>
<dd> Display undeleted entries only</dd>
<dt>-v</dt>
<dd> Verbose output to stderr.</dd>
<dt>-V</dt>
<dd> Display version.</dd>
<dt>-z zone</dt>
<dd> The ASCII string of the time zone of the original system. For example, EST or GMT. These strings must be defined by your operating system and may vary.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </dd>
</dl>
<p> Once the inode has been determined, the file can be recovered using <code><a href="/docs/linux/man/1-icat/">icat</a>(1)</code> from The Coroners Toolkit. The amount of information recovered from deleted file entries varies depending on the system. For example, on Linux, a recently deleted file can be easily recovered, while in Solaris not even the inode can be determined. If you just want to find what file name belongs to an inode, it is easier to use <code><a href="/docs/linux/man/1-ffind/">ffind</a>(1).</code> </p>
<h2>EXAMPLES</h2>
<p> To get a list of all files and directories in an image use: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -r image 2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>or just (if no inode is specified, the root directory inode is used):</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -r image</p>
<p> To get the full path of deleted files in a given directory: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -d -p image 29</p>
<p> To get the mactime output do: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -m /usr/local image 2</p>
<p> If you have a disk image and the file system starts in sector 63, use: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -o 63 disk-img.dd</p>
<p> If you have a disk image that is split use: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># fls -i &quot;split&quot; -o 63 disk-1.dd disk-2.dd disk-3.dd</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffind/">ffind</a></code>(1), <code><a href="/docs/linux/man/1-icat/">icat</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
