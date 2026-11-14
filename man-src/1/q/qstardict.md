---
title: "qstardict(1)"
name: "qstardict"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qstardict/"
description: "qstardict – a Qt4 dictionary"
---

<h2>NAME</h2>
<p> <code>qstardict</code> &#8211; a Qt4 dictionary</p>
<h2>DESCRIPTION</h2>
<p> <code>QStarDict</code> is a StarDict clone written with Qt4. The user interface is similar to StarDict. You can start QStarDict from the menu or by running the <code>qstardict</code> command.</p>
<h2>TRANSLATION REFORMATTING AND ABBREVIATION EXPANSION</h2>
<p> QStarDict can reformat translations and expand dictionary abbreviations. For example this translation: </p>
<pre>
1&gt; First _val. of _w. 2&gt; Second _val. of _w. ...
can be shown as
1. Fist value of word
2. Second value of word
3. ...
But reformatting and expanding takes additional CPU time. If the translation reformatting and instant search are both turned on this can decrease QStarDict performance.
</pre>
<h2>DICTIONARIES</h2>
<p> Dictionaries for StarDict plugin are in <code>StarDict</code> format and by default must be placed into /usr/share/stardict/dic or ~/.stardict/dic directories. A dictionary must consist of three files: </p>
<p>&nbsp;<wbr>&#8211; .dict[.dz]&nbsp;<wbr>file &#8211; main dictionary file<br />
&nbsp;<wbr>&#8211; .idx &#8211; index file<br />
&nbsp;<wbr>&#8211; .ifo &#8211; description file </p>
<p> These files must be placed together in one directory.</p>
<h2>PRONOUNCING PROGRAMS</h2>
<p> QStarDict can pronounce words using external program when popup window is shown. You must set a voice program to pronounce text from stdin. By default this is <code>festival</code> with <code>&#8211;tts</code> option.</p>
<h2>D-BUS</h2>
<p> QStarDict supports D-Bus message bus. List of available methods: </p>
<p> <code>void org.qstardict.dbus.showPopup(QString text</code><i>)</i><br />
 <code>void org.qstardict.dbus.showTranslation(QString text</code><i>)</i><br />
 <code>QString org.qstardict.dbus.translate(QString text</code><i>)</i><br />
 <code>QString org.qstardict.dbus.translateHtml(QString text</code><i>)</i><br />
 <code>QDBusVariant org.freedesktop.DBus.Properties.Get(QString interface_name</code><i>, QString property_name</i><code>)</code><br />
 <code>void org.freedesktop.DBus.Properties.Set(QString interface_name</code><i>, QString property_name</i><code>, QDBusVariant value</code><i>)</i><br />
 <code>QString org.freedesktop.DBus.Introspectable.Introspect()</code> </p>
<p> List of available properties: </p>
<p> <code>readwrite int org.qstardict.dbus.mainWindowVisible</code> </p>
<p> You can call these methods from your applications or by using the <code>qdbus</code> program. This command </p>
<pre>
qdbus org.qstardict.dbus&nbsp;<wbr>/qstardict org.qstardict.dbus.showPopup&nbsp;<wbr>&quot;text&quot;
will show a QStarDict popup window with a translation of the &quot;text&quot;.
If you want to show/hide QStarDict window using keyboard shortcuts you must bind the following command to a shortcut:
qdbus org.qstardict.dbus&nbsp;<wbr>/qstardict org.freedesktop.DBus.Properties.Set&nbsp;<wbr>\
<br>
org.qstardict.dbus mainWindowVisible&nbsp;<wbr>\
<br>
$(( ! $(qdbus org.qstardict.dbus&nbsp;<wbr>/qstardict&nbsp;<wbr>\
<br>
org.freedesktop.DBus.Properties.Get org.qstardict.dbus mainWindowVisible)))
</pre>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="http://qstardict.ylsoftware.com">http://qstardict.ylsoftware.com</a> laURL: L raQStarDict website</p>
<h2>AUTHOR</h2>
<p> <code>QStarDict</code> was written by Alexander Rodin &lt;rodin.alexander [at] gmail.com&gt;. </p>
<p> This manual page was written by Alexander Rodin &lt;rodin.alexander [at] gmail.com&gt;, for the Debian project (but may be used by others). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-stardict/">stardict</a>(1)</code> <code><a href="/docs/linux/man/1-sdcv/">sdcv</a>(1)</code> <code><a href="/docs/linux/man/1-qdbus/">qdbus</a>(1)</code> </p>
<h2>Index</h2>
