---
title: "mono-shlib-cop(1)"
name: "mono-shlib-cop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mono-shlib-cop/"
description: "mono-shlib-cop – Shared Library Usage Checker"
---

<h2>NAME</h2>
<p> mono-shlib-cop &#8211; Shared Library Usage Checker</p>
<h2>SYNOPSIS</h2>
<p> <code>mono-shlib-cop</code> [OPTIONS]* [ASSEMBLY-FILE-NAME]*</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-p, &#8211;prefixes=PREFIX</i></p>
<dd> Mono installation prefixes. This is to find $prefix/etc/mono/config. The default is based upon the location of mscorlib.dll, and is normally correct.</dl>
<h2>DESCRIPTION</h2>
<p> <i>mono-shlib-cop </i> is a tool that inspects a managed assembly looking for erroneous or suspecious usage of shared libraries. </p>
<p> The tool takes one or more assembly filenames, and inspects each assembly specified. </p>
<p> The errors checked for include:</p>
<dl>
<dt>*</p>
<dd> Does the shared library exist?</p>
<dt>*</p>
<dd> Does the requested symbol exist within the shared library?</dl>
<p> The warnings checked for include:</p>
<dl>
<dt>*</p>
<dd> Is the target shared library a versioned library? (Relevant only on Unix systems, not Mac OS X or Windows.)</dl>
<p> In general, only versioned libraries such as <i>libc.so.6 </i> are present on the user&#8217;s machine, and efforts to load <i>libc.so </i> will result in a <code>System.DllNotFoundException. </code> There are three solutions to this:</p>
<dl>
<dt>1.</p>
<dd> Require that the user install any <i>-devel </i> packages which provide the unversioned library. This usually requires that the user install a large number of additional packages, complicating the installation process.</p>
<dt>2.</p>
<dd> Use a fully versioned name in your <code>DllImport </code> statements. This requires editing your source code and recompiling whenever you need to target a different version of the shared library.</p>
<dt>3.</p>
<dd> Provide an <i>assembly.config </i> file which contains &lt;dllmap/&gt; elements to remap the shared library name used by your assembly to the actual versioned shared library present on the users system. Mono provides a number of pre-existing &lt;dllmap/&gt; entries, including ones for <i>libc.so </i> and <i>libX11.so.</i></dl>
<h2>EXAMPLE</h2>
<p> The following code contains examples of the above errors and warnings: </p>
<pre><code>
using System.Runtime.InteropServices; // for DllImport
class Demo
{
    [DllImport("bad-library-name")] private static extern void BadLibraryName();
    [DllImport("libc.so")] private static extern void BadSymbolName();
    [DllImport("libcap.so")] private static extern int cap_clear(IntPtr cap_p);
}
</code></pre>
<dl>
<dt>Bad library name</p>
<dd> Assuming that the library <i>bad-library-name</i> doesn&#8217;t exist on your machine, <i>Demo.BadLibraryName </i> will generate an error, as it requires a shared library which cannot be loaded. This may be ignorable; see <code>BUGS</code></p>
<dt>Bad symbol name</p>
<dd> <i>Demo.BadSymbolName </i> will generate an error, as <i>libc.so </i> (remapped to <i>libc.so.6</i> by mono&#8217;s <i>$prefix/etc/mono/config </i> file) doesn&#8217;t contain the function <i>BadSymbolName</i></p>
<dt>Unversioned library dependency</p>
<dd> Assuming you have the file <i>libcap.so</i> , <i>Demo.cap_clear </i> will generate a warning because, while <i>libcap.so </i> could be loaded, <i>libcap.so </i> might not exist on the users machine (on FC2, <i>/lib/libcap.so </i> is provided by <i>libcap-devel</i> , and you can&#8217;t assume that end users will have any <i>-devel</i> packages installed).</dl>
<h2>FIXING CODE</h2>
<p> The fix depends on the warning or error:</p>
<dl>
<dt>Bad library names</p>
<dd> Use a valid library name in the <code>DllImport </code> attribute, or provide a &lt;dllmap/&gt; entry to map your existing library name to a valid library name.</p>
<dt>Bad symbol names</p>
<dd> Reference a symbol that actually exists in the target library.</p>
<dt>Unversioned library dependency</p>
<dd> Provide a &lt;dllmap/&gt; entry to reference a properly versioned library, or ignore the warning (see <code>BUGS</code> ).</dl>
<h2>DLLMAP ENTRIES</h2>
<p> Mono looks for an <i>ASSEMBLY-NAME</i> .config file for each assembly loaded, and reads this file to find Dll mapping information. For example, with <i>mcs.exe</i> , Mono would read <i>mcs.exe.config</i> , and for <i>Mono.Posix.dll</i> , Mono would read <i>Mono.Posix.dll.config</i> . </p>
<p> The <i>.config </i> file is an XML document containing a top-level &lt;configuration/&gt; section with nested &lt;dllmap/&gt; entries, which contains <code>dll</code> and <code>target</code> attributes. The dll attribute should contain the same string used in your <code>DllImport </code> attribute value, and the target attribute specifies which shared library mono should <i>actually</i> load at runtime. </p>
<p> A sample .config file is: </p>
<pre>
        &lt;configuration&gt;
                &lt;dllmap dll=&quot;gtkembedmoz&quot; target=&quot;libgtkembedmoz.so&quot; /&gt;
        &lt;/configuration&gt;
</pre>
<h2>BUGS</h2>
<dl>
<dt>*</p>
<dd> Only <code>DllImport</code> entries are checked; the surrounding IL is ignored. Consequently, if a runtime check is performed to choose which shared library to invoke, an error will be reported even though the specified library is never used. Consider this code: </p>
<pre><code>
using System.Runtime.InteropServices; // for DllImport
class Beep
{
    [DllImport("kernel32.dll")] private static extern int Beep(int dwFreq, int dwDuration);
    [DllImport("libcurses.so")] private static extern int beep();
  public
    static void Beep()
    {
        if (System.IO.Path.DirectorySeparatorChar == '\') {
            Beep(750, 300);
        } else {
            beep();
        }
    }
}
</code></pre>
<p> If <i>mono-shlib-cop</i> is run on this assembly, an error will be reported for using <i>kernel32.dll</i> , even though <i>kernel32.dll</i> will never be used on Unix platforms.</p>
<dt>*</p>
<dd> <i>mono-shlib-cop</i> currently only examines the shared library file extension to determine if a warning should be generated. A <i>.so</i> extension will always generate a warning, even if the <i>.so </i> is not a symlink, isn&#8217;t provided in a <i>-devel </i> package, and there is no versioned shared library (possible examples including <i>/usr/lib/libtcl8.4.so, </i> <i>/usr/lib/libubsec.so,</i> etc.). </p>
<p> Consequently, warnings for any such libraries are useless, and incorrect. </p>
<p> Windows and Mac OS X will never generate warnings, as these platforms use different shared library extensions.</dl>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
