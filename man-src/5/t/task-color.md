---
title: "task-color(5)"
name: "task-color"
section: "5"
letter: "t"
url: "/docs/linux/man/5-task-color/"
description: "task-color – A color tutorial for the Taskwarrior command line todo manager."
---

<p>task-color &#8211; A color tutorial for the Taskwarrior command line todo manager.</p>
<h2>Setup</h2>
<p>The first thing you need is a terminal program that supports color. All terminal programs support color, but only a few support lots of colors. First tell your terminal program to use color by specifying the TERM environment variable like this: </p>
<p>&nbsp;<wbr>TERM=xterm-color </p>
<p> In this example, xterm-color is used &#8211; a common value, and one that doesn&#8217;t require that you use xterm. This works for most setups. This setting belongs in your shell profile (~/.bash_profile, ~/.bashrc, ~/.cshrc etc, depending on which shell you use). If this is a new setting, you will need to either run that profile script, or close and reopen the terminal window (which does the same thing). </p>
<p> Now tell Taskwarrior that you want to use color. This is the default for Taskwarrior, so the following step may be unnecessary. </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config color on </p>
<p> This command will make sure there is an entry in your ~/.taskrc file that looks like: </p>
<p>&nbsp;<wbr>color=on </p>
<p> Now Taskwarrior is ready.</p>
<h2>Automatic Monochrome</h2>
<p>It should be mentioned that Taskwarrior is aware of whether its output is going to a terminal, or to a file or through a pipe. When Taskwarrior output goes to a terminal, color is desirable, but consider the following command: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task list&nbsp;<wbr>&gt;&nbsp;<wbr>file.txt </p>
<p> Do we really want all those color control codes in the file? Taskwarrior assumes that you do not, and temporarily sets color to &#8216;off&#8217; while generating the output. This explains the output from the following command: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task show | grep&nbsp;<wbr>&#8216;^color&nbsp;<wbr>&#8216;<br />
&nbsp;<wbr>color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>off </p>
<p> it always returns &#8216;off&#8217;, no matter what the setting, because the output is being sent to a pipe. </p>
<p> If you wanted those color codes, you can override this behavior by setting the _forcecolor variable to on, like this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config&nbsp;<wbr>_forcecolor on<br />
&nbsp;<wbr>$&nbsp;<wbr>task config | grep&nbsp;<wbr>&#8216;^color&nbsp;<wbr>&#8216;<br />
&nbsp;<wbr>color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on </p>
<p> or by temporarily overriding it like this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task rc._forcecolor=on config | grep&nbsp;<wbr>&#8216;^color&nbsp;<wbr>&#8216;<br />
&nbsp;<wbr>color&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on</p>
<h2>Available Colors</h2>
<p>Taskwarrior has a &#8216;color&#8217; command that will show all the colors it is capable of displaying. Try this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task color </p>
<p> The output cannot be replicated here in a man page, but you should see a set of color samples. How many you see depends on your terminal program&#8217;s ability to render them. </p>
<p> You should at least see the Basic colors and Effects &#8211; if you do, then you have 16-color support. If your terminal supports 256 colors, you&#8217;ll know it!</p>
<h2>16-Color Support</h2>
<p>The basic color support is provided through named colors: </p>
<p>&nbsp;<wbr>black, red, blue, green, magenta, cyan, yellow, white </p>
<p> Foreground color (for text) is simply specified as one of the above colors, or not specified at all to use the default terminal text color. </p>
<p> Background color is specified by using the word &#8216;on&#8217;, and one of the above colors. Some examples: </p>
<p>&nbsp;<wbr>green&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>green text, default background color<br />
&nbsp;<wbr>green on yellow&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>green text, yellow background<br />
&nbsp;<wbr>on yellow&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>default text color, yellow background </p>
<p> These colors can be modified further, by making the foreground bold, or by making the background bright. Some examples: </p>
<p>&nbsp;<wbr>bold green<br />
&nbsp;<wbr>bold white on bright red<br />
&nbsp;<wbr>on bright cyan </p>
<p> The order of the words is not important, so the following are equivalent: </p>
<p>&nbsp;<wbr>bold green<br />
&nbsp;<wbr>green bold </p>
<p> But the &#8216;on&#8217; is important &#8211; colors before the &#8216;on&#8217; are foreground, and colors after &#8216;on&#8217; are background. </p>
<p> There is an additional &#8216;underline&#8217; attribute that may be used: </p>
<p>&nbsp;<wbr>underline bold red on black </p>
<p> And an &#8216;inverse&#8217; attribute: </p>
<p>&nbsp;<wbr>inverse red </p>
<p> Taskwarrior has a command that helps you visualize these color combinations. Try this: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task color underline bold red on black </p>
<p> You can use this command to see how the various color combinations work. You will also see some sample colors displayed, like the ones above, in addition to the sample requested. </p>
<p> Some combinations look very nice, some look terrible. Different terminal programs do implement slightly different versions of &#8216;red&#8217;, for example, so you may see some unexpected variation across machines. The brightness of your display is also a factor.</p>
<h2>256-Color Support</h2>
<p>Using 256 colors follows the same form, but the names are different, and some colors can be referenced in different ways. First there is by color ordinal, which is like this: </p>
<p>&nbsp;<wbr>color0<br />
&nbsp;<wbr>color1<br />
&nbsp;<wbr>color2<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>color255 </p>
<p> This gives you access to all 256 colors, but doesn&#8217;t help you much. This range is a combination of 8 basic colors (color0 &#8211; color7), then 8 brighter variations (color8 &#8211; color15). Then a block of 216 colors (color16 &#8211; color231). Then a block of 24 gray colors (color232 &#8211; color255). </p>
<p> The large block of 216 colors (6x6x6 = 216) represents a color cube, which can be addressed via RGB values from 0 to 5 for each component color. A value of 0 means none of this component color, and a value of 5 means the most intense component color. For example, a bright red is specified as: </p>
<p>&nbsp;<wbr>rgb500 </p>
<p> And a darker red would be: </p>
<p>&nbsp;<wbr>rgb300 </p>
<p> Note that the three digits represent the three component values, so in this example the 5, 0 and 0 represent red=5, green=0, blue=0. Combining intense red with no green and no blue yields red. Similarly, blue and green are: </p>
<p>&nbsp;<wbr>rgb005<br />
&nbsp;<wbr>rgb050 </p>
<p> Another example &#8211; bright yellow &#8211; is a mix of bright red and bright green, but no blue component, so bright yellow is addressed as: </p>
<p>&nbsp;<wbr>rgb550 </p>
<p> A soft pink would be addressed as: </p>
<p>&nbsp;<wbr>rgb515 </p>
<p> See if you agree, by running: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task color black on rgb515 </p>
<p> You may notice that the large color block is represented as 6 squares. All colors in the first square have a red value of 0. All colors in the 6th square have a red value of 5. Within each square, blue ranges from 0 to 5 left to right, and within each square green ranges from 0 to 5, top to bottom. This scheme takes some getting used to. </p>
<p> The block of 24 gray colors can also be accessed as gray0 &#8211; gray23, in a continuous ramp from black to white.</p>
<h2>Mixing 16- And 256-Colors</h2>
<p>If you specify 16-colors, and view on a 256-color terminal, no problem. If you try the reverse, specifying 256-colors and viewing on a 16-color terminal, you will be disappointed, perhaps even appalled. </p>
<p> There is some limited color mapping &#8211; for example, if you were to specify this combination: </p>
<p>&nbsp;<wbr>red on gray3 </p>
<p> you are mixing a 16-color and 256-color specification. Taskwarrior will map red to color1, and proceed. Note that red and color1 are not quite the same tone. </p>
<p> Note also that there is no bold or bright attributes when dealing with 256 colors, but there is still underline available.</p>
<h2>Legend</h2>
<p>Taskwarrior will show examples of all defined colors used in your .taskrc, or theme, if you run this command: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task color legend </p>
<p> This gives you an example of each of the colors, so you can see the effect, without necessarily creating a set of tasks that meet each of the rule criteria.</p>
<h2>Rules</h2>
<p>Taskwarrior supports colorization rules. These are configuration values that specify a color, and the conditions under which that color is used. By example, let us add a few tasks: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task add project:Home priority:H pay the bills&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(1)<br />
&nbsp;<wbr>$&nbsp;<wbr>task add project:Home&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>clean the rug&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(2)<br />
&nbsp;<wbr>$&nbsp;<wbr>task add project:Garden&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>clean out the garage&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(3) </p>
<p> We can add a color rule that uses a blue background for all tasks in the Home project: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config color.project.Home&nbsp;<wbr>&#8216;on blue&#8217; </p>
<p> We use quotes around &#8216;on blue&#8217; because there are two words, but they represent one value in the .taskrc file. Now suppose we wish to use a bold yellow text color for all cleaning work: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task config color.keyword.clean&nbsp;<wbr>&#8216;bold yellow&#8217; </p>
<p> Now what happens to task 2, which belongs to project Home (blue background), and is also a cleaning task (bold yellow foreground)? The colors are combined, and the task is shown as &quot;bold yellow on blue&quot;. </p>
<p> Color rules can be applied by project and description keyword, as shown, and also by priority (or lack of priority), by active status, by being due or overdue, by being tagged, or having a specific tag (perhaps the most useful rule) or by being a recurring task. </p>
<p> It is possible to create a very colorful mix of rules. With 256-color support, those colors can be made subtle, and complementary, but without care, this can be a visual mess. Beware! </p>
<p> In such cases, consider using the &#8216;rule.color.merge=no&#8217; option to disable the color blending. </p>
<p> The precedence for the color rules is determined by the configuration variable &#8216;rule.precedence.color&#8217;, which by default contains: </p>
<p>&nbsp;<wbr>deleted,completed,active,keyword.,tag.,project.,overdue,scheduled,due.today,due,blocked,blocking,recurring,tagged,uda. </p>
<p> These are just the color rules with the &#8216;color.&#8217; prefix removed. The rule &#8216;color.due.today&#8217; is the highest precedence, and &#8216;color.deleted&#8217; is the lowest. </p>
<p> The keyword rule shown here as &#8216;keyword.&#8217; corresponds to a wildcard pattern, meaning &#8216;color.keyword.*&#8217;, or in other words all the keyword rules. Similarly for the &#8216;color.tag.*&#8217; and &#8216;color.project.*&#8217; rules. </p>
<p> There is also &#8216;color.project.none&#8217;, &#8216;color.tag.none&#8217; and &#8216;color.pri.none&#8217; to specifically represent missing data.</p>
<h2>Themes</h2>
<p>Taskwarrior supports themes. What this really means is that with the ability to include other files into the .taskrc file, different sets of color rules can be included. </p>
<p> To get a good idea of what a color theme looks like, try adding this entry to your .taskrc file (note that your installation may use a slightly different path from the example): </p>
<dl>
<dd>include /usr/share/doc/task/rc/dark-256.theme</dl>
<p> You can use any of the standard Taskwarrior themes: </p>
<dl>
<dd>dark-16.theme<br />
 dark-256.theme<br />
 dark-blue-256.theme<br />
 dark-gray-256.theme<br />
 dark-green-256.theme<br />
 dark-red-256.theme<br />
 dark-violets-256.theme<br />
 dark-yellow-green.theme<br />
 light-16.theme<br />
 light-256.theme<br />
 solarized-dark-256.theme<br />
 solarized-light-256.theme<br />
 dark-default-16.theme<br />
 dark-gray-blue-256.theme<br />
 no-color.theme</dl>
<p> Bear in mind that if you are using a terminal with a dark background, you will see better results using a dark theme. </p>
<p> You can also see how the theme will color the various tasks with the command: </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>task color legend </p>
<p> Better yet, create your own, and share it. We will gladly host the theme file on &lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt;.</p>
<h2>CREDITS &amp; COPYRIGHTS</h2>
<p>Copyright (C) 2006 &#8211; 2016 P. Beckingham, F. Hernandez. </p>
<p> Taskwarrior is distributed under the MIT license. See <a rel="nofollow" href="http://www.opensource.org/licenses/mit-license.php">http://www.opensource.org/licenses/mit-license.php</a> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-task/">task</a>(1),</code> <code><a href="/docs/linux/man/5-taskrc/">taskrc</a>(5),</code> <code><a href="/docs/linux/man/5-task-sync/">task-sync</a>(5)</code> For more information regarding Taskwarrior, the following may be referenced:</p>
<dl>
<dt>The official site at</p>
<dd>&lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt;</p>
<dt>The official code repository at</p>
<dd>&lt;<a rel="nofollow" href="https://git.tasktools.org/scm/tm/task.git">https://git.tasktools.org/scm/tm/task.git</a>&gt;</p>
<dt>You can contact the project by writing an email to</p>
<dd>&lt;support [at] taskwarrior.org&gt; </p>
<h2>Reporting Bugs</h2>
<dl>
<dt>Bugs in Taskwarrior may be reported to the issue-tracker at</p>
<dd>&lt;<a rel="nofollow" href="http://taskwarrior.org">http://taskwarrior.org</a>&gt; </p>
</dl>
