---
title: "qio(3)"
name: "qio"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qio/"
description: "qio – Quick I/O routines for reading files"
---

<p>qio &#8211; Quick I/O routines for reading files </p>
<h2>Synopsis</h2>
<pre>
    #include &lt;inn/qio.h&gt;
    QIOSTATE *QIOopen(const char *name);
    QIOSTATE *QIOfdopen(int&gt; I&lt;fd);
    void QIOclose(QIOSTATE *qp);
    char *QIOread(QIOSTATE *qp);
    int QIOfileno(QIOSTATE *qp);
    size_t QIOlength(QIOSTATE *qp);
    int QIOrewind(QIOSTATE *qp);
    off_t QIOtell(QIOSTATE *qp);
    bool QIOerror(QIOSTATE *qp);
    bool QIOtoolong(QIOSTATE *qp);
</pre>
<h2>Description</h2>
<p> The routines described in this manual page are part of <i><a href="/docs/linux/man/3-libinn/">libinn</a></i>(3). They are used to provide quick read access to files; the <font SIZE="-1">QIO</font> routines use buffering adapted to the block size of the device, similar to stdio, but with a more convenient syntax for reading newline-terminated lines. <font SIZE="-1">QIO</font> is short for &#8220;Quick I/O&#8221; (a bit of a misnomer, as <font SIZE="-1">QIO</font> provides read-only access to files only). </p>
<p> The <font SIZE="-1">QIOSTATE</font> structure returned by <code>QIOopen</code> and <code>QIOfdopen</code> is the analog to stdio&#8217;s <font SIZE="-1">FILE</font> structure and should be treated as a black box by all users of these routines. Only the above <font SIZE="-1">API</font> should be used. </p>
<p> <code>QIOopen</code> opens the given file for reading. For regular files, if your system provides that information and the size is reasonable, <font SIZE="-1">QIO</font> will use the block size of the underlying file system as its buffer size; otherwise, it will default to a buffer of 8&nbsp;<wbr><font SIZE="-1">KB</font>. Returns a pointer to use for subsequent calls, or <font SIZE="-1">NULL</font> on error. <code>QIOfdopen</code> performs the same operation except on an already-open file descriptor (<i>fd</i> must designate a file open for reading). </p>
<p> <code>QIOclose</code> closes the open file and releases any resources used by the <font SIZE="-1">QIOSTATE</font> structure. The <font SIZE="-1">QIOSTATE</font> pointer should not be used again after it has been passed to this function. </p>
<p> <code>QIOread</code> reads the next newline-terminated line in the file and returns a pointer to it, with the trailing newline replaced by nul. The returned pointer is a pointer into a buffer in the <font SIZE="-1">QIOSTATE</font> object and therefore will remain valid until <code>QIOclose</code> is called on that object. If <font SIZE="-1">EOF</font> is reached, an error occurs, or if the line is longer than the buffer size, <font SIZE="-1">NULL</font> is returned instead. To distinguish between the error cases, use <code>QIOerror</code> and <code>QIOtoolong</code>. </p>
<p> <code>QIOfileno</code> returns the descriptor of the open file. </p>
<p> <code>QIOlength</code> returns the length in bytes of the last line returned by <code>QIOread</code>. Its return value is only defined after a successful call to <code>QIOread</code>. </p>
<p> <code>QIOrewind</code> sets the read pointer back to the beginning of the file and reads the first block of the file in anticipation of future reads. It returns 0 if successful and -1 on error. </p>
<p> <code>QIOtell</code> returns the current value of the read pointer (the <i><a href="/docs/linux/man/2-lseek/">lseek</a></i>(2) offset at which the next line will start). </p>
<p> <code>QIOerror</code> returns true if there was an error in the last call to <code>QIOread</code>, false otherwise. <code>QIOtoolong</code> returns true if there was an error and the error was that the line was too long. If <code>QIOread</code> returns <font SIZE="-1">NULL</font>, these functions should be called to determine what happened. If <code>QIOread</code> returned <font SIZE="-1">NULL</font> and <code>QIOerror</code> is false, <font SIZE="-1">EOF</font> was reached. Note that if <code>QIOtoolong</code> returns true, the next call to <code>QIOread</code> will try to read the remainder of the line and will likely return a partial line; users of this library should in general treat long lines as fatal errors.</p>
<h2>Examples</h2>
<p> This block of code opens <i>/etc/motd</i> and reads it a line at a time, printing out each line preceded by its offset in the file. </p>
<pre>
    QIOSTATE *qp;
    off_t offset;
    char *p;
    qp = QIOopen(&quot;/etc/motd&quot;);
    if (qp == NULL) {
        perror(&quot;Open error&quot;);
        <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
    }
    for (p = QIOread(qp); p != NULL; p = QIOread(qp))
        printf(&quot;%ld: %s
&quot;, (unsigned long) QIOtell(qp), p);
    if (QIOerror(qp)) {
        perror(&quot;Read error&quot;);
        <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
    }
    QIOclose(qp);
</pre>
<h2>History</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Updated by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> qio.pod 9768 2014-12-07 21:22:57Z iulius $</p>
