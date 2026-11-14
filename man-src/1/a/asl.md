---
title: "asl(1)"
name: "asl"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asl/"
description: "asl – cross assembler for microprocessors and -controllers"
---

<h2 class="name">NAME</h2>
<p> <code>asl &#8211; cross assembler for microprocessors and -controllers</code></p>
<h2>SYNTAX</h2>
<p> <code>asl </code> [ option(s) ] file(s) [ option(s) ] file(s) &#8230; </p>
<h2>DESCRIPTION</h2>
<p> AS is a cross assembler that can be used to write assembler programs for a variety of different microprocessors and -controllers. <code>asl</code> is the UNIX/C implementation of AS. A complete description of AS is far beyond the scope of this manual page, which is only intended as a quick reference for AS&#8217;s command line interface. For a more detailed introduction into the usage of AS, see the user&#8217;s manual. </p>
<h2>COMMAND-LINE PARAMETERS</h2>
<p> Every argument that starts with a slash (/), plus (+) or minus (-) sign is regarded as a command-line parameter. Some command-line parameters take an argument as additional parameter. Every argument that is not recognized as a command-line parameter is regarded as an assembler source file to be assembled. A source file name that does not have an extension is automatically extended with the default extension &#8216;.asm&#8217;. Options are turned on with a parameter starting with a slash (/) or minus sign (-), whereas a parameter with a leading plus sign (+) turns an option off. In the following list, all options will be shown in the form that is needed to change the default behaviour, which might be a plus or minus sign, depening on wether the option is on or off by default. </p>
<p> <code>asl</code> accepts the following command-line parameters:</p>
<dl>
<dt><code>-A</code></p>
<dd>
<p> Change the data structure that is internally used to store the symbol table. By default, AS uses binary trees to store macro and symbol definitions. Turning this option on will change this to AVL-balanced trees. Depending on the ratio of symbol entries and lookups, this might speed up assembly. Using AVL-balanced trees helps also reducing the stack usage, which is however irrelevant for the C version of AS.</p>
<dt><code>-a</code></p>
<dd>
<p> Instruct AS to write out the shared symbol definitions in a format suitable for including into an AS assembler program. The file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.inc&#8217;. See the user manual for more information about symbol sharing.</p>
<dt><code>-cpu &lt;name&gt;</code></p>
<dd> Set the target processor to &lt;name&gt;. Use this option if the source file does not contain a CPU statement.</p>
<dt><code>-alias &lt;new name=old name&gt;</code></p>
<dd> Define a CPU alias. An alias is a name that can be used as an argument to the CPU pseudo-instruction just like an intrinsic CPU type. Its usage will set the same target as the old name, however the predefined symbols MOMCPU and MOMCPUNAME will be set to the new name. This option is primarily useful for adding a new member to a processor family that has the same core, but is different in its internal peripherals, thus allowing to distinguish between them.</p>
<dt><code>-C</code></p>
<dd>
<p> Add a cross reference table to the assembler listing. A cross reference table lists all symbols that have been referenced at least once during assembly, including the source line number(s) and count of every reference. This option only makes sense when the generation of an assembly listing has been turned on via the <code>-L</code> or <code>-l</code> parameters.</p>
<dt><code>-c</code></p>
<dd>
<p> Instruct AS to write out the shared symbol definitions in a format suitable for including into a C program. The file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.h&#8217;. See the user manual for more information about symbol sharing.</p>
<dt><code>-D &lt;name[=value]&gt;[,&#8230;]</code></p>
<dd> Pre-define symbols. Predefined symbols are entered into the global symbol table prior to assembly of the source file(s). If no value is given for a symbol, it is assigned the integer value 1. Value expressions may contain arithmetic expressions as described in the user manual, but they may not reference any other predefined or internal symbols.</p>
<dt><code>-E [file]</code></p>
<dd> Force AS to send warning and error messages to <code>file</code> rather than to the standard error output. The file names !0 to !4 are used to refer to the standard input, output, error, auxilliary, and printer channels predefined by the operating system (on some systems, some of these handles might not exist). If the [file] specification is omitted, a name is constructed by replacing the source file&#8217;s extension with &#8216;.log&#8217;.</p>
<dt><code>+G</code></p>
<dd> Supress code generation, reducing the functionality of AS to macro preprocessing.</p>
<dt><code>-g [MAP|Atmel|NoICE]</code></p>
<dd>
<p> Instruct AS to write an additional file containing debug information. This information covers the symbol table and the relation between source line numbers and machine addresses. The argument specifies whether debug info shall be written in AS&#8217;s own MAP format, the object format for Atmel&#8217;s AVR tools, or a command file suitable for John Hartman&#8217;s NoICE. If no argument is given, MAP will be chosen. The file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.map&#8217;, &#8216;.obj&#8217;, or &#8216;.noi&#8217; respectively.</p>
<dt><code>-gnuerrors</code></p>
<dd>
<p> Output errors and their location in the source code in a format similar to the GNU C compiler, thus making it easier to integrate AS into environments designed for this format. Note that in contrast to the standard format used by AS, locations inside are not reported!</p>
<dt><code>-h</code></p>
<dd>
<p> Force AS to print all hexadecimal constants with lowercase letters, rather than with uppercase letters A..F which is the default.</p>
<dt><code>-i &lt;path[:path&#8230;]&gt;</code></p>
<dd> Add new entries to the list of paths that are searched for include files. New entries are prepended to the current include path list, so if multiple paths are given with one command-line parameter, they will be entered into the path list in reverse order.</p>
<dt><code>-I</code></p>
<dd>
<p> Add an include file list to the assembly listing. An include file list contains all files that have been included while assembling the source files, including multiple and nested inclusion. Nesting of inclusion is identified by different indention. This option only makes sense when the generation of an assembly listing has been turned on via the <code>-L</code> or <code>-l</code> parameters.</p>
<dt><code>-L</code></p>
<dd>
<p> Turn on generation of an assembly listing and send it to a file whose name is constructed by replacing the source file&#8217;s extension with &#8216;.lst&#8217;.</p>
<dt><code>-l</code></p>
<dd>
<p> Turn on generation of an assembly listing and send it to the console.</p>
<dt><code>-M</code></p>
<dd>
<p> Turn on generation of a macro definition file. A macro definition file is a file that contains all macro definitions that have been detected during assembly, in a format suitable for an inclusion into another file. The macro definition file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.mac&#8217;.</p>
<dt><code>-n</code></p>
<dd>
<p> Force AS to extend all error and warning messages with their internal error resp. warning number.</p>
<dt><code>-noicemask [mask]</code></p>
<dd> By default, AS will only write symbols to the NoICE debug info that are located in the code segment. By changing this binary mask, more and/or different masks may be chosen. The assignment is bit 1=code, 2=data, 3=idata, 4=xdata, 5=ydata, 6=bitdata, 7=io, 8=reg, 9=romdata . Negating this option reverts the mask to code-only.</p>
<dt><code>-o &lt;name&gt;</code></p>
<dd> Tell AS to write the code output to a file &lt;name&gt;. By default, the code output file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.p&#8217;. If multiple files are assembled with one command, this parameter may also be given multiply. If there are less output specifications than source file names, AS will switch back to the default naming convention after all output specifications have been used up.</p>
<dt><code>-olist &lt;name&gt;</code></p>
<dd>
<p> Tell AS to write the assembly lsting to a file &lt;name&gt;, instead of a file with the standard name in the source file&#8217;s directory. This option only makes sense when an assembly listing has been requested via the &#8216;-L&#8217; option.</p>
<dt><code>-shareout &lt;name&gt;</code></p>
<dd>
<p> Tell AS to write shared symbol definitions to a file &lt;name&gt;, instead of constructing the name from the source file&#8217;s name. See the user manual for more information about symbol sharing.</p>
<dt><code>-P</code></p>
<dd>
<p> Turn on generation of a macro output file. A macro output file contains the intermediate source code that remains after macro expansion and conditional assembly. The macro output file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.i&#8217;.</p>
<dt><code>-p</code></p>
<dd>
<p> Instruct AS to write out the shared symbol definitions in a format suitable for including into a Pascal or Modula-2 program. The file&#8217;s name is constructed by replacing the source file&#8217;s extension with &#8216;.inc&#8217;. See the user manual for more information about symbol sharing.</p>
<dt><code>-q or -quiet</code></p>
<dd> Turn on silent assembly mode. In silent compilation mode, AS will not do any console output except for warning and error messages.</p>
<dt><code>-r [pass number]</code></p>
<dd> Tell AS to output warnings when a situation appears in a source file that forces another pass of assembly. Such situations either take place when a symbol is undefined in the first pass or a symbol&#8217;s value has changed compared to the previous pass. This option is useful to track down sources of excessive multi-passing, but be aware that it might yield a fairly large number of warnings, especially in the first pass. Optionally, a pass number may be added to this option to inhibit output until a certain pass is reached.</p>
<dt><code>-s</code></p>
<dd>
<p> Add a section list to the assembly listing. A section list contains all sections that have been defined in the source files, marking their nesting level by different levels of indentation. This option only makes sense when the generation of an assembly listing has been turned on via the <code>-L</code> or <code>-l</code> parameters.</p>
<dt><code>-t &lt;mask&gt;</code></p>
<dd> Turn on or off parts of the assembly listing that have no individual command line parameter. AS internally keeps an integer value whose bits represent certain components of the listing. A positive command line parameter (-t or /t) sets the bits set in &lt;mask&gt;, whereas a negated parameter (+t) resets the bits set in &lt;mask&gt;. The individual bits have the following meaning: bit 0 = source lines and generated machine code, bit 1 = symbol table, bit 2 = macro table, bit 3 = function table, bit 4 = line numbering.</p>
<dt><code>-u</code></p>
<dd>
<p> Tell AS to do additional bookkeeping about which address ranges have been used by the assembled program. This option enables the detection of overlapping memory usage. If an assembly listing has been turned on via the <code>-L</code> or <code>-l</code> parameters, it will also contain a list of all used memory areas.</p>
<dt><code>-U </code></p>
<dd>
<p> Force AS to operate in case-sensitive mode. By default, names of symbols, macros, user-defined functions and sections are treated in a case-insensitive manner.</p>
<dt><code>-w</code></p>
<dd>
<p> Suppress output of warnings.</p>
<dt><code>-x</code></p>
<dd>
<p> Turn on extended error reporting. With extended error reporting, several error and warning messages will also print the item that created the message, e.g. the name of an unknown instruction. When this option is given twice, the erroneous source line is additinally printed. </p>
</dl>
<h2>PRESETTING PARAMETERS</h2>
<p> Parameters need not neccessarily be given in the command line itself. Before processing of command line parameters starts, AS will look if the <code>ASCMD</code> environment variable is defined. If it exists, its contents will be treated as additional command line parameters whose syntax is absolutely equal to normal command line parameters. An exception is made if the variable&#8217;s contents start with a &#8216;@&#8217; sign; in such a case, the string after the &#8216;@&#8217; sign is treated as the name of a file that contains the options. Such a file (also called a &#8216;key file&#8217;) has the advantage that it allows the options to be written in different lines, and it does not have a size limit. Some operating systems (like MS-DOS) have a length limit on command lines and environment variable contents, so the key file may be your only option if you have a lot of lengthy parameters for AS. </p>
<p> As parameters given in the <code>ASCMD</code> environment variable or a key file are processed prior to the command line itself, and can therefore be overridden by command line parameters. </p>
<h2>NATIONAL LANGUAGE SUPPORT</h2>
<p> AS supports the needs of different languages and countries in the sense that it will try to adapt to the language and date/time formats valid for the current environment. Upon startup, the COUNTRY setting made in the CONFIG.SYS file is queried for DOS and OS/2 implementations of AS. For UNIX systems, AS tries to read the LC_TIME resp. LC_MESSAGES environment variables to find out the correct format for date/time outputs resp. the local language. If this fails, the LC_ALL and finally LANG variables are probed. If none of these environment variables points to a specific local environment resp. contains a locale specification unknown to AS, the standard english/C locale is used. </p>
<p> The messages AS can output in different languages are stored in separate files with the extension &#8216;.msg&#8217; . AS will search for these files in the following directories: </p>
<p> &#8211; The current directory </p>
<p> &#8211; The directory the executable of AS was loaded from (only on DOS platforms version &gt;=3.0 or if path was explicitly specified) </p>
<p> &#8211; The directory specified in the AS_MSGPATH environment variable resp. the directories listed in the PATH environment variable if AS_MSGPATH does not exist. </p>
<p> &#8211; The LIBDIR directory set at compile time from the Makefile. </p>
<h2>RETURN CODES</h2>
<p> Depending on the assembly&#8217;s turnout, <code>asl</code> will generate different return codes:</p>
<dl>
<dt><code>0</code></p>
<dd> No errors, warnings might have occured.</p>
<dt><code>1</code></p>
<dd> No command line parameters were given, AS printed a short list of possible command line parameters and terminated thereafter.</p>
<dt><code>2</code></p>
<dd> Errors occured during assembly of at least one source file, no code file was generated for the corresponding source file(s).</p>
<dt><code>3</code></p>
<dd> A fatal error occured during assembly that forced immediate program termination. Code files may be generated, but are probably unusuable.</p>
<dt><code>4</code></p>
<dd> Program termination already occured during initialization. This might be either due to a incorrect command line parameter or an error during loading the program&#8217;s overlay file (only possible on MS-DOS).</p>
<dt><code>255</code></p>
<dd> During initialization, an internal error happened that should not occur. If the reaction is reproducable, note down the situation and send a bug report to the author. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To assemble a source file <code>file1.asm</code> without any additional bells and whistles, use: </p>
<p> <code>asl file1</code> </p>
<p> which will create an output file <code>file1.p</code> given that there are no errors. If you additionally want a listing and rename the output file to <code>a.out,</code> use </p>
<p> <code>asl -L file1 -o a.out</code> </p>
<p> To make the listing as comprehensive as possible and to get more detailed error messages, use: </p>
<p> <code>asl -LuCIs -t 16 -nx file1</code> </p>
<h2>TIPS</h2>
<p> calling AS without any parameters will print a short help containing all command line parameters and implemented target processors, while calling with command line parameters but without any source file name will result in AS asking for a source file name on the console. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-plist/">plist</a>(1), <a href="/docs/linux/man/1-pbind/">pbind</a>(1), <a href="/docs/linux/man/1-p2hex/">p2hex</a>(1), <a href="/docs/linux/man/1-p2bin/">p2bin</a>(1) </p>
<h2>HISTORY</h2>
<p> AS originally appeared as a DOS program in 1989, written in Borland-Pascal, and was ported to C and UNIX in 1996. </p>
<h2>BUGS</h2>
<p> There are too many options. </p>
<p> Command line interpreters of some operating systems reserve some characters for their own use, so it might be necessary to give command line parameters with certain tricks (e.g., with the help of escape characters). </p>
<h2>AUTHOR(S)</h2>
<p> Alfred Arnold (alfred [at] ccac.rwth-aachen.de), and a few others&#8230; </p>
<h2>Index</h2>
