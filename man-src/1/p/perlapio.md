---
title: "perlapio(1)"
name: "perlapio"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlapio/"
description: "perlapio – perl’s IO abstraction interface."
---

<h2 class="name">NAME</h2>
<p> perlapio &#8211; perl&#8217;s IO abstraction interface. </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define PERLIO_NOT_STDIO 0 /* For co-existence with stdio only */
#include &lt;perlio.h&gt;        /* Usually via #include &lt;perl.h&gt; */
PerlIO *PerlIO_stdin(void);
PerlIO *PerlIO_stdout(void);
PerlIO *PerlIO_stderr(void);
PerlIO *PerlIO_open(const char *path, const char *mode);
PerlIO *PerlIO_fdopen(int fd, const char *mode);
PerlIO *PerlIO_reopen(const char *path, /* deprecated */
                      const char *mode, PerlIO *old);
int PerlIO_close(PerlIO *f);
int PerlIO_stdoutf(const char *fmt, ...) int PerlIO_puts(PerlIO *f, const char *string);
int PerlIO_putc(PerlIO *f, int ch);
SSize_t PerlIO_write(PerlIO *f, const void *buf, size_t numbytes);
int PerlIO_printf(PerlIO *f, const char *fmt, ...);
int PerlIO_vprintf(PerlIO *f, const char *fmt, va_list args);
int PerlIO_flush(PerlIO *f);
int PerlIO_eof(PerlIO *f);
int PerlIO_error(PerlIO *f);
void PerlIO_clearerr(PerlIO *f);
int PerlIO_getc(PerlIO *d);
int PerlIO_ungetc(PerlIO *f, int ch);
SSize_t PerlIO_read(PerlIO *f, void *buf, size_t numbytes);
int PerlIO_fileno(PerlIO *f);
void PerlIO_setlinebuf(PerlIO *f);
Off_t PerlIO_tell(PerlIO *f);
int PerlIO_seek(PerlIO *f, Off_t offset, int whence);
void PerlIO_rewind(PerlIO *f);
int PerlIO_getpos(PerlIO *f, SV *save);  /* prototype changed */
int PerlIO_setpos(PerlIO *f, SV *saved); /* prototype changed */
int PerlIO_fast_gets(PerlIO *f);
int PerlIO_has_cntptr(PerlIO *f);
SSize_t PerlIO_get_cnt(PerlIO *f);
char *PerlIO_get_ptr(PerlIO *f);
void PerlIO_set_ptrcnt(PerlIO *f, char *ptr, SSize_t count);
int PerlIO_canset_cnt(PerlIO *f);          /* deprecated */
void PerlIO_set_cnt(PerlIO *f, int count); /* deprecated */
int PerlIO_has_base(PerlIO *f);
char *PerlIO_get_base(PerlIO *f);
SSize_t PerlIO_get_bufsiz(PerlIO *f);
PerlIO *PerlIO_importFILE(FILE *stdio, const char *mode);
FILE *PerlIO_exportFILE(PerlIO *f, const char *mode);
FILE *PerlIO_findFILE(PerlIO *f);
void PerlIO_releaseFILE(PerlIO *f, FILE *stdio);
int PerlIO_apply_layers(PerlIO *f, const char *mode,
                        const char *layers);
int PerlIO_binmode(PerlIO *f, int ptype, int imode,
                   const char *layers);
void PerlIO_debug(const char *fmt, ...)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Perl&#8217;s source code, and extensions that want maximum portability, should use the above functions instead of those defined in <font SIZE="-1">ANSI C</font>&#8216;s <i>stdio.h</i>. The perl headers (in particular &#8220;perlio.h&#8221;) will <tt>&quot;#define&quot;</tt> them to the I/O mechanism selected at Configure time. </p>
<p> The functions are modeled on those in <i>stdio.h</i>, but parameter order has been &#8220;tidied up a little&#8221;. </p>
<p> <tt>&quot;PerlIO *&quot;</tt> takes the place of <font SIZE="-1">FILE</font> *. Like <font SIZE="-1">FILE</font> * it should be treated as opaque (it is probably safe to assume it is a pointer to something). </p>
<p> There are currently two implementations:</p>
<dl>
<dt>1. <font SIZE="-1">USE_STDIO</font></p>
<dd> All above are #define&#8217;d to stdio functions or are trivial wrapper functions which call stdio. In this case <i>only</i> PerlIO * is a <font SIZE="-1">FILE</font> *. This has been the default implementation since the abstraction was introduced in perl5.003_02.</p>
<dt>2. <font SIZE="-1">USE_PERLIO</font></p>
<dd> Introduced just after perl5.7.0, this is a re-implementation of the above abstraction which allows perl more control over how <font SIZE="-1">IO</font> is done as it decouples <font SIZE="-1">IO</font> from the way the operating system and C library choose to do things. For <font SIZE="-1">USE_PERLIO</font> PerlIO * has an extra layer of indirection &#8211; it is a pointer-to-a-pointer. This allows the PerlIO * to remain with a known value while swapping the implementation around underneath <i>at run time</i>. In this case all the above are true (but very simple) functions which call the underlying implementation. </p>
<p> This is the only implementation for which <tt>&quot;PerlIO_apply_layers()&quot;</tt> does anything &#8220;interesting&#8221;. </p>
<p> The <font SIZE="-1">USE_PERLIO</font> implementation is described in perliol.</dl>
<p> Because &#8220;perlio.h&#8221; is a thin layer (for efficiency) the semantics of these functions are somewhat dependent on the underlying implementation. Where these variations are understood they are noted below. </p>
<p> Unless otherwise noted, functions return 0 on success, or a negative value (usually <tt>&quot;EOF&quot;</tt> which is usually -1) and set <tt>&quot;errno&quot;</tt> on error.</p>
<dl>
<dt><code>PerlIO_stdin()</code>, <code>PerlIO_stdout()</code>, <code>PerlIO_stderr()</code></p>
<dd> Use these rather than <tt>&quot;stdin&quot;</tt>, <tt>&quot;stdout&quot;</tt>, <tt>&quot;stderr&quot;</tt>. They are written to look like &#8220;function calls&#8221; rather than variables because this makes it easier to <i>make them</i> function calls if platform cannot export data to loaded modules, or if (say) different &#8220;threads&#8221; might have different values.</p>
<dt><code>PerlIO_open(path, mode)</code>, <code>PerlIO_fdopen(fd,mode)</code></p>
<dd> These correspond to <code>fopen()</code>/<code>fdopen()</code> and the arguments are the same. Return <tt>&quot;NULL&quot;</tt> and set <tt>&quot;errno&quot;</tt> if there is an error. There may be an implementation limit on the number of open handles, which may be lower than the limit on the number of open files &#8211; <tt>&quot;errno&quot;</tt> may not be set when <tt>&quot;NULL&quot;</tt> is returned if this limit is exceeded.</p>
<dt><code>PerlIO_reopen(path,mode,f)</code></p>
<dd> While this currently exists in both implementations, perl itself does not use it. <i>As perl does not use it, it is not well tested.</i> </p>
<p> Perl prefers to <tt>&quot;dup&quot;</tt> the new low-level descriptor to the descriptor used by the existing PerlIO. This may become the behaviour of this function in the future.</p>
<dt><code>PerlIO_printf(f,fmt,&#8230;)</code>, <code>PerlIO_vprintf(f,fmt,a)</code></p>
<dd> These are <code>fprintf()</code>/<code>vfprintf()</code> equivalents.</p>
<dt><code>PerlIO_stdoutf(fmt,&#8230;)</code></p>
<dd> This is <code>printf()</code> equivalent. printf is #defined to this function, so it is (currently) legal to use <tt>&quot;printf(fmt,...)&quot;</tt> in perl sources.</p>
<dt><code>PerlIO_read(f,buf,count)</code>, <code>PerlIO_write(f,buf,count)</code></p>
<dd> These correspond functionally to <code>fread()</code> and <code>fwrite()</code> but the arguments and return values are different. The <code>PerlIO_read()</code> and <code>PerlIO_write()</code> signatures have been modeled on the more sane low level <code>read()</code> and <code>write()</code> functions instead: The &#8220;file&#8221; argument is passed first, there is only one &#8220;count&#8221;, and the return value can distinguish between error and <tt>&quot;EOF&quot;</tt>. </p>
<p> Returns a byte count if successful (which may be zero or positive), returns negative value and sets <tt>&quot;errno&quot;</tt> on error. Depending on implementation <tt>&quot;errno&quot;</tt> may be <tt>&quot;EINTR&quot;</tt> if operation was interrupted by a signal.</p>
<dt><code>PerlIO_close(f)</code></p>
<dd> Depending on implementation <tt>&quot;errno&quot;</tt> may be <tt>&quot;EINTR&quot;</tt> if operation was interrupted by a signal.</p>
<dt><code>PerlIO_puts(f,s)</code>, <code>PerlIO_putc(f,c)</code></p>
<dd> These correspond to <code>fputs()</code> and <code>fputc()</code>. Note that arguments have been revised to have &#8220;file&#8221; first.</p>
<dt><code>PerlIO_ungetc(f,c)</code></p>
<dd> This corresponds to <code>ungetc()</code>. Note that arguments have been revised to have &#8220;file&#8221; first. Arranges that next read operation will return the byte <code>c</code>. Despite the implied &#8220;character&#8221; in the name only values in the range 0..0xFF are defined. Returns the byte <code>c</code> on success or -1 (<tt>&quot;EOF&quot;</tt>) on error. The number of bytes that can be &#8220;pushed back&#8221; may vary, only 1 character is certain, and then only if it is the last character that was read from the handle.</p>
<dt><code>PerlIO_getc(f)</code></p>
<dd> This corresponds to <code>getc()</code>. Despite the c in the name only byte range 0..0xFF is supported. Returns the character read or -1 (<tt>&quot;EOF&quot;</tt>) on error.</p>
<dt><code>PerlIO_eof(f)</code></p>
<dd> This corresponds to <code>feof()</code>. Returns a true/false indication of whether the handle is at end of file. For terminal devices this may or may not be &#8220;sticky&#8221; depending on the implementation. The flag is cleared by <code>PerlIO_seek()</code>, or <code>PerlIO_rewind()</code>.</p>
<dt><code>PerlIO_error(f)</code></p>
<dd> This corresponds to <code>ferror()</code>. Returns a true/false indication of whether there has been an <font SIZE="-1">IO</font> error on the handle.</p>
<dt><code>PerlIO_fileno(f)</code></p>
<dd> This corresponds to <code>fileno()</code>, note that on some platforms, the meaning of &#8220;fileno&#8221; may not match Unix. Returns -1 if the handle has no open descriptor associated with it.</p>
<dt><code>PerlIO_clearerr(f)</code></p>
<dd> This corresponds to <code>clearerr()</code>, i.e., clears &#8216;error&#8217; and (usually) &#8216;eof&#8217; flags for the &#8220;stream&#8221;. Does not return a value.</p>
<dt><code>PerlIO_flush(f)</code></p>
<dd> This corresponds to <code>fflush()</code>. Sends any buffered write data to the underlying file. If called with <tt>&quot;NULL&quot;</tt> this may flush all open streams (or core dump with some <font SIZE="-1">USE_STDIO</font> implementations). Calling on a handle open for read only, or on which last operation was a read of some kind may lead to undefined behaviour on some <font SIZE="-1">USE_STDIO</font> implementations. The <font SIZE="-1">USE_PERLIO</font> (layers) implementation tries to behave better: it flushes all open streams when passed <tt>&quot;NULL&quot;</tt>, and attempts to retain data on read streams either in the buffer or by seeking the handle to the current logical position.</p>
<dt><code>PerlIO_seek(f,offset,whence)</code></p>
<dd> This corresponds to <code>fseek()</code>. Sends buffered write data to the underlying file, or discards any buffered read data, then positions the file descriptor as specified by <code>offset</code> and <code>whence</code> (sic). This is the correct thing to do when switching between read and write on the same handle (see issues with <code>PerlIO_flush()</code> above). Offset is of type <tt>&quot;Off_t&quot;</tt> which is a perl Configure value which may not be same as stdio&#8217;s <tt>&quot;off_t&quot;</tt>.</p>
<dt><code>PerlIO_tell(f)</code></p>
<dd> This corresponds to <code>ftell()</code>. Returns the current file position, or (Off_t) -1 on error. May just return value system &#8220;knows&#8221; without making a system call or checking the underlying file descriptor (so use on shared file descriptors is not safe without a <code>PerlIO_seek()</code>). Return value is of type <tt>&quot;Off_t&quot;</tt> which is a perl Configure value which may not be same as stdio&#8217;s <tt>&quot;off_t&quot;</tt>.</p>
<dt><code>PerlIO_getpos(f,p)</code>, <code>PerlIO_setpos(f,p)</code></p>
<dd> These correspond (loosely) to <code>fgetpos()</code> and <code>fsetpos()</code>. Rather than stdio&#8217;s Fpos_t they expect a &#8220;Perl Scalar Value&#8221; to be passed. What is stored there should be considered opaque. The layout of the data may vary from handle to handle. When not using stdio or if platform does not have the stdio calls then they are implemented in terms of <code>PerlIO_tell()</code> and <code>PerlIO_seek()</code>.</p>
<dt><code>PerlIO_rewind(f)</code></p>
<dd> This corresponds to <code>rewind()</code>. It is usually defined as being </p>
<p>PerlIO_seek(f, (Off_t)0L, SEEK_SET);<br />
PerlIO_clearerr(f);</p>
<dt><code>PerlIO_tmpfile()</code></p>
<dd> This corresponds to <code>tmpfile()</code>, i.e., returns an anonymous PerlIO or <font SIZE="-1">NULL</font> on error. The system will attempt to automatically delete the file when closed. On Unix the file is usually <tt>&quot;unlink&quot;</tt>-ed just after it is created so it does not matter how it gets closed. On other systems the file may only be deleted if closed via <code>PerlIO_close()</code> and/or the program exits via <tt>&quot;exit&quot;</tt>. Depending on the implementation there may be &#8220;race conditions&#8221; which allow other processes access to the file, though in general it will be safer in this regard than ad. hoc. schemes.</p>
<dt><code>PerlIO_setlinebuf(f)</code></p>
<dd> This corresponds to <code>setlinebuf()</code>. Does not return a value. What constitutes a &#8220;line&#8221; is implementation dependent but usually means that writing &#8220;
&#8221; flushes the buffer. What happens with things like &#8220;this
that&#8221; is uncertain. (Perl core uses it <i>only</i> when &#8220;dumping&#8221;; it has nothing to do with $| auto-flush.)</dl>
<h3>Co-existence with stdio</h3>
<p> There is outline support for co-existence of PerlIO with stdio. Obviously if PerlIO is implemented in terms of stdio there is no problem. However in other cases then mechanisms must exist to create a <font SIZE="-1">FILE</font> * which can be passed to library code which is going to use stdio calls. </p>
<p> The first step is to add this line: </p>
<p>#define PERLIO_NOT_STDIO 0</p>
<p> <i>before</i> including any perl header files. (This will probably become the default at some point). That prevents &#8220;perlio.h&#8221; from attempting to #define stdio functions onto PerlIO functions. </p>
<p> <font SIZE="-1">XS</font> code is probably better using &#8220;typemap&#8221; if it expects <font SIZE="-1">FILE</font> * arguments. The standard typemap will be adjusted to comprehend any changes in this area.</p>
<dl>
<dt><code>PerlIO_importFILE(f,mode)</code></p>
<dd> Used to get a PerlIO * from a <font SIZE="-1">FILE</font> *. </p>
<p> The mode argument should be a string as would be passed to fopen/PerlIO_open. If it is <font SIZE="-1">NULL</font> then &#8211; for legacy support &#8211; the code will (depending upon the platform and the implementation) either attempt to empirically determine the mode in which <i>f</i> is open, or use &#8220;r+&#8221; to indicate a read/write stream. </p>
<p> Once called the <font SIZE="-1">FILE</font> * should <i></i><font SIZE="-1"><i>ONLY</i></font><i></i> be closed by calling <tt>&quot;PerlIO_close()&quot;</tt> on the returned PerlIO *. </p>
<p> The PerlIO is set to textmode. Use PerlIO_binmode if this is not the desired mode. </p>
<p> This is <code>not</code> the reverse of <code>PerlIO_exportFILE()</code>.</p>
<dt><code>PerlIO_exportFILE(f,mode)</code></p>
<dd> Given a PerlIO * create a &#8216;native&#8217; <font SIZE="-1">FILE</font> * suitable for passing to code expecting to be compiled and linked with <font SIZE="-1">ANSI C</font> <i>stdio.h</i>. The mode argument should be a string as would be passed to fopen/PerlIO_open. If it is <font SIZE="-1">NULL</font> then &#8211; for legacy support &#8211; the <font SIZE="-1">FILE</font> * is opened in same mode as the PerlIO *. </p>
<p> The fact that such a <font SIZE="-1">FILE</font> * has been &#8216;exported&#8217; is recorded, (normally by pushing a new :stdio &#8220;layer&#8221; onto the PerlIO *), which may affect future PerlIO operations on the original PerlIO *. You should not call <tt>&quot;fclose()&quot;</tt> on the file unless you call <tt>&quot;PerlIO_releaseFILE()&quot;</tt> to disassociate it from the PerlIO *. (Do not use <code>PerlIO_importFILE()</code> for doing the disassociation.) </p>
<p> Calling this function repeatedly will create a <font SIZE="-1">FILE</font> * on each call (and will push an :stdio layer each time as well).</p>
<dt><code>PerlIO_releaseFILE(p,f)</code></p>
<dd> Calling PerlIO_releaseFILE informs PerlIO that all use of <font SIZE="-1">FILE</font> * is complete. It is removed from the list of &#8216;exported&#8217; <font SIZE="-1">FILE</font> *s, and the associated PerlIO * should revert to its original behaviour. </p>
<p> Use this to disassociate a file from a PerlIO * that was associated using <code>PerlIO_exportFILE()</code>.</p>
<dt><code>PerlIO_findFILE(f)</code></p>
<dd> Returns a native <font SIZE="-1">FILE</font> * used by a stdio layer. If there is none, it will create one with PerlIO_exportFILE. In either case the <font SIZE="-1">FILE</font> * should be considered as belonging to PerlIO subsystem and should only be closed by calling <tt>&quot;PerlIO_close()&quot;</tt>.</dl>
<h3>Fast gets Functions</h3>
<p> In addition to standard-like <font SIZE="-1">API</font> defined so far above there is an &#8220;implementation&#8221; interface which allows perl to get at internals of PerlIO. The following calls correspond to the various FILE_xxx macros determined by Configure &#8211; or their equivalent in other implementations. This section is really of interest to only those concerned with detailed perl-core behaviour, implementing a PerlIO mapping or writing code which can make use of the &#8220;read ahead&#8221; that has been done by the <font SIZE="-1">IO</font> system in the same way perl does. Note that any code that uses these interfaces must be prepared to do things the traditional way if a handle does not support them.</p>
<dl>
<dt><code>PerlIO_fast_gets(f)</code></p>
<dd> Returns true if implementation has all the interfaces required to allow perl&#8217;s <tt>&quot;sv_gets&quot;</tt> to &#8220;bypass&#8221; normal <font SIZE="-1">IO</font> mechanism. This can vary from handle to handle. </p>
<pre>
  PerlIO_fast_gets(f) = PerlIO_has_cntptr(f) &amp;&amp; \
                        PerlIO_canset_cnt(f) &amp;&amp; \
                        'Can set pointer into buffer'
</pre>
<dt><code>PerlIO_has_cntptr(f)</code></p>
<dd> Implementation can return pointer to current position in the &#8220;buffer&#8221; and a count of bytes available in the buffer. Do not use this &#8211; use PerlIO_fast_gets.</p>
<dt><code>PerlIO_get_cnt(f)</code></p>
<dd> Return count of readable bytes in the buffer. Zero or negative return means no more bytes available.</p>
<dt><code>PerlIO_get_ptr(f)</code></p>
<dd> Return pointer to next readable byte in buffer, accessing via the pointer (dereferencing) is only safe if <code>PerlIO_get_cnt()</code> has returned a positive value. Only positive offsets up to value returned by <code>PerlIO_get_cnt()</code> are allowed.</p>
<dt><code>PerlIO_set_ptrcnt(f,p,c)</code></p>
<dd> Set pointer into buffer, and a count of bytes still in the buffer. Should be used only to set pointer to within range implied by previous calls to <tt>&quot;PerlIO_get_ptr&quot;</tt> and <tt>&quot;PerlIO_get_cnt&quot;</tt>. The two values <i>must</i> be consistent with each other (implementation may only use one or the other or may require both).</p>
<dt><code>PerlIO_canset_cnt(f)</code></p>
<dd> Implementation can adjust its idea of number of bytes in the buffer. Do not use this &#8211; use PerlIO_fast_gets.</p>
<dt><code>PerlIO_set_cnt(f,c)</code></p>
<dd> Obscure &#8211; set count of bytes in the buffer. Deprecated. Only usable if <code>PerlIO_canset_cnt()</code> returns true. Currently used in only doio.c to force count less than -1 to -1. Perhaps should be PerlIO_set_empty or similar. This call may actually do nothing if &#8220;count&#8221; is deduced from pointer and a &#8220;limit&#8221;. Do not use this &#8211; use <code>PerlIO_set_ptrcnt()</code>.</p>
<dt><code>PerlIO_has_base(f)</code></p>
<dd> Returns true if implementation has a buffer, and can return pointer to whole buffer and its size. Used by perl for <code>-T</code> / <code>-B</code> tests. Other uses would be very obscure&#8230;</p>
<dt><code>PerlIO_get_base(f)</code></p>
<dd> Return <i>start</i> of buffer. Access only positive offsets in the buffer up to the value returned by <code>PerlIO_get_bufsiz()</code>.</p>
<dt><code>PerlIO_get_bufsiz(f)</code></p>
<dd> Return the <i>total number of bytes</i> in the buffer, this is neither the number that can be read, nor the amount of memory allocated to the buffer. Rather it is what the operating system and/or implementation happened to <tt>&quot;read()&quot;</tt> (or whatever) last time <font SIZE="-1">IO</font> was requested.</dl>
<h3>Other Functions</h3>
<dl>
<dt>PerlIO_apply_layers(f,mode,layers)</p>
<dd> The new interface to the <font SIZE="-1">USE_PERLIO</font> implementation. The layers &#8220;:crlf&#8221; and &#8220;:raw&#8221; are only ones allowed for other implementations and those are silently ignored. (As of perl5.8 &#8220;:raw&#8221; is deprecated.) Use <code>PerlIO_binmode()</code> below for the portable case.</p>
<dt>PerlIO_binmode(f,ptype,imode,layers)</p>
<dd> The hook used by perl&#8217;s <tt>&quot;binmode&quot;</tt> operator. <code>ptype</code> is perl&#8217;s character for the kind of <font SIZE="-1">IO:</font></p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8216;&lt;&#8216; read</p>
<dd>
<dt>&#8216;&gt;&#8217; write</p>
<dd>
<dt>&#8216;+&#8217; read/write</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>imode</code> is <tt>&quot;O_BINARY&quot;</tt> or <tt>&quot;O_TEXT&quot;</tt>. </p>
<p> <code>layers</code> is a string of layers to apply, only &#8220;:crlf&#8221; makes sense in the non <font SIZE="-1">USE_PERLIO</font> case. (As of perl5.8 &#8220;:raw&#8221; is deprecated in favour of passing <font SIZE="-1">NULL.</font>) </p>
<p> Portable cases are: </p>
<pre><code>
PerlIO_binmode(f, ptype, O_BINARY, NULL);
and PerlIO_binmode(f, ptype, O_TEXT, ":crlf");
</code></pre>
<p> On Unix these calls probably have no effect whatsoever. Elsewhere they alter &#8220;
&#8221; to <font SIZE="-1">CR,LF</font> translation and possibly cause a special text &#8220;end of file&#8221; indicator to be written or honoured on read. The effect of making the call after doing any <font SIZE="-1">IO</font> to the handle depends on the implementation. (It may be ignored, affect any data which is already buffered as well, or only apply to subsequent data.)</dl>
<dt>PerlIO_debug(fmt,&#8230;)</p>
<dd> PerlIO_debug is a <code>printf()</code>-like function which can be used for debugging. No return value. Its main use is inside PerlIO where using real printf, <code>warn()</code> etc. would recursively call PerlIO and be a problem. </p>
<p> PerlIO_debug writes to the file named by <tt>$ENV</tt>{&#8216;<font SIZE="-1">PERLIO_DEBUG</font>&#8216;} or defaults to stderr if the environment variable is not defined. Typical use might be </p>
<pre>
  Bourne shells (sh, ksh, bash, zsh, ash, ...):
   PERLIO_DEBUG=/tmp/perliodebug.log ./perl -Di somescript some args
  Csh/Tcsh:
   setenv PERLIO_DEBUG /tmp/perliodebug.log
   ./perl -Di somescript some args
  If you have the &quot;env&quot; utility:
   env PERLIO_DEBUG=/tmp/perliodebug.log ./perl -Di somescript args
  Win32:
   set PERLIO_DEBUG=perliodebug.log
   perl -Di somescript some args
</pre>
<p> On a Perl built without <tt>&quot;-DDEBUGGING&quot;</tt>, or when the <tt>&quot;-Di&quot;</tt> command-line switch is not specified, or under taint, <code>PerlIO_debug()</code> is a no-op. </p>
</dl>
<h2>Index</h2>
