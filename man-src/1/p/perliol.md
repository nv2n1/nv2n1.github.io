---
title: "perliol(1)"
name: "perliol"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perliol/"
---

<h2 class="name">NAME</h2>
 

 perliol - C API for Perl's implementation of IO in Layers. 

<h2>SYNOPSIS</h2>

 <pre><code>
/* Defining a layer ... */
#include &lt;perliol.h&gt;
</code></pre>

<h2>DESCRIPTION</h2>

 This document describes the behavior and implementation of the PerlIO abstraction described in perlapio when <tt>&quot;USE_PERLIO&quot;</tt> is defined.

<h3>History and Background</h3>

 The PerlIO abstraction was introduced in perl5.003_02 but languished as just an abstraction until perl5.7.0. However during that time a number of perl extensions switched to using it, so the <font SIZE="-1">API</font> is mostly fixed to maintain (source) compatibility. 

 The aim of the implementation is to provide the PerlIO <font SIZE="-1">API</font> in a flexible and platform neutral manner. It is also a trial of an ``Object Oriented C, with vtables'' approach which may be applied to Perl 6.

<h3>Basic Structure</h3>

 PerlIO is a stack of layers. 

 The low levels of the stack work with the low-level operating system calls (file descriptors in C) getting bytes in and out, the higher layers of the stack buffer, filter, and otherwise manipulate the I/O, and return characters (or bytes) to Perl. Terms <i>above</i> and <i>below</i> are used to refer to the relative positioning of the stack layers. 

 A layer contains a ``vtable'', the table of I/O operations (at C level a table of function pointers), and status flags. The functions in the vtable implement operations like ``open'', ``read'', and ``write''. 

 When I/O, for example ``read'', is requested, the request goes from Perl first down the stack using ``read'' functions of each layer, then at the bottom the input is requested from the operating system services, then the result is returned up the stack, finally being interpreted as Perl data. 

 The requests do not necessarily go always all the way down to the operating system: that's where PerlIO buffering comes into play. 

 When you do an <b>open()</b> and specify extra PerlIO layers to be deployed, the layers you specify are ``pushed'' on top of the already existing default stack. One way to see it is that ``operating system is on the left'' and ``Perl is on the right''. 

 What exact layers are in this default stack depends on a lot of things: your operating system, Perl version, Perl compile time configuration, and Perl runtime configuration. See PerlIO, ``<font SIZE="-1">PERLIO''</font> in perlrun, and open for more information. 

 <b>binmode()</b> operates similarly to <b>open()</b>: by default the specified layers are pushed on top of the existing stack. 

 However, note that even as the specified layers are ``pushed on top'' for <b>open()</b> and <b>binmode()</b>, this doesn't mean that the effects are limited to the ``top'': PerlIO layers can be very 'active' and inspect and affect layers also deeper in the stack. As an example there is a layer called ``raw'' which repeatedly ``pops'' layers until it reaches the first layer that has declared itself capable of handling binary data. The ``pushed'' layers are processed in left-to-right order. 

 <b>sysopen()</b> operates (unsurprisingly) at a lower level in the stack than <b>open()</b>. For example in Unix or Unix-like systems <b>sysopen()</b> operates directly at the level of file descriptors: in the terms of PerlIO layers, it uses only the ``unix'' layer, which is a rather thin wrapper on top of the Unix file descriptors.

<h3>Layers vs Disciplines</h3>

 Initial discussion of the ability to modify <font SIZE="-1">IO</font> streams behaviour used the term ``discipline'' for the entities which were added. This came (I believe) from the use of the term in ``sfio'', which in turn borrowed it from ``line disciplines'' on Unix terminals. However, this document (and the C code) uses the term ``layer''. 

 This is, I hope, a natural term given the implementation, and should avoid connotations that are inherent in earlier uses of ``discipline'' for things which are rather different.

<h3>Data Structures</h3>

 The basic data structure is a PerlIOl: 

 
typedef struct _PerlIO PerlIOl;
typedef struct _PerlIO_funcs PerlIO_funcs;
typedef PerlIOl *PerlIO;
struct _PerlIO {
    PerlIOl *next;     /* Lower layer */
    PerlIO_funcs *tab; /* Functions for this layer */
    U32 flags;         /* Various flags for state */
};
 

 A <tt>&quot;PerlIOl *&quot;</tt> is a pointer to the struct, and the <i>application</i> level <tt>&quot;PerlIO *&quot;</tt> is a pointer to a <tt>&quot;PerlIOl *&quot;</tt> - i.e. a pointer to a pointer to the struct. This allows the application level <tt>&quot;PerlIO *&quot;</tt> to remain constant while the actual <tt>&quot;PerlIOl *&quot;</tt> underneath changes. (Compare perl's <tt>&quot;SV *&quot;</tt> which remains constant while its <tt>&quot;sv_any&quot;</tt> field changes as the scalar's type changes.) An <font SIZE="-1">IO</font> stream is then in general represented as a pointer to this linked-list of ``layers''. 

 It should be noted that because of the double indirection in a <tt>&quot;PerlIO *&quot;</tt>, a <tt>&quot;&amp;(perlio-&gt;next)&quot;</tt> ``is'' a <tt>&quot;PerlIO *&quot;</tt>, and so to some degree at least one layer can use the ``standard'' <font SIZE="-1">API</font> on the next layer down. 

 A ``layer'' is composed of two parts:
<dl>
<dt>1.
<dd> The functions and attributes of the ``layer class''.
<dt>2.
<dd> The per-instance data for a particular handle.</dl>

<h3>Functions and Attributes</h3>

 The functions and attributes are accessed via the ``tab'' (for table) member of <tt>&quot;PerlIOl&quot;</tt>. The functions (methods of the layer ``class'') are fixed, and are defined by the <tt>&quot;PerlIO_funcs&quot;</tt> type. They are broadly the same as the public <tt>&quot;PerlIO_xxxxx&quot;</tt> functions: 

 
struct _PerlIO_funcs {
    Size_t fsize;
    char *name;
    Size_t size;
    IV kind;
    IV (*Pushed)
    (pTHX_ PerlIO *f,
     const char *mode,
     SV *arg,
     PerlIO_funcs *tab);
    IV (*Popped)
    (pTHX_ PerlIO *f);
    PerlIO *(*Open)(pTHX_ PerlIO_funcs *tab,
                    PerlIO_list_t *layers, IV n,
                    const char *mode,
                    int fd, int imode, int perm,
                    PerlIO *old,
                    int narg, SV **args);
    IV (*Binmode)
    (pTHX_ PerlIO *f);
    SV *(*Getarg)(pTHX_ PerlIO *f, CLONE_PARAMS *param, int flags)
        IV (*Fileno)(pTHX_ PerlIO *f);
    PerlIO *(*Dup)(pTHX_ PerlIO *f,
                   PerlIO *o,
                   CLONE_PARAMS *param,
                   int flags)
        /* Unix-like functions - cf sfio line disciplines */
        SSize_t (*Read)(pTHX_ PerlIO *f, void *vbuf, Size_t count);
    SSize_t (*Unread)(pTHX_ PerlIO *f, const void *vbuf, Size_t count);
    SSize_t (*Write)(pTHX_ PerlIO *f, const void *vbuf, Size_t count);
    IV (*Seek)
    (pTHX_ PerlIO *f, Off_t offset, int whence);
    Off_t (*Tell)(pTHX_ PerlIO *f);
    IV (*Close)
    (pTHX_ PerlIO *f);
    /* Stdio-like buffered IO functions */
    IV (*Flush)
    (pTHX_ PerlIO *f);
    IV (*Fill)
    (pTHX_ PerlIO *f);
    IV (*Eof)
    (pTHX_ PerlIO *f);
    IV (*Error)
    (pTHX_ PerlIO *f);
    void (*Clearerr)(pTHX_ PerlIO *f);
    void (*Setlinebuf)(pTHX_ PerlIO *f);
    /* Perl's snooping functions */
    STDCHAR *(*Get_base)(pTHX_ PerlIO *f);
    Size_t (*Get_bufsiz)(pTHX_ PerlIO *f);
    STDCHAR *(*Get_ptr)(pTHX_ PerlIO *f);
    SSize_t (*Get_cnt)(pTHX_ PerlIO *f);
    void (*Set_ptrcnt)(pTHX_ PerlIO *f, STDCHAR *ptr, SSize_t cnt);
};
 

 The first few members of the struct give a function table size for compatibility check ``name'' for the layer, the size to <tt>&quot;malloc&quot;</tt> for the per-instance data, and some flags which are attributes of the class as whole (such as whether it is a buffering layer), then follow the functions which fall into four basic groups:
<dl>
<dt>1.
<dd> Opening and setup functions
<dt>2.
<dd> Basic <font SIZE="-1">IO</font> operations
<dt>3.
<dd> Stdio class buffering options.
<dt>4.
<dd> Functions to support Perl's traditional ``fast'' access to the buffer.</dl>
 

 A layer does not have to implement all the functions, but the whole table has to be present. Unimplemented slots can be <font SIZE="-1">NULL</font> (which will result in an error when called) or can be filled in with stubs to ``inherit'' behaviour from a ``base class''. This ``inheritance'' is fixed for all instances of the layer, but as the layer chooses which stubs to populate the table, limited ``multiple inheritance'' is possible.

<h3>Per-instance Data</h3>

 The per-instance data are held in memory beyond the basic PerlIOl struct, by making a PerlIOl the first member of the layer's struct thus: 

 
typedef struct
{
    struct _PerlIO base; /* Base "class" info */
    STDCHAR *buf;        /* Start of buffer */
    STDCHAR *end;        /* End of valid part of buffer */
    STDCHAR *ptr;        /* Current position in buffer */
    Off_t posn;          /* Offset of buf into the file */
    Size_t bufsiz;       /* Real size of buffer */
    IV oneword;          /* Emergency buffer */
} PerlIOBuf;
 

 In this way (as for perl's scalars) a pointer to a PerlIOBuf can be treated as a pointer to a PerlIOl.

<h3>Layers in action.</h3>

 
table perlio unix | |
    +-- -- -- -- -- -+ +-- -- -- -- --+ +-- -- -- --+PerlIO-&gt;| | ---&gt;| next | ---&gt;| NULL |
    +-- -- -- -- -- -+ +-- -- -- -- --+ +-- -- -- --+ | | | buffer | | fd |
    +-- -- -- -- -- -+ | | +-- -- -- --+ | | +-- -- -- -- --+
 

 The above attempts to show how the layer scheme works in a simple case. The application's <tt>&quot;PerlIO *&quot;</tt> points to an entry in the table(s) representing open (allocated) handles. For example the first three slots in the table correspond to <tt>&quot;stdin&quot;</tt>,<tt>&quot;stdout&quot;</tt> and <tt>&quot;stderr&quot;</tt>. The table in turn points to the current ``top'' layer for the handle - in this case an instance of the generic buffering layer ``perlio''. That layer in turn points to the next layer down - in this case the low-level ``unix'' layer. 

 The above is roughly equivalent to a ``stdio'' buffered stream, but with much more flexibility:
<dl>
<dt>&bull;
<dd> If Unix level <tt>&quot;read&quot;</tt>/<tt>&quot;write&quot;</tt>/<tt>&quot;lseek&quot;</tt> is not appropriate for (say) sockets then the ``unix'' layer can be replaced (at open time or even dynamically) with a ``socket'' layer.
<dt>&bull;
<dd> Different handles can have different buffering schemes. The ``top'' layer could be the ``mmap'' layer if reading disk files was quicker using <tt>&quot;mmap&quot;</tt> than <tt>&quot;read&quot;</tt>. An ``unbuffered'' stream can be implemented simply by not having a buffer layer.
<dt>&bull;
<dd> Extra layers can be inserted to process the data as it flows through. This was the driving need for including the scheme in perl 5.7.0+ - we needed a mechanism to allow data to be translated between perl's internal encoding (conceptually at least Unicode as <font SIZE="-1">UTF-8</font>), and the ``native'' format used by the system. This is provided by the ``:encoding(xxxx)'' layer which typically sits above the buffering layer.
<dt>&bull;
<dd> A layer can be added that does ``\n'' to <font SIZE="-1">CRLF</font> translation. This layer can be used on any platform, not just those that normally do such things.</dl>

<h3>Per-instance flag bits</h3>

 The generic flag bits are a hybrid of <tt>&quot;O_XXXXX&quot;</tt> style flags deduced from the mode string passed to <tt>&quot;PerlIO_open()&quot;</tt>, and state bits for typical buffer layers.
<dl>
<dt><font SIZE="-1">PERLIO_F_EOF</font>
<dd> End of file.
<dt><font SIZE="-1">PERLIO_F_CANWRITE</font>
<dd> Writes are permitted, i.e. opened as ``w'' or ``r+'' or ``a'', etc.
<dt><font SIZE="-1">PERLIO_F_CANREAD</font>
<dd> Reads are permitted i.e. opened ``r'' or ``w+'' (or even ``a+'' - ick).
<dt><font SIZE="-1">PERLIO_F_ERROR</font>
<dd> An error has occurred (for <tt>&quot;PerlIO_error()&quot;</tt>).
<dt><font SIZE="-1">PERLIO_F_TRUNCATE</font>
<dd> Truncate file suggested by open mode.
<dt><font SIZE="-1">PERLIO_F_APPEND</font>
<dd> All writes should be appends.
<dt><font SIZE="-1">PERLIO_F_CRLF</font>
<dd> Layer is performing Win32-like ``\n'' mapped to <font SIZE="-1">CR,LF</font> for output and <font SIZE="-1">CR,LF</font> mapped to ``\n'' for input. Normally the provided ``crlf'' layer is the only layer that need bother about this. <tt>&quot;PerlIO_binmode()&quot;</tt> will mess with this flag rather than add/remove layers if the <tt>&quot;PERLIO_K_CANCRLF&quot;</tt> bit is set for the layers class.
<dt><font SIZE="-1">PERLIO_F_UTF8</font>
<dd> Data written to this layer should be <font SIZE="-1">UTF-8</font> encoded; data provided by this layer should be considered <font SIZE="-1">UTF-8</font> encoded. Can be set on any layer by ``:utf8'' dummy layer. Also set on ``:encoding'' layer.
<dt><font SIZE="-1">PERLIO_F_UNBUF</font>
<dd> Layer is unbuffered - i.e. write to next layer down should occur for each write to this layer.
<dt><font SIZE="-1">PERLIO_F_WRBUF</font>
<dd> The buffer for this layer currently holds data written to it but not sent to next layer.
<dt><font SIZE="-1">PERLIO_F_RDBUF</font>
<dd> The buffer for this layer currently holds unconsumed data read from layer below.
<dt><font SIZE="-1">PERLIO_F_LINEBUF</font>
<dd> Layer is line buffered. Write data should be passed to next layer down whenever a ``\n'' is seen. Any data beyond the ``\n'' should then be processed.
<dt><font SIZE="-1">PERLIO_F_TEMP</font>
<dd> File has been <tt>&quot;unlink()&quot;</tt>ed, or should be deleted on <tt>&quot;close()&quot;</tt>.
<dt><font SIZE="-1">PERLIO_F_OPEN</font>
<dd> Handle is open.
<dt><font SIZE="-1">PERLIO_F_FASTGETS</font>
<dd> This instance of this layer supports the &quot;fast <tt>&quot;gets&quot;</tt>&quot; interface. Normally set based on <tt>&quot;PERLIO_K_FASTGETS&quot;</tt> for the class and by the existence of the function(s) in the table. However a class that normally provides that interface may need to avoid it on a particular instance. The ``pending'' layer needs to do this when it is pushed above a layer which does not support the interface. (Perl's <tt>&quot;sv_gets()&quot;</tt> does not expect the streams fast <tt>&quot;gets&quot;</tt> behaviour to change during one ``get''.)</dl>

<h3>Methods in Detail</h3>

<dl>
<dt>fsize
<dd> <pre>
        Size_t fsize;
</pre> 

 Size of the function table. This is compared against the value PerlIO code ``knows'' as a compatibility check. Future versions <i>may</i> be able to tolerate layers compiled against an old version of the headers.
<dt>name
<dd> <pre>
        char * name;
</pre> 

 The name of the layer whose <b>open()</b> method Perl should invoke on <b>open()</b>. For example if the layer is called <font SIZE="-1">APR,</font> you will call: 

 <pre>
  open $fh, &quot;&gt;:APR&quot;, ...
</pre> 

 and Perl knows that it has to invoke the <b>PerlIOAPR_open()</b> method implemented by the <font SIZE="-1">APR</font> layer.
<dt>size
<dd> <pre>
        Size_t size;
</pre> 

 The size of the per-instance data structure, e.g.: 

 <pre>
  sizeof(PerlIOAPR)
</pre> 

 If this field is zero then <tt>&quot;PerlIO_pushed&quot;</tt> does not malloc anything and assumes layer's Pushed function will do any required layer stack manipulation - used to avoid malloc/free overhead for dummy layers. If the field is non-zero it must be at least the size of <tt>&quot;PerlIOl&quot;</tt>, <tt>&quot;PerlIO_pushed&quot;</tt> will allocate memory for the layer's data structures and link new layer onto the stream's stack. (If the layer's Pushed method returns an error indication the layer is popped again.)
<dt>kind
<dd> <pre>
        IV kind;
</pre>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> <font SIZE="-1">PERLIO_K_BUFFERED</font> 

 The layer is buffered.
<dt>&bull;
<dd> <font SIZE="-1">PERLIO_K_RAW</font> 

 The layer is acceptable to have in a binmode(<font SIZE="-1">FH</font>) stack - i.e. it does not (or will configure itself not to) transform bytes passing through it.
<dt>&bull;
<dd> <font SIZE="-1">PERLIO_K_CANCRLF</font> 

 Layer can translate between ``\n'' and <font SIZE="-1">CRLF</font> line ends.
<dt>&bull;
<dd> <font SIZE="-1">PERLIO_K_FASTGETS</font> 

 Layer allows buffer snooping.
<dt>&bull;
<dd> <font SIZE="-1">PERLIO_K_MULTIARG</font> 

 Used when the layer's <b>open()</b> accepts more arguments than usual. The extra arguments should come not before the <tt>&quot;MODE&quot;</tt> argument. When this flag is used it's up to the layer to validate the args.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Pushed
<dd> 
IV (*Pushed)
(pTHX_ PerlIO *f, const char *mode, SV *arg);
 

 The only absolutely mandatory method. Called when the layer is pushed onto the stack. The <tt>&quot;mode&quot;</tt> argument may be <font SIZE="-1">NULL</font> if this occurs post-open. The <tt>&quot;arg&quot;</tt> will be non-<tt>&quot;NULL&quot;</tt> if an argument string was passed. In most cases this should call <tt>&quot;PerlIOBase_pushed()&quot;</tt> to convert <tt>&quot;mode&quot;</tt> into the appropriate <tt>&quot;PERLIO_F_XXXXX&quot;</tt> flags in addition to any actions the layer itself takes. If a layer is not expecting an argument it need neither save the one passed to it, nor provide <tt>&quot;Getarg()&quot;</tt> (it could perhaps <tt>&quot;Perl_warn&quot;</tt> that the argument was un-expected). 

 Returns 0 on success. On failure returns -1 and should set errno.
<dt>Popped
<dd> <pre>
        IV      (*Popped)(pTHX_ PerlIO *f);
</pre> 

 Called when the layer is popped from the stack. A layer will normally be popped after <tt>&quot;Close()&quot;</tt> is called. But a layer can be popped without being closed if the program is dynamically managing layers on the stream. In such cases <tt>&quot;Popped()&quot;</tt> should free any resources (buffers, translation tables, ...) not held directly in the layer's struct. It should also <tt>&quot;Unread()&quot;</tt> any unconsumed data that has been read and buffered from the layer below back to that layer, so that it can be re-provided to what ever is now above. 

 Returns 0 on success and failure. If <tt>&quot;Popped()&quot;</tt> returns <i>true</i> then <i>perlio.c</i> assumes that either the layer has popped itself, or the layer is super special and needs to be retained for other reasons. In most cases it should return <i>false</i>.
<dt>Open
<dd> <pre>
        PerlIO *        (*Open)(...);
</pre> 

 The <tt>&quot;Open()&quot;</tt> method has lots of arguments because it combines the functions of perl's <tt>&quot;open&quot;</tt>, <tt>&quot;PerlIO_open&quot;</tt>, perl's <tt>&quot;sysopen&quot;</tt>, <tt>&quot;PerlIO_fdopen&quot;</tt> and <tt>&quot;PerlIO_reopen&quot;</tt>. The full prototype is as follows: 

 
PerlIO *(*Open)(pTHX_ PerlIO_funcs *tab,
                PerlIO_list_t *layers, IV n,
                const char *mode,
                int fd, int imode, int perm,
                PerlIO *old,
                int narg, SV **args);
 

 Open should (perhaps indirectly) call <tt>&quot;PerlIO_allocate()&quot;</tt> to allocate a slot in the table and associate it with the layers information for the opened file, by calling <tt>&quot;PerlIO_push&quot;</tt>. The <i>layers</i> is an array of all the layers destined for the <tt>&quot;PerlIO *&quot;</tt>, and any arguments passed to them, <i>n</i> is the index into that array of the layer being called. The macro <tt>&quot;PerlIOArg&quot;</tt> will return a (possibly <tt>&quot;NULL&quot;</tt>) <font SIZE="-1">SV</font> * for the argument passed to the layer. 

 Where a layer opens or takes ownership of a file descriptor, that layer is responsible for getting the file descriptor's close-on-exec flag into the correct state. The flag should be clear for a file descriptor numbered less than or equal to <tt>&quot;PL_maxsysfd&quot;</tt>, and set for any file descriptor numbered higher. For thread safety, when a layer opens a new file descriptor it should if possible open it with the close-on-exec flag initially set. 

 The <i>mode</i> string is an &quot;<tt>&quot;fopen()&quot;</tt>-like&quot; string which would match the regular expression <tt>&quot;/^[I#]?[rwa]\+?[bt]?$/&quot;</tt>. 

 The <tt>'I'</tt> prefix is used during creation of <tt>&quot;stdin&quot;</tt>..<tt>&quot;stderr&quot;</tt> via special <tt>&quot;PerlIO_fdopen&quot;</tt> calls; the <tt>'#'</tt> prefix means that this is <tt>&quot;sysopen&quot;</tt> and that <i>imode</i> and <i>perm</i> should be passed to <tt>&quot;PerlLIO_open3&quot;</tt>; <tt>'r'</tt> means <b>r</b>ead, <tt>'w'</tt> means <b>w</b>rite and <tt>'a'</tt> means <b>a</b>ppend. The <tt>'+'</tt> suffix means that both reading and writing/appending are permitted. The <tt>'b'</tt> suffix means file should be binary, and <tt>'t'</tt> means it is text. (Almost all layers should do the <font SIZE="-1">IO</font> in binary mode, and ignore the b/t bits. The <tt>&quot;:crlf&quot;</tt> layer should be pushed to handle the distinction.) 

 If <i>old</i> is not <tt>&quot;NULL&quot;</tt> then this is a <tt>&quot;PerlIO_reopen&quot;</tt>. Perl itself does not use this (yet?) and semantics are a little vague. 

 If <i>fd</i> not negative then it is the numeric file descriptor <i>fd</i>, which will be open in a manner compatible with the supplied mode string, the call is thus equivalent to <tt>&quot;PerlIO_fdopen&quot;</tt>. In this case <i>nargs</i> will be zero. The file descriptor may have the close-on-exec flag either set or clear; it is the responsibility of the layer that takes ownership of it to get the flag into the correct state. 

 If <i>nargs</i> is greater than zero then it gives the number of arguments passed to <tt>&quot;open&quot;</tt>, otherwise it will be 1 if for example <tt>&quot;PerlIO_open&quot;</tt> was called. In simple cases SvPV_nolen(*args) is the pathname to open. 

 If a layer provides <tt>&quot;Open()&quot;</tt> it should normally call the <tt>&quot;Open()&quot;</tt> method of next layer down (if any) and then push itself on top if that succeeds. <tt>&quot;PerlIOBase_open&quot;</tt> is provided to do exactly that, so in most cases you don't have to write your own <tt>&quot;Open()&quot;</tt> method. If this method is not defined, other layers may have difficulty pushing themselves on top of it during open. 

 If <tt>&quot;PerlIO_push&quot;</tt> was performed and open has failed, it must <tt>&quot;PerlIO_pop&quot;</tt> itself, since if it's not, the layer won't be removed and may cause bad problems. 

 Returns <tt>&quot;NULL&quot;</tt> on failure.
<dt>Binmode
<dd> <pre>
        IV        (*Binmode)(pTHX_ PerlIO *f);
</pre> 

 Optional. Used when <tt>&quot;:raw&quot;</tt> layer is pushed (explicitly or as a result of binmode(<font SIZE="-1">FH</font>)). If not present layer will be popped. If present should configure layer as binary (or pop itself) and return 0. If it returns -1 for error <tt>&quot;binmode&quot;</tt> will fail with layer still on the stack.
<dt>Getarg
<dd> <pre>
        SV *      (*Getarg)(pTHX_ PerlIO *f,
                            CLONE_PARAMS *param, int flags);
</pre> 

 Optional. If present should return an <font SIZE="-1">SV</font> * representing the string argument passed to the layer when it was pushed. e.g. ``:encoding(ascii)'' would return an SvPV with value ``ascii''. (<i>param</i> and <i>flags</i> arguments can be ignored in most cases) 

 <tt>&quot;Dup&quot;</tt> uses <tt>&quot;Getarg&quot;</tt> to retrieve the argument originally passed to <tt>&quot;Pushed&quot;</tt>, so you must implement this function if your layer has an extra argument to <tt>&quot;Pushed&quot;</tt> and will ever be <tt>&quot;Dup&quot;</tt>ed.
<dt>Fileno
<dd> <pre>
        IV        (*Fileno)(pTHX_ PerlIO *f);
</pre> 

 Returns the Unix/Posix numeric file descriptor for the handle. Normally <tt>&quot;PerlIOBase_fileno()&quot;</tt> (which just asks next layer down) will suffice for this. 

 Returns -1 on error, which is considered to include the case where the layer cannot provide such a file descriptor.
<dt>Dup
<dd> <pre>
        PerlIO * (*Dup)(pTHX_ PerlIO *f, PerlIO *o,
                        CLONE_PARAMS *param, int flags);
</pre> 

 <font SIZE="-1">XXX:</font> Needs more docs. 

 Used as part of the ``clone'' process when a thread is spawned (in which case param will be non-NULL) and when a stream is being duplicated via '&amp;' in the <tt>&quot;open&quot;</tt>. 

 Similar to <tt>&quot;Open&quot;</tt>, returns PerlIO* on success, <tt>&quot;NULL&quot;</tt> on failure.
<dt>Read
<dd> <pre>
        SSize_t (*Read)(pTHX_ PerlIO *f, void *vbuf, Size_t count);
</pre> 

 Basic read operation. 

 Typically will call <tt>&quot;Fill&quot;</tt> and manipulate pointers (possibly via the <font SIZE="-1">API</font>). <tt>&quot;PerlIOBuf_read()&quot;</tt> may be suitable for derived classes which provide ``fast gets'' methods. 

 Returns actual bytes read, or -1 on an error.
<dt>Unread
<dd> <pre>
        SSize_t (*Unread)(pTHX_ PerlIO *f,
                          const void *vbuf, Size_t count);
</pre> 

 A superset of stdio's <tt>&quot;ungetc()&quot;</tt>. Should arrange for future reads to see the bytes in <tt>&quot;vbuf&quot;</tt>. If there is no obviously better implementation then <tt>&quot;PerlIOBase_unread()&quot;</tt> provides the function by pushing a ``fake'' ``pending'' layer above the calling layer. 

 Returns the number of unread chars.
<dt>Write
<dd> 
SSize_t (*Write)(PerlIO *f, const void *vbuf, Size_t count);
 

 Basic write operation. 

 Returns bytes written or -1 on an error.
<dt>Seek
<dd> <pre>
        IV      (*Seek)(pTHX_ PerlIO *f, Off_t offset, int whence);
</pre> 

 Position the file pointer. Should normally call its own <tt>&quot;Flush&quot;</tt> method and then the <tt>&quot;Seek&quot;</tt> method of next layer down. 

 Returns 0 on success, -1 on failure.
<dt>Tell
<dd> <pre>
        Off_t   (*Tell)(pTHX_ PerlIO *f);
</pre> 

 Return the file pointer. May be based on layers cached concept of position to avoid overhead. 

 Returns -1 on failure to get the file pointer.
<dt>Close
<dd> <pre>
        IV      (*Close)(pTHX_ PerlIO *f);
</pre> 

 Close the stream. Should normally call <tt>&quot;PerlIOBase_close()&quot;</tt> to flush itself and close layers below, and then deallocate any data structures (buffers, translation tables, ...) not held directly in the data structure. 

 Returns 0 on success, -1 on failure.
<dt>Flush
<dd> <pre>
        IV      (*Flush)(pTHX_ PerlIO *f);
</pre> 

 Should make stream's state consistent with layers below. That is, any buffered write data should be written, and file position of lower layers adjusted for data read from below but not actually consumed. (Should perhaps <tt>&quot;Unread()&quot;</tt> such data to the lower layer.) 

 Returns 0 on success, -1 on failure.
<dt>Fill
<dd> <pre>
        IV      (*Fill)(pTHX_ PerlIO *f);
</pre> 

 The buffer for this layer should be filled (for read) from layer below. When you ``subclass'' PerlIOBuf layer, you want to use its <i>_read</i> method and to supply your own fill method, which fills the PerlIOBuf's buffer. 

 Returns 0 on success, -1 on failure.
<dt>Eof
<dd> <pre>
        IV      (*Eof)(pTHX_ PerlIO *f);
</pre> 

 Return end-of-file indicator. <tt>&quot;PerlIOBase_eof()&quot;</tt> is normally sufficient. 

 Returns 0 on end-of-file, 1 if not end-of-file, -1 on error.
<dt>Error
<dd> <pre>
        IV      (*Error)(pTHX_ PerlIO *f);
</pre> 

 Return error indicator. <tt>&quot;PerlIOBase_error()&quot;</tt> is normally sufficient. 

 Returns 1 if there is an error (usually when <tt>&quot;PERLIO_F_ERROR&quot;</tt> is set), 0 otherwise.
<dt>Clearerr
<dd> <pre>
        void    (*Clearerr)(pTHX_ PerlIO *f);
</pre> 

 Clear end-of-file and error indicators. Should call <tt>&quot;PerlIOBase_clearerr()&quot;</tt> to set the <tt>&quot;PERLIO_F_XXXXX&quot;</tt> flags, which may suffice.
<dt>Setlinebuf
<dd> <pre>
        void    (*Setlinebuf)(pTHX_ PerlIO *f);
</pre> 

 Mark the stream as line buffered. <tt>&quot;PerlIOBase_setlinebuf()&quot;</tt> sets the <font SIZE="-1">PERLIO_F_LINEBUF</font> flag and is normally sufficient.
<dt>Get_base
<dd> <pre>
        STDCHAR *       (*Get_base)(pTHX_ PerlIO *f);
</pre> 

 Allocate (if not already done so) the read buffer for this layer and return pointer to it. Return <font SIZE="-1">NULL</font> on failure.
<dt>Get_bufsiz
<dd> <pre>
        Size_t  (*Get_bufsiz)(pTHX_ PerlIO *f);
</pre> 

 Return the number of bytes that last <tt>&quot;Fill()&quot;</tt> put in the buffer.
<dt>Get_ptr
<dd> <pre>
        STDCHAR *       (*Get_ptr)(pTHX_ PerlIO *f);
</pre> 

 Return the current read pointer relative to this layer's buffer.
<dt>Get_cnt
<dd> <pre>
        SSize_t (*Get_cnt)(pTHX_ PerlIO *f);
</pre> 

 Return the number of bytes left to be read in the current buffer.
<dt>Set_ptrcnt
<dd> <pre>
        void    (*Set_ptrcnt)(pTHX_ PerlIO *f,
                              STDCHAR *ptr, SSize_t cnt);
</pre> 

 Adjust the read pointer and count of bytes to match <tt>&quot;ptr&quot;</tt> and/or <tt>&quot;cnt&quot;</tt>. The application (or layer above) must ensure they are consistent. (Checking is allowed by the paranoid.)</dl>

<h3>Utilities</h3>

 To ask for the next layer down use PerlIONext(PerlIO *f). 

 To check that a PerlIO* is valid use PerlIOValid(PerlIO *f). (All this does is really just to check that the pointer is non-NULL and that the pointer behind that is non-NULL.) 

 PerlIOBase(PerlIO *f) returns the ``Base'' pointer, or in other words, the <tt>&quot;PerlIOl*&quot;</tt> pointer. 

 PerlIOSelf(PerlIO* f, type) return the PerlIOBase cast to a type. 

 Perl_PerlIO_or_Base(PerlIO* f, callback, base, failure, args) either calls the <i>callback</i> from the functions of the layer <i>f</i> (just by the name of the <font SIZE="-1">IO</font> function, like ``Read'') with the <i>args</i>, or if there is no such callback, calls the <i>base</i> version of the callback with the same args, or if the f is invalid, set errno to <font SIZE="-1">EBADF</font> and return <i>failure</i>. 

 Perl_PerlIO_or_fail(PerlIO* f, callback, failure, args) either calls the <i>callback</i> of the functions of the layer <i>f</i> with the <i>args</i>, or if there is no such callback, set errno to <font SIZE="-1">EINVAL.</font> Or if the f is invalid, set errno to <font SIZE="-1">EBADF</font> and return <i>failure</i>. 

 Perl_PerlIO_or_Base_void(PerlIO* f, callback, base, args) either calls the <i>callback</i> of the functions of the layer <i>f</i> with the <i>args</i>, or if there is no such callback, calls the <i>base</i> version of the callback with the same args, or if the f is invalid, set errno to <font SIZE="-1">EBADF.</font> 

 Perl_PerlIO_or_fail_void(PerlIO* f, callback, args) either calls the <i>callback</i> of the functions of the layer <i>f</i> with the <i>args</i>, or if there is no such callback, set errno to <font SIZE="-1">EINVAL.</font> Or if the f is invalid, set errno to <font SIZE="-1">EBADF.</font>

<h3>Implementing PerlIO Layers</h3>

 If you find the implementation document unclear or not sufficient, look at the existing PerlIO layer implementations, which include:
<dl>
<dt>&bull;
<dd> C implementations 

 The <i>perlio.c</i> and <i>perliol.h</i> in the Perl core implement the ``unix'', ``perlio'', ``stdio'', ``crlf'', ``utf8'', ``byte'', ``raw'', ``pending'' layers, and also the ``mmap'' and ``win32'' layers if applicable. (The ``win32'' is currently unfinished and unused, to see what is used instead in Win32, see ``Querying the layers of filehandles'' in PerlIO .) 

 PerlIO::encoding, PerlIO::scalar, PerlIO::via in the Perl core. 

 PerlIO::gzip and APR::PerlIO (mod_perl 2.0) on <font SIZE="-1">CPAN.</font>
<dt>&bull;
<dd> Perl implementations 

 PerlIO::via::QuotedPrint in the Perl core and PerlIO::via::* on <font SIZE="-1">CPAN.</font></dl>
 

 If you are creating a PerlIO layer, you may want to be lazy, in other words, implement only the methods that interest you. The other methods you can either replace with the ``blank'' methods 

 <pre>
    PerlIOBase_noop_ok
    PerlIOBase_noop_fail
</pre> 

 (which do nothing, and return zero and -1, respectively) or for certain methods you may assume a default behaviour by using a <font SIZE="-1">NULL</font> method. The Open method looks for help in the 'parent' layer. The following table summarizes the behaviour: 

 
    method      behaviour with NULL
    Clearerr    PerlIOBase_clearerr
    Close       PerlIOBase_close
    Dup         PerlIOBase_dup
    Eof         PerlIOBase_eof
    Error       PerlIOBase_error
    Fileno      PerlIOBase_fileno
    Fill        FAILURE
    Flush       SUCCESS
    Getarg      SUCCESS
    Get_base    FAILURE
    Get_bufsiz  FAILURE
    Get_cnt     FAILURE
    Get_ptr     FAILURE
    Open        INHERITED
    Popped      SUCCESS
    Pushed      SUCCESS
    Read        PerlIOBase_read
    Seek        FAILURE
    Set_cnt     FAILURE
    Set_ptrcnt  FAILURE
    Setlinebuf  PerlIOBase_setlinebuf
    Tell        FAILURE
    Unread      PerlIOBase_unread
    Write       FAILURE
 FAILURE        Set errno (to EINVAL in Unixish, to LIB$_INVARG in VMS)
                and return -1 (for numeric return values) or NULL (for
                pointers)
 INHERITED      Inherited from the layer below
 SUCCESS        Return 0 (for numeric return values) or a pointer


<h3>Core Layers</h3>

 The file <tt>&quot;perlio.c&quot;</tt> provides the following layers:
<dl>
<dt>&quot;unix&quot;
<dd> A basic non-buffered layer which calls Unix/POSIX <tt>&quot;read()&quot;</tt>, <tt>&quot;write()&quot;</tt>, <tt>&quot;lseek()&quot;</tt>, <tt>&quot;close()&quot;</tt>. No buffering. Even on platforms that distinguish between O_TEXT and O_BINARY this layer is always O_BINARY.
<dt>&quot;perlio&quot;
<dd> A very complete generic buffering layer which provides the whole of PerlIO <font SIZE="-1">API.</font> It is also intended to be used as a ``base class'' for other layers. (For example its <tt>&quot;Read()&quot;</tt> method is implemented in terms of the <tt>&quot;Get_cnt()&quot;</tt>/<tt>&quot;Get_ptr()&quot;</tt>/<tt>&quot;Set_ptrcnt()&quot;</tt> methods). 

 ``perlio'' over ``unix'' provides a complete replacement for stdio as seen via PerlIO <font SIZE="-1">API.</font> This is the default for <font SIZE="-1">USE_PERLIO</font> when system's stdio does not permit perl's ``fast gets'' access, and which do not distinguish between <tt>&quot;O_TEXT&quot;</tt> and <tt>&quot;O_BINARY&quot;</tt>.
<dt>&quot;stdio&quot;
<dd> A layer which provides the PerlIO <font SIZE="-1">API</font> via the layer scheme, but implements it by calling system's stdio. This is (currently) the default if system's stdio provides sufficient access to allow perl's ``fast gets'' access and which do not distinguish between <tt>&quot;O_TEXT&quot;</tt> and <tt>&quot;O_BINARY&quot;</tt>.
<dt>&quot;crlf&quot;
<dd> A layer derived using ``perlio'' as a base class. It provides Win32-like ``\n'' to <font SIZE="-1">CR,LF</font> translation. Can either be applied above ``perlio'' or serve as the buffer layer itself. ``crlf'' over ``unix'' is the default if system distinguishes between <tt>&quot;O_TEXT&quot;</tt> and <tt>&quot;O_BINARY&quot;</tt> opens. (At some point ``unix'' will be replaced by a ``native'' Win32 <font SIZE="-1">IO</font> layer on that platform, as Win32's read/write layer has various drawbacks.) The ``crlf'' layer is a reasonable model for a layer which transforms data in some way.
<dt>&quot;mmap&quot;
<dd> If Configure detects <tt>&quot;mmap()&quot;</tt> functions this layer is provided (with ``perlio'' as a ``base'') which does ``read'' operations by <b>mmap()</b>ing the file. Performance improvement is marginal on modern systems, so it is mainly there as a proof of concept. It is likely to be unbundled from the core at some point. The ``mmap'' layer is a reasonable model for a minimalist ``derived'' layer.
<dt>&quot;pending&quot;
<dd> An ``internal'' derivative of ``perlio'' which can be used to provide <b>Unread()</b> function for layers which have no buffer or cannot be bothered. (Basically this layer's <tt>&quot;Fill()&quot;</tt> pops itself off the stack and so resumes reading from layer below.)
<dt>&quot;raw&quot;
<dd> A dummy layer which never exists on the layer stack. Instead when ``pushed'' it actually pops the stack removing itself, it then calls Binmode function table entry on all the layers in the stack - normally this (via PerlIOBase_binmode) removes any layers which do not have <tt>&quot;PERLIO_K_RAW&quot;</tt> bit set. Layers can modify that behaviour by defining their own Binmode entry.
<dt>&quot;utf8&quot;
<dd> Another dummy layer. When pushed it pops itself and sets the <tt>&quot;PERLIO_F_UTF8&quot;</tt> flag on the layer which was (and now is once more) the top of the stack.</dl>
 

 In addition <i>perlio.c</i> also provides a number of <tt>&quot;PerlIOBase_xxxx()&quot;</tt> functions which are intended to be used in the table slots of classes which do not need to do anything special for a particular method.

<h3>Extension Layers</h3>

 Layers can be made available by extension modules. When an unknown layer is encountered the PerlIO code will perform the equivalent of : 

 <pre>
   use PerlIO 'layer';
</pre> 

 Where <i>layer</i> is the unknown layer. <i>PerlIO.pm</i> will then attempt to: 

 <pre>
   require PerlIO::layer;
</pre> 

 If after that process the layer is still not defined then the <tt>&quot;open&quot;</tt> will fail. 

 The following extension layers are bundled with perl:
<dl>
<dt>&quot;:encoding&quot;
<dd> <pre>
   use Encoding;
</pre> 

 makes this layer available, although <i>PerlIO.pm</i> ``knows'' where to find it. It is an example of a layer which takes an argument as it is called thus: 

 <pre>
   open( $fh, &quot;&lt;:encoding(iso-8859-7)&quot;, $pathname );
</pre>
<dt>&quot;:scalar&quot;
<dd> Provides support for reading data from and writing data to a scalar. 

 <pre>
   open( $fh, &quot;+&lt;:scalar&quot;, \$scalar );
</pre> 

 When a handle is so opened, then reads get bytes from the string value of <i></i>$scalar<i></i>, and writes change the value. In both cases the position in <i></i>$scalar<i></i> starts as zero but can be altered via <tt>&quot;seek&quot;</tt>, and determined via <tt>&quot;tell&quot;</tt>. 

 Please note that this layer is implied when calling <b>open()</b> thus: 

 <pre>
   open( $fh, &quot;+&lt;&quot;, \$scalar );
</pre>
<dt>&quot;:via&quot;
<dd> Provided to allow layers to be implemented as Perl code. For instance: 

 <pre>
   use PerlIO::via::StripHTML;
   open( my $fh, &quot;&lt;:via(StripHTML)&quot;, &quot;index.html&quot; );
</pre> 

 See PerlIO::via for details.</dl>

<h2>TODO</h2>

 Things that need to be done to improve this document.
<dl>
<dt>&bull;
<dd> Explain how to make a valid fh without going through <b>open()</b>(i.e. apply a layer). For example if the file is not opened through perl, but we want to get back a fh, like it was opened by Perl. 

 How PerlIO_apply_layera fits in, where its docs, was it made public? 

 Currently the example could be something like this: 

 <pre><code>
PerlIO *foo_to_PerlIO(pTHX_ char *mode, ...)
{
    char *mode;                  /* "w", "r", etc */
    const char *layers = ":APR"; /* the layer name */
    PerlIO *f = PerlIO_allocate(aTHX);
    if (!f) {
        return NULL;
    }
    PerlIO_apply_layers(aTHX_ f, mode, layers);
    if (f) {
        PerlIOAPR *st = PerlIOSelf(f, PerlIOAPR);
        /* fill in the st struct, as in _open() */
        st-&gt;file = file;
        PerlIOBase(f)-&gt;flags |= PERLIO_F_OPEN;
        return f;
    }
    return NULL;
}
</code></pre>
<dt>&bull;
<dd> fix/add the documentation in places marked as <font SIZE="-1">XXX.</font>
<dt>&bull;
<dd> The handling of errors by the layer is not specified. e.g. when $! should be set explicitly, when the error handling should be just delegated to the top layer. 

 Probably give some hints on using <font SIZE="-1"><b>SETERRNO</b></font><b>()</b> or pointers to where they can be found.
<dt>&bull;
<dd> I think it would help to give some concrete examples to make it easier to understand the <font SIZE="-1">API.</font> Of course I agree that the <font SIZE="-1">API</font> has to be concise, but since there is no second document that is more of a guide, I think that it'd make it easier to start with the doc which is an <font SIZE="-1">API,</font> but has examples in it in places where things are unclear, to a person who is not a PerlIO guru (yet). 

</dl>

<h2>Index</h2>


