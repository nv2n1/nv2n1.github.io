---
title: "libmagic(3)"
name: "libmagic"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmagic/"
description: "magic_open magic_close magic_error magic_descriptor magic_buffer magic_setflags magic_check magic_compile magic_load – Magic number recognition library"
---

<h2>NAME</h2>
<p> <code>magic_open</code> <code>magic_close</code> <code>magic_error</code> <code>magic_descriptor</code> <code>magic_buffer</code> <code>magic_setflags</code> <code>magic_check</code> <code>magic_compile</code> <code>magic_load</code> &#8211; Magic number recognition library</p>
<h2>LIBRARY</h2>
<p> Lb libmagic</p>
<h2>SYNOPSIS</h2>
<p> In magic.h Ft magic_t Fn magic_open int flags Ft void Fn magic_close magic_t cookie Ft const char * Fn magic_error magic_t cookie Ft int Fn magic_errno magic_t cookie Ft const char * Fn magic_descriptor magic_t cookie int fd Ft const char * Fn magic_file magic_t cookie const char *filename Ft const char * Fn magic_buffer magic_t cookie const void *buffer size_t length Ft int Fn magic_setflags magic_t cookie int flags Ft int Fn magic_check magic_t cookie const char *filename Ft int Fn magic_compile magic_t cookie const char *filename Ft int Fn magic_list magic_t cookie const char *filename Ft int Fn magic_load magic_t cookie const char *filename</p>
<h2>DESCRIPTION</h2>
<p> These functions operate on the magic database file which is described in <a href="/docs/linux/man/5-magic/">magic</a>(5). </p>
<p> The function Fn magic_open creates a magic cookie pointer and returns it. It returns <code>NULL</code> if there was an error allocating the magic cookie. The <i>flags</i> argument specifies how the other magic functions should behave:</p>
<dl>
<dt><code>MAGIC_NONE</code></dt>
<dd> No special handling.</dd>
<dt><code>MAGIC_DEBUG</code></dt>
<dd> Print debugging messages to stderr.</dd>
<dt><code>MAGIC_SYMLINK</code></dt>
<dd> If the file queried is a symlink, follow it.</dd>
<dt><code>MAGIC_COMPRESS</code></dt>
<dd> If the file is compressed, unpack it and look at the contents.</dd>
<dt><code>MAGIC_DEVICES</code></dt>
<dd> If the file is a block or character special device, then open the device and try to look in its contents.</dd>
<dt><code>MAGIC_MIME_TYPE</code></dt>
<dd> Return a MIME type string, instead of a textual description.</dd>
<dt><code>MAGIC_MIME_ENCODING</code></dt>
<dd> Return a MIME encoding, instead of a textual description.</dd>
<dt><code>MAGIC_MIME</code></dt>
<dd> A shorthand for MAGIC_MIME_TYPE | MAGIC_MIME_ENCODING.</dd>
<dt><code>MAGIC_CONTINUE</code></dt>
<dd> Return all matches, not just the first.</dd>
<dt><code>MAGIC_CHECK</code></dt>
<dd> Check the magic database for consistency and print warnings to stderr.</dd>
<dt><code>MAGIC_PRESERVE_ATIME</code></dt>
<dd> On systems that support utime(3) or <a href="/docs/linux/man/2-utimes/">utimes</a>(2), attempt to preserve the access time of files analysed.</dd>
<dt><code>MAGIC_RAW</code></dt>
<dd> Don&#8217;t translate unprintable characters to a \ooo octal representation.</dd>
<dt><code>MAGIC_ERROR</code></dt>
<dd> Treat operating system errors while trying to open files and follow symlinks as real errors, instead of printing them in the magic buffer.</dd>
<dt><code>MAGIC_APPLE</code></dt>
<dd> Return the Apple creator and type.</dd>
<dt><code>MAGIC_NO_CHECK_APPTYPE</code></dt>
<dd> Don&#8217;t check for <code>EMX</code> application type (only on EMX).</dd>
<dt><code>MAGIC_NO_CHECK_CDF</code></dt>
<dd> Don&#8217;t get extra information on MS Composite Document Files.</dd>
<dt><code>MAGIC_NO_CHECK_COMPRESS</code></dt>
<dd> Don&#8217;t look inside compressed files.</dd>
<dt><code>MAGIC_NO_CHECK_ELF</code></dt>
<dd> Don&#8217;t print ELF details.</dd>
<dt><code>MAGIC_NO_CHECK_ENCODING</code></dt>
<dd> Don&#8217;t check text encodings.</dd>
<dt><code>MAGIC_NO_CHECK_SOFT</code></dt>
<dd> Don&#8217;t consult magic files.</dd>
<dt><code>MAGIC_NO_CHECK_TAR</code></dt>
<dd> Don&#8217;t examine tar files.</dd>
<dt><code>MAGIC_NO_CHECK_TEXT</code></dt>
<dd> Don&#8217;t check for various types of text files.</dd>
<dt><code>MAGIC_NO_CHECK_TOKENS</code></dt>
<dd> Don&#8217;t look for known tokens inside ascii files.</dd></dl>
<p> The Fn magic_close function closes the <a href="/docs/linux/man/5-magic/">magic</a>(5) database and deallocates any resources used. </p>
<p> The Fn magic_error function returns a textual explanation of the last error, or <code>NULL</code> if there was no error. </p>
<p> The Fn magic_errno function returns the last operating system error number (errno(2) ) that was encountered by a system call. </p>
<p> The Fn magic_file function returns a textual description of the contents of the <i>filename</i> argument, or <code>NULL</code> if an error occurred. If the <i>filename</i> is <code>NULL</code> then stdin is used. </p>
<p> The Fn magic_descriptor function returns a textual description of the contents of the <i>fd</i> argument, or <code>NULL</code> if an error occurred. </p>
<p> The Fn magic_buffer function returns a textual description of the contents of the <i>buffer</i> argument with <i>length</i> bytes size. </p>
<p> The Fn magic_setflags function sets the <i>flags</i> described above. Note that using both MIME flags together can also return extra information on the charset. </p>
<p> The Fn magic_check function can be used to check the validity of entries in the colon separated database files passed in as <i>filename</i> or <code>NULL</code> for the default database. It returns 0 on success and -1 on failure. </p>
<p> The Fn magic_compile function can be used to compile the the colon separated list of database files passed in as <i>filename</i> or <code>NULL</code> for the default database. It returns 0 on success and -1 on failure. The compiled files created are named from the <a href="/docs/linux/man/1-basename/">basename</a>(1) of each file argument with &#8220;.mgc&#8221; appended to it. </p>
<p> The Fn magic_list function dumps all magic entries in a human readable format, dumping first the entries that are matched against binary files and then the ones that match text files. It takes and optional Fa filename argument which is a colon separated list of database files, or <code>NULL</code> for the default database. </p>
<p> The Fn magic_load function must be used to load the the colon separated list of database files passed in as <i>filename</i> or <code>NULL</code> for the default database file before any magic queries can performed. </p>
<p> The default database file is named by the MAGIC environment variable. If that variable is not set, the default database file name is /usr/share/misc/magic. Fn magic_load adds &#8220;.mgc&#8221; to the database filename as appropriate.</p>
<h2>RETURN VALUES</h2>
<p> The function Fn magic_open returns a magic cookie on success and <code>NULL</code> on failure setting errno to an appropriate value. It will set errno to Er EINVAL if an unsupported value for flags was given. The Fn magic_list , Fn magic_load , Fn magic_compile , and Fn magic_check functions return 0 on success and -1 on failure. The Fn magic_buffer , Fn magic_getpath , and Fn magic_file , functions return a string on success and <code>NULL</code> on failure. The Fn magic_error function returns a textual description of the errors of the above functions, or <code>NULL</code> if there was no error. Finally, Fn magic_setflags returns -1 on systems that don&#8217;t support utime(3), or <a href="/docs/linux/man/2-utimes/">utimes</a>(2) when <code>MAGIC_PRESERVE_ATIME</code> is set.</p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/misc/magic </code></dt>
<dd> The non-compiled default magic database.</dd>
<dt><code>/usr/share/misc/magic.mgc </code></dt>
<dd> The compiled default magic database.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-file/">file</a>(1), <a href="/docs/linux/man/5-magic/">magic</a>(5)</p>
<h2>AUTHORS</h2>
<p> An M&aring;ns Rullg&aring;rd Initial libmagic implementation, and configuration. An Christos Zoulas API cleanup, error code and allocation handling. </p>
<h2>Index</h2>
