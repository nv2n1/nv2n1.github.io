---
title: "ifm(1)"
name: "ifm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifm/"
description: "IFM – Interactive Fiction Mapper"
---

<h2>NAME</h2>
<p> IFM &#8211; Interactive Fiction Mapper</p>
<h2>SYNOPSIS</h2>
<p> <code>ifm</code> [<i>options</i>] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> IFM is a program for keeping track of your progress through an Interactive Fiction game. You can record each room you visit and its relation to other rooms, the initial locations of useful items you find, and the tasks you need to perform in order to solve the game. </p>
<p> The IFM mapping commands are designed so that you can easily add to the map as you explore the game. You type in the rooms you visit and the directions you move in to reach other rooms, and IFM calculates the position of each room relative to the others. A map can consist of several independent sections, allowing you to divide up the map however you like. </p>
<p> The IFM task commands, if used, allow you to specify the order in which game-solving tasks must be done. The IFM program can then calculate and print different styles of walkthrough for the game. </p>
<p> IFM can write hardcopy maps directly to PostScript, suitable for printing or viewing. It can also write maps in Fig format, which can be viewed and edited using Xfig, or converted into many other formats. </p>
<p> This man page just presents a summary of the command-line options. Detailed documentation on how to use IFM can be found in the in the <code>SEE ALSO</code> section.</p>
<h3>Output options:</h3>
<dl>
<dt><code>-m</code>, <code>-map</code>[=<i>sections</i>]</dt>
<dd> Select map output</dd>
<dt><code>-i</code>, <code>-items</code></dt>
<dd> Select item output</dd>
<dt><code>-t</code>, <code>-tasks</code></dt>
<dd> Select task output</dd>
<dt><code>-f</code>, <code>-format</code> &lt;fmt&gt;</dt>
<dd> Select output format</dd>
<dt><code>-o</code>, <code>-output</code> &lt;file&gt;</dt>
<dd> Write output to file</dd></dl>
<h3>Auxiliary options:</h3>
<dl>
<dt><code>-S</code>, <code>-style</code> (name)</dt>
<dd> Push a style onto the style list</dd>
<dt><code>-s</code>, <code>-set</code> (var=val)</dt>
<dd> Set a customization variable</dd>
<dt><code>-w</code>, <code>-nowarn</code></dt>
<dd> Don&#8217;t print warnings</dd>
<dt><code>-noinit</code></dt>
<dd> Don&#8217;t read personal init file</dd></dl>
<h3>Preprocessor options:</h3>
<dl>
<dt><code>-D</code> (var[=val])</dt>
<dd> Define a preprocessor symbol</dd>
<dt><code>-I</code> (dir)</dt>
<dd> Prepend directory to search path</dd>
<dt><code>-P</code></dt>
<dd> Just preprocess input</dd></dl>
<h3>Information options:</h3>
<dl>
<dt><code>-show</code> &lt;type&gt;</dt>
<dd> Show information</dd>
<dt><code>-v</code>, <code>-version</code></dt>
<dd> Print program version</dd>
<dt><code>-h</code>, <code>-help</code></dt>
<dd> This help message</dd></dl>
<h3>Output formats (may be abbreviated):</h3>
<dl>
<dt>ps</dt>
<dd> PostScript</dd>
<dt>fig</dt>
<dd> Fig drawing commands</dd>
<dt>text</dt>
<dd> Nicely-formatted ASCII text</dd>
<dt>rec</dt>
<dd> Recording of game commands</dd>
<dt>dot</dt>
<dd> Graph of task dependencies</dd>
<dt>raw</dt>
<dd> Raw ASCII text fields</dd>
<dt>tk</dt>
<dd> Tcl/Tk program commands (tkifm)</dd></dl>
<h3>Show options (may be abbreviated):</h3>
<dl>
<dt>maps</dt>
<dd> Show map sections</dd>
<dt>vars</dt>
<dd> Show defined variables</dd>
<dt>path</dt>
<dd> Show file search path</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>IFMPATH</dt>
<dd> Colon-separated list of extra directories to search for include files.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.ifmrc</dt>
<dd> User resource file (ifm.ini on Windoze).</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; Glenn Hutchings &lt;zondo [at] pillock.freeserve.co.uk&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>/usr/share/doc/ifm-5.1/ifm</dt>
<dd> Online documentation</dd>
<dt>/usr/share/doc/ifm-5.1/ifm.pdf</dt>
<dd> Documentation suitable for printing </dd>
</dl>
