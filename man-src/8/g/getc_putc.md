---
title: "getc_putc(8)"
name: "getc_putc"
section: "8"
letter: "g"
url: "/docs/linux/man/8-getc_putc/"
description: "getc_putc – program to test hard drive performance."
---

<p>getc_putc &#8211; program to test hard drive performance. </p>
<h2>Synopsis</h2>
<p><code>getc_putc</code> <i>[-d dir] [-s size(KiB)] [-m machine-name]</i> <i>[-u uid-to-use:gid-to-use] [-g gid-to-use]</i> </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>getc_putc</code>, program. This is a simple adjunct to the <code>bonnie++</code> benchmark. It is used to test various ways of doing IO one byte at a time, usually you don&#8217;t need to do enough of this for it to be a performance issue for it to matter much which way you do it. But sometimes it&#8217;s necessary (for example whan parsing IO from a terminal and then launching another process which will take over all IO, such as a simple shell). The real benefits of this are to help settle some arguements about the performance of such things, and to educate novices about how bad per-byte IO really is. </p>
<h2>Options</h2>
<p>For getc_putc every option is of the form of a hyphen followed by a letter and then the next parameter contains the value.</p>
<dl>
<dt><code>-d</code></p>
<dd>the directory to use for the tests.</p>
<dt><code>-s</code></p>
<dd>the size of the file for byte IO performance measured in kilobytes. NB You can specify the size in mega-bytes if you add &#8216;m&#8217; to the end of the number. </p>
<p> The default for this test is to test with a 40MiB file. Of the file only 1/32 of it will be used for write() and read() system calls (anything else takes too long), and only 1/4 of it will be used for locked getc() and putc(). </p>
<dt><code>-m</code></p>
<dd>name of the machine &#8211; for display purposes only. </p>
<dt><code>-u</code></p>
<dd>user-id to use. When running as root specify the UID to use for the tests. It is not recommended to use root, so if you really want to run as root then use <code>-u root.</code> Also if you want to specify the group to run as then use the <code>user:group</code> format. If you specify a user by name but no group then the primary group of that user will be chosen. If you specify a user by number and no group then the group will be <code>nogroup.</code> </p>
<dt><code>-g</code></p>
<dd>group-id to use. Same as using <code>:group</code> for the <code>-u</code> parameter, just a different way to specify it for compatibility with other programs. </p>
<dt><code>-q</code></p>
<dd>quiet mode. If specified then some of the extra informational messages will be suppressed. Also the csv data will be the only output on standard out and the plain text data will be on standard error. This means you can run <code>getc_putc -q &gt;&gt; file.csv</code> to record your csv data. </p>
</dl>
<h2>Output</h2>
<p>The primary output is plain-text in 80 columns which is designed to fit well when pasted into email and which will work well with Braille displays. </p>
<p> The second type of output is CSV (Comma Seperated Values). This can easily be imported into any spread-sheet or database program. </p>
<p> For every test the result is a speed in KiB/s. I do not display the CPU time because it presumably is 99% of the power of a single CPU (or something very close to that).</p>
<h2>Author</h2>
<p>This program, it&#8217;s manual page, and the Debian package were written by Russell Coker &lt;russell [at] coker.com.au&gt;. </p>
<p> The documentation, the Perl scripts, and all the code for testing the creation of thousands of files was written by Russell Coker, but the entire package is under joint copyright with Tim Bray.</p>
<h2>Signals</h2>
<p>Handles SIGINT and does a cleanup (which may take some time), a second SIGINT or a SIGQUIT will cause it to immidiately die. </p>
<p> SIGXCPU and SIGXFSZ act like SIGINT. </p>
<p> Ignores SIGHUP.</p>
<h2>Availability</h2>
<p>The source is available from <a rel="nofollow" href="http://www.coker.com.au/bonnie++">http://www.coker.com.au/bonnie++</a> . </p>
<p> See <a rel="nofollow" href="http://etbe.coker.com.au/category/benchmark">http://etbe.coker.com.au/category/benchmark</a> for further information.</p>
<h2>See Also</h2>
<p><code>bonnie++</code>(8), <code><a href="/docs/linux/man/8-zcav/">zcav</a></code>(8) </p>
