---
title: "packfile_password(3)"
name: "packfile_password"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packfile_password/"
description: "packfile_password – Sets the global I/O encryption password. Allegro game programming library."
---

<p>packfile_password &#8211; Sets the global I/O encryption password. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void packfile_password(const char *password);</code></pre>
<h2>Description</h2>
<p>Sets the encryption password to be used for all read/write operations on files opened in future using Allegro&#8217;s packfile functions (whether they are compressed or not), including all the save, load and config routines. Files written with an encryption password cannot be read unless the same password is selected, so be careful: if you forget the key, nobody can make your data come back again! Pass NULL or an empty string to return to the normal, non-encrypted mode. If you are using this function to prevent people getting access to your datafiles, be careful not to store an obvious copy of the password in your executable: if there are any strings like &quot;I&#8217;m the password for the datafile&quot;, it would be fairly easy to get access to your data :-) Note #1: when writing a packfile, you can change the password to whatever you want after opening the file, without affecting the write operation. On the contrary, when writing a sub-chunk of a packfile, you must make sure that the password that was active at the time the sub-chunk was opened is still active before closing the sub-chunk. This is guaranteed to be true if you didn&#8217;t call the packfile_password() routine in the meantime. Read operations, either on packfiles or sub-chunks, have no such restriction. Note #2: as explained above, the password is used for all read/write operations on files, including for several functions of the library that operate on files without explicitly using packfiles (e.g. load_bitmap()). The unencrypted mode is mandatory in order for those functions to work. Therefore remember to call packfile_password(NULL) before using them if you previously changed the password. As a rule of thumb, always call packfile_password(NULL) when you are done with operations on packfiles. The only exception to this is custom packfiles created with pack_fopen_vtable(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen/">pack_fopen</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3) </p>
