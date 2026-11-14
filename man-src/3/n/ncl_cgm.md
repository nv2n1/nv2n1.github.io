---
title: "ncl_cgm(3)"
name: "ncl_cgm"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_cgm/"
description: "CGM_open, CGM_close, CGM_lseek, CGM_read, CGM_write, CGM_directory, CGM_freeDirectory, CGM_printDirectory, CGM_getInstr, CGM_flushGetInstr, CGM_putInstr, CGM_flushOutputInstr, CGM_initMetaEdit, CGM..."
---

<p>CGM_open, CGM_close, CGM_lseek, CGM_read, CGM_write, CGM_directory, CGM_freeDirectory, CGM_printDirectory, CGM_getInstr, CGM_flushGetInstr, CGM_putInstr, CGM_flushOutputInstr, CGM_initMetaEdit, CGM_termMetaEdit, CGM_copyFrames, CGM_deleteFrames, CGM_mergeFrames CGM_moveFrames, CGM_readFrames, CGM_valid, CGM_writeFile, CGM_writeFrames, CGM_appendFrames &#8211; Computer Graphics Metafile operations</p>
<h2>Syntax</h2>
<pre><code>#include &lt;cgm_tools.h&gt;</code>
<code>Cgm_fd CGM_open(metafile, size, flags, mode)</code>
<code>char *metafile;</code>
<code>unsigned size;</code>
<code>int flags;</code>
<code>int mode;</code>
<code>int CGM_close(cgm_fd)</code>
<code>Cgm_fd cgm_fd;</code>
<code>int CGM_lseek(cgm_fd, offset)</code>
<code>Cgm_fd cgm_fd;</code>
<code>int offset;</code>
<code>int CGM_read(cgm_fd, buf)</code>
<code>Cgm_fd cgm_fd;</code>
<code>unsigned char *buf;</code>
<code>int CGM_write(cgm_fd, buf)</code>
<code>Cgm_fd cgm_fd;</code>
<code>unsigned char *buf;</code>
<code>Directory *CGM_directory(cgm_fd)</code>
<code>Cgm_fd cgm_fd;</code>
<code>void CGM_freeDirectory(dir)</code>
<code>Directory *dir;</code>
<code>void CGM_printDirectory(dir)</code>
<code>Directory *dir;</code>
<code>int CGM_getInstr(cgm_fd, instr)</code>
<code>Cgm_fd cgm_fd;</code>
<code>Instr *instr;</code>
<code>void CGM_flushGetInstr(cgm_fd)</code>
<code>Cgm_fd cgm_fd;</code>
<code>int CGM_putInstr(cgm_fd, instr)</code>
<code>Cgm_fd cgm_fd;</code>
<code>Instr *instr;</code>
<code>int CGM_flushOutputInstr(cgm_fd)</code>
<code>Cgm_fd cgm_fd;</code>
<code>Directory *CGM_initMetaEdit (metafile, size)</code>
<code>char *metafile;</code>
<code>unsigned int size;</code>
<code>int CGM_termMetaEdit()</code>
<code>Directory *CGM_copyFrames(start, num, target )</code>
<code>unsigned int start;</code>
<code>int num;</code>
<code>unsigned int target;</code>
<code>Directory *CGM_deleteFrames(start, num)</code>
<code>unsigned int start,</code>
<code>num;</code>
<code>Directory *CGM_mergeFrames(bottom, top)</code>
<code>unsigned bottom, top;</code>
<code>Directory *CGM_moveFrames (start, num, target)</code>
<code>unsigned int start, num, target;</code>
<code>Directory *CGM_readFrames(metafile, start, num, target, size)</code>
<code>char *metafile;</code>
<code>unsigned int start;</code>
<code>int num;</code>
<code>unsigned int target, size;</code>
<code>int *CGM_validCGM(metafile)</code>
<code>char *metafile;</code>
<code>int CGM_writeFile(metafile)</code>
<code>char *metafile;</code>
<code>int CGM_writeFrames(metafile, start, num)</code>
<code>char *metafile;</code>
<code>unsigned start, num;</code>
<code>int CGM_appendFrames(metafile, start, num)</code>
<code>char *metafile;</code>
<code>unsigned start, num;</code></pre>
<h2>Description</h2>
<p>The argument <i>cgm_fd</i> refers to a valid file descriptor created for reading or writing, as appropriate by <code>CGM_open</code>. <code>CGM_read</code>, <code>CGM_directory</code>, <code>CGM_getInstr</code> and <code>CGM_flushGetInstr</code> require a file descriptor open for reading. <code>CGM_write</code>, <code>CGM_getInstr</code>,<code>CGM_flushGetInstr</code> and <code>CGM_flushOutputInstr</code> require a <i>Cgm_fd</i> open for writing. <code>CGM_close</code> and <code>CGM_lseek</code> will accept any valid <i>Cgm_fd</i>. </p>
<p> The <i>size</i> argument refers to the CGM record size in bytes. For an NCAR CGM this value is 1440. </p>
<p> <i>buf</i> is a pointer to user allocated memory of size <i>size</i>. This storage will be used for buffering input and output of <code>CGM_read</code> and <code>CGM_write</code> respectively. </p>
<p> The <i>dir</i> argument is a pointer to a <i>Directory</i> structure created with <code>CGM_directory</code> or <code>CGM_initMetaEdit</code>. <i>dir</i> is a private resource that should <i>NOT</i> be directly modified by the user. A set of convenience macros is provided for this purpose in <i>cgm_tools.h</i>. </p>
<p> The <i>start</i>, <i>num</i> and <i>target</i> arguments are used to address frame numbers in a metafile being edited with one of the commands: <code>CGM_copyFrames</code>, <code>CGM_deleteFrames</code>, <code>CGM_readFrames</code>, <code>CGM_moveFrames</code>, <code>CGM_writeFrames</code> and <code>CGM_mergeFrames</code>. The <i>start</i> argument is the first frame in a sequence of <i>num</i> frame(s) to perform the editing operation on. <i>target</i> is similar to <i>start</i> and is used by commands that require two frame addresses such as <i>copy</i>. Addressing begins at zero. </p>
<dl COMPACT>
<dt>CGM_open</p>
<dd>This command is modeled after the unix <i>open</i> command. It will open a CGM for reading or writing as specified by the <i>flags</i> argument and return a <i>Cgm_fd</i> file descriptor. The <i>flags</i> and <i>open</i> parameters are passed directly on to the system <i>open</i> command. For a detailed explanation of these two arguments see <a href="/docs/linux/man/2-open/">open</a>(2).</p>
<dt>CGM_close</p>
<dd>Delete a file descriptor. The inverse of <code>CGM_open</code>. See <a href="/docs/linux/man/2-close/">close</a>(2).</p>
<dt>CGM_read</p>
<dd><code>CGM_read</code> attempts to read <i>size</i> bytes from the object referenced through the descriptor <i>cgm_fd</i>. <i>size</i> is set at the creation of <i>cgm_fd</i> by <code>CGM_open</code>. <code>CGM_read</code> returns the number of bytes successfully read. A zero is returned on EOF and a negative number implies an error occurred. The unix system call <i>read</i> is called by <code>CGM_read</code>. See <a href="/docs/linux/man/2-read/">read</a>(2).</p>
<dt>CGM_write</p>
<dd>Attempts to write a single record of <i>size</i> bytes from <i>buf</i> from the object referenced by <i>cgm_edit</i> where <i>size</i> is the record size parameter provided at the creation of <i>cgm_fd</i>. <i>write</i> returns the number of bytes successfully written. A negative return number implies an error occurred. The unix system call <i>write</i> is called by <code>CGM_write</code>. See <a href="/docs/linux/man/2-write/">write</a>(2).</p>
<dt>CGM_lseek</p>
<dd>Advance the file pointer of <i>cgm_fd</i> to <i>offset</i> bytes. Upon successful completion the current file pointer offset is returned. A negative return value is an error. The unix system call <i>lseek</i> is called by <code>CGM_lseek</code>. See <a href="/docs/linux/man/2-lseek/">lseek</a>(2).</p>
<dt>CGM_directory</p>
<dd>Create a table of contents for the metafile referenced by <i>cgm_fd</i>. Return a pointer to this table of type <i>Directory</i>. The contents of the directory include number of metafiles, number of frames, record offset for each frame, frame length in records, optional frame description and metafile status. These fields are meant to be read only and should only be referenced by the convenience macros provided in cgm_tools.h. A NULL pointer is returned on failure.</p>
<dt>CGM_freeDirectory</p>
<dd>Free memory allocated to a directory created by <code>CGM_directory</code> or <code>CGM_initMetaEdit</code>.</p>
<dt>CGM_printDirectory</p>
<dd>Print the contents of a directory pointed to by <i>dir</i> to the standard output.</p>
<dt>CGM_getInstr,</p>
<dd>Fetch the next instruction in file referenced by <i>cgm_edit</i> and convert it into a usable format pointed to by <i>instr</i>. <code>CGM_getInstr</code> provides an interface to the metafile for extracting CGM elements. The user need not be concerned with the binary format of the metafile. The fields of the <i>Instr</i> are as described in <i>cgm_tools.h</i>. The user should note that the maximum allowable data length returned in a single invocation is 32760 bytes. The CGM standard allows upto 32767 bytes to be stored in a single instruction. But 32767 is not a nice number to work with. Should the data length of a CGM instruction exceed 32760 bytes, indicated by the boolean <i>more</i> flag, the next invocation of <code>CGM_getInstr</code> will return the remaining data upto the same limit. And so on&#8230; <code>CGMgetInstrR requires a valid </code><i>Cgm_fd</i> open for reading. For a description on CGM see the ANSI standard.</p>
<dt>CGM_flushGetInstr</p>
<dd>Flush the input buffer used by <code>CGM_getInstr</code>. <code>CGM_getInstr</code> buffers the contents of the CGM and only performs actual reads as necessary. If the user desires other then sequential read access to a CGM it becomes necessary to flush the input buffer before reading from a new location.</p>
<dt>CGM_putInstr</p>
<dd>The analog to <code>CGM_getInstr</code>. This function buffers CGM instructions to be written to a CGM referenced by <i>cgm_fd</i>. Again the user need not be concerned with the binary format of the file. Writes are performed sequentially in record size <i>size</i> as specified during the creation of <i>cgm_fd</i>. The same data length constraints that are placed on <code>CGM_getInstr</code> hold for <code>CGM_putInstr</code>. If the user wants to output instructions with a data length greater than 32760 bytes then the data must be broken up into blocks no greater than this size. The user must also set the boolean <i>more</i> flag in the <i>Instr</i>. <i>cgm_fd</i> must be a valid file descriptor open for writing. For a description of the fields of the <i>Instr</i> see the file <i>cgm_tools.h</i>.</p>
<dt>CGM_flushOutputInstr</p>
<dd>Flush the output buffer used by <code>CGM_putInstr</code> for the file referenced by <i>cgm_fd</i>. It is necessary to explicitly flush the output buffer used by <code>CGM_putInstr</code> before the file is closed or any random access is performed. Otherwise not all CGM elements will actually get written.</p>
<dt>CGM_initMetaEdit</p>
<dd>Initialize a metafile for editing. This is the initialization routine for the higher level editing routines contained in this package: <code>CGM_copyFrames, CGM_deleteFrames</code>, <code>CGM_readFrames</code>, <code>CGM_moveFrames</code>, <code>CGM_writeFile</code>, <code>CGM_writeFrames</code>, and <code>CGM_mergeFrames</code>. These routines only work on one metafile at a time (the one named in <code>CGM_initMetaEdit</code>. Invoking this routine for a second time without explicitly saving any changes will have the effect of loading a new file and discarding all changes made in the previous file. <code>CGM_initMetaEdit</code> and all proceeding editing functions that <code>make</code> changes to the file return a pointer to a <i>Directory</i> as a convenience that allows the user to examine the state of the file. The contents of the directory are private and should NOT be changed by the user. A set of macros is provided in <i>cgm_tools.h</i> to be used for retrieving the directory&#8217;s contents. <code>Note</code>: no changes are actually made to the edit file unless it is explicitly overwritten with either <code>CGM_writeFile</code> or <code>CGM_writeFrames</code>.</p>
<dt>CGM_termMetaEdit</p>
<dd>Terminate the editing session started with <code>CGM_initMetaEdit</code>. This routine should be called after any editing changes have been saved, if desired to save them, and before exiting the editing session. <code>CGM_termMetaEdit</code> frees valuable resources.</p>
<dt>CGM_copyFrames</p>
<dd>Copy <i>num</i> frames beginning with <i>start</i> to the frame addressed by <i>target</i>. If <i>target</i> is already occupied then the source frames are inserted in its place while the target frame, and all proceeding frames, are advanced. <code>CGM_copy</code> operates on the file initialized by <code>CGM_initMetaEdit</code> (the edit file). On successful completion a pointer to the current directory is returned. On error a NULL pointer is returned.</p>
<dt>CGM_deleteFrames</p>
<dd>Delete <i>num</i> frames from the edit file starting with frame <i>start</i>. On successful completion a pointer to the current directory is returned. On error a NULL pointer is returned.</p>
<dt>CGM_mergeFrames</p>
<dd>Overwrite the contents of frame addressed <i>bottom</i> with the union of the frame at location <i>bottom</i> and the frame at location <i>top</i>. The effect of this command is equivalent to drawing the <i>top</i> frame on top of the <i>bottom</i> frame. It is not a union in the true sense of the word. On successful completion a pointer to the current directory is returned. On error a NULL pointer is returned.</p>
<dt>CGM_moveFrames</p>
<dd>Move a block of <i>num</i> frames from the edit file starting with with frame <i>start</i> to the position occupied by frame <i>target</i> On successful completion a pointer to the current directory is returned. On error a NULL pointer is returned.</p>
<dt>CGM_readFrames</p>
<dd>Read <i>num</i> frames from metafile <i>file</i> starting with frame <i>start</i>. Insert the frames at address <i>target</i> in the edit file. On successful completion a pointer to the current directory is returned. On error a NULL pointer is returned.</p>
<dt>CGM_validCGM</p>
<dd>Determine whether a file is a valid NCAR CGM or not. This function performs a few simple diagnostics in an effort to determine whether a given file is in the NCAR CGM format. The tests performed are not rigorous and it is conceivable that the information retrieved is incorrect. A return of 1 indicates a valid NCAR CGM. A return of 0 indicates the file is not a NCAR CGM. A return of -1 indicates an error occurred and the global variable `errno&#8217; is set accordingly.</p>
<dt>CGM_writeFile</p>
<dd>Write the entire contents of the current edit file to <i>file</i>. <code>CGM_writeFile</code> returns the integer one on success and a negative number on failure.</p>
<dt>CGM_writeFrames</p>
<dd>Write a block of <i>num</i> frames starting with frame <i>start</i> to <i>file</i>. The source frames come from the edit file. Note: CGM frames are contained in a wrapper made up of CGM <i>delimiter</i> elements. The file created by <code>CGM_writeFrames</code> will use the <i>wrapper</i> provided by the current edit file. Thus if a file <i>foo</i> contains <i>n</i> frames that are <i>read</i> into an editing session with a file <i>goo</i> and then these same frames are written out to a file <i>zoid</i>, <i>zoid</i> may or may not be the same as the original <i>foo</i>. <code>CGM_writeFrames</code> returns the integer one on success and a negative number on failure.</p>
<dt>CGM_appendFrames</p>
<dd>Append a block of <i>num</i> frames starting with frame <i>start</i> to <i>file</i>. <i>file</i> must already exist and be a valid NCAR CGM. <code>CGM_appendFrames</code> returns the integer one on success and a negative number on failure.</dl>
<h2>See Also</h2>
<p>ANSI X3.122 <i>Computer Graphics Metafile for the Storage and Transfer of Picture Description Information. </i></p>
<h2>Bugs</h2>
<p>CGMs with more the one metafile stored in the are not guaranteed to work. </p>
<p> Should not have to explicitly flush the output buffer for <code>CGM_getInstr</code>. This should be handled automatically when the file is closed.</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>
