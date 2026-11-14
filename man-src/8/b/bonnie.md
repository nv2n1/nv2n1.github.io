---
title: "bonnie(8)"
name: "bonnie"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bonnie/"
description: "bonnie++ – program to test hard drive performance."
---

<p>bonnie++ &#8211; program to test hard drive performance. </p>
<h2>Synopsis</h2>
<p><code>bonnie++</code> <i>[-d dir] [-c concurrency] [-s size(MiB)[:chunk-size(b)]]</i> <i>[-n number-to-stat(*1024)[:max-size[:min-size][:num-directories[:chunk-size]]]]</i> <i>[-m machine-name] [-r ram-size-in-MiB] [-x number-of-tests]</i> <i>[-u uid-to-use:gid-to-use] [-g gid-to-use]</i> <i>[-q] [-f size-for-char-io] [-b] [-D] [-p processes | -y p|s ]</i> <i>[-z seed-num|-Z random-file]</i> </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bonnie++</code>, program. Bonnie++ is a program to test hard drives and file systems for performance or the lack therof. There are a many different types of file system operations which different applications use to different degrees. Bonnie++ tests some of them and for each test gives a result of the amount of work done per second and the percentage of CPU time this took. For performance results higher numbers are better, for CPU usage and latency lower are better (NB a configuration scoring a performance result of 2000 and a CPU result of 90% is better in terms of CPU use than a configuration delivering performance of 1000 and CPU usage of 60%). There are two sections to the program&#8217;s operations. The first is to test the IO throughput in a fashion that is designed to simulate some types of database applications. The second is to test creation, reading, and deleting many small files in a fashion similar to the usage patterns of programs such as Squid or INN. All the details of the tests performed by Bonnie++ are contained in the file <code>/usr/share/doc/bonnie++/readme.html</code> </p>
<h2>Options</h2>
<p>For Bonnie++ every option is of the form of a hyphen followed by a letter and then the next parameter contains the value.</p>
<dl>
<dt><code>-d</code></p>
<dd>the directory to use for the tests.</p>
<dt><code>-c</code></p>
<dd>the level of concurrency (default 1). The number of copies of the test to be performed at the same time.</p>
<dt><code>-s</code></p>
<dd>the size of the file(s) for IO performance measures in megabytes. If the size is greater than 1G then multiple files will be used to store the data, and each file will be up to 1G in size. This parameter may include the chunk size seperated from the size by a colon. The chunk-size is measured in bytes and must be a power of two from 256 to 1048576, the default is 8192. NB You can specify the size in giga-bytes or the chunk-size in kilo-bytes if you add <code>g</code> or <code>k</code> to the end of the number respectively. </p>
<p> If the specified size is 0 then this test will be skipped.</p>
<dt><code>-n</code></p>
<dd>the number of files for the file creation test. This is measured in multiples of 1024 files. This is because no-one will want to test less than 1024 files, and we need the extra space on braille displays. </p>
<p> If the specified number is 0 then this test will be skipped. </p>
<p> The default for this test is to test with 0 byte files. To use files of other sizes you can specify <code>number:max:min:num-directories:chunk-size</code> where <code>max</code> is the maximum size and <code>min</code> is the minimum size (both default to 0 if not specified). If minimum and maximum sizes are specified then every file will have a random size from the range <code>min..max</code> inclusive. If you specify a number of directories then the files will be evenly distributed amoung that many sub-directories. </p>
<p> If <code>max</code> is <code>-1</code> then hard links will be created instead of files. If <code>max</code> is <code>-2</code> then soft links will be created instead of files. </p>
<dt><code>-m</code></p>
<dd>name of the machine &#8211; for display purposes only. </p>
<dt><code>-r</code></p>
<dd>RAM size in megabytes. If you specify this the other parameters will be checked to ensure they make sense for a machine of that much RAM. You should not need to do this in general use as it should be able to discover the RAM size. NB If you specify a size of 0 then all checks will be disabled&#8230; </p>
<dt><code>-x</code></p>
<dd>number of test runs. This is useful if you want to perform more than one test. It will dump output continuously in CSV format until either the number of tests have been completed, or it is killed. </p>
<dt><code>-u</code></p>
<dd>user-id to use. When running as root specify the UID to use for the tests. It is not recommended to use root (since the occasion when a Bonnie++ bug wiped out someone&#8217;s system), so if you really want to run as root then use <code>-u root.</code> Also if you want to specify the group to run as then use the <code>user:group</code> format. If you specify a user by name but no group then the primary group of that user will be chosen. If you specify a user by number and no group then the group will be <code>nogroup.</code> </p>
<dt><code>-g</code></p>
<dd>group-id to use. Same as using <code>:group</code> for the <code>-u</code> parameter, just a different way to specify it for compatibility with other programs. </p>
<dt><code>-q</code></p>
<dd>quiet mode. If specified then some of the extra informational messages will be suppressed. Also the csv data will be the only output on standard out and the plain text data will be on standard error. This means you can run <code>bonnie++ -q &gt;&gt; file.csv</code> to record your csv data. </p>
<dt><code>-f size-for-char-io</code></p>
<dd>fast mode control, skips per-char IO tests if no parameter, otherwise specifies the size of the tests for per-char IO tests (default 20M). </p>
<dt><code>-b</code></p>
<dd>no write buffering. fsync() after every write. </p>
<dt><code>-p</code></p>
<dd>number of processes to serve semaphores for. This is used to create the semaphores for synchronising multiple Bonnie++ processes. All the processes which are told to use the semaphore with <code>-ys</code> will start each test with synchronization. Use &quot;-p -1&quot; to delete the semaphore. </p>
<dt><code>-y s|p</code></p>
<dd>perform synchronization before each test. Option <code>s</code> for semaphores and option <code>p</code> for prompting. </p>
<dt><code>-D</code></p>
<dd>use direct IO (O_DIRECT) for the bulk IO tests </p>
<dt><code>-z seed</code></p>
<dd>random number seed to repeat the same test. </p>
<dt><code>-Z random-file</code></p>
<dd>file containing random data in network byte order.</dl>
<h2>Multiple Processes</h2>
<p>Run the following commands to run three copies of Bonnie++ simultaneously: </p>
<p> bonnie++ -p3 </p>
<p> bonnie++ -y &gt; out1 &amp; </p>
<p> bonnie++ -y &gt; out2 &amp; </p>
<p> bonnie++ -y &gt; out3 &amp;</p>
<h2>Output</h2>
<p>The primary output is plain-text in 80 columns which is designed to fit well when pasted into email and which will work well with Braille displays. </p>
<p> The second type of output is CSV (Comma Seperated Values). This can easily be imported into any spread-sheet or database program. Also I have included the programs <code>bon_csv2html</code> and <code>bon_csv2txt</code> to convert CSV data to HTML and plain-ascii respectively. </p>
<p> For every test two numbers are reported, the amount of work done (higher numbers are better) and the percentage of CPU time taken to perform the work (lower numbers are better). If a test completes in less than 500ms then the output will be displayed as &quot;++++&quot;. This is because such a test result can&#8217;t be calculated accurately due to rounding errors and I would rather display no result than a wrong result. </p>
<p> Data volumes for the 80 column text display use &quot;K&quot; for KiB (1024 bytes), &quot;M&quot; for MiB (1048576 bytes), and &quot;G&quot; for GiB (1073741824 bytes). So K/sec means a multiple of 1024 bytes per second.</p>
<h2>Author</h2>
<p>This program, its manual page, and the Debian package were written by Russell Coker &lt;russell [at] coker.com.au&gt;, parts of the program are based on the work of Tim Bray &lt;tbray [at] textuality.com&gt;. </p>
<p> The documentation, the Perl scripts, and all the code for testing the creation of thousands of files was written by Russell Coker, but the entire package is under joint copyright with Tim Bray.</p>
<h2>Signals</h2>
<p>Handles SIGINT and does a cleanup (which may take some time), a second SIGINT or a SIGQUIT will cause it to immediately die. </p>
<p> SIGXCPU and SIGXFSZ act like SIGINT. </p>
<p> Ignores SIGHUP.</p>
<h2>Bugs</h2>
<p>The random file sizes will add up to different values for different test runs. I plan to add some code that checks the sum and ensures that the sum of the values will be the same on seperate runs. </p>
<h2>Availability</h2>
<p>The source is available from <a rel="nofollow" href="http://www.coker.com.au/bonnie++">http://www.coker.com.au/bonnie++</a> . </p>
<p> See <a rel="nofollow" href="http://etbe.coker.com.au/category/benchmark">http://etbe.coker.com.au/category/benchmark</a> for further information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-zcav/">zcav</a></code>(8), <code><a href="/docs/linux/man/8-getc_putc/">getc_putc</a></code>(8), <code><a href="/docs/linux/man/1-bon_csv2html/">bon_csv2html</a></code>(1), <code><a href="/docs/linux/man/1-bon_csv2txt/">bon_csv2txt</a></code>(1) </p>
