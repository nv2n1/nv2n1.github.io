---
title: "pack_fopen(3)"
name: "pack_fopen"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pack_fopen/"
description: "pack_fopen – Opens a file according to mode. Allegro game programming library."
---

<p>pack_fopen &#8211; Opens a file according to mode. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>PACKFILE *pack_fopen(const char *filename, const char *mode);</code></p>
<h2>Description</h2>
<p>Opens a file according to mode, which may contain any of the flags: `r&#8217; &#8211; open file for reading. `w&#8217; &#8211; open file for writing, overwriting any existing data. `p&#8217; &#8211; open file in packed mode. Data will be compressed as it is written to the file, and automatically uncompressed during read operations. Files created in this mode will produce garbage if they are read without this flag being set. `!&#8217; &#8211; open file for writing in normal, unpacked mode, but add the value F_NOPACK_MAGIC to the start of the file, so that it can later be opened in packed mode and Allegro will automatically detect that the data does not need to be decompressed. Instead of these flags, one of the constants F_READ, F_WRITE, F_READ_PACKED, F_WRITE_PACKED or F_WRITE_NOPACK may be used as the mode parameter. The packfile functions also understand several &quot;magic&quot; filenames that are used for special purposes. These are: `#&#8217; &#8211; read data that has been appended to your executable file with the exedat utility, as if it was a regular independent disk file. `filename.dat#object_name&#8217; &#8211; open a specific object from a datafile, and read from it as if it was a regular file. You can treat nested datafiles exactly like a normal directory structure, for example you could open `filename.dat#graphics/level1/mapdata&#8217;. `#object_name&#8217; &#8211; combination of the above, reading an object from a datafile that has been appended onto your executable. With these special filenames, the contents of a datafile object or appended file can be read in an identical way to a normal disk file, so any of the file access functions in Allegro (eg. load_pcx() and set_config_file()) can be used to read from them. Note that you can&#8217;t write to these special files, though: the fake file is read only. Also, you must save your datafile uncompressed or with per-object compression if you are planning on loading individual objects from it (otherwise there will be an excessive amount of seeking when it is read). Finally, be aware that the special Allegro object types aren&#8217;t the same format as the files you import the data from. When you import data like bitmaps or samples into the grabber, they are converted into a special Allegro-specific format, but the `#&#8217; marker file syntax reads the objects as raw binary chunks. This means that if, for example, you want to use load_pcx() to read an image from a datafile, you should import it as a binary block rather than as a BITMAP object. Example: </p>
<pre><code>PACKFILE *input_file;

input_file = pack_fopen(&quot;scores.dat&quot;, &quot;rp&quot;);
if (!input_file)
    abort_on_error(&quot;Couldn't read `scores.dat'!&quot;);</code></pre>
<h2>Return Value</h2>
<p>On success, pack_fopen() returns a pointer to a PACKFILE structure, and on error it returns NULL and stores an error code in `errno&#8217;. An attempt to read a normal file in packed mode will cause `errno&#8217; to be set to EDOM. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fclose/">pack_fclose</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_chunk/">pack_fopen_chunk</a></code>(3), <code><a href="/docs/linux/man/3-packfile_password/">packfile_password</a></code>(3), <code><a href="/docs/linux/man/3-pack_fread/">pack_fread</a></code>(3), <code><a href="/docs/linux/man/3-pack_getc/">pack_getc</a></code>(3), <code><a href="/docs/linux/man/3-file_select_ex/">file_select_ex</a></code>(3), <code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3) </p>
