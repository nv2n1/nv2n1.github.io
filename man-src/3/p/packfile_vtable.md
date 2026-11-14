---
title: "packfile_vtable(3)"
name: "packfile_vtable"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packfile_vtable/"
description: "PACKFILE_VTABLE – Packfile vtable structure, for custom packfiles. Allegro game programming library."
---

<p>PACKFILE_VTABLE &#8211; Packfile vtable structure, for custom packfiles. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct PACKFILE_VTABLE</code></p>
<h2>Description</h2>
<pre> int pf_fclose(void *userdata);
 int pf_getc(void *userdata);
 int pf_ungetc(int c, void *userdata);
 long pf_fread(void *p, long n, void *userdata);
 int pf_putc(int c, void *userdata);
 long pf_fwrite(const void *p, long n, void *userdata);
 int pf_fseek(void *userdata, int offset);
 int pf_feof(void *userdata);
 int pf_ferror(void *userdata);</pre>
<p>This is the vtable which must be provided for custom packfiles, which then can read from and write to wherever you like (eg. files in memory). You should provide all the entries of the vtable, even if they are empty stubs doing nothing, to avoid Allegro (or you) calling a NULL method at some point. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pack_fopen_vtable/">pack_fopen_vtable</a></code>(3), <code><a href="/docs/linux/man/3-expackf/">expackf</a></code>(3)</p>
