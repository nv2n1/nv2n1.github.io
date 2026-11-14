---
title: "install_allegro(3)"
name: "install_allegro"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_allegro/"
description: "install_allegro – Initialise the Allegro library."
---

<h2>NAME</h2>
<p> install_allegro &#8211; Initialise the Allegro library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_allegro(int system_id, int *errno_ptr, int (*atexit_ptr)());</code></p>
<h2>DESCRIPTION</h2>
<p> Initialises the Allegro library. You must call either this or allegro_init() before doing anything other than using the Unicode routines. If you want to use a text mode other than UTF-8, you can set it with set_uformat() before you call this. The other functions that can be called before this one will be marked explicitly in the documentation, like set_config_file(). </p>
<p> The available system ID codes will vary from one platform to another, but you will almost always want to pass SYSTEM_AUTODETECT. Alternatively, SYSTEM_NONE installs a stripped down version of Allegro that won&#8217;t even try to touch your hardware or do anything platform specific: this can be useful for situations where you only want to manipulate memory bitmaps, such as the text mode datafile tools or the Windows GDI interfacing functions. </p>
<p> The `errno_ptr&#8217; and `atexit_ptr&#8217; parameters should point to the errno variable and atexit function from your libc: these are required because when Allegro is linked as a DLL, it doesn&#8217;t have direct access to your local libc data. `atexit_ptr&#8217; may be NULL, in which case it is your responsibility to call allegro_exit() manually. Example: </p>
<pre>
   install_allegro(SYSTEM_AUTODETECT, &amp;errno, atexit);
</pre>
<h2>RETURN VALUE</h2>
<p> This function returns zero on success and non-zero on failure (e.g. no system driver could be used). Note: in previous versions of Allegro this function would abort on error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-allegro_exit/">allegro_exit</a></code>(3), <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-set_config_file/">set_config_file</a></code>(3) </p>
<h2>Index</h2>
