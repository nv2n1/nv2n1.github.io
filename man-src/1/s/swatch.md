---
title: "swatch(1)"
name: "swatch"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swatch/"
description: "swatch – simple watcher"
---

<h2 class="name">NAME</h2>
<p> swatch &#8211; simple watcher </p>
<h2>SYNOPSIS</h2>
<p> <code>swatch</code> [ <code>&#8211;awk-field-syntax</code> ] [ <code>&#8211;config-file|-c</code> <i>file</i> ] [ <code>&#8211;daemon</code> ] [ <code>&#8211;extra-include-dir|-I</code> <i>path</i> ] [ <code>&#8211;extra-module|-M</code> <i>module_name</i> ] [ <code>&#8211;help|-h</code> ] [ <code>&#8211;input-record-separator</code> <i>regex</i> ] [ <code>&#8211;old-style-config|-O</code> ] [ <code>&#8211;pid-file</code> <i>file</i> ] [ <code>&#8211;restart-time|-r</code> <i>time</i> ] [ <code>&#8211;script-dir</code> <i>path</i> ] [ <code>&#8211;tail-args</code> <i>arguments_for_tail_program</i> ] [ <code>&#8211;tail-program-name</code> <i>filename</i> ] [ <code>&#8211;version|-V</code> ] [ <code>&#8211;use-cpan-file-tail</code> ] [ [ <code>&#8211;examine|-f</code> <i>file_to_examine</i> ] | [ <code>&#8211;read-pipe|-p</code> <i>program_to_pipe_from</i> ] | [ <code>&#8211;tail-file|-t</code> <i>file_to_tail</i> ] ] [ <code>&#8211;debug</code> [ <i>level</i> ] ] [ <code>&#8211;dump-script</code> <i>filename</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Swatch</code> is designed to monitor system activity. In order for <code>Swatch</code> to be useful, it requires a configuration file which contains <i>pattern(s)</i> to look for and <i>action(s)</i> to perform when each pattern is found.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>&#8211;awk-field-syntax</code></p>
<dd> Use this option only if you want to overide regular expression backreferencing in favor of <a href="/docs/linux/man/1-awk/">awk</a><code>(1)</code> style field referencing. Included for backward compatability.</p>
<dt><code>&#8211;config-file|-c</code> <i>filename</i></p>
<dd> Tells <code>swatch</code> where to find its configuration file. The default is <i>${</i><font SIZE="-1"><i>HOME</i></font><i>}/.swatchrc</i>.</p>
<dt><code>&#8211;daemon</code></p>
<dd> This tells <code>swatch</code> to run in the background and disassociate itself from any terminal.</p>
<dt><code>&#8211;extra-include-dir|-I</code> <i>path</i></p>
<dd> This tells <code>swatch</code> where to look for custom <i>action</i> modules.</p>
<dt><code>&#8211;extra-module|-M</code> <i>module_name</i></p>
<dd> This tells <code>swatch</code> what custom <i>action</i> modules to load in.</p>
<dt><code>&#8211;help|-h</code></p>
<dd> Prints usage information and exits.</p>
<dt><code>&#8211;input-record-separator</code>=<i>regular_expression</i></p>
<dd> Tells <code>swatch</code> to use <i>regular_expression</i> to delineate the boundary of each input record. The default is a carriage return.</p>
<dt><code>&#8211;old-style-config|-O</code></p>
<dd> This tells <code>swatch</code> that your configuration file is written using the syntax that was abandoned back in the 1990&#8217;s.</p>
<dt><code>&#8211;pid-file</code> <i>file</i></p>
<dd> Writes the process <font SIZE="-1">ID</font> to <i>file</i>. Useful when running in daemon mode.</p>
<dt><code>&#8211;restart-time</code>=<i>[+]hh:mm[am|pm]</i> or <code>-r</code> <i>[+]hh:mm[am|pm]</i></p>
<dd> Restart at the specified time where <i>hh</i> is hours and <i>mm</i> is minutes. If the am/pm indicator is omitted, then a 24-hour clock is assumed. If the time is preceded by the &#8220;+&#8221; character, then the restart time will be set to the current time plus the specified time and the am/pm indicator will be ignored.</p>
<dt><code>&#8211;script-dir</code>=<i>/path/to/directory</i></p>
<dd> This switch causes the temporary watcher script to be written to a file in the specified directory rather than the user&#8217;s home directory. It is highly advised that you do <font SIZE="-1"><code>NOT</code></font> use directories that are writable by others such as /tmp.</p>
<dt><code>&#8211;tail-args</code> <i>arguments_for_tail_program</i></p>
<dd> Pass specific options to the <a href="/docs/linux/man/1-tail/">tail</a><code>(1)</code> program.</p>
<dt><code>&#8211;tail-program-name</code> <i>filename</i></p>
<dd> Runs an alternate <a href="/docs/linux/man/1-tail/">tail</a><code>(1)</code> like program instead of the system default.</p>
<dt><code>&#8211;version</code> or <code>-V</code></p>
<dd> Prints version information and exits.</p>
<dt><code>&#8211;use-cpan-file-tail</code></p>
<dd> Use <font SIZE="-1">CPAN</font>&#8216;s File::Tail module to read the log file instead of the <i><a href="/docs/linux/man/1-tail/">tail</a></i>(1) command.</dl>
<p> You may specify only one of the following options:</p>
<dl>
<dt><code>&#8211;tail-file</code>=<i>filename</i> or <code>-t</code> <i>filename</i></p>
<dd> Examine lines of text as they are added to filename.</p>
<dt><code>&#8211;read-pipe</code>=<i>command</i> or <code>-p</code> <i>command</i></p>
<dd> Examine input piped in from the <i>command</i>.</p>
<dt><code>&#8211;examine</code>=<i>filename</i> or <code>-f</code> <i>filename</i></p>
<dd> Use <i>filename</i> as the file to examine. <code>Swatch</code> will do a single pass through the named file.</dl>
<p> The following options are purely for debugging purposes, but are documented here for completeness:</p>
<dl>
<dt><code>&#8211;debug</code>[=<i>level</i>]</p>
<dd> Spew out various levels of debugging for swatch developers.</p>
<dt><code>&#8211;dump-script</code>[=<i>filename</i>]</p>
<dd> Instead of running the watcher script after it is generated, it is written to <i>filename</i> or to <font SIZE="-1">STDOUT.</font></dl>
<p> If swatch is called with no options, it is the same as typing the command line </p>
<pre>
        swatch --config-file=~/.swatchrc --tail-file=/var/log/syslog
</pre>
<p> or if /var/log/messages exists </p>
<pre>
        swatch --config-file=~/.swatchrc --tail-file=/var/log/messages
</pre>
<h2>THE CONFIGURATION FILE</h2>
<p> The configuration file is used by the <a href="/docs/linux/man/8-swatch/">swatch</a><code>(8)</code> program to determine what types of expression patterns to look for and what type of action(s) should be taken when a pattern is matched. </p>
<p> Each line should contain a keyword and a, sometimes optional, value for that keyword. The keyword and value are separated by a space or an equal (=) sign. </p>
<p> watchfor regex </p>
<p> ignore regex</p>
<dl>
<dt><code>echo [modes]</code></p>
<dd> Echo the matched line. The text mode may be <i>normal</i>, <i>bold</i>, <i>underscore</i>, <i>blink</i>, <i>inverse</i>, <i>black</i>, <i>red</i>, <i>green</i>, <i>yellow</i>, <i>blue</i>, <i>magenta</i>, <i>cyan</i>, <i>white</i>, <i>black_h</i>, <i>red_h</i>, <i>green_h</i>, <i>yellow_h</i>, <i>blue_h</i>, <i>magenta_h</i>, <i>cyan_h</i>, and/or <i>white_h</i>. The <i>_h</i> colors specify a highlighting color. The other colors are assigned to the letters. Some modes may not work on some terminals. <code>Normal</code> is the default.</p>
<dt><code>bell [N]</code></p>
<dd> Echo the matched line, and send a bell <i>N</i> times (default = 1).</p>
<dt><code>exec command</code></p>
<dd> Execute <i>command</i>. The <i>command</i> may contain variables which are substituted with fields from the matched line. A <i></i>$N<i></i> will be replaced by the <i>Nth</i> field in the line. A <i></i>$0<i></i> or <i>$*</i> will be replaced by the entire line.</p>
<dt><code>mail [addresses=address:address:&#8230;][,subject=your_text_here]</code></p>
<dd> Send <i>mail</i> to <i>address(es)</i> containing the matched lines as they appear (default address is the user who is running the program).</p>
<dt><code>pipe command[,keep_open]</code></p>
<dd> Pipe matched lines into <i>command</i>. Use the <code>keep_open</code> option to force the pipe to stay open until a different pipe action is run or until swatch exits.</p>
<dt><code>write [user:user:&#8230;]</code></p>
<dd> Use <a href="/docs/linux/man/1-write/">write</a><code>(1)</code> to send matched lines to <i>user(s)</i>.</p>
<dt><code>throttle hours:minutes:seconds,[key=message|regex|&lt;regexE</code>]&gt;</p>
<dd> This action has been depreciated. Use <code>threshold</code> instead For example,</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> throttle 15:00,key=&#8220;foo&#8221;</dl>
</dl>
<dl>
<dt>
<dd>
<p> would look like this </p>
<dl>
<dt>
<dd> threshold track_by=&#8220;foo&#8221;,type=limit,count=1,seconds=900</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>threshold track_by=key, type=&lt;limit|threshold|both</code>, count=number, seconds=number&gt;</p>
<dd> Thresholding can be done for the complete <code>watchfor</code> block and/or for individual actions. Add &#8220;threshold=on&#8221; as an option along with the other threshold options when thresholding an individual action.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>track_by</code></p>
<dd> The value of this should be something that is unique to the <code>watchfor</code> regular expression. Tip: enclose unique parts of the regular expression in parentheses, then use the sub matches as part of the value (e.g. track_by=&#8220;$2:$4&#8221;).</p>
<dt><code>type</code></p>
<dd> There are three types of thresholding. They are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>limit</code></p>
<dd> Perform action(s) for the first &quot;<code>count</code>&#8220; matches during the time interval specified by &#8221;<code>seconds</code>&quot;, then ignore events for the rest of the time interval (kind of like throttle)</p>
<dt><code>threshold</code></p>
<dd> Perform action(s) on each match for up to <code>count</code> matches during the time interval specified by <code>seconds</code></p>
<dt><code>both</code></p>
<dd> Perform actions(s) once per time interval after &quot;<code>count</code>&#8220; matches occur, then ignore additional matches during the time interval specified by &#8221;<code>seconds</code>&quot;</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>continue</code></p>
<dd> Use this action to cause <code>swatch</code> to continue to try to match other pattern/action groups after it is done with the current pattern/action block.</p>
<dt><code>quit</code></p>
<dd> Use this action to cause <code>swatch</code> to clean up and quit immediately.</dl>
<h2>SPECIAL OPTION</h2>
<p> The following may be used as an option for any of the above actions except for throttle and threshold.</p>
<dl>
<dt><code>when=</code><i>day_of_week:hour_of_day</i></p>
<dd> Use this option to specify windows of time and days when the action can be performed. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> mail=sysad-pager [at] somehost.somedomain,when=1-6:8-17</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>FOR PERL HACKS ONLY</h2>
<dl>
<dt><code>perlcode</code> [<i>depth</i>] arbitrary_Perl_code</p>
<dd> This permits you to easily insert random Perl code into your swatchrc file. The optional depth value tells swatch how deep into the code to put the perl code. (0=outside the main loop, 1=inside the main loop (default), 2=just inside the conditional used by the current watchfor statement, and 3=inside the throttle block). </p>
<p> Its intended use is to permit variable substitution. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> perlcode <tt>$syslog</tt>=&#8220;^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}.*&#8221;; </p>
<p> watchfor /$syslog hostname pppd/&gt;</dl>
</dl>
<dl>
<dt>
<dd>
<p> but any valid Perl is permitted. Remember the semicolon, and make judicious use of the <code>&#8211;dump-script</code> option if you run into trouble.</dl>
</dl>
<h2>CONFIGURATION EXAMPLE</h2>
<dl>
<dt>
<dd> perlcode my <tt>$fsf_regex</tt> = &#8216;\d{2}:\d{2}:\d{2}\s+(.* file system full)&#8217;; </p>
<p> watchfor /$fsf_regex/<br />
&nbsp;<wbr>threshold track_by=$1,type=limit,count=1,seconds=60<br />
&nbsp;<wbr>echo<br />
&nbsp;<wbr>bell</dl>
<p> In this example, a line which contains the string &#8220;file system full&#8221; will be echoed and the screen bell will sound. Also, <code>threshold</code> will use what is matched within the parentheses as its key rather than trying to use the log message with its time stamp cut out. Multiple instances of the message will not be echoed if they appear within a minute of the first one. Instead the following message will be acted upon after the time interval has expired.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-signal/">signal</a><code>(3)</code>, <a href="/docs/linux/man/1-perl/">perl</a><code>(1)</code>, <a href="/docs/linux/man/1-perlre/">perlre</a><code>(1)</code></p>
<h2>NOTES</h2>
<p> Upon receiving an <font SIZE="-1">ALRM</font> or <font SIZE="-1">HUP</font> signal swatch will re-read the configuration file and restart, except when used with the <i>&#8211;daemon</i> command line option where it will simply exit. Swatch will terminate gracefully when it receives a <font SIZE="-1">QUIT, TERM,</font> or <font SIZE="-1">INT</font> signal.</p>
<h2>AUTHOR</h2>
<pre>
    E. Todd Atkins
    Todd.Atkins [at] StanfordAlumni.ORG
</pre>
<h2>AVAILABILITY</h2>
<p> Swatch is a SourceForge project whose project page is at <a rel="nofollow" href="http://sourceforge.net/projects/swatch">http://sourceforge.net/projects/swatch</a> and homepage is at <a rel="nofollow" href="http://swatch.sourceforge.net">http://swatch.sourceforge.net</a> </p>
<h2>Index</h2>
