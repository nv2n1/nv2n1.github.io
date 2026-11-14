---
title: "tclxinit(3)"
name: "tclxinit"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tclxinit/"
description: "Tclx_Init, Tclxcmd_Init, TclX_Main, Tkx_Init, TkX_Main – Extended Tcl initialization."
---

<p>Tclx_Init, Tclxcmd_Init, TclX_Main, Tkx_Init, TkX_Main &#8211; Extended Tcl initialization. </p>
<h2>Synopsis</h2>
<pre>-ltclx -ltcl
#include &quot;tclExtend.h&quot;
int
Tclx_Init (Tcl_Interp *interp);
int
Tclxcmd_Init (Tcl_Interp *interp);
int
void
TclX_Main (int argc,
 char **argv,
 Tcl_AppInitProc *appInitProc);
int
Tkx_Init (Tcl_Interp *interp);
void
TkX_Main (int argc,
 char **argv,
 Tcl_AppInitProc *appInitProc);
void
TclX_SetAppInfo (int defaultValues,
 char *appName,
 char *appLongName,
 char *appVersion,
 int appPatchlevel);</pre>
<h2>Description</h2>
<p>These functions are used to initialize Extended Tcl and applications based on Extended Tcl. This manual page also discusses various issues and approaches of integrating TclX into other applications.</p>
<h3>Tclx_Init</h3>
<p>Initializes Extended Tcl, adding the extended command set to the interpreter. This is called from <code>Tcl_AppInit</code>. This function must be called after the <code>Tcl_Init</code> function. In addition to the standard command set, it enables use of tlib packages libraries and makes the standard TclX library available. </p>
<p> Parameters</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; A pointer to the interpreter to add the commands to.</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>TCL_OK</code> if all is ok, <code>TCL_ERROR</code> if an error occurred.</dl>
<h3>Tclxcmd_Init</h3>
<p>Add the TclX command set to the interpreter, with the exception of the TclX library management commands. This is normally called by <code>Tclx_Init</code> and should only be used if you don&#8217;t want the TclX library handling. </p>
<p> Parameters</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; A pointer to the interpreter to add the commands to.</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>TCL_OK</code> if all is ok, <code>TCL_ERROR</code> if an error occurred.</dl>
<h3>TclX_Main</h3>
<p>This function parses the command line according to the TclX shell specification (Unix shell compatible). It creates an interpreter and calls the specified function <code>appInitProc</code> to initialize any application specific commands. It then either evaluates the command of script specified on the command line or enters an interactive command loop. This procedure never returns, it exits the process when it&#8217;s done. Using the TclX shell also gives you SIGINT handling in interactive shells.</p>
<h3>Tkx_Init</h3>
<p>Initializes Extended Tcl Tk environment. This is called from <code>Tcl_AppInit</code> after the <code>Tk_Init</code> function. </p>
<p> Parameters</p>
<dl COMPACT>
<dd><code>o </code><i>interp</i> &#8211; A pointer to the interpreter to add the commands to.</dl>
<p> Returns:</p>
<dl COMPACT>
<dd><code>TCL_OK</code> if all is ok, <code>TCL_ERROR</code> if an error occurred.</dl>
<h3>TkX_Main</h3>
<p>This function parses the command line according to the wish shell specification. It creates an interpreter and calls the specified function <code>appInitProc</code> to initialize any application specific commands. It then either evaluates the command of script specified on the command line or enters an interactive command loop. This procedure never returns, it exits the process when it&#8217;s done. Using the TclX wish shell gives you SIGINT handling in interactive shells, otherwise it is identical to standard wish.</p>
<h3>TclX_SetAppInfo</h3>
<p>Store the application information returned by infox. </p>
<p> Parameters</p>
<dl COMPACT>
<dd><code>o </code><i>defaultValues</i> &#8211; If true, then the values are assigned only if they are not already defined (defaulted). If false, the values are always set.<br />
 <code>o </code><i>appName</i> &#8211; Application symbolic name.<br />
 <code>o </code><i>appLongName</i> &#8211; Long, natural language application name.<br />
 <code>o </code><i>appVersion</i> &#8211; Version number of the application.<br />
 <code>o </code><i>appPatchlevel</i> &#8211; Patch level of the application. If less than zero, don&#8217;t change.</dl>
<p> String pointers are saved without copying, don&#8217;t release the memory. If the arguments are NULL, don&#8217;t change the values.</p>
<h2>Dynamic Loading Of Tclx</h2>
<p>TclX can be dynamically loaded on systems that support shared libraries and the load command. This can be done using either the <code>load</code> or the <code>package require</code> commands. If <code>package require</code> is to be used, a <code>pkgIndex,tcl</code> must be constructed. The <code>pkg_mkIndex</code> does not generate a pkgIndex.tcl file that works with TclX. Instead a command similar to </p>
<dl COMPACT>
<dd>package ifneeded Tclx 7.5.0 &quot;load $dir/libtclx.so&quot;</dl>
<p> should be placed in the directory containing the TclX shared library. A prototype <code>pkgIndex,tcl</code> file is build by TclX and is installed in the run time directory under the name <code>pkgIndex,proto</code>. This file can&#8217;t be used as-is, but should be renamed and copied or combined with an existing <code>pkgIndex,tcl</code> in the directory containing the shared library. </p>
<p> There is no need to dynamically load <code>libtkx.so</code>, since it only contains support for <code>wishx</code>. </p>
<h2>Integrating Tclx With Other Extensions And Applications</h2>
<p>The main aspects to integrating TclX with into an application is to decide if the application is based on the standard Tcl/Tk shells or the TclX shells. If the standard shells are desired, then all that is necessary is to call <code>Tclx_Init</code> after <code>Tcl_Init</code> and<br />
&nbsp;<wbr><code>Tkx_Init</code>&nbsp;<wbr>after&nbsp;<wbr><code>Tk_Init</code>.&nbsp;<wbr>&nbsp;<wbr>This functionality may also be&nbsp;<wbr> dynamically loaded. </p>
<p> To get the TclX shell in a Tcl only application, with the <code>tcl</code> command functionality, call <code>TclX_Main</code> from the <code>main</code> function instead of <code>Tcl_Main</code>. This shell has arguments conforming to other Unix shells and SIGINT signal handling when interactive,. </p>
<p> To get the Tclx shell in a Tk application, with the <code>wishx</code> command functionality, call <code>TkX_Main</code> from the <code>main</code> function instead of <code>Tk_Main</code>. This shell has SIGINT signal handling when interactive,</p>
