---
title: "funionfs(1)"
name: "funionfs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funionfs/"
description: "funionfs – user-space directory concatenation."
---

<h2>NAME</h2>
<p> funionfs &#8211; user-space directory concatenation.</p>
<h2>SYNOPSIS</h2>
<p> <code>funionfs </code> <i>upper_dir mountpoint [ option ] &#8230;</i></p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>-o opt,[opt&#8230;]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mount options<br />
&nbsp;<wbr>-h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print help<br />
&nbsp;<wbr>-V&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print version </p>
<p> Mount options include:<br />
funionfs_debug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print some debugging information<br />
dirs=LIST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>A colon separated list of directories<br />
/branch1=rw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a directory in a read-write mode<br />
/branch1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if no permission is specified, the branch<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>is in a read-write mode<br />
/branch2=ro&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a directory in a read-only mode<br />
copyupuid=N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uid of the copied-up files&nbsp;<wbr>(no default)<br />
copyupgid=N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gid of the copied-up files&nbsp;<wbr>(no default)<br />
copyupmode=N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mode of the copied-up files&nbsp;<wbr>(no default)<br />
del_string=N&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>string to mark a deleted file(default:&nbsp;<wbr>_DELETED~&nbsp;<wbr>)<br />
delete=TYPE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies how funionfs deletes and renames<br />
all&nbsp;<wbr>(default)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delete all objects in read-write branch&nbsp;<wbr>(default)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and add a whiteout file if objects exists in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>read-only branches.<br />
whiteout&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only add a whiteout file in upper&nbsp;<wbr>(rw)&nbsp;<wbr>branch<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or delete file in upper branch.<br />
copyup=TYPE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies how to manage attributes<br />
preserve&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>preserve uid, gid and mode of object&nbsp;<wbr>(default)<br />
currentuser&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the object owns to the user doing the operation<br />
mounter&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the object owns to the mounter </p>
<p> There is no implementation of -o delete and -o copyup for now. </p>
<p> You could use the mount command instead :<br />
mount -t fuse funionfs#/upper_dir mountpoint&nbsp;<wbr>[&nbsp;<wbr>options&nbsp;<wbr>] </p>
<p> If you want to name all directories in &#8216;-o dirs=&#8217;, then pass &quot;none&quot; as upper_dir </p>
<h2>DESCRIPTION</h2>
<p> <i>funionfs</i> concatenates directories mentioned in options (and <i>upper_dir</i> ) to <i>mountpoint. </i> Also, although some (but not all) of the directories are read-only, you still can write in resulting mounted directory. For example, if you have files <i>a/a </i> and <i>b/b </i> and mount mountpoint <i>r</i> with &quot;-o dirs=a=ro:b=ro:w=rw&quot;, then you will see files <i>r/a</i> and <i>r/b.</i> You will be able to write to them, and original files will remain intact (changes will go to <i>w</i> ). Note that it is impossible to have file with name ending by <i>del_string</i> value, if you create <i>r/a_DELETED~</i> in mentioned example, it will dissapear together with a.</p>
<h2>SEE ALSO</h2>
<p> The source..</p>
<h2>BUGS</h2>
<p> You cannot mount an overlay on / (the program that list the content of / will hang). This is probably due to a loop call of the fuse driver. There is no known solution for now. </p>
<p> Probably minor (or major) mistakes in not-so-frequent cases. </p>
<p> Not enough tested. </p>
<h2>Index</h2>
