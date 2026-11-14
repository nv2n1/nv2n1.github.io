---
title: "mkbundle(1)"
name: "mkbundle"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkbundle/"
description: "mkbundle, mkbundle2 – Creates a bundled executable."
---

<h2>NAME</h2>
<p> mkbundle, mkbundle2 &#8211; Creates a bundled executable.</p>
<h2>SYNOPSIS</h2>
<p> <code>mkbundle [options] assembly1 [assembly2 &#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>mkbundle</i> generates an executable program that will contain static copies of the assemblies listed on the command line. By default only the assemblies specified in the command line will be included in the bundle. To automatically include all of the dependencies referenced, use the &quot;&#8211;deps&quot; command line option. </p>
<p> Use <i>mkbundleFP when you want the startup runtime to load the 1.0 profile, and use mkbundle2</i> when you want the startup runtime to load the 2.0 profile. </p>
<p> For example, to create a bundle for hello world, use the following command: </p>
<pre>
        $ mkbundle -o hello hello.exe
</pre>
<p> The above will pull hello.exe into a native program called &quot;hello&quot;. Notice that the produced image still contains the CIL image and no precompilation is done. </p>
<p> In addition, it is possible to control whether <i>mkbundle</i> should compile the resulting executable or not with the -c option. This is useful if you want to link additional libraries or control the generated output in more detail. For example, this could be used to link some libraries statically: </p>
<pre>
        $ mkbundle -c -o host.c -oo bundles.o --deps hello.exe
        $ cc host.c bundles.o /usr/lib/libmono.a -lc -lrt
</pre>
<p> You may also use <i>mkbundle</i> to generate a bundle you can use when embedding the Mono runtime in a native application. In that case, use both the -c and &#8211;nomain options. The resulting host.c file will not have a main() function. Call mono_mkbundle_init() before initializing the JIT in your code so that the bundled assemblies are available to the embedded runtime.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c</i></p>
<dd> Produce the stub file, do not compile the resulting stub.</p>
<dt><i>-o filename</i></p>
<dd> Places the output on `out&#8217;. If the flag -c is specified, this is the C host program. If not, this contains the resulting executable.</p>
<dt><i>-oo filename</i></p>
<dd> Specifies the name to be used for the helper object file that contains the bundle.</p>
<dt><i>-L path</i></p>
<dd> Adds the `path&#8217; do the search list for assemblies. The rules are the same as for the compiler -lib: or -L flags.</p>
<dt>Specifies that a machine.config file must be bundled as well.</p>
<dd> Typically this is $prefix/etc/mono/1.0/machine.config or $prefix/etc/mono/2.0/machine.config depending on the profile that you are using (1.0 or 2.0)</p>
<dt><i>&#8211;nodeps</i></p>
<dd> This is the default: <i>mkbundle</i> will only include the assemblies that were specified on the command line to reduce the size of the resulting image created.</p>
<dt><i>&#8211;deps</i></p>
<dd> This option will bundle all of the referenced assemblies for the assemblies listed on the command line option. This is useful to distribute a self-contained image.</p>
<dt><i>&#8211;keeptemp</i></p>
<dd> By default <i>mkbundle</i> will delete the temporary files that it uses to produce the bundle. This option keeps the file around.</p>
<dt><i>&#8211;machine-config FILE</i></p>
<dd> Uses the given FILE as the machine.config file for the generated application.</p>
<dt><i>&#8211;nomain</i></p>
<dd> With the -c option, generate the host stub without a main() function.</p>
<dt><i>&#8211;config-dir DIR</i></p>
<dd> When passed, DIR will be set for the MONO_CFG_DIR environment variable</p>
<dt><i>&#8211;static</i></p>
<dd> By default <i>mkbundle</i> dynamically links to mono and glib. This option causes it to statically link instead.</p>
<dt><code>Important:</code></p>
<dd> Since the Mono runtime is licensed under the LGPL, even if you use static you should transfer the component pieces of the mkbundle to your users so they are able to upgrade the Mono runtime on their own.</p>
<dt>If you want to use this for commercial licenses, you must obtain a</p>
<dd> proprietary license for Mono from mono [at] novell.com</p>
<dt><i>-z</i></p>
<dd> Compresses the assemblies before embedding. This results in smaller executable files, but increases startup time and requires zlib to be installed on the target system.</dl>
<h2>WINDOWS</h2>
<p> On Windows systems, it it necessary to have Unix-like toolchain to be installed for <i>mkbundle</i> to work. You can use cygwin&#8217;s and install gcc, gcc-mingw and as packages.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>AS</i></p>
<dd> Assembler command. The default is &quot;as&quot;.</p>
<dt><i>CC</i></p>
<dd> C compiler command. The default is &quot;cc&quot; under Linux and &quot;gcc&quot; under Windows.</p>
<dt><i>MONO_BUNDLED_OPTIONS</i></p>
<dd> Options to be passed to the bundled Mono runtime, separated by spaces. See the <a href="/docs/linux/man/1-mono/">mono</a>(1) manual page or run mono &#8211;help.</dl>
<h2>FILES</h2>
<p> This program will load referenced assemblies from the Mono assembly cache.</p>
<h2>BUGS</h2>
<p> The option &quot;&#8211;static&quot; is not supported under Windows. Moreover, a full cygwin environment containing at least &quot;gcc&quot; and &quot;as&quot; is required for the build process. The generated executable does not depend on cygwin.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mcs/">mcs</a>(1),</code><a href="/docs/linux/man/1-mono/">mono</a>(1),<code><a href="/docs/linux/man/5-mono-config/">mono-config</a>(5).</code> </p>
<h2>Index</h2>
