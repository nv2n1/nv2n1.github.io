---

title: "mysqlmetagrep(1)"
name: "mysqlmetagrep"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlmetagrep/"
description: "mysqlmetagrep – Search Database Object Definitions"
---

<p> mysqlmetagrep &#8211; Search Database Object Definitions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlmetagrep [</code><i>options</i><code>] [</code><i>pattern</i><code> | </code><i>server</i><code>] &#8230;</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>This utility searches for objects matching a given pattern on all the servers specified using instances of the <code>&#8211;server</code> option. It produces output that displays the matching objects. By default, the first nonoption argument is taken to be the pattern unless the <code>&#8211;pattern</code> option is given. If the <code>&#8211;pattern</code> option is given, all nonoption arguments are treated as connection specifications. </dd>
<p> Internally, the utility generates an SQL statement for searching the necessary tables in the <code>INFORMATION_SCHEMA</code> database on the designated servers and executes it in turn before collecting the result and printing it as a table. Use the <code>&#8211;sql</code> option to have the utility display the statement rather than execute it. This can be useful if you want to feed the output of the statement to another application such as the <code>mysql</code> monitor. </p>
<p> The MySQL server supports two forms of patterns when matching strings: SQL Simple Patterns (used with the <code>LIKE</code> operator) and POSIX Regular Expressions (used with the <code>REGEXP</code> operator). </p>
<p> By default, the utility uses the <code>LIKE</code> operator to match the name (and optionally, the body) of objects. To use the <code>REGEXP</code> operator instead, use the <code>&#8211;regexp</code> option. </p>
<p> Note that since the <code>REGEXP</code> operator does substring searching, it is necessary to anchor the expression to the beginning of the string if you want to match the beginning of the string. </p>
<p> To specify how to display output, use one of the following values with the <code>&#8211;format</code> option: </p>
<dl>
<dt>
</dt><dd> &bull; <code>grid</code> (default) </dd>
<p> Display output in grid or table format like that of the <code>mysql</code> monitor.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>csv</code> </dd>
<p> Display output in comma-separated values format.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>tab</code> </dd>
<p> Display output in tab-separated format.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>vertical</code> </dd>
<p> Display output in single-column format like that of the \G command for the <code>mysql</code> monitor.</dl>
<p>SQL Simple Patterns </p>
<p> The simple patterns defined by the SQL standard consist of a string of characters with two characters that have special meaning: % (percent) matches zero or more characters and _ (underscore) matches exactly one character. </p>
<p> For example: </p>
<dl>
<dt>
</dt><dd> &bull; &#8216;mats%&#8217; </dd>
<p> Match any string that starts with &#8216;mats&#8217;.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8216;%kindahl%&#8217; </dd>
<p> Match any string containing the word &#8216;kindahl&#8217;.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8216;%_&#8217; </dd>
<p> Match any string consisting of one or more characters.</dl>
<p>POSIX Regular Expressions </p>
<p> POSIX regular expressions are more powerful than the simple patterns defined in the SQL standard. A regular expression is a string of characters, optionally containing characters with special meaning: </p>
<dl>
<dt>
</dt><dd> &bull; <code>.</code> </dd>
<p> Match any character.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>^</code> </dd>
<p> Match the beginning of a string.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>$</code> </dd>
<p> Match the end of a string.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>[axy]</code> </dd>
<p> Match <code>a</code>, <code>x</code>, or <code>y</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>[a-f]</code> </dd>
<p> Match any character in the range <code>a</code> to <code>f</code> (that is, <code>a</code>, <code>b</code>, <code>c</code>, <code>d</code>, <code>e</code>, or <code>f</code>).</dl>
<dl>
<dt>
</dt><dd> &bull; <code>[^axy]</code> </dd>
<p> Match any character <i>except</i><code>a</code>, <code>x</code>, or <code>y</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>a*</code> </dd>
<p> Match a sequence of zero or more <code>a</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>a+</code> </dd>
<p> Match a sequence of one or more <code>a</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>a?</code> </dd>
<p> Match zero or one <code>a</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>ab|cd</code> </dd>
<p> Match <code>ab</code> or <code>cd</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>a{5}</code> </dd>
<p> Match five instances of <code>a</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>a{2,5}</code> </dd>
<p> Match from two to five instances of <code>a</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; <code>(abc)+</code> </dd>
<p> Match one or more repetitions of <code>abc</code>.</dl>
<p> This is but a brief set of examples of regular expressions. The full syntax is described in the m[blue]<code>MySQL manual</code>m[][1], but can often be found in <i><a href="/docs/linux/man/7-regex/">regex</a>(7)</i>.<br/>
OPTIONS </p>
<p> <code>mysqlmetagrep</code> accepts the following command-line options: </p>
<dl>
<dt>
</dt><dd> &bull; &#8211;help </dd>
<p> Display a help message and exit.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;body, -b </dd>
<p> Search the body of stored programs (procedures, functions, triggers, and events). The default is to match only the name.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;database=&lt;pattern&gt; </dd>
<p> Look only in databases matching this pattern.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;format=&lt;format&gt;, -f&lt;format&gt; </dd>
<p> Specify the output display format. Permitted format values are <code>grid</code>, <code>csv</code>, <code>tab</code>, and <code>vertical</code>. The default is <code>grid</code>.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;object-types=&lt;types&gt;, &#8211;search-objects=&lt;types&gt; </dd>
<p> Search only the object types named in <i>types</i>, which is a comma-separated list of one or more of the values <code>procedure</code>, <code>function</code>, <code>event</code>, <code>trigger</code>, <code>table</code>, and <code>database</code>. </p>
<p> The default is to search in objects of all types.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;pattern=&lt;pattern&gt;, -e=&lt;pattern&gt; </dd>
<p> The pattern to use when matching. This is required when the first nonoption argument looks like a connection specification rather than a pattern. </p>
<p> If the <code>&#8211;pattern</code> option is given, the first nonoption argument is treated as a connection specifier, not as a pattern.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;regexp, &#8211;basic-regexp, -G </dd>
<p> Perform pattern matches using the <code>REGEXP</code> operator. The default is to use <code>LIKE</code> for matching. This affects the <code>&#8211;database</code> and <code>&#8211;pattern</code> options.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;server=&lt;source&gt; </dd>
<p> Connection information for a server to search in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;]. Use this option multiple times to search multiple servers.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;sql, &#8211;print-sql, -p </dd>
<p> Print rather than executing the SQL code that would be executed to find all matching objects. This can be useful to save the statement for later execution or to use it as input for other programs.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;version </dd>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> For the <code>&#8211;format</code> option, the permitted values are not case sensitive. In addition, values may be specified as any unambiguous prefix of a valid value. For example, <code>&#8211;format=g</code> specifies the grid format. An error occurs if a prefix matches more than one valid value. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools which is required to read the login-path values from the login configuration file (.mylogin.cnf).<br/>
EXAMPLES </p>
<p> Find all objects with a name that matches the pattern &#8216;t_&#8217; (the letter t followed by any single character): </p>
<dl>
<dt>
</dt><dd>
<pre><code>
$ mysqlmetagrep-- pattern = "t_" --server = mats[at] localhost + -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+ | Connection | Object Type | Object Name | Database |
                                            +-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+ | mats : *@localhost : 3306 | TABLE | t1 | test |
                                                                                                                                                      | mats : *@localhost : 3306 | TABLE | t2 | test |
                                                                                                                                                               | mats : *@localhost : 3306 | TABLE | t3 | test |
                                                                                                                                                                        +-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+
</code></pre>
</dd></dl>
<p> To find all object that contain &#8216;t2&#8217; in the name or the body (for routines, triggers, and events): </p>
<dl>
<dt>
</dt><dd>
$ mysqlmetagrep &#8211; b&#8211; pattern = &#8220;%t2%&#8221; &#8211;server = mats[at] localhost : 3306 + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; -+ | Connection | Object Type | Object Name | Database |<br/>
                                                  +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; -+ | root : *@localhost : 3306 | TRIGGER | tr_foo | test |<br/>
                                                                                                                                                            | root : *@localhost : 3306 | TABLE | t2 | test |<br/>
                                                                                                                                                                     +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; -+
</dd></dl>
<p> In the preceding output, the trigger name does not match the pattern, but is displayed because its body does. </p>
<p> This is the same as the previous example, but using the <code>REGEXP</code> operator. Note that in the pattern it is not necessary to add wildcards before or after t2: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
$ mysqlmetagrep - Gb-- pattern = "t2" --server = mats[at] localhost + -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+ | Connection | Object Type | Object Name | Database |
                                                 +-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+ | root : *@localhost : 3306 | TRIGGER | tr_foo | test |
                                                                                                                                                           | root : *@localhost : 3306 | TABLE | t2 | test |
                                                                                                                                                                    +-- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -- --+-- -- -- -- -- -+
</code></pre>
</dd></dl>
<h2>COPYRIGHT</h2>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> MySQL manual</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://dev.mysql.com/doc/mysql/en/regexp.html">http://dev.mysql.com/doc/mysql/en/regexp.html</a></dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
