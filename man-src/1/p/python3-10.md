---
title: "python3-10(1)"
name: "python3-10"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python3-10/"
description: "python – an interpreted, interactive, object-oriented programming language"
---

<p>python &#8211; an interpreted, interactive, object-oriented programming language </p>
<h2>Synopsis</h2>
<p><code>python</code> [ <code>-B</code> ] [ <code>-b</code> ] [ <code>-d</code> ] [ <code>-E</code> ] [ <code>-h</code> ] [ <code>-i</code> ] [ <code>-I</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-m</code> <i>module-name</i> ] [ <code>-q</code> ] [ <code>-O</code> ] [ <code>-OO</code> ] [ <code>-s</code> ] [ <code>-S</code> ] [ <code>-u</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-v</code> ] [ <code>-V</code> ] [ <code>-W</code> <i>argument</i> ] [ <code>-x</code> ] [ <code>-X</code> <i>option</i> ] [ <code>-?</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>&#8211;check-hash-based-pycs</code> <i>default</i> | <i>always</i> | <i>never</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>-c</code> <i>command</i> | <i>script</i> | &#8211; ] [ <i>arguments</i> ]</p>
<h2>Description</h2>
<p>Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax. For an introduction to programming in Python, see the Python Tutorial. The Python Library Reference documents built-in and standard types, constants, functions and modules. Finally, the Python Reference Manual describes the syntax and semantics of the core language in (perhaps too) much detail. (These documents may be located via the <code>INTERNET RESOURCES</code> below; they may be installed on your system as well.) </p>
<p> Python&#8217;s basic power can be extended with your own modules written in C or C++. On most systems such modules may be dynamically loaded. Python is also adaptable as an extension language for existing applications. See the internal documentation for hints. </p>
<p> Documentation for installed Python modules and packages can be viewed by running the <code>pydoc</code> program.</p>
<h2>Command Line Options</h2>
<dl COMPACT>
<dt><code>-B</code></p>
<dd>Don&#8217;t write <i>.pyc</i> files on import. See also PYTHONDONTWRITEBYTECODE.</p>
<dt><code>-b</code></p>
<dd>Issue warnings about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytearray with str. (-bb: issue errors)</p>
<dt><code>-c </code><i>command</i></p>
<dd>Specify the command to execute (see next section). This terminates the option list (following options are passed as arguments to the command).</p>
<dt><code>&#8211;check-hash-based-pycs </code><i>mode</i></p>
<dd>Configure how Python evaluates the up-to-dateness of hash-based .pyc files.</p>
<dt><code>-d</code></p>
<dd>Turn on parser debugging output (for expert only, depending on compilation options).</p>
<dt><code>-E</code></p>
<dd>Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.</p>
<dt><code>-h , -? , &#8211;help</code></p>
<dd>Prints the usage for the interpreter executable and exits.</p>
<dt><code>-i</code></p>
<dd>When a script is passed as first argument or the <code>-c</code> option is used, enter interactive mode after executing the script or the command. It does not read the $PYTHONSTARTUP file. This can be useful to inspect global variables or a stack trace when a script raises an exception.</p>
<dt><code>-I</code></p>
<dd>Run Python in isolated mode. This also implies <code>-E</code> and <code>-s</code>. In isolated mode sys.path contains neither the script&#8217;s directory nor the user&#8217;s site-packages directory. All PYTHON* environment variables are ignored, too. Further restrictions may be imposed to prevent the user from injecting malicious code.</p>
<dt><code>-m </code><i>module-name</i></p>
<dd>Searches <i>sys.path</i> for the named module and runs the corresponding <i>.py</i> file as a script. This terminates the option list (following options are passed as arguments to the module).</p>
<dt><code>-O</code></p>
<dd>Remove assert statements and any code conditional on the value of __debug__; augment the filename for compiled (bytecode) files by adding .opt-1 before the .pyc extension.</p>
<dt><code>-OO</code></p>
<dd>Do <code>-O</code> and also discard docstrings; change the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension.</p>
<dt><code>-q</code></p>
<dd>Do not print the version and copyright messages. These messages are also suppressed in non-interactive mode.</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t add user site directory to sys.path.</p>
<dt><code>-S</code></p>
<dd>Disable the import of the module <i>site</i> and the site-dependent manipulations of <i>sys.path</i> that it entails. Also disable these manipulations if <i>site</i> is explicitly imported later.</p>
<dt><code>-u</code></p>
<dd>Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.</p>
<dt><code>-v</code></p>
<dd>Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.</p>
<dt><code>-V , &#8211;version</code></p>
<dd>Prints the Python version number of the executable and exits. When given twice, print more information about the build. </p>
<dt><code>-W </code><i>argument</i></p>
<dd>Warning control. Python&#8217;s warning machinery by default prints warning messages to <i>sys.stderr</i>. </p>
<p> The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default): </p>
<p>&nbsp;<wbr>&nbsp;-Wdefault&nbsp;<wbr>&nbsp;#&nbsp;Warn once per call location<br />
&nbsp;<wbr>&nbsp;-Werror&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Convert to exceptions<br />
&nbsp;<wbr>&nbsp;-Walways&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Warn every time<br />
&nbsp;<wbr>&nbsp;-Wmodule&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Warn once per calling module<br />
&nbsp;<wbr>&nbsp;-Wonce&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Warn once per Python process<br />
&nbsp;<wbr>&nbsp;-Wignore&nbsp;<wbr>&nbsp;<wbr>&nbsp;#&nbsp;Never warn </p>
<p> The action names can be abbreviated as desired and the interpreter will resolve them to the appropriate action name. For example, <code>-Wi</code> is the same as <code>-Wignore .</code> </p>
<p> The full form of argument is: <i>action:message:category:module:lineno</i> </p>
<p> Empty fields match all values; trailing empty fields may be omitted. For example <code>-W ignore::DeprecationWarning</code> ignores all DeprecationWarning warnings. </p>
<p> The <i>action</i> field is as explained above but only applies to warnings that match the remaining fields. </p>
<p> The <i>message</i> field must match the whole printed warning message; this match is case-insensitive. </p>
<p> The <i>category</i> field matches the warning category (ex: &quot;DeprecationWarning&quot;). This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category. </p>
<p> The <i>module</i> field matches the (fully-qualified) module name; this match is case-sensitive. </p>
<p> The <i>lineno</i> field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number. </p>
<p> Multiple <code>-W</code> options can be given; when a warning matches more than one option, the action for the last matching option is performed. Invalid <code>-W</code> options are ignored (though, a warning message is printed about invalid options when the first warning is issued). </p>
<p> Warnings can also be controlled using the <code>PYTHONWARNINGS</code> environment variable and from within a Python program using the warnings module. For example, the warnings.filterwarnings() function can be used to use a regular expression on the warning message. </p>
<dt><code>-X </code><i>option</i></p>
<dd>Set implementation specific option. The following options are available: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X faulthandler: enable faulthandler </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X showrefcount: output the total reference count and number of used<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory blocks when the program finishes or after each statement in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;interactive interpreter. This only works on debug builds </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X tracemalloc: start tracing Python memory allocations using the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tracemalloc module. By default, only the most recent frame is stored in a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;traceback of a trace. Use -X tracemalloc=NFRAME to start tracing with a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;traceback limit of NFRAME frames </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X importtime: show how long each import takes. It shows module name,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cumulative time&nbsp;(including nested imports)&nbsp;and self time&nbsp;(excluding<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nested imports). Note that its output may be broken in multi-threaded<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;application. Typical usage is python3 -X importtime -c&nbsp;&#8216;import asyncio&#8217; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X dev: enable CPython&#8217;s&nbsp;&quot;development mode&quot;, introducing additional runtime<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks which are too expensive to be enabled by default. It will not be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;more verbose than the default if the code is correct: new warnings are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;only emitted when an issue is detected. Effect of the developer mode:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Add default warning filter, as -W default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Install debug hooks on memory allocators: see the PyMem_SetupDebugHooks()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;C function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Enable the faulthandler module to dump the Python traceback on a crash<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Enable asyncio debug mode<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Set the dev_mode attribute of sys.flags to True<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;io.IOBase destructor logs close()&nbsp;exceptions </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X utf8: enable UTF-8 mode for operating system interfaces, overriding the default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locale-aware mode. -X utf8=0 explicitly disables UTF-8 mode&nbsp;(even when it would<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;otherwise activate automatically). See PYTHONUTF8 for more details </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X pycache_prefix=PATH: enable writing .pyc files to a parallel tree rooted at the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;given directory instead of to the code tree. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-X warn_default_encoding: enable opt-in EncodingWarning for&nbsp;&#8216;encoding=None&#8217; </p>
<dt><code>-x</code></p>
<dd>Skip the first line of the source. This is intended for a DOS specific hack only. Warning: the line numbers in error messages will be off by one!</dl>
<h2>Interpreter Interface</h2>
<p>The interpreter interface resembles that of the UNIX shell: when called with standard input connected to a tty device, it prompts for commands and executes them until an EOF is read; when called with a file name argument or with a file as standard input, it reads and executes a <i>script</i> from that file; when called with <code>-c</code> <i>command</i>, it executes the Python statement(s) given as <i>command</i>. Here <i>command</i> may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements! In non-interactive mode, the entire input is parsed before it is executed. </p>
<p> If available, the script name and additional arguments thereafter are passed to the script in the Python variable <i>sys.argv</i>, which is a list of strings (you must first <i>import sys</i> to be able to access it). If no script name is given, <i>sys.argv[0]</i> is an empty string; if <code>-c</code> is used, <i>sys.argv[0]</i> contains the string <i>&#8216;-c&#8217;.</i> Note that options interpreted by the Python interpreter itself are not placed in <i>sys.argv</i>. </p>
<p> In interactive mode, the primary prompt is `&gt;&gt;&gt;&#8217;; the second prompt (which appears when a command is not complete) is `&#8230;&#8217;. The prompts can be changed by assignment to <i>sys.ps1</i> or <i>sys.ps2</i>. The interpreter quits when it reads an EOF at a prompt. When an unhandled exception occurs, a stack trace is printed and control returns to the primary prompt; in non-interactive mode, the interpreter exits after printing the stack trace. The interrupt signal raises the <i>KeyboardInterrupt</i> exception; other UNIX signals are not caught (except that SIGPIPE is sometimes ignored, in favor of the <i>IOError</i> exception). Error messages are written to stderr.</p>
<h2>Files And Directories</h2>
<p>These are subject to difference depending on local installation conventions; ${prefix} and ${exec_prefix} are installation-dependent and should be interpreted as for GNU software; they may be the same. On Debian GNU/{Hurd,Linux} the default for both is <i>/usr</i>.</p>
<dl COMPACT>
<dt><i>${exec_prefix}/bin/python</i></p>
<dd>Recommended location of the interpreter.</dl>
<p> <i>${prefix}/lib/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/lib/python&lt;version&gt;</i></p>
<dl COMPACT>
<dd>Recommended locations of the directories containing the standard modules.</dl>
<p> <i>${prefix}/include/python&lt;version&gt;</i><br />
 <i>${exec_prefix}/include/python&lt;version&gt;</i></p>
<dl COMPACT>
<dd>Recommended locations of the directories containing the include files needed for developing Python extensions and embedding the interpreter.</dl>
<h2>Environment Variables</h2>
<dl COMPACT>
<dt>PYTHONHOME</p>
<dd>Change the location of the standard Python libraries. By default, the libraries are searched in ${prefix}/lib/python&lt;version&gt; and ${exec_prefix}/lib/python&lt;version&gt;, where ${prefix} and ${exec_prefix} are installation-dependent directories, both defaulting to <i>/usr/local</i>. When $PYTHONHOME is set to a single directory, its value replaces both ${prefix} and ${exec_prefix}. To specify different values for these, set $PYTHONHOME to ${prefix}:${exec_prefix}.</p>
<dt>PYTHONPATH</p>
<dd>Augments the default search path for module files. The format is the same as the shell&#8217;s $PATH: one or more directory pathnames separated by colons. Non-existent directories are silently ignored. The default search path is installation dependent, but generally begins with ${prefix}/lib/python&lt;version&gt; (see PYTHONHOME above). The default search path is always appended to $PYTHONPATH. If a script argument is given, the directory containing the script is inserted in the path in front of $PYTHONPATH. The search path can be manipulated from within a Python program as the variable <i>sys.path</i>.</p>
<dt>PYTHONPLATLIBDIR</p>
<dd>Override sys.platlibdir.</p>
<dt>PYTHONSTARTUP</p>
<dd>If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same name space where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts <i>sys.ps1</i> and <i>sys.ps2</i> in this file.</p>
<dt>PYTHONOPTIMIZE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-O</code> option. If set to an integer, it is equivalent to specifying <code>-O</code> multiple times.</p>
<dt>PYTHONDEBUG</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-d</code> option. If set to an integer, it is equivalent to specifying <code>-d</code> multiple times.</p>
<dt>PYTHONDONTWRITEBYTECODE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-B</code> option (don&#8217;t try to write <i>.pyc</i> files).</p>
<dt>PYTHONINSPECT</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-i</code> option.</p>
<dt>PYTHONIOENCODING</p>
<dd>If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax <i>encodingname</i><code>:</code><i>errorhandler</i> The <i>errorhandler</i> part is optional and has the same meaning as in str.encode. For stderr, the <i>errorhandler</i><br />
&nbsp;part is ignored;&nbsp;the handler will always be&nbsp;&#8216;backslashreplace&#8217;.</p>
<dt>PYTHONNOUSERSITE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-s</code> option (Don&#8217;t add the user site directory to sys.path).</p>
<dt>PYTHONUNBUFFERED</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-u</code> option.</p>
<dt>PYTHONVERBOSE</p>
<dd>If this is set to a non-empty string it is equivalent to specifying the <code>-v</code> option. If set to an integer, it is equivalent to specifying <code>-v</code> multiple times.</p>
<dt>PYTHONWARNINGS</p>
<dd>If this is set to a comma-separated string it is equivalent to specifying the <code>-W</code> option for each separate value.</p>
<dt>PYTHONHASHSEED</p>
<dd>If this variable is set to &quot;random&quot;, a random value is used to seed the hashes of str and bytes objects. </p>
<p> If PYTHONHASHSEED is set to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the hash randomization. Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values. </p>
<p> The integer must be a decimal number in the range [0,4294967295]. Specifying the value 0 will disable hash randomization.</p>
<dt>PYTHONMALLOC</p>
<dd>Set the Python memory allocators and/or install debug hooks. The available memory allocators are <i>malloc</i> and <i>pymalloc</i>. The available debug hooks are <i>debug</i>, <i>malloc_debug</i>, and <i>pymalloc_debug</i>.</p>
<dd>When Python is compiled in debug mode, the default is <i>pymalloc_debug</i> and the debug hooks are automatically used. Otherwise, the default is <i>pymalloc</i>.</p>
<dt>PYTHONMALLOCSTATS</p>
<dd>If set to a non-empty string, Python will print statistics of the pymalloc memory allocator every time a new pymalloc object arena is created, and on shutdown.</p>
<dd>This variable is ignored if the $<code>PYTHONMALLOC</code> environment variable is used to force the <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) allocator of the C library, or if Python is configured without pymalloc support.</p>
<dt>PYTHONASYNCIODEBUG</p>
<dd>If this environment variable is set to a non-empty string, enable the debug mode of the asyncio module.</p>
<dt>PYTHONTRACEMALLOC</p>
<dd>If this environment variable is set to a non-empty string, start tracing Python memory allocations using the tracemalloc module.</p>
<dd>The value of the variable is the maximum number of frames stored in a traceback of a trace. For example, <i>PYTHONTRACEMALLOC=1</i> stores only the most recent frame.</p>
<dt>PYTHONFAULTHANDLER</p>
<dd>If this environment variable is set to a non-empty string, <i>faulthandler.enable()</i> is called at startup: install a handler for SIGSEGV, SIGFPE, SIGABRT, SIGBUS and SIGILL signals to dump the Python traceback.</p>
<dd>This is equivalent to the <code>-X faulthandler</code> option.</p>
<dt>PYTHONEXECUTABLE</p>
<dd>If this environment variable is set, <i>sys.argv[0]</i> will be set to its value instead of the value got through the C runtime. Only works on Mac OS X.</p>
<dt>PYTHONUSERBASE</p>
<dd>Defines the user base directory, which is used to compute the path of the user <i>site-packages</i> directory and Distutils installation paths for <i>python setup.py install &#8211;user</i>.</p>
<dt>PYTHONPROFILEIMPORTTIME</p>
<dd>If this environment variable is set to a non-empty string, Python will show how long each import takes. This is exactly equivalent to setting <code>-X importtime</code> on the command line.</p>
<dt>PYTHONBREAKPOINT</p>
<dd>If this environment variable is set to 0, it disables the default debugger. It can be set to the callable of your debugger of choice.</dl>
<h3>Debug-mode variables</h3>
<p>Setting these variables only has an effect in a debug build of Python, that is, if Python was configured with the <code>&#8211;with-pydebug</code> build option.</p>
<dl COMPACT>
<dt>PYTHONTHREADDEBUG</p>
<dd>If this environment variable is set, Python will print threading debug info. The feature is deprecated in Python 3.10 and will be removed in Python 3.12.</p>
<dt>PYTHONDUMPREFS</p>
<dd>If this environment variable is set, Python will dump objects and reference counts still alive after shutting down the interpreter.</dl>
<h2>Author</h2>
<p>The Python Software Foundation: <a rel="nofollow" href="https://www.python.org/psf/">https://www.python.org/psf/</a></p>
<h2>Internet Resources</h2>
<p>Main website: <a rel="nofollow" href="https://www.python.org/">https://www.python.org/</a><br />
 Documentation: <a rel="nofollow" href="https://docs.python.org/">https://docs.python.org/</a><br />
 Developer resources: <a rel="nofollow" href="https://devguide.python.org/">https://devguide.python.org/</a><br />
 Downloads: <a rel="nofollow" href="https://www.python.org/downloads/">https://www.python.org/downloads/</a><br />
 Module repository: <a rel="nofollow" href="https://pypi.org/">https://pypi.org/</a><br />
 Newsgroups: comp.lang.python, comp.lang.python.announce</p>
<h2>Licensing</h2>
<p>Python is distributed under an Open Source license. See the file &quot;LICENSE&quot; in the Python source distribution for information on terms &amp; conditions for accessing and otherwise using Python and for a DISCLAIMER OF ALL WARRANTIES.</p>
