---
title: "tigrc(5)"
name: "tigrc"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tigrc/"
description: "tigrc – Tig configuration file"
---

<p>tigrc &#8211; Tig configuration file</p>
<h2>Synopsis</h2>
<pre><code>set</code> <i>variable</i> <code>=</code> <i>value</i>
<code>bind</code> <i>keymap</i> <i>key</i> <i>action</i>
<code>color</code> <i>area</i> <i>fgcolor</i> <i>bgcolor</i> <i>[attributes]</i>
<code>source</code> <i>path</i></pre>
<h2>Description</h2>
<p>You can permanently set an option by putting it in the ~/.tigrc file. The file consists of a series of <i>commands</i>. Each line of the file may contain only one command. Commands can span multiple lines if each line is terminated by a backslash (<i>\</i>) character. </p>
<p> The hash mark (<i>#</i>) is used as a <i>comment</i> character. All text after the comment character to the end of the line is ignored. You can use comments to annotate your initialization file. </p>
<p> Certain options can be manipulated at runtime via the option menu. In addition, options can also be toggled with the :toggle prompt command or by entering the configuration command into the prompt. </p>
<p> In some environments, a user&#8217;s configuration will be stored in the alternate location $XDG_CONFIG_HOME/tig/config. For brevity, this document will refer only to ~/.tigrc.</p>
<h2>Git Configuration</h2>
<p>Alternatively to using ~/.tigrc, Tig options can be set by putting them in one of the Git configuration files, which are read by Tig on startup. See <i><a href="/docs/linux/man/1-git-config/">git-config</a>(1)</i> for which files to use. The following example show the basic syntax to use for settings, bindings and colors. </p>
<dl>
<dd>
<pre>[tig] show-changes = true
[tig &quot;color&quot;] cursor = yellow red bold
[tig &quot;bind&quot;] generic = P parent</pre>
</dl>
<p> In addition to tig-specific options, the following Git options are read from the Git configuration: </p>
<p> <i>color.*</i></p>
<dl>
<dd>Colors for the various UI types. Can be configured via the <i>git-colors</i> setting.</dl>
<p> <i>core.abbrev</i></p>
<dl>
<dd>The width of the commit ID. See also <i>id-width</i> option.</dl>
<p> <i>core.editor</i></p>
<dl>
<dd>The editor command. Can be overridden by setting GIT_EDITOR.</dl>
<p> <i>core.worktree</i></p>
<dl>
<dd>The path to the root of the working tree.</dl>
<p> <i>gui.encoding</i></p>
<dl>
<dd>The encoding to use for displaying of file content.</dl>
<p> <i>i18n.commitencoding</i></p>
<dl>
<dd>The encoding used for commits. The default is UTF-8.</dl>
<h2>Set Command</h2>
<p>A few selective variables can be configured via the set command. The syntax is: </p>
<dl>
<dd>
<pre><code>set</code> variables <code>=</code> value</pre>
</dl>
<p> Examples: </p>
<dl>
<dd>
<pre>set commit-order = topo # Order commits topologically
set git-colors = no # Do not read Git's color settings.
set horizontal-scroll = 33% # Scroll 33% of the view width
set blame-options = -C -C -C # Blame lines from other files
# Wrap branch names with () and tags with &lt;&gt;
set reference-format = (branch) &lt;tag&gt;
# Configure blame view columns using command spanning multiple lines.
set blame-view = \
 date:default \
 author:abbreviated \
 file-name:auto \
 id:yes,color \
 line-number:yes,interval=5 text</pre>
</dl>
<p> Or in the Git configuration files: </p>
<dl>
<dd>
<pre>[tig]
 line-graphics = no # Disable graphics characters
 tab-size = 8 # Number of spaces per tab</pre>
</dl>
<p> The type of variables is either bool, int, string, or mixed. </p>
<p> Valid bool values</p>
<dl>
<dd>To set a bool variable to true use either &quot;1&quot;, &quot;true&quot;, or &quot;yes&quot;. Any other value will set the variable to false.</dl>
<p> Valid int values</p>
<dl>
<dd>A non-negative integer.</dl>
<p> Valid string values</p>
<dl>
<dd>A string of characters. Optionally, use either &#8216; or &quot; as delimiters.</dl>
<p> Valid mixed values</p>
<dl>
<dd>These values are composites of the above types. The valid values are specified in the description.</dl>
<h3>Variables</h3>
<p>The following variables can be set: </p>
<p> <i>diff-options</i> (string)</p>
<dl>
<dd>A space-separated string of diff options to use in the diff view. <a href="/docs/linux/man/1-git-show/">git-show</a>(1) is used for formatting and always passes &#8211;patch-with-stat. Can control display of commit header metadata, passing option &#8211;format. This option overrides any options specified in the TIG_DIFF_OPTS environment variable (described in <code><a href="/docs/linux/man/1-tig/">tig</a></code>(1)), but is itself overridden by diff flags given on the command line invocation.</dl>
<p> <i>blame-options</i> (string)</p>
<dl>
<dd>A space-separated string of default blame options. Can be used for telling <a href="/docs/linux/man/1-git-blame/">git-blame</a>(1) how to detect the origin of lines. The options are ignored when Tig is started in blame mode and given blame options on the command line.</dl>
<p> <i>log-options</i> (string)</p>
<dl>
<dd>A space-separated string of default options that should be passed to the <a href="/docs/linux/man/1-git-log/">git-log</a>(1) command used by the log view. Options can be overridden by command line options. Used internally override custom &#8216;pretty.format&#8217; settings that break the log view.</dl>
<p> <i>main-options</i> (string)</p>
<dl>
<dd>A space-separated string of default options that should be passed to the <a href="/docs/linux/man/1-git-log/">git-log</a>(1) command used by the main view. Options can be overridden by command line options.</dl>
<p> <i>reference-format</i> (string)</p>
<dl>
<dd>A space-separated string of format strings used for formatting reference names. Wrap the name of the reference type with the characters you would like to use for formatting, e.g. [tag] and &lt;remote&gt;. If no format is specified for local-tag, the format for tag is used. Similarly, if no format is specified for tracked-remote the remote format is used. Prefix with hide: to not show that reference type, e.g. hide:remote. Supported reference types are: </p>
<dl>
<dd>&bull; head : The current HEAD.</dl>
<dl>
<dd>&bull; tag : A signed tag.</dl>
<dl>
<dd>&bull; local-tag : An unsigned tag.</dl>
<dl>
<dd>&bull; remote : A remote.</dl>
<dl>
<dd>&bull; tracked-remote : The remote tracked by current HEAD.</dl>
<dl>
<dd>&bull; replace : A replaced reference.</dl>
<dl>
<dd>&bull; branch : Any other reference.</dl>
</dl>
<p> <i>line-graphics</i> (mixed) [ascii|default|utf-8|&lt;bool&gt;]</p>
<dl>
<dd>What type of character graphics for line drawing.</dl>
<p> <i>truncation-delimiter</i> (mixed) [utf-8|&lt;string&gt;]</p>
<dl>
<dd>A single character to draw where columns are truncated. The default is &quot;~&quot;. The special value &quot;utf-8&quot; refers to the character &quot;&#8230;&quot; (&quot;Midline Horizontal Ellipsis&quot;).</dl>
<p> <i>horizontal-scroll</i> (mixed)</p>
<dl>
<dd>Interval to scroll horizontally in each step. Can be specified either as the number of columns, e.g. <i>5</i>, or as a percentage of the view width, e.g. <i>33%</i>, where the maximum is 100%. For percentages it is always ensured that at least one column is scrolled. The default is to scroll <i>50%</i> of the view width.</dl>
<p> <i>git-colors</i> (list)</p>
<dl>
<dd>A space-separated list of &quot;key=value&quot; pairs where the key is a Git color name and the value is a Tig color name, e.g. &quot;branch.current=main-head&quot; and &quot;grep.filename=grep.file&quot;. Set to &quot;no&quot; to disable.</dl>
<p> <i>show-notes</i> (mixed) [&lt;reference&gt;|&lt;bool&gt;]</p>
<dl>
<dd>Whether to show notes for a commit. When set to a note reference the reference is passed to git show &#8211;notes=. Notes are enabled by default.</dl>
<p> <i>show-changes</i> (bool)</p>
<dl>
<dd>Whether to show staged and unstaged changes in the main view.</dl>
<p> <i>show-untracked</i> (bool)</p>
<dl>
<dd>Whether to show also untracked changes in the main view.</dl>
<p> <i>vertical-split</i> (mixed) [auto|&lt;bool&gt;]</p>
<dl>
<dd>Whether to split the view horizontally or vertically. &quot;auto&quot; (which is the default) means that it will depend on the window dimensions. When true vertical orientation is used, and false sets the orientation to horizontal.</dl>
<p> <i>split-view-height</i> (mixed)</p>
<dl>
<dd>The height of the bottom view in a horizontally split display. Can be specified either as the number of rows, e.g. <i>5</i>, or as a percentage of the view height, e.g. <i>80%</i>, where the maximum is 100%. It is always ensured that the smaller of the views is at least four rows high. The default is <i>67%</i>.</dl>
<p> <i>split-view-width</i> (mixed)</p>
<dl>
<dd>Width of the right-most view in a vertically split display. Can be specified either as the number of column, e.g. <i>5</i>, or as a percentage of the view width, e.g. <i>80%</i>, where the maximum is 100%. It is always ensured that the smaller of the views is at least four columns wide. The default is <i>50%</i>.</dl>
<p> <i>status-show-untracked-dirs</i> (bool)</p>
<dl>
<dd>Show untracked directories contents in the status view (analog to git ls-files &#8211;directory option). On by default.</dl>
<p> <i>status-show-untracked-files</i> (bool)</p>
<dl>
<dd>Show untracked files in the status view (mirrors Git&#8217;s status.showUntrackedFiles option). On by default.</dl>
<p> <i>tab-size</i> (int)</p>
<dl>
<dd>Number of spaces per tab. The default is 8 spaces.</dl>
<p> <i>diff-context</i> (int)</p>
<dl>
<dd>Number of context lines to show for diffs.</dl>
<p> <i>diff-highlight</i> (mixed)</p>
<dl>
<dd>Whether to highlight diffs using Git&#8217;s <i>diff-highlight</i> program. Defaults to false. When set to true then <i>diff-highlight</i> is used, else the option value is used as the path. When this option is in effect, highlighted regions are governed by color diff-add-highlight and color diff-del-highlight.</dl>
<p> <i>ignore-space</i> (mixed) [no|all|some|at-eol|&lt;bool&gt;]</p>
<dl>
<dd>Ignore space changes in diff view. By default no space changes are ignored. Changing this to &quot;all&quot;, &quot;some&quot; or &quot;at-eol&quot; is equivalent to passing &quot;&#8211;ignore-all-space&quot;, &quot;&#8211;ignore-space&quot; or &quot;&#8211;ignore-space-at-eol&quot; respectively to git diff or git show. </p>
<p> <code>Warning:</code> when ignore-space is set to some, all or at-eol, then the <code>status-update</code> and <code>status-revert</code> may fail when updating or reverting chunks containing lines with space changes. Similarly, <code>stage-update-line</code> may fail when updating a line adjacent to a line with space changes</dl>
<p> <i>commit-order</i> (enum) [auto|default|topo|date|author-date|reverse]</p>
<dl>
<dd>Commit ordering using the default (chronological reverse) order, topological order, date order or reverse order. When set to &quot;auto&quot; (which is the default), topological order is automatically used in the main view when the commit graph is enabled. In repositories with a long commit history it is advised to set this option to &quot;default&quot; to speed up loading of the main view.</dl>
<p> <i>ignore-case</i> (enum) [no|yes|smart-case]</p>
<dl>
<dd>Ignore case in searches. &quot;smart-case&quot; ignores case if the search string doesn&#8217;t contain any uppercase letters. By default, the search is case sensitive.</dl>
<p> <i>mailmap</i> (bool)</p>
<dl>
<dd>Read canonical name and email addresses for authors and committers from .mailmap. Off by default. See <a href="/docs/linux/man/1-git-shortlog/">git-shortlog</a>(1).</dl>
<p> <i>wrap-lines</i> (bool)</p>
<dl>
<dd>Wrap long lines. By default, lines are not wrapped. Not compatible with line numbers enabled.</dl>
<p> <i>focus-child</i> (bool)</p>
<dl>
<dd>Whether to focus the child view when it is opened. When disabled the focus will remain in the parent view, avoiding reloads of the child view when navigating the parent view. True by default.</dl>
<p> <i>send-child-enter</i> (bool)</p>
<dl>
<dd>Whether to send &quot;enter&quot; key presses to the child view, even if parent view is active. When disabled the child view has to be explicitly focused to receive the &quot;enter&quot; key presses. In practice only relevant when set focus-child = no. True by default.</dl>
<p> <i>editor-line-number</i> (bool)</p>
<dl>
<dd>Whether to pass the selected line number to the editor command. The line number is passed as +&lt;line-number&gt; in front of the file name. Example: vim +10 tig.c</dl>
<p> <i>history-size</i> (int)</p>
<dl>
<dd>Size of the persistent ~/.tig_history file when compiled with readline support. Default is 500. Set to 0 to disable.</dl>
<p> <i>mouse</i> (bool)</p>
<dl>
<dd>Whether to enable mouse support. Off by default since it makes selecting text from the terminal less intuitive. When enabled hold down Shift (or Option on Mac) to select text. Mouse support requires that ncurses itself support mouse events.</dl>
<p> <i>mouse-scroll</i> (int)</p>
<dl>
<dd>Interval to scroll up or down using the mouse. The default is 3 lines. Mouse support requires that ncurses itself support mouse events and that you have enabled mouse support in ~/.tigrc with set mouse = true.</dl>
<p> <i>mouse-wheel-cursor</i> (bool)</p>
<dl>
<dd>Whether to prefer moving the cursor to scrolling the view when using the mouse wheel. Off by default. Combines well with set mouse-scroll = 1. Mouse support requires that ncurses itself support mouse events and that you have enabled mouse support in ~/.tigrc with set mouse = true.</dl>
<p> <i>pgrp</i> (bool)</p>
<dl>
<dd>Make tig process-group leader when starting and clean all processes when exiting. Off by default. Do not enable this option if you are using a Zsh version affected by zsh-workers/43379. Run xclip with setsid to keep clipboard content after exiting tig. If you are using git-credential-cache helper, set option credentialCache.ignoreSIGHUP.</dl>
<p> <i>start-on-head</i> (bool)</p>
<dl>
<dd>Start with cursor on HEAD commit.</dl>
<p> <i>refresh-mode</i> (mixed) [manual|auto|after-command|periodic|&lt;bool&gt;]</p>
<dl>
<dd>Configures how views are refreshed based on modifications to watched files in the repository. When set to <i>manual</i>, nothing is refreshed automatically. When set to <i>auto</i>, views are refreshed when a modification is detected in another view. When set to <i>after-command</i> only refresh after returning from an external command. When set to <i>periodic</i>, visible views are refreshed periodically using <i>refresh-interval</i>.</dl>
<p> <i>refresh-interval</i> (int)</p>
<dl>
<dd>Interval in seconds between view refresh update checks when <i>refresh-mode</i> is set to <i>periodic</i>.</dl>
<p> <i>file-args</i> (args)</p>
<dl>
<dd>Command line arguments referring to files. These are filtered using <a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a>(1).</dl>
<p> <i>rev-args</i> (args)</p>
<dl>
<dd>Command line arguments referring to revisions. These are filtered using <a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a>(1).</dl>
<h3>View settings</h3>
<p>The view settings define the order and options for the different columns of a view. Each view setting expects a space-separated list of column specifications. Column specifications starts with the column type, and can optionally be followed by a colon (:) and a list of column options. E.g. the following column specification defines an <i>author</i> column displaying the author email and with a fixed width of 20 characters: author:email,width=20. </p>
<p> The first option value in a column specification is always the <i>display</i> option. When no <i>display</i> value is given, <i>yes</i> is assumed. For <i>display</i> options expecting an enumerated value this will automatically resolve to the default enum value. For example, file-name will automatically have its <i>display</i> setting resolve to <i>auto</i>. </p>
<p> Specifications can also be given for a single column, for example to override the defaults in the system tigrc file. To override a single column, use the column name as a suffix after the view setting name, e.g. main-view-date will allow to set the date in the main view. </p>
<p> Examples: </p>
<dl>
<dd>
<pre># Enable both ID and line numbers in the blame view
set blame-view = date:default author:full file-name:auto id:yes,color \
 line-number:yes,interval=5 text
# Change grep view to be similar to `git grep` format
set grep-view = file-name:yes line-number:yes,interval=1 text
# Show file sizes as units
set tree-view = line-number:no,interval=5 mode author:full \
 file-size:units date:default id:no file-name
# Show line numbers for every 10th line in the pager view
set pager-view = line-number:yes,interval=10 text
# Shorthands to change view settings for a previously defined column
set main-view-date = custom
set main-view-date-format = &quot;%Y-%m-%d %H:%M&quot;
set blame-view-line-number = no
# Use Git's default commit order, even when the commit graph is enabled.
set commit-order = default</pre>
</dl>
<p> The following list shows which the available view settings and what column types they support: </p>
<p> blob-view, diff-view, log-view, pager-view, stage-view</p>
<dl>
<dd>line-number, text</dl>
<p> blame-view</p>
<dl>
<dd>author, date, file-name, id, line-number, text</dl>
<p> grep-view</p>
<dl>
<dd>file-name, line-number, text</dl>
<p> main-view, reflog-view</p>
<dl>
<dd>author, date, commit-title, id, line-number, ref</dl>
<p> refs-view</p>
<dl>
<dd>author, date, commit-title, id, line-number, ref</dl>
<p> stash-view</p>
<dl>
<dd>author, date, commit-title, id, line-number</dl>
<p> status-view</p>
<dl>
<dd>file-name, line-number, status</dl>
<p> tree-view</p>
<dl>
<dd>author, date, id, file-name, file-size, line-number, mode</dl>
<p> Supported column types and their respective column options: </p>
<p> author</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (mixed) [full|abbreviated|email|email-user|&lt;bool&gt;]: How to display author names. If set to &quot;abbreviated&quot; author initials will be shown.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the column. When set to a value between 1 and 10, the author name will be abbreviated to the author&#8217;s initials. When set to zero, the width is automatically sized to fit the content.</dl>
<dl>
<dd>&bull; <i>maxwidth</i> (int): Maximum width of the column. Permit automatically sizing content, up to this limit.</dl>
</dl>
<p> commit-title</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>graph</i> (mixed) [no|v2|v1]: Whether to show the revision graph in the main view on start-up. &quot;v1&quot; refers to the old graph rendering, which is less accurate but faster and thus recommended in large repositories. See also the <i>line-graphics</i> options.</dl>
<dl>
<dd>&bull; <i>refs</i> (bool): Whether to show references (branches, tags, and remotes) in the main view. Can be toggled.</dl>
<dl>
<dd>&bull; <i>overflow</i> (bool or int): Whether to highlight text in commit titles exceeding a given width. When set to a boolean, it enables or disables the highlighting using the default width of 50 character. When set to an int, the assigned value is used as the maximum character width.</dl>
</dl>
<p> date</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (mixed) [relative|relative-compact|custom|default|&lt;bool&gt;]: How to display dates. If set to &quot;relative&quot; or &quot;relative-compact&quot; a relative date will be used, e.g. &quot;2 minutes ago&quot; or &quot;2m&quot;. If set to &quot;custom&quot;, the <a href="/docs/linux/man/3-strftime/">strftime</a>(3) string format specified in the &quot;format&quot; option is used.</dl>
<dl>
<dd>&bull; <i>local</i> (bool): If true, use <a href="/docs/linux/man/3-localtime/">localtime</a>(3) to convert to local timezone. Note that relative dates always use local offsets.</dl>
<dl>
<dd>&bull; <i>format</i> (string): format string to pass to <a href="/docs/linux/man/3-strftime/">strftime</a>(3) when <i>custom</i> display mode has been selected.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the column. When set to zero, the width is automatically sized to fit the content.</dl>
</dl>
<p> file-name</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (mixed) [auto|always|&lt;bool&gt;]: When to display file names. If set to &quot;auto&quot; file names are shown only when needed, e.g. when running: tig blame -C &lt;file&gt;.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Width of the column. When set to zero, the width is automatically sized to fit the content.</dl>
<dl>
<dd>&bull; <i>maxwidth</i> (int): Maximum width of the column. Permit automatically sizing content, up to this limit.</dl>
</dl>
<p> file-size</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (mixed) [default|units|&lt;bool&gt;]: How to display file sizes. When set to &quot;units&quot;, sizes are shown using binary prefixes, e.g. 12524 bytes is shown as &quot;12.2K&quot;.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the filename column. When set to zero, the width is automatically sized to fit the content.</dl>
</dl>
<p> id</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (bool): Whether to show commit IDs in the main view.</dl>
<dl>
<dd>&bull; <i>width</i> (int) : Fixed width for the commit ID column. When unset Tig will use the value of <i>core.abbrev</i> if found. See <a href="/docs/linux/man/1-git-config/">git-config</a>(1) on how to set <i>core.abbrev</i>. When set to zero the width is automatically sized to fit the content of reflog (e.g. ref/stash@{4}) IDs and otherwise default to 7.</dl>
</dl>
<p> line-number</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (bool): Whether to show line numbers.</dl>
<dl>
<dd>&bull; <i>interval</i> (int): Interval between line numbers.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the column. When set to zero, the width is automatically sized to fit the content.</dl>
</dl>
<p> mode</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (bool): Whether to show file modes.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the column. When set to zero, the width is automatically sized to fit the content.</dl>
</dl>
<p> ref</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (bool): Whether to show the reference name.</dl>
<dl>
<dd>&bull; <i>width</i> (int): Fixed width for the column. When set to zero, the width is automatically sized to fit the content.</dl>
<dl>
<dd>&bull; <i>maxwidth</i> (int): Maximum width of the column. Permit automatically sizing content, up to this limit.</dl>
</dl>
<p> status</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>display</i> (mixed) [no|short|long|&lt;bool&gt;]: How to display the status label.</dl>
</dl>
<p> text</p>
<dl>
<dd>
<dl>
<dd>&bull; <i>commit-title-overflow</i> (bool or int): Whether to highlight commit titles exceeding a given width in the diff view. When set to a boolean, it enables or disables the highlighting using the default width of 50 character. When set to an int, the assigned value is used as the maximum character width.</dl>
</dl>
<p> All column options can be toggled. For <i>display</i> options, use the option name as the prefix followed by a dash and the column name. E.g. :toggle author-display will toggle the <i>display</i> option in the <i>author</i> column. For all other options use the column name followed by a dash and then the option name as the suffix. E.g. :toggle commit-title-graph will toggle the <i>graph</i> option in the <i>commit-title</i> column. Alternatively, use the option menu to manipulate options.</p>
<h2>Bind Command</h2>
<p>Using bind commands, keys can be mapped to an action when pressed in a given key map. The syntax is: </p>
<dl>
<dd>
<pre><code>bind</code> <i>keymap</i> <i>key</i> <i>action</i></pre>
</dl>
<p> Examples: </p>
<dl>
<dd>
<pre># Add keybinding to quickly jump to the next diff chunk in the stage view
bind stage &lt;Enter&gt; :/^@@
# Disable the default mapping for running git-gc
bind generic G none
# User-defined external command to amend the last commit
bind status + !git commit --amend
# User-defined internal command that reloads ~/.tigrc
bind generic S :source ~/.tigrc
# UTF8-encoded characters can be used as key values.
bind generic &oslash; @sh -c &quot;printf '%s' %(commit) | pbcopy&quot;</pre>
</dl>
<p> Or in the Git configuration files: </p>
<dl>
<dd>
<pre>[tig &quot;bind&quot;]
 # 'unbind' the default quit key binding
 main = Q none
 # Cherry-pick current commit onto current branch
 generic = C !git cherry-pick %(commit)</pre>
</dl>
<p> Keys are mapped by first searching the keybindings for the current view, then the keybindings for the <code>generic</code> keymap, and last the default keybindings. Thus, the view keybindings override the generic keybindings which override the built-in keybindings. </p>
<p> Keybindings at the line-entry prompt are typically governed by the readline library, and are configured separately in ~/.inputrc. See <i><a href="/docs/linux/man/1-readline/">readline</a>(1)</i>. Tig respects but does not require an $if tig section in ~/.inputrc. </p>
<p> Keymaps</p>
<dl>
<dd>Valid keymaps are: <code>main</code>, <code>diff</code>, <code>log</code>, <code>reflog</code>, <code>help</code>, <code>pager</code>, <code>status</code>, <code>stage</code>, <code>tree</code>, <code>blob</code>, <code>blame</code>, <code>refs</code>, <code>stash</code>, <code>grep</code> and <code>generic</code>. Use <code>generic</code> to set key mapping in all keymaps. Use <code>search</code> to define keys for navigating search results during search.</dl>
<p> Key values</p>
<dl>
<dd>Key values should never be quoted. Use either an ASCII or UTF8-encoded character or one of the following symbolic key names. Symbolic key names are case insensitive and starts with &quot;&lt;&quot; and ends with &quot;&gt;&quot;. Use <code>&lt;Hash&gt;</code> to bind to the # key, since the hash mark is used as a comment character. Use <code>&lt;LessThan&gt;</code> to bind to the &lt; key.</dl>
<p> <code>&lt;Enter&gt;</code>, <code>&lt;Space&gt;</code>, <code>&lt;Backspace&gt;</code>, <code>&lt;Tab&gt;</code>, <code>&lt;Escape&gt;</code> or <code>&lt;Esc&gt;</code>, <code>&lt;Left&gt;</code>, <code>&lt;Right&gt;</code>, <code>&lt;Up&gt;</code>, <code>&lt;Down&gt;</code>, <code>&lt;Insert&gt;</code> or <code>&lt;Ins&gt;</code>, <code>&lt;Delete&gt;</code> or <code>&lt;Del&gt;</code>, <code>&lt;Hash&gt;</code>, <code>&lt;LessThan&gt;</code> or <code>&lt;LT&gt;</code>, <code>&lt;Home&gt;</code>, <code>&lt;End&gt;</code>, <code>&lt;PageUp&gt;</code> or <code>&lt;PgUp&gt;</code>, <code>&lt;PageDown&gt;</code> or <code>&lt;PgDown&gt;</code>, <code>&lt;ScrollBack&gt;</code> or <code>&lt;SBack&gt;</code>, <code>&lt;ScrollFwd&gt;</code> or <code>&lt;SFwd&gt;</code>, <code>&lt;ShiftTab&gt;</code> or <code>&lt;BackTab&gt;</code>, <code>&lt;ShiftLeft&gt;</code>, <code>&lt;ShiftRight&gt;</code>, <code>&lt;ShiftDelete&gt;</code> or <code>&lt;ShiftDel&gt;</code>, <code>&lt;ShiftHome&gt;</code>, <code>&lt;ShiftEnd&gt;</code>, <code>&lt;SingleQuote&gt;</code>, <code>&lt;DoubleQuote&gt;</code>, <code>&lt;F1&gt;</code> &#8230; <code>&lt;F19&gt;</code> </p>
<p> To define key mappings with the Ctrl key, use &lt;Ctrl-key&gt;. In addition, key combos consisting of an initial Escape key followed by a normal key value can be bound using &lt;Esc&gt;key. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>bind main R refresh
bind main &lt;Down&gt; next
bind main &lt;Ctrl-f&gt; scroll-page-down
bind main &lt;Esc&gt;o options
bind main &lt;ShiftTab&gt; parent</pre>
</dl>
<p> Notes </p>
<dl>
<dd>&bull; Tig reads keystrokes via ncurses and is subject to various limitations. See <i><a href="//www.systutorials.com/docs/linux/man/3x-ncurses/">ncurses</a>(3x)</i> and <i><a href="/docs/linux/man/5-terminfo/">terminfo</a>(5)</i> (or termcap).</dl>
<dl>
<dd>&bull; Ctrl-m and Ctrl-i cannot be bound as they conflict with <i>Enter</i> and <i>Tab</i> respectively.</dl>
<dl>
<dd>&bull; Case differences cannot be distinguished in control sequences such as Ctrl-f and Ctrl-F.</dl>
<dl>
<dd>&bull; Ctrl-&lt;Space&gt; is typically translated to Ctrl-@, which is available for binding.</dl>
<dl>
<dd>&bull; Only some subset of special symbolic keys such as &lt;ShiftTab&gt; will be available in any given terminal emulator.</dl>
<dl>
<dd>&bull; Ctrl-z is automatically used for process control and will suspend Tig and open a subshell (use fg to reenter Tig). </p>
<p> Actions</p>
<dl>
<dd>Actions are either specified as user-defined commands (external or internal) or using action names as described in the following sections.</dl>
</dl>
<h3>External user-defined command</h3>
<p>These actions start with one or more of the following option flags followed by the command that should be executed. </p>
<table>
<tr VALIGN=top>
<td>
<p> ! </td>
<td>
<p> Run the command in the foreground with output shown.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> @ </td>
<td>
<p> Run the command in the background with no output.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> + </td>
<td>
<p> Run the command synchronously, and echo the first line of output to the status bar.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ? </td>
<td>
<p> Prompt the user before executing the command.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> &lt; </td>
<td>
<p> Exit Tig after executing the command.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> &gt; </td>
<td>
<p> Re-open Tig instantly in the last displayed view after executing the command.
</td>
</tr>
</table>
<p> Unless otherwise specified, commands are run in the foreground with their console output shown (as if <i>!</i> was specified). When multiple command options are specified their behavior are combined, e.g. &quot;?&lt;git commit&quot; will prompt the user whether to execute the command and will exit Tig after completion. </p>
<p> <font SIZE="+1"> <code>Browsing state variables</code></p>
<dl>
<dd>User-defined commands can optionally refer to Tig&#8217;s internal state using the following variable names, which are substituted before commands are run: </font></p>
<table>
<tr VALIGN=top>
<td>
<p> %(head) </td>
<td>
<p> The currently viewed <i>head</i> ID. Defaults to HEAD
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(commit) </td>
<td>
<p> The currently selected commit ID.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(blob) </td>
<td>
<p> The currently selected blob ID.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(branch) </td>
<td>
<p> The currently selected branch name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(remote) </td>
<td>
<p> The currently selected remote name. For remote branches %(branch) will contain the branch name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(tag) </td>
<td>
<p> The currently selected tag name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(refname) </td>
<td>
<p> The currently selected reference name including the remote name for remote branches.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(stash) </td>
<td>
<p> The currently selected stash name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(directory) </td>
<td>
<p> The current directory path in the tree view or &quot;.&quot; if undefined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(file) </td>
<td>
<p> The currently selected file.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(lineno) </td>
<td>
<p> The currently selected line number. Defaults to 0.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(ref) </td>
<td>
<p> The reference given to blame or HEAD if undefined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(revargs) </td>
<td>
<p> The revision arguments passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(fileargs) </td>
<td>
<p> The file arguments passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(cmdlineargs) </td>
<td>
<p> All other options passed on the command line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(diffargs) </td>
<td>
<p> Options from <i>diff-options</i> or <i>TIG_DIFF_OPTS</i> used by the diff and stage view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(blameargs) </td>
<td>
<p> Options from <i>blame-options</i> used by the blame view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(logargs) </td>
<td>
<p> Options from <i>log-options</i> used by the log view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(mainargs) </td>
<td>
<p> Options from <i>main-options</i> used by the main view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(prompt) </td>
<td>
<p> Prompt for the argument value. Optionally specify a custom prompt using &quot;%(prompt Enter branch name: )&quot;
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(text) </td>
<td>
<p> The text of the currently selected line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:head) </td>
<td>
<p> The name of the checked out branch, e.g. master
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:head-id) </td>
<td>
<p> The commit ID of the checked out branch.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:remote) </td>
<td>
<p> The remote associated with the checked out branch, e.g. origin/master.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:cdup) </td>
<td>
<p> The path to change directory to the repository root, e.g. ../
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:prefix) </td>
<td>
<p> The path prefix of the current work directory, e.g subdir/.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:git-dir) </td>
<td>
<p> The path to the Git directory, e.g. /src/repo/.git.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:worktree) </td>
<td>
<p> The worktree path, if defined.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> %(repo:is-inside-work-tree) </td>
<td>
<p> Whether Tig is running inside a work tree, either true or false.
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> Examples: </p>
<dl>
<dd></font></p>
<pre># Save the current commit as a patch file when the user selects a commit
# in the main view and presses 'S'.
bind main S !git format-patch -1 %(commit)
# Create and checkout a new branch; specify custom prompt
bind main B ?git checkout -b &quot;%(prompt Enter new branch name: )&quot;
# Show commit statistics for the author under the cursor
bind main U +sh -c 'git --no-pager shortlog -s --author=&quot;$(git show -s --format=%aE %(commit))&quot; &lt;/dev/tty'</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Advanced shell-like commands</code></p>
<dl>
<dd>If your command requires use of dynamic features, such as subshells, expansion of environment variables and process control, this can be achieved by using a shell command: </p>
<p> <code>Example 1. Configure a binding to copy the current commit ID to the clipboard.</code> </p>
<dl>
<dd></font></p>
<pre>bind generic I @sh -c &quot;echo -n %(commit) | xclip -selection c&quot;</pre>
</dl>
<p> Or by using a combination of Git aliases and Tig external commands. The following example entries can be put in either the .gitconfig or .git/config file: </p>
<p> <code>Example 2. Git configuration which binds Tig keys to Git command aliases.</code> </p>
<dl>
<dd>
<pre>[alias]
 gitk-bg = !&quot;gitk HEAD --not $(git rev-parse --remotes) &amp;&quot;
 publish = !&quot;for i in origin public; do git push $i; done&quot;
[tig &quot;bind&quot;]
 # @-prefix means that the console output will not be shown.
 generic = V !@git gitk-bg
 generic = &gt; !git publish</pre>
</dl>
</dl>
<h3>Internal user-defined commands</h3>
<p>Actions beginning with a <i>:</i> will be run and interpreted as internal commands and act similar to commands run via Tig&#8217;s prompt. Valid internal commands are configuration file options (as described in this document) and pager view commands. Examples: </p>
<dl>
<dd>
<pre># Reload ~/.tigrc when 'S' is pressed
bind generic S :source .tigrc
# Change diff view to show all commit changes regardless of file limitations
bind diff F :set diff-options = --full-diff
# Show the output of <a href="//www.systutorials.com/docs/linux/man/1-git-reflog/">git-reflog</a>(1) in the pager view
bind generic W :!git reflog
# Search for previous diff (c)hunk and next diff header
bind stage 2 :?^@@
bind stage D :/^diff --(git|cc)
bind main I :toggle id # Show/hide the ID column
bind diff D :toggle diff-options --minimal # Use minimal diff algorithm
bind diff [ :toggle diff-context -3 # Decrease context (-U arg)
bind diff ] :toggle diff-context +3 # Increase context
bind generic V :toggle split-view-height -10% # Decrease split height</pre>
</dl>
<p> Similar to external commands, pager view commands can contain variable names that will be substituted before the command is run.</p>
<h3>Action names</h3>
<p>Valid action names are described below. Note, all action names are case-insensitive, and you may use <i>&#8211;</i>, <i>_</i>, and <i>.</i> interchangeably, e.g. &quot;view-main&quot;, &quot;View.Main&quot;, and &quot;VIEW_MAIN&quot; are the same. </p>
<p> <font SIZE="+1"> <code>View switching</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> view-main </td>
<td>
<p> Show main view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-diff </td>
<td>
<p> Show diff view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-log </td>
<td>
<p> Show log view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-reflog </td>
<td>
<p> Show reflog view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-tree </td>
<td>
<p> Show tree view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-blob </td>
<td>
<p> Show blob view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-blame </td>
<td>
<p> Show blame view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-refs </td>
<td>
<p> Show refs view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-status </td>
<td>
<p> Show status view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-stage </td>
<td>
<p> Show stage view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-stash </td>
<td>
<p> Show stash view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-grep </td>
<td>
<p> Show grep view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-pager </td>
<td>
<p> Show pager view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-help </td>
<td>
<p> Show help view
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
</dl>
<p> </font><font SIZE="+2"> <code>View manipulation</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> enter </td>
<td>
<p> Enter and open selected line
</td>
</tr>
<tr VALIGN=top>
<td>
<p> back </td>
<td>
<p> Go back to the previous view state
</td>
</tr>
<tr VALIGN=top>
<td>
<p> next </td>
<td>
<p> Move to next
</td>
</tr>
<tr VALIGN=top>
<td>
<p> previous </td>
<td>
<p> Move to previous
</td>
</tr>
<tr VALIGN=top>
<td>
<p> parent </td>
<td>
<p> Move to parent
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-next </td>
<td>
<p> Move focus to the next view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> refresh </td>
<td>
<p> Reload and refresh view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> maximize </td>
<td>
<p> Maximize the current view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-close </td>
<td>
<p> Close the current view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> view-close-no-quit </td>
<td>
<p> Close the current view without quitting
</td>
</tr>
<tr VALIGN=top>
<td>
<p> quit </td>
<td>
<p> Close all views and quit
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
</dl>
<p> </font><font SIZE="+3"> <code>View-specific actions</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> status-update </td>
<td>
<p> Stage/unstage chunk or file changes
</td>
</tr>
<tr VALIGN=top>
<td>
<p> status-revert </td>
<td>
<p> Revert chunk or file changes
</td>
</tr>
<tr VALIGN=top>
<td>
<p> status-merge </td>
<td>
<p> Merge file using external tool
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stage-update-line </td>
<td>
<p> Stage/unstage single line
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stage-split-chunk </td>
<td>
<p> Split current diff chunk
</td>
</tr>
</table>
<p> <font SIZE="+3"> </p>
</dl>
<p> </font><font SIZE="+4"> <code>Cursor navigation</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> move-up </td>
<td>
<p> Move cursor one line up
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-down </td>
<td>
<p> Move cursor one line down
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-page-down </td>
<td>
<p> Move cursor one page down
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-page-up </td>
<td>
<p> Move cursor half a page up
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-half-page-down </td>
<td>
<p> Move cursor half a page down
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-half-page-up </td>
<td>
<p> Move cursor one page up
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-first-line </td>
<td>
<p> Move cursor to first line
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-last-line </td>
<td>
<p> Move cursor to last line
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-next-merge </td>
<td>
<p> Move cursor to next merge commit
</td>
</tr>
<tr VALIGN=top>
<td>
<p> move-prev-merge </td>
<td>
<p> Move cursor to previous merge commit
</td>
</tr>
</table>
<p> <font SIZE="+4"> </p>
</dl>
<p> </font><font SIZE="+5"> <code>Scrolling</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> scroll-line-up </td>
<td>
<p> Scroll one line up
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-line-down </td>
<td>
<p> Scroll one line down
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-page-up </td>
<td>
<p> Scroll one page up
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-page-down </td>
<td>
<p> Scroll one page down
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-first-col </td>
<td>
<p> Scroll to the first line columns
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-left </td>
<td>
<p> Scroll two columns left
</td>
</tr>
<tr VALIGN=top>
<td>
<p> scroll-right </td>
<td>
<p> Scroll two columns right
</td>
</tr>
</table>
<p> <font SIZE="+5"> </p>
</dl>
<p> </font><font SIZE="+6"> <code>Searching</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> search </td>
<td>
<p> Search the view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> search-back </td>
<td>
<p> Search backwards in the view
</td>
</tr>
<tr VALIGN=top>
<td>
<p> find-next </td>
<td>
<p> Find next search match
</td>
</tr>
<tr VALIGN=top>
<td>
<p> find-prev </td>
<td>
<p> Find previous search match
</td>
</tr>
</table>
<p> <font SIZE="+6"> </p>
</dl>
<p> </font><font SIZE="+7"> <code>Misc</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> edit </td>
<td>
<p> Open in editor
</td>
</tr>
<tr VALIGN=top>
<td>
<p> prompt </td>
<td>
<p> Open the prompt
</td>
</tr>
<tr VALIGN=top>
<td>
<p> options </td>
<td>
<p> Open the options menu
</td>
</tr>
<tr VALIGN=top>
<td>
<p> screen-redraw </td>
<td>
<p> Redraw the screen
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stop-loading </td>
<td>
<p> Stop all loading views
</td>
</tr>
<tr VALIGN=top>
<td>
<p> show-version </td>
<td>
<p> Show version information
</td>
</tr>
<tr VALIGN=top>
<td>
<p> none </td>
<td>
<p> Do nothing
</td>
</tr>
</table>
<p> <font SIZE="+7"> </p>
</dl>
<p> </font></p>
<h2>Color Command</h2>
<p>Color commands control highlighting and the user interface styles. If your terminal supports color, these commands can be used to assign foreground and background combinations to certain areas. Optionally, an attribute can be given as the last parameter. The syntax is: </p>
<dl>
<dd>
<pre><code>color</code> <i>area</i> <i>fgcolor</i> <i>bgcolor</i> <i>[attributes]</i></pre>
</dl>
<p> Examples: </p>
<dl>
<dd>
<pre># Override the default terminal colors to white on black.
color default white black
# Diff colors
color diff-header yellow default
color diff-index blue default
color diff-chunk magenta default
color &quot;Reported-by:&quot; green default
# View-specific color
color tree.date black cyan bold</pre>
</dl>
<p> Or in the Git configuration files: </p>
<dl>
<dd>
<pre>[tig &quot;color&quot;]
 # A strange looking cursor line
 cursor = red default underline
 # UI colors
 title-blur = white blue
 title-focus = white blue bold
# View-specific color
[tig &quot;color.tree&quot;]
 date = cyan default bold</pre>
</dl>
<p> Area names</p>
<dl>
<dd>Can be either a built-in area name or a custom quoted string. The latter allows custom color rules to be added for lines matching a quoted string. Valid built-in area names are described below. Note, all names are case-insensitive, and you may use <i>&#8211;</i>, and <i>_</i> interchangeably, e.g. &quot;Diff-Header&quot; and &quot;DIFF_HEADER&quot; are the same. View-specific colors can be defined by prefixing the view name to the area name, e.g. &quot;stage.diff-chunk&quot; and &quot;diff.diff-chunk&quot;.</dl>
<p> Color names</p>
<dl>
<dd>Valid colors include: <code>white</code>, <code>black</code>, <code>green</code>, <code>magenta</code>, <code>blue</code>, <code>cyan</code>, <code>yellow</code>, <code>red</code>, <code>default</code>. Use <code>default</code> to refer to the default terminal colors, for example, to keep the background transparent when you are using a terminal with a transparent background. </p>
<p> Colors can also be specified using the keywords <code>color0</code>, <code>color1</code>, &#8230;, <code>colorN-1</code> (where <code>N</code> is the number of colors supported by your terminal). This is useful when you remap the colors for your display or want to enable colors supported by 88-color and 256-color terminals. Note that the <i>color</i> prefix is optional. If you prefer, you can specify colors directly by their numbers <code>0</code>, <code>1</code>, &#8230;, <code>N-1</code> instead, just like in the configuration file of Git.</dl>
<p> Attribute names</p>
<dl>
<dd>Valid attributes include: <code>normal</code>, <code>blink</code>, <code>bold</code>, <code>dim</code>, <code>reverse</code>, <code>standout</code>, and <code>underline</code>. Note, not all attributes may be supported by the terminal.</dl>
<h3>UI colors</h3>
<p>The colors and attributes to be used for the text that is not highlighted or that specify the use of the default terminal colors can be controlled by setting the <code>default</code> color option. </p>
<p> <code>Table 1. General</code> </p>
<table>
<tr VALIGN=top>
<td>
<p> default </td>
<td>
<p> Override default terminal colors (see above).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cursor </td>
<td>
<p> The cursor line.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> status </td>
<td>
<p> The status window showing info messages.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> title-focus </td>
<td>
<p> The title window for the current view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> title-blur </td>
<td>
<p> The title window of any backgrounded view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> search-result </td>
<td>
<p> Highlighted search result.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> delimiter </td>
<td>
<p> Delimiter shown for truncated lines.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> header </td>
<td>
<p> The view header lines. Use <i>status.header</i> to color the staged, unstaged, and untracked sections in the status view. Use <i>help.header</i> to color the keymap sections in the help view.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> line-number </td>
<td>
<p> Line numbers.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> The commit ID.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> date </td>
<td>
<p> The author date.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> author </td>
<td>
<p> The commit author.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mode </td>
<td>
<p> The file mode holding the permissions and type.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> overflow </td>
<td>
<p> Title text overflow.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> directory </td>
<td>
<p> The directory name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> file </td>
<td>
<p> The file name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> file-size </td>
<td>
<p> File size.
</td>
</tr>
</table>
<p> <code>Table 2. Main view colors</code> </p>
<table>
<tr VALIGN=top>
<td>
<p> graph-commit </td>
<td>
<p> The commit dot in the revision graph.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> palette-[0-13] </td>
<td>
<p> 14 different colors, used for distinguishing branches or commits. By default, the palette uses the ASCII colors, where the second half of them have the bold attribute enabled to give a brighter color. Example: palette-0 = red
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-commit </td>
<td>
<p> The commit comment.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-annotated </td>
<td>
<p> The commit comment of an annotated commit.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-head </td>
<td>
<p> Label of the current branch.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-remote </td>
<td>
<p> Label of a remote.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-tracked </td>
<td>
<p> Label of the remote tracked by the current branch.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-tag </td>
<td>
<p> Label of a signed tag.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-local-tag </td>
<td>
<p> Label of a local tag.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-ref </td>
<td>
<p> Label of any other reference.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> main-replace </td>
<td>
<p> Label of replaced reference.
</td>
</tr>
</table>
<p> <code>Table 3. Status view</code> </p>
<table>
<tr VALIGN=top>
<td>
<p> stat-none </td>
<td>
<p> Empty status label.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stat-staged </td>
<td>
<p> Status flag of staged files.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stat-unstaged </td>
<td>
<p> Status flag of unstaged files.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stat-untracked </td>
<td>
<p> Status flag of untracked files.
</td>
</tr>
</table>
<p> <code>Table 4. Help view</code> </p>
<table>
<tr VALIGN=top>
<td>
<p> help-group </td>
<td>
<p> Help group name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> help-action </td>
<td>
<p> Help action name.
</td>
</tr>
</table>
<h3>Highlighting</h3>
<p>Diff markup</p>
<dl>
<dd>Options concerning diff start, chunks and lines added and deleted.</dl>
<p> <code>diff-header</code>, <code>diff-chunk</code>, <code>diff-add</code>, <code>diff-add2</code>, <code>diff-del</code>, <code>diff-del2</code>, <code>diff-add-highlight</code>, <code>diff-del-highlight</code> </p>
<p> Enhanced Git diff markup</p>
<dl>
<dd>Extra diff information emitted by the Git diff machinery, such as mode changes, rename detection, and similarity.</dl>
<p> <code>diff-oldmode</code>, <code>diff-newmode</code>, <code>diff-copy-from</code>, <code>diff-copy-to</code>, <code>diff-similarity</code>, <code>diff-index</code> </p>
<p> Pretty print commit headers</p>
<dl>
<dd>Commit diffs and the revision logs are usually formatted using pretty printed headers , unless &#8211;pretty=raw was given. This includes lines, such as merge info, commit ID, and author and committer date.</dl>
<p> <code>pp-refs</code>, <code>pp-reflog</code>, <code>pp-reflogmsg</code>, <code>pp-merge</code> </p>
<p> Raw commit header</p>
<dl>
<dd>Usually shown when &#8211;pretty=raw is given, however <i>commit</i> is pretty much omnipresent.</dl>
<p> <code>commit</code>, <code>parent</code>, <code>tree</code>, <code>author</code>, <code>committer</code> </p>
<p> Commit message</p>
<dl>
<dd>Signed-off-by, Acked-by, Reviewed-by and Tested-by lines are colorized. Characters in the commit title exceeding a predefined width can be highlighted.</dl>
<p> Tree markup</p>
<dl>
<dd>Colors for information of the tree view.</dl>
<p> <code>tree-dir</code>, <code>tree-file</code></p>
<h2>Source Command</h2>
<p>Source commands make it possible to read additional configuration files. Sourced files are included in-place, meaning when a <i>source</i> command is encountered the file will be immediately read. Any commands later in the current configuration file will take precedence. </p>
<p> If the given path does not exist, tig will proceed with a warning. Give the -q parameter to suppress the warning. </p>
<p> The syntax is: </p>
<dl>
<dd>
<pre><code>source</code> <i>[-q]</i> <i>path</i></pre>
</dl>
<p> Examples: </p>
<dl>
<dd>
<pre>source ~/.tig/colorscheme.tigrc
source ~/.tig/keybindings.tigrc</pre>
</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2006-2014 Jonas Fonseca &lt;m[blue]<code>jonas.fonseca [at] gmail.com</code>m[]<font SIZE="-2">[1]</font>&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tig/">tig</a></code>(1), <code><a href="/docs/linux/man/7-tigmanual/">tigmanual</a></code>(7), <a href="/docs/linux/man/7-git/">git</a>(7), <a href="/docs/linux/man/1-git-config/">git-config</a>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>jonas.fonseca [at] gmail.com</p>
<dl>
<dd>mailto:jonas.fonseca [at] gmail.com</dl>
