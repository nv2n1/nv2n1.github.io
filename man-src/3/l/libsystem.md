---
title: "libsystem(3)"
name: "libsystem"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libsystem/"
description: "pm_system – run a Netpbm program with program input and output"
---

<h2>Name</h2>
<p> pm_system &#8211; run a Netpbm program with program input and output </p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;netpbm/pm_system.h&gt;
pm_system(void stdinFeeder(int, void *),
          void *const feederParm,
          void stdoutAccepter(int, void *),
          void *const accepterParm,
          const char *const shellCommand);
pm_system_lp(const char *const progName,
             void stdinFeeder(int, void *),
             void *const feederParm,
             void stdoutAccepter(int, void *),
             void *const accepterParm,
             ...);
pm_system_vp(const char *const progName,
             const char **const argArray,
             void stdinFeeder(int, void *),
             void *const feederParm,
             void stdoutAccepter(int, void *),
             void *const accepterParm);
</code></pre>
<h2>Example</h2>
<p> This simple example converts a PNM image on Standard Input to a JFIF (JPEG) image on Standard Output. In this case, <code>pm_system()</code> is doing no more than <code>system()</code> would do. </p>
<p>pm_system(NULL, NULL, NULL, NULL, &#8220;pnmtojpeg&#8221;);</p>
<p> This example does the same thing, but moves the data through memory buffers to illustrate use with memory buffers, and we throw in a stage to shrink the image too:<br />
#include &lt;netpbm/pm_system.h&gt;<br />
char pnmData[100 * 1024]; /* Input file better be &lt; 100K */<br />
char jfifData[100 * 1024];<br />
struct bufferDesc pnmBuffer;<br />
struct bufferDesc jfifBuffer;<br />
unsigned int jfifSize;<br />
pnmBuffer.size = fread(pnmData, 1, sizeof(pnmData), stdin);<br />
pnmBuffer.buffer = pnmData;<br />
pnmBuffer.bytesTransferredP = NULL;<br />
jfifBuffer.size = sizeof(jfifData);<br />
jfifBuffer.buffer = jfifData;<br />
jfifBuffer.bytesTransferredP = &amp;jfifSize;<br />
pm_system(&amp;pm_feed_from_memory, &amp;pnmBuffer,<br />
          &amp;pm_accept_to_memory, &amp;jfifBuffer,<br />
          &#8220;pamscale .5 | pnmtojpeg&#8221;);<br />
fwrite(jfifData, 1, jfifSize, stdout);</p>
<p> This example reads an image into libnetpbm PAM structures, then brightens it, then writes it out, to illustrate use of <code>pm_system</code> with PAM structures.<br />
#include &lt;netpbm/pam.h&gt;<br />
#include &lt;netpbm/pm_system.h&gt;<br />
struct pam inpam;<br />
struct pam outpam;<br />
tuple **inTuples;<br />
tuple **outTuples;<br />
struct pamtuples inPamtuples;<br />
struct pamtuples outPamtuples;<br />
inTuples = pnm_readpam(stdin, &amp;inpam, sizeof(inpam));<br />
outpam = inpam;<br />
inPamtuples.pamP = &amp;inpam;<br />
inPamtuples.tuplesP = &amp;inTuples;<br />
outPamtuples.pamP = &amp;outpam;<br />
outPamtuples.tuplesP = &amp;outTuples;<br />
pm_system(&amp;pm_feed_from_pamtuples, &amp;inPamtuples,<br />
          &amp;pm_accept_to_pamtuples, &amp;outPamtuples,<br />
          &#8220;ppmbrighten -v 100&#8221;);<br />
outpam.file = stdout;<br />
pnm_writepam(&amp;outpam, outTuples);</p>
<h2>DESCRIPTION</h2>
<p> These library functions are part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pm_system()</code> is a lot like the standard C library <code>system()</code> subroutine. It runs a shell and has that shell execute a shell command that you specify. But <code>pm_system()</code> gives you more control over the Standard Input and Standard Output of that shell command than <code>system()</code>. <code>system()</code> passes to the shell command as Standard Input and Output whatever is the Standard Input and Output of the process that calls <code>system()</code>. But with <code>pm_system()</code>, you specify as arguments subroutines to execute to generate the shell command&#8217;s Standard Input stream and to process the shell command&#8217;s Standard Output stream. </p>
<p> Your Standard Input feeder subroutine can generate the stream in limitless ways. <code>pm_system()</code> gives it a file descriptor of a pipe to which to write the stream it generates. <code>pm_system()</code> hooks up the other end of that pipe to the shell command&#8217;s Standard Input. </p>
<p> Likewise, your Standard Output accepter subroutine can do anything it wants with the stream it gets. <code>pm_system()</code> gives it a file descriptor of a pipe from which to read the stream. <code>pm_system()</code> hooks up the other end of that pipe to the shell command&#8217;s Standard Output. </p>
<p> The argument <i>stdinFeeder</i> is a function pointer that identifies your Standard Input feeder subroutine. <code>pm_system()</code> runs it in a child process and waits for that process to terminate (and accepts its completion status) before returning. <i>feederParm</i> is the argument that <code>pm_system()</code> passes to the subroutine; it is opaque to <code>pm_system()</code>. </p>
<p> If you pass <i>stdinFeeder</i> = NULL, <code>pm_system()</code> simply passes your current Standard Input stream to the shell command (as <code>system()</code> would do), and does not create a child process. </p>
<p> The argument <i>stdoutAccepter</i> is a function pointer that identifies your Standard Output accepter subroutine. <code>pm_system()</code> calls it in the current process. <i>accepterParm</i> is an argument analogous to <i>feederParm</i>. </p>
<p> If you pass <i>stdoutAccepter</i> = NULL, <code>pm_system()</code> simply passes your current Standard Output stream to the shell command (as <code>system()</code> would do. </p>
<p> The argument <i>shellCommand</i> is a null-terminated string containing the shell command that the shell is to execute. It can be any command that means something to the shell and can take a pipe for Standard Input and Output. Example: </p>
<pre>
<tt>
    ppmbrighten -v 100 | pamdepth 255 | pamscale .5
</tt>
</pre>
<p> <code>pm_system()</code> creates a child process to run the shell and waits for that process to terminate (and accepts its completion status) before returning. </p>
<h3>pm_system_lp()</h3>
<p> <code>pm_system_lp()</code> is like <code>pm_system()</code> except that instead of running a shell, which in turn typically runs another program, you run a program of your choice directly. </p>
<p> Argument <i>progName</i> identifies the program to run, the same way as with <code>execlp()</code> or a shell command: if it contains a slash (/), it is the full name of the file that contains the program. If not, it is a name to be looked up in the system&#8217;s program search path (determined by the PATH environment variable). </p>
<p> You identify the arguments to the program the same way as for <code>execlp()</code>: with the variable arguments at the end of the <code>pm_system_lp()</code> argument list. Each is a NUL-terminated string. The last argument <i>must</i> be NULL to tell <code>pm_system_lp()</code> where the arguments end. </p>
<p> Note that the first argument (&#8216;arg0&#8217;) to a program is conventionally the first word of the command used to run the program, as if it were being run due to a shell command. In other words, typically the name of the program. </p>
<p> Example: </p>
<p>pm_system_lp(&#8216;pnmtojpeg&#8217;, NULL, NULL, NULL, NULL,<br />
             &#8216;pnmtojpeg&#8217;, &#8216;mypicture.jpg&#8217;, &#8216;-quality=50&#8217;, NULL);</p>
<p> <code>pm_system_lp()</code> is much safer than <code>pm_system()</code> when your program computes the arguments or gets them from a user. If you build a shell command using such arguments, unless you&#8217;re really careful, you may end up building a shell command that does something very different from what you intended, because the argument could contain characters that mean something to the shell such as &#8216;|&#8217;. </p>
<p> <code>pm_system_lp()</code> can also be considerably faster that <code>pm_system()</code>, since it skips the whole running of the shell. </p>
<h3>pm_system_vp()</h3>
<p> <code>pm_system_vp()</code> is like <code>pm_system_lp()</code> except that instead of supplying the program arguments as variable arguments, you supply them as an array, as with <code>execvp()</code>. A NULL element in the array identifies the end of the arguments. </p>
<p> Example: </p>
<p>const char *argArray[3];<br />
argArray[0] = &#8216;pnmtojpeg&#8217;;<br />
argArray[1] = &#8216;-quality=50&#8217;;<br />
argArray[2] = NULL;<br />
pm_system_vp(&#8216;pnmtojpeg&#8217;, argArray, NULL, NULL, NULL, NULL);</p>
<h2>Applications</h2>
<p> The point of <code>pm_system()</code> and friends is to allow you to write a C program that uses other programs internally, as a shell script would. This is particularly desirable with Netpbm, because Netpbm consists of a lot of programs that perform basic graphic manipulations and you&#8217;d like to be able to build a program that does a more sophisticated graphic manipulation by calling the more basic Netpbm programs. These building block programs typically take input from Standard Input and write output to Standard Output. </p>
<p> The obvious alternative is to use a higher level language &#8212; Bourne Shell or Perl, for example. But often you want your program to do manipulations of your graphical data that are easier and more efficient in C. Or you want to use the Netpbm subroutine library in your program. The Netpbm subroutine library is a C-linkage library; the subroutines in it are not usable from a Bourne Shell or Perl program. </p>
<p> A typical use of <code>pm_system()</code> is to place the contents of some graphical image file in memory, run a Netpbm program against it, and have what would ordinarily go into an output file in memory too, for further processing. To do that, you can use the memory buffer Standard Input feeder and Standard Output accepter described below. </p>
<p> If your program uses the Netpbm subroutine library to read, write, and manipulate images, you may have an image in an array of PAM tuples. If you want to manipulate that image with a Netpbm program (perhaps remap the colors using <code>pnmremap</code>), you can use the pamtuple Standard Input feeder and Standard Output acceptor described below. </p>
<h2>Broken Pipe Behavior</h2>
<p> When you set up a shell command to take input from a pipe, as you do with <code>pm_system()</code>, you need to understand how pipes work with respect to the programs at either end of the pipe agreeing to how much data is to be transferred. Here are some notes on that. </p>
<p> It is normal to read a pipe before the process on the other end has written the data you hope to read, and it is normal to write to a pipe before the process on the other end has tried to read your data. Writes to a pipe can be buffered until the reading end requests the data. A process reading or writing a pipe can block until the other end is ready. Or a read or write can complete with an indication that the other end is not ready at the moment and therefore no data, or less data than was requested, was transferred. </p>
<p> The pipe is normally controlled by the writing end. When you read from a pipe, you keep reading until the program on the other end of the pipe closes it, and then you get an end-of-file indication. You then normally close the reading end of the pipe, since it is no longer useful. </p>
<p> When you close the reading end of a pipe before getting the end-of-file indication and the writer subsequently tries to write to the pipe, that is an error condition for the writer. In a typical default Unix environment, that error causes the writer to receive a SIGPIPE signal and that signal causes the writer process to terminate abnormally. But if, alternatively, the writer has ordered that SIGPIPE be blocked, ignored, or handled, the signal does not cause the death of the writer. Instead, the write operation simply completes with an error indication. </p>
<h2>Standard Feeders And Acceptors</h2>
<p> You can supply anything you like as a Standard Input feeder or Standard Output acceptor, but the Netpbm subroutine library comes with a few that perform commonly needed functions. </p>
<h3>Memory Buffer</h3>
<p> These routines are for when you just want to treat an area of memory as a file. If the shell command would ordinarily read a 513 byte regular file from its Standard Input, you want it to take 513 bytes from a certain address in your process&#8217; memory. Whatever bytes the shell command wants to write to its output file you want it to store at another address in your process&#8217; memory. </p>
<p> The Standard Input feeder for this is called <code>pm_feed_from_memory</code>. The Standard Output accepter is <code>pm_accept_to_memory</code>. </p>
<p> For both of these, the argument is the address of a <code>struct bufferDesc</code>, which is defined as follows: </p>
<p>struct bufferDesc {<br />
    unsigned int size;<br />
    unsigned char *buffer;<br />
    unsigned int *bytesTransferredP;<br />
};</p>
<p> <i>size</i> is the size of the memory buffer and <i>buffer</i> is its location in memory (address). The Standard Input feeder will attempt to feed the entire buffer to the shell command&#8217;s Standard Input; the Standard Output accepter will not accept any more data from the shell command&#8217;s Standard Output than will fit in the buffer. Both return the actual amount of data read or written, in bytes, at the location identified by <i>bytesTransferredP</i>. Unless <code>bytesTransferredP</code> is NULL. </p>
<p> Because a process typically terminates abnormally when it is not able to write everything to a pipe that it wanted to, <i>bytesTransferredP</i> is not usually useful in the Standard Input feeder case. </p>
<h3>Pamtuple</h3>
<p> These routines are for when you have images in memory in the data structures used by the PAM family of subroutines in the Netpbm library &#8212; i.e. struct PAM and an array of struct tuple. With these routines, you can run a Netpbm program against such an image just as you would against the same image in a regular file. </p>
<p> The Standard Input feeder for this is called <code>pm_feed_from_pamtuples</code>. The Standard Output accepter is <code>pm_accept_to_pamtuples</code>. </p>
<p> For both of these, the argument is the address of a <code>struct pamtuples</code>, which is defined as follows: </p>
<pre><code>
struct pamtuples {
    struct pam *pamP;
    tuple ***tuplesP;
};
</code></pre>
<p> For the Standard Input feeder, you supply a struct pam, valid up through the <i>tuple_type</i> member (except it doesn&#8217;t matter what the <i>file</i> member is) and array of tuples. </p>
<p> For the Standard Output Accepter, you supply only space in memory for the struct pam and the address of the tuple array. The routine fills in the struct pam up through the <i>tuple_type</i> member (except leaves the <i>file</i> member undefined) and allocates space for the tuple array with malloc(). You are responsible for freeing that memory. </p>
<h2>HISTORY</h2>
<p> <code>pm_system()</code> was introduced in Netpbm 10.13 (January 2003). </p>
<h2>Index</h2>
