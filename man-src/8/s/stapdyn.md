---
title: "stapdyn(8)"
name: "stapdyn"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stapdyn/"
description: "stapdyn – systemtap dyninst runtime"
---

<p>stapdyn &#8211; systemtap dyninst runtime </p>
<h2>Synopsis</h2>
<p><code>stapdyn</code> [ <i>OPTIONS</i> ] <i>MODULE</i> [ <i>MODULE-OPTIONS</i> ] </p>
<h2>Description</h2>
<p>The <i>stapdyn</i> program is the dyninst back-end of the Systemtap tool. It expects a shared library produced by the front-end <i>stap</i> tool, when run with <i>&#8211;dyninst</i>. Splitting the systemtap tool into a front-end and a back-end allows a user to compile a systemtap script on a development machine that has the debugging information (need to compile the script) and then transfer the resulting shared objevct to a production machine that doesn&#8217;t have any development tools or debugging information installed. Please refer to stappaths (7) for the version number, or run rpm -q systemtap (fedora/red hat) apt-get -v systemtap (ubuntu) </p>
<h2>Options</h2>
<p>The <i>stapdyn</i> program supports the following options. Any other option prints a list of supported options.</p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose mode.</p>
<dt><code>-V</code></p>
<dd>Print version number and exit.</p>
<dt><code>-w</code></p>
<dd>Suppress warnings from the script.</p>
<dt><code>-c CMD</code></p>
<dd>Command CMD will be run and the <i>stapdyn</i> program will exit when CMD does. The &#8216;_stp_target&#8217; variable will contain the pid for CMD.</p>
<dt><code>-x PID</code></p>
<dd>The &#8216;_stp_target&#8217; variable will be set to PID.</p>
<dt><code>-o FILE</code></p>
<dd>Send output to FILE. If the module uses bulk mode, the output will be in percpu files FILE_x(FILE_cpux in background and bulk mode) where &#8216;x&#8217; is the cpu number. This supports <a href="/docs/linux/man/3-strftime/">strftime</a>(3) formats for FILE.</p>
<dt><code>-C WHEN</code></p>
<dd>Control coloring of error messages. WHEN must be either &quot;never&quot;, &quot;always&quot;, or &quot;auto&quot; (i.e. enable only if at a terminal). If the option is missing, then &quot;auto&quot; is assumed. Colors can be modified using the SYSTEMTAP_COLORS environment variable. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for more information on syntax and behaviour.</p>
<dt><code>var1=val</code></p>
<dd>Sets the value of global variable var1 to val. Global variables contained within a script are treated as options and can be set from the stapdyn command line. </p>
</dl>
<h2>Arguments</h2>
<p><code>MODULE</code> is either a module path or a module name. If it is a module name, the module will be looked for in the following directory (where &#8216;VERSION&#8217; is the output of &quot;uname -r&quot;):</p>
<dl>
<dd>/lib/modules/VERSION/systemtap</dl>
<p> $ stap &#8211;dyninst -p4 -m mod1 -e&nbsp;<wbr>&#8216;global var1=&quot;foo&quot;; probe begin{printf(&quot;%s
&quot;, var1); exit()}&#8217; </p>
<p> Running this with an additional module argument: </p>
<p> $ stapdyn mod1.so var1=&quot;HelloWorld&quot;<br />
 HelloWorld </p>
<p> Spaces and exclamation marks currently cannot be passed into global variables this way.</p>
<h2>Examples</h2>
<p>See the <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap) manual page for a collection of sample scripts. Here is a very basic example of how to use <i>stapdyn.</i> First, use <i>stap</i> to compile a script. The <i>stap</i> program will report the pathname to the resulting module. $ stap &#8211;dyninst -p4 -e &#8216;probe begin { printf(&quot;Hello World!
&quot;); exit() }&#8217;<br />
 /home/user/.systemtap/cache/85/stap_8553d83f78c_265.so Run <i>stapdyn</i> with the pathname to the module as an argument. $ stapdyn /home/user/.systemtap/cache/85/stap_8553d83f78c_265.so<br />
 Hello World! </p>
<h2>Safety And Security</h2>
<p>Systemtap, in DynInst mode, is a developer tool, and runs completely unprivileged. The Linux kernel will only permit one&#8217;s own processes to be accessed, which is enforced by the <i><a href="/docs/linux/man/2-ptrace/">ptrace</a></i>(2) system call. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for additional information on safety and security.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-stap/">stap</a></i>(1), <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapprobes/">stapprobes</a></i>(3stap), <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8), <i><a href="/docs/linux/man/8-staprun/">staprun</a></i>(8), <i><a href="//www.systutorials.com/docs/linux/man/3stap-stapex/">stapex</a></i>(3stap) </p>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
