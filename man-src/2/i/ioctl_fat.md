---
title: "ioctl_fat(2)"
name: "ioctl_fat"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl_fat/"
description: "ioctl_fat – manipulating the FAT filesystem"
---

<h2 class="name">NAME</h2>
<p> ioctl_fat &#8211; manipulating the FAT filesystem </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/msdos_fs.h&gt;
#include &lt;sys/ioctl.h&gt;
int ioctl(int fd, FAT_IOCTL_GET_ATTRIBUTES, uint32_t *attr);
int ioctl(int fd, FAT_IOCTL_SET_ATTRIBUTES, uint32_t *attr);
int ioctl(int fd, FAT_IOCTL_GET_VOLUME_ID, uint32_t *id);
int ioctl(int fd, VFAT_IOCTL_READDIR_BOTH,
          struct __fat_dirent[2] entry);
int ioctl(int fd, VFAT_IOCTL_READDIR_SHORT,
          struct __fat_dirent[2] entry);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) system call can be used to read and write metadata of FAT filesystems that are not accessible using other system calls.</p>
<h3>Reading and setting file attributes</h3>
<p> Files and directories in the FAT filesystem possess an attribute bit mask that can be read with <code>FAT_IOCTL_GET_ATTRIBUTES</code> and written with <code>FAT_IOCTL_SET_ATTRIBUTES</code>. </p>
<p> The <i>fd</i> argument contains a file descriptor for a file or directory. It is sufficient to create the file descriptor by calling <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the <code>O_RDONLY</code> flag. </p>
<p> The <i>attr</i> argument contains a pointer to a bit mask. The bits of the bit mask are:</p>
<dl>
<dt><code>ATTR_RO</code></p>
<dd> This bit specifies that the file or directory is read-only.</p>
<dt><code>ATTR_HIDDEN</code></p>
<dd> This bit specifies that the file or directory is hidden.</p>
<dt><code>ATTR_SYS</code></p>
<dd> This bit specifies that the file is a system file.</p>
<dt><code>ATTR_VOLUME</code></p>
<dd> This bit specifies that the file is a volume label. This attribute is read-only.</p>
<dt><code>ATTR_DIR</code></p>
<dd> This bit specifies that this is a directory. This attribute is read-only.</p>
<dt><code>ATTR_ARCH</code></p>
<dd> This bit indicates that this file or directory should be archived. It is set when a file is created or modified. It is reset by an archiving system.</dl>
<p> The zero value <code>ATTR_NONE</code> can be used to indicate that no attribute bit is set.</p>
<h3>Reading the volume ID</h3>
<p> FAT filesystems are identified by a volume ID. The volume ID can be read with <code>FAT_IOCTL_GET_VOLUME_ID</code>. </p>
<p> The <i>fd</i> argument can be a file descriptor for any file or directory of the filesystem. It is sufficient to create the file descriptor by calling <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the <code>O_RDONLY</code> flag. </p>
<p> The <i>id</i> argument is a pointer to the field that will be filled with the volume ID. Typically the volume ID is displayed to the user as a group of two 16-bit fields: </p>
<p> printf(&quot;Volume ID %04x-%04x
&quot;, id &gt;&gt; 16, id &amp; 0xFFFF);</p>
<h3>Reading short filenames of a directory</h3>
<p> A file or directory on a FAT filesystem always has a short filename consisting of up to 8 capital letters, optionally followed by a period and up to 3 capital letters for the file extension. If the actual filename does not fit into this scheme, it is stored as a long filename of up to 255 UTF-16 characters. </p>
<p> The short filenames in a directory can be read with <code>VFAT_IOCTL_READDIR_SHORT</code>. <code>VFAT_IOCTL_READDIR_BOTH</code> reads both the short and the long filenames. </p>
<p> The <i>fd</i> argument must be a file descriptor for a directory. It is sufficient to create the file descriptor by calling <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the <code>O_RDONLY</code> flag. The file descriptor can be used only once to iterate over the directory entries by calling <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) repeatedly. </p>
<p> The <i>entry</i> argument is a two-element array of the following structures: </p>
<p> struct __fat_dirent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_ino;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__kernel_off_t&nbsp;<wbr>&nbsp;d_off;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t short&nbsp;<wbr>&nbsp;d_reclen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_name[256]; }; </p>
<p> The first entry in the array is for the short filename. The second entry is for the long filename. </p>
<p> The <i>d_ino</i> and <i>d_off</i> fields are filled only for long filenames. The <i>d_ino</i> field holds the inode number of the directory. The <i>d_off</i> field holds the offset of the file entry in the directory. As these values are not available for short filenames, the user code should simply ignore them. </p>
<p> The field <i>d_reclen</i> contains the length of the filename in the field <i>d_name</i>. To keep backward compatibility, a length of 0 for the short filename signals that the end of the directory has been reached. However, the preferred method for detecting the end of the directory is to test the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) return value. If no long filename exists, field <i>d_reclen</i> is set to 0 and <i>d_name</i> is a character string of length 0 for the long filename.</p>
<h2>RETURN VALUE</h2>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error. </p>
<p> For <code>VFAT_IOCTL_READDIR_BOTH</code> and <code>VFAT_IOCTL_READDIR_SHORT</code> a return value of 1 signals that a new directory entry has been read and a return value of 0 signals that the end of the directory has been reached.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code></p>
<dd> This error is returned by <code>VFAT_IOCTL_READDIR_BOTH</code> and <code>VFAT_IOCTL_READDIR_SHORT</code> if the file descriptor <i>fd</i> refers to a removed, but still open directory.</p>
<dt><code>ENOTDIR</code></p>
<dd> This error is returned by <code>VFAT_IOCTL_READDIR_BOTH</code> and <code>VFAT_IOCTL_READDIR_SHORT</code> if the file descriptor <i>fd</i> does not refer to a directory.</p>
<dt><code>ENOTTY</code></p>
<dd> The file descriptor <i>fd</i> does not refer to an object in a FAT filesystem.</dl>
<p> For further error values, see <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> <code>VFAT_IOCTL_READDIR_BOTH</code> and <code>VFAT_IOCTL_READDIR_SHORT</code> first appeared in Linux 2.0. </p>
<p> <code>FAT_IOCTL_GET_ATTRIBUTES</code> and <code>FAT_IOCTL_SET_ATTRIBUTES</code> first appeared in Linux 2.6.12. </p>
<p> <code>FAT_IOCTL_GET_VOLUME_ID</code> was introduced in version 3.11 of the Linux kernel.</p>
<h2>CONFORMING TO</h2>
<p> This API is Linux-specific.</p>
<h2>EXAMPLES</h2>
<h3>Toggling the archive flag</h3>
<p> The following program demonstrates the usage of <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) to manipulate file attributes. The program reads and displays the archive attribute of a file. After inverting the value of the attribute, the program reads and displays the attribute again. </p>
<p> The following was recorded when applying the program for the file <i>/mnt/user/foo</i>: </p>
<p> # ./toggle_fat_archive_flag /mnt/user/foo Archive flag is set Toggling archive flag Archive flag is not set</p>
<h3>Program source (toggle_fat_archive_flag.c)</h3>
<p> #include &lt;fcntl.h&gt; #include &lt;linux/msdos_fs.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;unistd.h&gt; </p>
<p> /*<br />
&nbsp;*&nbsp;Read file attributes of a file on a FAT filesystem.<br />
&nbsp;*&nbsp;Output the state of the archive flag.<br />
&nbsp;*/ static uint32_t readattr(int fd) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t attr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;ioctl(fd, FAT_IOCTL_GET_ATTRIBUTES,&nbsp;&amp;attr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ioctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(attr&nbsp;&amp;&nbsp;ATTR_ARCH)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Archive flag is set
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Archive flag is not set
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return attr; } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t attr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s FILENAME
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Read and display the FAT file attributes.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attr&nbsp;=&nbsp;readattr(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Invert archive attribute.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Toggling archive flag
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attr ha=&nbsp;ATTR_ARCH; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Write the changed FAT file attributes.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;ioctl(fd, FAT_IOCTL_SET_ATTRIBUTES,&nbsp;&amp;attr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ioctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Read and display the FAT file attributes.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;readattr(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>Reading the volume ID</h3>
<p> The following program demonstrates the use of <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) to display the volume ID of a FAT filesystem. </p>
<p> The following output was recorded when applying the program for directory <i>/mnt/user</i>: </p>
<p> $ ./display_fat_volume_id /mnt/user Volume ID 6443-6241</p>
<h3>Program source (display_fat_volume_id.c)</h3>
<p> #include &lt;fcntl.h&gt; #include &lt;linux/msdos_fs.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t id;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s FILENAME
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Read volume ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;ioctl(fd, FAT_IOCTL_GET_VOLUME_ID,&nbsp;&amp;id);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ioctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Format the output as two groups of 16 bits each.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Volume ID&nbsp;%04x-%04x
&quot;, id&nbsp;&gt;&gt;&nbsp;16, id&nbsp;&amp;&nbsp;0xFFFF); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>Listing a directory</h3>
<p> The following program demonstrates the use of <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) to list a directory. </p>
<p> The following was recorded when applying the program to the directory <i>/mnt/user</i>: </p>
<p> $ <code>./fat_dir /mnt/user</code> 46 -&gt; &#8221; 46. -&gt; &#8221; ALONGF~1.TXT -&gt; &#8216;a long filename.txt&#8217; UPPER.TXT -&gt; &#8221; LOWER.TXT -&gt; &#8216;lower.txt&#8217;</p>
<h3>Program source</h3>
<p> #include &lt;fcntl.h&gt; #include &lt;linux/msdos_fs.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/ioctl.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;__fat_dirent entry[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Usage:&nbsp;%s DIRECTORY
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Open file descriptor for the directory.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY | O_DIRECTORY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Read next directory entry.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;ioctl(&nbsp;fd, VFAT_IOCTL_READDIR_BOTH, entry); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;If an error occurs, the return value is -1.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;If the end of the directory list has been reached,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;the return value is 0.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;For backward compatibility the end of the directory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;list is also signaled by d_reclen&nbsp;==&nbsp;0.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;&lt;&nbsp;1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Write both the short name and the long name.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s -&gt;&nbsp;&#8216;%s&#8217;
&quot;, entry[0].d_name, entry[1].d_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;VFAT_IOCTL_READDIR_BOTH&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Close the file descriptor.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
