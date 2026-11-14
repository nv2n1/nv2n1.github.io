---
title: "drawtiming(1)"
name: "drawtiming"
section: "1"
letter: "d"
url: "/docs/linux/man/1-drawtiming/"
description: "drawtiming – generate timing diagram from signal description"
---

<h2>NAME</h2>
<p> <code>drawtiming</code> &#8211; generate timing diagram from signal description</p>
<h2>SYNOPSIS</h2>
<p> [-<code>-verbose</code> ] [-<code>-scale </code><i>factor</i> ] [-<code>-pagesize </code><i>WxH</i> ] [-<code>-aspect</code> ] [-<code>-cell-height </code><i>H</i> ] [-<code>-cell-width </code><i>W</i> ] [-<code>-font-size </code><i>pts</i> ] [-<code>-line-width </code><i>W</i> ] &#8211;<code>-output </code><i>target</i> <i>file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> This application provides a command line tool for documenting hardware and software designs through ideal timing diagrams. It reads signal descriptions from a text file with an intuitive syntax, and outputs an ideal timing diagram to an image file. Notation typical of timing diagrams found in the Electrical Engineering discipline is used, including arrows indicating causal relationships between signal transitions. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show usage reminder.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Increase diagnostic output.</p>
<dt><code>&#8211;scale </code><i>factor</i></p>
<dd> Scale the diagram by the given <i>factor</i> The default scaling factor is 1.0.</p>
<dt><code>&#8211;pagesize </code><i>WidthxHeight</i></p>
<dd> Scale the diagram to fit given image size.</p>
<dt><code>&#8211;aspect</code></p>
<dd> Maintain fixed aspect ratio if &#8211;pagesize given.</p>
<dt><code>&#8211;cell-height </code><i>H</i></p>
<dd> Height of the each signal in pixels. Default is 32.</p>
<dt><code>&#8211;cell-width </code><i>W</i></p>
<dd> Width for the time unit in pixels. Defaults is 64.</p>
<dt><code>&#8211;font-size </code><i>pts</i></p>
<dd> Font size in pts. Default is 18.</p>
<dt><code>&#8211;line-width </code><i>W</i></p>
<dd> Line width for drawings in pixels. Default is 1.</p>
<dt><code>&#8211;output </code><i>target</i></p>
<dd> The name and format of the output image is determined by <i>target</i></p>
<dt><i>file &#8230;</i></p>
<dd> The input files describe the signals to be diagrammed. See the Sx FILES and Sx EXAMPLES sections for a description of their format.</dl>
<h2>FILES</h2>
<p> The following is a technical description of the input file syntax and semantics. If you are reading this for the first time, you may want to skip ahead to the Sx EXAMPLES section. </p>
<p> The input file consists of a series of statements describing the signal transitions during each clock period of the timing diagram. Whitespace and comments following a `#&#8217; are ignored. </p>
<dl>
<dt><code>SIGNAL=VALUE</code></p>
<dd> This statement changes the value of a signal at the beginning of the current clock, and adds it to the list of signal dependencies. The signal name may consist of one or more words consisting of alphanumerics and underscores joined by periods, `signal.name&#8217; , for example. The signal value format is described further on.</p>
<dt><code>SIGNAL</code></p>
<dd> This statement adds a signal to the list of dependencies without changing its value.</dl>
<p> Statements are seperated by the following symbols:</p>
<dl>
<dt><code>,</code></p>
<dd> The comma seperator is used to seperate statements without affecting the dependency list or clock (ie: the next statement will add to the dependency list).</p>
<dt><code>;</code></p>
<dd> The semicolon seperator resets the list of dependencies without incrementing the clock</p>
<dt><code>.</code></p>
<dd> The period seperator resets the list of dependencies and increments the clock.</p>
<dt><code>=&gt;</code></p>
<dd> The &quot;causes&quot; seperator renders dependency arrows based on the current list of dependencies and then resets the dependency list.</p>
<dt><code>-tD&gt;</code></p>
<dd> The &quot;delay&quot; seperator renders a delay arrow from the last dependency with the annotation <i>tD</i></dl>
<p> Signal values are rendered according to the following rules:</p>
<dl>
<dt><code>0 , 1 , true , false</code></p>
<dd> A binary high/low signal.</p>
<dt><code>tick</code></p>
<dd> A clock pulse which repeats.</p>
<dt><code>pulse</code></p>
<dd> A one-shot clock pulse.</p>
<dt><code>X</code></p>
<dd> A don&#8217;t care value.</p>
<dt><code>Z</code></p>
<dd> A tristate value.</p>
<dt><code>Qq </code>ABC</p>
<dd> Any other alphanumeric token, or text enclosed in quotes is rendered as a state. For example, `Qq 1 &#8216; , is rendered as a state, whereas, `1&#8217; , is rendered as a high signal.</dl>
<h2>EXAMPLES</h2>
<p> Let&#8217;s look at an example input file, and parse its meaning. </p>
<blockquote>
<pre>
POWER=0, FIRE=0, ARMED=0, LED=OFF, COUNT=N.
POWER=1 =&gt; LED=GREEN.
FIRE=1. 
FIRE =&gt; ARMED=1.
FIRE=0.
FIRE=1.
FIRE, ARMED =&gt; LED=RED;
FIRE =&gt; COUNT=&quot;N+1&quot;.
</pre>
</blockquote>
<p> This input file descibes the changes in five signals over a period of seven clock cycles. The end of each clock cycle is indicated with a period. For example, the following line indicates a single signal, named `FIRE&#8217; became true during a clock cycle: </p>
<blockquote><p><tt>FIRE=1.</tt></p></blockquote>
<p> The first clock period of the input file provides the initial value for all signals to be diagrammed. The signals will appear on the timing diagram in the order they first appear in the input file. Signals are assumed to have the Qq don&#8217;t care value if their initial value is not given. </p>
<p> Independent signal transitions which occur simultaneously are normally seperated by commas. Since signals aren&#8217;t normally expected to change simultaneously, the initial state is a good example of this: </p>
<blockquote><p><tt>POWER=0, FIRE=0, ARMED=0, LED=OFF, COUNT=N.</tt></p></blockquote>
<p> Dependencies can also be indicated for a signal transition. Dependencies are rendered as arrows on the timing diagram from the last change in each dependency to the dependent signal transition. Here, the previous change in the state of `FIRE&#8217; causes a change in the `ARMED&#8217; signal. </p>
<blockquote><p><tt>FIRE =&gt; ARMED=1.</tt></p></blockquote>
<p> To indicate that a change in one signal causes an immediate change in another signal, list both signal changes in the same clock period: </p>
<blockquote><p><tt>POWER=1 =&gt; LED=GREEN.</tt></p></blockquote>
<p> For signal state changes with multiple dependencies, seperate the dependencies with commas: </p>
<blockquote><p><tt>FIRE, ARMED =&gt; LED=RED.</tt></p></blockquote>
<p> Sometimes, a single dependency causes multiple independent signals to change. Use a semicolon to start a new list of dependencies. Modifying the previous line to indicate that `FIRE&#8217; also causes `COUNT&#8217; to increment yields: </p>
<blockquote><p><tt>FIRE, ARMED =&gt; LED=RED;</tt></p></blockquote>
<blockquote><p><tt>FIRE =&gt; COUNT=&quot;N+1&quot;.</tt></p></blockquote>
<p> You can find this example and others along with their generated timing diagrams on the homepage for at `<a rel="nofollow" href="http://drawtiming.sourceforge.net'">http://drawtiming.sourceforge.net&#8217;</a></p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 on success, and 2 if the command fails.</p>
<h2>COMPATIBILITY</h2>
<p> The command has been tested on FreeBSD, Linux, and Cygwin.</p>
<h2>AUTHORS</h2>
<p> This software package was written by An Edward Counce Aq ecounce [at] users.sourceforge.net Additional modifications by An Salvador E. Tropea Aq set [at] users.sourceforge.net An Daniel Beer</p>
<h2>BUGS</h2>
<p> None reported. </p>
<h2>Index</h2>
