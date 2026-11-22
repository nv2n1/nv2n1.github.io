---

title: "pylint(1)"
name: "pylint"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pylint/"
description: "pylint – python code static checker"
---

<p> <code>pylint </code> &#8211; python code static checker </p>
<h2>SYNOPSIS</h2>
<p> <code>pylint</code> [ <i>OPTIONS</i> ] [ <i>&lt;arguments&gt;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>pylint </code> is a Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells (as defined in Martin Fowler&#8217;s Refactoring book) </p>
<p> Pylint can be seen as another PyChecker since nearly all tests you can do with PyChecker can also be done with Pylint. However, Pylint offers some more features, like checking length of lines of code, checking if variable names are well-formed according to your coding standard, or checking if declared interfaces are truly implemented, and much more. </p>
<p> Additionally, it is possible to write plugins to add your own checks. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</dt>
<dd> show program&#8217;s version number and exit</dd>
<dt>&#8211;help, -h</dt>
<dd> show this help message and exit </dd>
</dl>
<h2>MASTER</h2>
<dl>
<dt>&#8211;rcfile=&lt;file&gt;</dt>
<dd> Specify a configuration file.</dd>
<dt>&#8211;init-hook=&lt;code&gt;</dt>
<dd> Python code to execute, usually for sys.path manipulation such as pygtk.require().</dd>
<dt>&#8211;errors-only, -e</dt>
<dd> In debug mode, checkers without error messages are disabled and for others, only the ERROR messages are displayed, and no reports are done by default</dd>
<dt>&#8211;profile=&lt;y_or_n&gt;</dt>
<dd> Profiled execution. [current: no]</dd>
<dt>&#8211;ignore=&lt;file&gt;</dt>
<dd> Add &lt;file or directory&gt; to the black list. It should be a base name, not a path. You may set this option multiple times. [current: CVS]</dd>
<dt>&#8211;persistent=&lt;y_or_n&gt;</dt>
<dd> Pickle collected data for later comparisons. [current: yes]</dd>
<dt>&#8211;load-plugins=&lt;modules&gt;</dt>
<dd> List of plugins (as comma separated values of python modules names) to load, usually to register additional checkers. [current: none] </dd>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt>&#8211;help-msg=&lt;msg-id&gt;</dt>
<dd> Display a help message for the given message id and exit. The value may be a comma separated list of message ids.</dd>
<dt>&#8211;list-msgs</dt>
<dd> Generate pylint&#8217;s full documentation.</dd>
<dt>&#8211;generate-rcfile</dt>
<dd> Generate a sample configuration file according to the current configuration. You can put other options before this one to get them in the generated configuration.</dd>
<dt>&#8211;generate-man</dt>
<dd> Generate pylint&#8217;s man page. </dd>
</dl>
<h2>MESSAGES CONTROL</h2>
<dl>
<dt>&#8211;enable-checker=&lt;checker ids&gt;</dt>
<dd> Enable only checker(s) with the given id(s). This option conflicts with the disable-checker option</dd>
<dt>&#8211;disable-checker=&lt;checker ids&gt;</dt>
<dd> Enable all checker(s) except those with the given id(s). This option conflicts with the enable-checker option</dd>
<dt>&#8211;enable-msg-cat=&lt;msg cats&gt;</dt>
<dd> Enable all messages in the listed categories.</dd>
<dt>&#8211;disable-msg-cat=&lt;msg cats&gt;</dt>
<dd> Disable all messages in the listed categories.</dd>
<dt>&#8211;enable-msg=&lt;msg ids&gt;</dt>
<dd> Enable the message(s) with the given id(s).</dd>
<dt>&#8211;disable-msg=&lt;msg ids&gt;</dt>
<dd> Disable the message(s) with the given id(s). </dd>
</dl>
<h2>REPORTS</h2>
<dl>
<dt>&#8211;output-format=&lt;format&gt;, -f &lt;format&gt;</dt>
<dd> Set the output format. Available formats are text, parseable, colorized, msvs (visual studio) and html [current: text]</dd>
<dt>&#8211;include-ids=&lt;y_or_n&gt;, -i &lt;y_or_n&gt;</dt>
<dd> Include message&#8217;s id in output [current: no]</dd>
<dt>&#8211;files-output=&lt;y_or_n&gt;</dt>
<dd> Put messages in a separate file for each module / package specified on the command line instead of printing them on stdout. Reports (if any) will be written in a file name &quot;pylint_global.[txt|html]&quot;. [current: no]</dd>
<dt>&#8211;reports=&lt;y_or_n&gt;, -r &lt;y_or_n&gt;</dt>
<dd> Tells whether to display a full report or only the messages [current: yes]</dd>
<dt>&#8211;evaluation=&lt;python_expression&gt;</dt>
<dd> Python expression which should return a note less than 10 (10 is the highest note). You have access to the variables errors warning, statement which respectively contain the number of errors / warnings messages and the total number of statements analyzed. This is used by the global evaluation report (R0004). [current: 10.0 &#8211; ((float(5 * error + warning + refactor + convention) / statement) * 10)]</dd>
<dt>&#8211;comment=&lt;y_or_n&gt;</dt>
<dd> Add a comment according to your evaluation note. This is used by the global evaluation report (R0004). [current: no]</dd>
<dt>&#8211;enable-report=&lt;rpt ids&gt;</dt>
<dd> Enable the report(s) with the given id(s).</dd>
<dt>&#8211;disable-report=&lt;rpt ids&gt;</dt>
<dd> Disable the report(s) with the given id(s). </dd>
</dl>
<h2>DESIGN</h2>
<dl>
<dt>&#8211;max-args=&lt;int&gt;</dt>
<dd> Maximum number of arguments for function / method [current: 5]</dd>
<dt>&#8211;max-locals=&lt;int&gt;</dt>
<dd> Maximum number of locals for function / method body [current: 15]</dd>
<dt>&#8211;max-returns=&lt;int&gt;</dt>
<dd> Maximum number of return / yield for function / method body [current: 6]</dd>
<dt>&#8211;max-branchs=&lt;int&gt;</dt>
<dd> Maximum number of branch for function / method body [current: 12]</dd>
<dt>&#8211;max-statements=&lt;int&gt;</dt>
<dd> Maximum number of statements in function / method body [current: 50]</dd>
<dt>&#8211;max-parents=&lt;num&gt;</dt>
<dd> Maximum number of parents for a class (see R0901). [current: 7]</dd>
<dt>&#8211;max-attributes=&lt;num&gt;</dt>
<dd> Maximum number of attributes for a class (see R0902). [current: 7]</dd>
<dt>&#8211;min-public-methods=&lt;num&gt;</dt>
<dd> Minimum number of public methods for a class (see R0903). [current: 2]</dd>
<dt>&#8211;max-public-methods=&lt;num&gt;</dt>
<dd> Maximum number of public methods for a class (see R0904). [current: 20] </dd>
</dl>
<h2>CLASSES</h2>
<dl>
<dt>&#8211;ignore-iface-methods=&lt;method names&gt;</dt>
<dd> List of interface methods to ignore, separated by a comma. This is used for instance to not check methods defines in Zope&#8217;s Interface base class. [current: isImplementedBy,deferred,extends,names,namesAndDescriptions,queryDescriptionFor,getBases,getDescriptionFor,getDoc,getName,getTaggedValue,getTaggedValueTags,isEqualOrExtendedBy,setTaggedValue,isImplementedByInstancesOf,adaptWith,is_implemented_by]</dd>
<dt>&#8211;defining-attr-methods=&lt;method names&gt;</dt>
<dd> List of method names used to declare (i.e. assign) instance attributes. [current: __init__,__new__,setUp] </dd>
</dl>
<h2>IMPORTS</h2>
<dl>
<dt>&#8211;deprecated-modules=&lt;modules&gt;</dt>
<dd> Deprecated modules which should not be used, separated by a comma [current: regsub,string,TERMIOS,Bastion,rexec]</dd>
<dt>&#8211;import-graph=&lt;file.dot&gt;</dt>
<dd> Create a graph of every (i.e. internal and external) dependencies in the given file (report R0402 must not be disabled) [current: none]</dd>
<dt>&#8211;ext-import-graph=&lt;file.dot&gt;</dt>
<dd> Create a graph of external dependencies in the given file (report R0402 must not be disabled) [current: none]</dd>
<dt>&#8211;int-import-graph=&lt;file.dot&gt;</dt>
<dd> Create a graph of internal dependencies in the given file (report R0402 must not be disabled) [current: none] </dd>
</dl>
<h2>FORMAT</h2>
<dl>
<dt>&#8211;max-line-length=&lt;int&gt;</dt>
<dd> Maximum number of characters on a single line. [current: 80]</dd>
<dt>&#8211;max-module-lines=&lt;int&gt;</dt>
<dd> Maximum number of lines in a module [current: 1000]</dd>
<dt>&#8211;indent-string=&lt;string&gt;</dt>
<dd> String used as indentation unit. This is usually &quot; &quot; (4 spaces) or &quot; &quot; (1 tab). [current: &#8216; &#8216;] </dd>
</dl>
<h2>SIMILARITIES</h2>
<dl>
<dt>&#8211;min-similarity-lines=&lt;int&gt;</dt>
<dd> Minimum lines number of a similarity. [current: 4]</dd>
<dt>&#8211;ignore-comments=&lt;y or n&gt;</dt>
<dd> Ignore comments when computing similarities. [current: yes]</dd>
<dt>&#8211;ignore-docstrings=&lt;y or n&gt;</dt>
<dd> Ignore docstrings when computing similarities. [current: yes] </dd>
</dl>
<h2>TYPECHECK</h2>
<dl>
<dt>&#8211;ignore-mixin-members=&lt;y_or_n&gt;</dt>
<dd> Tells whether missing members accessed in mixin class should be ignored. A mixin class is detected if its name ends with &quot;mixin&quot; (case insensitive). [current: yes]</dd>
<dt>&#8211;ignored-classes=&lt;members names&gt;</dt>
<dd> List of classes names for which member attributes should not be checked (useful for classes with attributes dynamically set). [current: SQLObject]</dd>
<dt>&#8211;zope=&lt;y_or_n&gt;</dt>
<dd> When zope mode is activated, add a predefined set of Zope acquired attributes to generated-members. [current: no]</dd>
<dt>&#8211;generated-members=&lt;members names&gt;</dt>
<dd> List of members which are set dynamically and missed by pylint inference system, and so shouldn&#8217;t trigger E0201 when accessed. [current: REQUEST,acl_users,aq_parent] </dd>
</dl>
<h2>VARIABLES</h2>
<dl>
<dt>&#8211;init-import=&lt;y_or_n&gt;</dt>
<dd> Tells whether we should check for unused import in __init__ files. [current: no]</dd>
<dt>&#8211;dummy-variables-rgx=&lt;regexp&gt;</dt>
<dd> A regular expression matching names used for dummy variables (i.e. not used). [current: _|dummy]</dd>
<dt>&#8211;additional-builtins=&lt;comma separated list&gt;</dt>
<dd> List of additional names supposed to be defined in builtins. Remember that you should avoid to define new builtins when possible. [current: none] </dd>
</dl>
<h2>MISCELLANEOUS</h2>
<dl>
<dt>&#8211;notes=&lt;comma separated values&gt;</dt>
<dd> List of note tags to take in consideration, separated by a comma. [current: FIXME,XXX,TODO] </dd>
</dl>
<h2>BASIC</h2>
<dl>
<dt>&#8211;required-attributes=&lt;attributes&gt;</dt>
<dd> Required attributes for module, separated by a comma [current: none]</dd>
<dt>&#8211;no-docstring-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match functions or classes name which do not require a docstring [current: __.*__]</dd>
<dt>&#8211;module-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct module names [current: (([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$]</dd>
<dt>&#8211;const-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct module level names [current: (([A-Z_][A-Z0-9_]*)|(__.*__))$]</dd>
<dt>&#8211;class-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct class names [current: [A-Z_][a-zA-Z0-9]+$]</dd>
<dt>&#8211;function-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct function names [current: [a-z_][a-z0-9_]{2,30}$]</dd>
<dt>&#8211;method-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct method names [current: [a-z_][a-z0-9_]{2,30}$]</dd>
<dt>&#8211;attr-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct instance attribute names [current: [a-z_][a-z0-9_]{2,30}$]</dd>
<dt>&#8211;argument-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct argument names [current: [a-z_][a-z0-9_]{2,30}$]</dd>
<dt>&#8211;variable-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct variable names [current: [a-z_][a-z0-9_]{2,30}$]</dd>
<dt>&#8211;inlinevar-rgx=&lt;regexp&gt;</dt>
<dd> Regular expression which should only match correct list comprehension / generator expression variable names [current: [A-Za-z_][A-Za-z0-9_]*$]</dd>
<dt>&#8211;good-names=&lt;names&gt;</dt>
<dd> Good variable names which should always be accepted, separated by a comma [current: i,j,k,ex,Run,_]</dd>
<dt>&#8211;bad-names=&lt;names&gt;</dt>
<dd> Bad variable names which should always be refused, separated by a comma [current: foo,bar,baz,toto,tutu,tata]</dd>
<dt>&#8211;bad-functions=&lt;builtin function names&gt;</dt>
<dd> List of builtins function names that should not be used, separated by a comma [current: map,filter,apply,input] </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables are used :<br/>
&nbsp;<wbr>*&nbsp;<wbr>PYLINTHOME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>path to the directory where data of persistent run will be stored. If not found, it defaults to ~/.pylint.d/ or .pylint.d (in the current working directory) . The current PYLINTHOME is ~/.pylint.d.<br/>
&nbsp;<wbr>*&nbsp;<wbr>PYLINTRC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>path to the configuration file. If not found, it will use the first&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> existent file in ~/.pylintrc, /etc/pylintrc. The current PYLINTRC is None. </p>
<h2>OUTPUT</h2>
<p> Using the default text output, the message format is :<br/>
&nbsp;<wbr>&nbsp;<wbr>MESSAGE_TYPE: LINE_NUM:[OBJECT:]&nbsp;<wbr>MESSAGE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> There are 5 kind of message types :<br/>
&nbsp;<wbr>*&nbsp;<wbr>(C)&nbsp;<wbr>convention, for programming standard violation&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>*&nbsp;<wbr>(R)&nbsp;<wbr>refactor, for bad code smell&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>*&nbsp;<wbr>(W)&nbsp;<wbr>warning, for python specific problems&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>*&nbsp;<wbr>(E)&nbsp;<wbr>error, for probable bugs in the code&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>*&nbsp;<wbr>(F)&nbsp;<wbr>fatal, if an error occurred which prevented pylint from doing further processing.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br/>
&nbsp;<wbr>&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> /usr/share/doc/pylint/ </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2003-2008 Sylvain Thenault (thenault [at] gmail.com). Copyright (c) 2003-2008 LOGILAB S.A. (Paris, FRANCE). <a rel="nofollow" href="http://www.logilab.fr/">http://www.logilab.fr/</a> &#8212; mailto:contact [at] logilab.fr </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.</p>
<h2>BUGS</h2>
<p> Please report bugs on the project&#8217;s mailing list: mailto://python-projects [at] logilab.org </p>
<h2>AUTHOR</h2>
<p> Sylvain Thenault &lt;sylvain.thenault [at] logilab.fr&gt; </p>
