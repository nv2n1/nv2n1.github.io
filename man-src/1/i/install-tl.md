---
title: "install-tl(1)"
name: "install-tl"
section: "1"
letter: "i"
url: "/docs/linux/man/1-install-tl/"
description: "install-tl – TeX Live cross-platform installer"
---

<h2 class="name">NAME</h2>
<p> install-tl &#8211; TeX Live cross-platform installer </p>
<h2>SYNOPSIS</h2>
<p> install-tl [<i>option</i>]&#8230; </p>
<p> install-tl-windows.bat [<i>option</i>]&#8230; </p>
<p> install-tl-advanced.bat [<i>option</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This installer creates a runnable TeX Live installation from various media, including over the network, from local hard disk, a <font SIZE="-1">DVD,</font> etc. The installer works on all platforms supported by TeX Live. For information on initially downloading TeX Live, see &lt;<a rel="nofollow" href="https://tug.org/texlive/acquire.html">https://tug.org/texlive/acquire.html</a>&gt;. </p>
<p> The basic idea of TeX Live installation is for you to choose one of the top-level <i>schemes</i>, each of which is defined as a different set of <i>collections</i> and <i>packages</i>, where a collection is a set of packages, and a package is what contains actual files. </p>
<p> Within the installer, you can choose a scheme, and further customize the set of collections to install, but not the set of the packages. To work at the package level, use <tt>&quot;tlmgr&quot;</tt> (reference just below) after the initial installation is complete. </p>
<p> The default is <tt>&quot;scheme-full&quot;</tt>, which installs everything, and this is highly recommended.</p>
<h2>REFERENCES</h2>
<p> Post-installation configuration, package updates, and more, are handled through <code><a href="/docs/linux/man/1-tlmgr/">tlmgr</a></code>(1), the TeX Live Manager (&lt;<a rel="nofollow" href="https://tug.org/texlive/tlmgr.html">https://tug.org/texlive/tlmgr.html</a>&gt;). </p>
<p> The most up-to-date version of this installer documentation is on the Internet at &lt;<a rel="nofollow" href="https://tug.org/texlive/doc/install-tl.html">https://tug.org/texlive/doc/install-tl.html</a>&gt;. </p>
<p> For the full documentation of TeX Live, see &lt;<a rel="nofollow" href="https://tug.org/texlive/doc">https://tug.org/texlive/doc</a>&gt;.</p>
<h2>OPTIONS</h2>
<p> As usual, all options can be specified in any order, and with either a leading <tt>&quot;-&quot;</tt> or <tt>&quot;--&quot;</tt>. An argument value can be separated from its option by either a space or <tt>&quot;=&quot;</tt>.</p>
<dl>
<dt><code>-gui</code> [[=]<i>module</i>]</p>
<dd> If no <i>module</i> is given, starts the Tcl/Tk (see below) <font SIZE="-1">GUI</font> installer. </p>
<p> If <i>module</i> is given loads the given installer module. Currently the following modules are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;text&quot;</p>
<dd> The text mode user interface (default on Unix systems, including Macs). Same as the <tt>&quot;-no-gui&quot;</tt> option.</p>
<dt>&quot;tcl&quot; (or &quot;perltk&quot; or &quot;wizard&quot; or &quot;expert&quot; or nothing)</p>
<dd> The Tcl/Tk user interface (default on Windows). It starts with a small number of configuration options, roughly equivalent to what the former wizard option offers, but a button <tt>&quot;Advanced&quot;</tt> takes you to a screen with roughly the same options as the former <tt>&quot;perltk&quot;</tt> interface.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The default <font SIZE="-1">GUI</font> requires Tcl/Tk. This is standard on Macs (although it is considered deprecated since Catalina) and is often already installed on GNU/Linux, or can be easily installed through a distro package manager. For Windows, TeX Live provides a Tcl/Tk runtime.</dl>
<dt><code>-no-gui</code></p>
<dd> Use the text mode installer (default except on Windows and Macs).</p>
<dt><code>-lang</code> <i>llcode</i></p>
<dd> By default, the Tcl <font SIZE="-1">GUI</font> uses the language detection built into Tcl/Tk. If that fails you can select a different language by giving this option with a language code (based on <font SIZE="-1">ISO 639-1</font>). Currently supported (but not necessarily completely translated) are: English (en, default), Czech (cs), German (de), French (fr), Italian (it), Japanese (ja), Dutch (nl), Polish (pl), Brazilian Portuguese (pt_BR), Russian (ru), Slovak (sk), Slovenian (sl), Serbian (sr), Ukrainian (uk), Vietnamese (vi), simplified Chinese (zh_CN), and traditional Chinese (zh_TW).</p>
<dt><code>-repository</code> <i>url|path</i></p>
<dd> Specify the package repository to be used as the source of the installation. In short, this can be a directory name or a url using http(s), ftp, or scp. The documentation for <tt>&quot;tlmgr&quot;</tt> has the details (&lt;<a rel="nofollow" href="https://tug.org/texlive/doc/tlmgr.html#OPTIONS">https://tug.org/texlive/doc/tlmgr.html#OPTIONS</a>&gt;). </p>
<p> For installation, the default is to pick a mirror automatically, using &lt;<a rel="nofollow" href="https://mirror.ctan.org/systems/texlive/tlnet">https://mirror.ctan.org/systems/texlive/tlnet</a>&gt;; the chosen mirror is used for the entire download. You can use the special argument <tt>&quot;ctan&quot;</tt> as an abbreviation for this. (See &lt;<a rel="nofollow" href="https://ctan.org">https://ctan.org</a>&gt; for more about <font SIZE="-1">CTAN</font> and its mirrors.) </p>
<p> After installation is complete, you can use that installation as the repository for another installation. If you chose to install less than the full scheme containing all packages, the list of available schemes will be adjusted accordingly.</p>
<dt><code>-select-repository</code></p>
<dd> This option allows you to choose a particular mirror from the current list of active <font SIZE="-1">CTAN</font> mirrors. This option is supported in the <tt>&quot;text&quot;</tt> and <tt>&quot;gui&quot;</tt> installer modes, and will also offer to install from local media if available, or from a repository specified on the command line. It&#8217;s useful when the (default) automatic redirection does not choose a good host for you.</p>
<dt><code>-all-options</code></p>
<dd> Normally options not relevant to the current platform are not shown (e.g., when running on Unix, Windows-specific options are omitted). Giving this command line option allows configuring such &#8220;foreign&#8221; settings.</p>
<dt><code>-custom-bin</code> <i>path</i></p>
<dd> If you have built your own set of TeX Live binaries (perhaps because your platform was not supported by TeX Live out of the box), this option allows you to specify the <i>path</i> to a directory where the binaries for the current system are present. The installation will continue as usual, but at the end all files from <i>path</i> are copied over to <tt>&quot;bin/custom/&quot;</tt> under your installation directory and this <tt>&quot;bin/custom/&quot;</tt> directory is what will be added to the path for the post-install actions. To install multiple custom binary sets, manually rename <tt>&quot;custom&quot;</tt> before doing each. </p>
<p> For more information on custom binaries, see &lt;<a rel="nofollow" href="https://tug.org/texlive/custom-bin.html">https://tug.org/texlive/custom-bin.html</a>&gt;. For general information on building TeX Live, see &lt;<a rel="nofollow" href="https://tug.org/texlive/build.html">https://tug.org/texlive/build.html</a>&gt;.</p>
<dt><code>-debug-translation</code></p>
<dd> In the former Perl/Tk <font SIZE="-1">GUI</font> modes, this option reported any missing, or more likely untranslated, messages to standard error. Not yet implemented for the Tcl interface. Helpful for translators to see what remains to be done.</p>
<dt><code>-force-platform</code> <i>platform</i></p>
<dd> Instead of auto-detecting the current platform, use <i>platform</i>. Binaries for this platform must be present and they must actually be runnable, or installation will fail. <tt>&quot;-force-arch&quot;</tt> is a synonym.</p>
<dt><code>-help</code>, <code>&#8211;help</code>, <code>-?</code></p>
<dd> Display this help and exit. (This help is also on the web at &lt;<a rel="nofollow" href="https://tug.org/texlive/doc/install-tl.html">https://tug.org/texlive/doc/install-tl.html</a>&gt;). Sometimes the <tt>&quot;perldoc&quot;</tt> and/or <tt>&quot;PAGER&quot;</tt> programs on the system have problems, possibly resulting in control characters being literally output. This can&#8217;t always be detected, but you can set the <tt>&quot;NOPERLDOC&quot;</tt> environment variable and <tt>&quot;perldoc&quot;</tt> will not be used.</p>
<dt><code>-in-place</code></p>
<dd> This is a quick-and-dirty installation option in case you already have an rsync or svn checkout of TeX Live. It will use the checkout as-is and will just do the necessary post-install. Be warned that the file <tt>&quot;tlpkg/texlive.tlpdb&quot;</tt> may be rewritten, that removal has to be done manually, and that the only realistic way to maintain this installation is to redo it from time to time. This option is not available via the installer interfaces. <font SIZE="-1">USE AT YOUR OWN RISK.</font></p>
<dt><code>-init-from-profile</code> <i>profile_file</i></p>
<dd> Similar to <code>-profile</code> (see &#8220;<font SIZE="-1">PROFILES&#8221;</font> below), but only initializes the installation configuration from <i>profile_file</i> and then starts a normal interactive session. Environment variables are not ignored.</p>
<dt><code>-logfile</code> <i>file</i></p>
<dd> Write both all messages (informational, debugging, warnings) to <i>file</i>, in addition to standard output or standard error. </p>
<p> If this option is not given, the installer will create a log file in the root of the writable installation tree, for example, <tt>&quot;/usr/local/texlive/YYYY/install-tl.log&quot;</tt> for the <i></i><font SIZE="-1"><i>YYYY</i></font><i></i> release.</p>
<dt><code>-no-cls</code></p>
<dd> For the text mode installer only: do not clear the screen when entering a new menu (for debugging purposes).</p>
<dt><code>-no-persistent-downloads</code></p>
<dd>
<dt><code>-persistent-downloads</code></p>
<dd> For network installs, activating this option makes the installer try to set up a persistent connection using the <tt>&quot;Net::LWP&quot;</tt> Perl module. This opens only one connection between your computer and the server per session and reuses it, instead of initiating a new download for each package, which typically yields a significant speed-up. </p>
<p> This option is turned on by default, and the installation program will fall back to using <tt>&quot;wget&quot;</tt> if this is not possible. To disable usage of <font SIZE="-1">LWP</font> and persistent connections, use <tt>&quot;-no-persistent-downloads&quot;</tt>.</p>
<dt><code>-no-verify-downloads</code></p>
<dd> By default, if a GnuPG <tt>&quot;gpg&quot;</tt> binary is found in <font SIZE="-1">PATH,</font> downloads are verified against a cryptographic signature. This option disables such verification. The full description is in the Crytographic Verification section of the <tt>&quot;tlmgr&quot;</tt> documentation, e.g., &lt;<a rel="nofollow" href="https://tug.org/texlive/doc/tlmgr.html#CRYPTOGRAPHIC-VERIFICATION">https://tug.org/texlive/doc/tlmgr.html#CRYPTOGRAPHIC-VERIFICATION</a>&gt;</p>
<dt><code>-non-admin</code></p>
<dd> For Windows only: configure for the current user, not for all users.</p>
<dt><code>-portable</code></p>
<dd> Install for portable use, e.g., on a <font SIZE="-1">USB</font> stick. Also selectable from within the perltk and text installers.</p>
<dt><code>-print-platform</code></p>
<dd> Print the TeX Live identifier for the detected platform (hardware/operating system) combination to standard output, and exit. <tt>&quot;-print-arch&quot;</tt> is a synonym.</p>
<dt><code>-profile</code> <i>profile_file</i></p>
<dd> Load <i>profile_file</i> and do the installation with no user interaction, that is, a batch (unattended) install. Environment variables are ignored. See &#8220;<font SIZE="-1">PROFILES&#8221;</font> below.</p>
<dt><code>-q</code></p>
<dd> Omit normal informational messages.</p>
<dt><code>-scheme</code> <i>scheme</i></p>
<dd> Schemes are the highest level of package grouping in TeX Live; the default is to use the <tt>&quot;full&quot;</tt> scheme, which includes everything. This option overrides that default. You can change the scheme again before the actual installation with the usual menu. The <i>scheme</i> argument may optionally have a prefix <tt>&quot;scheme-&quot;</tt>. The list of supported scheme names depends on what your package repository provides; see the interactive menu list.</p>
<dt><code>-v</code></p>
<dd> Include verbose debugging messages; repeat for maximum debugging: <tt>&quot;-v -v&quot;</tt>. (Further repeats are accepted but ignored.)</p>
<dt><code>-version</code>, <code>&#8211;version</code></p>
<dd> Output version information and exit. If <tt>&quot;-v&quot;</tt> is also given, the versions of the TeX Live modules used are also reported.</dl>
<h2>PROFILES</h2>
<p> A <i>profile</i> file contains all the values needed to perform an installation. After a normal installation has finished, a profile for that exact installation is written to the file <tt>&quot;tlpkg/texlive.profile&quot;</tt>. In addition, from the text menu one can select <tt>&quot;P&quot;</tt> to save the current setup as a profile at any time. </p>
<p> Such a profile file can be given as the argument to <tt>&quot;-profile&quot;</tt>, for example to redo the exact same installation on a different system. Alternatively, you can use a custom profile, most easily created by starting from a generated one and changing values, or an empty file, which will take all the defaults. </p>
<p> As mentioned above, the installer only supports selection by scheme and collections, not individual packages, so packages cannot be specified in profile files either. Use <tt>&quot;tlmgr&quot;</tt> to work at the package level. </p>
<p> Within a profile file, each line consists of </p>
<p> <i>variable</i> [<i>value</i>] </p>
<p> except for comment lines starting with <tt>&quot;#&quot;</tt>. The possible variable names are listed below. Values, when present, are either <tt>0</tt> or <tt>1</tt> for booleans, or strings (which must be specified without any quote characters). Leading whitespace is ignored. </p>
<p> If the variable <tt>&quot;selected_scheme&quot;</tt> is defined and <i>no</i> collection variables at all are defined, then the collections required by the specified scheme (which might change over time) are installed, without explicitly listing them. This eases maintenance of profile files. If any collections are specified in a profile, though, then all desired collections must be given explicitly. </p>
<p> For example, a line </p>
<pre>
  selected_scheme scheme-small
</pre>
<p> along with definitions for the installation directories (given below under &#8220;path options&#8221;) suffices to install the &#8220;small&#8221; scheme with all default options. The schemes are described in the <tt>&quot;S&quot;</tt> menu in the text installer, or equivalent. </p>
<p> Besides <tt>&quot;selected_scheme&quot;</tt>, here is the list of variable names supported in a profile: </p>
<p> <code>collection options</code> (prefix <tt>&quot;collection-&quot;</tt>) </p>
<p> Collections are specified with a variable name with the prefix <tt>&quot;collection-&quot;</tt> followed by a collection name; there is no value. For instance, <tt>&quot;collection-basic&quot;</tt>. The collections are described in the <tt>&quot;C&quot;</tt> menu. </p>
<p> Schemes and collections (and packages) are ultimately defined by the files in the <tt>&quot;tlpkg/tlpsrc/&quot;</tt> source directory. </p>
<p> <code>path options</code> </p>
<p> It is best to define all of these, even though they may not be used in the installation, so as to avoid unintentionally getting a default value that could cause problems later. </p>
<pre>
  TEXDIR
  TEXMFCONFIG
  TEXMFVAR
  TEXMFHOME
  TEXMFLOCAL
  TEXMFSYSCONFIG
  TEXMFSYSVAR
</pre>
<p> <code>installer options</code> (prefix <tt>&quot;instopt_&quot;</tt>)</p>
<dl>
<dt>&quot;instopt_adjustpath&quot; (default 0 on Unix, 1 on Windows)</p>
<dd> Adjust <tt>&quot;PATH&quot;</tt> environment variable.</p>
<dt>&quot;instopt_adjustrepo&quot; (default 1)</p>
<dd> Set remote repository to a multiplexed <font SIZE="-1">CTAN</font> mirror after installation; see <tt>&quot;-repository&quot;</tt> above.</p>
<dt>&quot;instopt_letter&quot; (default 0)</p>
<dd> Set letter size paper as the default, instead of a4.</p>
<dt>&quot;instopt_portable&quot; (default 0)</p>
<dd> Install for portable use, e.g., on a <font SIZE="-1">USB</font> stick.</p>
<dt>&quot;instopt_write18_restricted&quot; (default 1)</p>
<dd> Enable <tt>&quot;\write18&quot;</tt> for a restricted set of programs.</dl>
<p> <code>tlpdb options</code> (prefix <tt>&quot;tlpdbopt_&quot;</tt>) </p>
<p> The definitive list is given in <tt>&quot;tlpkg/TeXLive/TLConfig.pm&quot;</tt>, in the hash <tt>%TeXLive::TLConfig::TLPDBOptions</tt>, together with explanations. All items given there <i>except</i> for <tt>&quot;tlpdbopt_location&quot;</tt> can be specified. Here is the current list: </p>
<pre>
  tlpdbopt_autobackup
  tlpdbopt_backupdir
  tlpdbopt_create_formats
  tlpdbopt_desktop_integration
  tlpdbopt_file_assocs
  tlpdbopt_generate_updmap
  tlpdbopt_install_docfiles
  tlpdbopt_install_srcfiles
  tlpdbopt_post_code
  tlpdbopt_sys_bin
  tlpdbopt_sys_info
  tlpdbopt_sys_man
  tlpdbopt_w32_multi_user
</pre>
<p> <code>platform options</code> (prefix <tt>&quot;binary_&quot;</tt>) </p>
<p> For each supported platform in TeX Live (directories under <tt>&quot;bin/&quot;</tt>), the variable <tt>&quot;binary_&quot;</tt><i></i><font SIZE="-1"><i>PLATFORM</i></font><i></i> can be set with value 1. For example: </p>
<pre>
  binary_x86_64-linux 1
</pre>
<p> If no <tt>&quot;binary_&quot;</tt> settings are made, the default is whatever the current machine is running. </p>
<p> In releases before 2017, many profile variables had different names (not documented here; see the <tt>&quot;install-tl&quot;</tt> source). They are accepted and transformed to the names given above. When a profile is written, the names above are always used. </p>
<p> For more details on all of the above options, consult the TeX Live installation manual, linked from &lt;<a rel="nofollow" href="https://tug.org/texlive/doc">https://tug.org/texlive/doc</a>&gt;.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> For ease in scripting and debugging, <tt>&quot;install-tl&quot;</tt> looks for the following environment variables. They are not of interest for normal user installations.</p>
<dl>
<dt>&quot;TEXLIVE_DOWNLOADER&quot;</p>
<dd>
<dt>&quot;TL_DOWNLOAD_PROGRAM&quot;</p>
<dd>
<dt>&quot;TL_DOWNLOAD_ARGS&quot;</p>
<dd> These override the normal choice of a download program; see the <tt>&quot;tlmgr&quot;</tt> documentation, e.g., &lt;<a rel="nofollow" href="https://tug.org/texlive/doc/tlmgr.html#ENVIRONMENT-VARIABLES">https://tug.org/texlive/doc/tlmgr.html#ENVIRONMENT-VARIABLES</a>&gt;.</p>
<dt>&quot;TEXLIVE_INSTALL_ENV_NOCHECK&quot;</p>
<dd> Omit the check for environment variables containing the string <tt>&quot;tex&quot;</tt>. People developing TeX-related software are likely to have many such variables.</p>
<dt>&quot;TEXLIVE_INSTALL_NO_CONTEXT_CACHE&quot;</p>
<dd> Omit creating the ConTeXt cache. This is useful for redistributors.</p>
<dt>&quot;TEXLIVE_INSTALL_NO_RESUME&quot;</p>
<dd> Omit check for installing on top of a previous installation and then asking about importing previous settings.</p>
<dt>&quot;TEXLIVE_INSTALL_NO_WELCOME&quot;</p>
<dd> Omit printing the welcome message after successful installation, e.g., when testing.</p>
<dt>&quot;TEXLIVE_INSTALL_PAPER&quot;</p>
<dd> Set the default paper size for all relevant programs; must be either <tt>&quot;letter&quot;</tt> or <tt>&quot;a4&quot;</tt>. The default is <tt>&quot;a4&quot;</tt>.</p>
<dt>&quot;TEXLIVE_INSTALL_PREFIX&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXDIR&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFCONFIG&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFVAR&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFHOME&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFLOCAL&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFSYSCONFIG&quot;</p>
<dd>
<dt>&quot;TEXLIVE_INSTALL_TEXMFSYSVAR&quot;</p>
<dd> Specify the respective directories. <tt>&quot;TEXLIVE_INSTALL_PREFIX&quot;</tt> defaults to <tt>&quot;/usr/local/texlive&quot;</tt>, while <tt>&quot;TEXLIVE_INSTALL_TEXDIR&quot;</tt> defaults to the release directory within that prefix, e.g., <tt>&quot;/usr/local/texlive/2016&quot;</tt>. All the defaults can be seen by running the installer interactively and then typing <tt>&quot;D&quot;</tt> for the directory menu.</p>
<dt>&quot;NOPERLDOC&quot;</p>
<dd> Don&#8217;t try to run the <tt>&quot;--help&quot;</tt> message through <tt>&quot;perldoc&quot;</tt>.</dl>
<h2>AUTHORS AND COPYRIGHT</h2>
<p> This script and its documentation were written for the TeX Live distribution (&lt;<a rel="nofollow" href="https://tug.org/texlive">https://tug.org/texlive</a>&gt;) and both are licensed under the <font SIZE="-1">GNU</font> General Public License Version 2 or later. </p>
<p> <tt>$Id:</tt> install-tl 59056 2021-05-02 21:48:01Z karl $ </p>
<h2>Index</h2>
