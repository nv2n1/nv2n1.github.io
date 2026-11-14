---
title: "ts(1)"
name: "ts"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ts/"
description: "ts – timestamp input"
---

<h2 class="name">NAME</h2>
<p> ts &#8211; timestamp input </p>
<h2>SYNOPSIS</h2>
<p> ts [-r] [-i | -s] [-m] [format]</p>
<h2>DESCRIPTION</h2>
<p> ts adds a timestamp to the beginning of each line of input. </p>
<p> The optional format parameter controls how the timestamp is formatted, as used by <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). The default format is &#8220;%b <tt>%d</tt> <tt>%H:</tt>%M:%S&#8221;. In addition to the regular strftime conversion specifications, &#8220;%.S&#8221; and &#8220;%.s&#8221; and &#8220;%.T&#8221; are like &#8220;%S&#8221; and &#8220;%s&#8221; and &#8220;%T&#8221;, but provide subsecond resolution (ie, &#8220;30.00001&#8221; and &#8220;1301682593.00001&#8221; and &#8220;1:15:30.00001&#8221;). </p>
<p> If the -r switch is passed, it instead converts existing timestamps in the input to relative times, such as &#8220;15m5s ago&#8221;. Many common timestamp formats are supported. Note that the Time::Duration and Date::Parse perl modules are required for this mode to work. Currently, converting localized dates is not supported. </p>
<p> If both -r and a format is passed, the existing timestamps are converted to the specified format. </p>
<p> If the -i or -s switch is passed, ts reports incremental timestamps instead of absolute ones. The default format changes to &#8220;%H:%M:%S&#8221;, and &#8220;%.S&#8221; and &#8220;%.s&#8221; can be used as well. In case of -i, every timestamp will be the time elapsed since the last timestamp. In case of -s, the time elapsed since start of the program is used. </p>
<p> The -m switch makes the system&#8217;s monotonic clock be used.</p>
<h2>ENVIRONMENT</h2>
<p> The standard <font SIZE="-1">TZ</font> environment variable controls what time zone dates are assumed to be in, if a timezone is not specified as part of the date.</p>
<h2>AUTHOR</h2>
<p> Copyright 2006 by Joey Hess &lt;id [at] joeyh.name&gt; </p>
<p> Licensed under the <font SIZE="-1">GNU GPL.</font> </p>
<h2>Index</h2>
