---
title: "debconf-devel(7)"
name: "debconf-devel"
section: "7"
letter: "d"
url: "/docs/linux/man/7-debconf-devel/"
description: "debconf – developers guide"
---

<p>debconf &#8211; developers guide</p>
<h2>Description</h2>
<p>This is a guide for developing packages that use debconf. </p>
<p> This manual assumes that you are familiar with debconf as a user, and are familiar with the basics of debian package construction. </p>
<p> This manual begins by explaining two new files that are added to debian packages that use debconf. Then it explains how the debconf protocol works, and points you at some libraries that will let your programs speak the protocol. It discusses other maintainer scripts that debconf is typically used in: the postinst and postrm scripts. Then moves on to more advanced topics like shared debconf templates, debugging, and some common techniques and pitfalls of programming with debconf. It closes with a discussion of debconf&#8217;s current shortcomings.</p>
<h2>The Config Script</h2>
<p>Debconf adds an additional maintainer script, the config script, to the set of maintainer scripts that can be in debian packages (the postinst, preinst, postrm, and prerm). The config script is responsible for asking any questions necessary to configure the package. </p>
<p> Note: It is a little confusing that dpkg refers to running a package&#8217;s postinst script as &quot;configuring&quot; the package, since a package that uses debconf is often fully pre-configured, by its config script, before the postinst ever runs. Oh well. </p>
<p> Like the postinst, the config script is passed two parameters when it is run. The first tells what action is being performed, and the second is the version of the package that is currently installed. So, like in a postinst, you can use dpkg &#8211;compare-versions on $2 to make some behavior happen only on upgrade from a particular version of a package, and things like that. </p>
<p> The config script can be run in one of three ways:</p>
<dl>
<dt><code>1</code></p>
<dd>If a package is pre-configured, with dpkg-preconfigure, its config script is run, and is passed the parameters &quot;configure&quot;, and installed-version.</p>
<dt><code>2</code></p>
<dd>When a package&#8217;s postinst is run, debconf will try to run the config script then too, and it will be passed the same parameters it was passed when it is pre-configured. This is necessary because the package might not have been pre-configured, and the config script still needs to get a chance to run. See HACKS for details.</p>
<dt><code>3</code></p>
<dd>If a package is reconfigured, with dpkg-reconfigure, its config script it run, and is passed the parameters &quot;reconfigure&quot; and installed-version.</dl>
<p> Note that since a typical package install or upgrade using apt runs steps 1 and 2, the config script will typically be run twice. It should do nothing the second time (to ask questions twice in a row is annoying), and it should definitely be idempotent. Luckily, debconf avoids repeating questions by default, so this is generally easy to accomplish. </p>
<p> Note that the config script is run before the package is unpacked. It should only use commands that are in essential packages. The only dependency of your package that is guaranteed to be met when its config script is run is a dependency (possibly versioned) on debconf itself. </p>
<p> The config script should not need to modify the filesystem at all. It just examines the state of the system, and asks questions, and debconf stores the answers to be acted on later by the postinst script. Conversely, the postinst script should almost never use debconf to ask questions, but should instead act on the answers to questions asked by the config script.</p>
<h2>The Templates File</h2>
<p>A package that uses debconf probably wants to ask some questions. These questions are stored, in template form, in the templates file. </p>
<p> Like the config script, the templates file is put in the control.tar.gz section of a deb. Its format is similar to a debian control file; a set of stanzas separated by blank lines, with each stanza having a RFC822-like form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Template: foo/bar<br />
&nbsp;<wbr>&nbsp;<wbr>Type: string<br />
&nbsp;<wbr>&nbsp;<wbr>Default: foo<br />
&nbsp;<wbr>&nbsp;<wbr>Description: This is a sample string question.<br />
This is its extended description.<br />
.<br />
Notice that:<br />
&nbsp;<wbr>&#8211; Like in a debian package description, a dot<br />
on its own line sets off a new paragraph.<br />
&nbsp;<wbr>&#8211; Most text is word-wrapped, but doubly-indented<br />
text is left alone, so you can use it for lists<br />
of items, like this list. Be careful, since<br />
it is not word-wrapped, if it&#8217;s too wide<br />
it will look bad. Using it for short items<br />
is best&nbsp;<wbr>(so this is a bad example). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Template: foo/baz<br />
&nbsp;<wbr>&nbsp;<wbr>Type: boolean<br />
&nbsp;<wbr>&nbsp;<wbr>Description: Clear enough, no?<br />
This is another question, of boolean type. </p>
<p> For some real-life examples of templates files, see /var/lib/dpkg/info/debconf.templates, and other .templates files in that directory. </p>
<p> Let&#8217;s look at each of the fields in turn..</p>
<dl>
<dt><code>Template</code></p>
<dd>The name of the template, in the &#8216;Template&#8217; field, is generally prefixed with the name of the package. After that the namespace is wide open; you can use a simple flat layout like the one above, or set up &quot;subdirectories&quot; containing related questions.</p>
<dt><code>Type</code></p>
<dd>The type of the template determines what kind of widget is displayed to the user. The currently supported types are:</p>
<dl>
<dd>
<dl>
<dt><code>string</code></p>
<dd>Results in a free-form input field that the user can type any string into.</p>
<dt><code>password</code></p>
<dd>Prompts the user for a password. Use this with caution; be aware that the password the user enters will be written to debconf&#8217;s database. You should probably clean that value out of the database as soon as is possible.</p>
<dt><code>boolean</code></p>
<dd>A true/false choice.</p>
<dt><code>select</code></p>
<dd>A choice between one of a number of values. The choices must be specified in a field named &#8216;Choices&#8217;. Separate the possible values with commas and spaces, like this:</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>Choices: yes, no, maybe</dl>
<dt><code>multiselect</code></p>
<dd>Like the select data type, except the user can choose any number of items from the choices list (or choose none of them).</p>
<dt><code>note</code></p>
<dd>Rather than being a question per se, this datatype indicates a note that can be displayed to the user. It should be used only for important notes that the user really should see, since debconf will go to great pains to make sure the user sees it; halting the install for them to press a key. It&#8217;s best to use these only for warning about very serious problems, and the error datatype is often more suitable.</p>
<dt><code>error</code></p>
<dd>This datatype is used for error messages, such as input validation errors. Debconf will show a question of this type even if the priority is too high or the user has already seen it.</p>
<dt><code>title</code></p>
<dd>This datatype is used for titles, to be set with the SETTITLE command.</p>
<dt><code>text</code></p>
<dd>This datatype can be used for fragments of text, such as labels, that can be used for cosmetic reasons in the displays of some frontends. Other frontends will not use it at all. There is no point in using this datatype yet, since no frontends support it well. It may even be removed in the future.</dl>
</dl>
<dt><code>Default</code></p>
<dd>
<dl>
<dd>The &#8216;Default&#8217; field tells debconf what the default value should be. For multiselect, it can be a list of choices, separated by commas and spaces, similar to the &#8216;Choices&#8217; field. For select, it should be one of the choices. For boolean, it is &quot;true&quot; or &quot;false&quot;, while it can be anything for a string, and it is ignored for passwords. </p>
<p> Don&#8217;t make the mistake of thinking that the default field contains the &quot;value&quot; of the question, or that it can be used to change the value of the question. It does not, and cannot, it just provides a default value for the first time the question is displayed. To provide a default that changes on the fly, you&#8217;d have to use the SET command to change the value of a question.</dl>
<dt><code>Description</code></p>
<dd>
<dl>
<dd>The &#8216;Description&#8217; field, like the description of a Debian package, has two parts: A short description and an extended description. Note that some debconf frontends don&#8217;t display the long description, or might only display it if the user asks for help. So the short description should be able to stand on its own. </p>
<p> If you can&#8217;t think up a long description, then first, think some more. Post to debian-devel. Ask for help. Take a writing class! That extended description is important. If after all that you still can&#8217;t come up with anything, leave it blank. There is no point in duplicating the short description. </p>
<p> Text in the extended description will be word-wrapped, unless it is prefixed by additional whitespace (beyond the one required space). You can break it up into separate paragraphs by putting &quot; .&quot; on a line by itself between them.</dl>
</dl>
<h2>Questions</h2>
<p>A question is an instantiated template. By asking debconf to display a question, your config script can interact with the user. When debconf loads a templates file (this happens whenever a config or postinst script is run), it automatically instantiates a question from each template. It is actually possible to instantiate several independent questions from the same template (using the REGISTER command), but that is rarely necessary. Templates are static data that comes from the templates file, while questions are used to store dynamic data, like the current value of the question, whether a user has seen a question, and so on. Keep the distinction between a template and a question in mind, but don&#8217;t worry too much about it.</p>
<h2>Shared Templates</h2>
<p>It&#8217;s actually possible to have a template and a question that are shared among a set of packages. All the packages have to provide an identical copy of the template in their templates files. This can be useful if a bunch of packages need to ask the same question, and you only want to bother the user with it once. Shared templates are generally put in the shared/ pseudo-directory in the debconf template namespace.</p>
<h2>The Debconf Protocol</h2>
<p>Config scripts communicate with debconf using the debconf protocol. This is a simple line-oriented protocol, similar to common internet protocols such as SMTP. The config script sends debconf a command by writing the command to standard output. Then it can read debconf&#8217;s reply from standard input. </p>
<p> Debconf&#8217;s reply can be broken down into two parts: A numeric result code (the first word of the reply), and an optional extended result code (the remainder of the reply). The numeric code uses 0 to indicate success, and other numbers to indicate various kinds of failure. For full details, see the table in Debian policy&#8217;s debconf specification document. </p>
<p> The extended return code is generally free form and unspecified, so you should generally ignore it, and should certainly not try to parse it in a program to work out what debconf is doing. The exception is commands like GET, that cause a value to be returned in the extended return code. </p>
<p> Generally you&#8217;ll want to use a language-specific library that handles the nuts and bolts of setting up these connections to debconf and communicating with it. </p>
<p> For now, here are the commands in the protocol. This is not the definitive definition, see Debian policy&#8217;s debconf specification document for that.</p>
<dl>
<dt><code>VERSION number</code></p>
<dd>You generally don&#8217;t need to use this command. It exchanges with debconf the protocol version number that is being used. The current protocol version is 2.0, and versions in the 2.x series will be backwards-compatible. You may specify the protocol version number you are speaking and debconf will return the version of the protocol it speaks in the extended result code. If the version you specify is too low, debconf will reply with numeric code 30.</p>
<dt><code>CAPB capabilities</code></p>
<dd>
<dl>
<dd>You generally don&#8217;t need to use this command. It exchanges with debconf a list of supported capabilities (separated by spaces). Capabilities that both you and debconf support will be used, and debconf will reply with all the capabilities it supports. </p>
<p> If &#8216;escape&#8217; is found among your capabilities, debconf will expect commands you send it to have backslashes and newlines escaped (as \ and 
 respectively) and will in turn escape backslashes and newlines in its replies. This can be used, for example, to substitute multi-line strings into templates, or to get multi-line extended descriptions reliably using METAGET. In this mode, you must escape input text yourself (you can use <code><a href="/docs/linux/man/1-debconf-escape/">debconf-escape</a></code>(1) to help with this if you want), but the confmodule libraries will unescape replies for you.</dl>
<dt><code>SETTITLE question</code></p>
<dd>
<dl>
<dd>This sets the title debconf displays to the user, using the short description of the template for the specified question. The template should be of type title. You rarely need to use this command since debconf can automatically generate a title based on your package&#8217;s name. </p>
<p> Setting the title from a template means they are stored in the same place as the rest of the debconf questions, and allows them to be translated.</dl>
<dt><code>TITLE string</code></p>
<dd>This sets the title debconf displays to the user to the specified string. Use of the SETTITLE command is normally to be preferred as it allows for translation of the title.</p>
<dt><code>INPUT priority question</code></p>
<dd>
<dl>
<dd>Ask debconf to prepare to display a question to the user. The question is not actually displayed until a GO command is issued; this lets several INPUT commands be given in series, to build up a set of questions, which might all be asked on a single screen. </p>
<p> The priority field tells debconf how important it is that this question be shown to the user. The priority values are:</p>
<dl>
<dt><code>low</code></p>
<dd>Very trivial items that have defaults that will work in the vast majority of cases; only control freaks see these.</p>
<dt><code>medium</code></p>
<dd>Normal items that have reasonable defaults.</p>
<dt><code>high</code></p>
<dd>Items that don&#8217;t have a reasonable default.</p>
<dt><code>critical</code></p>
<dd>Items that will probably break the system without user intervention.</dl>
<p> Debconf decides if the question is actually displayed, based on its priority, and whether the user has seen it before, and which frontend is being used. If the question will not be displayed, debconf replies with code 30.</dl>
<dt><code>GO</code></p>
<dd>
<dl>
<dd>Tells debconf to display the accumulated set of questions (from INPUT commands) to the user. </p>
<p> If the backup capability is supported and the user indicates they want to back up a step, debconf replies with code 30.</dl>
<dt><code>CLEAR</code></p>
<dd>Clears the accumulated set of questions (from INPUT commands) without displaying them.</p>
<dt><code>BEGINBLOCK</code></p>
<dd>
<dt><code>ENDBLOCK</code></p>
<dd>Some debconf frontends can display a number of questions to the user at once. Maybe in the future a frontend will even be able to group these questions into blocks on screen. BEGINBLOCK and ENDBLOCK can be placed around a set of INPUT commands to indicate blocks of questions (and blocks can even be nested). Since no debconf frontend is so sophisticated yet, these commands are ignored for now.</p>
<dt><code>STOP</code></p>
<dd>This command tells debconf that you&#8217;re done talking to it. Often debconf can detect termination of your program and this command is not necessary.</p>
<dt><code>GET question</code></p>
<dd>After using INPUT and GO to display a question, you can use this command to get the value the user entered. The value is returned in the extended result code.</p>
<dt><code>SET question value</code></p>
<dd>This sets the value of a question, and it can be used to override the default value with something your program calculates on the fly.</p>
<dt><code>RESET question</code></p>
<dd>This resets the question to its default value (as is specified in the &#8216;Default&#8217; field of its template).</p>
<dt><code>SUBST question key value</code></p>
<dd>Questions can have substitutions embedded in their &#8216;Description&#8217; and &#8216;Choices&#8217; fields (use of substitutions in &#8216;Choices&#8217; fields is a bit of a hack though; a better mechanism will eventually be developed). These substitutions look like &quot;${key}&quot;. When the question is displayed, the substitutions are replaced with their values. This command can be used to set the value of a substitution. This is useful if you need to display some message to the user that you can&#8217;t hard-code in the templates file.</p>
<dd>Do not try to use SUBST to change the default value of a question; it won&#8217;t work since there is a SET command explicitly for that purpose.</p>
<dt><code>FGET question flag</code></p>
<dd>Questions can have flags associated with them. The flags can have a value of &quot;true&quot; or &quot;false&quot;. This command returns the value of a flag.</p>
<dt><code>FSET question flag value</code></p>
<dd>
<dl>
<dd>This sets the value of a question&#8217;s flag. The value must be either &quot;true&quot; or &quot;false&quot;. </p>
<p> One common flag is the &quot;seen&quot; flag. It is normally only set if a user has already seen a question. Debconf usually only displays questions to users if they have the seen flag set to &quot;false&quot; (or if it is reconfiguring a package). Sometimes you want the user to see a question again &#8212; in these cases you can set the seen flag to false to force debconf to redisplay it.</dl>
<dt><code>METAGET question field</code></p>
<dd>This returns the value of any field of a question&#8217;s associated template (the Description, for example).</p>
<dt><code>REGISTER template question</code></p>
<dd>This creates a new question that is bound to a template. By default each template has an associated question with the same name. However, any number of questions can really be associated with a template, and this lets you create more such questions.</p>
<dt><code>UNREGISTER question</code></p>
<dd>This removes a question from the database.</p>
<dt><code>PURGE</code></p>
<dd>Call this in your postrm when your package is purged. It removes all of your package&#8217;s questions from debconf&#8217;s database.</p>
<dt><code>X_LOADTEMPLATEFILE /path/to/templates [owner]</code></p>
<dd>This extension loads the specified template file into debconf&#8217;s database. The owner defaults to the package that is being configured with debconf.</dl>
<p> Here is a simple example of the debconf protocol in action. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>INPUT medium debconf/frontend<br />
&nbsp;<wbr>&nbsp;<wbr>30 question skipped<br />
&nbsp;<wbr>&nbsp;<wbr>FSET debconf/frontend seen false<br />
&nbsp;<wbr>&nbsp;<wbr>0 false<br />
&nbsp;<wbr>&nbsp;<wbr>INPUT high debconf/frontend<br />
&nbsp;<wbr>&nbsp;<wbr>0 question will be asked<br />
&nbsp;<wbr>&nbsp;<wbr>GO<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>Here debconf displays a question to the user.&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>0 ok<br />
&nbsp;<wbr>&nbsp;<wbr>GET no/such/question<br />
&nbsp;<wbr>&nbsp;<wbr>10 no/such/question doesn&#8217;t exist<br />
&nbsp;<wbr>&nbsp;<wbr>GET debconf/frontend<br />
&nbsp;<wbr>&nbsp;<wbr>0 Dialog</p>
<h2>Libraries</h2>
<p>Setting things up so you can talk to debconf, and speaking the debconf protocol by hand is a little too much work, so some thin libraries exist to relieve this minor drudgery. </p>
<p> For shell programming, there is the /usr/share/debconf/confmodule library, which you can source at the top of a shell script, and talk to debconf in a fairly natural way, using lower-case versions of the debconf protocol commands, that are prefixed with &quot;db_&quot; (ie, &quot;db_input&quot; and &quot;db_go&quot;). For details, see <code><a href="/docs/linux/man/3-confmodule/">confmodule</a></code>(3)<br />
&nbsp;<wbr>. </p>
<p> Perl programmers can use the <code><a href="//www.systutorials.com/docs/linux/man/3pm-Debconf::Client::ConfModule/">Debconf::Client::ConfModule</a></code>(3pm) perl module, and python programmers can use the debconf python module. </p>
<p> The rest of this manual will use the /usr/share/debconf/confmodule library in example shell scripts. Here is an example config script using that library, that just asks a question: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>&nbsp;<wbr>set -e<br />
&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>/usr/share/debconf/confmodule<br />
&nbsp;<wbr>&nbsp;<wbr>db_set mypackage/reboot-now false<br />
&nbsp;<wbr>&nbsp;<wbr>db_input high mypackage/reboot-now || true<br />
&nbsp;<wbr>&nbsp;<wbr>db_go || true </p>
<p> Notice the uses of &quot;|| true&quot; to prevent the script from dying if debconf decides it can&#8217;t display a question, or the user tries to back up. In those situations, debconf returns a non-zero exit code, and since this shell script is set -e, an untrapped exit code would make it abort. </p>
<p> And here is a corresponding postinst script, that uses the user&#8217;s answer to the question to see if the system should be rebooted (a rather absurd example..): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>&nbsp;<wbr>set -e<br />
&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>/usr/share/debconf/confmodule<br />
&nbsp;<wbr>&nbsp;<wbr>db_get mypackage/reboot-now<br />
&nbsp;<wbr>&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>&quot;$RET&quot;&nbsp;<wbr>=&nbsp;<wbr>true&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>shutdown -r now</p>
<p>&nbsp;<wbr>&nbsp;<wbr>fi </p>
<p> Notice the use of the $RET variable to get at the extended return code from the GET command, which holds the user&#8217;s answer to the question.</p>
<h2>The Postinst Script</h2>
<p>The last section had an example of a postinst script that uses debconf to get the value of a question, and act on it. Here are some things to keep in mind when writing postinst scripts that use debconf:</p>
<dl>
<dt><code>*</code></p>
<dd>Avoid asking questions in the postinst. Instead, the config script should ask questions using debconf, so that pre-configuration will work.</p>
<dt><code>*</code></p>
<dd>Always source /usr/share/debconf/confmodule at the top of your postinst, even if you won&#8217;t be running any db_* commands in it. This is required to make sure the config script gets a chance to run (see HACKS for details).</p>
<dt><code>*</code></p>
<dd>Avoid outputting anything to stdout in your postinst, since that can confuse debconf, and postinst should not be verbose anyway. Output to stderr is ok, if you must.</p>
<dt><code>*</code></p>
<dd>If your postinst launches a daemon, make sure you tell debconf to STOP at the end, since debconf can become a little confused about when your postinst is done otherwise.</p>
<dt><code>*</code></p>
<dd>Make your postinst script accept a first parameter of &quot;reconfigure&quot;. It can treat it just like &quot;configure&quot;. This will be used in a later version of debconf to let postinsts know when they are reconfigured.</dl>
<h2>Other Scripts</h2>
<p>Besides the config script and postinst, you can use debconf in any of the other maintainer scripts. Most commonly, you&#8217;ll be using debconf in your postrm, to call the PURGE command when your package is purged, to clean out its entries in the debconf database. (This is automatically set up for you by <code><a href="/docs/linux/man/1-dh_installdebconf/">dh_installdebconf</a></code>(1)<code>,</code> by the way.) </p>
<p> A more involved use of debconf would be if you want to use it in the postrm when your package is purged, to ask a question about deleting something. Or maybe you find you need to use it in the preinst or prerm for some reason. All of these uses will work, though they&#8217;ll probably involve asking questions and acting on the answers in the same program, rather than separating the two activities as is done in the config and postinst scripts. </p>
<p> Note that if your package&#8217;s sole use of debconf is in the postrm, you should make your package&#8217;s postinst source /usr/share/debconf/confmodule, to give debconf a chance to load up your templates file into its database. Then the templates will be available when your package is being purged. </p>
<p> You can also use debconf in other, standalone programs. The issue to watch out for here is that debconf is not intended to be, and must not be used as a registry. This is unix after all, and programs are configured by files in /etc, not by some nebulous debconf database (that is only a cache anyway and might get blown away). So think long and hard before using debconf in a standalone program. </p>
<p> There are times when it can make sense, as in the apt-setup program which uses debconf to prompt the user in a manner consistent with the rest of the debian install process, and immediately acts on their answers to set up apt&#8217;s sources.list.</p>
<h2>Localization</h2>
<p>Debconf supports localization of templates files. This is accomplished by adding more fields, with translated text in them. Any of the fields can be translated. For example, you might want to translate the description into Spanish. Just make a field named &#8216;Description-es&#8217; that holds the translation. If a translated field is not available, debconf falls back to the normal English field. </p>
<p> Besides the &#8216;Description&#8217; field, you should translate the &#8216;Choices&#8217; field of a select or multiselect template. Be sure to list the translated choices in the same order as they appear in the main &#8216;Choices&#8217; field. You do not need to translate the &#8216;Default&#8217; field of a select or multiselect question, and the value of the question will be automatically returned in English. </p>
<p> You will find it easier to manage translations if you keep them in separate files; one file per translation. In the past, the <code><a href="/docs/linux/man/1-debconf-getlang/">debconf-getlang</a></code>(1) and <code><a href="/docs/linux/man/1-debconf-mergetemplate/">debconf-mergetemplate</a></code>(1) programs were used to manage debian/template.ll files. This has been superseded by the <code><a href="/docs/linux/man/7-po-debconf/">po-debconf</a></code>(7) package, which lets you deal with debconf translations in .po files, just like any other translations. Your translators will thank you for using this new improved mechanism. </p>
<p> For the details on po-debconf, see its man page. If you&#8217;re using debhelper, converting to po-debconf is as simple as running the <code><a href="/docs/linux/man/1-debconf-gettextize/">debconf-gettextize</a></code>(1) command once, and adding a Build-Dependency on po-debconf and on debhelper (&gt;= 4.1.13).</p>
<h2>Putting It All Together</h2>
<p>So you have a config script, a templates file, a postinst script that uses debconf, and so on. Putting these pieces together into a debian package isn&#8217;t hard. You can do it by hand, or can use <code><a href="/docs/linux/man/1-dh_installdebconf/">dh_installdebconf</a></code>(1) which will merge your translated templates, copy the files into the right places for you, and can even generate the call to PURGE that should go in your postrm script. Make sure that your package depends on debconf (&gt;= 0.5), since earlier versions were not compatible with everything described in this manual. And you&#8217;re done. </p>
<p> Well, except for testing, debugging, and actually using debconf for more interesting things than asking a few basic questions. For that, read on..</p>
<h2>Debugging</h2>
<p>So you have a package that&#8217;s supposed to use debconf, but it doesn&#8217;t quite work. Maybe debconf is just not asking that question you set up. Or maybe something weirder is happening; it spins forever in some kind of loop, or worse. Luckily, debconf has plenty of debugging facilities.</p>
<dl>
<dt><code>DEBCONF_DEBUG</code></p>
<dd>
<dl>
<dd>The first thing to reach for is the DEBCONF_DEBUG environment variable. If you set and export DEBCONF_DEBUG=developer, debconf will output to stderr a dump of the debconf protocol as your program runs. It&#8217;ll look something like this &#8212; the typo is made clear: </p>
<p>&nbsp;<wbr>debconf&nbsp;<wbr>(developer):&nbsp;<wbr>&lt;&#8211; input high debconf/frontand<br />
&nbsp;<wbr>debconf&nbsp;<wbr>(developer): &#8211;&gt;&nbsp;<wbr>10&nbsp;<wbr>&quot;debconf/frontand&quot;&nbsp;<wbr>doesn&#8217;t exist<br />
&nbsp;<wbr>debconf&nbsp;<wbr>(developer):&nbsp;<wbr>&lt;&#8211; go<br />
&nbsp;<wbr>debconf&nbsp;<wbr>(developer): &#8211;&gt;&nbsp;<wbr>0 ok </p>
<p> It&#8217;s rather useful to use debconf&#8217;s readline frontend when you&#8217;re debugging (in the author&#8217;s opinion), as the questions don&#8217;t get in the way, and all the debugging output is easily preserved and logged.</dl>
<dt><code>DEBCONF_C_VALUES</code></p>
<dd>
<dl>
<dd>If this environment variable is set to &#8216;true&#8217;, the frontend will display the values in Choices-C fields (if present) of select and multiselect templates rather than the descriptive values.</dl>
<dt><code>debconf-communicate</code></p>
<dd>Another useful tool is the <code><a href="/docs/linux/man/1-debconf-communicate/">debconf-communicate</a></code>(1) program. Fire it up and you can speak the raw debconf protocol to debconf, interactively. This is a great way to try stuff out on the fly.</p>
<dt><code>debconf-show</code></p>
<dd>If a user is reporting a problem, <code><a href="/docs/linux/man/1-debconf-show/">debconf-show</a></code>(1) can be used to dump out all the questions owned by your package, displaying their values and whether the user has seen them.</p>
<dt><code>.debconfrc</code></p>
<dd>
<dl>
<dd>To avoid the often tedious build/install/debug cycle, it can be useful to load up your templates with <code><a href="/docs/linux/man/1-debconf-loadtemplate/">debconf-loadtemplate</a></code>(1) and run your config script by hand with the <code><a href="/docs/linux/man/1-debconf/">debconf</a></code>(1) command. However, you still have to do that as root, right? Not so good. And ideally you&#8217;d like to be able to see what a fresh installation of your package looks like, with a clean debconf database. </p>
<p> It turns out that if you set up a ~/.debconfrc file for a normal user, pointing at a personal config.dat and template.dat for the user, you can load up templates and run config scripts all you like, without any root access. If you want to start over with a clean database, just blow away the *.dat files. </p>
<p> For details about setting this up, see <code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5)<code>,</code> and note that /etc/debconf.conf makes a good template for a personal ~/.debconfrc file.</dl>
</dl>
<h2>Advanced Programming With Debconf</h2>
<h3>Config file handling</h3>
<p>Many of you seem to want to use debconf to help manage config files that are part of your package. Perhaps there is no good default to ship in a conffile, and so you want to use debconf to prompt the user, and write out a config file based on their answers. That seems easy enough to do, but then you consider upgrades, and what to do when someone modifies the config file you generate, and dpkg-reconfigure, and &#8230; </p>
<p> There are a lot of ways to do this, and most of them are wrong, and will often earn you annoyed bug reports. Here is one right way to do it. It assumes that your config file is really just a series of shell variables being set, with comments in between, and so you can just source the file to &quot;load&quot; it. If you have a more complicated format, reading (and writing) it becomes a bit trickier. </p>
<p> Your config script will look something like this: </p>
<p>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>CONFIGFILE=/etc/foo.conf<br />
&nbsp;<wbr>set -e<br />
&nbsp;<wbr>.&nbsp;<wbr>/usr/share/debconf/confmodule </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Load config file, if it exists.<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-e&nbsp;<wbr>$CONFIGFILE&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>.&nbsp;<wbr>$CONFIGFILE || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>Store values from config file into</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>debconf db.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_set mypackage/foo&nbsp;<wbr>&quot;$FOO&quot;</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_set mypackage/bar&nbsp;<wbr>&quot;$BAR&quot;</p>
<p>&nbsp;<wbr>fi </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Ask questions.<br />
&nbsp;<wbr>db_input medium mypackage/foo || true<br />
&nbsp;<wbr>db_input medium mypackage/bar || true<br />
&nbsp;<wbr>db_go || true </p>
<p> And the postinst will look something like this: </p>
<p>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>CONFIGFILE=/etc/foo.conf<br />
&nbsp;<wbr>set -e<br />
&nbsp;<wbr>.&nbsp;<wbr>/usr/share/debconf/confmodule<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>Generate config file, if it doesn&#8217;t exist.<br />
&nbsp;<wbr>#&nbsp;<wbr>An alternative is to copy in a template<br />
&nbsp;<wbr>#&nbsp;<wbr>file from elsewhere.<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>!&nbsp;<wbr>-e&nbsp;<wbr>$CONFIGFILE&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>echo&nbsp;<wbr>&quot;#&nbsp;<wbr>Config file for my package&quot;&nbsp;<wbr>&gt;&nbsp;<wbr>$CONFIGFILE</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>echo&nbsp;<wbr>&quot;FOO=&quot;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$CONFIGFILE</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>echo&nbsp;<wbr>&quot;BAR=&quot;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$CONFIGFILE</p>
<p>&nbsp;<wbr>fi </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Substitute in the values from the debconf db.<br />
&nbsp;<wbr>#&nbsp;<wbr>There are obvious optimizations possible here.<br />
&nbsp;<wbr>#&nbsp;<wbr>The cp before the sed ensures we do not mess up<br />
&nbsp;<wbr>#&nbsp;<wbr>the config file&#8217;s ownership and permissions.<br />
&nbsp;<wbr>db_get mypackage/foo<br />
&nbsp;<wbr>FOO=&quot;$RET&quot;<br />
&nbsp;<wbr>db_get mypackage/bar<br />
&nbsp;<wbr>BAR=&quot;$RET&quot;<br />
&nbsp;<wbr>cp -a -f&nbsp;<wbr>$CONFIGFILE&nbsp;<wbr>$CONFIGFILE.tmp </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>If the admin deleted or commented some variables but then set<br />
&nbsp;<wbr>#&nbsp;<wbr>them via debconf,&nbsp;<wbr>(re-)add them to the conffile.<br />
&nbsp;<wbr>test -z&nbsp;<wbr>&quot;$FOO&quot;&nbsp;<wbr>|| grep -Eq&nbsp;<wbr>&#8216;^&nbsp;<wbr>*FOO=&#8217;&nbsp;<wbr>$CONFIGFILE ||&nbsp;<wbr>\<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>echo&nbsp;<wbr>&quot;FOO=&quot;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$CONFIGFILE</p>
<p>&nbsp;<wbr>test -z&nbsp;<wbr>&quot;$BAR&quot;&nbsp;<wbr>|| grep -Eq&nbsp;<wbr>&#8216;^&nbsp;<wbr>*BAR=&#8217;&nbsp;<wbr>$CONFIGFILE ||&nbsp;<wbr>\<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>echo&nbsp;<wbr>&quot;BAR=&quot;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>$CONFIGFILE</p>
<p>&nbsp;<wbr>sed -e&nbsp;<wbr>&quot;s/^&nbsp;<wbr>*FOO=.*/FOO=\&quot;$FOO\&quot;/&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-e&nbsp;<wbr>&quot;s/^&nbsp;<wbr>*BAR=.*/BAR=\&quot;$BAR\&quot;/&quot;&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;&nbsp;<wbr>$CONFIGFILE&nbsp;<wbr>&gt;&nbsp;<wbr>$CONFIGFILE.tmp<br />
&nbsp;<wbr>mv -f&nbsp;<wbr>$CONFIGFILE.tmp&nbsp;<wbr>$CONFIGFILE </p>
<p> Consider how these two scripts handle all the cases. On fresh installs the questions are asked by the config script, and a new config file generated by the postinst. On upgrades and reconfigures, the config file is read in, and the values in it are used to change the values in the debconf database, so the admin&#8217;s manual changes are not lost. The questions are asked again (and may or may not be displayed). Then the postinst substitutes the values back into the config file, leaving the rest of it unchanged.</p>
<h3>Letting the user back up</h3>
<p>Few things are more frustrating when using a system like debconf than being asked a question, and answering it, then moving on to another screen with a new question on it, and realizing that hey, you made a mistake, with that last question, and you want to go back to it, and discovering that you can&#8217;t. </p>
<p> Since debconf is driven by your config script, it can&#8217;t jump back to a previous question on its own but with a little help from you, it can accomplish this feat. The first step is to make your config script let debconf know it is capable of handling the user pressing a back button. You use the CAPB command to do this, passing backup as a parameter. </p>
<p> Then after each GO command, you must test to see if the user asked to back up (debconf returns a code of 30), and if so jump back to the previous question. </p>
<p> There are several ways to write the control structures of your program so it can jump back to previous questions when necessary. You can write goto-laden spaghetti code. Or you can create several functions and use recursion. But perhaps the cleanest and easiest way is to construct a state machine. Here is a skeleton of a state machine that you can fill out and expand. </p>
<p>&nbsp;<wbr>#!/bin/sh<br />
&nbsp;<wbr>set -e<br />
&nbsp;<wbr>.&nbsp;<wbr>/usr/share/debconf/confmodule<br />
&nbsp;<wbr>db_capb backup<br />
&nbsp;<wbr><br />
&nbsp;<wbr>STATE=1<br />
&nbsp;<wbr>while true;&nbsp;<wbr>do<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>case&nbsp;<wbr>&quot;$STATE&quot;&nbsp;<wbr>in</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1)</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>Two unrelated questions.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_input medium my/question || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_input medium my/other_question || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>;;</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2)</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>Only ask this question if the</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>first question was answered in</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>the affirmative.</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_get my/question</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if&nbsp;<wbr>[&nbsp;<wbr>&quot;$RET&quot;&nbsp;<wbr>=&nbsp;<wbr>&quot;true&quot;&nbsp;<wbr>];&nbsp;<wbr>then</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_input medium my/dep_question || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fi</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>;;</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*)</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>The default case catches when&nbsp;<wbr>$STATE is greater than the</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>last implemented state, and breaks out of the loop. This</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>requires that states be numbered consecutively from 1</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>with no gaps, as the default case will also be entered</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>if there is a break in the numbering</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>break&nbsp;<wbr>#&nbsp;<wbr>exits the enclosing&nbsp;<wbr>&quot;while&quot;&nbsp;<wbr>loop</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>;;</p>
<p>&nbsp;<wbr>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>esac</p>
<p>&nbsp;<wbr><br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if db_go;&nbsp;<wbr>then</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>STATE=$(($STATE&nbsp;<wbr>+&nbsp;<wbr>1))</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>else</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>STATE=$(($STATE &#8211; 1))</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fi</p>
<p>&nbsp;<wbr>done </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>$STATE -eq 0&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>The user has asked to back up from the first</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>question. This case is problematical. Regular</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>dpkg and apt package installation isn&#8217;t capable</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>of backing up questions between packages as this</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>is written, so this will exit leaving the package</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>unconfigured &#8211; probably the best way to handle</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>the situation.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>exit 10</p>
<p>&nbsp;<wbr>fi </p>
<p> Note that if all your config script does is ask a few unrelated questions, then there is no need for the state machine. Just ask them all, and GO; debconf will do its best to present them all in one screen, and the user won&#8217;t need to back up.</p>
<h3>Preventing infinite loops</h3>
<p>One gotcha with debconf comes up if you have a loop in your config script. Suppose you&#8217;re asking for input and validating it, and looping if it&#8217;s not valid: </p>
<p>&nbsp;<wbr>ok=&#8221;<br />
&nbsp;<wbr>do while&nbsp;<wbr>[&nbsp;<wbr>!&nbsp;<wbr>&quot;$ok&quot;&nbsp;<wbr>];<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_input low foo/bar || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_go || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_get foo/bar</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if&nbsp;<wbr>[&nbsp;<wbr>&quot;$RET&quot;&nbsp;<wbr>];&nbsp;<wbr>then</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ok=1</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fi</p>
<p>&nbsp;<wbr>done </p>
<p> This looks ok at first glance. But consider what happens if the value of foo/bar is &quot;&quot; when this loop is entered, and the user has their priority set high, or is using a non-interactive frontend, and so they are not really asked for input. The value of foo/bar is not changed by the db_input, and so it fails the test and loops. And loops &#8230; </p>
<p> One fix for this is to make sure that before the loop is entered, the value of foo/bar is set to something that will pass the test in the loop. So for example if the default value of foo/bar is &quot;1&quot;, then you could RESET foo/bar just before entering the loop. </p>
<p> Another fix is to check the return code of the INPUT command. If it is 30 then the user is not being shown the question you asked them, and you should break out of the loop.</p>
<h3>Choosing among related packages</h3>
<p>Sometimes a set of related packages can be installed, and you want to prompt the user which of the set should be used by default. Examples of such sets are window managers, or ispell dictionary files. </p>
<p> While it would be possible for each package in the set to simply prompt, &quot;Should this package be default?&quot;, this leads to a lot of repetitive questions if several of the packages are installed. It&#8217;s possible with debconf to present a list of all the packages in the set and allow the user to choose between them. Here&#8217;s how. </p>
<p> Make all the packages in the set use a shared template. Something like this: </p>
<p>&nbsp;<wbr>Template: shared/window-manager<br />
&nbsp;<wbr>Type: select<br />
&nbsp;<wbr>Choices:&nbsp;<wbr>${choices}<br />
&nbsp;<wbr>Description: Select the default window manager.<br />
&nbsp;<wbr>&nbsp;<wbr>Select the window manager that will be started by<br />
&nbsp;<wbr>&nbsp;<wbr>default when X starts. </p>
<p> Each package should include a copy of the template. Then it should include some code like this in its config script: </p>
<p>&nbsp;<wbr>db_metaget shared/window-manager owners<br />
&nbsp;<wbr>OWNERS=$RET<br />
&nbsp;<wbr>db_metaget shared/window-manager choices<br />
&nbsp;<wbr>CHOICES=$RET<br />
&nbsp;<wbr><br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>&quot;$OWNERS&quot;&nbsp;<wbr>!=&nbsp;<wbr>&quot;$CHOICES&quot;&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_subst shared/window-manager choices&nbsp;<wbr>$OWNERS</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_fset shared/window-manager seen false</p>
<p>&nbsp;<wbr>fi<br />
&nbsp;<wbr><br />
&nbsp;<wbr>db_input medium shared/window-manager || true<br />
&nbsp;<wbr>db_go || true </p>
<p> A bit of an explanation is called for. By the time your config script runs, debconf has already read in all the templates for the packages that are being installed. Since the set of packages share a question, debconf records that fact in the owners field. By a strange coincidence, the format of the owners field is the same as that of the choices field (a comma and space delimited list of values). </p>
<p> The METAGET command can be used to get the list of owners and the list of choices. If they are different, then a new package has been installed. So use the SUBST command to change the list of choices to be the same as the list of owners, and ask the question. </p>
<p> When a package is removed, you probably want to see if that package is the currently selected choice, and if so, prompt the user to select a different package to replace it. </p>
<p> This can be accomplished by adding something like this to the prerm scripts of all related packages (replacing &lt;package&gt; with the package name): </p>
<p>&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-e&nbsp;<wbr>/usr/share/debconf/confmodule&nbsp;<wbr>];&nbsp;<wbr>then<br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>.&nbsp;<wbr>/usr/share/debconf/confmodule</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>I no longer claim this question.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_unregister shared/window-manager</p>
<p>&nbsp;<wbr><br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>See if the shared question still exists.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if db_get shared/window-manager;&nbsp;<wbr>then</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_metaget shared/window-manager owners</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_subst shared/window-manager choices&nbsp;<wbr>$RET</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_metaget shared/window-manager value</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if&nbsp;<wbr>[&nbsp;<wbr>&quot;&lt;package&gt;&quot;&nbsp;<wbr>=&nbsp;<wbr>&quot;$RET&quot;&nbsp;<wbr>]&nbsp;<wbr>;&nbsp;<wbr>then</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_fset shared/window-manager seen false</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_input high shared/window-manager || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>db_go || true</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fi</p>
<p>&nbsp;<wbr><br />
&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>Now do whatever the postinst script did</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>#&nbsp;<wbr>to update the window manager symlink.</p>
<p>&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fi</p>
<p>&nbsp;<wbr>fi</p>
<h2>Hacks</h2>
<p>Debconf is currently not fully integrated into dpkg (but I want to change this in the future), and so some messy hacks are currently called for. </p>
<p> The worst of these involves getting the config script to run. The way that works now is the config script will be run when the package is pre-configured. Then, when the postinst script runs, it starts up debconf again. Debconf notices it is being used by the postinst script, and so it goes off and runs the config script. This can only work if your postinst loads up one of the debconf libraries though, so postinsts always have to take care to do that. We hope to address this later by adding explicit support to dpkg for debconf. The <code><a href="/docs/linux/man/1-debconf/">debconf</a></code>(1) program is a step in this direction. </p>
<p> A related hack is getting debconf running when a config script, postinst, or other program that uses it starts up. After all, they expect to be able to talk to debconf right away. The way this is accomplished for now is that when such a script loads a debconf library (like /usr/share/debconf/confmodule), and debconf is not already running, it is started up, and a new copy of the script is re-execed. The only noticeable result is that you need to put the line that loads a debconf library at the very top of the script, or weird things will happen. We hope to address this later by changing how debconf is invoked, and turning it into something more like a transient daemon. </p>
<p> It&#8217;s rather hackish how debconf figures out what templates files to load, and when it loads them. When the config, preinst, and postinst scripts invoke debconf, it will automatically figure out where the templates file is, and load it. Standalone programs that use debconf will cause debconf to look for templates files in /usr/share/debconf/templates/progname.templates. And if a postrm wants to use debconf at purge time, the templates won&#8217;t be available unless debconf had a chance to load them in its postinst. This is messy, but rather unavoidable. In the future some of these programs may be able to use debconf-loadtemplate by hand though. </p>
<p> /usr/share/debconf/confmodule&#8217;s historic behavior of playing with file descriptors and setting up a fd #3 that talks to debconf, can cause all sorts of trouble when a postinst runs a daemon, since the daemon ends up talking to debconf, and debconf can&#8217;t figure out when the script terminates. The STOP command can work around this. In the future, we are considering making debconf communication happen over a socket or some other mechanism than stdio. </p>
<p> Debconf sets DEBCONF_RECONFIGURE=1 before running postinst scripts, so a postinst script that needs to avoid some expensive operation when reconfigured can look at that variable. This is a hack because the right thing would be to pass $1 = &quot;reconfigure&quot;, but doing so without breaking all the postinsts that use debconf is difficult. The migration plan away from this hack is to encourage people to write postinsts that accept &quot;reconfigure&quot;, and once they all do, begin passing that parameter.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7) is the debconf user&#8217;s guide. </p>
<p> The debconf specification in debian policy is the canonical definition of the debconf protocol. /usr/share/doc/debian-policy/debconf_specification.txt.gz </p>
<p> <code><a href="/docs/linux/man/5-debconf-conf/">debconf.conf</a></code>(5) has much useful information, including some info about the backend database.</p>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
