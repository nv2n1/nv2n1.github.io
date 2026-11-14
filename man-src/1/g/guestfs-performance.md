---
title: "guestfs-performance(1)"
name: "guestfs-performance"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guestfs-performance/"
description: "guestfs-performance – engineering libguestfs for greatest performance"
---

<h2 class="name">NAME</h2>
<p> guestfs-performance &#8211; engineering libguestfs for greatest performance </p>
<h2>DESCRIPTION</h2>
<p> This page documents how to get the greatest performance out of libguestfs, especially when you expect to use libguestfs to manipulate thousands of virtual machines or disk images. </p>
<p> Three main areas are covered. Libguestfs runs an appliance (a small Linux distribution) inside qemu/KVM. The first two areas are: minimizing the time taken to start this appliance, and the number of times the appliance has to be started. The third area is shortening the time taken for inspection of VMs.</p>
<h2>BASELINE MEASUREMENTS</h2>
<p> Before making changes to how you use libguestfs, take baseline measurements.</p>
<h3>Baseline: Starting the appliance</h3>
<p> On an unloaded machine, time how long it takes to start up the appliance: </p>
<pre>
 time guestfish -a /dev/null run
</pre>
<p> Run this command several times in a row and discard the first few runs, so that you are measuring a typical &#8220;hot cache&#8221; case. </p>
<p> <i>Side note for developers:</i> If you are compiling libguestfs from source, there is a program called <i>utils/boot-benchmark/boot-benchmark</i> which does the same thing, but performs multiple runs and prints the mean and standard deviation. To run it, do: </p>
<pre>
 make
 ./run utils/boot-benchmark/boot-benchmark
</pre>
<p> There is a manual page <i>utils/boot-benchmark/boot-benchmark.1</i> </p>
<p> <i>Explanation</i> </p>
<p> The guestfish command above starts up the libguestfs appliance on a null disk, and then immediately shuts it down. The first time you run the command, it will create an appliance and cache it (usually under <i>/var/tmp/.guestfs-*</i>). Subsequent runs should reuse the cached appliance. </p>
<p> <i>Expected results</i> </p>
<p> You should expect to be getting times under 6 seconds. If the times you see on an unloaded machine are above this, then see the section &#8220;<font SIZE="-1">TROUBLESHOOTING POOR PERFORMANCE&#8221;</font> below.</p>
<h3>Baseline: Performing inspection of a guest</h3>
<p> For this test you will need an unloaded machine and at least one real guest or disk image. If you are planning to use libguestfs against only X guests (eg. X = Windows), then using an X guest here would be most appropriate. If you are planning to run libguestfs against a mix of guests, then use a mix of guests for testing here. </p>
<p> Time how long it takes to perform inspection and mount the disks of the guest. Use the first command if you will be using disk images, and the second command if you will be using libvirt. </p>
<pre>
 time guestfish --ro -a disk.img -i exit
 time guestfish --ro -d GuestName -i exit
</pre>
<p> Run the command several times in a row and discard the first few runs, so that you are measuring a typical &#8220;hot cache&#8221; case. </p>
<p> <i>Explanation</i> </p>
<p> This command starts up the libguestfs appliance on the named disk image or libvirt guest, performs libguestfs inspection on it (see &#8220;<font SIZE="-1">INSPECTION&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)), mounts the guest’s disks, then discards all these results and shuts down. </p>
<p> The first time you run the command, it will create an appliance and cache it (usually under <i>/var/tmp/.guestfs-*</i>). Subsequent runs should reuse the cached appliance. </p>
<p> <i>Expected results</i> </p>
<p> You should expect times which are ≤ 5 seconds greater than measured in the first baseline test above. (For example, if the first baseline test ran in 5 seconds, then this test should run in ≤ 10 seconds).</p>
<h2>UNDERSTANDING THE APPLIANCE AND WHEN IT IS BUILT/CACHED</h2>
<p> The first time you use libguestfs, it will build and cache an appliance. This is usually in <i>/var/tmp/.guestfs-*</i>, unless you have set <tt>$TMPDIR</tt> or <tt>$LIBGUESTFS_CACHEDIR</tt> in which case it will be under that temporary directory. </p>
<p> For more information about how the appliance is constructed, see &#8220;<font SIZE="-1">SUPERMIN APPLIANCES&#8221;</font> in <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1). </p>
<p> Every time libguestfs runs it will check that no host files used by the appliance have changed. If any have, then the appliance is rebuilt. This usually happens when a package is installed or updated on the host (eg. using programs like <tt>&quot;yum&quot;</tt> or <tt>&quot;apt-get&quot;</tt>). The reason for reconstructing the appliance is security: the new program that has been installed might contain a security fix, and so we want to include the fixed program in the appliance automatically. </p>
<p> These are the performance implications:</p>
<dl>
<dt>&bull;</p>
<dd> The process of building (or rebuilding) the cached appliance is slow, and you can avoid this happening by using a fixed appliance (see below).</p>
<dt>&bull;</p>
<dd> If not using a fixed appliance, be aware that updating software on the host will cause a one time rebuild of the appliance.</p>
<dt>&bull;</p>
<dd> <i>/var/tmp</i> (or <tt>$TMPDIR</tt>, <tt>$LIBGUESTFS_CACHEDIR</tt>) should be on a fast disk, and have plenty of space for the appliance.</dl>
<h2>USING A FIXED APPLIANCE</h2>
<p> To fully control when the appliance is built, you can build a fixed appliance. This appliance should be stored on a fast local disk. </p>
<p> To build the appliance, run the command: </p>
<pre>
 libguestfs-make-fixed-appliance &lt;directory&gt;
</pre>
<p> replacing <tt>&quot;&lt;directory&gt;&quot;</tt> with the name of a directory where the appliance will be stored (normally you would name a subdirectory, for example: <i>/usr/local/lib/guestfs/appliance</i> or <i>/dev/shm/appliance</i>). </p>
<p> Then set <tt>$LIBGUESTFS_PATH</tt> (and ensure this environment variable is set in your libguestfs program), or modify your program so it calls <tt>&quot;guestfs_set_path&quot;</tt>. For example: </p>
<pre>
 export LIBGUESTFS_PATH=/usr/local/lib/guestfs/appliance
</pre>
<p> Now you can run libguestfs programs, virt tools, guestfish etc. as normal. The programs will use your fixed appliance, and will not ever build, rebuild, or cache their own appliance. </p>
<p> (For detailed information on this subject, see: <code><a href="/docs/linux/man/1-libguestfs-make-fixed-appliance/">libguestfs-make-fixed-appliance</a></code>(1)).</p>
<h3>Performance of the fixed appliance</h3>
<p> In our testing we did not find that using a fixed appliance gave any measurable performance benefit, even when the appliance was located in memory (ie. on <i>/dev/shm</i>). However there are two points to consider:</p>
<dl>
<dt>1.</p>
<dd> Using a fixed appliance stops libguestfs from ever rebuilding the appliance, meaning that libguestfs will have more predictable start-up times.</p>
<dt>2.</p>
<dd> The appliance is loaded on demand. A simple test such as: </p>
<pre>
 time guestfish -a /dev/null run
</pre>
<p> does not load very much of the appliance. A real libguestfs program using complicated <font SIZE="-1">API</font> calls would demand-load a lot more of the appliance. Being able to store the appliance in a specified location makes the performance more predictable.</dl>
<h2>REDUCING THE NUMBER OF TIMES THE APPLIANCE IS LAUNCHED</h2>
<p> By far the most effective, though not always the simplest way to get good performance is to ensure that the appliance is launched the minimum number of times. This will probably involve changing your libguestfs application. </p>
<p> Try to call <tt>&quot;guestfs_launch&quot;</tt> at most once per target virtual machine or disk image. </p>
<p> Instead of using a separate instance of <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1) to make a series of changes to the same guest, use a single instance of guestfish and/or use the guestfish <i>&#8211;listen</i> option. </p>
<p> Consider writing your program as a daemon which holds a guest open while making a series of changes. Or marshal all the operations you want to perform before opening the guest. </p>
<p> You can also try adding disks from multiple guests to a single appliance. Before trying this, note the following points:</p>
<dl>
<dt>1.</p>
<dd> Adding multiple guests to one appliance is a security problem because it may allow one guest to interfere with the disks of another guest. Only do it if you trust all the guests, or if you can group guests by trust.</p>
<dt>2.</p>
<dd> There is a hard limit to the number of disks you can add to a single appliance. Call &#8220;guestfs_max_disks&#8221; in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) to get this limit. For further information see &#8220;<font SIZE="-1">LIMITS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3).</p>
<dt>3.</p>
<dd> Using libguestfs this way is complicated. Disks can have unexpected interactions: for example, if two guests use the same <font SIZE="-1">UUID</font> for a filesystem (because they were cloned), or have volume groups with the same name (but see <tt>&quot;guestfs_lvm_set_filter&quot;</tt>).</dl>
<p> <code><a href="/docs/linux/man/1-virt-df/">virt-df</a></code>(1) adds multiple disks by default, so the source code for this program would be a good place to start.</p>
<h2>SHORTENING THE TIME TAKEN FOR INSPECTION OF VMs</h2>
<p> The main advice is obvious: Do not perform inspection (which is expensive) unless you need the results. </p>
<p> If you previously performed inspection on the guest, then it may be safe to cache and reuse the results from last time. </p>
<p> Some disks don’t need to be inspected at all: for example, if you are creating a disk image, or if the disk image is not a <font SIZE="-1">VM,</font> or if the disk image has a known layout. </p>
<p> Even when basic inspection (<tt>&quot;guestfs_inspect_os&quot;</tt>) is required, auxiliary inspection operations may be avoided:</p>
<dl>
<dt>&bull;</p>
<dd> Mounting disks is only necessary to get further filesystem information.</p>
<dt>&bull;</p>
<dd> Listing applications (<tt>&quot;guestfs_inspect_list_applications&quot;</tt>) is an expensive operation on Linux, but almost free on Windows.</p>
<dt>&bull;</p>
<dd> Generating a guest icon (<tt>&quot;guestfs_inspect_get_icon&quot;</tt>) is cheap on Linux but expensive on Windows.</dl>
<h2>PARALLEL APPLIANCES</h2>
<p> Libguestfs appliances are mostly I/O bound and you can launch multiple appliances in parallel. Provided there is enough free memory, there should be little difference in launching 1 appliance vs N appliances in parallel. </p>
<p> On a 2-core (4-thread) laptop with 16 <font SIZE="-1">GB</font> of <font SIZE="-1">RAM,</font> using the (not especially realistic) test Perl script below, the following plot shows excellent scalability when running between 1 and 20 appliances in parallel: </p>
<pre><code>
12 ++-- -+-- --+-- --+-- --+-- -- -+-- --+-- --+-- --+-- --+-- -++ + + + + + + + + + +* | |
    | * |
    11 ++ ++ | |
    | |
    | ** |
    10 ++ ++ | * |
    | |
    s | |
    9 ++ ++e | |
    | * |
    c | |
    8 ++*++o | * |
    | |
    n 7 ++ ++ | * |
    d | * |
    | |
    s 6 ++ ++ | ** |
    | * |
    | |
    5 ++ ++ | |
    | * |
    | ** |
    4 ++ ++ | |
    | |
    +***+ + + + + + + +3 ++-*-+-- --+-- --+-- --+-- -- -+-- --+-- --+-- --+-- --+-- -++0 2 4 6 8 10 12 14 16 18 20 number of parallel appliances
</code></pre>
<p> It is possible to run many more than 20 appliances in parallel, but if you are using the libvirt backend then you should be aware that out of the box libvirt limits the number of client connections to 20. </p>
<p> The simple Perl script below was used to collect the data for the plot above, but there is much more information on this subject, including more advanced test scripts and graphs, available in the following blog postings: </p>
<p> <a rel="nofollow" href="http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-1/">http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-1/</a> <a rel="nofollow" href="http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-2/">http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-2/</a> <a rel="nofollow" href="http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-3/">http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-3/</a> <a rel="nofollow" href="http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-4/">http://rwmj.wordpress.com/2013/02/25/multiple-libguestfs-appliances-in-parallel-part-4/</a> </p>
<p>#!/ usr / bin / env perl</p>
<p>use strict;<br />
use threads;<br />
use warnings;<br />
use Sys::Guestfs;<br />
use Time::HiRes qw(time);</p>
<p>sub test<br />
{<br />
    my $g = Sys::Guestfs-&gt;new;<br />
    $g-&gt;add_drive_ro(&#8220;/dev/null&#8221;);<br />
    $g-&gt;launch();</p>
<p>#You could add some work for libguestfs to do here.</p>
<p>    $g-&gt;close();<br />
}</p>
<p>#Get everything into cache.<br />
test();<br />
test();<br />
test();</p>
<p> for<br />
     my $nr_threads(1..20)<br />
     {<br />
         my $start_t = time();<br />
         my @threads;<br />
         foreach (1.. $nr_threads) {<br />
             push @threads, threads-&gt;create(\&amp; test)<br />
         }<br />
         foreach (@threads) {<br />
             $_-&gt;join();<br />
             if (my $err = $_-&gt;error()) {<br />
                 die &#8220;launch failed with $nr_threads threads: $err&#8221;<br />
             }<br />
         }<br />
         my $end_t = time();<br />
         printf(&#8220;%d %.2f
&#8221;, $nr_threads, $end_t &#8211; $start_t);<br />
     }</p>
<h2>USING USER-MODE LINUX</h2>
<p> Since libguestfs 1.24, it has been possible to use the User-Mode Linux (uml) backend instead of <font SIZE="-1">KVM</font> (see &#8220;USER-MODE <font SIZE="-1">LINUX BACKEND&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3)). This section makes some general remarks about this backend, but it is <code>highly advisable</code> to measure your own workload under <font SIZE="-1">UML</font> rather than trusting comments or intuition.</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">UML</font> usually performs the same or slightly slower than <font SIZE="-1">KVM,</font> on baremetal.</p>
<dt>&bull;</p>
<dd> However <font SIZE="-1">UML</font> often performs the same under virtualization as it does on baremetal, whereas <font SIZE="-1">KVM</font> can run much slower under virtualization (since hardware virt acceleration is not available).</p>
<dt>&bull;</p>
<dd> Upload and download is as much as 10 times slower on <font SIZE="-1">UML</font> than <font SIZE="-1">KVM.</font> Libguestfs sends this data over the <font SIZE="-1">UML</font> emulated serial port, which is far less efficient than KVM’s virtio-serial.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">UML</font> lacks some features (eg. qcow2 support), so it may not be applicable at all.</dl>
<p> For some actual figures, see: <a rel="nofollow" href="http://rwmj.wordpress.com/2013/08/14/performance-of-user-mode-linux-as-a-libguestfs-backend/#content">http://rwmj.wordpress.com/2013/08/14/performance-of-user-mode-linux-as-a-libguestfs-backend/#content</a></p>
<h2>TROUBLESHOOTING POOR PERFORMANCE</h2>
<h3>Ensure hardware virtualization is available</h3>
<p> Use <i>/proc/cpuinfo</i> to ensure that hardware virtualization is available. Note that you may need to enable it in your <font SIZE="-1">BIOS.</font> </p>
<p> Hardware virt is not usually available inside VMs, and libguestfs will run slowly inside another virtual machine whatever you do. Nested virtualization does not work well in our experience, and is certainly no substitute for running libguestfs on baremetal.</p>
<h3>Ensure <font SIZE="-1">KVM</font> is available</h3>
<p> Ensure that <font SIZE="-1">KVM</font> is enabled and available to the user that will run libguestfs. It should be safe to set 0666 permissions on <i>/dev/kvm</i> and most distributions now do this.</p>
<h3>Processors to avoid</h3>
<p> Avoid processors that don’t have hardware virtualization, and some processors which are simply very slow (<font SIZE="-1">AMD</font> Geode being a great example).</p>
<h3>Xen dom0</h3>
<p> In Xen, dom0 is a virtual machine, and so hardware virtualization is not available.</p>
<h3>Use libguestfs ≥ 1.34 and qemu ≥ 2.7</h3>
<p> During the libguestfs 1.33 development cycle, we spent a large amount of time concentrating on boot performance, and added some patches to libguestfs, qemu and Linux which in some cases can reduce boot times to well under 1 second. You may therefore get much better performance by moving to the versions of libguestfs or qemu mentioned in the heading.</p>
<h2>DETAILED ANALYSIS</h2>
<h3>Boot analysis</h3>
<p> In the libguestfs source directory, in <i>utils/boot-analysis</i> is a program called <tt>&quot;boot-analysis&quot;</tt>. This program is able to produce a very detailed breakdown of the boot steps (eg. qemu, <font SIZE="-1">BIOS,</font> kernel, libguestfs init script), and can measure how long it takes to perform each step. </p>
<p> To run this program, do: </p>
<pre>
 make
 ./run utils/boot-analysis/boot-analysis
</pre>
<p> There is a manual page <i>utils/boot-benchmark/boot-analysis.1</i></p>
<h3>Detailed timings using ts</h3>
<p> Use the <code><a href="/docs/linux/man/1-ts/">ts</a></code>(1) command (from moreutils) to show detailed timings: </p>
<pre>
 $ guestfish -a /dev/null run -v |&amp; ts -i '%.s'
 0.000022 libguestfs: launch: program=guestfish
 0.000134 libguestfs: launch: version=1.29.31fedora=23,release=2.fc23,libvirt
 0.000044 libguestfs: launch: backend registered: unix
 0.000035 libguestfs: launch: backend registered: uml
 0.000035 libguestfs: launch: backend registered: libvirt
 0.000032 libguestfs: launch: backend registered: direct
 0.000030 libguestfs: launch: backend=libvirt
 0.000031 libguestfs: launch: tmpdir=/tmp/libguestfsw18rBQ
 0.000029 libguestfs: launch: umask=0002
 0.000031 libguestfs: launch: euid=1000
 0.000030 libguestfs: libvirt version = 1002012 (1.2.12)
 [etc]
</pre>
<p> The timestamps are seconds (incrementally since the previous line).</p>
<h3>Detailed timings using SystemTap</h3>
<p> You can use SystemTap (<code><a href="/docs/linux/man/1-stap/">stap</a></code>(1)) to get detailed timings from libguestfs programs. </p>
<p> Save the following script as <i>time.stap</i>: </p>
<p>global last;</p>
<p>function display_time()<br />
{<br />
    now = gettimeofday_us();<br />
    delta = 0;<br />
    if (last &gt; 0)<br />
        delta = now &#8211; last;<br />
    last = now;</p>
<p>    printf(&#8220;%d (+%d):&#8221;, now, delta);<br />
}</p>
<p>probe begin<br />
{<br />
    last = 0;<br />
    printf(&#8220;ready
&#8221;);<br />
}</p>
<p>/* Display all calls to static markers. */<br />
probe process(&#8220;/usr/lib*/libguestfs.so.0&#8221;)<br />
    .provider(&#8220;guestfs&#8221;)<br />
    .mark(&#8220;*&#8221;)<br />
    ?<br />
{<br />
    display_time();<br />
    printf(&#8220;	%s %s
&#8221;, $$name, $$parms);<br />
}</p>
<p>/* Display all calls to guestfs_* functions. */<br />
probe process(&#8220;/usr/lib*/libguestfs.so.0&#8221;)<br />
    .function(&#8220;guestfs_[a-z]*&#8221;)<br />
    ?<br />
{<br />
    display_time();<br />
    printf(&#8220;	%s %s
&#8221;, probefunc(), $$parms);<br />
}</p>
<p> Run it as root in one window: </p>
<pre>
 # stap time.stap
 ready
</pre>
<p> It prints &#8220;ready&#8221; when SystemTap has loaded the program. Run your libguestfs program, guestfish or a virt tool in another window. For example: </p>
<pre>
 $ guestfish -a /dev/null run
</pre>
<p> In the stap window you will see a large amount of output, with the time taken for each step shown (microseconds in parenthesis). For example: </p>
<p>xxxx(+0)<br />
    : guestfs_create<br />
      xxxx(+29)<br />
    : guestfs_set_pgroup g = 0x17a9de0 pgroup = 0x1 xxxx(+9)<br />
    : guestfs_add_drive_opts_argv g = 0x17a9de0 [&#8230;] xxxx(+8)<br />
    : guestfs_int_safe_strdup g = 0x17a9de0 str = 0x7f8a153bed5d xxxx(+19)<br />
    : guestfs_int_safe_malloc g = 0x17a9de0 nbytes = 0x38 xxxx(+5)<br />
    : guestfs_int_safe_strdup g = 0x17a9de0 str = 0x17a9f60 xxxx(+10)<br />
    : guestfs_launch g = 0x17a9de0 xxxx(+4)<br />
    : launch_start<br />
          [etc]</p>
<p> You will need to consult, and even modify, the source to libguestfs to fully understand the output.</p>
<h3>Detailed debugging using gdb</h3>
<p> You can attach to the appliance BIOS/kernel using gdb. If you know what you&#8217;re doing, this can be a useful way to diagnose boot regressions. </p>
<p> Firstly, you have to change qemu so it runs with the <tt>&quot;-S&quot;</tt> and <tt>&quot;-s&quot;</tt> options. These options cause qemu to pause at boot and allow you to attach a debugger. Read <code><a href="/docs/linux/man/1-qemu/">qemu</a></code>(1) for further information. Libguestfs invokes qemu several times (to scan the help output and so on) and you only want the final invocation of qemu to use these options, so use a qemu wrapper script like this: </p>
<pre><code>
#!/ bin / bash -

#Set this to point to the real qemu binary.
qemu = / usr / bin / qemu - kvm

       if["$1" != "-global"];
then
#Scanning help output etc.
        exec $qemu "$@" else
#Really running qemu.
    exec $qemu -
    S - s "$@" fi
</code></pre>
<p> Now run guestfish or another libguestfs tool with the qemu wrapper (see &#8220;<font SIZE="-1">QEMU WRAPPERS&#8221;</font> in <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3) to understand what this is doing): </p>
<pre>
 LIBGUESTFS_HV=/path/to/qemu-wrapper guestfish -a /dev/null -v run
</pre>
<p> This should pause just after qemu launches. In another window, attach to qemu using gdb: </p>
<pre>
 $ gdb
 (gdb) set architecture i8086
 The target architecture is assumed to be i8086
 (gdb) target remote :1234
 Remote debugging using :1234
 0x0000fff0 in ?? ()
 (gdb) cont
</pre>
<p> At this point you can use standard gdb techniques, eg. hitting <tt>&quot;^C&quot;</tt> to interrupt the boot and <tt>&quot;bt&quot;</tt> get a stack trace, setting breakpoints, etc. Note that when you are past the <font SIZE="-1">BIOS</font> and into the Linux kernel, you&#8217;ll want to change the architecture back to 32 or 64 bit.</p>
<h2>PERFORMANCE REGRESSIONS IN OTHER PROGRAMS</h2>
<p> Sometimes performance regressions happen in other programs (eg. qemu, the kernel) that cause problems for libguestfs. </p>
<p> In the libguestfs source, <i>utils/boot-benchmark/boot-benchmark-range.pl</i> is a script which can be used to benchmark libguestfs across a range of git commits in another project to find out if any commit is causing a slowdown (or speedup). </p>
<p> To find out how to use this script, consult the manual: </p>
<pre>
 ./utils/boot-benchmark/boot-benchmark-range.pl --man
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-supermin/">supermin</a></code>(1), <code><a href="/docs/linux/man/1-guestfish/">guestfish</a></code>(1), <code><a href="/docs/linux/man/3-guestfs/">guestfs</a></code>(3), <code><a href="/docs/linux/man/3-guestfs-examples/">guestfs-examples</a></code>(3), <code><a href="/docs/linux/man/1-guestfs-internals/">guestfs-internals</a></code>(1), <code><a href="/docs/linux/man/1-libguestfs-make-fixed-appliance/">libguestfs-make-fixed-appliance</a></code>(1), <code><a href="/docs/linux/man/1-stap/">stap</a></code>(1), <code><a href="/docs/linux/man/1-qemu/">qemu</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012-2019 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <code><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></code>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAT">DETAILED ANALYSIS</a></p>
<dd>
<dt><a href="#lbAY">PERFORMANCE REGRESSIONS IN OTHER PROGRAMS</a></p>
<dd>
<dt><a href="#lbAZ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBA">AUTHORS</a></p>
<dd>
<dt><a href="#lbBB">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbBC">LICENSE</a></p>
<dd>
<dt><a href="#lbBD">BUGS</a></p>
<dd></dl>
