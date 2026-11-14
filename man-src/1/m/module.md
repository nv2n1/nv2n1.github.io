---
title: "module(1)"
name: "module"
section: "1"
letter: "m"
url: "/docs/linux/man/1-module/"
description: "module – command interface to the Modules package"
---

<h2 class="name">NAME</h2>
<p> module &#8211; command interface to the Modules package </p>
<h2>SYNOPSIS</h2>
<p> <code>module</code> [ <i>switches</i> ] [ <i>sub-command</i> ] <i>[ sub-command-args ]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>module</code> is a user interface to the Modules package. The Modules package provides for the dynamic modification of the user&#8217;s environment via <i>modulefiles.</i> </p>
<p> Each <i>modulefile</i> contains the information needed to configure the shell for an application. Once the Modules package is initialized, the environment can be modified on a per-module basis using the <code>module</code> command which interprets <i>modulefiles.</i> Typically <i>modulefiles</i> instruct the <code>module</code> command to alter or set shell environment variables such as PATH, MANPATH, etc. <i>modulefiles</i> may be shared by many users on a system and users may have their own collection to supplement or replace the shared <i>modulefiles.</i> </p>
<p> The <i>modulefiles</i> are added to and removed from the current environment by the user. The environment changes contained in a <i>modulefile</i> can be summarized through the <code>module</code> command as well. If no arguments are given, a summary of the <code>module</code> usage and <i>sub-commands</i> are shown. </p>
<p> The action for the <code>module</code> command to take is described by the <i>sub-command</i> and its associated arguments.</p>
<h3>Package Initialization</h3>
<p> The Modules package and the <code>module</code> command are initialized when a shell-specific initialization script is sourced into the shell. The script creates the <code>module</code> command, either as an alias or shell function, creates Modules environment variables, and if enabled to do so, a snapshot of the environment is saved as either (if BEGINENV=1) <i>$HOME/.modulesbeginenv</i> or (if BEGINENV=99) whatever <i>$MODULESBEGINENV</i> points to. </p>
<p> The <code>module</code> alias or function executes the <code>modulecmd</code> program and has the shell evaluate the command&#8217;s output. The first argument to <code>modulecmd</code> specifies the type of shell. </p>
<p> The initialization scripts are kept in <i>$MODULESHOME/init/&lt;shell&gt;</i> where <i>&lt;shell&gt;</i> is the name of the sourcing shell. The sh, csh, tcsh, bash, ksh, and zsh shells are supported by <code>modulecmd.</code> In addition, python, perl, and cmake &quot;shells&quot; are supported, which writes the environment changes to stdout as python, perl, or cmake code. </p>
<p> The perl <i>module</i> command is set up with: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>use lib&nbsp;<wbr>$ENV{&#8216;MODULESHOME&#8217;}.&quot;/init&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>use perl; </p>
<p> And the python <i>module</i> command is defined with: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>import os;<br />
&nbsp;<wbr>&nbsp;<wbr>if os.environ.has_key(&#8216;PYTHONPATH&#8217;):<br />
&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>os.environ[&#8216;PYTHONPATH&#8217;]&nbsp;<wbr>+=&#8217;:&#8217;+os.environ[&#8216;MODULESHOME&#8217;]+&quot;/init&quot;;</p>
<p>&nbsp;<wbr>&nbsp;<wbr>else:<br />
&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>os.environ[&#8216;PYTHONPATH&#8217;]&nbsp;<wbr>=&nbsp;<wbr>os.environ[&#8216;MODULESHOME&#8217;]+&quot;/init&quot;;</p>
<p>&nbsp;<wbr>&nbsp;<wbr>from python import module; </p>
<h3>Modulecmd startup</h3>
<p> Upon invocation <i>modulecmd</i> sources rc files which contain global, user and modulefile specific setups. These files are interpreted as modulefiles. See <code><a href="/docs/linux/man/4-modulefile/">modulefile</a></code>(4) for detailed information. </p>
<p> Upon invocation of modulecmd module RC files are sourced in the following order: </p>
<pre><code>
Global RC file as specified by ${MODULERCFILE} or ${MODULESHOME} / etc / rc User specific module RC file ${HOME} /.modulerc All.modulerc and.version files found during modulefile seeking.
</code></pre>
<h3>Command line switches</h3>
<p> The module command accepts command line switches as its first parameter. These may be used to control output format of all information displayed and the <i>module</i> behavior in case of locating and interpreting module files. </p>
<p> All switches may be entered either in short or long notation. The following switches are accepted: </p>
<dl>
<dt><i>&#8211;help, -H</i></p>
<dd> Give some helpful usage information, and terminates the command.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;version, -V</i></p>
<dd> Lists the current version of the module command, and some configured option values. The command then terminates without further processing.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;force, -f</i></p>
<dd> Force active dependency resolution. This will result in modules found on a <i>prereq</i> command inside a module file being load automatically. Unloading module files using this switch will result in all required modules which have been loaded automatically using the <i>-f</i> switch being unload. This switch is experimental at the moment.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;terse, -t</i></p>
<dd> Display <i>avail</i> and <i>list</i> output in short format.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;long, -l</i></p>
<dd> Display <i>avail</i> and <i>list</i> output in long format.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;human, -h</i></p>
<dd> Display short output of the <i>avail</i> and <i>list</i> commands in human readable format.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;verbose, -v</i></p>
<dd> Enable verbose messages during module command execution.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;silent, -s</i></p>
<dd> Disable verbose messages. Redirect <i>stderr</i> to <i>/dev/null</i> if <i>stderr</i> is found not to be a tty. This is a useful option for module commands being written into <i>.cshrc</i>, <i>.login</i> or <i>.profile</i> files, because some remote shells (as <i><a href="/docs/linux/man/1-rsh/">rsh</a></i>(1)) and remote execution commands (like <i>rdist</i>) get confused if there is output on stderr.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;create, -c</i></p>
<dd> Create caches for <i>module avail</i> and <i>module apropos</i>. You must be granted write access to the ${<font SIZE="-1">MODULEHOME</font>}/modulefiles/ directory if you try to invoke <i>module</i> with the <i>-c</i> option.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;icase, -i</i></p>
<dd> Case insensitive module parameter evaluation. Currently only implemented for the <i>module apropos</i> command.</p>
<dl>
<dt>
<dd></dl>
<dt><i>&#8211;userlvl &lt;lvl&gt;, -u &lt;lvl&gt;</i></p>
<dd> Set the user level to the specified value. The argument of this option may be one of:</dl>
<p> <i>novice, nov</i> Novice </p>
<p> <i>expert, exp</i> Experienced module user </p>
<p> <i>advanced, adv</i> Advanced module user</p>
<h3>Module Sub-Commands</h3>
<dl>
<dt>
<dd>
<dl>
<dt><code>help&nbsp;<wbr>&nbsp;<wbr> [modulefile&#8230;]</code></p>
<dd> Print the usage of each sub-command. If an argument is given, print the Module-specific help information for the <i>modulefile</i>(s).</p>
<dt><code>add&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> modulefile&#8230;</code></p>
<dd>
<dt><code>load&nbsp;<wbr>&nbsp;<wbr> modulefile&#8230;</code></p>
<dd> Load <i>modulefile</i>(s) into the shell environment.</p>
<dt><code>rm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> modulefile&#8230;</code></p>
<dd>
<dt><code>unload modulefile&#8230;</code></p>
<dd> Remove <i>modulefile</i>(s) from the shell environment.</p>
<dt><code>swap&nbsp;<wbr>&nbsp;<wbr> [modulefile1] modulefile2</code></p>
<dd>
<dt><code>switch [modulefile1] modulefile2</code></p>
<dd> Switch loaded <i>modulefile1</i> with <i>modulefile2</i>. If <i> modulefile1</i> is not specified, then it is assumed to be the currently loaded module with the same root name as <i>modulefile2</i>.</p>
<dt><code>show&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> modulefile&#8230;</code></p>
<dd>
<dt><code>display modulefile&#8230;</code></p>
<dd> Display information about one or more <i>modulefile</i>s. The display sub-command will list the full path of the <i>modulefile</i>(s) and all (or most) of the environment changes the modulefile(s) will make if loaded. (It will not display any environment changes found within conditional statements.)</p>
<dt><code>list</code></p>
<dd> List loaded modules.</p>
<dt><code>avail [path&#8230;]</code></p>
<dd> List all available modulefiles in the current <font SIZE="-1">MODULEPATH</font>, where the sorting order is given by the <font SIZE="-1">LC_COLLATE</font> locale environment variable. </p>
<p> All directories in the <font SIZE="-1">MODULEPATH</font> are recursively searched for files containing the <i>modulefile</i> magic cookie. </p>
<p> If an argument is given, then each directory in the <font SIZE="-1">MODULEPATH</font> is searched for modulefiles whose pathname match the argument. </p>
<p> Multiple versions of an application can be supported by creating a subdirectory for the application containing modulefiles for each version.</p>
<dt><code>use [-a|&#8211;append] directory&#8230;</code></p>
<dd> Prepend one or more directories to the <font SIZE="-1">MODULEPATH</font> environment variable. The &#8211;append flag will append the directory to <font SIZE="-1">MODULEPATH</font>.</p>
<dt><code>unuse directory&#8230;</code></p>
<dd> Remove one or more directories from the <font SIZE="-1">MODULEPATH</font> environment variable.</p>
<dt><code>update</code></p>
<dd> Attempt to reload all loaded modulefiles. The environment will be reconfigured to match the environment saved in <i>${</i><font SIZE="-1"><i>HOME</i></font><i>}/.modulesbeginenv</i> (if BEGINENV=1) or the file pointed at by <i>$MODULESBEGINEV</i> (if BEGINENV=99) and the modulefiles will be reloaded. This is only valid if modules was configured with &#8211;enable-beginenv (which defines BEGINENV), otherwise this will cause a warning. <code>update</code> will only change the environment variables that the <i>modulefile</i>s set.</p>
<dt><code>clear</code></p>
<dd> Force the Modules package to believe that no modules are currently loaded.</p>
<dt><code>purge</code></p>
<dd> Unload all loaded modulefiles.</p>
<dt><code>refresh</code></p>
<dd> Force a refresh of all non-persistent components of currently loaded modules. This should be used on derived shells where aliases need to be reinitialized but the environment variables have already been set by the currently loaded modules.</p>
<dt><code>whatis [modulefile&#8230;]</code></p>
<dd> Display the information set up by the <i>module-whatis</i> commands inside the specified modulefile(s). If no <i>modulefile</i> is specified, all &#8216;whatis&#8217; lines will be shown.</p>
<dt><code>apropos string</code></p>
<dd>
<dt><code>keyword string</code></p>
<dd> Seeks through the &#8216;whatis&#8217; informations of all modulefiles for the specified string. All <i>module-whatis</i> informations matching the <i>string</i> will be displayed.</p>
<dt><code>initadd modulefile&#8230;</code></p>
<dd> Add <i>modulefile</i>(s) to the shell&#8217;s initialization file in the user&#8217;s home directory. The startup files checked (in order) are:<br />
 csh &#8211; .modules, .cshrc(.ext), .csh_variables, and .login(.ext)<br />
 tcsh &#8211; .modules, .tcshrc, .cshrc(.ext), .csh_variables, and .login(.ext)<br />
 sh and ksh &#8211; .modules, .profile(.ext), and .kshenv(.ext)<br />
 bash &#8211; .modules, .bash_profile, .bash_login, .profile(.ext), and .bashrc(.ext)<br />
 zsh &#8211; .modules, .zcshrc(.ext), .zshenv(.ext), and .zlogin(.ext) </p>
<p> If a &#8216;module load&#8217; line is found in any of these files, the <i>modulefile</i>(s) is(are) appended to any existing list of modulefiles. The &#8216;module load&#8217; line must be located in at least one of the files listed above for any of the &#8216;init&#8217; sub-commands to work properly. If the &#8216;module load&#8217; line is found in multiple shell initialization files, all of the lines are changed.</p>
<dt><code>initprepend modulefile [modulefile&#8230;]</code></p>
<dd> Does the same as <code>initadd</code> but prepends the given modules to the beginning of the list.</p>
<dt><code>initrm modulefile&#8230;</code></p>
<dd> Remove <i>modulefile</i>(s) from the shell&#8217;s initialization files.</p>
<dt><code>initswitch modulefile1 modulefile2</code></p>
<dd> Switch <i>modulefile1</i> with <i>modulefile2</i> in the shell&#8217;s initialization files.</p>
<dt><code>initlist</code></p>
<dd> List all of the modulefiles loaded from the shell&#8217;s initialization file.</p>
<dt><code>initclear</code></p>
<dd> Clear all of the modulefiles from the shell&#8217;s initialization files.</dl>
</dl>
<h3>Modulefiles</h3>
<p> <i>modulefile</i>s are written in the Tool Command Language (Tcl) and are interpreted by <code>modulecmd.</code> <i>modulefile</i>s can use conditional statements. Thus the effect a <i>modulefile</i> will have on the environment may change depending upon the current state of the environment. </p>
<p> Environment variables are unset when unloading a <i>modulefile.</i> Thus, it is possible to <code>load</code> a <i>modulefile</i> and then <code>unload</code> it without having the environment variables return to their prior state. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>MODULESHOME</code></font></p>
<dd> The location of the master Modules package file directory containing <code>module</code> command initialization scripts, the executable program <code>modulecmd,</code> and a directory containing a collection of master <i>modulefiles.</i></p>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>MODULEPATH</code></font></p>
<dd> The path that the <code>module</code> command searches when looking for <i>modulefiles.</i> Typically, it is set to a default value by the bootstrap procedure. <font SIZE="-1">MODULEPATH</font> can be set using &#8216;module use&#8217; or by the module initialization script to search group or personal <i>modulefile</i> directories before or after the master <i>modulefile</i> directory.</p>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>LOADEDMODULES</code></font></p>
<dd> A colon separated list of all loaded <i>modulefiles.</i></p>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>_LMFILES_</code></font></p>
<dd> A colon separated list of the full pathname for all loaded <i>modulefiles.</i></p>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>MODULESBEGINENV</code></font></p>
<dd> If modules has been configured (BEGINENV=99) to test for this environment variable, then if it exists, it is the name of the file to store the the initial shell environment. This environment variable will have embedded environment variables unrolled to one level. The contents of this variable is only used the first time <i>modules</i> is invoked.</p>
<dt><font SIZE="-1"></font><font SIZE="-2"><code>_MODULESBEGINENV_</code></font></p>
<dd> The filename of the file containing the initialization environment snapshot. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/Modules</code></p>
<dd> The <font SIZE="-1">MODULESHOME</font> directory.</p>
<dt><code>${</code><font SIZE="-1"><code>MODULESHOME</code></font><code>}/etc/rc</code></p>
<dd> The system-wide <i>modules rc file.</i> The location of this file can be changed using the <font SIZE="-1">MODULERCFILE</font> environment variable as described above.</p>
<dt><code>${</code><font SIZE="-1"><code>HOME</code></font><code>}/.modulerc</code></p>
<dd> The user specific <i>modules rc file.</i></p>
<dt><code>${</code><font SIZE="-1"><code>MODULESHOME</code></font><code>}/modulefiles</code></p>
<dd> The directory for system-wide <i>modulefiles.</i> The location of the directory can be changed using the <font SIZE="-1">MODULEPATH</font> environment variable as described above.</p>
<dt><code>${</code><font SIZE="-1"><code>MODULESHOME</code></font><code>}/bin/modulecmd</code></p>
<dd> The <i>modulefile</i> interpreter that gets executed upon each invocation of <code>module.</code></p>
<dt><code>${</code><font SIZE="-1"><code>MODULESHOME</code></font><code>}/init/</code><i>&lt;shell&gt;</i></p>
<dd> The Modules package initialization file sourced into the user&#8217;s environment.</p>
<dt><code>${</code><font SIZE="-1"><code>MODULEPATH</code></font><code>}/.moduleavailcache</code></p>
<dd> File containing the cached list of all <i>modulefiles</i> for each directory in the <font SIZE="-1">MODULEPATH</font> (only when the avail cache is enabled via the configure option &#8211;enable-cache which sets CACHE_AVAIL).</p>
<dt><code>${</code><font SIZE="-1"><code>MODULEPATH</code></font><code>}/.moduleavailcachedir</code></p>
<dd> File containing the names and modification times for all sub-directories with an avail cache (see above).</p>
<dt><code>${</code><font SIZE="-1"><code>HOME</code></font><code>}/.modulesbeginenv</code></p>
<dd> A snapshot of the user&#8217;s environment taken at Module initialization. This information is used by the <code>module update</code> sub-command (if BEGINENV=1), else</p>
<dt><code>$MODULESBEGINENV</code></p>
<dd> If this defines a valid filename, it serves the same purpose as above (if BEGINENV=99).</dl>
<h2>VERSION</h2>
<p> 3.2.10</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/4-modulefile/">modulefile</a></code>(4) </p>
<h2>Index</h2>
