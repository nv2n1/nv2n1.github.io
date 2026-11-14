---
title: "sprof(1)"
name: "sprof"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sprof/"
description: "sprof – read and display shared object profiling data"
---

<h2 class="name">NAME</h2>
<p> sprof &#8211; read and display shared object profiling data </p>
<h2>SYNOPSIS</h2>
<pre><code>
sprof[option]... shared - object - path[profile - data - path]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>sprof</code> command displays a profiling summary for the shared object (shared library) specified as its first command-line argument. The profiling summary is created using previously generated profiling data in the (optional) second command-line argument. If the profiling data pathname is omitted, then <code>sprof</code> will attempt to deduce it using the soname of the shared object, looking for a file with the name <i>&lt;soname&gt;.profile</i> in the current directory.</p>
<h2>OPTIONS</h2>
<p> The following command-line options specify the profile output to be produced:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;call-pairs</code></p>
<dd> Print a list of pairs of call paths for the interfaces exported by the shared object, along with the number of times each path is used.</p>
<dt><code>-p</code>, <code>&#8211;flat-profile</code></p>
<dd> Generate a flat profile of all of the functions in the monitored object, with counts and ticks.</p>
<dt><code>-q</code>, <code>&#8211;graph</code></p>
<dd> Generate a call graph.</dl>
<p> If none of the above options is specified, then the default behavior is to display a flat profile and a call graph. </p>
<p> The following additional command-line options are available:</p>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a summary of command-line options and arguments and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display a short usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the program version and exit.</dl>
<h2>CONFORMING TO</h2>
<p> The <code>sprof</code> command is a GNU extension, not present in POSIX.1.</p>
<h2>EXAMPLES</h2>
<p> The following example demonstrates the use of <code>sprof</code>. The example consists of a main program that calls two functions in a shared object. First, the code of the main program: </p>
<p> $ <code>cat prog.c</code> #include &lt;stdlib.h&gt; </p>
<p> void x1(void); void x2(void); </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x1();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x2();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> The functions <i>x1</i>() and <i>x2</i>() are defined in the following source file that is used to construct the shared object: </p>
<p> $ <code>cat libdemo.c</code> #include &lt;unistd.h&gt; </p>
<p> void consumeCpu1(int lim) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;lim;&nbsp;j++) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>getppid();<br />
 } </p>
<p> void x1(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;100;&nbsp;j++) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>consumeCpu1(200000);<br />
 } </p>
<p> void consumeCpu2(int lim) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;lim;&nbsp;j++) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>getppid();<br />
 } </p>
<p> void x2(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;1000;&nbsp;j++) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>consumeCpu2(10000);<br />
 } </p>
<p> Now we construct the shared object with the real name <i>libdemo.so.1.0.1</i>, and the soname <i>libdemo.so.1</i>: </p>
<p> $ <code>cc -g -fPIC -shared -Wl,-soname,libdemo.so.1 \</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>-o libdemo.so.1.0.1 libdemo.c</code> </p>
<p> Then we construct symbolic links for the library soname and the library linker name: </p>
<p> $ <code>ln -sf libdemo.so.1.0.1 libdemo.so.1</code> $ <code>ln -sf libdemo.so.1 libdemo.so</code> </p>
<p> Next, we compile the main program, linking it against the shared object, and then list the dynamic dependencies of the program: </p>
<p> $ <code>cc -g -o prog prog.c -L. -ldemo</code> $ <code>ldd prog</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>linux-vdso.so.1 =&gt; (0x00007fff86d66000)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>libdemo.so.1 =&gt; not found<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>libc.so.6 =&gt; /lib64/libc.so.6 (0x00007fd4dc138000)<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/lib64/ld-linux-x86-64.so.2 (0x00007fd4dc51f000)</p>
<p> In order to get profiling information for the shared object, we define the environment variable <code>LD_PROFILE</code> with the soname of the library: </p>
<p> $ <code>export LD_PROFILE=libdemo.so.1</code> </p>
<p> We then define the environment variable <code>LD_PROFILE_OUTPUT</code> with the pathname of the directory where profile output should be written, and create that directory if it does not exist already: </p>
<p> $ <code>export LD_PROFILE_OUTPUT=$(pwd)/prof_data</code> $ <code>mkdir -p $LD_PROFILE_OUTPUT</code> </p>
<p> <code>LD_PROFILE</code> causes profiling output to be <i>appended</i> to the output file if it already exists, so we ensure that there is no preexisting profiling data: </p>
<p> $ <code>rm -f $LD_PROFILE_OUTPUT/$LD_PROFILE.profile</code> </p>
<p> We then run the program to produce the profiling output, which is written to a file in the directory specified in <code>LD_PROFILE_OUTPUT</code>: </p>
<p> $ <code>LD_LIBRARY_PATH=. ./prog</code> $ <code>ls prof_data</code> libdemo.so.1.profile </p>
<p> We then use the <code>sprof -p</code> option to generate a flat profile with counts and ticks: </p>
<p> $ <code>sprof -p libdemo.so.1 $LD_PROFILE_OUTPUT/libdemo.so.1.profile</code> Flat profile: </p>
<p> Each sample counts as 0.01 seconds.<br />
&nbsp;<wbr>&nbsp;%&nbsp;<wbr>&nbsp;<wbr>&nbsp;cumulative&nbsp;<wbr>&nbsp;<wbr>&nbsp;self&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;self&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;total<br />
&nbsp;time&nbsp;<wbr>&nbsp;<wbr>&nbsp;seconds&nbsp;<wbr>&nbsp;<wbr>&nbsp;seconds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calls&nbsp;<wbr>&nbsp;us/call&nbsp;<wbr>&nbsp;us/call&nbsp;<wbr>&nbsp;name<br />
&nbsp;60.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.06&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.06&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100&nbsp;<wbr>&nbsp;<wbr>&nbsp;600.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;consumeCpu1<br />
&nbsp;40.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.04&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;40.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;consumeCpu2<br />
&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x1<br />
&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x2 </p>
<p> The <code>sprof -q</code> option generates a call graph: </p>
<p> $ <code>sprof -q libdemo.so.1 $LD_PROFILE_OUTPUT/libdemo.so.1.profile</code> </p>
<p> index % time self children called name </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100/100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x1&nbsp;[1] [0] 100.0 0.00 0.00 100 consumeCpu1 [0] &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1/1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;UNKNOWN&gt; [1] 0.0 0.00 0.00 1 x1 [1]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;100/100&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;consumeCpu1&nbsp;[0] &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1000/1000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x2&nbsp;[3] [2] 0.0 0.00 0.00 1000 consumeCpu2 [2] &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1/1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;UNKNOWN&gt; [3] 0.0 0.00 0.00 1 x2 [3]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1000/1000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;consumeCpu2&nbsp;[2] &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<p> Above and below, the &quot;&lt;UNKNOWN&gt;&quot; strings represent identifiers that are outside of the profiled object (in this example, these are instances of <i>main()</i>). </p>
<p> The <code>sprof -c</code> option generates a list of call pairs and the number of their occurrences: </p>
<p> $ <code>sprof -c libdemo.so.1 $LD_PROFILE_OUTPUT/libdemo.so.1.profile</code> &lt;UNKNOWN&gt; x1 1 x1 consumeCpu1 100 &lt;UNKNOWN&gt; x2 1 x2 consumeCpu2 1000</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1), <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
