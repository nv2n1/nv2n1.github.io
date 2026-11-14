---
title: "nsiswrapper(1)"
name: "nsiswrapper"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nsiswrapper/"
description: "nsiswrapper – Helper program for making NSIS Windows installers"
---

<h2 class="name">NAME</h2>
<p> nsiswrapper &#8211; Helper program for making NSIS Windows installers </p>
<h2>SYNOPSIS</h2>
<pre><code>
nsiswrapper[options][roots...] nsiswrapper myprogram.exe anotherprog.exe docs / &gt; script.nsis
                                                                                          nsiswrapper-- run myprogram.exe anotherprog.exe docs /
</code></pre>
<h2>DESCRIPTION</h2>
<p> nsiswrapper is a helper program for making it easier to create Windows installers in a cross-compiler environment. It still requires <font SIZE="-1">NSIS</font> (a Windows installer generator) but cuts out the tedium of writing the <font SIZE="-1">NSIS</font> command script, and can even invoke <font SIZE="-1">NSIS</font> automatically to generate a final Windows executable. </p>
<p> The general way to use it is to list out some files that you want packaged. For example: </p>
<pre>
  nsiswrapper myprogram.exe
</pre>
<p> This will search for <tt>&quot;myprogram.exe&quot;</tt> and any libraries (<tt>&quot;*.dll&quot;</tt>) that it depends upon, and then it will print out an <font SIZE="-1">NSIS</font> script. </p>
<p> If you want to have it run <tt>&quot;makensis&quot;</tt> as well (to automatically create a Windows installer) then do: </p>
<pre>
  nsiswrapper --run myprogram.exe
</pre>
<p> which will generate <tt>&quot;installer.exe&quot;</tt> output file that contains <tt>&quot;myprogram.exe&quot;</tt> plus any dependencies. </p>
<p> You can list other files and directories that you want to have contained in your installer. For example: </p>
<pre>
  nsiswrapper myprogram.exe anotherprog.exe docs/*.html
</pre>
<p> There are many other command line options which control aspects of the <font SIZE="-1">NSIS</font> command script (and hence, the final installer), such as:</p>
<dl>
<dt>*</p>
<dd> The name of the final installer.</p>
<dt>*</p>
<dd> Desktop shortcuts and menu items.</p>
<dt>*</p>
<dd> License files.</dl>
<p> It&#8217;s a good idea to examine the <font SIZE="-1">NSIS</font> command script, to check that nsiswrapper is including all the right dependencies.</p>
<h2>ROOTS (FILES AND DIRECTORIES)</h2>
<p> Each parameter should refer to a file or directory which is to be included in the installer. </p>
<p> These are known as &#8220;roots&#8221; because we also automatically add any dependencies to the list of files. Thus if a Windows executable requires any DLLs, those are added automatically. DLLs are searched for on the current <tt>$PATH</tt> (environment variable). </p>
<p> We choose the install location by removing any common prefix from the names of roots, which generally ensures that the original directory structure is preserved. Thus for example if the original roots (and any dependencies) are: </p>
<pre>
 /usr/i686-pc-mingw32/sys-root/mingw/bin/program.exe
 /usr/i686-pc-mingw32/sys-root/mingw/bin/library.dll
 /usr/i686-pc-mingw32/sys-root/mingw/etc/config
</pre>
<p> then the install directory will look like this: </p>
<pre>
 $INSTDIR/bin/program.exe
 $INSTDIR/bin/library.dll
 $INSTDIR/etc/config
</pre>
<p> (<tt>$INSTDIR</tt> is the installation directory chosen by the user at install time). </p>
<p> You can also specify the install location (relative to <tt>$INSTDIR</tt>) by adding roots of the form: </p>
<pre>
 source=destination
</pre>
<p> for example: </p>
<pre>
 /usr/i686-pc-mingw32/sys-root/mingw/bin/program.exe=program.exe
 /usr/i686-pc-mingw32/sys-root/mingw/bin/library.dll=library.dll
 /usr/i686-pc-mingw32/sys-root/mingw/etc/config=conf/config
</pre>
<p> which results in: </p>
<pre>
 $INSTDIR/program.exe
 $INSTDIR/library.dll
 $INSTDIR/conf/config
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print brief help message and exit.</p>
<dt><code>&#8211;man</code></p>
<dd> Print the full manual page for the command and exit.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose messages while running. If this is not given then we try to operate quietly.</p>
<dt><code>&#8211;run</code></p>
<dd> Normally this program just prints out the <font SIZE="-1">NSIS</font> installer command script. However if you supply this option, then we run <tt>&quot;makensis&quot;</tt> and attempt to generate an actual Windows installer.</p>
<dt><code>&#8211;with-gtk</code></p>
<dd> <font SIZE="-1">GTK</font> programs should normally supply this option. It ensures that the correct files are copied and/or created by the installer for <font SIZE="-1">GTK</font> programs to work.</p>
<dt><code>&#8211;name Name</code></p>
<dd> Set the long name of the installer. </p>
<p> If not set, the script tries to invent a suitable name based on the first root file given on the command line. </p>
<p> See also <code>&#8211;outfile</code>.</p>
<dt><code>&#8211;outfile myinstaller.exe</code></p>
<dd> Set the output filename for the installer. </p>
<p> If not set, this defaults to <tt>&quot;installer.exe&quot;</tt>. </p>
<p> This is the same as the <tt>&quot;OutFile&quot;</tt> option to <font SIZE="-1">NSIS</font>.</p>
<dt><code>&#8211;installdir &#8216;C:oo&#8217;</code></p>
<dd> Set the default Windows installation directory. If not set, this program will choose a suitable default based on the name. </p>
<p> In any case, the end user can override this when they run the installer. </p>
<p> Note that since this string will contain backslashes, you should single-quote it to protect it from the shell. </p>
<p> This is the same as the <tt>&quot;InstallDir&quot;</tt> option to <font SIZE="-1">NSIS</font>.</p>
<dt><code>&#8211;installdirregkey &#8216;</code><font SIZE="-1"><code>HKLM</code></font><code> SOFTWARE\FOO&#8217;</code></p>
<dd> Set the name of the registry key used to save the installation directory. This has two purposes: Firstly it is used to automagically remember the installation directory between installs. Secondly your program can use this as one method to find its own installation directory (there are other ways to do this). </p>
<p> The default is <tt>&quot;HKLM SOFTWARE\Name&quot;</tt> where <tt>&quot;Name&quot;</tt> is derived from the name of the installer. </p>
<p> Note that since this string will contain backslashes and spaces, you should single-quote it to protect it from the shell. </p>
<p> This is the same as the <tt>&quot;InstallDirRegKey&quot;</tt> option to <font SIZE="-1">NSIS</font>. </p>
</dl>
<h2>Index</h2>
