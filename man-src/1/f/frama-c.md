---
title: "frama-c(1)"
name: "frama-c"
section: "1"
letter: "f"
url: "/docs/linux/man/1-frama-c/"
description: "frama-c[.byte] – a static analyzer for C programs frama-c-gui[.byte] – the graphical interface of frama-c"
---

<h2 class="name">NAME</h2>
<p> frama-c[.byte] &#8211; a static analyzer for C programs frama-c-gui[.byte] &#8211; the graphical interface of frama-c</p>
<h2>SYNOPSIS</h2>
<p> <code>frama-c</code> [ <i>options</i> ] <i>files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>frama-c</code> is a suite of tools dedicated to the analysis of source code written in C. It gathers several static analysis techniques in a single collaborative framework. This framework can be extended by additional plugins placed in the <code>$FRAMAC_PLUGIN</code> directory. The command</p>
<dl>
<dt>
<dd> frama-c -help</dl>
<p> will provide the full list of the plugins that are currently installed. <code>frama-c-gui</code> is the graphical user interface of <code>frama-c</code>. It features the same options as the command-line version. <code>frama-c.byte&nbsp;<wbr></code>and&nbsp;<wbr><code>frama-c-gui.byte&nbsp;<wbr></code>are the ocaml bytecode versions of the command-line and graphical user interface respectively. </p>
<p> By default, Frama-C recognizes <code>.c</code> files as C files needing pre-processing and <code>.i</code> files as C files having been already pre-processed. Some plugins may extend the list of recognized files. Pre-processing can be customized through the <code>-cpp-command</code> and <code>-cpp-extra-args</code> options. </p>
<h2>OPTIONS</h2>
<p> <code>Syntax</code> Options taking an additional parameters can also be written under the form</p>
<dl>
<dt>
<dd> &#8211;<i>option</i>=<i>param</i></dl>
<p> This option is mandatory when <i>param</i> starts with a dash (&#8216;-&#8216;) Most options that takes no parameter have a corresponding</p>
<dl>
<dt>
<dd> -no<i>-option</i></dl>
<p> option which has the opposite effect. <code>General options</code></p>
<dl>
<dt><code>-add-path&nbsp;<wbr></code><i>p1[,p2[&#8230;,pn]]</i></p>
<dd> adds directories <i>&lt;p1&gt;&nbsp;<wbr></i>through <i>&lt;pn&gt;&nbsp;<wbr></i>to the list of directories in which plugins are searched <code>-help</code> gives the list of options that control the behavior of Frama-C&#8217;s kernel and the list of installed plugins.</p>
<dt><code>[-no]-annot</code></p>
<dd> reads ACSL annotation. This is the default. Annotation are not pre-processed by default. Use <code>-pp-annot</code> for that.</p>
<dt><code>[-no]-constfold</code></p>
<dd> folds all syntactically constant expressions in the code before the analyzes. Defaults to no.</p>
<dt><code>[-no]-continue-on-annot-error</code></p>
<dd> When analyzing an annotation, the default behavior (the <code>-no</code> version of this option) when a typechecking error occurs is to reject the source file as is the case for typechecking errors within the C code. With this option on, the typechecker will only output a warning and discard the annotation but typechecking will continue.</p>
<dt><code>-cpp-command&nbsp;<wbr></code><i>cmd</i></p>
<dd> Uses <i>cmd</i> as the command to pre-process C files. Defaults to the <code>CPP</code> environment variable or to</p>
<dt>
<dd> gcc -C -E -I.</p>
<dt>
<dd> if it is not set. In order to preserve ACSL annotations, the preprocessor must keep comments (the <code>-E</code> option for gcc).</p>
<dt><code>-cpp-extra-args&nbsp;<wbr></code><i>args</i></p>
<dd> Gives additional arguments to the pre-processor. This is only useful when <code>-preprocess-annot</code> is set. Pre-processing annotations is done in two separate pre-processing stages. The first one is a normal pass on the C code which retains macro definitions. These are then used in the second pass during which annotations are pre-processed. <i>args</i> are used only for the first pass, so that arguments that should not be used twice (such as additional include directives or macro definitions) must thus go there instead of <code>-cpp-command</code>.</p>
<dt><code>-float-digits&nbsp;<wbr></code><i>n</i></p>
<dd> When outputting floating-point numbers, display <i>n</i> digits. Defaults to 4.</p>
<dt><code>-general-font&nbsp;<wbr></code><i>f</i></p>
<dd> Uses <i>f</i> as the general font of the GUI (the value of <code>FRAMAC_GENERALFONT</code> if defined or Helvetica by default).</p>
<dt><code>-journal-disable</code></p>
<dd> Do not output a journal of the current session. See <code>-journal-enable</code>.</p>
<dt><code>-journal-enable</code></p>
<dd> On by default, dumps a journal of all the actions performed during the current Frama-C session in the form of an ocaml script that can be replayed with <code>-load-script</code>. The name of the script can be set with the <code>-journal-name</code> option.</p>
<dt><code>-journal-name&nbsp;<wbr></code><i>name</i></p>
<dd> Set the name of the journal file (without the <i>.ml</i> extension). Defaults to frama_c_journal.</p>
<dt><code>[-no]-keep-comments</code></p>
<dd> Tries to preserve comments when pretty-printing the source code (defaults to no).</p>
<dt><code>[-no]-keep-switch</code></p>
<dd> When <code>-simplify-cfg</code> is set, keeps switch statements. Defaults to no.</p>
<dt><code>[-no]-lib-entry</code></p>
<dd> Indicates that the entry point is called during program execution. This implies in particular that global variables can not be assumed to have their initial values. The default is <code>-no-lib-entry</code>: the entry point is also the starting point of the program and globals have their initial value.</p>
<dt><code>-load&nbsp;<wbr></code><i>file</i></p>
<dd> load the (previously saved) state contained in <i>file</i>.</p>
<dt><code>-load-module&nbsp;<wbr></code><i>m1[,m2[&#8230;,mn]]</i></p>
<dd> loads the ocaml modules <i>&lt;m1&gt;</i>through <i>&lt;mn&gt;</i>. These modules must be <code>.cmxs</code>files for the native code version of Frama-c and <code>.cmo</code>or<code>.cma</code>files for the bytecode version (see the Dynlink section of Ocaml manual for more information). All modules which are present in the plugin search paths are automatically loaded.</p>
<dt><code>-load-script&nbsp;<wbr></code><i>s1[,s2,[&#8230;,sn]]</i></p>
<dd> loads the ocaml scripts <i>&lt;s1&gt;&nbsp;<wbr></i>through <i>&lt;sn&gt;</i>. The scripts must be <code>.ml</code>files. They must be compilable relying only on Ocaml standard library and Frama-C&#8217;s API. If some custom compilation step is needed, compile them outside of Frama-C and use <code>-load-module</code> instead.</p>
<dt><code>-machdep&nbsp;<wbr></code><i>machine</i></p>
<dd> uses <i>machine</i> as the current machine-dependent configuration (size of the various integer types, endiandness, &#8230;). The list of currently supported machines is available through <code>-machdep help</code> option.</p>
<dt><code>-main&nbsp;<wbr></code><i>f</i></p>
<dd> Sets <i>f</i> as the entry point of the analysis. Defaults to &#8216;main&#8217;. By default, it is considered as the starting point of the program under analysis. Use <code>-lib-entry</code> if <i>f</i> is supposed to be called in the middle of an execution.</p>
<dt><code>-monospace-font&nbsp;<wbr></code><i>f</i></p>
<dd> Uses <i>f</i> as the monospace font in the GUI (defaults to value of <code>FRAMAC_MONOSPACEFONT</code> if defined or Monospace by default).</p>
<dt><code>-obfuscate</code></p>
<dd> prints an obfuscated version of the code (where original identifiers are replaced by meaningless one) and exits. The correspondance table between original and new symbols is kept at the beginning of the result.</p>
<dt><code>-ocode&nbsp;<wbr></code><i>file</i></p>
<dd> redirects pretty-printed code to <i>file</i> instead of standard output.</p>
<dt><code>[-no]-orig-name</code></p>
<dd> During the normalization phase, some variables may get renamed when different variable with the name can co-exist (e.g. a global variable and a formal parameter). When this option is on, a message is printed each time this occurs. Defaults to no.</p>
<dt><code>[-no]-overflow</code></p>
<dd> arithmetic operations may overflow (this is the default option). The <code>-no-overflow</code> version assumes that the result of all arithmetic operations is within the bounds of the associated type</p>
<dt><code>[-no]-pp-annot</code></p>
<dd> pre-process annotations. This is currently only possible when using gcc (or GNU cpp) pre-processor. The default is to not pre-process annotations.</p>
<dt><code>[-no]-print</code></p>
<dd> pretty-prints the source code as normalized by CIL (defaults to no).</p>
<dt><code>-print-libpath</code></p>
<dd> outputs the directory where Frama-C kernel library is installed</p>
<dt><code>-print-path</code></p>
<dd> outputs the directory where Frama-C stores its data (can be overidden by the <code>FRAMAC_SHARE</code> variable)</p>
<dt><code>-print-plugin-path</code></p>
<dd> outputs the directory where Frama-C searchs its plugins (can be overidden by the <code>FRAMAC_PLUGIN</code> variable and the <code>-add-path</code> option)</p>
<dt><code>-save&nbsp;<wbr></code><i>file</i></p>
<dd> Saves Frama-C&#8217;s state into <i>file</i> after the analyzes have taken place.</p>
<dt><code>[-no]-simplify-cfg</code></p>
<dd> removes break, continue and switch statement before the analyzes. Defaults to no.</p>
<dt><code>-time&nbsp;<wbr></code><i>file</i></p>
<dd> outputs user time and date in the given <i>file</i> when Frama-C exits.</p>
<dt><code>-typecheck</code></p>
<dd> forces typechecking of the source files. This option is only relevant if no further analysis is requested (as typechecking will implicitely occurs before the analysis is launched).</p>
<dt><code>-ulevel&nbsp;<wbr></code><i>n</i></p>
<dd> syntactically unroll loops <i>n</i> times before the analysis. This can be quite costly and some plugins (e.g. the value analysis) provide more efficient ways to perform the same thing. See their respective manuals for more information.</p>
<dt><code>[-no]-unicode</code></p>
<dd> outputs ACSL formulas with utf8 characters. This is the default. When given the <code>-no-unicode</code> option, Frama-C will use the ASCII version instead. See the ACSL manual for the correspondance.</p>
<dt><code>[-no]-unspecified-access</code></p>
<dd> checks the that read/write accesses occuring in unspecified order (according to the C standard&#8217;s notion of sequence point) are performed on separate locations. This is the default. With <code>-no-unspecified-access ,</code> assumes that it is always the case.</p>
<dt><code>-verbose&nbsp;<wbr></code><i>n</i></p>
<dd> set verbosity level of the output to <i>n</i></p>
<dt><code>-version</code></p>
<dd> outputs the version string of Frama-C <code>Plugins specific options</code> For each <i>plugin</i>, the command</p>
<dt>
<dd> frama-c &#8211;<i>plugin</i>-help</dl>
<p> will give the list of options that are specific to the plugin. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>FRAMAC_SHARE</code></p>
<dd> The directory where Frama-C datas are installed.</p>
<dt><code>FRAMAC_PLUGIN</code></p>
<dd> A list of directory where Frama-C can find plug-ins.</p>
<dt><code>FRAMAC_GENERALFONT</code></p>
<dd> The default font of the GUI.</p>
<dt><code>FRAMAC_MONOSPACEFONT</code></p>
<dd> The default font for pretty-printing code in the GUI.</dl>
<h2>SEE ALSO</h2>
<p> <i>Frama-C homepage</i>, <a rel="nofollow" href="http://frama-c.cea.fr">http://frama-c.cea.fr</a> </p>
<h2>Index</h2>
