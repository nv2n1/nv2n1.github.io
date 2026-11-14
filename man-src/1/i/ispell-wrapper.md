---
title: "ispell-wrapper(1)"
name: "ispell-wrapper"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ispell-wrapper/"
description: "ispell-wrapper – smart wrapper for ispell"
---

<h2 class="name">NAME</h2>
<p> ispell-wrapper &#8211; smart wrapper for ispell </p>
<h2>SYNOPSIS</h2>
<pre><code>
ispell - wrapper[--emacs = name][--language = regexp][--dry - run][ispell options] file
         Options(all long only options)
    : --emacs = name Set the language to use by emacs dict name
    -- language = regexp Set the language to use by name
                  -- dry
                  - run Only show what would have done
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ispell-wrapper</code> is a wrapper script for ispell intended to be used in a Debian system in conjunction with the infrastructure introduced by the dictionaries-common package. Option &#8211;dry-run will show the string to be run without doing anything else. </p>
<p> It automatically sets the <code>-d</code>, <code>-w</code>, and <code>-T</code> options to ispell as a function of the chosen language. Of course, this only works for dictionary packages that comply with the above mentioned Policy. </p>
<p> Here is how the language is defined (in order of priority):</p>
<dl>
<dt>1)</p>
<dd> By matching the emacs dict name given in &#8211;emacs option to the name of one of the emacs dicts names provided by installed languages in the system. This match must be exact (although is case insensitive). Note that this will override any value given in the &#8211;language option.</p>
<dt>2)</p>
<dd> By matching the regexp given in option &#8211;language to the list of installed languages in the system.</p>
<dt>3)</p>
<dd> By matching the regexp stored in the environment variable <font SIZE="-1">ISPELLDEFAULT</font> to the list of installed languages in the system.</p>
<dt>4)</p>
<dd> By using the value stored in the user-specific file ~/.ispell-default (use <code><a href="/docs/linux/man/1-select-default-iwrap/">select-default-iwrap</a></code>(1) to set it).</p>
<dt>5)</p>
<dd> By using the value stored in the site-wide file /etc/dictionaries-common/ispell-default (use <code><a href="/docs/linux/man/8-select-default-ispell/">select-default-ispell</a></code>(8) as superuser to set it).</dl>
<p> Note: regexp matches are case-insensitive and the <font SIZE="-1">ISO-8859-1</font> special characters are transformed into their <font SIZE="-1">ASCII</font> equivalents. German ess-zet is equivalent to the character &#8220;s&#8221; and the ae ligature to the character &#8220;e&#8221;.</p>
<h2>EXAMPLE</h2>
<p> Let us say that the following dictionaries are installed in the system (as appearing in the Debconf question at installation time): </p>
<pre>
    castellano (Spanish TeX mode)
    castellano8 (Spanish 8 bit)
    portugu&ecirc;s (European Portuguese)
    portugu&ecirc;s brasileiro (Brazilian Portuguese)
</pre>
<p> Choosing the regexp (either in the &#8211;language option or in the environment variable <font SIZE="-1">ISPELLDEFAULT</font>) to be &#8220;span&#8221; will yield an error, since two languages will match (&#8220;castellano&#8221; and &#8220;castellano8&#8221;). However, if the regexp is &#8220;span.*8&#8221;, the language &#8220;castellano8 (Spanish 8 bit)&#8221; will be chosen.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">ISPELLDEFAULT</font></p>
<dd> Regexp that matches the name of the default language to use, if no &#8211;language option is given.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.ispell-default</p>
<dd> Contains the name of the language to use, if no &#8211;language option is given or if the <font SIZE="-1">ISPELLDEFAULT</font> environment variable is not set. This is a user-specific choice.</p>
<dt>/etc/dictionaries-common/ispell-default</p>
<dd> Name of the language to use when everything above is not set. This is a system-wide setting.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-select-default-ispell/">select-default-ispell</a></code>(8), <code><a href="/docs/linux/man/1-select-default-iwrap/">select-default-iwrap</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Rafael Laboissiere </p>
<h2>Index</h2>
