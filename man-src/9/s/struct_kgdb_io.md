---
title: "struct_kgdb_io(9)"
name: "struct_kgdb_io"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_kgdb_io/"
description: "struct_kgdb_io – Describe the interface for an I/O driver to talk with KGDB."
---

<p>struct_kgdb_io &#8211; Describe the interface for an I/O driver to talk with KGDB.</p>
<h2>Synopsis</h2>
<pre><code>struct kgdb_io {
    const char *name;
    int (*read_char)(void);
    void (*write_char)(u8);
    void (*flush)(void);
    int (*init)(void);
    void (*pre_exception)(void);
    void (*post_exception)(void);
    int is_console;
};</code></pre>
<h2>Members</h2>
<p>name</p>
<dl>
<dd>Name of the I/O driver.</dl>
<p> read_char</p>
<dl>
<dd>Pointer to a function that will return one char.</dl>
<p> write_char</p>
<dl>
<dd>Pointer to a function that will write one char.</dl>
<p> flush</p>
<dl>
<dd>Pointer to a function that will flush any pending writes.</dl>
<p> init</p>
<dl>
<dd>Pointer to a function that will initialize the device.</dl>
<p> pre_exception</p>
<dl>
<dd>Pointer to a function that will do any prep work for the I/O driver.</dl>
<p> post_exception</p>
<dl>
<dd>Pointer to a function that will do any cleanup work for the I/O driver.</dl>
<p> is_console</p>
<dl>
<dd>1 if the end device is a console 0 if the I/O device is not a console</dl>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
