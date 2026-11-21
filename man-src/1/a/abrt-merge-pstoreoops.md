---

title: "abrt-merge-pstoreoops(1)"
name: "abrt-merge-pstoreoops"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-merge-pstoreoops/"
---

abrt-merge-pstoreoops - Scans files for split oops message. Can print and/or delete them. 

<i>abrt-merge-pstoreoops</i> [-v] [-od] FILE...

This tool takes list of files, reads all of the files, scans them for split oops messages and join oops parts to original oops message.

<h2>OPTIONS</h2>

 

 -o
<dl>
<dt>
</dt><dd> Print found oopses</dd></dl>
 

 -d
<dl>
<dt>
</dt><dd> Delete files with found oopses</dd></dl>
 

 -v, --verbose
<dl>
<dt>
</dt><dd> Be more verbose. Can be given multiple times.</dd></dl>

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
