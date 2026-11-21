---

title: "frama-c-gui(1)"
name: "frama-c-gui"
section: "1"
letter: "f"
url: "/docs/linux/man/1-frama-c-gui/"
description: "frama-c[.byte] – a static analyzer for C programs frama-c-gui[.byte] – the graphical interface of frama-c"
---

<p> <code>frama-c</code> [ <i>options</i> ] <i>files</i> </p>
<p> <code>frama-c</code> is a suite of tools dedicated to the analysis of source code written in C. It gathers several static analysis techniques in a single collaborative framework. This framework can be extended by additional plugins placed in the <code>$FRAMAC_PLUGIN</code> directory. The command</p>
<dl>
<dt>
</dt><dd> frama-c -help</dd></dl>
<p> will provide the full list of the plugins that are currently installed. <code>frama-c-gui</code> is the graphical user interface of <code>frama-c</code>. It features the same options as the command-line version. <code>frama-c.byte&nbsp;<wbr></code>and&nbsp;<wbr><code>frama-c-gui.byte&nbsp;<wbr></code>are the ocaml bytecode versions of the command-line and graphical user interface respectively. </p>
<p> By default, Frama-C recognizes <code>.c</code> files as C files needing pre-processing and <code>.i</code> files as C files having been already pre-processed. Some plugins may extend the list of recognized files. Pre-processing can be customized through the <code>-cpp-command</code> and <code>-cpp-extra-args</code> options. </p>
<h2>OPTIONS</h2>
<p> <code>Syntax</code> Options taking an additional parameters can also be written under the form</p>
<dl>
<dt>
</dt><dd> &#8211;<i>option</i>=<i>param</i></dd></dl>
<p> This option is mandatory when <i>param</i> starts with a dash (&#8216;-&#8216;) Most options that takes no parameter have a corresponding</p>
<dl>
<dt>
</dt><dd> -no<i>-option</i></dd></dl>
<p> option which has the opposite effect. <code>General options</code></p>
<dl>
<dt><code>-add-path&nbsp;<wbr></code><i>p1[,p2[&#8230;,pn]]</i></dt>
<dd> adds directories <i>&lt;p1&gt;&nbsp;<wbr></i>through <i>&lt;pn&gt;&nbsp;<wbr></i>to the list of directories in which plugins are searched <code>-help</code> gives the list of options that control the behavior of Frama-C&#8217;s kernel and the list of installed plugins.</dd>
<dt><code>[-no]-annot</code></dt>
<dd> reads ACSL annotation. This is the default. Annotation are not pre-processed by default. Use <code>-pp-annot</code> for that.</dd>
<dt><code>[-no]-constfold</code></dt>
<dd> folds all syntactically constant expressions in the code before the analyzes. Defaults to no.</dd>
<dt><code>[-no]-continue-on-annot-error</code></dt>
<dd> When analyzing an annotation, the default behavior (the <code>-no</code> version of this option) when a typechecking error occurs is to reject the source file as is the case for typechecking errors within the C code. With this option on, the typechecker will only output a warning and discard the annotation but typechecking will continue.</dd>
<dt><code>-cpp-command&nbsp;<wbr></code><i>cmd</i></dt>
<dd> Uses <i>cmd</i> as the command to pre-process C files. Defaults to the <code>CPP</code> environment variable or to</dd>
<dt>
</dt><dd> gcc -C -E -I.</dd>
<dt>
</dt><dd> if it is not set. In order to preserve ACSL annotations, the preprocessor must keep comments (the <code>-E</code> option for gcc).</dd>
<dt><code>-cpp-extra-args&nbsp;<wbr></code><i>args</i></dt>
<dd> Gives additional arguments to the pre-processor. This is only useful when <code>-preprocess-annot</code> is set. Pre-processing annotations is done in two separate pre-processing stages. The first one is a normal pass on the C code which retains macro definitions. These are then used in the second pass during which annotations are pre-processed. <i>args</i> are used only for the first pass, so that arguments that should not be used twice (such as additional include directives or macro definitions) must thus go there instead of <code>-cpp-command</code>.</dd>
<dt><code>-float-digits&nbsp;<wbr></code><i>n</i></dt>
<dd> When outputting floating-point numbers, display <i>n</i> digits. Defaults to 4.</dd>
<dt><code>-general-font&nbsp;<wbr></code><i>f</i></dt>
<dd> Uses <i>f</i> as the general font of the GUI (the value of <code>FRAMAC_GENERALFONT</code> if defined or Helvetica by default).</dd>
<dt><code>-journal-disable</code></dt>
<dd> Do not output a journal of the current session. See <code>-journal-enable</code>.</dd>
<dt><code>-journal-enable</code></dt>
<dd> On by default, dumps a journal of all the actions performed during the current Frama-C session in the form of an ocaml script that can be replayed with <code>-load-script</code>. The name of the script can be set with the <code>-journal-name</code> option.</dd>
<dt><code>-journal-name&nbsp;<wbr></code><i>name</i></dt>
<dd> Set the name of the journal file (without the <i>.ml</i> extension). Defaults to frama_c_journal.</dd>
<dt><code>[-no]-keep-comments</code></dt>
<dd> Tries to preserve comments when pretty-printing the source code (defaults to no).</dd>
<dt><code>[-no]-keep-switch</code></dt>
<dd> When <code>-simplify-cfg</code> is set, keeps switch statements. Defaults to no.</dd>
<dt><code>[-no]-lib-entry</code></dt>
<dd> Indicates that the entry point is called during program execution. This implies in particular that global variables can not be assumed to have their initial values. The default is <code>-no-lib-entry</code>: the entry point is also the starting point of the program and globals have their initial value.</dd>
<dt><code>-load&nbsp;<wbr></code><i>file</i></dt>
<dd> load the (previously saved) state contained in <i>file</i>.</dd>
<dt><code>-load-module&nbsp;<wbr></code><i>m1[,m2[&#8230;,mn]]</i></dt>
<dd> loads the ocaml modules <i>&lt;m1&gt;</i>through <i>&lt;mn&gt;</i>. These modules must be <code>.cmxs</code>files for the native code version of Frama-c and <code>.cmo</code>or<code>.cma</code>files for the bytecode version (see the Dynlink section of Ocaml manual for more information). All modules which are present in the plugin search paths are automatically loaded.</dd>
<dt><code>-load-script&nbsp;<wbr></code><i>s1[,s2,[&#8230;,sn]]</i></dt>
<dd> loads the ocaml scripts <i>&lt;s1&gt;&nbsp;<wbr></i>through <i>&lt;sn&gt;</i>. The scripts must be <code>.ml</code>files. They must be compilable relying only on Ocaml standard library and Frama-C&#8217;s API. If some custom compilation step is needed, compile them outside of Frama-C and use <code>-load-module</code> instead.</dd>
<dt><code>-machdep&nbsp;<wbr></code><i>machine</i></dt>
<dd> uses <i>machine</i> as the current machine-dependent configuration (size of the various integer types, endiandness, &#8230;). The list of currently supported machines is available through <code>-machdep help</code> option.</dd>
<dt><code>-main&nbsp;<wbr></code><i>f</i></dt>
<dd> Sets <i>f</i> as the entry point of the analysis. Defaults to &#8216;main&#8217;. By default, it is considered as the starting point of the program under analysis. Use <code>-lib-entry</code> if <i>f</i> is supposed to be called in the middle of an execution.</dd>
<dt><code>-monospace-font&nbsp;<wbr></code><i>f</i></dt>
<dd> Uses <i>f</i> as the monospace font in the GUI (defaults to value of <code>FRAMAC_MONOSPACEFONT</code> if defined or Monospace by default).</dd>
<dt><code>-obfuscate</code></dt>
<dd> prints an obfuscated version of the code (where original identifiers are replaced by meaningless one) and exits. The correspondance table between original and new symbols is kept at the beginning of the result.</dd>
<dt><code>-ocode&nbsp;<wbr></code><i>file</i></dt>
<dd> redirects pretty-printed code to <i>file</i> instead of standard output.</dd>
<dt><code>[-no]-orig-name</code></dt>
<dd> During the normalization phase, some variables may get renamed when different variable with the name can co-exist (e.g. a global variable and a formal parameter). When this option is on, a message is printed each time this occurs. Defaults to no.</dd>
<dt><code>[-no]-overflow</code></dt>
<dd> arithmetic operations may overflow (this is the default option). The <code>-no-overflow</code> version assumes that the result of all arithmetic operations is within the bounds of the associated type</dd>
<dt><code>[-no]-pp-annot</code></dt>
<dd> pre-process annotations. This is currently only possible when using gcc (or GNU cpp) pre-processor. The default is to not pre-process annotations.</dd>
<dt><code>[-no]-print</code></dt>
<dd> pretty-prints the source code as normalized by CIL (defaults to no).</dd>
<dt><code>-print-libpath</code></dt>
<dd> outputs the directory where Frama-C kernel library is installed</dd>
<dt><code>-print-path</code></dt>
<dd> outputs the directory where Frama-C stores its data (can be overidden by the <code>FRAMAC_SHARE</code> variable)</dd>
<dt><code>-print-plugin-path</code></dt>
<dd> outputs the directory where Frama-C searchs its plugins (can be overidden by the <code>FRAMAC_PLUGIN</code> variable and the <code>-add-path</code> option)</dd>
<dt><code>-save&nbsp;<wbr></code><i>file</i></dt>
<dd> Saves Frama-C&#8217;s state into <i>file</i> after the analyzes have taken place.</dd>
<dt><code>[-no]-simplify-cfg</code></dt>
<dd> removes break, continue and switch statement before the analyzes. Defaults to no.</dd>
<dt><code>-time&nbsp;<wbr></code><i>file</i></dt>
<dd> outputs user time and date in the given <i>file</i> when Frama-C exits.</dd>
<dt><code>-typecheck</code></dt>
<dd> forces typechecking of the source files. This option is only relevant if no further analysis is requested (as typechecking will implicitely occurs before the analysis is launched).</dd>
<dt><code>-ulevel&nbsp;<wbr></code><i>n</i></dt>
<dd> syntactically unroll loops <i>n</i> times before the analysis. This can be quite costly and some plugins (e.g. the value analysis) provide more efficient ways to perform the same thing. See their respective manuals for more information.</dd>
<dt><code>[-no]-unicode</code></dt>
<dd> outputs ACSL formulas with utf8 characters. This is the default. When given the <code>-no-unicode</code> option, Frama-C will use the ASCII version instead. See the ACSL manual for the correspondance.</dd>
<dt><code>[-no]-unspecified-access</code></dt>
<dd> checks the that read/write accesses occuring in unspecified order (according to the C standard&#8217;s notion of sequence point) are performed on separate locations. This is the default. With <code>-no-unspecified-access ,</code> assumes that it is always the case.</dd>
<dt><code>-verbose&nbsp;<wbr></code><i>n</i></dt>
<dd> set verbosity level of the output to <i>n</i></dd>
<dt><code>-version</code></dt>
<dd> outputs the version string of Frama-C <code>Plugins specific options</code> For each <i>plugin</i>, the command</dd>
<dt>
</dt><dd> frama-c &#8211;<i>plugin</i>-help</dd></dl>
<p> will give the list of options that are specific to the plugin. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>FRAMAC_SHARE</code></dt>
<dd> The directory where Frama-C datas are installed.</dd>
<dt><code>FRAMAC_PLUGIN</code></dt>
<dd> A list of directory where Frama-C can find plug-ins.</dd>
<dt><code>FRAMAC_GENERALFONT</code></dt>
<dd> The default font of the GUI.</dd>
<dt><code>FRAMAC_MONOSPACEFONT</code></dt>
<dd> The default font for pretty-printing code in the GUI.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>Frama-C homepage</i>, <a rel="nofollow" href="http://frama-c.cea.fr">http://frama-c.cea.fr</a> </p>
