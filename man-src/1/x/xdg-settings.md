---
title: "xdg-settings(1)"
name: "xdg-settings"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-settings/"
description: "xdg-settings – get various settings from the desktop environment"
---

<h2 class="name">NAME</h2>
<p> xdg-settings &#8211; get various settings from the desktop environment </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-settings</code> {<i>get</i> | <i>check</i> | <i>set</i>} {<code>property</code>} [<code>subproperty</code>] [<code>value</code>]</p>
<dt> <code>xdg-settings</code> {<code>&#8211;help</code> | <code>&#8211;list</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>xdg-settings gets various settings from the desktop environment. For instance, desktop environments often provide proxy configuration and default web browser settings. Using xdg-settings these parameters can be extracted for use by applications that do not use the desktop environment&#8217;s libraries (which would use the settings natively). </p>
<p> xdg-settings is for use inside a desktop session only. It is not recommended to use xdg-settings as root.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show command synopsis.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List all properties xdg-settings knows about.</dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
<dd> Show this manual page.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the xdg-utils version information.</dl>
<h2>PROPERTIES</h2>
<p> When using xdg-settings to get, check or set a desktop setting, properties and possibly sub-properties are used to specify the setting to be changed. </p>
<p> Some properties (such as default-web-browser) fully describe the setting to be changed. Other properties (such as default-url-scheme-handler) require more information (in this case the actual scheme to set the default handler for) which must be provided in a sub-property.</p>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Error in command line syntax.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> One of the files passed on the command line did not exist.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> A required tool could not be found.</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> The action failed.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-mime/">xdg-mime</a></code>(1), <code><a href="/docs/linux/man/1-xdg-open/">xdg-open</a></code>(1), m[blue]<code>MIME applications associations specification</code>m[]<font SIZE="-2">[1]</font></p>
<h2>EXAMPLES</h2>
<p> Get the desktop file name of the current default web browser </p>
<dl>
<dt>
<dd>
<pre>
        xdg-settings get default-web-browser
      
</pre>
</dl>
<p> Check whether the default web browser is firefox.desktop, which can be false even if &quot;get default-web-browser&quot; says that is the current value (if only some of the underlying settings actually reflect that value) </p>
<dl>
<dt>
<dd>
<pre>
        xdg-settings check default-web-browser firefox.desktop
      
</pre>
</dl>
<p> Set the default web browser to google-chrome.desktop </p>
<dl>
<dt>
<dd>
<pre>
        xdg-settings set default-web-browser google-chrome.desktop
      
</pre>
</dl>
<p> Set the default mailto URL scheme handler to be evolution.desktop </p>
<dl>
<dt>
<dd>
<pre>
        xdg-settings set default-url-scheme-handler mailto evolution.desktop
      
</pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>Mike Mammarella</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009-2011 </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> MIME applications associations specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/">http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/</a></dl>
</dl>
<h2>Index</h2>
