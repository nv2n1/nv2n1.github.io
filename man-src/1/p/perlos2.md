---
title: "perlos2(1)"
name: "perlos2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlos2/"
---

<h2 class="name">NAME</h2>
 

 perlos2 - Perl under OS/2, DOS, Win0.3*, Win0.95 and WinNT. 

<h2>SYNOPSIS</h2>

 One can read this document in the following formats: 

 <pre>
        man perlos2
        view perl perlos2
        explorer perlos2.html
        info perlos2
</pre> 

 to list some (not all may be available simultaneously), or it may be read <i>as is</i>: either as <i></i><font SIZE="-1"><i>README</i></font><i>.os2</i>, or <i>pod/perlos2.pod</i>. 

 To read the <i>.INF</i> version of documentation (<b>very</b> recommended) outside of <font SIZE="-1">OS/2,</font> one needs an <font SIZE="-1">IBM</font>'s reader (may be available on <font SIZE="-1">IBM</font> ftp sites (?) (<font SIZE="-1">URL</font> anyone?)) or shipped with <font SIZE="-1">PC DOS 7.0</font> and <font SIZE="-1">IBM</font>'s Visual Age C<font SIZE="-2">++</font> 3.5. 

 A copy of a Win* viewer is contained in the ``Just add <font SIZE="-1">OS/2</font> Warp'' package 

 <pre>
  <a HREF="ftp://ftp.software.ibm.com/ps/products/os2/tools/jaow/jaow.zip">ftp://ftp.software.ibm.com/ps/products/os2/tools/jaow/jaow.zip</a>
</pre> 

 in <i>?:\JUST_ADD\view.exe</i>. This gives one an access to <font SIZE="-1">EMX</font>'s <i>.INF</i> docs as well (text form is available in <i>/emx/doc</i> in <font SIZE="-1">EMX</font>'s distribution). There is also a different viewer named xview. 

 Note that if you have <i>lynx.exe</i> or <i>netscape.exe</i> installed, you can follow <font SIZE="-1">WWW</font> links from this document in <i>.INF</i> format. If you have <font SIZE="-1">EMX</font> docs installed correctly, you can follow library links (you need to have <tt>&quot;view emxbook&quot;</tt> working by setting <tt>&quot;EMXBOOK&quot;</tt> environment variable as it is described in <font SIZE="-1">EMX</font> docs).

<h2>DESCRIPTION</h2>

<h3>Target</h3>

 The target is to make <font SIZE="-1">OS/2</font> one of the best supported platform for using/building/developing Perl and <i>Perl applications</i>, as well as make Perl the best language to use under <font SIZE="-1">OS/2.</font> The secondary target is to try to make this work under <font SIZE="-1">DOS</font> and Win* as well (but not <b>too</b> hard). 

 The current state is quite close to this target. Known limitations:
<dl>
<dt>&bull;
<dd> Some *nix programs use <b>fork()</b> a lot; with the mostly useful flavors of perl for <font SIZE="-1">OS/2</font> (there are several built simultaneously) this is supported; but some flavors do not support this (e.g., when Perl is called from inside <font SIZE="-1">REXX</font>). Using <b>fork()</b> after <i>use</i>ing dynamically loading extensions would not work with <i>very</i> old versions of <font SIZE="-1">EMX.</font>
<dt>&bull;
<dd> You need a separate perl executable <i>perl__.exe</i> (see ``perl__.exe'') if you want to use <font SIZE="-1">PM</font> code in your application (as Perl/Tk or OpenGL Perl modules do) without having a text-mode window present. 

 While using the standard <i>perl.exe</i> from a text-mode window is possible too, I have seen cases when this causes degradation of the system stability. Using <i>perl__.exe</i> avoids such a degradation.
<dt>&bull;
<dd> There is no simple way to access <font SIZE="-1">WPS</font> objects. The only way I know is via <tt>&quot;OS2::REXX&quot;</tt> and <tt>&quot;SOM&quot;</tt> extensions (see <font SIZE="-1">OS2::REXX</font>, <font SIZE="-1">SOM</font>). However, we do not have access to convenience methods of Object-REXX. (Is it possible at all? I know of no Object-REXX <font SIZE="-1">API.</font>) The <tt>&quot;SOM&quot;</tt> extension (currently in alpha-text) may eventually remove this shortcoming; however, due to the fact that <font SIZE="-1">DII</font> is not supported by the <tt>&quot;SOM&quot;</tt> module, using <tt>&quot;SOM&quot;</tt> is not as convenient as one would like it.</dl>
 

 Please keep this list up-to-date by informing me about other items.

<h3>Other OSes</h3>

 Since <font SIZE="-1">OS/2</font> port of perl uses a remarkable <font SIZE="-1">EMX</font> environment, it can run (and build extensions, and - possibly - be built itself) under any environment which can run <font SIZE="-1">EMX.</font> The current list is <font SIZE="-1">DOS,</font> DOS-inside-OS/2, Win0.3*, Win0.95 and WinNT. Out of many perl flavors, only one works, see &quot;<i>perl_.exe</i>&quot;. 

 Note that not all features of Perl are available under these environments. This depends on the features the <i>extender</i> - most probably <font SIZE="-1">RSX</font> - decided to implement. 

 Cf. ``Prerequisites''.

<h3>Prerequisites</h3>

<dl>
<dt><font SIZE="-1">EMX</font>
<dd> <font SIZE="-1">EMX</font> runtime is required (may be substituted by <font SIZE="-1">RSX</font>). Note that it is possible to make <i>perl_.exe</i> to run under <font SIZE="-1">DOS</font> without any external support by binding <i>emx.exe</i>/<i>rsx.exe</i> to it, see <tt>&quot;emxbind&quot;</tt>. Note that under <font SIZE="-1">DOS</font> for best results one should use <font SIZE="-1">RSX</font> runtime, which has much more functions working (like <tt>&quot;fork&quot;</tt>, <tt>&quot;popen&quot;</tt> and so on). In fact <font SIZE="-1">RSX</font> is required if there is no <font SIZE="-1">VCPI</font> present. Note the <font SIZE="-1">RSX</font> requires <font SIZE="-1">DPMI.</font> Many implementations of <font SIZE="-1">DPMI</font> are known to be very buggy, beware! 

 Only the latest runtime is supported, currently <tt>&quot;0.9d fix 03&quot;</tt>. Perl may run under earlier versions of <font SIZE="-1">EMX,</font> but this is not tested. 

 One can get different parts of <font SIZE="-1">EMX</font> from, say 

 <pre>
  <a HREF="ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/emx+gcc/">ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/emx+gcc/</a>
  <a rel="nofollow" HREF="http://hobbes.nmsu.edu/h-browse.php?dir=/pub/os2/dev/emx/v0.9d/">http://hobbes.nmsu.edu/h-browse.php?dir=/pub/os2/dev/emx/v0.9d/</a>
</pre> 

 The runtime component should have the name <i>emxrt.zip</i>. 

 <font SIZE="-1"><b>NOTE</b></font>. When using <i>emx.exe</i>/<i>rsx.exe</i>, it is enough to have them on your path. One does not need to specify them explicitly (though this 

 <pre>
  emx perl_.exe -de 0
</pre> 

 will work as well.)
<dt><font SIZE="-1">RSX</font>
<dd> To run Perl on <font SIZE="-1">DPMI</font> platforms one needs <font SIZE="-1">RSX</font> runtime. This is needed under DOS-inside-OS/2, Win0.3*, Win0.95 and WinNT (see ``Other OSes''). <font SIZE="-1">RSX</font> would not work with <font SIZE="-1">VCPI</font> only, as <font SIZE="-1">EMX</font> would, it requires <font SIZE="-1">DMPI.</font> 

 Having <font SIZE="-1">RSX</font> and the latest <i>sh.exe</i> one gets a fully functional <b>*nix</b>-ish environment under <font SIZE="-1">DOS,</font> say, <tt>&quot;fork&quot;</tt>, <tt>&quot;``&quot;</tt> and pipe-<tt>&quot;open&quot;</tt> work. In fact, MakeMaker works (for static build), so one can have Perl development environment under <font SIZE="-1">DOS.</font> 

 One can get <font SIZE="-1">RSX</font> from, say 

 <pre>
  <a rel="nofollow" HREF="http://cd.textfiles.com/hobbesos29804/disk1/EMX09C/">http://cd.textfiles.com/hobbesos29804/disk1/EMX09C/</a>
  <a HREF="ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/emx+gcc/contrib/">ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/emx+gcc/contrib/</a>
</pre> 

 Contact the author on <tt>&quot;rainer [at] mathematik.uni-bielefeld.de&quot;</tt>. 

 The latest <i>sh.exe</i> with <font SIZE="-1">DOS</font> hooks is available in 

 <pre>
  <a rel="nofollow" HREF="http://www.ilyaz.org/software/os2/">http://www.ilyaz.org/software/os2/</a>
</pre> 

 as <i>sh_dos.zip</i> or under similar names starting with <tt>&quot;sh&quot;</tt>, <tt>&quot;pdksh&quot;</tt> etc.
<dt><font SIZE="-1">HPFS</font>
<dd> Perl does not care about file systems, but the perl library contains many files with long names, so to install it intact one needs a file system which supports long file names. 

 Note that if you do not plan to build the perl itself, it may be possible to fool <font SIZE="-1">EMX</font> to truncate file names. This is not supported, read <font SIZE="-1">EMX</font> docs to see how to do it.
<dt>pdksh
<dd> To start external programs with complicated command lines (like with pipes in between, and/or quoting of arguments), Perl uses an external shell. With <font SIZE="-1">EMX</font> port such shell should be named <i>sh.exe</i>, and located either in the wired-in-during-compile locations (usually <i>F:/bin</i>), or in configurable location (see &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;). 

 For best results use <font SIZE="-1">EMX</font> pdksh. The standard binary (5.2.14 or later) runs under <font SIZE="-1">DOS</font> (with ``<font SIZE="-1">RSX''</font>) as well, see 

 <pre>
  <a rel="nofollow" HREF="http://www.ilyaz.org/software/os2/">http://www.ilyaz.org/software/os2/</a>
</pre></dl>

<h3>Starting Perl programs under <font SIZE="-1">OS/2</font> (and <font SIZE="-1">DOS</font> and...)</h3>

 Start your Perl program <i>foo.pl</i> with arguments <tt>&quot;arg1 arg2 arg3&quot;</tt> the same way as on any other platform, by 

 <pre>
        perl foo.pl arg1 arg2 arg3
</pre> 

 If you want to specify perl options <tt>&quot;-my_opts&quot;</tt> to the perl itself (as opposed to your program), use 

 <pre>
        perl -my_opts foo.pl arg1 arg2 arg3
</pre> 

 Alternately, if you use OS/2-ish shell, like <font SIZE="-1">CMD</font> or 4os2, put the following at the start of your perl script: 

 <pre>
        extproc perl -S -my_opts
</pre> 

 rename your program to <i>foo.cmd</i>, and start it by typing 

 <pre>
        foo arg1 arg2 arg3
</pre> 

 Note that because of stupid <font SIZE="-1">OS/2</font> limitations the full path of the perl script is not available when you use <tt>&quot;extproc&quot;</tt>, thus you are forced to use <tt>&quot;-S&quot;</tt> perl switch, and your script should be on the <tt>&quot;PATH&quot;</tt>. As a plus side, if you know a full path to your script, you may still start it with 

 <pre>
        perl ../../blah/foo.cmd arg1 arg2 arg3
</pre> 

 (note that the argument <tt>&quot;-my_opts&quot;</tt> is taken care of by the <tt>&quot;extproc&quot;</tt> line in your script, see &quot;<tt>&quot;extproc&quot;</tt> on the first line&quot;). 

 To understand what the above <i>magic</i> does, read perl docs about <tt>&quot;-S&quot;</tt> switch - see perlrun, and cmdref about <tt>&quot;extproc&quot;</tt>: 

 <pre>
        view perl perlrun
        man perlrun
        view cmdref extproc
        help extproc
</pre> 

 or whatever method you prefer. 

 There are also endless possibilities to use <i>executable extensions</i> of 4os2, <i>associations</i> of <font SIZE="-1">WPS</font> and so on... However, if you use *nixish shell (like <i>sh.exe</i> supplied in the binary distribution), you need to follow the syntax specified in ``Command Switches'' in perlrun. 

 Note that <b>-S</b> switch supports scripts with additional extensions <i>.cmd</i>, <i>.btm</i>, <i>.bat</i>, <i>.pl</i> as well.

<h3>Starting <font SIZE="-1">OS/2</font> (and <font SIZE="-1">DOS</font>) programs under Perl</h3>

 This is what <b>system()</b> (see ``system'' in perlfunc), <tt>&quot;``&quot;</tt> (see ``I/O Operators'' in perlop), and <i>open pipe</i> (see ``open'' in perlfunc) are for. (Avoid <b>exec()</b> (see ``exec'' in perlfunc) unless you know what you do). 

 Note however that to use some of these operators you need to have a sh-syntax shell installed (see ``Pdksh'', ``Frequently asked questions''), and perl should be able to find it (see &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;). 

 The cases when the shell is used are:
<dl>
<dt>1.
<dd> One-argument <b>system()</b> (see ``system'' in perlfunc), <b>exec()</b> (see ``exec'' in perlfunc) with redirection or shell meta-characters;
<dt>2.
<dd> Pipe-open (see ``open'' in perlfunc) with the command which contains redirection or shell meta-characters;
<dt>3.
<dd> Backticks <tt>&quot;``&quot;</tt> (see ``I/O Operators'' in perlop) with the command which contains redirection or shell meta-characters;
<dt>4.
<dd> If the executable called by <b>system()</b>/<b>exec()</b>/pipe-<b>open()</b>/<tt>&quot;``&quot;</tt> is a script with the ``magic'' <tt>&quot;#!&quot;</tt> line or <tt>&quot;extproc&quot;</tt> line which specifies shell;
<dt>5.
<dd> If the executable called by <b>system()</b>/<b>exec()</b>/pipe-<b>open()</b>/<tt>&quot;``&quot;</tt> is a script without ``magic'' line, and <tt>$ENV{EXECSHELL}</tt> is set to shell;
<dt>6.
<dd> If the executable called by <b>system()</b>/<b>exec()</b>/pipe-<b>open()</b>/<tt>&quot;``&quot;</tt> is not found (is not this remark obsolete?);
<dt>7.
<dd> For globbing (see ``glob'' in perlfunc, ``I/O Operators'' in perlop) (obsolete? Perl uses builtin globbing nowadays...).</dl>
 

 For the sake of speed for a common case, in the above algorithms backslashes in the command name are not considered as shell metacharacters. 

 Perl starts scripts which begin with cookies <tt>&quot;extproc&quot;</tt> or <tt>&quot;#!&quot;</tt> directly, without an intervention of shell. Perl uses the same algorithm to find the executable as <i>pdksh</i>: if the path on <tt>&quot;#!&quot;</tt> line does not work, and contains <tt>&quot;/&quot;</tt>, then the directory part of the executable is ignored, and the executable is searched in <i>.</i> and on <tt>&quot;PATH&quot;</tt>. To find arguments for these scripts Perl uses a different algorithm than <i>pdksh</i>: up to 3 arguments are recognized, and trailing whitespace is stripped. 

 If a script does not contain such a cooky, then to avoid calling <i>sh.exe</i>, Perl uses the same algorithm as <i>pdksh</i>: if <tt>$ENV{EXECSHELL}</tt> is set, the script is given as the first argument to this command, if not set, then <tt>&quot;$ENV{COMSPEC} /c&quot;</tt> is used (or a hardwired guess if <tt>$ENV{COMSPEC}</tt> is not set). 

 When starting scripts directly, Perl uses exactly the same algorithm as for the search of script given by <b>-S</b> command-line option: it will look in the current directory, then on components of <tt>$ENV{PATH}</tt> using the following order of appended extensions: no extension, <i>.cmd</i>, <i>.btm</i>, <i>.bat</i>, <i>.pl</i>. 

 Note that Perl will start to look for scripts only if <font SIZE="-1">OS/2</font> cannot start the specified application, thus <tt>&quot;system 'blah'&quot;</tt> will not look for a script if there is an executable file <i>blah.exe</i> <i>anywhere</i> on <tt>&quot;PATH&quot;</tt>. In other words, <tt>&quot;PATH&quot;</tt> is essentially searched twice: once by the <font SIZE="-1">OS</font> for an executable, then by Perl for scripts. 

 Note also that executable files on <font SIZE="-1">OS/2</font> can have an arbitrary extension, but <i>.exe</i> will be automatically appended if no dot is present in the name. The workaround is as simple as that: since <i>blah.</i> and <i>blah</i> denote the same file (at list on <font SIZE="-1">FAT</font> and <font SIZE="-1">HPFS</font> file systems), to start an executable residing in file <i>n:/bin/blah</i> (no extension) give an argument <tt>&quot;n:/bin/blah.&quot;</tt> (dot appended) to <b>system()</b>. 

 Perl will start <font SIZE="-1">PM</font> programs from <font SIZE="-1">VIO</font> (=text-mode) Perl process in a separate <font SIZE="-1">PM</font> session; the opposite is not true: when you start a non-PM program from a <font SIZE="-1">PM</font> Perl process, Perl would not run it in a separate session. If a separate session is desired, either ensure that shell will be used, as in <tt>&quot;system 'cmd /c myprog'&quot;</tt>, or start it using optional arguments to <b>system()</b> documented in <tt>&quot;OS2::Process&quot;</tt> module. This is considered to be a feature.

<h2>Frequently asked questions</h2>

<h3>It does not work</h3>

 Perl binary distributions come with a <i>testperl.cmd</i> script which tries to detect common problems with misconfigured installations. There is a pretty large chance it will discover which step of the installation you managed to goof. <tt>&quot;;-)&quot;</tt>

<h3>I cannot run external programs</h3>

<dl>
<dt>&bull;
<dd> Did you run your programs with <tt>&quot;-w&quot;</tt> switch? See ``Starting <font SIZE="-1">OS/2</font> (and <font SIZE="-1">DOS</font>) programs under Perl''.
<dt>&bull;
<dd> Do you try to run <i>internal</i> shell commands, like <tt>&quot;`copy a b`&quot;</tt> (internal for <i>cmd.exe</i>), or <tt>&quot;`glob a*b`&quot;</tt> (internal for ksh)? You need to specify your shell explicitly, like <tt>&quot;`cmd /c copy a b`&quot;</tt>, since Perl cannot deduce which commands are internal to your shell.</dl>

<h3>I cannot embed perl into my program, or use <i>perl.dll</i> from my program.</h3>

<dl>
<dt>Is your program EMX-compiled with &quot;-Zmt -Zcrtdll&quot;?
<dd> Well, nowadays Perl <font SIZE="-1">DLL</font> should be usable from a differently compiled program too... If you can run Perl code from <font SIZE="-1">REXX</font> scripts (see <font SIZE="-1">OS2::REXX</font>), then there are some other aspect of interaction which are overlooked by the current hackish code to support differently-compiled principal programs. 

 If everything else fails, you need to build a stand-alone <font SIZE="-1">DLL</font> for perl. Contact me, I did it once. Sockets would not work, as a lot of other stuff.
<dt>Did you use ExtUtils::Embed?
<dd> Some time ago I had reports it does not work. Nowadays it is checked in the Perl test suite, so grep <i>./t</i> subdirectory of the build tree (as well as <i>*.t</i> files in the <i>./lib</i> subdirectory) to find how it should be done ``correctly''.</dl>

<h3>`` and pipe-open do not work under <font SIZE="-1">DOS.</font></h3>

 This may a variant of just ``I cannot run external programs'', or a deeper problem. Basically: you <i>need</i> <font SIZE="-1">RSX</font> (see ``Prerequisites'') for these commands to work, and you may need a port of <i>sh.exe</i> which understands command arguments. One of such ports is listed in ``Prerequisites'' under <font SIZE="-1">RSX.</font> Do not forget to set variable &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot; as well. 

 <font SIZE="-1">DPMI</font> is required for <font SIZE="-1">RSX.</font>

<h3>Cannot start find.exe pattern file</h3>

 The whole idea of the ``standard C <font SIZE="-1">API</font> to start applications'' is that the forms <tt>&quot;foo&quot;</tt> and <tt>&quot;foo&quot;</tt> of program arguments are completely interchangeable. <i>find</i> breaks this paradigm; 

 <pre>
  find &quot;pattern&quot; file
  find pattern file
</pre> 

 are not equivalent; <i>find</i> cannot be started directly using the above <font SIZE="-1">API.</font> One needs a way to surround the doublequotes in some other quoting construction, necessarily having an extra non-Unixish shell in between. 

 Use one of 

 <pre>
  system 'cmd', '/c', 'find &quot;pattern&quot; file';
  `cmd /c 'find &quot;pattern&quot; file'`
</pre> 

 This would start <i>find.exe</i> via <i>cmd.exe</i> via <tt>&quot;sh.exe&quot;</tt> via <tt>&quot;perl.exe&quot;</tt>, but this is a price to pay if you want to use non-conforming program.

<h2>INSTALLATION</h2>

<h3>Automatic binary installation</h3>

 The most convenient way of installing a binary distribution of perl is via perl installer <i>install.exe</i>. Just follow the instructions, and 99% of the installation blues would go away. 

 Note however, that you need to have <i>unzip.exe</i> on your path, and <font SIZE="-1">EMX</font> environment <i>running</i>. The latter means that if you just installed <font SIZE="-1">EMX,</font> and made all the needed changes to <i>Config.sys</i>, you may need to reboot in between. Check <font SIZE="-1">EMX</font> runtime by running 

 <pre>
        emxrev
</pre> 

 Binary installer also creates a folder on your desktop with some useful objects. If you need to change some aspects of the work of the binary installer, feel free to edit the file <i>Perl.pkg</i>. This may be useful e.g., if you need to run the installer many times and do not want to make many interactive changes in the <font SIZE="-1">GUI.</font> 

 <b>Things not taken care of by automatic binary installation:</b>
<dl>
<dt>&quot;PERL_BADLANG&quot;
<dd> may be needed if you change your codepage <i>after</i> perl installation, and the new value is not supported by <font SIZE="-1">EMX.</font> See &quot;<tt>&quot;PERL_BADLANG&quot;</tt>&quot;.
<dt>&quot;PERL_BADFREE&quot;
<dd> see &quot;<tt>&quot;PERL_BADFREE&quot;</tt>&quot;.
<dt><i>Config.pm</i>
<dd> This file resides somewhere deep in the location you installed your perl library, find it out by 

 <pre>
  perl -MConfig -le &quot;print $INC{'Config.pm'}&quot;
</pre> 

 While most important values in this file <i>are</i> updated by the binary installer, some of them may need to be hand-edited. I know no such data, please keep me informed if you find one. Moreover, manual changes to the installed version may need to be accompanied by an edit of this file.</dl>
 

 <font SIZE="-1"><b>NOTE</b></font>. Because of a typo the binary installer of 5.00305 would install a variable <tt>&quot;PERL_SHPATH&quot;</tt> into <i>Config.sys</i>. Please remove this variable and put &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot; instead.

<h3>Manual binary installation</h3>

 As of version 5.00305, <font SIZE="-1">OS/2</font> perl binary distribution comes split into 11 components. Unfortunately, to enable configurable binary installation, the file paths in the zip files are not absolute, but relative to some directory. 

 Note that the extraction with the stored paths is still necessary (default with unzip, specify <tt>&quot;-d&quot;</tt> to pkunzip). However, you need to know where to extract the files. You need also to manually change entries in <i>Config.sys</i> to reflect where did you put the files. Note that if you have some primitive unzipper (like <tt>&quot;pkunzip&quot;</tt>), you may get a lot of warnings/errors during unzipping. Upgrade to <tt>&quot;(w)unzip&quot;</tt>. 

 Below is the sample of what to do to reproduce the configuration on my machine. In <i></i><font SIZE="-1"><i>VIEW.EXE</i></font><i></i> you can press <tt>&quot;Ctrl-Insert&quot;</tt> now, and cut-and-paste from the resulting file - created in the directory you started <i></i><font SIZE="-1"><i>VIEW.EXE</i></font><i></i> from. 

 For each component, we mention environment variables related to each installation directory. Either choose directories to match your values of the variables, or create/append-to variables to take into account the directories.
<dl>
<dt>Perl <font SIZE="-1">VIO</font> and <font SIZE="-1">PM</font> executables (dynamically linked)
<dd> <pre>
  unzip perl_exc.zip *.exe *.ico -d f:/emx.add/bin
  unzip perl_exc.zip *.dll -d f:/emx.add/dll
</pre> 

 (have the directories with <tt>&quot;*.exe&quot;</tt> on <font SIZE="-1">PATH,</font> and <tt>&quot;*.dll&quot;</tt> on <font SIZE="-1">LIBPATH</font>);
<dt>Perl_ <font SIZE="-1">VIO</font> executable (statically linked)
<dd> <pre>
  unzip perl_aou.zip -d f:/emx.add/bin
</pre> 

 (have the directory on <font SIZE="-1">PATH</font>);
<dt>Executables for Perl utilities
<dd> <pre>
  unzip perl_utl.zip -d f:/emx.add/bin
</pre> 

 (have the directory on <font SIZE="-1">PATH</font>);
<dt>Main Perl library
<dd> <pre>
  unzip perl_mlb.zip -d f:/perllib/lib
</pre> 

 If this directory is exactly the same as the prefix which was compiled into <i>perl.exe</i>, you do not need to change anything. However, for perl to find the library if you use a different path, you need to <tt>&quot;set PERLLIB_PREFIX&quot;</tt> in <i>Config.sys</i>, see &quot;<tt>&quot;PERLLIB_PREFIX&quot;</tt>&quot;.
<dt>Additional Perl modules
<dd> <pre>
  unzip perl_ste.zip -d f:/perllib/lib/site_perl/5.30.0/
</pre> 

 Same remark as above applies. Additionally, if this directory is not one of directories on <tt>@INC</tt> (and <tt>@INC</tt> is influenced by <tt>&quot;PERLLIB_PREFIX&quot;</tt>), you need to put this directory and subdirectory <i>./os2</i> in <tt>&quot;PERLLIB&quot;</tt> or <tt>&quot;PERL5LIB&quot;</tt> variable. Do not use <tt>&quot;PERL5LIB&quot;</tt> unless you have it set already. See ``<font SIZE="-1">ENVIRONMENT''</font> in perl. 

 <b>[Check whether this extraction directory is still applicable with the new directory structure layout!]</b>
<dt>Tools to compile Perl modules
<dd> <pre>
  unzip perl_blb.zip -d f:/perllib/lib
</pre> 

 Same remark as for <i>perl_ste.zip</i>.
<dt>Manpages for Perl and utilities
<dd> <pre>
  unzip perl_man.zip -d f:/perllib/man
</pre> 

 This directory should better be on <tt>&quot;MANPATH&quot;</tt>. You need to have a working <i>man</i> to access these files.
<dt>Manpages for Perl modules
<dd> <pre>
  unzip perl_mam.zip -d f:/perllib/man
</pre> 

 This directory should better be on <tt>&quot;MANPATH&quot;</tt>. You need to have a working man to access these files.
<dt>Source for Perl documentation
<dd> <pre>
  unzip perl_pod.zip -d f:/perllib/lib
</pre> 

 This is used by the <tt>&quot;perldoc&quot;</tt> program (see perldoc), and may be used to generate <font SIZE="-1">HTML</font> documentation usable by <font SIZE="-1">WWW</font> browsers, and documentation in zillions of other formats: <tt>&quot;info&quot;</tt>, <tt>&quot;LaTeX&quot;</tt>, <tt>&quot;Acrobat&quot;</tt>, <tt>&quot;FrameMaker&quot;</tt> and so on. [Use programs such as <i>pod2latex</i> etc.]
<dt>Perl manual in <i>.INF</i> format
<dd> <pre>
  unzip perl_inf.zip -d d:/os2/book
</pre> 

 This directory should better be on <tt>&quot;BOOKSHELF&quot;</tt>.
<dt>Pdksh
<dd> <pre>
  unzip perl_sh.zip -d f:/bin
</pre> 

 This is used by perl to run external commands which explicitly require shell, like the commands using <i>redirection</i> and <i>shell metacharacters</i>. It is also used instead of explicit <i>/bin/sh</i>. 

 Set <tt>&quot;PERL_SH_DIR&quot;</tt> (see &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;) if you move <i>sh.exe</i> from the above location. 

 <b>Note.</b> It may be possible to use some other sh-compatible shell (untested).</dl>
 

 After you installed the components you needed and updated the <i>Config.sys</i> correspondingly, you need to hand-edit <i>Config.pm</i>. This file resides somewhere deep in the location you installed your perl library, find it out by 

 <pre>
  perl -MConfig -le &quot;print $INC{'Config.pm'}&quot;
</pre> 

 You need to correct all the entries which look like file paths (they currently start with <tt>&quot;f:/&quot;</tt>).

<h3><b>Warning</b></h3>

 The automatic and manual perl installation leave precompiled paths inside perl executables. While these paths are overwritable (see &quot;<tt>&quot;PERLLIB_PREFIX&quot;</tt>&quot;, &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;), some people may prefer binary editing of paths inside the executables/DLLs.

<h2>Accessing documentation</h2>

 Depending on how you built/installed perl you may have (otherwise identical) Perl documentation in the following formats:

<h3><font SIZE="-1">OS/2</font> <i>.INF</i> file</h3>

 Most probably the most convenient form. Under <font SIZE="-1">OS/2</font> view it as 

 <pre>
  view perl
  view perl perlfunc
  view perl less
  view perl ExtUtils::MakeMaker
</pre> 

 (currently the last two may hit a wrong location, but this may improve soon). Under Win* see ``<font SIZE="-1">SYNOPSIS''</font>. 

 If you want to build the docs yourself, and have <i></i><font SIZE="-1"><i>OS/2</i></font><i> toolkit</i>, run 

 <pre>
        pod2ipf &gt; perl.ipf
</pre> 

 in <i>/perllib/lib/pod</i> directory, then 

 <pre>
        ipfc /inf perl.ipf
</pre> 

 (Expect a lot of errors during the both steps.) Now move it on your <font SIZE="-1">BOOKSHELF</font> path.

<h3>Plain text</h3>

 If you have perl documentation in the source form, perl utilities installed, and <font SIZE="-1">GNU</font> groff installed, you may use 

 <pre>
        perldoc perlfunc
        perldoc less
        perldoc ExtUtils::MakeMaker
</pre> 

 to access the perl documentation in the text form (note that you may get better results using perl manpages). 

 Alternately, try running pod2text on <i>.pod</i> files.

<h3>Manpages</h3>

 If you have <i>man</i> installed on your system, and you installed perl manpages, use something like this: 

 <pre>
        man perlfunc
        man 3 less
        man ExtUtils.MakeMaker
</pre> 

 to access documentation for different components of Perl. Start with 

 <pre>
        man perl
</pre> 

 Note that dot (<i>.</i>) is used as a package separator for documentation for packages, and as usual, sometimes you need to give the section - <tt>3</tt> above - to avoid shadowing by the <i></i><a HREF="/docs/linux/man/1-less/">less</a><i>(1) manpage</i>. 

 Make sure that the directory <b>above</b> the directory with manpages is on our <tt>&quot;MANPATH&quot;</tt>, like this 

 <pre>
  set MANPATH=c:/man;f:/perllib/man
</pre> 

 for Perl manpages in <tt>&quot;f:/perllib/man/man1/&quot;</tt> etc.

<h3><font SIZE="-1">HTML</font></h3>

 If you have some <font SIZE="-1">WWW</font> browser available, installed the Perl documentation in the source form, and Perl utilities, you can build <font SIZE="-1">HTML</font> docs. Cd to directory with <i>.pod</i> files, and do like this 

 <pre>
        cd f:/perllib/lib/pod
        pod2html
</pre> 

 After this you can direct your browser the file <i>perl.html</i> in this directory, and go ahead with reading docs, like this: 

 <pre>
        explore file:///f:/perllib/lib/pod/perl.html
</pre> 

 Alternatively you may be able to get these docs prebuilt from <font SIZE="-1">CPAN.</font>

<h3><font SIZE="-1">GNU</font> info files</h3>

 Users of Emacs would appreciate it very much, especially with <tt>&quot;CPerl&quot;</tt> mode loaded. You need to get latest <tt>&quot;pod2texi&quot;</tt> from <tt>&quot;CPAN&quot;</tt>, or, alternately, the prebuilt info pages.

<h3><i></i><font SIZE="-1"><i>PDF</i></font><i></i> files</h3>

 for <tt>&quot;Acrobat&quot;</tt> are available on <font SIZE="-1">CPAN</font> (may be for slightly older version of perl).

<h3>LaTeX docs</h3>

 can be constructed using <tt>&quot;pod2latex&quot;</tt>.

<h2>BUILD</h2>

 Here we discuss how to build Perl under <font SIZE="-1">OS/2.</font>

<h3>The short story</h3>

 Assume that you are a seasoned porter, so are sure that all the necessary tools are already present on your system, and you know how to get the Perl source distribution. Untar it, change to the extract directory, and 

 <pre>
  gnupatch -p0 &lt; os2\diff.configure
  sh Configure -des -D prefix=f:/perllib
  make
  make test
  make install
  make aout_test
  make aout_install
</pre> 

 This puts the executables in f:/perllib/bin. Manually move them to the <tt>&quot;PATH&quot;</tt>, manually move the built <i>perl*.dll</i> to <tt>&quot;LIBPATH&quot;</tt> (here for Perl <font SIZE="-1">DLL</font> <i>*</i> is a not-very-meaningful hex checksum), and run 

 <pre>
  make installcmd INSTALLCMDDIR=d:/ir/on/path
</pre> 

 Assuming that the <tt>&quot;man&quot;</tt>-files were put on an appropriate location, this completes the installation of minimal Perl system. (The binary distribution contains also a lot of additional modules, and the documentation in <font SIZE="-1">INF</font> format.) 

 What follows is a detailed guide through these steps.

<h3>Prerequisites</h3>

 You need to have the latest <font SIZE="-1">EMX</font> development environment, the full <font SIZE="-1">GNU</font> tool suite (gawk renamed to awk, and <font SIZE="-1">GNU</font> <i>find.exe</i> earlier on path than the <font SIZE="-1">OS/2</font> <i>find.exe</i>, same with <i>sort.exe</i>, to check use 

 <pre>
  find --version
  sort --version
</pre> 

 ). You need the latest version of <i>pdksh</i> installed as <i>sh.exe</i>. 

 Check that you have <font SIZE="-1"><b>BSD</b></font> libraries and headers installed, and - optionally - Berkeley <font SIZE="-1">DB</font> headers and libraries, and crypt. 

 Possible locations to get the files: 

 <pre>
  <a HREF="ftp://ftp.uni-heidelberg.de/pub/os2/unix/">ftp://ftp.uni-heidelberg.de/pub/os2/unix/</a>
  <a rel="nofollow" HREF="http://hobbes.nmsu.edu/h-browse.php?dir=/pub/os2">http://hobbes.nmsu.edu/h-browse.php?dir=/pub/os2</a>
  <a rel="nofollow" HREF="http://cd.textfiles.com/hobbesos29804/disk1/DEV32/">http://cd.textfiles.com/hobbesos29804/disk1/DEV32/</a>
  <a rel="nofollow" HREF="http://cd.textfiles.com/hobbesos29804/disk1/EMX09C/">http://cd.textfiles.com/hobbesos29804/disk1/EMX09C/</a>
</pre> 

 It is reported that the following archives contain enough utils to build perl: <i>gnufutil.zip</i>, <i>gnusutil.zip</i>, <i>gnututil.zip</i>, <i>gnused.zip</i>, <i>gnupatch.zip</i>, <i>gnuawk.zip</i>, <i>gnumake.zip</i>, <i>gnugrep.zip</i>, <i>bsddev.zip</i> and <i>ksh527rt.zip</i> (or a later version). Note that all these utilities are known to be available from <font SIZE="-1">LEO:</font> 

 <pre>
  <a HREF="ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/">ftp://crydee.sai.msu.ru/pub/comp/os/os2/leo/gnu/</a>
</pre> 

 Note also that the <i>db.lib</i> and <i>db.a</i> from the <font SIZE="-1">EMX</font> distribution are not suitable for multi-threaded compile (even single-threaded flavor of Perl uses multi-threaded C <font SIZE="-1">RTL,</font> for compatibility with XFree86-OS/2). Get a corrected one from 

 <pre>
  <a rel="nofollow" HREF="http://www.ilyaz.org/software/os2/db_mt.zip">http://www.ilyaz.org/software/os2/db_mt.zip</a>
</pre> 

 If you have <i>exactly the same version of Perl</i> installed already, make sure that no copies or perl are currently running. Later steps of the build may fail since an older version of <i>perl.dll</i> loaded into memory may be found. Running <tt>&quot;make test&quot;</tt> becomes meaningless, since the test are checking a previous build of perl (this situation is detected and reported by <i>os2/os2_base.t</i> test). Do not forget to unset <tt>&quot;PERL_EMXLOAD_SEC&quot;</tt> in environment. 

 Also make sure that you have <i>/tmp</i> directory on the current drive, and <i>.</i> directory in your <tt>&quot;LIBPATH&quot;</tt>. One may try to correct the latter condition by 

 <pre>
  set BEGINLIBPATH .\.
</pre> 

 if you use something like <i></i><font SIZE="-1"><i>CMD.EXE</i></font><i></i> or latest versions of <i>4os2.exe</i>. (Setting <font SIZE="-1">BEGINLIBPATH</font> to just <tt>&quot;.&quot;</tt> is ignored by the <font SIZE="-1">OS/2</font> kernel.) 

 Make sure your gcc is good for <tt>&quot;-Zomf&quot;</tt> linking: run <tt>&quot;omflibs&quot;</tt> script in <i>/emx/lib</i> directory. 

 Check that you have link386 installed. It comes standard with <font SIZE="-1">OS/2,</font> but may be not installed due to customization. If typing 

 <pre>
  link386
</pre> 

 shows you do not have it, do <i>Selective install</i>, and choose <tt>&quot;Link object modules&quot;</tt> in <i>Optional system utilities/More</i>. If you get into link386 prompts, press <tt>&quot;Ctrl-C&quot;</tt> to exit.

<h3>Getting perl source</h3>

 You need to fetch the latest perl source (including developers releases). With some probability it is located in 

 <pre>
  <a rel="nofollow" HREF="http://www.cpan.org/src/">http://www.cpan.org/src/</a>
  <a rel="nofollow" HREF="http://www.cpan.org/src/unsupported">http://www.cpan.org/src/unsupported</a>
</pre> 

 If not, you may need to dig in the indices to find it in the directory of the current maintainer. 

 Quick cycle of developers release may break the <font SIZE="-1">OS/2</font> build time to time, looking into 

 <pre>
  <a rel="nofollow" HREF="http://www.cpan.org/ports/os2/">http://www.cpan.org/ports/os2/</a>
</pre> 

 may indicate the latest release which was publicly released by the maintainer. Note that the release may include some additional patches to apply to the current source of perl. 

 Extract it like this 

 <pre>
  tar vzxf perl5.00409.tar.gz
</pre> 

 You may see a message about errors while extracting <i>Configure</i>. This is because there is a conflict with a similarly-named file <i>configure</i>. 

 Change to the directory of extraction.

<h3>Application of the patches</h3>

 You need to apply the patches in <i>./os2/diff.*</i> like this: 

 <pre>
  gnupatch -p0 &lt; os2\diff.configure
</pre> 

 You may also need to apply the patches supplied with the binary distribution of perl. It also makes sense to look on the perl5-porters mailing list for the latest OS/2-related patches (see &lt;<a rel="nofollow" HREF="http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/">http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/</a>&gt;). Such patches usually contain strings <tt>&quot;/os2/&quot;</tt> and <tt>&quot;patch&quot;</tt>, so it makes sense looking for these strings.

<h3>Hand-editing</h3>

 You may look into the file <i>./hints/os2.sh</i> and correct anything wrong you find there. I do not expect it is needed anywhere.

<h3>Making</h3>

 <pre>
  sh Configure -des -D prefix=f:/perllib
</pre> 

 <tt>&quot;prefix&quot;</tt> means: where to install the resulting perl library. Giving correct prefix you may avoid the need to specify <tt>&quot;PERLLIB_PREFIX&quot;</tt>, see &quot;<tt>&quot;PERLLIB_PREFIX&quot;</tt>&quot;. 

 <i>Ignore the message about missing </i>&quot;ln&quot;<i>, and about </i>&quot;-c&quot;<i> option to tr</i>. The latter is most probably already fixed, if you see it and can trace where the latter spurious warning comes from, please inform me. 

 Now 

 <pre>
  make
</pre> 

 At some moment the built may die, reporting a <i>version mismatch</i> or <i>unable to run perl</i>. This means that you do not have <i>.</i> in your <font SIZE="-1">LIBPATH,</font> so <i>perl.exe</i> cannot find the needed <i>perl67B2.dll</i> (treat these hex digits as line noise). After this is fixed the build should finish without a lot of fuss.

<h3>Testing</h3>

 Now run 

 <pre>
  make test
</pre> 

 All tests should succeed (with some of them skipped). If you have the same version of Perl installed, it is crucial that you have <tt>&quot;.&quot;</tt> early in your <font SIZE="-1">LIBPATH</font> (or in <font SIZE="-1">BEGINLIBPATH</font>), otherwise your tests will most probably test the wrong version of Perl. 

 Some tests may generate extra messages similar to
<dl>
<dt>A lot of &quot;bad free&quot;
<dd> in database tests related to Berkeley <font SIZE="-1">DB.</font> <i>This should be fixed already.</i> If it persists, you may disable this warnings, see &quot;<tt>&quot;PERL_BADFREE&quot;</tt>&quot;.
<dt>Process terminated by <font SIZE="-1">SIGTERM/SIGINT</font>
<dd> This is a standard message issued by <font SIZE="-1">OS/2</font> applications. *nix applications die in silence. It is considered to be a feature. One can easily disable this by appropriate sighandlers. 

 However the test engine bleeds these message to screen in unexpected moments. Two messages of this kind <i>should</i> be present during testing.</dl>
 

 To get finer test reports, call 

 <pre>
  perl t/harness
</pre> 

 The report with <i>io/pipe.t</i> failing may look like this: 

 <pre><code>
Failed Test Status Wstat Total Fail Failed List of failed-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --io / pipe.t 12 1 8.33 % 9 7 tests skipped, plus 56 subtests skipped.Failed 1 / 195 test scripts, 99.49 % okay.1 / 6542 subtests failed,
    99.98 % okay.
</code></pre> 

 The reasons for most important skipped tests are:
<dl>
<dt><i>op/fs.t</i>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>18
<dd> Checks <tt>&quot;atime&quot;</tt> and <tt>&quot;mtime&quot;</tt> of <tt>&quot;stat()&quot;</tt> - unfortunately, <font SIZE="-1">HPFS</font> provides only 2sec time granularity (for compatibility with <font SIZE="-1">FAT</font>?).
<dt>25
<dd> Checks <tt>&quot;truncate()&quot;</tt> on a filehandle just opened for write - I do not know why this should or should not work.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt><i>op/stat.t</i>
<dd> Checks <tt>&quot;stat()&quot;</tt>. Tests:
<dl>
<dt>
<dd>
<dl>
<dt>4
<dd> Checks <tt>&quot;atime&quot;</tt> and <tt>&quot;mtime&quot;</tt> of <tt>&quot;stat()&quot;</tt> - unfortunately, <font SIZE="-1">HPFS</font> provides only 2sec time granularity (for compatibility with <font SIZE="-1">FAT</font>?).</dl>
</dl>

<dl>
<dt>
<dd></dl>
</dl>

<h3>Installing the built perl</h3>

 If you haven't yet moved <tt>&quot;perl*.dll&quot;</tt> onto <font SIZE="-1">LIBPATH,</font> do it now. 

 Run 

 <pre>
  make install
</pre> 

 It would put the generated files into needed locations. Manually put <i>perl.exe</i>, <i>perl__.exe</i> and <i>perl___.exe</i> to a location on your <font SIZE="-1">PATH,</font> <i>perl.dll</i> to a location on your <font SIZE="-1">LIBPATH.</font> 

 Run 

 <pre>
  make installcmd INSTALLCMDDIR=d:/ir/on/path
</pre> 

 to convert perl utilities to <i>.cmd</i> files and put them on <font SIZE="-1">PATH.</font> You need to put <i>.EXE</i>-utilities on path manually. They are installed in <tt>&quot;$prefix/bin&quot;</tt>, here <tt>$prefix</tt> is what you gave to <i>Configure</i>, see ``Making''. 

 If you use <tt>&quot;man&quot;</tt>, either move the installed <i>*/man/</i> directories to your <tt>&quot;MANPATH&quot;</tt>, or modify <tt>&quot;MANPATH&quot;</tt> to match the location. (One could have avoided this by providing a correct <tt>&quot;manpath&quot;</tt> option to <i>./Configure</i>, or editing <i>./config.sh</i> between configuring and making steps.)

<h3>a.out-style build</h3>

 Proceed as above, but make <i>perl_.exe</i> (see &quot;<i>perl_.exe</i>&quot;) by 

 <pre>
  make perl_
</pre> 

 test and install by 

 <pre>
  make aout_test
  make aout_install
</pre> 

 Manually put <i>perl_.exe</i> to a location on your <font SIZE="-1">PATH.</font> 

 <b>Note.</b> The build process for <tt>&quot;perl_&quot;</tt> <i>does not know</i> about all the dependencies, so you should make sure that anything is up-to-date, say, by doing 

 <pre>
  make perl_dll
</pre> 

 first.

<h2>Building a binary distribution</h2>

 [This section provides a short overview only...] 

 Building should proceed differently depending on whether the version of perl you install is already present and used on your system, or is a new version not yet used. The description below assumes that the version is new, so installing its DLLs and <i>.pm</i> files will not disrupt the operation of your system even if some intermediate steps are not yet fully working. 

 The other cases require a little bit more convoluted procedures. Below I suppose that the current version of Perl is <tt>5.8.2</tt>, so the executables are named accordingly.
<dl>
<dt>1.
<dd> Fully build and test the Perl distribution. Make sure that no tests are failing with <tt>&quot;test&quot;</tt> and <tt>&quot;aout_test&quot;</tt> targets; fix the bugs in Perl and the Perl test suite detected by these tests. Make sure that <tt>&quot;all_test&quot;</tt> make target runs as clean as possible. Check that <i>os2/perlrexx.cmd</i> runs fine.
<dt>2.
<dd> Fully install Perl, including <tt>&quot;installcmd&quot;</tt> target. Copy the generated DLLs to <tt>&quot;LIBPATH&quot;</tt>; copy the numbered Perl executables (as in <i>perl5.8.2.exe</i>) to <tt>&quot;PATH&quot;</tt>; copy <tt>&quot;perl_.exe&quot;</tt> to <tt>&quot;PATH&quot;</tt> as <tt>&quot;perl_5.8.2.exe&quot;</tt>. Think whether you need backward-compatibility DLLs. In most cases you do not need to install them yet; but sometime this may simplify the following steps.
<dt>3.
<dd> Make sure that <tt>&quot;CPAN.pm&quot;</tt> can download files from <font SIZE="-1">CPAN.</font> If not, you may need to manually install <tt>&quot;Net::FTP&quot;</tt>.
<dt>4.
<dd> Install the bundle <tt>&quot;Bundle::OS2_default&quot;</tt> 

 <pre>
 perl5.8.2 -MCPAN -e &quot;install Bundle::OS2_default&quot; &lt; nul |&amp; tee 00cpan_i_1
</pre> 

 This may take a couple of hours on 1GHz processor (when run the first time). And this should not be necessarily a smooth procedure. Some modules may not specify required dependencies, so one may need to repeat this procedure several times until the results stabilize. 

 <pre>
 perl5.8.2 -MCPAN -e &quot;install Bundle::OS2_default&quot; &lt; nul |&amp; tee 00cpan_i_2
 perl5.8.2 -MCPAN -e &quot;install Bundle::OS2_default&quot; &lt; nul |&amp; tee 00cpan_i_3
</pre> 

 Even after they stabilize, some tests may fail. 

 Fix as many discovered bugs as possible. Document all the bugs which are not fixed, and all the failures with unknown reasons. Inspect the produced logs <i>00cpan_i_1</i> to find suspiciously skipped tests, and other fishy events. 

 Keep in mind that <i>installation</i> of some modules may fail too: for example, the DLLs to update may be already loaded by <i></i><font SIZE="-1"><i>CPAN</i></font><i>.pm</i>. Inspect the <tt>&quot;install&quot;</tt> logs (in the example above <i>00cpan_i_1</i> etc) for errors, and install things manually, as in 

 <pre>
  cd $CPANHOME/.cpan/build/Digest-MD5-2.31
  make install
</pre> 

 Some distributions may fail some tests, but you may want to install them anyway (as above, or via <tt>&quot;force install&quot;</tt> command of <tt>&quot;CPAN.pm&quot;</tt> shell-mode). 

 Since this procedure may take quite a long time to complete, it makes sense to ``freeze'' your <font SIZE="-1">CPAN</font> configuration by disabling periodic updates of the local copy of <font SIZE="-1">CPAN</font> index: set <tt>&quot;index_expire&quot;</tt> to some big value (I use 365), then save the settings 

 <pre>
  CPAN&gt; o conf index_expire 365
  CPAN&gt; o conf commit
</pre> 

 Reset back to the default value <tt>1</tt> when you are finished.
<dt>5.
<dd> When satisfied with the results, rerun the <tt>&quot;installcmd&quot;</tt> target. Now you can copy <tt>&quot;perl5.8.2.exe&quot;</tt> to <tt>&quot;perl.exe&quot;</tt>, and install the other OMF-build executables: <tt>&quot;perl__.exe&quot;</tt> etc. They are ready to be used.
<dt>6.
<dd> Change to the <tt>&quot;./pod&quot;</tt> directory of the build tree, download the Perl logo <i>CamelGrayBig.BMP</i>, and run 

 <pre>
  ( perl2ipf &gt; perl.ipf ) |&amp; tee 00ipf
  ipfc /INF perl.ipf |&amp; tee 00inf
</pre> 

 This produces the Perl docs online book <tt>&quot;perl.INF&quot;</tt>. Install in on <tt>&quot;BOOKSHELF&quot;</tt> path.
<dt>7.
<dd> Now is the time to build statically linked executable <i>perl_.exe</i> which includes newly-installed via <tt>&quot;Bundle::OS2_default&quot;</tt> modules. Doing testing via <tt>&quot;CPAN.pm&quot;</tt> is going to be painfully slow, since it statically links a new executable per <font SIZE="-1">XS</font> extension. 

 Here is a possible workaround: create a toplevel <i>Makefile.PL</i> in <i></i>$CPANHOME<i>/.cpan/build/</i> with contents being (compare with ``Making executables with a custom collection of statically loaded extensions'') 

 <pre>
  use ExtUtils::MakeMaker;
  WriteMakefile NAME =&gt; 'dummy';
</pre> 

 execute this as 

 <pre>
  perl_5.8.2.exe Makefile.PL &lt;nul |&amp; tee 00aout_c1
  make -k all test &lt;nul |&amp; 00aout_t1
</pre> 

 Again, this procedure should not be absolutely smooth. Some <tt>&quot;Makefile.PL&quot;</tt>'s in subdirectories may be buggy, and would not run as ``child'' scripts. The interdependency of modules can strike you; however, since non-XS modules are already installed, the prerequisites of most modules have a very good chance to be present. 

 If you discover some glitches, move directories of problematic modules to a different location; if these modules are non-XS modules, you may just ignore them - they are already installed; the remaining, <font SIZE="-1">XS,</font> modules you need to install manually one by one. 

 After each such removal you need to rerun the <tt>&quot;Makefile.PL&quot;</tt>/<tt>&quot;make&quot;</tt> process; usually this procedure converges soon. (But be sure to convert all the necessary external C libraries from <i>.lib</i> format to <i>.a</i> format: run one of 

 <pre>
  emxaout foo.lib
  emximp -o foo.a foo.lib
</pre> 

 whichever is appropriate.) Also, make sure that the DLLs for external libraries are usable with with executables compiled without <tt>&quot;-Zmtd&quot;</tt> options. 

 When you are sure that only a few subdirectories lead to failures, you may want to add <tt>&quot;-j4&quot;</tt> option to <tt>&quot;make&quot;</tt> to speed up skipping subdirectories with already finished build. 

 When you are satisfied with the results of tests, install the build C libraries for extensions: 

 <pre>
  make install |&amp; tee 00aout_i
</pre> 

 Now you can rename the file <i>./perl.exe</i> generated during the last phase to <i>perl_5.8.2.exe</i>; place it on <tt>&quot;PATH&quot;</tt>; if there is an inter-dependency between some <font SIZE="-1">XS</font> modules, you may need to repeat the <tt>&quot;test&quot;</tt>/<tt>&quot;install&quot;</tt> loop with this new executable and some excluded modules - until the procedure converges. 

 Now you have all the necessary <i>.a</i> libraries for these Perl modules in the places where Perl builder can find it. Use the perl builder: change to an empty directory, create a ``dummy'' <i>Makefile.PL</i> again, and run 

 <pre>
  perl_5.8.2.exe Makefile.PL |&amp; tee 00c
  make perl                  |&amp; tee 00p
</pre> 

 This should create an executable <i>./perl.exe</i> with all the statically loaded extensions built in. Compare the generated <i>perlmain.c</i> files to make sure that during the iterations the number of loaded extensions only increases. Rename <i>./perl.exe</i> to <i>perl_5.8.2.exe</i> on <tt>&quot;PATH&quot;</tt>. 

 When it converges, you got a functional variant of <i>perl_5.8.2.exe</i>; copy it to <tt>&quot;perl_.exe&quot;</tt>. You are done with generation of the local Perl installation.
<dt>8.
<dd> Make sure that the installed modules are actually installed in the location of the new Perl, and are not inherited from entries of <tt>@INC</tt> given for inheritance from the older versions of Perl: set <tt>&quot;PERLLIB_582_PREFIX&quot;</tt> to redirect the new version of Perl to a new location, and copy the installed files to this new location. Redo the tests to make sure that the versions of modules inherited from older versions of Perl are not needed. 

 Actually, the log output of <b><a HREF="/docs/linux/man/1-pod2ipf/">pod2ipf</a></b>(1) during the step 6 gives a very detailed info about which modules are loaded from which place; so you may use it as an additional verification tool. 

 Check that some temporary files did not make into the perl install tree. Run something like this 

 <pre>
  pfind . -f &quot;!(/\.(pm|pl|ix|al|h|a|lib|txt|pod|imp|bs|dll|ld|bs|inc|xbm|yml|cgi|uu|e2x|skip|packlist|eg|cfg|html|pub|enc|all|ini|po|pot)$/i or /^\w+$/&quot;) | less
</pre> 

 in the install tree (both top one and <i>sitelib</i> one). 

 Compress all the DLLs with <i>lxlite</i>. The tiny <i>.exe</i> can be compressed with <tt>&quot;/c:max&quot;</tt> (the bug only appears when there is a fixup in the last 6 bytes of a page (?); since the tiny executables are much smaller than a page, the bug will not hit). Do not compress <tt>&quot;perl_.exe&quot;</tt> - it would not work under <font SIZE="-1">DOS.</font>
<dt>9.
<dd> Now you can generate the binary distribution. This is done by running the test of the <font SIZE="-1">CPAN</font> distribution <tt>&quot;OS2::SoftInstaller&quot;</tt>. Tune up the file <i>test.pl</i> to suit the layout of current version of Perl first. Do not forget to pack the necessary external DLLs accordingly. Include the description of the bugs and test suite failures you could not fix. Include the small-stack versions of Perl executables from Perl build directory. 

 Include <i>perl5.def</i> so that people can relink the perl <font SIZE="-1">DLL</font> preserving the binary compatibility, or can create compatibility DLLs. Include the diff files (<tt>&quot;diff -pu old new&quot;</tt>) of fixes you did so that people can rebuild your version. Include <i>perl5.map</i> so that one can use remote debugging.
<dt>10.
<dd> Share what you did with the other people. Relax. Enjoy fruits of your work.
<dt>11.
<dd> Brace yourself for thanks, bug reports, hate mail and spam coming as result of the previous step. No good deed should remain unpunished!</dl>

<h2>Building custom <i>.EXE</i> files</h2>

 The Perl executables can be easily rebuilt at any moment. Moreover, one can use the <i>embedding</i> interface (see perlembed) to make very customized executables.

<h3>Making executables with a custom collection of statically loaded extensions</h3>

 It is a little bit easier to do so while <i>decreasing</i> the list of statically loaded extensions. We discuss this case only here.
<dl>
<dt>1.
<dd> Change to an empty directory, and create a placeholder &lt;Makefile.PL&gt;: 

 <pre>
  use ExtUtils::MakeMaker;
  WriteMakefile NAME =&gt; 'dummy';
</pre>
<dt>2.
<dd> Run it with the flavor of Perl (<i>perl.exe</i> or <i>perl_.exe</i>) you want to rebuild. 

 <pre>
  perl_ Makefile.PL
</pre>
<dt>3.
<dd> Ask it to create new Perl executable: 

 <pre>
  make perl
</pre> 

 (you may need to manually add <tt>&quot;PERLTYPE=-DPERL_CORE&quot;</tt> to this commandline on some versions of Perl; the symptom is that the command-line globbing does not work from <font SIZE="-1">OS/2</font> shells with the newly-compiled executable; check with 

 <pre>
  .\perl.exe -wle &quot;print for @ARGV&quot; *
</pre> 

 ).
<dt>4.
<dd> The previous step created <i>perlmain.c</i> which contains a list of <b>newXS()</b> calls near the end. Removing unnecessary calls, and rerunning 

 <pre>
  make perl
</pre> 

 will produce a customized executable.</dl>

<h3>Making executables with a custom search-paths</h3>

 The default perl executable is flexible enough to support most usages. However, one may want something yet more flexible; for example, one may want to find Perl <font SIZE="-1">DLL</font> relatively to the location of the <font SIZE="-1">EXE</font> file; or one may want to ignore the environment when setting the Perl-library search patch, etc. 

 If you fill comfortable with <i>embedding</i> interface (see perlembed), such things are easy to do repeating the steps outlined in L/&lt;Making executables with a custom collection of statically loaded extensions&gt;, and doing more comprehensive edits to <b>main()</b> of <i>perlmain.c</i>. The people with little desire to understand Perl can just rename <b>main()</b>, and do necessary modification in a custom <b>main()</b> which calls the renamed function in appropriate time. 

 However, there is a third way: perl <font SIZE="-1">DLL</font> exports the <b>main()</b> function and several callbacks to customize the search path. Below is a complete example of a ``Perl loader'' which
<dl>
<dt>1.
<dd> Looks for Perl <font SIZE="-1">DLL</font> in the directory <tt>&quot;$exedir/../dll&quot;</tt>;
<dt>2.
<dd> Prepends the above directory to <tt>&quot;BEGINLIBPATH&quot;</tt>;
<dt>3.
<dd> Fails if the Perl <font SIZE="-1">DLL</font> found via <tt>&quot;BEGINLIBPATH&quot;</tt> is different from what was loaded on step 1; e.g., another process could have loaded it from <tt>&quot;LIBPATH&quot;</tt> or from a different value of <tt>&quot;BEGINLIBPATH&quot;</tt>. In these cases one needs to modify the setting of the system so that this other process either does not run, or loads the <font SIZE="-1">DLL</font> from <tt>&quot;BEGINLIBPATH&quot;</tt> with <tt>&quot;LIBPATHSTRICT=T&quot;</tt> (available with kernels after September 2000).
<dt>4.
<dd> Loads Perl library from <tt>&quot;$exedir/../dll/lib/&quot;</tt>.
<dt>5.
<dd> Uses Bourne shell from <tt>&quot;$exedir/../dll/sh/ksh.exe&quot;</tt>.</dl>
 

 For best results compile the C file below with the same options as the Perl <font SIZE="-1">DLL.</font> However, a lot of functionality will work even if the executable is not an <font SIZE="-1">EMX</font> applications, e.g., if compiled with 

 <pre>
  gcc -Wall -DDOSISH -DOS2=1 -O2 -s -Zomf -Zsys perl-starter.c \
    -DPERL_DLL_BASENAME=\&quot;perl312F\&quot; -Zstack 8192 -Zlinker /PM:VIO
</pre> 

 Here is the sample C file: 

 
#define INCL_DOS
#define INCL_NOPM
/* These are needed for compile if os2.h includes os2tk.h, not
 * os2emx.h */
#define INCL_DOSPROCESS
#include "EXTERN.h"
#include &lt;os2.h&gt;
#define PERL_IN_MINIPERLMAIN_C
#include "perl.h"
static char *me;
HMODULE handle;
static void
die_with(char *msg1, char *msg2, char *msg3, char *msg4)
{
    ULONG c;
    char *s = " error: ";
    DosWrite(2, me, strlen(me), &amp;c);
    DosWrite(2, s, strlen(s), &amp;c);
    DosWrite(2, msg1, strlen(msg1), &amp;c);
    DosWrite(2, msg2, strlen(msg2), &amp;c);
    DosWrite(2, msg3, strlen(msg3), &amp;c);
    DosWrite(2, msg4, strlen(msg4), &amp;c);
    DosWrite(2, "\r\n", 2, &amp;c);
    exit(255);
}
typedef ULONG (*fill_extLibpath_t)(int type,
                                   char *pre,
                                   char *post,
                                   int replace,
                                   char *msg);
typedef int (*main_t)(int type, char *argv[], char *env[]);
typedef int (*handler_t)(void *data, int which);
#ifndef PERL_DLL_BASENAME
#define PERL_DLL_BASENAME "perl"
#endif
static HMODULE
load_perl_dll(char *basename)
{
    char buf[300], fail[260];
    STRLEN l, dirl;
    fill_extLibpath_t f;
    ULONG rc_fullname;
    HMODULE handle, handle1;
    if (_execname(buf, sizeof(buf) - 13) != 0)
        die_with("Can't find full path: ", strerror(errno), "", "");
    /* XXXX Fill 'me' with new value */
    l = strlen(buf);
    while (l &amp;&amp; buf[l - 1] != '/' &amp;&amp; buf[l - 1] != '\\')
        l--;
    dirl = l - 1;
    strcpy(buf + l, basename);
    l += strlen(basename);
    strcpy(buf + l, ".dll");
    if ((rc_fullname = DosLoadModule(fail, sizeof fail, buf, &amp;handle)) != 0 &amp;&amp; DosLoadModule(fail, sizeof fail, basename, &amp;handle) != 0)
        die_with("Can't load DLL ", buf, "", "");
    if (rc_fullname)
        return handle; /* was loaded with short name; all is fine */
    if (DosQueryProcAddr(handle, 0, "fill_extLibpath", (PFN *)&amp;f))
        die_with(buf,
                 ": DLL exports no symbol ",
                 "fill_extLibpath",
                 "");
    buf[dirl] = 0;
    if (f(0 /*BEGINLIBPATH*/, buf /* prepend */, NULL /* append */,
          0 /* keep old value */, me))
        die_with(me, ": prepending BEGINLIBPATH", "", "");
    if (DosLoadModule(fail, sizeof fail, basename, &amp;handle1) != 0)
        die_with(me,
                 ": finding perl DLL again via BEGINLIBPATH",
                 "",
                 "");
    buf[dirl] = '\\';
    if (handle1 != handle) {
        if (DosQueryModuleName(handle1, sizeof(fail), fail))
            strcpy(fail, "???");
         die_with(buf,
                  ":\n\tperl DLL via BEGINLIBPATH is different: \n\t",
                  fail,
                  "\n\tYou may need to manipulate global BEGINLIBPATH"
                     " and LIBPATHSTRICT"
                     "\n\tso that the other copy is loaded via"
                     BEGINLIBPATH.");
    }
    return handle;
}
int main(int argc, char **argv, char **env)
{
    main_t f;
    handler_t h;
    me = argv[0];
    /**/
    handle = load_perl_dll(PERL_DLL_BASENAME);
    if (DosQueryProcAddr(handle,
                         0,
                         "Perl_OS2_handler_install",
                         (PFN *)&amp;h))
        die_with(PERL_DLL_BASENAME,
                 ": DLL exports no symbol ",
                 "Perl_OS2_handler_install",
                 "");
    if (!h((void *)"~installprefix", Perlos2_handler_perllib_from) || !h((void *)"~dll", Perlos2_handler_perllib_to) || !h((void *)"~dll/sh/ksh.exe", Perlos2_handler_perl_sh))
        die_with(PERL_DLL_BASENAME,
                 ": Can't install @INC manglers",
                 "",
                 "");
    if (DosQueryProcAddr(handle, 0, "dll_perlmain", (PFN *)&amp;f))
        die_with(PERL_DLL_BASENAME,
                 ": DLL exports no symbol ",
                 "dll_perlmain",
                 "");
    return f(argc, argv, env);
}


<h2>Build FAQ</h2>

<h3>Some / became \ in pdksh.</h3>

 You have a very old pdksh. See ``Prerequisites''.

<h3>'errno' - unresolved external</h3>

 You do not have MT-safe <i>db.lib</i>. See ``Prerequisites''.

<h3>Problems with tr or sed</h3>

 reported with very old version of tr and sed.

<h3>Some problem (forget which ;-)</h3>

 You have an older version of <i>perl.dll</i> on your <font SIZE="-1">LIBPATH,</font> which broke the build of extensions.

<h3>Library ... not found</h3>

 You did not run <tt>&quot;omflibs&quot;</tt>. See ``Prerequisites''.

<h3>Segfault in make</h3>

 You use an old version of <font SIZE="-1">GNU</font> make. See ``Prerequisites''.

<h3>op/sprintf test failure</h3>

 This can result from a bug in emx sprintf which was fixed in 0.9d fix 03.

<h2>Specific (mis)features of OS/2 port</h2>

<h3>setpriority, getpriority</h3>

 Note that these functions are compatible with *nix, not with the older ports of '94 - 95. The priorities are absolute, go from 32 to -95, lower is quicker. 0 is the default priority. 

 <font SIZE="-1"><b>WARNING</b></font>. Calling <tt>&quot;getpriority&quot;</tt> on a non-existing process could lock the system before Warp3 fixpak22. Starting with Warp3, Perl will use a workaround: it aborts <b>getpriority()</b> if the process is not present. This is not possible on older versions <tt>&quot;2.*&quot;</tt>, and has a race condition anyway.

<h3>system()</h3>

 Multi-argument form of <tt>&quot;system()&quot;</tt> allows an additional numeric argument. The meaning of this argument is described in OS2::Process. 

 When finding a program to run, Perl first asks the <font SIZE="-1">OS</font> to look for executables on <tt>&quot;PATH&quot;</tt> (<font SIZE="-1">OS/2</font> adds extension <i>.exe</i> if no extension is present). If not found, it looks for a script with possible extensions added in this order: no extension, <i>.cmd</i>, <i>.btm</i>, <i>.bat</i>, <i>.pl</i>. If found, Perl checks the start of the file for magic strings <tt>&quot;#!&quot;</tt> and <tt>&quot;extproc &quot;</tt>. If found, Perl uses the rest of the first line as the beginning of the command line to run this script. The only mangling done to the first line is extraction of arguments (currently up to 3), and ignoring of the path-part of the ``interpreter'' name if it can't be found using the full path. 

 E.g., <tt>&quot;system 'foo', 'bar', 'baz'&quot;</tt> may lead Perl to finding <i>C:/emx/bin/foo.cmd</i> with the first line being 

 <pre>
 extproc /bin/bash    -x   -c
</pre> 

 If <i>/bin/bash.exe</i> is not found, then Perl looks for an executable <i>bash.exe</i> on <tt>&quot;PATH&quot;</tt>. If found in <i>C:/emx.add/bin/bash.exe</i>, then the above <b>system()</b> is translated to 

 <pre>
  system qw(C:/emx.add/bin/bash.exe -x -c C:/emx/bin/foo.cmd bar baz)
</pre> 

 One additional translation is performed: instead of <i>/bin/sh</i> Perl uses the hardwired-or-customized shell (see &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;). 

 The above search for ``interpreter'' is recursive: if <i>bash</i> executable is not found, but <i>bash.btm</i> is found, Perl will investigate its first line etc. The only hardwired limit on the recursion depth is implicit: there is a limit 4 on the number of additional arguments inserted before the actual arguments given to <b>system()</b>. In particular, if no additional arguments are specified on the ``magic'' first lines, then the limit on the depth is 4. 

 If Perl finds that the found executable is of <font SIZE="-1">PM</font> type when the current session is not, it will start the new process in a separate session of necessary type. Call via <tt>&quot;OS2::Process&quot;</tt> to disable this magic. 

 <font SIZE="-1"><b>WARNING</b></font>. Due to the described logic, you need to explicitly specify <i>.com</i> extension if needed. Moreover, if the executable <i>perl5.6.1</i> is requested, Perl will not look for <i>perl5.6.1.exe</i>. [This may change in the future.]

<h3>extproc on the first line</h3>

 If the first chars of a Perl script are <tt>&quot;extproc &quot;</tt>, this line is treated as <tt>&quot;#!&quot;</tt>-line, thus all the switches on this line are processed (twice if script was started via cmd.exe). See ``<font SIZE="-1">DESCRIPTION''</font> in perlrun.

<h3>Additional modules:</h3>

 OS2::Process, <font SIZE="-1">OS2::DLL</font>, <font SIZE="-1">OS2::REXX</font>, OS2::PrfDB, OS2::ExtAttr. These modules provide access to additional numeric argument for <tt>&quot;system&quot;</tt> and to the information about the running process, to DLLs having functions with <font SIZE="-1">REXX</font> signature and to the <font SIZE="-1">REXX</font> runtime, to <font SIZE="-1">OS/2</font> databases in the <i>.INI</i> format, and to Extended Attributes. 

 Two additional extensions by Andreas Kaiser, <tt>&quot;OS2::UPM&quot;</tt>, and <tt>&quot;OS2::FTP&quot;</tt>, are included into <tt>&quot;ILYAZ&quot;</tt> directory, mirrored on <font SIZE="-1">CPAN.</font> Other OS/2-related extensions are available too.

<h3>Prebuilt methods:</h3>

<dl>
<dt>&quot;File::Copy::syscopy&quot;
<dd> used by <tt>&quot;File::Copy::copy&quot;</tt>, see File::Copy.
<dt>&quot;DynaLoader::mod2fname&quot;
<dd> used by <tt>&quot;DynaLoader&quot;</tt> for <font SIZE="-1">DLL</font> name mangling.
<dt>&quot;Cwd::current_drive()&quot;
<dd> Self explanatory.
<dt>&quot;Cwd::sys_chdir(name)&quot;
<dd> leaves drive as it is.
<dt>&quot;Cwd::change_drive(name)&quot;
<dd> changes the ``current'' drive.
<dt>&quot;Cwd::sys_is_absolute(name)&quot;
<dd> means has drive letter and is_rooted.
<dt>&quot;Cwd::sys_is_rooted(name)&quot;
<dd> means has leading <tt>&quot;[/\\]&quot;</tt> (maybe after a drive-letter:).
<dt>&quot;Cwd::sys_is_relative(name)&quot;
<dd> means changes with current dir.
<dt>&quot;Cwd::sys_cwd(name)&quot;
<dd> Interface to cwd from <font SIZE="-1">EMX.</font> Used by <tt>&quot;Cwd::cwd&quot;</tt>.
<dt>&quot;Cwd::sys_abspath(name, dir)&quot;
<dd> Really really odious function to implement. Returns absolute name of file which would have <tt>&quot;name&quot;</tt> if <font SIZE="-1">CWD</font> were <tt>&quot;dir&quot;</tt>. <tt>&quot;Dir&quot;</tt> defaults to the current dir.
<dt>&quot;Cwd::extLibpath([type])&quot;
<dd> Get current value of extended library search path. If <tt>&quot;type&quot;</tt> is present and positive, works with <tt>&quot;END_LIBPATH&quot;</tt>, if negative, works with <tt>&quot;LIBPATHSTRICT&quot;</tt>, otherwise with <tt>&quot;BEGIN_LIBPATH&quot;</tt>.
<dt>&quot;Cwd::extLibpath_set( path [, type ] )&quot;
<dd> Set current value of extended library search path. If <tt>&quot;type&quot;</tt> is present and positive, works with &lt;<font SIZE="-1">END_LIBPATH</font>&gt;, if negative, works with <tt>&quot;LIBPATHSTRICT&quot;</tt>, otherwise with <tt>&quot;BEGIN_LIBPATH&quot;</tt>.
<dt>&quot;OS2::Error(do_harderror,do_exception)&quot;
<dd> Returns<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&quot;undef&quot;</tt> if it was not called yet, otherwise bit 1 is
 set if on the previous call do_harderror was enabled, bit 2 is set if on previous call do_exception was enabled. 

 This function enables/disables error popups associated with hardware errors (Disk not ready etc.) and software exceptions. 

 I know of no way to find out the state of popups <i>before</i> the first call to this function.
<dt>&quot;OS2::Errors2Drive(drive)&quot;
<dd> Returns <tt>&quot;undef&quot;</tt> if it was not called yet, otherwise return false if errors were not requested to be written to a hard drive, or the drive letter if this was requested. 

 This function may redirect error popups associated with hardware errors (Disk not ready etc.) and software exceptions to the file <font SIZE="-1">POPUPLOG.OS2</font> at the root directory of the specified drive. Overrides <b>OS2::Error()</b> specified by individual programs. Given argument undef will disable redirection. 

 Has global effect, persists after the application exits. 

 I know of no way to find out the state of redirection of popups to the disk <i>before</i> the first call to this function.
<dt><b>OS2::SysInfo()</b>
<dd> Returns a hash with system information. The keys of the hash are 

 <pre>
        MAX_PATH_LENGTH, MAX_TEXT_SESSIONS, MAX_PM_SESSIONS,
        MAX_VDM_SESSIONS, BOOT_DRIVE, DYN_PRI_VARIATION,
        MAX_WAIT, MIN_SLICE, MAX_SLICE, PAGE_SIZE,
        VERSION_MAJOR, VERSION_MINOR, VERSION_REVISION,
        MS_COUNT, TIME_LOW, TIME_HIGH, TOTPHYSMEM, TOTRESMEM,
        TOTAVAILMEM, MAXPRMEM, MAXSHMEM, TIMER_INTERVAL,
        MAX_COMP_LENGTH, FOREGROUND_FS_SESSION,
        FOREGROUND_PROCESS
</pre>
<dt><b>OS2::BootDrive()</b>
<dd> Returns a letter without colon.
<dt>&quot;OS2::MorphPM(serve)&quot;, &quot;OS2::UnMorphPM(serve)&quot;
<dd> Transforms the current application into a <font SIZE="-1">PM</font> application and back. The argument true means that a real message loop is going to be served. <b>OS2::MorphPM()</b> returns the <font SIZE="-1">PM</font> message queue handle as an integer. 

 See ``Centralized management of resources'' for additional details.
<dt>&quot;OS2::Serve_Messages(force)&quot;
<dd> Fake on-demand retrieval of outstanding <font SIZE="-1">PM</font> messages. If <tt>&quot;force&quot;</tt> is false, will not dispatch messages if a real message loop is known to be present. Returns number of messages retrieved. 

 Dies with ``QUITing...'' if <font SIZE="-1">WM_QUIT</font> message is obtained.
<dt>&quot;OS2::Process_Messages(force [, cnt])&quot;
<dd> Retrieval of <font SIZE="-1">PM</font> messages until window creation/destruction. If <tt>&quot;force&quot;</tt> is false, will not dispatch messages if a real message loop is known to be present. 

 Returns change in number of windows. If <tt>&quot;cnt&quot;</tt> is given, it is incremented by the number of messages retrieved. 

 Dies with ``QUITing...'' if <font SIZE="-1">WM_QUIT</font> message is obtained.
<dt>&quot;OS2::_control87(new,mask)&quot;
<dd> the same as <b><a HREF="/docs/linux/man/3-_control87/">_control87</a></b>(3) of <font SIZE="-1">EMX.</font> Takes integers as arguments, returns the previous coprocessor control word as an integer. Only bits in <tt>&quot;new&quot;</tt> which are present in <tt>&quot;mask&quot;</tt> are changed in the control word.
<dt><b>OS2::get_control87()</b>
<dd> gets the coprocessor control word as an integer.
<dt>&quot;OS2::set_control87_em(new=MCW_EM,mask=MCW_EM)&quot;
<dd> The variant of <b>OS2::_control87()</b> with default values good for handling exception mask: if no <tt>&quot;mask&quot;</tt>, uses exception mask part of <tt>&quot;new&quot;</tt> only. If no <tt>&quot;new&quot;</tt>, disables all the floating point exceptions. 

 See ``Misfeatures'' for details.
<dt>&quot;OS2::DLLname([how [, \&amp;xsub]])&quot;
<dd> Gives the information about the Perl <font SIZE="-1">DLL</font> or the <font SIZE="-1">DLL</font> containing the C function bound to by <tt>&amp;xsub</tt>. The meaning of <tt>&quot;how&quot;</tt> is: default (2): full name; 0: handle; 1: module name.</dl>
 

 (Note that some of these may be moved to different libraries - eventually).

<h3>Prebuilt variables:</h3>

<dl>
<dt>$OS2::emx_rev
<dd> numeric value is the same as _emx_rev of <font SIZE="-1">EMX,</font> a string value the same as _emx_vprt (similar to <tt>&quot;0.9c&quot;</tt>).
<dt>$OS2::emx_env
<dd> same as _emx_env of <font SIZE="-1">EMX,</font> a number similar to 0x8001.
<dt>$OS2::os_ver
<dd> a number <tt>&quot;OS_MAJOR + 0.001 * OS_MINOR&quot;</tt>.
<dt>$OS2::is_aout
<dd> true if the Perl library was compiled in <font SIZE="-1">AOUT</font> format.
<dt>$OS2::can_fork
<dd> true if the current executable is an <font SIZE="-1">AOUT EMX</font> executable, so Perl can fork. Do not use this, use the portable check for <tt>$Config::Config</tt>{dfork}.
<dt>$OS2::nsyserror
<dd> This variable (default is 1) controls whether to enforce the contents of $^E to start with <tt>&quot;SYS0003&quot;</tt>-like id. If set to 0, then the string value of $^E is what is available from the <font SIZE="-1">OS/2</font> message file. (Some messages in this file have an <tt>&quot;SYS0003&quot;</tt>-like id prepended, some not.)</dl>

<h3>Misfeatures</h3>

<dl>
<dt>&bull;
<dd> Since <b><a HREF="/docs/linux/man/3-flock/">flock</a></b>(3) is present in <font SIZE="-1">EMX,</font> but is not functional, it is emulated by perl. To disable the emulations, set environment variable <tt>&quot;USE_PERL_FLOCK=0&quot;</tt>.
<dt>&bull;
<dd> Here is the list of things which may be ``broken'' on <font SIZE="-1">EMX</font> (from <font SIZE="-1">EMX</font> docs):
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> The functions <b><a HREF="/docs/linux/man/3-recvmsg/">recvmsg</a></b>(3), <b><a HREF="/docs/linux/man/3-sendmsg/">sendmsg</a></b>(3), and <b><a HREF="/docs/linux/man/3-socketpair/">socketpair</a></b>(3) are not implemented.
<dt>&bull;
<dd> <b><a HREF="/docs/linux/man/3-sock_init/">sock_init</a></b>(3) is not required and not implemented.
<dt>&bull;
<dd> <b><a HREF="/docs/linux/man/3-flock/">flock</a></b>(3) is not yet implemented (dummy function). (Perl has a workaround.)
<dt>&bull;
<dd> <b><a HREF="/docs/linux/man/3-kill/">kill</a></b>(3): Special treatment of PID=0, PID=1 and PID=-1 is not implemented.
<dt>&bull;
<dd> <b><a HREF="/docs/linux/man/3-waitpid/">waitpid</a></b>(3): 

 <pre>
      WUNTRACED
              Not implemented.
      waitpid() is not implemented for negative values of PID.
</pre></dl>
</dl>

<dl>
<dt>
<dd> 

 Note that <tt>&quot;kill -9&quot;</tt> does not work with the current version of <font SIZE="-1">EMX.</font></dl>

<dt>&bull;
<dd> See ``Text-mode filehandles''.
<dt>&bull;
<dd> Unix-domain sockets on <font SIZE="-1">OS/2</font> live in a pseudo-file-system <tt>&quot;/sockets/...&quot;</tt>. To avoid a failure to create a socket with a name of a different form, <tt>&quot;/socket/&quot;</tt> is prepended to the socket name (unless it starts with this already). 

 This may lead to problems later in case the socket is accessed via the ``usual'' file-system calls using the ``initial'' name.
<dt>&bull;
<dd> Apparently, <font SIZE="-1">IBM</font> used a compiler (for some period of time around '95?) which changes <font SIZE="-1">FP</font> mask right and left. This is not <i>that</i> bad for <font SIZE="-1">IBM</font>'s programs, but the same compiler was used for DLLs which are used with general-purpose applications. When these DLLs are used, the state of floating-point flags in the application is not predictable. 

 What is much worse, some DLLs change the floating point flags when in <b>_DLLInitTerm()</b> (e.g., <i></i><font SIZE="-1"><i>TCP32IP</i></font><i></i>). This means that even if you do not <i>call</i> any function in the <font SIZE="-1">DLL,</font> just the act of loading this <font SIZE="-1">DLL</font> will reset your flags. What is worse, the same compiler was used to compile some <font SIZE="-1">HOOK</font> DLLs. Given that <font SIZE="-1">HOOK</font> dlls are executed in the context of <i>all</i> the applications in the system, this means a complete unpredictability of floating point flags on systems using such <font SIZE="-1">HOOK</font> DLLs. E.g., <i></i><font SIZE="-1"><i>GAMESRVR.DLL</i></font><i></i> of <font SIZE="-1"><b>DIVE</b></font> origin changes the floating point flags on each write to the <font SIZE="-1">TTY</font> of a <font SIZE="-1">VIO</font> (windowed text-mode) applications. 

 Some other (not completely debugged) situations when <font SIZE="-1">FP</font> flags change include some video drivers (?), and some operations related to creation of the windows. People who code <b>OpenGL</b> may have more experience on this. 

 Perl is generally used in the situation when all the floating-point exceptions are ignored, as is the default under <font SIZE="-1">EMX.</font> If they are not ignored, some benign Perl programs would get a <tt>&quot;SIGFPE&quot;</tt> and would die a horrible death. 

 To circumvent this, Perl uses two hacks. They help against <i>one</i> type of damage only: <font SIZE="-1">FP</font> flags changed when loading a <font SIZE="-1">DLL.</font> 

 One of the hacks is to disable floating point exceptions on Perl startup (as is the default with <font SIZE="-1">EMX</font>). This helps only with compile-time-linked DLLs changing the flags before <b>main()</b> had a chance to be called. 

 The other hack is to restore <font SIZE="-1">FP</font> flags after a call to <b>dlopen()</b>. This helps against similar damage done by DLLs <b>_DLLInitTerm()</b> at runtime. Currently no way to switch these hacks off is provided.</dl>

<h3>Modifications</h3>

 Perl modifies some standard C library calls in the following ways:
<dl>
<dt>&quot;popen&quot;
<dd> <tt>&quot;my_popen&quot;</tt> uses <i>sh.exe</i> if shell is required, cf. &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;.
<dt>&quot;tmpnam&quot;
<dd> is created using <tt>&quot;TMP&quot;</tt> or <tt>&quot;TEMP&quot;</tt> environment variable, via <tt>&quot;tempnam&quot;</tt>.
<dt>&quot;tmpfile&quot;
<dd> If the current directory is not writable, file is created using modified <tt>&quot;tmpnam&quot;</tt>, so there may be a race condition.
<dt>&quot;ctermid&quot;
<dd> a dummy implementation.
<dt>&quot;stat&quot;
<dd> <tt>&quot;os2_stat&quot;</tt> special-cases <i>/dev/tty</i> and <i>/dev/con</i>.
<dt>&quot;mkdir&quot;, &quot;rmdir&quot;
<dd> these <font SIZE="-1">EMX</font> functions do not work if the path contains a trailing <tt>&quot;/&quot;</tt>. Perl contains a workaround for this.
<dt>&quot;flock&quot;
<dd> Since <b><a HREF="/docs/linux/man/3-flock/">flock</a></b>(3) is present in <font SIZE="-1">EMX,</font> but is not functional, it is emulated by perl. To disable the emulations, set environment variable <tt>&quot;USE_PERL_FLOCK=0&quot;</tt>.</dl>

<h3>Identifying DLLs</h3>

 All the DLLs built with the current versions of Perl have <font SIZE="-1">ID</font> strings identifying the name of the extension, its version, and the version of Perl required for this <font SIZE="-1">DLL.</font> Run <tt>&quot;bldlevel DLL-name&quot;</tt> to find this info.

<h3>Centralized management of resources</h3>

 Since to call certain <font SIZE="-1">OS/2 API</font> one needs to have a correctly initialized <tt>&quot;Win&quot;</tt> subsystem, OS/2-specific extensions may require getting <tt>&quot;HAB&quot;</tt>s and <tt>&quot;HMQ&quot;</tt>s. If an extension would do it on its own, another extension could fail to initialize. 

 Perl provides a centralized management of these resources:
<dl>
<dt>&quot;HAB&quot;
<dd> To get the <font SIZE="-1">HAB,</font> the extension should call <tt>&quot;hab = perl_hab_GET()&quot;</tt> in C. After this call is performed, <tt>&quot;hab&quot;</tt> may be accessed as <tt>&quot;Perl_hab&quot;</tt>. There is no need to release the <font SIZE="-1">HAB</font> after it is used. 

 If by some reasons <i>perl.h</i> cannot be included, use 

 
extern int Perl_hab_GET(void);
 

 instead.
<dt>&quot;HMQ&quot;
<dd> There are two cases:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> the extension needs an <tt>&quot;HMQ&quot;</tt> only because some <font SIZE="-1">API</font> will not work otherwise. Use <tt>&quot;serve = 0&quot;</tt> below.
<dt>&bull;
<dd> the extension needs an <tt>&quot;HMQ&quot;</tt> since it wants to engage in a <font SIZE="-1">PM</font> event loop. Use <tt>&quot;serve = 1&quot;</tt> below.</dl>
</dl>

<dl>
<dt>
<dd> 

 To get an <tt>&quot;HMQ&quot;</tt>, the extension should call <tt>&quot;hmq = perl_hmq_GET(serve)&quot;</tt> in C. After this call is performed, <tt>&quot;hmq&quot;</tt> may be accessed as <tt>&quot;Perl_hmq&quot;</tt>. 

 To signal to Perl that <font SIZE="-1">HMQ</font> is not needed any more, call <tt>&quot;perl_hmq_UNSET(serve)&quot;</tt>. Perl process will automatically morph/unmorph itself into/from a <font SIZE="-1">PM</font> process if <font SIZE="-1">HMQ</font> is needed/not-needed. Perl will automatically enable/disable <tt>&quot;WM_QUIT&quot;</tt> message during shutdown if the message queue is served/not-served. 

 <font SIZE="-1"><b>NOTE</b></font>. If during a shutdown there is a message queue which did not disable <font SIZE="-1">WM_QUIT,</font> and which did not process the received <font SIZE="-1">WM_QUIT</font> message, the shutdown will be automatically cancelled. Do not call <tt><a HREF="/docs/linux/man/1-perl_hmq_get/">perl_hmq_GET</a>(1)</tt> unless you are going to process messages on an orderly basis.</dl>

<dt>Treating errors reported by <font SIZE="-1">OS/2 API</font>
<dd> There are two principal conventions (it is useful to call them <tt>&quot;Dos*&quot;</tt> and <tt>&quot;Win*&quot;</tt> - though this part of the function signature is not always determined by the name of the <font SIZE="-1">API</font>) of reporting the error conditions of <font SIZE="-1">OS/2 API.</font> Most of <tt>&quot;Dos*&quot;</tt> APIs report the error code as the result of the call (so 0 means success, and there are many types of errors). Most of <tt>&quot;Win*&quot;</tt> <font SIZE="-1">API</font> report success/fail via the result being <tt>&quot;TRUE&quot;</tt>/<tt>&quot;FALSE&quot;</tt>; to find the reason for the failure one should call <b>WinGetLastError()</b> <font SIZE="-1">API.</font> 

 Some <tt>&quot;Win*&quot;</tt> entry points also overload a ``meaningful'' return value with the error indicator; having a 0 return value indicates an error. Yet some other <tt>&quot;Win*&quot;</tt> entry points overload things even more, and 0 return value may mean a successful call returning a valid value 0, as well as an error condition; in the case of a 0 return value one should call <b>WinGetLastError()</b> <font SIZE="-1">API</font> to distinguish a successful call from a failing one. 

 By convention, all the calls to <font SIZE="-1">OS/2 API</font> should indicate their failures by resetting $^E. All the Perl-accessible functions which call <font SIZE="-1">OS/2 API</font> may be broken into two classes: some <b>die()</b>s when an <font SIZE="-1">API</font> error is encountered, the other report the error via a false return value (of course, this does not concern Perl-accessible functions which <i>expect</i> a failure of the <font SIZE="-1">OS/2 API</font> call, having some workarounds coded). 

 Obviously, in the situation of the last type of the signature of an <font SIZE="-1">OS/2 API,</font> it is must more convenient for the users if the failure is indicated by <b>die()</b>ing: one does not need to check $^E to know that something went wrong. If, however, this solution is not desirable by some reason, the code in question should reset $^E to 0 before making this <font SIZE="-1">OS/2 API</font> call, so that the caller of this Perl-accessible function has a chance to distinguish a success-but-0-return value from a failure. (One may return undef as an alternative way of reporting an error.) 

 The macros to simplify this type of error propagation are
<dl>
<dt>
<dd>
<dl>
<dt>&quot;CheckOSError(expr)&quot;
<dd> Returns true on error, sets $^E. Expects <b>expr()</b> be a call of <tt>&quot;Dos*&quot;</tt>-style <font SIZE="-1">API.</font>
<dt>&quot;CheckWinError(expr)&quot;
<dd> Returns true on error, sets $^E. Expects <b>expr()</b> be a call of <tt>&quot;Win*&quot;</tt>-style <font SIZE="-1">API.</font>
<dt>&quot;SaveWinError(expr)&quot;
<dd> Returns <tt>&quot;expr&quot;</tt>, sets $^E from <b>WinGetLastError()</b> if <tt>&quot;expr&quot;</tt> is false.
<dt>&quot;SaveCroakWinError(expr,die,name1,name2)&quot;
<dd> Returns <tt>&quot;expr&quot;</tt>, sets $^E from <b>WinGetLastError()</b> if <tt>&quot;expr&quot;</tt> is false, and <b>die()</b>s if <tt>&quot;die&quot;</tt> and $^E are true. The message to die is the concatenated strings <tt>&quot;name1&quot;</tt> and <tt>&quot;name2&quot;</tt>, separated by <tt>&quot;: &quot;</tt> from the contents of $^E.
<dt>&quot;WinError_2_Perl_rc&quot;
<dd> Sets <tt>&quot;Perl_rc&quot;</tt> to the return value of <b>WinGetLastError()</b>.
<dt>&quot;FillWinError&quot;
<dd> Sets <tt>&quot;Perl_rc&quot;</tt> to the return value of <b>WinGetLastError()</b>, and sets $^E to the corresponding value.
<dt>&quot;FillOSError(rc)&quot;
<dd> Sets <tt>&quot;Perl_rc&quot;</tt> to <tt>&quot;rc&quot;</tt>, and sets $^E to the corresponding value.</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>Loading DLLs and ordinals in DLLs
<dd> Some DLLs are only present in some versions of <font SIZE="-1">OS/2,</font> or in some configurations of <font SIZE="-1">OS/2.</font> Some exported entry points are present only in DLLs shipped with some versions of <font SIZE="-1">OS/2.</font> If these DLLs and entry points were linked directly for a Perl executable/DLL or from a Perl extensions, this binary would work only with the specified versions/setups. Even if these entry points were not needed, the <i>load</i> of the executable (or <font SIZE="-1">DLL</font>) would fail. 

 For example, many newer useful APIs are not present in <font SIZE="-1">OS/2</font> v2; many PM-related APIs require DLLs not available on floppy-boot setup. 

 To make these calls fail <i>only when the calls are executed</i>, one should call these <font SIZE="-1">API</font> via a dynamic linking <font SIZE="-1">API.</font> There is a subsystem in Perl to simplify such type of calls. A large number of entry points available for such linking is provided (see <tt>&quot;entries_ordinals&quot;</tt> - and also <tt>&quot;PMWIN_entries&quot;</tt> - in <i>os2ish.h</i>). These ordinals can be accessed via the APIs: 

 <pre>
 CallORD(), DeclFuncByORD(), DeclVoidFuncByORD(),
 DeclOSFuncByORD(), DeclWinFuncByORD(), AssignFuncPByORD(),
 DeclWinFuncByORD_CACHE(), DeclWinFuncByORD_CACHE_survive(),
 DeclWinFuncByORD_CACHE_resetError_survive(),
 DeclWinFunc_CACHE(), DeclWinFunc_CACHE_resetError(),
 DeclWinFunc_CACHE_survive(), DeclWinFunc_CACHE_resetError_survive()
</pre> 

 See the header files and the C code in the supplied OS/2-related modules for the details on usage of these functions. 

 Some of these functions also combine dynaloading semantic with the error-propagation semantic discussed above.</dl>

<h2>Perl flavors</h2>

 Because of idiosyncrasies of <font SIZE="-1">OS/2</font> one cannot have all the eggs in the same basket (though <font SIZE="-1">EMX</font> environment tries hard to overcome this limitations, so the situation may somehow improve). There are 4 executables for Perl provided by the distribution:

<h3><i>perl.exe</i></h3>

 The main workhorse. This is a chimera executable: it is compiled as an <tt>&quot;a.out&quot;</tt>-style executable, but is linked with <tt>&quot;omf&quot;</tt>-style dynamic library <i>perl.dll</i>, and with dynamic <font SIZE="-1">CRT DLL.</font> This executable is a <font SIZE="-1">VIO</font> application. 

 It can load perl dynamic extensions, and it can <b>fork()</b>. 

 <b>Note.</b> Keep in mind that <b>fork()</b> is needed to open a pipe to yourself.

<h3><i>perl_.exe</i></h3>

 This is a statically linked <tt>&quot;a.out&quot;</tt>-style executable. It cannot load dynamic Perl extensions. The executable supplied in binary distributions has a lot of extensions prebuilt, thus the above restriction is important only if you use custom-built extensions. This executable is a <font SIZE="-1">VIO</font> application. 

 <i>This is the only executable with does not require </i><font SIZE="-1"><i>OS/2.</i></font><i></i> The friends locked into <tt>&quot;M$&quot;</tt> world would appreciate the fact that this executable runs under <font SIZE="-1">DOS,</font> Win0.3*, Win0.95 and WinNT with an appropriate extender. See ``Other OSes''.

<h3><i>perl__.exe</i></h3>

 This is the same executable as <i>perl___.exe</i>, but it is a <font SIZE="-1">PM</font> application. 

 <b>Note.</b> Usually (unless explicitly redirected during the startup) <font SIZE="-1">STDIN, STDERR,</font> and <font SIZE="-1">STDOUT</font> of a <font SIZE="-1">PM</font> application are redirected to <i>nul</i>. However, it is possible to <i>see</i> them if you start <tt>&quot;perl__.exe&quot;</tt> from a <font SIZE="-1">PM</font> program which emulates a console window, like <i>Shell mode</i> of Emacs or <font SIZE="-1">EPM.</font> Thus it <i>is possible</i> to use Perl debugger (see perldebug) to debug your <font SIZE="-1">PM</font> application (but beware of the message loop lockups - this will not work if you have a message queue to serve, unless you hook the serving into the <b>getc()</b> function of the debugger). 

 Another way to see the output of a <font SIZE="-1">PM</font> program is to run it as 

 <pre>
  pm_prog args 2&gt;&amp;1 | cat -
</pre> 

 with a shell <i>different</i> from <i>cmd.exe</i>, so that it does not create a link between a <font SIZE="-1">VIO</font> session and the session of <tt>&quot;pm_porg&quot;</tt>. (Such a link closes the <font SIZE="-1">VIO</font> window.) E.g., this works with <i>sh.exe</i> - or with Perl! 

 <pre>
  open P, 'pm_prog args 2&gt;&amp;1 |' or die;
  print while &lt;P&gt;;
</pre> 

 The flavor <i>perl__.exe</i> is required if you want to start your program without a <font SIZE="-1">VIO</font> window present, but not <tt>&quot;detach&quot;</tt>ed (run <tt>&quot;help detach&quot;</tt> for more info). Very useful for extensions which use <font SIZE="-1">PM,</font> like <tt>&quot;Perl/Tk&quot;</tt> or <tt>&quot;OpenGL&quot;</tt>. 

 Note also that the differences between <font SIZE="-1">PM</font> and <font SIZE="-1">VIO</font> executables are only in the <i>default</i> behaviour. One can start <i>any</i> executable in <i>any</i> kind of session by using the arguments <tt>&quot;/fs&quot;</tt>, <tt>&quot;/pm&quot;</tt> or <tt>&quot;/win&quot;</tt> switches of the command <tt>&quot;start&quot;</tt> (of <i></i><font SIZE="-1"><i>CMD.EXE</i></font><i></i> or a similar shell). Alternatively, one can use the numeric first argument of the <tt>&quot;system&quot;</tt> Perl function (see OS2::Process).

<h3><i>perl___.exe</i></h3>

 This is an <tt>&quot;omf&quot;</tt>-style executable which is dynamically linked to <i>perl.dll</i> and <font SIZE="-1">CRT DLL. I</font> know no advantages of this executable over <tt>&quot;perl.exe&quot;</tt>, but it cannot <b>fork()</b> at all. Well, one advantage is that the build process is not so convoluted as with <tt>&quot;perl.exe&quot;</tt>. 

 It is a <font SIZE="-1">VIO</font> application.

<h3>Why strange names?</h3>

 Since Perl processes the <tt>&quot;#!&quot;</tt>-line (cf. ``<font SIZE="-1">DESCRIPTION''</font> in perlrun, ``Command Switches'' in perlrun, ``No Perl script found in input'' in perldiag), it should know when a program <i>is a Perl</i>. There is some naming convention which allows Perl to distinguish correct lines from wrong ones. The above names are almost the only names allowed by this convention which do not contain digits (which have absolutely different semantics).

<h3>Why dynamic linking?</h3>

 Well, having several executables dynamically linked to the same huge library has its advantages, but this would not substantiate the additional work to make it compile. The reason is the complicated-to-developers but very quick and convenient-to-users ``hard'' dynamic linking used by <font SIZE="-1">OS/2.</font> 

 There are two distinctive features of the dyna-linking model of <font SIZE="-1">OS/2:</font> first, all the references to external functions are resolved at the compile time; second, there is no runtime fixup of the DLLs after they are loaded into memory. The first feature is an enormous advantage over other models: it avoids conflicts when several DLLs used by an application export entries with the same name. In such cases ``other'' models of dyna-linking just choose between these two entry points using some random criterion - with predictable disasters as results. But it is the second feature which requires the build of <i>perl.dll</i>. 

 The address tables of DLLs are patched only once, when they are loaded. The addresses of the entry points into DLLs are guaranteed to be the same for all the programs which use the same <font SIZE="-1">DLL.</font> This removes the runtime fixup - once <font SIZE="-1">DLL</font> is loaded, its code is read-only. 

 While this allows some (significant?) performance advantages, this makes life much harder for developers, since the above scheme makes it impossible for a <font SIZE="-1">DLL</font> to be ``linked'' to a symbol in the <i>.EXE</i> file. Indeed, this would need a <font SIZE="-1">DLL</font> to have different relocations tables for the (different) executables which use this <font SIZE="-1">DLL.</font> 

 However, a dynamically loaded Perl extension is forced to use some symbols from the perl executable, e.g., to know how to find the arguments to the functions: the arguments live on the perl internal evaluation stack. The solution is to put the main code of the interpreter into a <font SIZE="-1">DLL,</font> and make the <i>.EXE</i> file which just loads this <font SIZE="-1">DLL</font> into memory and supplies command-arguments. The extension <font SIZE="-1">DLL</font> cannot link to symbols in <i>.EXE</i>, but it has no problem linking to symbols in the <i>.DLL</i>. 

 This <i>greatly</i> increases the load time for the application (as well as complexity of the compilation). Since interpreter is in a <font SIZE="-1">DLL,</font> the C <font SIZE="-1">RTL</font> is basically forced to reside in a <font SIZE="-1">DLL</font> as well (otherwise extensions would not be able to use <font SIZE="-1">CRT</font>). There are some advantages if you use different flavors of perl, such as running <i>perl.exe</i> and <i>perl__.exe</i> simultaneously: they share the memory of <i>perl.dll</i>. 

 <font SIZE="-1"><b>NOTE</b></font>. There is one additional effect which makes DLLs more wasteful: DLLs are loaded in the shared memory region, which is a scarse resource given the 512M barrier of the ``standard'' <font SIZE="-1">OS/2</font> virtual memory. The code of <i>.EXE</i> files is also shared by all the processes which use the particular <i>.EXE</i>, but they are ``shared in the private address space of the process''; this is possible because the address at which different sections of the <i>.EXE</i> file are loaded is decided at compile-time, thus all the processes have these sections loaded at same addresses, and no fixup of internal links inside the <i>.EXE</i> is needed. 

 Since DLLs may be loaded at run time, to have the same mechanism for DLLs one needs to have the address range of <i>any of the loaded</i> DLLs in the system to be available <i>in all the processes</i> which did not load a particular <font SIZE="-1">DLL</font> yet. This is why the DLLs are mapped to the shared memory region.

<h3>Why chimera build?</h3>

 Current <font SIZE="-1">EMX</font> environment does not allow DLLs compiled using Unixish <tt>&quot;a.out&quot;</tt> format to export symbols for data (or at least some types of data). This forces <tt>&quot;omf&quot;</tt>-style compile of <i>perl.dll</i>. 

 Current <font SIZE="-1">EMX</font> environment does not allow <i>.EXE</i> files compiled in <tt>&quot;omf&quot;</tt> format to <b>fork()</b>. <b>fork()</b> is needed for exactly three Perl operations:
<dl>
<dt>&bull;
<dd> explicit <b>fork()</b> in the script,
<dt>&bull;
<dd> <tt>&quot;open FH, &quot;|-&quot;&quot;</tt>
<dt>&bull;
<dd> <tt>&quot;open FH, &quot;-|&quot;&quot;</tt>, in other words, opening pipes to itself.</dl>
 

 While these operations are not questions of life and death, they are needed for a lot of useful scripts. This forces <tt>&quot;a.out&quot;</tt>-style compile of <i>perl.exe</i>.

<h2>ENVIRONMENT</h2>

 Here we list environment variables with are either <font SIZE="-1">OS/2-</font> and <font SIZE="-1">DOS-</font> and Win*-specific, or are more important under <font SIZE="-1">OS/2</font> than under other OSes.

<h3>PERLLIB_PREFIX</h3>

 Specific for <font SIZE="-1">EMX</font> port. Should have the form 

 <pre>
  path1;path2
</pre> 

 or 

 <pre>
  path1 path2
</pre> 

 If the beginning of some prebuilt path matches <i>path1</i>, it is substituted with <i>path2</i>. 

 Should be used if the perl library is moved from the default location in preference to <tt>&quot;<a HREF="/docs/linux/man/5-perl/">PERL</a>(5)LIB&quot;</tt>, since this would not leave wrong entries in <tt>@INC</tt>. For example, if the compiled version of perl looks for <tt>@INC</tt> in <i>f:/perllib/lib</i>, and you want to install the library in <i>h:/opt/gnu</i>, do 

 <pre>
  set PERLLIB_PREFIX=f:/perllib/lib;h:/opt/gnu
</pre> 

 This will cause Perl with the prebuilt <tt>@INC</tt> of 

 <pre>
  f:/perllib/lib/5.00553/os2
  f:/perllib/lib/5.00553
  f:/perllib/lib/site_perl/5.00553/os2
  f:/perllib/lib/site_perl/5.00553
  .
</pre> 

 to use the following <tt>@INC:</tt> 

 <pre>
  h:/opt/gnu/5.00553/os2
  h:/opt/gnu/5.00553
  h:/opt/gnu/site_perl/5.00553/os2
  h:/opt/gnu/site_perl/5.00553
  .
</pre>

<h3>PERL_BADLANG</h3>

 If 0, perl ignores <b>setlocale()</b> failing. May be useful with some strange <i>locale</i>s.

<h3>PERL_BADFREE</h3>

 If 0, perl would not warn of in case of unwarranted <b>free()</b>. With older perls this might be useful in conjunction with the module DB_File, which was buggy when dynamically linked and OMF-built. 

 Should not be set with newer Perls, since this may hide some <i>real</i> problems.

<h3>PERL_SH_DIR</h3>

 Specific for <font SIZE="-1">EMX</font> port. Gives the directory part of the location for <i>sh.exe</i>.

<h3>USE_PERL_FLOCK</h3>

 Specific for <font SIZE="-1">EMX</font> port. Since <b><a HREF="/docs/linux/man/3-flock/">flock</a></b>(3) is present in <font SIZE="-1">EMX,</font> but is not functional, it is emulated by perl. To disable the emulations, set environment variable <tt>&quot;USE_PERL_FLOCK=0&quot;</tt>.

<h3>TMP or TEMP</h3>

 Specific for <font SIZE="-1">EMX</font> port. Used as storage place for temporary files.

<h2>Evolution</h2>

 Here we list major changes which could make you by surprise.

<h3>Text-mode filehandles</h3>

 Starting from version 5.8, Perl uses a builtin translation layer for text-mode files. This replaces the efficient well-tested <font SIZE="-1">EMX</font> layer by some code which should be best characterized as a ``quick hack''. 

 In addition to possible bugs and an inability to follow changes to the translation policy with off/on switches of <font SIZE="-1">TERMIO</font> translation, this introduces a serious incompatible change: before <b>sysread()</b> on text-mode filehandles would go through the translation layer, now it would not.

<h3>Priorities</h3>

 <tt>&quot;setpriority&quot;</tt> and <tt>&quot;getpriority&quot;</tt> are not compatible with earlier ports by Andreas Kaiser. See <tt>&quot;setpriority, getpriority&quot;</tt>.

<h3><font SIZE="-1">DLL</font> name mangling: pre 5.6.2</h3>

 With the release 5.003_01 the dynamically loadable libraries should be rebuilt when a different version of Perl is compiled. In particular, DLLs (including <i>perl.dll</i>) are now created with the names which contain a checksum, thus allowing workaround for <font SIZE="-1">OS/2</font> scheme of caching DLLs. 

 It may be possible to code a simple workaround which would
<dl>
<dt>&bull;
<dd> find the old DLLs looking through the old <tt>@INC</tt>;
<dt>&bull;
<dd> mangle the names according to the scheme of new perl and copy the DLLs to these names;
<dt>&bull;
<dd> edit the internal <tt>&quot;LX&quot;</tt> tables of <font SIZE="-1">DLL</font> to reflect the change of the name (probably not needed for Perl extension DLLs, since the internally coded names are not used for ``specific'' DLLs, they used only for ``global'' DLLs).
<dt>&bull;
<dd> edit the internal <tt>&quot;IMPORT&quot;</tt> tables and change the name of the ``old'' <i>perl????.dll</i> to the ``new'' <i>perl????.dll</i>.</dl>

<h3><font SIZE="-1">DLL</font> name mangling: 5.6.2 and beyond</h3>

 In fact mangling of <i>extension</i> DLLs was done due to misunderstanding of the <font SIZE="-1">OS/2</font> dynaloading model. <font SIZE="-1">OS/2</font> (effectively) maintains two different tables of loaded <font SIZE="-1">DLL:</font>
<dl>
<dt>Global DLLs
<dd> those loaded by the base name from <tt>&quot;LIBPATH&quot;</tt>; including those associated at link time;
<dt>specific DLLs
<dd> loaded by the full name.</dl>
 

 When resolving a request for a global <font SIZE="-1">DLL,</font> the table of already-loaded specific DLLs is (effectively) ignored; moreover, specific DLLs are <i>always</i> loaded from the prescribed path. 

 There is/was a minor twist which makes this scheme fragile: what to do with DLLs loaded from
<dl>
<dt>&quot;BEGINLIBPATH&quot; and &quot;ENDLIBPATH&quot;
<dd> (which depend on the process)
<dt><i>.</i> from &quot;LIBPATH&quot;
<dd> which <i>effectively</i> depends on the process (although <tt>&quot;LIBPATH&quot;</tt> is the same for all the processes).</dl>
 

 Unless <tt>&quot;LIBPATHSTRICT&quot;</tt> is set to <tt>&quot;T&quot;</tt> (and the kernel is after 2000/09/01), such DLLs are considered to be global. When loading a global <font SIZE="-1">DLL</font> it is first looked in the table of already-loaded global DLLs. Because of this the fact that one executable loaded a <font SIZE="-1">DLL</font> from <tt>&quot;BEGINLIBPATH&quot;</tt> and <tt>&quot;ENDLIBPATH&quot;</tt>, or <i>.</i> from <tt>&quot;LIBPATH&quot;</tt> may affect <i>which</i> <font SIZE="-1">DLL</font> is loaded when <i>another</i> executable requests a <font SIZE="-1">DLL</font> with the same name. <i>This</i> is the reason for version-specific mangling of the <font SIZE="-1">DLL</font> name for perl <font SIZE="-1">DLL.</font> 

 Since the Perl extension DLLs are always loaded with the full path, there is no need to mangle their names in a version-specific ways: their directory already reflects the corresponding version of perl, and <tt>@INC</tt> takes into account binary compatibility with older version. Starting from <tt>5.6.2</tt> the name mangling scheme is fixed to be the same as for Perl 5.005_53 (same as in a popular binary release). Thus new Perls will be able to <i>resolve the names</i> of old extension DLLs if <tt>@INC</tt> allows finding their directories. 

 However, this still does not guarantee that these <font SIZE="-1">DLL</font> may be loaded. The reason is the mangling of the name of the <i>Perl </i><font SIZE="-1"><i>DLL</i></font><i></i>. And since the extension DLLs link with the Perl <font SIZE="-1">DLL,</font> extension DLLs for older versions would load an older Perl <font SIZE="-1">DLL,</font> and would most probably segfault (since the data in this <font SIZE="-1">DLL</font> is not properly initialized). 

 There is a partial workaround (which can be made complete with newer <font SIZE="-1">OS/2</font> kernels): create a forwarder <font SIZE="-1">DLL</font> with the same name as the <font SIZE="-1">DLL</font> of the older version of Perl, which forwards the entry points to the newer Perl's <font SIZE="-1">DLL.</font> Make this <font SIZE="-1">DLL</font> accessible on (say) the <tt>&quot;BEGINLIBPATH&quot;</tt> of the new Perl executable. When the new executable accesses old Perl's extension DLLs, they would request the old Perl's <font SIZE="-1">DLL</font> by name, get the forwarder instead, so effectively will link with the currently running (new) Perl <font SIZE="-1">DLL.</font> 

 This may break in two ways:
<dl>
<dt>&bull;
<dd> Old perl executable is started when a new executable is running has loaded an extension compiled for the old executable (ouph!). In this case the old executable will get a forwarder <font SIZE="-1">DLL</font> instead of the old perl <font SIZE="-1">DLL,</font> so would link with the new perl <font SIZE="-1">DLL.</font> While not directly fatal, it will behave the same as new executable. This beats the whole purpose of explicitly starting an old executable.
<dt>&bull;
<dd> A new executable loads an extension compiled for the old executable when an old perl executable is running. In this case the extension will not pick up the forwarder - with fatal results.</dl>
 

 With support for <tt>&quot;LIBPATHSTRICT&quot;</tt> this may be circumvented - unless one of DLLs is started from <i>.</i> from <tt>&quot;LIBPATH&quot;</tt> (I do not know whether <tt>&quot;LIBPATHSTRICT&quot;</tt> affects this case). 

 <font SIZE="-1"><b>REMARK</b></font>. Unless newer kernels allow <i>.</i> in <tt>&quot;BEGINLIBPATH&quot;</tt> (older do not), this mess cannot be completely cleaned. (It turns out that as of the beginning of 2002, <i>.</i> is not allowed, but <i>.\.</i> is - and it has the same effect.) 

 <font SIZE="-1"><b>REMARK</b></font>. <tt>&quot;LIBPATHSTRICT&quot;</tt>, <tt>&quot;BEGINLIBPATH&quot;</tt> and <tt>&quot;ENDLIBPATH&quot;</tt> are not environment variables, although <i>cmd.exe</i> emulates them on <tt>&quot;SET ...&quot;</tt> lines. From Perl they may be accessed by Cwd::extLibpath and Cwd::extLibpath_set.

<h3><font SIZE="-1">DLL</font> forwarder generation</h3>

 Assume that the old <font SIZE="-1">DLL</font> is named <i>perlE0AC.dll</i> (as is one for 5.005_53), and the new version is 5.6.1. Create a file <i>perl5shim.def-leader</i> with 

 <pre><code>
LIBRARY 'perlE0AC' INITINSTANCE TERMINSTANCE
    DESCRIPTION '@#perl5-porters [at] perl.org:5.006001#@ Perl module for 5.00553 -&gt; Perl 5.6.1 forwarder' CODE LOADONCALL
        DATA LOADONCALL NONSHARED MULTIPLE
            EXPORTS
</code></pre> 

 modifying the versions/names as needed. Run 

 <pre>
 perl -wnle &quot;next if 0../EXPORTS/; print qq(  \&quot;$1\&quot;)
                                          if /\&quot;(\w+)\&quot;/&quot; perl5.def &gt;lst
</pre> 

 in the Perl build directory (to make the <font SIZE="-1">DLL</font> smaller replace perl5.def with the definition file for the older version of Perl if present). 

 <pre>
 cat perl5shim.def-leader lst &gt;perl5shim.def
 gcc -Zomf -Zdll -o perlE0AC.dll perl5shim.def -s -llibperl
</pre> 

 (ignore multiple <tt>&quot;warning L4085&quot;</tt>).

<h3>Threading</h3>

 As of release 5.003_01 perl is linked to multithreaded C <font SIZE="-1">RTL DLL.</font> If perl itself is not compiled multithread-enabled, so will not be perl's <b>malloc()</b>. However, extensions may use multiple thread on their own risk. 

 This was needed to compile <tt>&quot;Perl/Tk&quot;</tt> for XFree86-OS/2 out-of-the-box, and link with DLLs for other useful libraries, which typically are compiled with <tt>&quot;-Zmt -Zcrtdll&quot;</tt>.

<h3>Calls to external programs</h3>

 Due to a popular demand the perl external program calling has been changed wrt Andreas Kaiser's port. <i>If</i> perl needs to call an external program <i>via shell</i>, the <i>f:/bin/sh.exe</i> will be called, or whatever is the override, see &quot;<tt>&quot;PERL_SH_DIR&quot;</tt>&quot;. 

 Thus means that you need to get some copy of a <i>sh.exe</i> as well (I use one from pdksh). The path <i>F:/bin</i> above is set up automatically during the build to a correct value on the builder machine, but is overridable at runtime, 

 <b>Reasons:</b> a consensus on <tt>&quot;perl5-porters&quot;</tt> was that perl should use one non-overridable shell per platform. The obvious choices for <font SIZE="-1">OS/2</font> are <i>cmd.exe</i> and <i>sh.exe</i>. Having perl build itself would be impossible with <i>cmd.exe</i> as a shell, thus I picked up <tt>&quot;sh.exe&quot;</tt>. This assures almost 100% compatibility with the scripts coming from *nix. As an added benefit this works as well under <font SIZE="-1">DOS</font> if you use DOS-enabled port of pdksh (see ``Prerequisites''). 

 <b>Disadvantages:</b> currently <i>sh.exe</i> of pdksh calls external programs via <b>fork()</b>/<b>exec()</b>, and there is <i>no</i> functioning <b>exec()</b> on <font SIZE="-1">OS/2.</font> <b>exec()</b> is emulated by <font SIZE="-1">EMX</font> by an asynchronous call while the caller waits for child completion (to pretend that the <tt>&quot;pid&quot;</tt> did not change). This means that 1 <i>extra</i> copy of <i>sh.exe</i> is made active via <b>fork()</b>/<b>exec()</b>, which may lead to some resources taken from the system (even if we do not count extra work needed for <b>fork()</b>ing). 

 Note that this a lesser issue now when we do not spawn <i>sh.exe</i> unless needed (metachars found). 

 One can always start <i>cmd.exe</i> explicitly via 

 <pre>
  system 'cmd', '/c', 'mycmd', 'arg1', 'arg2', ...
</pre> 

 If you need to use <i>cmd.exe</i>, and do not want to hand-edit thousands of your scripts, the long-term solution proposed on p5-p is to have a directive 

 <pre>
  use OS2::Cmd;
</pre> 

 which will override <b>system()</b>, <b>exec()</b>, <tt>&quot;``&quot;</tt>, and <tt>&quot;open(,'...|')&quot;</tt>. With current perl you may override only <b>system()</b>, <b>readpipe()</b> - the explicit version of <tt>&quot;``&quot;</tt>, and maybe <b>exec()</b>. The code will substitute the one-argument call to <b>system()</b> by <tt>&quot;CORE::system('cmd.exe', '/c', shift)&quot;</tt>. 

 If you have some working code for <tt>&quot;OS2::Cmd&quot;</tt>, please send it to me, I will include it into distribution. I have no need for such a module, so cannot test it. 

 For the details of the current situation with calling external programs, see ``Starting <font SIZE="-1">OS/2</font> (and <font SIZE="-1">DOS</font>) programs under Perl''. Set us mention a couple of features:
<dl>
<dt>&bull;
<dd> External scripts may be called by their basename. Perl will try the same extensions as when processing <b>-S</b> command-line switch.
<dt>&bull;
<dd> External scripts starting with <tt>&quot;#!&quot;</tt> or <tt>&quot;extproc &quot;</tt> will be executed directly, without calling the shell, by calling the program specified on the rest of the first line.</dl>

<h3>Memory allocation</h3>

 Perl uses its own <b>malloc()</b> under <font SIZE="-1">OS/2</font> - interpreters are usually malloc-bound for speed, but perl is not, since its malloc is lightning-fast. Perl-memory-usage-tuned benchmarks show that Perl's malloc is 5 times quicker than <font SIZE="-1">EMX</font> one. I do not have convincing data about memory footprint, but a (pretty random) benchmark showed that Perl's one is 5% better. 

 Combination of perl's <b>malloc()</b> and rigid <font SIZE="-1">DLL</font> name resolution creates a special problem with library functions which expect their return value to be <b>free()</b>d by system's <b>free()</b>. To facilitate extensions which need to call such functions, system memory-allocation functions are still available with the prefix <tt>&quot;emx_&quot;</tt> added. (Currently only <font SIZE="-1">DLL</font> perl has this, it should propagate to <i>perl_.exe</i> shortly.)

<h3>Threads</h3>

 One can build perl with thread support enabled by providing <tt>&quot;-D usethreads&quot;</tt> option to <i>Configure</i>. Currently <font SIZE="-1">OS/2</font> support of threads is very preliminary. 

 Most notable problems:
<dl>
<dt>&quot;COND_WAIT&quot;
<dd> may have a race condition (but probably does not due to edge-triggered nature of <font SIZE="-1">OS/2</font> Event semaphores). (Needs a reimplementation (in terms of chaining waiting threads, with the linked list stored in per-thread structure?)?)
<dt><i>os2.c</i>
<dd> has a couple of static variables used in OS/2-specific functions. (Need to be moved to per-thread structure, or serialized?)</dl>
 

 Note that these problems should not discourage experimenting, since they have a low probability of affecting small programs.

<h2>BUGS</h2>

 This description is not updated often (since 5.6.1?), see <i>./os2/Changes</i> for more info.

<h2>AUTHOR</h2>

 Ilya Zakharevich, cpan [at] ilyaz.org

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-perl/">perl</a></b>(1). 

<h2>Index</h2>



<dt><a HREF="#lbAJ">Frequently asked questions</a>
<dd>


<dt><a HREF="#lbAP">INSTALLATION</a>
<dd>


<dt><a HREF="#lbAT">Accessing documentation</a>
<dd>


<dt><a HREF="#lbBB">BUILD</a>
<dd>


<dt><a HREF="#lbBL">Building a binary distribution</a>
<dd>
<dt><a HREF="#lbBM">Building custom <i>.EXE</i> files</a>
<dd>


<dt><a HREF="#lbBP">Build FAQ</a>
<dd>


<dt><a HREF="#lbBX">Specific (mis)features of OS/2 port</a>
<dd>


<dt><a HREF="#lbCI">Perl flavors</a>
<dd>


<dt><a HREF="#lbCQ">ENVIRONMENT</a>
<dd>


<dt><a HREF="#lbCX">Evolution</a>
<dd>


<dt><a HREF="#lbDH">BUGS</a>
<dd>
<dt><a HREF="#lbDI">AUTHOR</a>
<dd>
<dt><a HREF="#lbDJ">SEE ALSO</a>
<dd></dl>
