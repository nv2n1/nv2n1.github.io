---
title: "stderr(3)"
name: "stderr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderr/"
description: "stdin, stdout, stderr – standard I/O streams"
---

<p>stdin, stdout, stderr &#8211; standard I/O streams</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

extern FILE *stdin;
extern FILE *stdout;
extern FILE *stderr;</code></pre>
<h2>Description</h2>
<p>Under normal circumstances every UNIX program has three streams opened for it when it starts up, one for input, one for output, and one for printing diagnostic or error messages. These are typically attached to the user&#8217;s terminal (see <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)) but might instead refer to files or other devices, depending on what the parent process chose to set up. (See also the &quot;Redirection&quot; section of <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1).) </p>
<p> The input stream is referred to as &quot;standard input&quot;; the output stream is referred to as &quot;standard output&quot;; and the error stream is referred to as &quot;standard error&quot;. These terms are abbreviated to form the symbols used to refer to these files, namely <i>stdin</i>, <i>stdout</i>, and <i>stderr</i>. </p>
<p> Each of these symbols is a <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) macro of type pointer to <i>FILE</i>, and can be used with functions like <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3) or <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3). </p>
<p> Since <i>FILE</i>s are a buffering wrapper around UNIX file descriptors, the same underlying files may also be accessed using the raw UNIX file interface, that is, the functions like <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). </p>
<p> On program startup, the integer file descriptors associated with the streams <i>stdin</i>, <i>stdout</i>, and <i>stderr</i> are 0, 1, and 2, respectively. The preprocessor symbols <code>STDIN_FILENO</code>, <code>STDOUT_FILENO</code>, and <code>STDERR_FILENO</code> are defined with these values in <i>&lt;unistd.h&gt;</i>. (Applying <code><a href="/docs/linux/man/3-freopen/">freopen</a></code>(3) to one of these streams can change the file descriptor number associated with the stream.) </p>
<p> Note that mixing use of <i>FILE</i>s and raw file descriptors can produce unexpected results and should generally be avoided. (For the mas****stic among you: POSIX.1, section 8.2.3, describes in detail how this interaction is supposed to work.) A general rule is that file descriptors are handled in the kernel, while stdio is just a library. This means for example, that after an <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), the child inherits all open file descriptors, but all old streams have become inaccessible. </p>
<p> Since the symbols <i>stdin</i>, <i>stdout</i>, and <i>stderr</i> are specified to be macros, assigning to them is nonportable. The standard streams can be made to refer to different files with help of the library function <code><a href="/docs/linux/man/3-freopen/">freopen</a></code>(3), specially introduced to make it possible to reassign <i>stdin</i>, <i>stdout</i>, and <i>stderr</i>. The standard streams are closed by a call to <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) and by normal program termination.</p>
<h2>Conforming To</h2>
<p>The <i>stdin</i>, <i>stdout</i>, and <i>stderr</i> macros conform to C89 and this standard also stipulates that these three streams shall be open at program startup.</p>
<h2>Notes</h2>
<p>The stream <i>stderr</i> is unbuffered. The stream <i>stdout</i> is line-buffered when it points to a terminal. Partial lines will not appear until <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3) or <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) is called, or a newline is printed. This can produce unexpected results, especially with debugging output. The buffering mode of the standard streams (or any other stream) can be changed using the <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3) or <code><a href="/docs/linux/man/3-setvbuf/">setvbuf</a></code>(3) call. Note that in case <i>stdin</i> is associated with a terminal, there may also be input buffering in the terminal driver, entirely unrelated to stdio buffering. (Indeed, normally terminal input is line buffered in the kernel.) This kernel input handling can be modified using calls like <code><a href="/docs/linux/man/3-tcsetattr/">tcsetattr</a></code>(3); see also <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), and <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
