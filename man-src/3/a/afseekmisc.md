---
title: "afseekmisc(3)"
name: "afseekmisc"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afseekmisc/"
---

afReadMisc, afWriteMisc, afSeekMisc - access miscellaneous metadata in an audio file 

<h2>Synopsis</h2><pre>#include &lt;audiofile.h&gt;</pre><pre>int afReadMisc (AFfilehandle file, int miscid, void *buffer, int nbytes);</pre><pre>int afWriteMisc (AFfilehandle file, int miscid, const void *buffer, int nbytes);</pre><pre>int afSeekMisc (AFfilehandle file, int miscid, int offbytes);</pre><h2>Description</h2>afReadMisc reads up to <i>nbytes</i> from the miscellaneous data chunk identified by <i>miscid</i> in <i>file</i>. 

 afWriteMisc writes up to <i>nbytes</i> to the miscellaneous data chunk identified by <i>miscid</i> in <i>file</i>. 

 afSeekMisc changes the current offset within the miscellaneous data chunk identified by <i>miscid</i> to the offset <i>offbytes</i>.
<h2>Return Value</h2>afReadMisc returns the number of bytes read from the specified miscellaneous chunk into the buffer referred to by <i>buffer</i>. 

 afWriteMisc returns the number of bytes written to the specified miscellaneous chunk from the buffer referred to by <i>buffer</i>. 

 afSeekMisc returns the new location of the logical data pointer as measured as an offset in bytes from the beginning of the miscellaneous chunk's data area.
<h2>Errors</h2>afReadMisc, afWriteMisc, and afSeekMisc can produce the following error codes: 

<dl COMPACT><dd>&bull; 

 AF_BAD_READ</dl><dl COMPACT><dd>&bull; 

 AF_BAD_WRITE</dl><dl COMPACT><dd>&bull; 

 AF_BAD_MISCSEEK</dl><dl COMPACT><dd>&bull; 

 AF_BAD_MISCID</dl><dl COMPACT><dd>&bull; 

 AF_BAD_TRACKID</dl><dl COMPACT><dd>&bull; 

 AF_BAD_FILEHANDLE</dl><h2>Author</h2>Michael Pruett &lt;michael [at] 68k.org&gt;
