---

title: "taskrc(5)"
name: "taskrc"
section: "5"
letter: "t"
url: "/docs/linux/man/5-taskrc/"
description: "taskrc – Configuration details for the"
---

<p>taskrc &#8211; Configuration details for the </p>
<p> <a href="/docs/linux/man/1-task/">task</a>(1) command </p>

<p> <code>$HOME/.taskrc</code> <br/>
 <code>task rc:&lt;directory-path&gt;/.taskrc ...</code> <br/>
 <code>TASKRC=&lt;directory-path&gt;/.taskrc task ...</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Taskwarrior</code> obtains its configuration data from a file called <i>.taskrc</i> . This file is normally located in the user&#8217;s home directory: </p>
<dl>
<dd> <p> $HOME/.taskrc </p>
 </dd></dl>
<p>The default location can be overridden using the <i>rc:</i> attribute when running task: </p>
<dl>
<dd> <p> $ task rc:&lt;directory-path&gt;/.taskrc ... </p>
 </dd></dl>
<p>or using the TASKRC environment variable: </p>
<dl>
<dd> <p> $ TASKRC=/tmp/.taskrc task ... </p>
 </dd></dl>
<p>Individual options can be overridden by using the <i>rc.&lt;name&gt;:</i> attribute when running task: </p>
<dl>
<dd> <p> $ task rc.&lt;name&gt;:&lt;value&gt; ... </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> $ task rc.&lt;name&gt;=&lt;value&gt; ... </p>
 </dd></dl>
<p>If <code>Taskwarrior</code> is run without an existing configuration file it will ask if it should create a default, sample <i>.taskrc</i> file in the user&#8217;s home directory. </p>
<p>The .taskrc file follows a very simply syntax defining name/value pairs: </p>
<dl>
<dd> <p> &lt;name&gt; = &lt;value&gt; </p>
 </dd></dl>
<p>There may be whitespace around &lt;name&gt;, &#8216;=&#8216; and &lt;value&gt;, and it is ignored. Whitespace within the &lt;value&gt; is left intact. Whitespace is not permitted in comma-separated lists. The entry must be on a single line, no continuations. Values support UTF8 as well as JSON encoding, such as \uNNNN. </p>
<p>Note that Taskwarrior is flexible about the values used to represent Boolean items. You can use &quot;on&quot;, &quot;yes&quot;, &quot;y&quot;, &quot;1&quot; and &quot;true&quot;. Anything else means &quot;off&quot;. </p>
<dl>
<dd> <p> include &lt;file&gt; </p>
 </dd></dl>
<p>There may be whitespace around &#8216;include&#8217; and &lt;file&gt;. The file may be an absolute or relative path, and the special character &#8216;~&#8216; is expanded to mean $HOME. The entry must be on a single line, no continuations. </p>
<dl>
<dd> <p> # &lt;comment&gt; </p>
 </dd></dl>
<p>A comment consists of the character &#8216;#&#8216;, and extends from the &#8216;#&#8216; to the end of the line. There is no way to comment a multi-line block. There may be blank lines. </p>
<p>Almost every value has a default setting, and an empty .taskrc file is one that makes use of every default. The contents of the .taskrc file therefore represent overrides of the default values. To remove a default value completely there must be an entry like this: </p>
<dl>
<dd> <p> &lt;name&gt; = </p>
 </dd></dl>
<p>This entry overrides the default value with a blank value. </p>
<h2>EDITING</h2>
<p> You can edit your .taskrc file by hand if you wish, or you can use the &#8216;config&#8217; command. To permanently set a value in your .taskrc file, use this command: </p>
<dl>
<dd> <p> $ task config nag &quot;You have more urgent tasks.&quot; </p>
 </dd></dl>
<p>To delete an entry, use this command: </p>
<dl>
<dd> <p> $ task config nag </p>
 </dd></dl>
<p>Taskwarrior will then use the default value. To explicitly set a value to blank, and therefore avoid using the default value, use this command: </p>
<dl>
<dd> <p> $ task config nag &quot;&quot; </p>
 </dd></dl>
<p>Taskwarrior will also display all your settings with this command: </p>
<dl>
<dd> <p> $ task show </p>
 </dd></dl>
<p>and in addition, will also perform a check of all the values in the file, warning you of anything it finds amiss. </p>
<h2>NESTING CONFIGURATION FILES</h2>
<p> The .taskrc can include other files containing configuration settings by using the <code>include</code> statement: </p>
<dl>
<dd> <p> include &lt;path/to/the/configuration/file/to/be/included&gt; </p>
 </dd></dl>
<p>By using include files you can divide your main configuration file into several ones containing just the relevant configuration data like colors, etc. </p>
<p>There are two excellent uses of includes in your .taskrc, shown here: </p>
<dl>
<dd> <p> include /usr/share/doc/task/rc/holidays.en-US.rc <br/>
 include /usr/share/doc/task/rc/dark-16.theme </p>
 </dd></dl>
<p>This includes two standard files that are distributed with Taskwarrior, which define a set of US holidays, and set up a 16-color theme to use, to color the reports and calendar. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> These environment variables override defaults and command line arguments. </p>
<dl>
<dt><code>TASKDATA=~/.task</code></dt>
<dd> <p> This overrides the default path for the Taskwarrior data files. </p>
 </dd>
<dt><code>TASKRC=~/.taskrc</code></dt>
<dd> <p> This overrides the default RC file. </p>
 </dd></dl>
<h2>CONFIGURATION VARIABLES</h2>
<p> Valid variable names and their default values are: </p>
<h3>FILES</h3>
<dl>
<dt><code>data.location=$HOME/.task</code></dt>
<dd> <p> This is a path to the directory containing all the Taskwarrior files. By default, it is set up to be ~/.task, for example: /home/paul/.task </p>
<p>Note that you can use the <code>~</code> shell meta character, which will be properly expanded. </p>
<p>Note that the TASKDATA environment variable overrides this setting. </p>
 </dd>
<dt><code>locking=on</code></dt>
<dd> <p> Determines whether to use file locking when accessing the pending.data and completed.data files. Defaults to &quot;on&quot;. Solaris users who store the data files on an NFS mount may need to set locking to &quot;off&quot;. Note that there is danger in setting this value to &quot;off&quot; - another program (or another instance of task) may write to the task.pending file at the same time. </p>
 </dd>
<dt><code>gc=on</code></dt>
<dd> <p> Can be used to temporarily suspend garbage collection (gc), so that task IDs don&#8217;t change. Note that this should be used in the form of a command line override (task rc.gc=off ...), and not permanently used in the .taskrc file, as this significantly affects performance in the long term. </p>
 </dd>
<dt><code>hooks=on</code></dt>
<dd> <p> This master control switch enables hook script processing. The default value is &#8216;on&#8217;, but certain extensions and environments may need to disable hooks. </p>
 </dd>
<dt><code>exit.on.missing.db=no</code></dt>
<dd> <p> When set to &#8216;yes&#8217; causes the program to exit if the database (~/.task or rc.data.location or TASKDATA override) is missing. Default value is &#8216;no&#8217;. </p>
 </dd></dl>
<h3>TERMINAL</h3>
<dl>
<dt><code>detection=on</code></dt>
<dd> <p> Determines whether to use ioctl to establish the size of the window you are using, for text wrapping. </p>
 </dd>
<dt><code>defaultwidth=80</code></dt>
<dd> <p> The width of output used when auto-detection support is not available. Defaults to 80. If set to 0, it is interpreted as infinite width, therefore with no word-wrapping; this is useful when redirecting report output to a file for subsequent handling. </p>
 </dd>
<dt><code>defaultheight=24</code></dt>
<dd> <p> The height of output used when auto-detection support is not available. Defaults to 24. If set to 0, it is interpreted as infinite height. This is useful when redirecting charts to a file for subsequent handling. </p>
 </dd>
<dt><code>avoidlastcolumn=no</code></dt>
<dd> <p> Causes the width of the terminal minus one to be used as the full width. This avoids placing color codes in the last column which can cause problems for Cygwin users. Default value is &#8216;no&#8217;. </p>
 </dd>
<dt><code>hyphenate=on</code></dt>
<dd> <p> Hyphenates lines when wrapping breaks occur mid-word. Default value is &#8216;on&#8217;. </p>
 </dd>
<dt><code>editor=vi</code></dt>
<dd> <p> Specifies which text editor you wish to use for when the <code>task edit &lt;ID&gt;</code> command is used. Taskwarrior will first look for this configuration variable. If found, it is used. Otherwise it will look for the $VISUAL or $EDITOR environment variables, before it defaults to using &quot;vi&quot;. </p>
 </dd>
<dt><code>reserved.lines=1</code></dt>
<dd> <p> This is the number of lines reserved at the bottom of the screen for the shell prompt. This is only referenced when &#8216;limit:page&#8217; is used. </p>
 </dd></dl>
<h3>MISCELLANEOUS</h3>
<dl>
<dt><code>verbose=on|off|nothing|list...</code></dt>
<dd> <p> When set to &quot;on&quot; (the default), helpful explanatory comments are added to all output from Taskwarrior. Setting this to &quot;off&quot; means that you would see regular output. </p>
<p>The special value &quot;nothing&quot; can be used to eliminate all optional output, which results in only the formatted data being shown, with nothing else. This output is most readily parsed and used by shell scripts. </p>
<p>Alternatively, you can specify a comma-separated list of verbosity tokens that control specific occasions when output is generated. This list may contain: </p>
<p> <br/>
&nbsp;<wbr>blank&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Inserts extra blank lines in output, for clarity <br/>
&nbsp;<wbr>header&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Messages that appear before report output <br/>
&nbsp;<wbr>footnote&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Messages that appear after report output <br/>
&nbsp;<wbr>label&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Column labels on tabular reports <br/>
&nbsp;<wbr>new-id&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Provides feedback of any new task IDs <br/>
&nbsp;<wbr>new-uuid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Provides feedback of any new task UUIDs. Deprecated, to be <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>merged with new-id. <br/>
&nbsp;<wbr>affected&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Reports&nbsp;<wbr>&#8216;N tasks affected&#8217;&nbsp;<wbr>and similar <br/>
&nbsp;<wbr>edit&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Used the verbose template for the&nbsp;<wbr>&#8216;edit&#8217;&nbsp;<wbr>command <br/>
&nbsp;<wbr>special&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Feedback when applying special tags <br/>
&nbsp;<wbr>project&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Feedback about project status changes <br/>
&nbsp;<wbr>sync&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Feedback about sync <br/>
&nbsp;<wbr>filter&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Shows the filter used in the command <br/>
&nbsp;<wbr>unwait&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Notification when a task leaves the&nbsp;<wbr>&#8216;waiting&#8217;&nbsp;<wbr>state <br/>
&nbsp;<wbr>recur&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Notification when a new recurring task instance is created </p>
<p>&quot;affected&quot;, &quot;new-id&quot;, &quot;new-uuid&quot; &quot;project&quot; and &quot;unwait&quot; imply &quot;footnote&quot;. </p>
<p>Note that the &quot;on&quot; setting is equivalent to all the tokens being specified, and the &quot;nothing&quot; setting is equivalent to none of the tokens being specified. </p>
<p>Here are the shortcut equivalents: </p>
<p> <br/>
&nbsp;<wbr>verbose=on <br/>
&nbsp;<wbr>verbose=blank,header,footnote,label,new-id,affected,edit,special,project,sync,filter,unwait </p>
<p> <br/>
&nbsp;<wbr>verbose=off <br/>
&nbsp;<wbr>verbose=blank,label,new-id,edit </p>
<p> <br/>
&nbsp;<wbr>verbose=nothing <br/>
&nbsp;<wbr>verbose= </p>
<p>Those additional comments are sent to the standard error for header, footnote and project. The others are sent to standard output. </p>
 </dd>
<dt><code>confirmation=yes</code></dt>
<dd> <p> May be &quot;yes&quot; or &quot;no&quot;, and determines whether Taskwarrior will ask for confirmation before deleting a task or performing the undo command. The default value is &quot;yes&quot;. Consider leaving this setting as &quot;yes&quot;, for safety. </p>
 </dd>
<dt><code>allow.empty.filter=yes</code></dt>
<dd> <p> An empty filter combined with a write command is potentially a way to modify all tasks by mistake, and when this is detected, confirmation is required. Setting this to &#8216;no&#8217; means that it is an error to use a write command with no filter. </p>
 </dd>
<dt><code>indent.annotation=2</code></dt>
<dd> <p> Controls the number of spaces to indent annotations when shown beneath the description field. The default value is &quot;2&quot;. </p>
 </dd>
<dt><code>indent.report=0</code></dt>
<dd> <p> Controls the indentation of the entire report output. Default is &quot;0&quot;. </p>
 </dd>
<dt><code>row.padding=0</code></dt>
<dd> <p> Controls left and right padding around each row of the report output. Default is &quot;0&quot;. </p>
 </dd>
<dt><code>column.padding=0</code></dt>
<dd> <p> Controls padding between columns of the report output. Default is &quot;1&quot;. </p>
 </dd>
<dt><code>bulk=3</code></dt>
<dd> <p> Is a number, defaulting to 3. When this number or greater of tasks are modified in a single command, confirmation will be required, regardless of the value of <code>confirmation</code> variable. The special value bulk=0 is treated as an infinity. </p>
<p>This is useful for preventing large-scale unintended changes. </p>
 </dd>
<dt><code>nag=You have more urgent tasks.</code></dt>
<dd> <p> This may be a string of text, or blank. It is used as a prompt when a task is started of completed, when there are other tasks with a higher urgency. Default value is: &#8216;You have more urgent tasks&#8217;. It is a gentle reminder that you are contradicting your own urgency settings. </p>
 </dd>
<dt><code>list.all.projects=no</code></dt>
<dd> <p> May be yes or no, and determines whether the &#8216;projects&#8217; command lists all the project names you have used, or just the ones used in active tasks. The default value is &quot;no&quot;. </p>
 </dd>
<dt><code>summary.all.projects=no</code></dt>
<dd> <p> If set to yes, shows all projects in the summary report, even if there are no pending tasks. The default value is &quot;no&quot;. </p>
 </dd>
<dt><code>complete.all.tags=yes</code></dt>
<dd> <p> May be yes or no, and determines whether the tab completion scripts consider all the tag names you have used, or just the ones used in active tasks. The default value is &quot;no&quot;. </p>
 </dd>
<dt><code>list.all.tags=yes</code></dt>
<dd> <p> May be yes or no, and determines whether the &#8216;tags&#8217; command lists all the tag names you have used, or just the ones used in active tasks. The default value is &quot;no&quot;. </p>
 </dd>
<dt><code>print.empty.columns=no</code></dt>
<dd> <p> May be yes or no, and determines whether columns with no data for any task are printed. Defaults to no. </p>
 </dd>
<dt><code>search.case.sensitive=yes</code></dt>
<dd> <p> May be yes or no, and determines whether keyword lookup and substitutions on the description and annotations are done in a case sensitive way. Defaults to yes on most platforms. Defaults to no on Cygwin due to older regex library problems with case-insensitivity. </p>
 </dd>
<dt><code>regex=on</code></dt>
<dd> <p> Controls whether regular expression support is enabled. The default value is on. </p>
 </dd>
<dt><code>xterm.title=no</code></dt>
<dd> <p> Sets the xterm window title when reports are run. Defaults to off. </p>
 </dd>
<dt><code>expressions=infix|postfix</code></dt>
<dd> <p> Sets a preference for infix expressions (1 + 2) or postfix expressions (1 2 +). Defaults to infix. </p>
 </dd>
<dt><code>json.array=on</code></dt>
<dd> <p> Determines whether the export command encloses the JSON output in &#8216;[...]&#8216; and adds &#8216;,&#8216; after each exported task object to create a properly-formed JSON array. With json.array=off, export writes raw JSON objects to STDOUT, one per line. Defaults to on. </p>
 </dd>
<dt><code>json.depends.array=on</code></dt>
<dd> <p> Determines whether the export command encodes dependencies as an array of string UUIDs, or one comma-separated string. Defaults to on. </p>
 </dd>
<dt><code>_forcecolor=no</code></dt>
<dd> <p> Taskwarrior shuts off color automatically when the output is not sent directly to a TTY. For example, this command: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> $ task list &gt; file </p>
 </dd></dl>
<p>will not use any color. To override this, use: </p>
<dl>
<dd> <p> $ task rc._forcecolor=yes list &gt; file </p>
 </dd></dl>
</dl>
<dt><code>active.indicator=*</code></dt>
<dd> <p> The character or string to show in the start.active column. Defaults to *. </p>
 </dd>
<dt><code>tag.indicator=+</code></dt>
<dd> <p> The character or string to show in the tag.indicator column. Defaults to +. </p>
 </dd>
<dt><code>dependency.indicator=D</code></dt>
<dd> <p> The character or string to show in the depends.indicator column. Defaults to +. </p>
 </dd>
<dt><code>uda.&lt;name&gt;.indicator=U</code></dt>
<dd> <p> The character or string to show in the &lt;uda&gt;.indicator column. Defaults to U. </p>
 </dd>
<dt><code>recurrence=yes</code></dt>
<dd> <p> Controls whether recurrence is enabled, and whether recurring tasks continue to generate new task instances. Defaults to &#8216;yes&#8217;. </p>
 </dd>
<dt><code>recurrence.confirmation=prompt</code></dt>
<dd> <p> Controls whether changes to recurring tasks propagates to other child tasks with or without confirmation. A value of &#8216;yes&#8217; means propagate changes without confirmation. A value of &#8216;no&#8217; means do not propagate changes and don&#8217;t ask for confirmation. A value of &#8216;prompt&#8217; prompts you every time. Defaults to &#8216;prompt&#8217;. </p>
 </dd>
<dt><code>recurrence.indicator=R</code></dt>
<dd> <p> The character or string to show in the recurrence_indicator column. Defaults to R. </p>
 </dd>
<dt><code>recurrence.limit=1</code></dt>
<dd> <p> The number of future recurring tasks to show. Defaults to 1. For example, if a weekly recurring task is added with a due date of tomorrow, and recurrence.limit is set to 2, then a report will list 2 pending recurring tasks, one for tomorrow, and one for a week from tomorrow. </p>
 </dd>
<dt><code>undo.style=side</code></dt>
<dd> <p> When the &#8216;undo&#8217; command is run, Taskwarrior presents a before and after comparison of the data. This can be in either the &#8216;side&#8217; style, which compares values side-by-side in a table, or &#8216;diff&#8217; style, which uses a format similar to the &#8216;diff&#8217; command. </p>
 </dd>
<dt><code>abbreviation.minimum=2</code></dt>
<dd> <p> Minimum length of any abbreviated command/value. This means that &quot;ve&quot;, &quot;ver&quot;, &quot;vers&quot;, &quot;versi&quot;, &quot;versio&quot; will all equate to &quot;version&quot;, but &quot;v&quot; will not. Default is 2. </p>
 </dd>
<dt><code>debug=off</code></dt>
<dd> <p> Taskwarrior has a debug mode that causes diagnostic output to be displayed. Typically this is not something anyone would want, but when reporting a bug, debug output can be useful. It can also help explain how the command line is being parsed, but the information is displayed in a developer-friendly, not a user-friendly way. </p>
<p>Turning debug on automatically sets debug.hooks=1, debug.parser=1 and debug.tls=2 if they do not already have assigned values. </p>
 </dd>
<dt><code>debug.hooks=0</code></dt>
<dd> <p> Controls the hook system diagnostic level. Level 0 means no diagnostics. Level 1 shows hook calls. Level 2 also shows exit status and I/O. </p>
 </dd>
<dt><code>debug.parser=0</code></dt>
<dd> <p> Controls the parser diagnostic level. Level 0 shows no diagnostics. Level 1 shows the final parse tree. Level 2 shows the parse tree from all phases of the parse. Level 3 shows expression evaluation details. </p>
 </dd>
<dt><code>debug.tls=0</code></dt>
<dd> <p> Controls the GnuTLS diagnostic level. For &#8216;sync&#8217; debugging. Level 0 means no diagnostics. Level 9 is the highest. Level 2 is a good setting for debugging. </p>
 </dd>
<dt><code>obfuscate=1</code></dt>
<dd> <p> When set to &#8216;1&#8217;, will replace all report text with &#8216;xxx&#8217;. This is useful for sharing report output in bug reports. Default value is &#8216;0&#8217;. </p>
 </dd>
<dt><code>alias.rm=delete</code></dt>
<dd> <p> Taskwarrior supports command aliases. This alias provides an alternate name (rm) for the delete command. You can use aliases to provide alternate names for any of the commands. Several commands you may use are actually aliases - the &#8216;history&#8217; report, for example, or &#8216;export&#8217;. </p>
 </dd></dl>
<h3>DATES</h3>
<dl>
<dt><code>dateformat=Y-M-D</code></dt>
<dd>  </dd>
<dt><code>dateformat.report=</code></dt>
<dd>  </dd>
<dt><code>dateformat.holiday=YMD</code></dt>
<dd>  </dd>
<dt><code>dateformat.edit=Y-M-D H:N:S</code></dt>
<dd>  </dd>
<dt><code>dateformat.info=Y-M-D H:N:S</code></dt>
<dd>  </dd>
<dt><code>dateformat.annotation=</code></dt>
<dd>  </dd>
<dt><code>report.X.dateformat=Y-M-D</code></dt>
<dd> <p> This is a string of characters that defines how Taskwarrior formats date values. The precedence order for the configuration variable is report.X.dateformat then dateformat.report then dateformat for formatting the due dates in reports. If both report.X.dateformat and dateformat.report are not set then dateformat will be applied to the date. Entered dates as well as all other displayed dates in reports are formatted according to dateformat. </p>
<p>The default value is the ISO-8601 standard: Y-M-D. The string can contain the characters: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> m minimal-digit month, for example 1 or 12 <br/>
 d minimal-digit day, for example 1 or 30 <br/>
 y two-digit year, for example 09 or 12 <br/>
 D two-digit day, for example 01 or 30 <br/>
 M two-digit month, for example 01 or 12 <br/>
 Y four-digit year, for example 2009 or 2015 <br/>
 a short name of weekday, for example Mon or Wed <br/>
 A long name of weekday, for example Monday or Wednesday <br/>
 b short name of month, for example Jan or Aug <br/>
 B long name of month, for example January or August <br/>
 v minimal-digit week, for example 3 or 37 <br/>
 V two-digit week, for example 03 or 37 <br/>
 h minimal-digit hour, for example 3 or 21 <br/>
 n minimal-digit minutes, for example 5 or 42 <br/>
 s minimal-digit seconds, for example 7 or 47 <br/>
 H two-digit hour, for example 03 or 21 <br/>
 N two-digit minutes, for example 05 or 42 <br/>
 S two-digit seconds, for example 07 or 47 <br/>
 J three-digit Julian day, for example 023 or 365 <br/>
 j Julian day, for example 23 or 365 </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The characters &#8216;v&#8217;, &#8216;V&#8217;, &#8216;a&#8217; and &#8216;A&#8217; can only be used for formatting printed dates (not to parse them). </p>
 </dd></dl>
<dl>
<dd> <p> The string may also contain other characters to act as spacers, or formatting. Examples for other values of dateformat: </p>
 </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 d/m/Y would use for input and output 24/7/2009 <br/>
 yMD would use for input and output 090724 <br/>
 M-D-Y would use for input and output 07-24-2009 </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Examples for other values of dateformat.report: </p>
 </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 a D b Y (V) would emit &quot;Fri 24 Jul 2009 (30)&quot; <br/>
 A, B D, Y would emit &quot;Friday, July 24, 2009&quot; <br/>
 wV a Y-M-D would emit &quot;w30 Fri 2009-07-24&quot; <br/>
 yMD.HN would emit &quot;110124.2342&quot; <br/>
 m/d/Y H:N would emit &quot;1/24/2011 10:42&quot; <br/>
 a D b Y H:N:S would emit &quot;Mon 24 Jan 2011 11:19:42&quot; </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Undefined fields are put to their minimal valid values (1 for month and day and 0 for hour, minutes and seconds) when there is at least one more global date field that is set. Otherwise, they are set to the corresponding values of &quot;now&quot;. For example: </p>
 </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 8/1/2013 with m/d/Y implies August 1, 2013 at midnight (inferred) <br/>
 8/1 20:40 with m/d H:N implies August 1, 2013 (inferred) at 20:40 </p>
 </dd></dl>
</dl>
<dt><code>date.iso=yes</code></dt>
<dd> <p> Enables ISO-8601 date support. The default value is &quot;yes&quot;. </p>
 </dd>
<dt><code>weekstart=Sunday</code></dt>
<dd> <p> Determines the day a week starts. Valid values are Sunday or Monday only. The default value is &quot;Sunday&quot;. </p>
 </dd>
<dt><code>displayweeknumber=yes</code></dt>
<dd> <p> Determines if week numbers are displayed when using the &quot;task calendar&quot; command. The week number is dependent on the day a week starts. The default value is &quot;yes&quot;. </p>
 </dd>
<dt><code>due=7</code></dt>
<dd> <p> This is the number of days into the future that define when a task is considered due, and is colored accordingly. The default value is 7. </p>
 </dd>
<dt><code>calendar.details=sparse</code></dt>
<dd> <p> If set to full running &quot;task calendar&quot; will display the details of tasks with due dates that fall into the calendar period. The corresponding days will be color-coded in the calendar. If set to sparse only the corresponding days will be color coded and no details will be displayed. The displaying of due dates with details is turned off by setting the variable to none. The default value is &quot;sparse&quot;. </p>
 </dd>
<dt><code>calendar.details.report=list</code></dt>
<dd> <p> The report to run when displaying the details of tasks with due dates when running the &quot;task calendar&quot; command. The default value is &quot;list&quot;. </p>
 </dd>
<dt><code>calendar.offset=off</code></dt>
<dd> <p> If &quot;on&quot; the first month in the calendar report is effectively changed by the offset value specified in calendar.offset.value. It defaults to &quot;off&quot;. </p>
 </dd>
<dt><code>calendar.offset.value=-1</code></dt>
<dd> <p> The offset value to apply to the first month in the calendar report. The default value is &quot;-1&quot;. </p>
 </dd>
<dt><code>calendar.holidays=full</code></dt>
<dd> <p> If set to full running &quot;task calendar&quot; will display holidays in the calendar by color-coding the corresponding days. A detailed list with the dates and names of the holidays is also shown. If set to sparse only the days are color-coded and no details on the holidays will be displayed. The displaying of holidays is turned off by setting the variable to none. The default value is &quot;none&quot;. </p>
 </dd>
<dt><code>calendar.legend=yes</code></dt>
<dd> <p> Determines whether the calendar legend is displayed. The default value is &quot;yes&quot;. </p>
 </dd></dl>
<h3>JOURNAL ENTRIES</h3>
<dl>
<dt><code>journal.time=no</code></dt>
<dd> <p> May be yes or no, and determines whether the &#8216;start&#8217; and &#8216;stop&#8217; commands should record an annotation when being executed. The default value is &quot;no&quot;. The text of the corresponding annotations is controlled by: </p>
 </dd>
<dt><code>journal.time.start.annotation=Started task</code></dt>
<dd> <p> The text of the annotation that is recorded when executing the start command and having set journal.time. </p>
 </dd>
<dt><code>journal.time.stop.annotation=Stopped task</code></dt>
<dd> <p> The text of the annotation that is recorded when executing the stop command and having set journal.time. </p>
 </dd>
<dt><code>journal.info=on</code></dt>
<dd> <p> When enabled, this setting causes a change log of each task to be displayed by the &#8216;info&#8217; command. Default value is &quot;on&quot;. </p>
 </dd></dl>
<h3>HOLIDAYS</h3>
<p> Holidays are entered either directly in the .taskrc file or via an include file that is specified in .taskrc. For each holiday the name and the date is required to be given: </p>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 holiday.towel.name=Day of the towel <br/>
 holiday.towel.date=20100525 <br/>
 holiday.sysadmin.name=System Administrator Appreciation Day <br/>
 holiday.sysadmin.date=20100730 </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> Dates are to be entered according to the setting in the dateformat.holiday variable. </p>
 </dd></dl>
<dl>
<dd> <p> The following holidays are computed automatically: Good Friday (goodfriday), Easter (easter), Easter Monday (eastermonday), Ascension (ascension), Pentecost (pentecost). The date for these holidays is the given keyword: </p>
 </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 holiday.eastersunday.name=Easter <br/>
 holiday.eastersunday.date=easter </p>
 </dd></dl>
</dl>
<p>Note that the Taskwarrior distribution contains example holiday files that can be included like this: </p>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <br/>
 include /usr/share/doc/task/rc/holidays.en-US.rc </p>
 </dd></dl>
</dl>
<dl>
<dt><code>monthsperline=3</code></dt>
<dd> <p> Determines how many months the &quot;task calendar&quot; command renders across the screen. Defaults to however many will fit. If more months than will fit are specified, Taskwarrior will only show as many that will fit. </p>
 </dd></dl>
<h3>DEPENDENCIES</h3>
<dl>
<dt><code>dependency.reminder=on</code></dt>
<dd> <p> Determines whether dependency chain violations generate reminders. </p>
 </dd>
<dt><code>dependency.confirmation=yes</code></dt>
<dd> <p> Determines whether dependency chain repair requires confirmation. </p>
 </dd></dl>
<h3>COLOR CONTROLS</h3>
<dl>
<dt><code>color=on</code></dt>
<dd> <p> May be &quot;on&quot; or &quot;off&quot;. Determines whether Taskwarrior uses color. When &quot;off&quot;, will use dashes (-----) to underline column headings. </p>
 </dd>
<dt><code>fontunderline=on</code></dt>
<dd> <p> Determines if font underlines or ASCII dashes should be used to underline headers, even when color is enabled. </p>
<p>Taskwarrior has a number of coloration rules. They correspond to a particular attribute of a task, such as it being due, or being active, and specifies the automatic coloring of that task. A list of valid colors, depending on your terminal, can be obtained by running the command: </p>
 </dd>
<dl>
<dd> <p> <code>task color</code> </p>
 </dd></dl>
<dl>
<dd> <p> Note that no default values are listed here - the defaults now correspond to the dark-256.theme (Linux) and dark-16.theme (other) theme values. The coloration rules are as follows: </p>
 </dd></dl>
<dl>
<dd> <p> <code>color.due.today</code> Task is due today <br/>
 <code>color.active</code> Task is started, therefore active. <br/>
 <code>color.scheduled</code> Task is scheduled, therefore ready for work. <br/>
 <code>color.until</code> Task has an expiration date. <br/>
 <code>color.blocking</code> Task is blocking another in a dependency. <br/>
 <code>color.blocked</code> Task is blocked by a dependency. <br/>
 <code>color.overdue</code> Task is overdue (due some time prior to now). <br/>
 <code>color.due</code> Task is coming due. <br/>
 <code>color.project.none</code> Task does not have an assigned project. <br/>
 <code>color.tag.none</code> Task has no tags. <br/>
 <code>color.tagged</code> Task has at least one tag. <br/>
 <code>color.recurring</code> Task is recurring. <br/>
 <code>color.completed</code> Task is completed. <br/>
 <code>color.deleted</code> Task is deleted. </p>
 </dd></dl>
<dl>
<dd> <p> To disable a coloration rule for which there is a default, set the value to nothing, for example: </p>
 </dd>
<dl>
<dd> <p> <code>color.tagged=</code> </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> By default, colors produced by rules blend. This has the advantage of conveying additional information, by producing combinations that are not used by any particular rule directly. </p>
<p>However, color blending can produce highlighting combinations which are not desired. In such cases, use the following option to disable this behaviour: </p>
 </dd></dl>
<dt><code>rule.color.merge=yes</code></dt>
<dd> <p> Can be &quot;yes&quot; or &quot;no&quot;. When &quot;no&quot;, disables merging of colors produced by different color rules. Use if your color scheme produces unpleasing foreground and background combinations. </p>
<p>See the <a href="/docs/linux/man/5-task-color/">task-color</a>(5) man pages for color details. </p>
<p>Certain attributes like tags, projects and keywords can have their own coloration rules. </p>
 </dd>
<dt><code>color.tag.X=yellow</code></dt>
<dd> <p> Colors any task that has the tag X. </p>
 </dd>
<dt><code>color.project.X=on green</code></dt>
<dd> <p> Colors any task assigned to project X. </p>
 </dd>
<dt><code>color.keyword.X=on blue</code></dt>
<dd> <p> Colors any task where the description or any annotation contains X. </p>
 </dd>
<dt><code>color.uda.X=on green</code></dt>
<dd> <p> Colors any task that has the user defined attribute X. </p>
 </dd>
<dt><code>color.uda.X.VALUE=on green</code></dt>
<dd> <p> Colors any task that has the user defined attribute X set to VALUE. </p>
 </dd>
<dt><code>color.uda.X.none=on green</code></dt>
<dd> <p> Colors any task that does not have the user defined attribute X. </p>
 </dd>
<dt><code>color.error=white on red</code></dt>
<dd> <p> Colors any of the error messages. </p>
 </dd>
<dt><code>color.warning=bold red</code></dt>
<dd> <p> Colors any of the warning messages. </p>
 </dd>
<dt><code>color.header=green</code></dt>
<dd> <p> Colors any of the messages printed prior to the report output. </p>
 </dd>
<dt><code>color.footnote=green</code></dt>
<dd> <p> Colors any of the messages printed last. </p>
 </dd>
<dt><code>color.summary.bar=on green</code></dt>
<dd> <p> Colors the summary progress bar. Should consist of a background color. </p>
 </dd>
<dt><code>color.summary.background=on black</code></dt>
<dd> <p> Colors the summary progress bar. Should consist of a background color. </p>
 </dd>
<dt><code>color.calendar.today=black on cyan</code></dt>
<dd> <p> Color of today in calendar. </p>
 </dd>
<dt><code>color.calendar.due=black on green</code></dt>
<dd> <p> Color of days with due tasks in calendar. </p>
 </dd>
<dt><code>color.calendar.due.today=black on magenta</code></dt>
<dd> <p> Color of today with due tasks in calendar. </p>
 </dd>
<dt><code>color.calendar.overdue=black on red</code></dt>
<dd> <p> Color of days with overdue tasks in calendar. </p>
 </dd>
<dt><code>color.calendar.weekend=bright white on black</code></dt>
<dd> <p> Color of weekend days in calendar. </p>
 </dd>
<dt><code>color.calendar.holiday=black on bright yellow</code></dt>
<dd> <p> Color of holidays in calendar. </p>
 </dd>
<dt><code>color.calendar.weeknumber=black on white</code></dt>
<dd> <p> Color of weeknumbers in calendar. </p>
 </dd>
<dt><code>color.label=</code></dt>
<dd> <p> Colors the report labels. Defaults to not use color. </p>
 </dd>
<dt><code>color.label.sort=</code></dt>
<dd> <p> Colors the report labels for sort columns. Defaults to color.label. </p>
 </dd>
<dt><code>color.alternate=on rgb253</code></dt>
<dd> <p> Color of alternate tasks. This is to apply a specific color to every other task in a report, which can make it easier to visually separate tasks. This is especially useful when tasks are displayed over multiple lines due to long descriptions or annotations. </p>
 </dd>
<dt><code>color.history.add=on red</code></dt>
<dd> <p> <br/>
 <code>color.history.done=on green</code> <br/>
 <code>color.history.delete=on yellow</code> </p>
 </dd>
<dl>
<dd> <p> Colors the bars on the ghistory report graphs. Defaults to red, green and yellow bars. </p>
 </dd></dl>
<dt><code>color.burndown.pending=on red</code></dt>
<dd> <p> <br/>
 <code>color.burndown.started=on yellow</code> <br/>
 <code>color.burndown.done=on green</code> </p>
 </dd>
<dl>
<dd> <p> Colors the bars on the burndown reports graphs. Defaults to red, green and yellow bars. </p>
 </dd></dl>
<dt><code>color.undo.before=red</code></dt>
<dd> <p> <br/>
 <code>color.undo.after=green</code> </p>
 </dd>
<dl>
<dd> <p> Colors used by the undo command, to indicate the values both before and after a change that is to be reverted. </p>
 </dd></dl>
<dt><code>color.sync.added=green</code></dt>
<dd> <p> <br/>
 <code>color.sync.changed=yellow</code> <br/>
 <code>color.sync.rejected=red</code> </p>
 </dd>
<dl>
<dd> <p> Colors the output of the sync command. </p>
 </dd></dl>
<dt><code>rule.precedence.color=due.today,active,blocking,blocked,overdue,due,</code></dt>
<dd> <p> <code>scheduled,keyword.,project.,tag.,uda.,recurring,</code> <code>pri.,tagged,completed,deleted</code> </p>
 </dd>
<dl>
<dd> <p> This setting specifies the precedence of the color rules, from highest to lowest. Note that the prefix &#8216;color.&#8216; is omitted (for brevity), and that any wildcard value (color.tag.XXX) is shortened to &#8216;tag.&#8216;, which places all specific tag rules at the same precedence, again for brevity. </p>
 </dd></dl>
<dt><code>color.debug=green</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Colors all debug output, if enabled. </p>
 </dd></dl>
<h3>URGENCY</h3>
<p>The urgency calculation uses a polynomial with several terms, each of which has a configurable coefficient. Those coefficients are: </p>
<dl>
<dt><code>urgency.blocking.coefficient=8.0</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Urgency coefficient for blocking tasks </p>
 </dd></dl>
<p> <code>urgency.blocked.coefficient=-5.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for blocked tasks </p>
 </dd></dl>
<p> <code>urgency.due.coefficient=12.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for due dates </p>
 </dd></dl>
<p> <code>urgency.waiting.coefficient=-3.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for waiting status </p>
 </dd></dl>
<p> <code>urgency.active.coefficient=4.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for active tasks </p>
 </dd></dl>
<p> <code>urgency.scheduled.coefficient=5.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for scheduled tasks </p>
 </dd></dl>
<p> <code>urgency.project.coefficient=1.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for projects </p>
 </dd></dl>
<p> <code>urgency.tags.coefficient=1.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for tags </p>
 </dd></dl>
<p> <code>urgency.annotations.coefficient=1.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for annotations </p>
 </dd></dl>
<p> <code>urgency.age.coefficient=2.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for the age of tasks </p>
 </dd></dl>
<p> <code>urgency.age.max=365</code> </p>
<dl>
<dd> <p> Maximum age in days. After this number of days has elapsed, the urgency of a task won&#8217;t increase any more because of aging. </p>
 </dd></dl>
<p> <code>urgency.user.tag.&lt;tag&gt;.coefficient=...</code> </p>
<dl>
<dd> <p> Specific tag coefficient. </p>
 </dd></dl>
<p> <code>urgency.user.tag.next.coefficient=15.0</code> </p>
<dl>
<dd> <p> Urgency coefficient for tag &#8216;next&#8217;. </p>
 </dd></dl>
<p> <code>urgency.user.project.&lt;project&gt;.coefficient=...</code> </p>
<dl>
<dd> <p> Specific project coefficient. </p>
 </dd></dl>
<p> <code>urgency.user.keyword.&lt;keyword&gt;.coefficient=...</code> </p>
<dl>
<dd> <p> Specific description keyword coefficient. </p>
 </dd></dl>
<p> <code>urgency.uda.&lt;name&gt;.coefficient=...</code> </p>
<dl>
<dd> <p> Presence/absence of UDA data. </p>
 </dd></dl>
<p> <code>urgency.uda.&lt;name&gt;.&lt;value&gt;.coefficient=...</code> </p>
<dl>
<dd> <p> Specific value of UDA data. </p>
 </dd></dl>
<p>The coefficients reflect the relative importance of the various terms in the urgency calculation. These are default values, and may be modified to suit your preferences, but it is important that you carefully consider any modifications. </p>
<p> <code>urgency.inherit=off</code> </p>
<dl>
<dd> <p> Not actually a coefficient. When enabled, blocking tasks inherit the highest urgency value found in the tasks they block. This is done recursively. It is recommended to set urgency.blocking.coefficient and urgency.blocked.coefficient to 0.0 in order for this setting to be the most useful. </p>
 </dd></dl>
<h3>DEFAULTS</h3>
<dl>
<dt><code>default.project=foo</code></dt>
<dd> <p> Provides a default project name for the <i>task add</i> command, if you don&#8217;t specify one. The default is blank. </p>
 </dd>
<dt><code>default.due=...</code></dt>
<dd> <p> Provides a default due date for the <i>task add</i> command, if you don&#8217;t specify one. You can use a date, or a duration value which is assumed to be relative to &#8216;now&#8217;. The default is blank. </p>
 </dd>
<dt><code>uda.&lt;name&gt;.default=...</code></dt>
<dd> <p> Provides default values for UDA fields when using the <i>task add</i> command, if you don&#8217;t specify values. The default is blank. </p>
 </dd>
<dt><code>default.command=next</code></dt>
<dd> <p> Provides a default command that is run every time Taskwarrior is invoked with no arguments. For example, if set to: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> default.command=project:foo list </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> then Taskwarrior will run the &quot;project:foo list&quot; command if no command is specified. This means that by merely typing </p>
 </dd></dl>
<dl>
<dd>  </dd>
<dl>
<dd> <p> $ task <br/>
 [task project:foo list] <br/>
 <br/>
 ID Project Pri Description <br/>
&nbsp;<wbr>1 foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Design foo <br/>
&nbsp;<wbr>2 foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Build foo </p>
 </dd></dl>
</dl>
<h3>REPORTS</h3>
<p>The reports can be customized by using the following configuration variables. The output columns, their labels and the sort order can be set using the corresponding variables for each report. Each report name is used as a &quot;command&quot; name. For example </p>
<dl>
<dt><code>task overdue</code></dt>
<dd>  </dd>
<dt><code>report.X.description</code></dt>
<dd> <p> The description for report X when running the &quot;task help&quot; command. </p>
 </dd>
<dt><code>report.X.columns</code></dt>
<dd> <p> This is a comma-separated list of columns and formatting specifiers. See the command &#8216;task columns&#8217; for a full list of options and examples. </p>
 </dd>
<dt><code>report.X.labels</code></dt>
<dd> <p> The labels for each column that will be used when generating report X. The labels are a comma separated list. </p>
 </dd>
<dt><code>report.X.sort</code></dt>
<dd> <p> The sort order of the tasks in the generated report X. The sort order is specified by using the column ids post-fixed by a &quot;+&quot; for ascending sort order or a &quot;-&quot; for descending sort order. The sort IDs are separated by commas. For example: </p>
<p> <br/>
&nbsp;<wbr>report.list.sort=due+,priority-,start.active-,project+ </p>
<p>Additionally, after the &quot;+&quot; or &quot;-&quot;, there can be a solidus &quot;/&quot; which indicates that there are breaks after the column values change. For example: </p>
<p> <br/>
&nbsp;<wbr>report.minimal.sort=project+/,description+ </p>
<p>This sort order now specifies that there is a listing break between each project. A listing break is simply a blank line, which provides a visual grouping. </p>
<p>A special sort value of &quot;none&quot; indicates that no sorting is required, and tasks will be presented in the order (if any) in which they are selected. </p>
 </dd>
<dt><code>report.X.filter</code></dt>
<dd> <p> This adds a filter to the report X so that only tasks matching the filter criteria are displayed in the generated report. </p>
 </dd>
<dt><code>report.X.dateformat</code></dt>
<dd> <p> This adds a dateformat to the report X that will be used by the &quot;due date&quot; column. If it is not set then dateformat.report and dateformat will be used in this order. See the <code>DATES</code> section for details on the sequence placeholders. </p>
 </dd>
<dt><code>report.X.annotations</code></dt>
<dd> <p> This adds the possibility to control the output of annotations for a task in a report. Deprecated. Use the <code>description</code> column with a format (e.g., <code>description.count</code>) instead. </p>
 </dd>
<dt>Taskwarrior comes with a number of predefined reports, which are:</dt>
<dd>  </dd>
<dt><code>next</code></dt>
<dd> <p> Lists the most important tasks. </p>
 </dd>
<dt><code>long</code></dt>
<dd> <p> Lists all pending tasks and all data, matching the specified criteria. </p>
 </dd>
<dt><code>list</code></dt>
<dd> <p> Lists all tasks matching the specified criteria. </p>
 </dd>
<dt><code>ls</code></dt>
<dd> <p> Short listing of all tasks matching the specified criteria. </p>
 </dd>
<dt><code>minimal</code></dt>
<dd> <p> Minimal listing of all tasks matching the specified criteria. </p>
 </dd>
<dt><code>newest</code></dt>
<dd> <p> Shows the newest tasks. </p>
 </dd>
<dt><code>oldest</code></dt>
<dd> <p> Shows the oldest tasks. </p>
 </dd>
<dt><code>overdue</code></dt>
<dd> <p> Lists overdue tasks matching the specified criteria. </p>
 </dd>
<dt><code>active</code></dt>
<dd> <p> Lists active tasks matching the specified criteria. </p>
 </dd>
<dt><code>completed</code></dt>
<dd> <p> Lists completed tasks matching the specified criteria. </p>
 </dd>
<dt><code>recurring</code></dt>
<dd> <p> Lists recurring tasks matching the specified criteria. </p>
 </dd>
<dt><code>waiting</code></dt>
<dd> <p> Lists all waiting tasks matching the specified criteria. </p>
 </dd>
<dt><code>all</code></dt>
<dd> <p> Lists all tasks matching the specified criteria. </p>
 </dd>
<dt><code>blocked</code></dt>
<dd> <p> Lists all tasks that have dependencies. </p>
 </dd></dl>
<h3>USER DEFINED ATTRIBUTES</h3>
<p>User defined attributes (UDAs) are an extension mechanism that allows you to define new attributes for Taskwarrior to store and display. One such example is an &#8216;estimate&#8217; attribute that could be used to store time estimates associated with a task. This &#8216;estimate&#8217; attribute is not built in to Taskwarrior, but with a few simple configuration settings you can instruct Taskwarrior to store this item, and provide access to it for custom reports and filters. </p>
<p>This allows you to augment Taskwarrior to accommodate your workflow, or bend the rules and use Taskwarrior to store and synch data that is not necessarily task-related. </p>
<p>One important restriction is that because this is an open system that allows the definition of any new attribute, Taskwarrior cannot understand the meaning of that attribute. So while Taskwarrior will faithfully store, modify, report, sort and filter your UDA, it does not understand anything about it. For example if you define a UDA named &#8216;estimate&#8217;, Taskwarrior will not know that this value is weeks, hours, minutes, money, or some other resource count. </p>
<dl>
<dt><code>uda.&lt;name&gt;.type=string|numeric|date|duration</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Defines a UDA called &#8216;&lt;name&gt;&#8216;, of the specified type. </p>
 </dd></dl>
<dt><code>uda.&lt;name&gt;.label=&lt;column heading&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Provides a default report label for the UDA called &#8216;&lt;name&gt;&#8216;. </p>
 </dd></dl>
<dt><code>uda.&lt;name&gt;.values=A,B,C</code></dt>
<dd>  </dd>
<dl>
<dd> <p> For type &#8216;string&#8217; UDAs only, this provides a comma-separated list of acceptable values. In this example, the &#8216;&lt;name&gt;&#8216; UDA may only contain values &#8216;A&#8217;, &#8216;B&#8217;, or &#8216;C&#8217;, but may also contain no value. </p>
<p>Note that the order of the value is important, and denotes the sort order from highest (&#8216;A&#8217;) to lowest (&#8216;C&#8217;). </p>
<p>Note that a blank value is permitted. </p>
 </dd></dl>
<dt><code>uda.&lt;name&gt;.default=...</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Provides a default value for the UDA called &#8216;&lt;name&gt;&#8216;. </p>
 </dd></dl>
<dt><code>Example &#8216;estimate&#8217; UDA</code></dt>
<dd> <p> This example shows an &#8216;estimate&#8217; UDA that stores specific values for the size of a task. Note the blank value after &#8216;trivial&#8217;. </p>
 </dd>
<dl>
<dd> <p> <code>uda.estimate.type=string</code> <br/>
 <code>uda.estimate.label=Size Estimate</code> <br/>
 <code>uda.estimate.values=huge,large,medium,small,trivial,</code> </p>
 </dd></dl>
<dl>
<dd> <p> Note that the value are sorted </p>
<p> <br/>
&nbsp;<wbr>huge&nbsp;<wbr>&gt;&nbsp;<wbr>large&nbsp;<wbr>&gt;&nbsp;<wbr>medium&nbsp;<wbr>&gt;&nbsp;<wbr>small&nbsp;<wbr>&gt;&nbsp;<wbr>trivial&nbsp;<wbr>&gt;&nbsp;<wbr>&#8216;&#8216; </p>
 </dd></dl>
<h3>CONTEXT</h3>
<p> Context setting is a mechanism which allows the user to set a permanent filter, thus avoiding the need to specify one filter repeatedly. More details on usage can be found in the <a href="/docs/linux/man/1-task/">task</a>(1) man page. </p>
<p>The current context is stored in the .taskrc file, along with definitions for all user provided contexts. </p>
<dl>
<dt><code>context=&lt;name&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Stores the value of the currently active context. </p>
 </dd></dl>
<dt><code>context.&lt;name&gt;=&lt;filter&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Stores the definition of the context with the name &lt;name&gt;. </p>
 </dd></dl>
<h3>SYNC</h3>
<p>These configuration settings are used to connect and sync tasks with the task server. </p>
<dl>
<dt><code>taskd.server=&lt;host&gt;:&lt;port&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Specifies the hostname and port of the Taskserver. Hostname may be an IPv4 or IPv6 address, or domain. Port is an integer. </p>
 </dd></dl>
<dt><code>taskd.credentials=&lt;organization&gt;/&lt;user&gt;/&lt;key&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> User identification for the Taskserver, which includes a private key. </p>
 </dd></dl>
<dt><code>taskd.certificate=&lt;path&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Specifies the path to the client certificate used for identification with the Taskserver. </p>
 </dd></dl>
<dt><code>taskd.key=&lt;path&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Specifies the path to the client key used for encrypted communication with the Taskserver. </p>
 </dd></dl>
<dt><code>taskd.ca=&lt;path&gt;</code></dt>
<dd>  </dd>
<dl>
<dd> <p> Specifies the path to the CA certificate in the event that your Taskserver is using a self-signed certificate. Optional. </p>
 </dd></dl>
<dt><code>taskd.trust=strict|ignore hostname|allow all</code></dt>
<dd>  </dd>
<dl>
<dd> <p> This settings allows you to override the trust level when server certificates are validated. With &quot;allow all&quot;, the server certificate is trusted automatically. With &quot;ignore hostname&quot;, the server certificate is verified but the hostname is ignored. With &quot;strict&quot;, the server certificate is verified. Default is &quot;strict&quot;, which requires full validation. </p>
 </dd></dl>
<dt><code>taskd.ciphers=NORMAL</code></dt>
<dd> <p> Override of the cipher selection. The set of ciphers used by TLS may be controlled by both server and client. There must be some overlap between client and server supported ciphers, or communication cannot occur. Default is &quot;NORMAL&quot;. See GnuTLS documentation for full details. </p>
 </dd></dl>
<h2>CREDITS &amp; COPYRIGHTS</h2>
<p> Copyright (C) 2006 - 2016 P. Beckingham, F. Hernandez. </p>
<p>This man page was originally written by Federico Hernandez. </p>
<p>Taskwarrior is distributed under the MIT license. See <a rel="nofollow" href="http://www.opensource.org/licenses/mit-license.php">http://www.opensource.org/licenses/mit-license.php</a> for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-task/">task</a>(1),</code> <code><a href="/docs/linux/man/5-task-color/">task-color</a>(5),</code> <code><a href="/docs/linux/man/5-task-sync/">task-sync</a>(5)</code> </p>
<p>For more information regarding Taskwarrior, see the following: </p>
<dl>
<dt>The official site at</dt>
<dd> <p> &lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt; </p>
 </dd>
<dt>The official code repository at</dt>
<dd> <p> &lt;<a rel="nofollow" href="https://git.tasktools.org/scm/tm/task.git">https://git.tasktools.org/scm/tm/task.git</a>&gt; </p>
 </dd>
<dt>You can contact the project by emailing</dt>
<dd> <p> &lt;support [at] taskwarrior.org&gt; </p>
 </dd></dl>
<h2>REPORTING BUGS</h2>
<dl>
<dt>Bugs in Taskwarrior may be reported to the issue-tracker at</dt>
<dd> <p> &lt;<a rel="nofollow" href="https://bug.tasktools.org/">https://bug.tasktools.org/</a>&gt; </p>
 </dd></dl>
