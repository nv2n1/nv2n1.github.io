---
title: "task(1)"
name: "task"
section: "1"
letter: "t"
url: "/docs/linux/man/1-task/"
description: "task – A command line todo manager."
---

<h2 class="name">NAME</h2>
<p> task &#8211; A command line todo manager.</p>
<h2>SYNOPSIS</h2>
<p> <code>task &lt;filter&gt; &lt;command&gt; [ &lt;mods&gt; | &lt;args&gt; ]</code><br />
 <code>task &#8211;version</code> </p>
<h2>DESCRIPTION</h2>
<p> Taskwarrior is a command line todo list manager. It maintains a list of tasks that you want to do, allowing you to add/remove, and otherwise manipulate them. Taskwarrior has a rich set of subcommands that allow you to do various things with it. </p>
<p> At the core, Taskwarrior is a list processing program. You add text and additional related parameters and redisplay the information in a nice way. It turns into a todo list program when you add due dates and recurrence. It turns into an organized todo list program when you add priorities, tags (one word descriptors), project groups, etc. </p>
<h2>FILTER</h2>
<p> The &lt;filter&gt; consists of zero or more search criteria that select tasks. For example, to list all pending tasks belonging to the &#8216;Home&#8217; project: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task project:Home list </p>
<p> You can specify multiple filter terms, each of which further restricts the result: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task project:Home&nbsp;<wbr>+weekend garden list </p>
<p> This example applies three filters: the &#8216;Home&#8217; project, the &#8216;weekend&#8217; tag, and the description or annotations must contain the character sequence &#8216;garden&#8217;. In this example, &#8216;garden&#8217; is translated internally to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>description.contains:garden </p>
<p> as a convenient shortcut. The &#8216;contains&#8217; here is an attribute modifier, which is used to exert more control over the filter than simply absence or presence. See the section &#8216;ATTRIBUTE MODIFIERS&#8217; below for a complete list of modifiers. </p>
<p> Note that a filter may have zero terms, which means that all tasks apply to the command. This can be dangerous, and this special case is confirmed, and cannot be overridden. For example, this command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task modify&nbsp;<wbr>+work<br />
&nbsp;<wbr>&nbsp;<wbr>This command has no filter, and will modify all tasks.&nbsp;<wbr>&nbsp;<wbr>Are you sure?&nbsp;<wbr>(yes/no) </p>
<p> will add the &#8216;work&#8217; tag to all tasks, but only after confirmation. </p>
<p> More filter examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>task 28&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>+weekend&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>task project:Home due.before:today&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>task ebeeab00-ccf8-464b-8b58-f7f2d606edfb&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt; </p>
<p> By default filter elements are combined with an implicit &#8216;and&#8217; operator, but &#8216;or&#8217; and &#8216;xor&#8217; may also be used, provided parentheses are included: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&#8216;(&nbsp;<wbr>/[Cc]at|[Dd]og/&nbsp;<wbr>or&nbsp;<wbr>/[0-9]+/&nbsp;<wbr>)&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>&lt;mods&gt; </p>
<p> The parentheses isolate the logical term from any default command filter or implicit report filter which would be combined with an implicit &#8216;and&#8217;. </p>
<p> A filter may target specific tasks using ID or UUID numbers. To specify multiple tasks use one of these forms (space-separated list of ID numbers, UUID numbers or ID ranges): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task 1 2 3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delete<br />
&nbsp;<wbr>&nbsp;<wbr>task 1-3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>info<br />
&nbsp;<wbr>&nbsp;<wbr>task 1 2-5 19&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>modify pri:H<br />
&nbsp;<wbr>&nbsp;<wbr>task 4-7 ebeeab00-ccf8-464b-8b58-f7f2d606edfb info </p>
<h2>MODIFICATIONS</h2>
<p> The &lt;mods&gt; consist of zero or more changes to apply to the selected tasks, such as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>project:Home<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>+weekend&nbsp;<wbr>+garden due:tomorrow<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>Description/annotation text<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>/from/to/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;- replace first match<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>&lt;command&gt;&nbsp;<wbr>/from/to/g&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;- replace all matches </p>
<h2>SUBCOMMANDS</h2>
<p> Taskwarrior supports different kinds of commands. There are read commands, write commands, miscellaneous commands and script helper commands. Read commands do not allow modification of tasks. Write commands can alter almost any aspect of a task. Script helper commands are provided to help you write add-on scripts, for example, shell completion (only minimal output is generated, as with verbose=nothing). </p>
<h2>READ SUBCOMMANDS</h2>
<p> Reports are read subcommands. There are several reports currently predefined in Taskwarrior. The output and sort behavior of these reports can be configured in the configuration file. See also the man page <a href="/docs/linux/man/5-taskrc/">taskrc</a>(5). There are also other read subcommands that are not reports. </p>
<dl>
<dt><code>task &#8211;version</code></p>
<dd> This is the only conventional command line argument that Taskwarrior supports, and is intended for add-on scripts to verify the version number of an installed Taskwarrior without invoking the mechanisms that create default files. </p>
<dt><code>task &lt;filter&gt;</code></p>
<dd> With no command specified, the default command is run, and the filter applied. </p>
<dt><code>task &lt;filter&gt; active</code></p>
<dd> Shows all tasks matching the filter that are started but not completed. </p>
<dt><code>task &lt;filter&gt; all</code></p>
<dd> Shows all tasks matching the filter, including parents of recurring tasks. </p>
<dt><code>task &lt;filter&gt; blocked</code></p>
<dd> Shows all tasks matching the filter, that are currently blocked by other tasks. </p>
<dt><code>task &lt;filter&gt; blocking</code></p>
<dd> Shows all tasks matching the filter, that block other tasks. </p>
<dt><code>task &lt;filter&gt; burndown.daily</code></p>
<dd> Shows a graphical burndown chart, by day. </p>
<dt><code>task &lt;filter&gt; burndown.weekly</code></p>
<dd> Shows a graphical burndown chart, by week. Note that &#8216;burndown&#8217; is an alias to the &#8216;burndown.weekly&#8217; report. </p>
<dt><code>task &lt;filter&gt; burndown.monthly</code></p>
<dd> Shows a graphical burndown chart, by month. </p>
<dt><code>task calendar [due|&lt;month&gt; &lt;year&gt;|&lt;year&gt;] [y]</code></p>
<dd> Shows a monthly calendar with due tasks marked. Shows one horizontal line of months. If the &#8216;y&#8217; argument is provided, will show at least one complete year. If a year is provided, such as &#8216;2015&#8217;, then that full year is shown. If both a month and a year are specified (&#8216;6 2015&#8217;) then the months displayed begin at the specified month and year. If the &#8216;due&#8217; argument is provided, will show the starting month of the earliest due task. </p>
<dt><code>task colors [sample | legend]</code></p>
<dd> Displays all possible colors, a named sample, or a legend containing all currently defined colors. </p>
<dt><code>task columns [substring]</code></p>
<dd> Displays all supported columns and formatting styles. Useful when creating custom reports. If a substring is provided, only matching column names are shown. </p>
<dt><code>task commands</code></p>
<dd> Shows all the supported commands, with some details of each. </p>
<dt><code>task &lt;filter&gt; completed</code></p>
<dd> Shows all tasks matching the filter that are completed. </p>
<dt><code>task &lt;filter&gt; count</code></p>
<dd> Displays only a count of tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; export</code></p>
<dd> Exports all tasks in the JSON format. Redirect the output to a file, if you wish to save it, or pipe it to another command or script to convert it to another format. The standard task release comes with a few example scripts, such as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>export-csv.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-sql.py<br />
&nbsp;<wbr>&nbsp;<wbr>export-xml.py<br />
&nbsp;<wbr>&nbsp;<wbr>export-yaml.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-html.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-tsv.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-xml.rb<br />
&nbsp;<wbr>&nbsp;<wbr>export-ical.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-xml.pl<br />
&nbsp;<wbr>&nbsp;<wbr>export-yad.pl </p>
<dt><code>task &lt;filter&gt; ghistory.annual</code></p>
<dd> Shows a graphical report of task status by year. </p>
<dt><code>task &lt;filter&gt; ghistory.monthly</code></p>
<dd> Shows a graphical report of task status by month. Note that &#8216;ghistory&#8217; is an alias to &#8216;ghistory.monthly&#8217;. </p>
<dt><code>task help</code></p>
<dd> Shows the long usage text. </p>
<dt><code>task &lt;filter&gt; history.annual</code></p>
<dd> Shows a report of task history by year. </p>
<dt><code>task &lt;filter&gt; history.monthly</code></p>
<dd> Shows a report of task history by month. Note that &#8216;history&#8217; is an alias to &#8216;history.monthly&#8217;. </p>
<dt><code>task &lt;filter&gt; ids</code></p>
<dd> Applies the filter then extracts only the task IDs and presents them as a space-separated list. This is useful as input to a task command, to achieve this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>$(task project:Home ids)&nbsp;<wbr>modify priority:H </p>
<p> This example first gets the IDs for the project:Home filter, then sets the priority to H for each of those tasks. This can also be achieved directly: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task project:Home modify priority:H </p>
<p> This command is mainly of use to external scripts. </p>
<dt><code>task &lt;filter&gt; uuids</code></p>
<dd> Applies the filter on all tasks (even deleted and completed tasks) then extracts only the task UUIDs and presents them as a comma-separated list. This is useful as input to a task command, to achieve this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>$(task project:Home status:completed uuids)&nbsp;<wbr>modify status:pending </p>
<p> This example first gets the UUIDs for the project:Home and status:completed filters, then makes each of those tasks pending again. </p>
<p> This command is mainly of use to external scripts. </p>
<dt><code>task udas</code></p>
<dd> Shows a list of UDAs that are defined, including their name, type, label and allowed values. Also shows UDA usage and any orphan UDAs. </p>
<dt><code>task &lt;filter&gt; information</code></p>
<dd> Shows all data and metadata for the specified tasks. This is the only means of displaying all aspects of a given task, including the change history. </p>
<dt><code>task &lt;filter&gt; list</code></p>
<dd> Provides a standard listing of tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; long</code></p>
<dd> Provides the most detailed listing of tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; ls</code></p>
<dd> Provides a short listing of tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; minimal</code></p>
<dd> Provides a minimal listing of tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; newest</code></p>
<dd> Shows the newest tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; next</code></p>
<dd> Shows a page of the most urgent tasks, sorted by urgency, which is a calculated value. </p>
<dt><code>task &lt;filter&gt; ready</code></p>
<dd> Shows a page of the most urgent ready tasks, sorted by urgency. A ready task is one that is either unscheduled, or has a scheduled date that is past and has no wait date. </p>
<dt><code>task &lt;filter&gt; oldest</code></p>
<dd> Shows the oldest tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; overdue</code></p>
<dd> Shows all incomplete tasks matching the filter that are beyond their due date. </p>
<dt><code>task &lt;filter&gt; projects</code></p>
<dd> Lists all project names that are currently used by pending tasks, and the number of tasks for each. </p>
<dt><code>task &lt;filter&gt; recurring</code></p>
<dd> Shows all recurring tasks matching the filter. </p>
<dt><code>task &lt;filter&gt; unblocked</code></p>
<dd> Shows all tasks that are not currently blocked by other tasks, matching the filter. </p>
<dt><code>task &lt;filter&gt; waiting</code></p>
<dd> Shows all waiting tasks matching the filter. </p>
</dl>
<h2>WRITE SUBCOMMANDS</h2>
<dl>
<dt><code>task add &lt;mods&gt;</code></p>
<dd> Adds a new pending task to the task list. </p>
<dt><code>task &lt;filter&gt; annotate &lt;mods&gt;</code></p>
<dd> Adds an annotation to an existing task. </p>
<dt><code>task &lt;filter&gt; append &lt;mods&gt;</code></p>
<dd> Appends description text to an existing task. </p>
<dt><code>task &lt;filter&gt; delete &lt;mods&gt;</code></p>
<dd> Deletes the specified task from task list. </p>
<dt><code>task &lt;filter&gt; denotate &lt;mods&gt;</code></p>
<dd> Deletes an annotation for the specified task. If the provided description matches an annotation exactly, the corresponding annotation is deleted. If the provided description matches annotations partly, the first partly matched annotation is deleted. </p>
<dt><code>task &lt;filter&gt; done &lt;mods&gt;</code></p>
<dd> Marks the specified task as done. </p>
<dt><code>task &lt;filter&gt; duplicate &lt;mods&gt;</code></p>
<dd> Duplicates the specified task and allows modifications. </p>
<dt><code>task &lt;filter&gt; edit</code></p>
<dd> Launches a text editor to let you modify all aspects of a task directly. In general, this is not the recommended method of modifying tasks, but is provided for exceptional circumstances. Use carefully. </p>
<dt><code>task import [&lt;file&gt; &#8230;]</code></p>
<dd> Imports tasks in the JSON format. Can be used to add new tasks, or update existing ones. Tasks are identified by their UUID. </p>
<p> If no file or &quot;-&quot; is specified, import tasks from STDIN. </p>
<p> Setting rc.recurrence.confirmation to an appropriate level is recommended if import is to be used in automated workflows. See <a href="/docs/linux/man/5-taskrc/">taskrc</a>(5). </p>
<p> For importing other file formats, the standard task release comes with a few example scripts, such as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>import-todo.sh.pl<br />
&nbsp;<wbr>&nbsp;<wbr>import-yaml.pl </p>
<dt><code>task log &lt;mods&gt;</code></p>
<dd> Adds a new task that is already completed, to the task list. </p>
<dt><code>task &lt;filter&gt; modify &lt;mods&gt;</code></p>
<dd> Modifies the existing task with provided information. </p>
<dt><code>task &lt;filter&gt; prepend &lt;mods&gt;</code></p>
<dd> Prepends description text to an existing task. </p>
<dt><code>task &lt;filter&gt; start &lt;mods&gt;</code></p>
<dd> Marks the specified tasks as started. </p>
<dt><code>task &lt;filter&gt; stop &lt;mods&gt;</code></p>
<dd> Removes the <i>start</i> time from the specified task. </p>
</dl>
<h2>MISCELLANEOUS SUBCOMMANDS</h2>
<p> Miscellaneous subcommands either accept no command line arguments, or accept non-standard arguments. </p>
<dl>
<dt><code>task calc &lt;expression&gt;</code></p>
<dd> Evaluates an algebraic expression. Can be used to test how Taskwarrior parses and evaluates the expression given on the command line. </p>
<p> Examples: </p>
<p>&nbsp;<wbr>task calc 1&nbsp;<wbr>+&nbsp;<wbr>1<br />
&nbsp;<wbr>2 </p>
<p>&nbsp;<wbr>task calc now&nbsp;<wbr>+&nbsp;<wbr>8d<br />
&nbsp;<wbr>2015-03-26T18:06:57 </p>
<p>&nbsp;<wbr>task calc eom<br />
&nbsp;<wbr>2015-03-31T23:59:59 </p>
<dt><code>task config [name [value | &#8221;]]</code></p>
<dd> Add, modify and remove settings directly in the Taskwarrior configuration. This command either modifies the &#8216;name&#8217; setting with a new value of &#8216;value&#8217;, or adds a new entry that is equivalent to &#8216;name=value&#8217;: </p>
<p>&nbsp;<wbr>task config name value </p>
<p> This command sets a blank value. This has the effect of suppressing any default value: </p>
<p>&nbsp;<wbr>task config name&nbsp;<wbr>&#8221; </p>
<p> Finally, this command removes any &#8216;name=&#8230;&#8217; entry from the .taskrc file: </p>
<p>&nbsp;<wbr>task config name </p>
<dt><code>task context &lt;name&gt;</code></p>
<dd> Sets the currently active context. See the CONTEXT section. </p>
<p> Example: </p>
<p>&nbsp;<wbr>task context work </p>
<dt><code>task context delete &lt;name&gt;</code></p>
<dd> Deletes the context with the name &lt;name&gt;. If the context being deleted is currently set as active, it will be unset. </p>
<p> Example: </p>
<p>&nbsp;<wbr>task context delete work </p>
<dt><code>task context define &lt;name&gt; &lt;filter&gt;</code></p>
<dd> Defines a new context with name &lt;name&gt; and definition &lt;filter&gt;. This command does not affect the currently set context, just adds a new context definition. </p>
<p> Examples: </p>
<p>&nbsp;<wbr>task context define work project:Work<br />
&nbsp;<wbr>task context define home project:Home or&nbsp;<wbr>+home<br />
&nbsp;<wbr>task context define superurgent due:today and&nbsp;<wbr>+urgent </p>
<dt><code>task context list</code></p>
<dd> Outputs a list of available contexts along with their definitions. </p>
<dt><code>task context none</code></p>
<dd> Clears the currently active context, if any was set. </p>
<dt><code>task context show</code></p>
<dd> Shows the currently active context, along with its definition. </p>
<dt><code>task diagnostics</code></p>
<dd> Shows diagnostic information, of the kind needed when reporting a problem. When you report a bug, it is likely that the platform, version, and environment are important. Running this command generates a summary of similar information that should accompany a bug report. </p>
<p> It includes compiler, library and software information. It does not include any personal information, other than the location and size of your task data files. </p>
<p> This command also performs a diagnostic scan of your data files looking for common problems, such as duplicate UUIDs. </p>
<dt><code>task execute &lt;external command&gt;</code></p>
<dd> Executes the specified command. Not useful by itself, but when used in conjunction with aliases and extensions can provide seamless integration. </p>
<dt><code>task logo</code></p>
<dd> Displays the Taskwarrior logo. </p>
<dt><code>task reports</code></p>
<dd> Lists all supported reports. This includes the built-in reports, and any custom reports you have defined. </p>
<dt><code>task show [all | substring]</code></p>
<dd> Shows all the current settings. If a substring is specified just the settings containing that substring will be displayed. </p>
<dt><code>task &lt;filter&gt; stats</code></p>
<dd> Shows statistics of the tasks defined by the filter. </p>
<dt><code>task &lt;filter&gt; summary</code></p>
<dd> Shows a report of aggregated task status by project. </p>
<dt><code>task &lt;filter&gt; tags</code></p>
<dd> Show a list of all tags used. Any special tags used are highlighted. Note that virtual tags are not listed &#8211; they don&#8217;t really exist, and are just a convenient notation for other task metadata. It is an error to attempt to add or remove a virtual tag. </p>
<dt><code>task timesheet [weeks]</code></p>
<dd> Shows a weekly report of tasks completed and started. </p>
<dt><code>task undo</code></p>
<dd> Reverts the most recent action. Obeys the confirmation setting. </p>
<dt><code>task version</code></p>
<dd> Shows the Taskwarrior version number. </p>
</dl>
<h2>HELPER SUBCOMMANDS</h2>
<dl>
<dt><code>task _aliases</code></p>
<dd> Generates a list of all aliases, for autocompletion purposes. </p>
<dt><code>task _columns</code></p>
<dd> Displays only a list of supported columns. </p>
<dt><code>task _commands</code></p>
<dd> Generates a list of all commands, for autocompletion purposes. </p>
<dt><code>task _config</code></p>
<dd> Lists all supported configuration variables, for completion purposes. </p>
<dt><code>task _context</code></p>
<dd> Lists all available context variables, for completion purposes. </p>
<dt><code>task &lt;filter&gt; _ids</code></p>
<dd> Shows only the IDs of matching tasks, in the form of a list. Deprecated in favor of _unique. </p>
<dt><code>task _show</code></p>
<dd> Shows the combined defaults and overrides of the configuration settings, for use by third-party applications. </p>
<dt><code>task &lt;filter&gt; _unique &lt;attribute&gt;</code></p>
<dd> Reports a unique set of attribute values. For example, to see all the active projects: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>+PENDING&nbsp;<wbr>_unique projects </p>
<dt><code>task &lt;filter&gt; _uuids</code></p>
<dd> Shows only the UUIDs of matching tasks among all tasks (even deleted and completed tasks), in the form of a list. Deprecated in favor of _unique. </p>
<dt><code>task _udas</code></p>
<dd> Shows only defined UDA names, in the form of a list. </p>
<dt><code>task &lt;filter&gt; _projects</code></p>
<dd> Shows only a list of all project names used. Deprecated in favor of _unique. </p>
<dt><code>task &lt;filter&gt; _tags</code></p>
<dd> Shows only a list of all tags used, for autocompletion purposes. Deprecated in favor of _unique. </p>
<dt><code>task &lt;filter&gt; _urgency</code></p>
<dd> Displays the urgency measure of a task. </p>
<dt><code>task _version</code></p>
<dd> Shows only the Taskwarrior version number. </p>
<dt><code>task _zshcommands</code></p>
<dd> Generates a list of all commands, for zsh autocompletion purposes. </p>
<dt><code>task &lt;filter&gt; _zshids</code></p>
<dd> Shows the IDs and descriptions of matching tasks. </p>
<dt><code>task &lt;filter&gt; _zshuuids</code></p>
<dd> Shows the UUIDs and descriptions of matching tasks. </p>
<dt><code>task _get &lt;DOM&gt; [&lt;DOM&gt; &#8230;]</code></p>
<dd> Accesses and displays the DOM reference(s). Used to extract individual values from tasks, or the system. Supported DOM references are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>rc.&lt;name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>context.program<br />
&nbsp;<wbr>&nbsp;<wbr>context.args<br />
&nbsp;<wbr>&nbsp;<wbr>context.width<br />
&nbsp;<wbr>&nbsp;<wbr>context.height<br />
&nbsp;<wbr>&nbsp;<wbr>system.version<br />
&nbsp;<wbr>&nbsp;<wbr>system.os<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;id&gt;.&lt;attribute&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;uuid&gt;.&lt;attribute&gt; </p>
<p> Note that the &#8216;rc.&lt;name&gt;&#8217; reference may need to be escaped using &#8216;&#8211;&#8216; to prevent the reference from being interpreted as an override. </p>
<p> Note that if the DOM reference is not valid, or the reference evaluates to a missing value, the command exits with 1. </p>
<p> Additionally, some components of the attributes of particular types may be extracted by DOM references. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>task&nbsp;<wbr>_get 2.due.year<br />
&nbsp;<wbr>&nbsp;<wbr>2015 </p>
<p> For a full list of supported attribute-specific DOM references, consult the online documentation at: &lt;<a rel="nofollow" href="http://taskwarrior.org/docs/dom.html">http://taskwarrior.org/docs/dom.html</a>&gt; </p>
</dl>
<h2>ATTRIBUTES AND METADATA</h2>
<dl>
<dt><code>ID</code></p>
<dd> Tasks can be specified uniquely by IDs, which are simply the indexes of the tasks in the data file. The ID of a task may therefore change, but only when a command is run that displays IDs. When modifying tasks, it is safe to rely on the last displayed ID. Always run a report to check you have the right ID for a task. IDs can be given to task as a sequence, for example,<br />
 <code>task 1,4-10,19 delete</code> </p>
<dt><code>+tag|-tag</code></p>
<dd> Tags are arbitrary words associated with a task. Use + to add a tag and &#8211; to remove a tag from a task. A task can have any quantity of tags. </p>
<p> Certain tags (called &#8216;special tags&#8217;), can be used to affect the way tasks are treated. For example, if a task has the special tag &#8216;nocolor&#8217;, then it is exempt from all color rules. The supported special tags are: </p>
<p>&nbsp;<wbr>+nocolor&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Disable color rules processing for this task<br />
&nbsp;<wbr>+nonag&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Completion of this task suppresses all nag messages<br />
&nbsp;<wbr>+nocal&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>This task will not appear on the calendar<br />
&nbsp;<wbr>+next&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Elevates task so it appears on&nbsp;<wbr>&#8216;next&#8217;&nbsp;<wbr>report </p>
<p> There are also virtual tags, which represent task metadata in tag form. These tags do not exist, but can be used to filter tasks. The supported virtual tags are: </p>
<p>&nbsp;<wbr>ACTIVE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is started<br />
&nbsp;<wbr>ANNOTATED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has annotations<br />
&nbsp;<wbr>BLOCKED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is blocked<br />
&nbsp;<wbr>BLOCKING&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is blocking<br />
&nbsp;<wbr>CHILD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has a parent<br />
&nbsp;<wbr>COMPLETED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has completed status<br />
&nbsp;<wbr>DELETED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has deleted status<br />
&nbsp;<wbr>DUE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due<br />
&nbsp;<wbr>DUETODAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due today<br />
&nbsp;<wbr>LATEST&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is the newest added task<br />
&nbsp;<wbr>MONTH&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due this month<br />
&nbsp;<wbr>ORPHAN&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has any orphaned UDA values<br />
&nbsp;<wbr>OVERDUE&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is overdue<br />
&nbsp;<wbr>PARENT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is a parent<br />
&nbsp;<wbr>PENDING&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has pending status<br />
&nbsp;<wbr>PRIORITY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has a priority<br />
&nbsp;<wbr>PROJECT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has a project<br />
&nbsp;<wbr>READY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is actionable<br />
&nbsp;<wbr>SCHEDULED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is scheduled<br />
&nbsp;<wbr>TAGGED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has tags<br />
&nbsp;<wbr>TODAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due today<br />
&nbsp;<wbr>TOMORROW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due sometime tomorrow<br />
&nbsp;<wbr>UDA&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task has any UDA values<br />
&nbsp;<wbr>UNBLOCKED&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is not blocked<br />
&nbsp;<wbr>UNTIL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task expires<br />
&nbsp;<wbr>WAITING&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is waiting<br />
&nbsp;<wbr>WEEK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due this week<br />
&nbsp;<wbr>YEAR&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task is due this year<br />
&nbsp;<wbr>YESTERDAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Matches if the task was due sometime yesterday </p>
<p> You can use +BLOCKED to filter blocked tasks, or -BLOCKED for unblocked tasks. Similarly, -BLOCKED is equivalent to +UNBLOCKED. It is an error to attempt to add or remove a virtual tag. </p>
<dt><code>project:&lt;project-name&gt;</code></p>
<dd> Specifies the project to which a task is related to. </p>
<dt><code>priority:H|M|L or priority:</code></p>
<dd> Specifies High, Medium, Low and no priority for a task. </p>
<dt><code>due:&lt;due-date&gt;</code></p>
<dd> Specifies the due-date of a task. </p>
<dt><code>recur:&lt;frequency&gt;</code></p>
<dd> Specifies the frequency of a recurrence of a task. </p>
<dt><code>scheduled:&lt;ready-date&gt;</code></p>
<dd> Specifies the date after which a task can be accomplished. </p>
<dt><code>until:&lt;expiration date of task&gt;</code></p>
<dd> Specifies the expiration date of a task, after which it will be deleted. </p>
<dt><code>limit:&lt;number-of-rows&gt;</code></p>
<dd> Specifies the desired number of tasks a report should show, if a positive integer is given. The value &#8216;page&#8217; may also be used, and will limit the report output to as many lines of text as will fit on screen. This defaults to 25 lines. </p>
<dt><code>wait:&lt;wait-date&gt;</code></p>
<dd> When a task is given a wait date, it is hidden from most reports by changing its status to &#8216;waiting&#8217;. When that date is passed, the status is changed back to &#8216;pending&#8217;, and the task becomes visible. </p>
<dt><code>depends:&lt;id1,id2 &#8230;&gt;</code></p>
<dd> Declares this task to be dependent on id1 and id2. This means that the tasks id1 and id2 should be completed before this task. Consequently, this task will then show up on the &#8216;blocked&#8217; report. It accepts a comma-separated list of ID numbers, UUID numbers and ID ranges. When prefixing any element of this list by &#8216;-&#8216;, the specified tasks are removed from the dependency list. </p>
<dt><code>entry:&lt;entry-date&gt;</code></p>
<dd> For report purposes, specifies the date that a task was created. </p>
</dl>
<h2>ATTRIBUTE MODIFIERS</h2>
<p> Attribute modifiers improve filters. Supported modifiers are: </p>
<dl>
<dt>
<dd> <code>before (synonyms under, below)</code><br />
 <code>after (synonyms over, above)</code><br />
 <code>none</code><br />
 <code>any</code><br />
 <code>is (synonym equals)</code><br />
 <code>isnt (synonym not)</code><br />
 <code>has (synonym contains)</code><br />
 <code>hasnt</code><br />
 <code>startswith (synonym left)</code><br />
 <code>endswith (synonym right)</code><br />
 <code>word</code><br />
 <code>noword</code></dl>
<p> For example: </p>
<dl>
<dt>
<dd> task due.before:eom priority.not:L list</dl>
<p> The <i>before</i> modifier is used to compare values, preserving semantics, so project.before:B list all projects that begin with &#8216;A&#8217;. Priority &#8216;L&#8217; is before &#8216;M&#8217;, and due:2011-01-01 is before due:2011-01-02. The synonyms &#8216;under&#8217; and &#8216;below&#8217; are included to allow filters that read more naturally. </p>
<p> The <i>after</i> modifier is the inverse of the <i>before</i> modifier. </p>
<p> The <i>none</i> modifier requires that the attribute does not have a value. For example: </p>
<p>&nbsp;<wbr>task priority:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list<br />
&nbsp;<wbr>task priority.none: list </p>
<p> are equivalent, and list tasks that do not have a priority. </p>
<p> The <i>any</i> modifier requires that the attribute has a value, but any value will suffice. </p>
<p> The <i>is</i> modifier requires an exact match with the value. </p>
<p> The <i>isnt</i> modifier is the inverse of the <i>is</i> modifier. </p>
<p> The <i>has</i> modifier is used to search for a substring, such as: </p>
<p>&nbsp;<wbr>task description.has:foo list<br />
&nbsp;<wbr>task foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list </p>
<p> These are equivalent and will return any task that has &#8216;foo&#8217; in the description or annotations. </p>
<p> The <i>hasnt</i> modifier is the inverse of the <i>has</i> modifier. </p>
<p> The <i>startswith</i> modifier matches against the left, or beginning of an attribute, such that: </p>
<p>&nbsp;<wbr>task project.startswith:H list<br />
&nbsp;<wbr>task project:H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list </p>
<p> are equivalent and will match any project starting with &#8216;H&#8217;. Matching all projects not starting with &#8216;H&#8217; is done with: </p>
<p>&nbsp;<wbr>task project.not:H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list </p>
<p> The <i>endswith</i> modifier matches against the right, or end of an attribute. </p>
<p> The <i>word</i> modifier requires that the attribute contain the whole word specified, such that this: </p>
<p>&nbsp;<wbr>task description.word:bar list </p>
<p> Will match the description &#8216;foo bar baz&#8217; but does not match &#8216;dog food&#8217;. </p>
<p> The <i>noword</i> modifier is the inverse of the <i>word</i> modifier. </p>
<h2>EXPRESSIONS AND OPERATORS</h2>
<p> You can use the following operators in filter expressions: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>and&nbsp;<wbr>&nbsp;<wbr>or&nbsp;<wbr>&nbsp;<wbr>xor&nbsp;<wbr>&nbsp;<wbr>!&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Logical operators<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;&nbsp;<wbr>&nbsp;<wbr>&lt;=&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>&nbsp;<wbr>==&nbsp;<wbr>&nbsp;<wbr>!=&nbsp;<wbr>&nbsp;<wbr>!==&nbsp;<wbr>&nbsp;<wbr>&gt;=&nbsp;<wbr>&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>Relational operators<br />
&nbsp;<wbr>&nbsp;<wbr>(&nbsp;<wbr>&nbsp;<wbr>)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Precedence </p>
<p> For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task due.before:eom priority.not:L list<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&#8216;(&nbsp;<wbr>due&nbsp;<wbr>&lt;&nbsp;<wbr>eom or priority&nbsp;<wbr>!=&nbsp;<wbr>L&nbsp;<wbr>)&#8217;&nbsp;<wbr>list<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&#8216;!&nbsp;<wbr>(&nbsp;<wbr>project:Home or project:Garden&nbsp;<wbr>)&#8217;&nbsp;<wbr>list </p>
<p> The <i>=</i> operator tests for approximate equality. Dates compare equal if they are on the same day (hour and minutes are ignored). Strings compare equal if the left operand starts with the right operand. The <i>==</i> operator tests for exact equality. The <i>!=</i> and <i>!==</i> operators are the negation of <i>=</i> and <i>==</i> respectively. The negation operator is <i>!</i>. </p>
<p> Note that the parentheses are required when using a logical operator other than the &#8216;and&#8217; operator. The reason is that some reports contain filters that must be combined with the command line. Consider this example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task project:Home or project:Garden list </p>
<p> While this looks correct, it is not. The &#8216;list&#8217; report contains a filter of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task show report.list.filter </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Config Variable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Value<br />
&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;&nbsp;<wbr>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>report.list.filter status:pending </p>
<p> Which means the example is really: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task status:pending project:Home or project:Garden list </p>
<p> The implied &#8216;and&#8217; operator makes it: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task status:pending and project:Home or project:Garden list </p>
<p> This is a precedence error &#8211; the &#8216;and&#8217; and &#8216;or&#8217; need to be grouped using parentheses, like this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task status:pending and&nbsp;<wbr>(&nbsp;<wbr>project:Home or project:Garden&nbsp;<wbr>)&nbsp;<wbr>list </p>
<p> The original example therefore must be entered as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&#8216;(&nbsp;<wbr>project:Home or project:Garden&nbsp;<wbr>)&#8217;&nbsp;<wbr>list </p>
<p> This includes quotes to escape the parentheses, so that the shell doesn&#8217;t interpret them and hide them from Taskwarrior. </p>
<p> There is redundancy between operators, attribute modifiers and other syntactic sugar. For example, the following are all equivalent: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>task foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>/foo/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list<br />
&nbsp;<wbr>&nbsp;<wbr>task description.contains:foo list<br />
&nbsp;<wbr>&nbsp;<wbr>task description.has:foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list<br />
&nbsp;<wbr>&nbsp;<wbr>task&nbsp;<wbr>&#8216;description&nbsp;<wbr>~&nbsp;<wbr>foo&#8217;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list </p>
<h2>SPECIFYING DATES AND FREQUENCIES</h2>
<h3>DATES</h3>
<p> Taskwarrior reads dates from the command line and displays dates in the reports. The expected and desired date format is determined by the configuration variable <i>dateformat</i> </p>
<dl>
<dt>
<dd>
<dl>
<dt>Exact specification</p>
<dd> task &#8230; due:7/14/2008 </p>
<dt>ISO-8601</p>
<dd> task &#8230; due:2013-03-14T22:30:00Z </p>
<dt>Relative wording</p>
<dd> task &#8230; due:now<br />
 task &#8230; due:today<br />
 task &#8230; due:yesterday<br />
 task &#8230; due:tomorrow </p>
<dt>Day number with ordinal</p>
<dd> task &#8230; due:23rd<br />
 task &#8230; due:3wks<br />
 task &#8230; due:1day<br />
 task &#8230; due:9hrs </p>
<dt>Start of next (work) week (Monday), calendar week (Sunday or Monday), month, quarter and year</p>
<dd>
 task &#8230; due:sow<br />
 task &#8230; due:soww<br />
 task &#8230; due:socw<br />
 task &#8230; due:som<br />
 task &#8230; due:soq<br />
 task &#8230; due:soy </p>
<dt>End of current (work) week (Friday), calendar week (Saturday or Sunday), month, quarter and year</p>
<dd>
 task &#8230; due:eow<br />
 task &#8230; due:eoww<br />
 task &#8230; due:eocw<br />
 task &#8230; due:eom<br />
 task &#8230; due:eoq<br />
 task &#8230; due:eoy </p>
<dt>At some point or later</p>
<dd>
 task &#8230; wait:later<br />
 task &#8230; wait:someday </p>
<p> This sets the wait date to 1/18/2038. </p>
<dt>Next occurring weekday</p>
<dd> task &#8230; due:fri </p>
<dt>Predictable holidays</p>
<dd> task &#8230; due:goodfriday<br />
 task &#8230; due:easter<br />
 task &#8230; due:eastermonday<br />
 task &#8230; due:ascension<br />
 task &#8230; due:pentecost<br />
 task &#8230; due:midsommar<br />
 task &#8230; due:midsommarafton</dl>
</dl>
<h3>FREQUENCIES</h3>
<p> Recurrence periods. Taskwarrior supports several ways of specifying the <i>frequency</i> of recurring tasks. </p>
<dl>
<dt>
<dd>
<dl>
<dt>daily, day, 1da, 2da, &#8230;</p>
<dd> Every day or a number of days. </p>
<dt>weekdays</p>
<dd> Mondays, Tuesdays, Wednesdays, Thursdays, Fridays and skipping weekend days. </p>
<dt>weekly, 1wk, 2wks, &#8230;</p>
<dd> Every week or a number of weeks. </p>
<dt>biweekly, fortnight</p>
<dd> Every two weeks. </p>
<dt>monthly, month, 1mo, 2mo, &#8230;</p>
<dd> Every month. </p>
<dt>quarterly, 1qtr, 2qtrs, &#8230;</p>
<dd> Every three months, a quarter, or a number of quarters. </p>
<dt>semiannual</p>
<dd> Every six months. </p>
<dt>annual, yearly, 1yr, 2yrs, &#8230;</p>
<dd> Every year or a number of years. </p>
<dt>biannual, biyearly, 2yr</p>
<dd> Every two years.</dl>
</dl>
<h2>CONTEXT</h2>
<p> Context is a user-defined filter, which is automatically applied to all commands that filter the task list. In particular, any report command will have its result affected by the current active context. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task list<br />
&nbsp;<wbr>ID Age Project&nbsp;<wbr>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Urg<br />
&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>2d&nbsp;<wbr>&nbsp;<wbr>Sport&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run 5 miles&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.42<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>1d&nbsp;<wbr>&nbsp;<wbr>Home&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Clean the dishes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.14 </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context home<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;home&#8217;&nbsp;<wbr>set. Use&nbsp;<wbr>&#8216;task context none&#8217;&nbsp;<wbr>to remove. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task list<br />
&nbsp;<wbr>ID Age Project&nbsp;<wbr>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Urg<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>1d&nbsp;<wbr>&nbsp;<wbr>Home&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Clean the dishes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.14<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;home&#8217;&nbsp;<wbr>set. Use&nbsp;<wbr>&#8216;task context none&#8217;&nbsp;<wbr>to remove. </p>
<p> As seen in the example above, context is applied by specifying its name to the &quot;context&quot; command. To change the currently applied context, just pass the new context&#8217;s name to the &#8216;context&#8217; command. </p>
<p> To unset any context, use the &#8216;none&#8217; subcommand. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context none<br />
&nbsp;<wbr>Context unset. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task list<br />
&nbsp;<wbr>ID Age Project&nbsp;<wbr>&nbsp;<wbr>Description&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Urg<br />
&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>2d&nbsp;<wbr>&nbsp;<wbr>Sport&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Run 5 miles&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.42<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>1d&nbsp;<wbr>&nbsp;<wbr>Home&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Clean the dishes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1.14 </p>
<p> Context can be defined using the &#8216;define&#8217; subcommand, specifying both the name of the new context, and it&#8217;s assigned filter. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context define home project:Home<br />
&nbsp;<wbr>Are you sure you want to add&nbsp;<wbr>&#8216;context.home&#8217;&nbsp;<wbr>with a value of&nbsp;<wbr>&#8216;project:Home&#8217;?&nbsp;<wbr>(yes/no)&nbsp;<wbr>yes<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;home&#8217;&nbsp;<wbr>successfully defined. </p>
<p> To remove the definition, use the &#8216;delete&#8217; subcommand. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context delete home<br />
&nbsp;<wbr>Are you sure you want to remove&nbsp;<wbr>&#8216;context.home&#8217;?&nbsp;<wbr>(yes/no)&nbsp;<wbr>yes<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;home&#8217;&nbsp;<wbr>successfully undefined. </p>
<p> To check what is the currently active context, use the &#8216;show&#8217; subcommand. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context show<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;home&#8217;&nbsp;<wbr>with filter&nbsp;<wbr>&#8216;project:Home&#8217;&nbsp;<wbr>is currently applied. </p>
<p> Contexts can store arbitrarily complex filters. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task context define family project:Family or&nbsp;<wbr>+paul or&nbsp;<wbr>+nancy<br />
&nbsp;<wbr>Are you sure you want to add&nbsp;<wbr>&#8216;context.home&#8217;&nbsp;<wbr>with a value of&nbsp;<wbr>&#8216;project:Family or&nbsp;<wbr>+paul or&nbsp;<wbr>+nancy&#8217;?&nbsp;<wbr>(yes/no)&nbsp;<wbr>yes<br />
&nbsp;<wbr>Context&nbsp;<wbr>&#8216;family&#8217;&nbsp;<wbr>successfully defined. </p>
<p> Contexts are permanent, and the currently set context name is stored in the &quot;context&quot; configuration variable. The context definition is stored in the &quot;context.&lt;name&gt;&quot; configuration variable. </p>
<h2>COMMAND ABBREVIATION</h2>
<p> All Taskwarrior commands may be abbreviated as long as a unique prefix is used, for example: </p>
<dl>
<dt>
<dd> $ task li</dl>
<p> is an unambiguous abbreviation for </p>
<dl>
<dt>
<dd> $ task list</dl>
<p> but </p>
<dl>
<dt>
<dd> $ task l</dl>
<p> could be list, ls or long. </p>
<p> Note that you can restrict the minimum abbreviation size using the configuration setting: </p>
<dl>
<dt>
<dd> abbreviation.minimum=3</dl>
<h2>SPECIFYING DESCRIPTIONS</h2>
<p> Some task descriptions need to be escaped because of the shell and the special meaning of some characters to the shell. This can be done either by adding quotes to the description or escaping the special character: </p>
<dl>
<dt>
<dd> $ task add &quot;quoted &#8216; quote&quot;<br />
 $ task add escaped \&#8217; quote</dl>
<p> The argument &#8212; (a double dash) tells Taskwarrior to treat all other args as description: </p>
<dl>
<dt>
<dd> $ task add &#8212; project:Home needs scheduling</dl>
<p> In other situations, the shell sees spaces and breaks up arguments. For example, this command: </p>
<dl>
<dt>
<dd> $ task 123 modify /from this/to that/</dl>
<p> is broken up into several arguments, which is corrected with quotes: </p>
<dl>
<dt>
<dd> $ task 123 modify &quot;/from this/to that/&quot;</dl>
<p> It is sometimes necessary to force the shell to pass quotes to Taskwarrior intact, so you can use: </p>
<dl>
<dt>
<dd> $ task add project:\&#8217;Three Word Project\&#8217; description</dl>
<p> Taskwarrior supports Unicode using only the UTF8 encoding, with no Byte Order Marks in the data files. </p>
<h2>CONFIGURATION FILE AND OVERRIDE OPTIONS</h2>
<p> Taskwarrior stores its configuration in a file in the user&#8217;s home directory: ~/.taskrc. The default configuration file can be overridden with: </p>
<dl>
<dt><code>task rc:&lt;path-to-alternate-file&gt; &#8230;</code></p>
<dd> Specifies an alternate configuration file. </p>
<dt><code>TASKRC=/tmp/.taskrc task ..</code></p>
<dd> The environment variable overrides the default and the command line specification of the .taskrc file. </p>
<dt><code>task rc.&lt;name&gt;:&lt;value&gt; &#8230;</code></p>
<dd> <code>task rc.&lt;name&gt;=&lt;value&gt; &#8230;</code> Specifies individual configuration file overrides. </p>
<dt><code>TASKDATA=/tmp/.task task &#8230;</code></p>
<dd> The environment variable overrides the default, the command line, and the &#8216;data.location&#8217; configuration setting of the task data directory. </p>
</dl>
<h2>MORE EXAMPLES</h2>
<p> For examples please see the online documentation starting at </p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="http://taskwarrior.org/docs">http://taskwarrior.org/docs</a>&gt;</dl>
<p> Note that the online documentation can be more detailed and more current than this man page. </p>
<h2>FILES</h2>
<dl>
<dt>~/.taskrc</p>
<dd> User configuration file &#8211; see also <a href="/docs/linux/man/5-taskrc/">taskrc</a>(5). Note that this can be overridden on the command line or by the TASKRC environment variable. </p>
<dt>~/.task</p>
<dd> The default directory where task stores its data files. The location can be configured in the configuration variable &#8216;data.location&#8217;, or overridden with the TASKDATA environment variable.. </p>
<dt>~/.task/pending.data</p>
<dd> The file that contains the tasks that are not yet done. </p>
<dt>~/.task/completed.data</p>
<dd> The file that contains the completed (&quot;done&quot;) tasks. </p>
<dt>~/.task/undo.data</p>
<dd> The file that contains information needed by the &quot;undo&quot; command. </p>
</dl>
<h2>CREDITS &amp; COPYRIGHTS</h2>
<p> Copyright (C) 2006 &#8211; 2016 P. Beckingham, F. Hernandez. </p>
<p> Taskwarrior is distributed under the MIT license. See <a rel="nofollow" href="http://www.opensource.org/licenses/mit-license.php">http://www.opensource.org/licenses/mit-license.php</a> for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-taskrc/">taskrc</a>(5),</code> <code><a href="/docs/linux/man/5-task-color/">task-color</a>(5),</code> <code><a href="/docs/linux/man/5-task-sync/">task-sync</a>(5)</code> </p>
<p> For more information regarding Taskwarrior, see the following: </p>
<dl>
<dt>The official site at</p>
<dd> &lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt; </p>
<dt>The official code repository at</p>
<dd> &lt;<a rel="nofollow" href="https://git.tasktools.org/scm/tm/task.git">https://git.tasktools.org/scm/tm/task.git</a>&gt; </p>
<dt>You can contact the project by emailing</p>
<dd> &lt;support [at] taskwarrior.org&gt; </p>
</dl>
<h2>REPORTING BUGS</h2>
<dl>
<dt>Bugs in Taskwarrior may be reported to the issue-tracker at</p>
<dd> &lt;<a rel="nofollow" href="https://bug.tasktools.org/">https://bug.tasktools.org/</a>&gt; </p>
</dl>
<h2>Index</h2>
