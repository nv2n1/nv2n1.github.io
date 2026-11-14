---
title: "isdnconf(1)"
name: "isdnconf"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isdnconf/"
description: "isdnconf – manipulate or read ISDN phone number config files."
---

<h2>NAME</h2>
<p> isdnconf &#8211; manipulate or read ISDN phone number config files. </p>
<h2>SYNOPSIS</h2>
<p> <code>isdnconf</code> </p>
<h2>DESCRIPTION</h2>
<p> <i>isdnconf</i> can manipulate or read the file <i>/etc/isdn/callerid.conf</i> as well as <i>~/.isdn</i>. Entries can be added or removed from these files. Additionally, entries can be searched for and displayed in a way similar to <code>grep</code>. An entry can be an own MSN (<code>[MSN]</code>) or a phone number (<code>[NUMBER]</code>). </p>
<p> You can use this program to build your own phonebook. These files are used by many of the other ISDN utilities that use phone numbers, to display a number symbolically instead of as a plain number. </p>
<h2>OPTIONS</h2>
<p> Note: use of the options -A and -D is dangerous! The complete structure of the file may be changed, and all comments are removed! Make backups of your data files before trying these. </p>
<p> <code>COMMAND OPTIONS:</code> </p>
<dl>
<dt><code>-A</code></p>
<dd> Add a new entry, which is read from standard input. The following values are asked for (shown here with examples):</p>
<dl>
<dt>
<dd>
<pre>
Alias:          Fred
Number:         0815/441777
SI:             0
Zone:           4
Interface:      -
Flags:          I|O
Program:        /usr/local/bin/ring
User:           uucp
Group:          user
Interval:
Time:           8-20
Flags:          (control-D here indicates end of flags)
Alias:          (control-D here indicates end of entries)
</pre>
<p> If you want another [Flags] entry, simply enter the data for another program for this number at the point where the control-D was given above. </p>
<p> If you want to add another number, simply enter the data for the next number at the Alias prompt. </p>
<p> You can also pipe the data into the program; the input data must correspond to the prompts that the program gives! Note that you can only add one number at a time then (there&#8217;s no way of telling <i>isdnconf</i> that you want to stop giving Flags info and start giving the next Alias info). </p>
</dl>
<dt><code>-D</code></p>
<dd> Delete one or more entries which match the data options given. How to supply the data to match is discussed below (see <code>DATA OPTIONS</code>). </p>
<dt><code>-V</code></p>
<dd> version: display the program&#8217;s version and terminate. </p>
</dl>
<p> If both -A and -D are given together, <i>isdnconf</i> will terminate, as this is not a valid combination. </p>
<p> If neither -A nor -D is given, then <i>isdnconf</i> will display entries which match the data given. </p>
<p> <code>DATA OPTIONS:</code> (not applicable for -A)</p>
<dl>
<dt><code>-n &#8216;number&#8217;</code></p>
<dd> number: match the given number. It can contain wildcards. </p>
<dt><code>-a &#8216;alias&#8217;</code></p>
<dd> alias: match the given alias name. The name can contain wildcards. Note: due to a bug, use &#8216;?&#8217; instead of &#8216;-&#8216;. </p>
<dt><code>-t &#8216;SI&#8217;</code></p>
<dd> SI: match the given service indicator. </p>
<dt><code>-c &#8216;code&#8217;</code></p>
<dd> code: match the area code of the phone number. Only usable for displaying (not for -A nor -D). </p>
<dt><code>-i</code></p>
<dd> ignore case for the -n and -a options. </p>
<dt><code>-w</code></p>
<dd> word: the parameters for -n and -a must match the <code>whole</code> value, not just a substring.</p>
<dl>
<dt>
<dd> Examples (here for -n): </p>
<pre>
&quot;*34*&quot; matches 123456, 345677, 1234
&quot;34*&quot;  matches 34567, 34111 but not 1234
&quot;34??&quot; matches 3411, 3456
&quot;34&quot;   matches only 34
</pre>
<p> Without the -w option, these would match: </p>
<pre>
&quot;*34*&quot; matches 123456, 345677, 1234
&quot;34*&quot;  matches 123456, 345677, 1234, 34567, 34111
&quot;34??&quot; matches 123456, 345677, 1234, 3411, 3456
&quot;34&quot;   matches 123456, 345677, 1234, 3411, 3456, 34567
</pre>
</dl>
<dt><code>-d</code></p>
<dd> and: by default the values given to options -n, -a and -t will be combined with a logical OR. If these should be combined with a logical AND (which is probably what most people expect!) you must use this -d option. In this case you can only supply each of the -n, -a and -t options exactly once. </p>
<dt><code>OTHER OPTIONS:</code></p>
<dd>
<dt><code>-q</code></p>
<dd> quiet: when using the -A or -D commands, the output is suppressed. When not using the -A or -D commands, only the alias of the matching number is shown, or just the number in case the alias is not found. </p>
<dt><code>-m</code></p>
<dd> MSN: when used in combination with the -A command, instructs <code>isdnconf</code> to create a new MSN entry; the default is to create a new NUMBER entry. Only the values alias, number, SI, zone and interface are applicable to an MSN entry. </p>
</dl>
<p> The following two options do not apply to the -A and -D commands. They only change the output format. </p>
<dl>
<dt><code>-s</code></p>
<dd> short: only display the alias and the number. </p>
<dt><code>-l</code></p>
<dd> long: also display the programs to run (<code>[START]</code>). </p>
<dt><code>-f &#8216;filename&#8217;</code></p>
<dd> file: usually <code>isdnconf</code> uses the <i>/etc/isdn/callerid.conf</i> and the <i>~/.isdn</i> files. If <code>isdnconf</code> should be applied to another file, use this option. </p>
<dt><code>-g</code></p>
<dd> global: only applies to the -A and -D commands. Instead of editing <i>~/.isdn</i>, <i>/etc/isdn/callerid.conf</i> is edited. </p>
<dt><code>-1</code></p>
<dd> first: only delete or display the first entry. </p>
<dt><code>-M</code></p>
<dd> isdnmon: used internally by isdnmon to get alias info. </p>
</dl>
<h2>AUTHOR</h2>
<p> Andreas Kool &lt;akool [at] isdn4linux.de&gt;<br />
 manpage adapted from the README by Paul Slootman &lt;paul [at] isdn4linux.de&gt; </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a></i>(5), <i><a href="/docs/linux/man/8-isdnlog/">isdnlog</a></i>(8) </p>
<h2>Index</h2>
