---
title: "pylint-3-4(1)"
name: "pylint-3-4"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pylint-3-4/"
description: "pylint – python code static checker"
---

<p><code>pylint</code> &#8211; python code static checker </p>
<h2>Synopsis</h2>
<p><code>pylint</code> [ <i>OPTIONS</i> ] [ <i>&lt;arguments&gt;</i> ] </p>
<h2>Description</h2>
<p><code>pylint</code> is a Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells (as defined in Martin Fowler&#8217;s Refactoring book) </p>
<p> Pylint can be seen as another PyChecker since nearly all tests you can do with PyChecker can also be done with Pylint. However, Pylint offers some more features, like checking length of lines of code, checking if variable names are well-formed according to your coding standard, or checking if declared interfaces are truly implemented, and much more. </p>
<p> Additionally, it is possible to write plugins to add your own checks. </p>
<p> Pylint is shipped with &quot;pylint-gui&quot;, &quot;pyreverse&quot; (UML diagram generator) and &quot;symilar&quot; (an independent similarities checker). </p>
<h2>Options</h2>
<dl COMPACT>
<dt>&#8211;version</p>
<dd>show program&#8217;s version number and exit</p>
<dt>&#8211;help, -h</p>
<dd>show this help message and exit</p>
<dt>&#8211;long-help</p>
<dd>more verbose help. </p>
</dl>
<h2>Master</h2>
<dl COMPACT>
<dt>&#8211;rcfile=&lt;file&gt;</p>
<dd>Specify a configuration file.</p>
<dt>&#8211;init-hook=&lt;code&gt;</p>
<dd>Python code to execute, usually for sys.path manipulation such as pygtk.require().</p>
<dt>&#8211;errors-only, -E</p>
<dd>In error mode, checkers without error messages are disabled and for others, only the ERROR messages are displayed, and no reports are done by default</p>
<dt>&#8211;py3k</p>
<dd>In Python 3 porting mode, all checkers will be disabled and only messages emitted by the porting checker will be displayed</p>
<dt>&#8211;ignore=&lt;file&gt;[,&lt;file&gt;&#8230;]</p>
<dd>Add files or directories to the blacklist. They should be base names, not paths. [current: CVS]</p>
<dt>&#8211;persistent=&lt;y_or_n&gt;</p>
<dd>Pickle collected data for later comparisons. [current: yes]</p>
<dt>&#8211;load-plugins=&lt;modules&gt;</p>
<dd>List of plugins (as comma separated values of python modules names) to load, usually to register additional checkers. [current: none]</p>
<dt>&#8211;jobs=&lt;n-processes&gt;, -j &lt;n-processes&gt;</p>
<dd>Use multiple processes to speed up Pylint. [current: 1]</p>
<dt>&#8211;extension-pkg-whitelist=&lt;pkg[,pkg]&gt;</p>
<dd>A comma-separated list of package or module names from where C extensions may be loaded. Extensions are loading into the active Python interpreter and may run arbitrary code [current: none] </p>
</dl>
<h2>Commands</h2>
<dl COMPACT>
<dt>&#8211;help-msg=&lt;msg-id&gt;</p>
<dd>Display a help message for the given message id and exit. The value may be a comma separated list of message ids.</p>
<dt>&#8211;list-msgs</p>
<dd>Generate pylint&#8217;s messages.</p>
<dt>&#8211;list-conf-levels</p>
<dd>Generate pylint&#8217;s messages.</p>
<dt>&#8211;full-documentation</p>
<dd>Generate pylint&#8217;s full documentation.</p>
<dt>&#8211;generate-rcfile</p>
<dd>Generate a sample configuration file according to the current configuration. You can put other options before this one to get them in the generated configuration. </p>
</dl>
<h2>Messages Control</h2>
<dl COMPACT>
<dt>&#8211;confidence=&lt;levels&gt;</p>
<dd>Only show warnings with the listed confidence levels. Leave empty to show all. Valid levels: HIGH, INFERENCE, INFERENCE_FAILURE, UNDEFINED [current: none]</p>
<dt>&#8211;enable=&lt;msg ids&gt;, -e &lt;msg ids&gt;</p>
<dd>Enable the message, report, category or checker with the given id(s). You can either give multiple identifier separated by comma (,) or put this option multiple time. See also the &quot;&#8211;disable&quot; option for examples.</p>
<dt>&#8211;disable=&lt;msg ids&gt;, -d &lt;msg ids&gt;</p>
<dd>Disable the message, report, category or checker with the given id(s). You can either give multiple identifiers separated by comma (,) or put this option multiple times (only on the command line, not in the configuration file where it should appear only once).You can also use &quot;&#8211;disable=all&quot; to disable everything first and then reenable specific checks. For example, if you want to run only the similarities checker, you can use &quot;&#8211;disable=all &#8211;enable=similarities&quot;. If you want to run only the classes checker, but have no Warning level messages displayed, use&quot;&#8211;disable=all &#8211;enable=classes &#8211;disable=W&quot; </p>
</dl>
<h2>Reports</h2>
<dl COMPACT>
<dt>&#8211;output-format=&lt;format&gt;, -f &lt;format&gt;</p>
<dd>Set the output format. Available formats are text, parseable, colorized, msvs (visual studio) and html. You can also give a reporter class, eg mypackage.mymodule.MyReporterClass. [current: text]</p>
<dt>&#8211;files-output=&lt;y_or_n&gt;</p>
<dd>Put messages in a separate file for each module / package specified on the command line instead of printing them on stdout. Reports (if any) will be written in a file name &quot;pylint_global.[txt|html]&quot;. [current: no]</p>
<dt>&#8211;reports=&lt;y_or_n&gt;, -r &lt;y_or_n&gt;</p>
<dd>Tells whether to display a full report or only the messages [current: yes]</p>
<dt>&#8211;evaluation=&lt;python_expression&gt;</p>
<dd>Python expression which should return a note less than 10 (10 is the highest note). You have access to the variables errors warning, statement which respectively contain the number of errors / warnings messages and the total number of statements analyzed. This is used by the global evaluation report (RP0004). [current: 10.0 &#8211; ((float(5 * error + warning + refactor + convention) / statement) * 10)]</p>
<dt>&#8211;comment=&lt;y_or_n&gt;</p>
<dd>Add a comment according to your evaluation note. This is used by the global evaluation report (RP0004). [current: no]</p>
<dt>&#8211;msg-template=&lt;template&gt;</p>
<dd>Template used to display messages. This is a python new-style format string used to format the message information. See doc for all details </p>
</dl>
<h2>Exceptions</h2>
<dl COMPACT>
<dt>&#8211;overgeneral-exceptions=&lt;comma-separated class names&gt;</p>
<dd>Exceptions that will emit a warning when being caught. Defaults to &quot;Exception&quot; [current: Exception] </p>
</dl>
<h2>Classes</h2>
<dl COMPACT>
<dt>&#8211;ignore-iface-methods=&lt;method names&gt;</p>
<dd>List of interface methods to ignore, separated by a comma. This is used for instance to not check methods defines in Zope&#8217;s Interface base class. [current: isImplementedBy,deferred,extends,names,namesAndDescriptions,queryDescriptionFor,getBases,getDescriptionFor,getDoc,getName,getTaggedValue,getTaggedValueTags,isEqualOrExtendedBy,setTaggedValue,isImplementedByInstancesOf,adaptWith,is_implemented_by]</p>
<dt>&#8211;defining-attr-methods=&lt;method names&gt;</p>
<dd>List of method names used to declare (i.e. assign) instance attributes. [current: __init__,__new__,setUp]</p>
<dt>&#8211;valid-classmethod-first-arg=&lt;argument names&gt;</p>
<dd>List of valid names for the first argument in a class method. [current: cls]</p>
<dt>&#8211;valid-metaclass-classmethod-first-arg=&lt;argument names&gt;</p>
<dd>List of valid names for the first argument in a metaclass class method. [current: mcs]</p>
<dt>&#8211;exclude-protected=&lt;protected access exclusions&gt;</p>
<dd>List of member names, which should be excluded from the protected access warning. [current: _asdict,_fields,_replace,_source,_make] </p>
</dl>
<h2>Logging</h2>
<dl COMPACT>
<dt>&#8211;logging-modules=&lt;comma separated list&gt;</p>
<dd>Logging modules to check that the string format arguments are in logging function parameter format [current: logging] </p>
</dl>
<h2>Variables</h2>
<dl COMPACT>
<dt>&#8211;init-import=&lt;y_or_n&gt;</p>
<dd>Tells whether we should check for unused import in __init__ files. [current: no]</p>
<dt>&#8211;dummy-variables-rgx=&lt;regexp&gt;</p>
<dd>A regular expression matching the name of dummy variables (i.e. expectedly not used). [current: _$|dummy]</p>
<dt>&#8211;additional-builtins=&lt;comma separated list&gt;</p>
<dd>List of additional names supposed to be defined in builtins. Remember that you should avoid to define new builtins when possible. [current: none]</p>
<dt>&#8211;callbacks=&lt;callbacks&gt;</p>
<dd>List of strings which can identify a callback function by name. A callback name must start or end with one of those strings. [current: cb_,_cb] </p>
</dl>
<h2>Design</h2>
<dl COMPACT>
<dt>&#8211;max-args=&lt;int&gt;</p>
<dd>Maximum number of arguments for function / method [current: 5]</p>
<dt>&#8211;ignored-argument-names=&lt;regexp&gt;</p>
<dd>Argument names that match this expression will be ignored. Default to name with leading underscore [current: _.*]</p>
<dt>&#8211;max-locals=&lt;int&gt;</p>
<dd>Maximum number of locals for function / method body [current: 15]</p>
<dt>&#8211;max-returns=&lt;int&gt;</p>
<dd>Maximum number of return / yield for function / method body [current: 6]</p>
<dt>&#8211;max-branches=&lt;int&gt;</p>
<dd>Maximum number of branch for function / method body [current: 12]</p>
<dt>&#8211;max-statements=&lt;int&gt;</p>
<dd>Maximum number of statements in function / method body [current: 50]</p>
<dt>&#8211;max-parents=&lt;num&gt;</p>
<dd>Maximum number of parents for a class (see R0901). [current: 7]</p>
<dt>&#8211;max-attributes=&lt;num&gt;</p>
<dd>Maximum number of attributes for a class (see R0902). [current: 7]</p>
<dt>&#8211;min-public-methods=&lt;num&gt;</p>
<dd>Minimum number of public methods for a class (see R0903). [current: 2]</p>
<dt>&#8211;max-public-methods=&lt;num&gt;</p>
<dd>Maximum number of public methods for a class (see R0904). [current: 20] </p>
</dl>
<h2>Basic</h2>
<dl COMPACT>
<dt>&#8211;required-attributes=&lt;attributes&gt;</p>
<dd>Required attributes for module, separated by a comma [current: none]</p>
<dt>&#8211;bad-functions=&lt;builtin function names&gt;</p>
<dd>List of builtins function names that should not be used, separated by a comma [current: map,filter,input]</p>
<dt>&#8211;good-names=&lt;names&gt;</p>
<dd>Good variable names which should always be accepted, separated by a comma [current: i,j,k,ex,Run,_]</p>
<dt>&#8211;bad-names=&lt;names&gt;</p>
<dd>Bad variable names which should always be refused, separated by a comma [current: foo,bar,baz,toto,tutu,tata]</p>
<dt>&#8211;name-group=&lt;name1:name2&gt;</p>
<dd>Colon-delimited sets of names that determine each other&#8217;s naming style when the name regexes allow several styles. [current: none]</p>
<dt>&#8211;include-naming-hint=&lt;y_or_n&gt;</p>
<dd>Include a hint for the correct naming format with invalid-name [current: no]</p>
<dt>&#8211;function-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct function names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;function-name-hint=&lt;string&gt;</p>
<dd>Naming hint for function names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;variable-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct variable names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;variable-name-hint=&lt;string&gt;</p>
<dd>Naming hint for variable names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;const-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct constant names [current: (([A-Z_][A-Z0-9_]*)|(__.*__))$]</p>
<dt>&#8211;const-name-hint=&lt;string&gt;</p>
<dd>Naming hint for constant names [current: (([A-Z_][A-Z0-9_]*)|(__.*__))$]</p>
<dt>&#8211;attr-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct attribute names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;attr-name-hint=&lt;string&gt;</p>
<dd>Naming hint for attribute names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;argument-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct argument names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;argument-name-hint=&lt;string&gt;</p>
<dd>Naming hint for argument names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;class-attribute-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct class attribute names [current: ([A-Za-z_][A-Za-z0-9_]{2,30}|(__.*__))$]</p>
<dt>&#8211;class-attribute-name-hint=&lt;string&gt;</p>
<dd>Naming hint for class attribute names [current: ([A-Za-z_][A-Za-z0-9_]{2,30}|(__.*__))$]</p>
<dt>&#8211;inlinevar-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct inline iteration names [current: [A-Za-z_][A-Za-z0-9_]*$]</p>
<dt>&#8211;inlinevar-name-hint=&lt;string&gt;</p>
<dd>Naming hint for inline iteration names [current: [A-Za-z_][A-Za-z0-9_]*$]</p>
<dt>&#8211;class-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct class names [current: [A-Z_][a-zA-Z0-9]+$]</p>
<dt>&#8211;class-name-hint=&lt;string&gt;</p>
<dd>Naming hint for class names [current: [A-Z_][a-zA-Z0-9]+$]</p>
<dt>&#8211;module-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct module names [current: (([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$]</p>
<dt>&#8211;module-name-hint=&lt;string&gt;</p>
<dd>Naming hint for module names [current: (([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$]</p>
<dt>&#8211;method-rgx=&lt;regexp&gt;</p>
<dd>Regular expression matching correct method names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;method-name-hint=&lt;string&gt;</p>
<dd>Naming hint for method names [current: [a-z_][a-z0-9_]{2,30}$]</p>
<dt>&#8211;no-docstring-rgx=&lt;regexp&gt;</p>
<dd>Regular expression which should only match function or class names that do not require a docstring. [current: __.*__]</p>
<dt>&#8211;docstring-min-length=&lt;int&gt;</p>
<dd>Minimum line length for functions/classes that require docstrings, shorter ones are exempt. [current: -1] </p>
</dl>
<h2>Miscellaneous</h2>
<dl COMPACT>
<dt>&#8211;notes=&lt;comma separated values&gt;</p>
<dd>List of note tags to take in consideration, separated by a comma. [current: FIXME,XXX,TODO] </p>
</dl>
<h2>Typecheck</h2>
<dl COMPACT>
<dt>&#8211;ignore-mixin-members=&lt;y_or_n&gt;</p>
<dd>Tells whether missing members accessed in mixin class should be ignored. A mixin class is detected if its name ends with &quot;mixin&quot; (case insensitive). [current: yes]</p>
<dt>&#8211;ignored-modules=&lt;module names&gt;</p>
<dd>List of module names for which member attributes should not be checked (useful for modules/projects where namespaces are manipulated during runtime and thus existing member attributes cannot be deduced by static analysis [current: none]</p>
<dt>&#8211;ignored-classes=&lt;members names&gt;</p>
<dd>List of classes names for which member attributes should not be checked (useful for classes with attributes dynamically set). [current: SQLObject, optparse.Values, thread._local, _thread._local]</p>
<dt>&#8211;zope=&lt;y_or_n&gt;</p>
<dd>When zope mode is activated, add a predefined set of Zope acquired attributes to generated-members. [current: no]</p>
<dt>&#8211;generated-members=&lt;members names&gt;</p>
<dd>List of members which are set dynamically and missed by pylint inference system, and so shouldn&#8217;t trigger E1101 when accessed. Python regular expressions are accepted. [current: REQUEST,acl_users,aq_parent] </p>
</dl>
<h2>Spelling</h2>
<dl COMPACT>
<dt>&#8211;spelling-dict=&lt;dict name&gt;</p>
<dd>Spelling dictionary name. Available dictionaries: none. To make it working install python-enchant package. [current: none]</p>
<dt>&#8211;spelling-ignore-words=&lt;comma separated words&gt;</p>
<dd>List of comma separated words that should not be checked. [current: none]</p>
<dt>&#8211;spelling-private-dict-file=&lt;path to file&gt;</p>
<dd>A path to a file that contains private dictionary; one word per line. [current: none]</p>
<dt>&#8211;spelling-store-unknown-words=&lt;y_or_n&gt;</p>
<dd>Tells whether to store unknown words to indicated private dictionary in &#8211;spelling-private-dict-file option instead of raising a message. [current: no] </p>
</dl>
<h2>Format</h2>
<dl COMPACT>
<dt>&#8211;max-line-length=&lt;int&gt;</p>
<dd>Maximum number of characters on a single line. [current: 100]</p>
<dt>&#8211;ignore-long-lines=&lt;regexp&gt;</p>
<dd>Regexp for a line that is allowed to be longer than the limit. [current: ^*(# )?&lt;?https?://S+&gt;?$]</p>
<dt>&#8211;single-line-if-stmt=&lt;y_or_n&gt;</p>
<dd>Allow the body of an if to be on the same line as the test if there is no else. [current: no]</p>
<dt>&#8211;no-space-check=NO_SPACE_CHECK</p>
<dd>List of optional constructs for which whitespace checking is disabled [current: trailing-comma,dict-separator]</p>
<dt>&#8211;max-module-lines=&lt;int&gt;</p>
<dd>Maximum number of lines in a module [current: 1000]</p>
<dt>&#8211;indent-string=&lt;string&gt;</p>
<dd>String used as indentation unit. This is usually &quot; &quot; (4 spaces) or &quot;	&quot; (1 tab). [current: &#8216; &#8216;]</p>
<dt>&#8211;indent-after-paren=&lt;int&gt;</p>
<dd>Number of spaces of indent required inside a hanging or continued line. [current: 4]</p>
<dt>&#8211;expected-line-ending-format=&lt;empty or LF or CRLF&gt;</p>
<dd>Expected format of line ending, e.g. empty (any line ending), LF or CRLF. [current: none] </p>
</dl>
<h2>Imports</h2>
<dl COMPACT>
<dt>&#8211;deprecated-modules=&lt;modules&gt;</p>
<dd>Deprecated modules which should not be used, separated by a comma [current: regsub,TERMIOS,Bastion,rexec]</p>
<dt>&#8211;import-graph=&lt;file.dot&gt;</p>
<dd>Create a graph of every (i.e. internal and external) dependencies in the given file (report RP0402 must not be disabled) [current: none]</p>
<dt>&#8211;ext-import-graph=&lt;file.dot&gt;</p>
<dd>Create a graph of external dependencies in the given file (report RP0402 must not be disabled) [current: none]</p>
<dt>&#8211;int-import-graph=&lt;file.dot&gt;</p>
<dd>Create a graph of internal dependencies in the given file (report RP0402 must not be disabled) [current: none] </p>
</dl>
<h2>Similarities</h2>
<dl COMPACT>
<dt>&#8211;min-similarity-lines=&lt;int&gt;</p>
<dd>Minimum lines number of a similarity. [current: 4]</p>
<dt>&#8211;ignore-comments=&lt;y or n&gt;</p>
<dd>Ignore comments when computing similarities. [current: yes]</p>
<dt>&#8211;ignore-docstrings=&lt;y or n&gt;</p>
<dd>Ignore docstrings when computing similarities. [current: yes]</p>
<dt>&#8211;ignore-imports=&lt;y or n&gt;</p>
<dd>Ignore imports when computing similarities. [current: no] </p>
</dl>
<h2>Environment Variables</h2>
<p>The following environment variables are used:<br />
&nbsp;<wbr>*&nbsp;<wbr>PYLINTHOME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>Path to the directory where the persistent for the run will be stored. If&nbsp;<wbr> not found, it defaults to ~/.pylint.d/ or .pylint.d (in the current working directory).<br />
&nbsp;<wbr>*&nbsp;<wbr>PYLINTRC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>Path to the configuration file. See the documentation for the method used to search for configuration file. </p>
<h2>Output</h2>
<p>Using the default text output, the message format is :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>MESSAGE_TYPE: LINE_NUM:[OBJECT:]&nbsp;<wbr>MESSAGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> There are 5 kind of message types :<br />
&nbsp;<wbr>*&nbsp;<wbr>(C)&nbsp;<wbr>convention, for programming standard violation&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>(R)&nbsp;<wbr>refactor, for bad code smell&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>(W)&nbsp;<wbr>warning, for python specific problems&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>(E)&nbsp;<wbr>error, for probable bugs in the code&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>(F)&nbsp;<wbr>fatal, if an error occurred which prevented pylint from doing further processing. </p>
<h2>Output Status Code</h2>
<p>Pylint should leave with following status code:<br />
&nbsp;<wbr>*&nbsp;<wbr>0 if everything went fine&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>1 if a fatal message was issued&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>2 if an error message was issued&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>4 if a warning message was issued&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>8 if a refactor message was issued&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>16 if a convention message was issued&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>*&nbsp;<wbr>32 on usage error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> status 1 to 16 will be bit-ORed so you can know which different categories has been issued by analysing pylint output status code </p>
<h2>See Also</h2>
<p>/usr/share/doc/pythonX.Y-pylint/ </p>
<h2>Bugs</h2>
<p>Please report bugs on the project&#8217;s mailing list: mailto:code-quality [at] python.org </p>
<h2>Author</h2>
<p>Logilab &lt;python-projects [at] lists.logilab.org&gt;</p>
