---
title: "staprun(8)"
name: "staprun"
section: "8"
letter: "s"
url: "/docs/linux/man/8-staprun/"
description: "staprun – systemtap runtime"
---

<p>staprun &#8211; systemtap runtime </p>
<h2>Synopsis</h2>
<p><code>staprun</code> [ <i>OPTIONS</i> ] <i>MODULE</i> [ <i>MODULE-OPTIONS</i> ] </p>
<h2>Description</h2>
<p>The <i>staprun</i> program is the back-end of the Systemtap tool. It expects a kernel module produced by the front-end <i>stap</i> tool. Splitting the systemtap tool into a front-end and a back-end allows a user to compile a systemtap script on a development machine that has the kernel development tools (needed to compile the script) and then transfer the resulting kernel module to a production machine that doesn&#8217;t have any development tools installed. Please refer to stappaths (7) for the version number, or run rpm -q systemtap (fedora/red hat) apt-get -v systemtap (ubuntu) </p>
<h2>Options</h2>
<p>The <i>staprun</i> program supports the following options. Any other option prints a list of supported options.</p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode. The level of verbosity is also set in the <i>SYSTEMTAP_VERBOSE</i> environment variable.</p>
<dt><code>-V</code></p>
<dd>Print version number and exit.</p>
<dt><code>-w</code></p>
<dd>Suppress warnings from the script.</p>
<dt><code>-u</code></p>
<dd>Load the uprobes.ko module.</p>
<dt><code>-c CMD</code></p>
<dd>Command CMD will be run and the <i>staprun</i> program will exit when CMD does. The &#8216;_stp_target&#8217; variable will contain the pid for CMD.</p>
<dt><code>-x PID</code></p>
<dd>The &#8216;_stp_target&#8217; variable will be set to PID.</p>
<dt><code>-o FILE</code></p>
<dd>Send output to FILE. If the module uses bulk mode, the output will be in percpu files FILE_x(FILE_cpux in background and bulk mode) where &#8216;x&#8217; is the cpu number. This supports <a href="/docs/linux/man/3-strftime/">strftime</a>(3) formats for FILE.</p>
<dt><code>-b BUFFER_SIZE</code></p>
<dd>The systemtap module will specify a buffer size. Setting one here will override that value. The value should be an integer between 1 and 4095 which be assumed to be the buffer size in MB. That value will be per-cpu if bulk mode is used.</p>
<dt><code>-L</code></p>
<dd>Load module and start probes, then detach from the module leaving the probes running. The module can be attached to later by using the <code>-A</code> option.</p>
<dt><code>-A</code></p>
<dd>Attach to loaded systemtap module.</p>
<dt><code>-C WHEN</code></p>
<dd>Control coloring of error messages. WHEN must be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enable only if at a terminal). If the option is missing, then &quot;auto&quot; is assumed. Colors can be modified using the SYSTEMTAP_COLORS environment variable. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more information on syntax and behaviour.</p>
<dt><code>-d</code></p>
<dd>Delete a module. Only detached or unused modules the user has permission to access will be deleted. Use &quot;*&quot; (quoted) to delete all unused modules.</p>
<dt><code>-D</code></p>
<dd>Run staprun in background as a daemon and show it&#8217;s pid.</p>
<dt><code>-R</code></p>
<dd>Rename the module to a unique name before inserting it.</p>
<dt><code>-r N:URI</code></p>
<dd>Pass the given number and URI data to the tapset functions remote_id() and remote_uri().</p>
<dt><code>-S</code><i> size[,N]</i></p>
<dd>Sets the maximum size of output file and the maximum number of output files. If the size of output file will exceed <code>size</code> , systemtap switches output file to the next file. And if the number of output files exceed <code>N</code> , systemtap removes the oldest output file. You can omit the second argument.</p>
<dt><code>-T timeout</code></p>
<dd>Sets maximum time reader thread will wait before dumping trace buffer. Value is in ms, default is 200ms. Setting this to a high value decreases number of stapio wake-ups, allowing deeper sleep for embedded platforms. But it impacts interactivity on terminal as traces are dumped less often in case of low throughput. There is no interactivity or performance impact for high throughput as trace is dumped when buffer is full, before this timeout expires.</p>
<dt><code>var1=val</code></p>
<dd>Sets the value of global variable var1 to val. Global variables contained within a module are treated as module options and can be set from the staprun command line. </p>
</dl>
<h2>Arguments</h2>
<p><code>MODULE</code> is either a module path or a module name. If it is a module name, the module will be looked for in the following directory (where &#8216;VERSION&#8217; is the output of &quot;uname -r&quot;):</p>
<dl>
<dd>/lib/modules/VERSION/systemtap</dl>
<p> Any additional arguments on the command line are passed to the module. One use of these additional module arguments is to set the value of global variables declared within the module. </p>
<p> $ stap -p4 -m mod1 -e&nbsp;<wbr>&#8216;global var1=&quot;foo&quot;; probe begin{printf(&quot;%s
&quot;, var1); exit()}&#8217; </p>
<p> Running this with an additional module argument: </p>
<p> $ staprun mod1.ko var1=&quot;HelloWorld&quot;<br />
 HelloWorld </p>
<p> Spaces and exclamation marks currently cannot be passed into global variables this way.</p>
<h2>Examples</h2>
<p>See the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap) manual page for a collection of sample scripts. </p>
<p> Here is a very basic example of how to use <i>staprun.</i> First, use <i>stap</i> to compile a script. The <i>stap</i> program will report the pathname to the resulting module. </p>
<p> $ stap -p4 -e &#8216;probe begin { printf(&quot;Hello World!
&quot;); exit() }&#8217;<br />
 /home/user/.systemtap/cache/85/stap_8553d83f78c_265.ko </p>
<p> Run <i>staprun</i> with the pathname to the module as an argument. </p>
<p> $ staprun /home/user/.systemtap/cache/85/stap_8553d83f78c_265.ko<br />
 Hello World!</p>
<h2>Module Detaching And Attaching</h2>
<p>After the <i>staprun</i> program installs a Systemtap kernel module, users can detach from the kernel module and reattach to it later. The <code>-L</code> option loads the module and automatically detaches. Users can also detach from the kernel module interactively by sending the SIGQUIT signal from the keyboard (typically by typing Ctrl-\). </p>
<p> To reattach to a kernel module, the <i>staprun</i> <code>-A</code> option would be used.</p>
<h2>File Switching By Signal</h2>
<p>After <i>staprun</i> launched the <i>stapio</i> program, users can command it to switch output file to next file when it outputs to file(s) (running staprun with <code>-o</code> option) by sending a <code>SIGUSR2</code> signal to the <i>stapio</i> process. When it receives SIGUSR2, it will switch output file to new file with suffix <i>.N</i> where N is the sequential number. For example, </p>
<p> $ staprun -o foo &#8230; </p>
<p> outputs trace logs to <i>foo</i> and if it receives <code>SIGUSR2</code> signal, it switches output to <i>foo.1</i> file. And receiving <code>SIGUSR2</code> again, it switches to <i>foo.2</i> file.</p>
<h2>Safety And Security</h2>
<p>Systemtap, in the default kernel-module runtime mode, is an administrative tool. It exposes kernel internal data structures and potentially private user information. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for additional information on safety and security. </p>
<p> To increase system security, users of systemtap must be root, or in the <i>staprun</i> group in order to execute this setuid <i>staprun</i> program. A user may select a particular privilege level with the stap <i>&#8211;privilege=</i> option, which <i>staprun</i> will later enforce.</p>
<dl>
<dt>stapdev</p>
<dd>Members of the <i>stapdev</i> group can write and load script modules with root-equivalent privileges, without particular security constraints. (Many safety constraints remain.)</p>
<dt>stapsys</p>
<dd>Members of the <i>stapsys</i> group have almost all the privileges of <i>stapdev</i>, except for guru mode constructs.</p>
<dt>staprun</p>
<dd>Members only of the <i>stapusr</i> group may any-privileged modules placed into the /lib/modules/VERSION/systemtap by the system administrator.</p>
<dt>staprun</p>
<dd>Members only of the <i>stapusr</i> group may also write and load low-privilege script modules, which are normally limited to manipulating their own processes (and not the kernel nor other users&#8217; processes).</dl>
<p> Part of the privilege enforcement mechanism may require using a stap-server and administrative trust in its cryptographic signer; see the <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8) manual page for a for more information. </p>
<p> On a kernel with FIPS mode enabled, staprun normally refuses to attempt to load systemtap-generated kernel modules. This is because on some kernels, this results in a panic. If your kernel includes corrections such as linux commit #002c77a48b47, then you can force staprun to attempt module loads anyway, by setting the <code>STAP_FIPS_OVERRIDE</code> environment variable to any value.</p>
<h2>Files</h2>
<dl>
<dt>/lib/modules/VERSION/systemtap</p>
<dd>If MODULE is a module name, the module will be looked for in this directory. Users who are only in the <i>&#8216;stapusr&#8217;</i> group can install modules located in this directory. This directory must be owned by the root user and not be world writable. </p>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-stap/">stap</a></i>(1), <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap), <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8), <i><a href="/docs/linux/man/8-stapdyn/">stapdyn</a></i>(8), <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap) </p>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
