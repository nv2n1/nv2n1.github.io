---

title: "xdg-mime(1)"
name: "xdg-mime"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-mime/"
description: "xdg-mime – command line tool for querying information about file type handling and adding descriptions for new file types"
---

<p> xdg-mime &#8211; command line tool for querying information about file type handling and adding descriptions for new file types </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-mime</code> query {filetype | default} &#8230;</dt>
<dt> <code>xdg-mime</code> default <i>application</i> <i>mimetype(s)</i></dt>
<dt> <code>xdg-mime</code> install [<code>&#8211;mode&nbsp;</code><i>mode</i>] [<code>&#8211;novendor</code>] <i>mimetypes-file</i></dt>
<dt> <code>xdg-mime</code> uninstall [<code>&#8211;mode&nbsp;</code><i>mode</i>] <i>mimetypes-file</i></dt>
<dt> <code>xdg-mime</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dt></dl>
<h2>DESCRIPTION</h2>
<dd>The xdg-mime program can be used to query information about file types and to add descriptions for new file types.</dd>
<h2>COMMANDS</h2>
<p> query</p>
<dl>
<dt>
</dt><dd> Returns information related to file types. </dd>
<p> The <i>query</i> option is for use inside a desktop session only. It is not recommended to use xdg-mime query as root. </p>
<p> The following queries are supported: </p>
<p> query filetype <i>FILE</i>: Returns the file type of <i>FILE</i> in the form of a MIME type. </p>
<p> query default <i>mimetype</i>: Returns the default application that the desktop environment uses for opening files of type <i>mimetype</i>. The default application is identified by its *.desktop file.</dl>
<p> default</p>
<dl>
<dt>
</dt><dd> Ask the desktop environment to make <i>application</i> the default application for opening files of type <i>mimetype</i>. An application can be made the default for several file types by specifying multiple mimetypes. </dd>
<p> <i>application</i> is the desktop file id of the application and has the form vendor-name.desktop. <i>application</i> must already be installed in the desktop menu before it can be made the default handler. The application&#8217;s desktop file must list support for all the MIME types that it wishes to be the default handler for. </p>
<p> Requests to make an application a default handler may be subject to system policy or approval by the end-user. xdg-mime query can be used to verify whether an application is the actual default handler for a specific file type. </p>
<p> The <i>default</i> option is for use inside a desktop session only. It is not recommended to use xdg-mime default as root.</dl>
<p> install</p>
<dl>
<dt>
</dt><dd> Adds the file type descriptions provided in <i>mimetypes-file</i> to the desktop environment. <i>mimetypes-file</i> must be a XML file that follows the freedesktop.org Shared MIME-info Database specification and that has a mime-info element as its document root. For each new file type one or more icons with name <i>type</i>&#8211;<i>subtype</i> must be installed with the <code>xdg-icon-resource</code> command in the <i>mimetypes</i> context. For example the filetype application/vnd.oasis.opendocument.text requires an icon named application-vnd.oasis.opendocument.text to be installed (unless the file type recommends another icon name).</dd></dl>
<p> uninstall</p>
<dl>
<dt>
</dt><dd> Removes the file type descriptions provided in <i>mimetypes-file</i> and previously added with <code>xdg-mime install</code> from the desktop environment. <i>mimetypes-file</i> must be a XML file that follows the freedesktop.org Shared MIME-info Database specification and that has a mime-info element as its document root.</dd></dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;mode</code> <i>mode</i></p>
<dl>
<dt>
</dt><dd> <i>mode</i> can be <i>user</i> or <i>system</i>. In user mode the file is (un)installed for the current user only. In system mode the file is (un)installed for all users on the system. Usually only root is allowed to install in system mode. </dd>
<p> The default is to use system mode when called by root and to use user mode when called by a non-root user.</dl>
<p> <code>&#8211;novendor</code></p>
<dl>
<dt>
</dt><dd> Normally, xdg-mime checks to ensure that the <i>mimetypes-file</i> to be installed has a proper vendor prefix. This option can be used to disable that check. </dd>
<p> A vendor prefix consists of alpha characters ([a-zA-Z]) and is terminated with a dash (&quot;-&quot;). Companies and organizations are encouraged to use a word or phrase, preferably the organizations name, for which they hold a trademark as their vendor prefix. The purpose of the vendor prefix is to prevent name conflicts.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show command synopsis.</dd></dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
</dt><dd> Show this manual page.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show the xdg-utils version information.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> xdg-mime honours the following environment variables: </p>
<p> XDG_UTILS_DEBUG_LEVEL</p>
<dl>
<dt>
</dt><dd> Setting this environment variable to a non-zero numerical value makes xdg-mime do more verbose reporting on stderr. Setting a higher value increases the verbosity.</dd></dl>
<p> XDG_UTILS_INSTALL_MODE</p>
<dl>
<dt>
</dt><dd> This environment variable can be used by the user or administrator to override the installation mode. Valid values are <i>user</i> and <i>system</i>.</dd></dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
</dt><dd> Error in command line syntax.</dd></dl>
<p> <code>2</code></p>
<dl>
<dt>
</dt><dd> One of the files passed on the command line did not exist.</dd></dl>
<p> <code>3</code></p>
<dl>
<dt>
</dt><dd> A required tool could not be found.</dd></dl>
<p> <code>4</code></p>
<dl>
<dt>
</dt><dd> The action failed.</dd></dl>
<p> <code>5</code></p>
<dl>
<dt>
</dt><dd> No permission to read one of the files passed on the command line.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-icon-resource/">xdg-icon-resource</a></code>(1), <code><a href="/docs/linux/man/1-xdg-desktop-menu/">xdg-desktop-menu</a></code>(1), m[blue]<code>Shared MIME database specification</code>m[][1], m[blue]<code>MIME applications associations specification</code>m[][2]</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd>
<pre>
xdg-mime query filetype /tmp/foobar.png
</pre>
</dd></dl>
<p> Prints the MIME type of the file /tmp/foobar.png, in this case image/png </p>
<dl>
<dt>
</dt><dd>
<pre>
xdg-mime query default image/png
</pre>
</dd></dl>
<p> Prints the .desktop filename of the application which is registered to open PNG files. </p>
<dl>
<dt>
</dt><dd>
<pre>
xdg-mime install shinythings-shiny.xml
</pre>
</dd></dl>
<p> Adds a file type description for &quot;shiny&quot;-files. &quot;shinythings-&quot; is used as the vendor prefix. The file type description could look as follows. </p>
<dl>
<dt>
</dt><dd>
<pre>
shinythings-shiny.xml:
&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;mime-info xmlns='<a rel="nofollow" href="http://www.freedesktop.org/standards/shared-mime-info'">http://www.freedesktop.org/standards/shared-mime-info'</a>&gt;
  &lt;mime-type type=&quot;text/x-shiny&quot;&gt;
    &lt;comment&gt;Shiny new file type&lt;/comment&gt;
    &lt;glob pattern=&quot;*.shiny&quot;/&gt;
    &lt;glob pattern=&quot;*.shi&quot;/&gt;
  &lt;/mime-type&gt;
&lt;/mime-info&gt;
</pre>
</dd></dl>
<p> An icon for this new file type must also be installed, for example with: </p>
<dl>
<dt>
</dt><dd>
<pre>
xdg-icon-resource install --context mimetypes --size 64 shiny-file-icon.png text-x-shiny
</pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> <code>Kevin Krammer</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Jeremy White</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> Shared MIME database specification</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/shared-mime-info-spec/">http://www.freedesktop.org/wiki/Specifications/shared-mime-info-spec/</a></dd></dl>
<dt> 2.</dt>
<dd> MIME applications associations specification</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/">http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/</a></dd></dl>
</dl>
