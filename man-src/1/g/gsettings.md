---
title: "gsettings(1)"
name: "gsettings"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsettings/"
description: "gsettings – GSettings configuration tool"
---

<h2 class="name">NAME</h2>
<p> gsettings &#8211; GSettings configuration tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gsettings</code> get <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i></dt>
<dt> <code>gsettings</code> monitor <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] [<i>KEY</i>]</dt>
<dt> <code>gsettings</code> writable <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i></dt>
<dt> <code>gsettings</code> range <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i></dt>
<dt> <code>gsettings</code> describe <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i></dt>
<dt> <code>gsettings</code> set <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i> <i>VALUE</i></dt>
<dt> <code>gsettings</code> reset <i>SCHEMA</i>&nbsp;[:<i>PATH</i>] <i>KEY</i></dt>
<dt> <code>gsettings</code> reset-recursively <i>SCHEMA</i>&nbsp;[:<i>PATH</i>]</dt>
<dt> <code>gsettings</code> list-schemas [&#8211;print-paths]</dt>
<dt> <code>gsettings</code> list-relocatable-schemas</dt>
<dt> <code>gsettings</code> list-keys <i>SCHEMA</i>&nbsp;[:<i>PATH</i>]</dt>
<dt> <code>gsettings</code> list-children <i>SCHEMA</i>&nbsp;[:<i>PATH</i>]</dt>
<dt> <code>gsettings</code> list-recursively [<i>SCHEMA</i>&nbsp;[:<i>PATH</i>]]</dt>
<dt> <code>gsettings</code> help [<i>COMMAND</i>]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gsettings</code></p>
<dd>offers a simple commandline interface to <code>GSettings</code>. It lets you get, set or monitor an individual key for changes. </dd>
<p> The <i>SCHEMA</i> and <i>KEY</i> arguments are required for most commands to specify the schema id and the name of the key to operate on. The schema id may optionally have a :<i>PATH</i> suffix. Specifying the path is only needed if the schema does not have a fixed path. </p>
<p> When setting a key, you also need specify a <i>VALUE</i> The format for the value is that of a serialized <code>GVariant</code>, so e.g. a string must include explicit quotes: &quot;&#8217;foo&#8217;&quot;. This format is also used when printing out values. </p>
<p> Note that gsettings needs a D-Bus session bus connection to write changes to the dconf database.</p>
<h2>COMMANDS</h2>
<p> <code>get</code></p>
<dl>
<dt>
</dt><dd> Gets the value of <i>KEY</i>. The value is printed out as a serialized <code>GVariant</code>.</dd></dl>
<p> <code>monitor</code></p>
<dl>
<dt>
</dt><dd> Monitors <i>KEY</i> for changes and prints the changed values. If no <i>KEY</i> is specified, all keys in the schema are monitored. Monitoring will continue until the process is terminated.</dd></dl>
<p> <code>writable</code></p>
<dl>
<dt>
</dt><dd> Finds out whether <i>KEY</i> is writable.</dd></dl>
<p> <code>range</code></p>
<dl>
<dt>
</dt><dd> Queries the range of valid values for <i>KEY</i>.</dd></dl>
<p> <code>describe</code></p>
<dl>
<dt>
</dt><dd> Queries the description of valid values for <i>KEY</i>.</dd></dl>
<p> <code>set</code></p>
<dl>
<dt>
</dt><dd> Sets the value of <i>KEY</i> to <i>VALUE</i>. The value is specified as a serialized <code>GVariant</code>.</dd></dl>
<p> <code>reset</code></p>
<dl>
<dt>
</dt><dd> Resets <i>KEY</i> to its default value.</dd></dl>
<p> <code>reset-recursively</code></p>
<dl>
<dt>
</dt><dd> Reset all keys under the given <i>SCHEMA</i>.</dd></dl>
<p> <code>list-schemas</code></p>
<dl>
<dt>
</dt><dd> Lists the installed, non-relocatable schemas. See <code>list-relocatable-schemas</code> if you are interested in relocatable schemas. If [<code>&#8211;print-paths</code>] is given, the path where each schema is mapped is also printed.</dd></dl>
<p> <code>list-relocatable-schemas</code></p>
<dl>
<dt>
</dt><dd> Lists the installed, relocatable schemas. See <code>list-schemas</code> if you are interested in non-relocatable schemas.</dd></dl>
<p> <code>list-keys</code></p>
<dl>
<dt>
</dt><dd> Lists the keys in <i>SCHEMA</i>.</dd></dl>
<p> <code>list-children</code></p>
<dl>
<dt>
</dt><dd> Lists the children of <i>SCHEMA</i>.</dd></dl>
<p> <code>list-recursively</code></p>
<dl>
<dt>
</dt><dd> Lists keys and values, recursively. If no <i>SCHEMA</i> is given, list keys in all schemas.</dd></dl>
<p> <code>help</code></p>
<dl>
<dt>
</dt><dd> Prints help and exits.</dd></dl>
<h2>Index</h2>
